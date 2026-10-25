# Zusammenarbeit und Prüfungen

Aktuelle Aufgaben: [NEXT_GATES](00-uebersicht/NEXT_GATES.md).
Die [Herkunft des Journals](00-uebersicht/HERKUNFT.md) beschreibt den ursprünglichen Import.

## Wie Sie beitragen können

Dieses Programm arbeitet lakatosianisch: Ein Gegenbeispiel ist wertvoller als eine
Zustimmung. Besonders willkommen sind

- **Fehlernachweise** in Beweisen, die als `✓ [M]` markiert sind,
- **Gegenbeispiele** zu konditionalen Resultaten `⚠ [M]`,
- **Quellenhinweise** auf bereits bekannte Resultate, die einen offenen Knoten schließen
  oder ein No-Go verschärfen,
- **Verschärfungen** bestehender No-Gos,
- **Konstruktionen** für eine der aktuellen Aufgaben aus [NEXT_GATES](00-uebersicht/NEXT_GATES.md).

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

### Historische Journalmarken

Die folgende Tabelle erklärt die Notation der Journaltexte. Heutige Resultate
werden mit Scope, Beweisanker sowie getrenntem mathematischem und externem
Reviewstatus im [Forschungsregister](00-uebersicht/RESEARCH_STATE.yaml) geführt.
Eine Journalmarke ist keine eigenständige aktuelle Statuspromotion.

| Marke | Wann |
|---|---|
| `✓ [M]` | vollständiger Beweis liegt im Dokument selbst vor |
| `✓ [K]` | Objekt ist konstruiert und typgeprüft, Konsequenzen noch offen |
| `⚠ [M]` | Beweis vollständig, aber unter einer explizit benannten offenen Voraussetzung |
| `✗ [M]` | Route gesichert ausgeschlossen; das Hindernis ist benannt |
| `❓ [O]` | offen; die Frage ist präzise formuliert und mit Knoten-ID versehen |

Rechenregeln für die BC-Algebra sind in [KONVENTIONEN.md](00-grundlegung/KONVENTIONEN.md) verbindlich
festgelegt. Bei Widersprüchen zwischen einem Katalogeintrag und den Konventionen hat die
Konventionsdatei Vorrang.

---

## Haftungsausschluss

Die Dokumente sind **nicht peer-reviewed** und enthalten **keinen Beweis der Riemannschen
Hypothese**. Einige als gesichert markierte Aussagen wurden im Laufe des Programms durch
spätere Audits korrigiert oder zurückgerollt; solche Fälle sind im
[CHANGELOG](00-uebersicht/archiv/root-journal-2026-10-03/CHANGELOG.md) und in den Auditdateien nachvollziehbar. Wer Resultate von hier
weiterverwendet, sollte den zugehörigen Beweis eigenständig prüfen.

---

## Änderungen prüfen und übernehmen

Änderungen werden nach ihrer tatsächlichen Auswirkung geprüft. Dateiendung,
Verzeichnis und PR-Titel entscheiden nicht über den Prüfbedarf. Für gemischte
Änderungen gelten die Anforderungen jeder betroffenen Klasse.

Diese Regeln beschreiben den operativen Ablauf. Der Forschungsstatus steht in
[`RESEARCH_STATE.yaml`](00-uebersicht/RESEARCH_STATE.yaml); die
[Pflegeanleitung](00-uebersicht/RESEARCH_STATE_MAINTENANCE.md) erklärt seine Felder.
Historische Auditberichte bleiben Belege für ihren jeweiligen Stand.

## Drei Änderungsklassen

| Klasse | Tatsächliche Auswirkung | Erforderliche Prüfung |
| --- | --- | --- |
| Mathematik | Satz, Beweis, Hypothese, Scope, mathematischer Status, Certifier, mathematischer Input oder Fehlerbudget wird geändert. | Prüfung des betroffenen Claims und seiner Abhängigkeiten am exakten Commit; relevante Zertifikatsläufe und Nachweis der Beweisanker; ausdrückliche Freigabe für die konkrete Änderung. |
| Infrastruktur | Workflow, Generator, Validator, Schema oder reine Integrationsmetadaten werden geändert, ohne mathematische Aussage oder Zertifikatsbedeutung zu verändern. | Technische Tests und passende Integrationsprüfung; bei CI-Routing auch relevante/irrelevante Pfade und Fehlerfälle prüfen. Bestehende mathematische Resultate werden dadurch nicht erneut vollständig auditiert. |
| Dokumentation | Sprache, Links, Darstellung oder Einstieg werden geändert, ohne Claims, Status, Belegbindung oder Prüfregeln zu verändern. | Diff-, Link- und gegebenenfalls Darstellungsprüfung sowie die vorhandenen anwendbaren CI-Checks. Unveränderte mathematische Großrechnungen sind dafür nicht erforderlich. |

Ein Certifier bleibt Mathematik, auch wenn er unter `scripts/` liegt. Eine
Statuspromotion bleibt Mathematik, auch wenn nur YAML oder Markdown geändert
wird. Änderungen dieser Governance und anderer Prüfregeln zählen zur
Infrastruktur. Bei unklarer Auswirkung wird vor einer Erleichterung der Prüfung
der betroffene Claim oder Prüfpfad geklärt.

## Prüfbedarf vor dem Lauf festlegen

Vor Beginn eines Abnahmelaufs wird festgehalten, welche Checks für die
betroffene Änderung **verpflichtend** sind und welche nur als zusätzlicher
Audit dienen. Ein nachträglich fehlgeschlagener Pflichtcheck wird nicht
rückwirkend zum optionalen Audit erklärt. Ein konkreter mathematischer
Zertifikatsfehler wird unabhängig vom Namen des Checks untersucht.

