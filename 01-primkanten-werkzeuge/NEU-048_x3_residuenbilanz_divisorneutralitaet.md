# NEU-48 — X.3.18: Residuenbilanz und Divisorneutralität

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-47  
**Ziel:** Residuentest der Faktorzerlegung
\(D_{\mathrm{Fesh}}^{\mathrm{rel}} = D_{\mathrm{Arch}} \cdot D_{\mathrm{prim}} \cdot D_{\mathrm{Jac}} \cdot D_{\mathrm{scatt}}\).
Zentrale These:

\[
\boxed{
\operatorname{div} D_{\mathrm{Spec}}^{\mathrm{rel}} = \operatorname{div} D_{\mathrm{scatt}},
\qquad
\operatorname{div} D_{\mathrm{Jac}} = 0.
}
\tag{48.0}
\]

---

## 0. Residuentabelle der vollständigen Zerlegung

**Satz 48.1 — Residuentabelle** \(\checkmark\) [M]

Aus \(\xi(s) = D_{\mathrm{Arch}}(s)\cdot\zeta(s)\) mit \(D_{\mathrm{Arch}} = \frac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\):

\[
\frac{\xi'}{\xi}(s)
=
\frac{\zeta'}{\zeta}(s)
+\frac{1}{s}+\frac{1}{s-1}
-\frac{1}{2}\log\pi
+\frac{1}{2}\psi(s/2).
\tag{48.1}
\]

Residuenbilanz:

| Stelle \(s_0\) | \(\mathrm{Res}_{s_0}\,\xi'/\xi\) | Quelle | Träger in Zerlegung |
|---|---|---|---|
| \(s=1\) | \(0\) (reguliert) | \(\mathrm{Res}_{1}\,\zeta'/\zeta = 1\), kompensiert durch \(1/(s-1)\) | \(D_{\mathrm{Arch}}\) |
| \(s=0\) | \(0\) (reguliert) | \(\mathrm{Res}_{0}\,\zeta'/\zeta = 0\), zusätzlich \(1/s\) absorbiert | \(D_{\mathrm{Arch}}\) |
| \(s=-2k\), \(k\ge1\) | \(0\) (kompensiert) | \(\mathrm{Res}_{-2k}\,\zeta'/\zeta = 1\), kompensiert durch \(\tfrac{1}{2}\psi(s/2)\) | **nur** \(D_{\mathrm{Arch}}\) |
| \(s=\rho\) (nichttrivial) | \(m_\rho\) | Nullstellen von \(\xi\) | \(D_{\mathrm{scatt},N}\) |
| alle anderen Punkte | \(0\) | keine künstlichen Divisoren | — |

Status: \(\checkmark\) [M]

---

## 1. Satz 48.2 — Trivialnullstellen-Neutralität von \(D_{\mathrm{Spec}}^{\mathrm{rel}}\)

Für jedes \(k \ge 1\):

\[
\boxed{
\lim_{N\to\infty}
\operatorname{Res}_{s=-2k}\,
\partial_s\log D_{\mathrm{Spec},N}^{\mathrm{rel}}(s)
= 0.
}
\tag{48.2}
\]

**Interpretation:** \(D_{\mathrm{Spec}}^{\mathrm{rel}}\) trägt keine Gamma-Schicht. Jede Gamma-Struktur in \(D_{\mathrm{Spec}}\) würde (48.2) verletzen oder eine nicht-kanonische Kompensation erfordern.

**Nachweisweg:** Analysiere \(D_{\mathrm{Jac},N}\) und \(D_{\mathrm{scatt},N}\) separat an \(s=-2k\):
- \(D_{\mathrm{Jac},N}\): Jacobi-Determinante der freien Operatoren \(D_{\mathrm{rel},p}^-\). Diese haben Spektrum auf \(\{\frac{1}{2}+it : t\in\mathbb{R}\}\) (RH-Annahme) oder allgemein auf \(\mathbb{C}\setminus\{-2k\}\). Kein natürlicher Pol bei \(s=-2k\).
- \(D_{\mathrm{scatt},N}\): \(1 - M_p(s)/(1-p^{-s})\). Pole von \(M_p(s)\) kommen aus Spektrum von \(D_{\mathrm{rel},p}^-\), nicht aus \(s=-2k\). Pole von \((1-p^{-s})^{-1}\) bei \(s = 2\pi i n/\log p\) (Primstellen), ebenfalls nicht bei \(s=-2k\).

Status: \(\warning\) [M] — strukturell plausibel, formaler Nachweis ausständig.

---

## 2. Satz 48.3 — Divisorträger von \(D_{\mathrm{scatt},N}\) (Hadamard-Test)

Für jede nichttriviale Nullstelle \(\rho\) von \(\xi\) mit Multiplizität \(m_\rho\):

\[
\boxed{
\lim_{N\to\infty}
\operatorname{Res}_{s=\rho}\,
\partial_s\log D_{\mathrm{scatt},N}(s)
= m_\rho.
}
\tag{48.3}
\]

Äquivalent in schwächerer, beweisrelevanterer Form:

\[
\boxed{
\partial_s\log D_{\mathrm{scatt},N}(s)
\longrightarrow
\sum_\rho m_\rho\left(\frac{1}{s-\rho}+\frac{1}{\rho}\right)
}
\tag{48.4}
\]

im konturweise-meromorphen Sinn. Der exponentielle Hadamard-Freiheitsgrad \(e^{a+bs}\) bleibt in \(D_{\mathrm{Jac}}\) und erscheint nicht in (48.4).

**Wichtiger Hinweis:** Nicht behaupten:

\[
D_{\mathrm{scatt},N} \to \prod_\rho E_1(s/\rho)\quad\text{(zu stark).}
\tag{48.5}
\]

Die korrekte Aussage ist (48.4) über logarithmische Ableitungen. Die logarithmische Ableitung sieht genau den Divisor — der exponentielle Anteil ist unsichtbar und sitzt in \(D_{\mathrm{Jac}}\).

Status: Hauptziel von NEU-48. \(\:?\:\) [O]

---

## 3. Satz 48.4 — Divisorneutralität von \(D_{\mathrm{Jac},N}\)

Für jede zulässige Kontur \(\gamma\):

\[
\boxed{
\lim_{N\to\infty}
\frac{1}{2\pi i}
\int_\gamma
\partial_s\log D_{\mathrm{Jac},N}(s)\,ds
= 0.
}
\tag{48.6}
\]

Äquivalent:

\[
\boxed{
D_{\mathrm{Jac},N} \rightsquigarrow e^{a_N + b_N s}
}
\tag{48.7}
\]

bis auf zulässige reguläre Faktoren.

**Nachweisweg:** \(D_{\mathrm{Jac},N}(s) = \prod_{p\le N}\det(s-D_{\mathrm{rel},p}^-)\).
- Nullstellen von \(D_{\mathrm{Jac},N}\) sind Eigenwerte von \(D_{\mathrm{rel},p}^-\).
- Nach Konstruktion ist \(D_{\mathrm{rel},p}^-\) der relative Jacobi-Operator im \(p\)-Kanal, mit Spektrum auf \(\frac{1}{2}+i\mathbb{R}\) (RH) oder zumindest im kritischen Streifen.
- Kontur \(\gamma\) gehört zum Bereich, in dem keine Jacobi-Eigenwerte liegen.
- Dann ist \(D_{\mathrm{Jac},N}\) holomorph auf \(\gamma\) und (48.6) gilt trivialerweise.

**Zirkularitätswarnung:** Wenn RH benutzt wird, um zu argumentieren, dass \(D_{\mathrm{Jac}}\) divisorneutral in einem bestimmten Bereich ist, muss das von der Hauptaussage (48.3) entkoppelt werden. Sonst entsteht Zirkulärität.

Status: \(\warning\) [M] — strukturell klar, Zirkularitätsfrage offen.

---

## 4. Satz 48.5 — Zulässiger Konvergenztyp

Nicht:

\[
D_{\mathrm{Spec},N}^{\mathrm{rel}} \to 1\quad\text{lokal gleichm. holomorph (verboten!).}
\tag{48.8}
\]

Sondern:

\[
\boxed{
\partial_s\log D_{\mathrm{Spec},N}^{\mathrm{rel}}
\to
\partial_s\log D_{\mathrm{Had}}^{\mathrm{rel}}
}
\tag{48.9}
\]

als meromorphe 1-Form, in einem der folgenden Sinne:

| Konvergenztyp | Beschreibung | Status |
|---|---|---|
| **Distributionell** | Konvergenz gegen meromorphe Distribution | \(\:?\:\) [O] |
| **Konturweise** | Konvergenz der Konturintegrale | \(\:?\:\) [O] |
| **Trace-formelartig** | Konvergenz als Spurformel-Grenzwert | \(\:?\:\) [O] |
| **Meromorph-relativ** | Quotient \(D_{\mathrm{Spec},N}^{\mathrm{rel}}/D_{\mathrm{Had}}^{\mathrm{rel}}\) konvergiert holomorph gegen \(e^{h_N}\), \(h_N\to 0\) | \(\:?\:\) [O] |

Status: \(\warning\) [M] als Rahmenbedingung; genaue Konvergenzmode: \(\:?\:\) [O]

---

## 5. Birman-Schwinger-Konturindex (Kern von NEU-48)

Die entscheidende Frage lässt sich als Spektralindex-Problem formulieren.

Für den Birman-Schwinger-Operator \(\mathcal{K}_p(s) := M_p(s)/(1-p^{-s})\), schreibe:

\[
D_{\mathrm{scatt},N}(s) = \prod_{p\le N} \det(1 - \mathcal{K}_p(s)).
\tag{48.10}
\]

Ein Pol von \(\partial_s\log D_{\mathrm{scatt},N}\) bei \(s_0\) entsteht genau dann, wenn

\[
\ker(1-\mathcal{K}_p(s_0)) \ne 0
\]

für mindestens ein \(p\). Dann ist

\[
\operatorname{Res}_{s=s_0}\partial_s\log D_{\mathrm{scatt},N}(s)
= \sum_{p\le N} \operatorname{Ind}_{s_0}(1-\mathcal{K}_p)
\tag{48.11}
\]

(algebraischer Nullstellenzähler, im geeigneten Spurklasse-Sinn).

**Kern-These von NEU-48:**

\[
\boxed{
\sum_{p\le N} \operatorname{Ind}_{s=\rho}(1-\mathcal{K}_p)
\longrightarrow m_\rho
\quad\text{für } N\to\infty.
}
\tag{48.12}
\]

Das heißt: Die Feshbach-Eigenwertbedingung

\[
1 - \mathcal{K}_p(\rho) = 0
\]

muss bei den nichttrivialen Nullstellen \(\rho\) von \(\xi\) mit Multiplizität \(m_\rho\) erfüllt sein.

Status: Kern-Engpass. \(\:?\:\) [O]

---

## 6. Verbindung Birman-Schwinger \(\leftrightarrow\) Jacobi-Spektrum

Die Feshbach-Eigenwertbedingung

\[
\det(1-\mathcal{K}_p(s)) = 0
\]

ist äquivalent zur Existenz eines Vektors \(v \in \mathcal H_{\mathrm{rel},p}\) mit

\[
(C_p^{\mathrm{rel}})^\# (s - D_{\mathrm{rel},p}^-)^{-1} C_p^{\mathrm{rel}} v = (1-p^{-s}) v.
\tag{48.13}
\]

Das ist genau die reduzierte Eigenwertgleichung des gekoppelten Feshbach-Operators \(\mathbb{F}_p\) im Primsektor \(\varepsilon_p\).

Also:

\[
\boxed{
\text{Eigenwerte von } \mathbb{F}_p\text{ im Primsektor}
\quad\longleftrightarrow\quad
\text{Nullstellen von }D_{\mathrm{scatt},p}.
}
\tag{48.14}
\]

Status: \(\checkmark\) [M] formal; Zusammenhang mit \(\xi\)-Nullstellen: \(\:?\:\) [O]

---

## 7. Statusmatrix

| Aussage | Status |
|---|---|
| Residuentabelle vollständig (Satz 48.1) | \(\checkmark\) [M] |
| \(D_{\mathrm{Spec}}^{\mathrm{rel}}\) neutral bei \(s=-2k\) (Satz 48.2) | \(\warning\) [M]; Nachweis \(\:?\:\) [O] |
| \(D_{\mathrm{scatt}}\) trägt Divisor bei \(\rho\) (Satz 48.3) | \(\:?\:\) [O] Kern-Engpass |
| \(D_{\mathrm{Jac}}\) divisorneutral (Satz 48.4) | \(\warning\) [M]; Zirkularität offen |
| Konvergenztyp \(D_{\mathrm{Spec}}^{\mathrm{rel}}\) meromorph-konturweise (Satz 48.5) | \(\:?\:\) [O] |
| Birman-Schwinger-Konturindex (48.12) | \(\:?\:\) [O] Haupt-Engpass |
| Feshbach-Eigenwertbedingung (48.14) | \(\checkmark\) [M] formal |

---

## 8. Kompakter Kernsatz (Designentscheidungen gesichert)

\[
\boxed{D_{\mathrm{Arch}} \text{ kompensiert } 0,1,-2,-4,\ldots}\tag{48.D1}
\]

\[
\boxed{D_{\mathrm{Jac}} \text{ ist divisorneutral.}}\tag{48.D2}
\]

\[
\boxed{D_{\mathrm{scatt}} \text{ trägt genau die nichttrivialen Nullstellen.}}\tag{48.D3}
\]

\[
\boxed{\text{Korrekte Konvergenz: meromorph-konturweise, nicht holomorph-normal.}}\tag{48.D4}
\]

---

## 9. Nächster Schritt

\[
\boxed{
\text{NEU-49: Nachweis des Birman-Schwinger-Konturindex (48.12).}
}
\]

\[
\boxed{
\text{Zeige: }\sum_{p\le N}\operatorname{Ind}_{s=\rho}(1-\mathcal{K}_p) \longrightarrow m_\rho.
}
\]

Drei mögliche Zugänge:
1. **Funktionalanalytisch:** Spurklasse-Argument für \(\mathcal{K}_p\), Konvergenz des Fredholm-Index.
2. **Spektraltheoretisch:** Jacobi-Spektrum von \(D_{\mathrm{rel},p}^-\) direkt mit \(\xi\)-Nullstellen verbinden.
3. **Trace-formelartig:** Hadamard-Konvergenz der Streudeterminante via Regularisierung.
