# X-C1-NODE-SCHUR-WAXING — optimierter Knotensplit und erste Architektur-Schwelle

**Datum:** 17. September 2026.  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** analytische Waxing-Funktion und Rest-Schur-Gate `a=49/125` auf PR #137.  
**Scope:** Prime-2-only-Fenster, mit rigoroser Schwellenanalyse ab `a0=49/125`.

## 0. Ergebnis

Sei

```math
\ell=\log2,\qquad w_2=\frac{\ell}{\sqrt2},
\qquad H(s)=\int_s^\infty h(t)\,dt,
```

und im Prime-2-only-Bereich `ell/2<a<log3/2`

```math
C(a)=\kappa_*+w_2-H(2a-\ell)-H(\ell),
```

```math
m(a)=H(a+\ell/2)+H(a-\ell/2)-H(2a-\ell)-H(\ell),
```

```math
z(a)=\frac{\ell}{2a},\qquad
p(a)=1-\frac94z^5+\frac52z^3-\frac54z,
```

```math
\lambda_2(a)=1+2a h(2a)-C(a),\qquad
\delta(a)=\lambda_2(a)+\frac7{12}.
```

Für den even-Momentverlust setze

```math
\beta_e(a)=
\left[
\frac{(a/2)^2}{2(1-(a/2)^2/12)}
\right]^2.
```

Für `0<theta<1` definiere

```math
\mu(a,\theta)=\theta m(a),
```

```math
S(a,\theta)
=\lambda_2(a)+\mu p(a)
\left(1-\frac{\mu}{\delta(a)}\right),
```

```math
\eta(a,\theta)
=\frac{\min\{S(a,\theta),\delta(a)\}}
       {(1+\mu/\delta(a))^2},
```

```math
G_{\rm even}(a,\theta)
=
\frac{
 \eta(a,\theta)
 -\left[C(a)+\frac{\theta}{1-\theta}m(a)\right]\beta_e(a)
}{1+\beta_e(a)},
```

und die optimierte Node-Schur-Funktion

```math
\boxed{
G_{\rm node}(a)=\sup_{0<\theta<1}G_{\rm even}(a,\theta).
}
```

Dann ist für

```math
a_0=\frac{49}{125}=0.392,
```

die **erste Versagensschwelle dieser Node-Schur-Zertifikatsarchitektur nach dem bewiesenen Startpunkt** rigoros eingeschlossen durch

```math
\boxed{
0.3930108<a_{\rm node}<0.3930109.
}                                                     \tag{NS0}
```

Genauer:

```math
G_{\rm node}(a)>0
\quad\text{für jedes }a\in[0.392,0.3930108],       \tag{NS1}
```

während

```math
G_{\rm node}(0.3930109)<0.                           \tag{NS2}
```

Der parallele Odd-Gap bleibt am rechten Endpunkt sogar

```math
G_{\rm odd}(0.3930109)>\frac14.                     \tag{NS3}
```

**Bedeutung:** (NS0) ist keine Negativitätsschwelle von `Q_W`. Sie ist die erste rigoros lokalisierte Grenze der Architektur, die Mode 2 ausschließlich durch die optimale konstante Gamma-Skalarisierung plus die räumlich variable äußere Prime-2/Gamma-Knotenreserve und den optimierten Splitparameter `theta` trägt. Der positive nichtkonstante Gamma-Rest und die Prime-2-Differenzenergie sind weiterhin nicht verwendet.

---

## 1. Warum `C(a)` auf dem betrachteten Ast der richtige globale Knotenboden ist

Im verbundenen Prime-2-only-Fenster besitzt die Knotenfunktion zwei Kandidaten für ihr Minimum:

```math
R_{\rm ctr}(a)=2H(a)-\kappa_*,
```

und am inneren Rand des aktiven Prime-2-Endbandes

```math
R_{\rm end}(a)=H(2a-\ell)+H(\ell)-\kappa_*-w_2.
```

Am Startpunkt `a0=49/125` wurde im Eltern-Gate rigoros

```math
R_{\rm ctr}(a_0)>R_{\rm end}(a_0)
```

bewiesen. Die Differenz

```math
D(a)=R_{\rm ctr}(a)-R_{\rm end}(a)
```

