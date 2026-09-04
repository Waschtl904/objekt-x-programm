# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front  
**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## Current BMIX reduction

The raw symmetric-strip geometry is local. With the type-correct residual intertwining defect

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V,
\]

one has

\[
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
\]

For fine steps `V-U<log(2)/2`, the frozen martingale cutoff gives

\[
\widetilde Q_B R_V=0,
\qquad
C_{V,U}=-R_VQ_B.
\]

Hence the preferred quantitative BMIX target is

\[
\boxed{\|R_VQ_BB_V\|}.
\]

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

Downstream remains

```text
B-METINC-WIDTH + FD23 machinery
  -> B-FLAGMOD contribution
  -> [with B-FLAGPHASE] B-FLAGTIGHT ?
  -> B-SIGN ?
  -> Strong Terminal ?
```

No converse is added.

## Exact local identities retained

Canonical P11 uses

\[
D_s=U_{s/2}-U_{-s/2},
\qquad
E_T:\mathscr H_T\to L^2(\mathbb R)\text{ zero extension},
\qquad
P_T=E_T^*.
\]

The raw old-hub increment between `U` and `V` is supported on

\[
\mathcal S_{U,V}=\{x:U<|x|<V\},
\]

which is `R43-GEO-RAW-STRIP ✓[M]` locally.

For BMIX, because `R_V` has different source and residual codomain spaces, `Q_I` acts on the source and `\widetilde Q_I` on the residual codomain. Then

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

\[
[R_V^*R_V,Q_I]=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

With `B_V=(I+R_V^*R_V)^{-1}`,

\[
Q_BB_VQ_I
=-Q_BB_VR_V^*C_{V,U}B_VQ_I
+Q_BB_VC_{V,U}^*R_VB_VQ_I,
\]

and

\[
\|R_VB_V\|=\|B_VR_V^*\|\le\frac12.
\]

This yields `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` locally.

The exact channel formula is

\[
(C_{V,U}f)(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
([D_{k\log p},M_U]E_Vf)(u)
\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Support localization alone does not imply operator-norm smallness.

For `0<V-U<log(2)/2`, the outer residual strip is killed by the frozen depth cutoff, giving `R43-RESIDUAL-DEAD-LAYER ✓[M]` and `C_{V,U}=-R_VQ_B`.

For the residual marks, if

\[
r=\min\{k,\ell,J_{p,V}(u)\},
\]

then

\[
\langle q_{p,k;V},q_{p,\ell;V}\rangle
=
\begin{cases}
p^{r-(k+\ell)/2}-p^{-(k+\ell)/2},&r\ge1,\\
0,&r=0,
\end{cases}
\]

and hence

\[
0\le\langle q_{p,k;V},q_{p,\ell;V}\rangle\le p^{-|k-\ell|/2}.
\]

This is `R43-RESIDUAL-MARK-GRAM ✓[M]` locally.

## Remaining firewalls

- `BMIX`: conditioned fine-step defect `||R_VQ_BB_V||` still needs decay/summability.
- `NORMMIX`: control the old-metric offblock `P_IG_{S,U}^{-1/2}P_B`.
- `COND`: control the separate horizon drift `B_U -> B_V`.
- `FD23-UNIF`: prove fixed-interval compactness/norm continuity of the concrete modulus-vector family.

The positivity-free spectral-width bound and the full pairwise coercivity factor remain unchanged.

## Governance

Local exact only: `R43-GEO-RAW-STRIP ✓[M]`, `R43-BMIX-FESHBACH-ABSORPTION ✓[M]`, `R43-RESIDUAL-DEAD-LAYER ✓[M]`, `R43-RESIDUAL-MARK-GRAM ✓[M]`, `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`.

All project-level gates remain OPEN: B-METINC-GEO-BMIX, B-METINC-GEO-BDRY, B-METINC-NORMMIX, B-METINC-COND, FD23-UNIF, B-METINC-NEW, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6, R43. No freeze, no formal independent GREEN, no Object-X/RH promotion. R38–R42 unchanged/frozen; R37/G4c separate and OPEN.
