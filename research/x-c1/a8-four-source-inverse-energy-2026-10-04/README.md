# A8→A9: positiver Anschluss von vier Quellen

4. Oktober 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Die neuen Quellen der Grade 2 und 4 beziehungsweise 3 und 5 bestehen den vollständigen alten Schurabzug. Für ihre festen Koeffizienten gelten die rational geprüften Böden

\[
S_{\mathrm{gerade}}\succeq10^{-5}I_2,\qquad
S_{\mathrm{ungerade}}\succeq33\cdot10^{-6}I_2.
\]

Der alte A8-Raum wird vollständig einschließlich seiner unendlich vielen hohen Richtungen berücksichtigt. Die Rechnung verwendet seine nachgewiesene Positivität und die alten Form-/Operatoridentitäten. Neue A9-Gesamtpositivität wird nicht vorausgesetzt. Die gesamte neue Quotientenfamilie und Objekt X bleiben offen.

## Lesen und prüfen

- [Aussage und Beweisbindung](PROOF.md)
- [Vollständiger mathematischer Nachweis](reports/NACHWEIS.md)
- [Ergebnis in verständlicher Form](reports/ERGEBNIS.md)
- [Exakte Schlusszertifikate](reports/expected/INDEPENDENT_ENERGY_CHECK.json)
- [Gerichtete Rechnung](reports/expected/FINAL_GATE.json)
- [Neue Rechenprogramme](code/) und [unveränderte ursprüngliche Hilfsmodule](vendor/)
- [Herkunft und Hashbindungen](SOURCE_BINDINGS.json)
- [Unverändertes vollständiges Rechenarchiv](inputs/ObjektX_A8_Inverse_Energie_2026-10-04.zip)

Das Archiv enthält alle acht numerischen Eingaben, Programme und Ergebnisse. Seine 31 manifestgebundenen Dateien bleiben unverändert. Lesbare Kopien werden beim Replay bytegleich gegen das Archiv geprüft. Die ursprünglichen Berichte bewahren ihren Entstehungsstand, einschließlich „GitHub nicht verändert“. Die aktuelle Integration wird im [Forschungsregister](../../../00-uebersicht/RESEARCH_STATE.yaml) geführt.

## Reproduktion

Vom Repository-Stamm, mit Python 3.13:

```text
python -m pip install -r research/x-c1/a8-four-source-inverse-energy-2026-10-04/requirements.txt
python -B research/x-c1/a8-four-source-inverse-energy-2026-10-04/replay.py --output ../a8-four-source-replay
```

Das Zielverzeichnis muss neu sein und außerhalb des Repositorys liegen. Der Wrapper prüft Archiv, Manifest und lesbare Kopien. Er berechnet die 764 neuen gemischten Paarungen bei **3072 und 4096 Bit**, die alte Schurmatrix und inverse Energie bei 2048 Bit sowie die exakten Schlussprüfungen erneut. Alle numerischen Felder müssen mit den gebundenen Ergebnissen übereinstimmen; lediglich die gemessenen Laufzeiten werden beim Vergleich ausgelassen. Das Archiv und seine Dateien bleiben nach dem Lauf unverändert.

Der Lauf rekonstruiert die neuen gemischten Integrale und Energieabschätzungen. Die ursprünglichen vollständigen A8/A9-Modelle und frühere Grambudgets bleiben gebundene Eingaben. Ein separater Bruchprüfer bestätigt die Schlussminoren und 36 Gamma-Polynomidentitäten; dies ist keine externe analytische Begutachtung.

## Abnahme dieses Integrationspakets

Pflichtprüfungen vor dem Merge:

1. Vollständiger neuer Replay einschließlich beider Präzisionen, Quellbindungen, positiver Schlussminoren und 36 algebraischer Kontrollen.
2. Negativkontrollen für beschädigte Archivbindungen und unerlaubte Entpackpfade; Prüfung des relevanten und irrelevanten CI-Routings.
3. Registry-Konsistenz, deterministisch erzeugte Ansichten und bestehende Registry-Tests.
4. Erfolgreiche anwendbare CI am endgültigen PR-Head; nach dem Merge derselbe Integrationsnachweis am Main-Commit.

Der nächste mathematische Schritt ist eine größere ausdrücklich festgelegte Quellfamilie mit gemeinsamem Fehlerbudget. Für die gesamte Fortsetzung wird zusätzlich eine vollständige Quotienten- und Restabdeckung benötigt.
