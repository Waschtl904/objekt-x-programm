# X-C1-CONNECTED-CROSSING — a=387/1000: altes Mode-2-Crossing und positive Gamma-Rettung

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** Connected-3/8, Waxing-19/50 und Waxing-193/500 auf PR #137.  
**Scope:** gesamte Klasse
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad a=\frac{387}{1000}.
\]
Kein A1-Import, keine numerische Eigenwertannahme, keine dritte Momentbedingung.

## 0. Ergebnis

Der Punkt \(a=387/1000\) überschreitet die diagnostische Nullstelle der **alten**
skalarisierten Unterform mit dem konstanten Gamma-Anteil \(1/5\). Mit einer festen
rationalen Knotenreserve \(C=331/200\) gilt dort exakt
\[
\lambda^{\rm old}_2
=\frac32+\frac{2a}{5}-C
=-\frac1{5000}<0.
\]
Das ist ein echtes Crossing dieser Unterzerlegung, aber kein negativer Weil-Vektor.

Die bisher ausgelagerte positive Gammaenergie reicht bereits aus, das Crossing zu
reparieren. Auf allen inneren Abständen \(0<t\le2a=387/500\) gilt rigoros
\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}
>\frac1{2t}+\frac{43}{200}.
\]
Mit demselben Knotenbudget \(C=331/200\) werden die Diagonalkoeffizienten dadurch
\[
\lambda_1=-\frac{48859}{100000},\qquad
\lambda_2=\frac{1141}{100000}>0,
\]
und \(\lambda_n\ge\lambda_2\) für alle \(n\ge2\).

Die beiden tatsächlichen Mellinbedingungen kontrollieren weiterhin genau die beiden
negativen niedrigen Richtungen. Der zugehörige Rang-2-Defekt erfüllt
\[
\|B\|^2<\frac{331}{5705}<\frac3{50}<1.
\]
Damit ist die Binomialfaktorisierung \(S=(I-B^*B)^{1/2}\) vorwärts definiert und
\[
\boxed{
Q_W[u]\ge\frac{2687}{250100}\|u\|_2^2
>\frac1{100}\|u\|_2^2
\qquad(0\ne u\in\mathcal W_a).
}
\]

**Schluss:** Das erste Mode-2-Crossing der alten \(1/5\)-Unterform ist keine
Notwendigkeit für C15. Es markiert nur, dass diese Unterform zu viel positive
Gammaenergie ausgelagert hat. Am rationalen Punkt \(a=0.387\) genügt bereits eine
stärkere, unabhängig bewiesene Kerneluntergrenze.

## 1. Importierte exakte Kantenidentität

Setze
\[
I_a=(-a,a),\quad L=2a=\frac{387}{500},\quad
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\]
\[
\kappa_*=\log(8\pi)+\gamma+\frac\pi2,\quad
t_2=\log2,\quad w_2=\frac{\log2}{\sqrt2}.
\]
Da \(L<\log3\), ist im verbundenen Intervall nur Prime 2 aktiv.

Wie im Connected-Elternbeweis gilt auf NULLPOL exakt
\[
Q_W[u]
=
\int_{x<y\in I_a}h(y-x)|u(y)-u(x)|^2\,dx\,dy
+w_2\int_{-a}^{a-t_2}|u(x+t_2)-u(x)|^2\,dx
+\int_{I_a}\rho_a(x)|u(x)|^2\,dx,
\]
mit
\[
H(s)=\int_s^\infty h(t)\,dt,\qquad
W_a(x)=H(a+x)+H(a-x),
\]
\[
d_P(x)=w_2\{\mathbf1_{I_a}(x-t_2)+\mathbf1_{I_a}(x+t_2)\},
\qquad
\rho_a=W_a-\kappa_*-d_P.
\]

Keine innere Zellgrenze wird eingeführt; die komplette Gamma-Nahtenergie bleibt in
der verbundenen Form.

## 2. Knotenreserve bei a=387/1000

Wir wählen
\[
C=\frac{331}{200}=1.655.
\]

### 2.1 Zentrum

Die beigefügte rationale Intervallrechnung benutzt nur `Fraction`-Arithmetik in allen
beweisrelevanten Vergleichen. Aus rational eingeschlossenen Reihen für
\[
H(s)=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2}),
\]
\(\pi\), Euler-\(\gamma\) und Logarithmen folgt
\[
2H(a)-\kappa_*>-\frac{331}{200}. \tag{X1}
\]

### 2.2 Prime-2-Endbänder

