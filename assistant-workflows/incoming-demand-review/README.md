# Incoming Demand Review

An internal pre-reply review of a demand against the supplied contract, payment
records and correspondence. It makes the claim, supporting evidence, adverse
evidence and unresolved questions visible before a lawyer chooses a response.

The workflow pays particular attention to two easily missed follow-ups: the
transaction-level reconciliation needed to establish an amount, and the
receipt/trigger evidence needed to assess a response date. It can credit a
well-supported supplier claim as well as identify contradictions in a demand.

## Use

Choose **Incoming Demand Review** and supply the demand and the relevant record.
Identify the represented party and any scope limit. For example:

> We act for the buyer. Review the attached demand and file and tell me what
> needs attention before we reply. Use only these four documents.

Expect an internal assessment, a claim-to-record comparison, provisional amount
and date analysis, and prioritized evidence/client-instruction questions. Source
coverage and missing attachments remain explicit. The workflow targets a
proportionate, concise review, while retaining adverse facts and qualifications.

For a local Markdown import in Mike, upload `SKILL.md` and set the title to
Incoming Demand Review, type Assistant, practice Litigation and jurisdiction
General. No document template or additional asset is required. This folder is a
community add-on; it is not one of Mike's approved default workflows.

## Review limits

Legal authorities, service facts and response decisions require lawyer
verification. A sender's date and an incomplete account are evidence to assess,
not established deadlines or balances. Read the whole output: a qualified
analysis can still end in an overconfident proposed position.

The workflow supports internal human review. The selected host, model, document
access and citation pipeline affect the result. External-facing use, legal
accuracy across jurisdictions and confidentiality isolation need separate
validation.

## Evaluation

The [evaluation bundle](evaluation/README.md) contains fictional inputs, separate
review keys, a deterministic DOCX generator and fixture integrity checks. Keep
the review keys outside the generating model's context. Static fixture checks
do not evaluate model behavior.

The [pilot report](RESULTS.md) records the actual in-Mike comparisons,
model/settings, source/citation checks, independent agent review, failed earlier
revisions and limits. The final workflow is frozen before its fresh held-out
case. This small synthetic pilot does not measure lawyer time saved or establish
broad reliability.

## Origin and license

Author: **Lawyered**. MIT; see [LICENSE](LICENSE). The repository's existing MIT
notice remains unchanged.

This is an AI-assisted adaptation of Lawyered's unpublished demand-review
practice workflow, reviewed on 2026-11-02 and substantially rewritten as a
portable document-review add-on. The private source has no public URL. Its
reusable concepts include distinguishing allegations from evidence, preserving
counterevidence and separating asserted dates from verified triggers. No private
client files, firm routing or account configuration are part of the contribution.
This provenance statement describes the adaptation; it is not an independent
legal determination of ownership or exhaustive originality.