erfüllt

```math
D'(a)=2\{h(2a-\ell)-h(a)\}>0,
```

denn im gesamten Prime-2-only-Bereich oberhalb `a0` gilt

```math
2a-\ell<a
```

(`a<log3/2<log2`) und `h` ist fallend. Also bleibt das aktive Endbandminimum von `a0` bis zum Eintritt von Prime 3 der globale Knotenboden. Damit ist

```math
-C(a)=R_{\rm end}(a)
```

auf diesem Ast exakt.

Die variable Reserve

```math
V_a(x)=\rho_a(x)+C(a)\ge0
```

besitzt auf

```math
J_a=\{|x|\ge\ell/2\}
```

den Boden

```math
\boxed{m(a)=V_a(\ell/2).}                           \tag{NS4}
```

---

## 2. Exakte `P_2`-Masse des äußeren Knotenbereiches

Für die normierte zweite Legendre-Mode `e_2` auf `(-a,a)` gilt mit

```math
z=\frac{\ell}{2a}
```

exakt

```math
p(a)=\langle e_2,1_{J_a}e_2\rangle
=5\int_z^1P_2(s)^2\,ds
=1-\frac94z^5+\frac52z^3-\frac54z.                 \tag{NS5}
```

Außerdem

```math
\frac{dp}{dz}=-\frac54(3z^2-1)^2\le0,
```

sodass `p(a)` mit `a` wächst.

Die maximal konstante Gamma-Skalarisierung liefert wie zuvor

```math
\lambda_2(a)=1+2ah(2a)-C(a),
```

und der even-Hochmodenboden ab `e_4`

```math
\delta(a)=\lambda_2(a)+\frac7{12}.                 \tag{NS6}
```

---

## 3. Optimierter Knotensplit

Für komplexe Zahlen und jedes `0<theta<1` gilt exakt

```math
|A+B|^2
\ge
\theta|A|^2-\frac{\theta}{1-\theta}|B|^2,          \tag{NS7}
```

denn die Differenz ist

```math
(1-\theta)\left|A+\frac{B}{1-\theta}\right|^2.
```

Wende dies auf die Knotenreserve `m(a) int_J |x+u_0e_0|^2` an. Dann bleibt für den Hochmodenvektor `x=alpha e_2+y` die positive Knotenkopplung

```math
\mu(a,\theta)=\theta m(a),
```

während die rekonstruierte konstante Mode zusätzlich

```math
\frac{\theta}{1-\theta}m(a)|u_0|^2
```

kostet.

Auf `C e_2 direct-sum Y_even` besitzt der Hochmodenblock das Schur-Unterbudget

```math
S(a,\theta)
=\lambda_2(a)+\mu p(a)
 \left(1-\frac{\mu}{\delta(a)}\right).             \tag{NS8}
```

Ist `S>0`, liefert die obere Dreiecksrücktransformation mit

```math
\|D^{-1}b\|\le\frac\mu\delta
```

den `L^2`-Boden

```math
\eta(a,\theta)
=\frac{\min\{S,\delta\}}{(1+\mu/\delta)^2}.       \tag{NS9}
```

Die even-Momentrekonstruktion erfüllt

```math
|u_0|^2\le\beta_e(a)\|x\|^2.
```

Daher ist der vollständige even-Quellgap exakt durch die oben definierte Größe `G_even(a,theta)` kontrolliert.

**Firewall:** Ist `G_even<=0`, ist lediglich dieser explizite Lower-Bound-Mechanismus unentschieden oder verbraucht. Daraus folgt kein negativer Weil-Vektor.

---

## 4. Optimierung als eindimensionales streng konkaves Problem

Setze für festes `a`

```math
m=m(a),\quad d=\delta(a),\quad p=p(a),\quad
\lambda=\lambda_2(a),\quad b=\beta_e(a),
```

und parametrisiere durch

```math
\mu=\theta m,\qquad 0<\mu<m.
```

Im Schwellenbereich liegt `S<d`, sodass

```math
E(\mu)=
\frac{\lambda+p\mu-(p/d)\mu^2}{(1+\mu/d)^2}.       \tag{NS10}
```

Der Momentverlust ist

```math
M(\mu)=C+\frac{\mu m}{m-\mu}.                      \tag{NS11}
```

