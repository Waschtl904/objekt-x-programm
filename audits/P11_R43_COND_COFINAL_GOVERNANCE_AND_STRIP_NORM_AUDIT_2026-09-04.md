# P11 / R43 — COND cofinal gate, provenance, and strip-norm firewall

**Date:** 2026-09-04  
**Status:** local exact hardening; `B-METINC-COND` remains OPEN

## 0. Scope and governance

This note reconciles the referee review received on 2026-09-04 after head `026b6cc721e683577352edd3399f1ec78d509ef1`.

It does **not** close `R43-COND-CANONICAL-PSD-REALIZATION`, `R43-COND-FIXED-SOURCE-REANCHOR`, `B-METINC-COND`, `B-METINC`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, Object X, or RH.  No freeze and no new formal independent-GREEN booking occur here.

The main points are:

1. record the cofinal/local sign target actually sufficient for the FD23 partition route;
2. make the chronology of the auxiliary comparator `\widehat B_{U;V}` independently auditable from Git history;
3. sharpen the exact reduced Schur form into an ambient `M`-relative firewall;
4. remove obsolete kernel/rank witness branches after residual nesting;
5. compute the exact `p=2` cross-coefficient limit;
6. test the referee's proposed `\alpha/\beta` fine-step scaling in the actual frozen operator norm.

---

## 1. Cofinal/local PSD is the relevant sign target

The exact B-FLAGDYN sufficient criterion FD23 is formulated on a terminal partition

\[
U_0<U_1<\cdots\to\infty
\]

with cellwise suprema over `V\in[U_k,U_{k+1}]`.  Therefore a global order theorem for every coarse pair `U<V` is stronger than is needed by this route.

For canonical COND define

\[
K_{U,V}^{\rm Schur}
:=M^*(I+SS^*)^{-1}M-R_U^*R_U.
\]

A sufficient sign hypothesis for the partition route is the **eventual local** statement

\[
\boxed{
\exists U_*,h_*>0\quad
\forall U\ge U_*,\quad
0<V-U<h_*
\Longrightarrow
K_{U,V}^{\rm Schur}\succeq0.
}
\tag{CG1}
\]

Indeed, choose a cofinal partition with mesh `<h_*`; then every endpoint step, and every within-cell pair used in the FD20--FD21 suprema, lies in the sign regime.  This supplies the positive COND increment form required by the antitone/telescoping machinery.  It does **not** supply the quantitative reanchor/path estimate or summability by itself.

Book locally:

```text
R43-COND-COFINAL-LOCAL-PSD-SUFFICIENT ✓[M]
```

The stronger all-pairs statement remains optional.  The live application gate is henceforth read as eventual fine-step PSD, not as a demand for arbitrary coarse terminal pairs.

---

## 2. Provenance of the two-step comparator is now Git-verifiable

The comparator

\[
\widehat B_{U;V}:=(I+\iota^*A_V\iota)^{-1}
\]

and the exact split

\[
\iota^*B_V\iota-B_U
=(\widehat B_{U;V}-B_U)
+(\iota^*B_V\iota-\widehat B_{U;V})
\tag{CG2}
\]

were first committed in

```text
669cda8204228f25ea840ea81733fdeb30c39cc4
```

file

```text
audits/P11_R43_COND_COMPRESSION_REANCHOR_AUDIT_2026-09-04.md
```

as equation `(C11)`.

GitHub's commit metadata records both author and committer timestamp

```text
2026-09-04T17:45:39Z
```

for that commit.  The present referee review was received later, at `2026-09-04T19:08:09Z` in the research conversation.  Thus the auxiliary two-step comparator and the explicit firewall against silently retyping its second term as BMIX/BDRY predate the review and the later target-space sign calculation.

This is a governance/provenance record, not a mathematical promotion.

---

## 3. Exact reduced form and the ambient M-relative firewall

From the companion residual-Schur audit,

