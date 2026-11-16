# Technischer Nachtrag zu den sechs Sourcery-Kommentaren — 12. November 2026

Basis: `33425401dd1c2797f7ec8319389091c2ed2e8d7e`, integrierter PR #266.
Umfang: Prüfinfrastruktur und datierte Statusdarstellung. Originalarchive,
Lesefassungen, mathematische Ergebnisse, `SCOPE.json`, Quellenindex und globale
Forschungsregistry bleiben unverändert. Keine neue physische Rechnung.

## Befunde und Maßnahmen

| Kommentar in PR #266 | Befund | Technischer Nachtrag |
| --- | --- | --- |
| [Review-/Autorisierungsfelder](https://github.com/Waschtl904/objekt-x-programm/pull/266#discussion_r4546787295) | **Bestätigt.** Veränderte Felder bestanden bisher trotz aktualisiertem Manifest. | Alle drei Werte und die vollständige Feldmenge sind als historischer Vorbereitungsstand fest gebunden; Negativtests ändern/entfernen jedes Feld über den vollständigen Prüfeinstieg. |
| [Fehlende Originale](https://github.com/Waschtl904/objekt-x-programm/pull/266#discussion_r4546787312) | **Bestätigt.** Der zweite Eintrag konnte verschwinden. | Beide vollständigen Datensätze, die gesamte native Herkunftsnotiz, das originale native Ergebnis und dessen Quellenindexeintrag sind gebunden. Tests entfernen oder verändern jeden der drei nativen Einträge und beide fehlenden Originaleinträge bei aktualisiertem Manifest. |
| [Symlink-Elternpfade](https://github.com/Waschtl904/objekt-x-programm/pull/266#discussion_r4546787305) | **Bestätigt für Verzeichnisverknüpfungen an Paketwurzel und Elternpfad unter Windows.** Der weitergehende konkrete POSIX-`rglob`-Ablauf ist damit nicht nachgewiesen. | Die Baseline akzeptiert echte Windows-Junctions an Wurzel und Elternpfad mit unveränderten Paketbytes. Die neue Prüfung verwirft Links/Reparse-Points in sämtlichen Pfadkomponenten und durchlaufenen Einträgen; aufgelöste Dateien müssen innerhalb des Paketstamms bleiben. Tests verwenden unter POSIX echte Symlinks, unter Windows echte Junctions. |
| [Historischer Prüfauftrag](https://github.com/Waschtl904/objekt-x-programm/pull/266#discussion_r4546787317) | **Bestätigt.** Der ungekennzeichnete alte Auftrag konnte als aktueller Status gelesen werden. | Datierte Einordnung vor dem erhaltenen Wortlaut; README und alter Prüfbericht verweisen auf den separaten [Integrationsnachweis](INTEGRATION_2026-11-12.md). |
| [Historischer `subprocess.run`](https://github.com/Waschtl904/objekt-x-programm/pull/266#discussion_r4546787322) | **Shell-Injection im geprüften Datenfluss widerlegt.** Beabsichtigte Ausführung archivgebundener Python-Skripte bleibt vorhanden. | Nur Datenflussprüfung; das historische Original bleibt unverändert und wird von dieser CI nicht ausgeführt. Einzelheiten unten. |
| [Aktiver `subprocess.run`](https://github.com/Waschtl904/objekt-x-programm/pull/266#discussion_r4546787326) | **Skriptpfad-Umlenkung bestätigt; Shell-Injection im geprüften Aufruf widerlegt.** | `original_root` konnte trotz unverändertem Archiv-SHA einen externen Python-Pfad auswählen. Jetzt festes Archivwurzelverzeichnis, erneute Hashprüfung der tatsächlich entpackten Bytes, Pfadprüfung und Zeitlimit; Negativtests verhindern jeden Prozessaufruf bei umgelenktem Pfad oder verändertem Archiv. |

## Symlink-Reproduktion und Grenze

Unter Windows/Python 3.13.7 wurden Paketwurzel und deren Elternverzeichnis
jeweils durch eine echte Junction ersetzt: Der unveränderte alte Prüfer
meldete jeweils `INTEGRATION_BINDINGS_PASS`. Der alte Prüfer lehnte dagegen
eine zusätzliche unaufgeführte Junction mit zusätzlicher Datei wegen der
abweichenden Dateiliste ab. Die pauschale Behauptung, ausgelassene erwartete
Nachfahren könnten trotz exakter Dateimengengleichheit passieren, ist damit
nicht belegt. Der bestätigte Wurzel-/Elternpfadfall genügt für die Korrektur.

Die Prüfung schützt einen statischen Checkout. Gleichzeitiges bösartiges
Austauschen von Dateisystemeinträgen während des Laufs ist kein hier geprüfter
Bedrohungsfall. Eine SHA-Bindung ersetzt auch keine Codeprüfung, wenn Prüfer
und zugehörige Erwartungen gemeinsam geändert werden.

## Datenfluss der beiden Prozessaufrufe

**Historisches `pruefe_gpt1.py`:** Der normale Aufruf liest das Originalarchiv
einmal in `raw`, prüft dessen fest kodierten SHA256
`6651b8b8f0092f91c4a7d4da75d32f9ec5c45720dc82af8e085589d414bad870`,
entpackt dieselben Bytes in ein frisches temporäres Verzeichnis, prüft das
enthaltene Manifest und startet die fest gewählten `lauf.py`/`vorpruefung.py`.
`sys.executable` und eine Argumentliste werden ohne Shell verwendet.
Die Aussage gilt für den dokumentierten normalen Python-Aufruf. Seine
historischen `assert`-Prüfungen sind unter `python -O` deaktivierbar, einschließlich
des damaligen `assert not sys.flags.optimize`; dieser Modus ist keine sichere
Ausführung dieses Originals. Der Nachtrag führt es nicht aus und legitimiert
keinen optimierten Replay. Der aktive Prüfer lehnt optimiertes Python explizit ab.

**Aktiver `verify_integration.py`:** Der konstante Archiv-SHA verhinderte bisher
keine Umlenkung durch `SOURCE_INDEX.json.archives[].original_root`: Ein absoluter
Pfad verdrängte das temporäre Stammverzeichnis. Ein harmloser Baseline-Test
fing `subprocess.run` ab und bestätigte den extern ausgewählten Skriptpfad;
das fremde Skript wurde nicht ausgeführt. Dies korrigiert die zunächst zu
weite Einschätzung, der Archivhash allein binde auch den ausgeführten Pfad.

Jetzt muss der Metadateneintrag exakt dem festgelegten Archivwurzelverzeichnis
entsprechen. Entpackt werden frisch gehashte Bytes desselben bekannten Archivs;
der Skriptpfad wird ausschließlich aus dieser Konstante gebildet und geprüft.
Python führt bewusst den überprüften Archivcode aus, mit Argumentliste,
`shell=False` und 120 Sekunden Zeitlimit. Shell-Escaping ist für diesen
Aufruf weder erforderlich noch eine Reparatur der gefundenen Pfad-Umlenkung.

## Prüfungen dieses Nachtrags

Die neuen Negativtests aktualisieren das Paketmanifest nach jeder absichtlichen
Metadatenänderung. Der Fehler muss aus der unabhängigen Schutzregel stammen.
Ausführungsbezogene Negativtests prüfen zusätzlich, dass kein Prozess gestartet wird.

Lokaler Lauf unter Windows, Python 3.13.7:

- Paketbindungen und begrenzter skalarer Replay: bestanden, gespeichertes
  Ergebnis unverändert; keine neue q-Auswertung. Der abschließende lokale
  Byteabgleich bezieht auch das zurückgestellte große Archiv ein: acht
  Archive und sämtliche 34 Lesefassungen gegen ihre Archivmitglieder geprüft,
  ohne Release-Upload.
- 21 Schutztests: **18 bestanden, 3 übersprungen**. Alle bisherigen sechs
  Tests und die neuen Metadaten-, Herkunfts-, Skriptpfad- und vier
  Verzeichnisverknüpfungstests bestehen. Die drei übersprungenen Tests betreffen
  Datei-, Manifest- und defekte Symlinks; Windows verweigert das erforderliche
  Recht (`WinError 1314`).
- Unveränderter Registry-Testsatz: **73/76 bestanden**. Weiterhin scheitern
  `test_nonregular_target_is_rejected` (kein `os.mkfifo`),
  `test_symlink_file_parent_and_registry_are_rejected` (Symlink-Recht) und
  `test_reference_copy_cannot_be_active_pending_or_have_meta` (Windows-Pfad
  statt erwarteter Linux-Fehlermeldung). Keine Testabschwächung vorgenommen.
- Generator `--check`, Registry-Validator mit Merge-Basis, Active-Front-Check
  und `git diff --check`: bestanden.
- Alle 41 veröffentlichten Originalarchive/Lesefassungen und alle übrigen
  unveränderten Paketdateien sind gegen die Git-Blobs des Merge-Stands
  geprüft; die bisherigen Dokumentkörper bleiben erhalten. Lokale Links und
  das erneuerte Manifest sind im abschließenden Diff-Abgleich enthalten.

**Offen bleibt der Linux-Lauf dieses Nachtrags**, einschließlich der echten
POSIX-Symlink-Fälle und des vollständigen Registry-Testsatzes. Die vorhandene
lokale Docker-Linux-Engine war nicht erreichbar und ließ sich nicht starten;
der eigene erfolglose Startversuch wurde beendet. Der bestehende Ubuntu-CI-
Workflow führt den erweiterten Testsatz unverändert aus, sobald ein Nachtrags-PR
veröffentlicht wird. Eine zukünftige PR-CI oder der alte 76/76-Lauf auf PR #266
wird hier nicht als Prüfung dieser Revision ausgegeben.

Der historische äußere Manifest-SHA bleibt an PR #266 gebunden. Für die
tatsächlich geänderten aktiven Paketdateien wird `MANIFEST.json` erneuert.
Release-Upload, mathematische Statusaufwertung und neue Forschungsserie sind
kein Bestandteil dieses Nachtrags.

## Revision vom 16. November: abgeschlossene Review von PR #267

Der vorstehende Abschnitt bleibt der Vorbereitungsbericht vom 12. November.
Seine damals offene Linux-Prüfung wurde inzwischen am Head
`ca41c21f7ecd259598f52fea298b67166f7c125c` abgeschlossen:
[Paketprüfung](https://github.com/Waschtl904/objekt-x-programm/actions/runs/43259383342)
mit **21/21 Schutztests ohne Auslassungen**, Paketbindungen und skalarem Replay;
[Registry-Prüfung](https://github.com/Waschtl904/objekt-x-programm/actions/runs/43259383755)
mit **76/76 Tests** am Testmerge `d2f66abd6d8a33d414cabc6f6b835fe0c4621005`.
Dessen Eltern sind die Integrationsbasis `33425401dd1c2797f7ec8319389091c2ed2e8d7e`
und der genannte Head; sein Baum entspricht dem Kandidatenbaum
`1fac328fbabc1438da63932a37e1739640d26ec8`.

Nach der Umstellung auf bereit zur Prüfung ging am 16. November um 05:55:36 UTC
die abgeschlossene Sourcery-Review ein. Der grüne Sourcery-Check ersetzt nicht
die Einordnung ihrer vier konkreten Kommentare:

| Kommentar | Einordnung und Maßnahme |
| --- | --- |
| [Vollständige Herkunftseinträge](https://github.com/Waschtl904/objekt-x-programm/pull/267#discussion_r4582424792) | **Bestätigt.** Unbekannte Archiv-ID, falscher Mitgliedspfad beim fehlenden Asset und doppelte Lesefassungsdatensätze konnten bei erneuertem Manifest passieren. Jetzt sind alle 34 vollständigen Datensätze einschließlich Ziel, Archiv-ID, Mitglied, Größe und SHA256 durch einen unabhängigen kanonischen SHA256 gebunden; Ziele müssen eindeutig sein. Reihenfolge bleibt bedeutungslos. Auch doppelte Archiv-IDs werden verworfen. Negativtests schließen Änderungen an Originalbytes mit gleichzeitig angepasstem Index und Manifest ein. |
| [Doppelte JSON-Schlüssel](https://github.com/Waschtl904/objekt-x-programm/pull/267#discussion_r4582424807) | **Bestätigt.** Der bisherige Parser nahm den jeweils letzten Wert. Alle JSON-Einlesestellen des aktiven Prüfers verwenden jetzt einen Duplikate ablehnenden Parser, auch für verschachtelte Objekte. Tests mit widersprüchlichen Status-, Quellen- und Manifesteinträgen verlangen Abbruch vor jedem Prozessstart. |
| [Behaupteter POSIX-Absturz](https://github.com/Waschtl904/objekt-x-programm/pull/267#discussion_r4582424816) | **Widerlegt für die unterstützte CPython-3.13-Umgebung.** Der oben gebundene Ubuntu-Lauf mit CPython 3.13.18 besteht einschließlich aller POSIX-Pfadtests. `stat.FILE_ATTRIBUTE_REPARSE_POINT = 1024` ist in [CPython 3.13 Lib/stat.py](https://github.com/python/cpython/blob/3.13/Lib/stat.py#L186) ohne Windows-Bedingung definiert. Es ist das Dateiattribut `st_file_attributes`, dessen Fehlen bereits abgefangen wird. Keine unbegründete Codeänderung. |
| [Zurückgewiesene Pfadaliase](https://github.com/Waschtl904/objekt-x-programm/pull/267#discussion_r4582424826) | **Als Nutzungseinschränkung bestätigt, kein Umgehungsfehler.** Die Ablehnung aller verknüpften Vorfahren ist der ausdrücklich getestete Schutzvertrag dieses Pakets. Er gilt auch für externe Assets. Aufruf über einen tatsächlichen, vollständig aufgelösten Pfad ohne Symlink/Junction/Reparse Point; gegebenenfalls Paket und Asset in ein solches Verzeichnis kopieren. Automatische Auflösung vor der Prüfung würde gerade den geforderten Wurzel-/Elternpfad-Negativtest umgehen. Dieser Nachtrag lockert die Regel nicht. |

Die zwei bestätigten Schutzlücken begründen diese sichtbare Revision des alten
Kandidaten. Seine CI bleibt an seinen alten Head gebunden. Lokal bestehen nun
**22 von 25 Schutztests**, die drei bekannten Datei-Symlink-Tests sind unter
Windows wegen fehlenden Rechts übersprungen. Die neuen Negativfälle wurden vor
der Korrektur gegen den alten Prüfer mit erneuertem Manifest ausgeführt und
zeigen dort die fehlende Ablehnung. Die unveränderten 76 Registry-Tests sowie
alle 25 Schutztests müssen für diese Revision erneut in der Linux-PR-CI bestehen;
das wird hier nicht vorweggenommen. Originaldateien, Archive, mathematische
Aussagen, Quellenindex, historischer Scope und Forschungsregistry sind unverändert.
