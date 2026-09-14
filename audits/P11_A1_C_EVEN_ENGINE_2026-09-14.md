# P11 A1 C-EVEN — verified assembly engine before the 1075x1075 factorization

**Date:** 2026-09-14  
**Status:** theorem-level assembly/error architecture plus exact-head engine preflight; **no C-even positivity claim**.  
**Parent main:** `a660aef4b99d50f07e04c03a51db52196347d262` / PR #121.  
**Registry / Object-X working definition:** unchanged.

## 1. Frozen C-even target

The PR #121 protocol is unchanged:

```text
M = 2150
parity = even
dimension = 1075
target = 1e-35
Omega = 1551
panel width <= 0.4
Gauss-Legendre q = 40
analytic strip |Im xi| <= 0.4
precision ladder = 512,768,1024,1536,2048,3072 bits
```

Open theorem:

```math
A_e\succeq10^{-35}I_{1075}.
```

Already certified:

```math
\varepsilon_Q<4\times10^{-38}.
```

## 2. Exact node form

At a positive Gauss node `x_s`, define the 1075-dimensional even vector

```math
b_s=(b_{0,s},b_{2,s},\ldots,b_{2148,s})^T,
```

```math
b_{n,s}=(-1)^{n/2}\sqrt{\frac{4(n+1/2)}\pi}\,j_n(x_s),
\qquad
\alpha_s=w_s r(x_s).
```

Then

```math
K_e^{(Q)}=\sum_s\alpha_s b_sb_s^T,
```

and

```math
A_e^{(Q)}=0.1I+K_e^{(Q)}+2aa^T,
\qquad
a_n=2\sqrt{n+1/2}\,i_n(1/2).
```

## 3. Nodewise perturbation lemma `✓[M]`

For proposals `alpha0_s,b0_s` with

```math
|\alpha_s-\alpha_s^0|\le e_{\alpha,s},
\qquad
\|b_s-b_s^0\|_2\le e_{b,s},
```

and `B_s=||b_s^0||`,

```math
\boxed{
\|\alpha_s b_sb_s^T-\alpha_s^0b_s^0(b_s^0)^T\|_{op}
\le
 e_{\alpha,s}(B_s+e_{b,s})^2
+|\alpha_s^0|(2B_se_{b,s}+e_{b,s}^2).
}
```

Hence the sum of these node bounds is a rigorous `epsilon_eval` around any stored midpoint Gauss matrix.  Fast midpoint outer products are allowed only because every nodewise uncertainty is paid explicitly here.

## 4. Full finite error ledger

Keep separate

```math
\varepsilon_{tot}
=\varepsilon_Q
+\varepsilon_{eval}
+\varepsilon_{gemm}
+\varepsilon_{moment}
+\varepsilon_{storage}.
```

No BLAS/storage loss is silently absorbed.  A later midpoint factorization must prove positivity after the full shift

```math
10^{-35}+\varepsilon_{tot}.
```

## 5. Bessel-engine audit

### 5.1 Pure interval Miller / CF engines `×[engine]`

Multiple exact-head preflights tested a single high-to-low interval Miller chain and CF/Miller two-sided scaling.  They failed fail-closed from interval wrapping or inability to obtain a nonzero glue interval in the high-frequency part of the band.  This is only an implementation-class negative result:

```text
one long interval Miller/CF chain across the turning region  ×[engine]
```

It is not a mathematical statement about the Legendre backend.

### 5.2 Direct turning-anchor resolved core `✓[K/M]_part`

The successful preflight uses:

- low side: elementary Arb `j_0,j_1` and upward recurrence;
- direct high anchors at
  ```text
  n_hi ≈ x + 8 x^(1/3) + 16;
  ```
- downward recurrence only from those direct anchors through the turning region;
- interval intersection in the overlap zone.

At fixed Gauss nodes near `x=0.4,500,1000,1551`, the resolved-core intervals overlap independent direct Arb Bessel evaluations and the even moment-series samples are positive finite enclosures.

The naive per-component bound

```math
|j_n(x)|\le x^n/(2n+1)!!
```

above the turning anchor is valid but far too wide to feed `epsilon_eval`.  It is therefore **not** used for the final node-vector error.

## 6. New parity-energy identity `✓[M]`

