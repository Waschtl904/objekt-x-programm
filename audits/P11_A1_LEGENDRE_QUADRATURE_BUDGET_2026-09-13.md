# P11 A1-LEGENDRE-QBUDGET — rigorous analytic quadrature budget for the final finite backend

**Date:** 2026-09-13  
**Status:** theorem-level analytic audit plus Exact-Head Arb constants; no Registry promotion.  
**Parent main:** `861a5026fe2d4465ffe8db0199e8ba7e31ea4175` / PR #117.  
**Registry:** unchanged.  
**Object-X working definition:** unchanged.

---

## 1. Purpose

PR #117 introduced an alternative orthonormal Legendre backend for the final `a=1` finite certificate.  The remaining finite task there is to prove, separately in the even and odd normalized Legendre sectors,

```math
L_{e}\succeq 10^{-35}I,
\qquad
L_{o}\succeq 10^{-35}I,
```

for blocks of dimension `1075` each.

Before assembling those matrices, one must know that the chosen numerical integration rule can resolve a `10^{-35}` spectral margin with a rigorous error budget.

This audit proves exactly that.  It fixes a concrete panel/Gauss rule and proves an a-priori operator-norm bound

```math
\boxed{
\|K-\widetilde K\|_{op}<4\times10^{-38}
}
```

for each parity block, where `K` is the exact bounded-band operator matrix and `K~` is the exact Gauss-rule matrix before finite-precision evaluation error.

Thus the analytic quadrature remainder is more than two orders of magnitude below the predeclared `10^{-35}` finite-head target.

This audit does **not** certify the final matrices themselves.  It removes only the analytic quadrature-remainder uncertainty.

---

## 2. Fixed A1 bounded operator

Use the already certified `a=1` reduction

```math
c=0.1,
\qquad
\Omega=1551,
```

and

```math
r(\xi)
=(m_1(\xi)-c)\mathbf 1_{[-\Omega,\Omega]}(\xi).
```

The bounded lower operator is

```math
L_1
=cI+K+\mathcal E^*\mathcal E,
```

where

```math
K=P_I\mathcal F^{-1}M_r\mathcal FP_I,
\qquad I=(-1,1).
```

The already merged Exact-Head gates prove on the real band

```math
\|r\|_\infty<12.
```

The present audit needs a complex-strip bound for the analytic continuation used by Gauss certification.

---

## 3. Normalized Legendre matrix formula

Let

```math
T_n(x)=\sqrt{n+\frac12}\,P_n(x),
\qquad -1<x<1.
```

Then

```math
\langle T_n,T_m\rangle=\delta_{nm}.
```

With the unitary Fourier convention,

```math
\widehat T_n(\xi)
=(-i)^n\sqrt{\frac{2(n+1/2)}{\pi}}\,j_n(\xi).
```

Since `r` is real and even, opposite parities decouple.  For equal parity,

```math
\boxed{
K_{nm}
=
\frac{4\sqrt{\nu_n\nu_m}}{\pi}
(-1)^{(m-n)/2}
\int_0^{\Omega}
r(\xi)j_n(\xi)j_m(\xi)\,d\xi,
}
```

where

```math
\nu_n=n+\frac12.
```

PR #117 uses orders `0,...,2149`, hence each parity block has dimension `1075`.

---

## 4. Analytic continuation of the multiplier

On the real axis the archimedean term is

```math
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right).
```

For complex `z`, use the analytic continuation

```math
\boxed{
D(z)
:=\frac12\left[
\psi\left(\frac14+\frac{iz}{2}\right)
+
\psi\left(\frac14-\frac{iz}{2}\right)
\right].
}
```

It agrees with the real part on real `z` and is analytic as long as neither digamma branch reaches a pole.

We work in the strip

```math
|\operatorname{Im}z|\le0.4.
```

Then for

```math
w_\pm=\frac14\pm\frac{iz}{2}
```

one has

```math
\operatorname{Re}w_\pm\ge0.05,
\qquad
|\operatorname{Im}w_\pm|\le775.5
```

on the full frequency range `0<=Re z<=1551`.

---

## 5. Rigorous digamma strip bound `✓[M]`

Shift

```math
u=w+20.
```

Then

```math
\operatorname{Re}u\ge20.05.
```

Binet's representation gives for `Re u>0`

