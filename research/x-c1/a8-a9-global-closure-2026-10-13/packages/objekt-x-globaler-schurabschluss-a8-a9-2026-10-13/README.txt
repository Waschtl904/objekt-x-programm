Objekt X — globaler Schurabschluss A8->A9, Gegenprüfung 13. Oktober 2026

Mit BERICHT.txt beginnen. HERLEITUNG.txt enthält den vollständigen neuen
analytischen Anschluss. ASSEMBLY_AUDIT.json enthält die exakten rationalen
Konstanten und die neuen 203x203-LDL-Zertifikate. ANSCHLUSS_GPT2.txt ist
der konkrete Auftrag für die weitere Gegenprüfung.

Das Ergebnis ist bedingt auf die geerbten analytischen Operator-,
Domänen- und vollständigen Raumzerlegungsvoraussetzungen. Der positive
gemeinsame Restvergleich und der Positivitätsübergang A8->A9 sind unter
diesen Voraussetzungen geschlossen. Der gesonderte Tailboden 1/20,
Objekt X und RH sind weiterhin offen. Externe Begutachtung bleibt offen.

Vollständiger rationaler Replay nach frischem Entpacken:

 python -B reproduce.py --receipt EIGENE_PRUEFQUITTUNG.json

Benötigt Python 3.11 oder neuer, ausschließlich die Standardbibliothek.
Alle vier benötigten unveränderten Eingangsarchive liegen in inputs/.
Der Replay prüft Manifeste und Bindungen, entpackt frisch, wiederholt die
globalen Gram-, Antwort-/Common96-, Außenrest- und Logzertifikate und baut
danach die neue endgültige Residualbilanz auf. Die Ausgabequittung und
ihre Protokolle werden am angegebenen Ort angelegt.

Nach bereits geprüftem vollständigem Eingangs-Replay lässt sich nur die
neue Schlussbilanz separat wiederholen:

 python -B reproduce.py --assembly-only --receipt SCHLUSSBILANZ.json

Diese zweite Variante ist ausdrücklich kein erneuter vollständiger
Eingangs-Replay. Die Quittung unterscheidet beide Modi.

FULL_CHAIN_REPLAY.json dokumentiert die hier erneut vollständig
ausgeführte rationale Kette aus frisch entpackten Archiven. logs/ enthält
die Protokolle und die gesondert ausgeführten analytischen Baustein-
kontrollen. Die separate Pruefquittung.json neben dem ZIP dokumentiert
die spätere Prüfung des fertig gepackten Rückgabepakets; deren Modus
ist dort ausdrücklich genannt.

Die großen globalen Integrationen wurden bei dieser Gegenprüfung nicht
erneut erzeugt. Ihre vollständige Wiederholung ist als --rebuild im
unveränderten Grampaket beschrieben und benötigt python-flint 0.9.0.

Der Wrapper replay_responses_portably.py lässt beim alten Vergleich der
generierten PRECISION_CHECK.json ausschließlich CRLF/LF-Unterschiede zu.
Originalarchive, Originalcode und mathematische Daten werden nicht geändert.
Die Normalisierung des einen Vergleichs erfolgt im Arbeitsspeicher.

Nicht mit Python -O starten: Assertions gehören zu den Zertifikaten.
Historische false-Flags in den Vorpaketen sind unveränderte Provenienz;
der neue aktuelle Schluss steht in BERICHT.txt und ASSEMBLY_AUDIT.json.
