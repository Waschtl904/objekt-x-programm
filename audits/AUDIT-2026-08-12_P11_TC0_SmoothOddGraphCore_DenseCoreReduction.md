# P11-TC0 — Smooth Odd Graph-Core Gate and Dense-Core Reduction

**Datum:** 2026-08-12  
**Programm:** P11 — `Global Coupling and the Object-X Candidate Geometry`  
**Knoten:** `[P11-TC0]`  
**Scope:** direkter Terminalkonvergenzpfad; kein O3-Folgeknoten; Form-/Graph-Core, nicht Operator-Core.

---

## 0. Status

\[
\boxed{
[P11\text{-}TC0]
\quad
\checkmark[M]_{\rm A}
+\checkmark[M]_{\rm B}
+\checkmark[M]_{\rm C}
}
\]

mit

\[
\boxed{
\text{TC0-A: } C_c^\infty(-R,R)\text{ ist ein Gamma-Form-Core},
}
\]

\[
\boxed{
\text{TC0-B: } C_c^\infty(-R,R)\text{ ist ein Objekt-X-Graph-Core},
}
\]

\[
\boxed{
\text{TC0-C: } C_c^\infty(-R,R)_{\rm odd}\text{ ist ein Core von }\mathcal K_{X,R}^{-}.
}
\]

**Firewall:** Es wird nicht behauptet, dass \(C_c^\infty(-R,R)\) ein Operator-Core von \(C_{\Gamma,R}\) in dessen Operatorgraphnorm ist. Fuer den direkten Terminalkonvergenzpfad wird nur der Form-/Graph-Core benoetigt.

---

## 1. Verbindliche Ausgangsdaten

Aus C1z-B1 gilt auf \(\mathscr H_R=L^2(-R,R)\)

\[
q_{\Gamma,R}(f)
=
\frac1{2\pi}\int_{\mathbb R}
\bigl(1+g_\infty(\xi)\bigr)
\left|\widehat{E_Rf}(\xi)\right|^2\,d\xi,
\]

mit

\[
g_\infty(\xi)
=
\sum_{j=0}^\infty
\frac{\xi^2/4}{a_j(a_j^2+\xi^2/4)},
\qquad a_j=j+\frac14.
\]

Setze

\[
w(\xi):=1+g_\infty(\xi).
\]

Die Formdomaene ist

\[
\mathcal D_{\Gamma,R}
=
\left\{
f\in L^2(-R,R):
\int_{\mathbb R}w(\xi)|\widehat{E_Rf}(\xi)|^2\,d\xi<\infty
\right\}.
\]

Aus C1z-B2-C1 gilt fuer festes \(R\):

\[
\boxed{
q_{\Gamma,R}(f)
\le q_R^X(f)
\le (1+\|H_R\|^2)q_{\Gamma,R}(f).
}
\tag{TC0.1}
\]

Damit sind Gamma-Formnorm und Objekt-X-Graphnorm auf derselben Formdomaene topologisch aequivalent.

---

## 2. TC0-A — Gamma-Form-Core

### Satz TC0.1

Fuer jedes feste \(R>0\) gilt

\[
\boxed{
\overline{C_c^\infty(-R,R)}^{\,\|\cdot\|_{q_{\Gamma,R}}}
=
\mathcal D_{\Gamma,R}.
}
\tag{TC0.2}
\]

### Beweis

Sei

\[
f\in\mathcal D_{\Gamma,R},
\qquad F:=E_Rf.
\]

Dann

\[
\operatorname{supp}F\subset[-R,R].
\]

#### Schritt 1 — Trägerdilatation nach innen

Fuer \(0<a<1\) definiere

\[
F_a(x):=a^{-1/2}F(x/a).
\]

Dann ist die Dilatation auf \(L^2(\mathbb R)\) unitaer und

\[
\operatorname{supp}F_a
\subset[-aR,aR]\Subset(-R,R).
\]

Auf Fourierseite gilt

\[
\widehat{F_a}(\xi)=a^{1/2}\widehat F(a\xi).
\]

Fuer \(\lambda\ge1\) gilt summandenweise

\[
\frac{\lambda^2\xi^2/4}{a_j(a_j^2+\lambda^2\xi^2/4)}
\le
\lambda^2
\frac{\xi^2/4}{a_j(a_j^2+\xi^2/4)}.
\]

Nach Summation:

\[
g_\infty(\lambda\xi)
\le
\lambda^2g_\infty(\xi).
\]

Da \(\lambda^2\ge1\), folgt auch fuer \(w=1+g_\infty\)

\[
\boxed{
w(\lambda\xi)\le\lambda^2w(\xi).}
\tag{TC0.3}
\]

Insbesondere fuer \(\lambda=a^{-1}\):

\[
\boxed{
w(\xi/a)\le a^{-2}w(\xi).}
\tag{TC0.4}
\]

