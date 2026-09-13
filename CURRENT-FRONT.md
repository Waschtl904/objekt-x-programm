# CURRENT FRONT — Objekt X / COMMON-JUMP → NP-OVERLAP

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 13. September 2026; keine Registry-Promotion.  
> **Kanonische Hauptaudits:** [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md) · [Q0 first channel](audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md) · [Review correction / Prime overlap](audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Registry und Arbeitsdefinition bleiben unverändert.

## 1. Gesicherte gemeinsame Geometrie `✓[M]`

Mit

```math
K_t=T_{t/2}-T_{-t/2}
```

entstehen archimedischer Ort und Primzahlpotenzen aus derselben positiven Featurefamilie. Auf der Nullpolklasse

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

gilt für jedes `a>0`

```math
\boxed{
Q_W(v,w)=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle,
}
```

mit

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\kappa_*,
\qquad
\kappa_*=\log\pi-\psi(1/4).
```

COMMON-JUMP, NP-R1-Subsumption und cutoff-gauge covariance bleiben `✓[M]`.

## 2. `Q_0` / erster Gamma-Kanal `✓[M]`

Die archimedische Dichte zerfällt als

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m\ge0}e^{-\alpha_m t},
\qquad \alpha_m=2m+\frac12.
```

Für

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_tdt
```

gilt

```math
A_\alpha
=\frac{2}{\alpha}(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
```

Mit

```math
Q_0=-\partial_x^2+\frac14
```

folgt exakt

```math
\boxed{
A_{1/2}=4I-Q_0^{-1},
\qquad
A_{1/2}Q_0=-4\partial_x^2.
}
```

Außerdem

```math
\boxed{
Q_0:C_c^\infty(-a,a)\xrightarrow{\cong}D_{NP}(a)
}
```

support-erhaltend und

```math
\langle Q_0u,A_{1/2}Q_0u\rangle
=4\|u''\|^2+\|u'\|^2.
```

## 3. Höhere Gamma-Kanäle: Exponent geklärt `✓[M]`

Für den komprimierten Resolventenkern

```math
R_\alpha(x,y)=\frac{1}{2\alpha}e^{-\alpha|x-y|}
```

liefert der Schur-Test exakt

```math
\|1_{(-a,a)}R_\alpha1_{(-a,a)}\|
\le\frac{1-e^{-\alpha a}}{\alpha^2}.
```

Daher

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge\frac{2}{\alpha}e^{-\alpha a}\|v\|^2.
}
```

Die im externen Review aufgeworfene `e^{-alpha a}`/`e^{-2alpha a}`-Frage ist damit zugunsten des stärkeren Exponenten geschlossen.

## 4. Short-window-Buchung korrigiert

Aus den `Q_0`- und höheren Kanalabschätzungen folgt architekturintern ein short-window Gap. Der dazugehörige Bound ist

```math
B(a)=\frac{4\pi^2}{\pi^2+a^2}
+\sum_{m=1}^\infty\frac{2}{\alpha_m}e^{-\alpha_ma}.
```

Mit `x=e^{-a/2}` gilt geschlossen

```math
B(a)=\frac{4\pi^2}{\pi^2+a^2}
+\log\frac{1+x}{1-x}+2\arctan x-4x.
```

Ein eigener Arb-Checker zertifiziert den eindeutigen Schnittpunkt `B(a_*)=kappa_*` auf dem Exact Head; die vorgesehene Bracket ist

```math
0.1033784517534<a_*<0.1033784517535<\frac12\log2.
```

**Literatur-Firewall:** Die Existenz der Kleinfensterpositivität ist kein neuer Satz des Projekts. Suzuki Theorem 1.4 beweist bereits eine stärkere unbedingte Kleinfensterpositivität auf der vollen lokalen Klasse. Unsere Buchung ist daher:

```text
COMMON-JUMP/Q0 interne Herleitung der Kleinfenster-Coercivity  ✓[M]_part
Short-window positivity als neuer Literatur-Satz               ×[M]
```

Der Wert des Resultats ist strukturell: die eigene positive Architektur reproduziert die bekannte Kleinfenster-Coercivity und deren führende `log(1/a)`-Skala.

## 5. Exakte neue Restform — Prime overlap `✓[M]`

Setze

```math
\mathcal A(v)
:=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|K_tv\|^2dt
-\kappa_*\|v\|^2.
```

Da

```math
\|K_tv\|^2
=2\|v\|^2-2\operatorname{Re}\langle T_tv,v\rangle,
```

cancelt der gesamte Prime-Diagonalledger exakt gegen den Prime-Anteil von `Gamma_a`. Auf `D_NP(a)` bleibt

```math
\boxed{
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
}
```

mit

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

Für `log n>=2a` sind die Träger disjunkt und die Korrelation ist null.

Äquivalent ist all-`a` NP-GAP genau die Operatorungleichung

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)},
}
```

wobei

```math
\mathbf O_a
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\frac{T_{\log n}+T_{-\log n}}2.
```

**Das ist jetzt der kanonische harte Rest.** Die große Prime-Schwelle selbst ist nach Zentrierung nicht die Wand; die Wand ist der endliche gewichtete Überlappungsoperator.

## 6. `Q_0`-Transport des Prime overlap `✓[M]`

Für `v=Q_0u` gilt exakt

```math
\boxed{
\operatorname{Re}\langle T_tv,v\rangle
=
\operatorname{Re}\langle T_tu'',u''\rangle
+\frac12\operatorname{Re}\langle T_tu',u'\rangle
+\frac1{16}\operatorname{Re}\langle T_tu,u\rangle.
}
```

Damit wird der arithmetische Defekt auf Nullpol zu einer endlichen Summe gewöhnlicher Shift-Korrelationen auf den Sobolev-Ebenen `0,1,2`.

## 7. Mehrkanal-Gamma-Leiter — zulässig, aber auxiliary

Für

```math
Q_m=-\partial_x^2+\alpha_m^2
```

gilt

```math
M(Q_mu)(s)=\left(\alpha_m^2-(s-1/2)^2\right)M(u)(s),
```

also Nullstellen bei

```math
s=-2m,\qquad s=2m+1.
```

Die endlichen Mengen

```math
F_N=\{-2m,2m+1:0\le m<N\}
```

sind mit Connes--Consani Proposition C.1 verträglich: die negativen geraden Punkte sind triviale, nicht nichttriviale Zeta-Nullstellen. Die Leiter ist damit strukturell legitim, bleibt aber auxiliary, solange sie den Prime-overlap nicht quantitativ kontrolliert.

## 8. Neue Default-Hauptfront — NP-OVERLAP `?[O]`

Zu beweisen ist

```math
\boxed{
\mathcal A(v)\ge\mathcal O_a(v)
\quad
(v\in D_{NP}(a),\ a>0).
}
```

Priorität:

1. Spektrum und positive Spektralmasse von `O_a` auf Nullpol;
2. `Q_0`-transportierte Shift-Korrelationen und Parität;
3. scharfe Abklingung der Überlappung für `log n -> 2a`;
4. Verbindung zur bereits bewiesenen Prime-Power-AR(1)/Weil-tail-Struktur;
5. Gamma-Mehrkanalleiter nur dann weiterziehen, wenn sie eine quantitative Kontrolle von `O_a` liefert.

Ein Beweis für alle `a` bleibt RH-hart.

## 9. Numerik-Firewall

Endlichdimensionale Ritz-Minima sind obere Schranken für das wahre Infimum. Positive nicht zertifizierte Ritz-Gaps beweisen nichts. Der neue `a_*`-Checker ist ein separater Arb-Zertifikatsgate und betrifft nur den short-window Schwellenwert.

## 10. Status

```text
COMMON-JUMP architecture                                  ✓[M]
Q0 first-channel intertwining                             ✓[M]
e^{-alpha a} higher-channel bound                         ✓[M]
short-window coercivity inside COMMON-JUMP                ✓[M]_part
short-window positivity as a new literature theorem       ×[M]
centered Prime-overlap decomposition                      ✓[M]
Q0 Sobolev transport of Prime overlap                     ✓[M]
finite multi-null Gamma ladder                            ✓[M] auxiliary
all-a NP-OVERLAP domination                               ?[O]
forward Object-X candidate architecture                   ✓[M]_part
full positive Object-X realization / RH                   ?[O]
publication novelty of the architecture                   ?[O]
```

PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten.