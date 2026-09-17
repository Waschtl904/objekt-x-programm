# X-C1 NODE-SCHUR-WAXING — optimierter Knotensplit im Prime-2-only-Bereich

**Datum:** 17. September 2026  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** Connected-Faktorisierung, analytische Gamma-Waxing-Funktion und Rest-Schur-Gate `a=49/125` auf PR #137.  
**Scope:** Prime-2-only-Bereich `log(2)/2 < a < log(3)/2`; keine Aussage jenseits des Eintritts von Prime 3.

## 0. Ergebnis

Der variable Knotenmechanismus des `49/125`-Gates lässt sich als eindimensionale optimierte Waxing-Funktion formulieren. Für

\[
\ell=\log2,\qquad w=\frac{\ell}{\sqrt2},\qquad
H(s)=\int_s^\infty h(t)\,dt,
\]

setze

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
\lambda_2(a)=1+2a h(2a)-C(a),\qquad
\delta(a)=\lambda_2(a)+\frac7{12}.
\]

Für `0<theta<1` folgt aus

\[
|A+B|^2\ge\theta |A|^2-\frac{\theta}{1-\theta}|B|^2
\]

der Knotenkopplungskoeffizient

\[
\mu(a,\theta)=\theta m(a).
\]

Der rohe unendlichdimensionale Schur-Pivot wird von unten kontrolliert durch

\[
S_{\rm node}(a,\theta)
=\lambda_2(a)+\mu p\left(1-\frac{\mu}{\delta}\right).
\]

Die Rücktransformation kostet den Faktor `(1+mu/delta)^2`. Mit

\[
\beta_e(a)=\left[\frac{(a/2)^2}{2\left(1-(a/2)^2/12\right)}\right]^2
\]

erhält man den vollständigen even-Gap

\[
G_e(a,\theta)
=
\frac{\min\{S_{\rm node}(a,\theta),\delta(a)\}}
     {(1+\mu(a,\theta)/\delta(a))^2}
-
\frac{\beta_e(a)}{1+\beta_e(a)}
\left(C(a)+\frac{\theta}{1-\theta}m(a)\right).
\tag{N1}
\]

Definiere

\[
G_{\rm node}(a)=\sup_{0<\theta<1}G_e(a,\theta).
\tag{N2}
\]

Der aktuelle Gate liefert eine rigorose lokale Crossing-Einschließung

\[
\boxed{0.3930108<a_{\rm node}<0.3930110}
\tag{N3}
\]

in folgendem präzisen Sinn:

- bei `a=0.3930108` ist `G_e(a,0.791438)>0`;
- bei `a=0.3930110` ist der eindeutige theta-Maximierer in `0.791438<theta_*<0.791439` eingeschlossen und selbst dort gilt `G_e<0`;
- der Odd-Gap ist am oberen Endpunkt weiterhin `>1/4`.

Damit ist der erste Verlust **dieses optimierten Node-Schur-Mechanismus in der betrachteten lokalen Fortsetzung** auf etwa `0.393011` lokalisiert. Ein globaler Monotoniesatz von `G_node(a)` auf dem gesamten Prime-2-only-Bereich wird hier ausdrücklich noch NICHT behauptet; deshalb wird (N3) als rigoros eingeschlossener Crossing der von `a=0.392` fortgesetzten Architektur, nicht als bereits bewiesene global erste Nullstelle, bezeichnet.

## 1. Herleitung des Schur-Pivots

Wie im `49/125`-Beweis schreibe im even-Sektor

\[
x=\alpha e_2+y,\qquad y\in Y_{\rm even}=\overline{\operatorname{span}}\{e_4,e_6,\ldots\}.
\]

Auf der äußeren Prime-2-Zone

\[
J_a=\{|x|\ge \ell/2\}
\]
gilt `V_a>=m(a)`. Nach dem theta-Split bleibt im Hochmodenblock

\[
\lambda_2|\alpha|^2+\delta\|y\|^2+\mu\langle x,P_Jx\rangle.
\]

Relativ zu `C e_2 direct-sum Y_even` ist

\[
D=\delta I+\mu P_YP_JP_Y\succeq\delta I,
\quad
b=\mu P_YP_Je_2,
\quad
A_{22}=\lambda_2+\mu p.
\]

Daher

\[
A_{22}-\langle b,D^{-1}b\rangle
\ge
\lambda_2+\mu p-\frac{\mu^2}{\delta}p
=S_{\rm node}.
\]

Dies ist dasselbe unendlichdimensionale Schur-Argument wie am Punkt `49/125`, nun als Funktion von `a` und `theta`.

## 2. Momenttransport

Die even-NULLPOL-Bedingung liefert weiterhin

\[
|u_0|^2\le\beta_e(a)\|x\|^2.
\]

Der theta-Split kostet auf `u_0` zusätzlich

\[
\frac{\theta}{1-\theta}m(a)|u_0|^2,
\]

während der globale negative Knotenboden `C(a)|u_0|^2` beträgt. Nach Rückrechnung von `x` auf die volle even-Norm folgt exakt (N1).

