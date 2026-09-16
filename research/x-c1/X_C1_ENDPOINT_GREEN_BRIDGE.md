# X-C1-ENDPOINT-GREEN — kompakte Green-Brücke und vollständiger Zweiquellentest

**Datum:** 16. September 2026. **Spur:** Draft PR #137.
**Gelesener C1-STORAGE-Anker:** `3a81019e43d95750493d47030728966576b3b942`.
**Status:** analytische Autorenherleitung; externe Prüfung OFFEN; keine Neuheitsbehauptung.

Diese Fortsetzung konstruiert die Endpunktabbildung und einen expliziten signierten Randspeicher. Zusätzlich wird der VORAB fixierte Zweiquellenraum aus C0 §10.2 einschließlich Gamma- und Polbilanz behandelt. Sie konstruiert NICHT die noch gesuchte positive Gesamtauswertung C_a.

A1 wird nicht benutzt oder erneut geprüft. Die drei C0-Dateien, die beiden bisherigen C1-STORAGE-Dateien, PR #131, main und Registry bleiben unverändert. Der ursprüngliche C0-Prüfer und der A1-Prüfer werden nicht ausgeführt. Die Green-Brücke ist eine zusätzliche Auslesung des bestehenden Vormediators, kein zweiter konkurrierender C0.

## 1. Die beiden Mellinbedingungen sind exakt die zwei äußeren Green-Schwänze

Es gelten die eingefrorenen Konventionen

```math
L=-\partial_x^2+\frac14,\quad G(x)=e^{-|x|/2},\quad LG=\delta_0,
\qquad E_\pm(u)=\int e^{\pm y/2}u(y)\,dy.
```

Der Ableitungssprung von G ist -1; damit ist insbesondere KEIN zusätzlicher Faktor 2 nötig. Für u in C_c^infinity(I_a), I_a=(-a,a), setze

```math
\phi=G*u.
```

Außerhalb des Quellenträgers gilt exakt

```math
\phi(x)=e^{-x/2}E_+(u)\quad(x\ge a),\qquad
\phi(x)=e^{x/2}E_-(u)\quad(x\le-a).                 \tag{EG1}
```

Somit sind beide Mellinbedingungen äquivalent zum Verschwinden beider äußeren Schwänze. Auf der tatsächlichen NULLPOL-Klasse folgt

```math
\boxed{L:C_c^\infty(I_a)\longrightarrow\mathcal W_a
\text{ ist bijektiv, mit }L^{-1}u=G*u.}            \tag{EG2}
```

Beweis: Die Faltung ist glatt und löst Lphi=u. EG1, auch mit jedem engeren Intervall um supp u, zeigt kompakten Träger innerhalb desselben Fensters. Umgekehrt liefert partielle Integration E_lambda(Lphi)=(1/4-lambda^2)E_lambda(phi), also E_+=E_-=0. Eine kompakt getragene Lösung von Lphi=0 ist null. Die Brücke erhält den konvexen Trägerhüllenrand; sie wird NICHT als erhaltend für innere Trägerlücken behauptet.

### 1.1 Passender Abschluss, ohne Wechsel der C0-Testtopologie

Für die bestehende H1-Quellenklasse gilt ebenso

```math
L:H^3_0(I_a)\xrightarrow{\ \cong\ }
H^1_0(I_a)\cap\ker E_+\cap\ker E_-.               \tag{EG3}
```

Die Nullfortsetzung von u gehört zu H1(R); der Green-Inverse gehört zu H3(R). EG1 liefert phi=phi'=0 an beiden Fensterrändern; aus phi''=phi/4-u und der Nullspur von u folgt zusätzlich phi''=0. Dies sind genau die H3_0-Spuren. Die umgekehrte Abbildung ist direkt. Dichte folgt durch Approximation von phi in H3_0 mit glatten kompakten Funktionen und anschließender Anwendung von L.

Mit den Ableitungssummennormen ergibt partielle Integration

```math
\|L\phi\|_{H^1}^2
=\|\phi'''\|_2^2+\frac32\|\phi''\|_2^2
 +\frac9{16}\|\phi'\|_2^2+\frac1{16}\|\phi\|_2^2.
```

Daher gilt insbesondere ||phi||_{H3}<=4||u||_{H1}, unabhängig von a. Das ist eine Normaussage über die Green-Brücke, KEINE radienuniforme Weil-Positivität.

