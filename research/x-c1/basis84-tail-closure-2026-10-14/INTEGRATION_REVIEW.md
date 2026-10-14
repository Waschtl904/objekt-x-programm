# Technische Reviewhinweise zur Integration

14. Oktober 2026. Diese Notiz bewertet den zusätzlichen automatischen Code-Review
von PR #221; sie ist keine externe mathematische Begutachtung.

## Umgesetzte Absicherungen

Der Integrationsprüfer bindet die beiden historischen Archividentitäten nun
zusätzlich als feste SHA-256-Konstanten im geprüften Code. Ein gemeinsam mit
seiner Katalogdatei und deren Sidecar ersetztes Archiv wird damit verworfen.
Der neue Gegenkontrolltest verändert genau diese abgestimmten Metadaten.
Die historischen Archive, deren Mitglieder und die mathematischen Prüfer sind
unverändert. Die Git-Commitbindung bleibt der Vertrauensanker des Codes selbst.

Die GitHub-Ergebnisartefakte enthalten zusätzlich `github.run_attempt` im Namen.
Dadurch haben spätere Wiederholungen desselben Workflow-Laufs eigene Nachweise.
Das ändert keine mathematische Aussage und keine Abnahmequittung.

## Bewertete Fehlalarme und Quellenmodell

Die vier als Shell-Injection gemeldeten Aufrufe liegen in den unveränderten
Originalprüfern. Sie verwenden `subprocess.run` mit einer Argumentliste, ohne
`shell=True`: ausführbar ist `sys.executable`, danach folgt ein fest benanntes
Python-Skript aus dem zuvor per SHA-256 geprüften Originalarchiv. Eingabepfade
werden als einzelne Argumente übergeben. Sie werden weder als Shell-Befehl
zusammengesetzt noch durch eine Shell ausgewertet. Eine zusätzliche Shell-
Quotierung würde die Argumentwerte verändern. Ein unbestätigter Botbefund wird
deshalb nicht als Sicherheitsnachweis übernommen; die Originale bleiben versiegelt.

Die A9-Invers- und Domänenresultate sind mathematische Abhängigkeiten mit festen
Beweisankern. Der Tail-Replay verwendet ihre im Originalarchiv eingebetteten,
hashgebundenen Fassungen. Er liest keine aktuellen Arbeitsdateien aus den
separaten A9-Verzeichnissen. Deren spätere Änderung verändert den gebundenen
Tail-Beweis daher nicht. Der Global-Closure-Speicher und sein Rekonstruktionscode
werden dagegen tatsächlich gelesen und sind bereits im Workflowfilter enthalten.
Ein neuer mathematischer Abhängigkeitsstand müsste ausdrücklich neu gebunden
und geprüft werden; ein blindes Wiederholen alter Daten könnte ihn nicht prüfen.

Zusätzliche automatische Reviews und ihre etwaigen Fehlalarm-Status werden im
Integrationsnachweis getrennt von den erfolgreichen ausführbaren CI-Prüfungen
ausgewiesen. Sie werden weder als bestandener Review noch als Mathematikbeweis
gezählt. Es werden keine GitHub-Schutzregeln umgangen.
