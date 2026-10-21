---
name: "eu-ai-act-triage"
description: "Fast triage of a system under the EU AI Act (Regulation (EU) 2024/1689) - 20-40 minutes through a scope gate (Article 2) and a chain of eight questions: is it an AI system at all (Article 3(1)), is the practice prohibited (Article 5), is it high-risk (Article 6 plus Annexes I and III), is general-purpose AI in play (Chapter V), which transparency obligations apply (Article 50), what is the operator's role (provider, deployer, importer, distributor, authorised representative, product manufacturer, plus requalification under Article 25), and what is the resulting obligation map with deadlines. Output is a triage card: classification, role, applicable chapters, gaps, next steps, and a confidence tag on every cited provision. This is triage, not a conformity assessment - a high-risk, GPAI, or suspected-prohibited result routes to a human and a full analysis. Use when the question is whether the AI Act applies, how a system classifies, or whether the organisation is a provider or a deployer."
license: "MIT"
metadata:
  version: "1.2.0"
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

## Workflow - 8 steps plus two entry gates

### Step 0 - provision verification (mandatory, before any citation)

No article number or provision text enters the card from model memory. Before recording a legal basis, fetch the current consolidated text of Regulation (EU) 2024/1689 from EUR-Lex - consolidated version 02024R1689-20260727 - and compare the wording. Do not verify against the 2024 original (CELEX 32024R1689): Regulation (EU) 2026/1744 of 8 July 2026 (CELEX 32026R1744, the "Digital Omnibus on AI") amended, among others, Articles 2, 3, 4, 5, 6, 25, 27, 50, 111 and 113 and Annex I, and added Article 4a. Check EUR-Lex for a consolidated version later than 02024R1689-20260727 and use the latest one. Note the consolidated-version identifier, the retrieval date and the source on the card. A provision that could not be verified in-session gets the tag [check in EUR-Lex] and can never support a "does NOT apply" determination.

### Step 0a - scope gate (Article 2)

Before any classification, establish that the AI Act reaches this operator and this system. Record the scope result on the card; an out-of-scope result ends triage with its reasoning, and an unestablished one is a gap, never "out of scope".

Who is covered (Article 2(1)) - the operator must fall under at least one limb:

- providers placing AI systems on the market or putting them into service, or placing general-purpose AI models on the market, in the Union - whether established in the Union or in a third country,
- deployers established or located in the Union,
- providers and deployers established or located in a third country, where the output produced by the AI system is used in the Union,
- importers and distributors of AI systems,
- product manufacturers placing an AI system on the market or putting it into service together with their product and under their own name or trademark,
- authorised representatives of providers not established in the Union,
- affected persons located in the Union.

Exclusions to check one by one, each with the fact that supports it:

- systems used exclusively for military, defence or national security purposes, and areas outside the scope of Union law (Article 2(3)),
- public authorities of a third country and international organisations acting under international cooperation agreements for law enforcement or judicial cooperation, with adequate safeguards (Article 2(4)),
- AI systems or models specifically developed and put into service for the sole purpose of scientific research and development (Article 2(6)),
- research, testing or development activity before the system is placed on the market or put into service - testing in real-world conditions is NOT excluded (Article 2(8)),
- obligations of deployers who are natural persons using AI systems in the course of a purely personal, non-professional activity (Article 2(10)) - the exclusion covers the deployer's obligations, not the provider's,
- AI systems released under free and open-source licences - unless they are high-risk or fall under Article 5 or Article 50 (Article 2(12)).

Confirm each paragraph number against the consolidated text in step 0 before it enters the card.

### Step 1 - is it an "AI system" (Article 3(1))

Check each element of the definition separately: a machine-based system; designed to operate with varying levels of autonomy; may exhibit adaptiveness after deployment; infers, from the input it receives, how to generate outputs (predictions, content, recommendations, decisions); outputs can influence physical or virtual environments.

