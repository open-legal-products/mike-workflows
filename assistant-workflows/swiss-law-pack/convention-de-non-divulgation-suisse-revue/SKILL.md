---
name: "convention-de-non-divulgation-suisse-revue"
description: "Review a non-disclosure agreement under Swiss law from the perspective of the party represented by the user and produce one result table (topic, finding with risk rating and clause reference, recommended change). The checklist names the Swiss statutory anchors for each topic: Code of Obligations (interpretation, auxiliary persons, penalty clauses, assignment), Civil Code (excessive commitment, burden of proof), Civil Procedure Code (interim measures, duty to cooperate, forum, arbitration), Data Protection Act, Private International Law Act, Criminal Code and Unfair Competition Act for trade secrets. Instructions in French."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "French"
  mike-display-name: "Convention de non-divulgation Suisse revue"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Transactions"
  jurisdictions: "Switzerland"
---
# Convention de non-divulgation Suisse: revue

## Instructions

Examinez la convention de non-divulgation (NDA) téléversée selon le droit suisse, du point de vue de la partie que représente l'utilisatrice ou l'utilisateur. Si la partie représentée n'est pas encore indiquée, demandez-le d'abord : partie divulgatrice, partie destinataire ou les deux côtés (convention réciproque). Ne demandez rien de plus de ce qui ressort du document.

Remettez ensuite exactement un tableau de résultats en Markdown. Une ligne par point essentiel, guidée par la liste de contrôle ci-dessous, et une dernière ligne «Risque global». Le tableau comporte exactement ces colonnes :

- Thème
- Constat
- Recommandation

Commencez chaque constat par un niveau de risque : «Faible» pour un standard ou un risque limité, «Moyen» pour un point négociable, «Élevé» pour un risque juridique, commercial ou d'exécution important, «Critique» pour un point qui peut empêcher la signature. Exemple : «Élevé : le ch. 4 limite l'obligation de confidentialité à deux ans, y compris pour les secrets de fabrication.»

Le constat ne mentionne que les points de la colonne «Général» et de la colonne de la partie représentée, avec un renvoi à la clause et à la base légale lorsque la liste de contrôle en indique une. Les points qui ne grèvent que l'autre partie n'ont pas leur place dans le tableau, sauf s'ils créent en même temps un risque pour la partie représentée. La recommandation est formulée du point de vue de la partie représentée et assez concrètement pour être portée à la négociation comme proposition de modification. Signalez aussi les erreurs de rédaction qui touchent la partie représentée : définitions incohérentes, désignations erronées des parties, renvois erronés, numérotation, dispositions en double ou manquantes, annexes manquantes.

Tenez-vous au texte du document. N'inventez ni clauses, ni faits, ni délais, ni montants, ni décisions de justice. Citez les articles de loi sous la forme «art. 163 al. 3 CO». Rédigez de manière concise et sans texte continu en dehors du tableau.

## Format du tableau de résultats

Les lignes d'exemple n'illustrent que la forme. Citez le chiffre, l'annexe ou la page concernés directement dans le constat et dans la recommandation.

| Thème | Constat | Recommandation |
| --- | --- | --- |
| Définition des informations confidentielles | Moyen : le ch. 1 ne couvre que les informations désignées par écrit comme confidentielles ; les divulgations orales lors de séances ne sont pas protégées. Il existe une lacune de protection pour la partie divulgatrice. | Pour la partie divulgatrice : inclure les divulgations orales et visuelles et prévoir une confirmation écrite dans un délai de 30 jours. |
| Peine conventionnelle | Élevé : le ch. 8 prévoit CHF 500 000 par violation sans condition de faute ; une réduction par le juge reste possible (art. 163 al. 3 CO), mais le montant grève de manière disproportionnée la partie destinataire. | Pour la partie destinataire : limiter la peine à un montant proportionné à la valeur de la transaction, exiger une faute et imputer les dommages-intérêts sur la peine. |

## Liste de contrôle

