---
name: "china-labor-contract-tabular-review"
description: "Use this workflow to review employment contracts governed by PRC (mainland) law under the Labor Contract Law (劳动合同法) and related rules, and extract structured information into the tabular review columns defined in table-columns.yaml. Each column records the contract term next to the statutory position, for comparing many contracts at once."
license: "MIT"
metadata:
  version: "0.1.0"
  author: "1152405245hwc-coder"
  language: "English"
  mike-display-name: "China Labor Contract Tabular Review"
  mike-type: "tabular"
  mike-availability: "add-on"
  practice: "Employment"
  jurisdictions: "People's Republic of China"
---
# China Labor Contract Tabular Review

## Instructions

- Apply each column prompt in `table-columns.yaml` to each document independently.
- Extract only information supported by the document text.
- Include clause references, section names, dates, amounts, party names, and defined terms where available.
- If responsive information is not found, return an empty value or a concise "Not found" response.
- Keep cell outputs concise while including enough context to make each extracted value useful.
- Do not invent citations, facts, parties, dates, rights, obligations, or financial consequences.
- Render the completed results as an exportable Excel (`.xlsx`) file. If Excel output is not possible, render the results as a Markdown table.
## Review Guidance

- Each cell states the contract term with its clause reference first, then the comparison with the statutory position. If the contract is silent, write "Not agreed"; do not leave the cell empty and do not fill it with the statutory rule unmarked.
- Statutory positions in the column prompts summarize the cited articles. Confirm every cited article against the official Chinese text in force; points tagged [TO VERIFY] are not confirmed and cannot support a finding that a clause is lawful.
- Quote the original Chinese wording for disputed clauses (unilateral changes, penalties, social-insurance waivers, non-competes) rather than paraphrasing.
- Local standards (minimum wage, social-insurance base) are not in the contract; write "Check local standard" instead of guessing.
- Ratings in "Risk Rating" and "Key Issues" depend on the side represented. If the user does not say, use the employer compliance view and state "View: employer (default)" on the first line of "Key Issues".
- This table extracts and compares; it is not a legal opinion. For a clause-by-clause review with replacement wording, use the China Labor Contract Review assistant workflow. For PIPL process duties, use the China PIPL Pack.
