# CURRENT FRONT — Objekt X / P11 Strong Terminal

> **Operative Kopfschicht — zuerst lesen.**  
> **Stand:** 4. September 2026  
> **Aktive Härtung:** `research/r43-gcac-hardening`.  Der aktuelle R43-Arbeitsbaum bleibt OPEN.  Primärgate ist weiterhin **B-FLAGTIGHT**; die bevorzugte derivative-free Route ist **B-FLAGDYN**.  Für den Modulus-Zweig ist `B-METINC` offen und zerfällt in NEW / GEO / NORMMIX / COND plus `FD23-UNIF`.  Der COND-Teil hat jetzt eine eigene Single-Source-Registry: `00-uebersicht/P11_R43_COND_LEDGER_2026-09-04.md`.  Strong Terminal/C6, R43, Object X und RH bleiben OPEN; kein Freeze und keine Gate-Promotion.

## 1. Aktuelles Ziel

Für festes `0<R<S` ist der verbleibende Strong-Terminal-Block weiterhin die Normalbahn.  Die sufficient research chain ist

```text
GC-AC candidate-closed
  -> [B-FLAGMOD + B-FLAGPHASE]
  => B-FLAGTIGHT
  -> B-SIGN
  -> Strong Terminal ?
```

Das `=>` ist nur hinreichend, keine Äquivalenz.

## 2. B-FLAGDYN

Auf festem Quellraum

\[
Q_{m,U}=W_U^*P_mW_U,
\qquad
q_m(U)=\langle\varepsilon_R,Q_{m,U}\varepsilon_R\rangle.
\]

Die O1-Modulus/Phase-Reduktion liefert die beiden projizierten Defektkanäle `B-FLAGMOD` und `B-FLAGPHASE`.  FD23 ist partition-basiert: es genügt, auf einer kofinalen feinen Terminalpartition summierbare Zellmajoranten zu erhalten.

## 3. B-METINC live tree

```text
B-METINC-WIDTH [OPEN]
├─ B-METINC-NEW [OPEN]
├─ B-METINC-GEO [OPEN]
│  ├─ R43-GEO-RAW-STRIP ✓[M]
│  ├─ B-METINC-GEO-BMIX [OPEN]
│  │  ├─ R43-BMIX-FESHBACH-ABSORPTION ✓[M]
│  │  ├─ R43-RESIDUAL-DEAD-LAYER ✓[M]
│  │  ├─ R43-RESIDUAL-MARK-GRAM ✓[M]
│  │  └─ conditioned decay/summability [OPEN]
│  └─ B-METINC-GEO-BDRY [OPEN]
├─ B-METINC-NORMMIX [OPEN]
├─ B-METINC-COND [OPEN]
│  └─ see 00-uebersicht/P11_R43_COND_LEDGER_2026-09-04.md
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

## 4. Current COND checkpoint

Canonical old-conditioning is

\[
\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle,
\qquad \iota=E_{U,V}.
\]

Set

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\qquad
\Phi_S=SS^*(I+SS^*)^{-1},
\qquad
C=(I-\Pi_{U,V})M.
\]

Frozen residual nesting gives

\[
\Pi_{U,V}M=\jmath R_U,
\qquad
M^*M-R_U^*R_U=C^*C\succeq0.
\]

The exact sign operator is

\[
\boxed{
K_{U,V}^{\rm Schur}
=M^*(I+SS^*)^{-1}M-R_U^*R_U
=C^*C-M^*\Phi_SM.
}
\]

The stronger all-pairs sign theorem is OPEN.  For the partition strategy the relevant sufficient target has been sharpened to eventual fine-step PSD:

\[
\exists U_*,h_*>0:\quad U\ge U_*,\ 0<V-U<h_*
\Longrightarrow K_{U,V}^{\rm Schur}\succeq0.
\]

That application theorem is also OPEN.

### Current COND negatives

The following shortcuts are theorem-level unavailable:

- target zero-coupling `M^*S=0`;
- old-residual / strip orthogonality;
- ambient `M`-independent domination `(I-\Pi)\succeq\Phi_S`;
- the old `Mx=0, R_Ux\ne0` and rank witness branches;
- strip operator-norm smallness;
- the proposed `\beta<1` Criterion-B operator-norm route.

The explicit `p=2` witness has

\[
F_K\to F_\infty=\frac{10-\sqrt2}{28}>0,
\]

so the near cancellation at `K=3` is not asymptotic.  More strongly, the `k=1` prime layer gives cofinal growth of `\|(I-\Pi)S\|`; large strip norm is nevertheless absorbed by the saturated Feshbach factor `\Phi_S\le I` and therefore does not decide the exact sign.

The next destructive target is

\[
\ker C\subseteq\ker(S^*M)?
\]

followed, if necessary, by the exact generalized Rayleigh/Douglas problem on finite exact `p=2` cutoffs with a separate exhaustion theorem before any promotion.

## 5. Governance

The auxiliary comparator

\[
\widehat B_{U;V}=(I+\iota^*A_V\iota)^{-1}
\]

and the internal two-step split were already committed in `669cda8204228f25ea840ea81733fdeb30c39cc4` at GitHub timestamp `2026-09-04T17:45:39Z`, before the later referee request on the taxonomy question.  Thus `COND-INNER` / `COND-SCHUR` is not a post-hoc move of the adverse term into GEO-BMIX.

R38–R42 remain unchanged/frozen under their existing reviewer/governance status.  R37/G4c remains separate and OPEN.  No new formal independent GREEN, no Strong-Terminal/C6 promotion, no Object-X/RH promotion.
