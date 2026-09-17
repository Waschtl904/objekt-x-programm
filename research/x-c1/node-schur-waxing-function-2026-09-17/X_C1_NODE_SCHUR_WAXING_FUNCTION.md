# X-C1 NODE-SCHUR-WAXING — korrigierter optimierter Knotensplit im Prime-2-only-Bereich

**Datum:** 17. September 2026  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Elternstand:** Connected-Faktorisierung, analytische Gamma-Waxing-Funktion und Rest-Schur-Gate `a=49/125` auf PR #137.  
**Scope:** Prime-2-only-Bereich `log(2)/2 < a < log(3)/2`; keine Aussage jenseits des Eintritts von Prime 3.

## 0. Korrigiertes Ergebnis

Setze
\[
\ell=\log2,\qquad w=\frac{\ell}{\sqrt2},\qquad
H(s)=\int_s^\infty h(t)\,dt,
\]
\[
C(a)=\kappa_*+w-H(2a-\ell)-H(\ell),
\]
\[
m(a)=H\!\left(a+\frac\ell2\right)+H\!\left(a-\frac\ell2\right)-H(2a-\ell)-H(\ell),
\]
\[
z(a)=\frac{\ell}{2a},\qquad
p(a)=1-\frac94z^5+\frac52z^3-\frac54z,
\]
\[
\lambda_2(a)=1+2ah(2a)-C(a),\qquad
\delta(a)=\lambda_2(a)+\frac7{12}.
\]

Für \(0<\theta<1\) folgt aus
\[
|A+B|^2\ge \theta|A|^2-\frac{\theta}{1-\theta}|B|^2
\]
der Knotenkopplungskoeffizient
\[
\mu(a,\theta)=\theta m(a).
\]

Der rohe unendlichdimensionale Schur-Pivot wird von unten kontrolliert durch
\[
S_{\rm node}(a,\theta)
=
\lambda_2(a)+\mu p\left(1-\frac{\mu}{\delta}\right).
\]

Nach Schur-Quadratvervollständigung ist
\[
\eta(a,\theta)
=
\frac{\min\{S_{\rm node}(a,\theta),\delta(a)\}}
     {(1+\mu(a,\theta)/\delta(a))^2}.
\]

Mit
\[
\beta_e(a)=
\left[
\frac{(a/2)^2}{2(1-(a/2)^2/12)}
\right]^2
\]
und
\[
K(a,\theta)
=
C(a)+\frac{\theta}{1-\theta}m(a)
\]
liefert die even-Momentbedingung
\[
|u_0|^2\le\beta_e(a)\|x\|^2.
\]

Aus
\[
q_{\rm even}[u]\ge
\eta(a,\theta)\|x\|^2-K(a,\theta)|u_0|^2
\]
und
\[
\|u_{\rm even}\|^2=\|x\|^2+|u_0|^2
\le(1+\beta_e(a))\|x\|^2
\]
folgt daher **nicht** die frühere Formel, sondern
\[
\boxed{
G_e^{\rm corr}(a,\theta)
=
\frac{\eta(a,\theta)-\beta_e(a)K(a,\theta)}
     {1+\beta_e(a)}.
}
\tag{N1-corr}
\]

Die Differenz zur früher committed Formel ist
\[
G_e^{\rm commit}-G_e^{\rm corr}
=
\frac{\beta_e\,\eta}{1+\beta_e}>0
\]
im positiven Bereich. Der frühere Ausdruck war daher geringfügig zu groß.

Trotz dieser Korrektur bleibt die lokale Crossing-Einschließung bestehen:
\[
\boxed{
0.3930108<a_{\rm node}^{\rm corr}<0.3930110.
}
\tag{N2-corr}
\]

Präzise:
- bei \(a=0.3930108\) gilt
  \[
  G_e^{\rm corr}(a,0.791438)>0;
  \]
- bei \(a=0.3930110\) liegt der eindeutige \(\theta\)-Maximierer in
  \[
  \boxed{0.791428<\theta_*<0.791429},
  \]
  und selbst auf diesem gesamten Bracket ist
  \[
  G_e^{\rm corr}<0;
  \]
- der Odd-Gap bleibt am oberen Endpunkt \(>1/4\).

Der exakte Checker liefert für die gerichteten Außenintervalle insbesondere
\[
G_e^{\rm corr}(0.3930108,0.791438)>7.23\times10^{-8},
\]
\[
\sup_{\theta\in(0.791428,0.791429)}
G_e^{\rm corr}(0.3930110,\theta)
<-9.16\times10^{-7}.
\]

Ohne einen zusätzlichen Monotoniesatz in \(a\) ist dies ein rigoros eingeschlossener **lokaler Crossing der von \(a=0.392\) fortgesetzten Node-Schur-Architektur**, nicht die bereits bewiesene global erste Nullstelle im gesamten Prime-2-only-Bereich.

## 1. Unendlichdimensionaler Schur-Pivot

Im even-Sektor schreibe
\[
x=\alpha e_2+y,\qquad
y\in Y_{\rm even}
=
\overline{\operatorname{span}}\{e_4,e_6,\ldots\}.
\]

Auf
\[
J_a=\{|x|\ge\ell/2\}
\]
gilt \(V_a\ge m(a)\). Nach dem \(\theta\)-Split bleibt
\[
\lambda_2|\alpha|^2+\delta\|y\|^2
+\mu\langle x,P_Jx\rangle.
\]

