# P11 / R43 — cofinal COND PSD kernel-witness no-go

**Date:** 2026-09-04  
**Status:** theorem-level negative result for the canonical Loewner/PSD COND route; `B-METINC-COND` itself remains OPEN

## 0. Scope and firewall

This note continues the frozen canonical old-conditioning analysis with

\[
M:=R_V\iota,\qquad
S:=R_VP_{\mathcal N},\qquad
\Pi:=\Pi_{U,V},\qquad
C:=(I-\Pi)M,
\]

and

\[
K_{U,V}^{\rm Schur}
:=M^*(I+SS^*)^{-1}M-R_U^*R_U
=C^*C-M^*\Phi_SM,
\qquad
\Phi_S:=SS^*(I+SS^*)^{-1}.
\]

The previous audit proved the exact kernel criterion

\[
Cx=0,\quad S^*Mx\ne0
\Longrightarrow
\langle x,K_{U,V}^{\rm Schur}x\rangle
=-\|(I+S^*S)^{-1/2}S^*Mx\|^2<0.
\]

The present note realizes this criterion explicitly in the frozen residual geometry, at arbitrarily late terminals and arbitrarily fine terminal increments.

This **kills the canonical Loewner/PSD antitonicity route**, including the previously recorded eventual-fine-step PSD sufficient hypothesis. It does **not** prove that the actual vector-specific `B-METINC-COND` contribution is uncontrollable, does not close `B-METINC`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, Object X, or RH, and creates no project-level GREEN promotion.

---

## 1. Frozen fine-step layer form

Put

\[
a_p:=\frac12\log p,
\qquad
a_2=\frac12\log2.
\]

Assume

\[
0<h:=V-U<a_2.
\]

The sharp dead-layer theorem gives zero residual rows on the new outer spatial strip. Inside `(-U,U)`, because `h<a_p` for every prime, the depth can increase by at most one:

\[
J_{p,V}(u)-J_{p,U}(u)\in\{0,1\}.
\]

If the depth increases from `j-1` to `j`, then the newly exposed martingale coordinate is the `j`-th layer and its scalar amplitude on an old-source vector `f` is, up to the positive factor

\[
\sqrt{\log p\,(p-1)}\,p^{(j-1)/2},
\]

exactly

\[
\sum_{k\ge j}p^{-3k/4}D_{k\log p}E_Uf(u).
\tag{N1}
\]

Thus `Cf=0` follows if no translation with index `k>=j` from any depth-increment row meets the support of `f`.

---

## 2. A locally finite opposite-boundary resonance set

Define

\[
\Lambda
:=
\{n a_p:\ p\text{ prime},\ n\ge2\}.
\tag{N2}
\]

This set is locally finite: in a bounded interval `0<=lambda<=L`, the condition `n a_p<=L` is equivalent to `p^n<=e^{2L}`, which has only finitely many prime-power solutions.

Hence, for every lower terminal bound `U_*>0`, one can choose

\[
U>U_*
\]

such that

\[
2U-a_2\notin\Lambda.
\tag{N3}
\]

For such a `U`, local finiteness gives a positive gap

\[
\rho_U
:=\operatorname{dist}(2U-a_2,\Lambda)>0.
\tag{N4}
\]

Given any prescribed `h_*>0`, choose

\[
0<h<\min\left\{h_*,\frac{a_2}{4},\frac{\rho_U}{16}\right\},
\qquad
V:=U+h.
\tag{N5}
\]

Set `epsilon:=h/2` and choose an interval length

\[
0<\ell<\min\{h/4,\rho_U/16\}.
\tag{N6}
\]

Let `I_Q` be the interval of length `ell` centered at `U+epsilon`, and define

\[
I_P:=I_Q-a_2.
\tag{N7}
\]

Then

\[
I_Q\subset(U,V),
\qquad
I_P\subset(-U,U)
\]

for all sufficiently large `U` (and already for `U>a_2`). Put

\[
f:=1_{I_P},\qquad g:=1_{I_Q}.
\tag{N8}
\]

