# Historische Quellen und Branch-Konsolidierung

Dieser Einstieg dient der Navigation. Der aktuelle Forschungsstand steht in [CURRENT_STATE.md](CURRENT_STATE.md), die nächsten mathematischen Aufgaben in [NEXT_GATES.md](NEXT_GATES.md). Maßgebliche Statusquelle bleibt [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml).

## Letzte Branch-Pflege: 2. Oktober 2026

Die [neue Bereinigungscharge](BRANCH_HYGIENE_2026-10-02.md) entfernt 23 vollständig
integrierte Arbeitsbranches. Erhalten bleiben Main, der offene q11/A13-Branch
von PR #187 und der geschützte `KEEP_AUDIT`-Anker. Alle 102 Tags bleiben
unverändert. Neu hinzukommende Arbeitsbranches sind in diesen datierten Zahlen
nicht enthalten.

## Abgeschlossener Archivierungsstand vom 26. September 2026

Die Branch-Konsolidierung vom 26. September 2026 ist abgeschlossen. Am Abschlussstand blieben zwei Remote-Branches erhalten: `main` und der als `KEEP_AUDIT` bezeichnete Branch `research/x-c1-inherited-resonance-shell-schur-2026-09-18`. Der Tagbestand betrug 102. Diese Angaben beschreiben den datierten Abschlussstand, keine automatisch aktualisierte Bestandsanzeige.

Abschlusscommit auf Main: [`dd0473868ff47b3dd918114bfc7ce48b15f3e8fd`](https://github.com/Waschtl904/objekt-x-programm/commit/dd0473868ff47b3dd918114bfc7ce48b15f3e8fd). Die sechs unten verlinkten Integrations-PRs bewahren 324 Versions-IDs mit 323 unterschiedlichen Originalblobs; 73 bereits dokumentierte Main-Zuordnungen wurden weiterverwendet. Die vollständigen Commit-Historien sind zusätzlich über die geschützten Archivtags erreichbar.

Die administrative Bereinigung schließt keine mathematischen Fragen. Historische Fassungen, Skripte und Workflowtexte bleiben historische Quellen; ihre damaligen Statusangaben werden nicht zur heutigen Forschungsfront. O8 und die kanonischen Reviewstatus werden durch die Archivierung nicht verändert.

## Originalfassungen nach Familie

| Familie | Gebundene Versions-IDs | Inhaltsbeleg | Integration |
| --- | --- | --- | --- |
| Critical-Half / PR116 / RP2 / Weyl | 89 | [Quellen und Provenienz](archiv/CRITICAL_HALF_RP2_SOURCE_PRESERVATION_2026-09-26/README.md) | [PR #166](https://github.com/Waschtl904/objekt-x-programm/pull/166) |
| A1-Audits | 11 | [Quellen und Provenienz](archiv/A1_AUDITS_SOURCE_PRESERVATION_2026-09-26/README.md) | [PR #167](https://github.com/Waschtl904/objekt-x-programm/pull/167) |
| Governance und CI | 59 | [Quellen und Provenienz](archiv/GOVERNANCE_CI_SOURCE_PRESERVATION_2026-09-26/README.md) | [PR #168](https://github.com/Waschtl904/objekt-x-programm/pull/168) |
| NP/OX | 34, davon 18 bereits im Critical-Half-Paket | [Quellen und Provenienz](archiv/NP_OX_SOURCE_PRESERVATION_2026-09-26/README.md) | [PR #169](https://github.com/Waschtl904/objekt-x-programm/pull/169) |
| Terminal / C0 / C1 | 33 | [Quellen und Provenienz](archiv/X_C0_C1_TERMINAL_SOURCE_PRESERVATION_2026-09-26/README.md) | [PR #170](https://github.com/Waschtl904/objekt-x-programm/pull/170) |
| SW1 | 116 | [Quellen und Provenienz](archiv/SW1_SOURCE_PRESERVATION_2026-09-26/README.md) | [PR #171](https://github.com/Waschtl904/objekt-x-programm/pull/171) |

Die Familienzahlen sind wegen gemeinsam verwendeter Originalfassungen nicht zu addieren. Die Quellenverzeichnisse binden Originalpfad, Quellcommit, Blob, SHA-256 und die vollständig erhaltenen Nutzdaten.

## Bereits zuvor integrierte Einzelfälle

- [Integrität: Einordnung der elf historischen Fassungen](archiv/INTEGRITY_CONTENT_RECONCILIATION_2026-09-25.md). Inhaltstransfer und Historienabsicherung sind getrennte Nachweise.
- [R43: drei historische Originalfassungen](archiv/R43_CONTENT_RECONCILIATION_2026-09-26/README.md). Unabhängiger mathematischer Review bleibt offen.

## Datierte Register und Vorbereitungsstände

Die folgenden Unterlagen bleiben unverändert als Belege ihrer jeweiligen Zeitpunkte erhalten. Frühere Branchzahlen, `HOLD`-Einträge oder noch offene Archivierungsmaßnahmen darin sind keine aktuelle Liste noch zu löschender Branches. Die ursprünglichen Entscheidungen und Prüfgrenzen bleiben nachlesbar.

- [Historisches Inhaltsregister, 23. September](archiv/HISTORICAL_CONTENT_REGISTER_2026-09-23.md)
- [Historische Entscheidungsmatrix, 23. September](archiv/HISTORICAL_CONTENT_DECISION_MATRIX_2026-09-23.md)
- [Familienprüfung der damaligen 58 Unique-Branches, 24. September](archiv/UNIQUE_BRANCH_FAMILY_REVIEW_2026-09-24.md)
- [Inhaltskarte der historischen Fassungen, 24. September](archiv/UNIQUE_BRANCH_CONTENT_MAP_2026-09-24.json)
- [Archivmanifest der ursprünglichen 21er-Charge, 25. September](ARCHIVE_MANIFEST_2026-09-25.md) · [JSON](ARCHIVE_MANIFEST_2026-09-25.json)

Die datierten Manifest- und Quellenbytes werden durch diesen Einstieg nicht ersetzt oder umgeschrieben. Gesicherte Archivtags und mathematische Beweisanker bleiben unverändert.