Counter-examples outside the definition: classic purely rule-based software with no inference layer, simple automation, a spreadsheet with formulas. The European Commission has issued guidelines on the definition - confirm the current document in EUR-Lex before citing it.

Result: YES / NO / BORDERLINE. On NO, triage ends, but the reasoning and the register entry stay - a year from now someone will ask why you decided this was not an AI system.

### Step 2 - prohibited practices (Article 5) - checklist

Work through every point, not a "general impression". The labels below are only an index: each prohibition is a set of statutory elements, and the card records, for each point that is in play, every element of the verified text as MET / NOT MET / UNKNOWN, with the fact behind it. Record at least: the intended purpose, the actual use, the affected persons, the harm, and any exception, consent or safeguard the provision names.

- subliminal techniques, or purposefully manipulative or deceptive techniques, with the objective or effect of materially distorting behaviour by appreciably impairing the person's ability to make an informed decision, causing or reasonably likely to cause significant harm (Article 5(1)(a))
- exploitation of vulnerabilities due to age, disability or a specific social or economic situation, with the objective or effect of materially distorting behaviour, causing or reasonably likely to cause significant harm (Article 5(1)(b))
- social scoring leading to unjustified detrimental treatment
- assessing the risk of committing a criminal offence based solely on profiling or personality traits
- untargeted scraping of facial images from the internet or CCTV to build facial recognition databases
- emotion recognition in the workplace and in education (outside medical and safety exceptions)
- biometric categorisation inferring sensitive attributes (race, political opinions, trade union membership, religion, sex life, orientation)
- real-time remote biometric identification in publicly accessible spaces for law enforcement (narrow exceptions)
- generating or manipulating realistic images, video, audio or similar material of an identifiable natural person's intimate parts, or of an identifiable natural person engaged in sexually explicit activities, without that person's freely given, specific, informed, unambiguous and explicit consent (Article 5(1)(ba))
- generating or manipulating material or performance within the meaning of Article 2, points (c) and (e), of Directive 2011/93/EU, except where a "without right" defence applies under national law (Article 5(1)(bb))

Points (ba) and (bb) were added by Regulation (EU) 2026/1744 and apply from 2 December 2026, together with Article 5(1a) and (1b). Placing on the market or putting into service is caught only where generating that material is the intended purpose, or where the system's design, training, architecture, capabilities or user-facing functionalities make it a reasonably foreseeable and reproducible outcome without significant technical modification and the system lacks reasonable and adequate technical safety measures and other safeguards to reliably prevent that generation or manipulation, taking into account reasonably foreseeable misuse, and to correct observed or reported misuse (Article 5(1a)(a)). Use is caught only where the deployer uses the system for the purpose of generating or manipulating such material (Article 5(1a)(b)). Manipulation that does not increase the exposure of depicted intimate parts or alter the nature of depicted sexually explicit activities is not "manipulation" for point (ba) (Article 5(1b)); this carve-out does not apply to point (bb).

The other prohibitions apply since 2 February 2025. Decision rule per point: every element MET - prohibited practice likely, STOP and escalate; any element UNKNOWN - suspected prohibited practice, STOP and escalate with the open elements listed; an element clearly NOT MET on established facts - that point is not engaged, and the card states which element fails and why. Both escalation results go to the human gate with the element table attached.

### Step 3 - high-risk (Article 6 plus Annex I and Annex III)

Two qualification paths:

- Path A (Article 6(1), Annex I): the system is a product, or a safety component of a product, covered by the Union harmonisation legislation listed in Annex I and subject to third-party conformity assessment (medical devices, toys, lifts, aviation, vehicles, and so on). Since Regulation (EU) 2026/1744:
  - "safety component" is narrower (Article 3(14)): a component that fulfils a safety function or whose failure endangers the health and safety of persons or property; systems used solely for user assistance, performance optimisation, efficiency, automation, convenience or quality control are not safety components, unless their failure would endanger health and safety (Article 6(1a) and (1b));
  - third-party assessment required only for non-safety reasons (for example radio spectrum) does not meet the Article 6(1)(b) condition (Article 6(1c));
  - machinery: Directive 2006/42/EC was removed from Annex I Section A and Regulation (EU) 2023/1230 added to Section B. For high-risk systems under Section B acts only Article 6(1), Article 60a and Articles 102 to 112 apply, and Articles 57 to 59 only in so far as the high-risk requirements have been integrated into that sectoral legislation (Article 2(2)).
