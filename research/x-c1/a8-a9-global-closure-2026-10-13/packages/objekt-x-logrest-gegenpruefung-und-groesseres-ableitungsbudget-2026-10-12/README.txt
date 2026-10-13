Objekt X — Logrest-Gegenprüfung und größeres Ableitungsbudget
12. Oktober 2026

Lesereihenfolge: BERICHT.txt, PROOF_REVIEW.txt, ANSCHLUSS_GPT2.txt.

Reproduktion mit Python 3.11+ und Standardbibliothek:

 python -B reproduce_review.py \
  --responses-zip /pfad/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip \
  --common-zip /pfad/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip

Die beiden großen gebundenen Vorgänger-ZIPs werden extern erwartet. Ihre
vollständigen SHA256-Werte werden kontrolliert. Das aktuelle Originalpaket
ist unverändert in inputs enthalten, mitsamt seinem Logrand-Vorgänger.

Der Aufruf führt aus:
1. Manifest und Archive prüfen, Originalpaket frisch entpacken.
2. Den vollständigen rationalen Original-Replay ausführen.
3. Neue Young-Budgets einschließlich Matrixvergleich mit dem bisherigen
   Ziel und der nach unten gerundeten skalaren Alternative neu berechnen.
4. Feste rationale gemeinsame Logobergrame, Modellradien und zwei neue
   206x206-Schurtests rekonstruieren. Die stärkeren richtungsabhängigen
   Ableitungszielmatrizen werden exakt in faktorisierter Form aufgebaut.
5. Beide neu erzeugten JSON-Ergebnisse mit data vergleichen.

Keine python -O-Ausführung: Die assertions sind Teil der Prüfgates.

data/YOUNG_BUDGET_AUDIT.json:
  rationale affine E_theta-Ziele, skalare Budgets, Matrixvergrößerungsbeweis.
data/DIRECTIONAL_DERIVATIVE_TARGET.json:
  vollständige C0-/G-Faktoren und rationale Koeffizienten des noch größeren
  E_dir=alpha*T-b*D-gamma*C0.transpose()*G*C0.
data/INPUT_REPLAY.log:
  Protokoll des ersten hier ausgeführten Original-Replays.

Diese Reproduktion integriert keine neuen Rand- oder Restfunktionen.
Die analytischen Voraussetzungen und die Identifikation des exakt
regularisierten Restes sind zusätzlich mathematisch zu prüfen.

ACTUAL_REGULARIZED_DERIVATIVE_GRAM_COMPUTED=false.
FULL_REMAINDER_CERTIFIED=false.
