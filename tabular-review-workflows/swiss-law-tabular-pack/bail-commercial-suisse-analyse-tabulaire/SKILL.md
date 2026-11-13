---
name: "bail-commercial-suisse-analyse-tabulaire"
description: "Tabular review of commercial leases under Swiss law (Art. 253 et seq. CO): parties, premises and purpose, term and options, notice, net rent and service charges, index and stepped rent, security, subletting and transfer, maintenance, tenant fit-out, return, extension, default, exclusivity, governing law. Column prompts in French; every prompt names the statutory default it is compared with."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "French"
  mike-display-name: "Bail commercial Suisse analyse tabulaire"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Real Estate"
  jurisdictions: "Switzerland"
---

# Bail commercial Suisse: analyse tabulaire

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Remarques sur cet examen

- L'objet de l'examen est constitué des contrats de bail portant sur des locaux commerciaux au sens des art. 253 ss CO (bureau, magasin, artisanat, entrepôt), y compris les annexes telles que conditions générales, plans et procès-verbaux de remise. Le bail d'habitation, le bail à ferme et les contrats de droit de superficie ne sont pas couverts.
- Chaque question de colonne indique le régime légal auquel la clause est comparée. Indiquez dans la cellule ce que le contrat prévoit et signalez s'il déroge au régime légal. N'évaluez pas si la dérogation est admissible ; cela relève de l'avocate ou de l'avocat.
- Le contrat peut renvoyer aux conditions générales d'une association. Indiquez ces conditions avec leur édition lorsque le contrat les désigne, et ne répondez à la question de la colonne à partir de leur texte que si celui-ci a été fourni.
- Citez les articles de loi sous la forme «art. 266d CO». Répondez dans la langue de la question de la colonne.
- Le tableau ne remplace pas un conseil juridique. Il s'agit d'un projet destiné à être examiné par une avocate ou un avocat.
