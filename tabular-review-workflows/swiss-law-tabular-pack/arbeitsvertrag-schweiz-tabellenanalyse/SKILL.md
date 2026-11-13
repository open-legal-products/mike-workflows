---
name: "arbeitsvertrag-schweiz-tabellenanalyse"
description: "Tabular review of individual employment contracts under Swiss law (Art. 319 et seq. CO): parties, term, probation, notice periods, salary and bonus, working time and overtime, sick pay, holidays, non-compete, confidentiality, intellectual property, data protection, collective agreements, governing law. Column prompts in German; every prompt names the statutory default it is compared with."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "German"
  mike-display-name: "Arbeitsvertrag Schweiz Tabellenanalyse"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Employment"
  jurisdictions: "Switzerland"
---

# Arbeitsvertrag Schweiz: Tabellenanalyse

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Hinweise zu dieser Prüfung

- Gegenstand sind Einzelarbeitsverträge nach Art. 319 ff. OR, einschliesslich Anhänge wie Reglemente und Stellenbeschriebe. Lehrverträge, Personalverleih und öffentlich-rechtliche Anstellungen sind nicht abgedeckt.
- Jede Spaltenfrage nennt den gesetzlichen Normalfall, mit dem die Klausel verglichen wird. Halten Sie in der Zelle fest, was der Vertrag regelt, und vermerken Sie, wenn er vom Normalfall abweicht. Beurteilen Sie nicht, ob die Abweichung zulässig ist; das bleibt der Anwältin oder dem Anwalt vorbehalten.
- Zitieren Sie Gesetzesartikel in der Form «Art. 335c Abs. 1 OR». Antworten Sie in der Sprache der Spaltenfrage, mit Schweizer Schreibweise (ss, kein scharfes s).
- Die Tabelle ersetzt keine Rechtsberatung. Sie ist ein Entwurf für die Prüfung durch eine Anwältin oder einen Anwalt.
