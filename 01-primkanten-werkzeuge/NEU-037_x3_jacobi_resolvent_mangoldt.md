# NEU-37 — X.3.7: Jacobi-Resolvent und effektives Mangoldt-Gewicht

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-34–36  
**Ziel:** Berechnung des Resolventen von

\[
A_N^- = H_N+\beta_N J_N^-
\]

auf den endlichen Fourier-Orbits

\[
\mathcal H_{n,a}^{(M)}
\]

und Diagnose, ob daraus ein effektives Mangoldt-Gewicht entsteht.

---

## 0. Ergebnisübersicht

NEU-37 liefert drei Resultate.

1. **Exakte Jacobi-Resolventformel.**  
   Auf jedem Orbit \(\mathcal H_{n,a}^{(M)}\) ist

   \[
   (w-A_N^-)^{-1}
   \]

   durch eine Kontinuanten-/Kettenbruchformel vollständig berechenbar.

2. **Exakte lokale Determinante.**  
   Für jeden Orbit gilt

   \[
   \det(w-A_{n,a}^{(M),-})
   =
   P_{M+1}^{(n,a)}(w-h(n)),
   \]

   wobei \(P_k^{(n,a)}\) die Jacobi-Kontinuanten erfüllen:

   \[
   P_0=1,\qquad
   P_1=z,\qquad
   P_{k+1}=zP_k+b_{k-1}^2P_{k-1}.
   \]

3. **Wichtige Diagnose.**  
   Der Jacobi-Resolvent erzeugt von selbst nicht automatisch ein Mangoldt-Gewicht.  
   Das benötigte arithmetische Gewicht ist äquivalent zu einer nichttrivialen Momentenidentität der \(Wres\)-Jacobi-Maße.

Der offene Kern ist daher:

\[
\boxed{
\text{Zeige eine BC-intrinsische Momentenidentität }
\mu_{N,k}^{Wres}\rightsquigarrow \Lambda_N.
}
\]

Status der exakten Resolventrechnung: ✓ [M]  
Status der Mangoldt-Identifikation: ❓ [O]

---

## 1. Orbitzerlegung

Fixiere \(n\in\langle p\le N\rangle\) und eine Restklasse \(a\) modulo \(n\).  
Die Fourier-Verschiebung aus \(\widetilde\omega_2\) hat die Form

\[
r\longmapsto r+n.
\]

Daher ist der natürliche endliche Orbit:

\[
\mathcal H_{n,a}^{(M)}
:=
\operatorname{span}
\{E_0,\dots,E_M\},
\qquad
E_j:=E_{a+jn,n}=e_{a+jn}V_n.
\]

Auf diesem Orbit wirkt der rohe Shift \(\Theta_N\) durch

\[
\Theta_NE_j
=
\alpha_j E_{j+1},
\qquad
\alpha_j
=
\gamma_N(a+jn)\log n,
\qquad
0\le j<M,
\]

und

\[
\Theta_NE_M=0.
\]

Die \(Wres\)-Adjungierte erfüllt auf dem endlichen Orbit:

\[
\Theta_N^\dagger E_j
=
\alpha_{j-1}E_{j-1},
\qquad
\alpha_{-1}=0.
\]

Damit ist die schiefadjungierte Kopplung aus NEU-35:

\[
\boxed{
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger).
}
\tag{37.1}
\]

Also

\[
J_N^-E_j
=
\frac{\alpha_j}{2}E_{j+1}
-
\frac{\alpha_{j-1}}{2}E_{j-1}.
\tag{37.2}
\]

Setze

\[
b_j:=\frac{\beta_N\alpha_j}{2}
=
\frac{\beta_N\gamma_N}{2}(a+jn)\log n.
\tag{37.3}
\]

Dann gilt:

\[
A_N^-E_j
=
h(n)E_j+b_jE_{j+1}-b_{j-1}E_{j-1}.
\tag{37.4}
\]

Hier ist \(h(n)\) der diagonale logarithmische/modulare Eigenwert von \(H_N\) auf dem \(V_n\)-Sektor.

Status: ✓ [M]

---

## 2. Reduktion auf eine tridiagonale Matrix

Für

\[
D_N^-=\frac12I+iA_N^-
\]

verwenden wir die Variable

\[
w:=-i\left(s-\frac12\right).
\tag{37.5}
\]

Dann gilt:

\[
s-D_N^-
=
i(w-A_N^-),
\]

also

\[
(s-D_N^-)^{-1}
=
-i(w-A_N^-)^{-1}.
\tag{37.6}
\]