\[
\Pi M=\jmath R_U,
\qquad
C:=(I-\Pi)M,
\qquad
\Phi_S:=SS^*(I+SS^*)^{-1},
\]

so

\[
\boxed{
K_{U,V}^{\rm Schur}
=C^*C-M^*\Phi_SM
=M^*\bigl[(I-\Pi)-\Phi_S\bigr]M.
}
\tag{CG3}
\]

Consider the strongest ambient Loewner criterion that discards the special range of `M`:

\[
(I-\Pi)-\Phi_S\succeq0.
\tag{CG4}
\]

Because `I-\Pi` is a projection and

\[
0\preceq\Phi_S\preceq P_{\overline{\operatorname{Ran}S}},
\qquad
\ker\Phi_S=(\overline{\operatorname{Ran}S})^\perp,
\]

one has exactly

\[
\boxed{
(I-\Pi)\succeq\Phi_S
\iff
\overline{\operatorname{Ran}S}\perp\operatorname{Ran}\Pi.
}
\tag{CG5}
\]

Proof: if (CG4) holds and `y\in\operatorname{Ran}\Pi`, then
`0\le\langle y,[(I-\Pi)-\Phi_S]y\rangle=-\langle y,\Phi_Sy\rangle`, hence `\Phi_Sy=0`, so `y\perp\overline{\operatorname{Ran}S}`. Conversely, under this orthogonality `\Phi_S` acts in `\operatorname{Ran}(I-\Pi)` and `0\le\Phi_S\le I-\Pi`.

The previous `p=2` old-residual/strip witness proves this orthogonality false in the frozen model. Therefore the ambient `M`-independent domination route is unavailable. Any surviving proof of (CG1) must use the restricted geometry of `\operatorname{Ran}M` (or an equivalent `M`-relative factorization), rather than proving (CG4) on the whole residual target.

Book locally:

```text
R43-COND-AMBIENT-MFREE-DOMINATION-CHARACTERIZATION ✓[M]
R43-COND-AMBIENT-MFREE-DOMINATION-ROUTE ×[M]
```

The second booking is route-specific only; it is not a negative result for canonical COND PSD.

---

## 4. Two obsolete witness branches are excluded by nesting

From

\[
\Pi M=\jmath R_U
\]

we immediately get

\[
Mx=0\Longrightarrow R_Ux=0,
\]

hence

\[
\boxed{
\ker M\subseteq\ker R_U.
}
\tag{CG6}
\]

In finite cutoffs it also follows that

\[
\boxed{
\operatorname{rank}R_U\le\operatorname{rank}M.
}
\tag{CG7}
\]

Therefore the earlier cheap negative tests

```text
Mx=0 but R_Ux!=0
rank(R_U)>rank(M)
```

are structurally impossible after `R43-COND-OLD-SOURCE-RESIDUAL-NESTING`.

The correct reduced kernel test is instead

\[
\boxed{
\ker C\subseteq\ker(S^*M)\;?
}
\tag{CG8}
\]

because if `Cx=0` but `S^*Mx\ne0`, then

\[
\langle x,K_{U,V}^{\rm Schur}x\rangle
=-\|(I+S^*S)^{-1/2}S^*Mx\|^2<0.
\tag{CG9}
\]

Book locally:

```text
R43-COND-M-KERNEL-WITNESS-EXCLUDED ✓[M]
R43-COND-M-RANK-WITNESS-EXCLUDED ✓[M]
R43-COND-C-KERNEL-WITNESS-CRITERION ✓[M]
```

---

## 5. Exact p=2 cross coefficient limit

The previous target-coupling audit obtained

\[
F_K
=-2^{-3/2}
+\sum_{k=1}^{K}
2^{-(k+1)/2}
\left(\frac12-2^{-(k+1)}\right).
\]

Both geometric series can be summed exactly.  One finds

\[
\boxed{
F_\infty
:=\lim_{K\to\infty}F_K
=\frac5{14}-\frac{\sqrt2}{28}
=\frac{10-\sqrt2}{28}
\approx0.3066352299.
}
\tag{CG10}
\]

