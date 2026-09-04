# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front

**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`
- `audits/P11_R43_COND_COMPRESSION_REANCHOR_AUDIT_2026-09-04.md`
- `audits/P11_R43_COND_RESIDUAL_SCHUR_TARGET_COUPLING_2026-09-04.md`
- `audits/P11_R43_COND_COFINAL_PSD_KERNEL_WITNESS_NOGO_2026-09-04.md`

## Current front

With the type-correct residual intertwining defect `C_{V,U}=R_VQ_I-\widetilde Q_I R_V` and `B_V=(I+R_V^*R_V)^{-1}`,

\[
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
\]

For `0<V-U<=log(2)/2`, the frozen martingale cutoff yields the dead outer residual layer and the conditioned one-way BMIX channel.  BMIX itself remains OPEN.

The canonical SW14 old-conditioning term is

\[
\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle,
\qquad \iota=E_{U,V}.
\]

Set

\[
M=R_V\iota,
\qquad S=R_VP_{\mathcal N},
\qquad\Phi_S=SS^*(I+SS^*)^{-1},
\qquad C=(I-\Pi_{U,V})M.
\]

Frozen nesting gives

\[
\Pi_{U,V}M=\jmath R_U,
\qquad M^*M-R_U^*R_U=C^*C\succeq0,
\]

and the exact total sign operator is

\[
K_{U,V}^{\rm Schur}=C^*C-M^*\Phi_SM.
\]

### COND sign route: negative theorem

The explicit cofinal kernel witness proves that for arbitrary `U_*,h_*>0` there exist `U>=U_*` and `0<h<h_*` with an old-source vector `f` satisfying

\[
Cf=0,
\qquad S^*Mf\ne0.
\]

Therefore

\[
\langle f,K_{U,U+h}^{\rm Schur}f\rangle
=-\|(I+S^*S)^{-1/2}S^*Mf\|^2<0.
\]

Hence both the all-pairs canonical Loewner order and the eventual-fine-step PSD sufficient route are theorem-level false:

```text
R43-COND-C-KERNEL-WITNESS-REALIZED          ✓[M]_neg
R43-COND-COFINAL-LOCAL-PSD                  ×[M]
R43-COND-CANONICAL-PSD-REALIZATION          ×[M]
R43-COND-LOEWNER-ANTITONE-TELESCOPE-ROUTE   ×[M]
```

This does **not** close `B-METINC-COND` negatively.  The live COND target is now the structured canonical path `v_U=H_U^*E_{X,U}f`, with a signed/absolute increment estimate rather than global operator order.

## Live tree

```text
B-METINC-WIDTH [OPEN]
├─ B-METINC-NEW [OPEN]
├─ B-METINC-GEO [OPEN]
│  ├─ R43-GEO-RAW-STRIP ✓[M]
│  ├─ B-METINC-GEO-BMIX [OPEN]
│  │  ├─ FESHBACH-ABSORPTION ✓[M]
│  │  ├─ RESIDUAL-DEAD-LAYER-SHARP ✓[M]
│  │  ├─ RESIDUAL-MARK-GRAM ✓[M]
│  │  └─ conditioned defect decay/summability [OPEN]
│  └─ B-METINC-GEO-BDRY [OPEN]
├─ B-METINC-NORMMIX [OPEN]
├─ B-METINC-COND [OPEN]
│  ├─ COND-INNER sign ✓[M]
│  ├─ total canonical Loewner/PSD route ×[M]
│  └─ structured-vector signed/absolute estimate [OPEN]
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

Downstream remains `B-METINC -> B-FLAGMOD`, together with `B-FLAGPHASE` as the sufficient route to `B-FLAGTIGHT`, then `B-SIGN`, then Strong Terminal. No converse is added.

## Exact BMIX identities retained

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

Retaining both Feshbach factors gives the local exact `R43-BMIX-FESHBACH-ABSORPTION ✓[M]`.  Support localization alone does not imply norm smallness.

## Structured-vector COND pivot

The auxiliary comparator

\[
\widehat B_{U;V}=(I+\iota^*A_V\iota)^{-1}
\]

still obeys `\widehat B_{U;V}\preceq B_U`, so the exact signed split

\[
\iota^*B_V\iota-B_U
=(\widehat B_{U;V}-B_U)
+(\iota^*B_V\iota-\widehat B_{U;V})
\]

remains a useful quantitative decomposition.  It must now be estimated on the actual `v_U`, not promoted to a positive total telescope.

The first-martingale `H/R` coefficient match and fixed-source prime-power shell localization are the preferred next inputs.

## Governance

Local exact/negative only.  `B-METINC-COND`, BMIX, BDRY, NORMMIX, NEW, FD23-UNIF, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6 and R43 remain OPEN.  No freeze, no formal independent GREEN, no Object-X/RH promotion.  R38--R42 unchanged/frozen; R37/G4c separate and OPEN.