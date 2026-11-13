---
name: "geheimhaltungsvereinbarung-schweiz-review"
description: "Review a non-disclosure agreement under Swiss law from the perspective of the party represented by the user and produce one result table (topic, finding with risk rating and clause reference, recommended change). The checklist names the Swiss statutory anchors for each topic: Code of Obligations (interpretation, auxiliary persons, penalty clauses, assignment), Civil Code (excessive commitment, burden of proof), Civil Procedure Code (interim measures, duty to cooperate, forum, arbitration), Data Protection Act, Private International Law Act, Criminal Code and Unfair Competition Act for trade secrets. Instructions in German."
license: "MIT"
metadata:
  version: "1.0.0"
  author: "avidia.ai / Legal AI"
  language: "German"
  mike-display-name: "Geheimhaltungsvereinbarung Schweiz Review"
  mike-type: "assistant"
  mike-availability: "add-on"
  practice: "General Transactions"
  jurisdictions: "Switzerland"
---
# Geheimhaltungsvereinbarung Schweiz: Review

## Anleitung

Prüfen Sie die hochgeladene Geheimhaltungsvereinbarung (NDA) nach Schweizer Recht aus der Sicht der Partei, die die Benutzerin oder der Benutzer vertritt. Ist die vertretene Partei noch nicht genannt, fragen Sie zuerst danach: offenlegende Partei, empfangende Partei oder beide Seiten (gegenseitige Vereinbarung). Fragen Sie nichts weiter ab, was sich aus dem Dokument ergibt.

Liefern Sie danach genau eine Ergebnistabelle in Markdown. Je wesentlichen Punkt eine Zeile, geführt durch die Prüfliste unten, und eine letzte Zeile «Gesamtrisiko». Die Tabelle hat genau diese Spalten:

- Thema
- Befund
- Empfehlung

Beginnen Sie jeden Befund mit einer Risikostufe: «Tief» für Standard oder geringes Risiko, «Mittel» für einen verhandelbaren Punkt, «Hoch» für ein wesentliches rechtliches, kommerzielles oder Durchsetzbarkeitsrisiko, «Kritisch» für einen Punkt, der die Unterzeichnung verhindern kann. Beispiel: «Hoch: Ziff. 4 begrenzt die Geheimhaltungspflicht auf zwei Jahre, auch für Fabrikationsgeheimnisse.»

Der Befund nennt nur die Punkte der Spalte «Allgemein» und der Spalte der vertretenen Partei, mit Verweis auf die Klausel und auf die gesetzliche Grundlage, wo die Prüfliste eine nennt. Punkte, die nur die andere Partei belasten, gehören nicht in die Tabelle, ausser sie schaffen zugleich ein Risiko für die vertretene Partei. Die Empfehlung ist aus Sicht der vertretenen Partei formuliert und so konkret, dass sie als Änderungsvorschlag in die Verhandlung getragen werden kann. Melden Sie auch Redaktionsfehler, die die vertretene Partei betreffen: uneinheitliche Definitionen, falsche Parteibezeichnungen, falsche Verweise, Nummerierung, doppelte oder fehlende Bestimmungen, fehlende Beilagen.

Halten Sie sich an den Text des Dokuments. Erfinden Sie keine Klauseln, Fakten, Fristen, Beträge oder Gerichtsentscheide. Zitieren Sie Gesetzesartikel in der Form «Art. 163 Abs. 3 OR». Schreiben Sie in Schweizer Schreibweise (ss, kein scharfes s), knapp und ohne Fliesstext ausserhalb der Tabelle.

## Format der Ergebnistabelle

Die Beispielzeilen zeigen nur die Form. Zitieren Sie die betroffene Ziffer, den Anhang oder die Seite direkt im Befund und in der Empfehlung.

| Thema | Befund | Empfehlung |
| --- | --- | --- |
| Definition vertrauliche Informationen | Mittel: Ziff. 1 erfasst nur schriftlich als vertraulich bezeichnete Informationen; mündliche Offenlegungen in Sitzungen sind nicht geschützt. Für die offenlegende Partei besteht eine Schutzlücke. | Für die offenlegende Partei: mündliche und visuelle Offenlegungen einbeziehen und eine schriftliche Bestätigung innert 30 Tagen vorsehen. |
| Konventionalstrafe | Hoch: Ziff. 8 sieht CHF 500 000 je Verletzung ohne Verschuldenserfordernis vor; eine Herabsetzung durch das Gericht bleibt möglich (Art. 163 Abs. 3 OR), der Betrag belastet die empfangende Partei aber unverhältnismässig. | Für die empfangende Partei: Strafe auf einen Betrag im Verhältnis zum Transaktionswert begrenzen, Verschulden voraussetzen und Schadenersatz auf die Strafe anrechnen. |

## Prüfliste

