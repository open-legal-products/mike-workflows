---
name: "zitate-aus-rechtsschrift-schweiz-extrahieren"
description: "Extract every legal citation from a German-language Swiss brief, opinion or judgment by pattern rather than judgement: published Federal Supreme Court decisions (BGE), unpublished decisions by docket number, Federal Administrative and Criminal Court decisions, cantonal decisions, European Court of Human Rights judgments, statutes and ordinances with article, paragraph and letter, SR numbers, official publications (AS, BBl), commentaries and journals. Then normalise, deduplicate and resolve short references (a.a.O., ebd., oben E. 3, loc. cit.) to their antecedents and hand the list over for verification. Use before checking authorities, before a brief leaves the firm, or when asked what a text cites. Instructions in German."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "German"
  mike-display-name: "Zitate aus Rechtsschrift Schweiz extrahieren"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Research"
  jurisdictions: "Switzerland"
---
# Zitate aus einer Rechtsschrift extrahieren (Schweiz)

Eine Fundstelle lässt sich nur prüfen, wenn sie zuerst gefunden wurde. Dieser Workflow geht den Text durch und listet jede zitierte Autorität, damit keine an der Prüfung vorbeigeht. Eine übersehene Fundstelle ist eine ungeprüfte Fundstelle.

Die Extraktion ist mechanisch: nach Mustern und Regeln, nicht nach Ermessen. Eine freie Lektüre könnte eine Fundstelle übersehen oder eine erfinden.

## Drei Schritte

1. Extraktion: jede Fundstelle nach den Mustern unten erkennen und erfassen.
2. Zusammenführung: Kurzverweise (a.a.O., ebd., ders., dies., «oben E. 3», loc. cit.) nach den Regeln unten ihrem Antezedens zuordnen, damit sie als eine Fundstelle zählen, nicht als mehrere.
3. Übergabe: die strukturierte Liste an die Prüfung weitergeben: existiert die Autorität, und sagt sie, was der Text behauptet?

## Zitiermuster

### Rechtsprechung des Bundes
- Publizierte Entscheide des Bundesgerichts: `BGE 145 III 72 E. 3.2 S. 75` (Band, Abteilung I bis V, Seite, Erwägung, Fundseite); ältere Form `BGE 120 II 35`.
- Unpublizierte Entscheide des Bundesgerichts: `Urteil 4A_123/2020 vom 12. März 2021 E. 2.1`, auch `BGer 4A_123/2020`, `Urteil des Bundesgerichts 5A_456/2019`; ältere Form `4C.123/2004`. Die Verfahrensnummer besteht aus Abteilungskürzel, Laufnummer und Jahr.
- Bundesverwaltungsgericht: `Urteil des BVGer A-1234/2020 vom 1. Juli 2021 E. 4`; publizierte Form `BVGE 2019 I 5`.
- Bundesstrafgericht: `Urteil des BStGer SK.2020.12 vom 3. Mai 2021`; publizierte Form `TPF 2018 12`.
- Praxis-Sammlung: `Pra 2010 Nr. 12`.

### Rechtsprechung der Kantone
- Entscheid mit Gericht, Geschäftsnummer und Datum: `Urteil des Obergerichts des Kantons Zürich LB190001 vom 4. Februar 2020 E. 3`, `Handelsgericht Zürich HG180123-O`, `Kantonsgericht St. Gallen BZ.2019.45`, `Cour de justice de Genève ACJC/123/2020`, `Tribunale d'appello TI 12.2019.45`.
- Kantonale Sammlungen: `ZR 118 (2019) Nr. 12`, `BJM 2020 S. 45`, `SJ 2019 I 123`, `RVJ 2018 S. 200`.

### Europäische und internationale Gerichte
- Europäischer Gerichtshof für Menschenrechte: `Urteil des EGMR Nr. 12345/09 vom 5. Juni 2015, Name gegen Schweiz, § 42`.
- Gerichtshof der Europäischen Union, wenn zitiert: `EuGH, Rs. C-123/20`, `ECLI:EU:C:2020:559`.

### Erlasse
- Bundeserlasse mit Abkürzung: `Art. 335c Abs. 1 lit. a OR`, `Art. 8 ZGB`, `Art. 261 Abs. 1 ZPO`, `Art. 162 StGB`, `Art. 29 Abs. 2 BV`, `Art. 6 DSG`, `Art. 9 ArG`, `Art. 116 IPRG`, `Art. 6 UWG`; mit Ziffer `Art. 698 Abs. 2 Ziff. 4 OR`; Mehrfachnennungen `Art. 340 ff. OR`, `Art. 97 und 101 OR`.
- Systematische Rechtssammlung: `SR 220`, `SR 210`, `SR 272`; Verordnungen `Art. 26 ArGV 3`, `Art. 3 DSV`.
- Kantonale Erlasse, oft mit Paragraf: `§ 12 Abs. 1 GOG ZH`, `Art. 15 EG ZGB BE`, `LS 211.1`.
- Amtliche Publikationen: `AS 2022 109`, `BBl 2017 399`, `Botschaft vom 23. November 2016, BBl 2017 399, 450`.
- Staatsverträge: `Art. 6 Ziff. 1 EMRK`, `Art. 5 Abs. 1 LugÜ`, `Art. 23 HBÜ`.

