# Gerichtete Prüfung zweier festgefrorener Schalenrichtungen

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, unter den gebundenen Operator-, Domänen- und Quellenvoraussetzungen. Je Parität wird ausschließlich der zuvor im separaten Kandidatenpaket ausgewählte Grad-11-Kandidat geprüft.

| Parität | vollständiges Intervall für L(c) | Einschließung der gewählten Schwelle τ(c) | Ergebnis |
|---|---:|---:|---|
| gerade | [−12,293; 15,280] | [1014,219; 1014,220] | DOES_NOT_EXCLUDE_FOR_DIRECTION |
| ungerade | [118,635; 186,422] | [474,717; 474,718] | DOES_NOT_EXCLUDE_FOR_DIRECTION |

Beide Nichtausschlüsse beziehen sich auf den Test mit der angegebenen **K_P-Obermajorante**. Eine schärfere Budgetrechnung kann einen anderen Test ergeben. Weder die feste Regel noch N12 sind damit bestätigt oder abgeschlossen.

Die eingefrorenen rationalen Rohkoeffizienten werden exakt W-normiert; die gerichtete Rechnung optimiert weder Richtung noch Translationsschnitt. I₀ enthält alle Koeffizienten-, Fhat-/T-, Quadratur- und Endpunktreste. Der ganze hohe Anteil bleibt symmetrisch um I₀ bezahlt. Neu ist ein analytisch bezahlter Taylorrest der polynomialen Gamma-Kopplung.

[Vollständige zusätzliche Herleitung und Fehlerbudget](PROOF.md).

```sh
python -m pip install -r research/x-c1/frozen-shell-direction-certificates-2026-10-17/requirements.txt
python research/x-c1/frozen-shell-direction-certificates-2026-10-17/verify.py
```

Pflichtprüfung: Hashbindungen, feste Kandidaten, beide vollständigen gerichteten Läufe, bytegleiche Ergebnisse, richtungsabhängige Schwellen, Registry. Replay bestätigt Implementierungsreproduktion; externe mathematische Prüfung bleibt offen.
