Objekt X — Anschlussabgleich und L2-Modellfehlerbudget
12. Oktober 2026

Start: BERICHT.txt, PROOF_REVIEW.txt, ANSCHLUSS_GPT2.txt.

Reproduktion mit Python 3.11+ und Standardbibliothek:

 python -B reproduce_review.py \
  --responses-zip /pfad/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip \
  --boundary-review-zip /pfad/Objekt-X-Randtest-Gegenpruefung-und-globaler-Anschluss-2026-10-12.zip

Das aktuelle Zusatzpaket und unser voriges Logrest-Review sind unverändert
in inputs eingebettet. Die beiden externen Archive werden durch ihre
vollständigen SHA256-Werte gebunden.

Der Prüfer spielt die aktuelle Budgetrechnung neu ab (vier 203er-Tests),
rekonstruiert die zwei zusätzlichen 206er-Matrixvergleiche und rechnet
die L2-Fehlerbedingung für den gerundeten Logabzug rational nach.
Die ursprünglichen analytischen Voraussetzungen und früheren vollen
Quellen-Replays bleiben gebundene Eingaben. Die vollständigen älteren
Replays werden durch diesen Aufruf nicht nochmals ausgeführt.

data/CONSOLIDATION_AUDIT.json enthält die Matrixzertifikate und alle
exakten Fehlerbudgets. data/INPUT_REPLAY.log dokumentiert den ersten
Replay des aktuellen Zusatzpakets.

Der Aufruf berechnet kein globales Residualintegral und keinen tatsächlichen
globalen Modellfehler. Dafür bleiben die beiden linken Seiten von (C5)
in PROOF_REVIEW.txt herzustellen. Nicht mit python -O ausführen.

FULL_REMAINDER_CERTIFIED=false; A8->A9 und Tailboden 1/20 offen.
