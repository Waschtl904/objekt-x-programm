# Tatsächlicher Integrationsprüfumfang — 11. November 2026

Die technischen Checks ändern keine mathematische Aussage und ersetzen
GPT1s noch ausstehendes Integrationsvotum nicht.

## Bestanden

- Acht vorhandene Originalarchive einschließlich des 245.913.425-Byte-
  Release-Assets nach Größe und SHA256 geprüft.
- 34 Lesefassungen mit ihren konkreten Original-Archivmitgliedern bytegleich.
- Paketmanifest, Statusgrenzen und portabler rationaler Zweitspalten-Zahlenschluss
  geprüft; gespeichertes Ergebnis vollständig gleich. Keine neue q-Auswertung.
- Sechs Schutztests gegen beschädigte Originalbytes, nicht deklarierte Dateien,
  falsche Zweitspalten-/Herkunftsabschlüsse, verwechselte Abnahmen und zirkuläre
  A11-Eingaben bestanden.
- Generatorprüfung, Registry-Validierung mit Basis
  `eff257c6853c41179dbb0e99adfb699208473869` und Active-Front-Check bestanden.
- 112 lokale Markdown-Links und fünf relevante/irrelevante Workflow-Pfadfälle
  geprüft. Neue Workflow-Actions sind gepinnt; Berechtigung `contents: read`.
- Die bereits im Register gepinnte historische Integrations-CI wurde online
  bestätigt: Lauf 40196047159, Versuch 1, Head
  `344c1f4787900003dc57203987222bad91828fe3`. Das ist keine neue PR-CI.

## Vollständige Registry-Tests: lokaler Plattformfehler, kein PASS

Der unveränderte vorhandene Testsatz führte unter Windows 76 Tests aus:
73 bestanden, 3 scheiterten. Konkrete Ursachen:

1. `test_nonregular_target_is_rejected`: `os.mkfifo` ist auf diesem Windows
   nicht vorhanden.
2. `test_symlink_file_parent_and_registry_are_rejected`: Windows verweigert
   der Testumgebung das Symlink-Recht (WinError 1314).
3. `test_reference_copy_cannot_be_active_pending_or_have_meta`: Die Fixture
   erzeugt Windows-Backslashes und erhält deshalb zuerst den erwartbaren
   Sicherheitsfehler für einen unzulässigen Repositorypfad; ihr Linux-
   Fehlermuster passt anschließend nicht.

Die Tests und Validatoren wurden nicht geändert oder abgeschwächt. Eine
vorhandene lokale Linux-Engine war nicht verfügbar. Der vollständige
unveränderte Linux-Testsatz bleibt verpflichtend für die spätere PR-CI.
Ein lokaler Gesamt-PASS oder bereits erfolgreicher neuer CI-Lauf wird nicht
behauptet. Der anfängliche reine Zeilenendenfehler in der Registerdatei wurde
behoben; Originaldateien wurden dafür nicht verändert.

## Noch ausstehend

- GPT1-Prüfung der mathematischen Aussagegrenzen und Belegzuordnung dieses Bestands.
- Öffentliche Freigabe; neuer PR und dessen gesamte anwendbare CI.
- Gesonderte Freigabe eines konkreten mergefähigen PR-Heads.
- Fehlende Ergebnisabnahme-/Zweitspaltenoriginale, drei native Herkunftsbindungen
  und ganze physische zweite Restenergie bleiben inhaltlich offen.

Die frühere Erstspaltenrechnung, das Budgetzertifikat und historische
Großrechnungen wurden in diesem Integrationsschritt nicht erneut ausgeführt.
