---
name: "contrat-de-travail-suisse-analyse-tabulaire"
description: "Tabular review of individual employment contracts under Swiss law (Art. 319 et seq. CO): parties, term, probation, notice periods, salary and bonus, working time and overtime, sick pay, holidays, non-compete, confidentiality, intellectual property, data protection, collective agreements, governing law. Column prompts in French; every prompt names the statutory default it is compared with."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "French"
  mike-display-name: "Contrat de travail Suisse analyse tabulaire"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Employment"
  jurisdictions: "Switzerland"
---

# Contrat de travail Suisse: analyse tabulaire

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Remarques sur cet examen

- L'objet de l'examen est constitué des contrats individuels de travail au sens des art. 319 ss CO, y compris les annexes telles que règlements et cahiers des charges. Les contrats d'apprentissage, la location de services et les rapports de service de droit public ne sont pas couverts.
- Chaque question de colonne indique le régime légal auquel la clause est comparée. Indiquez dans la cellule ce que le contrat prévoit et signalez s'il déroge au régime légal. N'évaluez pas si la dérogation est admissible ; cela relève de l'avocate ou de l'avocat.
- Citez les articles de loi sous la forme «art. 335c al. 1 CO». Répondez dans la langue de la question de la colonne.
- Le tableau ne remplace pas un conseil juridique. Il s'agit d'un projet destiné à être examiné par une avocate ou un avocat.
