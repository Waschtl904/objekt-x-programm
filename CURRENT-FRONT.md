# CURRENT FRONT — Objekt X / A1-FINITE-1104

> **Stand:** 14. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudits:** [A1 Osipov N1102](audits/P11_A1_OSIPOV1102_REDUCTION_2026-09-14.md) · [A1 Omega1551](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md) · [A1 Legendre backend](audits/P11_A1_LEGENDRE_FINITE_CERTIFICATE_2026-09-13.md) · [Legendre quadrature budget](audits/P11_A1_LEGENDRE_QUADRATURE_BUDGET_2026-09-13.md).

## 1. Closed architecture

`COMMON-JUMP/Q0`, rank-2 completion, Morse/parity, canonical `lambda=1`, exact `a=1` Fourier multiplier and the moment-augmented Schur theorem remain `✓[M]`.

For

```math
m_1(\xi)=\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n),
```

Exact-Head Arb certifies

```math
m_1(\xi)>0.1\quad(|\xi|\ge1551),
\qquad
\|r\|_\infty<12,
```

for `r=(m_1-0.1)1_{[-1551,1551]}`.

## 2. Osipov analytic PSWF bound `✓[M] / ✓[K/M]`

Osipov Theorem 4 gives for the finite-Fourier eigenvalue

```math
|\lambda_n^F|\le
\nu(n,c)=\frac{\sqrt\pi c^n(n!)^2}{(2n)!\Gamma(n+3/2)}.
```

The concentration eigenvalue is

```math
\mu_n=\frac{c}{2\pi}|\lambda_n^F|^2.
```

At the predeclared values `c=1551`, `N=1102`, the 256-bit Exact-Head Arb gate certifies

```math
\boxed{\mu_{1102}<10^{-43}},
```

```math
\boxed{\tau_{1102}>0.099},
```

and

```math
\boxed{\text{Schur penalty}<1.5\times10^{-40}}.
```

The actual certified upper bound for the penalty is about `1.22873e-40`.

## 3. Canonical remaining finite theorem

The existing predeclared sufficient threshold remains

```math
\boxed{(L_1)_{RR}\succeq3\times10^{-39}I.}
```

The first `1102` PSWF modes split into `551 even + 551 odd`; moment augmentation adds at most one direction in each parity sector. Hence

```text
resolved dimension <=1104 = 552 even + 552 odd.
```

This is the **canonical smallest certified reduction**. The resolved lower bound itself remains `?[O]`.

## 4. Alternative orthonormal Legendre backend

PRs #117–#118 remain an independent explicit verification route:

```text
M=2150,
1075 even + 1075 odd,
Gram matrix exactly I,
finite target 1e-35.
```

The analytic Gauss-Legendre remainder is certified with per-parity operator error

```math
<4\times10^{-38}.
```

Open there are matrix assembly / special-function rounding and verified positive factorization. This route does not supersede the smaller PSWF route.

## 5. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
rank-2 completion / Morse / parity                    ✓[M]
Omega1551 multiplier floor / ||r||                    ✓[K/M]
Osipov theorem + concentration conversion             ✓[M]
N=1102 Arb concentration / Schur constants            ✓[K/M]
canonical finite reduction <=1104                     ✓[K/M]
canonical resolved lower bound >=3e-39                ?[O]
Legendre M=2150 backend                               ✓[K/M]
Legendre quadrature operator error <4e-38             ✓[K/M]
Legendre finite positivity                            ?[O]
certified a=1 completion                              ?[O]
all-a NP-GAP                                          ?[O]
forward Object-X candidate architecture               ✓[M]_part
full positive Object-X / RH                           ?[O]
```

## 6. Firewalls

- `3e-39` is a sufficient target, not a fitted eigenvalue.
- No PSWF eigenvector is certified or needed for the Osipov tail bound.
- The finite resolved lower bound is still open.
- Fixed-window `a=1`, all-window NP-GAP, Object X and RH remain open.
