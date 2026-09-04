# P11 / R43 — BMIX external-review reconciliation and step-count firewall

**Date:** 2026-09-04  
**Scope:** destructive reconciliation of the post-BMIX external review against the frozen R43 definitions  
**Status:** local exact corrections/firewalls only; BMIX, COND, B-METINC, B-FLAGMOD, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6 remain OPEN

## 0. Governance

This audit does **not** import the external review's suggested Hilbert--Schmidt route, its claimed uniform bound on `||R_V||`, or its claimed `O(h)` total support size for COND without proof. It separates the valid structural observations from three quantitative overreaches.

The frozen residual operator is

\[
(R_Vf)(u)
=
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Vf(u)
\otimes \mathsf Q_V(u)\eta_{p,k},
\]

with

\[
B_V=(I+R_V^*R_V)^{-1},
\qquad
J_{p,V}(u)
=
\max\left\{0,
\left\lfloor\frac{2(V-|u|)_+}{\log p}\right\rfloor
\right\}.
\]

The already proved BMIX reduction remains

\[
\|Q_BB_VQ_I\|\le \|C_{V,U}B_V\|,
\qquad
C_{V,U}=R_VP-\widetilde P R_V.
\]

## 1. Accepted: the step-count firewall, with corrected arithmetic

Let a terminal partition be

\[
U_0<U_1<\cdots<U_N\asymp U,
\qquad
h_j:=U_{j+1}-U_j.
\]

For a constant mesh `h`, one has `N=Theta(U/h)`. Therefore a merely linear per-step bound

\[
\Omega_{m,j}\le \varepsilon_m h
\]

gives

\[
\sum_{j<N}\Omega_{m,j}
\lesssim
\varepsilon_m\frac Uh h
=
\varepsilon_m U,
\]

not `epsilon_m U/h`. Thus the external review's displayed multiplication contained an arithmetic typo, but its substantive warning is correct: **`O(h)` per step does not by itself yield a cofinal summable telescope.**

This matters because B-FLAGDYN/B-FLAGTIGHT takes the terminal horizon to infinity before the final `m -> infinity` tail limit can discharge a uniform majorant.

### Sufficient target shapes

A useful per-step theorem must carry more than strip thickness alone. Sufficient mechanisms include, for example:

1. a cofinal nonconstant mesh with
   \[
   \sum_j h_j=\infty,
   \qquad
   \sum_j h_j^\alpha<\infty
   \quad(\alpha>1),
   \]
   together with `Omega_{m,j} <= epsilon_m h_j^alpha` and `epsilon_m -> 0`;
2. genuine terminal decay `a(U_j)` with a summable cofinal majorant;
3. a direct global/telescoping energy estimate that avoids summing per-step operator norms.

Book only the firewall:

```text
R43-BMIX-STEP-COUNT-FIREWALL ✓[M]  (elementary summability obstruction)
```

It does **not** prove any BMIX decay.

## 2. Sharpened exact dead-layer threshold

Let

\[
\delta:=V-U>0.
\]

For almost every point in the outer strip `U<|u|<V`,

\[
0<V-|u|<\delta.
\]

If

\[
\boxed{\delta\le \frac12\log2,}
\]

then for every prime `p>=2`,

\[
\frac{2(V-|u|)}{\log p}
<
\frac{2\delta}{\log2}
\le1,
\]

so `J_{p,V}(u)=0` almost everywhere on the strip. Therefore

\[
\boxed{
\widetilde Q R_V=0,
\qquad
C_{V,U}P=0,
\qquad
C_{V,U}=-\widetilde P R_VQ
}
\]

holds for `0<delta<=log(2)/2` in the `L^2` sense.

The equality case is allowed because the only point at which the ratio can reach `1` for `p=2` is the boundary `|u|=U`, a null set for the multiplication projections.

Conversely, if

\[
\delta>\frac12\log2,
\]

then the set

\[
\{u: U<|u|<V-\tfrac12\log2\}
\]

has positive measure and satisfies `J_{2,V}(u)>=1`. Thus the universal dead outer layer fails on positive measure.

Hence the exact a.e. threshold is

\[
\boxed{\delta\le \frac12\log2.}
\]

This sharpens the earlier sufficient strict inequality without changing its validity.

Book:

```text
R43-RESIDUAL-DEAD-LAYER-SHARP ✓[M]
```

as a local frozen-definition sharpening only.

## 3. Rejected: the proposed Hilbert--Schmidt strip argument

The external review proposes a schematic identity of the form

\[
\|R_VQ_B\|_{HS}^2
\stackrel{?}{=}
\sum_{p,k}c_{p,k}^2
\int_{U<|u|<V}|\cdot|^2\,du
\]

and infers `O(h)` from strip measure. That passage is not valid for the frozen continuous `L^2` source operator.

The primitive pieces of `R_V` are translations (and differences of translations) followed by multiplication. A nonzero truncated translation

\[
T=M_AU_tM_B:L^2(\mathbb R)\to L^2(\mathbb R)
\]

on a positive-measure overlap is a partial isometry on an infinite-dimensional `L^2` subspace. In particular it is not compact and therefore not Hilbert--Schmidt. Equivalently, its distributional kernel contains a Dirac factor `delta(u-v-t)`, not an `L^2(du\,dv)` kernel.