Thus the small positive value at `K=3`,

\[
F_3=\frac{15-10\sqrt2}{64}\approx0.0134041,
\]

is a finite-cutoff near-cancellation, not an asymptotic decay mechanism.

For normalized indicator witnesses `\widehat f=|I|^{-1/2}1_{I_P}` and `\widehat g=|I|^{-1/2}1_{I_Q}`, the cross term from that construction is

\[
\langle M\widehat f,S\widehat g\rangle
=(\log2)F_K,
\]

so along late horizons with `K\to\infty` the exhibited coupling remains `O(1)`.

Book locally:

```text
R43-COND-P2-CROSS-COEFFICIENT-SATURATION ✓[M]
```

This is a statement about the explicit witness coefficient, not yet a complete norm asymptotic for `M^*S` in every horizon regime.

---

## 6. Fine strip width does not make alpha or beta small in operator norm

Write, as in the live front,

\[
S_0:=\Pi S,
\qquad
S_1:=(I-\Pi)S,
\qquad
\alpha_{U,V}:=\|S_0\|,
\qquad
\beta_{U,V}:=\|S_1\|.
\tag{CG11}
\]

Fix

\[
t=\frac12\log2,
\qquad0<h=V-U<t,
\]

and choose the same normalized strip indicator `\widehat g` centered at `V-\delta`, with interval length small relative to `h`.

### 6.1 p=2 lower bounds

For the `p=2` channel and each retained left translate indexed by `\ell`, the old depth is `\ell-1` and the new depth is `\ell`.  Hence the single newly added martingale coordinate has squared mark coefficient `1/2`, while the old part of `\eta_{2,\ell}` has squared norm

\[
\frac12-2^{-\ell}.
\]

The translated output intervals are disjoint after choosing the witness interval sufficiently short. Therefore, if `L=L(U)\to\infty` counts the retained left translates,

\[
\|S_1\widehat g\|^2
\ge
\frac{\log2}{2}
\sum_{\ell=1}^{L}2^{-\ell/2},
\tag{CG12}
\]

and

\[
\|S_0\widehat g\|^2
\ge
(\log2)
\sum_{\ell=2}^{L}
2^{-\ell/2}\left(\frac12-2^{-\ell}\right).
\tag{CG13}
\]

Letting `U\to\infty`,

\[
\boxed{
\liminf\beta_{U,V}^2
\ge
\frac{1+\sqrt2}{2}\log2
\approx0.8367026620,
}
\tag{CG14}
\]

and

\[
\boxed{
\liminf\alpha_{U,V}^2
\ge
\frac{5+3\sqrt2}{14}\log2
\approx0.4576078809.
}
\tag{CG15}
\]

These lower bounds are independent of the strip thickness `h`.  In particular, shrinking support does not imply `\alpha,\beta=O(\sqrt h)` in operator norm.

### 6.2 In fact beta diverges by the k=1 prime layer

The full frozen residual model gives a much stronger statement.  For every prime `p`, take the `k=1` left translate of the same normalized strip indicator.  For primes satisfying

\[
\frac12\log p>h-\delta+O(|I|),
\qquad
\frac12\log p<V-\delta-O(|I|),
\]

the translated output lies in `(0,U)` and has

\[
J_{p,U}=0,
\qquad
J_{p,V}=1.
\]

Thus this entire `p,k=1` contribution lies in `S_1`.  The newly retained martingale mark is

\[
\eta_{p,1}=\sqrt{p-1}\,p^{-1/2}\psi_{p,0},
\]

so the squared residual contribution of that prime is exactly

\[
(\log p)\,p^{-1/2}\frac{p-1}{p}
=(\log p)(p-1)p^{-3/2}.
\tag{CG16}
\]

Different prime sectors are orthogonal. Hence

