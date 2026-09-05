# P11 / R43 — structured-vector COND front

**Date:** 2026-09-05  
**Status:** OPEN research front after elimination of the overstrong uniform Loewner/PSD helper route

**Companion reconciliation:** `audits/P11_R43_POSTMERGE_REFEREE_RECONCILIATION_2026-09-04.md`  
**Two-prime strengthening:** `audits/P11_R43_COND_TWO_PRIME_POINTWISE_LOCAL_NOGO_2026-09-05.md`  
**Parallel epsilon route:** `00-uebersicht/P11_R43_COND_EPSILON_TELESCOPE_FRONT_2026-09-04.md`

## 0. Exact negative input and corrected scope

Merged PR #53 established an explicit arbitrary-source direction `f` on arbitrarily late and arbitrarily fine selected terminal pairs such that

\[
C_{U,V}f=0,
\qquad
S^*Mf\ne0,
\]

and therefore

\[
\langle f,K_{U,V}^{\rm Schur}f\rangle<0.
\]

The theorem-level negative conclusions are:

```text
R43-COND-C-KERNEL-WITNESS-REALIZED             ✓[M]_neg
R43-COND-COFINAL-LOCAL-PSD                     ×[M]
R43-COND-CANONICAL-PSD-REALIZATION             ×[M]
R43-COND-UNIFORM-LOCAL-LOEWNER-TELESCOPE-ROUTE ×[M]
```

The older shorter label `LOEWNER-ANTITONE-TELESCOPE-ROUTE ×[M]` is scope-corrected to the **uniform-local** route.

### 0.1 Two-prime strengthening

The exact `p=2,3` argument sharpens the arbitrary-source no-go to

\[
\boxed{
\exists U_0>0\ \forall U\ge U_0\ \exists h_0(U)>0\ \forall 0<h<h_0(U):
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\]

Thus every sufficiently late terminal has a punctured right neighbourhood containing **only non-PSD arbitrary-source canonical COND steps**.

The same audit gives a nonoptimal absolute `c_*>0` with

\[
h_0(U)\ge c_*e^{-4U}
\]

for all sufficiently late `U`. Hence any actually PSD canonical step must satisfy

\[
K_{U,U+h}^{\rm Schur}\succeq0
\Longrightarrow
h\ge c_*e^{-4U}.
\]

Bookings:

```text
R43-COND-TWO-PRIME-POINTWISE-LOCAL-NOGO ✓[M]_neg
R43-COND-PARTITION-PSD-STEP-FLOOR       ✓[M] necessary only
```

This still does not exclude a specially selected good partition, because the local forbidden radius may shrink. Therefore

```text
R43-COND-PARTITION-SELECTIVE-PSD ?[O]
```

remains open.

The strict referee's proposed `co-countable U / all h>0` statement is not adopted; the kernel construction uses a genuine fine-step dead-layer/one-new-layer regime.

This is elimination and strengthening of an overstrong arbitrary-source helper route, not a Strong-Terminal or `B-METINC-COND` no-go.

## 1. Provenance of the actual structured target — pre-no-go

The structured vector is not introduced after the negative result. It was already fixed in

```text
ca370c6b95c0a454da82376bc82b9e2261113e0d
```

commit message:

```text
R43: audit terminal metric increments before shell reindexing
```

in file

`audits/P11_R43_TERMINAL_METRIC_INCREMENT_DEFINITION_AUDIT_2026-09-04.md`.

There equation `(MI12)` defines

\[
\boxed{v_T(f):=H_T^*E_{X,T}f\in L^2(-T,T)}
\]

and `(MI15)` identifies canonical old-conditioning as

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
=\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle.
}
\]

Thus this branch returns to the originally frozen scalar path; it is not an ad-hoc restriction invented after the arbitrary-source no-go.

## 2. Actual structured target

For fixed source `X<U<V`, the live target is vector-sensitive rather than operator order:

\[
\boxed{
\bigl|\Delta s_{\rm cond}^{U,V}(f)\bigr|
\le \Omega_X(U,V;f)
}
\]

with a cofinal summability mechanism compatible with B-FLAGDYN and preferably an `m`-tail factor before terminal summation.

A merely qualitative statement such as `Cv_U\ne0` is not enough. The exact competition is quantitative.

## 3. Exact signed split retained

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

Old-source residual nesting gives

\[
\widehat B_{U;V}-B_U\preceq0,
\]

while the source-strip Schur correction satisfies

\[
\iota^*B_V\iota-\widehat B_{U;V}\succeq0.
\]

Therefore on `v_U`