```math
\psi(u)
=\log u-\frac1{2u}
-2\int_0^\infty
\frac{t}{t^2+u^2}\frac{dt}{e^{2\pi t}-1}.
```

Because

```math
|t^2+u^2|
=|t+iu|\,|t-iu|
\ge (\operatorname{Re}u)^2,
```

and

```math
\int_0^\infty\frac{t}{e^{2\pi t}-1}dt=\frac1{24},
```

we obtain

```math
\boxed{
|\psi(u)|
\le
|\log u|+
\frac1{2|u|}+
\frac1{12(\operatorname{Re}u)^2}.
}
```

On the present rectangle `|u|<776` and `|arg u|<pi/2`, hence conservatively

```math
|\log u|\le\log 776+\frac\pi2.
```

Finally the recurrence

```math
\psi(w)=\psi(w+20)-\sum_{k=0}^{19}\frac1{w+k}
```

and `Re w>=0.05` give

```math
|\psi(w)|
\le
\log776+\frac\pi2
+\frac1{2(20.05)}
+\frac1{12(20.05)^2}
+\sum_{k=0}^{19}\frac1{k+0.05}.
```

The Exact-Head Arb checker encloses this by

```text
31.72102304353538...
```

for each branch.  Therefore the half-sum `D(z)` obeys the same bound.

---

## 6. Prime comb strip bound `✓[M]`

For `|Im z|<=0.4`,

```math
|\cos(z\log n)|
\le\cosh(0.4\log n).
```

At `a=1` the active prime powers are

```text
2,3,4,5,7.
```

Thus the complete Prime cosine block satisfies

```math
\left|
2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(z\log n)
\right|
\le
2\sum_n\frac{\Lambda(n)}{\sqrt n}\cosh(0.4\log n).
```

The Exact-Head Arb enclosure is

```text
6.901485349908333...
```

Combining Sections 5 and 6 with `log pi` and `c=0.1` gives

```math
\boxed{|r(z)|<42}
```

throughout the analytic strip used below.  The actual certified bound is

```text
39.86723827929312...
```

Status: `✓[K/M]` for the numerical constant, conditional only on standard Arb elementary-function enclosures.

---

## 7. Spherical-Bessel complex bound `✓[M]`

The Poisson representation

```math
j_n(z)
=\frac{(-i)^n}{2}
\int_{-1}^{1}P_n(s)e^{izs}\,ds
```

and `|P_n(s)|<=1` on `[-1,1]` imply

```math
\boxed{
|j_n(z)|\le e^{|\operatorname{Im}z|}.
}
```

Hence on `|Im z|<=0.4`, for orders through `2149`,

```math
\left|
\frac{4\sqrt{\nu_n\nu_m}}{\pi}
 r(z)j_n(z)j_m(z)
\right|
\le
\frac4\pi(2149.5)e^{0.8}\cdot42.
```

The Arb gate certifies the conservative uniform bound

```math
\boxed{M_{int}<260000.}
```

The actual enclosed value is about `242828.3034`.

---

## 8. Fixed panel/Gauss rule and Bernstein ellipse `✓[M]`

Predeclare:

```text
panel width <= 0.4,
Gauss--Legendre order q=40.
```

The interval `[0,1551]` is covered by at most

```text
3878 panels.
```

For a full-width `0.4` panel, the affine half-width is `0.2`.  The complex strip height `0.4` therefore corresponds in normalized panel coordinates to Bernstein-ellipse semiminor

```math
b=\frac{0.4}{0.2}=2.
```

Thus

```math
\boxed{\rho=b+\sqrt{1+b^2}=2+\sqrt5.}
```

For an analytic function bounded by `M` on the Bernstein ellipse, the standard Gauss--Legendre estimate used in the compact-window literature gives

```math
\boxed{
|I-Q_q|
\le
\frac{4M\rho}{(\rho-1)(\rho^{2q}-1)}.
}
```

We deliberately omit the additional affine half-width factor; this only enlarges the bound and is therefore conservative.

With `M=260000`, `q=40`, `rho=2+sqrt5`, Arb certifies

```text
per-panel error < 9.483e-45.
```

Multiplying by `3878` panels gives

```math
\boxed{\varepsilon_{entry}<3.678\times10^{-41}.}
```

---

## 9. Matrix operator-norm budget `✓[K/M]`

Each parity block has dimension

```text
N_par=1075.
```

If every entry error has absolute value at most `eps_entry`, then

