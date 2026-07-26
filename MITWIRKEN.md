# Mitwirken und Herkunft

## Herkunft dieses Repositories

Dieses Repository ist die kuratierte öffentliche Fassung eines privaten Forschungsjournals
(`rh-fragenkatalog`), das zwischen 2025 und Juli 2026 entstanden ist.

**Was übernommen wurde:** alle 324 Forschungsdokumente, inhaltlich unverändert.

**Was neu ist:**

- **Thematische Gliederung.** Statt der historischen Zweiteilung in `katalog/` und
  `werkzeuge/` — die dieselbe Nummernfolge NEU-3 bis NEU-221 auf zwei Ordner verteilte —
  liegen die Dokumente jetzt in neun thematischen Strängen mit durchgehender Nummerierung.
- **Vereinheitlichte Dateinamen.** Alle Namen folgen dem Muster `NEU-NNN[suffix]_Titel.md`
  mit dreistelliger, nullaufgefüllter Nummer, damit die Verzeichnissortierung der
  Journalreihenfolge entspricht. Die **Katalog-ID im Text bleibt unverändert**: die Datei
  `NEU-058_...` gehört zum Eintrag NEU-58.
- **ASCII-Dateinamen.** Umlaute und ein fehlerhaft kodiertes kyrillisches Zeichen in sechs
  Dateinamen wurden bereinigt (`ä` → `ae` usw.). Der Dateiinhalt ist davon nicht betroffen.
- **Navigationsebene.** [README](README.md), [Gesamtindex](INDEX.md),
  [Statusregister](STATUS.md), [Glossar](GLOSSAR.md) und eine Übersicht je Strang.
- **Reparierte Querverweise.** Relative Links zwischen Dokumenten wurden auf die neue
  Struktur umgeschrieben.
- **Lizenz und Zitierangaben.** [CC BY 4.0](LICENSE), [CITATION.cff](CITATION.cff).

Was **nicht** verändert wurde: der Text der Forschungsdokumente, ihre Statusmarken, ihre
Beweise und ihre Fehler. Nummernkollisionen und bewusste Kataloglücken wurden nicht
"aufgeräumt", sondern in [STATUS.md](STATUS.md) dokumentiert — sie gehören zur
Prozessgeschichte.

---

## Wie Sie beitragen können

Dieses Programm arbeitet lakatosianisch: Ein Gegenbeispiel ist wertvoller als eine
Zustimmung. Besonders willkommen sind

- **Fehlernachweise** in Beweisen, die als `✓ [M]` markiert sind,
- **Gegenbeispiele** zu konditionalen Resultaten `⚠ [M]`,
- **Quellenhinweise** auf bereits bekannte Resultate, die einen offenen Knoten schließen
  oder ein No-Go verschärfen,
- **Verschärfungen** bestehender No-Gos,
- **Konstruktionen** für einen der offenen Knoten aus [OFFENE_PROBLEME.md](OFFENE_PROBLEME.md).

### Vorgehen

Bitte über **Issues**. Ein nützliches Issue nennt

1. die betroffene **Katalog-ID** (z. B. NEU-219u) und, falls vorhanden, den **Knoten** (z. B. `[O-219-5e1h]`),
2. die genaue Stelle — Abschnittsnummer oder zitierte Formel,
3. den Einwand oder Beitrag,
4. die daraus folgende **Statusänderung**, sofern eine vorliegt (etwa `✓ [M]` → `✗ [M]`).

Bei Pull Requests: Der Dokumenttext ist ein Journal, keine Reinschrift. Korrekturen werden
als **neuer Revisionsabschnitt oder neuer Eintrag** geführt, nicht durch stilles
Überschreiben — nachvollziehbare Fehlerkorrektur ist der Kern der Methode. Bestehende
Aussagen werden also markiert und widerlegt, nicht gelöscht.

### Statusmarken korrekt setzen

| Marke | Wann |
|---|---|
| `✓ [M]` | vollständiger Beweis liegt im Dokument selbst vor |
| `✓ [K]` | Objekt ist konstruiert und typgeprüft, Konsequenzen noch offen |
| `⚠ [M]` | Beweis vollständig, aber unter einer explizit benannten offenen Voraussetzung |
| `✗ [M]` | Route gesichert ausgeschlossen; das Hindernis ist benannt |
| `❓ [O]` | offen; die Frage ist präzise formuliert und mit Knoten-ID versehen |

Rechenregeln für die BC-Algebra sind in [KONVENTIONEN.md](KONVENTIONEN.md) verbindlich
festgelegt. Bei Widersprüchen zwischen einem Katalogeintrag und den Konventionen hat die
Konventionsdatei Vorrang.

---

## Haftungsausschluss

Die Dokumente sind **nicht peer-reviewed** und enthalten **keinen Beweis der Riemannschen
Hypothese**. Einige als gesichert markierte Aussagen wurden im Laufe des Programms durch
spätere Audits korrigiert oder zurückgerollt; solche Fälle sind im
[CHANGELOG](CHANGELOG.md) und in den Auditdateien nachvollziehbar. Wer Resultate von hier
weiterverwendet, sollte den zugehörigen Beweis eigenständig prüfen.
