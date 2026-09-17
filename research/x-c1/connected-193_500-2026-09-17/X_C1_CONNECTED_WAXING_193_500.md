# X-C1-CONNECTED-WAXING — rationaler Gate bei a=193/500

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** Connected-3/8 und Waxing-19/50 auf PR #137.  
**Scope:** gesamte Klasse
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad a=\frac{193}{500}.
\]
Kein A1-Import, keine numerische Eigenwertannahme und keine zusätzliche Momentbedingung.

## 0. Ergebnis

Für \(a=193/500\) bleibt die bisherige globale Connected-Faktorisierung der skalarisierten Unterform noch im Zwei-Moden-Regime. Es gibt eine vorwärts definierte positive Auswertung mit
\[
\boxed{
Q_W[u]\ge \frac{1193}{5002000}\|u\|_2^2
>\frac1{5000}\|u\|_2^2
\qquad (u\ne0,\ u\in\mathcal W_a).
}
\]

Die Prime-2-Korrelation ist aktiv. Prime 3 ist noch inaktiv, da \(2a=193/250<\log3\).

Der Beweis verwendet dieselbe unzerlegte regionale Gamma-Differenzenergie und genau die zwei globalen Mellinmomente wie der Elternnachweis. Neu geschlossen werden drei knappe Delta-Punkte:

1. globale Knotenreserve \(\rho_a(x)>-3307/2000\);
2. zusätzliche äußere Gamma-Leckage auf den Prime-2-Endbändern ist \(>1/2>w_2\);
3. die bisherigen Moment-Taylorbudgets \(1/50\) und \(1/150\) bleiben bei \(|x|/2\le193/1000\) gültig.

## 1. Ausgangsidentität

Setze
\[
I_a=(-a,a),\qquad h(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\qquad \kappa_*=\log(8\pi)+\gamma+\frac\pi2,
\]
\[
t_2=\log2,\qquad w_2=\frac{\log2}{\sqrt2},
\qquad H(s)=\int_s^\infty h(t)\,dt.
\]

Auf NULLPOL gilt wie im Connected-Elternnachweis
\[
Q_W[u]
=
\int_{x<y,\ x,y\in I_a} h(y-x)|u(y)-u(x)|^2\,dx\,dy
+
w_2\!\int_{-a}^{a-t_2}|u(x+t_2)-u(x)|^2dx
+
\int_{I_a}\rho_a(x)|u(x)|^2dx,
\]
mit
\[
\rho_a(x)=H(a+x)+H(a-x)-\kappa_*
-w_2\bigl(1_{I_a}(x-t_2)+1_{I_a}(x+t_2)\bigr).
\]

Für alle vorkommenden Abstände \(0<t\le2a<4/5\) behalten wir die bereits bewiesene Unterzerlegung
\[
h(t)>\frac1{2t}+\frac15.
\]
Der positive Restkernel und die Prime-Differenzenergie werden als positive Ausgänge beibehalten.

## 2. Rigorose rationale Einschließung der Knotenreserve

Die Schwierigkeit ist die knappe Reserve nahe dem Mode-2-Crossing. Deshalb werden \(H\), \(\pi\), \(\gamma\) und \(\log2\) im Begleitprüfer ausschließlich mit exakten Brüchen eingeschlossen.

### 2.1 Zentrum

Konvexität von \(H\) gibt
\[
H(a+x)+H(a-x)\ge2H(a).
\]

Für Euler-\(\gamma\) benutzen wir die klassische rationale Schranke
\[
\gamma<H_{200}-\log200-\frac1{401}.
\]
Der Logarithmus wird durch die positive atanh-Reihe mit rationalem Rest eingeschlossen. \(\pi\) wird durch Machins Formel
\[
\pi=16\arctan\frac15-4\arctan\frac1{239}
\]
mit alternierenden rationalen Reihen eingeschlossen.

Ebenso wird
\[
H(s)=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2})
\]
durch exakte rationale Intervalle berechnet; \(e^{-s/2}\) benutzt die alternierende Exponentialreihe.

