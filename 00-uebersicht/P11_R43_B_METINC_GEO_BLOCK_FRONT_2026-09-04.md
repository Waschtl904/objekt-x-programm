# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front

**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`

## Current front

The fixed-terminal BMIX block is reduced by the type-correct residual intertwining defect

\[
C_{V,U}=R_VQ_I-\widetilde Q_I R_V
\]

and

\[
\boxed{
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
}
\]

For `0<V-U<log(2)/2`, the frozen martingale cutoff yields

\[
\widetilde Q_B R_V=0,
\qquad
\boxed{C_{V,U}=-R_VQ_B.}
\]

Thus the preferred quantitative BMIX target is `||R_VQ_BB_V||`.

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

## Exact local BMIX identities

`R_V` acts from the source space to a residual field space. `Q_I` acts on the source and `\widetilde Q_I` on the residual codomain. Hence

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

\[
\|C_{V,U}\|=
\max\{\|\widetilde Q_B R_VQ_I\|,\|\widetilde Q_I R_VQ_B\|\},
\]

and

\[
[R_V^*R_V,Q_I]=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

With `B_V=(I+R_V^*R_V)^{-1}`,

\[
Q_BB_VQ_I
=-Q_BB_VR_V^*C_{V,U}B_VQ_I
+Q_BB_VC_{V,U}^*R_VB_VQ_I,
\]

while

\[
\|R_VB_V\|=\|B_VR_V^*\|
=\sup_{t\ge0}\frac{t}{1+t^2}\le\frac12.
\]

This is `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` locally; BMIX remains OPEN.

The exact prime-power defect is

\[
(C_{V,U}f)(u)
=
\sum_{p,k}
\sqrt{\log p}\,p^{-k/4}
([D_{k\log p},M_U]E_Vf)(u)
\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Support localization alone does not imply operator-norm smallness.

For fine steps the frozen depth

\[
J_{p,V}(u)=\max\left\{0,\left\lfloor\frac{2(V-|u|)_+}{\log p}\right\rfloor\right\}
\]

is zero throughout the new strip for every prime. This gives `R43-RESIDUAL-DEAD-LAYER ✓[M]` locally.

For the residual marks, with `r=min{k,l,J_{p,V}(u)}`,

\[
\langle q_{p,k;V},q_{p,l;V}\rangle
=
\begin{cases}
p^{r-(k+l)/2}-p^{-(k+l)/2},&r\ge1,\\
0,&r=0,
\end{cases}
\]

and therefore

\[
0\le\langle q_{p,k;V},q_{p,l;V}\rangle\le p^{-|k-l|/2}.
\]

This is `R43-RESIDUAL-MARK-GRAM ✓[M]` locally.

## Remaining firewalls

- BMIX: decay/summability of `||R_VQ_BB_V||`.
- BDRY: strip quadratic term.
- NORMMIX: old-metric offblock `P_IG_{S,U}^{-1/2}P_B`.
- COND: separate terminal drift `B_U -> B_V`.
- FD23-UNIF: fixed-interval compactness/norm continuity of the concrete modulus-vector family.

## Governance

Local exact only: `R43-GEO-RAW-STRIP ✓[M]`, `R43-BMIX-FESHBACH-ABSORPTION ✓[M]`, `R43-RESIDUAL-DEAD-LAYER ✓[M]`, `R43-RESIDUAL-MARK-GRAM ✓[M]`, `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`.

All project gates remain OPEN: B-METINC-GEO-BMIX, B-METINC-GEO-BDRY, B-METINC-NORMMIX, B-METINC-COND, FD23-UNIF, B-METINC-NEW, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6, R43. No freeze, no formal independent GREEN, no Object-X/RH promotion. R38–R42 unchanged/frozen; R37/G4c separate and OPEN.
