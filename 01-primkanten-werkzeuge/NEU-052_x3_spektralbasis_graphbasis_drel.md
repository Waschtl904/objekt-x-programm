# NEU-52 — X.3.22: Spektralbasis-Blatt — η-Graphbasis vs. globale Eigenbasis von D_rel

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-51  
**Ziel:** Klärung η vs. φ, globale Spektralformel für K_pq, S1/S2-Kriterium ohne kanalweise Diagonalisierungsannahme.

---

## 0. Gefährliche Abkürzung (Obstruktion)

Würde man η_{p;m;r,u} als Eigenbasis von D_rel behandeln:

\[
D_{\mathrm{rel}}\,\eta_{p;m;r,u} = \lambda_{p;m;r,u}\,\eta_{p;m;r,u},
\tag{52.WARN}
\]

so erhielte man formal

\[
R_{\mathrm{rel}}(s)[a,b] = \frac{\delta_{a,b}}{\lambda_a - s},
\]

und die Off-Diagonal-Terme K_{pq} für p≠q verschwänden, sofern die Kanalindizes orthogonal sind. Das würde den Befund von NEU-50 rückgängig machen.

\[
\boxed{\times\,[M]:\quad \eta_{p;m;r,u}\text{ darf nicht als Eigenbasis von }D_{\mathrm{rel}}\text{ behandelt werden.}}
\tag{52.D0}
\]

---

## 1. Satz 52.1 — η ist Graphbasis, nicht Eigenbasis

Die Vektoren \(\eta_{p;m;s,u} \sim e_{u+ps}V_{pm}\) spannen den relativen Kopplungsraum

\[
\mathcal{H}_{\mathrm{rel}} = \overline{\mathrm{span}}\{\eta_{p;m;s,u}\}
\tag{52.1}
\]

dicht auf. Sie sind eine **Kopplungs-/Graphbasis** — keine Spektralbasis.

Im Allgemeinen gilt:

\[
D_{\mathrm{rel}}\,\eta_a = \sum_b J_{ba}\,\eta_b
\qquad (J_{ba}\neq 0 \text{ generisch für }a\neq b),
\tag{52.2}
\]

weil \(D_{\mathrm{rel}} = iJ_N^-\) und \(J_N^-\) durch \(\Theta_N\) mit gewichtetem Fourier-Shift definiert ist (NEU-30 ff.).

Status: ✓ [M]

---

## 2. Satz 52.2 — Globale Spektralformel

Sei \(\{\phi_\alpha\}\) die globale Spektralbasis (Eigen- oder Spektralmaßbasis) von \(D_{\mathrm{rel}}\):

\[
D_{\mathrm{rel}}\,\phi_\alpha = \lambda_\alpha\,\phi_\alpha.
\tag{52.3}
\]

Dann ist der Resolvent-Kernel:

\[
R_{\mathrm{rel}}(s)[a,b]
:= \langle\eta_a,(D_{\mathrm{rel}}-s)^{-1}\eta_b\rangle
= \sum_\alpha \frac{\overline{\langle\phi_\alpha,\eta_a\rangle}\,\langle\phi_\alpha,\eta_b\rangle}{\lambda_\alpha-s}.
\tag{52.4}
\]

Bei kontinuierlichem Spektrum (Spektralmaß \(\mu_{a,b}\)):

\[
R_{\mathrm{rel}}(s)[a,b]
= \int_{\sigma(D_{\mathrm{rel}})} \frac{1}{\lambda-s}\,d\mu_{a,b}(\lambda).
\tag{52.5}
\]

Die vollständige Matrixelement-Formel für \(K_{pq}\) wird damit:

\[
\boxed{
K_{pq}(s)_{(r,n),(t,m)}
= r\,t\,\log p\,\log q\;
\sum_{u,v,\alpha}
uv\,
\frac{\overline{\langle\phi_\alpha,\eta_{p;n;r,u}\rangle}\,
\langle\phi_\alpha,\eta_{q;m;t,v}\rangle}
{\lambda_\alpha-s}.
}
\tag{52.6}
\]

**Schlüsselpunkt:** Für \(p\neq q\) ist \(K_{pq}(s)\neq 0\) genau dann, wenn die globalen Moden \(\phi_\alpha\) nicht kanaldiagonal sind, d.h. wenn

\[
\langle\phi_\alpha,\eta_{p;n;r,u}\rangle\neq 0
\quad\text{und}\quad
\langle\phi_\alpha,\eta_{q;m;t,v}\rangle\neq 0
\tag{52.7}
\]

gleichzeitig für dasselbe \(\alpha\) und \(p\neq q\) gelten. Das ist generisch der Fall, sofern \(D_{\mathrm{rel}}\) keine kanaldiagonale Blockstruktur hat.

Status: ✓ [M] strukturell.

---

## 3. Satz 52.3 — Spurklasse-Kriterium über globale Moden

**Die korrekte (nicht kanalweise) Bedingung:**

\[
\boxed{
\sum_\alpha \frac{\left\|\sum_{p\le N}V_p^*\phi_\alpha\right\|^2}{|\lambda_\alpha-s|} < \infty.
}
\tag{52.8}
\]

