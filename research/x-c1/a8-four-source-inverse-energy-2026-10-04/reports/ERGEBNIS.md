# Vier Quellen bestehen den vollständigen alten Energieabzug

4. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

Der nächste Test ist ausgeführt und in beiden Paritäten positiv. Für die beiden neuen A9-Quellen der Grade 2 und 4 sowie der Grade 3 und 5 bleibt eine positive Reserve erhalten, nachdem die günstigste Antwort aus dem **gesamten alten A8-Raum** berücksichtigt wurde. Das schließt dessen unendlich viele hohe Richtungen ein.

Für die jeweilige Koeffizientenmatrix des exakten Schurrests gilt, unter den dokumentierten alten Formraum- und Operatoridentitäten:

\[
S_{\mathrm{gerade}}\succeq\frac{1}{100000}I_2,
\qquad
S_{\mathrm{ungerade}}\succeq\frac{33}{1000000}I_2.
\]

Diese Zahlen sind durch exakte rationale Hauptminoren geprüft. Sie beziehen sich auf die festgelegten zwei neuen Quellkoeffizienten je Parität. Es sind keine bereits umgerechneten globalen physischen oder T-Reserven.

Anschaulich: Die vier neuen Quellen kosten mehr positive Energie, als die vollständige alte Antwort ihnen abziehen kann. Damit können diese vier Quellen positiv an den alten Raum angeschlossen werden.

## Was gegenüber dem vorherigen Stand neu ist

Die vorangegangene Rechnung zeigte deutliche vollständige Funktionsreste der vier alten Näherungslösungen. Ihre bloße Größe entschied noch nicht, ob sie die Fortsetzung verhindern. Jetzt wurde ihre **inverse alte Energie** nach oben eingeschlossen und mit der verbleibenden Formenergie verglichen.

Die entscheidende neue Rechnung sind 764 gemischte Paarungen zwischen der vollständigen hohen Wirkung der neuen Quellen und der alten Kopplung. Sie bewahren die gemeinsame Wirkung der niedrigen und hohen alten Anteile. Der globale winzige alte Reserveboden wäre hier als alleinige Abschätzung zu grob.

| Parität | Sicherer rationaler Boden | Zusätzlich berechnete det/trace-Untergrenze, gerundet |
| --- | ---: | ---: |
| Gerade, Grade 2 und 4 | 0,000010 | 0,0000103266218031 |
| Ungerade, Grade 3 und 5 | 0,000033 | 0,0000338412378435 |

Die angegebenen rationalen Böden gelten schon bei getrennter Einschließung von Restform und inverser Residualenergie. Eine zusätzliche Ausnutzung ihrer exakten algebraischen Korrelation ist für dieses positive Ergebnis nicht erforderlich.

## Prüfungen

- Neue gemischte Paarungen mit gerichteter Arb-Arithmetik bei 3072 und 4096 Bit berechnet. Alle gespeicherten numerischen Blöcke sind identisch; ausgegeben wird mit nach außen gerundeten 70 Dezimalstellen.
- Alle 764 niedrigen Quellpaarungen mit den vorhandenen Daten abgeglichen; zusätzlich acht vollständige Gram-Kontraktionen über einen anderen Datenweg kontrolliert.
- Die alte hinreichende Schurmatrix neu aufgebaut: jeweils 191 strikt positive gerichtete LDL-Pivots. Die benutzte inverse Matrix erhält eine eigene Residuumschranke.
- Die beiden Schlusszertifikate mit einem separaten Prüfer ausschließlich über exakte Brüche kontrolliert. Dieser prüft außerdem 36 exakte Polynomidentitäten der neuen Gamma-Integrationsmethode.

Der andere Datenweg teilt ursprüngliche Formeln und Eingangsdaten mit der Hauptrechnung. Die rationalen Schlussprüfungen ersetzen keine unabhängige analytische Begutachtung.

## Reichweite und nächster Schritt

Bewiesen ist eine positive Erweiterung um **diese vier Quellen** relativ zur dokumentierten analytischen Grundlage. Der ganze neue Quotientenraum ist damit nicht abgedeckt. Eine vollständige neue hohe Antwort wurde nicht als Funktion konstruiert; für den Test genügt ihre bewiesene Energieobergrenze.

Für Objekt X ist dies ein konkreter Fortschritt beim konstruktiven Anschluss neuer Quellen. Das primäre Ziel bleibt die gemeinsame intrinsische Prim-/Gamma-Geometrie mit exakter Gram-Identität der vollständigen Form. Objekt X ist weiterhin offen; eine Gesamtpositivität am neuen Endpunkt wurde hier nicht vorausgesetzt.

Der nächste sachliche Arbeitsschritt ist, den positiven Anschluss als Baustein festzuhalten und eine größere, klar definierte Familie neuer Quellen mit demselben Energieverfahren zu untersuchen. Für einen vollständigen Fortsetzungssatz braucht es anschließend eine Abdeckung des gesamten neuen Quotienten samt dessen Rest. Aus vier erfolgreichen Quellen folgt dafür noch kein uniformer Satz.

## Unterlagen

- [Mathematischer Nachweis und Fehlerbudget](NACHWEIS.md)
- [Reproduktion und Dateibedeutung](README.md)
- [Exakte Schlussprüfung](expected/INDEPENDENT_ENERGY_CHECK.json)
- [Gerichtete Energieergebnisse](expected/FINAL_GATE.json)
- [Quellbindungen](SOURCE_BINDINGS.json)

Die Rechnung verwendet den gebundenen Repository-Stand `8e6944406511d8e28dff7c977cb62d641eb45c41`. GitHub und die Repository-Registry wurden in diesem Arbeitsblock nicht verändert.
