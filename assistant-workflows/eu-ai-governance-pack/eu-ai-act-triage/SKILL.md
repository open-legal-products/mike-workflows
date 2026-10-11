---
name: "eu-ai-act-triage"
description: "Fast triage of a system under the EU AI Act (Regulation (EU) 2024/1689) - 20-40 minutes through a chain of eight questions: is it an AI system at all (Article 3(1)), is the practice prohibited (Article 5), is it high-risk (Article 6 plus Annexes I and III), is general-purpose AI in play (Chapter V), which transparency obligations apply (Article 50), what is the operator's role (provider, deployer, importer, distributor, plus requalification under Article 25), and what is the resulting obligation map with deadlines. Output is a triage card: classification, role, applicable chapters, gaps, next steps, and a confidence tag on every cited provision. This is triage, not a conformity assessment - a high-risk, GPAI, or suspected-prohibited result routes to a human and a full analysis. Use when the question is whether the AI Act applies, how a system classifies, or whether the organisation is a provider or a deployer."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "Wieslaw Mazur / MateMatic Solutions"
  language: "English"
  mike-display-name: "EU AI Act Triage"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "AI Governance"
  jurisdictions: "European Union"
---
# EU AI Act Triage

Before an organisation pays for a full conformity audit, it should know whether it has a problem at all - and how big. Most "does the AI Act apply to us" questions do not need a hundred-page analysis. They need an ordered chain of determinations where each question closes or opens the next one: definition, prohibitions, high-risk, GPAI, transparency, role, obligation map, report. After 20-40 minutes the organisation holds a triage card: it knows which basket the system sits in, who it is in the value chain, and what follows from that.

The card is not a legal opinion. It is a structured starting point: an entry for the organisation's AI system register and a decision on whether the matter goes to a human for full analysis.

## When to use

- The organisation deploys or buys a tool with an AI component and asks whether the AI Act applies.
- Inventory work: a list of systems needs a preliminary classification each.
- A software vendor asks whether its product is a high-risk system or GPAI.
- A law firm builds an AI system register for a client or for itself.

## What this workflow does NOT do

- It does not replace a full compliance review or conformity assessment. The card says "this looks high-risk under Annex III point X", not "you meet Articles 8-15".
- It does not issue a legal opinion - the output is a draft classification for approval by an authorised human.
- On a high-risk, GPAI, or suspected-prohibited result it routes to a human and a full analysis. Triage ends there.
- It does not assess GDPR compliance - it flags the overlap for a separate DPIA workflow.
- It does not perform a fundamental rights impact assessment - it only signals that one is required (step 7).

## Workflow - 8 steps plus an entry gate

### Step 0 - provision verification (mandatory, before any citation)

No article number or provision text enters the card from model memory. Before recording a legal basis, fetch the current text of Regulation (EU) 2024/1689 from EUR-Lex (CELEX 32024R1689) and compare the wording. Note the retrieval date and source on the card. A provision that could not be verified in-session gets the tag [check in EUR-Lex] and can never support a "does NOT apply" determination.

### Step 1 - is it an "AI system" (Article 3(1))

Check each element of the definition separately: a machine-based system; designed to operate with varying levels of autonomy; may exhibit adaptiveness after deployment; infers, from the input it receives, how to generate outputs (predictions, content, recommendations, decisions); outputs can influence physical or virtual environments.

Counter-examples outside the definition: classic purely rule-based software with no inference layer, simple automation, a spreadsheet with formulas. The European Commission has issued guidelines on the definition - confirm the current document in EUR-Lex before citing it.

Result: YES / NO / BORDERLINE. On NO, triage ends, but the reasoning and the register entry stay - a year from now someone will ask why you decided this was not an AI system.

### Step 2 - prohibited practices (Article 5) - checklist

Tick every point, not a "general impression":

- subliminal or purposefully manipulative techniques causing significant harm
- exploitation of vulnerabilities (age, disability, social or economic situation)
- social scoring leading to unjustified detrimental treatment
- assessing the risk of committing a criminal offence based solely on profiling or personality traits
- untargeted scraping of facial images from the internet or CCTV to build facial recognition databases
- emotion recognition in the workplace and in education (outside medical and safety exceptions)
- biometric categorisation inferring sensitive attributes (race, political opinions, trade union membership, religion, sex life, orientation)
- real-time remote biometric identification in publicly accessible spaces for law enforcement (narrow exceptions)

The prohibitions apply since 2 February 2025. A SUSPICION on even one point means STOP - human gate immediately.

### Step 3 - high-risk (Article 6 plus Annex I and Annex III)

Two qualification paths:

