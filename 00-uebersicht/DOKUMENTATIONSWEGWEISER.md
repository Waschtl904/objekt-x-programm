# Dokumentation lesen und einordnen

**Projektpriorität:** Zuerst Objekt X gemäß seiner vollständigen Arbeitsdefinition
konstruieren, danach den möglichen RH-Anschluss verfolgen. Die
[Forschungsstrategie](OBJEKT_X_FORSCHUNGSSTRATEGIE.md) begründet die konstruktive
Fortsetzung als Hauptaufgabe; [NEXT_GATES](NEXT_GATES.md) enthält die operative Reihenfolge.

Das Repository enthält eine laufende mathematische Untersuchung und ihre
Entstehungsgeschichte. Für den Einstieg genügt eine kurze Lesestrecke; die
historischen Dateien werden erst für konkrete Herkunftsfragen benötigt.

## Welcher Einstieg passt?

| Ziel | Lesestrecke |
| --- | --- |
| Erster Überblick | [README](../README.md) → [Gesamtüberblick](OBJEKT_X_GESAMTUEBERBLICK.md) |
| Fachliche Begutachtung | [Reviewleitfaden](EXTERNE_BEGUTACHTUNG.md) → [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md) → [Architektur](OBJEKT_X_ARCHITECTURE.md) → Beweispakete |
| Aktuellen Stand prüfen | [CURRENT_STATE](CURRENT_STATE.md) → [SURVIVOR_REGISTRY](SURVIVOR_REGISTRY.md) → [RESEARCH_STATE](RESEARCH_STATE.yaml) |
| Forschung fortsetzen | [NEXT_GATES](NEXT_GATES.md) → betroffene Quellen → [CONTRIBUTING](../CONTRIBUTING.md) |
| Ein Ergebnis reproduzieren | Ergebnis im Register wählen → Paket-README → Beweis, Quellenbindungen und Reproduktionsanleitung |
| Entwicklung nachvollziehen | [Archiveinstieg](ARCHIVE_INDEX.md) → datiertes Original und zugehörige Korrekturen |

## Welche Quelle beantwortet welche Frage?

| Quelle | Rolle |
| --- | --- |
| Arbeitsdefinition | Anforderungen an Objekt X und an seine globale Identifikation |
| Architektur und Gesamtüberblick | Erklärung der Begriffe und Zusammenhänge; keine zusätzliche Beweisautorität |
| `RESEARCH_STATE.yaml` | Operativer Status, Geltungsbereiche, Abhängigkeiten, Beweisanker und Reviewstatus |
| `CURRENT_STATE.md`, `NEXT_GATES.md`, `SURVIVOR_REGISTRY.md` | Aus dem Register erzeugte lesbare Ansichten |
| Gepinnte Beweispakete | Mathematische Aussagen, Voraussetzungen und Herleitungen |
| Zertifikate, Skripte und CI-Belege | Jeweils ausgewiesene Rechen- und Integrationsprüfung |
| Datierte Audits und Archive | Prüfumfang, Korrekturen und Entwicklung zum damaligen Zeitpunkt |

Ein Merge, eine neue Datei oder ein erfolgreicher CI-Lauf ändert für sich
genommen keinen mathematischen Reviewstatus. Der Registereintrag und der
konkrete Beweis sind gemeinsam zu lesen.

## Karte des Repositorys

