# Modellanschluss und analytische Ergänzung des festen geraden Zeugen

Version vom 23. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN. L1 bleibt offen.**
Dieses Ergänzungspaket veröffentlicht den geprüften Zwischenstand zu #252/#254.
Die zweite Richtung und eine vollständige interne analytische Abnahme werden nicht freigegeben.

## Inhalt und Herkunft

| Verzeichnis | Gebundener Inhalt |
| --- | --- |
| [model-connection](model-connection/REVISION-2026-10-23.txt) | Ganze Funktionsidentifikation, Fehlerbuch und deterministische Summationsrevision; historische Berichte und neue Revisionsquittung getrennt |
| [joint-audit](joint-audit/BERICHT.txt) | 191 Quellenkoordinaten, Modellkontrollen, ganze rohe Operatorgrenze und Gegenprüfung des separat veröffentlichten Bindungsfixes |
| [finite-audit](finite-audit/BERICHT.txt) | Quellen-/Verstärkungscaps, Kontur-/Cachekontrollen, gemeinsame Kleinrestbuchung und endliche Pflichtenliste |

Alle drei gelieferten Teilpakete samt Manifesten bleiben bytegleich. Eingebettete
Patches und frühere Veröffentlichungspläne sind historische Belege, keine beim
Aufruf automatisch ausgeführten Repositoryänderungen. Der Vierdateienfix aus
PR A ist **nicht** Bestandteil des hier vorgeschlagenen Repository-Diffs.

Die deterministische Revision ordnet die fünf Summanden vor ihrer Addition.
Frühere unbestimmte Mengeniteration konnte wenige rationale Intervallendpunkte
ändern. Die revidierte Rechnung behält die Schwelle `1e-150` und wird mit
`PYTHONHASHSEED=0` und `1` wiederholt. Sie überschreibt keinen historischen Prüfer.

## Quellen und Aussagegrenzen

Bezugscommit: `beb38c9d1cba666bb3b7ddab9577873e59d854c4`.
[668 Quellenbindungen](finite-audit/SOURCE_BINDINGS.json) und das Quelleninventar
der Modellrevision bezeichnen dieselben Bytes. Die 568 historischen Eingänge
des separaten Fixes sind ein anderes Inventar: 100 ursprüngliche Paketdateien
einschließlich Manifest plus 568 Historieneingänge ergeben 668 Auditquellen;
nach dem Fix kommt eine Paketdatei hinzu, also 669 isolierte Dateien.

Der neue Prüfeinstieg exportiert die Quellen aus dem gebundenen Git-Commit.
Er liest keine zufällig vorhandenen Arbeitsdateien und funktioniert deshalb
auch nach dem getrennten Merge des Bindungsfixes. Historische `ACCEPTANCE.json`
und Reproduktionsquittungen behalten ihren ursprünglichen Bezugsstand.

[STATUS.json](STATUS.json) ordnet L1 ausdrücklich den Teilpflichten
`LOW-HIGH-SOURCES`, `H-SOURCE` und `REST-CATALOGUE` zu. H-SOURCE allein ist
keine Umbenennung oder Erledigung der gesamten Pflicht L1. Zu prüfen bleibt,
ob eRaw-, eLow-, Feature- und h-Modellpreise die tatsächliche korrigierte Quelle
einschließlich hoher Anteile, Antwortmodell, Gamma-Rest und eingefrorener
T-Koeffizienten vollständig decken. Die 191 niedrigen Koordinaten ersetzen
diesen ganzen Nachweis nicht. Die übrigen übernommenen Voraussetzungen P1–P5
stehen im [bedingten Satz](PROOF.md).

## Zahlen und Fehlerbuchung

[NUMBERS.md](NUMBERS.md) berichtigt die beschädigte Exponentendarstellung anhand
exakter rationaler Oberendpunkte in den maschinenlesbaren Ergebnissen.
[NUMBERS.json](NUMBERS.json) bindet jede Anzeige an Datei, Feld und SHA-256.
Es werden keine unterlaufenden `float`-Werte und keine wiederholten Exponenten übernommen.

Die bedingte Restenergie bleibt `<4.632e-11`; der konservative Operatorweg
`<1.391e-10` und der Deckel `1e-9` bleiben erhalten. Die Quellen-Budgetäquivalente
sind keine Umkehrung der X-zu-L-Dualnorm-Abschätzung. Der p-Preis, der bereits
bezahlte innere Rand und die Gamma-Korrektur werden jeweils einmal gebucht.
Der sehr kleine algebraische Modellabgleich ist kein physischer Genauigkeitsgewinn.

## Vorab festgelegte Veröffentlichungsprüfung

Pflicht: alle Paket-/Quellenbindungen; exakte Zahlendarstellung und Statusgrenzen;
zwei vollständige Replays der deterministischen Modellrevision mit verschiedenen
Hash-Seeds; begrenzter gemeinsamer Audit einschließlich 191 Quellenkoordinaten
und Negativkontrollen; frische Quellencaps; acht Kontrollen des neuen Einstiegs;
Diff-/Link-/Metadatenprüfung und anwendbare CI am veröffentlichten Head.

Die unveränderten Cache-/Konturbelege und ihre vollständige frische Reproduktion
bleiben über [PORTABLE_REPLAY.json](finite-audit/evidence/PORTABLE_REPLAY.json)
gebunden. Der Veröffentlichungslauf führt weder die 411 alten Energieabschnitte
noch die Cache-/Konturprüfung ohne neuen Anlass erneut aus. Der separate
Bindungsfix prüft seinen isolierten Rand-Replay in eigenem Scope.

Python 3.12.14, `python-flint==0.9.0`; im vollständigen Git-Checkout:

```sh
python -B research/x-c1/w9-model-connection-audit-even-2026-10-23/verify.py
python -B research/x-c1/w9-model-connection-audit-even-2026-10-23/test_controls.py
python -u -B research/x-c1/w9-model-connection-audit-even-2026-10-23/verify.py --replay --report /tmp/model-publication.json
```

Für einen isolierten Export kann `--repo /pfad/zum/git-checkout` angegeben werden.
Der Bericht muss außerhalb des Paketverzeichnisses liegen. Kein Netzwerkzugriff
im mathematischen Replay; die gebundenen Git-Blobs müssen lokal vorhanden sein.
Die eigenständigen Reproduktionsanleitungen der Teilpakete bleiben erhalten.

Veröffentlichung als Draft; kein Merge und kein Auto-Merge. Integration,
mathematischer Status und externe Abnahme bleiben getrennt.