## 2. Tatsächliche zweiseitige Ports aus demselben Quellenfeld

Definiere auf der ganzen Zeitachse

```math
p(x)=\int_{-\infty}^x e^{-(x-y)/2}u(y)\,dy,
\qquad q(x)=\int_x^\infty e^{-(y-x)/2}u(y)\,dy.
```

Für H im vorhandenen M=L2(R;h) benutzt man u=R_0H. Beide Faltungsoperatoren sind M->L2(R) beschränkt, da R_0 beschränkt ist und die beiden Faltungskerne L1-Norm 2 haben. Auf physischen Zuständen ist p der vorhandene Gamma-Grundport Y_0; q ist ausdrücklich ein ZUKUNFTS-/ZWEISEITIGER Port, nicht eine unbenannte beschränkte Funktion eines einzelnen kausalen Zustands z_x.

Auf NULLPOL-Bahnen gilt

```math
p=\tfrac12\phi-\phi',\qquad q=\tfrac12\phi+\phi',
\qquad \phi=p+q,\quad (\partial_x+\tfrac12)p=u,
\quad(-\partial_x+\tfrac12)q=u.                   \tag{EG4}
```

Insbesondere sind p und q im selben Fenster kompakt getragen. Die zwei Momente werden nicht durch frei wählbare Terminaldaten ersetzt.

Die erste genaue positive Energieidentität lautet

```math
|p|^2+|q|^2=2|\phi'|^2+\tfrac12|\phi|^2,
```

```math
2\operatorname{Re}(\overline u\phi)
=|p|^2+|q|^2+\frac d{dx}(|p|^2-|q|^2).           \tag{EG5}
```

Der Speicher |p|^2-|q|^2 ist signiert und hat Nullendwerte. Integriert ergibt sich die positive GREEN-Paarung <u,G*u>=(||p||^2+||q||^2)/2. Diese Paarung ist NICHT Q_W. EG5 wird deshalb nicht als Lösung von C1-GEOM oder der ursprünglichen Supply ausgegeben.

## 3. Expliziter signierter Speicher für die tatsächliche C1-Randpaarung

Benutzt werden genau F_a, s_a und B_a aus X_C1_STORAGE.md (18)--(19):

```math
s_a[z_x]+\frac d{dx}F_a[z_x]
=2\operatorname{Re}(\overline u\,r_a),\qquad r_a=B_a u,
```

```math
B_a u=\int_0^\infty h(t)(u(x)-u(x-t))dt
-\sum_{t_n\le2a}w_nu(x-t_n)-\frac{\kappa_*}{2}u(x),
\quad h(t)=\frac{e^{-t/2}}{1-e^{-2t}}.
```

Auf dem glatten Testkern definiere den konkreten Strom

```math
J_a[u](x)=2\operatorname{Re}
 \left(\overline\phi\,r_a'-\overline{\phi'}\,r_a\right),
\qquad V_a^{\mathrm{br}}=J_a-F_a[z_x].
```

Die komplexe Green-Identität liefert punktweise

```math
2\operatorname{Re}(\overline{L\phi}\,r_a)
=2\operatorname{Re}(\overline\phi\,Lr_a)+J_a',
```

also die exakte Original-Gauge-Identität

```math
\boxed{s_a[z_x]
=2\operatorname{Re}(\overline\phi\,(LB_aL)\phi)
+\frac d{dx}V_a^{\mathrm{br}}.}                   \tag{EG6}
```

Das ist ein tatsächlich definierter endpunktbedingter signierter Speicher, kein bloßes Existenzsymbol. Der Ausdruck B_a und seine Ableitungen sind auf glatten kompakten Quellen wohldefiniert: am unteren Integralrand bleiben die Differenzen zusammen und sind O(t); die Primzahlsumme ist endlich. J_a ist wegen phi,phi' kompakt getragen. F_a hat die bereits bewiesenen Nullendwerte. Daher verschwinden beide Endwerte von V_a^{br}.

Der verbleibende Residualausdruck in EG6 ist weiterhin SIGNIERT. Weder seine punktweise Positivität noch eine positive integrierte Faktorisierung wird behauptet. Die H3/H1-Brücke aus EG3 ist abgeschlossen; die Stromidentität wird hier auf dem glatten Kern bewiesen, nicht ohne Nachweis auf eine größere Outputdomäne ausgedehnt.

### 3.1 Exakter Fenstertransport

Für a<b und eine alte Quelle u in W_a bleibt phi=G*u wörtlich unverändert. Neu aktivierte Verzögerungen t>2a erfüllen u(x-t)=u'(x-t)=0 auf supp phi. Deshalb gilt punktweise

```math
J_b[u]=J_a[u],\qquad
2\operatorname{Re}(\overline\phi LB_bL\phi)
=2\operatorname{Re}(\overline\phi LB_aL\phi),
```

```math
\boxed{V_b^{\mathrm{br}}-V_a^{\mathrm{br}}
=-(F_b-F_a).}                                    \tag{EG7}
```

Das Vorzeichen ist NEGATIV und stimmt mit dem bisherigen Original-Gauge-Kokzyklus überein. Es wird keine Isometrie zwischen noch nicht konstruierten positiven X-Ausgaberäumen daraus abgeleitet.

## 4. Gamma-Grundschwanz: genaue Auslöschung, nicht Weglassen der Grundenergie

Die klassische geometrische Reihe lautet

```math
h(t)=\sum_{m\ge0}e^{-\mu_mt},\qquad\mu_m=2m+\tfrac12.
```

Für x>a hat der kontinuierliche Teil von B_a die Darstellung

```math
B_\gamma u(x)=-\sum_{m\ge0}e^{-\mu_mx}E_{\mu_m}(u)
=-\sum_{m\ge1}e^{-\mu_mx}E_{\mu_m}(u).            \tag{EG8}
```

Hier vernichtet E_+(u)=0 exakt m=0. Für x-a>=d>0 folgt

```math
|B_\gamma u(x)|\le
\|u\|_1\frac{e^{-5(x-a)/2}}{1-e^{-2(x-a)}}.
```

Daher ist z.B. der zeitgewichtete äußere Tail endlich:

```math
\int_{a+d}^\infty e^{x-a}|B_\gamma u(x)|^2dx
\le\frac{\|u\|_1^2e^{-4d}}{4(1-e^{-2d})^2}.
```

Für den antikausalen Gamma-Port gilt die spiegelbildliche Aussage mit E_-. Beim festen a verschwinden die endlichen Primverzögerungen für x>3a. Es wird NICHT die unendliche Primzahl-Rohenergie hochskaliert. Diese ZEIT-Tail-Aussage ist kein Ersatz für den globalen kritischen Root-L-Output-Gate.

Die m=0-Energie ist nicht null: auf u=Lphi ist sie 4||p'||^2=4||phi''||^2+||phi'||^2. Nur ihr äußerer Schwanz verschwindet. Bei getrennt getragenen Potentialen verschwindet zusätzlich ihre gemischte Paarung.

## 5. Der unveränderte Prime-2-Zeuge: vollständige gemischte Weil-Paarung

Setze wie VOR diesem Arbeitspaket in C0 §10.2

```math
\ell=\log2,\quad\varepsilon=\frac1{100},\quad\delta=2\varepsilon=\frac1{50},
\quad b(x)=\begin{cases}
\exp(-1/(1-(x/\varepsilon)^2)),&|x|<\varepsilon,\\
0,&\text{sonst},
\end{cases}
```

```math
\phi_f(x)=b(x+\ell/2),\quad\phi_g(x)=b(x-\ell/2),
\qquad f=L\phi_f,\quad g=L\phi_g=U_\ell f,
\quad N=\|f\|_2^2=\|g\|_2^2>0.
```

Es gibt keine neue Testwahl, Normierung oder Parameteranpassung. EG2 gibt genau diese Potentiale zurück. Die Quellen sind disjunkt, haben beide Mellinmomente null, und nur die Primverzögerung log2 verbindet sie. Daher bleiben

```math
Q_{\rm pole}(f,g)=0,\quad
Q_{\rm fin}(f,g)=-\frac{\log2}{\sqrt2}N,
\quad Q_{\rm fin}(f,f)=Q_{\rm fin}(g,g)=0.          \tag{EG9}
```

### 5.1 Nicht mehr nur der nackte Primbeitrag

Für reelle getrennte Quellen mit f links von g folgt aus der Jumpform

