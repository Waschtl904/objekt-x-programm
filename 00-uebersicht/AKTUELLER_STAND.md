# Aktueller Stand — Objekt X / COMMON-JUMP → NP-GAP

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [COMMON-JUMP](../audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md), [Q0/short-window NP-GAP](../audits/P11_NP_GAP_Q0_FIRST_CHANNEL_2026-09-13.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md).

## 1. Gemeinsame Jump-Geometrie `✓[M]`

Für

```math
K_t=T_{t/2}-T_{-t/2}
```

entstehen Archimedes und Primzahlpotenzen aus derselben positiven Featurefamilie:

```math
\mu_a
=
\frac{e^{-t/2}}{1-e^{-2t}}dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
```

Mit

```math
\kappa_*=\log\pi-\psi(1/4)
=\log(8\pi)+\gamma+\frac\pi2,
```

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}+\kappa_*
```

gilt für jedes `a>0`

```math
Q_W(v,w)
=
\langle Ev,PEw\rangle
+
\langle X_av,X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
```

Auf der global RH-kompatiblen Nullpolklasse `D_NP=ker M(0) cap ker M(1)`:

```math
\boxed{
Q_W(v,w)
=
\langle X_av,X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

## 2. Archimedische Resolventenkanäle `✓[M]`

```math
\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m\ge0}e^{-\alpha_m t},
\qquad
\alpha_m=2m+\frac12.
```

Für

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_t\,dt
```

gilt exakt

```math
\boxed{
A_\alpha
=\frac{2}{\alpha}
(-\partial_x^2)(-\partial_x^2+\alpha^2)^{-1}.
}
```

## 3. Exakter `Q_0`-Treffer des ersten Kanals `✓[M]`

Mit

```math
Q_0=-\partial_x^2+\frac14
```

ist

```math
\boxed{
A_{1/2}=4I-Q_0^{-1},
\qquad
A_{1/2}Q_0=-4\partial_x^2.
}
```

Nur bei `alpha=1/2` cancelt der Resolventennenner in `A_alpha Q_0`. Damit ist die frühere `1/2`-Übereinstimmung ein exakter und in dieser Kanalfolge eindeutiger Intertwining-Satz.

## 4. Support-erhaltende Nullpolparametrisierung `✓[M]`

Der Green-Kern von `Q_0^{-1}` lautet

```math
G_0(x)=e^{-|x|/2}.
```

Für `supp(v) subset (-a,a)` sind die äußeren Tails proportional zu `E_+(v)` bzw. `E_-(v)`. Daher

```math
\boxed{
Q_0:C_c^\infty(-a,a)
\xrightarrow{\cong}
D_{NP}(a)
}
```

support-erhaltend.

Für `v=Q_0u` wird der erste nichtlokale Kanal exakt lokal:

```math
\boxed{
\langle v,A_{1/2}v\rangle
=4\|u''\|_2^2+\|u'\|_2^2.
}
```

## 5. Quantitative Schranken `✓[M]`

Dirichlet-Poincaré liefert auf Nullpol

```math
\boxed{
\langle v,A_{1/2}v\rangle
\ge
\frac{4\pi^2}{\pi^2+a^2}\|v\|_2^2.
}
```

Für jeden höheren Kanal und jedes auf `(-a,a)` getragene `v` ergibt der Schur-Test

```math
\boxed{
\langle v,A_\alpha v\rangle
\ge
\frac{2}{\alpha}e^{-\alpha a}\|v\|_2^2.
}
```

## 6. Short-window NP-GAP `✓[M]_part`

Definiere

```math
B(a)
=
\frac{4\pi^2}{\pi^2+a^2}
+
\sum_{m=1}^\infty
\frac{2}{\alpha_m}e^{-\alpha_m a}.
```

`B` ist stetig, streng fallend, `B(a)->infinity` für `a downarrow0` und `B(a)->0` für `a->infinity`. Sei `a_*` die eindeutige positive Lösung

```math
B(a_*)=\kappa_*.
```

Dann gilt für

```math
0<a<\min\{a_*,\tfrac12\log2\}
```

unkonditional

```math
\boxed{
\|X_av\|^2\ge\Gamma_a\|v\|_2^2
\qquad(v\in D_{NP}(a)).
}
```

Also ist der NP-GAP für einen nichtleeren Bereich ausreichend kleiner Fenster bewiesen.

## 7. Weiterhin offen

```math
\boxed{
\lambda_{NP}(a)\ge\Gamma_a
\quad\text{für alle }a>0
}
```

bleibt `?[O]`. Erst der all-`a`-Satz würde den verbleibenden globalen RH-äquivalenten Frame-Gap schließen.

## 8. Numerik-Firewall

Endlichdimensionale Ritz-Minima sind **obere** Schranken für das wahre Infimum. Die bisher während der Exploration genannten positiven Ritz-Gaps sind nicht Arb-zertifiziert und werden nicht promoted.

## 9. Status

```text
COMMON-JUMP common feature architecture       ✓[M]
Q0 first-channel intertwining                 ✓[M]
Q0 support-preserving null-pole map           ✓[M]
short-window NP-GAP                           ✓[M]_part
forward Object-X candidate architecture       ✓[M]_part
NP-GAP for every a>0                          ?[O]
full positive Object-X / RH                   ?[O]
publication novelty                           ?[O]
```

OX-GEN-A bleibt exakte Polschicht; POS-DIL #101--#105 bleibt auxiliary full-class geometry.