Bis auf den festen positiven Nenner `1+b` maximieren wir also

```math
\Phi(\mu)=E(\mu)-bM(\mu).                          \tag{NS12}
```

Direkte Differentiation gibt

```math
E'(\mu)=
\frac{p-3p\mu/d-2\lambda/d}{(1+\mu/d)^3},          \tag{NS13}
```

und

```math
E''(\mu)=
-\frac{6}{d}
\frac{p-p\mu/d-\lambda/d}{(1+\mu/d)^4}.            \tag{NS14}
```

Ferner

```math
M'(\mu)=\frac{m^2}{(m-\mu)^2},\qquad
M''(\mu)=\frac{2m^2}{(m-\mu)^3}.                   \tag{NS15}
```

Somit ist `Phi` strikt konkav, sobald

```math
p-pm/d-\lambda/d>0.                                \tag{NS16}
```

Diese Bedingung wird am kritischen rechten Endpunkt rigoros mit Reserve `>0.2656261841` zertifiziert. Daher existiert dort genau ein Optimierer.

---

## 5. Positivität bis `0.3930108`

Setze

```math
a_0=\frac{49}{125},\qquad
a_-=\frac{3930108}{10^7},
```

und verwende die **feste**, vorab erklärte Wahl

```math
\theta_f=\frac{79142}{100000}.
```

Der exakte Intervallprüfer zeigt am rechten Rand

```math
G_{\rm even}(a_-,\theta_f)
>7.2371170\cdot10^{-8}>0.                           \tag{NS17}
```

Noch wichtiger: Die vollständige Ableitung derselben festen Zertifikatsfunktion wird auf dem ganzen Intervall `a in [a0,a_-]` mit rationalen Intervallen eingeschlossen als

```math
-5.52269
<\frac{d}{da}G_{\rm even}(a,\theta_f)
<-5.18887<0.                                        \tag{NS18}
```

Dabei werden die benötigten Komponenten ebenfalls rigoros kontrolliert: `C` wächst, `m` fällt, `p` wächst, `lambda_2` und `delta` fallen und `beta_e` wächst. Der Checker verifiziert insbesondere `m'<0` und `lambda_2'<0` auf dem gesamten Intervall.

Aus (NS17)--(NS18) folgt

```math
G_{\rm node}(a)
\ge G_{\rm even}(a,\theta_f)>0
\qquad(a_0\le a\le a_-).                           \tag{NS19}
```

Damit ist die untere Seite der ersten Node-Schur-Grenze **intervallweit**, nicht nur punktweise, geschlossen.

---

## 6. Global optimierter negativer Befund bei `0.3930109`

Setze

```math
a_+=\frac{3930109}{10^7}.
```

Am Punkt `a_+` gilt die strikte Konkavitätsbedingung (NS16). Der Checker schließt die Ableitung des Optimierungsfunktionals an

```math
\theta_0=0.791425,
\qquad
\theta_1=0.791426
```

rigoros ein:

```math
\Phi'(\theta_0)>2.2018681\cdot10^{-7}>0,           \tag{NS20}
```

```math
\Phi'(\theta_1)<-1.0416260\cdot10^{-7}<0.          \tag{NS21}
```

Wegen strikter Konkavität liegt der **eindeutige globale Optimierer** daher in

```math
0.791425<\theta_*(a_+)<0.791426.                    \tag{NS22}
```

Eine nach außen gerundete Intervallauswertung auf diesem gesamten Optimiererintervall ergibt selbst für den maximal möglichen Gap

```math
\boxed{
G_{\rm node}(a_+)<-3.9196306\cdot10^{-7}<0.
}                                                     \tag{NS23}
```

Damit ist nicht bloß eine ungünstige `theta`-Wahl gescheitert; am rechten Endpunkt ist die **voll optimierte** Node-Schur-Untergrenze negativ.

---

## 7. Erste Architektur-Schwelle

Auf dem kompakten `a`-Intervall dieser Analyse sind alle Bausteine stetig und `delta>1/2`. Für `theta->1` geht der Momentverlust wegen `theta/(1-theta)m(a) beta_e(a)` gleichmäßig gegen `+infinity`; daher kann das Supremum in der Definition von `G_node` auf ein kompaktes `theta`-Intervall eingeschränkt werden. Folglich ist `G_node(a)` stetig.

