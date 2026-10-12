---
name: au-horizon-scan-tabular-review
description: Scan Australian digital, content, data and AI regulation and map sourced obligations to supplied product evidence.
license: MIT
metadata:
  version: 1.0.1
  author: Si Han Xu
  language: English
  mike-display-name: AU Horizon Scan Tabular Review
  mike-type: tabular
  mike-availability: add-on
  practice: Regulatory
  jurisdictions: Australia
---

# Regulatory Horizon Scan & Obligation Map — Australia

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Scope and legal anchors

- Map Australian digital, content, data and AI obligations from each reviewed instrument to supplied product, operational and owner evidence.
- Identify the jurisdiction first. Use legislation.gov.au for Commonwealth law; for state/territory law use that jurisdiction’s official legislation portal, parliamentary site and gazette/commencement source (NSW legislation.nsw.gov.au; Victoria legislation.vic.gov.au; Queensland legislation.qld.gov.au; WA legislation.wa.gov.au; SA legislation.sa.gov.au; Tasmania legislation.tas.gov.au; ACT legislation.act.gov.au; NT legislation.nt.gov.au). Cite the exact instrument, provision, point-in-time version, assent/registration and commencement source; the Federal Register is not the source for all Australian law.
- Determine force, scope, status and dates from the particular instrument and commencement provision. Apply a default commencement rule only after identifying the governing jurisdiction, applicable provision and evidence that it applies. Do not assume a six-month code transition.
- The Privacy Act does not impose a universal PIA requirement. Agencies covered by the Privacy (Australian Government Agencies — Governance) APP Code 2017 must conduct a PIA for all high privacy risk projects. Assess whether that Code applies; otherwise use OAIC guidance to determine whether a PIA is warranted.
- The six additional age-restricted-material codes were registered on 9 September 2025 and commenced from 9 March 2026, with some measures commencing later. Identify the applicable service’s code or standard and each relevant measure’s commencement date; do not assume every measure applied on 9 March 2026.
- Determine current enactment and commencement status of each relevant reform from the Federal Register of Legislation and AGD/OAIC official sources, citing the instrument, provision, version, commencement table and assessment date. Separate proposals, enacted future duties and commenced duties; do not describe an enacted reform as merely proposed or assume a proposal is law.
- Separate document facts, supplied organisational materials (identify source/version), cited law with pinpoint references and current official-source version/status, and labelled assessments/proposals. Return Not found for missing facts and Not assessed for unsupported analysis. Never infer consent, ownership, approval, deadlines, prior positions or deployed controls from silence. Proposed actions require human approval; do not submit, publish, deploy or accept residual risk.
