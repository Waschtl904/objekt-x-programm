# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front  
**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## One-line update

The raw symmetric-strip geometry is local. The BMIX cross block is now reduced through the type-correct residual intertwining defect

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V
\]

and the exact Feshbach-absorbed estimate

\[
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
\]

For fine steps `V-U<log(2)/2`, the frozen martingale cutoff gives an exact residual dead layer and

\[
\boxed{C_{V,U}=-R_VQ_B.}
\]

Hence the preferred quantitative BMIX target is the **conditioned fine-step defect**

\[
\boxed{\|R_VQ_BB_V\|},
\]

not the crude raw commutator norm.

## Live tree

```text
B-METINC-WIDTH [OPEN]
├─ summable width/conditioning majorants [OPEN]
│  ├─ B-METINC-NEW [OPEN]
│  ├─ B-METINC-GEO [OPEN]
│  │  ├─ R43-GEO-RAW-STRIP ✓[M]
│  │  ├─ B-METINC-GEO-BMIX [OPEN]
│  │  │  ├─ FESHBACH-ABSORPTION ✓[M]
│  │  │  ├─ RESIDUAL-DEAD-LAYER ✓[M]
│  │  │  ├─ RESIDUAL-MARK-GRAM ✓[M]
│  │  │  └─ conditioned defect decay/summability [OPEN]
│  │  └─ B-METINC-GEO-BDRY [OPEN]
│  ├─ B-METINC-NORMMIX [OPEN]
│  └─ B-METINC-COND [OPEN]
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

Downstream:

```text
B-METINC-WIDTH + FD23 machinery
  -> B-FLAGMOD contribution
  -> [with B-FLAGPHASE] B-FLAGTIGHT ?
  -> B-SIGN ?
  -> Strong Terminal ?
```

No converse is added.

## Raw strip theorem retained

Canonical P11 has

\[
D_s=U_{s/2}-U_{-s/2},
\qquad
E_T:\mathscr H_T\to L^2(\mathbb R)\text{ zero extension},
\qquad
P_T=E_T^*.
\]

For `X<U<V` and `\psi_s(f):=-D_sE_Xf`,

\[
K_{s,T}^*E_{X,T}f=P_T\psi_s(f),
\qquad K_{s,T}=P_TD_sE_T,
\]

and the raw increment is supported on

\[
\mathcal S_{U,V}=\{x:U<|x|<V\}.
\]

Hence raw unweighted interior/interior and interior/boundary increments collapse jointly when one raw field vanishes on this strip. This is `R43-GEO-RAW-STRIP ✓[M]`, local only.

## BMIX hardening

Frozen Schur geometry uses

\[
B_V=(I+R_V^*R_V)^{-1}.
\]

Because `R_V` has different source and residual codomain spaces, define `Q_I` on the source, `\widetilde Q_I` on the residual codomain, and

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V.
\]

Then

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

\[
\|C_{V,U}\|
=
\max\{\|\widetilde Q_B R_VQ_I\|,\|\widetilde Q_I R_VQ_B\|\},
\]

and

\[
[R_V^*R_V,Q_I]=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

Retaining both Feshbach factors,

\[
Q_BB_VQ_I
=-Q_BB_VR_V^*C_{V,U}B_VQ_I
+Q_BB_VC_{V,U}^*R_VB_VQ_I.
\]

Since

\[
\|R_VB_V\|=\|B_VR_V^*\|
=\sup_{t\ge0}\frac{t}{1+t^2}\le\frac12,
\]

\[
\boxed{
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
}
\]

Book `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` as a local exact reduction only. BMIX stays OPEN because decay/summability of the conditioned defect is unproved.

## Prime-power defect and fine-step dead layer

With `M_U=1_{(-U,U)}` on ambient `L^2(R)`, one has

\[
(C_{V,U}f)(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
([D_{k\log p},M_U]E_Vf)(u)
\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Thus every channel is a boundary-crossing translation commutator. Support localization alone does not imply operator-norm smallness.

For

\[
0<V-U<\frac12\log2,
\]

the frozen depth `J_{p,V}(u)` is zero throughout the new outer strip for every prime. Hence

\[
\widetilde Q_B R_V=0,
\qquad
\widetilde Q_I R_V=R_V,
\qquad
\boxed{C_{V,U}=-R_VQ_B.}
\]

This is `R43-RESIDUAL-DEAD-LAYER ✓[M]`, a local fine-step theorem only.

For the residual marks,

\[
q_{p,k;V}(u)=\mathsf Q_V(u)\eta_{p,k},
\qquad
r=\min\{k,\ell,J_{p,V}(u)\},
\]

and direct summation gives

\[
\langle q_{p,k;V},q_{p,\ell;V}\rangle
=
\begin{cases}
p^{r-(k+\ell)/2}-p^{-(k+\ell)/2},&r\ge1,\\
0,&r=0,
\end{cases}
\]

so

\[
0\le\langle q_{p,k;V},q_{p,\ell;V}\rangle
\le p^{-|k-\ell|/2}.
\]

This is `R43-RESIDUAL-MARK-GRAM ✓[M]` as local exact algebra only.

## Remaining mixing and compactness firewalls

`NORMMIX` remains the old-metric offblock problem

\[
P_IG_{S,U}^{-1/2}P_B,
\]

while `COND` remains the separate actual terminal change `B_U\to B_V`.

The positivity-free spectral-width route remains

\[
\|\mathscr E_{U,V}\|
\le\frac12\operatorname{width}\sigma(\mathbf H_S^{U,V}),
\]

and

\[
\mathfrak d_{m,\rm mod}(U,V)
\le
\frac{\operatorname{width}\sigma(\mathbf H_S^{U,V})}
{2\alpha_R(U,V)(\alpha_S(U,V)+\alpha_R(U,V))}.
\]

For the canonical jet tails and bounded `K\subset\mathcal H_S^0`,

\[
K\text{ relatively norm compact}
\iff
\sup_{x\in K}\|P_S^{[m]}x\|\to0.
\]

This is `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`; the concrete `FD23-UNIF` application remains OPEN.

## Immediate proof order

1. Estimate the conditioned fine-step defect `||R_VQ_BB_V||`.
2. Use the one-sided dead-layer identity before any crude prime sum.
3. Derive quantitative `COND` control for `B_U\to B_V`.
4. Control `NORMMIX`.
5. Prove fixed-interval compactness/norm continuity for `FD23-UNIF`.
6. Only then return to condition-weighted terminal summability.

## Governance

- `R43-GEO-RAW-STRIP`: ✓[M] local exact theorem only.
- `R43-BMIX-FESHBACH-ABSORPTION`: ✓[M] local exact theorem only.
- `R43-RESIDUAL-DEAD-LAYER`: ✓[M] local exact theorem only.
- `R43-RESIDUAL-MARK-GRAM`: ✓[M] local exact algebra only.
- `FD23-TAIL-COMPACTNESS-EQUIV`: ✓[M] abstract/canonical-tail theorem only.
- no new project-level `✓[M]`.
- B-METINC-GEO-BMIX: OPEN.
- conditioned BMIX decay/summability: OPEN.
- B-METINC-GEO-BDRY: OPEN.
- B-METINC-NORMMIX: OPEN.
- B-METINC-COND: OPEN.
- FD23-UNIF: OPEN.
- B-METINC-NEW: OPEN.
- B-METINC-WIDTH: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- R43: OPEN.
- no freeze, no new formal independent GREEN, no Object-X/RH promotion.
- R38–R42 unchanged/frozen; R37/G4c separate and OPEN.
