# Objekt-X-Programm

Ein offenes, KI-gestütztes mathematisches Forschungsjournal zur Konstruktion von Objekt X.

**Objekt X ist das Ziel einer noch unvollständigen Konstruktion:** Gesucht wird
eine kompatible positive Geometrie, welche die relevante Weil-Form exakt
darstellt. Das Programm untersucht dazu gemeinsame Prim-/Gamma-Operatoren,
endliche positive Kammern und deren Fortsetzung.

**Objekt X hat Vorrang.** Erst nach seiner erfolgreichen Konstruktion wird der
mögliche Anschluss an die Riemannsche Vermutung verfolgt. Die Anforderungen
an X, einschließlich der vollständigen geeigneten Testklasse, bleiben erhalten.

**Ein Beweis der Riemannschen Hypothese liegt nicht vor.** Globale
Weil-Positivität und die vollständige Konstruktion von Objekt X bleiben offen.
Die projektintern hergeleiteten Ergebnisse sind zur externen Prüfung offen.

## Einstieg

| Ich möchte … | Einstieg |
| --- | --- |
| Idee, Entwicklung und Grenzen verstehen | [Gesamtüberblick](00-uebersicht/OBJEKT_X_GESAMTUEBERBLICK.md) |
| Die weitere Forschungsrichtung verstehen | [Strategie für Objekt X](00-uebersicht/OBJEKT_X_FORSCHUNGSSTRATEGIE.md) |
| Das Projekt kritisch begutachten | [Leitfaden für externe Begutachtung](00-uebersicht/EXTERNE_BEGUTACHTUNG.md) |
| Den integrierten Stand und offene Aufgaben prüfen | [Aktueller Stand](00-uebersicht/CURRENT_STATE.md) · [Nächste Aufgaben](00-uebersicht/NEXT_GATES.md) |
| Einen konkreten Satz und seine Belege finden | [Ergebnisregister](00-uebersicht/SURVIVOR_REGISTRY.md) |
| Dateien, Manuskripte oder ältere Ansätze einordnen | [Dokumentationswegweiser](00-uebersicht/DOKUMENTATIONSWEGWEISER.md) |

## Forschungsstand in Kürze

Die folgende Zusammenfassung bezieht sich auf den integrierten Forschungsstand
und die Folgepakete bis **7. Oktober 2026**. Den operativen Status, die genauen Voraussetzungen und
die gepinnten Beweisanker verwaltet das
[Forschungsregister](00-uebersicht/RESEARCH_STATE.yaml).

| Bereich | Dokumentierter Stand | Aussagegrenze |
| --- | --- | --- |
| Endliche positive Geometrie | Drei positive Kammern bis $A_{11}=\log(11)/2$, mit kompatiblen Transporten | Kein Positivitätssatz für beliebig große Horizonte |
| Hoher und niedriger Schuranteil | Vollständige Reduktion auf einen endlichen kritischen Rest für jeden festen endlichen Horizont | Die Positivität dieses Rests muss jeweils begründet werden |
| Kanonische Richtung für A9→A11 | Maximaler Schur-Eigenwert in beiden Paritäten einfach; gerade Richtung lokalisiert | Ungerade ist die gesamte Ausgangsfamilie weiterhin `UNRESOLVED` |
| Ungerade Winkeldiagnose | Gemeinsamer Y-Kernel: central ≤2.933357°, quarter ≤3.070163°, half ≤3.642693°; Endpunktfolge: five_eighths ≤4.933780° | Bedingte Schnitte; Root bleibt `UNRESOLVED` |
| H₀-Folgeuntersuchung | Exaktes Hindernis für die benannte letzte Drei-Cut-Relaxation | Kein ursprünglicher Operatorgegenzeuge; vollständiges H₀ unentschieden |
| Konstruktiver Anschluss A8→A9 | [Acht feste Quellen und Restpilot](research/x-c1/a8-a9-remainder-progress-2026-10-07/README.md): positiver endlicher Anschluss, vollständige Restdarstellung, Halbinversen und erste gewichtete Fehlergrame | Voller neuer Rest, Kreuzkopplung und allgemeine Fortsetzung offen; analytische Grundlagen übernommen |
| Globales Ziel | Arbeitsdefinition und erforderliche Übergänge sind formuliert | Kofinale positive Familie, globaler Readout, vollständige Weil-Gramidentität und RH bleiben offen |

Die hier zusammengefassten projektinternen Ergebnisse tragen den Status
`AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`. Das bedeutet: projektintern hergeleitet,
mit angegebenen Beweisen und Zertifikaten; die unabhängige externe Prüfung ist
offen. Ein erfolgreicher Rechenlauf bestätigt seinen ausgewiesenen Prüfumfang.

