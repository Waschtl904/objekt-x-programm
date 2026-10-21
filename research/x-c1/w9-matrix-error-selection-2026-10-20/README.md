# Ein begründeter neuer K-Kandidat

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.** Die Auswahl ist abgeschlossen;
der gerichtete Energiepilot ist offen.

Der vorhandene vollständige F-Fehlergram erlaubt eine matrixwertige
Young-Abschätzung. Die daraus rational gebildete Untergrenze erfüllt
K_new>K_star und K_new<=K_actual. Damit wird eine Voraussetzung des festen
Ausschlusses aus #239 geändert. Die vollständige Restschranke bleibt durch
Monotonie verwendbar; neue Integrationen sind dafür nicht nötig.

Ein festes zulässiges Gewichtspaar liefert im Modell einen Spielraum von
etwa 0.3225e-6 vor zusätzlichen Fehlern und Dualterm. Das ist keine
gerichtete Reserve und kein Teilpass. Die alten Gewichte liegen im Modell
weiter über dem Budget. Der allgemeine Antwortmatrixweg bleibt offen,
wird hier aber wegen fehlender gewichteter Kreuzdaten zurückgestellt.

Siehe [Herleitung und festes Pilotprotokoll](PROOF.md),
[vorab festgelegte Abnahme](ACCEPTANCE_PLAN.md) und [Ergebnisse](EXPECTED.json).

Prüfen mit Python und python-flint==0.9.0:

```text
python verify.py --check
python audit.py
```

Der Replay erneuert keine historische Integration und zertifiziert keine
neue P-Obermatrix oder tatsächliche Teilenergie. Eine volle A9→A11-Fortsetzung
braucht weiterhin beide Paritäten und den gesamten Rest.