Der resultierende exakte Intervallvergleich liefert
\[
\boxed{2H(a)-\kappa_*>-\frac{3307}{2000}.}
\tag{W1}
\]

### 2.2 Prime-2-Endbänder

Auf einem aktiven Endband gilt \(|x|\ge t_2-a\). Dort ist das Minimum der äußeren Gamma-Leckage
\[
W_a(t_2-a)=H(2a-t_2)+H(t_2).
\]

Die Funktion
\[
F(\ell)=H(2a-\ell)+H(\ell)
\]
ist im relevanten Bereich streng wachsend, denn
\[
F'(\ell)=h(2a-\ell)-h(\ell)>0.
\]

Der Prüfer beweist zunächst
\[
\log2>\frac{693}{1000}.
\]
Daher
\[
W_a(t_2-a)-2H(a)
>
H\!\left(2a-\frac{693}{1000}\right)
+
H\!\left(\frac{693}{1000}\right)
-2H(a)
>\frac12.
\tag{W2}
\]

Außerdem
\[
w_2<\frac12
\]
aus \(\log2<7/10\) und \(\sqrt2>7/5\).

Damit kompensiert die zusätzliche äußere Gamma-Leckage den Prime-2-Knotengrad vollständig. Zusammen mit (W1) folgt fast überall
\[
\boxed{\rho_a(x)>-\frac{3307}{2000}.}
\tag{W3}
\]

Setze daher
\[
V_a(x)=\rho_a(x)+\frac{3307}{2000}>0.
\]

## 3. Globale Gamma-Diagonalisierung bleibt unverändert

Die singuläre regionale Energie
\[
\mathcal E_0[u]
=
\int_{x<y\in I_a}\frac{|u(y)-u(x)|^2}{2(y-x)}\,dx\,dy
\]
wird auf der normierten Legendrebasis des **gesamten Intervalls** diagonalisiert:
\[
\mathcal E_0[u]=\sum_{n\ge0}\mathsf H_n|u_n|^2.
\]

Der konstante Anteil \(1/5\) der Gamma-Unterform ergibt
\[
\frac15\int_{x<y}|u(y)-u(x)|^2dxdy
=
\frac{2a}{5}\sum_{n\ge1}|u_n|^2.
\]

Nach Abzug der konservativen Konstante \(3307/2000\) besitzt der modale Rest daher
\[
\lambda_0=-\frac{3307}{2000},
\]
und für \(n\ge1\)
\[
\lambda_n=\mathsf H_n+\frac{2a}{5}-\frac{3307}{2000}.
\]

Am neuen Endpunkt folgt exakt
\[
\boxed{\lambda_1=-\frac{4991}{10000},\qquad \lambda_2=\frac9{10000}>0.}
\tag{W4}
\]
Da die harmonischen Zahlen wachsen,
\[
\lambda_n\ge\lambda_2=\frac9{10000}\qquad(n\ge2).
\]

Somit besitzt **diese konkret skalarisierte Unterform** weiterhin nur zwei negative Moden.

## 4. Die zwei Mellinmomente kontrollieren weiterhin genau diese zwei Moden

Setze
\[
c(x)=\cosh(x/2),\qquad s(x)=\sinh(x/2).
\]
NULLPOL ist äquivalent zu
\[
\langle u,c\rangle=\langle u,s\rangle=0.
\]

Wie im Elternbeweis werden \(u_0\) und \(u_1\) dadurch aus den höheren Legendrekoeffizienten rekonstruiert.