Hinreichend für \(\mathcal{K}_N(s)\in\mathcal{S}_1\) via \((D_{\mathrm{rel}}-s)^{-1/2}V_N\in\mathcal{S}_2\).

**Warum kohärent, nicht kanalweise:** Die Norm enthält Kreuzterme:

\[
\left\|\sum_{p\le N}V_p^*\phi_\alpha\right\|^2
= \sum_{p,q\le N}\langle V_p^*\phi_\alpha, V_q^*\phi_\alpha\rangle.
\tag{52.9}
\]

Diese Interferenzterme (\(p\neq q\)) sind **der** Nichtüberzählungsmechanismus: Die kohärente Projektion auf globale Spektralmoden kann kleiner sein als die Summe der Einzel-Kanal-Projektionen.

**Kanalweise naive Bedingung** (aus NEU-51, jetzt ersetzt):

\[
\sum_p(\log p)^2\sum_{n,r,u}\frac{u^2r^2}{|\lambda_{p;n;r,u}-s|}<\infty
\quad\Longrightarrow\quad\text{nur gültig wenn }\eta\text{ Eigenbasis, also (52.D0) verboten.}
\tag{52.10}
\]

Status der korrekten Bedingung (52.8): ❓ [O] — Konvergenz ausständig.

---

## 4. Satz 52.4 — Falls nur S2 erreichbar: det_2 und D_Jac

Falls nur \(\mathcal{K}_N(s)\in\mathcal{S}_2\), arbeitet man mit:

\[
D_{\mathrm{scatt},N}(s) = \det_2(1-\mathcal{K}_N(s)).
\tag{52.11}
\]

Identität:

\[
\det_2(1-\mathcal{K}_N) = \det(1-\mathcal{K}_N)\cdot e^{\operatorname{Tr}\mathcal{K}_N}.
\tag{52.12}
\]

Daher wandert \(e^{\pm\operatorname{Tr}\mathcal{K}_N}\) nach \(D_{\mathrm{Jac},N}\), kompatibel mit NEU-47/48:

\[
D_{\mathrm{Jac}} \leftrightarrow e^{a+bs}.
\tag{52.13}
\]

Das ist kein Defekt, sondern die kanonische Aufteilung:

\[
\boxed{
D_{\mathrm{scatt}} = \det_2(1-\mathcal{K}_\infty)
\cdot (\text{exponentielle Korrekturen in }D_{\mathrm{Jac}}).
}
\tag{52.14}
\]

Status: ✓ [M] strukturell.

---

## 5. Nächste Frage: Globale Diagonalisierung von D_rel

Die richtige NEU-53-Frage ist nicht:

\[
\lambda_{p;n;r,u}\text{ aus }J_N^-?
\]

Sondern:

\[
\boxed{
\text{Welche globalen }\lambda_\alpha\text{ und Projektionskoeffizienten }\langle\phi_\alpha,\eta_{p;n;r,u}\rangle\text{ liefert }J_N^-?
}
\tag{52.15}
\]

Drei Teilfragen für NEU-53:

1. Ist \(\sigma(D_{\mathrm{rel}}) = \sigma(iJ_N^-)\) diskret, rein kontinuierlich, oder gemischt?
2. Welche Symmetrie hat \(\lambda_\alpha\) (reell wegen Selbstadjungiertheit von \(\mathcal{D}_{\mathrm{rel}} = iJ_N^-\))?
3. Sind die \(\langle\phi_\alpha,\eta_{p;n;r,u}\rangle\) explizit berechenbar aus \(\Theta_N\)?

---

## 6. Ablaufkette

\[
\eta\text{-Graphbasis}
\longrightarrow
D_{\mathrm{rel}}\text{-Spektralmaß }\{\lambda_\alpha,\phi_\alpha\}
\longrightarrow
K_{pq}\text{-Kernel (52.6)}
\longrightarrow
\mathcal{S}_1/\mathcal{S}_2\text{ via (52.8)}
\longrightarrow
\det\text{ oder }\det_2.
\tag{52.16}
\]

---

## 7. Statusmatrix

| Aussage | Status |
|---|---|
| η ist Graphbasis, nicht Eigenbasis (Satz 52.1) | ✓ [M] |
| Direkte-Eigenbasis-Annahme ausgeschlossen (52.D0) | ✗ [M] |
| Globale Spektralformel K_pq (Satz 52.2, Formel 52.6) | ✓ [M] strukturell |
| Off-Diagonal durch gemeinsame φ_α (52.7) | ✓ [M] generisch |
| Spurklasse S1 via (52.8) | ❓ [O] |
| S2 + det_2 + D_Jac-Korrektur (52.12–14) | ✓ [M] strukturell |
| Globale λ_α aus J_N^- | ❓ [O] → NEU-53 |

---

## 8. Nächster Schritt

\[
\boxed{
\text{NEU-53: Globale Diagonalisierung von }D_{\mathrm{rel}} = iJ_N^-:\;\text{Spektrum, Projektionskoeffizienten, S1-Konvergenz.}
}
\]
