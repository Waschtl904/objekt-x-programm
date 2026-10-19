# A1: vorhandenen Nachweis prüfen und wiederverwenden

Stand: 19. Oktober 2026. Infrastruktur für den eingefrorenen geraden
A1-Matrixnachweis; keine mathematische Statusänderung.

## Was der kurze Check aussagt

Ein neuer Git-Commit macht einen vorhandenen Nachweis nicht ungültig.
Der kurze Check prüft deshalb, ob der aktuelle A1-Baustein noch exakt zu einem
bereits erfolgreichen Rechenlauf gehört. Bei Übereinstimmung meldet er
`bound-certificate-unchanged`. Das Abschluss-Gate bezeichnet diesen Fall als
`REUSED`, ausdrücklich nicht als neue Berechnung.

Die Basis ist [Lauf 39272705942, Versuch 1](https://github.com/Waschtl904/objekt-x-programm/actions/runs/39272705942)
am Commit `250f50e196dee0ea46c31506d7b81efc1b1f3239`: frischer Matrixaufbau,
Matrixfingerprint, rigoroser Arb-LDL-Nachweis und Abschluss-Gate waren
erfolgreich. Die [Bindung](../.github/certificates/a1-c-even/manifest.json)
enthält 47 Quellen-/Voraussetzungsdateien, die Rechenkonfiguration, den
Matrixhash und die Hashes der archivierten Laufdaten und vollständigen
Build-, LDL- und Gate-Protokolle. Die Protokolle sind UTF-8-Texttranskripte
mit LF-Zeilenenden, ohne BOM und ohne Leerraum am Zeilenende. Der numerische Matrixhash
bleibt unverändert.

Diese Dateien sind eine dauerhafte Provenienz des bereits akzeptierten
Programmlaufs, kein neu erzeugtes eigenständig prüfbares LDL-Faktorisat.
Die Wiederverwendung benötigt keine ablaufenden Actions-Artefakte und
keinen frischen Netzwerkzugriff. Quellen und Protokolle bleiben im Git-Verlauf
verfügbar; eine unabhängige Nachrechnung bleibt möglich. Externe Prüfung
und die übergeordneten mathematischen Voraussetzungen bleiben offen bzw.
behalten ihren bisherigen Status.

## Gebundener Umfang

Die numerische Python-Kette besteht aus `a1_c_even_matrix_artifact.py`,
`certify_a1_c_even_exact_dyadic_matrix.py` und
`check_a1_c_even_engine_preflight_arb.py`. Der separate C-Prüfer ist
`check_a1_c_even_artifact_spd_ldl.c`; der manuelle Eigenwertaudit bleibt
ebenfalls gebunden. Die eingefrorene Kette liest keine zusätzlichen
Repository-Datentabellen: Parameter, Primbeiträge, Präzision, Quantisierung
und Zielmatrix sind in diesen Quellen enthalten.

Die Erkennung ist zusätzlich konservativ: Sie bindet alle vorhandenen
`check_a1_*`, `certify_a1_*` und `a1_*`-Quellen, weitere A1-Workflows,
`audits/P11_A1_*`, die A1-Statuskapsel und gemeinsame Laufzeitkonfiguration.
Auch neu hinzukommende oder entfernte Dateien dieser Gruppen werden erkannt.
Neue importierbare Geschwistermodule unter `scripts/` und neue Python-Pakete
auf Repository-Ebene erzwingen eine Prüfung, damit beispielsweise ein lokales
`flint.py` oder `sitecustomize` nicht unbemerkt den Importweg verändert.
Unabhängige bestehende Forschungsordner sind keine Suchpfade der
eingefrorenen numerischen Befehle.

Die drei numerischen Jobs einschließlich Runner, Setup-Actions,
Bibliotheksanforderungen, Compileraufruf, Befehlen, Parametern und Grep-Prüfungen
bleiben gegenüber dem historischen Workflow unverändert. Ihr genauer Text
sowie globale `env`-/`defaults`-Abschnitte werden gebunden. Die Wiederverwendung
behauptet keine neue Prüfung mit heute eventuell anderen installierbaren
Bibliotheksversionen; sie übernimmt den protokollierten historischen Lauf.

## Entscheidung bei einem neuen PR-Head

| Befund | Folge |
| --- | --- |
| Quellen, Konfiguration, Provenienz und bereits integrierte Wiederverwendungsregel unverändert | Kurzer Abgleich; historischen Nachweis übernehmen |
| A1-Quelle, Fehlerbudget, gebundene Voraussetzung, Importumgebung oder numerische Konfiguration geändert | Frischer A1-Rechenweg |
| Wiederverwendungsregel, Tests, Nachweisdateien oder A1-Hauptworkflow gegenüber der PR-Base geändert | Frischer A1-Rechenweg; der PR genehmigt seine eigene Ausnahme nicht |
| Manueller Audit | Frischer A1-Rechenweg mit gewähltem LDL-/Eigenwertzweig |
| Unvollständige oder beschädigte Evidenz, falscher Head, unlesbare Historie | Check schlägt fehl; kein grüner Ersatzstatus |

Der schnelle Weg verlangt eine vollständig festgestellte Git-Abstammung:
Nachweiscommit vor der PR-Base und PR-Base vor dem geprüften Head.
Bei einer noch nicht integrierten neueren Base ist zunächst deren Aufnahme
zu klären; die konservative Route verlangt sonst erneut den frischen Weg.

Ein erfolgreicher Build ohne erfolgreiche LDL-Prüfung reicht nicht.
Fehlgeschlagene, laufende, abgebrochene oder übersprungene historische
Pflichtjobs gelten nicht als Erfolg. Eine bloß im Shellskript angezeigte
`CERTIFIED`-Zeile reicht ebenfalls nicht: geprüft werden die tatsächlichen
zeitgestempelten Ergebniszeilen.

## Einführung und spätere Erneuerung

Der Einführungs-PR durchläuft einmal den vollständigen Rechenweg, weil
die neue Wiederverwendungsregel noch nicht in seiner Base steht. Nach
Integration kann jeder weitere unveränderte A1-Stand denselben gebundenen
Nachweis verwenden. Ein W9-Pythonversionsfix oder ein späterer Textfix im
gleichen PR löst dann keine A1-Neuberechnung aus.

Bei einer tatsächlichen A1-Änderung bleibt der alte Nachweis historisch gültig
für seinen alten Stand. Für eine neue Wiederverwendungsbasis werden der
erfolgreiche neue Lauf samt Versuch, vollständigen Protokollen, Quellen,
Konfiguration und genauer Aussage in einer ausdrücklich geprüften neuen
Bindung erfasst. Es gibt keine automatische Selbstpromotion eines
PR-Artefakts und kein Vertrauen in einen Cache-Schlüssel allein.

Die Routertests prüfen positive Wiederverwendung und Gegenfälle in kleinen
isolierten Git-Repositories. Sie lösen keine Matrixrechnung aus.
Diese Infrastruktur ändert weder A1-COMP noch `verified_through`, N12,
Meilenstein 4, Objekt X oder einen externen Reviewstatus.
