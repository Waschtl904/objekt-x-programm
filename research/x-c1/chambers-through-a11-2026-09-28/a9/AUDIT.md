# A9-Abnahmeprotokoll

27. September 2026 · lokale Forschung · externe Prüfung offen

## Ergebnis und Pflichtprüfungen

Die neue analytische Vorbereitung wurde vor dem vollen Modellaufbau erstellt
und mit 72 exakten Kontrollen abgeschlossen. Anschließend wurden die
sechs neuen Zellen am kleinen Modell durch 239 Vergleiche geprüft. Erst nach
diesem Erfolg wurde das vollständige Modell mit N=593, M=224 und 3072 Bit
berechnet. Die vollständige Kopplung und sämtliche Fehlerterme wurden danach
aus den gespeicherten Dateien geprüft.

Beide Arb-Läufe haben je 296 positive Pivots; die unabhängige Ganzzahlarithmetik
bestätigt sämtliche Pivots, die Matrixeinschließung, die inverse Spur und die
gemeinsamen rationalen Reserven. Arb meldet 21 Prüfgruppen,
der unabhängige Prüfer 37.
Kein fehlgeschlagener Pflichtcheck wurde aus dem Ergebnis entfernt oder zum
optionalen Check umklassifiziert.

Gemeinsamer physischer Boden: `1/100000000000000000000000000000000000`.
Gemeinsamer Defektboden: `1/1200000000000000000000000000000000001`.

## Unabhängigkeit und Grenzen

- Der volle Integralaufbau verwendet eine explizite A9-Anpassung des gepinnten
  O8-Programms. `ENGINE_ADAPTATION.diff` dokumentiert diese Änderungen.
- Der kleine Gegencheck setzt die volle Funktion V−Gamma−S anders zusammen
  und kontrolliert Normierungen und Kanäle. Einige Polynomialroutinen werden
  gemeinsam genutzt. Dies ist kein zweiter unabhängiger Vollaufbau bei Grad 593.
- Der Ganzzahlprüfer importiert weder Arb noch die gelieferten Rechenprogramme.
  Er rekonstruiert den Gamma-Residualfehler direkt aus dem gespeicherten
  rationalen Polynom, bildet die bezahlte Untermatrix selbst und prüft die LDL-
  Zerlegung mit nach außen gerundeten Ganzzahlintervallen.
- Der analytische Nachweis von Formdomäne, Gamma-Identität, vollständiger
  Gramrepräsentation und Operatortransporten bleibt Gegenstand externer Prüfung.
  Ein endlicher Zertifikatslauf ersetzt diese Argumente nicht.

## Quellen und Erhalt

`SOURCE_BINDINGS.json` bindet sieben mathematische Repository-Eingaben;
alle wurden aus ihren Commits gelesen und geprüft. Die lokale O10-Herleitung
und der rationale Helfer sind bytegleich übernommen.
`ENGINE_BINDINGS.json` bindet vier weitere veröffentlichte Programmquellen
und ihre lokalen Anpassungen. Die Repository-Lizenz wurde unverändert kopiert.

Der Repository-Arbeitsbaum wurde nicht bearbeitet. Es wurden keine Branches,
Tags, Statusdateien oder historischen Beweise verändert. Eine Veröffentlichung,
CI-Abnahme oder Integration dieses neuen A9-Pakets wird nicht behauptet.
Der zwischenzeitliche Main-Commit aus PR #176 wurde inhaltlich gelesen;
`MAIN_COMPATIBILITY.md` dokumentiert den Abgleich der Fourierorientierung
und des logarithmischen Lifts mit den konkreten A9-Eingaben.

## Nachvollziehbarkeit

`build.log` protokolliert den tatsächlich ausgeführten vollständigen Aufbau.
`ENVIRONMENT.json` nennt die tatsächlich verwendeten Laufzeitversionen.
Die Paketprüfung kontrolliert die komplette Kette aus Beweisquittung,
Modellhash, Fehlerprüfung, rationaler Reserve und unabhängigem Rechenergebnis.
`SHA256SUMS` bindet die gelieferten Dateien; das ZIP wird auf Inhalt und
Dateihashes geprüft.
