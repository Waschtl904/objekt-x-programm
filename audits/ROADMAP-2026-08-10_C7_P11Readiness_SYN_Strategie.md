# ROADMAP-2026-08-10: C7 → P11-Readiness → SYN → Seal

**Status beim Anlegen:** C6 abgeschlossen (letzter P11/C6-Phasen-Knoten: C1zB2C5c). PASS-A ACTIVE.  
**Sync nach C7a:** 2026-08-10 | Commit `a6d9c0a106cabe21e6092ab2536c4c64aa72658b`  
**Ziel:** Kontrollierter, gatgestützter Abschluss bis SYN und anschließendes Seal.

---

## 1. Ausgangslage nach C6z

C6 hat keine generische offene Liste hinterlassen, sondern genau **einen abgegrenzten Residual-Theoremtyp** exportiert. Die drei offenen Punkte sind:

| Label | Inhalt | Blocker-Status |
|-------|--------|---------------|
| **R2** | Quasi-Null-Nichtapproximation | Zwingend für \(q_{r,T} \to 0\)-Aussage |
| **R3** | Observability der tatsächlichen \(J_T(\beta)\) | Zwingend für Alignment-Mechanismus |
| **Window-Lower-Transfer** | Untere Fenster-Transferschranke | Abhängig von R2/R3-Ausgang |

---

## 2. C7 – Residualspezifische Observability

### Scope (hart begrenzt)
C7 adressiert **ausschließlich** die drei aus C6z exportierten Punkte. Es gibt keine neuen Stränge außerhalb dieses Residuals.

### Knotenstruktur und aktueller Stand

| Knoten | Titel | Rolle | Status |
|--------|-------|-------|--------|
| **C7a** | ActualJumpCoefficientCensus | R3: Exakte Typisierung von \(J_T(\beta)\); konstruktive Hub/Rest/Identitäts-Zerlegung; Protected Pair \((x_T, -x_T)\); Zieltyp auf integrierte Observability korrigiert | ✅ **DONE** (`a6d9c0a`) |
| **C7b** | ProtectedJumpPair\_OffDiagonalGram\_IntegratedObservabilityTest | Kernfrage: Kann \(G_T / X \to 0\) auf P11-relevanter Skala gezeigt werden? | 🔵 offen |
| **C7c** | Window-Lower-Transfer | Nur bei positivem C7b-Ausgang; untere Fenster-Transferschranke | ⏳ wartet |
| **C7d** | Konsequenzaudit | Welche P11-Aussage folgt aus C7a–C7c? | ⏳ wartet |
| **C7-CLOSE** | Abschlussknoten | Expliziter Gate-Entscheid | ⏳ wartet |

### Was C7a geliefert hat

C7a hat mehr geliefert als eine Sprung-Auflistung:

- **Exakte Typisierung** des Residualkoeffizienten:
\[
J_T(\beta) = J_{h,T}(\beta) - \lambda_T J_{1,T}(\beta) - \lambda_T J_{g,T}(\beta), \quad g_T = R_T^* R_T \mathbf{1}_T
\]
- **Kandidat = tatsächlicher Breakpoint:** \(\beta \in B_T^{\mathrm{act}}\) genau dann, wenn \(J_T(\beta) = 0\) nach allen Cancellations
- **Protected Pair (C6i-geschützt):** An \(x_T = T^{-1/2}\log(q_T/2)\), \(q_T \in \{3,5\}\) verschwinden Rest- und Identitätssprung exakt:
\[
|J_T(x_T)| = |J_{h,T}(x_T)| \geq j^* > 0, \quad J_T(-x_T) = -J_T(x_T)
\]
- **Starker neuer Satz** (integrierte Positivität für festes \(T\)):
\[
\lim_{X\to\infty} \frac{1}{2X}\int_{-X}^X |P_T(\xi)|^2\,d\xi = \sum_{\beta \in B_T^{\mathrm{act}}} |J_T(\beta)|^2 \geq 2{j^*}^2
\]
- **Korrektur des Zieltyps:** Globale punktweise Schranke \(|P_T(\xi)| \geq c|\xi|\|r_T\|\) kann nicht stimmen (\(P_T(\xi) = O_T(\xi^2)\) nahe 0). Verfolgt wird **integrierte Observability**.
- **Baker/Wüstholz eingeordnet:** Klassische Resultate über lineare Formen in Logarithmen betreffen Lageabstände; sie kontrollieren nicht die Cancellation der Koeffizienten in \(P_T\). C7a nutzt sie bewusst noch nicht.

### Mathematischer Eingang für C7b

C7a isoliert die Offdiagonalinterferenz:
\[
G_T = \sum_{\beta \neq \gamma} |\beta - \gamma| \cdot |J_T(\beta) J_T(\gamma)|
\]
mit der exakten Schranke:
\[
\frac{1}{2X}\int_{-X}^X |P_T(\xi)|^2\,d\xi \geq 2{j^*}^2 - \frac{G_T}{X}
\]
C7b hat damit **genau eine Kernfrage:** Kann \(G_T / X\) auf einer mit \(T\) kontrollierten Frequenzskala klein genug gemacht werden?