- Path B (Article 6(2), Annex III): a use case in one of the areas: biometrics; critical infrastructure; education and vocational training; employment and worker management; access to essential services (including credit scoring, pricing of life and health insurance, emergency dispatch, public benefits); law enforcement; migration, asylum and border control; administration of justice and democratic processes.

Article 6(3) filter: an Annex III system is not high-risk where it poses no significant risk of harm because it only performs a narrow procedural task, improves the result of a previously completed human activity, detects patterns or deviations without replacing human assessment, or performs a preparatory task. Exception to the exception: profiling of natural persons is always high-risk. Using the filter requires documenting the assessment and registering the system - confirm the exact paragraph numbers (Article 6(4), Article 49(2) [TO VERIFY]) in step 0.

### Step 4 - GPAI (Chapter V)

- Does the operator provide a general-purpose AI model, or integrate someone else's model into its own system?
- Obligations of GPAI model providers: technical documentation, information for downstream providers, a copyright policy, a training-content summary (Article 53). The partial open-source exemption does not cover models with systemic risk.
- Systemic-risk threshold (Article 51): presumption where the cumulative training compute exceeds 10^25 FLOP; then the additional obligations of Article 55 apply (model evaluations, adversarial testing, incident reporting, cybersecurity).
- GPAI Code of Practice (Article 56) - verify its status and current version at the source before relying on it.

Typical result for law firms and SMEs: deployer of a system built on GPAI, not a model provider. But see step 6 - requalification.

### Step 5 - transparency obligations (Article 50)

Each row is an obligation plus its exceptions. Before a row goes on the card as "applies", check the exception named in it; a row whose exception is met is recorded as "exception applies", with the fact behind it.

- Interaction with a human (chatbot): inform the person they are dealing with AI. Exceptions: obvious from the point of view of a reasonably well-informed person given the context; systems authorised by law to detect, prevent, investigate or prosecute criminal offences, unless available for the public to report a criminal offence.
- Synthetic content (audio, image, video, text): machine-readable marking on the provider side. Exceptions: the system performs an assistive function for standard editing, or does not substantially alter the input data provided by the deployer or its semantics; use authorised by law for criminal offences.
- Emotion recognition or biometric categorisation: the deployer informs the persons exposed. Exception: systems permitted by law to detect, prevent or investigate criminal offences.
- Deepfakes: the deployer discloses that the content was artificially generated or manipulated. Exception: use authorised by law for criminal offences. For evidently artistic, creative, satirical, fictional or analogous work the duty still applies but is limited to disclosing the existence of such content in a way that does not hamper the display or enjoyment of the work.
- Text published to inform the public on matters of public interest: disclose AI involvement. Exceptions: use authorised by law for criminal offences; or the content has undergone human review or editorial control AND a natural or legal person holds editorial responsibility for the publication; both conditions must be met.

These obligations apply from 2 August 2026, the general date of application (Article 113 - step 7). Transitional rule: providers of systems generating synthetic audio, image, video or text that were placed on the market before 2 August 2026 have until 2 December 2026 to comply with Article 50(2) (Article 111(4), added by Regulation (EU) 2026/1744). Assign exact Article 50 paragraph numbers to the card rows only after the step 0 verification.

### Step 6 - operator role (plus requalification under Article 25)

Determine the role: provider / deployer / importer / distributor / authorised representative / product manufacturer. Definitions in Article 3; the product manufacturer is an operator under Article 2(1).