Keine dritte Momentbedingung wird eingeführt.

## 3. Odd-Sektor

Setze

\[
\beta_o(a)=\left[\frac{(a/2)^2}{6\left(1-(a/2)^2/20\right)}\right]^2.
\]

Ohne irgendeine Knotenreserve liefert bereits der skalare Odd-Tail

\[
G_o(a)
=
\frac{\lambda_3(a)-[-\lambda_1(a)]\beta_o(a)}{1+\beta_o(a)},
\]

mit

\[
\lambda_1=\lambda_2-\frac12,\qquad
\lambda_3=\lambda_2+\frac13.
\]

Der Checker schließt am oberen Crossing-Endpunkt rigoros

\[
\boxed{G_o(0.3930110)>\frac14.}
\]

Der erste Architekturverlust ist in diesem Bereich somit even, nicht odd.

## 4. Warum die theta-Optimierung eindimensional rigoros ist

Im Crossing-Bereich gilt `S_node<delta`, daher ist der erste Term von (N1)

\[
\eta(\theta)
=\frac{\lambda_2+A\theta-B\theta^2}{(1+q\theta)^2},
\]

wobei

\[
A=mp,\qquad q=m/\delta,\qquad B=Aq.
\]

Direkte Differentiation ergibt

\[
\eta'(\theta)=
\frac{A-2\lambda_2q-3Aq\theta}{(1+q\theta)^3},
\]

und

\[
\eta''(\theta)=
\frac{6q\,[Aq\theta-A+\lambda_2q]}{(1+q\theta)^4}.
\]

Die rational eingeschlossenen Daten am oberen Endpunkt zeigen bereits bei `theta=1`

\[
Aq-A+\lambda_2q<0,
\]

also `eta''<0` auf `(0,1)`. Der Momentverlust

\[
\frac{\beta_e}{1+\beta_e}
\left(C+\frac{\theta}{1-\theta}m\right)
\]
ist strikt konvex in `theta`; sein Negativ ist daher strikt konkav. Somit besitzt `G_e(a,theta)` im relevanten Bereich höchstens einen inneren Maximierer.

Am oberen Endpunkt beweisen die rationalen Enclosures

\[
G_\theta(a,0.791438)>0,
\qquad
G_\theta(a,0.791439)<0,
\]

sodass der eindeutige Maximierer zwischen diesen beiden rationalen Zahlen liegt. Eine direkte Intervallauswertung auf diesem gesamten theta-Intervall liefert eine strikt negative Obergrenze für `G_e`.

## 5. Zertifikatsstruktur

Die beigefügte schnelle Standardbibliothek-Datei `check_x_c1_node_schur_function.py` führt die endgültigen Gate-Entscheidungen ausschließlich mit `fractions.Fraction` aus. Ihre Eingangsdaten sind 30-stellige rationale Außenintervalle für

- `C(a)`, `m(a)`, `p(a)`, `lambda_2(a)`, `delta(a)`, `beta_e(a)`, `beta_o(a)`

an den beiden rationalen Endpunkten. Diese Außenintervalle wurden separat mit 80-stelliger gerichteter Intervallarithmetik aus den ausgeschriebenen Formeln erzeugt; sie sind im Checker sichtbar und können unabhängig ersetzt werden.

Der Checker beweist sechs algebraische Gate-Aussagen:

1. positiver even-Gap am unteren Endpunkt;
2. positives theta-Derivat am linken theta-Bracket;
3. negatives theta-Derivat am rechten theta-Bracket;
4. negativer even-Gap auf dem gesamten Maximierer-Bracket am oberen Endpunkt;
5. strikte Konkavität des eta-Anteils;
6. Odd-Gap `>1/4`.

## 6. Aussagegrenze und nächster Mechanismus

Der optimierte Knotensplit verschiebt den bewiesenen Punkt `a=0.392` nur bis ungefähr `0.393011`. Das ist eine kleine, aber strukturell saubere Erweiterung. Entscheidend ist, dass hier **der gesamte verfügbare äußere Knotenboden `m(a)` und der Splitparameter theta optimiert** werden; die frühere feste Wahl `theta=1/2` ist nicht mehr die Ursache des Versagens.

Noch unbenutzt bleiben jedoch:

- der nichtkonstante positive Gamma-Rest `r_a(t)=g(t)-g(2a)`;
- die Prime-2-Differenzenergie.

Daher ist der Verlust von `G_node` weiterhin kein C15-No-Go. Der nächste qualitative Gate sollte diese beiden positiven Restenergien gemeinsam in den even-Hauptblock aufnehmen. Erst wenn auch deren vollständiger Schur-Beitrag rigoros ausgereizt ist, entsteht ein belastbarer Grund, Mode 2 in die C15-Restarchitektur zu überführen.

Beim Eintritt von Prime 3 bei `a>log(3)/2` muss die Knotengeometrie ohnehin neu aufgesetzt werden; keine Formel dieses Dokuments wird unverändert über diese Grenze extrapoliert.

**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.
