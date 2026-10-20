# Ganzer Restanschluss: vorhandener Kontrollweg zu grob

**UPPER_CONTROL_ROUTE_TOO_COARSE — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.**

1. F(Jw) liegt in [53.19429074226; 54.47525080963]e-6.
   Der obere Endpunkt überschreitet Budget_lo um etwa 0.358081448914e-6.
   Die gemeinsame D/U-Formfehlerhülle dominiert. Kein Platz für eine
   positive Restobergrenze in dieser Abschätzung.
2. X_ans u=w ist exakt lösbar, Rang 84. Aber schon die günstigste
   E_new-gewichtete Darstellung kostet etwa 5.78117e40. Ihr vorhandener
   vollständiger R-Transportpreis beträgt etwa 2.53568e37.
   Das sind Abschätzungspreise, keine gemessenen Restenergien.
3. Der zertifizierte Formboden kappa>3.24380497686e-6 führt mit diesem
   F_up auf eine negative erforderliche obere Residualenergie. Der
   vollständige obere Vergleich ist auf diesem Weg nicht erreichbar.

Keine neue Integration, physische Richtung oder automatische Folgerechnung.
Kein Ausschluss der Unterform; Punkt 4, N12 und externe Prüfung bleiben offen.
Der nächste Auftrag müsste eine konkrete gemeinsame Verbesserung der
F-Hülle und der vollständigen Residualkontrolle begründen.

[Herleitung, fehlende gemeinsame Daten und Stopplinie](PROOF.md) ·
[Abnahmeplan](ACCEPTANCE_PLAN.md) · [Abnahme](ACCEPTANCE.json).

Python mit python-flint 0.9.0:

```text
python -B research/x-c1/w9-rest-feasibility-even-2026-10-20/verify.py --check
python -B research/x-c1/w9-rest-feasibility-even-2026-10-20/audit.py
```