- Path A (Article 6(1), Annex I): the system is a product, or a safety component of a product, covered by the Union harmonisation legislation listed in Annex I and subject to third-party conformity assessment (machinery, medical devices, toys, lifts, aviation, vehicles, and so on).
- Path B (Article 6(2), Annex III): a use case in one of the areas: biometrics; critical infrastructure; education and vocational training; employment and worker management; access to essential services (including credit scoring, pricing of life and health insurance, emergency dispatch, public benefits); law enforcement; migration, asylum and border control; administration of justice and democratic processes.

Article 6(3) filter: an Annex III system is not high-risk where it poses no significant risk of harm because it only performs a narrow procedural task, improves the result of a previously completed human activity, detects patterns or deviations without replacing human assessment, or performs a preparatory task. Exception to the exception: profiling of natural persons is always high-risk. Using the filter requires documenting the assessment and registering the system - confirm the exact paragraph numbers (Article 6(4), Article 49(2) [TO VERIFY]) in step 0.

### Step 4 - GPAI (Chapter V)

- Does the operator provide a general-purpose AI model, or integrate someone else's model into its own system?
- Obligations of GPAI model providers: technical documentation, information for downstream providers, a copyright policy, a training-content summary (Article 53). The partial open-source exemption does not cover models with systemic risk.
- Systemic-risk threshold (Article 51): presumption where the cumulative training compute exceeds 10^25 FLOP; then the additional obligations of Article 55 apply (model evaluations, adversarial testing, incident reporting, cybersecurity).
- GPAI Code of Practice (Article 56) - verify its status and current version at the source before relying on it.

Typical result for law firms and SMEs: deployer of a system built on GPAI, not a model provider. But see step 6 - requalification.

### Step 5 - transparency obligations (Article 50)

- Interaction with a human (chatbot): inform the person they are dealing with AI, unless obvious from context.
- Synthetic content (audio, image, video, text): machine-readable marking on the provider side.
- Emotion recognition or biometric categorisation: inform the persons exposed.
- Deepfakes: disclose that the content was artificially generated or manipulated.
- Text published to inform the public on matters of public interest: disclose AI involvement, unless the content underwent human editorial control.

Assign exact Article 50 paragraph numbers to the card rows only after the step 0 verification.

### Step 6 - operator role (plus requalification under Article 25)

Determine the role: provider / deployer / importer / distributor / authorised representative. Definitions in Article 3.

Requalification test (Article 25) - you become the provider of a high-risk system when you: (1) put your name or trademark on the system, (2) make a substantial modification to a high-risk system, or (3) modify the intended purpose so that the system becomes high-risk.

The classic trap: "our chatbot" running on someone else's model, with the organisation's logo on the front. The role determines most of the obligation map, so settle this step before saying anything about obligations.

### Step 7 - obligation map, timeline, FRIA signal

State of the law relative to the triage date (deadlines in Article 113 - verify in step 0):

- since 2 February 2025: prohibitions (Article 5) and AI literacy (Article 4) - APPLYING,
- since 2 August 2025: GPAI, governance, penalties - APPLYING,
- since 2 August 2026: the main body, including Annex III high-risk and Article 50 - APPLYING,
- until 2 August 2027: Path A high-risk systems (Annex I products) - the longer statutory period still running.

Build the map: role and classification determine the applicable chapters and articles, and from when.

FRIA signal (Article 27): a fundamental rights impact assessment before deployment is required from deployers that are bodies governed by public law or private entities providing public services, and from deployers of credit scoring and life or health insurance pricing systems (Annex III point 5 - confirm the letters in step 0). The workflow signals the requirement and flags the DPIA overlap; it does not perform the FRIA.

### Step 8 - report: the triage card

The card, section by section:

- Header: date, who ran it, verification source, and retrieval date.
- Classification table, one row per question (AI system / prohibited / high-risk / GPAI / transparency), each row with its result, verified basis, and confidence tag.
- Operator role, with the Article 25 requalification risk and which limb triggers it.
- Applicable chapters, each with its date and status.
- The FRIA determination: required, not required, or needs analysis, with the trigger.
- Gaps: what the facts did not establish.
- Next steps, always including the register entry and, where triggered, the mandatory escalation to a human for full analysis.
- Confidence-tag summary: verified count, to-check count, and a hard zero for "do not use".

## Human gate

The triage card is a draft classification, not a decision. An authorised human (lawyer, compliance officer) reviews and approves the card before it enters the register as binding. Three results escalate mandatorily and immediately: suspected prohibited practice (Article 5), high-risk, GPAI. In those cases triage ends with a referral to a human and a full analysis.

## Source verification

The provision comes from a database, not from memory. Hard rules: every article, paragraph, point, and Annex number cited on the card must be verified in-session in EUR-Lex (CELEX 32024R1689), otherwise it carries the [check in EUR-Lex] tag; a [TO VERIFY] tag in this workflow marks a spot where a number or document status requires verification before use; a "the AI Act does not apply to us" determination can never rest on an unverified provision; the consolidated version takes precedence over memory of the original text - regulations get corrected by corrigenda.
