# Begrenzter eta-q-Zusatz am unveränderten Testvektor

Basis: 4e292a178bc3034049eb7abfa0c915a3c2bf815f (#248).
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

Einziger neuer Rechenauftrag: eta q[Jw], eta=10^-10, am bytegleich
übernommenen rationalen CANDIDATE.json aus #248. Die schon gebundenen
D96-Unter-/Obermatrizen enthalten die direkten analytischen Zuschläge.
Nur deren JJ-Blöcke werden ausgewertet. Keine neue Integration, Richtung,
Matrix, Gewichtung oder Wiederholung der historischen Großrechnungen.

Alle bisherigen Endpunkte und Fehlerpreise bleiben unverändert. Zum alten
Inversenergie-Untertest wird ausschließlich die neue untere eta-q-Grenze
addiert. Ausschluss nur bei Untergrenze > Budgetobergrenze; sonst OPEN,
kein Teilpass, keine Reserve. Die obere eta-q-Grenze ist keine obere
Inversenergie. Bei offenem Ausgang wird der noch fehlende variationale
Rest exakt benannt und ein begrenzter nächster Kontrollweg beschrieben.

Pflichtabnahme vor Veröffentlichung:

- Hashgeprüfte Eingabesnapshots einschließlich des Herkunftsarchivs;
  Identität von Testvektor, K_new, physischem Zeugen und Budget.
- Exakte rationale Intervallrechnung und unabhängige Kontrollrechnung
  mit Mittelpunkt/Radius statt vorzeichenbezogener Endpunktauswahl.
- Ein bytegleicher Replay aus einem frischen, ausdrücklich auf dieses
  Paket und seine vollständigen Dateiabhaengigkeiten beschränkten Git-Archiv.
  Das ist kein vollständiges Repository-Archiv und kein Replay der
  historischen Integrationen.
- Negative Kontrollen: Eingabe-/Ergebnistampering, fehlende Eingabe,
  falsches Vorzeichen, unzulässiger Pass/Reserve und Python -O.
- Beweis-/Paketbindungen, Register, erzeugte Ansichten, Active Front,
  Registry-Tests und Diffprüfung. Anwendbare CI separat.

Jeder Rechen-/Replayaufruf ist auf 120 Sekunden begrenzt. Keine automatische
Nachschärfung oder Großrechnung. Punkt 4 und N12 bleiben offen.