Auf \(\mathcal H_{n,a}^{(M)}\) setze

\[
z:=w-h(n).
\]

Dann ist

\[
w-A_{n,a}^{(M),-}
=
\begin{pmatrix}
z & -b_0 & 0 & \cdots & 0\\
b_0 & z & -b_1 & \cdots & 0\\
0 & b_1 & z & \ddots & 0\\
\vdots & \vdots & \ddots & \ddots & -b_{M-1}\\
0 & 0 & 0 & b_{M-1} & z
\end{pmatrix}.
\tag{37.7}
\]

Dies ist ein schief-Jacobi-Operator mit konstantem Diagonalteil.

Status: ✓ [M]

---

## 3. Kontinuanten und lokale Determinante

Definiere die linken Kontinuanten

\[
P_0(z)=1,\qquad
P_1(z)=z,
\]

und für \(k\ge1\):

\[
\boxed{
P_{k+1}(z)=zP_k(z)+b_{k-1}^2P_{k-1}(z).
}
\tag{37.8}
\]

Dann gilt für den Orbitdeterminanten:

\[
\boxed{
\det(w-A_{n,a}^{(M),-})=P_{M+1}^{(n,a)}(z).
}
\tag{37.9}
\]

Beispiele:

\[
P_1=z,
\]

\[
P_2=z^2+b_0^2,
\]

\[
P_3=z(z^2+b_0^2)+b_1^2z
=
z^3+(b_0^2+b_1^2)z,
\]

\[
P_4
=
z^4+(b_0^2+b_1^2+b_2^2)z^2+b_0^2b_2^2.
\]

Damit liegen die lokalen Eigenwerte von \(A_{n,a}^{(M),-}\) bei

\[
w=h(n)+\lambda,
\]

wobei \(\lambda\) Nullstelle von \(P_{M+1}^{(n,a)}\) ist.

Da die Matrix \(J_N^-\) real schiefsymmetrisch ist, sind diese \(\lambda\) rein imaginär im Hilbert-Normfall. Im \(Wres\)-indefiniten Fall ist dies nicht automatisch eine Aussage über echte geometrische Positivität; die Positivitätsfrage bleibt Teil von X.3.

Status: ✓ [M]

---

## 4. Diagonaler Resolvent

Für die \(Wres\)-Spur wird zunächst der diagonale Resolvent benötigt.

Sei

\[
G_j^{(n,a,M)}(z)
:=
\left((w-A_{n,a}^{(M),-})^{-1}\right)_{jj}.
\]

Dann gilt die Standardformel:

\[
\boxed{
G_j^{(n,a,M)}(z)
=
\frac{
P_j^{L}(z)\,P_{M-j}^{R}(z)
}{
P_{M+1}(z)
}.
}
\tag{37.10}
\]

Dabei ist

\[
P_j^{L}(z)
=
\det
\begin{pmatrix}
z & -b_0 & & \\
b_0 & z & \ddots & \\
& \ddots & \ddots & -b_{j-2}\\
& & b_{j-2} & z
\end{pmatrix}
\]

der linke Blockdeterminant der Länge \(j\), mit \(P_0^L=1\), und \(P_{M-j}^{R}\) der entsprechende rechte Blockdeterminant auf den Indizes \(j+1,\dots,M\).

Insbesondere:

\[
G_0(z)=\frac{P_M^{R}(z)}{P_{M+1}(z)},
\]

\[
G_M(z)=\frac{P_M^{L}(z)}{P_{M+1}(z)}.
\]

Äquivalent erhält man die Kettenbruchformel:

\[
G_0(z)
=
\cfrac{1}{
z+\cfrac{b_0^2}{
z+\cfrac{b_1^2}{
z+\cdots+\cfrac{b_{M-1}^2}{z}
}
}
}.
\tag{37.11}
\]

Status: ✓ [M]

---

## 5. Orbitbeitrag zur \(Wres\)-Resolventspur

Schreibe den diagonal durch \(Wres\) sichtbaren Anteil von \(L_3^\circ\) auf dem Orbit als

\[
L_3^\circ E_j=\ell_j^{(n,a)}E_j
\]

im Sinne:

\[
\operatorname{Tr}_{Wres,N}^{top}(T L_3^\circ)
=
\sum_{n,a,j}\ell_j^{(n,a)}\,T_{jj}
\]

für die in der \(Wres\)-Spur überlebenden diagonalen Komponenten.

Dann ist der Orbitbeitrag zu NEU-36:

