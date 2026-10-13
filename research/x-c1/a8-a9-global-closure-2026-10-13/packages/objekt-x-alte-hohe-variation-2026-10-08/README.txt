Objekt X — zwölf alte hohe Variationsfunktionen, 8. Oktober 2026

Ergebnis und Grenzen: BERICHT.txt. Herleitung: HERLEITUNG.txt.
Rationaler Schluss: EXACT_CHECK.json. Alle Dateien: MANIFEST.json.

Schneller Replay, nur Python-Standardbibliothek:
    python reproduce.py

Algebra erneut auswerten, python-flint 0.9.0 erforderlich:
    python reproduce.py --recompute-algebra --destination /frischer/pfad

Auch alle vier neuen Integrationsläufe wiederholen:
    python reproduce.py --recompute-integrals --destination /frischer/pfad

Der Zielordner muss neu sein. Bestehende Resultate bleiben erhalten.
Die Integrationen verwenden 3072 und 4096 Bit. Die Variationsauswertung
verwendet 1536 Bit; der U00-Nachlauf 1024 bzw. 1536 Bit.

Dieses Paket enthält die benötigten ausgewählten Quellinputs und Helfer,
aber keine erneute Herleitung der gesamten alten A8/A9-Operatoridentitäten.
PROVENIENZ.json bindet die vollständigen Vorgängerarchive per SHA-256.
Die zugelieferte Gegenprüfung betrifft den Vorgänger, nicht diesen neuen
Variationslauf. Ihre Linux-Aussage ist ein Befund des übermittelten Berichts.
