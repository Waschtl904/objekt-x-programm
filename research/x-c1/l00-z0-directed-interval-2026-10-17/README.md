# L₀,₀: vollständiges gerichtetes Intervall für z₀

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, bedingt auf die gebundenen Operator-, Domänen- und Quellenzertifikate. Baut auf dem Diagnose-PR #230 auf.

| Parität | L₀,₀ | Ausschlussschwelle |
|---|---:|---:|
| gerade | [−407,736; 401,497] | 980,113997 |
| ungerade | [−2,646; 11,832] | 398,766496 |

Dieser gebundene Skalartest mit z₀ liefert keinen Ausschluss. N12 und der volle Energievergleich bleiben offen. Der hohe Anteil wird vollständig durch seine Normschranke bezahlt; kein numerischer hoher Mittelpunkt wird verwendet.

[Herleitung und Fehlerbudget](PROOF.md). Exakte rationale Ergebnisse in `expected/`.

```sh
python3 -m pip install python-flint==0.9.0
python3 research/x-c1/l00-z0-directed-interval-2026-10-17/verify.py
```

Pflichtprüfung: Eingabe- und Eigenbindungen, beide vollständigen Intervallläufe, exakte k₀-Zuordnung, Endpunkt- und analytische Quadraturreste, bytegleicher Replay beider Ergebnisdateien. Externe mathematische Prüfung bleibt offen. Die unveränderten Vorgängerzertifikate sind keine neue unabhängige Prüfung ihrer großen Quellenintegrationen.

## Replay-Revision vom 17. Oktober 2026

Die zuvor verwendeten beiden `subprocess.run`-Aufrufe wurden nach dem
Sourcery-Sicherheitsaudit durch direkte Aufrufe der bestehenden Python-Einstiegspunkte
ersetzt. Der Replay prüft jetzt zusätzlich das Vorbereitungsskript und dessen
Quellenbindungen vor dem Import. Er akzeptiert keine externen Skriptpfade,
startet keine Shell und keinen Kindprozess. `python -O` wird ausdrücklich abgewiesen.
Der Certifier, die mathematischen Eingaben und beide erwarteten Ergebnisdateien
bleiben unverändert. Die Abnahme verlangt erneut einen vollständigen bytegleichen
Replay aus einem frischen Archiv sowie die CI am neuen Head. Der frühere
Replay-Nachweis bleibt an seinen damaligen Commit gebunden.

## Eingabe-Snapshot-Revision vom 17. Oktober 2026

Ein weiterer Sourcery-Befund betrifft den Certifier: Die frühere Fassung prüfte
Datei-Hashes und öffnete dieselben Eingaben später erneut. Eine gleichzeitige
Änderung zwischen Prüfung und Verwendung hätte damit ungeprüfte Bytes in die
Rechnung bringen können. Das ist eine Lücke des Eingabeladers, kein festgestellter
Fehler der aus frischen Archiven reproduzierten Zahlen.

Der Certifier liest nun jede gebundene Eingabe einmal, prüft den Digest dieser
Bytes und bewahrt sie in einem unveränderlichen Speicherabbild auf. Sowohl
JSON-Parsing als auch gzip-Dekompression verwenden ausschließlich dieses
Abbild. Ungebundene Zugriffe, falsche Hashes und Pfade außerhalb der gebundenen
Wurzel werden abgewiesen; auch der direkte Certifier lehnt `python -O` ab.
Ein Regressionstest im Replay verändert JSON- und gzip-Dateien nach dem Einlesen
und prüft die isolierten Originalbytes, die unveränderliche Abbildung sowie
Fehlerfälle. Der frühere Revisionsabschnitt beschreibt weiterhin seinen damaligen
Stand; in dieser Revision wird auch der Eingabelader des Certifiers geändert.

Pflichtabnahme vor Veröffentlichung: Snapshot-Regression, beide vollständigen
Intervallläufe aus einem frischen Repository-Archiv mit bytegleichem Vergleich
gegen die unveränderten Ergebnisdateien, Registry-Validator und relevante
Registry-Tests. Vor dem Merge müssen außerdem alle anwendbaren CI-Prüfungen am
endgültigen Head erfolgreich abschließen. Formeln, Fehlerbudgets, mathematische
Eingaben, Ergebnisdateien und `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN` bleiben
unverändert; die frühere Abnahme ersetzt den neuen Certifier-Replay nicht.
