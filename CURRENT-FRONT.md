# CURRENT FRONT — Objekt X / COMMON-JUMP → NP-DISCREPANCY

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 13. September 2026; keine Registry-Promotion.  
> **Hauptaudits:** [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md) · [Prime-overlap AR(1)](audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md) · [Pole-cleared Prime discrepancy](audits/P11_NP_DISCREPANCY_POLE_CLEARED_CORRELATION_2026-09-13.md).

Registry und Objekt-X-Arbeitsdefinition bleiben unverändert.

## 1. Gesicherte Basis `✓[M]`

Auf

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

gilt

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

mit

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

COMMON-JUMP, die `Q_0`-Nullpolparametrisierung und die exakten per-prime AR(1)-Fasern bleiben `✓[M]`.

## 2. Einzelshift-/Blocknormsummation als all-window-Strategie ausgeschlossen `×[M]`

Für `S_t=(T_t+T_{-t})/2` gilt exakt

```math
\|S_t\|
=\cos\frac{\pi}{\lceil2a/t\rceil+1}.
```

Für `a<log n<2a` ist `||S_{log n}||=1/2`. Daher wächst die unabhängige Shift-Normsumme mindestens wie

```math
\sum_{e^a<n<e^{2a}}\frac{\Lambda(n)}{\sqrt n}
=2e^a(1+o(1)).
```

Dagegen kann jede rein skalare untere Schranke für den archimedischen Operator auf den wachsenden Räumen `D_NP(a)` höchstens durch einen festen Testvektor beschränkt sein. Somit kann

```text
archimedean scalar lower bound + independent shift/block norm sum
```

den all-window-Satz nicht beweisen.

Dasselbe gilt für eine rohe `Phi_a`-Amplitude kombiniert nur mit einem `a`-unabhängigen Prolate-Konzentrationsfaktor: ein konstanter Faktor beseitigt die exponentielle Skala nicht.

## 3. Nullpol-Autokorrelations-Gauge `✓[M]`

Setze

```math
C_v(t):=\langle T_tv,v\rangle.
```

Für Nullpolfunktionen gilt exakt

```math
\int_{\mathbb R}e^{t/2}C_v(t)dt
=E_-(v)\overline{E_+(v)}=0.
```

Da `C_v(-t)=overline{C_v(t)}`,

```math
\boxed{
\int_0^{2a}
2\cosh(t/2)\operatorname{Re}C_v(t)dt=0.
}
```

Damit darf auf `D_NP(a)` der glatte Maßanteil `2 cosh(t/2)dt` exakt aus dem Prime-overlap herauszentriert werden.

## 4. Pole-cleared Prime discrepancy `✓[M]`

Definiere

```math
d\nu(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt),
```

```math
\boxed{
d\mathfrak D(t)=d\nu(t)-2\cosh(t/2)dt.
}
```

Dann für jedes `v in D_NP(a)`:

```math
\boxed{
\mathcal O_a(v)
=2\int_0^\infty
\operatorname{Re}C_v(t)\,d\mathfrak D(t).
}
```

Die kumulative Diskrepanz ist

```math
\boxed{
\mathfrak D(T)
=\sum_{\log n\le T}\frac{\Lambda(n)}{\sqrt n}
-4\sinh(T/2).
}
```

Der PNT-Hauptterm `~2e^{T/2}` cancelt dadurch. Insbesondere

```math
\mathfrak D(T)=o(e^{T/2}).
```

## 5. Exakte Stieltjesform `✓[M]`

Weil `C_v(2a)=0` und `D(0)=0`,

```math
\boxed{
\mathcal O_a(v)
=-2\int_0^{2a}
\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}C_v(t)dt.
}
```

Der RH-harte Rest trennt sich damit in

```text
arithmetisch:  pole-cleared Prime discrepancy D(t)
analytisch:    derivative of a compactly-supported positive-definite autocorrelation
```

statt in eine exponentiell große rohe Prime-Summe.

## 6. Laplace transform = pole-cleared zeta logarithmic derivative `✓[M]`

Für `Re(s)>1/2`:

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{\zeta'}{\zeta}\left(s+\frac12\right)
-\frac1{s-1/2}-\frac1{s+1/2}.
}
```

Äquivalent

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{d}{ds}
\log\left[(s^2-1/4)\zeta(s+1/2)\right].
}
```

Die Nullpol-Zentrierung entfernt damit im Prime-Maß exakt die beiden Polfaktoren `z=0,1`.

## 7. RH-harte Skala `✓[K/M]`

Unter RH folgt klassisch

```math
\mathfrak D(T)=O(T^3).
```

Umgekehrt impliziert bereits irgendein polynomialer Bound

```math
\mathfrak D(T)=O(T^K)
```

für festes `K` den klassischen Fehlerterm

```math
\psi(x)=x+O(\sqrt x(\log x)^K)
```

und damit RH.

**Firewall:** Die Diskrepanz selbst polynomial zu majorisieren ist also bereits RH-hart. Der neue Gewinn ist die exakte Zentrierung und die richtige Korrelationsform, nicht eine Abkürzung um die harte Arithmetik.

## 8. Neue Default-Hauptfront — NP-DISCREPANCY / NP-CORR `?[O]`

Zu beweisen bleibt

```math
\boxed{
\mathcal A(v)
\ge
-2\int_0^{2a}
\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}C_v(t)dt
\quad(v\in D_{NP}(a)).
}
```

Priorität:

1. Sign-/Oszillationsstruktur von `D(t)` gegen positive-definite Autokorrelationen;
2. `Q_0`-Transport von `C_v'`;
3. per-prime AR(1) als lokale Zerlegung desselben Diskrepanzproblems;
4. Toeplitz/Paley-Wiener/Prolate nur auf der **zentrierten** Diskrepanz, nicht auf der rohen Prime-Amplitude;
5. vorab definierte Korrelations-Zeugen als Falsifikationsgate.

## 9. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
centered Prime-overlap                                ✓[M]
exact per-prime AR(1) fibers                         ✓[M]
independent shift/block norm-sum route               ×[M]
raw-amplitude × constant-Prolate route               ×[M]
null-pole cosh autocorrelation identity              ✓[M]
pole-cleared Prime discrepancy                       ✓[M]
Stieltjes discrepancy-correlation identity           ✓[M]
pole-cleared zeta log-derivative identity            ✓[M]
NP-DISCREPANCY / anti-correlation domination         ?[O]
forward Object-X candidate architecture              ✓[M]_part
full positive Object-X / RH                          ?[O]
```
