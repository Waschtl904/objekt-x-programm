# P11 / R43 — shellwise collar refinement and common-mode obstruction

**Date:** 2026-09-06  
**Status:** exact/local reduction on top of PR #78; no reverse-normal decay claim  
**Exact parent head:** `a9d1f1a944bbb154db7bdb5844135501630bda5c`

## 0. Purpose and firewall

PR #78 shows, in the primitive denominator-normalized occupancy model, that the mean-channel kernel has an opposite-boundary layer of the form

\[
\omega_U^{U,V}(u)\lesssim L\left(e^{-(U-u)/2}+e^{-(U+u)/2}\right),
\qquad L:=V-U,
\tag{SC0}
\]

up to fixed-band/end-point constants in the local primitive model.

The crude estimate by `||omega||_infty` loses a factor of order `U` on a dyadic step.  A natural proposed repair is to combine the exponential kernel with a shellwise version of the PR-#64 collar escape estimate instead of using one whole collar at once.

This note records the exact outcome of that refinement:

1. PR #64 already gives the needed collar estimate for every admissible radius `r`, hence a shellwise distribution bound is available essentially for free.
2. Integrating that sharp universal distribution bound against the exponential boundary kernel improves the crude `O(log U)` estimate to `O((V-U)/U)`.
3. On a geometric/dyadic step `V-U \asymp U`, this is only `O(1)`, not the target `O(log U/U)`.
4. The universal `r/U` collar scale cannot be improved without extra structure: the normalized constant residual-difference mode saturates it.

Thus shell refinement alone does **not** close the reverse mean channel.  The next useful question is whether the actual structured reverse-normal vector excludes or suppresses the constant/common mode, or whether one must use the exact two-sided Schur/least-squares correlations rather than a positive occupancy majorant.

No theorem about parity, common-mode elimination, reverse-normal decay, FD23, FLAGDYN, Strong Terminal/C6, Object X, or RH is asserted here.

---

## 1. PR #64 is already uniform in the collar radius

PR #64 proves for every sufficiently large admissible `r` with `r <= U/8`

\[
\boxed{
\|\chi_{U,r}x\|^2
\le
C_1\frac rU\|x\|^2
+
C_2\frac rUe^{-r}
\left(\|R_Ux\|^2+\|x\|^2\right).
}
\tag{SC1}
\]

For the reverse-normal datum from PR #68,

\[
x=x_{\rm rev}
=\mathcal Q_{U,V}H_U^*E_{R,U}f_{\rm rev},
\tag{SC2}
\]

one has the exact normalization

\[
\boxed{
\|x_{\rm rev}\|^2+\|R_Ux_{\rm rev}\|^2\le1.
}
\tag{SC3}
\]

Therefore, for every sufficiently large `r` in the PR-#64 range,

\[
\boxed{
F_U(r):=\|\chi_{U,r}x_{\rm rev}\|^2
\le C\frac rU.
}
\tag{SC4}
\]

The point is that SC4 is not merely the special choice `r=8 log U`; it is a distribution-function estimate valid throughout the admissible radius range.

### Local booking

```text
R43-COND-REVERSE-SHELLWISE-COLLAR-DISTRIBUTION  ✓[M]_local
```

This is a local consequence of the exact PR-#64 and PR-#68 statements; it is not a new operatorwide theorem.

---

## 2. Weighted boundary integral as a Stieltjes integral

Consider one terminal side and write the inward distance

\[
d:=U-u\ge0.
\tag{SC5}
\]

Let

\[
d\mu_+(d):=|x_{\rm rev}(U-d)|^2\,dd,
\qquad
F_+(r):=\mu_+([0,r]).
\tag{SC6}
\]

Then `F_+(r) <= F_U(r)`, and hence from SC4

\[
F_+(r)\le C\frac rU
\qquad (r_0\le r\le U/8).
\tag{SC7}
\]

The corresponding positive exponential boundary weight is

\[
I_+:=L\int_0^U e^{-d/2}\,d\mu_+(d).
\tag{SC8}
\]

