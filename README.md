> [!NOTE]
> **Aktiver Repository-Einstieg.**
>
> Diese README dient der Orientierung. Sie ist **keine mathematische Beweis- oder Statusautorität**.
>
> - Kanonischer operativer Status: [`00-uebersicht/RESEARCH_STATE.yaml`](00-uebersicht/RESEARCH_STATE.yaml)
> - Lesbarer aktueller Stand: [`00-uebersicht/CURRENT_STATE.md`](00-uebersicht/CURRENT_STATE.md)
> - Nächste mathematische Gates: [`00-uebersicht/NEXT_GATES.md`](00-uebersicht/NEXT_GATES.md)
> - Konsolidierte Ergebnisübersicht: [`00-uebersicht/SURVIVOR_REGISTRY.md`](00-uebersicht/SURVIVOR_REGISTRY.md)
> - Branch-Konsolidierung: [Familienprüfung der 58 Unique-Branches](00-uebersicht/archiv/UNIQUE_BRANCH_FAMILY_REVIEW_2026-09-24.md)
> - Archivierungsvorbereitung: [Manifest für 21 Branchkandidaten](00-uebersicht/ARCHIVE_MANIFEST_2026-09-25.md) · [JSON](00-uebersicht/ARCHIVE_MANIFEST_2026-09-25.json)
> - R43-Quellenerhalt: [Zuordnung der drei historischen Fassungen](00-uebersicht/archiv/R43_CONTENT_RECONCILIATION_2026-09-26/README.md) — unabhängiger mathematischer Review weiterhin offen.
>
> Historische Status- und Navigationsfassungen bleiben als Provenienz erhalten und dürfen nicht mit der aktuellen Forschungsfront verwechselt werden.

# Objekt-X-Programm

*Ein langfristiges mathematisches Forschungsprogramm zur Riemannschen Hypothese.*

Objekt X bezeichnet das Ziel einer kompatiblen positiven Geometrie für die relevante Weil-Form-Struktur.

Das Programm arbeitet schrittweise über lokale positive Räume, gekoppelte Operatoren, Transportabbildungen und deren Kompatibilität. Der gegenwärtige Schwerpunkt liegt auf der Fortsetzung der bereits konstruierten Fixed-Horizon-Geometrie über den Horizont `a=1` hinaus.

**Objekt X ist noch nicht vollständig konstruiert.  
Globale Weil-Positivität ist nicht bewiesen.  
Die Riemannsche Hypothese bleibt offen.**

---

## Aktueller Forschungsstand

Für den festen Horizont ist die C1-Kette bis `a=1` konstruiert:

```text
C1a → C1b → kompakter Defekt → finite Schurreduktion
    → Terminalpositivität bei a=1
    → kompatibler positiver C1-Abschluss
```

Der aktuelle Status dieser Bausteine ist `AUTHOR_DERIVED`; ihre genauen Scopes, Beweisanker und Reviewgrenzen stehen in [`RESEARCH_STATE.yaml`](00-uebersicht/RESEARCH_STATE.yaml).

Zusätzlich ist für die erste Kammer

```math
1 \le A \le B \le C \le A_8,
\qquad
A_8=\frac{\log 8}{2},
```

das rohe T/D-Transport- und Cocycle-Paket **O1–O7** konstruiert:

```text
FIRST-CHAMBER-RAW-TD-COCYCLE-O1-O7
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN
```

Dieses Resultat ist ausdrücklich auf die erste geschlossene Kammer beschränkt.

Es beweist **keine** neue Terminalpositivität für `A>1`.

---

## Nächster lokaler Gate: O8

Der nächste mathematische Hauptschritt ist

```text
FIRST-CHAMBER-O8-TERMINAL-POSITIVITY
```

Für einen neuen Terminal

```math
1<A\le A_8
```

ist eine echte positive Reserve zu beweisen:

```math
G_A = I-R_A^*R_A \ge \eta_A I,
\qquad
\eta_A>0.
```

Die bisherige Schranke

```math
\|R_A\|\le\sqrt{90}
```

ist **keine Kontraktionsaussage** und liefert O8 nicht.

Insbesondere darf die frühere `191D`-Reduktion nicht ohne einen neuen analytischen Tail-/Kodimensionsbeweis auf `A>1` übertragen werden.

Vollständige Obligationen:
[`00-uebersicht/NEXT_GATES.md`](00-uebersicht/NEXT_GATES.md)

---

## Weitere offene Gates

Nach beziehungsweise neben O8 bleiben insbesondere offen:

### O9 — Positive corrected transport

Konstruktion der korrigierten positiven Räume und Transporte einschließlich

```text
Quotientenkompatibilität
isometrischer/beschränkter U^X-Transporte
Quellintertwining
Cocycle
```

ohne ein lokales Quadratwurzel-Intertwining vorauszusetzen.

### O10 — q=8 wall crossing

Strikt rechts von

```math
A_8=\frac{\log 8}{2}
```

wird `q=8` aktiv.

Dafür müssen neue gekoppelte Rohoperatoren und beide Wandtransporte konstruiert werden.

Am Endpunkt `A=A_8` bleibt `q=8` wegen der strikten Aktivierungsbedingung inaktiv.

### Unbeschränkter Horizont

Die bisherige positive C1-Geometrie ist ein **Fixed-Horizon-Resultat**.

Eine kompatible unbeschränkte oder kofinale Horizontfamilie bleibt offen.

### Globale Weil-Testklasse

Auch nach einer künftigen unbeschränkten C1-Geometrie muss die exakte Rückbindung an die vollständige geeignete Weil-Testklasse und einen fensterunabhängigen globalen Readout noch bewiesen werden.

---

## Status-Firewall

Folgende Schlussfolgerungen sind ausdrücklich **nicht zulässig**:

