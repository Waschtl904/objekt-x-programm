# NEU-53 — X.3.23: Operatorstatus von D_rel = iJ_N^- — Selbstadjungiertheit, Spektrum, Spektralmaßform

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-52  
**Ziel:** Essentielle Selbstadjungiertheit von iJ^-, Spektralalternativen, robuste Spektralmaß-Form für R_rel.

---

## 0. Gefährliche Abkürzung (Obstruktion)

Nicht Spektralart zuerst erraten, sondern Operatorfrage entscheiden:

\[
\boxed{\text{Was ist }D_{\mathrm{rel}}\text{ als Operator? Domäne, Symmetrie, essentielle Selbstadjungiertheit.}}
\tag{53.D0}
\]

Erst danach ist klar, ob \(\sum_\alpha\) eine Summe oder ein Spektralintegral ist.

---

## 1. Drei Ebenen strikt trennen

\[
D_{\mathrm{rel},N} = iJ_N^- \quad\text{für endliches }N.
\tag{53.1}
\]
\[
D_{\mathrm{rel},\infty} = \lim_{N\to\infty} D_{\mathrm{rel},N} \quad\text{(im Grenzoperatorsinn).}
\tag{53.2}
\]
\[
(D_{\mathrm{rel},\infty}-s)^{-1} \quad\text{als Resolvente des Grenzoperators.}
\tag{53.3}
\]

**Endliches N:** Auf endlichdimensionalem Raum ist \(J_N^{-*} = -J_N^-\), also \(iJ_N^-\) selbstadjungiert und \(\sigma(D_{\mathrm{rel},N}) \subset \mathbb{R}\) diskret. Harmlos.

**Engpass:** Der Grenzübergang \(N\to\infty\).

---

## 2. Satz 53.1 — Symmetrie und essentielle Selbstadjungiertheit

**Startdomäne:**

\[
\mathcal{D}_0 = \mathrm{span}_{\mathrm{fin}}\{\eta_{p;m;r,u}\}.
\tag{53.4}
\]

Auf \(\mathcal{D}_0\) gilt formal:

\[
\langle iJ^- x, y\rangle = \langle x, iJ^- y\rangle,
\tag{53.5}
\]

also ist \(iJ^-\) symmetrisch.

**Ziel-Satz:**

\[
\boxed{iJ^-\text{ ist wesentlich selbstadjungiert auf }\mathcal{D}_0.}
\tag{53.6}
\]

Äquivalent (Defizit-Index-Kriterium):

\[
\ker((iJ^-)^* - i) = 0, \qquad \ker((iJ^-)^* + i) = 0.
\tag{53.7}
\]

Est danach ist

\[
D_{\mathrm{rel}} = \overline{iJ^-}
\tag{53.8}
\]

kanonisch selbstadjungiert, und \((D_{\mathrm{rel}}-s)^{-1}\) ist für \(s\notin\mathbb{R}\) wohldefiniert.

**Beweisweg-Kandidaten:**
- Nelson-Kriterium: dichte analytische Vektoren.
- Kato-Rellich: falls \(J_N^- = A + B\) mit \(A\) selbstadjungiert und \(B\) relativ beschränkt.
- Direkte Abschätzung der Defizit-Kerne via \(\Theta_N\)-Struktur.

Status: \(\:?\:\) [O] \(\to\) erster Beweis-Engpass.

---

## 3. Satz 53.2 — Spektralalternativen

Nach Selbstadjungiertheit drei mögliche Fälle:

### Fall A — Diskretes Spektrum

\[
\sigma(D_{\mathrm{rel}}) = \{\lambda_\alpha\}_{\alpha\in A},\quad D_{\mathrm{rel}}\phi_\alpha=\lambda_\alpha\phi_\alpha.
\tag{53.9}
\]

Dann:

\[
R_{\mathrm{rel}}(s)[a,b] = \sum_\alpha \frac{\overline{\langle\phi_\alpha,\eta_a\rangle}\,\langle\phi_\alpha,\eta_b\rangle}{\lambda_\alpha-s}.
\tag{53.10}
\]

Voraussetzung: \((D_{\mathrm{rel}}-i)^{-1}\) ist kompakt.

### Fall B — Rein kontinuierliches Spektrum

Keine \(\ell^2\)-Eigenbasis. Robuste Form:

\[
R_{\mathrm{rel}}(s)[a,b] = \int_{\mathbb{R}} \frac{1}{\lambda-s}\,d\mu_{a,b}(\lambda),
\quad
\mu_{a,b}(\Delta) = \langle\eta_a, E_{D_{\mathrm{rel}}}(\Delta)\eta_b\rangle.
\tag{53.11}
\]

### Fall C — Gemischtes Spektrum

\[
R_{\mathrm{rel}}(s)[a,b]
= \sum_{\alpha\in\sigma_{\mathrm{pp}}} \frac{\overline{\langle\phi_\alpha,\eta_a\rangle}\,\langle\phi_\alpha,\eta_b\rangle}{\lambda_\alpha-s}
+ \int_{\sigma_{\mathrm{cont}}} \frac{1}{\lambda-s}\,d\mu_{a,b}^{\mathrm{cont}}(\lambda).
\tag{53.12}
\]

**Robuste Einheitsform (alle drei Fälle):**

\[
\boxed{
R_{\mathrm{rel}}(s)[a,b] = \int_{\mathbb{R}} \frac{1}{\lambda-s}\,d\mu_{a,b}(\lambda).
}
\tag{53.13}
\]

Die diskrete Summe ist nur ein Spezialfall. NEU-51/52 sind damit korrekt, sobald \(\sum_\alpha\) durch \(\int d\mu\) ersetzt wird.