```math
Q_\gamma(f,g)
=-\int\!\int e^{-\mu|x-y|}f(x)g(y)dxdy
```

für JEDEN einzelnen Gamma-Modus mu; der Gesamtbeitrag ist die Summe dieser Ausdrücke. Der skalare -kappa_*-Term ist wegen <f,g>=0 null. Präzise bezeichnen wir den Einzelbeitrag nachfolgend mit Q_{gamma,mu}. Separation gibt

```math
Q_{\gamma,\mu}(f,g)=-E_\mu(f)E_{-\mu}(g),
\qquad E_\mu(L\phi)=(\tfrac14-\mu^2)E_\mu(\phi).
```

Daraus folgt für die vollständige Gamma-Mischpaarung

```math
R_\gamma:=\sum_{m\ge1}
 (\mu_m^2-\tfrac14)^2e^{-\mu_m\ell}
 E_{\mu_m}(b)E_{-\mu_m}(b)>0,
\qquad Q_\gamma(f,g)=-R_\gamma.                   \tag{EG10}
```

m=0 verschwindet EXAKT. Alle übrigen Summanden sind positiv, weil b nichtnegativ und nicht null ist. Die Reihe konvergiert absolut: E_mu(b)E_-mu(b)<=||b||_1^2 exp(2mu epsilon), während ell-2epsilon>0 und der übrige Faktor nur polynomial in m wächst. Auf getrennten Trägern rechtfertigt dieser Abstand auch die modale Integration und die partielle Integration.

Damit ist die VOLLSTÄNDIGE gemischte Zielpaarung explizit:

```math
\boxed{Q_W(f,g)=-\frac{\log2}{\sqrt2}N-R_\gamma.}   \tag{EG11}
```

Eine negative gemischte Paarung ist mit positiver Gramgeometrie vereinbar. EG11 ist eine direkte Auswertung der tatsächlichen signierten Weil-Form, keine Ausgabe eines bereits konstruierten positiven C_a.

## 6. Strikte positive Untergrenze für genau den eingefrorenen Zweiquellenraum

Hier lässt sich zusätzlich OHNE A1 und OHNE numerische Quadratur der gesamte feste 2x2-Zielblock positiv kontrollieren. Setze D=Q_W(f,f)=Q_W(g,g) und C=(log2/sqrt2)N+R_gamma. Dann lautet er

```math
\begin{pmatrix}D&-C\\-C&D\end{pmatrix}.            \tag{EG12}
```

### 6.1 Diagonale

Für jede Verschiebung t>=delta sind f und U_t f disjunkt. Daher ||K_t f||^2=2N. Der ausgelassene Gamma-Integrand auf (0,delta) ist nichtnegativ. Mit kappa_*=log(8pi)+gamma+pi/2 folgt

```math
D\ge N\left(2\int_\delta^\infty h(t)dt-\kappa_*\right).
```

Substitution q=exp(-t/2) ergibt genau

```math
\int_\delta^\infty h(t)dt
=\operatorname{atanh}(e^{-\delta/2})+
 \arctan(e^{-\delta/2}),
```

also

```math
2\int_\delta^\infty h-\kappa_*
=\log\coth(\delta/4)-\log(8\pi)-\gamma
 -2\arctan\tanh(\delta/4).
```

Für z>0 gelten coth z>1/z und arctan(tanh z)<z. Mit delta=1/50, pi<22/7, gamma<1 und e<11/4 erhält man

```math
2\int_\delta^\infty h-\kappa_*
>\log(175/22)-1-1/100>99/100.                     \tag{EG13}
```

Die letzte Ungleichung verwendet (11/4)^2<175/22. Alle Konstantenschranken sind elementar: 22/7-pi ist das strikt positive Integral integral_0^1 x^4(1-x)^4/(1+x^2)dx; H_n-log n fällt von 1 gegen gamma; e<11/4 folgt durch geometrische Majorisierung der Exponentialreihe ab k=3. Damit ist D>(99/100)N bewiesen.

### 6.2 Gemischter Betrag

Der Trägerabstand beträgt mindestens ell-delta. Die positive Dichte h ist fallend und h(t)<=1+1/(2t). Cauchy-Schwarz auf den jeweils delta breiten Trägern liefert

```math
|Q_\gamma(f,g)|\le\delta h(\ell-\delta)N.
```