---

## 3. Exact kernel statement: `Cf=0`

We show that no newly exposed residual layer can see `f`.

Fix a prime `p`, a depth-increment row `u in (-U,U)`, and write the new layer index as `j>=1`. Necessarily

\[
j a_p-h
< U-|u| < j a_p
\tag{N9}
\]

(up to irrelevant endpoint null sets).

A contribution to the new layer from `f` could only come from some `k>=j` with

\[
u-k a_p\in I_P
\quad\text{or}\quad
u+k a_p\in I_P.
\tag{N10}
\]

### 3.1 Same-side rows cannot hit `I_P`

The interval `I_P` lies on the positive side at distance

\[
d:=U-(U+\epsilon-a_2)=a_2-\epsilon
\in(3a_2/4,a_2)
\tag{N11}
\]

from the right old boundary.

For a positive depth-increment row, combining (N9) with a hit of `I_P` by a translation `k>=j` forces, up to the interval tolerances,

\[
d\approx (j-k)a_p\le0,
\]

which is impossible because `d>3a_2/4` and `h+ell<a_2/2`. The other translation sign lies still farther from the right boundary and cannot hit `I_P` either.

Thus no positive-side new residual row contributes.

### 3.2 Opposite-side rows are excluded by the generic terminal gap

For a negative depth-increment row, the only possible hit of the positive interval `I_P` is the long translation across the whole old source window. Combining (N9) and (N10) gives

\[
\bigl|2U-a_2+\epsilon-(j+k)a_p\bigr|
< h+\ell.
\tag{N12}
\]

Since `k>=j>=1`, one has `j+k>=2`, so `(j+k)a_p in Lambda`.

But by (N4)--(N6),

\[
\operatorname{dist}(2U-a_2+\epsilon,\Lambda)
\ge \rho_U-\epsilon
>\frac{15}{16}\rho_U,
\]

while

\[
h+\ell<\frac{5}{64}\rho_U.
\]

Hence (N12) is impossible.

Therefore all newly exposed layer amplitudes vanish and

\[
\boxed{Cf=0.}
\tag{N13}
\]

This is an exact support statement, not a norm estimate.

---

## 4. Yet the old residual data couple to the new source strip

We now prove

\[
S^*Mf\ne0
\]

using the same `f` and the strip test vector `g`.

Because `I_P=I_Q-a_2`, a translated copy from prime `p` can overlap between the `f` and `g` channels only if

\[
|k-l|a_p=a_2
\quad\text{or}\quad
(k+l)a_p=a_2.
\tag{N14}
\]

The second alternative is impossible because `k+l>=2` and `a_p>=a_2`. In the first alternative, `a_p>=a_2` forces

\[
p=2,
\qquad
|k-l|=1.
\tag{N15}
\]

At fixed `V` there are only finitely many active translated intervals. Shrinking `ell` further if necessary, every non-exact translate mismatch has disjoint support. Therefore **only the exact `p=2`, adjacent-index overlaps survive** in the cross inner product.

Consider the first left-going overlap:

\[
l=1\quad\text{for }f,
\qquad
k=2\quad\text{for }g,
\]

on the output interval

\[
I_Q-2a_2.
\]

There both translation signs are negative, so their product is positive. Moreover

\[
J_{2,U}=1,
\qquad
J_{2,V}=2
\]

on this interval. The frozen mark Gram formula gives

\[
\langle q_{2,1;V},q_{2,2;V}\rangle
=2^{-1/2}-2^{-3/2}
=2^{-3/2}>0.
\tag{N16}
\]

The two residual coefficients are

\[
\sqrt{\log2}\,2^{-1/4},
\qquad
\sqrt{\log2}\,2^{-1/2}.
\]

Hence this single overlap contributes exactly

\[
\boxed{
\ell\,(\log2)\,2^{-9/4}>0
}
\tag{N17}
\]

to `\langle Mf,Sg\rangle`.

