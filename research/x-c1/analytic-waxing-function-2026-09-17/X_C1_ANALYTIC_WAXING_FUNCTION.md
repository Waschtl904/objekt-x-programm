# X-C1 — analytische Waxing-Funktion für den konstanten Gamma-Boden

**Datum:** 17. September 2026  
**Status:** neue analytische Autorenableitung; externe Prüfung offen.  
**Elternstand:** Connected-Faktorisierung und Crossing-Gate `a=387/1000` auf PR #137.  
**Scope:** die skalarisierte Connected-Unterform auf zusammenhängenden Fenstern `I_a=(-a,a)` für `0<a<=1`.  
**Nicht behauptet:** Positivität des vollen Einheitsfensters, ein C15-No-Go oder eine RH-Folgerung.

## 0. Ergebnis

Setze

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\qquad
g(t)=h(t)-\frac1{2t}.
```

Die zunächst naheliegende globale Aussage „`g` ist auf `(0,infty)` streng fallend“ ist falsch. Richtig und für das gesamte Einheitsfenster ausreichend ist

```math
\boxed{g'(t)<0\qquad(0<t\le2).} \tag{W1}
```

Daher ist für jedes `0<a<=1` der **maximale konstante Boden**, den man aus `g` auf allen inneren Abständen `0<t<=2a` ziehen darf,

```math
\boxed{c(a)=\inf_{0<t\le2a}g(t)=g(2a)
=h(2a)-\frac1{4a}.} \tag{W2}
```

Für die bisherige konstant-floor-skalarisierte Mode 2 folgt damit

```math
\Lambda_2(a)
=\frac32+2a\,c(a)+2\mathcal H(a)-\kappa_*
=1+2a\,h(2a)+2\mathcal H(a)-\kappa_*,               \tag{W3}
```

wobei

```math
\mathcal H(a)=\int_a^\infty h(t)dt,
\qquad \kappa_*=\log(8\pi)+\gamma+\frac\pi2.
```

`Lambda_2` ist auf `(0,1]` streng fallend und besitzt genau eine Nullstelle `a_cf`. Ein rein rationaler Intervallprüfer schließt

```math
\boxed{
\frac{3916683}{10^7}<a_{\rm cf}<\frac{3916684}{10^7}
}
```

also

```text
0.3916683 < a_cf < 0.3916684.
```

Diese Zahl ist die **Grenze der maximalen konstanten Gamma-Floor-Skalarisierung**, nicht eine Negativitätsschwelle der vollständigen Weil-Form. Der positive nichtkonstante Rest

```math
r_a(t)=g(t)-c(a)\ge0
```

bleibt danach noch verfügbar und kann Mode 2 über einen echten Block-/Schurmechanismus koppeln. C15 ist daher auch jenseits `a_cf` eine natürliche Schnittstelle, aber nicht allein aus (W3) logisch erzwungen.

## 1. Warum globale Monotonie falsch ist

Für `t->infty` gilt

```math
h(t)=O(e^{-t/2}),
```

also

```math
g(t)=-\frac1{2t}+O(e^{-t/2})\longrightarrow0^-.
```

Außerdem

```math
g'(t)=\frac1{2t^2}+O(e^{-t/2})>0
```

für hinreichend großes `t`. `g` kann daher auf `(0,infty)` nicht streng fallend sein.

Die für Objekt X relevante Aussage bis zum Einheitsfenster ist dagegen (W1), weil dort alle inneren Abstände höchstens `2a<=2` betragen.

## 2. Strikte Monotonie auf `(0,2]`

Schreibe

```math
x=t/2,\qquad 0<x\le1.
```

Mit `sinh(2x)=2sinh(x)cosh(x)` erhält man exakt

```math
h(t)=\frac14\left(\operatorname{csch}x+\operatorname{sech}x\right),
```

und daher

```math
g(t)=\frac14\left(
\operatorname{csch}x+\operatorname{sech}x-\frac1x
\right).
```

Da `dx/dt=1/2`, folgt

```math
g'(t)=\frac18\left(
\frac1{x^2}
-\operatorname{csch}x\,\operatorname{coth}x
-\operatorname{sech}x\,\tanh x
\right).                                             \tag{W4}
```

Es genügt also bereits

```math
\operatorname{csch}x\,\operatorname{coth}x>\frac1{x^2},
```

d.h.

```math
\sinh^2x<x^2\cosh x.                                 \tag{W5}
```

Für `0<x<=1` gilt aus der positiven Taylorreihe und dem Quotienten aufeinanderfolgender Terme ab `x^2/3!`

```math
\frac{\sinh x}{x}
=1+\frac{x^2}{3!}+\frac{x^4}{5!}+\cdots
\le1+\frac{x^2/6}{1-1/20}
=1+\frac{10}{57}x^2.                                 \tag{W6}
```

Somit

```math
\left(\frac{\sinh x}{x}\right)^2
\le1+\frac{20}{57}x^2+\frac{100}{3249}x^4
\le1+\frac{1240}{3249}x^2.
```

Exakt

```math
\frac{1240}{3249}<\frac12,
```

während

```math
\cosh x\ge1+\frac{x^2}{2}.
```

Damit folgt (W5) strikt für `x>0`. Der zusätzliche Term `sech(x)tanh(x)` in (W4) ist ebenfalls strikt positiv. Also gilt (W1).

## 3. Die maximale konstante Waxing-Funktion

Wegen (W1) ist `g` auf jedem `(0,2a]`, `a<=1`, streng fallend. Deshalb wird das Infimum am rechten Rand angenommen:

```math
c(a)=g(2a)
=\frac{e^{-a}}{1-e^{-4a}}-\frac1{4a}.               \tag{W7}
```

Dies ist nicht nur irgendein zulässiger Boden, sondern der **größte konstante** Wert `c`, für den

```math
h(t)\ge\frac1{2t}+c
\qquad(0<t\le2a)
```

gilt.

Außerdem ist `c(a)>0` für `a<=1`: aus der Monotonie genügt `g(2)>0`; und

```math
h(2)>e^{-1}>1/3>1/4.
```

## 4. Eindeutige konstant-floor Mode-2-Schwelle

Die bisherige globale Legendre-Diagonalisierung des singulären Anteils gibt für Mode 2 den harmonischen Faktor `H_2=3/2`. Wird nun der maximal mögliche konstante Rest `c(a)` verwendet, lautet der betreffende Koeffizient exakt (W3).

`h` ist selbst streng fallend, denn

```math
h'(t)=h(t)\left(\frac12-\coth t\right)<0.
```

Aus (W1) folgt

```math
c'(a)=2g'(2a)<0.
```

Ferner ist `c(a)<h(2a)<h(a)`. Da `mathcal H'(a)=-h(a)`, folgt

