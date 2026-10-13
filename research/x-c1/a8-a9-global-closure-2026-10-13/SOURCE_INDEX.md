# Quellenkatalog und Originalpakete

13. Oktober 2026. Vollständige Originalbytes; historische Aussagen behalten ihren damaligen Scope.

39 gespeicherte ZIP-Einträge entsprechen 38 verschiedenen Bytefassungen. Zusammen mit drei zusätzlichen eingebetteten Vorgängercontainern sind 41 ZIP-Fassungen und 1.275 Dateieinträge katalogisiert. Drei separat gespeicherte Begleitdateien sind ebenfalls erhalten.

15 äußere Container reichen zur verlustfreien Aufbewahrung; die übrigen werden aus den unveränderten eingebetteten ZIP-Mitgliedern gewonnen. Große äußere ZIPs liegen als geordnete Blöcke von höchstens 32 MiB vor. Es findet keine Neuerzeugung der Original-ZIPs statt.

`replay.py --output <neues-verzeichnis> --sources-only` stellt alle Originalnamen unter `originals/` wieder her und prüft SHA-256, Größen, alle Mitglieder und Quellenkanten. Der volle Aufruf ohne `--sources-only` führt zusätzlich die vollständige rationale Schlusskette aus.

Der Katalog [SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) enthält vollständige Hashes und Pfade. Die lesbaren Kopien sind bytegleich. Historische Markdown-Dateien erhalten nur im Kopienpfad die Endung `.md.txt`; ihre Inhalte und Originalnamen im ZIP bleiben unverändert. Einzelne frühe Originaltexte enthalten gemischte Windows-Zeichencodierungen; sie werden nicht stillschweigend umcodiert.

