# Abgleich älterer lokaler Arbeitsstände

7. Oktober 2026. **Historische Quellen und Navigation; keine Statuspromotion.**

Vergleichsbasis ist Main
[`11d433da421c913e649d71742b7bf9b8028ceb1a`](https://github.com/Waschtl904/objekt-x-programm/commit/11d433da421c913e649d71742b7bf9b8028ceb1a).
Der aktuelle Forschungsstand bleibt im [Register](../../RESEARCH_STATE.yaml),
die Arbeitsfolge in [NEXT_GATES](../../NEXT_GATES.md).

## Ergebnis

Die jüngste Ergebniskette war bereits integriert. Es fehlten jedoch einzelne
frühere Prüfberichte, Programme, Quittungen und Vorbereitungsfassungen.
Außerdem bezeichneten aktive Wegweiser den bereits ausgeführten Y-Kernel-Test
noch als nächsten Versuch. Diese Hinweise sind nachgeführt.

Verglichen wurden **73 lokale ZIP-Fassungen** mit den **2.752 Dateien** der
Main-Basis und den darin enthaltenen Archiven. 31 ZIP-Fassungen liegen bereits
als vollständige identische Archive auf Main. Weitere Inhalte sind dort als
Einzeldateien oder in Folgepaketen enthalten. Der Katalog berücksichtigt auch
verschachtelte Archive und unterschiedliche Dateinamen.

**231 zusätzliche unterschiedliche Dateien** sind mit ihren Originalbytes
im [Nachtragsarchiv](recovered-sources.zip) erhalten: zusammen 6.636.413 Bytes,
komprimiert rund 1,6 MB. Die Katalogeinträge unterscheiden:

- `BASE_MAIN`: Originalbytes am angegebenen Pfad des oben genannten Commits;
  ein `!` trennt einen ZIP-Pfad vom enthaltenen Mitglied.
- `RECOVERED_BYTES`: Originalbytes unter `files/<SHA-256>` im Nachtragsarchiv.
- `CONTAINER_CATALOG`: ursprünglicher ZIP-Hash und Verzeichnisinhalt; die
  enthaltenen Dateien sind über die beiden vorigen Arten erreichbar.
  `member_path` erhält den ursprünglichen Mitgliedsnamen; `path` bezeichnet
  gegebenenfalls die separate Ablage im Nachtragsarchiv.

[CATALOG.json](CATALOG.json) bindet alle 73 Ausgangsfassungen, 43 zusätzliche
verschachtelte oder äußere Container und alle ergänzten Dateiinhalte.
Zusätzlich sind 23 einzelne Projekttexte aus dem Downloadverzeichnis
katalogisiert, darunter Council-Analysen und R2-Gegenprüfungen aus August
und September sowie zwei doppelt benannte Fassungen. Die fünf Dateien
eines früheren lokalen Vorbereitungscommits sind ebenfalls
zugeordnet; zwei davon sind zusätzliche ursprüngliche Text-/Codefassungen.
Mehrere Dateinamen dürfen dasselbe Archiv oder dieselben Dateien bezeichnen.

Die ursprünglichen ZIP-Dateien bleiben lokal unverändert. Bei einem
`CONTAINER_CATALOG` wird **keine bytegleiche Rekonstruktion der ZIP-Verpackung**
behauptet; erhalten sind ihr ursprünglicher Hash, die Mitgliedspfade und die
vollständigen Mitgliedsinhalte. Bereits auf Main vorhandene große Modelldaten
werden dafür nicht nochmals kopiert.

## Einordnung der aufgefundenen Vorstufen

| Frühere Arbeit | Heutige Einordnung und Bezug |
| --- | --- |
| Einzelne Council-, R2- und NEU-250-Texte aus August/September | Historische Strategie- und Reviewbeiträge einschließlich ihrer Korrekturen. Im Original verwendete Bezeichnungen wie „externer Reviewer“ oder „unabhängig“ werden hier nicht als fachliche externe Abnahme bestätigt. Referenzierte zusätzliche Skripte, Zertifikate oder Sandbox-Dateien sind nur insoweit verfügbar, wie sie tatsächlich im Katalog enthalten sind. |
| Sechs Objekt-X-Kandidatenfassungen aus September, bis „diff-4 Reconciliation“ | Frühere nichtkanonische Vorschläge und Fehlerkorrekturen. Der spätere [Vor-ι′-Audit](../../../audits/P11_VOR_IOTA_PRIME_FESHBACH_FIREWALL_2026-09-11/README.md) behandelt die lokale Firewall. Die ursprünglichen Entwürfe werden historisch erhalten; ihre damaligen Arbeitsaufträge gelten nicht als heutige Freigabe. |
| PR-137-Konsolidierungs- und mathematisches Prüfpaket vom 18. September | Der [positive Meilenstein](../../../research/x-c1/pr137-consolidated-milestone-2026-09-18/README.md) ist integriert. Zusätzliche damalige Autorenreviews und ihre Quittungen fehlten als vollständige lokale Fassungen. Ihre Einwände und Prüfgrenzen bleiben erhalten; keine externe Begutachtung wird daraus abgeleitet. |
| CI-Reparatur und Critical-Half-Archivierungsentwurf | Historische Vorbereitungen; Nachfolger sind [PR #146](https://github.com/Waschtl904/objekt-x-programm/pull/146), [#148](https://github.com/Waschtl904/objekt-x-programm/pull/148) und die [Quellenerhaltung](../CRITICAL_HALF_RP2_SOURCE_PRESERVATION_2026-09-26/README.md). Alte Workflowtexte werden ausschließlich archiviert und nicht aktiviert. |
| O8/O9-Pakete vom 27. September | Hauptbeweise und Zahlen sind im [O8/O9-Paket](../../../research/x-c1/first-chamber-o8-o9-2026-09-27/README.md). Ergänzt werden fehlende ursprüngliche Fassungen von Eingabequittungen, Begleittexten und Reproduktionsunterlagen. Abweichende historische Laufzeiten, Pfade und Statusangaben werden nicht überschrieben. |
| Spektraltransport, relativer κ-Block und Resolventenmomente | Die in älteren Übergaben noch als lokal bezeichneten Blöcke sind in der [Spektralkette](../../../research/x-c1/renewable-low-schur-spectral-2026-09-29/README.md) bzw. [Schurkopplung](../../../research/x-c1/canonical-schur-coupling-2026-09-30/README.md) enthalten. Sie benötigen keine erneute Ergebnispromotion. |
| Y68, adaptive und direkte Linienrechnung, Y-Kernel und H₀-Folgepakete | Integrierte Ergebniskette bis PR #206/#210. Ihr historisches `UNRESOLVED` und die eng begrenzten positiven Teilbefunde bleiben unterscheidbar. Die aktuellen offenen Fragen stehen in [NEXT_GATES](../../NEXT_GATES.md). |
| Vorwärts-Schur-Spezifikation, Kreuzformpilot, 764-Einträge-Prüfung, vier Antwortvorschläge und vollständige Residuen vom 4. Oktober | Wesentliche Eingaben waren bereits im [Vier-Quellen-Anschluss](../../../research/x-c1/a8-four-source-inverse-energy-2026-10-04/README.md) gebunden. Die vollständigen Vorstufen und ergänzenden Gegenprüfungen sind nun ebenfalls auffindbar. Die Windows-LF-Korrektur bleibt von mathematischen Änderungen getrennt. |
| Kurze Acht-Quellen-Prüfung vom 5. Oktober | Kleine zusätzliche Prüfquittung; das vollständige Acht-Quellen-Paket und die Folgearbeiten sind durch [PR #213/#214](../../integrationsnachweise/PR213_2026-10-07.md) integriert. |

## Reichweite dieses Abgleichs

Der Abgleich umfasst zugängliche lokale Objekt-X-Ausgaben aus den
Arbeitsverzeichnissen vom 17. September bis 7. Oktober, die ausgewählten
Objekt-X-Archive und 23 einzelne Projekttexte im Downloadverzeichnis sowie
die einschlägigen jüngsten
Gesprächsübergaben. Ältere GitHub-Arbeit ist über PR-Historie und die bereits
integrierten [Archivfamilien](../../ARCHIVE_INDEX.md) eingeordnet.

Zusätzlich wurden 29 lokale Repository-Arbeitskopien und alle 214 bis zur
Vergleichsbasis vorhandenen Pull Requests inventarisiert. In den alten
Arbeitskopien vom 17./19. September sind 276 geänderte oder unversionierte
Dateien bereits bytegleich auf Main vorhanden; zwei weitere Originaltexte
stehen vollständig hinter ihren heutigen historischen Hinweisen. Der lokale
Vorbereitungscommit `f34c3d6118d9a7e14337abe4d096684952fa9b93` enthält eine
ausführlichere frühere Berichtsfassung und eine frühere Codefassung, die
zusätzlich erhalten werden. Ein weiterer lokaler Commit ist nur ein früherer
Integrationsversuch für die inzwischen gemergten PRs #161/#162. Die übrigen
alten unversionierten Dateien sind Python-Zwischenspeicher. Diese
Arbeitskopien werden weder zurückgesetzt noch gelöscht.

Am Vergleichsstand sind sechs weitere Remote-Arbeitsbranches vollständig
in Main enthalten. Ihre Existenz bedeutet keinen ausstehenden Inhaltstransfer.
Sie werden durch diesen Quellenabgleich nicht gelöscht.

Dies ist **keine vollständige Durchsicht aller jemals geführten Chats**,
keine neue Prüfung sämtlicher historischen Beweise und kein erneuter Lauf
der archivierten Rechenprogramme. Nicht zugängliche oder nicht als
Forschungsausgabe erkennbare Inhalte sind nicht erfasst. Entwürfe werden
durch ihre Erhaltung nicht zu registrierten Resultaten.

PR #187 bleibt die ausdrücklich offene q11/A13-Vorbereitung. Der geschützte
Auditanker und die 102 bestehenden Tags werden durch diesen Nachtrag nicht
verändert. Die 55 registrierten Resultate, ihre Beweisanker und der globale
mathematische Verifikationssnapshot bleiben unverändert. Die sechs Größen
des vollständigen Restpiloten werden hier nicht berechnet oder geschlossen.

## Byteprüfung und Abnahme

Vom Repository-Stamm genügt Python 3.13 mit Standardbibliothek und Git:

```text
python -B 00-uebersicht/archiv/LOCAL_HANDOFF_RECOVERY_2026-10-07/verify_recovery.py
```

Der [Prüfer](verify_recovery.py) liest die gepinnte Main-Basis aus der
Git-Historie und prüft die erhaltenen Bytes gegen den fest eingefrorenen
Katalog-Hash. Änderungen der Mitgliedsliste werden damit zurückgewiesen.
Er führt keine archivierten Programme aus. Im Standardlauf bleibt
`original_container_bytes_verified: false`: Die ursprünglichen ZIPs sind
für diesen Lauf keine Eingaben, ihre historische Vollständigkeit ist eine
übernommene Katalogbindung.

Mit den lokal erhaltenen Originalen lässt sich zusätzlich die vollständige
Containerzuordnung einschließlich aller Mitgliedsnamen, Größen und Hashes
direkt prüfen:

```text
python -B 00-uebersicht/archiv/LOCAL_HANDOFF_RECOVERY_2026-10-07/verify_recovery.py --originals ORIGINAL_ZIP_LOCATIONS.json
```

Diese lokale JSON-Datei ordnet jedem ursprünglichen äußeren ZIP-Hash seinen
Dateipfad zu. Sie enthält keine Beglaubigung: Der Prüfer liest und hasht die
Originalbytes und öffnet auch die verschachtelten Container. Lokale Pfade
werden nicht veröffentlicht. Die [Ausführungsquittung](SOURCE_CHECK.json)
dokumentiert den tatsächlichen Lauf mit allen 43 katalogisierten Originalcontainern.

Ein `PASS_SOURCE_BYTES` bestätigt jeweils den ausgewiesenen Byteprüfumfang,
keine mathematische Aussage. Historische
Manifestausnahmen oder früher dokumentierte Fehler werden dadurch nicht
rückwirkend aufgehoben.

Pflichtprüfungen für diesen Nachtrag: Bytezuordnung einschließlich
beschädigter Quell-/Katalogkontrollen, Links der geänderten Einstiege,
unveränderte Ergebnis- und Verifikationsfelder, deterministische
Statusansichten, Registry-Tests, historische Frontprüfung sowie die
anwendbare PR- und Main-CI. Änderungsklassen: Dokumentation und technische
Quellenerhaltung. Es werden keine mathematischen Behauptungen promotet und
keine bisherigen Zertifikatsprogramme ersetzt.
