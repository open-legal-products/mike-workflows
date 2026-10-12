---
name: sg-online-safety-tabular-review
description: Review Singapore online-safety designation, applicable codes and operational evidence to propose compliance priorities.
license: MIT
metadata:
  version: 1.0.1
  author: Si Han Xu
  language: English
  mike-display-name: SG Online Safety Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Online Safety
  jurisdictions: Singapore
---

# Online Safety Obligation Map — Singapore (Broadcasting Act Codes)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Identify service scope and current designation from cited Broadcasting Act provisions and official notifications. Determine commencement of amendments from the identified commencement source, not the year of the Online Safety (Miscellaneous Amendments) Act 2022.
- Identify the actual Code of Practice for Online Safety — Social Media Services or App Distribution Services and its version; map clause-level duties only after scope, designation and commencement are established.
- Compare requirements with supplied moderation, direction-response, complaints and reporting evidence. Determine adjacent-law application from identified current provisions, including the Penal Code and Undesirable Publications Act, without assuming blanket coverage.
- Use the identified code/version and clauses, official designation notifications and any received directions, plus supplied service inventories, moderation/reporting records, metrics and correspondence. Do not presume designation or code application. Distinguish document facts (cite the reviewed passage), operational facts (cite supplied organisational materials), external law or guidance (identify the current source/version and pinpoint provision), and labelled assessments or proposals. Return Not found for missing facts and Not assessed for unsupported analysis; do not infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence.
- Keep all drafts and proposed actions subject to human review. Do not submit, publish, approve deployment or accept residual risk without human approval.