The spherical-Bessel addition theorem is

```math
\sum_{n=0}^{\infty}(2n+1)j_n(x)^2P_n(\cos\theta)
=
j_0\!\left(2x\sin\frac\theta2\right).
```

At `theta=0`,

```math
\sum_n(2n+1)j_n(x)^2=1.
```

At `theta=pi`, since `P_n(-1)=(-1)^n`,

```math
\sum_n(-1)^n(2n+1)j_n(x)^2=j_0(2x).
```

Adding and dividing by two gives the exact even-sector identity

```math
\boxed{
\sum_{n\ \mathrm{even}}(2n+1)j_n(x)^2
=\frac{1+j_0(2x)}2.
}
```

Because

```math
|b_n(x)|^2=\frac{2(2n+1)}\pi j_n(x)^2,
```

the infinite normalized even vector has exact squared norm

```math
\boxed{
\|b_{\rm even}^{\infty}(x)\|_2^2
=\frac{1+j_0(2x)}\pi.
}
```

The finite C-even vector `n=0,2,...,2148` is a truncation, so the same quantity is a rigorous upper bound for its total norm.

## 7. Energy-tail node error `✓[M]`

Let `H_s` be any set of even orders whose Bessel values are sharply interval-enclosed, and let the midpoint proposal use their interval midpoints while setting all unresolved finite coordinates to zero.

For a resolved interval `J_n` with midpoint `m_n` and radius `rho_n`, the coordinate proposal error has absolute value at most

```math
c_n\rho_n,
\qquad
c_n=\sqrt{\frac{2(2n+1)}\pi}.
```

Thus

```math
E_{\rm head}^2
:=\sum_{n\in H_s}c_n^2\rho_n^2
```

bounds the squared resolved-coordinate error.

For each resolved coordinate define the rigorous lower absolute value

```math
\ell_n:=\max(0,|m_n|-\rho_n).
```

Then its true energy is at least `c_n^2 ell_n^2`.  Hence the squared norm of **all unresolved finite coordinates** is conservatively bounded by the infinite even energy remainder

```math
E_{\rm tail}^2
\le
\frac{1+j_0(2x_s)}\pi
-
\sum_{n\in H_s}c_n^2\ell_n^2.
```

(The right side also includes orders `n>=2150`, so it is conservative.)

Therefore

```math
\boxed{
 e_{b,s}
\le
\sqrt{E_{\rm head}^2+E_{\rm tail}^2}.
}
```

This replaces all huge individual high-order interval radii by a single exact parity-energy remainder.  It plugs directly into the nodewise perturbation lemma of §3.

## 8. Midpoint norm bound

For the same proposal,

```math
B_s^2=\|b_s^0\|_2^2
```

is computed from the stored resolved midpoints.  Independently,

```math
B_s\le\sqrt{\frac{1+j_0(2x_s)}\pi}
```

provides a rigorous sanity bound.

## 9. Moment block

The even moment vector is evaluated from the positive series for `i_n(1/2)`.  Its interval rank-one block is formed independently and its uncertainty is recorded as `epsilon_moment`.

## 10. Next exact gate

The C-even preflight must now report, at the four fixed representative Gauss nodes:

```text
B_s
e_b,s
resolved cutoff / turning anchors
```

using the parity-energy tail theorem rather than maximum individual tail radii.

Only if these `e_b,s` values are sufficiently small do we proceed to the global `155120`-node sharded `epsilon_eval` calculation.  No threshold or quadrature parameter is changed based on the result.

## 11. Final C-even acceptance unchanged

C-even is proved only by a later full `1075x1075` enclosure and verified interval congruence/LDL or Cholesky of

```math
A_e-10^{-35}I.
```

A zero-containing pivot or missing error-ledger term is `undecided`.

## 12. Status

```text
nodewise perturbation/operator-error lemma             ✓[M]
parity-energy identity / tail-error theorem            ✓[M]
long Miller/CF recurrence across turning region         ×[engine]
direct turning-anchor resolved-core preflight          ✓[K/M]_part
energy-tail e_b preflight                              ?[K/M]_part
global epsilon_eval                                    ?[O]
C-even finite positivity A_e>=1e-35 I                  ?[O]
C-odd                                                  not started
fixed-window a=1                                       ?[O]
```