Thus **thin support does not convert a translation channel into a Hilbert--Schmidt operator.** Channel weights and the mark Gram matrix may control an `L^2` square function or a quadratic form on particular vectors, but they do not justify the displayed HS norm formula.

Firewall:

```text
R43-BMIX-HS-STRIP-ROUTE ×[M]  (for the naive full-operator HS argument)
```

This is not a no-go for every Schatten/compactness argument after additional smoothing or finite-rank projection; it rejects only the proposed direct HS inference for the frozen translation operator.

## 4. Rejected: the claimed uniform `||R_V||=O(1)` from `sum_p log p p^{-3/2}`

The external review's proposed Schur estimate uses a prime summation with `p^{-3/2}` decay. That is not the frozen coefficient of `R_V`.

For `R_V`, the channel coefficient is

\[
\sqrt{\log p}\,p^{-k/4},
\]

so its squared `k=1` weight is

\[
\log p\,p^{-1/2},
\]

before the source-dependent cutoff and geometric interactions are used. The series

\[
\sum_p \log p\,p^{-1/2}
\]

does not converge. The stronger `p^{-3k/4}` coefficient belongs to the separate finite-prime operator `H_T`, not to the residual operator `R_V` used in BMIX.

Therefore the cited prime sum does **not** establish a `V`-uniform bound on `||R_V||`, and the Feshbach absorption cannot currently be downgraded to a mere constant improvement on that basis.

Status:

```text
uniform ||R_V||=O(1) from the proposed prime Schur sum: NOT PROVED
```

The exact Feshbach theorem remains valuable because it removes `||R_V||` without requiring any such uniform estimate.

## 5. COND localization: thin in density, not `O(h)` in total old-domain measure

The review correctly notices that the martingale depth changes on threshold layers inside the old interval, but its total-width count is too optimistic.

Fix a prime `p` and a fine increment `h=V-U<log(p)/2`. For `|u|<U`, write

\[
a_U(u):=\frac{2(U-|u|)}{\log p}.
\]

Then

\[
a_V(u)=a_U(u)+\frac{2h}{\log p},
\]

and `J_{p,V}(u)-J_{p,U}(u)=1` exactly where the fractional part of `a_U(u)` lies in an interval of length `2h/log p` adjacent to `1`.

As `|u|` runs from `0` to `U`, there are `Theta(U/log p)` threshold periods. Each affected radial layer has width `h`. Accounting for both signs of `u`, the union therefore has total measure

\[
\boxed{
|\mathcal A_{p;U,V}|
=
O\left(\frac{Uh}{\log p}+h\right),
}
\]

not `O(h)` uniformly in `U`.

Equivalently, the affected set has relative density `O(h/log p)` in the old interval. This is still useful structure, and the `1/log p` factor may interact favorably with prime weights, but **COND is not reduced to one fixed-width inner annulus.**

Accordingly BMIX and COND may still admit a common square-function/energy framework, but the external review has not yet supplied that theorem.

Status:

```text
COND threshold-layer localization: structurally valid
uniform total-width O(h) per prime: rejected
quantitative COND summability: OPEN
```

## 6. What remains genuinely useful from the external review

After correction, the durable lessons are:

1. the two-way BMIX defect has genuinely collapsed to the one-way conditioned channel
   \[
   -\widetilde P R_VQ B_V
   \]
   on dead-layer steps;
2. the mark Gram kernel gives exact geometric decay in the `k`-correlation direction;
3. the terminal mesh must be designed together with the summability target;
4. a full operator-norm or naive full-operator HS estimate is probably stronger than B-FLAGDYN actually needs;
5. the next attack should target the **actual scalar/flag increment or an `L^2` square-function energy on the relevant vectors**, preserving the `m`-tail factor from the beginning.

In particular, the preferred next target is not merely

\[
\|C_{V,U}B_V\|=O(h),
\]

but a directly summable estimate for the B-FLAGDYN increment, schematically

\[
\Omega_m(U,V)
\le
\varepsilon_m\,\omega(U,V),
\qquad
\varepsilon_m\to0,
\]

with a cofinal partition satisfying

\[
\sum_j\omega(U_j,U_{j+1})<\infty.
\]

This formulation places the `m`-tail mechanism before the terminal summation rather than hoping to recover it after a stronger global operator estimate.

## 7. Live tree after reconciliation

```text
B-METINC-GEO-BMIX [OPEN]
├─ R43-BMIX-FESHBACH-ABSORPTION ✓[M]
├─ R43-RESIDUAL-DEAD-LAYER ✓[M]
├─ R43-RESIDUAL-DEAD-LAYER-SHARP ✓[M]
├─ R43-RESIDUAL-MARK-GRAM ✓[M]
├─ R43-BMIX-STEP-COUNT-FIREWALL ✓[M]
├─ naive full-operator HS strip route ×[M]
└─ summable m-sensitive one-way BMIX estimate [OPEN]

B-METINC-COND [OPEN]
├─ threshold-layer localization [structural]
├─ relative affected density O(h/log p) per prime
└─ summable weighted COND estimate [OPEN]
```

All downstream gates remain OPEN. No freeze, no project-level promotion, and no Object-X/RH promotion are made.
