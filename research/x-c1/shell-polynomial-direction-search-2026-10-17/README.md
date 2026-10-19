# Kandidatensuche im neuen Schalenraum, Grad ≤ 11

Explorative Rechnung; **keine gerichtete Ausschluss- oder N12-Aussage**. Auf #231 aufgebaut, mit denselben gebundenen Repository-Eingaben. Die gerichtete Prüfung der eingefrorenen Kandidaten ist ein eigenes Paket und ein eigener PR.

| Parität | bester gefundener I₀-Mittelpunkt | grober Radius | richtungsabhängige Schwelle | Marge |
|---|---:|---:|---:|---:|
| gerade | 1,493637 | 13,785992 | 1014,219657 | −1026,512012 |
| ungerade | 152,528516 | 33,893399 | 474,717778 | −356,082661 |

58 deterministische Starts je Parität, physischer Gram mit Kondition 1,113 bzw. 1,315, Whitening, Ranglisten und exakte rationale Rohkoeffizienten in `data/`. Die Normierung gehört zur exakten Richtung; sie wird im späteren Certifier neu eingeschlossen. „Bester“ bedeutet bester gefundener Kandidat, nicht bewiesenes globales Optimum.

Die gegenwärtige grobe Schwelle ist bereits zu groß für die numerische duale Norm der gesamten I₀-Zeile. Weitere Starts mit demselben Budget helfen deshalb voraussichtlich nicht. Dies ist eine Diagnose **dieser Majorante**, kein Ausschluss stärkerer K_P-Budgets, anderer Residualzentren oder der Regel.

[Herleitung, Suchziel und Prüfgrenzen](PROOF.md).

```sh
python -m pip install -r research/x-c1/shell-polynomial-direction-search-2026-10-17/requirements.txt
python research/x-c1/shell-polynomial-direction-search-2026-10-17/verify.py
```

Pflichtprüfungen: Eingabebindungen; z₀-Kontrolle; vollständige 384/512-Knoten-Neuberechnung aller zwölf Richtungen; physischer Gram/Whitening; 58 Suchstarts; sechs unabhängige Gamma-Punktintegrale; Bindung der eingefrorenen Kandidaten. Netzvergleich und Punktkontrollen sind keine gerichteten Integrationsreste.
