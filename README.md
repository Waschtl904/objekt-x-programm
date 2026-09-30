> [!NOTE]
> **Aktiver Repository-Einstieg.**
>
> Diese README dient der Orientierung. Sie ist **keine mathematische Beweis- oder Statusautorität**.
>
> - Kanonischer operativer Status: [`00-uebersicht/RESEARCH_STATE.yaml`](00-uebersicht/RESEARCH_STATE.yaml)
> - Lesbarer Gesamtüberblick: [`00-uebersicht/OBJEKT_X_GESAMTUEBERBLICK.md`](00-uebersicht/OBJEKT_X_GESAMTUEBERBLICK.md)
> - Lesbarer aktueller Stand: [`00-uebersicht/CURRENT_STATE.md`](00-uebersicht/CURRENT_STATE.md)
> - Nächste mathematische Gates: [`00-uebersicht/NEXT_GATES.md`](00-uebersicht/NEXT_GATES.md)
> - Konsolidierte Ergebnisübersicht: [`00-uebersicht/SURVIVOR_REGISTRY.md`](00-uebersicht/SURVIVOR_REGISTRY.md)
> - Historische Quellen und abgeschlossene Branch-Konsolidierung: [Archiveinstieg](00-uebersicht/ARCHIVE_INDEX.md)
>
> Historische Status- und Navigationsfassungen bleiben als Provenienz erhalten und dürfen nicht mit der aktuellen Forschungsfront verwechselt werden.

# Objekt-X-Programm

*Ein langfristiges mathematisches Forschungsprogramm zur Riemannschen Hypothese.*

Objekt X bezeichnet das Ziel einer kompatiblen positiven Geometrie für die relevante Weil-Form-Struktur.

Das Programm arbeitet schrittweise über lokale positive Räume, gekoppelte Operatoren, Transportabbildungen und deren Kompatibilität. Drei lokale positive Kammern sind bis `A₁₁=log(11)/2` konstruiert. Der gegenwärtige Schwerpunkt liegt auf einer erneuerbaren positiven Reserve des niedrigen Schurrests für weitere Horizonte.

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

## O8 und O9: positiver Abschluss der ersten Kammer

Das [O8/O9-Forschungspaket](research/x-c1/first-chamber-o8-o9-2026-09-27/README.md)
ergänzt die rohen O1–O7-Transporte um zwei separat begründete Ergebnisse:

- **O8:** Neue Formraum-, Tail- und Kodimensionsreduktion sowie reproduzierte
  Zertifikate mit 191 strikt positiven Pivots je Parität. Kammerweit gilt
  `q_A[u] >= (12/10^30)||u||²` und
  `G_A >= [24/(23*10^30+24)] I > 10^-30 I`.
- **O9:** Positive korrigierte Readouts und vollständige Zielräume, isometrische
  Transporte, Quellintertwining und Cocycle für alle Paare und Tripel bis A₈.

Beide Ergebnisse sind als `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN` registriert.
Die eigenständige Ganzzahlprüfung bestätigt die O8-Zertifikatsarithmetik auf den
gebundenen Modellintervallen; eine externe analytische Abnahme bleibt offen.
Beweisanker, Reproduktionsbelege und Integrationsstand stehen in der
[`Survivor Registry`](00-uebersicht/SURVIVOR_REGISTRY.md).

---

## O10 bis A11: zwei weitere Kammern und allgemeines Wandgesetz

Das [zusammenhängende Forschungspaket](research/x-c1/chambers-through-a11-2026-09-28/README.md)
enthält die vollständige Abhängigkeitskette:

```text
O10: gekoppelte rohe q8-Wand
  → A9: zweite vollständige Terminalpositivität
  → allgemeines Ein-Wand-Lemma und q9
  → A11: dritte vollständige Terminalpositivität
```

- **A9:** `q_A[u] >= 10^-35 ||u||²`, mit 296 positiven Pivots je Parität.
- **A11:** `q_A[u] >= 10^-50 ||u||²` und
  `G_A >= 1/(13*10^50+1) I`, mit 285 positiven Pivots je Parität nach exakt
  rationaler Basisänderung und vollständig bezahlter ursprünglicher Norm.
- **Transport:** Positive korrigierte isometrische Transporte und Cocycle
  für alle `1<=A<=B<=C<=A11` über die q8- und q9-Wand.
- **Allgemeines Wandgesetz:** Rohe T-/D-Cocycles auf jedem festen endlichen
  Horizont. Vollständige Positivität benötigt weiterhin eigene Terminalreserven.