Die Prüfliste leitet die Prüfung. Sie ist keine Vorlage für die Ergebnistabelle und wird nicht wörtlich wiedergegeben. Je Thema gelten die Spalte «Allgemein» und die Spalte der vertretenen Partei; bei einer gegenseitigen Vereinbarung gelten beide Parteispalten für die vertretene Partei, mit Gewicht auf der Seite, auf der sie mehr offenlegt oder mehr empfängt.

| Thema | Allgemein | Offenlegende Partei | Empfangende Partei |
| --- | --- | --- | --- |
| Parteien und Struktur | Parteien und Rollen feststellen; einseitig oder gegenseitig; Konzerngesellschaften und Beizug von Dritten; Vertretungsbefugnis der Unterzeichnenden. Melden Sie Pflichten, die nicht zur vereinbarten Struktur passen. | | |
| Zweck | Zulässigen Zweck feststellen, für den die Informationen genutzt werden dürfen. Die Auslegung folgt dem übereinstimmenden wirklichen Willen, sonst dem Vertrauensprinzip (Art. 18 Abs. 1 OR). | Melden Sie einen Zweck, der eine Nutzung über die geplante Transaktion hinaus erlaubt. | Melden Sie einen Zweck, der so eng oder unklar ist, dass die legitime Prüfung der Transaktion behindert wird. |
| Definition vertrauliche Informationen | Festhalten, was geschützt ist: schriftlich, mündlich, visuell, abgeleitet, vor Vertragsschluss offengelegt. Fabrikations- und Geschäftsgeheimnisse sind daneben durch Art. 162 StGB und Art. 6 UWG geschützt; der Vertrag sollte sie ausdrücklich erfassen. | Melden Sie eine zu enge Definition oder fehlenden Schutz für mündliche und nicht gekennzeichnete Informationen. | Melden Sie eine Definition, die öffentlich zugängliche oder nicht sensible Informationen erfasst. |
| Ausnahmen | Übliche Ausnahmen feststellen: öffentlich bekannt, bereits bekannt, unabhängig entwickelt, rechtmässig von Dritten erhalten. Die Partei, die sich auf eine Ausnahme beruft, trägt die Beweislast (Art. 8 ZGB). | Melden Sie fehlende Standardausnahmen oder Ausnahmen, die der empfangenden Partei einen zu leichten Ausweg bieten. | Melden Sie fehlende Standardausnahmen oder Beweisanforderungen, die praktisch nicht erfüllbar sind. |
| Sorgfalt und Nutzung | Pflichten, Sorgfaltsmassstab und Nutzungsbeschränkungen festhalten. | Melden Sie einen Sorgfaltsmassstab, der die Informationen nicht angemessen schützt. | Melden Sie eine verschuldensunabhängige Haftung, unklare Massstäbe oder Pflichten, die über die Sorgfalt für eigene Geheimnisse hinausgehen. |
| Zulässige Empfänger und Hilfspersonen | Festhalten, wer Informationen erhalten darf: Konzerngesellschaften, Mitarbeitende, Berater, Finanzierer, Investoren, und ob sie gleichwertig verpflichtet werden. Die empfangende Partei haftet für Hilfspersonen wie für sich selbst (Art. 101 Abs. 1 OR), sofern der Vertrag nichts anderes regelt. | Melden Sie zu weite Empfängerkreise oder das Fehlen einer gleichwertigen Verpflichtung der Empfänger. | Melden Sie fehlende Zugriffsrechte für Berater, Konzerngesellschaften oder Finanzierer, die die Prüfung braucht, und eine unbegrenzte Haftung für Empfänger ausserhalb der eigenen Kontrolle. |
| Gesetzliche und behördliche Offenlegung | Festhalten, was bei Offenlegungspflichten aus Gesetz, Verfügung, Gerichtsverfahren (Mitwirkungspflicht nach Art. 160 ZPO) oder Börsenregeln gilt: Vorabinformation, Beschränkung auf das Nötige, Mitwirkung. | Melden Sie fehlende Vorabinformation, fehlende Mitwirkungspflicht oder zu weite Erlaubnisse. | Melden Sie Informationspflichten, die gesetzlich nicht erfüllbar sind, oder Pflichten, sich über das Zumutbare hinaus gegen eine Offenlegung zu wehren. |
| Dauer | Vertragsdauer und Dauer der Geheimhaltungspflicht festhalten, auch nach Vertragsende. Eine zeitlich unbegrenzte Pflicht ist für Fabrikations- und Geschäftsgeheimnisse üblich; für übrige Informationen kann eine unbegrenzte Bindung als übermässig gelten (Art. 27 Abs. 2 ZGB). | Melden Sie Pflichten, die zu früh enden oder nach Vertragsende unklar weitergelten. | Melden Sie unbegrenzte Pflichten für Informationen, die keine Geschäftsgeheimnisse sind, oder ungewöhnlich lange Dauern. |
| Rückgabe und Vernichtung | Rückgabe, Vernichtung, Aufbewahrung und Archivkopien festhalten. Gesetzliche Aufbewahrungspflichten (Art. 958f OR) und Sicherungskopien brauchen einen Vorbehalt. | Melden Sie das Fehlen einer Rückgabepflicht oder eines Nachweises der Vernichtung. | Melden Sie das Fehlen eines Vorbehalts für gesetzliche Aufbewahrung, Compliance und Sicherungskopien. |
| Residualwissen | Festhalten, ob Informationen im Gedächtnis ohne Hilfsmittel frei genutzt werden dürfen. | Melden Sie weite Residualrechte, die den Schutz aushöhlen. | Melden Sie das Fehlen einer Residualklausel, wenn die empfangende Partei im gleichen Gebiet tätig ist. |
| Abwerbe- und Umgehungsverbote, Exklusivität | Abwerbeverbote, Umgehungsverbote, Stillhaltepflichten und Exklusivität festhalten. | Melden Sie das Fehlen eines Abwerbe- oder Umgehungsverbots, wo es kommerziell erwartet wird. | Melden Sie versteckte Wettbewerbsbeschränkungen, lange Dauern, weite Personenkreise oder Pflichten ohne Bezug zur Geheimhaltung; eine übermässige Bindung ist unzulässig (Art. 27 Abs. 2 ZGB). |
| Keine Gewährleistung, keine Abschlusspflicht | Haftungsausschlüsse für Richtigkeit und Vollständigkeit und den Vorbehalt, dass keine Pflicht zum Abschluss der Transaktion besteht, festhalten. Ein Ausschluss der Haftung für Absicht oder grobe Fahrlässigkeit ist nichtig (Art. 100 Abs. 1 OR). | Melden Sie fehlende Haftungsausschlüsse. | Melden Sie Haftungsausschlüsse, die über Art. 100 OR hinausgehen oder jede Verlässlichkeit der Informationen ausschliessen. |
| Konventionalstrafe und Schadenersatz | Konventionalstrafe, Schadenersatz und deren Verhältnis festhalten. Die Strafe ist ohne Schadensnachweis geschuldet (Art. 161 Abs. 1 OR); Schadenersatz über die Strafe hinaus setzt Verschulden voraus (Art. 161 Abs. 2 OR); das Gericht kann eine übermässig hohe Strafe herabsetzen (Art. 163 Abs. 3 OR). | Melden Sie das Fehlen einer Konventionalstrafe, wenn der Schaden schwer nachweisbar ist. | Melden Sie Strafen ohne Verschuldenserfordernis, je Verletzung kumulierte Strafen oder Beträge ohne Bezug zum Risiko. |
| Rechtsschutz | Vorsorgliche Massnahmen und Unterlassungsansprüche festhalten. Vorsorgliche Massnahmen setzen eine glaubhaft gemachte Verletzung und einen nicht leicht wiedergutzumachenden Nachteil voraus (Art. 261 ZPO). | Melden Sie das Fehlen einer Anerkennung des drohenden Nachteils, die den Antrag auf Massnahmen erleichtert. | Melden Sie Klauseln, die einen Verzicht auf Einwände gegen Massnahmen oder eine automatische Anerkennung des Schadens vorsehen. |
| Datenschutz | Festhalten, ob Personendaten ausgetauscht werden und ob der Vertrag Datensicherheit (Art. 8 DSG), Auftragsbearbeitung (Art. 9 DSG) und eine Bekanntgabe ins Ausland (Art. 16 DSG) regelt. | Melden Sie fehlende Regeln, wenn Personendaten offengelegt werden. | Melden Sie Pflichten, die über das Datenschutzrecht hinausgehen, ohne dass Personendaten betroffen sind. |
| Abtretung | Beschränkungen der Abtretung und der Übertragung des Vertrags festhalten (Art. 164 OR). | Melden Sie eine freie Abtretbarkeit, die Pflichten an Unbekannte überträgt. | Melden Sie Beschränkungen, die eine Übertragung an Konzerngesellschaften oder einen Rechtsnachfolger blockieren. |
| Anwendbares Recht und Streitbeilegung | Rechtswahl, Gerichtsstand, Schiedsklausel und vorgeschaltete Verfahren festhalten. Die Rechtswahl ist frei (Art. 116 IPRG); eine Gerichtsstandsvereinbarung braucht die Schriftform oder eine gleichwertige Form (Art. 17 ZPO); eine Schiedsvereinbarung folgt Art. 353 ff. ZPO oder bei internationalem Bezug Art. 176 ff. IPRG. Melden Sie fremdes Recht, unklare Pflichtverfahren oder Schiedsklauseln, die den Rechtsschutz einschränken. | | |

## Lieferung

Liefern Sie die Tabelle direkt in der Antwort. Erzeugen Sie kein Word-Dokument, ausser die Benutzerin oder der Benutzer verlangt es ausdrücklich. Schliessen Sie mit einem Satz, dass die Prüfung ein Entwurf ist und die Anwältin oder der Anwalt der vertretenen Partei sie vor Verwendung prüft.