---

## 4. Satz 53.3 — Kompakter Resolvent als Testkriterium

\[
\boxed{
D_{\mathrm{rel}}\text{ hat kompakten Resolventen}
\iff
\sigma(D_{\mathrm{rel}})\text{ diskret mit endlicher Multiplizität.}
}
\tag{53.14}
\]

**Hinreichende Bedingung für Kompaktheit (Konfinement):**

\[
\|D_{\mathrm{rel}}\,\eta_a\| \to \infty \quad\text{entlang Basisflucht }a\to\infty,
\tag{53.15}
\]

oder äquivalent:

\[
\|(D_{\mathrm{rel}}-i)^{-1}\eta_a\| \to 0 \quad\text{entlang }a\to\infty.
\tag{53.16}
\]

**Erwartung für J_N^-:** Ein Jacobi-/Graphoperator auf unendlichem Raum hat generisch kontinuierliche Spektralanteile, sofern kein Konfinement durch \(\log(n)\)-Gewichte eingebaut ist. Die \(\gamma_N\log(n)\)-Gewichte in \(\Theta_N\) könnten Konfinement liefern.

Status: \(\:?\:\) [O] — Konfinement-Test ausständig.

---

## 5. Satz 53.4 — Projektionskoeffizienten als globale Jacobi-Eigenfunktionen

\[
c_\alpha(a) := \langle\phi_\alpha,\eta_a\rangle
\tag{53.17}
\]

erfüllt die globale Rekursion:

\[
\sum_b (iJ_N^-)_{ab}\,c_\alpha(b) = \lambda_\alpha c_\alpha(a),
\quad\text{d.h.}\quad
i\Theta_N^-\,c_\alpha = \lambda_\alpha c_\alpha.
\tag{53.18}
\]

Also: \(\langle\phi_\alpha,\eta_{p;n;r,u}\rangle\) sind **globale Jacobi-Eigenfunktionen auf dem gesamten Kopplungsgraphen**, nicht lokale Kanal-Größen.

Explizite Berechenbarkeit \(\iff\) Lösung der globalen Jacobi-Rekursion von \(i\Theta_N^-\).

Status: \(\:?\:\) [O]

---

## 6. Spurklasse-Kriterium (allgemeine Spektralmaß-Form)

Im allgemeinsten Fall:

\[
\boxed{
\int_{\mathbb{R}} \frac{1}{|\lambda-s|}\,d\nu_N(\lambda) < \infty,
\quad
d\nu_N(\lambda) = \|V_N^*\,dE_{D_{\mathrm{rel}}}(\lambda)\|_{\mathcal{S}_2}^2.
}
\tag{53.19}
\]

Im diskreten Spezialfall reduziert auf:

\[
\sum_\alpha \frac{\|V_N^*\phi_\alpha\|^2}{|\lambda_\alpha-s|} < \infty.
\tag{53.20}
\]

**Vollständige K_pq-Formel (spektralmaßrobust):**

\[
\boxed{
K_{pq}(s)_{(r,n),(t,m)}
= r\,t\,\log p\,\log q
\sum_{u,v} u\,v
\int_{\mathbb{R}} \frac{1}{\lambda-s}\,d\mu_{(p;n;r,u),(q;m;t,v)}(\lambda).
}
\tag{53.21}
\]

Das ist die allgemein korrekte Form von NEU-52 Formel (52.6).

---

## 7. Designentscheidung: Zwei Wege

| Weg | Voraussetzung | Konsequenz |
|---|---|---|
| **A — Diskreter Weg** | Kompakter Resolvent von \(D_{\mathrm{rel}}\) | \(\{\lambda_\alpha,\phi_\alpha\}\), Summenformel, Jacobi-Eigenfunktionen |
| **B — Spektralmaß-Weg** | Nur Selbstadjungiertheit | \(E_{D_{\mathrm{rel}}}(\lambda)\), Integralformel, keine Eigenbasis nötig |

Weg B ist robuster; Weg A ist schöner für explizite Rechnungen.

**Empfehlung:** Zeige erst essentielle Selbstadjungiertheit (Weg B-Basis), dann teste Konfinement (Weg A falls möglich).

---

## 8. Statusmatrix

| Aussage | Status |
|---|---|
| Drei-Ebenen-Trennung (53.1–53.3) | ✓ [M] |
| Symmetrie \(iJ^-\) auf \(\mathcal{D}_0\) | ✓ [M] formal |
| Essentielle Selbstadjungiertheit (53.6–53.7) | \(\:?\:\) [O] Erster Beweis-Engpass |
| Kompakter Resolvent / Konfinement (53.15) | \(\:?\:\) [O] |
| Robuste Spektralmaß-Form (53.13, 53.21) | ✓ [M] strukturell |
| Projektionskoeffizienten \(c_\alpha(a)\) via Jacobi-Rekursion (53.18) | \(\:?\:\) [O] |
| Spurklasse via (53.19) | \(\:?\:\) [O] |

---

## 9. Nächster Schritt

\[
\boxed{
\text{NEU-54: Beweis essentieller Selbstadjungiertheit von }iJ^-\text{ auf }\mathcal{D}_0\text{; Konfinement-Test via }\gamma_N\log(n)\text{-Gewichte.}
}
\]

Teilfragen:
1. Welcher Beweisweg (Nelson / Kato-Rellich / Defizit-Index direkt)?
2. Liefern \(\gamma_N\log(n)\)-Gewichte hinreichendes Konfinement für kompakten Resolventen?
3. Falls kein Konfinement: Spektralmaß \(\mu_{a,b}\) direkt aus \(\Theta_N\)-Matrixelementen?
