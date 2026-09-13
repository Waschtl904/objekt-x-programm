# Aktueller Stand — Objekt X / NP-DISCREPANCY

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Pole-cleared discrepancy](../audits/P11_NP_DISCREPANCY_POLE_CLEARED_CORRELATION_2026-09-13.md), [Prime-overlap AR(1)](../audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md).

## 1. Gesicherte Architektur

COMMON-JUMP und `Q_0` bleiben `✓[M]`. Auf Nullpol

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

Jeder vollständige Primzahlblock besitzt exakt die AR(1)-Faserform

```math
O_{p,a}^{(N)}=(\log p)(R_{p^{-1/2}}^{(N)}-I).
```

## 2. Methodischer No-Go

Die unabhängige Summe scharfer Einzelshift-Normen wächst mindestens wie

```math
2e^a(1+o(1)),
```

weil für `a<log n<2a` die komprimierte Shift-Norm exakt `1/2` ist. Rein skalare archimedische Untergrenzen plus unabhängige Shift-/Blocknormsummation können deshalb den all-window-Satz nicht beweisen.

Auch ein roher Prime-Multiplikator kombiniert nur mit einem `a`-unabhängigen Prolate-Konzentrationsfaktor beseitigt diese exponentielle Skala nicht.

## 3. Nullpol-Zentrierung des Prime-Maßes

Für

```math
C_v(t)=\langle T_tv,v\rangle
```

gilt auf Nullpol

```math
\boxed{
\int_0^{2a}2\cosh(t/2)\operatorname{Re}C_v(t)dt=0.
}
```

Definiere

```math
d\mathfrak D(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt)
-2\cosh(t/2)dt.
```

Dann exakt

```math
\boxed{
\mathcal O_a(v)=2\int\operatorname{Re}C_v(t)d\mathfrak D(t).
}
```

Die kumulative Diskrepanz

```math
\mathfrak D(T)
=\sum_{\log n\le T}\frac{\Lambda(n)}{\sqrt n}-4\sinh(T/2)
```

hat keinen exponentiellen PNT-Hauptterm mehr.

## 4. Pole-cleared Zeta-Struktur

Für `Re(s)>1/2`:

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{d}{ds}\log\left[(s^2-1/4)\zeta(s+1/2)\right].
}
```

Die Nullpol-Autokorrelation entfernt damit exakt die Polfaktoren `z=0,1` aus der Prime-Seite.

## 5. Neue Hauptfront

Durch Stieltjes-Integration:

```math
\boxed{
\mathcal O_a(v)
=-2\int_0^{2a}\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}C_v(t)dt.
}
```

Die aktive Frage lautet nun: Welche Sign-/Antikorrelationsstruktur erzwingt die positive-definite, kompakt getragene Autokorrelation gegen die pole-cleared Prime-Diskrepanz?

```text
NP-DISCREPANCY / NP-CORR    ?[O]
```

Polynomialer Wuchs von `D(T)` wäre bereits RH-hart; Ziel ist daher keine absolute Majorante, sondern eine strukturierte Korrelationsungleichung.

## 6. Status

```text
COMMON-JUMP / Q0                               ✓[M]
per-prime AR(1) fibers                        ✓[M]
independent shift/block norm-sum route        ×[M]
raw-amplitude constant-Prolate route          ×[M]
null-pole correlation gauge                   ✓[M]
pole-cleared Prime discrepancy                ✓[M]
NP-DISCREPANCY / anti-correlation             ?[O]
forward Object-X candidate                    ✓[M]_part
full positive Object-X / RH                   ?[O]
```
