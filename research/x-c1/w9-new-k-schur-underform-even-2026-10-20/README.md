# K_new: Gewichtsfrage entschieden, Schur-Untertest offen

Unter den gebundenen Voraussetzungen:

- **YOUNG_WEIGHT_FAMILY_EXCLUDED:** jede zulässige Gewichtung der festen
  Familie kostet >65.23831878691e-6 bei Budget <54.11716937864e-6.
- **SCHUR_LOWER_TEST_OPEN:** ein einzelner rationaler Test an der tatsächlich
  geänderten Unterform liefert >53.19341255729e-6 als Inversenergieuntergrenze.
  Damit folgt weder ein Klassenausschluss noch ein Teilpass oder eine Reserve.

Derselbe physische Zeuge und dieselbe Antwortregel; vorhandene Paarungen und
Fehlergrame wiederverwendet. Keine Gewichtssuche und keine neue Integration.
Vor einer oberen Großrechnung fehlt eine quantitative Kontrolle der noch
offenen Beiträge. Keine weitere Variante wurde begonnen.

[Herleitung und Aussagegrenzen](PROOF.md) · [Gewichtslemma](WEIGHTS.json) ·
[Schur-Ergebnis](RESULT.json) · [Eingefrorener Testvektor](CANDIDATE.json) ·
[Abnahmeplan](ACCEPTANCE_PLAN.md) · [Abnahmequittung](ACCEPTANCE.json)

```text
python -B verify.py --check
python -B audit.py
```

AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.
Punkt 4, N12 und Objekt X bleiben offen.
