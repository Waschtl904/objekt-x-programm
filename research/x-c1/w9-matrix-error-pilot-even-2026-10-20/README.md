# Fester gerader Matrixfehler-Pilot

**PILOT_PARTIAL_PASS · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Der in #245 festgelegte Kandidat besteht unter den gebundenen Voraussetzungen
den gerichteten Teiltest an genau einem geraden Zeugen:

- Teilenergie in `[53.68719767242, 53.90213205365] * 10^-6`.
- K_P in `[54.11716936070, 54.11716937864] * 10^-6`.
- Restbudget größer als `2.15037307060e-7`.
- Für den noch offenen vollständigen Dualterm wäre die ungewichtete
  Energie `< 1.90434988323e-8` hinreichend.

Die neue P-Obermatrix hat 287 positive rationale Pivots. Alle betroffenen
Fehler und die Teilnormgrenze wurden gemeinsam erneuert; alte Paarungen
und vollständige F-J-Fehler werden übernommen.

[Herleitung und Reichweite](PROOF.md), [exakte Ergebnisse](RESULT.json),
[rationale Matrix](SCHUR.json), [vorab festgelegte Abnahme](ACCEPTANCE_PLAN.md),
[Abnahmequittung](ACCEPTANCE.json).

```text
python -B verify.py --check
python -B audit.py
```

Ein Rechenaufruf stoppt nach spätestens 30 Minuten. Keine neue Integration,
keine Suche, keine R_L-Rechnung. Punkt 4, N12 und externe Prüfung bleiben offen.