### Entscheidgabel in C7-CLOSE
Nach C7-CLOSE gibt es genau zwei Pfade — kein automatisches C8:

**Pfad A (stark):** C7 beweist \(q_{r,T} \to 0\) vollständig  
→ P11-Readiness-Audit mit voller Theoremstärke möglich

**Pfad B (schwach):** C7 zeigt, dass der starke Satz nicht nötig ist; P11 schließt mit schwächerer aber vollständiger Aussage  
→ P11-Readiness-Audit mit angepasster Theoremformulierung

**Pfad X (Blocker):** C7 löst den zentralen Blocker nicht  
→ **Bewusster Entscheid** über genau einen weiteren mathematischen Block (nicht automatisch C8–C10)

---

## 3. P11-Readiness-Audit (Gate vor SYN)

Nach C7-CLOSE wird **nicht automatisch** weitergemacht. Stattdessen findet ein strukturierter Readiness-Check statt:

### Checkliste P11-Readiness

- [ ] **Hauptsätze vollständig bewiesen?** — Explizite Auflistung mit Audit-Referenz
- [ ] **Kritische \([O]\) identifiziert?** — Welche offenen Observables sind für den eigentlichen P11-Satz zwingend?
- [ ] **Verstärkungen vs. Notwendigkeiten getrennt?** — Offene Punkte, die nur Schärfungen, nicht Grundlage sind, werden explizit als „nicht-blockierend" klassifiziert
- [ ] **Keine unzulässigen Implikationen?** — Abhängigkeiten von No-Gos geprüft
- [ ] **Keine versteckten Firewalls?** — Insbesondere: Kein unbewiesener Übergang der Form \(\lambda_T \asymp T e^T\) oder ähnlich
- [ ] **Beweiskette geschlossen?** — Vom Gram-Kern bis zum P11-Hauptsatz lückenlos

### Gate-Entscheid
- **PASS:** → Unmittelbarer Wechsel von PASS-A ACTIVE zu SYN
- **FAIL:** → Genau eine begründete Entscheidung (neuer Block oder schwächere Theorem-Formulierung)

---

## 4. SYN

SYN ist die **Verdichtung**, keine neue Mathematik. Konkret:

- Die Auditknoten C1–C7 + alle Reconciliation-Dokumente werden zu einer **einzigen konsistenten Argumentkette** komprimiert
- Kleine Lücken dürfen sichtbar werden — aber wenn ein fundamental neuer Satz nötig wäre, war die Readiness-Prüfung zu früh
- SYN endet mit einem **SYN-Reaudit** (analog zu den bestehenden SYN-Primaer- und Zweitchecks für P05–P10)

---

## 5. Seal

Seal setzt nach dem SYN-Reaudit. Voraussetzungen:

- **Keine theorem-kritischen `?[O]` mehr**
- **Keine versteckten Firewalls** (insbesondere kein unbewiesener \(\lambda_T \asymp T e^T\)-Übergang oder äquivalent)
- SYN-Reaudit bestanden

---

## 6. papers/P11

Das Paper entsteht **erst aus dem versiegelten Stand**. Es ist dann:
- keine Forschungsnotiz
- die komprimierte Darstellung dessen, was durch die Audits vollständig getragen wird

---

## 7. Harte Regel (verbindlich ab sofort)

> **Nach C7-CLOSE gibt es zwingend den P11-Readiness-Entscheid.**  
> Kein automatisches C8, C9, C10.  
> Falls C7 den zentralen Blocker nicht löst: **bewusster Einzelentscheid** über genau einen weiteren mathematischen Block.

---

## 8. Aktueller Standort

```
C6 abgeschlossen (letzter Knoten: P11/C1zB2C5c)
      ↓
   C7a ✅ ActualJumpCoefficientCensus (a6d9c0a)
   [J_T(beta) exakt typisiert; Protected Pair; integrierte Positivität bewiesen]
      ↓
   C7b 🔵 ProtectedJumpPair_OffDiagonalGram_IntegratedObservabilityTest
   [Kernfrage: G_T/X → 0 auf P11-relevanter Skala?]
      ↓
   C7c ⏳ Window-Lower-Transfer
      ↓
   C7d ⏳ Konsequenzaudit
      ↓
   C7-CLOSE ⏳
      ↓
   P11-Readiness-Audit
   [Gate: alle Hauptsätze, kritische [O], Firewalls]
      ↓ (bei PASS)
   SYN
   [Verdichtung, keine neue Mathematik]
      ↓
   SYN-Reaudit
      ↓
   Seal
      ↓
   papers/P11
```

---

*Initiales Protokoll: 2026-08-10 | Sync nach C7a: 2026-08-10 20:56 CEST | PASS-A ACTIVE*
