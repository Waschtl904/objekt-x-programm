# Integritäts-Herkunftsbranch — gezielter Inhaltsnachtrag vom 25. September 2026

**Inhaltszuordnung, keine mathematische Statuspromotion und keine Löschfreigabe.**

Basis: `main@1cdf996470c454a7c0a79f9470bb20b48f173118`.
Herkunftsbranch: `chore/integrity-workflow-race-fix@ebaa488a17137c9a2d4eaf2576f7259cbf2bc913`.

Dieser Nachtrag präzisiert ausschließlich die elf bisherigen `TECHNICAL-INTEGRATION`-Einträge der [Inhaltskarte vom 24. September](UNIQUE_BRANCH_CONTENT_MAP_2026-09-24.json) und den zugehörigen Fall des [Familienberichts](UNIQUE_BRANCH_FAMILY_REVIEW_2026-09-24.md). Die damaligen Dateien bleiben unveränderte, an `5b5ac66b1f30b58126c7a9d0d528d240f12a26fa` gebundene Eingangssnapshots; ihre Sammelkategorie ist für diesen einen Branch zusammen mit diesem Nachtrag zu lesen. Die 19 anderweitig eingeordneten Branchfälle, 38 weiteren offenen Fälle und die früheren 138 A/B-Entscheidungen werden nicht neu bewertet.

## Geltung und Herkunft

Die sechs technischen Zuordnungen und die beiden historischen Manifestbewertungen werden aus dem vom Eigentümer übergebenen lesenden Prüfbericht vom **25. September 2026, 03:31:14 UTC** weiterverwendet. Das ist keine neue Durchführung seiner elf Hashprüfungen, der 559 Quellbindungen oder der 68 früheren Regressionstests. Die beiden fehlenden Begleittexte wurden zusätzlich direkt mit den gepinnten historischen Dateien verglichen.

Die nachstehenden Textnachfolger sind die gemeinsam mit diesem Nachtrag versionierten Dateien. Auf einem PR-Branch bedeutet das **TRANSFER_PREPARED**; erst bei Integration dieses Nachtrags samt Begleittexten in `main` bedeutet es **CONTENT_TRANSFER_INTEGRATED**. Der jeweilige PR-/Mergecommit bindet die Nachfolger ohne selbstreferenziellen Commit-Platzhalter. Die dauerhafte Sicherung der einzigartigen Branchhistorie ist davon unabhängig und bleibt vor jeder Löschung nachzuweisen.

## Elf Einzelfallentscheidungen

| ID | Quellpfad | Entscheidung und konkreter Nachfolger |
|---|---|---|
| U001 | `.canary` | Gezielter Transfer der Einschränkung eines Markerfunds; die begleitende `.canary` ist bytegleich zu Quellblob `0e609832086e22d256e55dbc3035f3dc8556a3db`. Kein Markerwert wird verändert. |
| U006 | `.github/workflows/integrity.yml` | MAIN-COVERED / SUCCESSOR durch PR #161; der ältere Rebase-/Retry-Ansatz und Erfolg ohne abschließend geprüftes Remote-Manifest werden nicht zurückgeholt. |
| U007 | `.github/workflows/integrity.yml` | MAIN-COVERED / SUCCESSOR durch U008 und PR #161; Neuerzeugung eines unversionierten Manifests, Warteschlangenkommentar und Jobberechtigungen sind im Nachfolger korrigiert. |
| U008 | `.github/workflows/integrity.yml` | MAIN-COVERED / SUCCESSOR durch PR #161; Recompute-/Publish-Schleife bleibt erhalten, PR-Tests und begrenzte Schreibrechte sind ergänzt. |
| U111 | `ATTRIBUTION.md` | Historischer Vorgänger von U112; der gemeinsame Begleittext wird über U112 transferiert. Kein zweiter unabhängiger Transferfall. |
| U112 | `ATTRIBUTION.md` | Gezielter Transfer der Abschnitte über Attribution und Kommentar-Marker; die zeitgebundene Aussage über einen damaligen „aktuellen Bot-Commit“ wird nicht als heutige Aussage übernommen. |
| U127 | `INTEGRITY.md` | HISTORICAL-SNAPSHOT-EXPLAINED: laut wiederverwendetem Prüfbericht stimmen 11/11 Hashwerte mit dem eigenen Quellcommit überein. Korrigiert U128. Keine alten Hashwerte übernehmen. |
| U128 | `INTEGRITY.md` | HISTORICAL-SNAPSHOT-EXPLAINED: laut wiederverwendetem Prüfbericht stimmen 11/11 Werte zum Elterncommit, aber nur 9/11 zum eigenen Commit; `.canary` und `ATTRIBUTION.md` waren dort bereits geändert. Kein gültiger Nachweis für den eigenen Snapshot. |
| U409 | `scripts/build_integrity.sh` | MAIN-COVERED / SUCCESSOR durch U410 und PR #161; deterministisches Format erhalten, MISSING-Zeilen bewusst durch Pflichtdateiprüfung ersetzt. |
| U410 | `scripts/build_integrity.sh` | MAIN-COVERED / SUCCESSOR durch PR #161; ausführbarer Code übernommen, sachlich unzutreffender Kommentar zu einem optionalen Zeitstempel nicht übernommen. |
| U558 | `scripts/verify_integrity.sh` | MAIN-COVERED / EXACT: Quell- und Main-Blob `ba56b229337622ddb5826ee470391613d2edf766` sind identisch. |

