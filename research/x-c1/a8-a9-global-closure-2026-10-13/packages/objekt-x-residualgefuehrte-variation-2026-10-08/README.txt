Objekt X — residualgeführte alte Variation, 8. Oktober 2026

BERICHT.txt: Ergebnis, Diagnose, Grenzen. HERLEITUNG.txt: Beweisführung.
EXACT_CHECK.json: rationaler Schluss. MANIFEST.json: alle Dateihashes.

Schneller Replay mit Python-Standardbibliothek:
    python reproduce.py

Mit python-flint 0.9.0, Algebra aus dem Paket wiederholen:
    python reproduce.py --recompute-algebra --destination /frischer/pfad

Zusätzlich alle vier Scan- und vier Formläufe wiederholen:
    python reproduce.py --recompute-integrals --destination /frischer/pfad

Der Zielordner muss neu sein. Gefrorene Auswahl und gebundene Originaldaten
bleiben erhalten. Neu integrierte Dateien werden bis auf das Laufzeitfeld
semantisch mit den gespeicherten Eingängen verglichen.
Die Auswahlheuristik wird dabei nicht erneut als Beweisvoraussetzung benutzt:
Jede festgelegte gültige Testfamilie darf variational geprüft werden.

Integrationen: 4096/6144 Bit. Variationsalgebra: 1536 Bit.
U00-Auswertung: 1536/2048 Bit. SELECTION_DIAGNOSTIC.json ist zusätzlich
diagnostisch; es enthält keine unendliche Restschranke.

Das Paket enthält ausgewählte gebundene Quellen, nicht eine neue Herleitung
der gesamten alten A8/A9-Operatoridentitäten. PROVENIENZ.json bindet die
unveränderten Vorgängerarchive. Die übermittelte Gegenprüfung betraf den
Vorgänger; eine Gegenprüfung dieses neuen Pakets bleibt offen.