Für
\[
z=\frac a2=\frac{193}{1000}
\]
liefern die positiven Taylorreihen rigoros
\[
\cosh z-1\le\frac{z^2}{2(1-z^2/12)}<\frac1{50},
\]
\[
\frac{\sinh z}{z}-1\le\frac{z^2}{6(1-z^2/20)}<\frac1{150}.
\]
Daher bleiben
\[
\frac{\|c_\perp\|}{c_0}<\frac1{50},\qquad
\frac{\|s_\perp\|}{s_1}<\frac1{150}.
\tag{W5}
\]

Für \(n\ge2\) setze \(z_n=\sqrt{\lambda_n}\,u_n\). Der Rang-zwei-Defektoperator \(B\) wird wie zuvor aus den beiden Momentzeilen definiert. Mit \(\lambda_n\ge9/10000\) folgt
\[
\|B\|^2<\max\left\{
\frac{3307}{2000}\frac{10000}{9}\frac1{50^2},
\frac{4991}{10000}\frac{10000}{9}\frac1{150^2}
\right\}.
\]

Der erste Term dominiert und ist exakt
\[
\boxed{\|B\|^2<\frac{3307}{4500}<1.}
\tag{W6}
\]

Damit ist \(S=(I-B^*B)^{1/2}\) durch die normkonvergente Binomialreihe konstruiert, bevor die Weil-Identität verwendet wird.

## 5. Positiver Output und quantitativer Gap

Der Output ist derselbe strukturelle Connected-Output wie im Elternbeweis: positiver Restkanten-/Prime-Differenzport, positiver Knotenport \(L^2(I_a,V_a dx)\), höherer Legendreport \(Sz\).

Durch exakte Quadratbilanz gilt
\[
\|T_a u\|^2=Q_W[u]\qquad(u\in\mathcal W_a).
\]

Aus (W6), \(\lambda_n\ge9/10000\), und
\[
\|u\|^2\le\left(1+\frac1{2500}\right)\sum_{n\ge2}|u_n|^2
\]
folgt
\[
Q_W[u]\ge
\frac{(1-3307/4500)(9/10000)}{1+1/2500}\|u\|^2
=
\boxed{\frac{1193}{5002000}\|u\|^2>\frac1{5000}\|u\|^2.}
\tag{W7}
\]

Keine Matrixeigenwerte und keine vorausgesetzte Positivität gehen in die Konstruktion ein.

## 6. Bedeutung der nächsten Schwelle

Die Nullstelle der **skalarisierten** Mode-2-Funktion
\[
\lambda_2(a)=\frac32+\frac{2a}{5}+2H(a)-\kappa_*
\]
liegt numerisch nahe \(a\approx0.38694\).

Das ist eine Warnschwelle dieser Unterzerlegung, kein Weil-No-Go und kein allgemeiner C1-No-Go. Nach ihrem Überschreiten gibt es mindestens zwei zulässige Richtungen: mehr bereits vorhandene positive Gamma-/Knotenenergie in den Hauptblock aufnehmen; oder Mode 2 als echten Restfreiheitsgrad über die Form-Schur-Schnittstelle C15 oder eine äquivalente Konstruktion transportieren.

Insbesondere darf keine dritte künstliche NULLPOL-Bedingung eingeführt werden.

## 7. Checks und Status

Der Begleitprüfer `check_x_c1_connected_193_500.py` verwendet nur Python-Standardbibliothek und exakte Brüche. Er verifiziert insbesondere rationale Einschließungen von \(\log2\), \(\pi\), Euler-\(\gamma\) und \(H(s)\), (W1) und (W2), die exakten Modenwerte (W4), die Taylorbudgets (W5), \(\|B\|^2<3307/4500<1\), und den exakten Gap \(1193/5002000>1/5000\).

Die unendlichdimensionale Legendre- und Formidentität wird aus dem Elternbeweis importiert; der Checker ersetzt diesen analytischen Beweis nicht.

**Status:** `X-C1-CONNECTED-193/500 / AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

Kein Merge, keine Registry-Promotion, kein A1-/C0-Replay und kein Gesamtclaim für \((-1,1)\), Objekt X oder RH.