Relativ zu \(\mathbb Ce_2\oplus Y_{\rm even}\):
\[
D=\delta I+\mu P_YP_JP_Y\succeq\delta I,
\]
\[
b=\mu P_YP_Je_2,\qquad
A_{22}=\lambda_2+\mu p.
\]

Daher
\[
A_{22}-\langle b,D^{-1}b\rangle
\ge
\lambda_2+\mu p-\frac{\mu^2}{\delta}p
=
S_{\rm node}.
\]

Dies ist ein Operator-Schur-Argument auf dem unendlichdimensionalen \(Y_{\rm even}\), keine endliche Matrixapproximation.

## 2. Korrigierter Momenttransport

Der Knotensplit kostet auf der rekonstruierten konstanten Mode
\[
\frac{\theta}{1-\theta}m(a)|u_0|^2,
\]
der globale negative Knotenboden kostet
\[
C(a)|u_0|^2.
\]

Damit ist der gesamte Momentverlust \(K(a,\theta)|u_0|^2\). Die Division durch \(1+\beta_e(a)\) in (N1-corr) ist ein eigener notwendiger Normschritt und wird im Checker explizit mitgeführt.

Keine dritte Mellinbedingung wird eingeführt.

## 3. Odd-Sektor

Setze
\[
\beta_o(a)
=
\left[
\frac{(a/2)^2}{6(1-(a/2)^2/20)}
\right]^2.
\]

Ohne Knotenreserve genügt
\[
G_o(a)
=
\frac{\lambda_3(a)-[-\lambda_1(a)]\beta_o(a)}
     {1+\beta_o(a)},
\]
mit
\[
\lambda_1=\lambda_2-\frac12,\qquad
\lambda_3=\lambda_2+\frac13.
\]

Der korrigierte Checker schließt
\[
\boxed{G_o(0.3930110)>\frac14.}
\]

Der lokale Architekturverlust ist damit even.

## 4. Rigorose \(\theta\)-Optimierung

Im Crossing-Bereich gilt \(S_{\rm node}<\delta\). Setze
\[
A=mp,\qquad q=m/\delta,\qquad B=Aq.
\]
Dann
\[
\eta(\theta)
=
\frac{\lambda_2+A\theta-B\theta^2}{(1+q\theta)^2},
\]
\[
\eta'(\theta)
=
\frac{A-2\lambda_2q-3Aq\theta}{(1+q\theta)^3},
\]
\[
\eta''(\theta)
=
\frac{6q(Aq\theta-A+\lambda_2q)}{(1+q\theta)^4}.
\]

Am oberen Endpunkt zeigen die gerichteten rationalen Intervalle
\[
Aq-A+\lambda_2q<0,
\]
also \(\eta''<0\) auf \((0,1)\).

Für die korrigierte Funktion
\[
G_e^{\rm corr}
=
\frac{\eta-\beta_e K}{1+\beta_e}
\]
ist
\[
\partial_\theta G_e^{\rm corr}
=
\frac{\eta'
-\beta_e m/(1-\theta)^2}
{1+\beta_e}.
\]

Der zweite Summand stammt von einer strikt konvexen Funktion in \(\theta\), daher bleibt \(G_e^{\rm corr}\) im relevanten Bereich strikt konkav. Die exakten Enclosures ergeben am oberen Endpunkt
\[
\partial_\theta G_e^{\rm corr}(0.791428)>0,
\]
\[
\partial_\theta G_e^{\rm corr}(0.791429)<0.
\]
Der Maximierer ist also eindeutig und liegt im angegebenen Bracket.

## 5. Zertifikatsstruktur

`check_x_c1_node_schur_function.py` benutzt für alle PASS-Entscheidungen `fractions.Fraction`.

Die Eingangsdaten sind gerichtete 30-stellige Außenintervalle für
\(C,m,p,\lambda_2,\delta,\beta_e,\beta_o\) an den beiden rationalen \(a\)-Endpunkten.

Geprüft werden:
1. korrigierter positiver even-Gap am unteren Endpunkt;
2. positives korrigiertes \(\theta\)-Derivat bei \(0.791428\);
3. negatives korrigiertes \(\theta\)-Derivat bei \(0.791429\);
4. korrigierter negativer even-Gap auf dem gesamten Maximierer-Bracket am oberen Endpunkt;
5. strikte Konkavität des \(\eta\)-Anteils;
6. Odd-Gap \(>1/4\).

## 6. Aussagegrenze und nächster Gate

Die korrigierte Node-Schur-Architektur verliert ihren positiven vollständigen even-Gap lokal bei ungefähr \(a=0.393011\).

Unbenutzt bleiben weiterhin:
\[
R_{\Gamma,a}[u]
=
\int_{x<y}
\bigl(g(y-x)-g(2a)\bigr)
|u(y)-u(x)|^2\,dx\,dy,
\]
sowie
\[
R_{2,a}[u]
=
w_2\int_{-a}^{a-\log2}
|u(x+\log2)-u(x)|^2\,dx.
\]

Der lokale Crossing ist deshalb weder ein Negativitätszeugnis für \(Q_W\) noch ein Nachweis der C15-Notwendigkeit.

Der nächste Gate ist **FULL-RESIDUAL-SCHUR**: Node-, nichtkonstante Gamma- und Prime-2-Differenzenergie werden gemeinsam als positiver Restoperator auf
\[
\mathbb Ce_2\oplus Y_{\ge4}^{\rm even}
\]
behalten. Erst nach dem vollständigen Schur-Pivot, Rücktransport und der expliziten Division durch \(1+\beta_e(a)\) darf ein vollständiger NULLPOL-Gap gebucht werden.

**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.
