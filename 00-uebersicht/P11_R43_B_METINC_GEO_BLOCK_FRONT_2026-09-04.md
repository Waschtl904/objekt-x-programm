# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front

**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## Current front

The exact raw symmetric-strip theorem remains local. The fixed-terminal Feshbach cross block is now reduced by the type-correct residual intertwining defect

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V.
\]

With `B_V=(I+R_V^*R_V)^{-1}`,

\[
\boxed{
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
}
\]

Thus the crude factor `2||R_V||` is removed by retaining the Feshbach factors.

For fine terminal steps

\[
0<V-U<\frac12\log2,
\]

the frozen martingale cutoff kills the residual output in the entire new outer strip, so

\[
\widetilde Q_B R_V=0,
\qquad
\boxed{C_{V,U}=-R_VQ_B.}
\]

Hence the preferred BMIX target is now

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

## Exact local BMIX facts

Because `R_V` acts from the source space to a residual field space, `Q_I` acts on the source and `\widetilde Q_I` on the residual codomain. Then

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

The scalar bound

\[
\sup_{t\ge0}\frac{t}{1+t^2}=\frac12
\]

gives

\[
\|R_VB_V\|=\|B_VR_V^*\|\le\frac12,
\]

which yields `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` as a local exact reduction only.

The exact prime-power defect formula is

\[
(C_{V,U}f)(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
([D_{k\log p},M_U]E_Vf)(u)
\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Every channel is a boundary-crossing translation commutator. Support localization alone does not imply small operator norm.

The fine-step dead-layer theorem `R43-RESIDUAL-DEAD-LAYER ✓[M]` follows from the frozen depth

\[
J_{p,V}(u)=\max\left\{0,\left\lfloor\frac{2(V-|u|)_+}{\log p}\right\rfloor\right\}.
\]

For `V-U<log(2)/2`, every prime has zero depth on the new strip.

For the residual marks, with

\[
r=\min\{k,\ell,J_{p,V}(u)\},
\]

\[
\langle q_{p,k;V},q_{p,\ell;V}\rangle
=
\begin{cases}
p^{r-(k+\ell)/2}-p^{-(k+\ell)/2},&r\ge1,\\
0,&r=0,
\end{cases}
\]

and

\[
0\le\langle q_{p,k;V},q_{p,\ell;V}\rangle\le p^{-|k-\ell|/2}.
\]

This is `R43-RESIDUAL-MARK-GRAM ✓[M]` locally.

## Remaining firewalls

- `BMIX`: prove decay/summability of the conditioned fine-step defect `||R_VQ_BB_V||`.
- `BDRY`: control the strip quadratic term.
- `NORMMIX`: control `P_IG_{S,U}^{-1/2}P_B` or an equivalent commutator.
- `COND`: control the separate horizon drift `B_U -> B_V`.
- `FD23-UNIF`: prove fixed-interval compactness/norm continuity of the concrete modulus-vector family.

The positivity-free spectral-width route and full pairwise coercivity factor remain unchanged.

## Governance

Local exact only: `R43-GEO-RAW-STRIP ✓[M]`, `R43-BMIX-FESHBACH-ABSORPTION ✓[M]`, `R43-RESIDUAL-DEAD-LAYER ✓[M]`, `R43-RESIDUAL-MARK-GRAM ✓[M]`, `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`.

All project gates remain OPEN: B-METINC-GEO-BMIX, B-METINC-GEO-BDRY, B-METINC-NORMMIX, B-METINC-COND, FD23-UNIF, B-METINC-NEW, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6, R43. No freeze, no formal independent GREEN, no Object-X/RH promotion. R38–R42 unchanged/frozen; R37/G4c separate and OPEN.
