# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front  
**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## One-line update

The raw symmetric-strip geometry is already local.  The BMIX cross block is now sharpened further: the type-correct residual intertwining defect

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V
\]

satisfies an exact Feshbach-absorbed bound

\[
\|Q_BB_VQ_I\|
\le \|C_{V,U}B_V\|
\le \|C_{V,U}\|,
\]

so the crude factor `2||R_V||` is unnecessary.  For fine terminal steps `V-U<log(2)/2`, the frozen martingale cutoff also creates an exact residual dead layer in the new outer strip.

## Live tree

```text
B-METINC-WIDTH [OPEN]
├─ summable width/conditioning majorants [OPEN]
│  ├─ B-METINC-NEW [OPEN]
│  ├─ B-METINC-GEO [OPEN]
│  │  ├─ R43-GEO-RAW-STRIP ✓[M]        (local raw theorem)
│  │  ├─ B-METINC-GEO-BMIX [OPEN]
│  │  │  ├─ FESHBACH-ABSORPTION ✓[M]   (local exact reduction)
│  │  │  ├─ RESIDUAL-DEAD-LAYER ✓[M]   (fine-step local theorem)
│  │  │  ├─ RESIDUAL-MARK-GRAM ✓[M]    (local exact algebra)
│  │  │  └─ conditioned defect decay/summability [OPEN]
│  │  └─ B-METINC-GEO-BDRY [OPEN]
│  ├─ B-METINC-NORMMIX [OPEN]          (G_{S,U}^{-1/2} offblock)
│  └─ B-METINC-COND [OPEN]             (B_U -> B_V; elevated priority)
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

Legacy normalized/source-metric `GEO-II` and `GEO-IB` remain OPEN.  Their raw unweighted support analogues are closed jointly by `R43-GEO-RAW-STRIP`.

Downstream remains

```text
B-METINC-WIDTH + FD23 machinery
  -> B-FLAGMOD contribution
  -> [with B-FLAGPHASE] B-FLAGTIGHT ?
  -> B-SIGN ?
  -> Strong Terminal ?
```

No converse is added.

## Frozen raw strip theorem

Canonical P11 has

\[
D_s=U_{s/2}-U_{-s/2},
\qquad
E_T:\mathscr H_T\to L^2(\mathbb R)\text{ zero extension},
\qquad
P_T=E_T^*.
\]

For `X<U<V` and

\[
\psi_s(f):=-D_sE_Xf,
\]

one has exactly

\[
K_{s,T}^*E_{X,T}f=P_T\psi_s(f),
\qquad K_{s,T}=P_TD_sE_T,
\]

and therefore the raw increment is supported on

\[
\mathcal S_{U,V}=\{x:U<|x|<V\}.
\]

Equivalently,

\[
\langle P_V\psi_a,P_V\psi_b\rangle-
\langle P_U\psi_a,P_U\psi_b\rangle
=
\int_{U<|x|<V}\psi_a\overline{\psi_b}.
\]

For the entire old hub, if `v_0` is the embedded terminal-`U` vector and `d` its old-geometry increment, then

\[
v_0=Q_Iv_0,
\qquad d=Q_Bd,
\qquad \langle d,v_0\rangle=0.
\]

This is `R43-GEO-RAW-STRIP ✓[M]`, a local exact frozen-definition theorem only.

## GEO-BMIX: type-correct residual intertwining defect

Frozen Schur geometry uses

\[
B_V=(I+R_V^*R_V)^{-1}.
\]

The actual fixed-terminal cross block is

\[
\Delta s_{\rm geo}
=
2\operatorname{Re}\langle d,Q_BB_VQ_Iv_0\rangle
+
\langle d,Q_BB_VQ_Bd\rangle.
\]

Because `R_V` has different domain and residual codomain, introduce

- `Q_I` on the source/domain;
- `\widetilde Q_I` as the same spatial multiplication on the residual codomain.

Define

\[
\boxed{C_{V,U}:=R_VQ_I-\widetilde Q_I R_V.}
\]

Then

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

and therefore

\[
\|C_{V,U}\|
=
\max\{\|\widetilde Q_B R_VQ_I\|,
       \|\widetilde Q_I R_VQ_B\|\}.
\]

Moreover

\[
[R_V^*R_V,Q_I]
=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

The crucial sharpening is to **retain** the two Feshbach factors.  Resolvent calculus gives

\[
Q_BB_VQ_I
=-Q_BB_VR_V^*C_{V,U}B_VQ_I
+Q_BB_VC_{V,U}^*R_VB_VQ_I.
\]

Since

\[
\|R_VB_V\|=\|B_VR_V^*\|
=\sup_{t\ge0}\frac{t}{1+t^2}
\le\frac12,
\]

one obtains exactly

\[
\boxed{
\|Q_BB_VQ_I\|
\le
\frac12\left(
\|C_{V,U}B_VQ_I\|
+
\|C_{V,U}B_VQ_B\|
\right)
\le
\|C_{V,U}B_V\|
\le
\|C_{V,U}\|.
}
\]

Book only the local reduction

```text
R43-BMIX-FESHBACH-ABSORPTION ✓[M].
```

BMIX remains OPEN because decay/summability of `||C_{V,U}B_V||` is not yet proved.

## Exact prime-power form of the defect

Let `M_U=1_{(-U,U)}` on ambient `L^2(R)`.  Since `E_VQ_I=M_UE_V` and the mark cutoff is pointwise in the spatial variable,

\[
\boxed{
(C_{V,U}f)(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
([D_{k\log p},M_U]E_Vf)(u)
\otimes\mathsf Q_V(u)\eta_{p,k}.
}
\]

For `(U_tg)(u)=g(u-t)`, each `[U_t,M_U]` is supported on

\[
(-U,U)\triangle((-U,U)+t).
\]

Thus every prime-power channel is a boundary-crossing translation commutator.  Support localization by itself does not imply small operator norm.

## Fine-step residual dead layer

For `u` in the outer strip `U<|u|<V`,

\[
V-|u|<V-U.
\]

If

\[
0<V-U<\frac12\log2,
\]

then for every prime `p\ge2`

\[
\frac{2(V-|u|)}{\log p}<1,
\]

hence the frozen martingale depth satisfies `J_{p,V}(u)=0`. Therefore

\[
\boxed{
\widetilde Q_B R_V=0
}
\]

on every such fine step, and consequently

\[
C_{V,U}Q_I=0,
\qquad
C_{V,U}=-\widetilde Q_I R_VQ_B.
\]

Book only

```text
R43-RESIDUAL-DEAD-LAYER ✓[M]
```

as a local fine-step theorem.  It is one-sided: new-strip source vectors can still be translated inward, so BMIX does not vanish automatically.

## Residual mark Gram algebra

For

\[
q_{p,k;V}(u)=\mathsf Q_V(u)\eta_{p,k},
\qquad
r=\min\{k,\ell,J_{p,V}(u)\},
\]

direct summation yields

\[
\langle q_{p,k;V}(u),q_{p,\ell;V}(u)\rangle
=
\begin{cases}
 p^{r-(k+\ell)/2}-p^{-(k+\ell)/2},&r\ge1,\\
 0,&r=0,
\end{cases}
\]

so in particular

\[
0\le
\langle q_{p,k;V}(u),q_{p,\ell;V}(u)\rangle
\le p^{-|k-\ell|/2}.
\]

Thus `k`-correlations inside one prime sector decay geometrically.  The remaining difficulty is not this algebra alone but the prime sum, boundary translation geometry, and Feshbach/source normalization.

Book the displayed exact algebra as

```text
R43-RESIDUAL-MARK-GRAM ✓[M].
```

## NORMMIX and COND remain distinct

The normalized spectral-width operator is

\[
\mathbf H_{\rm geo}
=G_{S,U}^{-1/2}\Delta G_{\rm geo}G_{S,U}^{-1/2}.
\]

Thus a second mixing layer remains:

```text
B-METINC-NORMMIX [OPEN]
    control P_I G_{S,U}^{-1/2} P_B
