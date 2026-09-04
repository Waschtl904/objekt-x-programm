# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front

**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## Current front

With the type-correct residual intertwining defect `C_{V,U}=R_VQ_I-\widetilde Q_I R_V` and `B_V=(I+R_V^*R_V)^{-1}`,

\[
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
\]

For `0<V-U<log(2)/2`, the frozen martingale cutoff yields `\widetilde Q_B R_V=0` and hence `C_{V,U}=-R_VQ_B`. Thus the preferred quantitative BMIX target is `||R_VQ_BB_V||`.

## Live tree

```text
B-METINC-WIDTH [OPEN]
├─ B-METINC-NEW [OPEN]
├─ B-METINC-GEO [OPEN]
│  ├─ R43-GEO-RAW-STRIP ✓[M]
│  ├─ B-METINC-GEO-BMIX [OPEN]
│  │  ├─ FESHBACH-ABSORPTION ✓[M]
│  │  ├─ RESIDUAL-DEAD-LAYER ✓[M]
│  │  ├─ RESIDUAL-MARK-GRAM ✓[M]
│  │  └─ conditioned defect decay/summability [OPEN]
│  └─ B-METINC-GEO-BDRY [OPEN]
├─ B-METINC-NORMMIX [OPEN]
├─ B-METINC-COND [OPEN]
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

Downstream remains `B-METINC -> B-FLAGMOD`, together with `B-FLAGPHASE` as the sufficient route to `B-FLAGTIGHT`, then `B-SIGN`, then Strong Terminal. No converse is added.

## Exact BMIX identities

Because `R_V` acts between source and residual field spaces, source projection `Q_I` and residual projection `\widetilde Q_I` are distinct. Then

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

and

\[
[R_V^*R_V,Q_I]=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

Retaining both Feshbach factors gives

\[
Q_BB_VQ_I=-Q_BB_VR_V^*C_{V,U}B_VQ_I+Q_BB_VC_{V,U}^*R_VB_VQ_I,
\]

with `||R_VB_V||=||B_VR_V^*||<=1/2`. This is `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` locally; BMIX remains OPEN.

The exact prime-power defect formula is

\[
(C_{V,U}f)(u)=\sum_{p,k}\sqrt{\log p}\,p^{-k/4}([D_{k\log p},M_U]E_Vf)(u)\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Support localization alone does not imply norm smallness.

The fine-step dead-layer theorem `R43-RESIDUAL-DEAD-LAYER ✓[M]` follows from the frozen source-dependent depth. For residual marks, with `r=min{k,l,J_{p,V}(u)}`,

\[
\langle q_{p,k;V},q_{p,l;V}\rangle=\begin{cases}p^{r-(k+l)/2}-p^{-(k+l)/2},&r\ge1,\\0,&r=0,\end{cases}
\]

hence `0<=<q_{p,k;V},q_{p,l;V}><=p^{-|k-l|/2}`. This is `R43-RESIDUAL-MARK-GRAM ✓[M]` locally.

## Remaining firewalls

BMIX conditioned decay/summability, BDRY, NORMMIX, COND, and concrete FD23-UNIF remain OPEN.

## Governance

Local exact only: `R43-GEO-RAW-STRIP ✓[M]`, `R43-BMIX-FESHBACH-ABSORPTION ✓[M]`, `R43-RESIDUAL-DEAD-LAYER ✓[M]`, `R43-RESIDUAL-MARK-GRAM ✓[M]`, `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`.

All project gates remain OPEN, including B-METINC-GEO-BMIX, B-METINC-GEO-BDRY, B-METINC-NORMMIX, B-METINC-COND, FD23-UNIF, B-METINC-NEW, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6, and R43. No freeze, no formal independent GREEN, no Object-X/RH promotion. R38–R42 unchanged/frozen; R37/G4c separate and OPEN.
