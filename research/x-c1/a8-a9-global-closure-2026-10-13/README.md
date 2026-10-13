# A8→A9: bedingter globaler Schurabschluss

13. Oktober 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Unter den gebundenen Operator-, Formdomänen- und vollständigen
Raumzerlegungsvoraussetzungen ist der konstruktive Positivitätsübergang
**A8→A9 in beiden Paritäten geschlossen**. Der vollständige unendliche
Formdualrest ist eingeschlossen. Der gesonderte Tailboden 1/20 wird dafür
nicht verwendet und bleibt offen.

| Größe | Gerade | Ungerade |
|---|---:|---:|
| Gesamter Formdualrest relativ zur festen Budgetmatrix | < 0,3954 % | < 0,6967 % |
| Untergrenze des genau bezeichneten reduzierten Schurvergleichs | > 1,3285·10⁻⁶ W_X | > 7,9795·10⁻⁶ W_X |

Die zweite Zeile ist weder ein Boden in der gesonderten Tailmetrik noch eine
uniforme Normschranke des gesamten A9-Raums. Allgemeine Horizontfortsetzung,
vollständige Testklasse, Objekt X, globale Weil-Positivität und RH bleiben offen.
Die analytischen Voraussetzungen benötigen weiterhin externe Begutachtung.

## Einstieg

- [Beweisanschluss und genaue Voraussetzungen](PROOF.md).
- [Chronologie einschließlich verworfener Ansätze und Korrekturen](CHRONOLOGY.md).
- [Alle Originalpakete und lesbaren Berichte](SOURCE_INDEX.md).
- [Vorab festgelegter Abnahmeumfang](ACCEPTANCE_PLAN.md).
- [Quellenkatalog mit vollständigen Hashes](SOURCE_BINDINGS.json).

Dieses Paket ergänzt den [integrierten Stand vom 7. Oktober](../a8-a9-remainder-progress-2026-10-07/README.md).
Die dortigen Originalaussagen bleiben datierte Forschungsprovenienz. Insbesondere
werden historische `false`-Felder und frühere offene Rechenaufträge nicht im
Original überschrieben. Die aktuelle Einordnung steht im
[Forschungsregister](../../../00-uebersicht/RESEARCH_STATE.yaml).

## Quellenbestand

39 gespeicherte ZIP-Dateien enthalten 38 verschiedene Bytefassungen; ein
signiertes C-Paket wurde zweimal identisch abgelegt. Einschließlich der
eingebetteten Vorgänger sind **41 unterschiedliche Originalcontainer mit
1.275 Dateien** erhalten. Hinzu kommen drei separat gespeicherte Begleitdateien.
411 Berichte, Herleitungen, Programme und kleinere Ergebnisdateien sind als
bytegleiche Kopien unmittelbar lesbar. Große Matrixdaten bleiben in den
unveränderten Originalcontainern vollständig enthalten.

Die Verschachtelung erlaubt die Ablage über 15 äußere Container. Große ZIPs
werden als geordnete Binärteile von höchstens 32 MiB gespeichert und vor dem
Prüfen bytegenau zusammengesetzt. Eingebettete ZIPs werden unverändert gelesen,
nicht aus ihren entpackten Inhalten neu komprimiert. SHA-256, Dateigröße,
vollständige Mitgliedslisten und jede katalogisierte Containerkante werden geprüft.

## Reproduktion

Python 3.12 oder 3.13, ausschließlich Standardbibliothek, vom Repository-Stamm:

```sh
python -B -m unittest discover -s research/x-c1/a8-a9-global-closure-2026-10-13 -p test_integration.py -v
python -u -B research/x-c1/a8-a9-global-closure-2026-10-13/replay.py --output ../a8-a9-global-check
```

Das Ziel muss neu sein und außerhalb des Repositorys liegen. Der Standardlauf:

1. stellt sämtliche Originalarchive her und prüft alle Dateien und lesbaren Kopien;
2. wiederholt die vollständige rationale Vorgängerkette des globalen Abschlusses:
   globaler Gram und Modellfehler, neue Antworten und Common96, Außenrest und
   Momentgeometrie, gemeinsamer Logrest und Zielmatrix;
3. rekonstruiert die beiden globalen Schurbilanzen mit allen 203 Kraftkoordinaten;
4. wiederholt die unabhängige rationale Reserveverschärfung und ihre Gegenkontrollen;
5. vergleicht die gesamte Schlussquittung mit der commitgebundenen
   [Erwartungsquittung](reports/ACCEPTANCE.json) und schreibt `ACCEPTANCE.json`,
   die beiden Schlussquittungen und die Unterprüferlogs.

Mit `--sources-only` wird ausschließlich die Archivrekonstruktion geprüft.
Dieser Lauf behauptet keinen mathematischen Replay. Die zwölf Integrations-
Gegenkontrollen prüfen beschädigte Daten, unvollständige Kataloge, unsichere
Pfade, fehlende Quellen, fehlgeschlagene Unterprüfer und das CI-Routing.

Die ursprünglichen großen Operator- und globalen Integrationen werden im
Standardlauf **nicht erneut erzeugt**. Ihre gerichteten Einschließungen,
Erzeugungsprogramme und analytischen Restherleitungen bleiben gebundene Eingaben.
Der optionale große Neuaufbau befindet sich weiterhin im originalen Grampaket.
Historische Zwischenpakete werden vollständig erhalten; ihre sämtlichen früheren
Rechenläufe werden durch diese Integration nicht erneut ausgeführt.

Die bereits im Abschlussarchiv enthaltene Portabilitätskorrektur normalisiert
genau einen CRLF/LF-Dateivergleich im Arbeitsspeicher. Sie verändert keine
numerischen Felder, Originalarchive oder Manifestbindungen.

## Nächste Forschungsfragen

Die übernommenen Operator-, Domänen- und Raumzerlegungssätze gezielt extern
prüfen lassen; danach den konstruktiven Mechanismus an weiteren Horizonten
untersuchen. Der frühere gesonderte Tailtest bleibt als alternative, stärkere
Aussage offen. Seine anderen Funktionale und seine Normierung dürfen nicht mit
den 203 Kräften dieses direkten Positivitätsbeweises gleichgesetzt werden.
