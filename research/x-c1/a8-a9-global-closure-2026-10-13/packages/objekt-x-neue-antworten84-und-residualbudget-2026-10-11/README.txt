Objekt X — neue Antworten84 und Residualbudget, 11. Oktober 2026

Lesereihenfolge: BERICHT.txt, PROOF.txt, ANSCHLUSS_GPT1.txt.
RESPONSES_EVEN.json und RESPONSES_ODD.json enthalten die neuen Hauptdaten.
Die Dateien mit _1024 sind die unabhängigen Präzisionswiederholungen.
AUDIT.json ist die rein rationale Prüfquittung; SUMMARY.json die Kurzfassung.

Rationaler Replay mit Standard-Python (keine Zusatzpakete nötig):

python -B reproduce.py --input-zip PFAD/ZUM/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip

Optional zusätzlich den gesamten großen Vorgänger rational wiederholen:

python -B reproduce.py --input-zip PFAD/ZUM/VORGAENGER.zip --full-input-replay

Nicht mit Python -O ausführen: Assertions sind Bestandteil des Prüfers.
Der beigefügte neue Eingangsreview wird separat gebunden und skalar geprüft.
Das 70-MB-Vorgängerarchiv ist nicht erneut eingebettet.

Frischer gerichteter Aufbau aus dem entpackten Vorgänger:
Benötigt python-flint, numpy, scipy. Getestet mit flint 0.9.0,
numpy 2.5.3 und scipy 1.18.1. Keine neue Internetrecherche erforderlich.

python -B compute.py --parent PFAD/ZUM/ENTPACKTEN/VORGAENGER --bits 768
python -B compute.py --parent PFAD/ZUM/ENTPACKTEN/VORGAENGER --bits 1024 --suffix _1024
python -B compare_precision.py
python -B audit.py --parent PFAD/ZUM/ENTPACKTEN/VORGAENGER

Diese Befehle schreiben die erzeugten JSON-Dateien im Skriptordner neu.
Für einen frischen Neuaufbau daher in einer separaten Kopie arbeiten.
Die geerbten Integrationen und analytischen Operatorannahmen bleiben
Eingaben; weder Neuaufbau noch Replay sind ein vollständiger A8->A9-Beweis.