Mit log2>2/3 folgt ell-delta>97/150 und deshalb

```math
R_\gamma<\frac{86}{2425}N.
```

Ferner gilt log2<7/10 und sqrt2>7/5, also log2/sqrt2<1/2. Die Logarithmusgrenzen folgen aus log2=2atanh(1/3)>2/3 sowie exp(7/10)>sum_{k=0}^3(7/10)^k/k!>2. Somit

```math
C<\left(\frac12+\frac{86}{2425}\right)N,
\qquad D-C>\frac{4409}{9700}N>\frac9{20}N.         \tag{EG14}
```

Da f und g L2-orthogonal sind und dieselbe Norm haben, folgt für ALLE komplexen alpha,beta

```math
\boxed{Q_W[\alpha f+\beta g]\ge
\frac9{20}\|\alpha f+\beta g\|_2^2,}              \tag{EG15}
```

mit strikter Ungleichung für nichtverschwindende Kombinationen. Insbesondere sind f, g, f+g und f-g einschließlich Gamma- und Polbilanz erfasst.

**Reichweite:** EG15 betrifft ausschließlich den fest deklarierten zweidimensionalen Quellenraum. Es ist kein weiterer A1-Audit, keine Matrixzertifizierung des vollständigen Fensters, keine Konstruktion von C_a und kein bestandener vollständiger C1-GEOM-Gate. Der Zielblock wird nicht durch eine angepasste Quadratwurzel zum Mediator erklärt. Für größere Fenster gilt dieselbe Aussage nur auf diesem unveränderten alten Quellenraum über die bekannte Fensterverträglichkeit.

## 7. Prüfer, Herkunft und verbleibendes Problem

`scripts/check_x_c1_endpoint_green_bridge.py` wurde lokal mit SymPy 1.14.0 ausgeführt: **29 exakte algebraische/rationale Checks PASS**. Enthalten sind die komplexen Green-/Stromidentitäten, Momentfaktoren, Gamma-Normierung, die exakte pi-Integralidentität und alle rationalen Budgets in EG13--EG15. Keine numerische Quadratur, keine Großmatrix, kein LDL, kein ursprünglicher C0-/A1-Lauf. Die endlichen Checks ersetzen nicht die analytischen Träger-, Abschluss- und Konvergenzbeweise. Keine unabhängige externe Zertifizierung und keine CI-green-Behauptung.

Neu konstruiert sind die support-erhaltende Endpunktabbildung auf der ganzen tatsächlichen Testklasse, ihre zweiseitigen Ports und der signierte Original-Gauge-Speicher mit exaktem Fenstertransport. Der vollständige VORAB fixierte Zweiquellentest ist analytisch ausgewertet und mit einer expliziten positiven Untergrenze versehen.

**Weiter offen:** Aus der konkreten Randpaarung bzw. EG6 eine nichtzirkuläre positive Gesamtauswertung für die gesamte Testklasse samt Outputdomäne und X-Connecting-Maps gewinnen. EG6 allein ist keine positive Faktorisierung. Keine Aussage über einen neuen Zusammenhang physikalischer Naturkonstanten, allgemeine Weil-Positivität, RH oder Literatur-Neuheit.

### Quellenanker

- [C0-Spezifikation und festgelegter Test](https://github.com/Waschtl904/objekt-x-programm/blob/3a81019e43d95750493d47030728966576b3b942/X_CANDIDATE_C0_SPEC.md), insbesondere §§2, 5, 9, 10.2. Nur Import der Daten; keine erneute Statusprüfung.
- [C1-STORAGE](https://github.com/Waschtl904/objekt-x-programm/blob/3a81019e43d95750493d47030728966576b3b942/research/x-c1/X_C1_STORAGE.md), insbesondere (18)--(21).
- [DLMF 5.7.6](https://dlmf.nist.gov/5.7#E6): klassische Digamma-/Resolventenreihe; keine importierte Positivität. Die hier benutzte Reihe für h ist außerdem direkt geometrisch beweisbar.

Allgemeine Green-, Resolventen- und Sobolevmethoden sind klassisch. Die Formeln dieses Arbeitspakets werden oben aus den festgelegten Projektquellen hergeleitet; eine Neuheitsrecherche oder externe Prüfung wird nicht vorgetäuscht.