Auf den aktiven Endbändern ist \(|x|\ge t_2-a\). Dort ist die zusätzliche äußere
Gamma-Leckage minimal bei
\[
H(2a-t_2)+H(t_2)-2H(a).
\]
Die rationale Intervallrechnung liefert
\[
H(2a-t_2)+H(t_2)-2H(a)>\frac{99}{200}, \tag{X2}
\]
während
\[
w_2<\frac{491}{1000}<\frac{99}{200}. \tag{X3}
\]
Daher kompensiert die zusätzliche Leckage den Prime-2-Knotengrad vollständig. Aus
(X1)--(X3) folgt
\[
\boxed{\rho_a(x)>-\frac{331}{200}\quad\text{für fast alle }x\in I_a.} \tag{X4}
\]
Also ist
\[
V_a(x):=\rho_a(x)+\frac{331}{200}>0.
\]

## 3. Das alte Crossing ist exakt

Wenn man wie bisher nur
\[
h(t)>\frac1{2t}+\frac15
\]
im Hauptblock behält, ergibt die Legendre-Diagonalisierung
\[
\lambda^{\rm old}_n
=
\mathsf H_n+\frac{2a}{5}\mathbf1_{n\ge1}-C.
\]
Für \(n=2\) gilt exakt
\[
\lambda^{\rm old}_2
=
\frac32+\frac{387}{2500}-\frac{331}{200}
=-\frac1{5000}<0. \tag{X5}
\]

Damit ist die im Audit prognostizierte Schwellenüberschreitung für **diese**
skalarisierte Unterform tatsächlich eingetreten. (X5) ist keine Aussage über den
Index der vollständigen Weil-Form.

## 4. Mehr vorhandene Gammaenergie im Hauptblock

Wir beweisen auf dem gesamten relevanten Abstand
\[
\boxed{
h(t)>\frac1{2t}+\frac{43}{200},
\qquad 0<t\le L=\frac{387}{500}.
} \tag{X6}
\]

Die Ungleichung ist äquivalent zu
\[
e^{t/2}>
\left(1+\frac{43}{100}t\right)\frac{\sinh t}{t}.
\]
Für \(0\le t\le L\) gilt
\[
\frac{\sinh t}{t}\le1+b t^2,\qquad
b=\frac1{6(1-L^2/20)}
=\frac{2500000}{14550693},
\]
weil ab dem \(t^2/6\)-Term das Verhältnis aufeinanderfolgender positiver Terme
höchstens \(L^2/20\) ist. Zugleich
\[
e^{t/2}\ge1+\frac t2+\frac{t^2}{8}+\frac{t^3}{48}.
\]
Die Differenz der rechten Majorante von \((1+43t/100)\sinh(t)/t\) und dieser
Exponential-Untergrenze hat nach Ausklammern von \(t\) die Form
\[
q(t)=\frac7{100}
-\frac{5449307}{116405544}t
-\frac{12349769}{232811088}t^2.
\]
Die beiden nichtkonstanten Koeffizienten sind negativ, also ist \(q\) auf
\([0,L]\) fallend. Am rechten Rand gilt exakt
\[
q(L)=
\frac{38566559213}{19400924000000}>0.
\]
Damit ist (X6) bewiesen.

Setze
\[
r_*(t)=h(t)-\frac1{2t}-\frac{43}{200}>0.
\]
Der \(r_*\)-Anteil bleibt als eigener positiver Kantenoutput erhalten.

## 5. Neue Legendre-Bilanz

Für die normierte Legendrebasis \(e_n\) auf \(I_a\) gilt wie im Elternbeweis
\[
\int_{x<y}\frac{|u(y)-u(x)|^2}{2(y-x)}\,dx\,dy
=\sum_{n\ge0}\mathsf H_n|u_n|^2.
\]
Der konstante Kernel \(43/200\) trägt
\[
\frac{43}{200}
\int_{x<y}|u(y)-u(x)|^2\,dx\,dy
=
\frac{43}{200}(2a)\sum_{n\ge1}|u_n|^2.
\]
Mit der Knotenzerlegung \(V_a-C\) folgt
\[
Q_W[u]
=
\|D_Iu\|_{\nu_*}^2+\|u\|_{L^2(V_a dx)}^2
+\sum_{n\ge2}\lambda_n|u_n|^2
-C|u_0|^2+\lambda_1|u_1|^2,
\]
wobei
\[
\lambda_n=\mathsf H_n+\frac{43}{200}(2a)-C,\qquad n\ge1.
\]
Somit exakt
\[
\lambda_1
=
1+\frac{43}{200}\frac{387}{500}-\frac{331}{200}
=
-\frac{48859}{100000}, \tag{X7}
\]
\[
\lambda_2
=
\frac32+\frac{43}{200}\frac{387}{500}-\frac{331}{200}
=
\frac{1141}{100000}>0. \tag{X8}
\]
Da \(\mathsf H_n\) wächst, gilt \(\lambda_n\ge\lambda_2\) für \(n\ge2\). Außerdem
\[
\lambda_3-\lambda_2=\frac13.
\]

## 6. Die zwei Mellinmomente reichen weiterhin

