# Zusammenarbeit und Prüfungen

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
   und geltende GitHub-Anforderungen abgleichen. Neue Commits erfordern die
   Prüfung ihrer tatsächlichen Auswirkungen; frühere CI-Ergebnisse gelten
   weiterhin nur für ihren ursprünglichen Commit. Ein veränderter Main-Stand
   wird auf Integrationsfolgen geprüft, ohne automatisch alte Mathematik
   erneut vollständig zu auditieren.
4. Innerhalb einer bereits erteilten ausdrücklichen oder bedingten
   Mergefreigabe handeln. Ist deren Scope unverändert und sind ihre Bedingungen
   erfüllt, ist keine zweite identische Freigabe nötig. Eine Freigabe für einen
   PR gilt nicht automatisch für weitere PRs. Vorbereitung, Veröffentlichung
   eines Entwurfs und grüne CI erteilen selbst keine Mergefreigabe.
5. Nach dem Merge den tatsächlichen Integrationscommit und die anwendbare
   Integrations-CI bestätigen. Bei neuen Fehlern die Ursache untersuchen;
   identische Timeout-Läufe nicht ohne technischen Grund wiederholen.

Änderungen werden grundsätzlich über Branch und PR integriert. Direkte
Main-Änderungen und Branchlöschungen benötigen einen dafür passenden Auftrag;
ein Mergeauftrag umfasst keine pauschale Bereinigung historischer Branches.

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