Aktuelle Arbeit außerhalb von `main` ist in den
[offenen Pull Requests](https://github.com/Waschtl904/objekt-x-programm/pulls)
sichtbar. Für ein Urteil über einen solchen Vorschlag sind dessen eigener
Commit, Belegumfang und Integrationsstatus anzugeben.

## Mathematischer Ansatz

Ausgangspunkt ist die physische finite Weil-Form. Ein gemeinsamer
Prim-/Gamma-Mediator trennt sie in einen positiven Anteil und einen Defekt.
Eine vollständige Schurreduktion macht den niedrigen Rest zum entscheidenden
Positivitätsproblem. Bisherige endliche Kammern liefern Bausteine für eine
Fortsetzung; ein allgemeiner Mechanismus zur Erneuerung ihrer positiven
Reserve fehlt noch.

```text
Finite Weil-Form → gemeinsamer Mediator → Defekt- und Schurreduktion
                → positive Kammern bis A11
                → [offen] positive Fortsetzung auf unbeschränkte Horizonte
                → [offen] vollständiges Objekt X mit exakter Weil-Gramidentität
                → danach: möglicher Anschluss an RH
```

Die [Arbeitsstrategie](00-uebersicht/OBJEKT_X_FORSCHUNGSSTRATEGIE.md) setzt beim
vollständigen neuen Schurrest an. Neue Terminalpositivität darf in seiner
Begründung nicht vorausgesetzt werden. Winkel- und Momentdiagnosen dienen
konkret benannten Abschätzungen dieser Fortsetzung.

Die [Architektur](00-uebersicht/OBJEKT_X_ARCHITECTURE.md) erklärt die Rollen
dieser Übergänge. Die [Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
legt die Anforderungen an Objekt X fest, insbesondere die vollständige
Testklasse und eine Konstruktion ohne vorausgesetzte Weil-Positivität.

## Belege, Reproduktion und Geschichte

- **Beweise:** Das [Ergebnisregister](00-uebersicht/SURVIVOR_REGISTRY.md)
  führt zu den jeweiligen Beweispaketen. Deren Voraussetzungen und
  Geltungsbereiche sind für die Aussagen entscheidend.
- **Reproduktion:** Paket-READMEs beschreiben Eingaben, Software und konkrete
  Prüfläufe; etwa die [Kammerkette bis A11](research/x-c1/chambers-through-a11-2026-09-28/README.md),
  der [gemeinsame Y-Kernel](research/x-c1/canonical-y-kernel-second-order-2026-10-03/README.md)
  und die [H₀-Folgeuntersuchungen](research/x-c1/canonical-h0-followups-2026-10-03/README.md).
  Analytischer Beweis, Zertifikatsreplay und unabhängiger Review sind getrennt ausgewiesen.
- **Geschichte:** Das [Archiv](00-uebersicht/ARCHIVE_INDEX.md) bewahrt frühere
  Kandidaten, Fehler, Korrekturen und verworfene Ansätze. Datierte Statusangaben
  beschreiben den damaligen Stand. Historische Originale behalten ihre Pfade
  und ihren Wortlaut am jeweiligen Quellcommit. Für die
  [verlegten Root-Dateien](00-uebersicht/archiv/root-journal-2026-10-03/README.md)
  sind Originalbytes sowie alte und neue Pfade dokumentiert.

Die versiegelten Originalpakete behalten auch ihre damaligen Integrationsangaben.
Ein dortiges `PENDING_STATUS_REVIEW` oder `RESEARCH_BRANCH_UNMERGED` beschreibt
den ursprünglichen Paketstand. Die heutige Aufnahme ist im
[Forschungsregister](00-uebersicht/RESEARCH_STATE.yaml) und
in den jeweiligen Integrationsnachweisen dokumentiert:
[#206](00-uebersicht/integrationsnachweise/PR206_2026-10-03.md),
[#211](00-uebersicht/integrationsnachweise/PR211_2026-10-04.md) und
[#213](00-uebersicht/integrationsnachweise/PR213_2026-10-07.md).

Diese README dient der Orientierung. Die lesbaren Statusansichten werden aus
`RESEARCH_STATE.yaml` erzeugt; mathematische Aussagen beruhen auf den dort
gebundenen Quellen.

## Autor, Mitarbeit und Zitation

Das Projekt wird von **Sebastian Schmalnauer** geführt und mit Unterstützung
verschiedener KI-Agenten entwickelt. Diese Mitwirkung und interne Kontrollen
ersetzen keine unabhängige fachliche Begutachtung. Eine Neuheitsbewertung
erfordert einen Vergleich mit der einschlägigen Literatur.

Für konkrete Einwände bitte Satz, Datei, Commit und Begründung nennen.
[CONTRIBUTING](CONTRIBUTING.md) beschreibt geeignete Beiträge und regelt ihre Prüfung.
Die [Herkunft des Journals](00-uebersicht/HERKUNFT.md) ist separat dokumentiert.

Zitation und Herkunft: [CITATION.cff](CITATION.cff) · [ATTRIBUTION](ATTRIBUTION.md).
Bei Verwendung einen konkreten Commit angeben. Originale Repository-Inhalte
stehen, soweit nicht anders angegeben, unter [CC BY 4.0](LICENSE).
Für Drittmaterial gelten die jeweiligen Rechte und Lizenzen.
