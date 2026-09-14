# P11 A1 C-EVEN — verified assembly engine before the 1075x1075 factorization

**Date:** 2026-09-14  
**Status:** theorem-level assembly/error architecture plus preflight; **no C-even positivity claim**.  
**Parent main:** `a660aef4b99d50f07e04c03a51db52196347d262` / PR #121.  
**Registry / Object-X working definition:** unchanged.

## 1. Frozen C-even target

Nothing in this audit changes the protocol frozen in PR #121:

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

The theorem to be certified later remains

```math
A_e\succeq10^{-35}I_{1075}.
```

The already certified analytic quadrature operator error is

```math
\varepsilon_Q<4\times10^{-38}.
```

## 2. Why a second assembly gate is needed

The fixed quadrature has `3878*40 = 155120` positive-frequency nodes.  A literal interval rank-one update of a `1075x1075` Arb matrix at every node would require an impractical number of interval scalar products.  This is a certification-engineering issue, not a mathematical change.

The proof-safe alternative is to separate

1. a fast midpoint proposal, which has no proof status;
2. rigorous nodewise enclosures of the scalar quadrature coefficient and Legendre-Fourier vector;
3. a theorem converting those nodewise errors into an operator-norm enclosure for the whole matrix;
4. an Arb interval matrix obtained by inflating the midpoint matrix by that proved operator budget;
5. the already frozen interval congruence / Cholesky stage.

## 3. Exact node form

For an even Gauss node `x_s>0`, let

```math
b_s=(b_{0,s},b_{2,s},\ldots,b_{2148,s})^T,
```

where

```math
b_{n,s}=(-1)^{n/2}\sqrt{\frac{4(n+1/2)}\pi}\,j_n(x_s).
```

Let `w_s>0` be the affine Gauss weight and

```math
\alpha_s=w_s r(x_s).
```

Then the Gauss approximation of the bounded-band block is exactly

```math
K_e^{(Q)}=\sum_s\alpha_s b_s b_s^T.
```

The full finite even block is

```math
A_e^{(Q)}=0.1I+K_e^{(Q)}+2aa^T,
```

with

```math
a_n=2\sqrt{n+1/2}\,i_n(1/2).
```

## 4. Nodewise perturbation lemma `✓[M]`

Suppose for each node we have point proposals `alpha0_s`, `b0_s` and rigorous bounds

```math
|\alpha_s-\alpha^0_s|\le e_{\alpha,s},
\qquad
\|b_s-b^0_s\|_2\le e_{b,s}.
```

Put

```math
B_s=\|b_s^0\|_2.
```

Then

```math
\|\alpha_s b_sb_s^T-\alpha_s^0b_s^0(b_s^0)^T\|_{op}
\le
 e_{\alpha,s}(B_s+e_{b,s})^2
+|\alpha_s^0|(2B_se_{b,s}+e_{b,s}^2).
```

**Proof.** Split

```math
\alpha bb^T-\alpha_0b_0b_0^T
=(\alpha-\alpha_0)bb^T
+\alpha_0(bb^T-b_0b_0^T).
```

Use `||bb^T||=||b||^2`, `||b||<=B+e_b`, and with `d=b-b0`,

```math
bb^T-b_0b_0^T=b_0d^T+db_0^T+dd^T,
```

whose operator norm is at most `2 B e_b+e_b^2`.  ∎

Therefore

```math
\boxed{
\|K_e^{(Q)}-\widetilde K_e^{(Q)}\|_{op}
\le\varepsilon_{eval}
:=\sum_s
\left[
 e_{\alpha,s}(B_s+e_{b,s})^2
+|\alpha_s^0|(2B_se_{b,s}+e_{b,s}^2)
\right].
}
```

This theorem removes the need to perform all outer products in interval arithmetic.  Only the **nodewise vector enclosure** and the scalar error sum need be rigorous.  The midpoint matrix may be produced by a fast dense backend because its lack of proof status is absorbed by `epsilon_eval`.

## 5. Midpoint linear-algebra rounding firewall

If the midpoint outer-product sum is itself accumulated in ordinary floating arithmetic, its matrix-rounding error must be bounded separately by `epsilon_gemm`.  It is **not** silently included in `epsilon_eval`.

The final exact Gauss matrix enclosure must satisfy

```math
\|K_e^{(Q)}-\widetilde K_{e,\rm stored}\|_{op}
\le \varepsilon_{eval}+\varepsilon_{gemm}.
```

A proof run may instead use a dyadic/high-precision midpoint accumulator for which `epsilon_gemm` is certified by an exact residual replay.  No BLAS result is accepted without an explicit rounding/error ledger.

## 6. Full finite error ledger

Let

```math
\varepsilon_{tot}
=\varepsilon_Q
+\varepsilon_{eval}
+\varepsilon_{gemm}
+\varepsilon_{moment}
+\varepsilon_{storage}.
```

The final factorization may use an interval matrix centered at the stored midpoint with an operator inflation at least `epsilon_tot`.  Equivalently, if a factorization is checked against the midpoint matrix, the shift must include the whole error budget:

```math
\widetilde A_e-
(10^{-35}+\varepsilon_{tot})I.
```

No component may be inferred from observed pivots.  All budgets are computed independently of the positivity outcome.

## 7. Bessel vector certification plan

For every fixed Gauss node the exact `b_s` vector is enclosed by Arb using the two regimes frozen in PR #121:

- `0<x<=1`: entire `0F1` representation;
- `x>1`: high-order Arb anchor pair plus downward three-term recurrence and a deterministic normalization pivot.

The preflight checks the implementation at fixed frequency locations spanning the complete band.  The final run must fail closed if an anchor/pivot interval contains zero or any enclosure becomes non-finite.

The vector error `e_b,s` is the Euclidean norm of the radii plus the exact difference between the stored dyadic/double proposal and the Arb midpoint point used to define the enclosure.

## 8. Moment block

The even moment vector is evaluated independently from the positive series for `i_n(1/2)`.  Its interval outer product is rank one.  Because it costs only `O(N^2)` once rather than once per Gauss node, it may be formed directly in Arb.  Its resulting operator uncertainty is recorded as `epsilon_moment`.

## 9. Preflight scope

The preflight is deliberately **not** a truncated positivity test.  It checks only:

1. fixed Gauss rule generation;
2. exact active prime-power mask `{2,3,4,5,7}`;
3. Bessel vector enclosure at predeclared representative nodes;
4. even moment coefficients at low/mid/high orders;
5. deterministic parity/phasing conventions;
6. finiteness and enclosure overlap against an independent direct Arb Bessel evaluation for selected orders.

Passing the preflight gives the assembly engine status `✓[K/M]_part`; it does not change `C-even ?[O]`.

## 10. C-even acceptance remains unchanged

C-even is proved only when a later exact-head run produces the full `1075x1075` even block enclosure and verifies

```math
A_e-10^{-35}I>0
```

by the frozen interval-congruence / fail-closed Cholesky or LDL protocol.

A zero-containing pivot, missing error ledger component, or non-finite special-function enclosure is `undecided`.

## 11. Status

```text
nodewise perturbation/operator-error lemma             ✓[M]
full C-even error-ledger architecture                  ✓[M]
C-even Bessel/moment engine preflight                  ?[K/M]_part
full even matrix evaluation-error budget               ?[O]
C-even finite positivity A_e>=1e-35 I                  ?[O]
C-odd                                                  not started
fixed-window a=1                                       ?[O]
```