Mit
\[
c(x)=\cosh(x/2),\qquad s(x)=\sinh(x/2)
\]
und ihren Legendrekoeffizienten \(c_n,s_n\) sind die zwei NULLPOL-Bedingungen
\[
u_0=-c_0^{-1}\sum_{n\ge2}c_nu_n,\qquad
u_1=-s_1^{-1}\sum_{n\ge2}s_nu_n.
\]
Für \(z=a/2=387/2000\) bleiben die früheren rationalen Taylorbudgets gültig:
\[
\frac{\|c_\perp\|}{c_0}<\frac1{50},\qquad
\frac{\|s_\perp\|}{s_1}<\frac1{150}. \tag{X9}
\]

Setze \(z_n=\sqrt{\lambda_n}u_n\), \(n\ge2\), und definiere denselben
Rang-2-Defektoperator mit den neuen Gewichten:
\[
Bz=
\begin{pmatrix}
\displaystyle\frac{\sqrt C}{c_0}\sum_{n\ge2}\frac{c_n}{\sqrt{\lambda_n}}z_n\\[2mm]
\displaystyle\frac{\sqrt{-\lambda_1}}{s_1}\sum_{n\ge2}\frac{s_n}{\sqrt{\lambda_n}}z_n
\end{pmatrix}.
\]
Aus (X8)--(X9) folgt
\[
\|B\|^2
<
\max\left\{
\frac{C}{\lambda_2}\frac1{2500},
\frac{-\lambda_1}{\lambda_2}\frac1{22500}
\right\}
=
\max\left\{
\frac{331}{5705},
\frac{48859}{25672500}
\right\}
=
\frac{331}{5705}
<\frac3{50}. \tag{X10}
\]

Damit ist
\[
S=(I-B^*B)^{1/2}
\]
durch die normkonvergente Binomialreihe definiert, bevor die Zielidentität verwendet
wird.

## 7. Positiver Output und Gap

Der Output ist derselbe Typ wie im Connected-Elternbeweis:
\[
T_{\rm cross}u=(D_Iu,\ u,\ Sz(u))
\]
im Produkt aus
- dem positiven Kantenraum für \(r_*(t)\) plus Prime-2-Differenzkanten,
- \(L^2(I_a,V_a dx)\),
- \(\ell^2(n\ge2)\).

Direktes Ausmultiplizieren und die zwei Momentgleichungen liefern
\[
\|T_{\rm cross}u\|^2=Q_W[u].
\]
Weiter
\[
\|u\|^2\le\left(1+\frac1{2500}\right)\sum_{n\ge2}|u_n|^2
\]
und daher
\[
Q_W[u]
\ge
\frac{\left(1-\frac{331}{5705}\right)\frac{1141}{100000}}
{1+\frac1{2500}}\|u\|^2
=
\boxed{\frac{2687}{250100}\|u\|^2}
>
\frac1{100}\|u\|^2. \tag{X11}
\]

## 8. Bedeutung für C15

Dieser Gate prüft genau die im Audit verlangte Alternative:

1. **Crossing-Zertifikat:** Die alte \(1/5\)-Unterform hat \(\lambda_2=-1/5000\).
2. **Positive ausgelagerte Energie:** Ein zusätzlicher fester Anteil der bereits
   vorhandenen Gammaenergie kann rigoros in den Hauptblock zurückgenommen werden.
3. **Schur-Entscheidung:** Dadurch wird \(\lambda_2\) wieder positiv und der
   Rang-2-Defekt bleibt kontraktiv.

Also:
\[
\boxed{\text{Bei }a=387/1000\text{ ist C15 noch nicht erforderlich.}}
\]

Das widerlegt keine spätere Notwendigkeit von C15. Es zeigt nur, dass die erste
diagnostische Crossing-Schwelle der alten Unterform zu konservativ war.

Ein sinnvoller nächster Gate ist nun nicht eine weitere Folge winziger
Zwischenpunkte. Entweder maximiert man die global beweisbare konstante
Gamma-Unterreserve systematisch, oder man wählt einen neuen rationalen Punkt jenseits
der daraus entstehenden verbesserten Mode-2-Schwelle und wiederholt denselben
Crossing-Test.

## 9. Checks und Grenzen

Der beigefügte Standardbibliothek-Prüfer benutzt in allen PASS-Entscheidungen
`fractions.Fraction`. Er prüft:
- rationale Einschließungen für \(\log2,\pi,\gamma,H\);
- Zentrum und Prime-2-Endband;
- (X6) über den rationalen Polynomrand;
- altes negatives und neues positives \(\lambda_2\);
- Moment-Taylorbudgets;
- Defektnorm und Gap.

**22/22 Checks PASS.** Die endliche Checkliste ersetzt nicht den
unendlichdimensionalen Legendre-/Dichtebeweis aus dem importierten Connected-Elternsatz.

Keine Aussage über das volle Einheitsfenster, Prime 3, all-window NP-GAP, Objekt X
oder RH. Kein A1-Replay und keine Statuspromotion durch den Commit.