Definiere

```math
a_{\rm node}
=\inf\{a\ge49/125:\ G_{\rm node}(a)\le0\}.
```

Aus (NS19), (NS23) und Stetigkeit folgt rigoros

```math
\boxed{
\frac{3930108}{10^7}
<a_{\rm node}<
\frac{3930109}{10^7}.
}                                                     \tag{NS24}
```

Dies ist die erste strukturelle Schwelle **dieser** optimierten Node-Schur-Zertifikatsarchitektur nach dem bereits bewiesenen `a=49/125`-Checkpoint.

---

## 8. Odd-Sektor bleibt nicht limitierend

Setze

```math
\beta_o(a)=
\left[
\frac{(a/2)^2}{6(1-(a/2)^2/20)}
\right]^2.
```

Da `lambda_1=lambda_2-1/2` und `lambda_3=lambda_2+1/3`, liefert die sinh-Momentrekonstruktion den Gap

```math
G_{\rm odd}(a)
=
\frac{
 \lambda_3(a)-[-\lambda_1(a)]\beta_o(a)
}{1+\beta_o(a)}.                                    \tag{NS25}
```

Am rechten Schwellenendpunkt zertifiziert der Checker

```math
\boxed{G_{\rm odd}(a_+)>0.28112207>\frac14.}       \tag{NS26}
```

Auf dem betrachteten Intervall fällt `lambda_2` und wächst `beta_o`; aus (NS25) ist der rechte Endpunkt damit der ungünstigste. Der Odd-Sektor ist an der Node-Schur-Schwelle klar nicht limitierend.

---

## 9. Was jetzt wirklich ausgeschöpft ist — und was nicht

Ausgereizt ist nun die folgende konkrete Architektur:

1. maximaler konstanter Gamma-Boden `c(a)=g(2a)`;
2. exakter globaler Prime-2-Knotenboden `C(a)`;
3. äußere variable Knotenreserve `m(a)1_{J_a}`;
4. vollständige `P_2`-Masse `p(a)` dieser Reserve;
5. unendlichdimensionaler Schur-Abzug gegen den even-Hochmodenraum;
6. **optimierter** Splitparameter `theta`;
7. tatsächlicher cosh-Momentverlust und Rückrechnung auf die volle even-Norm.

Nicht verwendet und deshalb weiterhin verfügbar sind:

- die nichtkonstante positive Gamma-Restform `int_{x<y}{g(y-x)-g(2a)}|u(y)-u(x)|^2 dxdy`;
- die positive Prime-2-Differenzenergie;
- C15 als Form-Schur-Transport eines echten Restfreiheitsgrades.

**Folgerung:** Jenseits `a_node` ist erstmals der richtige Zeitpunkt erreicht, einen dieser drei bisher unbenutzten Mechanismen zu aktivieren. Ein weiterer bloßer Knotensplit oder ein weiteres `theta`-Tuning ist durch (NS24) ausgeschöpft.

Prime 3 ist im gesamten Schwellenintervall noch inaktiv. Die hier definierten Funktionen dürfen nach `a=log3/2` nicht unverändert fortgesetzt werden.

---

## 10. Rechnerische Reproduktion und epistemischer Status

`check_x_c1_node_schur_waxing.py` benutzt für sämtliche PASS-Entscheidungen `Fraction`-Arithmetik und rigorose rationale Restabschätzungen für Exponential-, Logarithmus-, Arcustangens-, `pi`- und Euler-`gamma`-Einschließungen.

Nach der vollständigen exakten Auswertung werden die bereits rigorosen Intervalle lediglich **nach außen** auf Nenner `10^28` gerundet, bevor die Schur-/Optimierungsalgebra ausgeführt wird. Diese Kompaktierung kann die Intervalle nur verbreitern und erhält daher die Rigorosität.

Der gespeicherte Lauf liefert **13/13 PASS**.

**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

Keine Quadratur als Beweis, kein A1-Import, keine dritte Mellinbedingung, keine CI-GREEN-/Registry-Promotion, kein Einheitsfenster-, Objekt-X- oder RH-Claim.
