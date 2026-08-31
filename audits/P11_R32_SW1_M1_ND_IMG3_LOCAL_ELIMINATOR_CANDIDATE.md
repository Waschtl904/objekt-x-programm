# P11/R32 — SW1 M1-ND IMG3 Local Eliminator and Horizon Contraction Candidate

> **Stand:** 31. August 2026  
> **Stacked base:** research/sw1-m1-nd-img2-descriptor @ 2e193c5b5726ea66cb8f06de1e2cddbf963b887e  
> **Arbeitsbranch:** research/sw1-m1-nd-img3-eliminator  
> **Status:** AI-GREEN candidate — lokaler \(R0+\mathrm{KNF}+(R6,R7)\)-Eliminator und Horizon-Kontraktionssatz als Auditkandidat; finite/algebraische Prämissen separat zertifiziert. **Keine Promotion.**  
> **Scope-Firewall:** noch keine Injektivität von \(\mathscr N_R\), kein \(\ker\Gamma_I=\{0\}\), keine RH-/Objekt-X-Folgerung.

---

# 0. Ziel

IMG2 liefert

\[
\mathscr N_R(f,g)
=
D_R f+\mathcal R_R f+\mathcal H_R g
\]

auf

\[
\mathscr B_K\oplus\mathscr B_W,
\]

mit

\[
D_R^{-1}\in\mathcal B(\mathscr B_H^0)
\]

als reinem Multiplikationsinverse, aber bis IMG2 ausdrücklich **ohne** Beweis von

\[
\|D_R^{-1}\mathcal R_R\|<1.
\]

IMG3 verfolgt zwei getrennte Angriffe:

1. **lokale Elimination**
   \[
   R0+\mathrm{KNF}+(R6,R7),
   \]
   um Summen-/Differenzkanäle direkt zu synchronisieren;

2. **globale Horizon-Kontraktion**, indem die Selbstadjungiertheit des physischen FREE-Blocks mit exakter Row-Diagonaldominanz kombiniert wird.

Der zweite Punkt ist der stärkere neue Befund.

---

# Teil I — Lokaler Eliminator

## 1. Innerer Streifen

Wir arbeiten mit

\[
0<\sigma<R<\varepsilon<E_{\max},
\qquad
0<u<R.
\]

Die physikalischen Ausgabepunkte

\[
x=u,\qquad x=T-u,\qquad x=T+u
\]

liegen damit in den Rowtypen

\[
R0,\qquad R6,\qquad R7.
\]

Für die beiden äußeren Rows \(R6/R7\) gilt wegen \(u<R\):

- die \(p\)-Hubbranches bei \(a\pm u\) sind aktiv;
- die \(r\)-Hubbranches bei \(e\pm u\) sind aktiv;
- der \(q\)-Branch trifft \(\pm u\), liegt also unter dem Annuluscut und ist tot.

Diese Supportaussagen werden im IMG3-Eliminator-Skript aus den C1B2A-Slacks exakt geprüft.

## 2. Notation

Setze

\[
A_-:=y(a-u),\quad A_+:=y(a+u),
\]

\[
B_-:=y(b-u),\quad B_+:=y(b+u),
\]

\[
T_-:=y(T-u),\quad T_+:=y(T+u),
\]

\[
D_-:=y(2d-u),\quad D_+:=y(2d+u).
\]

Für Annuluswerte schreiben wir analog

\[
W_{A,\pm}:=w(a\pm u),\quad
W_{B,\pm}:=w(b\pm u),\quad
W_{e,\pm}:=w(e\pm u),\quad
W_{T,\pm}:=w(T\pm u).
\]

Weiter

\[
S_A=A_-+A_+,\qquad D_A=A_--A_+,
\]

\[
S_T=T_-+T_+,\qquad D_T=T_--T_+,
\]

\[
S_D=D_-+D_+,\qquad D_D=D_--D_+.
\]

Für die Annuluspaare werden \(S_{WA},D_{WA},S_{We},D_{We}\) identisch definiert.

## 3. R0

Aus der zertifizierten A1-Row \(R0\) folgt

\[
\boxed{
\begin{aligned}
0={}&
(1+2c_1)y(u)
+c_2S_A
+\beta_0S_T\\
&-pS_{WA}
-rS_{WB}
-qW_{T,-}
-\mathbf1_{\{u<\sigma\}}qW_{T,+}.
\end{aligned}}
\tag{IMG3.1}
\]

## 4. R6 und R7

Für \(x=T-u\):

\[
\boxed{
\begin{aligned}
0={}&
(1+\kappa)T_-
+\beta_TT_+
+\beta_0y(u)\\
&+\beta_-A_+
+\beta_+A_-
+\beta_bD_+\\
&+pW_{A,-}
+rW_{e,-}.
\end{aligned}}
\tag{IMG3.2}
\]

Für \(x=T+u\):

\[
\boxed{
\begin{aligned}
0={}&
\beta_TT_-
+(1+\kappa)T_+
+\beta_0y(u)\\
&+\beta_-A_-
+\beta_+A_+
+\beta_bD_-\\
&+pW_{A,+}
+rW_{e,+}.
\end{aligned}}
\tag{IMG3.3}
\]

Kein \(q\,w(u)\)-Term bleibt übrig, weil \(u<R\).

## 5. Differenzrow

Setze

\[
\lambda_\Delta:=1+\kappa-\beta_T,
\qquad
\gamma:=\beta_+-\beta_-.
\]

Dann liefert \(R6-R7\)

\[
\boxed{
0=
\lambda_\Delta D_T
+\gamma D_A
-\beta_bD_D
+pD_{WA}
+rD_{We}.
}
\tag{IMG3.4}
\]

Ferner gilt

\[
\lambda_\Delta>0,\qquad \gamma>0.
\]

## 6. KNF-Differenzrow

Die in IMG2 internalisierte KNF-Bedingung lautet

\[
\boxed{
qD_T+pD_A+rD_B=0.
}
\tag{IMG3.5}
\]

Damit besitzen IMG3.4 und IMG3.5 dieselben beiden Zielvariablen \((D_T,D_A)\).

## 7. Neuer DIFF-PIVOT

Die Koeffizientenmatrix ist

\[
\boxed{
M_{\rm diff}
=
\begin{pmatrix}
\lambda_\Delta&\gamma\\
q&p
\end{pmatrix}.
}
\tag{IMG3.6}
\]

Ihre Determinante ist

\[
\Delta_{\rm diff}=p\lambda_\Delta-q\gamma.
\]

Das Zertifikat vereinfacht exakt zu

\[
\boxed{
\Delta_{\rm diff}
=
\frac{2^{1/4}\sqrt{\log2}}{144}
\left(
72
+18\sqrt2\,\log2
+45\log2
+16\sqrt3\,\log3
\right)
>0.
}
\tag{IMG3.7}
\]

Definiere

\[
F_{\rm diff}
:=
-\beta_bD_D+pD_{WA}+rD_{We}.
\]

Dann folgt per Cramer

\[
\boxed{
D_T
=
\frac{-pF_{\rm diff}+\gamma rD_B}
{\Delta_{\rm diff}},
}
\tag{IMG3.8}
\]

\[
\boxed{
D_A
=
\frac{qF_{\rm diff}-\lambda_\Delta rD_B}
{\Delta_{\rm diff}}.
}
\tag{IMG3.9}
\]

Dies ist eine echte lokale Synchronisationsrelation. Daraus folgt noch keine globale Unique Continuation.

## 8. SUM-CANCEL

Setze

\[
\lambda_\Sigma:=1+\kappa+\beta_T.
\]

Aus \(R6+R7\) folgt

\[
0=
\lambda_\Sigma S_T
+2\beta_0y(u)
+(\beta_-+\beta_+)S_A
+\beta_bS_D
+pS_{WA}
+rS_{We}.
\tag{IMG3.10}
\]

Addiert man IMG3.1, verschwindet der gesamte \(p\)-Annulus-Summenkanal exakt.

Die verbleibende Gleichung ist

\[
\boxed{
\begin{aligned}
0={}&
A_TS_T
+A_AS_A
+A_0y(u)
+\beta_bS_D\\
&+r(S_{We}-S_{WB})
-qW_{T,-}
-\mathbf1_{\{u<\sigma\}}qW_{T,+},
\end{aligned}}
\tag{IMG3.11}
\]

mit

\[
A_T=\beta_0+\lambda_\Sigma>0,
\]

\[
\boxed{
A_A
=
c_2+\beta_-+\beta_+
=
\frac{2^{1/4}}{16}\log2
>0,
}
\]

und

\[
\boxed{
A_0
=
1+2c_1+2\beta_0
=
1+\frac14\log2
>0.
}
\]

Die positiven Skalarkoeffizienten sind keine punktweise Positivitätsaussage über die Funktionen.

## 9. Gemeinsamer Orbitstencil

Relativ zum inneren Basispunkt \(u\) liegen die Horizonwerte unter anderem auf

\[
A_-:(f_1,Q,3,0),\qquad
A_+:(f_1,P,1,0),
\]

\[
B_-:(f_1,Q,2,1),\qquad
B_+:(f_1,P,2,1),
\]

\[
T_-:(f_2,Q,2,0),\qquad
T_+:(f_2,P,2,0),
\]

\[
D_-:(f_1,Q,2,0),\qquad
D_+:(f_1,P,2,0).
\]

Die zusätzlichen Annuluswerte \(w(e\pm u)\) erreichen relativ zu diesem speziellen inneren Anker Index \(4\); der kombinierte lokale Stencil besitzt daher

\[
\boxed{|n|\le4.}
\]

Dies ist kein Widerspruch zur range-3-IMG2-Darstellung: dort wird die Reichweite relativ zum jeweiligen Outputindex gemessen.

---

# Teil II — No-Go gegen naive B96-Column-Stabilität

## 10. Exakter Witness

Ein erster Versuch wollte die B96-Ausgangsatome direkt unter jedem Pullback auf einzelne B96-Eingangsatome abbilden.

Diese Annahme ist falsch.

Exakter Witness:

- Referenzchamber \(0\);
- B96-Atomindex \(3\);
- Ausgangslift \(2\);
- aktive Row \(R5\);
- FREE-Branch \(r_{3a}\);
- effektiver Pullback \((-1,0,3)\).

Der Quellatomradius ist exakt

\[
\frac27>0,
\]

und der transformierte Mittelpunkt liegt exakt auf einer B96-Wand.

Somit liegt diese Wand im Inneren des Bildarcs. Daher

\[
\boxed{
\text{B96 ist nicht atomweise invariant unter allen effektiven Pullbacks.}
}
\tag{IMG3.12}
\]

Ein Column-Schur-Test ist nur nach zusätzlicher Pullback-Verfeinerung zulässig. Dieser No-Go betrifft nur die naive B96-Column-Abkürzung.

---

# Teil III — Horizon-Horizon-Kontraktion

## 11. Der richtige Horizon-Basisraum

Erinnere

\[
\mathscr B_H^0
=
\bigoplus_{k=0}^2m_kL^2(\mathbb T_L).
\]

Für

\[
x=\theta+kL\in(0,T_0)
\]

schreibe

\[
\widetilde f(x):=f_k(\theta).
\]

Da die Liftmasken \(m_k\) den positiven Horizont a.e. disjunkt parametrisieren,

\[
\|f\|_{\mathscr B_H^0}^2
=
\int_0^{T_0}|\widetilde f(x)|^2\,dx.
\tag{IMG3.13}
\]

Definiere

\[
\boxed{
(Vf)(x)
=
\frac1{\sqrt2}\widetilde f(|x|),
\qquad
|x|<T_0.
}
\tag{IMG3.14}
\]

Dann ist

\[
\boxed{
V:\mathscr B_H^0\to\mathscr H_+
\text{ unitär}.
}
\tag{IMG3.15}
\]

## 12. Reconciliation mit IMG0

IMG0 rekonstruiert aus \(f\)

\[
y_f(x)=\sqrt2\,\widetilde f(x)
\]

auf der positiven Halbachse und erweitert gerade. Mit IMG3.14 gilt

\[
\boxed{y_f=2Vf.}
\tag{IMG3.16}
\]

Sei

\[
\mathscr T:=I+A
\]

der physische FREE-Horizon-Operator.

Der P0-Basisoutput ist nach IMG.6

\[
\frac1{\sqrt2}(\mathscr T y_f)(x).
\]

Für gerades \(h\in\mathscr H_+\) gilt

\[
(V^*h)(x)=\sqrt2\,h(x)
\]

in positiven Liftkoordinaten. Damit ist der Horizon-Horizon-Block von \(\mathscr N_R\), erweitert von \(\mathscr B_K\) auf \(\mathscr B_H^0\),

\[
\boxed{
\mathscr T_B
=
V^*\mathscr TV.
}
\tag{IMG3.17}
\]

## 13. Selbstadjungiertheit

Da

\[
\mathscr T=I+A,
\qquad
A=R_{T_0}^*R_{T_0}\ge0,
\]

ist \(\mathscr T\) beschränkt und selbstadjungiert. Aus IMG3.17 folgt

\[
\boxed{
\mathscr T_B
\text{ ist beschränkt, selbstadjungiert und positiv}.
}
\tag{IMG3.18}
\]

Dies ist der entscheidende Grund, warum kein Column-B96-Ledger benötigt wird.

## 14. Diagonal-/Restzerlegung

IMG2 liefert den Multiplikationsoperator \(D_R\) aus dem einzigen Identitätspullback. Schreibe

\[
\boxed{
\mathscr T_B
=
D_R+\mathcal R_R.
}
\tag{IMG3.19}
\]

Weil \(D_R\) reell und diagonal ist,

\[
D_R=D_R^*.
\]

Mit IMG3.18 folgt

\[
\boxed{
\mathcal R_R=\mathcal R_R^*.
}
\tag{IMG3.20}
\]

## 15. Exakte Row-Absolutsummen

Für einen aktiven Rowtyp sei \(d_{\rm row}\) der Identitätskoeffizient und \(s_{\rm row}\) die Summe der Absolutbeträge sämtlicher nichtidentischer FREE-Koeffizienten dieser Row.

\[
\begin{array}{c|c|c}
\text{Row}&d_{\rm row}&s_{\rm row}\\
\hline
R0&1+2c_1&2c_2+2|\beta_0|\\
R1&1+c_1&c_1+c_2\\
R2,R3&1+\alpha_A&c_1+|\beta_-|+\beta_++c_2\\
R4I&1+\alpha_A&c_1+|\beta_-|+c_2\\
R5&1+\alpha_b&c_1+|\beta_-|+c_2+|\beta_b|\\
R6,R7&1+\kappa&|\beta_0|+|\beta_-|+|\beta_T|+\beta_++|\beta_b|.
\end{array}
\tag{IMG3.21}
\]

Definiere

\[
q_*
:=
\max_{\rm aktive\ Rows}
\frac{s_{\rm row}}{d_{\rm row}}.
\]

Das Maximum liegt exakt bei \(R6/R7\):

\[
\boxed{
q_*
=
\frac{
|\beta_0|+|\beta_-|+|\beta_T|+\beta_++|\beta_b|
}{
1+\kappa
}.
}
\tag{IMG3.22}
\]

Die numerische Ausgabe

\[
q_*\approx0.7675127831577783
\]

dient nur der Orientierung. Der Beweis verwendet stattdessen

\[
\boxed{
q_*<\frac{96}{125}.
}
\tag{IMG3.23}
\]

## 16. Elementare exakte Schranken

Das Zertifikat verwendet die atanh-Reihen

\[
\log2
=
2\sum_{n\ge0}
\frac{(1/3)^{2n+1}}{2n+1},
\]

\[
\log3
=
2\sum_{n\ge0}
\frac{(1/2)^{2n+1}}{2n+1},
\]

mit positivem geometrisch majorisiertem Rest. Daraus werden exakt

\[
\frac{56}{81}
<
\log2
<
\frac{1123}{1620},
\]

\[
\frac{263}{240}
<
\log3
<
\frac{923}{840}
\]

zertifiziert.

Ferner per ganzzahligem Potenzvergleich:

\[
\frac75<\sqrt2<\frac{577}{408},
\]

\[
2^{1/4}<\frac{11893}{10000},
\]

\[
\sqrt3<\frac{1351}{780},
\]

\[
2^{3/4}<\frac{8409}{5000}.
\]

Damit wird IMG3.23 vollständig rational nachgewiesen.

## 17. Minimaler und maximaler Diagonalwert

Aus den positiven arithmetischen Koeffizienten folgt

\[
\boxed{d_{\min}=1+c_1,}
\tag{IMG3.24}
\]

\[
\boxed{d_{\max}=1+\kappa.}
\tag{IMG3.25}
\]

Das Zertifikat beweist ferner

\[
\boxed{
\sqrt{\frac{d_{\max}}{d_{\min}}}
<
\frac{251}{200}.
}
\tag{IMG3.26}
\]

---

# Teil IV — Analytischer Selbstadjungiertheits-/Quadratformschritt

## 18. Symmetrische Graphmaß-Darstellung

Die A1-FREE-Rows sind endliche Summen von Restriktionen, Nullfortsetzungen, Translationen und Reflexionen mit Jacobi-Betrag \(1\) und reellen konstanten Koeffizienten.

Daher besitzt \(\mathcal R_R\) auf dem positiven Liftmodell eine endliche signierte Graphmaß-Darstellung \(\nu\) auf dem Produkt des Basisraums mit sich selbst:

\[
\langle\mathcal R_Rf,g\rangle
=
\int f(y)\overline{g(x)}\,d\nu(x,y).
\tag{IMG3.27}
\]

Nach Zusammenfassung identischer Graphstücke und wegen

\[
\mathcal R_R=\mathcal R_R^*
\]

ist dieses Graphmaß hermitesch symmetrisch; bei den hier reellen Koeffizienten symmetrisch.

Sei \(|\nu|\) seine Totalvariation. Die Symmetrie bleibt unter Totalvariation erhalten.

## 19. Row-Totalvariation

Sei \(s(x)\) die Rowmasse von \(|\nu|\). Die explizite A1-Rowdarstellung liefert a.e.

\[
s(x)\le s_{\operatorname{row}(x)}.
\]

Kollisionen oder Aggregation können die Totalvariation des zusammengefassten Kernels nur verkleinern, nie über die Summe der Absolutbeträge der Rohkoeffizienten hinaus vergrößern.

Mit IMG3.22–IMG3.23:

\[
\boxed{
s(x)
\le
q_*\,d_R(x)
\quad\text{a.e.}
}
\tag{IMG3.28}
\]

## 20. Quadratformlemma

Für \(f\in\mathscr B_H^0\):

\[
\begin{aligned}
|\langle\mathcal R_Rf,f\rangle|
&\le
\int |f(x)|\,|f(y)|\,d|\nu|(x,y)\\
&\le
\frac12
\int
\left(
|f(x)|^2+|f(y)|^2
\right)
d|\nu|(x,y).
\end{aligned}
\]

Wegen der Symmetrie von \(|\nu|\) sind die beiden Hälften gleich. Daher

\[
|\langle\mathcal R_Rf,f\rangle|
\le
\int s(x)|f(x)|^2dx.
\]

Mit IMG3.28 folgt

\[
\boxed{
|\langle\mathcal R_Rf,f\rangle|
\le
q_*
\langle D_Rf,f\rangle.
}
\tag{IMG3.29}
\]

## 21. Gewichtete Kontraktion

Definiere

\[
\boxed{
S_R
:=
D_R^{-1/2}
\mathcal R_R
D_R^{-1/2}.
}
\tag{IMG3.30}
\]

Da \(\mathcal R_R\) selbstadjungiert ist, ist auch \(S_R\) selbstadjungiert.

Setze \(g=D_R^{1/2}f\). Dann liefert IMG3.29

\[
|\langle S_Rg,g\rangle|
\le
q_*\|g\|^2.
\]

Für einen selbstadjungierten Operator ist die Norm das Supremum des Absolutbetrags der Quadratform auf der Einheitssphäre. Somit

\[
\boxed{
\|S_R\|
\le
q_*
<
\frac{96}{125}.
}
\tag{IMG3.31}
\]

## 22. Standard-\(L^2\)-Kontraktion

Setze

\[
\boxed{
K_R
:=
D_R^{-1}\mathcal R_R.
}
\tag{IMG3.32}
\]

Dann

\[
K_R
=
D_R^{-1/2}
S_R
D_R^{1/2}.
\]

Folglich

\[
\begin{aligned}
\|K_R\|
&\le
\|D_R^{-1/2}\|
\,
\|S_R\|
\,
\|D_R^{1/2}\|\\
&=
\sqrt{\frac{d_{\max}}{d_{\min}}}
\|S_R\|.
\end{aligned}
\]

Mit IMG3.23, IMG3.26 und IMG3.31:

\[
\boxed{
\|D_R^{-1}\mathcal R_R\|
<
\frac{96}{125}
\frac{251}{200}
=
\frac{3012}{3125}
<1.
}
\tag{IMG3.33}
\]

Dies ist der neue zentrale IMG3-Satzkandidat.

**Wichtig:** IMG3.33 ist ein unendlichdimensionaler \(L^2\)-Operatorsatz. Das Python-Zertifikat beweist die exakten Koeffizienten-/Rationalbounds; der Übergang über IMG3.15–IMG3.32 ist der separate analytische Beweis.

---

# Teil V — Kontrollierte Neumann-Transferdarstellung

## 23. Horizon-Inverses als konvergente Transferreihe

Aus

\[
\mathscr T_B
=
D_R+\mathcal R_R
=
D_R(I+K_R)
\]

und IMG3.33 folgt

\[
\boxed{
(I+K_R)^{-1}
=
\sum_{n=0}^{\infty}
(-K_R)^n
}
\tag{IMG3.34}
\]

in Operatornorm.

Also

\[
\boxed{
\mathscr T_B^{-1}
=
\sum_{n=0}^{\infty}
(-K_R)^nD_R^{-1}.
}
\tag{IMG3.35}
\]

Dies ist keine formale Reihe, sondern eine normkonvergente Operatorreihe.

Jeder Faktor \(K_R\) besteht aus den bereits zertifizierten endlichen FREE-Pullbacks. Die irrationale Orbitdynamik wird nicht endlich gemacht; Pfade beliebiger Länge werden stattdessen durch eine geometrisch konvergente Transferreihe kontrolliert.

## 24. Explizite Tail-Schranke

Setze

\[
\eta:=\frac{3012}{3125}.
\]

Dann

\[
\|K_R\|<\eta<1.
\]

Für

\[
P_N
:=
\sum_{n=0}^{N}
(-K_R)^nD_R^{-1}
\]

gilt

\[
\boxed{
\|\mathscr T_B^{-1}-P_N\|
\le
\frac{\eta^{N+1}}{1-\eta}
\|D_R^{-1}\|.
}
\tag{IMG3.36}
\]

Da IMG2 bereits \(\|D_R^{-1}\|<1\) liefert,

\[
\boxed{
\|\mathscr T_B^{-1}-P_N\|
<
\frac{\eta^{N+1}}{1-\eta}.
}
\tag{IMG3.37}
\]

Damit sind erstmals rigoros kontrollierte endliche Transfertrunkierungen des Horizon-Inversen möglich.

---

# Teil VI — Rückkehr zur eigentlichen Kernelbedingung

## 25. Keine \(\mathscr B_K\)-Invarianz nötig

Die IMG2-Firewall bleibt bestehen:

\[
D_R^{-1}\mathscr B_K
\subseteq\mathscr B_K
\]

ist nicht behauptet.

Ebenso wird nicht behauptet, dass

\[
K_R\mathscr B_K
\subseteq\mathscr B_K.
\]

Die Neumannreihe IMG3.35 wird auf dem vollständigen Horizon-Basisraum \(\mathscr B_H^0\) verstanden. Die KNF-Zulässigkeit wird erst anschließend als Descriptorbedingung auferlegt.

## 26. Annulus-only Neumann-Operator

Sei

\[
C_K:
\mathscr B_H^0
\to
L^2(0,R)
\]

der beschränkte KNF-Descriptoroperator und

\[
\mathscr B_K=\ker C_K.
\]

Sei ferner

\[
\mathcal H_R:
\mathscr B_W
\to
\mathscr B_H^0
\]

der HUB-Anteil von \(\mathscr N_R\).

Die Kernelgleichung lautet

\[
\mathscr T_Bf+\mathcal H_Rg=0,
\qquad
C_Kf=0.
\]

Aus IMG3.35:

\[
f
=
-\mathscr T_B^{-1}\mathcal H_Rg
=
-
\sum_{n=0}^{\infty}
(-K_R)^nD_R^{-1}\mathcal H_Rg.
\]

Definiere daher

\[
\boxed{
\mathscr A_R^{\rm Neu}
:=
C_K
\sum_{n=0}^{\infty}
(-K_R)^n
D_R^{-1}
\mathcal H_R.
}
\tag{IMG3.38}
\]

Die Reihe konvergiert in Operatornorm.

Dann gilt exakt:

\[
\boxed{
g\in\ker\mathscr A_R^{\rm Neu}
\iff
\left(
-\mathscr T_B^{-1}\mathcal H_Rg,\,
g
\right)
\in
\ker\mathscr N_R.
}
\tag{IMG3.39}
\]

Somit erhalten wir die Kernelbijektion

\[
\boxed{
\ker\mathscr A_R^{\rm Neu}
\cong
\ker\mathscr N_R.
}
\tag{IMG3.40}
\]

Dies ist inhaltlich dieselbe verbleibende Cross-Gram-/Schur-Frage wie A2, aber jetzt in einer expliziten normkonvergenten finite-range Transferdarstellung.

---

# Teil VII — Was damit wirklich neu ist

## 27. Geschlossener offener IMG2-Punkt als Kandidat

IMG2 führte ausdrücklich als offen:

\[
\|D_R^{-1}\mathcal R_R\|<1\ ?
\]

IMG3 liefert als Auditkandidat

\[
\boxed{
\|D_R^{-1}\mathcal R_R\|
<
\frac{3012}{3125}
<1.
}
\tag{IMG3.41}
\]

Damit wäre dieser einzelne IMG2-Restpunkt geschlossen, **sofern** der analytische Selbstadjungiertheits-/Graphmaßschritt unabhängig bestätigt wird.

## 28. Was weiterhin offen bleibt

Nicht bewiesen ist:

\[
\ker\mathscr A_R^{\rm Neu}=\{0\},
\]

äquivalent

\[
\ker\mathscr N_R=\{0\},
\]

äquivalent

\[
\ker\Gamma_I=\{0\}.
\]

Insbesondere folgt aus der Horizon-Kontraktion nicht, dass ein Annulusinput \(g\neq0\) unmöglich ist.

Die verbleibende Nichtentartungsfrage ist jetzt aber auf eine normkonvergente Transferreihe mit expliziter Tailkontrolle reduziert.

---

# Teil VIII — Zertifikate

## 29. Lokaler Eliminator

scripts/certify_sw1_m1_nd_img3_local_eliminator.py zertifiziert:

- inneren R0-Support;
- R6/R7-Support im \(u<R\)-Streifen;
- Sum-/Differenzformeln;
- KNF-Differenzrow;
- manifest positive DIFF-PIVOT-Determinante;
- Cramer-Rekonstruktion von \(D_T,D_A\);
- SUM-CANCEL;
- kombinierten Orbitstencil.

## 30. Horizon-Kontraktionskoeffizienten

scripts/certify_sw1_m1_nd_img3_horizon_contraction_coeffs.py zertifiziert:

- exakte Vorzeichen aller A1-Koeffizienten;
- acht aktive Row-Absolutsummen;
- R6/R7 als exaktes Maximum des Quotienten;
- rationale atanh-Schranken für \(\log2,\log3\);
- rationale Radikalschranken;
- \(q_*<96/125\);
- \(\sqrt{d_{\max}/d_{\min}}<251/200\);
- den endlichen Koeffizienten-Envelopenwert \(3012/3125<1\).

## 31. B96-Map-Stability-No-Go

scripts/certify_sw1_m1_nd_img3_b96_mapstability_nogo.py zertifiziert den exakten Witness gegen die naive Behauptung, B96 sei unter allen effektiven Pullbacks atomweise stabil.

Der frühere diagnostische Probeversuch scripts/probe_sw1_m1_nd_img3_schur_contraction.py ist gerade an diesem Witness gescheitert. Dieser rote Diagnoselauf wird nicht als negativer Befund gegen Horizon-Kontraktion interpretiert; er widerlegt nur die zu starke Atomstabilitätsannahme.

---

# 32. Scope-Firewall

Zulässig als IMG3-Auditkandidat:

\[
\boxed{
R0+\mathrm{KNF}+(R6,R7)
\text{ besitzt einen exakten lokalen DIFF-PIVOT.}
}
\]

\[
\boxed{
R0+(R6+R7)
\text{ eliminiert den }p\text{-Annulus-Summenkanal.}
}
\]

\[
\boxed{
\|D_R^{-1}\mathcal R_R\|
<
3012/3125
<1
}
\]

nach separater Bestätigung des analytischen Selbstadjungiertheits-/Graphmaßarguments.

\[
\boxed{
\mathscr T_B^{-1}
=
\sum_{n\ge0}
(-D_R^{-1}\mathcal R_R)^nD_R^{-1}
}
\]

in Operatornorm.

Nicht zulässig:

\[
\ker\mathscr N_R=\{0\},
\]

\[
\ker\Gamma_I=\{0\},
\]

eine Promotion zu \(\checkmark[M]\) ohne unabhängige Prüfung des analytischen Schritts, oder irgendeine Objekt-X-/RH-Folgerung.

---

# 33. Nächster mathematischer Gate

Der nächste sinnvolle Angriff ist nicht mehr „existiert überhaupt eine kontrollierte Rekurrenz?“.

Nach IMG3 lautet die konkrete Frage:

> Kann die Annulus-only Operatorreihe
> \[
> \mathscr A_R^{\rm Neu}
> =
> C_K
> \sum_{n\ge0}
> (-K_R)^n
> D_R^{-1}\mathcal H_R
> \]
> mit einer endlichen, rigoros tail-kontrollierten Trunkierung als bounded-below bzw. injektiv nachgewiesen werden?

Zwei mögliche Ausgänge:

1. **positive Route:** eine endliche Trunkierung besitzt eine quantitative Untergrenze größer als die rigorose Tailnorm;
2. **negative Route:** ein echter nichttrivialer \(g\) überlebt sämtliche Transferordnungen und liefert einen admissiblen Kernelvektor.

Bis einer dieser beiden Ausgänge bewiesen ist, bleibt

\[
\boxed{
\mathrm{M1\!-\!ND}:\ ?[O].
}
\]
