---
name: "privilege-preflight"
description: "Pre-flight check for legal content BEFORE it is sent to an external, cloud-based AI tool (a browser chatbot, an office-suite assistant, any API outside the firm's control). Inventories what actually sits in the prompt, scores five risk factors - client identifiability, facts under professional secrecy, litigation strategy and work-product, third-party personal data, the AI provider's terms - and returns a banded verdict SAFE / CAUTION / STOP with a factor table and a disclosure-impact assessment. For CAUTION it prepares a redacted draft of the prompt for human approval; for STOP it always shows a way forward instead of a bare prohibition. Sends nothing and never performs the final redaction. Use before pasting client-matter content into an external chatbot, for a firm-wide prompt audit, or as the skeleton of an internal AI usage policy."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "Privilege Preflight"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Professional Responsibility"
  jurisdictions: "European Union, General"
---
# Privilege Preflight

A prompt pasted into someone else's chatbot is a disclosure. Not "tool usage" - a disclosure. No lawyer would fax a case file to a newspaper to get a second opinion on the drafting style. Yet the same lawyer will paste half a statement of claim into a free chatbot "just to polish the wording". The two acts differ less than it seems: the content leaves the firm and lands with a third party, on terms nobody read, with retention nobody controls, possibly on servers outside the EEA.

This workflow does one thing: it holds the hand above the Enter key for the length of one check. It does not ban cloud AI - firms use it and will keep using it. It forces a conscious decision instead: what exactly leaves, to whom, on what terms, and what happens if it ever surfaces.

The verdict is banded, not binary. Most prompts are neither clean nor forbidden - they are redactable. That is why the middle band (CAUTION) ends with a redacted draft rather than a lecture.

The frame is European: legal professional privilege as shaped by the Court of Justice of the EU, national professional secrecy regimes, GDPR, and the Trade Secrets Directive. US attorney-client privilege appears only as a comparative footnote.

## When to use, and what this workflow does NOT do

Use it: before pasting client-matter content into an external AI chatbot; for a firm-wide prompt audit (retrospective: what people have been sending); as the skeleton of an internal AI usage policy - the SAFE / CAUTION / STOP bands translate directly into policy tiers; when a colleague asks "can I put this into the chatbot" - run the preflight instead of answering from gut feeling.

Explicit negative scope:

- it does NOT send anything anywhere - verdict and draft stay on the machine,
- it does NOT perform the final redaction - it prepares a redacted version as a draft; a human reads it, corrects it, and decides alone whether to send,
- it does NOT assess the legal merits of the prompt,
- it does NOT replace a data protection impact assessment for deploying an AI tool in the firm - the preflight checks a single piece of content, not a process,
- it does NOT give guarantees - a SAFE band means "no risk factor found", not "I vouch that no risk exists".

## Legal bases (cite with a confidence tag)

Quote an article number only when it is certain. Otherwise describe the duty in words and mark it [TO VERIFY]. Never invent a citation.

- Legal professional privilege, EU law - settled CJEU case law: AM&S v Commission (Case 155/79) recognised LPP for communications with independent external lawyers in EU competition investigations; Akzo Nobel v Commission (Case C-550/07 P) confirmed that in-house counsel communications are NOT covered by LPP in EU Commission competition proceedings. Practical consequence: in-house teams pasting internal legal analysis into a cloud tool cannot assume even the baseline EU-level protection external counsel would have.
- National professional secrecy regimes - in most continental systems secrecy is the lawyer's own enforceable duty, broader in scope than a common-law evidentiary privilege and typically unlimited in time. The exact statutory basis differs per jurisdiction - identify the user's regime and mark specifics [TO VERIFY] per country.
- GDPR - personal data of the client and of third parties inside a prompt is processing: the definition of personal data (Article 4(1)), the AI provider as a processor requiring a data processing agreement (Article 28), transfers outside the EEA (Chapter V).
- Trade Secrets Directive (EU) 2016/943 - protection depends on "reasonable steps" to keep the information secret; pasting a client's trade secret into a public chatbot is an argument AGAINST reasonable steps and can weaken the client's own protection, independently of any privilege question.
- Disciplinary and liability exposure - breach of professional secrecy is a disciplinary offence under bar rules and may found civil liability towards the client; the concrete provision depends on the bar involved [TO VERIFY].
- Comparative footnote only: US attorney-client privilege and work-product doctrine raise a parallel waiver debate, but this workflow does not use them as its framework.

