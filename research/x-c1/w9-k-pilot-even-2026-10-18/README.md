# Ein gerader K-Pilot: Vergleich weiterhin ausgeschlossen

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** unter den gebundenen Voraussetzungen.

Die festgelegte Änderung K_* = K+(13/10^8)G_F wurde gemeinsam mit E_*, P_*,
nu_* und allen betroffenen Fehlern ausgeführt. Alle 287 rationalen
Schurblock-Pivots sind positiv. Die neue Teilenergie liegt mindestens
2.91535e-6 über dem unveränderten K_P-Budget:
`PILOT_COMPARISON_EXCLUDED`.

[Herleitung und Aussagegrenze](PROOF.md), [exakte Ergebnisse](RESULT.json),
[rationale neue Matrizen](SCHUR.json.gz), [Abnahmeplan](ACCEPTANCE_PLAN.md),
[Abnahmequittung](ACCEPTANCE.json).

Aus dem Repository-Wurzelverzeichnis, mit Python und python-flint 0.9.0:

```sh
python research/x-c1/w9-k-pilot-even-2026-10-18/verify.py --check
```

Der Replay baut beide Ergebnisdateien vollständig neu auf und verlangt
Bytegleichheit. Keine neue Integration, RL-Rechnung oder Richtungssuche.
Die harte Laufzeitgrenze ist 30 Minuten pro vollständigem Aufruf.

Nur diese Kombination aus K-Schritt, Majorante und eingefrorener Antwort
scheitert am festen Zeugen. Keine negative Weil-Richtung, kein allgemeines
Majoranten-No-Go, kein N12-/Meilenstein-4-Abschluss. Kein Merge.