\[
\Delta s_{\rm cond}^{U,V}
=-\mathcal E_{\rm inner}(U,V)
+\mathcal E_{\rm Schur}(U,V),
\qquad
\mathcal E_{\rm inner},\mathcal E_{\rm Schur}\ge0.
\]

The problem is quantitative control of the two scalar energies, not a global operator sign.

## 4. Preferred frozen inputs

### 4.1 Fixed-source `H` structure

\[
H_U
=P_U\sum_{p^k\le e^{2U}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_U.
\]

Hence `v_U=H_U^*E_{X,U}f` is generated from the fixed source window by prime-power translations and is highly non-arbitrary.

### 4.2 Fixed-source localization

\[
D_{k\log p}E_Xf(u)\ne0
\Longrightarrow
\left||u|-\frac{k\log p}{2}\right|<X.
\]

Interaction with a terminal threshold near `U` therefore forces contributing prime powers into a fixed multiplicative shell around the terminal scale.

### 4.3 H/R first-martingale coefficient match

Residual coefficient:

\[
\sqrt{\log p}\,p^{-k/4}.
\]

First martingale layer factor:

\[
\sqrt{p-1}\,p^{-k/2}.
\]

After division by `\sqrt{p-1}`, their product is

\[
\sqrt{\log p}\,p^{-3k/4},
\]

exactly the hub coefficient. This is coefficient-level only; no full factorization `H=LR` is assumed.

## 5. Referee-hardened quantitative questions

The next calculations must answer, in order:

1. For `v_U=H_U^*E_{X,U}f`, determine the exact shell/support of `Cv_U`.
2. Determine the exact shell/support of `S^*Mv_U`.
3. Test whether the artificial interval-kernel mechanism can occur on the structured range of `H_U^*E_{X,U}`.
4. Quantify, not merely sign-test,
   \[
   \|Cv_U\|^2
   \quad\text{versus}\quad
   \langle Mv_U,\Phi_SMv_U\rangle.
   \]
5. Reduce both signed pieces to a common fixed-source shell sum if possible.
6. Insert any `m`-tail mechanism before the terminal summation.

Because `||S||` grows cofinally, no argument may infer positivity merely from `Cv_U\ne0`; the Feshbach term must be controlled with the saturated `\Phi_S`.

## 6. Success criterion

Useful theorem shapes include

\[
|\Delta s_{\rm cond}^{U,V}(f)|
\le a_X(U,V)\|f\|_{\mathcal X_X}^2,
\qquad
\sum_j a_X(U_j,U_{j+1})<\infty,
\]

or preferably

\[
|\Delta s_{\rm cond,m}^{U,V}(f)|
\le \varepsilon_m a_X(U,V)\|f\|^2,
\qquad
\varepsilon_m\to0,
\]

with the same cofinal summability.

No full operator-norm estimate is required unless it falls out for free.

## 7. Parallel epsilon-relaxed route

Exact PSD is not necessary. A separate open route is

\[
K_{U,V}^{\rm Schur}\succeq-\delta(U,V)I
\]

or a structured-vector analogue with summable `\delta` along a chosen partition.

The two-prime theorem does not produce the required upper bound on the whole negative part. It only supplies negative directions and a necessary floor for any exact-PSD step. Thus book only

```text
R43-COND-EPSILON-RELAXED-TELESCOPE ?[O]
R43-COND-STRIP-NORM-UPPER-BOUND     ?[O]
```

No `Ue^{-U}` or other negative-spectrum decay rate is currently proved.

## 8. Governance

- `B-METINC-COND`: OPEN.
- `R43-COND-CANONICAL-PSD-REALIZATION`: `×[M]` for the universal/pairwise claim.
- `R43-COND-COFINAL-LOCAL-PSD`: `×[M]` for the uniform eventual-fine-step claim.
- `R43-COND-UNIFORM-LOCAL-LOEWNER-TELESCOPE-ROUTE`: `×[M]`.
- `R43-COND-TWO-PRIME-POINTWISE-LOCAL-NOGO`: `✓[M]_neg`.
- `R43-COND-PARTITION-PSD-STEP-FLOOR`: `✓[M]` necessary only.
- `R43-COND-PARTITION-SELECTIVE-PSD`: `?[O]`.
- `R43-COND-EPSILON-RELAXED-TELESCOPE`: `?[O]`.
- structured-vector signed/absolute COND: OPEN.
- `B-METINC-NORMMIX`, GEO-BMIX/BDRY, NEW, FD23-UNIF, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6: OPEN.
- R43 remains OPEN; no freeze and no formal independent GREEN.
- no Object-X/RH promotion.