\[
\boxed{
\beta_{U,V}^2
\ge
\sum_{p\in\mathcal P(U,h,\delta,I)}
(\log p)(p-1)p^{-3/2},
}
\tag{CG17}
\]

where the admissible prime set exhausts all sufficiently large finite initial prime ranges as `U\to\infty` for any fixed fine-step pattern (and likewise for cofinal `h\downarrow0` with the interval chosen inside the strip).

Since for large primes

\[
(\log p)(p-1)p^{-3/2}\gtrsim \frac1p
\]

and Euler's prime harmonic series diverges,

\[
\boxed{
\beta_{U,V}\longrightarrow\infty
\quad\text{cofinally in the frozen operator norm geometry.}
}
\tag{CG18}
\]

Therefore the referee-proposed sufficient estimate requiring

\[
\beta<1,
\qquad
(1-\beta)^2C^*C\succeq\alpha^2R_U^*R_U
\]

cannot be the late-horizon operator-norm route in the frozen model.

Book locally:

```text
R43-COND-STRIP-NORM-SMALLNESS ×[M]
R43-COND-CRITERION-B-OPNORM-ROUTE ×[M]
```

These are route-specific negatives only.  They do not decide the exact saturated Feshbach criterion `K_{U,V}^{Schur}\succeq0`, because `\Phi_S=SS^*(I+SS^*)^{-1}\preceq I` deliberately saturates large strip norms.

---

## 7. Consequence for the live search

The exact sign problem remains

\[
\boxed{
K_{U,V}^{\rm Schur}
=C^*C-M^*\Phi_SM\succeq0\;?
}
\tag{CG19}
\]

but the search tree is now narrower:

1. no global all-pairs PSD theorem is required; eventual fine-step PSD suffices for the partition sign mechanism;
2. no ambient `M`-free domination can work;
3. old `M`-kernel and rank witnesses are impossible by nesting;
4. strip operator-norm smallness, including the proposed `\beta<1` route, is false;
5. the remaining viable routes must exploit the **saturated** operator `\Phi_S` and the special relative position of `\operatorname{Ran}M`, `\operatorname{Ran}C`, and `\operatorname{Ran}S`;
6. the cheapest destructive test is (CG8)--(CG9), followed by the exact generalized Rayleigh/Douglas problem.

The next quantitative work should therefore be `p=2` first but resolvent-saturated: compute `S^*M` and `C^*C` on the explicit collision family without replacing `\Phi_S` by `SS^*` or by `P_{\operatorname{Ran}S}`.

---

## 8. Status firewall

Local exact additions in this note:

```text
R43-COND-COFINAL-LOCAL-PSD-SUFFICIENT             ✓[M]
R43-COND-AMBIENT-MFREE-DOMINATION-CHARACTERIZATION ✓[M]
R43-COND-AMBIENT-MFREE-DOMINATION-ROUTE           ×[M]
R43-COND-M-KERNEL-WITNESS-EXCLUDED                ✓[M]
R43-COND-M-RANK-WITNESS-EXCLUDED                  ✓[M]
R43-COND-C-KERNEL-WITNESS-CRITERION               ✓[M]
R43-COND-P2-CROSS-COEFFICIENT-SATURATION           ✓[M]
R43-COND-STRIP-NORM-SMALLNESS                      ×[M]
R43-COND-CRITERION-B-OPNORM-ROUTE                 ×[M]
```

Still OPEN: `R43-COND-COFINAL-LOCAL-PSD` as an application theorem, `R43-COND-CANONICAL-PSD-REALIZATION` in the stronger pairwise sense, `R43-COND-FIXED-SOURCE-REANCHOR`, `B-METINC-COND`, `B-METINC-NORMMIX`, `B-METINC-GEO-BMIX`, `B-METINC-GEO-BDRY`, `B-METINC-NEW`, `B-METINC-WIDTH`, `B-METINC`, `B-FLAGMOD`, `B-FLAGPHASE`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, R43, Object X, RH.