Produktive technische Nachfolger sind bei `1cdf996470c454a7c0a79f9470bb20b48f173118` gebunden: Workflow-Blob `e0e3881051a16db3ff820cd62499e9132c3d99ce`, Generator-Blob `f15058381c1970f4dee3f269ce562d635515c4a0`, Prüfer-Blob `ba56b229337622ddb5826ee470391613d2edf766`. PR #161 wurde mit Head `ecf89ebb7b26e55b4b34a0db7ef4461cfa310df5` bei `f9dc0ce6230a9ee0755f0350b31e6082e5b524fd` integriert. Der Main-Lauf [36043002066](https://github.com/Waschtl904/objekt-x-programm/actions/runs/36043002066) veröffentlichte das bisherige operative Manifest. Dieser bereits abgeschlossene Block wird nicht erneut auditiert.

## Unveränderte historische Quellbindungen

Die folgenden Werte werden aus dem oben benannten Prüfbericht und den vorhandenen U-IDs übernommen; sie bezeichnen historische Quellen, nicht heutige Dateien.

| ID | Quellcommit | Quellblob | SHA-256 |
|---|---|---|---|
| U001 | `69dc670dcdf948a1735206e2f6d34d1727940513` | `0e609832086e22d256e55dbc3035f3dc8556a3db` | `e6c1afe34a565abf999843248c4fadaf1e55ae1ecd3bb1e8b009b872dfc00ba5` |
| U006 | `0b0a42cfb2020c3de53b3b522c3b942a85d02b4c` | `7462e5ecd000ffdc458e6e90490d50a1e4570f0f` | `de7c4d40b633a5fb43c65440be740af3486d3d4b176ddc7baea8ca8f6f935c42` |
| U007 | `69dc670dcdf948a1735206e2f6d34d1727940513` | `b9b6cd964a9306428f685251af5efda24f2f9fb8` | `cdf615afe8f93432f9f902d136993d25432d87ebd83b9761bfff1ee5d8fa51f0` |
| U008 | `ebaa488a17137c9a2d4eaf2576f7259cbf2bc913` | `e5eda3ae01e83bc27e963a050b88b84507e3ce5e` | `b45723ec5d7157ae672db2c0283505b4c19953ef48800961b9545ca6c30dbb3f` |
| U111 | `69dc670dcdf948a1735206e2f6d34d1727940513` | `898a8a2ecf8ed133f1b2a0c0fd6c5af5a9b01a4c` | `2240e7d7e7e596b16a02514a99be8e0c7e486461e4539ce0929af8794f7f23aa` |
| U112 | `ebaa488a17137c9a2d4eaf2576f7259cbf2bc913` | `ace9c7b880c04b9fbf31f52ab0b5b55b3d0b938e` | `75f9fb7653c73d93731e41d131939ea9157f51b734edb4d525b060fbe8741230` |
| U127 | `ebaa488a17137c9a2d4eaf2576f7259cbf2bc913` | `41828353cf91d73f0543bcc33ec1429ba3500d2d` | `8e3542704d23bc3f63e601fd0ca4ab257181cff124b5c6997a996fe84493f532` |
| U128 | `69dc670dcdf948a1735206e2f6d34d1727940513` | `8d94d6483cec6e2a8740089a20c354fcea611057` | `41ef617402446e15d85a5284ef90ef5d0bd6fb82423f6ad3554128c9af5105eb` |
| U409 | `69dc670dcdf948a1735206e2f6d34d1727940513` | `50b81bb4e38b9f8964d19c75dab3dff3a2e6cfee` | `a5c23748ccd527631f05527feddb771d6e543ea391b9792cae2d26b2e7d70e26` |
| U410 | `ebaa488a17137c9a2d4eaf2576f7259cbf2bc913` | `53250f300145dc89f87f9e8929c852ec8031ecfe` | `551577958edd9ee50a2a7c7c77bc4238d34bebce21854fa6807839a798fc5520` |
| U558 | `69dc670dcdf948a1735206e2f6d34d1727940513` | `ba56b229337622ddb5826ee470391613d2edf766` | `6dd925b50c45817892197fc75c8836bbdcb5338eba45850da4cfc8693e6edb90` |

## Begrenzung des Texttransfers

`.canary` übernimmt U001 exakt. `ATTRIBUTION.md` übernimmt U112 mit genau zwei redaktionellen Abweichungen: Der zeitgebundene Halbsatz über einen „aktuellen“ unsignierten Bot-Commit wird entfernt und dieser Nachtrag verlinkt. Das historische Original bleibt unter seinem Quellcommit erreichbar. Aussagen über den Signaturstatus einzelner heutiger Commits müssten separat commitgenau geprüft werden.

Die Lizenzabgrenzungen sind allgemeine Hinweise, keine Entscheidung über einen konkreten Rechtsfall. Primäre Referenzen: [CC-BY-4.0, insbesondere §§ 2(a)(2), 3(a)](https://creativecommons.org/licenses/by/4.0/legalcode) und [WIPO: Ausdrucksform gegenüber Ideen und mathematischen Konzepten](https://www.wipo.int/en/web/copyright/protection).

Nach Integration der Begleittexte sind die zwei konkret fehlenden Dateiinhalte übertragen; die historische Zuordnung von U111/U112 bleibt getrennt von ihrer heutigen Formulierung. **Inhaltstransfer ist keine Branch-Löschfreigabe.** Vor einer Branch-Disposition sind dauerhafter Historienanker, Referenzprüfung und gesonderter Löschauftrag weiterhin erforderlich. Die geplante Gruppe aus 21 anderen Branches erhält durch diesen Nachtrag keine zusätzliche Freigabe. O8 und alle mathematischen Statusfelder bleiben unverändert.