- **Allgemeiner hoher Tail:** Auf jedem festen endlichen Horizont wird der
  vollständige hohe Quellenraum bei ausreichend großem Schnitt positiv.
  Die dafür nötige Kodimension darf wachsen.

Die Ergebnisse sind `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`. Arb und getrennte
Ganzzahlarithmetik reproduzieren die Zertifikate auf den gebundenen vollständigen
Matrixintervallen. Die externe analytische Gesamtprüfung bleibt offen.

---

## Nächster lokaler Gate und weitere offene Aufgaben

### Erneuerbare Positivität des niedrigen Schurrests

Die [Spektral-/Renewal-Familie](research/x-c1/renewable-low-schur-spectral-2026-09-29/README.md)
liefert die echten kritischen Ränge **5/6/8 je Parität**, injektiven Transport
und kanonische Ergänzungen der Dimension **1/2** samt äußerer L2-Masse.
Die [kanonische Schurkopplungsfamilie](research/x-c1/canonical-schur-coupling-2026-09-30/README.md)
zertifiziert jetzt die tatsächlich starke relative Kopplung und einen
Spektralmischungsmechanismus auf einem echten kanonischen Zeugen. Die
Korollargrenzen für 1−κ betragen beim zweiten Übergang strikt weniger als
**1.371e-12 gerade** und **8.005e-12 ungerade**.

Der nächste lokale Schritt ist die **Isolation der tatsächlichen Maximiererrichtung**
durch zusätzliche gekoppelte Projektor-/Überlappbeziehungen. Die vorhandene
endliche Zertifikatsrelaxation lässt mehrere Richtungen und ungerade sogar
einen doppelten Eigenwert zu; daraus folgt keine Entartung des ursprünglichen
Operators. Allgemeines vorwärts gerichtetes Renewal bleibt offen.
Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.

Die hohe Tail-Reduktion steht auf jedem festen endlichen Horizont zur Verfügung.
Offen ist ein allgemeiner positiver Boden für den verbleibenden niedrigen Rest
einschließlich der gesamten hohen Kopplung. Die nächste Wand aktiviert `q=11`
strikt rechts von A11; die vollständige nächste Kammer ist noch nicht zertifiziert.

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

1. [`00-uebersicht/OBJEKT_X_GESAMTUEBERBLICK.md`](00-uebersicht/OBJEKT_X_GESAMTUEBERBLICK.md)  
   Zusammenhängende mathematische Gesamterzählung: klassische Grundlagen, eigene Resultate, No-Gos, heutige C1-Geometrie und offene globale Schritte.

2. [`00-uebersicht/CURRENT_STATE.md`](00-uebersicht/CURRENT_STATE.md)  
   Lesbare generierte Übersicht des registrierten Forschungsstands.

3. [`00-uebersicht/NEXT_GATES.md`](00-uebersicht/NEXT_GATES.md)  
   Aktuelle offene mathematische Gates und ihre Firewalls.

4. [`00-uebersicht/RESEARCH_STATE.yaml`](00-uebersicht/RESEARCH_STATE.yaml)  
   Kanonische operative Statusquelle mit Scopes, Abhängigkeiten und Beweisankern.

5. [`00-uebersicht/SURVIVOR_REGISTRY.md`](00-uebersicht/SURVIVOR_REGISTRY.md)  
   Konsolidierte Übersicht der weiterverwendbaren mathematischen Resultate.

6. [`00-uebersicht/OBJEKT_X_ARCHITECTURE.md`](00-uebersicht/OBJEKT_X_ARCHITECTURE.md)  
   Architektur und Stellung der lokalen Konstruktionen auf dem Weg zu Objekt X.

---

## Aktuelle Hauptfronten

Das Programm hat zwei getrennte langfristige Fronten.

### 1. Unbeschränkte Horizonterweiterung und kompatibler Transport

```text
UNRESTRICTED-HORIZON-AND-PROFILE-CONTINUATION
OPEN
```

Aktueller lokaler Einstieg: **erneuerbare Positivität des niedrigen Schurrests**.

Erneuerbare Profilreserven, eine unbeschränkte/kofinale Horizontfamilie und ihre positive Kompatibilität bleiben offen.

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

Der [Archiveinstieg](00-uebersicht/ARCHIVE_INDEX.md) bündelt die erhaltenen Originalfassungen, Inhaltsregister und datierten Konsolidierungsbelege. Er unterscheidet den abgeschlossenen Verwaltungsstand von weiterhin offenen mathematischen Prüfungen.

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
