# ROADMAP-2026-08-10: C7 → P11-Readiness → SYN → Seal

**Status beim Anlegen:** C6 abgeschlossen (letzter Knoten: C6z — `C6Closure_ResidualSpectralBlocker_CompletionDecision`). PASS-A ACTIVE.  
**Sync nach C7a:** 2026-08-10 | Commit `a6d9c0a106cabe21e6092ab2536c4c64aa72658b`  
**Roadmap-Firewall-Sync:** 2026-08-10 | vier mathematische Schreibfehler korrigiert  
**Sync nach C7b:** 2026-08-11 | Commit `0812f3f3ba54a670479241d993eba557f734e5d7`  
**Formelfix (3 Regressionen):** 2026-08-11 | Commits `fa72645` → dieser  
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
- **Kandidat vs. tatsächlicher Breakpoint:** \(\beta \in \mathcal{B}_T^{\mathrm{act}}\) genau dann, wenn \(J_T(\beta) \neq 0\) nach allen Cancellations. *(Korrektur: \(\neq 0\), nicht \(= 0\))*
- **Protected Pair (C6i-geschützt):** An
\[
x_T = T-\frac12\log(q_T/2), \quad q_T \in \{3,5\},
\]
verschwinden Rest- und Identitätssprung exakt:
\[
|J_T(x_T)| = |J_{h,T}(x_T)| \geq j^* > 0, \quad J_T(-x_T) = -J_T(x_T).
\]
- **Integrierte Positivität für festes \(T\):**
\[
\lim_{X\to\infty} \frac{1}{2X}\int_{-X}^X |P_T(\xi)|^2\,d\xi = \sum_{\beta \in \mathcal{B}_T^{\mathrm{act}}} |J_T(\beta)|^2 \geq 2{j^*}^2.
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
Eine natürliche hinreichende Schranke ist
\[
\delta_T^{\mathrm{act}} \gg \frac{e^{-5T}}{T}.
\]
Die stärkere Bedingung \(\delta_T^{\mathrm{act}}\gg T e^{-5T}\) würde ebenfalls genügen, ist aber nicht die aus der obigen Abschätzung natürliche Skala. C6v verhindert ohnehin, einen solchen Satz aus der Kandidatengeometrie allein zu ziehen.

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

### C7d – Konsequenzaudit (nächster Knoten)

C7d prüft in strikter Reihenfolge:

1. **Originalcheck:** Verlangt der ursprüngliche P11-Hauptsatz quantitative Residual-Observability (\(q_{r,T} \to 0\), \(a_{R,T}^{(2)} = 0\) oder äquivalente uniforme Untergrenze)? Falls ja: Das offene signierte Kriterium \(S_T(X_T) \geq -(1-\eta)D_T\) ist **theorem-kritisch** und darf nicht stillschweigend durch eine strukturelle Ersatzfassung umgangen werden.

2. **Struktursatz-Inventar:** Was ist der stärkste heute tatsächlich bewiesene P11-Struktursatz?

3. **Entscheid:** Falls der ursprüngliche Hauptsatz weiterhin R3 benötigt:
   - P11 strukturell weit fortgeschritten, aber **original-seal-not-ready**
   - C7 wird trotzdem als Untersuchungsblock geschlossen
   - Der exakt benannte R3-Blocker wird weitergetragen
   - Das ist **kein Scheitern von C7** — C7 hat sauber festgestellt, welche eine Aussage noch fehlt und welche scheinbaren Ersatzwege nicht funktionieren

### Entscheidgabel in C7-CLOSE

**Pfad A (stark):** C7 beweist \(q_{r,T} \to 0\) vollständig → P11-Readiness mit voller Theoremstärke  
**Pfad B (schwach):** P11 schließt mit schwächerer aber **vollständiger** Aussage → P11-Readiness mit angepasster Formulierung  
**Pfad X (Blocker):** C7 benennt exakt den verbleibenden Blocker → bewusster Einzelentscheid, kein automatisches C8–C10

---

## 3. P11-Readiness-Audit (Gate vor SYN)

Nach C7-CLOSE wird **nicht automatisch** weitergemacht.

### Checkliste P11-Readiness

- [ ] **Hauptsätze vollständig bewiesen?** — Explizite Auflistung mit Audit-Referenz
- [ ] **Kritische \([O]\) identifiziert?** — Welche offenen Observables sind für den eigentlichen P11-Satz zwingend?
- [ ] **Verstärkungen vs. Notwendigkeiten getrennt?** — Offene Punkte als nicht-blockierend klassifiziert
- [ ] **Keine unzulässigen Implikationen?** — Abhängigkeiten von No-Gos geprüft
- [ ] **Keine versteckten Firewalls?** — Kein unbewiesener Übergang \(\lambda_T \asymp T e^T\) oder ähnlich
- [ ] **Beweiskette geschlossen?** — Vom Gram-Kern bis zum P11-Hauptsatz lückenlos

### Gate-Entscheid
- **PASS:** → Wechsel von PASS-A ACTIVE zu SYN
- **FAIL:** → Genau eine begründete Entscheidung

---

## 4. SYN

Verdichtung, keine neue Mathematik. C1–C7 + alle Reconciliation-Dokumente zu einer konsistenten Argumentkette. Endet mit **SYN-Reaudit**.

---

## 5. Seal

Nach SYN-Reaudit. Voraussetzungen: keine theorem-kritischen `?[O]`, keine versteckten Firewalls, SYN-Reaudit bestanden.

---

## 6. papers/P11

Erst aus dem versiegelten Stand. Komprimierte Darstellung dessen, was durch die Audits vollständig getragen wird.

---

## 7. Harte Regel

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
      ↓
   C7d 🔵 Konsequenzaudit  ← NÄCHSTER KNOTEN
   [Original-P11-Hauptsatz vs. stärkster bewiesener Struktursatz;
    R3-Blocker theorem-kritisch oder nicht?]
      ↓
   C7-CLOSE ⏳
      ↓
   P11-Readiness-Audit → SYN → SYN-Reaudit → Seal → papers/P11
```

---

*Initiales Protokoll: 2026-08-10 | Sync C7a: 2026-08-10 | Sync C7b: 2026-08-11 | Formelfix: 2026-08-11 08:49 CEST | PASS-A ACTIVE*
