# NEU-34 — X.3: Spektrum der \(\widetilde\omega_2\)-Kopplung

**Stand:** 28. Juni 2026  
**Kette:** X.3 nach NEU-30–33  
**Status:** Diagnose abgeschlossen; rohe Kopplung liefert ein No-Go; symmetrisierte Jacobi-Kopplung als Reparaturkandidat.

---

## 0. Ausgangspunkt

Nach NEU-33 ist der naive Kommutatorterm

\[
K_N=[L_3^N,\cdot]
\]

trivial, weil der relevante \(V\)-Sektor von \(\mathbb N^\times\) abelsch ist. Die nichttriviale Kopplung kann daher nicht aus dem \(V\)-Kommutator kommen, sondern muss aus der Fourier-Richtung der Hochschild-Klasse stammen:

\[
\widetilde\omega_2(e_rV_n,e_sV_m)
  =-rs\log(n)\, e_{r+ns}V_{nm}.
\]

Insbesondere erzeugt die Kopplung bei Fixierung des zweiten Fourier-Modes \(s=1,m=1\) den Shift

\[
r\longmapsto r+n.
\]

Damit ist der natürliche rohe Kopplungsoperator auf Basisvektoren

\[
E_{r,n}:=e_rV_n
\]

gegeben durch

\[
\Theta_N E_{r,n}
   = -\gamma_N\, r\log(n)\,E_{r+n,n},
\tag{34.1}
\]

wobei \(\gamma_N\) eine Normierungs-/Trunkierungskonstante ist. Für \(n=1\) verschwindet der Term wegen \(\log(1)=0\).

Der diagonale Hamiltonterm sei

\[
H_NE_{r,n}=h(n)E_{r,n},
\qquad h(n)=\log n
\]

oder allgemeiner ein reeller Funktionswert von \(n\). Dann gilt formal

\[
[H_N,\Theta_N]=0,
\]

weil \(\Theta_N\) den \(n\)-Index erhält.

---

## 1. Orbitzerlegung der Fourier-Richtung

Für festes \(n>1\) zerfällt die Fourier-Richtung in Restklassen modulo \(n\):

\[
\mathcal H_{n,a}
  :=\overline{\operatorname{span}}\{E_{a+kn,n}: k\in\mathbb Z\},
  \qquad a\in\mathbb Z/n\mathbb Z.
\]

Auf \(\mathcal H_{n,a}\) wirkt \(\Theta_N\) als gewichteter Shift

\[
\Theta_{n,a}E_{k}
 = -\gamma_N(a+kn)\log(n)E_{k+1},
\tag{34.2}
\]

wobei

\[
E_k:=E_{a+kn,n}.
\]

Damit ist das Spektralproblem vollständig auf gewichtete Shifts auf eindimensionalen Gittern reduziert.

**Status:** ✓ [M]

---

## 2. Korrektur: \([H_N,\Theta_N]=0\) impliziert keine Normalität

Aus NEU-33 folgt korrekt

\[
[H_N,\Theta_N]=0.
\]

Dies reicht aber nicht, um

\[
A_N:=H_N+i\beta_N\Theta_N
\]

als normal zu klassifizieren. Normalität verlangt

\[
[A_N,A_N^*]=0.
\]

Da \(H_N\) auf jedem \(n\)-Sektor skalar ist, reduziert sich der Normalitätsdefekt auf

\[
[A_N,A_N^*]
  =\beta_N^2[\Theta_N,\Theta_N^*].
\]

Für die rohe Kopplung (34.1) gilt

\[
\Theta_N^*E_{r,n}
  =-\gamma_N(r-n)\log(n)E_{r-n,n}.
\]

Daher

\[
\Theta_N^*\Theta_NE_{r,n}
  =\gamma_N^2r^2\log(n)^2E_{r,n},
\]

während

\[
\Theta_N\Theta_N^*E_{r,n}
  =\gamma_N^2(r-n)^2\log(n)^2E_{r,n}.
\]

Also

\[
[\Theta_N,\Theta_N^*]E_{r,n}
  =\gamma_N^2\bigl((r-n)^2-r^2\bigr)\log(n)^2E_{r,n}
\]

und somit

\[
[\Theta_N,\Theta_N^*]E_{r,n}
  =\gamma_N^2(n^2-2nr)\log(n)^2E_{r,n}.
\tag{34.3}
\]

Für \(n>1\) ist dies im Allgemeinen nicht null.

**Folgerung:**

\[
[H_N,\Theta_N]=0
\quad\not\Rightarrow\quad
A_N\text{ normal}.
\]

Die Aussage „\(A_N=H_N+i\beta_N\Theta_N\) ist normal“ ist nur dann haltbar, wenn \(\Theta_N\) zusätzlich normal ist oder durch einen symmetrisierten Operator ersetzt wird.

**Status:** ✓ [M]

---

## 3. Spektrum der rohen endlichen Trunkierung

Betrachte eine endliche Fourier-Trunkierung eines Orbits

\[
\mathcal H_{n,a}^{(M)}
 :=\operatorname{span}\{E_0,E_1,\ldots,E_M\}.
\]

Mit Randprojektion ohne zyklischen Wrap-around ist \(\Theta_{n,a}^{(M)}\) strikt oberdreieckig:

\[
\Theta_{n,a}^{(M)}E_k
 =w_kE_{k+1},
\qquad
w_k=-\gamma_N(a+kn)\log(n),
\qquad 0\le k<M,
\]

und

\[
\Theta_{n,a}^{(M)}E_M=0.
\]

Damit ist

\[
(\Theta_{n,a}^{(M)})^{M+1}=0.
\]

Also

\[
\operatorname{Spec}(\Theta_{n,a}^{(M)})=\{0\}.
\]

Da \(H_N=h(n)\) auf diesem Orbit skalar ist, folgt

\[
\operatorname{Spec}\bigl(A_N^{raw}|_{\mathcal H_{n,a}^{(M)}}\bigr)
  =\{h(n)\}.
\tag{34.4}
\]

Über alle endlichen \(n\)-Sektoren ergibt sich nur

\[
\operatorname{Spec}(A_N^{raw})
  \subseteq \{h(n):n\in S_N\}.
\]

Die \(\widetilde\omega_2\)-Kopplung erzeugt also zwar nichttriviale Jordan-/Pseudospektralstruktur, aber keine neuen Eigenwerte in der natürlichen nichtzyklischen endlichen Trunkierung.

**Status:** ✓ [M]

---

## 4. Künstlicher zyklischer Wrap-around ist nicht intrinsisch

Falls man stattdessen den Rand künstlich identifiziert,

\[
E_M\mapsto E_0,
\]

erhält man einen gewichteten zyklischen Shift. Dann erfüllen die Eigenwerte \(\lambda\) von \(\Theta_{n,a}^{cyc}\)

\[
\lambda^{M+1}=\prod_{k=0}^{M}w_k.
\]

Also

\[
\lambda_j
  =\left(\prod_{k=0}^{M}w_k\right)^{1/(M+1)}
    \exp\left(\frac{2\pi ij}{M+1}\right),
  \qquad j=0,\ldots,M.
\]

Diese Eigenwerte hängen jedoch entscheidend von der künstlichen Randidentifikation ab. Der zyklische Wrap-around ist keine kanonische Operation der BC-Algebra und darf deshalb nicht als intrinsische Spektralkonstruktion verwendet werden.

**Status:** ✓ [M]

---

## 5. No-Go für den rohen Operator

Die rohe Kopplung

\[
A_N^{raw}=H_N+i\beta_N\Theta_N
\]

scheitert an zwei Punkten:

1. \(A_N^{raw}\) ist im Allgemeinen nicht normal, weil \(\Theta_N\) nicht normal ist.
2. In natürlicher endlicher Trunkierung verschiebt \(\Theta_N\) zwar Fourier-Indizes, erzeugt aber nur nilpotente Jordanstruktur und keine neuen Eigenwerte.