Damit sind die Dilatationsoperatoren fuer \(a\in[1/2,1)\) gleichmaessig beschraenkt im gewichteten Raum

\[
L^2(\mathbb R,w(\xi)d\xi).
\]

Genauer:

\[
\begin{aligned}
\int w(\xi)\,|a^{1/2}\widehat F(a\xi)|^2d\xi
&=
\int w(\eta/a)|\widehat F(\eta)|^2d\eta\\
&\le
 a^{-2}\int w(\eta)|\widehat F(\eta)|^2d\eta.
\end{aligned}
\tag{TC0.5}
\]

Fuer kompakt in \(\xi\) getragene Funktionen ist die starke Stetigkeit von Dilatationen unmittelbar. Durch Dichte solcher Funktionen im gewichteten \(L^2(wd\xi)\) und die uniforme Schranke (TC0.5) folgt fuer beliebiges \(F\) in der Formdomaene

\[
\boxed{
\|F_a-F\|_{q_\Gamma}\longrightarrow0
\qquad(a\uparrow1).
}
\tag{TC0.6}
\]

#### Schritt 2 — Mollifikation bei bereits innerem Träger

Waehle

\[
\rho\in C_c^\infty(-1,1),
\qquad
\rho\ge0,
\qquad
\int\rho=1,
\]

und

\[
\rho_\delta(x):=\delta^{-1}\rho(x/\delta).
\]

Fixiere \(a<1\) und waehle

\[
0<\delta<(1-a)R.
\]

Setze

\[
F_{a,\delta}:=\rho_\delta*F_a.
\]

Dann

\[
\operatorname{supp}F_{a,\delta}
\subset[-aR-\delta,aR+\delta]
\Subset(-R,R),
\]

also

\[
F_{a,\delta}\in C_c^\infty(-R,R).
\]

Auf Fourierseite:

\[
\widehat{F_{a,\delta}}(\xi)
=
\widehat\rho(\delta\xi)\widehat F_a(\xi).
\]

Wegen \(\rho\ge0\), \(\int\rho=1\) gilt

\[
|\widehat\rho(\delta\xi)|\le1
\]

und

\[
\widehat\rho(\delta\xi)\to1
\]

punktweise fuer \(\delta\downarrow0\). Dominierte Konvergenz liefert daher

\[
\boxed{
\|F_{a,\delta}-F_a\|_{q_\Gamma}\longrightarrow0
\qquad(\delta\downarrow0).
}
\tag{TC0.7}
\]

#### Schritt 3 — Diagonalfolge

Waehle \(a_n\uparrow1\) so, dass

\[
\|F_{a_n}-F\|_{q_\Gamma}<\frac1{2n}.
\]

Waehle danach

\[
0<\delta_n<(1-a_n)R
\]

so klein, dass

\[
\|F_{a_n,\delta_n}-F_{a_n}\|_{q_\Gamma}<\frac1{2n}.
\]

Dann

\[
F_n:=F_{a_n,\delta_n}\in C_c^\infty(-R,R)
\]

und

\[
\|F_n-F\|_{q_\Gamma}<\frac1n.
\]

Damit ist (TC0.2) bewiesen. \(\square\)

Status:

\[
\boxed{\checkmark[M]_{\rm TC0-A}.}
\]

---

## 3. TC0-B — Objekt-X-Graph-Core

Aus der Normaequivalenz (TC0.1) erzeugen \(\|\cdot\|_{q_{\Gamma,R}}\) und \(\|\cdot\|_{X,R}\) dieselbe Topologie auf \(\mathcal D_{\Gamma,R}\). Daher folgt unmittelbar aus TC0-A:

\[
\boxed{
\overline{C_c^\infty(-R,R)}^{\,\|\cdot\|_{X,R}}
=
\mathcal K_{X,R}.
}
\tag{TC0.8}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm TC0-B}.}
\]

---

## 4. TC0-C — odd Graph-Core

Die explizite Reihe fuer \(g_\infty\) haengt nur von \(\xi^2\) ab. Daher

\[
\boxed{g_\infty(-\xi)=g_\infty(\xi).}
\tag{TC0.9}
\]

Fuer die Reflexion

\[
(\mathcal Rf)(u):=f(-u)
\]

folgt deshalb

\[
q_{\Gamma,R}(\mathcal Rf)=q_{\Gamma,R}(f).
\]

Der Antisymmetrisierer

\[
P_-:=\frac{I-\mathcal R}{2}
\]

ist somit eine Kontraktion in der Gamma-Formnorm:

\[
q_{\Gamma,R}(P_-f)^{1/2}
\le q_{\Gamma,R}(f)^{1/2}.
\]

Mit (TC0.1):

\[
\begin{aligned}
q_R^X(P_-f)
&\le(1+\|H_R\|^2)q_{\Gamma,R}(P_-f)\\
&\le(1+\|H_R\|^2)q_{\Gamma,R}(f)\\
&\le(1+\|H_R\|^2)q_R^X(f).
\end{aligned}
\tag{TC0.10}
\]

Also ist \(P_-\) beschraenkt auf \(\mathcal K_{X,R}\).

Sei nun

\[
f\in\mathcal K_{X,R}^{-}.
\]

Nach TC0-B existiert \(\phi_n\in C_c^\infty(-R,R)\) mit

\[
\phi_n\to f
\]

in \(\|\cdot\|_{X,R}\). Setze

\[
\psi_n:=P_-\phi_n.
\]

Dann

\[
\psi_n\in C_c^\infty(-R,R)_{\rm odd}
\]

und, da \(P_-f=f\),

\[
\psi_n-f=P_-(\phi_n-f)\to0
\]

in \(\|\cdot\|_{X,R}\). Somit

\[
\boxed{
\overline{C_c^\infty(-R,R)_{\rm odd}}^{\,\|\cdot\|_{X,R}}
=
\mathcal K_{X,R}^{-}.
}
\tag{TC0.11}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm TC0-C}.}
\]

---

## 5. Dense-core reduction for terminal convergence

Fuer feste \(0<R<S\) sei

\[
W_T:=W_{R,S,-}^{[T]},
\qquad T>S.
\]

Die committed Terminal-Gauge-Geometrie gibt

\[
W_T^*W_T=I,
\]

also

\[
\boxed{\|W_T\|=1\quad\text{fuer alle }T>S.}
\tag{TC0.12}
\]

Sei

\[
\mathscr D_R^-:=C_c^\infty(-R,R)_{\rm odd}.
\]

Nach TC0-C ist \(\mathscr D_R^-\) dicht in \(\mathcal K_{X,R}^-\).

Angenommen, fuer jedes \(f\in\mathscr D_R^-\) ist \((W_Tf)_{T>S}\) eine Cauchyfamilie in \(\mathcal K_{X,S}^-\). Dann ist \((W_Tx)_T\) fuer jedes \(x\in\mathcal K_{X,R}^-\) Cauchy.

Denn fuer \(f\in\mathscr D_R^-\):

\[
\begin{aligned}
\|W_Ux-W_Tx\|
&\le
\|W_U(x-f)\|
+\|W_Uf-W_Tf\|
+\|W_T(f-x)\|\\
&\le
2\|x-f\|_{X,R}
+\|W_Uf-W_Tf\|.
\end{aligned}
\tag{TC0.13}
\]

Erst waehlt man \(f\) graphnormnah an \(x\), dann \(T,U\) gross genug fuer den Core-Cauchyterm.

Daher:

\[
\boxed{
\text{starke Terminal-Cauchy-Konvergenz auf }\mathscr D_R^-
\Longrightarrow
\text{starke Terminal-Cauchy-Konvergenz auf }\mathcal K_{X,R}^-.
}
\tag{TC0.14}
\]

Dies legitimiert den direkten Konvergenzpfad auf glatten odd Testvektoren.

---

## 6. Scope / Firewalls

Bewiesen:

\[
\boxed{
C_c^\infty(-R,R)_{\rm odd}
\text{ ist ein dichter Objekt-X-Graph-Core.}
}
\]

Bewiesen:

\[
\boxed{
\sup_T\|W_{R,S,-}^{[T]}\|=1
\text{ und daher reicht Core-Cauchy-Konvergenz fuer globale starke Konvergenz.}
}
\]

Nicht bewiesen:

\[
\boxed{
W_{R,S,-}^{[T]}f\text{ ist fuer glatte odd }f\text{ Cauchy}.}
\]

Nicht bewiesen:

\[
\boxed{
W_{R,S,-}^{[T]}\to W_{R,S,-}^{[\infty]}\text{ stark}.}
\]

Nicht behauptet:

\[
\boxed{
C_c^\infty(-R,R)\text{ ist Operator-Core von }C_{\Gamma,R}.
}
\]

---

## 7. Naechstes direktes Gate

Der naechste direkte Knoten ist nicht O3k, sondern

\[
\boxed{
\texttt{P11-TC1 — Cross-Terminal Overlap on the Smooth Odd Core}.}
\]

Mit

\[
C_{T,U}:=(W_{R,S,-}^{[T]})^*W_{R,S,-}^{[U]}
\]

ist fuer \(f\in\mathscr D_R^-\)

\[
\frac12\|W_Uf-W_Tf\|^2
=
\|f\|^2-\operatorname{Re}\langle f,C_{T,U}f\rangle.
\]

TC1 soll pruefen, ob dieser Cross-Terminal-Overlap eine explizite oder positive Future-Tail-/Gram-Darstellung besitzt, die ohne den superpolynomial konditionierten O3-Produktkanal kontrolliert werden kann.
