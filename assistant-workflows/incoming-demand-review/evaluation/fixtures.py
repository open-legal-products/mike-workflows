#!/usr/bin/env python3
"""Verify frozen fictional fixtures and produce deterministic DOCX model inputs.

Python standard library only. Fixture checks do not evaluate model behavior.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import unittest
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape
import zipfile

ROOT = Path(__file__).resolve().parent
MANIFEST = 'fixtures-manifest.json'
CASES = {
    'ph27': 'inputs/ph27/source-packet.json',
    'nightjar': 'inputs/nightjar/canonical.json',
    'alder': 'inputs/alder/canonical.json',
    'tideglass': 'inputs/tideglass/canonical.json',
}
W = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def verify(root):
    """Check the exact bundled file set, lengths and SHA-256 integrity."""
    manifest = json.loads((root / MANIFEST).read_text(encoding='utf-8'))
    if manifest.get('algorithm') != 'SHA-256':
        raise ValueError('unsupported manifest algorithm')
    entries = manifest['files']
    paths = [entry['path'] for entry in entries]
    if len(set(paths)) != len(paths):
        raise ValueError('duplicate manifest path')
    for name in paths:
        p = PurePosixPath(name)
        if p.is_absolute() or '..' in p.parts or str(p) != name or name == MANIFEST:
            raise ValueError('unsafe manifest path')
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    expected = set(paths) | {MANIFEST}
    if actual != expected:
        raise ValueError('fixture file set mismatch; missing=' + repr(sorted(expected - actual))
                         + '; unexpected=' + repr(sorted(actual - expected)))
    for entry in entries:
        path = root / entry['path']
        components = PurePosixPath(entry['path']).parts
        if any(root.joinpath(*components[:i]).is_symlink() for i in range(1, len(components) + 1)):
            raise ValueError('symlink fixture path')
        data = path.read_bytes()
        if len(data) != entry['bytes'] or sha256(data) != entry['sha256']:
            raise ValueError('fixture integrity mismatch: ' + entry['path'])
    for case, name in CASES.items():
        docs = load_documents(root / name)
        if len(docs) != 4 or len({name for name, text in docs}) != 4:
            raise ValueError('expected four distinct documents: ' + case)
        if not (root / 'inputs' / case / 'request.txt').read_text(encoding='utf-8').strip():
            raise ValueError('empty request: ' + case)
    return len(entries)


def load_documents(path):
    """Return exact document text; PH27 parts are paragraphs joined by LF."""
    data = json.loads(path.read_text(encoding='utf-8'))
    result = []
    for doc in data['documents']:
        name = doc.get('file', doc['id'] + '.docx')
        if PurePosixPath(name).name != name or not name.endswith('.docx'):
            raise ValueError('invalid document filename')
        text = doc['text'] if 'text' in doc else '\n'.join(p['text'] for p in doc['parts'])
        if not isinstance(text, str) or not text:
            raise ValueError('empty document')
        result.append((name, text))
    return result


def write_docx(path, text):
    """Minimal OPC package; fixed metadata and stored ZIP ensure reproducibility."""
    paragraphs = ''.join('<w:p><w:r><w:t xml:space="preserve">' + escape(p)
                         + '</w:t></w:r></w:p>' for p in text.split('\n'))
    parts = {
        '[Content_Types].xml': '<?xml version="1.0" encoding="UTF-8"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>',
        '_rels/.rels': '<?xml version="1.0" encoding="UTF-8"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>',
        'word/document.xml': '<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="' + W + '"><w:body>' + paragraphs + '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1080" w:right="1080" w:bottom="1080" w:left="1080"/></w:sectPr></w:body></w:document>',
    }
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_STORED) as package:
        for name, content in parts.items():
            info = zipfile.ZipInfo(name, (2000, 1, 1, 0, 0, 0))
            info.create_system = 0
            info.external_attr = 0x20
            package.writestr(info, content.encode('utf-8'))
    if read_docx(path) != text:
        raise ValueError('DOCX text differs from canonical source')


def read_docx(path):
    with zipfile.ZipFile(path) as package:
        if package.testzip() is not None:
            raise ValueError('DOCX ZIP integrity failure')
        for name in package.namelist():
            ET.fromstring(package.read(name))
        document = ET.fromstring(package.read('word/document.xml'))
    return '\n'.join(''.join(p.itertext()) for p in document.findall('.//w:body/w:p', {'w': W}))


def generate(root, output):
    verify(root)
    output = output.resolve()
    if output == root.resolve() or root.resolve() in output.parents:
        raise ValueError('output must be outside the evaluation bundle')
    if output.exists() and any(output.iterdir()):
        raise ValueError('output directory must be empty')
    output.mkdir(parents=True, exist_ok=True)
    records = []
    for case, name in CASES.items():
        folder = output / case
        folder.mkdir()
        for filename, text in load_documents(root / name):
            target = folder / filename
            write_docx(target, text)
            records.append({'path': target.relative_to(output).as_posix(),
                            'source': name, 'canonical_text_sha256': sha256(text.encode('utf-8')),
                            'bytes': target.stat().st_size, 'sha256': sha256(target.read_bytes())})
        request = folder / 'request.txt'
        shutil.copyfile(root / 'inputs' / case / 'request.txt', request)
        records.append({'path': request.relative_to(output).as_posix(),
                        'bytes': request.stat().st_size, 'sha256': sha256(request.read_bytes())})
    generated = {'algorithm': 'SHA-256', 'author': 'Lawyered', 'files': records}
    (output / 'generated-manifest.json').write_text(json.dumps(generated, indent=2) + '\n', encoding='utf-8')
    return generated


class FixtureRegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.work = Path(self.temp.name)
        self.bundle = self.work / 'bundle'
        shutil.copytree(ROOT, self.bundle)

    def test_intact_bundle(self):
        self.assertGreater(verify(self.bundle), 0)

    def test_changed_source_rejected(self):
        target = self.bundle / CASES['ph27']
        data = json.loads(target.read_text(encoding='utf-8'))
        data['documents'][0]['parts'][1]['text'] += ' Changed.'
        target.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'fixture integrity mismatch'):
            verify(self.bundle)

    def test_changed_hash_rejected(self):
        target = self.bundle / MANIFEST
        data = json.loads(target.read_text(encoding='utf-8'))
        data['files'][0]['sha256'] = '0' * 64
        target.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'fixture integrity mismatch'):
            verify(self.bundle)

    def test_missing_fixture_rejected(self):
        (self.bundle / CASES['alder']).unlink()
        with self.assertRaisesRegex(ValueError, 'fixture file set mismatch; missing='):
            verify(self.bundle)

    def test_unlisted_file_rejected(self):
        (self.bundle / 'unexpected.txt').write_text('unlisted', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'unexpected='):
            verify(self.bundle)

    def test_unsafe_manifest_path_rejected(self):
        target = self.bundle / MANIFEST
        data = json.loads(target.read_text(encoding='utf-8'))
        data['files'][0]['path'] = '../outside.json'
        target.write_text(json.dumps(data), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'unsafe manifest path'):
            verify(self.bundle)

    def test_exact_docx_text_for_all_documents(self):
        generate(self.bundle, self.work / 'generated')
        for case, name in CASES.items():
            for filename, text in load_documents(self.bundle / name):
                self.assertEqual(read_docx(self.work / 'generated' / case / filename), text)

    def test_deterministic_outputs(self):
        first, second = self.work / 'first', self.work / 'second'
        generate(self.bundle, first)
        generate(self.bundle, second)
        first_files = sorted(p.relative_to(first) for p in first.rglob('*') if p.is_file())
        second_files = sorted(p.relative_to(second) for p in second.rglob('*') if p.is_file())
        self.assertEqual(first_files, second_files)
        for path in first_files:
            self.assertEqual((first / path).read_bytes(), (second / path).read_bytes(), str(path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['verify', 'generate', 'test'])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.command == 'verify':
        print('Verified ' + str(verify(ROOT)) + ' frozen files. No model evaluation performed.')
    elif args.command == 'generate':
        if args.output is None:
            parser.error('generate requires --output outside the evaluation bundle')
        result = generate(ROOT, args.output)
        count = sum(item['path'].endswith('.docx') for item in result['files'])
        print('Generated ' + str(count) + ' text-verified DOCX inputs, '
              + str(len(CASES)) + ' requests and one deterministic manifest.')
    else:
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(FixtureRegressionTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()