Split at `U/8`.  The deep-bulk tail satisfies, using `||x_rev||<=1`,

\[
L\int_{U/8}^U e^{-d/2}\,d\mu_+(d)
\le Le^{-U/16}.
\tag{SC9}
\]

On `[r_0,U/8]`, Stieltjes integration by parts gives

\[
\int_{r_0}^{U/8}e^{-d/2}\,dF_+(d)
=
\left[e^{-d/2}F_+(d)\right]_{r_0}^{U/8}
+
\frac12\int_{r_0}^{U/8}e^{-d/2}F_+(d)\,dd.
\tag{SC10}
\]

Using SC7,

\[
\int_{r_0}^{U/8}e^{-d/2}\,dF_+(d)
\le
\frac CU
\left(
O(1)+\frac12\int_{r_0}^{\infty}d\,e^{-d/2}\,dd
\right)
\le \frac{C'}U.
\tag{SC11}
\]

The fixed initial interval `[0,r_0]` is harmless only at the same universal `O(1/U)` scale if SC1 is invoked after increasing constants to a fixed admissible radius; no asymptotic gain beyond `1/U` occurs there.

Consequently

\[
\boxed{
I_+\le C\frac LU+Le^{-cU}.
}
\tag{SC12}
\]

The reflected negative terminal side gives the same bound, so the primitive opposite-boundary majorant obtained by combining PR #78 with the shellwise PR-#64 estimate is

\[
\boxed{
\mathcal O_{\rm shell}(x_{\rm rev})
\le
C\frac{V-U}{U}
+(V-U)e^{-cU}.
}
\tag{SC13}
\]

### Consequences

- If `V-U=O(1)`, SC13 is `O(1/U)` and is stronger than the desired `O(log U/U)`.
- If `V-U=O(log U)`, SC13 is `O(log U/U)` and is exactly sufficient.
- On the geometric/dyadic scale relevant to the current FLAGDYN chain, `V-U \asymp U`, SC13 is only

\[
\boxed{O(1).}
\tag{SC14}
\]

Thus the shellwise refinement removes the earlier crude `O(log U)` loss but does not supply the final factor `1/U` needed on a dyadic step.

### Local bookings

```text
R43-COND-REVERSE-SHELLWISE-WEIGHTED-OCCUPANCY-BOUND   ✓[M]_local
R43-COND-REVERSE-SHELLWISE-DYADIC-DECAY                ×[M]
```

The first is confined to the primitive occupancy majorant from PR #78.  The second records failure of this **route**, not failure of reverse-normal decay itself.

---

## 3. Why the `r/U` distribution scale is universally sharp

PR #64 already identifies the obstruction: a normalized constant vector lies in the kernel of the old primitive residual-difference operator and places a fraction of order `r/U` of its `L^2` mass in the two terminal collars.

For the normalized constant profile on `(-U,U)`,

\[
x_{\rm const}(u)=(2U)^{-1/2},
\tag{SC15}
\]

one has exactly

\[
\|\chi_{U,r}x_{\rm const}\|^2=\frac rU.
\tag{SC16}
\]

Hence no argument based only on the universal old residual-graph bound can replace SC4 by `o(r/U)` uniformly over the whole graph unit ball.

Inserting SC16 into an exponential boundary weight of height `L` gives the natural scale

\[
L\int_0^\infty e^{-d/2}\frac{dd}{2U}
\asymp \frac LU,
\tag{SC17}
\]

matching SC13.  Therefore SC13 is not merely an artifact of integration by parts; it reflects the true universal common-mode obstruction.

### Firewall

SC15--SC17 do **not** assert that the actual structured vector `x_rev` contains a constant component.  They only show that PR #64's graph estimate, by itself, cannot exclude one strongly enough.

---

## 4. Finite Galerkin diagnostic of shell distribution

Using the same `U=30, V=40` primitive-band Galerkin proxy as PR #72/#76 and normalizing each profile by the same old graph norm, the cumulative two-sided outer-collar masses behave qualitatively as follows.

### Constant profile

```text
r=1   : 0.03279
r=2   : 0.06557
r=4   : 0.13115
r=8   : 0.26230
r=16  : 0.52460
```

This tracks `r/U` essentially exactly and illustrates the universal obstruction.

### Center-localized Gaussian proxy

```text
r=1   : 1.6e-7
r=2   : 2.36e-7
r=4   : 5.2e-7
r=8   : 4.4e-6
r=16  : 1.5e-3
```

### Wide edge-localized Gaussian proxy

```text
r=1   : 2.14e-4
r=2   : 4.20e-4
r=4   : 7.41e-4
r=8   : 9.78e-4
r=16  : 9.82e-4
```

### Narrow edge-localized Gaussian proxy

```text
r=1   : 2.29e-4
r=2   : 5.06e-4
r=4   : 8.95e-4
r=8   : 1.015e-3
r=16  : 1.016e-3
```

These numbers are diagnostic only.  They do not implement the actual `x_rev`.  Their role is to show that profiles with additional structural localization can beat the universal `r/U` law by orders of magnitude, whereas the common mode saturates it.

```text
R43-COND-REVERSE-COMMON-MODE-OBSTRUCTION  ✓[M]_proxy
```

`✓[M]_proxy` is diagnostic notation only.

---

## 5. The next structural question

The shellwise route fails precisely because the universal graph class contains the constant/common mode.  The actual vector is highly structured:

\[
x_{\rm rev}
=
\mathcal Q_{U,V}H_U^*E_{R,U}f_{\rm rev},
\qquad
f_{\rm rev}=(G_{R,\rm cond}^{U,V})^{-1/2}\varepsilon_R.
\tag{SC18}
\]

PR #56 gives

\[
H_U^*=-H_U
\tag{SC19}
\]

and an explicit sum of antisymmetric centered half-shifts

\[
H_U^*E_{R,U}f
=
-\sum_p\sqrt{\log p}\sum_{k\ge1}p^{-3k/4}
P_UD_{k\log p}E_{R,\infty}f,
\qquad
D_s=U_{s/2}-U_{-s/2}.
\tag{SC20}
\]

The centered difference `D_s` flips reflection parity.  This suggests a concrete next test:

1. determine the exact reflection parity of the fixed source normal `\varepsilon_R`;
2. verify whether `G_{R,cond}^{-1/2}` preserves that parity;
3. verify whether `\mathcal Q_{U,V}` commutes with reflection;
4. if so, determine whether the resulting parity/common-mode exclusion yields a stronger weighted boundary estimate than SC13.

These are **open checks** in the present note.  No parity theorem is booked here.

Alternatively, one may have to return to the exact two-sided Schur/least-squares form before the positive Cauchy occupancy majorant destroys cancellations between the two strip sides.

### Revised open nodes

```text
ROADMAP-COND-REVERSE-COMMON-MODE-ELIMINATION          ?[O]
ROADMAP-COND-REVERSE-REFLECTION-PARITY-COMPATIBILITY  ?[O]
ROADMAP-COND-REVERSE-WEIGHTED-OPPOSITE-COLLAR         ?[O]
ROADMAP-COND-REVERSE-EXACT-SCHUR-TWOSIDED-CANCELLATION ?[O]
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY              ?[O]
```

---

## 6. Scope / no-promotion firewall

This note proves only the shellwise consequence of the already established PR-#64 collar estimate and the resulting no-go for closing the dyadic primitive occupancy majorant by shell refinement alone.

It does **not** prove:

- that `x_rev` is odd or even;
- that the constant mode is absent from `x_rev`;
- a weighted opposite-boundary estimate for `x_rev`;
- reverse-normal stretch decay;
- FD23-UNIF;
- B-FLAGMOD / B-FLAGDYN / B-FLAGTIGHT;
- B-SIGN / B-ORIENT;
- Strong Terminal / C6;
- Object-X realization;
- RH.

Keep Draft.  No Registry promotion or mathematics merge without a fresh destructive review of the exact head.