All other surviving `p=2` adjacent-index overlaps have the same translation-sign product and nonnegative mark Gram coefficient. Other prime sectors have no overlap by (N14)--(N15). Therefore there is no cancellation, and

\[
\boxed{
\langle Mf,Sg\rangle>0.
}
\tag{N18}
\]

Consequently

\[
\boxed{S^*Mf\ne0.}
\tag{N19}
\]

---

## 5. Strict negative Rayleigh witness

Combine (N13) and (N19). Since

\[
\ker\Phi_S=\ker S^*,
\]

we have

\[
\langle Mf,\Phi_SMf\rangle>0.
\]

Therefore

\[
\boxed{
\langle f,K_{U,V}^{\rm Schur}f\rangle
=-\langle Mf,\Phi_SMf\rangle
=-\|(I+S^*S)^{-1/2}S^*Mf\|^2
<0.
}
\tag{N20}
\]

Thus

\[
\boxed{K_{U,V}^{\rm Schur}\not\succeq0.}
\tag{N21}
\]

for the pair constructed above.

---

## 6. Cofinal/local PSD is theorem-level false

The construction began with **arbitrary** `U_*>0` and `h_*>0`. We then chose `U>U_*` outside the locally finite resonance set and `0<h<h_*` satisfying (N5).

Hence

\[
\boxed{
\forall U_*>0\ \forall h_*>0\ \exists U\ge U_*\ \exists h\in(0,h_*):
\quad
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\tag{N22}
\]

In particular, the previous sufficient hypothesis

\[
\exists U_*,h_*>0:\quad
U\ge U_*,\ 0<V-U<h_*
\Longrightarrow
K_{U,V}^{\rm Schur}\succeq0
\]

is false in the frozen residual model.

The stronger all-pairs canonical antitonicity is therefore false as well.

### Local theorem-level negative bookings

```text
R43-COND-C-KERNEL-WITNESS-REALIZED            ✓[M]_neg
R43-COND-COFINAL-LOCAL-PSD                    ×[M]
R43-COND-CANONICAL-PSD-REALIZATION            ×[M]
R43-COND-LOEWNER-ANTITONE-TELESCOPE-ROUTE     ×[M]
```

Here the `×[M]` labels reject the corresponding canonical claims/routes. The abstract resolvent-antitone and reanchor lemmas remain mathematically correct; their canonical COND premise fails.

---

## 7. What survives for `B-METINC-COND`

The negative theorem is **not** a no-go for the actual Strong-Terminal program.

Canonical SW14 uses the quadratic form only on the structured path

\[
v_U=H_U^*E_{X,U}f
\]

(and ultimately inside normalized fixed-source metric increments). The witness `1_{I_P}` above is an arbitrary source direction and is not shown to lie on that structured path.

Therefore the correct next COND problem is no longer a global Loewner-order theorem. It is a **vector-sensitive signed/absolute increment estimate**, for example a bound of the schematic form

\[
\bigl|\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle\bigr|
\le \Omega_{X}(U,V)
\]

with a cofinal summable mechanism compatible with B-FLAGDYN / the `m`-tail structure.

Equivalently, the already proved internal split

\[
\iota^*B_V\iota-B_U
=(\widehat B_{U;V}-B_U)
+(\iota^*B_V\iota-\widehat B_{U;V})
\]

remains useful as a signed decomposition, but **not** as a positive telescope for the total canonical COND term.

This pivot is forced by theorem (N22), not by taxonomy.

---

## 8. Governance

- `B-METINC-COND`: OPEN, but the global/canonical PSD subroute is closed negatively.
- `R43-COND-FIXED-SOURCE-REANCHOR`: its abstract lemma remains valid; the canonical positive-chain application is no longer the live route.
- `B-METINC-NORMMIX`, GEO-BMIX/BDRY, NEW, FD23-UNIF, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6: OPEN.
- R43 remains OPEN; no freeze and no formal independent GREEN.
- R38--R42 unchanged/frozen; R37/G4c separate and OPEN.
- no Object-X/RH promotion.
