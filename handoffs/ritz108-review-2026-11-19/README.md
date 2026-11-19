# Objekt X: lesende Übergabe des Wiederholungslaufs vom 19. November 2026

Dieser Ordner stellt bereits vorhandene Artefakte zur lesenden Prüfung bereit.
Die Veröffentlichung führt keine Rechnung aus und trifft keine neue mathematische
Statusentscheidung. Maßgeblich bleibt **CONDITIONAL_NONRIGOROUS_RITZ_LOWER_VALUE**.
Native Herkunft der q-Lösung und statische GPT1-Abnahme sind offen. Die
Erstspaltenkontrolle ist kein q-Fehlernachweis. Es gibt keine obere Schranke der
vollständigen zweiten Restenergie, keinen Routenstopp und kein Zertifikat.

## Einstieg für die Prüfung

1. [Ergebnisbericht](ERGEBNIS.txt) und [strukturierter Bericht](ERGEBNIS.json).
2. [Tatsächlich ausgeführtes Skript](single_measurement.py), [Startparameter vor
   dem Start](START.json) und [vom Rechenskript geschriebene Startparameter](raw/START.json).
3. [Unverändertes Rohprotokoll](raw/SINGLE_RUN.log), [rohe Ergebnisausgabe](raw/RESULT.json)
   und [Prozessende](PROCESS_END.json).
4. [Eingangsmanifest mit Einzelhashes](RUN_BINDINGS.json),
   [Herkunftsbindungen der extrahierten Eingaben](ASSET_BINDINGS.json),
   [Identitäten der übergebenen Methodenprüfung](INPUT_IDENTITIES.json) und
   [Bibliotheks-Dateimanifest](DEPENDENCIES_MANIFEST.json).
5. [Skript des Erstversuchs](comparison/2026-11-18/single_measurement.py),
   [dessen Startparameter](comparison/2026-11-18/START.json),
   [dessen Abbruchprotokoll](comparison/2026-11-18/SINGLE_RUN.log) und
   [vorhandener Änderungsdiff](ONLY_CHANGE.diff).

Die Rückersetzung der drei Vorkommen von `14400` durch `1800` im ausgeführten
Skript stellt den Erstversuch bytegleich her. Es handelt sich um die Laufgrenze,
ihre Fehlermeldung und den START-Metadateneintrag. Präzision, Panels, Knoten,
Toleranzen und der über die gebundene Eingabedatei geladene Projektionskoeffizient
wurden nicht verändert. Dieser Vergleich ist eine Dateiprüfung, kein Rechenlauf.

## Rohdaten ohne ZIP lesen

Das [komprimierte Original](raw/ASSEMBLED_VECTORS.json.gz) bleibt bytegleich
erhalten. [ASSEMBLED_VECTORS.json](raw/ASSEMBLED_VECTORS.json) ist ausschließlich
seine unveränderte GZIP-Dekompression. Diese große Datei kann für eine Webansicht
zu umfangreich sein. Deshalb gibt es zusätzlich kleinere, abgeleitete Lesedateien:

- [erste rekonstruierte Spalte](readable/ASSEMBLED_VECTORS/first.json),
- [zweite Spalte](readable/ASSEMBLED_VECTORS/second.json),
- [Phi_g](readable/ASSEMBLED_VECTORS/Phi_g.json),
- [mc_g](readable/ASSEMBLED_VECTORS/mc_g.json),
- [Index der V-Zeilenblöcke](readable/ASSEMBLED_VECTORS/INDEX.json).

Die V-Matrix wird in 32 Dateien mit höchstens sechs Zeilen aufgeteilt. Indizes
sind nullbasiert. Die gespeicherten Ganzzahlen der Ball-Tupel bleiben exakt
erhalten; es wurden keine Dezimalwerte, Radien, Paarungen oder Energien neu
berechnet. Die wieder zusammengesetzten JSON-Werte wurden auf Gleichheit mit
dem Original-Payload geprüft. [DECOMPRESSION_MAP.json](DECOMPRESSION_MAP.json)
bindet Original, Dekompression und Leseaufteilung. Diese Zusatzdateien sind
ausdrücklich Lesedarstellungen, keine neuen Originalmessdaten.

## Originalbytes und Aussagegrenzen