Damit kann \(A_N^{raw} nicht der gesuchte selbstadjungierte bzw. normal-geometrische Approximant für \(D_X^{geom}\) sein.

**Status:** ✓ [M]

---

## 6. Reparatur: symmetrisierte Jacobi-Kopplung

Der richtige Spektralträger kann nicht der rohe Shift sein, sondern dessen kanonische symmetrische Kombination. Zwei natürliche Varianten sind:

\[
J_N^{+}:=\frac12(\Theta_N+\Theta_N^*),
\]

und

\[
J_N^{-}:=\frac{1}{2i}(\Theta_N-\Theta_N^*).
\]

Beide sind formal selbstadjungiert auf den endlichen Trunkierungen.

Der reparierte Kandidat lautet daher

\[
A_N^{Jac}=H_N+\beta_NJ_N,
\tag{34.5}
\]

mit

\[
J_N\in\{J_N^{+},J_N^{-}\}.
\]

Dann ist

\[
D_{X,N}^{Jac}:=\frac12 I+iA_N^{Jac}
\]

formal auf der kritischen Geraden, sobald \(A_N^{Jac} selbstadjungiert ist.

---

## 7. Spektralformel für die Jacobi-Trunkierung

Auf einem Orbit \(\mathcal H_{n,a}^{(M)}\) ist \(J_N^{+}\) eine tridiagonale Jacobi-Matrix mit Offdiagonalgewichten

\[
b_k=\frac12w_k
 =-\frac{\gamma_N}{2}(a+kn)\log(n),
\qquad 0\le k<M.
\]

Die Eigenwerte von

\[
A_{n,a,M}^{Jac}=h(n)I+\beta_NJ_{n,a,M}^{+}
\]

sind

\[
\lambda_{n,a,M,j}=h(n)+\beta_N\mu_{n,a,M,j},
\]

wobei \(\mu_{n,a,M,j}\) die Nullstellen des charakteristischen Polynoms

\[
P_{M+1}^{(n,a)}(\mu)
\]

sind, definiert durch die Rekursion

\[
P_0(\mu)=1,
\qquad
P_1(\mu)=\mu,
\]

und

\[
P_{k+1}(\mu)
  =\mu P_k(\mu)-b_{k-1}^2P_{k-1}(\mu).
\tag{34.6}
\]

Damit gilt

\[
\operatorname{Spec}(D_{X,N}^{Jac}|_{\mathcal H_{n,a}^{(M)}})
  =\left\{
       \frac12+i\bigl(h(n)+\beta_N\mu_{n,a,M,j}\bigr)
     :0\le j\le M
    \right\}.
\tag{34.7}
\]

Dies ist die erste nichttriviale, nicht-tautologische Spektralformel aus der BC-intrinsischen Kopplung.

**Status:** ✓ [M] für endliche Jacobi-Trunkierungen.

---

## 8. Konsequenz für X.3

NEU-34 verschiebt den Engpass:

Nicht mehr die Existenz eines nichttrivialen Kopplungsterms ist das Problem — diese liefert \(\widetilde\omega_2\). Das Problem ist die korrekte Selbstadjungiertmachung dieses Terms.

Die rohe Hochschild-Kopplung erzeugt einen gerichteten Shift:

\[
\Theta_N:E_{r,n}\mapsto E_{r+n,n}.
\]

Der RH-taugliche Operator muss aber den symmetrisierten Jacobi-Anteil verwenden:

\[
\Theta_N\leadsto J_N=\frac12(\Theta_N+\Theta_N^*)
\quad\text{oder}\quad
J_N=\frac1{2i}(\Theta_N-\Theta_N^*).
\]

Damit lautet der neue Kandidat:

\[
D_{X,N}^{geom}
  :=\frac12I+i\bigl(H_N+eta_NJ_N\bigr).
\tag{34.8}
\]

Der nächste echte Schritt ist nicht mehr „Spektrum von \(\Theta_N\)“, sondern:

\[
\det_{Wres}(s-D_{X,N}^{geom})
  \stackrel{?}{\longrightarrow} C\xi(s).
\]

---

## 9. Statusmatrix

| Aussage | Status |
|---|---:|
| Orbitzerlegung nach \((n,a\bmod n)\) | ✓ [M] |
| \([H_N,\Theta_N]=0\) | ✓ [M] |
| \([H_N,\Theta_N]=0\Rightarrow A_N\) normal | ✗ [M] |
| Normalitätsdefekt \([\Theta_N,\Theta_N^*]\) explizit berechnet | ✓ [M] |
| rohe endliche Trunkierung von \(\Theta_N\) nilpotent | ✓ [M] |
| Spektrum von \(A_N^{raw}\) nur \(h(n)\) | ✓ [M] |
| zyklischer Wrap-around nicht intrinsisch | ✓ [M] |
| symmetrisierte Jacobi-Kopplung \(J_N\) | ✓ [M] |
| Spektralrekursion für \(A_N^{Jac}\) | ✓ [M] |
| Determinantenkonvergenz zu \(\xi\) | ❓ [O] |
| Wahl zwischen \(J_N^+\) und \(J_N^-\) aus Frobenius-/Modularstruktur | ❓ [O] |

---

## 10. Neuer Leitsatz nach NEU-34

\[
\boxed{
\text{Die Hochschild-Kopplung }\widetilde\omega_2
\text{ liefert nicht direkt einen normalen Operator,}
\text{ sondern einen gerichteten gewichteten Shift.}
}
\]

\[
\boxed{
\text{Der RH-fähige geometrische Operator muss die kanonische}
\ Wres\text{-Adjungierung dieses Shifts verwenden.}
}
\]

Damit wird X.3 präziser:

\[
\boxed{
D_X^{geom}
=\frac12I+i\lim_{N\to\infty}(H_N+eta_NJ_N),
\quad
J_N=\operatorname{Sym}_{Wres}(\Theta_N).
}
\]

Der nächste natürliche Schritt ist daher **NEU-35**:

> Bestimme die kanonische \(Wres_{BC}^{top}\)-Adjungierung von \(\Theta_N\) und entscheide, ob \(J_N^+\) oder \(J_N^-\) die modular korrekte Kopplung ist.
