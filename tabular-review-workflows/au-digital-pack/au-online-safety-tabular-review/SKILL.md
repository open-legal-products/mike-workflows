---
name: au-online-safety-tabular-review
description: Map Australian online-safety obligations under the Online Safety Act 2021 (Cth) and applicable eSafety codes and standards.
license: MIT
metadata:
  version: 1.0.1
  author: Si Han Xu
  language: English
  mike-display-name: AU Online Safety Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Online Safety
  jurisdictions: Australia
---

# Online Safety Obligation Map — Australia (eSafety Codes & Standards)

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Determine service and material classes under the current Online Safety Act 2021 (Cth), eSafety register, applicable registered code/standard and clause.
- The six additional age-restricted-material codes were registered on 9 September 2025 and commenced from 9 March 2026, with some measures commencing later. Identify the applicable service’s code or standard and each relevant measure’s commencement date; do not assume every measure applied on 9 March 2026.
- Apply the registered Head Terms: class 1A material comprises child sexual exploitation material, pro-terror material and extreme crime and violence material, subject to the defined criteria. Class 1B is a subcategory of class 1 material comprising crime and violence material and drug-related material, in each case as further described in Annexure A of those Head Terms. Do not classify generic crime or violence material as class 1A.
- Apply the registered age-restricted Head Terms: class 1C is class 1 material describing or depicting specific fetish practices or fantasies, excluding class 1A material. Apply the definition of class 2 material in s 107 of the Online Safety Act 2021. Do not classify generic sexual content as class 1C.
- Distinguish code/standard duties, Basic Online Safety Expectations and statutory notice/reporting powers. Verify the version, service schedule, trigger and date for each measure. Compare only with supplied complaints, moderation, testing, reporting and incident evidence.
- Separate document facts, supplied organisational materials (identify source/version), cited law with pinpoint references and current official-source version/status, and labelled assessments/proposals. Return Not found for missing facts and Not assessed for unsupported analysis. Never infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence. Proposed actions require human approval; do not submit, publish, deploy or accept residual risk.
