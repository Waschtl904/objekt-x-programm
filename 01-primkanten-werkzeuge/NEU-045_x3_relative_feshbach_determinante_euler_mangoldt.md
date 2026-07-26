# NEU-45 — X.3.15: Relative Feshbach-Determinante und Euler-Mangoldt-Spur im Graphraum

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-39–44  
**Ziel:** Auswertung von \(\det_{Wres,rel}\mathbb F_N^{rel}(z,\beta)\) und Entscheidung, ob \(\prod_{p\le N}(1-p^{-s})\) direkt aus den \(p\)-Kanälen hervorgeht.

---

## 0. Kernantwort

\[
\boxed{\text{Ja, aber nur als Euler-Unterdeterminante / verbundener Primquotient.}}
\]

Die volle gekoppelte Feshbach-Determinante enthält zusätzlich Jacobi-Weyl-Korrekturen.

---

## 1. Zerlegung nach Primlabels

Durch Kantendiagonalität (NEU-44):
\[
\mathcal H_{rel,N}=\bigoplus_{p\le N}\mathcal H_{rel,p,N},\qquad
\mathcal P_N(\beta)=\bigoplus_{p\le N}p^{-\beta}\operatorname{id}_{\mathbb C\varepsilon_p}.
\]
Status: ✓ [M]

---

## 2. Primblock

\[
\boxed{
\mathbb F_p^{rel}(z,\beta)=
\begin{pmatrix}z-D_{rel,p}^- & -C_p^{rel}\\ -(C_p^{rel})^\# & 1-p^{-\beta}\end{pmatrix}
}\tag{45.2}
\]

auf \(\mathcal H_{rel,p,N}\oplus\mathbb C\varepsilon_p\). ✓ [M]

---

## 3. Zwei Schur-Determinanten

### Eliminierung des Primblocks (Satz 45.1a)

\[
\det\mathbb F_p^{rel}(z,\beta)=(1-p^{-\beta})\det S_p^{rel}(z,\beta),\tag{45.4}
\]
\[
S_p^{rel}(z,\beta)=z-D_{rel,p}^--\frac{C_p^{rel}(C_p^{rel})^\#}{1-p^{-\beta}}.
\]

### Eliminierung des Jacobi-Blocks (Satz 45.1b)

\[
\det\mathbb F_p^{rel}(z,\beta)=\det(z-D_{rel,p}^-)\cdot(1-p^{-\beta}-M_p(z)),\tag{45.5}
\]

\[
\boxed{M_p(z):=(C_p^{rel})^\#(z-D_{rel,p}^-)^{-1}C_p^{rel}.}\tag{45.6}
\]

Status: ✓ [M]

---

## 4. Produktformel

\[
\boxed{
\det\mathbb F_N^{rel}(z,\beta)=\prod_{p\le N}\det(z-D_{rel,p}^-)\cdot\prod_{p\le N}(1-p^{-\beta}-M_p(z)).
}\tag{45.8}
\]

Status: ✓ [M] endlich, relativ, kantendiagonal.

---

## 5. Drei Determinanten

### 5.1 Primdeterminante (Satz 45.1)

\[
\boxed{D_{prim,N}(\beta):=\det_{conn}(1-\mathcal P_N(\beta))=\prod_{p\le N}(1-p^{-\beta})=\zeta_N(\beta)^{-1}.}\tag{45.11}
\]

\[
\boxed{-\partial_\beta\log D_{prim,N}(\beta)=\frac{\zeta_N'}{\zeta_N}(\beta).}\tag{45.12}
\]

### 5.2 Volle Feshbach-Determinante (Satz 45.2)

\[
\boxed{D_{Fesh,N}:=\det_{Wres,rel}\mathbb F_N^{rel}(z,\beta)\ne D_{prim,N}\text{ bei }C_p^{rel}\ne0.}
\]

Status: ✓ [M]

---

## 6. Wo das Eulerprodukt sitzt

Für \(C_p^{rel}=0\) (Kopplung aus):
\[
\det\mathbb F_N^{rel}(z,\beta)=\prod_{p\le N}\det(z-D_{rel,p}^-)\cdot\prod_{p\le N}(1-p^{-\beta}).\tag{45.9}
\]

Das Eulerprodukt erscheint als Primblock-Unterdeterminante. Bei Kopplung \(C_p^{rel}\ne0\):
\[
1-p^{-\beta}\quad\leadsto\quad 1-p^{-\beta}-M_p(z).
\]
Status: ✓ [M]

---

## 7. Feshbach-Ableitung und Fehleridentität

\[
-\partial_\beta\log D_{Fesh,N}(z,\beta)=-\sum_{p\le N}\frac{\log(p)p^{-\beta}}{1-p^{-\beta}-M_p(z)}.\tag{45.17}
\]

Fehleridentität:

\[
\boxed{
E_{Fesh,N}(s)=\sum_p\partial_s\log\det(s-D_{rel,p}^-)+\sum_p\frac{\log(p)p^{-s}-M_p'(s)}{1-p^{-s}-M_p(s)}-\frac{\zeta_N'}{\zeta_N}(s).
}\tag{45.25}
\]

\[
\boxed{\text{Mangoldt folgt aus der vollen Feshbach-Ableitung nur wenn }M_p(z)=0\text{ oder kontrolliert renormiert.}}
\]

Status: ✓ [M]

---

## 8. Renormierter Primquotient (Satz 45.3)

\[
\boxed{Q_{Fesh,N}(z,\beta):=\frac{D_{Fesh,N}(z,\beta)}{\prod_p\det(z-D_{rel,p}^-)\cdot\prod_p(1-\frac{M_p(z)}{1-p^{-\beta}})}=\prod_p(1-p^{-\beta}).}\tag{45.20}
\]

\[
\boxed{\text{Die Eulerprodukt-Schicht ist als renormierter Primquotient exakt.}}
\]

Status: ✓ [M] algebraisch, ❓ [O] geometrische Legitimität.

---

## 9. Statusmatrix

| Aussage | Status |
|---|---:|
| Graphraum zerfällt nach Primlabels \(p\) | ✓ [M] |
| Primblock \(\mathbb F_p^{rel}\) und Schur-Determinante | ✓ [M] |
| Eulerprodukt \(\det_{conn}(1-\mathcal P_N)=\zeta_N^{-1}\) | ✓ [M] |
| Mangoldt aus \(-\partial_\beta\log\det_{conn}(1-\mathcal P_N)\) | ✓ [M] |
| Produktformel \(\det\mathbb F_N^{rel}=\prod_p\det(s-D_p^-)\cdot(1-p^{-\beta}-M_p)\) | ✓ [M] |
| Volle Feshbach-Determinante gleich Eulerprodukt | ✗ [M] |
| Weyl-Korrektur \(M_p(z)\) | ✓ [M] |
| Fehleridentität \(E_{Fesh,N}(s)\) | ✓ [M] |
| geometrisch legitime Renormierung | ❓ [O] |
| Grenzkontrole \(N\to\infty\) | ❓ [O] / OP-4.1a ⚠ |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |

---

## 10. Neuer offener Kern

\[
\boxed{\text{NEU-46: Verbundene/renormierte relative Determinante und Kontrolle der Weyl-Korrekturen }M_p.}
\]

Entscheidungsfrage: Verschwinden \(M_p(z)\) im relevanten Grenz, bleiben sie kontrolliert, oder sind sie eigentliche Spektraldaten von \(D_X^{geom}\)?
