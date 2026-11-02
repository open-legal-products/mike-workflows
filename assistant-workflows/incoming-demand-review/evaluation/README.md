# Synthetic incoming-demand evaluation fixtures

Author: Lawyered. Contribution license: MIT; see LICENSE. The repository's upstream MIT license remains unchanged.

This bundle contains four fictional, four-document evidence-review cases. PH27 is the original baseline fixture and its substantive frozen scorecard. Nightjar and Alder are development/regression cases for the current candidate. Tideglass was independently authored after the current candidate was frozen, without inspecting candidate outputs. Its trial does not support retuning the candidate on the case. Canonical source text, requests and substantive review checks are preserved. No actual client documents, model outputs, application captures, account information or provider integrations are included.

The bundle provides evaluation material and fixture verification. Its integrity checks do not run or score a model, establish workflow effectiveness or verify action isolation. Public fixtures and answer keys become known examples; future use cannot alone establish performance on unseen cases.

## Contents and upload boundary

- `inputs/ph27/source-packet.json`, `inputs/nightjar/canonical.json`, `inputs/alder/canonical.json`, and `inputs/tideglass/canonical.json` contain the source documents.
- Each adjacent `request.txt` is the neutral request for that case. Every request says: “Use only these four documents.”
- `review-only/` contains expected findings or scoring guidance. Review the complete output against these checks, record exact output evidence and source support, and leave unassessed items unassessed.
- `fixtures-manifest.json` freezes the exact bundled file set, lengths and SHA-256 hashes. It is an integrity record, not a signed provenance claim. Deliberate replacement of both a fixture and its manifest requires external review.

For a model run, upload **only the four generated DOCX files for one case**, then supply that case's `request.txt` as the user prompt. Alternatively, provide only that case's canonical JSON as a serialization of the same four documents, plus its request. Choose one representation. Do not upload answer keys, README, manifests, license, script, other cases or generated-manifest.json. Keep review-only material out of the generating model's context.

The PH27 JSON stores text in ordered `parts`; its canonical document text is those `text` values joined by one LF. Its part-location labels remain available for later source checking. The other three JSON fixtures store each document's exact `text` directly. DOCX paragraphs preserve these newline boundaries. No headings, labels or answer text are added to the generated source text.

## Run locally

Requires Python 3.8 or later; standard library only. Run from this directory:

```sh
python3 fixtures.py verify
python3 fixtures.py test
demand_fixture_out="$(mktemp -d)"
python3 fixtures.py generate --output "$demand_fixture_out"
```

Generation requires an empty output directory outside this evaluation bundle. It writes one folder per case, each with four DOCX documents and the unchanged request, plus a generated manifest with binary and canonical-text hashes. Output paths, current time, platform identity and absolute local paths are not embedded. ZIP entry order, metadata, timestamps and uncompressed content are fixed; no binary outputs need to be committed.

The eight regression checks cover intact fixtures; rejection of changed source, changed expected hash, a missing fixture, an unexpected file and unsafe manifest paths; exact canonical DOCX text for all 16 documents; and byte-identical repeat generation. These are file-integrity and serialization checks, not model-behavior or legal-accuracy tests.

For an actual model comparison, keep the request and source representation fixed, record the tested candidate version and relevant execution settings separately, and have a reviewer apply the case's checks to the actual output and retrievable evidence. Do not infer a score from matching keywords or formatting. Any external action compliance requires its own complete trace or enforced control; prose alone cannot establish it.

## Exact contribution allowlist

Only these files belong to this evaluation contribution:

```text
LICENSE
README.md
fixtures.py
fixtures-manifest.json
inputs/alder/canonical.json
inputs/alder/request.txt
inputs/nightjar/canonical.json
inputs/nightjar/request.txt
inputs/ph27/source-packet.json
inputs/ph27/request.txt
inputs/tideglass/canonical.json
inputs/tideglass/request.txt
review-only/alder-checks.json
review-only/nightjar-checks.json
review-only/ph27-scorecard.json
review-only/tideglass-checks.json
```
