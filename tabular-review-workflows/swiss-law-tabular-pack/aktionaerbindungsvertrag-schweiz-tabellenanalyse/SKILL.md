---
name: "aktionaerbindungsvertrag-schweiz-tabellenanalyse"
description: "Tabular review of shareholders' agreements of Swiss companies limited by shares: parties and holdings, term, voting undertakings, board composition, reserved matters, transfer restrictions, pre-emption and first-refusal rights, leaver provisions, drag-along and tag-along, anti-dilution, dividends, funding obligations, non-compete, deadlock, exit, penalties, relationship to the articles, dispute resolution. Column prompts in German; every prompt names the statutory default it is compared with."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "German"
  mike-display-name: "Aktionaerbindungsvertrag Schweiz Tabellenanalyse"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Corporate"
  jurisdictions: "Switzerland"
---

# Aktionärbindungsvertrag Schweiz: Tabellenanalyse

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Hinweise zu dieser Prüfung

- Gegenstand sind Aktionärbindungsverträge (ABV) über Aktiengesellschaften nach Schweizer Recht, einschliesslich Beilagen wie Aktionärsliste, Statuten und Organisationsreglement, wenn sie mitgeliefert werden. Gesellschafterverträge von GmbH und Investitionsverträge sind nur insoweit abgedeckt, als ihre Klauseln denselben Fragen entsprechen.
- Jede Spaltenfrage nennt den gesetzlichen Normalfall, mit dem die Klausel verglichen wird. Halten Sie in der Zelle fest, was der Vertrag regelt, und vermerken Sie, wenn er vom Normalfall abweicht oder eine Umsetzung in den Statuten verlangt. Beurteilen Sie nicht, ob eine Klausel durchsetzbar ist; das bleibt der Anwältin oder dem Anwalt vorbehalten.
- Englische Begriffe wie Drag-along, Tag-along, Good Leaver oder Call Option sind in Schweizer Verträgen üblich und dürfen in der Zelle stehen.
- Zitieren Sie Gesetzesartikel in der Form «Art. 704 Abs. 1 OR». Antworten Sie in der Sprache der Spaltenfrage, mit Schweizer Schreibweise (ss, kein scharfes s).
- Die Tabelle ersetzt keine Rechtsberatung. Sie ist ein Entwurf für die Prüfung durch eine Anwältin oder einen Anwalt.
