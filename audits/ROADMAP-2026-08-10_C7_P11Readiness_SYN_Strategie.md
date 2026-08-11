# ROADMAP-2026-08-10: C7 → P11-Readiness → SYN → Seal

**Status beim Anlegen:** C6 abgeschlossen (letzter Knoten: C6z — `C6Closure_ResidualSpectralBlocker_CompletionDecision`). PASS-A ACTIVE.  
**Sync nach C7a:** 2026-08-10 | Commit `a6d9c0a106cabe21e6092ab2536c4c64aa72658b`  
**Roadmap-Firewall-Sync:** 2026-08-10 | vier mathematische Schreibfehler korrigiert  
**Sync nach C7b:** 2026-08-11 | Commit `0812f3f3ba54a670479241d993eba557f734e5d7`  
**Ziel:** Kontrollierter, gategestützter Abschluss bis SYN und anschließendes Seal.

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
| **C7b** | ProtectedJumpPair\_OffDiagonalGram\_IntegratedObservabilityTest | Exakte Gramidentität \(D_T + S_T(X)\); skalenadaptierte Größe \(C_T(X)\); No-Go gegen Grobinvarianten bewiesen; korrigierter R3-Zieltyp \(S_T(X_T) \geq -(1-\eta)D_T\) | ✅ **DONE** (`0812f3f`) |
| **C7c** | Window-Lower-Transfer | Untere Fenster-Transferschranke | ⛔ **NICHT GETRIGGERT** — noch keine quantitative R3-Untergrenze vorhanden |
| **C7d** | Konsequenzaudit | Ist die offene signierte/clustered R3-Observability theorem-kritisch für P11? Oder kann P11 mit einer schwächeren vollständigen Aussage schließen? | 🔵 **NÄCHSTER KNOTEN** |
| **C7-CLOSE** | Abschlussknoten | Expliziter Gate-Entscheid | ⏳ wartet |

---

### Was C7a geliefert hat

- **Exakte Typisierung** des Residualkoeffizienten:
\[
J_T(\beta) = J_{h,T}(\beta) - \lambda_T J_{1,T}(\beta) - \lambda_T J_{g,T}(\beta), \quad g_T = R_T^* R_T \mathbf{1}_T.
\]
- **Kandidat = tatsächlicher Breakpoint:** \(\beta \in \mathcal B_T^{\mathrm{act}}\) genau dann, wenn \(J_T(\beta) = 0\) nach allen Cancellations.
- **Protected Pair (C6i-geschützt):** An \(x_T = T^{-1/2}\log(q_T/2)\), \(q_T \in \{3,5\}\) verschwinden Rest- und Identitätssprung exakt:
\[
|J_T(x_T)| = |J_{h,T}(x_T)| \geq j^* > 0, \quad J_T(-x_T) = -J_T(x_T).
\]
- **Integrierte Positivität für festes \(T\):**
\[
\lim_{X\to\infty} \frac{1}{2X}\int_{-X}^X |P_T(\xi)|^2\,d\xi = \sum_{\beta \in \mathcal B_T^{\mathrm{act}}} |J_T(\beta)|^2 \geq 2{j^*}^2.
\]
- **Zieltyp-Korrektur:** Globale punktweise Schranke strukturell unerreichbar (\(P_T(\xi) = O_T(\xi^2)\) nahe 0); verfolgt wird **integrierte Observability**.
- **Baker/Wüstholz eingeordnet:** Nur für Lageabstände relevant, nicht für Koeffizienten-Cancellation in \(P_T\).

---

### Was C7b geliefert hat

#### Exakte finite-\(X\)-Gramidentität
\[
\frac{1}{2X}\int_{-X}^X |P_T(\xi)|^2\,d\xi = D_T + S_T(X)
\]
mit
\[
D_T = \sum_\beta |J_T(\beta)|^2 \geq 2{j^*}^2
\]
und dem signierten Offdiagonalterm
\[
S_T(X) = \sum_{\beta \neq \gamma} J_T(\beta)\overline{J_T(\gamma)}\,\frac{\sin(X(\beta-\gamma))}{X(\beta-\gamma)}.
\]

#### Skalenadaptierte Offdiagonalgröße
Die C7a-Größe \(\mathfrak{G}_T\) liefert \(|S_T(X)| \leq \mathfrak{G}_T / X\), aber bei engen Kollisionen \(|\beta - \gamma| \ll X^{-1}\) sättigt der echte Grambeitrag bei 1 — die Singularität in \(\mathfrak{G}_T\) ist ein Artefakt der absoluten Abschätzung. Die intrinsische Größe ist:
\[
C_T(X) = \sum_{\beta \neq \gamma} |J_T(\beta)J_T(\gamma)|\,\min\!\left\{1,\,\frac{1}{X|\beta-\gamma|}\right\}.
\]

#### Explizites logisches No-Go (bewiesen)
Es existieren abstrakte gerade, kompakt getragene Stufenfunktionen mit \(P(0)=P'(0)=0\), festem Protected Pair und uniform beschränkter TV, während \(G \to \infty\). Konsequenz:
\[
\text{Protected Pair} + \text{Nullmomente} + \text{TV} \not\Rightarrow \mathfrak{G}_T\text{-Kontrolle}.
\]
Das widerlegt ausschließlich die Schlusskette aus den bisherigen Grobinvarianten — kein Gegenbeispiel gegen das tatsächliche \(r_T\).

#### Grobe Gap-Rechnung
Mit \(\delta_T^{\mathrm{act}} = \min_{\beta \neq \gamma}|\beta-\gamma|\) und C6z:
\[
\mathfrak{G}_T \lesssim \frac{T^4 e^{4T}}{\delta_T^{\mathrm{act}}}, \qquad
\frac{\mathfrak{G}_T}{X_T} \lesssim \frac{1}{T e^{5T} \delta_T^{\mathrm{act}}} \quad (X_T \asymp T^5 e^{9T}).
\]
Eine Schranke \(\delta_T^{\mathrm{act}} \gg T e^{-5T}\) würde genügen — aber C6v verhindert, diesen Satz aus der Kandidatengeometrie zu ziehen (synchronisierte arbiträr enge Kandidatenkollisionen möglich).

#### Korrigierter R3-Zieltyp
Nicht mehr \(\mathfrak{G}_T / X_T \to 0\), sondern das **signierte Kriterium**:
\[
S_T(X_T) \geq -(1-\eta)\,D_T \quad \text{für ein festes } \eta > 0.
\]
Dann folgt unmittelbar:
\[
\frac{1}{2X_T}\int_{-X_T}^{X_T} |P_T(\xi)|^2\,d\xi \geq \eta D_T \geq 2\eta{j^*}^2.
\]

#### Warum C7c nicht getriggert wird
Ohne quantitative R3-Untergrenze wäre ein Window-Lower-Transfer genau die unbewiesene Brücke, die die Roadmap ausschließt.

---

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
C6 abgeschlossen (letzter Knoten: C6z)
      ↓
   C7a ✅ ActualJumpCoefficientCensus (a6d9c0a)
   [J_T(beta) exakt typisiert; Protected Pair; integrierte Positivität bewiesen]
      ↓
   C7b ✅ ProtectedJumpPair_OffDiagonalGram_IntegratedObservabilityTest (0812f3f)
   [Exakte Gramidentität D_T + S_T(X); C_T(X) als intrinsische Größe;
    No-Go gegen Grobinvarianten bewiesen; R3-Ziel: S_T(X_T) >= -(1-eta)*D_T]
      ↓
   C7c ⛔ Window-Lower-Transfer (NICHT GETRIGGERT)
   [Keine quantitative R3-Untergrenze vorhanden]
      ↓
   C7d 🔵 Konsequenzaudit  ← NÄCHSTER KNOTEN
   [Ist signierte/clustered R3-Observability theorem-kritisch für P11?
    Oder: P11 mit schwächerer vollständiger Aussage schließbar?]
      ↓
   C7-CLOSE ⏳
      ↓
   P11-Readiness-Audit
   [Gate: alle Hauptsätze, kritische [O], Firewalls]
      ↓ (bei PASS)
   SYN → SYN-Reaudit → Seal → papers/P11
```

---

*Initiales Protokoll: 2026-08-10 | Sync C7a: 2026-08-10 | Sync C7b: 2026-08-11 08:17 CEST | PASS-A ACTIVE*
