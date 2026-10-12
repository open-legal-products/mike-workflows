---
name: sg-consultation-response-tabular-review
description: Review Singapore consultation papers and prepare evidence-grounded draft responses, consistency checks and submission plans for human approval.
license: MIT
metadata:
  version: 1.0.1
  author: Si Han Xu
  language: English
  mike-display-name: SG Consultation Response Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Singapore
---

# Consultation Response Drafting — Singapore (IMDA/PDPC/AGC/Ministry)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Identify the actual issuing body, paper, current deadline, channel and confidentiality terms from the official consultation source; distinguish statutory and policy consultations with a cited basis.
- Use supplied organisational positions and evidence to prepare question-by-question draft content. Preserve question numbering and label proposed positions, timelines and owners.
- Compare the full supplied draft with supplied prior filings and statements (for example, submissions to IMDA, PDPC or sector regulators). Report missing comparison materials rather than inferring consistency.
- Use the complete consultation paper and official notice; use supplied organisational positions, evidence, prior filings and public statements, approval records and the full response draft for cross-question checks. Report missing or partial inputs and limit the comparison accordingly. Distinguish document facts (cite the reviewed passage), operational facts (cite supplied organisational materials), external law or guidance (identify the current source/version and pinpoint provision), and labelled assessments or proposals. Return Not found for missing facts and Not assessed for unsupported analysis; do not infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence.
- Keep all drafts and proposed actions subject to human review. Do not submit, publish, approve deployment or accept residual risk without human approval.
