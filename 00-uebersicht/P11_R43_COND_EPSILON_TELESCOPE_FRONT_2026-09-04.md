# P11 / R43 — epsilon-relaxed COND telescope front

**Date:** 2026-09-05  
**Status:** `?[O]` research front; parallel to structured-vector COND

## 0. Motivation

The strengthened two-prime kernel theorem now proves that **every sufficiently late terminal** has a right-hand punctured fine-step neighbourhood on which canonical arbitrary-source Loewner PSD fails:

\[
\exists U_0\ \forall U\ge U_0\ \exists h_0(U)>0\ \forall 0<h<h_0(U):
K_{U,U+h}^{\rm Schur}\not\succeq0.
\]

Source:

`audits/P11_R43_COND_TWO_PRIME_POINTWISE_LOCAL_NOGO_2026-09-05.md`

Exact PSD is therefore unavailable as an arbitrarily fine local increment principle at any late terminal. This still does not exclude a quantitative lower defect bound

\[
K_{U,V}^{\rm Schur}\succeq-\delta(U,V)I
\]

or a vector-sensitive analogue with summable error along a chosen cofinal partition.

---

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

---

## 2. What the witness gives — and the direction it gives it

The two-prime theorem gives an absolute `c_*>0` such that, for all sufficiently late `U`, its constructed forbidden radius can be chosen with

\[
h_0(U)\ge c_*e^{-4U}.
\]

Thus a canonical PSD step must satisfy the necessary condition

\[
K_{U,U+h}^{\rm Schur}\succeq0
\Longrightarrow
h\ge c_*e^{-4U}.
\]

This constrains any partition-selective PSD route but does not eliminate it.

For the epsilon route, a witness `f` with `Cf=0` gives

\[
\frac{\langle f,Kf\rangle}{\|f\|^2}
=-\frac{\|(I+S^*S)^{-1/2}S^*Mf\|^2}{\|f\|^2}<0.
\]

For each **fixed bounded** `S`, functional calculus yields

\[
(I+S^*S)^{-1}\succeq (1+\|S\|^2)^{-1}I,
\]

hence

\[
-\frac{\langle f,Kf\rangle}{\|f\|^2}
\ge
\frac{\|S^*Mf\|^2}{(1+\|S\|^2)\|f\|^2}.
\]

This is a **necessary lower size** for any defect majorant `delta` that is meant to dominate the whole negative part. It is not the required upper estimate.

---

## 3. The central open inequality

To prove an operator epsilon telescope one needs a bound in the opposite direction:

\[
\boxed{
\sup_{\|x\|=1}
\bigl(-\langle x,K_{U,V}^{\rm Schur}x\rangle\bigr)_+
\le \delta(U,V),
}
\]

with summable `delta` along a chosen cofinal partition.

Since

\[
K=C^*C-M^*\Phi_SM,
\qquad 0\preceq\Phi_S\preceq I,
\]

a crude bound is

\[
K\succeq-M^*M,
\]

but this is far too weak for terminal summability. The useful problem is to exploit the **saturated** projection `Phi_S` together with source/strip geometry, rather than estimate by `||M||^2`.

The structured-vector variant is weaker and may be more relevant:

\[
\bigl(-\langle v_U,Kv_U\rangle\bigr)_+
\le \delta_X(U,V;f).
\]

---

## 4. Strip-norm upper bound is now the useful norm question

Earlier work showed that shrinking strip width does not force `||(I-Pi)S||` to zero and that a `beta<1` criterion cannot provide the false exact-PSD conclusion.

For epsilon control, the strategically useful direction is different. A quantitative estimate on the resolvent factor may require an **upper**, not lower, bound on the strip block, e.g.

\[
\|S_{U,V}\|\le B(U,V)
\]

or, preferably, a direct bound on the saturated interaction

\[
\|\Phi_S^{1/2}M\|
\]

on the relevant structured/source-localized subspace.

Book only:

```text
R43-COND-STRIP-NORM-UPPER-BOUND ?[O]
```

No upper bound is currently proved.

---

## 5. Partition-selective PSD after the two-prime theorem

The node remains open:

```text
R43-COND-PARTITION-SELECTIVE-PSD ?[O]
```

but any sufficiently late PSD partition step must obey

\[
U_{j+1}-U_j\ge h_0(U_j)\ge c_*e^{-4U_j}.
\]

This floor is not contradictory to a cofinal fine partition: an exponentially small lower floor can coexist with `U_j->infty` and `U_{j+1}-U_j->0`.

Therefore the two-prime theorem does **not** justify upgrading this node to `×[M]`.

---

## 6. What is not proved

No theorem currently gives

\[
\delta(U,V)\sim Ue^{-U}
\]

or any other summable global operator rate. In particular:

1. a negative witness bounds `lambda_min` from above, not from below;
2. resolvent injectivity is qualitative; for fixed `S` there is a pointwise norm-dependent lower factor, but no useful uniform cofinal lower factor is booked;
3. the epsilon route requires an **upper bound on the entire negative part over all source vectors**;
4. negativity on the arbitrary-source witness does not imply negativity on the canonical structured vector `v_U`;
5. the new `e^{-4U}` quantity is a lower floor for the *step size of any PSD increment*, not a decay theorem for the negative spectral amplitude.

---

## 7. Preferred quantitative attacks

1. exploit `Phi_S` exactly; never replace it by unsaturated `SS^*`;
2. attack `\|\Phi_S^{1/2}Mv_U\|` and `\|Cv_U\|` on the actual structured vector;
3. seek a saturated strip/source estimate before a full `||S||` estimate;
4. if an operator lower bound is attempted, characterize the negative spectral subspace and its angle to the structured range;
5. keep terminal step-count summability visible from the first inequality.

---

## 8. Status

```text
R43-COND-TWO-PRIME-POINTWISE-LOCAL-NOGO  ✓[M]_neg
R43-COND-PARTITION-PSD-STEP-FLOOR        ✓[M] necessary only
R43-COND-PARTITION-SELECTIVE-PSD         ?[O]
R43-COND-STRIP-NORM-UPPER-BOUND          ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE       ?[O]
B-METINC-COND                            OPEN
B-FLAGMOD                                OPEN
B-FLAGTIGHT                              OPEN
Strong Terminal/C6                      OPEN
```

No claimed decay rate, no positivity promotion, no freeze, no Object-X/RH promotion.
