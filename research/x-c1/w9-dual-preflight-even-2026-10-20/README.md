# Dual-Vorprüfung am unveränderten geraden Zeugen

**FULL_FIXED_COMPARISON_EXCLUDED_BY_DUAL_LOWER**

Unter den gebundenen Voraussetzungen ist die gesamte ausgewählte
Vergleichsenergie **> 69.15149379521e-6**, das Budget **< 54.11716937864e-6**.
Der Abstand ist **> 15.03432441658e-6**.

Bereits die fehlerkontrollierte variationale Basis84-Untergrenze des
vollständigen Dualterms entscheidet den Vergleich. Keine obere
Dualeinschließung und keine neue Restintegration sind dafür nötig.
Der Teilpass aus #246 bleibt korrekt; sein ausgelassener Dualanteil
überschreitet den verbleibenden Spielraum.

[Herleitung und genaue Reichweite](PROOF.md) ·
[Rationale Ergebnisse](EXPECTED.json) ·
[L-Obermatrix](L_UPPER.json) ·
[Abnahmeplan](ACCEPTANCE_PLAN.md) · [Quittung](ACCEPTANCE.json)

```text
python -B verify.py --check
python -B audit.py
```

Keine neue Variante, keine Suche, keine neue Integration. Kein Ausschluss
der tatsächlichen A9-Inverse oder aller Majoranten der neuen Unterform.
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN. Punkt 4 und N12 bleiben offen.