\[
\boxed{
H_{N,n,a,M}^{-}(s)
=
-i
\sum_{j=0}^{M}
\ell_j^{(n,a)}
G_j^{(n,a,M)}
\left(
-i(s-\frac12)-h(n)
\right).
}
\tag{37.12}
\]

Damit:

\[
\boxed{
H_N^-(s)
=
-i
\sum_{n,a,M}
\sum_{j=0}^{M}
\ell_j^{(n,a)}
\frac{
P_j^{L}(z_{n}(s))\,P_{M-j}^{R}(z_n(s))
}{
P_{M+1}^{(n,a)}(z_n(s))
},
}
\tag{37.13}
\]

wobei

\[
z_n(s):=-i(s-\frac12)-h(n).
\tag{37.14}
\]

Dies ist die exakte Jacobi-Resolventformel.

Status: ✓ [M]

---

## 6. Spezialfall: \(L_3^\circ\) proportional zur Identität auf dem Orbit

Falls

\[
\ell_j^{(n,a)}=\ell^{(n,a)}
\]

konstant ist, vereinfacht sich die Spur:

\[
\sum_{j=0}^{M}G_j(z)
=
\partial_z\log P_{M+1}(z).
\]

Dann:

\[
H_{N,n,a,M}^{-}(s)
=
-i\,\ell^{(n,a)}
\partial_z
\log P_{M+1}^{(n,a)}(z_n(s)).
\]

Da

\[
\partial_s z_n(s)=-i,
\]

folgt:

\[
\boxed{
H_{N,n,a,M}^{-}(s)
=
\ell^{(n,a)}
\partial_s
\log P_{M+1}^{(n,a)}(z_n(s)).
}
\tag{37.15}
\]

Also ist der Orbitbeitrag tatsächlich eine logarithmische Ableitung eines endlichen lokalen Determinanten.

Status: ✓ [M]

---

## 7. Allgemeiner Fall: gewichtete Jacobi-Spektralmaße

Im allgemeinen Fall definiert \(L_3^\circ\) ein gewichtetes Spektralmaß.

Seien \(\lambda_{\nu}^{(n,a,M)}\) die Nullstellen von \(P_{M+1}^{(n,a)}\), also die Eigenwerte des \(J_N^-\)-Anteils relativ zu \(z\). Dann kann man schreiben:

\[
\sum_{j=0}^{M}\ell_j^{(n,a)}G_j(z)
=
\int_{\mathbb C}
\frac{d\mu_{n,a,M}^{Wres}(\lambda)}{z-\lambda}.
\tag{37.16}
\]

Damit:

\[
\boxed{
H_{N,n,a,M}^{-}(s)
=
-i
\int_{\mathbb C}
\frac{d\mu_{n,a,M}^{Wres}(\lambda)}
{-i(s-\frac12)-h(n)-\lambda}.
}
\tag{37.17}
\]

Das ist eine Stieltjes-/Cauchy-Transformierte eines endlichen \(Wres\)-Jacobi-Maßes.

Damit wird NEU-36 zu einer Maßkonvergenzfrage:

\[
\sum_{n,a,M}
\mu_{n,a,M}^{Wres}
\quad\stackrel{?}{\longrightarrow}\quad
\text{Nullstellenmaß von }\xi.
\]

Status: ✓ [M] als Reformulierung, ❓ [O] als Konvergenzaussage.

---

## 8. Momentenentwicklung und Mangoldt-Test

Für \(|z|\) groß gilt:

\[
(w-A_{n,a}^{(M),-})^{-1}
=
\frac1z
\sum_{k\ge0}
\left(\frac{\beta_NJ_N^-}{z}\right)^k.
\]

Daher:

\[
H_{N,n,a,M}^{-}(s)
=
-i
\sum_{k\ge0}
\frac{
\mu_{k}^{(n,a,M)}
}{
z_n(s)^{k+1}
},
\tag{37.18}
\]

mit Momenten

\[
\mu_k^{(n,a,M)}
:=
\operatorname{Tr}_{Wres,n,a,M}
\left((\beta_NJ_N^-)^kL_3^\circ\right).
\tag{37.19}
\]

Wegen der tridiagonalen schiefadjungierten Struktur zählen diese Momente geschlossene Wege auf der Kette:

\[
j_0\to j_1\to\cdots\to j_k=j_0.
\]

Jeder Schritt trägt ein Gewicht \(b_j\), also letztlich Faktoren

\[
(a+jn)\log n.
\]

Damit enthalten die geraden Momente typischerweise Potenzen

\[
(\log n)^{2q}.
\]

Odd-Momente verschwinden in symmetrischen Fällen oder sind reine Rand-/Indefinitheitseffekte.

### Diagnose

Das Mangoldt-Gewicht ist linear:

\[
\Lambda(p^m)=\log p.
\]

Die Jacobi-Momente liefern aber zunächst geschlossene-Weg-Gewichte mit Potenzen von \(\log n\).

Daher gilt:

\[
\boxed{
J_N^-\text{ erzeugt }\Lambda_N\text{ nicht automatisch.}
}
\]

Die benötigte Aussage ist eine nichttriviale Renormierungs-/Momentenidentität:

\[
\boxed{
\mathcal R_N
\left(
\{\mu_k^{(n,a,M)}\}_{k,n,a,M}
\right)
=
\Lambda_N(\cdot)
+
o(1).
}
\tag{37.20}
\]

Status: ❓ [O]

---

## 9. Vergleich mit der gewünschten Dirichlet-Form

Für \(\Re(s)>1\) müsste die einfache logarithmische Ableitung die Form haben:

\[
\frac{\xi_N'}{\xi_N}(s)
=
\text{archimedische Terme}
-
\sum_{m\in\langle p\le N\rangle}
\Lambda_N(m)m^{-s}.
\tag{37.21}
\]

Die berechnete Jacobi-Form ist dagegen:

\[
H_N^-(s)
=
-i
\sum_{n,a,M}
\int
\frac{d\mu_{n,a,M}^{Wres}(\lambda)}
{-i(s-\frac12)-h(n)-\lambda}.
\tag{37.22}
\]

Dies ist primär eine Summe von Cauchy-Transformierten, nicht unmittelbar eine Dirichletreihe.

Um (37.22) in (37.21) zu verwandeln, braucht man eine Laplace-Darstellung:

\[
\frac{1}{-i(s-\frac12)-h(n)-\lambda}
=
\int_0^\infty
e^{-t[-i(s-\frac12)-h(n)-\lambda]}\,dt
\]

in einem geeigneten Halbebenenbereich.

Dann müsste die integrierte Jacobi-Dynamik erfüllen:

\[
\sum_{n,a,M}
\int
e^{t(h(n)+\lambda)}
\,d\mu_{n,a,M}^{Wres}(\lambda)
\quad
\rightsquigarrow
\quad
\sum_{m}\Lambda_N(m)e^{-t\log m}.
\tag{37.23}
\]

Das ist die eigentliche arithmetische Momentenbedingung.

Status: ❓ [O]

---

## 10. Konsequenz für NEU-36

NEU-36 verlangte:

\[
H_N^-(s)\to \frac{\xi'}{\xi}(s).
\]

NEU-37 zeigt:

\[
H_N^-(s)
=
\text{explizite Summe gewichteter Jacobi-Cauchy-Transformierter}.
\]

Daher wird der offene Fehlerterm

\[
E_N^{Jac}
\]

präzise zu:

\[
\boxed{
E_N^{Jac}(s)
=
-i
\sum_{n,a,M}
\int
\frac{d\mu_{n,a,M}^{Wres}(\lambda)}
{-i(s-\frac12)-h(n)-\lambda}
-
\frac{\xi_N'}{\xi_N}(s)
}
\tag{37.24}
\]

nach Abzug von Primtrunkierung und Gamma-Faktor.

Status: ✓ [M] als Fehleridentität, ❓ [O] für Abschätzung.

---

## 11. Wichtiger negativer Befund

Falls auf jedem Orbit:

1. \(H_N=h(n)I\) konstant ist,
2. \(L_3^\circ\) diagonal-konstant ist,
3. keine zusätzliche KMS-/Laplace-Gewichtung eingebaut wird,

dann ist

\[
H_N^-(s)
\]

nur eine logarithmische Ableitung von Produkten der Polynome

\[
P_{M+1}^{(n,a)}(-i(s-\frac12)-h(n)).
\]

In diesem Fall erhält man zwar eine endliche Determinantenstruktur, aber nicht automatisch den Eulerprodukt-Logarithmus

\[
-\sum_{m}\Lambda(m)m^{-s}.
\]

Daher ist der naive Satz

\[
J_N^- \Rightarrow \Lambda_N
\]

falsch.

Korrekt ist nur:

\[
\boxed{
J_N^- \Rightarrow \text{Jacobi-Momentenmaß}.
}
\]

Das Mangoldt-Gewicht muss durch eine zusätzliche BC-identifizierbare Momenten-/Laplace-Transformation gewonnen werden.

Status: ✓ [M]

---

## 12. Reparaturpfade

NEU-37 lässt drei mögliche Reparaturwege offen.

### Pfad A — KMS-gewichteter Resolvent

Ersetze die reine \(Wres\)-Resolventspur durch eine KMS-gewichtete Version:

\[
H_{N,KMS}^{-}(s)
=
\operatorname{Tr}_{Wres,N}
\left(
\phi_s\bigl((s-D_N^-)^{-1}L_3^\circ\bigr)
\right).
\]

Dann entsteht \(n^{-s}\) wieder direkt aus \(\phi_s\), wie in NEU-28.

Status: plausibel, ❓ [O]

---

### Pfad B — Laplace-Transform des Jacobi-Flusses

Arbeite nicht mit dem Resolventen als rationaler Funktion, sondern mit

\[
e^{-tA_N^-}
\]

und zeige:

\[
\operatorname{Tr}_{Wres,N}
\left(e^{-tA_N^-}L_3^\circ\right)
\sim
\sum_m\Lambda_N(m)e^{-t\log m}.
\]

Dann ist der Resolvent nur die Laplace-Transformierte dieser arithmetischen Wärme-/Flussformel.

Status: ❓ [O]

---

### Pfad C — Favard-Rekonstruktion

Interpretiere \(J_N^-\) als Jacobi-Operator eines orthogonalen Polynomsystems und versuche, die Jacobi-Koeffizienten \(b_j\) direkt aus den Momenten der Mangoldt-Maßes zu identifizieren.

Dazu müsste gezeigt werden:

\[
b_j^2
=
\text{kanonische Hankel-/Momentenfunktion von }\Lambda_N.
\]

Status: ❓ [O], aber strukturell sehr klar.

---

## 13. Neuer Leitsatz

### Satz 37.1 — Jacobi-Resolventformel

Auf jedem endlichen Orbit \(\mathcal H_{n,a}^{(M)}\) gilt:

\[
H_{N,n,a,M}^{-}(s)
=
-i
\sum_{j=0}^{M}
\ell_j^{(n,a)}
\frac{
P_j^{L}(z_n(s))P_{M-j}^{R}(z_n(s))
}{
P_{M+1}^{(n,a)}(z_n(s))
}.
\]

Insbesondere ist \(H_N^-\) eine explizite Summe endlicher Cauchy-Transformierter von \(Wres\)-Jacobi-Maßen.

Status: ✓ [M]

---

### Satz 37.2 — Mangoldt-Obstruktion des naiven Jacobi-Ansatzes

Aus der Jacobi-Resolventformel folgt nicht automatisch

\[
H_N^-(s)=\xi_N'(s)/\xi_N(s)+o(1).
\]

Vielmehr ist dies äquivalent zu einer zusätzlichen Momenten-/Laplace-Identität zwischen den \(Wres\)-Jacobi-Maßen und dem endlichen Mangoldt-Maß.

Status: ✓ [M] als Reduktion, ❓ [O] als Identität.

---

## 14. Statusmatrix

| Aussage | Status |
|---|---:|
| Orbitzerlegung \(\mathcal H_{n,a}^{(M)}\) | ✓ [M] |
| Matrixform von \(A_N^-\) | ✓ [M] |
| Kontinuantenrekursion für Orbitdeterminanten | ✓ [M] |
| diagonale Resolventformel | ✓ [M] |
| \(Wres\)-Resolvent als gewichtete Cauchy-Transformierte | ✓ [M] |
| Spezialfall als logarithmische Ableitung lokaler Polynome | ✓ [M] |
| automatische Erzeugung von \(\Lambda_N\) durch \(J_N^-\) | ✗ [M] |
| Momenten-/Laplace-Identität zu \(\Lambda_N\) | ❓ [O] |
| KMS-gewichtete Reparatur | ❓ [O] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |

---

## 15. Fazit

NEU-37 berechnet den Jacobi-Resolventen vollständig.

Der harte Punkt ist nicht mehr:

\[
\text{Wie berechnet man }(s-D_N^-)^{-1}?
\]

sondern:

\[
\text{Warum sollte seine }Wres\text{-Cauchy-Transformierte das Mangoldt-Maß erzeugen?}
\]

Die Antwort ist nicht automatisch in \(J_N^-\) enthalten.

Daher lautet die nächste Aufgabe:

\[
\boxed{
\text{NEU-38: KMS-gewichteter Jacobi-Resolvent und Rückgewinnung von }n^{-s}.
}
\]

Dort muss geprüft werden, ob der Kürzungsmechanismus aus NEU-28 mit der Jacobi-Kopplung aus NEU-35/37 kompatibel ist.
