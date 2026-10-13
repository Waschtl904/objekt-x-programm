Objekt X — Randtest-Gegenprüfung und globaler Anschluss
12. Oktober 2026

Lesereihenfolge: BERICHT.txt, PROOF_REVIEW.txt, ANSCHLUSS_GPT2.txt.

Reproduktion mit Python 3.11+ und ausschließlich Standardbibliothek:

 python -B reproduce_review.py \
   --responses-zip /pfad/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip \
   --parent-zip /pfad/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip

Die beiden großen, unveränderten Vorgängerarchive werden extern erwartet.
Der Prüfer kontrolliert ihre vollständigen SHA256-Bindungen. Das geprüfte
Randtestpaket ist unverändert in inputs enthalten. Der vorige eigene
Logrand-Anschluss liegt dort zusätzlich als gebundene Referenz; dessen
gesamter Replay wird durch diesen Aufruf nicht nochmals ausgeführt.

Der Aufruf prüft das Manifest, entpackt den Randtest frisch, rechnet die
Indikatorgeometrie mit einer getrennten rationalen Rekursion und führt den
vollständigen rationalen Replay des Randtestpakets aus. Dieser umfasst
dessen Antwort-/Außenresidual-Vorgänger. Kein assert mit python -O umgehen.

data/INDEPENDENT_GEOMETRY.json enthält die neuen gerichteten Grenzen.
data/INPUT_REPLAY.log dokumentiert den ersten hier ausgeführten Replay.
Der Prüfer berechnet keine neuen Quellenintegrale und behauptet keine
globale Restobergrenze. Die analytischen Voraussetzungen und Herleitungen
müssen zusätzlich mathematisch geprüft werden.

FULL_REMAINDER_CERTIFIED=false.