| Originaldatei | SHA-256 (Anfang) | Lesbarer Einstieg |
|---|---|---|
| Objekt-X-Alte-Hohe-Reserve-2026-10-08.zip | `3793af139974` | [BERICHT.txt](packages/objekt-x-alte-hohe-reserve-2026-10-08/BERICHT.txt) |
| Objekt-X-Alte-Hohe-Variation-2026-10-08.zip | `36e7de8c6944` | [BERICHT.txt](packages/objekt-x-alte-hohe-variation-2026-10-08/BERICHT.txt) |
| Objekt-X-Anschlussabgleich-und-L2-Modellfehlerbudget-2026-10-12.zip | `abc76a217d5a` | [BERICHT.txt](packages/objekt-x-anschlussabgleich-und-l2-modellfehlerbudget-2026-10-12/BERICHT.txt) |
| Objekt-X-Antwortpruefung-und-Aussenresidual8-2026-10-11.zip | `57b8731ee450` | [BERICHT.txt](packages/objekt-x-antwortpruefung-und-aussenresidual8-2026-10-11/BERICHT.txt) |
| Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11.zip | `d4394c74d224` | [BERICHT.txt](packages/objekt-x-aussenresidualpruefung-und-logarithmischer-randtail-2026-10-11/BERICHT.txt) |
| Objekt-X-Basis84-Pruefung-und-L-Energie-2026-10-10.zip | `5466bd9a66ba` | [README.txt](packages/objekt-x-basis84-pruefung-und-l-energie-2026-10-10/README.txt) |
| Objekt-X-Basis84-und-Abdeckungspruefung-2026-10-10.zip | `dd0e30a27d66` | [BERICHT.txt](packages/objekt-x-basis84-und-abdeckungspruefung-2026-10-10/BERICHT.txt) |
| Objekt-X-Basisabdeckung-und-Fehlerbudget-2026-10-10.zip | `0c54178047ca` | [README.txt](packages/objekt-x-basisabdeckung-und-fehlerbudget-2026-10-10/README.txt) |
| Objekt-X-Common96-Pruefung-und-Residualanschluss-2026-10-11.zip | `174f4f241034` | [BERICHT.txt](packages/objekt-x-common96-pruefung-und-residualanschluss-2026-10-11/BERICHT.txt) |
| Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip | `06b4cc975b8e` | [BERICHT.txt](packages/objekt-x-direkte-restform-und-positiver-96er-block-2026-10-11/BERICHT.txt) |
| Objekt-X-Endlicher-Schuranschluss-2026-10-09.zip | `884cf43ebb15` | [BERICHT.txt](packages/objekt-x-endlicher-schuranschluss-2026-10-09/BERICHT.txt) |
| Objekt-X-Galerkin84-Pruefung-und-Achter-Gegenzeugen-2026-10-11.zip | `0fbf3728ef7f` | [BERICHT.txt](packages/objekt-x-galerkin84-pruefung-und-achter-gegenzeugen-2026-10-11/BERICHT.txt) |
| Objekt-X-Galerkin84-und-Verlusttest-2026-10-11.zip | `461eee1352a8` | [BERICHT.txt](packages/objekt-x-galerkin84-und-verlusttest-2026-10-11/BERICHT.txt) |
| Objekt-X-Gemeinsame-Energie-2026-10-08.zip | `60f2f8bb79d3` | [BERICHT.txt](packages/objekt-x-gemeinsame-energie-2026-10-08/BERICHT.txt) |
| Objekt-X-Gemeinsame-Verlustbilanz-2026-10-10.zip | `aa1077fc6772` | [BERICHT.txt](packages/objekt-x-gemeinsame-verlustbilanz-2026-10-10/BERICHT.txt) |
| Objekt-X-Globale-Funktionsdarstellung-und-glatte-Korrektur-2026-10-12.zip | `86e510b6d68f` | [BERICHT.txt](packages/objekt-x-globale-funktionsdarstellung-und-glatte-korrektur-2026-10-12/BERICHT.txt) |
| Objekt-X-Globaler-Anschluss-und-Optimiertes-Restbudget-2026-10-12.zip | `7a51fbebb858` | [README.txt](packages/objekt-x-globaler-anschluss-und-optimiertes-restbudget-2026-10-12/README.txt) |
| Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip | `2ca3c682de8a` | [BERICHT.txt](packages/objekt-x-globaler-gram-und-vollstaendige-projektion-2026-10-13/BERICHT.txt) |
| Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip | `650859746572` | [BERICHT.txt](packages/objekt-x-globaler-schurabschluss-a8-a9-2026-10-13/BERICHT.txt) |
| Objekt-X-Globalmodell-Gegenpruefung-und-Fehlerrueckbindung-2026-10-12.zip | `d626f6ee355d` | [BERICHT.txt](packages/objekt-x-globalmodell-gegenpruefung-und-fehlerrueckbindung-2026-10-12/BERICHT.txt) |
| Objekt-X-Innere-Randterme-und-Gemeinsamer-Logrest-2026-10-12.zip | `96b8367c5f49` | [BERICHT.txt](packages/objekt-x-innere-randterme-und-gemeinsamer-logrest-2026-10-12/BERICHT.txt) |
| Objekt-X-Logrest-Gegenpruefung-und-groesseres-Ableitungsbudget-2026-10-12.zip | `6febe3404fc9` | [BERICHT.txt](packages/objekt-x-logrest-gegenpruefung-und-groesseres-ableitungsbudget-2026-10-12/BERICHT.txt) |
| Objekt-X-Modellfehler-Gegenpruefung-und-Skalarer-Integralanschluss-2026-10-13.zip | `0f9e5a041271` | [BERICHT.txt](packages/objekt-x-modellfehler-gegenpruefung-und-skalarer-integralanschluss-2026-10-13/BERICHT.txt) |
| Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip | `5b41695ea53c` | [BERICHT.txt](packages/objekt-x-neue-antworten84-und-residualbudget-2026-10-11/BERICHT.txt) |
| Objekt-X-Randtest-Gegenpruefung-und-globaler-Anschluss-2026-10-12.zip | `869a8b518825` | [BERICHT.txt](packages/objekt-x-randtest-gegenpruefung-und-globaler-anschluss-2026-10-12/BERICHT.txt) |
| Objekt-X-Randtest-im-unendlichen-Rest-2026-10-11.zip | `a7126347b620` | [BERICHT.txt](packages/objekt-x-randtest-im-unendlichen-rest-2026-10-11/BERICHT.txt) |
| Objekt-X-Residualgefuehrte-Variation-2026-10-08.zip | `befe66665cd2` | [BERICHT.txt](packages/objekt-x-residualgefuehrte-variation-2026-10-08/BERICHT.txt) |
| Objekt-X-Richtungsbruecke-und-Vergleichsgrenze-2026-10-11.zip | `4faa7004a062` | [BERICHT.txt](packages/objekt-x-richtungsbruecke-und-vergleichsgrenze-2026-10-11/BERICHT.txt) |
| Objekt-X-Richtungsbruecken-Pruefung-und-Konstantentest-2026-10-11.zip | `ec6b5398a8ac` | [BERICHT.txt](packages/objekt-x-richtungsbruecken-pruefung-und-konstantentest-2026-10-11/BERICHT.txt) |
| Objekt-X-Schurabschluss-Gegenpruefung-und-Reserve-2026-10-13.zip | `6b29274d3ead` | [BERICHT.txt](packages/objekt-x-schurabschluss-gegenpruefung-und-reserve-2026-10-13/BERICHT.txt) |
| Objekt-X-Signierter-C-Block-2026-10-07(1).zip | `11d3c5594963` | [BERICHT.txt](packages/objekt-x-signierter-c-block-2026-10-07-1/BERICHT.txt) |
| Objekt-X-Signierter-C-Block-2026-10-07.zip | `11d3c5594963` | [BERICHT.txt](packages/objekt-x-signierter-c-block-2026-10-07-1/BERICHT.txt) |
| Objekt-X-Signierter-C-Block-portabel-2026-10-08.zip | `b97f7274acdf` | [BERICHT.txt](packages/objekt-x-signierter-c-block-portabel-2026-10-08/BERICHT.txt) |
| Objekt-X-Tailarchitektur-und-64er-Lemma-2026-10-09.zip | `2fe86339d80f` | [BERICHT.txt](packages/objekt-x-tailarchitektur-und-64er-lemma-2026-10-09/BERICHT.txt) |
| Objekt-X-U00-Diagnose-2026-10-07.zip | `751db194618e` | [BERICHT.txt](packages/objekt-x-u00-diagnose-2026-10-07/BERICHT.txt) |
| Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11.zip | `2ac05dceb88e` | [BERICHT.txt](packages/objekt-x-unendlicher-dualrest-und-aussenrichtungen-2026-10-11/BERICHT.txt) |
| Objekt-X-Verlustbilanz-Pruefung-und-Residualanschluss-2026-10-10.zip | `2d610ebf2f79` | [README.txt](packages/objekt-x-verlustbilanz-pruefung-und-residualanschluss-2026-10-10/README.txt) |
| Objekt-X-Vollstaendiger-Globaler-Modellfehler-2026-10-12-v2.zip | `c323db96ea92` | [BERICHT.txt](packages/objekt-x-vollstaendiger-globaler-modellfehler-2026-10-12-v2/BERICHT.txt) |
| Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11.zip | `70faaa1a9f8c` | [BERICHT.txt](packages/objekt-x-zusammengesetzte-aussenresiduen-und-momentanschluss-2026-10-11/BERICHT.txt) |

## Separat gespeicherte Begleitdateien

- [Objekt-X-Galerkin84-Pruefung-und-Achter-Gegenzeugen-2026-10-11-Bericht.txt](standalone/Objekt-X-Galerkin84-Pruefung-und-Achter-Gegenzeugen-2026-10-11-Bericht.txt).
- [Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13-Bericht.txt](standalone/Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13-Bericht.txt).
- [Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13-Pruefquittung.json](standalone/Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13-Pruefquittung.json).

## Reichweite

Erfasst sind die zugänglichen gespeicherten Objekt-X-Dateien seit dem Main-Merge #215 vom 7. Oktober, einschließlich der rekursiven ZIP-Vorgänger. Der Katalog behauptet keine Durchsicht sämtlicher früherer Chats oder unpublizierter Arbeitsverzeichnisse. Temporäre Downloads, Bytecode und fremde Projekte sind keine zusätzlichen Originalquellen.

Das Vorhandensein historischer Prüfquittungen bedeutet nicht, dass ihre damaligen Integrationen hier erneut ausgeführt wurden. Welche mathematischen Zertifikate tatsächlich frisch nachgerechnet werden, steht im [Abnahmeplan](ACCEPTANCE_PLAN.md) und in der [Reproduktionsbeschreibung](README.md).
