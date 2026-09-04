# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front  
**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## One-line update

The raw symmetric-strip geometry is already local. The BMIX cross block is now sharpened further: with the type-correct residual intertwining defect

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V,
\]

one has the exact Feshbach-absorbed estimate

\[
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
\]

Thus the old crude factor `2||R_V||` is not part of the preferred route. For fine steps `V-U<log(2)/2`, the frozen martingale cutoff creates an exact residual dead layer in the new outer strip and in fact

\[
\boxed{C_{V,U}=-R_VQ_B.}
\]

So the only residual intertwining defect left on a fine step is **new-strip source input translated back into the old interior**.

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

Legacy normalized/source-metric `GEO-II` and `GEO-IB` remain OPEN. Their raw unweighted support analogues are closed jointly by `R43-GEO-RAW-STRIP`.

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

For `X<U<V` and `\psi_s(f):=-D_sE_Xf`, one has

\[
K_{s,T}^*E_{X,T}f=P_T\psi_s(f),
\qquad K_{s,T}=P_TD_sE_T,
\]

so the raw increment is supported on

\[
\mathcal S_{U,V}=\{x:U<|x|<V\},
\]

and

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

## GEO-BMIX: conditioned residual intertwining defect

Frozen Schur geometry uses

\[
B_V=(I+R_V^*R_V)^{-1}.
\]

The actual fixed-terminal cross term contains

\[
Q_BB_VQ_I.
\]

Because `R_V` has different domain and residual codomain, introduce `Q_I` on the source/domain and `\widetilde Q_I` as the corresponding spatial multiplication on the residual codomain, and define

\[
\boxed{C_{V,U}:=R_VQ_I-\widetilde Q_I R_V.}
\]

Then

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

and

\[
\|C_{V,U}\|=
\max\{\|\widetilde Q_B R_VQ_I\|,\|\widetilde Q_I R_VQ_B\|\}.
\]

Also

\[
[R_V^*R_V,Q_I]=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

Retaining the Feshbach factors gives

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

This is `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` as a local exact reduction only. `B-METINC-GEO-BMIX` remains OPEN because no decay or summability of `||C_{V,U}B_V||` has been proved.

## Exact prime-power form and fine-step dead layer

With `M_U=1_{(-U,U)}` on ambient `L^2(R)`, zero extension gives `E_VQ_I=M_UE_V`, hence

\[
(C_{V,U}f)(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
([D_{k\log p},M_U]E_Vf)(u)
\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Every channel is therefore a boundary-crossing translation commutator. Support localization alone does not imply small operator norm.

A stronger exact local fact follows from

\[
J_{p,V}(u)=
\max\left\{0,\left\lfloor\frac{2(V-|u|)_+}{\log p}\right\rfloor\right\}.
\]

If

\[
0<V-U<\frac12\log2,
\]

then for every `u` in `U<|u|<V` and every prime `p\ge2`, `J_{p,V}(u)=0`. Therefore

\[
\widetilde Q_B R_V=0.
\]

Because `\widetilde Q_I R_V=R_V` on such a step,

\[
\boxed{
C_{V,U}=R_VQ_I-R_V=-R_VQ_B.
}
\]

This is `R43-RESIDUAL-DEAD-LAYER ✓[M]`, a local fine-step theorem only. It is one-sided: source vectors in the new strip can still be translated inward, so BMIX need not vanish.

## Residual mark Gram algebra

For

\[
q_{p,k;V}(u)=\mathsf Q_V(u)\eta_{p,k},
\qquad
r=\min\{k,\ell,J_{p,V}(u)\},
\]

direct summation gives

\[
\langle q_{p,k;V}(u),q_{p,\ell;V}(u)\rangle
=
\begin{cases}
p^{r-(k+\ell)/2}-p^{-(k+\ell)/2},&r\ge1,\\
0,&r=0,
\end{cases}
\]

so

\[
0\le\langle q_{p,k;V}(u),q_{p,\ell;V}(u)\rangle
\le p^{-|k-\ell|/2}.
\]

Thus the `k`-correlations inside a fixed prime sector decay geometrically. This is `R43-RESIDUAL-MARK-GRAM ✓[M]` as local exact algebra; it does not control the prime sum by itself.

## NORMMIX and COND remain distinct

The normalized operator is

\[
\mathbf H_{\rm geo}=G_{S,U}^{-1/2}\Delta G_{\rm geo}G_{S,U}^{-1/2}.
\]

Thus `NORMMIX` remains

```text
B-METINC-NORMMIX [OPEN]
    control P_I G_{S,U}^{-1/2} P_B
```

or an equivalent commutator/reducing-subspace formulation.

The mechanisms remain distinct:

1. `BMIX`: fixed-`B_V` mixing, now reduced to conditioned `C_{V,U}B_V`;
2. `NORMMIX`: source-metric inverse square root mixes after pullback;
3. `COND`: actual terminal drift `B_U -> B_V`.

## Spectral-width and FD23 routes retained

For

\[
\mathbf H_X^{U,V}=G_{X,U}^{-1/2}(G_{X,V}-G_{X,U})G_{X,U}^{-1/2},
\]

\[
\|\mathscr E_{U,V}\|=\|[\mathbf H_S^{U,V},P_U]\|
\le\frac12\operatorname{width}\sigma(\mathbf H_S^{U,V}),
\]

and

\[
\mathfrak d_{m,\rm mod}(U,V)
\le
\frac{\operatorname{width}\sigma(\mathbf H_S^{U,V})}
{2\alpha_R(U,V)(\alpha_S(U,V)+\alpha_R(U,V))}.
\]

No cofinal uniform coercivity lower bound is booked.

For the canonical jet tails, every bounded `K\subset\mathcal H_S^0` satisfies

\[
K\text{ relatively norm compact}
\iff
\sup_{x\in K}\|P_S^{[m]}x\|\to0.
\]

This remains `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`; the concrete `FD23-UNIF` application remains OPEN.

## Immediate proof order

1. Estimate the **conditioned fine-step defect** `||R_VQ_BB_V||` (equal to `||C_{V,U}B_V||` when `V-U<log(2)/2`).
2. Use the one-sided dead-layer identity before any crude prime summation.
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
