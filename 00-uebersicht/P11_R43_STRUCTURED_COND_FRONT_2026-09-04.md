# P11 / R43 — structured-vector COND front

**Date:** 2026-09-04  
**Status:** OPEN research front after theorem-level closure of the arbitrary-source Loewner/PSD route

## 0. Frozen negative input

The merged PR #53 established, for arbitrarily late and arbitrarily fine generic terminal pairs, an explicit source direction `f` with

\[
C_{U,V}f=0,
\qquad
S^*Mf\ne0,
\]

and therefore

\[
\langle f,K_{U,V}^{\rm Schur}f\rangle<0.
\]

Hence the following are frozen negative route decisions:

```text
R43-COND-COFINAL-LOCAL-PSD                  ×[M]
R43-COND-CANONICAL-PSD-REALIZATION          ×[M]
R43-COND-LOEWNER-ANTITONE-TELESCOPE-ROUTE   ×[M]
```

This front must not reopen those arbitrary-source claims.

## 1. Actual structured target

For fixed source `X<U<V`, canonical SW14 uses

\[
v_U:=H_U^*E_{X,U}f,
\]

inside

\[
\Delta s_{\rm cond}^{U,V}(f)
=
\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle.
\]

The live target is a vector-sensitive estimate, not operator order:

\[
\boxed{
\bigl|\Delta s_{\rm cond}^{U,V}(f)\bigr|
\le \Omega_X(U,V;f)
}
\]

with a cofinal summability mechanism compatible with the B-FLAGDYN / `m`-tail route.

## 2. Exact signed split retained

The pre-existing comparator

\[
\widehat B_{U;V}
=(I+\iota^*R_V^*R_V\iota)^{-1}
\]

gives

\[
\iota^*B_V\iota-B_U
=(\widehat B_{U;V}-B_U)
+(\iota^*B_V\iota-\widehat B_{U;V}).
\]

The first term is nonpositive by old-source residual nesting.  The second is nonnegative and is the source-strip Schur correction.  The total has no fixed sign.

Thus the structured-vector scalar splits as

\[
\Delta s_{\rm cond}^{U,V}
=
-\mathcal E_{\rm inner}(U,V)
+\mathcal E_{\rm Schur}(U,V),
\]

with both energies nonnegative on the fixed vector `v_U`.

The new problem is quantitative cancellation/control of these two scalar energies, not a Loewner comparison between the operators.

## 3. Preferred frozen inputs

### 3.1 Fixed-source `H` structure

\[
H_U
=P_U\sum_{p^k\le e^{2U}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_U.
\]

Hence `v_U=H_U^*E_{X,U}f` is not arbitrary.  Every source component of `v_U` is generated from the fixed window `(-X,X)` by prime-power translations.

### 3.2 Fixed-source localization

For a translated fixed-source component,

\[
D_{k\log p}E_Xf(u)\ne0
\Longrightarrow
\left||u|-\frac{k\log p}{2}\right|<X.
\]

Thus interaction with a terminal threshold near `U` forces the contributing prime-power data into a fixed multiplicative shell around the terminal scale.

### 3.3 H/R first-martingale coefficient match

The residual coefficient is

\[
\sqrt{\log p}\,p^{-k/4},
\]

and the first martingale layer contributes

\[
\sqrt{p-1}\,p^{-k/2}.
\]

After division by `\sqrt{p-1}`, their product is exactly the hub weight

\[
\sqrt{\log p}\,p^{-3k/4}.
\]

This coefficient-level alignment is a preferred structural input.  A full operator factorization `H=LR` is **not** assumed until proved.

## 4. First quantitative questions

The next audit should answer, in order:

1. For `v_U=H_U^*E_{X,U}f`, what is the exact support/prime-power shell of `Cv_U`?
2. What is the exact support/prime-power shell of `S^*Mv_U`?
3. Does the structured path eliminate the arbitrary-source kernel witness mechanism automatically?
4. Can both signed pieces be reduced to the same fixed-source shell sum, so that their difference or absolute sum gains a terminal-decaying coefficient?
5. Can the resulting scalar bound be made `m`-tail sensitive **before** terminal summation?

## 5. Success criterion

A useful theorem should look like one of:

\[
|\Delta s_{\rm cond}^{U,V}(f)|
\le a_X(U,V)\,\|f\|_{\mathcal X_X}^2,
\]

with a cofinal partition satisfying

\[
\sum_j a_X(U_j,U_{j+1})<\infty,
\]

or, preferably for B-FLAGDYN,

\[
|\Delta s_{\rm cond,m}^{U,V}(f)|
\le \varepsilon_m\,a_X(U,V)\,\|f\|^2,
\qquad
\varepsilon_m\to0,
\]

with the same summability.

No full operator-norm estimate is required unless it falls out for free.

## 6. Governance

- `B-METINC-COND`: OPEN.
- arbitrary-source/eventual Loewner PSD: frozen `×[M]`; do not reopen.
- `B-METINC-NORMMIX`, GEO-BMIX/BDRY, NEW, FD23-UNIF, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6: OPEN.
- R43 remains OPEN; no freeze and no formal independent GREEN.
- no Object-X/RH promotion.