Ein technischer Timeout oder Runner-Abbruch ist zunächst eine technische
Diagnose, kein mathematischer Gegenbefund. Ein identischer Lauf wird nur dann
wiederholt, wenn dadurch realistisch neue Information zu erwarten ist; bei
reproduziertem Timeout wird stattdessen Ursache, Laufzeitgrenze oder
CI-Routing korrigiert.

## Zuständigkeit pro Branch

Für jeden aktiven Branch gibt es eine federführende Sitzung bzw. einen
federführenden Arbeitsstrang. Andere Sitzungen dürfen prüfen, kommentieren und
Übergaben vorbereiten, verändern denselben Branch aber nicht parallel ohne
ausdrückliche Koordination. Das verhindert konkurrierende Registry-Edits,
widersprüchliche Fixes und unnötige CI-Neustarts.

## Ein Abnahmeablauf pro PR

1. Scope und Änderungsklassen festhalten. Den betroffenen Diff und die dafür
   notwendigen Nachweise prüfen. Ein kurzer PR-Text genügt; ein zusätzlicher
   Governance-Bericht ist nicht für jeden Vorgang erforderlich.
2. Anwendbare CI auf dem endgültigen PR-Head erfolgreich abschließen lassen.
   Ein fehlgeschlagener, abgebrochener oder noch laufender ausgeführter Check
   wird nicht als Erfolg behandelt. Planmäßig nicht anwendbare Jobs dürfen
   übersprungen werden; vorgeschaltete Klassifikation und Abschluss-Gate
   müssen die gewählte Route bestätigen. Erwartete Checks dürfen nicht fehlen.
3. Unmittelbar vor dem Merge Head, Base, aktuellen Main-Stand, Mergeability
   und geltende GitHub-Anforderungen abgleichen. Neue Commits erfordern nur
   die Prüfung ihrer **neuen tatsächlichen Auswirkungen**; unveränderte
   Beweisblöcke werden nicht allein wegen eines späteren Dokumentations- oder
   Infrastrukturcommits erneut vollständig auditiert. Frühere CI-Ergebnisse
   bleiben an ihren ursprünglichen Commit gebunden, und dokumentierte
   Beweisprüfungen behalten ihre eigenen Beweisanker, solange Voraussetzungen
   und Abhängigkeiten unverändert bleiben. Ein veränderter Main-Stand wird auf
   Integrationsfolgen geprüft, ohne daraus automatisch einen Mathematik-Replay
   abzuleiten.
4. Innerhalb einer bereits erteilten ausdrücklichen oder bedingten
   Mergefreigabe handeln. Ist deren Scope unverändert und sind ihre Bedingungen
   erfüllt, ist keine zweite identische Freigabe nötig. Eine Freigabe für einen
   PR gilt nicht automatisch für weitere PRs. Eine eng begrenzte
   **Routinefreigabe** für wiederkehrende reine Sprach-, Link- oder
   Darstellungsänderungen darf nur gelten, wenn sie zuvor ausdrücklich mit
   Scope und Grenzen vereinbart wurde; sie darf niemals neue Claims,
   Statuspromotionen oder Infrastrukturänderungen umfassen. Vorbereitung,
   Veröffentlichung eines Entwurfs und grüne CI erteilen selbst keine
   Mergefreigabe.
5. Nach dem Merge den tatsächlichen Integrationscommit und die anwendbare
   Integrations-CI bestätigen. Bei neuen Fehlern die Ursache untersuchen;
   identische Timeout-Läufe nicht ohne technischen Grund wiederholen.

Änderungen werden grundsätzlich über Branch und PR integriert. Direkte
Main-Änderungen und Branchlöschungen benötigen einen dafür passenden Auftrag;
ein Mergeauftrag umfasst keine pauschale Bereinigung historischer Branches.

Für normale Änderungen genügt eine kurze PR-Beschreibung mit **Änderung,
Prüfung und offenen Punkten**. Pro Forschungsfront soll möglichst nur ein
aktiver Integrations-PR geführt werden. Überholte PRs werden nach dokumentiertem
Nachfolger bzw. gesicherter Provenienz geschlossen; Branchlöschungen bleiben
davon getrennt.

## Wissenschaftliche Bindungen erhalten

- Merge, CI-Erfolg und mathematische Promotion sind getrennte Ereignisse.
  Autorenresultat, externe Prüfung, reproduziertes Zertifikat und bewiesener
  Satz behalten ihre jeweiligen Rollen.
- Integrationsbasis, mathematischer Verifikationssnapshot, beobachteter
  Branch-Head und satzbezogener Beweisanker bleiben getrennt. Ein späterer
  Dokumentations- oder CI-Commit verschiebt keine Verifikation.
- Ein abgeschlossener Block wird bei einem konkreten mathematischen Einwand,
  Provenienzfehler oder reproduzierbaren Zertifikatsfehler erneut geöffnet.
  Eine reine Navigationsänderung ist dafür kein Anlass.
- Die aktive README ist bearbeitbar. Historische Originale, Hashbindungen
  und Beweisanker bleiben gemäß Register erhalten. Generierte Statusansichten
  werden aus der Registry erzeugt, nicht von Hand umgeschrieben.
- Fixed-Pair-Transport begründet keine unbeschränkte C1-Horizontkompatibilität.
  Globaler Readout, Objekt X, globale Weil-Positivität und RH erhalten durch
  diese Arbeitsregeln keinen neuen Status.
