# P11 / R43 — epsilon-relaxed COND telescope front

**Date:** 2026-09-04  
**Status:** `?[O]` research front; parallel to structured-vector COND

## 0. Motivation

The exact kernel witness falsifies uniform eventual fine-step Loewner positivity, but it does not exclude a quantitative lower defect bound

\[
K_{U,V}^{\rm Schur}\succeq-\delta(U,V)I
\]

or a vector-sensitive analogue with a summable error along a chosen cofinal partition.

This route is therefore logically independent of exact PSD.

## 1. Exact target

With

\[
K_{U,V}^{\rm Schur}=C^*C-M^*\Phi_SM,
\qquad
\Phi_S=SS^*(I+SS^*)^{-1},
\]

seek either

\[
\boxed{K_{U,V}^{\rm Schur}\succeq-\delta(U,V)I}
\]

or, on the actual structured path,

\[
\boxed{
\langle v_U,K_{U,V}^{\rm Schur}v_U\rangle
\ge-\delta_X(U,V;f)
}
\]

with a cofinal partition `U_j` satisfying

\[
\sum_j\delta(U_j,U_{j+1})<\infty
\]

or the corresponding structured scalar sum.

## 2. What is not proved

The post-merge referee suggested a scale `\delta\sim Ue^{-U}` from the interval witness. That rate is **not currently justified**:

1. the witness chooses `h,ell` after a possibly very small resonance gap;
2. injectivity of `(I+S^*S)^(-1/2)` gives strict sign but no quantitative lower singular-value bound;
3. one negative Rayleigh witness yields an upper estimate on `lambda_min` in the negative direction, not a global lower bound `K>=-delta I`;
4. `||S||` grows cofinally, so unsaturated norm estimates are especially unreliable.

Therefore no decay rate is booked.

## 3. Why the route survives the no-go

The kernel theorem proves

\[
\forall U_*,h_*>0\ \exists\text{ a bad fine pair}.
\]

It does **not** prove:

- a uniform negative lower bound;
- that every sufficiently fine pair is bad;
- that a selected cofinal partition must hit bad pairs;
- that negative errors are nonsummable;
- negativity on the structured vector `v_U`.

Hence an epsilon-relaxed telescope remains logically open.

## 4. Preferred quantitative attacks

1. exploit the exact saturated factor `Phi_S`, never replace it by `SS^*`;
2. use the fixed-source prime-power shell localization for `v_U`;
3. seek scalar estimates before operator-norm estimates;
4. if an operator lower bound is attempted, first identify the relevant negative spectral subspace and prove a quantitative angle/weight estimate;
5. keep terminal step-count summability visible from the start.

## 5. Status

```text
R43-COND-PARTITION-SELECTIVE-PSD       ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE     ?[O]
B-METINC-COND                          OPEN
B-FLAGMOD                              OPEN
B-FLAGTIGHT                            OPEN
Strong Terminal/C6                     OPEN
```

No claimed `Ue^{-U}` rate, no positivity promotion, no freeze, no Object-X/RH promotion.
