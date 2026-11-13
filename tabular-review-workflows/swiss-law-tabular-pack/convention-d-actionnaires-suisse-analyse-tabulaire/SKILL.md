---
name: "convention-d-actionnaires-suisse-analyse-tabulaire"
description: "Tabular review of shareholders' agreements of Swiss companies limited by shares: parties and holdings, term, voting undertakings, board composition, reserved matters, transfer restrictions, pre-emption and first-refusal rights, leaver provisions, drag-along and tag-along, anti-dilution, dividends, funding obligations, non-compete, deadlock, exit, penalties, relationship to the articles, dispute resolution. Column prompts in French; every prompt names the statutory default it is compared with."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "French"
  mike-display-name: "Convention d'actionnaires Suisse analyse tabulaire"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Corporate"
  jurisdictions: "Switzerland"
---

# Convention d'actionnaires Suisse: analyse tabulaire

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Remarques sur cet examen

- L'objet de l'examen est constitué des conventions d'actionnaires (CA) portant sur des sociétés anonymes de droit suisse, y compris les annexes telles que registre des actionnaires, statuts et règlement d'organisation lorsqu'elles sont fournies. Les conventions d'associés de Sàrl et les contrats d'investissement ne sont couverts que dans la mesure où leurs clauses répondent aux mêmes questions.
- Chaque question de colonne indique le régime légal auquel la clause est comparée. Indiquez dans la cellule ce que le contrat prévoit et signalez s'il déroge au régime légal ou exige une mise en œuvre dans les statuts. N'évaluez pas si une clause est exécutoire ; cela relève de l'avocate ou de l'avocat.
- Les termes anglais tels que drag-along, tag-along, good leaver ou call option sont usuels dans les contrats suisses et peuvent figurer dans la cellule.
- Citez les articles de loi sous la forme «art. 704 al. 1 CO». Répondez dans la langue de la question de la colonne.
- Le tableau ne remplace pas un conseil juridique. Il s'agit d'un projet destiné à être examiné par une avocate ou un avocat.
