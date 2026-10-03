# Leitfaden für externe Begutachtung

**Projektpriorität:** Zuerst Objekt X gemäß seiner vollständigen Arbeitsdefinition
konstruieren, danach den möglichen RH-Anschluss verfolgen. Die
[Forschungsstrategie](OBJEKT_X_FORSCHUNGSSTRATEGIE.md) begründet die konstruktive
Fortsetzung als Hauptaufgabe; [NEXT_GATES](NEXT_GATES.md) enthält die operative Reihenfolge.

Dieser Leitfaden erschließt das Objekt-X-Programm für eine fachliche
Erstbeurteilung. Er ist auch als Einstieg für einen KI-gestützten Review
geeignet. Die Bewertung darf ausdrücklich kritisch oder negativ ausfallen;
entscheidend sind überprüfbare Gründe und ein benannter Prüfumfang.

## Gegenstand und Ausgangslage

Das von Sebastian Schmalnauer mit Unterstützung verschiedener KI-Agenten
entwickelte Programm sucht eine nichtzirkuläre positive Darstellung der
relevanten Weil-Form. **Objekt X ist noch nicht vollständig konstruiert; RH
bleibt offen.** Das Repository enthält sowohl aktuelle Beweispakete als auch
ältere Kandidaten, Fehler, Korrekturen und aufgegebene Ansätze.

Der integrierte Forschungsstand mit Folgepaketen vom 3. Oktober 2026 umfasst projektintern
hergeleitete positive Kammern bis $A_{11}=\log(11)/2$. Die Fortsetzung zu
einer kofinalen positiven Familie und die globale Weil-Gramidentität sind
offen. Die untersuchte Winkellokalisierung ist eine Teilaufgabe dieser Fortsetzung.
Ihre bedingten Verbesserungen lösen das globale Problem nicht.

Für die jeweils aktuelle Einordnung gelten [CURRENT_STATE](CURRENT_STATE.md)
und das [Forschungsregister](RESEARCH_STATE.yaml). Ein Review sollte den
gelesenen **Commit** und gegebenenfalls separat untersuchte Pull Requests
nennen. Ein Branch-Head und ein mathematisch geprüfter Snapshot können
verschieden sein.

## Empfohlene Lesereihenfolge

| Schritt | Quelle | Zu klärende Frage |
| --- | --- | --- |
| 1. Ziel | [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md) | Welche Konstruktion und welche exakte Identität würden Objekt X ausmachen? |
| 2. Logik | [Architektur](OBJEKT_X_ARCHITECTURE.md) | Wie hängen physische Quellen, Mediator, Defekt, Schurrest und globaler Readout zusammen? |
| 3. Stand | [CURRENT_STATE](CURRENT_STATE.md), [SURVIVOR_REGISTRY](SURVIVOR_REGISTRY.md) | Was ist hergeleitet, nur bedingt bewiesen, ausgeschlossen oder offen? |
| 4. Belege | Die im Register gebundenen Beweispakete | Stimmen Voraussetzungen, Übergänge und ausgewiesene Geltungsbereiche? |
| 5. Entwicklung | [Gesamtüberblick](OBJEKT_X_GESAMTUEBERBLICK.md), [Archiveinstieg](ARCHIVE_INDEX.md) | Welche Ansätze wurden korrigiert oder aufgegeben, und warum? |

Für einen begrenzten ersten Review bieten sich drei zusammenhängende
Belegstrecken an:

- **Analytische Konstruktion:** Vom [C0/C1-Interface](OBJEKT_X_INTERFACE_2026-09-19.md)
  zu den Registereinträgen `C0-DIRECTED-FORM-SYSTEM`,
  `C1a-COUPLED-SPECTRAL-MEDIATOR`, `C1b-ZERO-EXTENSION-INTERTWINING`
  und `TERMINAL-191D-DEFECT-SCHUR-A1`. Das Register bindet ihre jeweiligen
  Originalquellen; die damalige Fortschrittstabelle des Interface-Dokuments
  ist historisch.
- **Endliche Positivität und Fortsetzung:** [Kammerkette bis A11](../research/x-c1/chambers-through-a11-2026-09-28/README.md),
  insbesondere [A11-Beweis](../research/x-c1/chambers-through-a11-2026-09-28/a11/PROOF.md),
  [allgemeiner hoher Tail](../research/x-c1/chambers-through-a11-2026-09-28/high-tail/PROOF.md)
  und [ausgewiesener Prüfumfang](../research/x-c1/chambers-through-a11-2026-09-28/REVIEW_SCOPE.md).
- **Grenzen der jüngsten Winkeldiagnose:** [Gemeinsamer Y-Kernel](../research/x-c1/canonical-y-kernel-second-order-2026-10-03/README.md)
  und [H₀-Folgeuntersuchungen](../research/x-c1/canonical-h0-followups-2026-10-03/README.md).
  Zentral sind die Unterscheidung zwischen eingeschränkten Schnitten und
  vollständiger Ausgangsfamilie sowie die erhaltenen gemeinsamen Abhängigkeiten.