Requalification test (Article 25(1)) - a distributor, importer, deployer or other third party becomes the provider of a high-risk system when it: (1) puts its name or trademark on a high-risk AI system already placed on the market or put into service (without prejudice to contractual arrangements allocating the obligations otherwise), (2) makes a substantial modification to a high-risk system, or (3) modifies the intended purpose so that the system becomes high-risk. The initial provider then no longer counts as the provider of that system, but must cooperate with the new one (Article 25(2) as amended).

Product manufacturer (Article 25(3)): where a high-risk AI system is a safety component of a product covered by the Union harmonisation legislation in Annex I Section A, the product manufacturer is the provider of that system when the system is placed on the market together with the product under the manufacturer's name or trademark, or is put into service under that name or trademark after the product has been placed on the market.

The classic trap: "our chatbot" running on someone else's model, with the organisation's logo on the front. The role determines most of the obligation map, so settle this step before saying anything about obligations.

### Step 7 - obligation map, timeline, FRIA signal

State of the law relative to the triage date (deadlines in Article 113 as amended by Regulation (EU) 2026/1744 - verify in step 0, and compare the triage date with each date below rather than copying "applying" from this list):

- since 2 February 2025: Chapters I and II - prohibitions (Article 5) and AI literacy (Article 4) - APPLYING, EXCEPT Article 5(1)(ba) and (bb) and Article 5(1a) and (1b), which apply only from 2 December 2026. Article 4 as replaced in 2026: providers and deployers take measures to support the AI literacy of their staff and of other persons dealing with AI systems on their behalf; no specific level has to be guaranteed,
- since 2 August 2025: notifying authorities and notified bodies (Chapter III Section 4), GPAI (Chapter V), governance (Chapter VII), penalties (Chapter XII) and confidentiality (Article 78) - APPLYING, except fines on GPAI model providers (Article 101), which apply from the general date,
- from 27 July 2026: Articles 102 to 110,
- from 2 August 2026: the general date of application, including Article 50 and Article 101,
- from 2 December 2026: the new prohibitions in Article 5(1)(ba) and (bb) with Article 5(1a) and (1b); Article 50(2) for synthetic-content systems already on the market before 2 August 2026 (Article 111(4)),
- from 2 December 2027: Chapter III Sections 1-3 for Annex III high-risk systems (Article 6(2)) - moved from 2 August 2026,
- from 2 August 2028: Chapter III Sections 1-3 for Annex I high-risk systems (Article 6(1)) - moved from 2 August 2027,
- by 2 August 2030: high-risk systems intended for use by public authorities that were on the market before the Chapter III date (Article 111(2)).

Build the map: role and classification determine the applicable chapters and articles, and from when.

FRIA signal (Article 27(1)): the trigger has two conditions, and both go on the card. (1) The system is a high-risk system under Article 6(2) (Annex III) - an Annex I (Article 6(1)) system does not trigger a FRIA, and neither does a system in the area of Annex III point 2 (critical infrastructure). (2) The deployer is either a body governed by public law or a private entity providing public services, or - whatever its nature - a deployer of a system under Annex III point 5(b) (creditworthiness or credit scoring, except systems used to detect financial fraud) or point 5(c) (risk assessment and pricing in life and health insurance). Where the DPIA under Article 35 GDPR, or the assessment under Article 27 of Directive (EU) 2016/680, already meets part of the FRIA, the deployer may cross-reference or include those sections (Article 27(4) as replaced by Regulation (EU) 2026/1744). The workflow signals the requirement and flags the DPIA overlap; it does not perform the FRIA.

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

The provision comes from a database, not from memory. Hard rules: every article, paragraph, point, and Annex number cited on the card must be verified in-session in EUR-Lex against the consolidated version (02024R1689-20260727, or a later consolidated version if one exists - never the 2024 original, CELEX 32024R1689), otherwise it carries the [check in EUR-Lex] tag; a [TO VERIFY] tag in this workflow marks a spot where a number or document status requires verification before use; a "the AI Act does not apply to us" determination can never rest on an unverified provision; the consolidated version takes precedence over memory of the original text - regulations get corrected by corrigenda.
