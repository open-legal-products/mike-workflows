---
name: sg-dpia-cross-border-tabular-review
description: Review Singapore data-protection impact assessments and cross-border transfers against the PDPA and identified PDPC guidance.
license: MIT
metadata:
  version: 1.0.1
  author: Si Han Xu
  language: English
  mike-display-name: SG DPIA Cross Border Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Data Protection
  jurisdictions: Singapore
---

# DPIA & Transfer Assessment — Singapore (PDPA)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Determine PDPA application, roles and each consent or exception basis from current identified statutory provisions and supplied processing evidence.
- Determine DPIA necessity and process from the identified dated PDPC Guide to Data Protection Impact Assessments and any sector source; verify currency rather than asserting the latest version. Assess compliance with s 26 and the prescribed requirements in Part 3 of the Personal Data Protection Regulations 2021, including the required comparable standard of protection and the applicable legally enforceable obligation or exception. Do not assert a former prescribed-whitelist regime.
- Distinguish binding PDPA requirements, PDPC guidance and voluntarily adopted GDPR practice. Propose mitigations; record sign-off and risk acceptance only from supplied approval records.
- Use supplied processing and transfer inventories, recipient contracts, due-diligence records, DPIA, control evidence, request logs and sign-off records; do not infer actual flows or effective controls from policy text. Distinguish document facts (cite the reviewed passage), operational facts (cite supplied organisational materials), external law or guidance (identify the current source/version and pinpoint provision), and labelled assessments or proposals. Return Not found for missing facts and Not assessed for unsupported analysis; do not infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence.
- Keep all drafts and proposed actions subject to human review. Do not submit, publish, approve deployment or accept residual risk without human approval.
