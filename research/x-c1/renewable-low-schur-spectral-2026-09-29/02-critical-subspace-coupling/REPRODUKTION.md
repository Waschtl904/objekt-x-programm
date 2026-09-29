# Reproduktion der kritischen Kopplung

## Voraussetzungen

- Ein vorhandener Checkout von `Waschtl904/objekt-x-programm` mit HEAD exakt `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`. Der Prüfer liest diesen Checkout; er wechselt keine Branches und ändert keine Referenzen.
- Python 3.13 und python-flint 0.9.0 für die Intervallrechnung. Der ausgelieferte Rechenlauf wurde unter Windows mit Git unter `C:\Program Files\Git\cmd\git.exe` ausgeführt. Dieser Pfad steht im Rechenskript; auf anderen Systemen muss nur die Variable `git` auf den vorhandenen Git-Pfad gesetzt werden.
- Für `verify_critical_subspace_coupling.py` genügt die Python-Standardbibliothek. Git wird dort automatisch gesucht, mit dem genannten Windows-Pfad als Ersatz.
- Das unveränderte `critical_vectors.json` in diesem Paket. Die Diagnose ihrer ursprünglichen Auswahl gehört zum vorausgehenden Strukturvergleich; hier werden ihre Dezimalwerte als exakte rationale Quellenkoeffizienten fixiert.

## Aufrufe

Im Paketverzeichnis, mit `PFAD_ZUM_REPOSITORY` durch den vorhandenen Checkout ersetzt:

```text
python critical_subspace_coupling.py --repo PFAD_ZUM_REPOSITORY --vectors critical_vectors.json --out replay-primary --bits 1024
python critical_subspace_coupling.py --repo PFAD_ZUM_REPOSITORY --vectors critical_vectors.json --out replay-crosscheck --bits 1280 --quadrature-extra 8
python verify_critical_subspace_coupling.py --primary replay-primary/coupling_bounds.json --crosscheck replay-crosscheck/coupling_bounds.json --vectors critical_vectors.json --repo PFAD_ZUM_REPOSITORY --out replay-verification.json
```

Die gesamten beiden Läufe benötigen auf dieser Maschine zusammen einige Minuten. Die Ausgabe enthält je Übergang und Parität drei Intervalle für **1−κ**. Laufzeitfelder sind nicht deterministisch; für einen Vergleich sind die mathematischen Schranken und Eingabe-Hashes maßgeblich.

Die bereits gelieferten Ergebnisse lassen sich ohne erneute Arb-Rechnung prüfen:

```text
python verify_critical_subspace_coupling.py --primary coupling_bounds.json --crosscheck coupling_bounds_crosscheck.json --vectors critical_vectors.json --repo PFAD_ZUM_REPOSITORY --out replay-verification.json
```

Ohne `--repo` entfallen ausschließlich die elf Git-/Dateibindungen. Die acht rationalen Formeltests, zwölf Intervallvergleiche, Metadaten- und Vektorhashprüfungen laufen weiterhin.

## Was geprüft wird

Die Intervallrechnung vergleicht jede Repository-Eingabe byteweise mit `git show` am festgehaltenen Commit. Der Inputumfang umfasst elf Dateien: je Terminal Modell, Reservebericht und Schur-Untergrenzen sowie die beiden neuen gemeinsamen physischen Reserveberichte. Bei A₈ wird `reserve_refined` verwendet.

Die tatsächlichen alten Quellen werden einschließlich Mellinkorrektur konstruiert. Die alte Form-Grammatrix wird positiv eingeschlossen. Danach werden die neuen niedrigen physischen Projektionen mit gerichteter Gauss-Legendre-Arithmetik ermittelt. Der unendliche duale hohe Anteil wird durch die vollständige Gramidentität erfasst. Unter den vorhandenen Terminalbindungen folgen Resolventen- und Kopplungsschranken.

Die Auswertung liefert **keinen neuen Aufbau der ursprünglichen Terminalmodelle**. Sie setzt deren Form-/Fehlerabschätzungen und Positivitätszertifikate voraus. Auch die unabhängigen rationalen Formeltests ersetzen diese Voraussetzungen nicht.

## Datenformat

- `one_minus_kappa_lower_exact` und `one_minus_kappa_upper_exact` sind die maßgeblichen, nach außen gerundeten rationalen Endpunkte.
- `one_minus_kappa_display` ist nur eine gerundete Anzeige.
- Zusätzliche `display`, `lower` und `upper`-Texte diagnostischer Arb-Größen dienen der Lesbarkeit. Sie ersetzen die exakten rationalen Endpunkte der Hauptergebnisse nicht.
- `new_D_b_metric_floor_exact` enthält den geerbten Boden für D in der b-Norm.
- `D_floor_depends_on_existing_new_terminal_certificate: true` kennzeichnet die wesentliche Abhängigkeit von der bereits bekannten neuen Positivität.

## Abgrenzung

Die Quellräume sind explizite alte rationale Diagnoseräume, keine nachgewiesenen Spektralprojektionen. Weder ein robuster Komplement-Gap noch kleine L²-Graphkorrekturen noch ein beliebig oft wiederholbarer Fortsetzungssatz werden durch dieses Paket behauptet. Repository, Registry und Main bleiben unverändert.
