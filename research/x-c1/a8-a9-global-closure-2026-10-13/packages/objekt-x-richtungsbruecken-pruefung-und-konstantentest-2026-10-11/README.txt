Objekt X — Richtungsbrücken-Prüfung und Konstantentest, 11. Oktober 2026

BERICHT.txt enthält Ergebnisse, Herleitung und den präzisierten nächsten
Rechenauftrag. Es wird kein Abschluss des unendlichen Rests behauptet.

Eigenständige Reproduktion mit Python 3, ausschließlich Standardbibliothek:

  python -B reproduce.py

Das Skript prüft alle Manifestbindungen, entpackt den mitgelieferten
unveränderten Eingang, führt dessen rationalen Replay aus und berechnet
anschließend die eigenen Gegenzeugenkontrollen neu. Die neue Quittung
muss mit INDEPENDENT_CONTROL.json übereinstimmen.

Die übergebenen analytischen Operatorvoraussetzungen werden nicht durch
einen rationalen Replay bewiesen. Ebenso führt dieser schnelle Replay
keine frische Operatorintegration aus. Die vier hier tatsächlich frisch
ausgeführten Integrationen sind in FRESH_REBUILD_REVIEW.json dokumentiert.
Sie können mit dem Originalskript rebuild_from_parent.py im enthaltenen
Eingangspaket und dessen gebundenem großen Vorgänger erneut ausgeführt
werden. Dafür werden python-flint 0.9.0, numpy und scipy benötigt.

Die zusätzliche Konstantenschranke wird dagegen vollständig rational
neu hergeleitet: inklusive Reihenresten und EulerGamma-Untergrenze.

AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN
