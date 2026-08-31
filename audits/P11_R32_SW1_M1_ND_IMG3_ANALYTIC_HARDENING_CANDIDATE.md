# P11/R32 — SW1 M1-ND IMG3 Analytic Hardening Candidate

> **Stand:** 31. August 2026  
> **Branch:** research/sw1-m1-nd-img3-eliminator  
> **Status:** AI-GREEN candidate für den analytischen Horizon-Kontraktionsschritt; keine Promotion.  
> **Zweck:** die zwei nichtmechanischen Lücken des IMG3-Kontraktionsarguments explizit schließen:
> 1. exakte unitäre Identifikation des Horizon-Horizon-Blocks;
> 2. legitime Verwendung der Row-Totalvariation ohne unzulässige „kostenlose Symmetrisierung“.
>
> Zusätzlich wird ein neues No-Go für jede **feste** endliche Neumann-Trunkierungsordnung im gesamten offenen SW1-Scope formuliert.

---

## 1. Räume und Normierung

Setze

\[
\mathscr B_H^0
=
\bigoplus_{k=0}^2 m_kL^2(\mathbb T_L).
\]

Für fast jedes \(x\in(0,T_0)\) existiert eindeutig

\[
x=\theta+kL,
\qquad
k\in\{0,1,2\},
\qquad
\theta=[x]_L.
\]

Für \(f=(f_0,f_1,f_2)\in\mathscr B_H^0\) definiere

\[
\widetilde f(x):=f_k(\theta).
\]

Wegen der disjunkten Liftmasken gilt exakt

\[
\|f\|_{\mathscr B_H^0}^2
=
\int_0^{T_0}|\widetilde f(x)|^2\,dx.
\tag{H.1}
\]

Definiere

\[
(Vf)(x)
=
\frac1{\sqrt2}\widetilde f(|x|),
\qquad
|x|<T_0.
\tag{H.2}
\]

Dann ist \(Vf\) gerade und

\[
\|Vf\|_{\mathscr H_+}^2
=
2\int_0^{T_0}\frac12|\widetilde f(x)|^2dx
=
\|f\|_{\mathscr B_H^0}^2.
\]

Also

\[
\boxed{
V:\mathscr B_H^0\to\mathscr H_+
\text{ ist unitär}.
}
\tag{H.3}
\]

---

## 2. Abgleich mit IMG0

IMG0 liefert für den physisch rekonstruierten geraden Horizonwert

\[
y_f(x)
=
\sqrt2\,\widetilde f(x),
\qquad
x>0,
\]

mit gerader Fortsetzung. Daher

\[
\boxed{y_f=2Vf.}
\tag{H.4}
\]

Für einen geraden Output \(h\in\mathscr H_+\) lautet die P0-Basiskomponente des Horizoncovers

\[
(R_0^{\rm out}U_Hh)_k(\theta)
=
\frac1{\sqrt2}h(\theta+kL).
\tag{H.5}
\]

Aus H.2 folgt gleichzeitig

\[
(V^*h)_k(\theta)
=
\sqrt2\,h(\theta+kL).
\tag{H.6}
\]

Sei

\[
\mathscr T:=I+A
\]

der physische FREE-Horizon-Operator. Für Input \(f\) ist der physische Horizoninput \(y_f=2Vf\), also der physische FREE-Output

\[
\mathscr Ty_f
=
2\mathscr TVf.
\]

Nach H.5 wird daraus in P0-Basisliftkoordinaten

\[
\frac1{\sqrt2}(2\mathscr TVf)
=
\sqrt2\,\mathscr TVf
=
V^*\mathscr TVf.
\]

Damit ist der Horizon-Horizon-Block des effektiven Operators exakt

\[
\boxed{
\mathscr T_B
=
V^*\mathscr TV.
}
\tag{H.7}
\]

Es fehlt kein Faktor \(\sqrt2\), und es wird keine bloß formale Species-Äquivarianz benutzt.

---

## 3. Selbstadjungiertheit

A1/A2 definieren

\[
A=R_{T_0}^*R_{T_0}\ge0.
\]

Daher ist

\[
\mathscr T=I+A
\]

beschränkt, selbstadjungiert und positiv.

Aus der unitären Äquivalenz H.7 folgt

\[
\boxed{
\mathscr T_B
\text{ ist beschränkt, selbstadjungiert und positiv}.
}
\tag{H.8}
\]

IMG2 zerlegt

\[
\mathscr T_B
=
D_R+\mathcal R_R,
\tag{H.9}
\]

wobei \(D_R\) ein reeller diagonaler Multiplikationsoperator ist. Somit

\[
D_R=D_R^*
\]

und daher

\[
\boxed{
\mathcal R_R=\mathcal R_R^*.
}
\tag{H.10}
\]

---

## 4. Raw-Graphmaß ohne Symmetrisierungsabkürzung

Die A1-FREE-Rows bestehen aus endlich vielen partiellen Translationen und Reflexionen mit Jacobi-Betrag \(1\), Restriktionen/Nullfortsetzungen und reellen konstanten Koeffizienten.

Sei \(X=(0,T_0)\) mit Lebesguemaß. Nach positiver Liftidentifikation kann jede nichtidentische Raw-Kante in der Form

\[
(T_jf)(x)
=
c_j\,1_{E_j}(x)\,
f(\phi_j(x))
\]

geschrieben werden, wobei

- \(E_j\subset X\) messbar ist,
- \(c_j\in\mathbb R\),
- \(\phi_j:E_j\to X\) eine partielle Translation oder Reflexion mit Jacobi-Betrag \(1\) ist.

Definiere das endliche signierte Maß

\[
\nu_0
=
\sum_j
c_j\,
(x\mapsto(x,\phi_j(x)))_\#
(1_{E_j}(x)\,dx).
\tag{H.11}
\]

Dann gilt für beschränkte einfache \(f,g\), und daher per Dichte auf \(L^2\),

\[
\langle\mathcal R_Rf,g\rangle
=
\int_{X\times X}
f(y)\overline{g(x)}
\,d\nu_0(x,y).
\tag{H.12}
\]

Wichtig: Es wird **nicht** behauptet, dass eine beliebige Raw-Darstellung kostenfrei symmetrisiert werden dürfe.

---

## 5. Warum das Raw-Maß selbst symmetrisch ist

Sei \(\tau(x,y)=(y,x)\) und

\[
\nu_0^\top:=\tau_\#\nu_0.
\]

Da die Koeffizienten reell sind, repräsentiert \(\nu_0^\top\) den Adjungierten \(\mathcal R_R^*\).

Wegen H.10 gilt

\[
\mathcal R_R=\mathcal R_R^*.
\]

Nehme messbare Rechtecke \(E\times F\subset X\times X\) und setze in H.12

\[
g=1_E,
\qquad
f=1_F.
\]

Dann folgt

\[
\nu_0(E\times F)
=
\nu_0^\top(E\times F)
\]

für alle messbaren Rechtecke.

Da beide endliche signierte Maße sind und messbare Rechtecke die Produktsigma-Algebra erzeugen, folgt aus der Eindeutigkeit endlicher signierter Maße

\[
\boxed{
\nu_0=\nu_0^\top.
}
\tag{H.13}
\]

Damit ist das **bereits aggregierte Raw-Graphmaß selbst symmetrisch**. Es ist keine nachträgliche Mittelung

\[
\frac12(\nu_0+\nu_0^\top)
\]

nötig, und daher entsteht auch keine zusätzliche Column-Masse.

Dies schließt die zentrale mögliche Lücke des ersten IMG3-Entwurfs.

---

## 6. Totalvariation und Row-Majorante

Aus H.13 folgt auch

\[
|\nu_0|
=
|\nu_0|^\top.
\tag{H.14}
\]

Die Row-Totalvariation sei

