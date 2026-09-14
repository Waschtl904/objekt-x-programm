# P11 A1-OSIPOV1102 — analytic PSWF concentration bound and smaller finite reduction

**Date:** 2026-09-14  
**Status:** theorem-level analytic reduction plus candidate `✓[K/M]` constants pending final exact-head rerun.  
**Parent main:** `93ad38311f07c52c750d6903685a51f7b66df56f` / PR #118.  
**Registry / Object-X working definition:** unchanged.

## 1. Purpose

PR #115 reduced the canonical `a=1` completion problem to a moment-augmented PSWF space of at most `1212 = 606+606` dimensions using the Karnik--Romberg--Davenport concentration bound at `N=1210`.

This audit imports a simpler classical non-asymptotic estimate from Andrei Osipov and shows that the same Schur argument already works at

```text
N = 1102.
```

No PSWF eigenvector or Sturm--Liouville eigenvalue is numerically computed.

## 2. Imported Osipov theorem `✓[K/M]` source / `✓[M]` algebra

For the finite-Fourier operator

```math
(F_c f)(x)=\int_{-1}^1 f(t)e^{icxt}\,dt,
```

Osipov, *Certain upper bounds on the eigenvalues associated with prolate spheroidal wave functions*, arXiv:1206.4541, Theorem 4, proves

```math
|\lambda_n^F|\le \nu(n,c),
```

where

```math
\boxed{
\nu(n,c)=
\frac{\sqrt\pi\,c^n(n!)^2}
{(2n)!\,\Gamma(n+3/2)}.
}
```

For the standard time-band concentration operator

```math
Q_c=P_{[-1,1]}B_{[-c,c]}P_{[-1,1]},
```

Osipov's normalization gives

```math
\boxed{
\mu_n=\frac{c}{2\pi}|\lambda_n^F|^2.
}
```

Hence

```math
\boxed{
\mu_n\le
\frac{c}{2\pi}\nu(n,c)^2.
}
```

This is exactly the concentration eigenvalue convention used by the A1 Prolate tail/Schur audits.

## 3. Predeclared A1 parameters

Keep all previously certified PR #115 constants:

```text
frequency band c_PSWF = 1551
multiplier floor alpha = 0.1
||r||_infty < 12
Gamma_1 = 11.22465178357848...
resolved lower-bound target = 3e-39
```

Predeclare the new PSWF cutoff

```text
N = 1102.
```

The first `1102` PSWF modes consist of `551 even + 551 odd`; adding the two moment Riesz directions increases this by at most one in each parity sector:

```text
resolved dimension <= 1104 = 552 even + 552 odd.
```

## 4. Arb gate

The exact-head checker

```text
scripts/check_a1_osipov1102_arb.py
```

uses 256-bit Arb arithmetic to evaluate the closed Osipov expression and then the already proved Schur formulas.

On the precursor head `2f6902e5...` it certified

```text
nu_1102 upper          = 1.8592186560245302...e-23
mu_1102 upper          = 8.5328255475684722...e-44
tail tau lower         = 0.0999999999999999999999999999999999999999990...
Schur penalty upper    = 1.2287268788498600...e-40
```

Thus, once the final documented exact head reruns green,

```math
\boxed{\mu_{1102}(1551)<10^{-43},}
```

```math
\boxed{\tau_{1102}>0.099,}
```

and

```math
\boxed{\text{Schur penalty}<1.5\times10^{-40}.}
```

## 5. Consequence

The abstract moment-augmented Schur theorem from PR #114 gives the sufficient condition

```math
(L_1)_{RR}\succeq\mu_R I,
\qquad
\mu_R\ge
\frac{\|r\|_\infty^2\mu_{1102}}{\tau_{1102}}.
```

The already predeclared target

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I}
```

therefore remains sufficient with more than an order of magnitude of Schur clearance.

The canonical finite problem is reduced from at most `1212` to at most `1104` dimensions, with parity blocks of at most `552 x 552`.

## 6. Relation to the Legendre backend

PRs #117--#118 provide an independent orthonormal Legendre certificate backend:

```text
M=2150,
1075 even + 1075 odd,
Gram matrix exactly I,
analytic quadrature operator error <4e-38 per parity block.
```

That route is not superseded.  It remains a basis-explicit verification backend and a cross-check.  The Osipov reduction only sharpens the smaller canonical PSWF route.

## 7. Status before final exact-head rerun

```text
Osipov finite-Fourier theorem import                    ✓[K/M]
concentration conversion mu=c|lambda^F|^2/(2pi)       ✓[M]
N=1102 Schur algebra                                    ✓[M]
mu_1102<1e-43                                           candidate ✓[K/M]
Schur penalty <1.5e-40                                  candidate ✓[K/M]
1104-dimensional sufficient reduction                  candidate ✓[K/M]
resolved lower bound >=3e-39                            ?[O]
certified a=1 completion                                ?[O]
all-a NP-GAP / full Object X / RH                       ?[O]
```

## 8. Firewalls

Do not claim:

- the Osipov bound proves the finite resolved lower bound;
- the PSWF basis has been numerically constructed or interval-enclosed;
- `N=1102` is optimal;
- the alternative Legendre backend is obsolete;
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
