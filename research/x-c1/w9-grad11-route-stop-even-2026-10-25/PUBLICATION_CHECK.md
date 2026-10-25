# Veröffentlichungsabgleich – neuer Begleittext

## Vorab festgelegter Umfang

Dieser Draft veröffentlicht bereits geprüfte Mathematik und ihre unveränderten Belege. Neue Begleittexte erklären Scope und Navigation; der neue Prüfer ist ausschließlich ein Byte-/Bindungsprüfer. Es werden keine mathematischen Eingaben, Fehlerpreise, Aussagen oder historischen Originale geändert.

Für diesen Veröffentlichungsschritt verpflichtend:

1. Main gleich `137940b4e8ea391af408992ae17fb4eebbd6d7c7`; keine unerwarteten vorhandenen Änderungen; vorhandene Branches und PRs vor Neuanlage auf Doppelveröffentlichung prüfen.
2. GPT1-ZIP: 12838318 Byte, SHA-256 `9fa36e19fcacc2f0392149d9b8c0f29b9b47a0987ce77be6631a4fcc437c0ca7`. Die geordnete Rekonstruktion aus den beiden unveränderten Binärteilen muss exakt diese vollständigen Originalbytes liefern.
3. Eingebettetes GPT2-ZIP: 875069 Byte, SHA-256 `be2b1ab43514454cfec95dd1283d81e8d2f34745f4cf1554ecfd2d6811888e93`; Originalarchive nicht neu verpacken.
4. Alle 54 Bindungen im GPT1-Originalmanifest und alle 33 Bindungen im GPT2-Originalmanifest prüfen; sämtliche 35 GPT2-Dateien mit ihren im GPT1-Paket enthaltenen Kopien vergleichen.
5. Alle 53 lesbaren Textmitglieder des GPT1-ZIPs und die gesonderte eingefrorene Belegkette bytegleich bereitstellen. Historische Prüfstandsvermerke bleiben erhalten.
6. Neue Begleitdateien getrennt kennzeichnen; Manifestabdeckung, relative Navigationslinks, exakte Git-Blob-Bytes und ausschließlich additive Änderungen im neuen Paketpfad prüfen.
7. Nach dem Push den Forschungsbranch frisch in ein separates Objektverzeichnis einlesen, sämtliche publizierten Dateien einschließlich ZIP aus den Remote-Git-Blobs gegen den vorbereiteten Commit vergleichen und den Byteprüfer darauf ausführen. Head, Tree, einzige Basis und Diff-Pfade prüfen; Ergebnis an den exakten Head binden.
8. Genau ein Draft-PR; Main unverändert, Auto-Merge aus, kein Merge und keine Branchlöschung. Tatsächlichen Abschlussabgleich in der PR-Beschreibung dokumentieren.

`verify_publication.py` prüft die Punkte 2–5 und die Manifestabdeckung von Punkt 6 sowohl auf Arbeitsdateien als auch auf explizit gewählten Git-Blobs. Er integriert nichts, lädt keine Forschungsabhängigkeiten und führt keine numerischen Originalprogramme aus. SHA-Bindungen ersetzen keine externe mathematische Begutachtung.

## Abgrenzung

Technische Bereitstellung: Ein direkter CLI-Push scheiterte vor der Veröffentlichung an fehlender CLI-Anmeldung. Der vollständige Base64-ZIP-Upload überschritt anschließend die 16-MiB-Anfragegrenze des Connectors. Daher werden ausschließlich aufeinanderfolgende Originalbytes als zwei Binärteile plus Deskriptor bereitgestellt. Das ursprüngliche ZIP wurde weder bearbeitet noch neu gepackt. Die fehlgeschlagenen Versuche erzeugten keinen Forschungsbranch und keinen PR. Die Bereitstellung erfolgt über den verbundenen GitHub-Connector.

Der neue Veröffentlichungsabgleich ist kein zusätzlicher F/K-Replay. Die dokumentierte mathematische Gegenprüfung bleibt an ihre ursprünglichen Eingänge und Ausgaben gebunden. Eine weitere Ganzrestintegration, Antwortsuche, Richtungswahl oder Unterformsuche ist nicht beauftragt. Die kanonischen Statusdateien und bestehende Forschungspakete werden in diesem Draft nicht geändert. Anwendbare automatisch ausgelöste Repository-CI bleibt separat an ihren jeweiligen Commit gebunden; ausstehende oder fehlgeschlagene Checks werden nicht als Erfolg ausgegeben. Es wird kein manueller Workflow gestartet.

AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; unter H1–H4 ausschließlich Ausschluss der festen äußeren Antwort mit `Q_new`. Keine negative tatsächliche Weil-Richtung; L1 und Zweiraumnachweis unberührt; Checkliste 3/10, Punkt 4 offen.