```math
\Lambda_2'(a)
=2c(a)+2a c'(a)-2h(a)<0.                            \tag{W8}
```

Die Nullstelle ist also, sobald ein Vorzeichenwechsel eingeschlossen ist, eindeutig.

Der Begleitprüfer verwendet nur exakte rationale Intervallarithmetik für Exponentialfunktion, Logarithmus, Arkustangens, `pi`, Euler-`gamma` und `mathcal H`. Er beweist

```math
\Lambda_2(3916683/10^7)>0,
\qquad
\Lambda_2(3916684/10^7)<0.                          \tag{W9}
```

Zusammen mit (W8) ergibt dies die angegebene eindeutige Einschließung von `a_cf`.

## 5. Beziehung zum Gate `a=387/1000`

Bei `a=387/1000` ist der optimale konstante Boden

```math
c(a)=g(774/1000),
```

und (W3) ist noch strikt positiv. Der dort benutzte einfache Boden `43/200` ist also konservativ, aber bereits ausreichend. Das erklärt konzeptionell, weshalb das frühere Crossing der `1/5`-Buchhaltung kein Strukturzwang war.

Die analytische Waxing-Funktion verschiebt die konstant-floor Mode-2-Schwelle von ungefähr `0.38694` auf

```text
0.3916683...0.3916684.
```

## 6. Was an der neuen Schwelle wirklich endet

Bei `a>a_cf` ist `Lambda_2(a)<0`. Daraus folgt exakt:

> Keine Faktorisierung, die **nur** den singulären `1/(2t)`-Anteil plus einen konstanten Gamma-Boden `c I` mit `c<=inf g` diagonal als Hauptreserve benutzt und den gesamten nichtkonstanten positiven Rest `r_a` auslagert, kann Mode 2 weiterhin als positive Diagonalrichtung dieses skalaren Hauptblocks behandeln.

Nicht folgt:

- ein negativer Weil-Vektor;
- drei negative Richtungen der vollständigen Form;
- die Unmöglichkeit eines angereicherten positiven Blocks;
- die logische Notwendigkeit einer bestimmten C15-Realisierung.

Denn `r_a(t)=g(t)-c(a)` bleibt eine positive, nichtkonstante Differenzenergie und kann Mode 2 mit höheren Richtungen koppeln.

## 7. Nächster qualitative Gate

Ein sinnvoller erster rationaler Punkt **oberhalb** der konstant-floor Schwelle ist

```math
a=49/125=0.392.
```

Dort muss zunächst `Lambda_2<0` rational bestätigt werden. Danach ist nicht noch ein neuer konstanter Boden zu suchen, sondern der verbleibende positive Rest

```math
\mathcal R_a[u]
=\int_{x<y}\bigl(g(y-x)-c(a)\bigr)|u(y)-u(x)|^2dxdy
```

auf

```math
\operatorname{span}\{P_2\}\oplus Y_{\ge3}
```

als Blockform zu behalten. Der nächste echte Test ist dann ein Schur-Gate

```math
A_{22}-C^*D^{-1}C>0.
```

Gelingt es, ist Mode 2 weiterhin durch bereits vorhandene positive Gammaenergie gerettet. Gelingt es mit kontrollierten Bounds für diese benannte Restzerlegung nicht, ist die C15-Form-Schur-Schnittstelle der natürliche nächste Kandidat. Das Scheitern einer groben Boundwahl allein wäre weiterhin kein Weil-No-Go.

## 8. Statusgrenzen

- `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.
- Keine Verwendung von A1.
- Kein neuer numerischer Eigenwertsatz.
- Keine dritte Mellinbedingung.
- Keine Behauptung globaler Monotonie von `g`.
- Kein Merge- oder Registry-Upgrade.