\[
s(x)
:=
\frac{d\,\pi_{1\#}|\nu_0|}{dx}(x),
\]

a.e. definiert.

Für einen festen \(x\) ist die Raw-Darstellung eine endliche Summe der aktiven A1-Offdiagonalkoeffizienten. Falls mehrere Graphkanten auf demselben \((x,y)\) aggregieren, gilt wegen der Dreiecksungleichung

\[
\text{Totalvariation nach Aggregation}
\le
\text{Summe der Raw-Absolutbeträge}.
\]

Daher

\[
s(x)
\le
s_{\operatorname{row}(x)}
\quad\text{a.e.}
\tag{H.15}
\]

Das exakte Koeffizientenzertifikat
scripts/certify_sw1_m1_nd_img3_horizon_contraction_coeffs.py
beweist

\[
s_{\rm row}
\le
q_*d_{\rm row}
\]

für jeden der acht aktiven Rowtypen, mit

\[
\boxed{
q_*<\frac{96}{125}.
}
\tag{H.16}
\]

Somit

\[
\boxed{
s(x)
\le
q_*d_R(x)
\quad\text{a.e.}
}
\tag{H.17}
\]

---

## 7. Quadratformabschätzung

Für \(f\in\mathscr B_H^0\) gilt

\[
\begin{aligned}
|\langle\mathcal R_Rf,f\rangle|
&\le
\int_{X\times X}
|f(x)|\,|f(y)|
\,d|\nu_0|(x,y)\\
&\le
\frac12
\int_{X\times X}
\left(
|f(x)|^2+|f(y)|^2
\right)
d|\nu_0|(x,y).
\end{aligned}
\]

Wegen H.14 stimmen die beiden Marginalintegrale überein. Daher

\[
|\langle\mathcal R_Rf,f\rangle|
\le
\int_X s(x)|f(x)|^2dx.
\]

Mit H.17:

\[
\boxed{
|\langle\mathcal R_Rf,f\rangle|
\le
q_*
\langle D_Rf,f\rangle.
}
\tag{H.18}
\]

---

## 8. Gewichtete und Standard-\(L^2\)-Kontraktion

Definiere

\[
S_R
=
D_R^{-1/2}
\mathcal R_R
D_R^{-1/2}.
\]

Dann ist \(S_R\) selbstadjungiert. Aus H.18 folgt

\[
\|S_R\|
\le
q_*
<
\frac{96}{125}.
\tag{H.19}
\]

Setze

\[
K_R
=
D_R^{-1}\mathcal R_R.
\]

Dann

\[
K_R
=
D_R^{-1/2}
S_R
D_R^{1/2}.
\]

Das Koeffizientenzertifikat beweist zusätzlich

\[
\sqrt{\frac{d_{\max}}{d_{\min}}}
<
\frac{251}{200}.
\tag{H.20}
\]

Somit

\[
\boxed{
\|K_R\|
<
\frac{96}{125}
\frac{251}{200}
=
\frac{3012}{3125}
<1.
}
\tag{H.21}
\]

Dies ist die gehärtete Form des IMG3-Horizon-Kontraktionssatzkandidaten.

---

## 9. Neumann-Inverses

Aus H.21 folgt auf \(\mathscr B_H^0\)

\[
\boxed{
\mathscr T_B^{-1}
=
\sum_{n=0}^\infty
(-K_R)^nD_R^{-1}
}
\tag{H.22}
\]

in Operatornorm.

Mit

\[
\eta=\frac{3012}{3125}
\]

gilt für die Trunkierung

\[
P_N
=
\sum_{n=0}^N
(-K_R)^nD_R^{-1}
\]

die Tail-Schranke

\[
\boxed{
\|\mathscr T_B^{-1}-P_N\|
\le
\frac{\eta^{N+1}}{1-\eta}
\|D_R^{-1}\|.
}
\tag{H.23}
\]

---

# Teil II — Annulus-Sichtbarkeit

## 10. Exakter \(N=0\)-Term

Setze

\[
\mathscr A_0
=
C_KD_R^{-1}\mathcal H_R.
\]

Für \(0<u<R\) liegen die sechs KNF-Samplepunkte in den festen Rows

\[
a-u:R2,\quad
a+u:R3,\quad
b\pm u:R5,\quad
T-u:R6,\quad
T+u:R7.
\]

Daher sind die entsprechenden Diagonalwerte

\[
d_A=1+\alpha_A,
\quad
d_B=1+\alpha_b,
\quad
d_T=1+\kappa.
\]

Direkte Komposition mit der Hubformel ergibt

\[
\boxed{
\begin{aligned}
(\mathscr A_0w)(u)
={}&
C_d[w(d-u)-w(d+u)]\\
&+
C_a[w(a-u)-w(a+u)]\\
&+
C_e[w(e-u)-w(e+u)]\\
&-
C_T[
w(T-u)-1_{\{u<\sigma\}}w(T+u)
],
\end{aligned}}
\tag{H.24}
\]

mit

\[
C_d
=
pr\left(\frac1{d_A}+\frac1{d_B}\right)>0,
\]

\[
C_a
=
pq\left(\frac1{d_A}+\frac1{d_T}\right)>0,
\]

\[
C_e
=
rq\left(\frac1{d_B}+\frac1{d_T}\right)>0,
\]

\[
C_T
=
\frac{p^2}{d_A}>0.
\]

Das Zertifikat
scripts/certify_sw1_m1_nd_img3_n0_annulus_blindset.py
prüft H.24 exakt.

---

## 11. \(N=0\)-Blindbereich

Die sichtbare Annulusmenge von H.24 liegt in

\[
(e-R,e+R)
\cup
(d-R,d+R)
\cup
(a-R,a+R)
\cup
(T-R,T+\sigma).
\tag{H.25}
\]

Auf SW1 gilt

\[
R+\varepsilon<\Delta,
\qquad
R<\varepsilon,
\]

also

\[
2R<\Delta.
\]

Ferner ist aus dem bereits auditierten Konstantensatz

\[
e>2\Delta.
\]

Daher sind die vier offenen Intervalle

\[
(R,e-R),
\]

\[
(e+R,d-R),
\]

\[
(d+R,a-R),
\]

\[
(a+R,T-R)
\]

nichtleer.

Somit enthält

\[
\ker\mathscr A_0
\]

den gesamten \(L^2\)-Raum des positiven Blindbereichs und ist insbesondere unendlichdimensional.

Also

\[
\boxed{
\mathscr A_0
\text{ ist niemals injektiv auf SW1}.
}
\tag{H.26}
\]

Dies ist nur ein No-Go für Ordnung \(0\).

---

## 12. No-Go für jede feste Trunkierungsordnung über dem gesamten SW1-Scope

Definiere

\[
\mathscr A_N
=
C_K
\sum_{n=0}^{N}
(-K_R)^n
D_R^{-1}
\mathcal H_R.
\tag{H.27}
\]

Für eine reine Raw-Pfadzählung gilt:

- \(C_K\) besitzt höchstens \(6\) Samplebranches;
- jede Offdiagonal-FREE-Row von \(\mathcal R_R\) besitzt höchstens \(5\) Sourcebranches;
- \(\mathcal H_R\) besitzt höchstens \(6\) Annulusbranches;
- \(D_R^{-1}\) erzeugt keine neue Abtastmap.

Daher besitzt Ordnung \(n\) höchstens

\[
36\cdot5^n
\]

Raw-Affine-Samplemaps.

Die gesamte Trunkierung \(0,\dots,N\) besitzt höchstens

\[
\boxed{
M_N
=
36\sum_{n=0}^{N}5^n
=
9(5^{N+1}-1)
}
\tag{H.28}
\]

solche Maps.

Jede dieser Maps ist bezüglich des inneren Parameters \(u\in(0,R)\) von der Form

\[
t=\pm u+c
\]

und sieht daher eine Annulusmenge von Länge höchstens \(R\).

Gates und zusätzliche Zellzerlegungen können die sichtbare Menge nur verkleinern; sie erzeugen keinen neuen affine Samplemap.

Somit

\[
\boxed{
|\operatorname{Vis}(\mathscr A_N)|
\le
M_NR.
}
\tag{H.29}
\]

---

## 13. Explizite SW1-Witnessparameter für jedes feste \(N\)

Für festes \(N\) setze \(M=M_N\) und

\[
R_N
=
\frac{\Delta T}
{10(M+1)(T+\Delta)},
\]

\[
\sigma_N=\frac{R_N}{2},
\qquad
\varepsilon_N=2R_N.
\]

Dann gilt exakt

\[
0<\sigma_N<R_N<\varepsilon_N
\]

und

\[
R_N+\varepsilon_N
=
3R_N
<
\Delta.
\]

Also ist dies ein zulässiger SW1-Punkt.

Ferner

\[
M R_N
<
T-R_N
<
T+\sigma_N-R_N
=
S_N-R_N.
\]

Mit H.29 besitzt die sichtbare Menge von \(\mathscr A_N\) strikt kleinere Maßlänge als der Annulus.

Daher existiert ein Blindset positiver Maßlänge und

\[
\boxed{
\ker\mathscr A_N
\text{ ist unendlichdimensional}
}
\tag{H.30}
\]

für diesen SW1-Punkt.

Somit:

\[
\boxed{
\text{Für kein festes }N
\text{ ist }\mathscr A_N
\text{ uniform injektiv/bounded-below auf ganz SW1}.
}
\tag{H.31}
\]

Das Zertifikat
scripts/certify_sw1_m1_nd_img3_fixedN_uniform_nogo.py
prüft die Pfadzahl und die expliziten Witness-Ungleichungen.

---

## 14. Konsequenz für die Strategie

Der im ersten IMG3-Entwurf formulierte mögliche nächste Schritt

> „Finde ein festes \(N\), so dass eine endliche Trunkierung eine Untergrenze besitzt, die größer als die uniforme Tailnorm ist“

kann **nicht** auf dem gesamten offenen SW1-Scope funktionieren.

Zulässig bleiben zwei Routen:

1. **parameteradaptive Route**
   \[
   N=N(R,\sigma,\varepsilon),
   \]
   wobei die notwendige Transferordnung für kleine \(R\) wachsen darf;

2. **direkte infinite-order Route**, welche die volle normkonvergente Neumannreihe und die irrationale Wiederkehr gemeinsam ausnutzt.

Die Horizon-Kontraktion H.21 ist mit diesem No-Go vollständig kompatibel.

---

## 15. Status

Als analytischer Kandidat ist nun gerechtfertigt:

\[
\boxed{
\|D_R^{-1}\mathcal R_R\|
<
3012/3125
<1.
}
\]

Dies beruht auf:

- der exakten unitären Identifikation H.7;
- der Selbstadjungiertheit H.10;
- der Maß-Eindeutigkeit H.13 statt einer unzulässigen Symmetrisierungsabkürzung;
- den exakten rationalen Koeffizientenbounds aus dem committed Certificate.

Noch **nicht** bewiesen ist

\[
\ker\mathscr A_R^{\rm Neu}=\{0\},
\]

also weiterhin nicht

\[
\ker\mathscr N_R=\{0\}.
\]

Der neue negative Strategiebefund lautet:

\[
\boxed{
\text{kein fixes endliches Neumann-}N
\text{ kann ganz SW1 uniform schließen.}
}
\]

Damit ist der nächste echte Gate präzisiert zu:

\[
\boxed{
\text{parameteradaptive Observabilität}
+
\text{quantitative Tailkontrolle}
}
\]

oder einer direkten infinite-order Unique-Continuation-Methode.