Alle 24 Dateien des vorhandenen Wiederholungspakets einschließlich seines
[MANIFEST.json](MANIFEST.json) sind unverändert übernommen. Drei Originaldateien
des Erstversuchs ergänzen den Vergleich. Das ursprüngliche MANIFEST deckt nur
seinen damaligen Bestand ab; das [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json)
bindet den gesamten heutigen Übergabebestand, ausgenommen sich selbst.
[FILE_LIST.txt](FILE_LIST.txt) nennt sämtliche Zielpfade einschließlich dieses
Veröffentlichungsmanifests. Es erfolgt keine stille Ersetzung älterer Manifeste.
Die lokale `.gitattributes` verhindert Git-Textkonvertierung und Filter innerhalb
dieses Ordners. Unveränderte Originale wurden weder formatiert noch bereinigt.

Die alten internen Statusnamen des Rohskripts, insbesondere `DIAGNOSTIC_ROUTE_OPEN`,
sind keine Freigabe einer Route. Maßgeblich ist die ausdrücklich bedingte
Einordnung in ERGEBNIS.txt und ERGEBNIS.json. Die angezeigte Arithmetikgenauigkeit
ist keine Einschließung der Quadratur-, Modell- oder physischen q-Fehler.
Auch ein Unterwert unter 0,2573 beweist nicht, dass die vollständige Restenergie
unter dieser Schwelle liegt. Eine neue statische GPT1-Abnahme wird nicht behauptet.

## Was ausschließlich lokal verbleibt

Die großen mathematischen Originaleingaben, die in RUN_BINDINGS.json mit absoluten
Windows-Pfaden und SHA256 bezeichnet sind, werden mit dieser Übergabe nicht neu
hochgeladen. Dazu gehören insbesondere COMMON_BANK_109.json.gz,
FIRST_COLUMN_COORDINATES.json, SECOND_SCALAR_RESULT.json, INVERSE_DATA.json,
SHARP_FORCE_SOLUTION_NATIVE.json.gz, PREPARED_CORE.json.gz, QUELLEN_NATIVE.json.gz,
historical_pairs.raw und die weiteren mathematischen `assets/*.raw`.
Etwaige bereits bestehende öffentliche Kopien werden hiermit weder neu geprüft
noch als Vollständigkeitsersatz behauptet. Die Eingangsbindung ist keine Schließung
der ausdrücklich offenen nativen Herkunft der q-Lösung.

Der installierte Python-Laufzeitbestand, die Dateien unter `deps/` (insbesondere
python-flint, mpmath und native Bibliotheken), die ursprünglichen Downloads/PDFs
und ZIP-Dateien sowie die privaten Arbeitsverzeichnisse verbleiben lokal.
DEPENDENCIES_MANIFEST.json veröffentlicht nur Bibliotheks-Dateinamen, Größen und
Hashes. Das Rechenskript verlangt python-flint 0.9.0; es wird hier nicht erneut
ausgeführt. Die vier beigefügten Hilfsmodule unter assets/ sind Originaldateien
aus dem vorhandenen Übergabepaket. Dieses Verzeichnis ist Prüfmaterial und kein
vollständig lauffähiges Reproduktionspaket. Fehlende Eingaben wurden nicht aus
Berichten rekonstruiert.

## Veröffentlichungsumfang

Ziel: `Waschtl904/objekt-x-programm`, separater Branch
`handoff/ritz108-review-2026-11-19`, ausschließlich dieser neue Übergabeordner.
Basis ist `a98703b90f7ff620656870932c61060e8b340d42`. Bestehende Projektdateien,
Register, Aussagen und Workflows bleiben unverändert. Ein Branch-Push ist keine
Integration in main. Es wird kein PR, Merge, Release oder manueller Workflow
beauftragt. Der vorhandene allgemeine Metadaten-Workflow kann auf einen Push
reagieren; dies ist kein neuer mathematischer Messlauf und keine Abnahme.

Die Originaldateien enthalten lokale Pfade mit dem Windows-Benutzernamen `sebas`
sowie lokale Dateinamen und Anhangskennungen. Diese Angaben werden zur Wahrung
der Originalbytes nicht stillschweigend entfernt und sind Teil des ausdrücklich
vorzulegenden öffentlichen Uploadumfangs. Die vorgeschaltete Inhaltsprüfung ist
in [SAFETY_SCAN.json](SAFETY_SCAN.json) dokumentiert.

Für eine Prüfung bitte Dateilinks mit der tatsächlich veröffentlichten vollständigen
Commit-SHA verwenden. Ein Branchname bezeichnet einen beweglichen Stand.
