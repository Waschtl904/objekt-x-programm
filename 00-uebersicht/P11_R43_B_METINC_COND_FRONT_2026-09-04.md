# P11 / R43 — B-METINC COND live front

**Date:** 2026-09-04  
**Status:** OPEN research front; canonical/eventual Loewner-PSD subroute closed negatively

**Single-source ledger:** `00-uebersicht/P11_R43_COND_LEDGER_2026-09-04.md`  
**Primary audits:**
- `audits/P11_R43_COND_COMPRESSION_REANCHOR_AUDIT_2026-09-04.md`
- `audits/P11_R43_COND_RESIDUAL_SCHUR_TARGET_COUPLING_2026-09-04.md`
- `audits/P11_R43_COND_COFINAL_GOVERNANCE_AND_STRIP_NORM_AUDIT_2026-09-04.md`
- `audits/P11_R43_COND_COFINAL_PSD_KERNEL_WITNESS_NOGO_2026-09-04.md`

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
\qquad
C=(I-\Pi_{U,V})M,
\]

frozen residual nesting gives

\[
\Pi_{U,V}M=\jmath R_U,
\qquad
M^*M-R_U^*R_U=C^*C\succeq0.
\]

The exact total sign operator is

\[
\boxed{
K_{U,V}^{\rm Schur}
=M^*(I+SS^*)^{-1}M-R_U^*R_U
=C^*C-M^*\Phi_SM.
}
\]

Thus pairwise canonical antitonicity is equivalent to `K_Schur>=0`.

## Breakthrough: canonical and eventual-fine-step PSD are false

The previous logical lemma remains valid: eventual PSD on every sufficiently late, sufficiently fine terminal pair **would** have been enough for the FD23 partition sign mechanism. The new kernel-witness theorem proves that this hypothesis is false in the frozen model.

For arbitrary `U_*>0` and `h_*>0`, choose `U>U_*` outside the locally finite resonance set

\[
\Lambda=\{n(\log p)/2:\ p\text{ prime},\ n\ge2\}.
\]

Then choose `0<h<h_*` sufficiently small and short intervals

\[
I_Q\subset(U,U+h),
\qquad
I_P=I_Q-\frac12\log2\subset(-U,U).
\]

With

\[
f=1_{I_P},\qquad g=1_{I_Q},
\]

the frozen fine-step layer geometry gives

\[
\boxed{Cf=0.}
\]

At the same time the `p=2`, adjacent-index overlap between the old source interval and the new strip survives. The first `(l,k)=(1,2)` overlap alone contributes

\[
|I_P|(\log2)2^{-9/4}>0
\]

to `\langle Mf,Sg\rangle`, and all other surviving exact `p=2` adjacent overlaps are nonnegative. Therefore

\[
\boxed{S^*Mf\ne0.}
\]

Hence

\[
\boxed{
\langle f,K_{U,U+h}^{\rm Schur}f\rangle
=-\|(I+S^*S)^{-1/2}S^*Mf\|^2<0.
}
\]

So

\[
\boxed{
\forall U_*,h_*>0\ \exists U\ge U_*\ \exists h\in(0,h_*):
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\]

Bookings:

```text
R43-COND-C-KERNEL-WITNESS-REALIZED          ✓[M]_neg
R43-COND-COFINAL-LOCAL-PSD                  ×[M]
R43-COND-CANONICAL-PSD-REALIZATION          ×[M]
R43-COND-LOEWNER-ANTITONE-TELESCOPE-ROUTE   ×[M]
```

This is a theorem-level negative result for the **arbitrary-source Loewner sign route only**. It is not a negative result for `B-METINC-COND` on the structured canonical vectors and not a Strong-Terminal no-go.

## What remains valid

The auxiliary comparator

\[
\widehat B_{U;V}=(I+\iota^*A_V\iota)^{-1}
\]

still satisfies

\[
\widehat B_{U;V}\preceq B_U
\]

because old-source residual energy increases. The exact internal split

\[
\iota^*B_V\iota-B_U
=(\widehat B_{U;V}-B_U)
+(\iota^*B_V\iota-\widehat B_{U;V})
\]

therefore remains useful as a **signed quantitative decomposition**, not as a positive telescope for the total term.

The comparator and split predate the adverse sign result (commit `669cda8204228f25ea840ea81733fdeb30c39cc4`, timestamp `2026-09-04T17:45:39Z`), so no taxonomy is being changed after the fact.

## Previously closed shortcuts

```text
R43-COND-TARGET-ORTHOGONALITY-SHORTCUT       ×[M]
R43-COND-OLD-RESIDUAL-STRIP-ORTHOGONALITY    ×[M]
R43-COND-AMBIENT-MFREE-DOMINATION-ROUTE      ×[M]
R43-COND-STRIP-NORM-SMALLNESS                ×[M]
R43-COND-CRITERION-B-OPNORM-ROUTE            ×[M]
```

The `p=2` coupling coefficient saturates at

\[
F_\infty=\frac{10-\sqrt2}{28}>0,
\]

and the strip block `||(I-\Pi)S||` is not operator-norm small; indeed it diverges cofinally. None of these facts decides the structured-vector COND estimate by itself because the exact Feshbach operator remains saturated.

## New live tree

```text
B-METINC-COND [OPEN]
├─ COND-INNER
│  ├─ old-source residual nesting ✓[M]
│  └─ Bhat_{U;V}-B_U <= 0 ✓[M]
├─ COND-SCHUR
│  ├─ residual-Schur reduction ✓[M]
│  ├─ zero-coupling shortcut ×[M]
│  ├─ ambient M-free domination ×[M]
│  ├─ strip-norm Criterion B ×[M]
│  └─ canonical/eventual Loewner PSD ×[M]
└─ STRUCTURED-VECTOR COND [OPEN]
   ├─ actual path v_U=H_U^*E_{X,U}f
   ├─ signed/absolute increment estimate [OPEN]
   └─ cofinal summability / m-tail compatible control [OPEN]
```

The abstract `R43-COND-REANCHOR-SUFFICIENT ✓[M]` theorem remains correct, but its application to a positive total canonical COND chain is no longer live because that chain is theorem-level false.

## Immediate next calculation

Stop testing arbitrary-source Loewner positivity. Insert the actual structured vector

\[
v_U=H_U^*E_{X,U}f
\]

into the exact signed split and estimate

\[
\bigl|\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle\bigr|.
\]

The preferred target is a directly summable B-FLAGDYN-compatible bound, ideally one carrying the fixed-source / `m`-tail mechanism before terminal summation.

## Status firewall

Still OPEN: structured-vector `B-METINC-COND`, `B-METINC-NORMMIX`, `B-METINC-GEO-BMIX`, `B-METINC-GEO-BDRY`, `B-METINC-NEW`, `FD23-UNIF`, `B-METINC-WIDTH`, `B-METINC`, `B-FLAGMOD`, `B-FLAGPHASE`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, R43, Object X, RH. No freeze and no new formal independent GREEN.