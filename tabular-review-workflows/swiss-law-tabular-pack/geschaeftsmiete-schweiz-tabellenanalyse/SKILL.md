---
name: "geschaeftsmiete-schweiz-tabellenanalyse"
description: "Tabular review of commercial leases under Swiss law (Art. 253 et seq. CO): parties, premises and purpose, term and options, notice, net rent and service charges, index and stepped rent, security, subletting and transfer, maintenance, tenant fit-out, return, extension, default, exclusivity, governing law. Column prompts in German; every prompt names the statutory default it is compared with."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "German"
  mike-display-name: "Geschaeftsmiete Schweiz Tabellenanalyse"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Real Estate"
  jurisdictions: "Switzerland"
---

# Geschäftsmiete Schweiz: Tabellenanalyse

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Hinweise zu dieser Prüfung

- Gegenstand sind Mietverträge über Geschäftsräume nach Art. 253 ff. OR (Büro, Laden, Gewerbe, Lager), einschliesslich Anhänge wie allgemeine Bedingungen, Pläne und Übergabeprotokolle. Wohnraummiete, Pacht und Baurechtsverträge sind nicht abgedeckt.
- Jede Spaltenfrage nennt den gesetzlichen Normalfall, mit dem die Klausel verglichen wird. Halten Sie in der Zelle fest, was der Vertrag regelt, und vermerken Sie, wenn er vom Normalfall abweicht. Beurteilen Sie nicht, ob die Abweichung zulässig ist; das bleibt der Anwältin oder dem Anwalt vorbehalten.
- Der Vertrag kann auf allgemeine Bedingungen eines Verbands verweisen. Nennen Sie diese Bedingungen mit Ausgabe, wenn der Vertrag sie bezeichnet, und beantworten Sie die Spaltenfrage aus ihrem Text nur, wenn er mitgeliefert wurde.
- Zitieren Sie Gesetzesartikel in der Form «Art. 266d OR». Antworten Sie in der Sprache der Spaltenfrage, mit Schweizer Schreibweise (ss, kein scharfes s).
- Die Tabelle ersetzt keine Rechtsberatung. Sie ist ein Entwurf für die Prüfung durch eine Anwältin oder einen Anwalt.
