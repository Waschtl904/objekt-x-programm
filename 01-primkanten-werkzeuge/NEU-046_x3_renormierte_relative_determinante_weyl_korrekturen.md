# NEU-46 — X.3.16: Verbundene/renormierte relative Determinante und Kontrolle der Weyl-Korrekturen \(M_p\)

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-39–45  
**Ziel:** Entscheide, ob die Weyl-Korrekturen \(M_p(z)=(C_p^{rel})^\#(z-D_{rel,p}^-)^{-1}C_p^{rel}\) im relevanten Grenzübergang verschwinden, oder ob sie als Spektraldaten von \(D_X^{geom}\) erhalten werden müssen.

---

## 0. Ausgangspunkt (NEU-45)

\[
D_{Fesh,N}(z,\beta)
=
\prod_{p\le N}
\det(z-D_{rel,p}^-)
\left(1-p^{-\beta}-M_p(z)\right).
\tag{46.1}
\]

Primdeterminante: \(D_{prim,N}(\beta)=\prod_p(1-p^{-\beta})=\zeta_N(\beta)^{-1}\) erzeugt \(-\partial_\beta\log D_{prim,N}=\zeta_N'/\zeta_N\).

**Entscheidungsfrage:** \(M_p(z)\stackrel{?}{\to}0\) oder Spektraldatum?

**Antwort (NEU-46):** \(M_p\) verschwindet nicht automatisch in einem nichttrivial gekoppelten Kanal.

---

## 1. \(M_p\) als zyklische Weyl-Funktion

Mit \(\Psi_p:=C_p^{rel}\varepsilon_p\):

\[
M_p(z)=\langle\Psi_p,(z-D_{rel,p}^-)^{-1}\Psi_p\rangle_{Wres,rel}
=\int\frac{d\mu_p(\lambda)}{z-\lambda}.\tag{46.5–6}
\]

Status: \(\checkmark\) [M]

---

## 2. Nichtverschwindungs-Satz

Resolvententwicklung für großes \(z\):

\[
M_p(z)=\frac{\langle\Psi_p,\Psi_p\rangle}{z}+\frac{\langle\Psi_p,D_{rel,p}^-\Psi_p\rangle}{z^2}+\cdots.
\tag{46.7}
\]

**Satz 46.1:**

\[
M_p\equiv0\Longleftrightarrow C_p^{rel}=0 \text{ (keine Feshbach-Kopplung).}\tag{46.8}
\]

Status: \(\checkmark\) [M] (positiv), \(\warning\) [M] (indefinit/Krein).

---

## 3. Spektralkollaps erzeugt Pol

**Satz 46.2:** Wenn \(D_{rel,p}^-\rightsquigarrow\log p\) im zyklischen Sinn:

\[
\mu_p\Rightarrow\|\Psi_p\|^2\delta_{\log p}\implies M_p(z)\to\frac{\|\Psi_p\|^2}{z-\log p}.\tag{46.9–10}
\]

Falsche Hoffnung: \(D_{rel,p}^-\to\log p\not\Rightarrow M_p\to0\).

Status: \(\checkmark\) [M]

---

## 4. Drei Regime

| Regime | Bedingung | Konsequenz | Status |
|---|---|---|---|
| **A** Entkopplung | \(C_p^{rel}=0\) | \(D_{Fesh}=D_{Jac}\cdot D_{prim}\); korrekte Mangoldt, aber geometrisch unzureichend | \(\checkmark\) [M] |
| **B** Schwache Kopplung | \(C_p^{rel}\mapsto g_N C_p^{rel}\), \(g_N\to0\) | \(M_p\to0\), aber Kopplung abgeschaltet | \(\checkmark\) [M], programmatisch verdächtig |
| **C** Renormierte Kopplung | \(M_p\) behalten, Faktorisierung | **korrekte Architektur** | \(\checkmark\) [M] |

---

## 5. Hauptresultat: Kanonische Drei-Faktoren-Zerlegung

**Satz 46.3:**

\[
\boxed{
D_{Fesh,N}^{rel}=D_{Euler,N}^{conn}\cdot D_{Spec,N}^{rel}
}\tag{46.23}
\]

wobei

\[
D_{Euler,N}^{conn}(s):=D_{prim,N}(s)=\det_{conn}(1-\mathcal P_N(s)),\tag{46.21}
\]

\[
D_{Spec,N}^{rel}(s):=D_{Jac,N}(s)\cdot D_{scatt,N}(s,s),\tag{46.22}
\]

\[
D_{Jac,N}(z):=\prod_{p\le N}\det(z-D_{rel,p}^-),\quad
D_{scatt,N}(z,\beta):=\prod_{p\le N}\left(1-\frac{M_p(z)}{1-p^{-\beta}}\right).\tag{46.13–14}
\]

Logarithmisch:

\[
\partial_s\log D_{Fesh,N}^{rel}(s,s)
=
-\frac{\zeta_N'}{\zeta_N}(s)+\partial_s\log D_{Spec,N}^{rel}(s).\tag{46.24}
\]

Status: \(\checkmark\) [M]

---

## 6. \(D_{scatt}\) als Birman-Schwinger-Determinante

\(D_{scatt,N}\) hat exakt die Struktur einer Streu-/Birman-Schwinger-Determinante:

- \(M_p(z)=(C_p)^\#(z-D_p)^{-1}C_p\) ist die Weyl-Funktion des angekoppelten Kanals.
- \(1-M_p(z)/(1-p^{-\beta})\) ist die Feshbach-Eigenwertbedingung im \(p\)-Kanal.
- \(D_{scatt,N}\) trägt die neu erzeugten Spektraldaten der Kopplung.

Status: \(\checkmark\) [M] als Spektralinterpretation; \(\:?\:) [O] als Nullstellenidentifikation.

---

## 7. Revidiertes Ziel für X.3

Faktorisierte Zielbehauptung (korrekt):

\[
\boxed{
\frac{\zeta_N'}{\zeta_N}(s)
+\partial_s\log D_{Arch,N}(s)
+\partial_s\log D_{Spec,N}^{rel}(s)
\longrightarrow\frac{\xi'}{\xi}(s).
}\tag{46.26}
\]

Idealer Fall (falls \(D_{Arch,N}\) alle Gamma-Terme trägt):

\[
\partial_s\log D_{Spec,N}^{rel}(s)\to0.\tag{46.27}
\]

Alternativ (gemischter Fall):

\[
\partial_s\log D_{Arch,N}+\partial_s\log D_{Spec,N}^{rel}\to\text{Gamma-/Polterme}.\tag{46.28}
\]

Status: \(\:?\:) [O]

---

## 8. Kontrolle \(D_{scatt}\)

Hinreichende Bedingung für Verschwinden:

\[
\sum_{p\le N}\left|\partial_s\left(\frac{M_p(s)}{1-p^{-s}}\right)\right|\to0.\tag{46.30}
\]

In nichttrivialer Kopplung unwahrscheinlich; realistischer: Konvergenz gegen expliziten Korrekturterm

\[
\partial_s\log D_{scatt,N}(s,s)\to G_{scatt}(s).\tag{46.31}
\]

Status: \(\:?\:) [O]

---

## 9. Konsequenz für RH-Operatorbild

Geometrische Spektraldaten (Kandidaten für Nullstellen von \(\xi\)):

\[
\boxed{D_{Spec,N}^{rel}\cdot D_{Arch,N}\longrightarrow\text{Hadamard-Nullstellendeterminante von }\xi.}\tag{46.32}
\]

Variante 3 (starkste): \(D_{Spec,N}^{rel}\Rightarrow\prod_\rho(1-s/\rho)e^{s/\rho}\) nach Hadamard-Regularisierung. Status: \(\:?\:) [O]

---

## 10. Statusmatrix

| Aussage | Status |
|---|---|
| \(M_p\) ist Weyl-Funktion des Kopplungsvektors | \(\checkmark\) [M] |
| \(M_p\equiv0\) impliziert Entkopplung (positiv) | \(\checkmark\) [M] |
| Spektralkollaps \(D_{rel,p}^-\to\log p\) lässt \(M_p\) nicht verschwinden | \(\checkmark\) [M] |
| Volle Feshbach-Det. faktorisiert in Euler- und Spektralanteil | \(\checkmark\) [M] |
| \(D_{scatt}\) ist Birman-Schwinger-Determinante | \(\checkmark\) [M] |
| automatische Vernachlässigbarkeit von \(M_p\) | \(\times\) [M] |
| geometrisch legitime Renormierung | \(\:?\:) [O] |
| Grenzwert \(\partial_s\log D_{Spec,N}^{rel}\) | \(\:?\:) [O] |
| Identifikation mit Gamma-/Nullstellenanteil | \(\:?\:) [O] |
| OP-4.1a globale Stetigkeit | \(\warning\) [M] |

---

## 11. Nächster Schritt

\[
\boxed{\text{NEU-47: Grenzwert von }D_{Spec,N}^{rel}(s)\text{ und Vergleich mit Gamma-/Hadamard-Faktoren.}}
\]