```

or an equivalent commutator/reducing-subspace formulation.

The three mechanisms remain distinct:

1. `BMIX`: fixed `B_V` mixing, now reduced to the conditioned defect `C_{V,U}B_V`;
2. `NORMMIX`: old source metric inverse square root mixes the split after pullback;
3. `COND`: actual terminal drift `B_U -> B_V`.

## Spectral-width route retained

For the normalized metric increment

\[
\mathbf H_X^{U,V}
=G_{X,U}^{-1/2}(G_{X,V}-G_{X,U})G_{X,U}^{-1/2},
\]

and `P_U=W_UW_U^*`,

\[
\|\mathscr E_{U,V}\|
=\|[\mathbf H_S^{U,V},P_U]\|
\le
\frac12\operatorname{width}\sigma(\mathbf H_S^{U,V}).
\]

The actual modulus gate still carries

\[
\mathfrak d_{m,\rm mod}(U,V)
\le
\frac{\operatorname{width}\sigma(\mathbf H_S^{U,V})}
{2\alpha_R(U,V)(\alpha_S(U,V)+\alpha_R(U,V))}.
\]

No cofinal uniform coercivity lower bound is booked.

## FD23 tail compactness retained

For the canonical jet tails

\[
\mathcal H_S^{[m]}
=\overline{\operatorname{span}}\{e_{S,n}:n\ge m\},
\]

and every bounded `K\subset\mathcal H_S^0`,

\[
K\text{ relatively norm compact}
\iff
\sup_{x\in K}\|P_S^{[m]}x\|\to0.
\]

This remains `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`.  The actual R43 family has not yet been proved compact/norm-continuous on fixed intervals, so `FD23-UNIF` remains OPEN.

## Immediate proof order

1. Estimate the **conditioned** BMIX defect `||C_{V,U}B_V||`, preserving the Feshbach factor.
2. Exploit the fine-step one-sided dead-layer identity before any crude prime summation.
3. Derive a quantitative `COND` resolvent increment for `B_U -> B_V` without conflating it with BMIX.
4. Control `NORMMIX` through the old-metric square-root offblock.
5. Prove fixed-interval compactness/norm continuity for `FD23-UNIF`.
6. Only then return to condition-weighted terminal summability.

## Governance

- `R43-GEO-RAW-STRIP`: ✓[M] local exact theorem only.
- `R43-BMIX-FESHBACH-ABSORPTION`: ✓[M] local exact theorem only.
- `R43-RESIDUAL-DEAD-LAYER`: ✓[M] local exact theorem only.
- `R43-RESIDUAL-MARK-GRAM`: ✓[M] local exact algebra only.
- `FD23-TAIL-COMPACTNESS-EQUIV`: ✓[M] abstract/canonical-tail theorem only.
- no new project-level `✓[M]`.
- `B-METINC-GEO`: OPEN.
- `B-METINC-GEO-BMIX`: OPEN.
- conditioned BMIX decay/summability: OPEN.
- `B-METINC-GEO-BDRY`: OPEN.
- legacy normalized `GEO-II`: OPEN.
- legacy normalized `GEO-IB`: OPEN.
- `B-METINC-NORMMIX`: OPEN.
- `B-METINC-COND`: OPEN, elevated priority.
- `FD23-UNIF`: OPEN.
- `B-METINC-NEW`: OPEN.
- `B-METINC-WIDTH`: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- R43: OPEN.
- no freeze.
- no new formal independent GREEN.
- R38–R42 unchanged/frozen.
- R37/G4c separate and OPEN.
- no Object-X/RH promotion.