```math
\|E_Q\|_2
\le\sqrt{\|E_Q\|_1\|E_Q\|_\infty}
\le N_{par}\varepsilon_{entry}.
```

Therefore the Exact-Head Arb gate certifies

```math
\boxed{
\|E_Q\|_{op}
<3.954\times10^{-38}
<4\times10^{-38}.
}
```

This is more than a factor `250` below the predeclared finite-head target

```math
10^{-35}.
```

Thus analytic quadrature truncation is no longer a plausible precision obstruction for the #117 Legendre backend.

Status:

```text
complex strip multiplier bound |r|<42              ✓[K/M]
complex spherical-Bessel bound                       ✓[M]
Gauss-40 / width-0.4 analytic remainder theorem     ✓[M]
per-entry quadrature error <3.678e-41               ✓[K/M]
parity operator quadrature error <4e-38             ✓[K/M]
```

---

## 10. Interface to the final verified matrix certificate

Let `A` denote one exact parity block of the finite Legendre lower operator and let `A_tilde` be the matrix obtained from the fixed Gauss rule, with all special-function values evaluated numerically.

The present audit certifies only the **analytic quadrature remainder**

```math
\|A-A^{(Q)}\|_{op}<4\times10^{-38},
```

where `A^(Q)` means the exact-real-arithmetic Gauss matrix plus exact moment rank-one term.

The final certificate must additionally bound:

1. interval/special-function evaluation and rounding error `eps_eval`;
2. any matrix-storage / conversion error;
3. the residual of the verified factorization.

A sufficient architecture is:

```math
\widetilde A
-
\left(10^{-35}+\varepsilon_Q+\varepsilon_{eval}+\varepsilon_{res}\right)I
=R^*R+\Delta,
```

with a rigorously verified residual satisfying

```math
\|\Delta\|_{op}\le\varepsilon_{res}
```

and positive slack after all budgets are summed.

Equivalently one may work fully in Arb and require every pivot interval in a verified LDL/Cholesky factorization of

```math
A-10^{-35}I
```

to be strictly positive.  Any pivot containing zero is **undecided**, not positive.

This is exactly the discipline required by the project's anti-overpromotion firewall.

---

## 11. Relation to Zhu's computational architecture

Xuefeng Zhu, arXiv:2608.24827v2, uses the same broad certification pattern for compact-window matrices: orthonormal Legendre modes, panelwise Gauss--Legendre quadrature, a Bernstein-ellipse remainder bound, and a verified Cholesky residual.

This audit does **not** import Zhu's matrix data or certificate as proof input.  The present constants, strip bound, frequency band and final target are derived independently for the Object-X `a=1` bounded lower operator.

The project has also separately noted that the currently available arXiv source archive does not provide an executable verifier/matrix package usable as a dependency here.  The final Object-X finite certificate must therefore remain independently reproducible.

---

## 12. What remains `?[O]`

For the Legendre backend, after this audit only the following computational theorem gate remains:

```text
assemble both 1075x1075 parity matrices at sufficient precision
        |
bound special-function / rounding error
        |
verify A_even >= 1e-35 I and A_odd >= 1e-35 I
        |
combine with #117 Legendre tail/cross penalty
        |
canonical a=1 completion
```

The quadrature truncation itself is already certified to be far below the target.

The smaller `1212`-dimensional PSWF route remains the canonical finite reduction; this Legendre route is an explicit orthonormal certificate backend.

---

## 13. Status

```text
A1-FINITE-1212 canonical PSWF reduction                    ✓[K/M]
A1-LEGENDRE orthonormal backend M=2150                    ✓[K/M]
Legendre analytic quadrature budget                        ✓[K/M]
operator quadrature error <4e-38                           ✓[K/M]
final even 1075x1075 lower bound >=1e-35                   ?[O]
final odd 1075x1075 lower bound >=1e-35                    ?[O]
canonical a=1 completion                                   ?[O]
all-a NP-GAP / full Object X / RH                          ?[O]
```

## 14. Firewalls

Do not claim:

- the successful quadrature-budget gate certifies either finite matrix;
- the final arithmetic/special-function evaluation error is already bounded;
- a floating-point Cholesky factor is sufficient;
- the Legendre route supersedes the smaller PSWF reduction;
- fixed-window `a=1`, all-window NP-GAP, Object X or RH is proved.
