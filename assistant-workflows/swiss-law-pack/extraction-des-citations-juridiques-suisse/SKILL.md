---
name: "extraction-des-citations-juridiques-suisse"
description: "Extract every legal citation from a French-language Swiss brief, opinion or judgment by pattern rather than judgement: published Federal Supreme Court decisions (BGE), unpublished decisions by docket number, Federal Administrative and Criminal Court decisions, cantonal decisions, European Court of Human Rights judgments, statutes and ordinances with article, paragraph and letter, SR numbers, official publications (AS, BBl), commentaries and journals. Then normalise, deduplicate and resolve short references (a.a.O., ebd., oben E. 3, loc. cit.) to their antecedents and hand the list over for verification. Use before checking authorities, before a brief leaves the firm, or when asked what a text cites. Instructions in French."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "French"
  mike-display-name: "Extraction des citations juridiques Suisse"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "Legal Research"
  jurisdictions: "Switzerland"
---
# Extraction des citations d'une écriture (Suisse)

Une référence ne peut être vérifiée que si elle a d'abord été trouvée. Ce workflow parcourt le texte et liste chaque autorité citée, afin qu'aucune n'échappe à la vérification. Une référence manquée est une référence non vérifiée.

L'extraction est mécanique : selon des modèles et des règles, non selon l'appréciation. Une lecture libre pourrait manquer une référence ou en inventer une.

## Trois étapes

1. Extraction : reconnaître et saisir chaque référence selon les modèles ci-dessous.
2. Regroupement : rattacher les renvois abrégés (op. cit., ibid., idem, eadem, «supra consid. 3», loc. cit.) à leur antécédent selon les règles ci-dessous, afin qu'ils comptent comme une seule référence et non comme plusieurs.
3. Remise : transmettre la liste structurée à la vérification : l'autorité existe-t-elle, et dit-elle ce que le texte affirme ?

## Modèles de citation

### Jurisprudence fédérale
- Décisions publiées du Tribunal fédéral : `ATF 145 III 72 consid. 3.2 p. 75` (volume, section I à V, page, considérant, page de référence) ; forme plus ancienne `ATF 120 II 35`.
- Décisions non publiées du Tribunal fédéral : `arrêt du Tribunal fédéral 4A_123/2020 du 12 mars 2021 consid. 2.1`, aussi `TF 4A_123/2020`, `arrêt 5A_456/2019`, `arrêt du Tribunal fédéral 5A_456/2019` ; forme plus ancienne `4C.123/2004`. Le numéro de procédure se compose de l'abréviation de la cour, d'un numéro courant et de l'année.
- Tribunal administratif fédéral : `arrêt du TAF A-1234/2020 du 1er juillet 2021 consid. 4` ; forme publiée `ATAF 2019 I 5`.
- Tribunal pénal fédéral : `arrêt du TPF SK.2020.12 du 3 mai 2021` ; forme publiée `TPF 2018 12`.
- Recueil de pratique : `Pra 2010 n° 12`.

### Jurisprudence cantonale
- Décision avec tribunal, numéro d'affaire et date : `arrêt de la Cour de justice de Genève ACJC/123/2020 du 4 février 2020 consid. 3`, `Tribunal cantonal vaudois HC/2020/123`, `Tribunal cantonal de Neuchâtel CACIV.2019.45`, `Tribunale d'appello TI 12.2019.45`, `Handelsgericht Zürich HG180123-O`.
- Recueils cantonaux : `SJ 2019 I 123`, `JdT 2020 II 45`, `RVJ 2018 p. 200`, `RJN 2019 p. 100`.

### Juridictions européennes et internationales
- Cour européenne des droits de l'homme : `arrêt de la CourEDH n° 12345/09 du 5 juin 2015, Nom c. Suisse, § 42`.
- Cour de justice de l'Union européenne, lorsqu'elle est citée : `CJUE, aff. C-123/20`, `ECLI:EU:C:2020:559`.

### Textes normatifs
- Actes fédéraux avec abréviation : `art. 335c al. 1 let. a CO`, `art. 8 CC`, `art. 261 al. 1 CPC`, `art. 162 CP`, `art. 29 al. 2 Cst.`, `art. 6 LPD`, `art. 9 LTr`, `art. 116 LDIP`, `art. 6 LCD` ; avec chiffre `art. 698 al. 2 ch. 4 CO` ; mentions multiples `art. 340 ss CO`, `art. 97 et 101 CO`.
- Recueil systématique : `RS 220`, `RS 210`, `RS 272` ; ordonnances `art. 26 OLT 3`, `art. 3 OPDo`.
- Actes cantonaux, souvent avec paragraphe : `§ 12 al. 1 GOG ZH`, `art. 15 LiCCS BE`, `LS 211.1`.
- Publications officielles : `RO 2022 109`, `FF 2017 399`, `Message du 23 novembre 2016, FF 2017 399, 450`.
- Traités internationaux : `art. 6 par. 1 CEDH`, `art. 5 al. 1 CLug`, `art. 23 CLaH 70`.

### Doctrine
- Commentaires : `CR CO I-Auteur, art. 340 N 5`, `BSK OR I-Autor, Art. 340 N 5` (exemple de commentaire alémanique), `ZK-Autor, art. 18 CO N 12`, `BK-Autor, art. 8 CC N 30`, `OFK-Autor, art. 257d CO N 3`, `KUKO OR-Autor, art. 163 N 2` ; le `Commentaire romand` se cite sous la forme `CR CO I-Auteur`.
- Monographies et articles : `Auteur, Titre, édition, lieu année, n. 123` ou `p. 45` ; revues `SJ 2020 p. 123`, `AJP/PJA 2019 p. 456`, `RJB 2018 p. 100`, `RSDA 2021 p. 50`, `recht 2020 p. 10`, `Jusletter du 3 février 2020`, `RDS 2019 I 200`.

## Regroupement des renvois abrégés

Les renvois abrégés suivent des règles différentes et ne doivent pas tous être rattachés à l'antécédent le plus proche :

- `ibid.`, `loc. cit.`, `op. cit.` sans complément : renvoient à l'autorité qui précède immédiatement.
- `op. cit.`, `préc.` avec complément portent souvent un indicateur qui l'emporte sur la proximité : un nom d'auteur, une partie du titre ou un numéro de note («Müller, op. cit., n. 12» ; «préc. n. 14»). Résolvez d'abord selon l'indicateur ; seulement pour un simple renvoi abrégé, selon la proximité.
- `idem`, `eadem` : même auteur que dans la référence de doctrine qui précède.
- Renvois à l'intérieur du texte (`supra consid. 3.2`, `cf. ch. 12`, `n. 45`) : à un passage du document lui-même, non à une autorité ; signalez-les comme «renvoi interne» et ne les reprenez pas dans la liste à vérifier.
- Formes descriptives («l'arrêt cité», «la disposition mentionnée») : rattachez selon les caractéristiques décrites (tribunal, parties, objet), non seulement selon la position.

Si plus d'un antécédent convient, ou aucun, marquez le renvoi **non résolu, à vérifier manuellement** plutôt que de deviner : un regroupement erroné fond deux autorités en une seule sans que l'on s'en aperçoive. Chaque renvoi résolu compte comme la même référence que son antécédent ; notez où il apparaît.

## Normalisation

- ATF : `ATF volume section page consid. considérant` sans page de référence ; section en chiffre romain.
- Arrêts non publiés du Tribunal fédéral : `arrêt numéro de procédure du date consid. considérant` avec la date en toutes lettres.
- Textes normatifs : `art. numéro al. numéro let. lettre abréviation` ; complétez le numéro RS lorsque le texte le mentionne ou que l'abréviation est univoque (CO RS 220, CC RS 210, CPC RS 272, CP RS 311.0, Cst. RS 101, LPD RS 235.1, LDIP RS 291, LTr RS 822.11, LCD RS 241).
- Doctrine : `Auteur, ouvrage, lieu année, référence` ; commentaires sous la forme `abréviation du commentaire-Auteur, art. numéro loi N numéro marginal`.

## Format de sortie

Un tableau numéroté avec les colonnes : N°, Type (Tribunal fédéral publié, Tribunal fédéral non publié, autres décisions fédérales, cantonal, CourEDH, texte normatif, publication officielle, doctrine), Citation (normalisée), Occurrence (page, numéro marginal ou note), Antécédent (pour les renvois abrégés), Statut (saisi, non résolu, aucun identifiant). Terminez par la liste des références à vérifier, groupées par type, et par les lieux où la vérification a lieu : arrêts du Tribunal fédéral sur bger.ch, textes normatifs sur fedlex.admin.ch, décisions cantonales dans les bases de données de jurisprudence des cantons.

## Limites

- L'extraction saisit les références sous une forme connue. Un renvoi descriptif sans identifiant («la pratique du Tribunal fédéral en matière de prohibition de concurrence») n'a rien à faire correspondre ; marquez-le «aucun identifiant, à vérifier manuellement».
- Il ne s'agit pas d'une vérification d'existence : le workflow indique ce qui est cité, non si la référence existe ou si elle étaye ce qui est affirmé.
- Les modèles couvrent les formes usuelles de la Suisse romande ; les formes alémaniques (BGE, E., Art. ... OR) et italiennes (DTF, consid., art. ... CO) sont reconnues lorsqu'elles figurent dans un texte français, mais le traitement complet est assuré par le workflow allemand de ce pack. Une manière de citer inhabituelle peut passer entre les mailles. En cas d'enjeu élevé, vérifiez en outre à la main.

## Provenance

La structure en trois étapes (extraction, regroupement, remise) suit le workflow «Legal Citation Extraction» de cette collection (MIT, Wieslaw Mazur / MateMatic Solutions), qui cite lui-même le modèle de conception d'eyecite (Free Law Project, BSD-2-Clause). Les modèles de citation suisses, la normalisation et les règles pour les renvois abrégés sont un travail propre d'avidia.ai / Legal AI. Aucun code n'a été repris.