La liste de contrôle guide l'examen. Elle n'est pas un modèle pour le tableau de résultats et ne doit pas être reproduite à la lettre. Pour chaque thème s'appliquent la colonne «Général» et la colonne de la partie représentée ; pour une convention réciproque, les deux colonnes de partie s'appliquent à la partie représentée, en mettant l'accent sur le côté où elle divulgue ou reçoit davantage.

| Thème | Général | Partie divulgatrice | Partie destinataire |
| --- | --- | --- | --- |
| Parties et structure | Déterminer les parties et leurs rôles ; unilatérale ou réciproque ; sociétés du groupe et recours à des tiers ; pouvoir de représentation des signataires. Signalez les obligations qui ne correspondent pas à la structure convenue. | | |
| Finalité | Déterminer la finalité admise pour laquelle les informations peuvent être utilisées. L'interprétation suit la réelle et commune intention des parties, à défaut le principe de la confiance (art. 18 al. 1 CO). | Signalez une finalité qui permet une utilisation au-delà de la transaction prévue. | Signalez une finalité si étroite ou si peu claire qu'elle entrave l'examen légitime de la transaction. |
| Définition des informations confidentielles | Déterminer ce qui est protégé : par écrit, oralement, visuellement, informations dérivées, informations divulguées avant la conclusion du contrat. Les secrets de fabrication et d'affaires sont en outre protégés par l'art. 162 CP et l'art. 6 LCD ; le contrat devrait les couvrir expressément. | Signalez une définition trop étroite ou l'absence de protection pour les informations orales et non marquées. | Signalez une définition qui couvre des informations accessibles au public ou non sensibles. |
| Exceptions | Déterminer les exceptions usuelles : information publique, déjà connue, développée de manière indépendante, obtenue licitement de tiers. La partie qui invoque une exception supporte le fardeau de la preuve (art. 8 CC). | Signalez l'absence d'exceptions standard ou des exceptions qui offrent à la partie destinataire une issue trop facile. | Signalez l'absence d'exceptions standard ou des exigences de preuve pratiquement impossibles à satisfaire. |
| Diligence et utilisation | Consigner les obligations, le standard de diligence et les restrictions d'utilisation. | Signalez un standard de diligence qui ne protège pas suffisamment les informations. | Signalez une responsabilité indépendante de la faute, des standards peu clairs ou des obligations qui vont au-delà de la diligence apportée à ses propres secrets. |
| Destinataires admis et auxiliaires | Consigner qui peut recevoir des informations : sociétés du groupe, collaborateurs, conseillers, financeurs, investisseurs, et s'ils sont soumis à des obligations équivalentes. La partie destinataire répond de ses auxiliaires comme de ses propres actes (art. 101 al. 1 CO), sauf disposition contractuelle contraire. | Signalez des cercles de destinataires trop larges ou l'absence d'engagement équivalent des destinataires. | Signalez l'absence de droits d'accès pour les conseillers, sociétés du groupe ou financeurs dont l'examen a besoin, et une responsabilité illimitée pour des destinataires hors de son contrôle. |
| Divulgation légale et par les autorités | Consigner ce qui s'applique en cas d'obligations de divulgation fondées sur la loi, une décision, une procédure judiciaire (obligation de collaborer selon l'art. 160 CPC) ou des règles boursières : information préalable, limitation à ce qui est nécessaire, collaboration. | Signalez l'absence d'information préalable, l'absence d'obligation de collaborer ou des autorisations trop larges. | Signalez des obligations d'information qui ne peuvent être satisfaites légalement, ou des obligations de s'opposer à une divulgation au-delà de ce qui est raisonnable. |
| Durée | Consigner la durée du contrat et celle de l'obligation de confidentialité, y compris après la fin du contrat. Une obligation illimitée dans le temps est usuelle pour les secrets de fabrication et d'affaires ; pour les autres informations, un engagement illimité peut être jugé excessif (art. 27 al. 2 CC). | Signalez des obligations qui prennent fin trop tôt ou dont la suite après la fin du contrat est peu claire. | Signalez des obligations illimitées pour des informations qui ne sont pas des secrets d'affaires, ou des durées inhabituellement longues. |
| Restitution et destruction | Consigner la restitution, la destruction, la conservation et les copies d'archives. Les obligations légales de conservation (art. 958f CO) et les copies de sauvegarde nécessitent une réserve. | Signalez l'absence d'obligation de restitution ou de preuve de la destruction. | Signalez l'absence de réserve pour la conservation légale, la conformité et les copies de sauvegarde. |
| Connaissances résiduelles | Consigner si les informations retenues en mémoire sans moyens auxiliaires peuvent être utilisées librement. | Signalez de larges droits résiduels qui vident la protection de sa substance. | Signalez l'absence de clause résiduelle lorsque la partie destinataire opère dans le même domaine. |
| Interdictions de débauchage et de contournement, exclusivité | Consigner les interdictions de débauchage, les interdictions de contournement, les obligations de standstill et l'exclusivité. | Signalez l'absence d'interdiction de débauchage ou de contournement là où elle est attendue commercialement. | Signalez des restrictions de concurrence cachées, des durées longues, des cercles de personnes larges ou des obligations sans rapport avec la confidentialité ; un engagement excessif est inadmissible (art. 27 al. 2 CC). |
| Absence de garantie, absence d'obligation de conclure | Consigner les exclusions de responsabilité pour l'exactitude et l'exhaustivité et la réserve selon laquelle il n'existe aucune obligation de conclure la transaction. Une exclusion de la responsabilité en cas d'intention ou de négligence grave est nulle (art. 100 al. 1 CO). | Signalez l'absence d'exclusions de responsabilité. | Signalez des exclusions de responsabilité qui vont au-delà de l'art. 100 CO ou qui excluent toute fiabilité des informations. |
| Peine conventionnelle et dommages-intérêts | Consigner la peine conventionnelle, les dommages-intérêts et leur rapport. La peine est due sans preuve du dommage (art. 161 al. 1 CO) ; des dommages-intérêts au-delà de la peine supposent une faute (art. 161 al. 2 CO) ; le juge peut réduire une peine excessive (art. 163 al. 3 CO). | Signalez l'absence de peine conventionnelle lorsque le dommage est difficile à prouver. | Signalez des peines sans condition de faute, des peines cumulées par violation ou des montants sans rapport avec le risque. |
| Protection juridique | Consigner les mesures provisionnelles et les prétentions en cessation. Les mesures provisionnelles supposent une violation rendue vraisemblable et un préjudice difficilement réparable (art. 261 CPC). | Signalez l'absence d'une reconnaissance du préjudice imminent qui facilite la requête de mesures. | Signalez les clauses qui prévoient une renonciation à s'opposer aux mesures ou une reconnaissance automatique du dommage. |
| Protection des données | Consigner si des données personnelles sont échangées et si le contrat règle la sécurité des données (art. 8 LPD), le traitement par un sous-traitant (art. 9 LPD) et la communication à l'étranger (art. 16 LPD). | Signalez l'absence de règles lorsque des données personnelles sont divulguées. | Signalez des obligations qui vont au-delà du droit de la protection des données sans que des données personnelles soient concernées. |
| Cession | Consigner les restrictions de la cession et du transfert du contrat (art. 164 CO). | Signalez une libre cessibilité qui transfère des obligations à des inconnus. | Signalez des restrictions qui bloquent un transfert à des sociétés du groupe ou à un successeur juridique. |
| Droit applicable et règlement des litiges | Consigner l'élection de droit, le for, la clause d'arbitrage et les procédures préalables. L'élection de droit est libre (art. 116 LDIP) ; une élection de for requiert la forme écrite ou une forme équivalente (art. 17 CPC) ; une convention d'arbitrage suit les art. 353 ss CPC ou, en cas d'élément d'extranéité, les art. 176 ss LDIP. Signalez un droit étranger, des procédures obligatoires peu claires ou des clauses d'arbitrage qui restreignent la protection juridique. | | |

## Remise

Remettez le tableau directement dans la réponse. Ne produisez pas de document Word, sauf si l'utilisatrice ou l'utilisateur le demande expressément. Terminez par une phrase indiquant que l'examen est un projet et que l'avocate ou l'avocat de la partie représentée le vérifie avant son utilisation.
