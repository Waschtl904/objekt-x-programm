# P11 / R43 — B-METINC COND live front

**Date:** 2026-09-04  
**Status:** OPEN research front

**Single-source ledger:** `00-uebersicht/P11_R43_COND_LEDGER_2026-09-04.md`  
**Primary audits:**
- `audits/P11_R43_COND_COMPRESSION_REANCHOR_AUDIT_2026-09-04.md`
- `audits/P11_R43_COND_RESIDUAL_SCHUR_TARGET_COUPLING_2026-09-04.md`
- `audits/P11_R43_COND_COFINAL_GOVERNANCE_AND_STRIP_NORM_AUDIT_2026-09-04.md`

## Exact reduction

For `X<U<V`, canonical SW14 old-conditioning is

\[
\Delta s_{\rm cond}^{U,V}(f)
=\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle,
\qquad \iota=E_{U,V}.
\]

With

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\qquad
\Phi_S=SS^*(I+SS^*)^{-1},
\]

and the canonical old-residual projection `\Pi=\Pi_{U,V}`, put

\[
C=(I-\Pi)M.
\]

Frozen residual nesting gives

\[
\Pi M=\jmath R_U,
\qquad
M^*M-R_U^*R_U=C^*C\succeq0.
\]

The exact total sign operator is

\[
\boxed{
K_{U,V}^{\rm Schur}
:=M^*(I+SS^*)^{-1}M-R_U^*R_U
=C^*C-M^*\Phi_SM.
}
\]

Thus

\[
\boxed{
\iota^*B_V\iota\preceq B_U
\iff
K_{U,V}^{\rm Schur}\succeq0.
}
\]

## Correct cofinal sign target

The FD23 B-FLAGDYN sufficient criterion is partition-based.  Therefore the sign theorem actually needed by the current route is the eventual fine-step statement

\[
\boxed{
\exists U_*,h_*>0:\quad
U\ge U_*,\ 0<V-U<h_*
\Longrightarrow K_{U,V}^{\rm Schur}\succeq0.
}
\]

A global theorem for arbitrary coarse `U<V` is stronger than necessary.  This clarification is booked as

```text
R43-COND-COFINAL-LOCAL-PSD-SUFFICIENT ✓[M]
```

but the application statement `R43-COND-COFINAL-LOCAL-PSD` remains OPEN.  Sign alone also does not close reanchor/path summability.

## Governance/provenance firewall

The auxiliary comparator

\[
\widehat B_{U;V}=(I+\iota^*A_V\iota)^{-1}
\]

and the two-step split were already committed as equation `(C11)` in

```text
669cda8204228f25ea840ea81733fdeb30c39cc4
```

at GitHub author/committer time

```text
2026-09-04T17:45:39Z.
```

This predates the later referee request to decide the Lakatos/taxonomy issue.  Hence `COND-INNER` / `COND-SCHUR` is a pre-existing internal refinement, not an after-the-fact transfer of the adverse term into GEO-BMIX.  Canonical SW14 `COND` remains unchanged.

## What has been ruled out

### 1. Zero coupling

\[
\Sigma=M^*\Phi_SM=0
\iff M^*S=0.
\]

The explicit fine-step `p=2` collision witness proves `M^*S\ne0`.  Therefore:

```text
R43-COND-TARGET-ORTHOGONALITY-SHORTCUT ×[M]
R43-COND-OLD-RESIDUAL-STRIP-ORTHOGONALITY ×[M]
```

### 2. Ambient M-free domination

The exact ambient criterion is

\[
(I-\Pi)\succeq\Phi_S
\iff
\overline{\operatorname{Ran}S}\perp\operatorname{Ran}\Pi.
\]

The right side is false in the frozen model.  Hence any surviving proof must genuinely exploit the restricted range of `M`; full-target Loewner domination is unavailable.

```text
R43-COND-AMBIENT-MFREE-DOMINATION-ROUTE ×[M]
```

### 3. Old M-kernel/rank witnesses

Nesting forces

\[
\ker M\subseteq\ker R_U,
\]

and finite cutoffs satisfy `rank(R_U)<=rank(M)`.  The old cheap `Mx=0,R_Ux!=0` and rank-obstruction witness branches are therefore excluded.

The correct reduced kernel test is

\[
\ker C\subseteq\ker(S^*M)?
\]

because `Cx=0`, `S^*Mx\ne0` gives an immediate negative Rayleigh quotient.

### 4. Strip operator-norm smallness / Criterion B

The explicit `p=2` coefficient has the exact limit

\[
\boxed{
F_\infty=\frac{10-\sqrt2}{28}\approx0.3066352299,
}
\]

so the near cancellation at `K=3` is not asymptotic decay.

More importantly, for normalized strip indicators the old/new strip blocks have `h`-independent lower bounds.  In particular

\[
\liminf\|(I-\Pi)S\|^2
\ge\frac{1+\sqrt2}{2}\log2,
\]

already from `p=2`.  The full `k=1` prime layer gives the stronger cofinal lower bound

\[
\|(I-\Pi)S\|^2
\ge
\sum_{p\in\mathcal P(U)}(\log p)(p-1)p^{-3/2}
\to\infty.
\]

Thus shrinking terminal-strip width does **not** imply operator-norm smallness, and the proposed sufficient route with `beta=||(I-Pi)S||<1` cannot hold late:

```text
R43-COND-STRIP-NORM-SMALLNESS ×[M]
R43-COND-CRITERION-B-OPNORM-ROUTE ×[M]
```

This does not harm the exact Feshbach problem because `Phi_S=SS^*(I+SS^*)^-1<=I` saturates large strip norms.

## Current live tree

```text
B-METINC-COND [OPEN]
├─ COND-INNER
│  ├─ old-source residual nesting ✓[M]
│  └─ Bhat_{U;V}-B_U <= 0 ✓[M]
├─ COND-SCHUR
│  ├─ residual-Schur reduction ✓[M]
│  ├─ Sigma regularized projection ✓[M]
│  ├─ zero-coupling shortcut ×[M]
│  ├─ ambient M-free domination ×[M]
│  ├─ strip-norm Criterion B ×[M]
│  ├─ eventual fine-step K_Schur >= 0 ? [OPEN]
│  └─ exact M-relative Douglas/Rayleigh route [OPEN]
└─ fixed-source reanchor / path summability [OPEN]
```

## Immediate next calculation

Work in the explicit `p=2` collision family **without** replacing `Phi_S` by `SS^*` or by the full range projection.  The first destructive target is

\[
\ker C\subseteq\ker(S^*M)?
\]

If violated, canonical local PSD fails immediately.  If it holds, solve the exact generalized Rayleigh/Douglas problem

\[
\sup_{x\perp\ker C}
\frac{\langle Mx,\Phi_SMx\rangle}{\|Cx\|^2}
\le1\;?
\]

first in finite exact `p=2` cutoffs, with no theorem promotion until cutoff stability/exhaustion is proved.

## Status firewall

Still OPEN: `R43-COND-COFINAL-LOCAL-PSD`, stronger all-pairs `R43-COND-CANONICAL-PSD-REALIZATION`, `R43-COND-FIXED-SOURCE-REANCHOR`, `B-METINC-COND`, `B-METINC-NORMMIX`, `B-METINC-GEO-BMIX`, `B-METINC-GEO-BDRY`, `B-METINC-NEW`, `B-METINC-WIDTH`, `B-METINC`, `B-FLAGMOD`, `B-FLAGPHASE`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, R43, Object X, RH.  No freeze and no new formal independent GREEN.