Diese Auswahl ermöglicht Teilprüfungen. Eine Gesamtbewertung muss zusätzlich
die verwendeten Vorresultate, externen Sätze und die globale Rückbindung
untersuchen. Die neuesten Zahlen allein beurteilen das Programm nicht.

## Begriffe und Aussagegrenzen

| Angabe | Bedeutung für den Review |
| --- | --- |
| `AUTHOR_DERIVED` | Projektintern hergeleitete Aussage im genau angegebenen Scope |
| `EXTERNAL_REVIEW_OPEN` | Die unabhängige externe fachliche Prüfung ist offen |
| `UNRESOLVED` | Der betreffende Test entscheidet die Frage nicht; daraus folgt weder Wahrheit noch Gegenbeispiel |
| `STRUCTURAL OPEN` | Im betreffenden Paket durch konkrete Zeugen nachgewiesene Informationsgrenze einer benannten Relaxation; nur für diese Familie gültig |
| Erfolgreiche CI / Zertifikatsreplay | Die angegebenen maschinellen Prüfungen bestehen für konkrete Eingaben und einen konkreten Commit |
| Integriert / gemergt | Bestandteil des Hauptstands; keine eigenständige mathematische Beglaubigung |

Der Dateititel [„Unabhängiger Gesamtaudit“](OBJEKT_X_UNABHAENGIGER_GESAMTAUDIT.md)
bezeichnet einen im Repository dokumentierten Audit mit eigenem Datum und
Prüfumfang. Er hebt `EXTERNAL_REVIEW_OPEN` nicht auf. Ebenso sind KI-Reviews,
die Wiederholung derselben Implementierung und eine unabhängige analytische
Prüfung getrennt zu bewerten.

## Kritische Prüffragen

1. **Testklasse und Normierungen:** Stimmen Quellenräume, Mellinbedingungen,
   Skalen, Polarisation und Normierungen mit der behaupteten Weil-Form überein?
   Wo wird eine Dichtheits- oder Stetigkeitsaussage benötigt?
2. **Nichtzirkularität:** Werden Positivität, Semibeschränktheit, Abschließbarkeit
   oder RH an einem Übergang vorausgesetzt, obwohl sie erst zu beweisen sind?
3. **Vollständiger Rest:** Erfasst die Schurreduktion die gesamte hohe Antwort?
   Sind Restabschätzungen, Invertierbarkeit und Fehlerbudgets analytisch gedeckt?
4. **Zertifikate:** Welche Eingaben sind neu berechnet, welche nur übernommen?
   Sind gemeinsame Abhängigkeiten und gerichtete Rundungen erhalten? Welche
   Kontrolle wäre von der vorhandenen Implementierung unabhängig?
5. **Quantoren und Fortsetzung:** Für welche Horizonte, Parameter und Familien
   gilt ein Satz? Was fehlt vom festen endlichen Horizont zur unbeschränkten
   Familie? Welche Reserve muss ein Fortsetzungsschritt neu erzeugen?
6. **Originalität und Nutzen:** Welche Teile sind bekannte Theorie, welche
   konkrete projektinterne Ableitungen? Gibt es einschlägige Vorarbeiten oder
   einfachere bekannte Wege? Haben Teilresultate auch ohne das globale Ziel Wert?
7. **Konstruktive Strategie:** Ist die vorgeschlagene vollständige Blockdarstellung
   gerechtfertigt? Welche konkrete Prim-/Gamma-Ungleichung könnte den neuen
   Schurrest kontrollieren, ohne seine Positivität vorauszusetzen? Welche
   Diagnose würde genau diese fehlende Schranke liefern?
8. **Forschungsentscheidung:** Welcher konkrete Einwand, Gegenversuch oder
   nächste Beweis würde die Einschätzung des Programms am stärksten verändern?

## Ein hilfreicher Reviewbericht

Bitte gelesene Quellen und Commit, geprüfte Aussagen und ausgelassene Teile
benennen. Einwände sind am besten mit Satz oder Abschnitt, fehlender Annahme
und möglichst einer Rechnung, Literaturstelle oder einem Gegenbeispiel
nachvollziehbar. Zwischen einem gefundenen Fehler, einer unbelegten Stelle
und einer noch ungeprüften Behauptung sollte unterschieden werden.

Für eine erste Einschätzung genügen: Zusammenfassung des verstandenen
Ansatzes, konkret geprüfte Stärken und Schwächen, entscheidende offene
Übergänge, Literaturbezug und eine begründete Empfehlung für den nächsten
Schritt. Eine Gesamtbestätigung ohne Prüfung der Belegkette wäre nicht gedeckt.

Rückmeldungen können über [CONTRIBUTING](../CONTRIBUTING.md) eingebracht werden.
Weitere Orientierung bietet der [Dokumentationswegweiser](DOKUMENTATIONSWEGWEISER.md).