| Bereich | Inhalt und Verwendung |
| --- | --- |
| [`00-uebersicht/`](.) | Aktuelle Orientierung und Statusansichten, daneben datierte Übersichten und Audits |
| [`research/x-c1/`](../research/x-c1/) | C1-Beweispakete mit Quellenbindungen, Daten, Zertifikaten und Reproduktionsanleitungen |
| [`research/`](../research/) | Weitere Forschungs- und Integrationspakete; Status jeweils über das Register prüfen |
| [`papers/`](../papers/README_papers.md) | Synthese-Manuskripte P01–P12; der Index und seine Reifestufen haben eigene Datierungen |
| [`00-grundlegung/`](../00-grundlegung/) und Themenstränge `01`–`07` | Grundlagen und gewachsene Forschungsnotizen; Zugang über den [Archivindex](ARCHIVE_INDEX.md) |
| [`audits/`](../audits/) und [`consolidation/`](../consolidation/) | Datierte Prüf-, Korrektur- und Konsolidierungsunterlagen |
| [`scripts/`](../scripts/), [`tests/`](../tests/), [`.github/workflows/`](../.github/workflows/) | Rechenwerkzeuge, Prüfungen und automatisierte Abläufe; mathematische Certifier sind Teil ihrer Beweispakete |
| Dateien im Stammverzeichnis | Einstieg, Mitarbeit, Zitation, Lizenz und Integrität sowie zwei durch Prüfskripte gebundene historische Einstiege |
| [Frühere Root-Dateien](archiv/root-journal-2026-10-03/README.md) | Verlegte Journal-Audits, Zwischenbilanzen, Protokolle und historische Übersichten mit alten und neuen Pfaden |

Die [Registry-Pflege](RESEARCH_STATE_MAINTENANCE.md) beschreibt, wie neue
Ergebnisse und ihre Belege aufgenommen werden. Die
[offenen Pull Requests](https://github.com/Waschtl904/objekt-x-programm/pulls)
zeigen Vorschläge außerhalb des integrierten Hauptstands.

Der [Abgleich lokaler Übergaben vom 7. Oktober](archiv/LOCAL_HANDOFF_RECOVERY_2026-10-07/README.md)
zeigt, welche früheren Prüfpakete bereits integriert oder in Folgepaketen
enthalten waren und welche Originaldateien zusätzlich gesichert wurden.
Der Katalog bewahrt auch frühere Vorschläge und Korrekturen als Geschichte.

## Historische Angaben richtig lesen

`CURRENT-FRONT.md`, `EINSTIEGSPROMPT.md`, `STATUS.md`, `OFFENE_PROBLEME.md`,
ältere Roadmaps und Themenregister beschreiben ihre datierten Arbeitsstände.
Wörter wie „aktuell“, „offen“, „geschlossen“, `FROZEN` oder `PUB` müssen in
diesem Kontext gelesen werden. Dasselbe gilt für frühere Dokumentzahlen.

Originale bleiben als Belege erhalten. Ein `LOCAL_UNMERGED` in einem älteren
Paket kann dessen ursprünglichen Veröffentlichungsstand meinen; eine spätere
Integration ist im Register verzeichnet. Beispiel: Das
[Direct-Line-Paket](../research/x-c1/canonical-direct-odd-line-2026-10-02/README.md)
wurde durch [PR #204](https://github.com/Waschtl904/objekt-x-programm/pull/204)
integriert, während seine Originalberichte ihre damaligen Angaben behalten.

Die Pfadnachweise des [ersten](archiv/root-journal-2026-10-03/MIGRATION.md) und
[zweiten Umzugs](archiv/root-navigation-2026-10-03/MIGRATION.md) führen von alten
Dateinamen zu ihrer heutigen Ablage. Originalfassungen bleiben erhalten;
Lesefassungen haben angepasste Links und ausdrücklich getrennte heutige Hinweise.
Der [historische Journalindex](archiv/root-navigation-2026-10-03/INDEX.md)
erschließt den früheren Bestand. Die [Importgeschichte](HERKUNFT.md) erklärt seine Herkunft.

Das [Glossar](GLOSSAR.md) unterscheidet die heutige Arbeitsdefinition von
älteren Kandidatenbegriffen. Der
[Dokumentationsaudit vom 2. Oktober](DOKUMENTATIONSAUDIT_2026-10-02.md) erklärt
relative Verweise in Archivkopien, die noch auf damalige Arbeitsverzeichnisse
zeigen. Dafür sind die heutigen Paket-Einstiege zu verwenden.

Der [Branch-Bereinigungsnachweis](BRANCH_HYGIENE_2026-10-02.md) dokumentiert
eine abgeschlossene Bereinigung. Seine Branch- und Tagzahlen sind datierte
Beobachtungen; sie sind keine laufende Bestandsanzeige.