```text
CI grün
    ≠ mathematisch unabhängig geprüft

Merge
    ≠ Satzpromotion

O1–O7
    ≠ O8-Terminalpositivität

Fixed-Horizon-Positivität
    ≠ unbeschränkte C1-Geometrie

C1-Geometrie
    ≠ globale Weil-Positivität

lokale oder finite Zertifikate
    ≠ Riemannsche Hypothese
```

Statusänderungen müssen über die dokumentierten mathematischen Beweis- und Auditregeln erfolgen.

---

## Hier beginnen

Für den aktuellen Stand in dieser Reihenfolge lesen:

1. [`00-uebersicht/CURRENT_STATE.md`](00-uebersicht/CURRENT_STATE.md)  
   Lesbare generierte Übersicht des registrierten Forschungsstands.

2. [`00-uebersicht/NEXT_GATES.md`](00-uebersicht/NEXT_GATES.md)  
   Aktuelle offene mathematische Gates und ihre Firewalls.

3. [`00-uebersicht/RESEARCH_STATE.yaml`](00-uebersicht/RESEARCH_STATE.yaml)  
   Kanonische operative Statusquelle mit Scopes, Abhängigkeiten und Beweisankern.

4. [`00-uebersicht/SURVIVOR_REGISTRY.md`](00-uebersicht/SURVIVOR_REGISTRY.md)  
   Konsolidierte Übersicht der weiterverwendbaren mathematischen Resultate.

5. [`00-uebersicht/OBJEKT_X_ARCHITECTURE.md`](00-uebersicht/OBJEKT_X_ARCHITECTURE.md)  
   Architektur und Stellung der lokalen Konstruktionen auf dem Weg zu Objekt X.

---

## Aktuelle Hauptfronten

Das Programm hat zwei getrennte langfristige Fronten.

### 1. Unbeschränkte Horizonterweiterung und kompatibler Transport

```text
UNRESTRICTED-HORIZON-AND-PROFILE-CONTINUATION
OPEN
```

Aktueller lokaler Einstieg: **O8**.

Danach bleiben unter anderem O9, O10, erneuerbare Profilreserven und unbeschränkte Horizontkompatibilität zu schließen.

### 2. Globale Weil-Testklasse und Readout

```text
FULL-WEIL-TEST-CLASS
OPEN
```

Diese Front setzt eine ausreichend kompatible globale beziehungsweise kofinale Geometrie voraus und ist von der lokalen Fixed-Horizon-Positivität zu unterscheiden.

---

## Forschungs- und Reviewstatus

Das Repository unterscheidet insbesondere zwischen:

```text
AUTHOR_DERIVED
EXTERNAL_REVIEW_OPEN
SCOPED_GREEN
OPEN
HISTORICAL_PROVENANCE
```

Die genaue Bedeutung und der jeweilige Scope stehen im kanonischen Register.

Historische Wörter wie `GREEN`, `CLOSED`, `PASS` oder ähnliche Statusangaben in älteren Dateien gelten ausschließlich im damaligen Kontext und werden nicht automatisch auf den heutigen Forschungsstand übertragen.

---

## Historische Provenienz

Frühere Arbeitsstände, alternative Beweisfassungen, Audits, No-Gos und technische Zwischenstufen werden bewusst erhalten.

Historisches Inhaltsregister:

[`00-uebersicht/archiv/HISTORICAL_CONTENT_REGISTER_2026-09-23.md`](00-uebersicht/archiv/HISTORICAL_CONTENT_REGISTER_2026-09-23.md)

Entscheidungsmatrix der erfassten historischen Fassungen:

[`00-uebersicht/archiv/HISTORICAL_CONTENT_DECISION_MATRIX_2026-09-23.md`](00-uebersicht/archiv/HISTORICAL_CONTENT_DECISION_MATRIX_2026-09-23.md)

Diese Dokumente dienen der Provenienz.

Sie erzeugen **keinen neuen mathematischen Satzstatus**.

Die frühere Root-README vom 14. September 2026 bleibt ebenfalls gepinnt erhalten:

[Historische README](https://github.com/Waschtl904/objekt-x-programm/blob/79988874cceeb01f17e0cda67485838c0b7c4f63/README.md)

---

## Arbeitsprinzip

Das Projekt folgt einem fail-closed Forschungsstil:

- Behauptungen werden auf ihren ausdrücklich bewiesenen Scope begrenzt.
- Numerische und computerassistierte Zertifikate werden von analytischen Aussagen getrennt.
- CI und Reproduzierbarkeit ersetzen keinen unabhängigen mathematischen Audit.
- No-Gos, Gegenbeispiele und fehlgeschlagene Konstruktionen werden als Forschungswissen bewahrt.
- Neue Resultate dürfen frühere Resultate ergänzen oder einschränken, aber nicht stillschweigend überschreiben.
- Globale Aussagen werden nicht aus lokalen oder Fixed-Horizon-Resultaten extrapoliert.

---

## Unabhängigkeit

Objekt X ist ein unabhängiges Forschungsprojekt.

Externe Publikationen werden dort zitiert, wo ihre Resultate, Methoden oder Vergleichswerte verwendet werden. Solche Zitate bedeuten keine Zusammenarbeit, institutionelle Verbindung, Zustimmung oder gemeinsame Verantwortung.

Bibliographische Korrekturen an historischen Repository-Ständen verändern keine mathematische Aussage und keinen Forschungsstatus, sofern dies nicht ausdrücklich in einem separaten mathematischen Audit begründet wird.

---

## Lizenz

Originale Repository-Inhalte stehen, soweit nicht anders angegeben, unter [`CC BY 4.0`](LICENSE).

Externe Publikationen und Drittmaterial unterliegen ihren jeweiligen Rechten und Lizenzen.