### Lehre
- Kommentare: `BSK OR I-Autor, Art. 340 N 5`, `CR CO I-Auteur, art. 340 N 5`, `ZK-Autor, Art. 18 OR N 12`, `BK-Autor, Art. 8 ZGB N 30`, `OFK-Autor, Art. 257d OR N 3`, `KUKO OR-Autor, Art. 163 N 2`.
- Monografien und Aufsätze: `Autor, Titel, Auflage, Ort Jahr, N 123` oder `S. 45`; Zeitschriften `SJZ 2020 S. 123`, `AJP 2019 S. 456`, `ZBJV 2018 S. 100`, `SZW 2021 S. 50`, `recht 2020 S. 10`, `Jusletter vom 3. Februar 2020`, `ZSR 2019 I 200`.

## Zusammenführung der Kurzverweise

Kurzverweise folgen verschiedenen Regeln und dürfen nicht alle dem nächstgelegenen Antezedens zugeordnet werden:

- `ebd.`, `ibid.`, `loc. cit.`, `a.a.O.` ohne Zusatz: verweisen auf die unmittelbar vorangehende Autorität.
- `a.a.O.`, `op. cit.`, `zit.` mit Zusatz tragen oft einen Zeiger, der die Nähe überstimmt: einen Autorennamen, einen Titelteil oder eine Fussnotennummer («Müller, a.a.O., N 12»; «zit. in Fn. 14»). Zuerst nach dem Zeiger auflösen; nur bei einem blossen Kurzverweis nach der Nähe.
- `ders.`, `dies.`: derselbe Autor wie in der vorangehenden Literaturstelle.
- Verweise innerhalb des Textes (`oben E. 3.2`, `vgl. Ziff. 12`, `Rz. 45`): auf die Stelle des Dokuments selbst, nicht auf eine Autorität; als «interner Verweis» ausweisen und nicht in die Prüfliste aufnehmen.
- Beschreibende Formen («das zitierte Urteil», «die genannte Bestimmung»): nach den beschriebenen Merkmalen zuordnen (Gericht, Parteien, Gegenstand), nicht nur nach der Position.

Passt mehr als ein Antezedens oder keines, markieren Sie den Verweis als **ungelöst, manuell prüfen**, statt zu raten: eine falsche Zusammenführung verschmilzt zwei Autoritäten unbemerkt zu einer. Jeder aufgelöste Verweis zählt als dieselbe Fundstelle wie sein Antezedens; vermerken Sie, wo er vorkommt.

## Normalisierung

- BGE: `BGE Band Abteilung Seite E. Erwägung` ohne Fundseite; Abteilung als römische Zahl.
- Unpublizierte Bundesgerichtsurteile: `Urteil Verfahrensnummer vom Datum E. Erwägung` mit ausgeschriebenem Datum.
- Erlasse: `Art. Nummer Abs. Nummer lit. Buchstabe Abkürzung`; die SR-Nummer ergänzen, wenn der Text sie nennt oder die Abkürzung eindeutig ist (OR SR 220, ZGB SR 210, ZPO SR 272, StGB SR 311.0, BV SR 101, DSG SR 235.1, IPRG SR 291, ArG SR 822.11, UWG SR 241).
- Lehre: `Autor, Werk, Ort Jahr, Fundstelle`; Kommentare in der Form `Kommentarkürzel-Autor, Art. Nummer Gesetz N Randnote`.

## Ausgabeformat

Eine nummerierte Tabelle mit den Spalten: Nr., Typ (Bundesgericht publiziert, Bundesgericht unpubliziert, Bundesgericht übrige, kantonal, EGMR, Erlass, amtliche Publikation, Lehre), Zitat (normalisiert), Vorkommen (Seite, Randziffer oder Fussnote), Antezedens (bei Kurzverweisen), Status (erfasst, ungelöst, kein Identifikator). Schliessen Sie mit der Liste der zu prüfenden Fundstellen, gruppiert nach Typ, und mit den Stellen, an denen die Prüfung erfolgt: Bundesgerichtsentscheide auf bger.ch, Erlasse auf fedlex.admin.ch, kantonale Entscheide in den Entscheiddatenbanken der Kantone.

## Grenzen

- Die Extraktion erfasst Fundstellen in bekannter Form. Ein beschreibender Verweis ohne Identifikator («die Praxis des Bundesgerichts zum Konkurrenzverbot») hat nichts zu matchen; markieren Sie ihn «kein Identifikator, manuell prüfen».
- Dies ist keine Existenzprüfung: der Workflow sagt, was zitiert wird, nicht ob die Fundstelle existiert oder das Behauptete stützt.
- Die Muster decken die üblichen Formen der deutschsprachigen Schweiz ab; französische und italienische Formen (ATF, DTF, arrêt du TF, consid., art. ... CO) werden erkannt, wenn sie in einem deutschen Text vorkommen, aber die vollständige Behandlung bietet der französische Workflow dieses Packs. Eine ungewöhnliche Zitierweise kann durchrutschen. Bei hohem Einsatz zusätzlich von Hand prüfen.

## Herkunft

Der dreistufige Aufbau (Extraktion, Zusammenführung, Übergabe) folgt dem Workflow «Legal Citation Extraction» dieser Sammlung (MIT, Wieslaw Mazur / MateMatic Solutions), der seinerseits das Entwurfsmuster von eyecite (Free Law Project, BSD-2-Clause) nennt. Die Schweizer Zitiermuster, die Normalisierung und die Regeln für Kurzverweise sind eigene Arbeit von avidia.ai / Legal AI. Es wurde kein Code übernommen.