## The five assessment factors

Score each factor separately: CLEAN / CAUTION / CRITICAL.

**(a) Client identifiability.** Direct (company name, registration number, personal names, case reference) AND mosaic: the combination of industry, city, dispute amount, and event date can point to one client even though no single element does. Mosaic test: would a local journalist with a search engine work out who this is?

**(b) Facts under professional secrecy.** Everything the lawyer learned in connection with providing legal assistance - including facts that look neutral (the mere fact that a client seeks advice on a given matter is itself covered).

**(c) Litigation strategy / work-product.** Planned pleas, assessment of the weaknesses of one's own position, negotiation tactics, internal notes on witness credibility. This is the most dangerous category - disclosure harms even after full pseudonymisation, because the value sits in the reasoning itself, not in the identity of the parties.

**(d) Third-party personal data.** Witnesses, the opposing party, family members, the client's employees. They chose no law firm and accepted no terms - the lawful basis for processing their data in a cloud AI tool is usually the weakest link.

**(e) Where the prompt goes.** The AI provider's terms: is prompt content used for model training, what is the retention period (and can it be switched off), where are the servers, is there a transfer outside the EEA and on what basis, is there a data processing agreement (Article 28 GDPR), free tier or business tier (the terms can differ radically). If the user does not know - assume the worst variant and say so explicitly.

## Workflow

1. **Content inventory.** Break the prompt into elements: who is named (entities, persons), which facts, which figures and dates, which document fragments, whether it contains the lawyer's own reasoning (assessment, tactics), and where the user wants to send it (tool name and tier). No inventory, no assessment - "I roughly know what is in there" does not count.
2. **Score the five factors.** Each factor (a)-(e) gets CLEAN / CAUTION / CRITICAL plus one sentence of justification quoting the fragment that drives the score.
3. **Banded verdict.** The aggregation rule is mechanical: any factor CRITICAL means STOP; factor (c) strategy or work-product at CAUTION or above means STOP (redaction does not cure work-product); otherwise, at least one CAUTION means CAUTION; all CLEAN means SAFE.
4. **Disclosure impact assessment.** For CAUTION and STOP: two or three sentences on what concretely happens if the content surfaces - towards the client (lost trust, harm to the matter), towards the lawyer (disciplinary exposure, liability), towards third parties (GDPR claims). No scaremongering - a realistic scenario.
5. **Redaction draft (CAUTION only).** Pseudonymise entities and values with placeholders [CLIENT], [COUNTERPARTY], [PERSON-1], [AMOUNT], [DATE], [PLACE], [CASE-REF]; delete fragments unnecessary for the prompt's purpose (the cheapest redaction is deletion); re-run the mosaic test AFTER redaction - does the combination of what remains still point to the client? For STOP, produce no draft - a redacted litigation strategy is still a litigation strategy.
6. **Alternatives (on STOP).** Always show a way forward, not only a prohibition: a local zero-cloud environment; a local model on the firm's own hardware; reformulating the question into an abstract one (ask about the rule, not the matter); doing the task without AI, if the stakes demand it.
7. **Human gate.** Present the result and stop.

## Output format

One result block:

- The prompt's working name and purpose.
- The target tool and tier, or "unknown - worst case assumed".
- The five-factor table: score per factor plus the content fragment driving it.
- The verdict: SAFE / CAUTION / STOP.
- The disclosure impact, 2-3 sentences.
- The recommendation: alternatives on STOP, the redacted draft on CAUTION, clear-to-send on SAFE.
- On CAUTION: the full redacted version, marked as a draft requiring human approval, with the post-redaction mosaic check result.
- The closing line: "The decision belongs to a human. This workflow has sent nothing."

## Human gate

The output is a draft, not a decision. Nothing gets sent until an authorised human has read the verdict, the factor table, and - on CAUTION - the entire redacted draft, line by line. The human approves, corrects, or rejects; sending is always the human's own act, performed outside this workflow.

The governance boundary is hard: the workflow prepares, the human executes. This covers redaction too - an automatically inserted placeholder can miss the context (e.g. [AMOUNT] inside a contract quote where the amount is the very subject of the question). A draft nobody read is worthless and must never be treated as "already anonymised".

The SAFE band passes through the gate as well: the human sees the factor table and presses Enter personally. SAFE shortens the deliberation, it does not remove the responsibility.
