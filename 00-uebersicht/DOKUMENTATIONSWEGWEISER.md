# Dokumentation lesen und einordnen

## Aktueller Einstieg

| Frage | Zuständige Datei |
| --- | --- |
| Was ist heute integriert, was bleibt offen? | [CURRENT_STATE](CURRENT_STATE.md) |
| Welche Aufgabe kommt als Nächstes? | [NEXT_GATES](NEXT_GATES.md) |
| Welche Resultate gelten in welchem Scope? | [SURVIVOR_REGISTRY](SURVIVOR_REGISTRY.md) |
| Wo sind Beweisanker und Reviewstatus festgelegt? | [RESEARCH_STATE](RESEARCH_STATE.yaml) |
| Wie passt alles zusammen? | [Gesamtüberblick](OBJEKT_X_GESAMTUEBERBLICK.md) und [Architektur](OBJEKT_X_ARCHITECTURE.md) |
| Was bedeutet Objekt X fachlich? | [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md) |
| Wie arbeite ich mit? | [MITWIRKEN](../MITWIRKEN.md), [CONTRIBUTING](../CONTRIBUTING.md) und [Registry-Pflege](RESEARCH_STATE_MAINTENANCE.md) |
| Warum gibt es so viele alte Dateien und Tags? | [Archiveinstieg](ARCHIVE_INDEX.md) und [Branch-Bereinigung](BRANCH_HYGIENE_2026-10-02.md) |

Die drei Statusansichten werden aus dem Forschungsregister erzeugt. Eine
neuere Datei, ein Merge oder eine grüne CI ändert für sich genommen keinen
mathematischen Reviewstatus.

## Lokale Folgepakete

**Integrationsnachtrag vom 2. Oktober 2026:** Das beim Dokumentationsaudit noch
lokale [Direct-Line-Paket](../research/x-c1/canonical-direct-odd-line-2026-10-02/README.md) ist durch
[PR #204](https://github.com/Waschtl904/objekt-x-programm/pull/204) integriert.
Die Registry führt jetzt 51 Resultate. Die Originaldateien behalten ihre
damalige lokale Statusangabe; die spätere Integration steht im Register.

Archivname: `Direkte-gemeinsame-Odd-Eigenlinie-2026-10-02.zip`.
SHA-256: `b7a37a9d6cb8ef49233b77af5c536759cf208ced362f7cdb608f97c3f5847019`.

Die ganze ungerade Familie bleibt UNRESOLVED. Der
[Y-Kernel-Gate mit zweiter Ordnung](Y_KERNEL_SECOND_ORDER_GATE_2026-10-02.md)
ist die nächste offene Aufgabe; seine Planung ist noch kein neues Resultat.

## Historische Unterlagen

`CURRENT-FRONT.md`, `EINSTIEGSPROMPT.md`, `STATUS.md`, `OFFENE_PROBLEME.md`,
ältere Roadmaps und die Themenregister beschreiben ihre datierten
Arbeitsstände. Ihre alten Wörter „aktuell“, „offen“ oder „geschlossen“ sind
in diesem zeitlichen Kontext zu lesen. Das gilt auch für damalige
Dokumentzahlen und SYN-/PUB-Markierungen.

Beweispakete, Auditberichte und Archivkopien bewahren ihre Originalfassungen.
Ein dort noch stehendes `LOCAL_UNMERGED` kann den damaligen Paketstand meinen;
für die spätere Integration ist die Registry zuständig. Das [Glossar](../GLOSSAR.md)
unterscheidet die heutige Arbeitsdefinition von älteren Kandidatenbegriffen.

Die lokale Linkprüfung des [Dokumentationsaudits](DOKUMENTATIONSAUDIT_2026-10-02.md)
erklärt auch relative Verweise, die in archivierten Originalen noch auf deren
damalige Arbeitsverzeichnisse zeigen. Die ursprünglichen Beweisdateien bleiben
erhalten; aktuelle Paket-Einstiege dienen als Navigation.
