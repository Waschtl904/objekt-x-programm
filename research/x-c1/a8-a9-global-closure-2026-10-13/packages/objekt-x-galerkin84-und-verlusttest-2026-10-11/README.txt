Objekt X — Galerkin84 und gemeinsamer Verlusttest

Start: BERICHT.txt und ANSCHLUSS_GPT1.txt. Beweisdetails: HERLEITUNG.txt.
Die Matrixgrößen, Zeilenbedeutungen und Fehlerfelder erklärt DATENFORMAT.txt.
BRIDGE_DIAGNOSTIC.json enthält ausdrücklich bedingte endliche Zielwerte
für eine stärkere Achterbrücke, keinen Beweis dieser neuen Brücke.

Schneller Replay mit Python 3 und ausschließlich Standardbibliothek:
  python reproduce.py

Er prüft sämtliche Paketbindungen und die neuen rationalen Zertifikate.
Die ursprünglichen großen Integrationen werden hierbei nicht erneut
ausgeführt. REPLAY.json dokumentiert diesen Umfang ausdrücklich.

Eine neue vollständige Matrixintegration nach dem Replay:
  python calculate.py --parity even --out recalculated-even
  python calculate.py --parity odd --out recalculated-odd

Benötigt Python 3.12 mit python-flint, NumPy und SciPy. Auf dem Autoren-
rechner: python-flint 0.9.0, NumPy 2.5.3, SciPy 1.18.1. Optional:
  --deps PFAD_ZUM_BIBLIOTHEKSORDNER
Die beiden Paritäten sollten auf Rechnern mit knappem Speicher
nacheinander ausgeführt werden. Abgeschlossene hohe und gemischte
Integrationsphasen werden unter dem gewählten Ausgabenamen gesichert.
Die gemischte Phase speichert außerdem nach jeweils acht logarithmischen
Kraftspalten und nach jeder Primverschiebungszelle einen Zwischenstand.
COMPARISON.json prüft die neuen Hauptmatrizen gegen die Paketdaten.

GALERKIN_*.json enthält gerichtete Modellmatrizen, zusätzliche analytische
Fehler, die feste rationale Matrix X, M und die rationale Prüfrichtung.
WITNESS_*.json enthält die davon getrennte vollständige Einzelintegration
bei höherer Präzision. MODEL_RAY_*.json bindet ihre Arbeitskoeffizienten
exakt an die rationale Linearkombination der Matrix-Arbeitsmittelpunkte.
Die tatsächliche Prüffunktion bleibt r=Jw. Die Quellprogramme für beide
Wege sind enthalten.
RESIDUAL_BUDGET.json enthält eine grobe volle L-formduale Restobergrenze
und das tatsächlich benötigte Budget; es behauptet keinen scharfen Gram.

Die 203 Zeilen von C84 gehören ausschließlich zur gemeinsamen
Verlustbilanz. FULL_REMAINDER_CERTIFIED=false. EXTERNAL_REVIEW_OPEN.
