# Dokumentationsaudit vom 2. Oktober 2026

Geprüfte Ausgangsbasis: `95a916a18b3b61d239b52cc15c2ee6c420980a94`.

## Umfang und Befund

Der Bestandslauf erfasst **1.559 Markdown-Dateien**. Geprüft wurden die
Navigation, relative Dateilinks, GitHub-Verweise auf gelöschte Branches und
die Trennung aktueller Statusquellen von historischen Berichten. Die aktiven
Einstiegsseiten, die Themenregister und die betroffenen Quellpassagen wurden
zusätzlich inhaltlich auf ihre Navigationsrolle gelesen.

Das ist kein erneuter mathematischer Gesamtaudit aller Forschungsbeweise.
Externe Literatur-URLs und sämtliche historischen Abschnittsanker wurden
nicht vollständig online geprüft. Die vorhandenen Registry-Validatoren
prüfen weiterhin die gebundenen Belege und historischen Originale.

| Befund | Nachpflege |
| --- | --- |
| README und Gesamtüberblick enthalten den integrierten adaptiven Gate, aber Einstieg und lokaler Folgestand sind schwer zu unterscheiden. | Kurzübersicht und [Dokumentationswegweiser](DOKUMENTATIONSWEGWEISER.md); das lokale Linienpaket bleibt ausdrücklich außerhalb der Registry. |
| STATUS und OFFENE_PROBLEME nennen ältere Arbeitsfronten. | Aktuelle Verweise vor dem erhaltenen historischen Originaltext. |
| Neun Themen-/Auditregister und der Manuskriptindex enthalten alte Zahlen und Statusangaben. | Zeitliche Einordnung und direkte Links zu den aktuellen Statusansichten. |
| Das Glossar identifiziert Objekt X noch mit dem historischen Fünfer-Tupel. | Heutige Arbeitsdefinition verlinkt; alter Kandidat als historischer Begriff erhalten. |
| MITWIRKEN verweist für neue Aufgaben auf die alte Aufgabenliste. | NEXT_GATES und der bestehende Abnahmeablauf verlinkt; Importzahl und Journalmarken zeitlich eingeordnet. |
| Sechs Links im Weil-Themenregister zeigen in den falschen Ordner. | Zielpfade zu den bereits vorhandenen Dateien im Primkanten-Ordner korrigiert. |
| Die Architekturkarte enthält beschädigte mathematische Anzeigebegrenzer. | GitHub-Mathematikblöcke hergestellt; Formeln und Geltungsbereich unverändert. |
| Der Archiveinstieg kennt nur die Branch-Konsolidierung vom 26. September. | Neue [Bereinigungscharge](BRANCH_HYGIENE_2026-10-02.md) ergänzt; der frühere Bericht bleibt datiert erhalten. |

Die operative Registry, ihre drei generierten Statusansichten, sämtliche
Forschungspakete, Beweisanker und Reviewstatus bleiben unverändert. Das
lokale Linienpaket wird durch diesen Dokumentations-PR nicht integriert.

## Relative Links in erhaltenen Originalen

Die Rohsuche liefert 109 Kandidaten. Viele sind mathematische Ausdrücke der
Form `](...)` und keine Dateilinks. 38 Treffer haben tatsächliche Dateipfade:
sechs reparierte Navigationslinks und **32 Linkvorkommen in archivierten
Berichten oder eingebetteten Originalkopien**. Diese Originalbytes werden
nicht nachträglich umgeschrieben.

| Historische Quelle | Heutige Navigation |
| --- | --- |
| [DAG_SYN vom 8. August](archiv/DAG_SYN_2026-08-08.md), zwei relative Pfade | [damalige Front](../CURRENT-FRONT.md) und [historische Theorem-Registry](ACTIVE_THEOREM_REGISTRY.md) |
| [Stand August 21–30](archiv/AKTUELLER_STAND_2026-08-21_bis_2026-08-30.md), acht relative Pfade | [Theorem-Registry](ACTIVE_THEOREM_REGISTRY.md), [P11/R32-Status](P11_R32_STATUS_2026-08-25.md), [damalige Roadmap](FORSCHUNGS_ROADMAP_2026-08-26.md), [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md) |
| [Destruktiver C6-Review](../audits/R43_C6_ROOT_ANCHOR_REVIEW_2026-09-07/destructive_review.md), 20 relative Pfade | [Paket-Einstieg mit finalen Quellen, Berichten und Prüfquittung](../audits/R43_C6_ROOT_ANCHOR_REVIEW_2026-09-07/README.md) |
| [Q9-Originalkopie im A11-Paket](../research/x-c1/chambers-through-a11-2026-09-28/a11/inputs/Q9.md), ein relativer Pfad | [allgemeines Ein-Wand-Lemma](../research/x-c1/chambers-through-a11-2026-09-28/wall/PROOF.md) |
| [A9-Originalkopie im A11-Paket](../research/x-c1/chambers-through-a11-2026-09-28/a11/inputs/A9_PROOF.md), ein relativer Pfad | [O10-Eingang im A9-Paket](../research/x-c1/chambers-through-a11-2026-09-28/a9/inputs/O10_PROOF.md) |

Im C6-Review bezeichnet `r43_global_budget_55a3/` ein damaliges lokales
Arbeitsverzeichnis. Die darunter genannten Forschungsdateien stehen heute
unter den entsprechenden Repository-Pfaden. Einige damals erwähnte lokale
JSON-/Review-Dateinamen sind unter diesem Namen nicht als Einzeldatei
veröffentlicht. Der Paket-Einstieg erschließt die tatsächlich vorhandenen
Belege; eine Gleichheit mit fehlenden Zwischenartefakten wird nicht behauptet.

## Branch- und Tagprovenienz

23 vollständig integrierte Arbeitsbranches wurden mit Zustimmung des Nutzers
gelöscht. Main, PR #187 und der geschützte Auditanker bleiben erhalten. Alle
102 Tags und die Schutzregeln sind unverändert. Die gelöschten Heads bleiben
über Main erreichbar und sind im [Bereinigungsnachweis](BRANCH_HYGIENE_2026-10-02.md)
gebunden. In den gescannten Markdown-Links wurde kein Verweis auf einen dieser
23 gelöschten Branchnamen gefunden.

## Abnahme dieses Dokumentations-PR

Verpflichtend sind die Prüfung der relativen Links aller geänderten Seiten,
der unveränderten Registry-/Beweis-/Archivbytes, der generierten Ansichten,
der Registry- und Frontvalidatoren sowie der anwendbaren PR-CI auf dem finalen
Head. Nach dem Merge wird die Main-CI geprüft. Unveränderte große
Operatorrechnungen werden durch diese Navigationspflege nicht erneut gestartet.
