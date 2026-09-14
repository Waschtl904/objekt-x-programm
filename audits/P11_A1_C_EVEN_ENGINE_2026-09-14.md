# P11 A1 C-EVEN — verified assembly engine before the 1075x1075 factorization

**Date:** 2026-09-14  
**Status:** theorem-level assembly/error architecture plus engine preflight; **no C-even positivity claim**.  
**Parent main:** `a660aef4b99d50f07e04c03a51db52196347d262` / PR #121.  
**Registry / Object-X working definition:** unchanged.

## 1. Frozen C-even target

Nothing here changes the protocol frozen in PR #121:

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

The open theorem remains

```math
A_e\succeq10^{-35}I_{1075}.
```

The already certified analytic quadrature operator error is

```math
\varepsilon_Q<4\times10^{-38}.
```

## 2. Why a second assembly gate is needed

The fixed quadrature contains `3878*40 = 155120` positive-frequency nodes.  Literal interval outer-product accumulation at all nodes would be unnecessarily expensive.  We therefore separate a fast midpoint proposal from a rigorous operator error ledger.

## 3. Exact node form

For each positive Gauss node `x_s`, let

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

## 4. Nodewise perturbation lemma `✓[M]`

For point proposals `alpha0_s,b0_s` with

```math
|\alpha_s-\alpha^0_s|\le e_{\alpha,s},
\qquad
\|b_s-b^0_s\|_2\le e_{b,s},
```

and `B_s=||b0_s||`,

```math
\boxed{
\|\alpha_s b_sb_s^T-\alpha_s^0b_s^0(b_s^0)^T\|_{op}
\le
 e_{\alpha,s}(B_s+e_{b,s})^2
+|\alpha_s^0|(2B_se_{b,s}+e_{b,s}^2).
}
```

Hence

```math
\boxed{
\|K_e^{(Q)}-\widetilde K_e^{(Q)}\|_{op}\le\varepsilon_{eval}
}
```

with `epsilon_eval` equal to the sum of the displayed node bounds.  This allows fast midpoint outer products while all loss of rigor is paid explicitly in an operator-norm error budget.

## 5. Full finite error ledger

Keep separate

```math
\varepsilon_{tot}
=\varepsilon_Q
+\varepsilon_{eval}
+\varepsilon_{gemm}
+\varepsilon_{moment}
+\varepsilon_{storage}.
```

No BLAS/GEMM or storage error is silently absorbed into `epsilon_eval`.  A midpoint factorization must ultimately prove positivity after the complete shift

```math
10^{-35}+\varepsilon_{tot}.
```

## 6. Bessel engine: negative result and replacement

### 6.1 Pure downward Miller — engineering No-Go

Four exact-head preflight variants tested a single interval Miller recurrence propagated from a high order all the way to order `0`:

1. direct tiny high-order Arb anchors;
2. a continued-fraction ratio with a broad tail box;
3. adaptive Miller top plus analytic high-order tail;
4. an orderspecific fixed-point ratio bound and elementary `j_0,j_1` normalization.

All failed **fail-closed** because interval wrapping made the low-order Miller values contain zero at frequencies in the middle/high band.  This is not a mathematical counterexample and does not affect the Legendre backend.  It is an implementation-class negative result:

```text
one interval downward-Miller chain from n>>x to n=0  ×[engine]
```

No further tuning of this engine class is permitted in C-even.

### 6.2 Two-sided rigorous recurrence — active engine

Use the numerically natural split at the turning region `n≈x`.

**Low side.** Start with the elementary Arb formulas

```math
j_0(x)=\frac{\sin x}{x},
\qquad
j_1(x)=\frac{\sin x}{x^2}-\frac{\cos x}{x},
```

and propagate the exact recurrence upward through a deterministic overlap index below the turning region.

**High side.** Choose the already predeclared adaptive top above the turning region.  Enclose the recessive ratio by the backward continued fraction.  For `k>x`, use

```math
0<r_k=\frac{j_{k+1}(x)}{j_k(x)}\le q_k<1,
```

where

```math
q_k=
\frac{2x}{(2k+3)+\sqrt{(2k+3)^2-4x^2}}
```

is the small fixed point of the worst-case quotient map.  Propagate downward only into the overlap region.

**Glue.** At an overlap order where both rigorous intervals exclude zero, divide the upward value by the downward unnormalised value.  This interval quotient contains the exact scale factor.  Multiply the high-side vector by that scale.  Wherever both sides are available, intersect their intervals; non-overlap is a hard bug.

**Very high orders.** Above the represented Miller top use

```math
|j_n(x)|\le\frac{x^n}{(2n+1)!!}
```

as a symmetric interval around zero.

The two-sided construction prevents uncertainty in the recessive high-order solution from being propagated through the unstable low-order regime.

## 7. Moment block

The even moment vector is evaluated independently from the positive series for `i_n(1/2)`.  Its rank-one interval block is formed directly; its operator uncertainty is recorded as `epsilon_moment`.

## 8. Preflight scope

The preflight checks only:

1. the frozen Gauss rule and active prime-power mask;
2. two-sided Bessel vector enclosures at fixed representative nodes;
3. interval agreement in the overlap region and against independent direct Arb Bessel values at fixed orders;
4. even moment coefficients at low/mid/high orders;
5. parity/phasing and finite scalar weights.

Passing this gives only an engine status `✓[K/M]_part`.  It is not a truncated positivity result.

## 9. C-even acceptance unchanged

C-even is proved only when a later exact-head run produces the full `1075x1075` even-block enclosure and verifies

```math
A_e-10^{-35}I>0
```

by the frozen interval-congruence / fail-closed LDL or Cholesky protocol.  A zero-containing pivot or missing error-ledger term is `undecided`.

## 10. Status

```text
nodewise perturbation/operator-error lemma             ✓[M]
full C-even error-ledger architecture                  ✓[M]
pure downward interval Miller to order 0               ×[engine]
two-sided Bessel engine preflight                      ?[K/M]_part
full even matrix evaluation-error budget               ?[O]
C-even finite positivity A_e>=1e-35 I                  ?[O]
C-odd                                                  not started
fixed-window a=1                                       ?[O]
```
