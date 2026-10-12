---
name: sg-horizon-scan-tabular-review
description: Map Singapore regulatory instruments, legal force, commencement and obligations to supplied product and compliance evidence.
license: MIT
metadata:
  version: 1.0.1
  author: Si Han Xu
  language: English
  mike-display-name: SG Horizon Scan Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Singapore
---

# Regulatory Horizon Scan & Obligation Map — Singapore

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Identify each Singapore instrument, official point-in-time version, lifecycle stage, regulated class and document-supported product nexus.
- Determine legal force and each provision’s commencement from the particular instrument and any notification, designation or direction with pinpoint citations. Do not treat assent or enactment year as commencement.
- Separate enacted obligations and penalties from guidance and proposed workstreams. Use supplied inventories, control evidence, owner records and prior filings for organisational mapping.
- Use the identified instrument and official lifecycle sources, plus supplied product inventories, owner records, compliance evidence and prior engagement records for organisational mapping. Distinguish document facts (cite the reviewed passage), operational facts (cite supplied organisational materials), external law or guidance (identify the current source/version and pinpoint provision), and labelled assessments or proposals. Return Not found for missing facts and Not assessed for unsupported analysis; do not infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence.
- Keep all drafts and proposed actions subject to human review. Do not submit, publish, approve deployment or accept residual risk without human approval.
