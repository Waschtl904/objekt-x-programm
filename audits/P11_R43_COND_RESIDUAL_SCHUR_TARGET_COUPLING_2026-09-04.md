# P11 / R43 — COND residual-Schur reduction and target-coupling audit

**Date:** 2026-09-04  
**Status:** local exact hardening; `B-METINC-COND` remains OPEN

## 0. Scope and governance firewall

This note follows the already frozen SW14 old-conditioning term

\[
\Delta s_{\rm cond}^{U,V}(f)
=\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle,
\qquad
\iota=E_{U,V},
\]

and the companion compression audit.  It records only exact algebraic and frozen-definition consequences.

It does **not** close `B-METINC-COND`, `B-METINC`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, Object X, or RH.  R43 remains OPEN; no freeze and no new formal independent-GREEN booking occur here.

The current SW14 taxonomy is **not redefined** in this note.  In particular, the Schur-compression correction remains a submechanism of the canonical old-conditioning term unless a separate future theorem proves a different taxonomic identification.

A useful chronology firewall is already present in the previous audit: the auxiliary comparator

\[
\widehat B_{U;V}:=(I+\iota^*A_V\iota)^{-1}
\]

and the split

\[
\iota^*B_V\iota-B_U
=(\widehat B_{U;V}-B_U)
+(\iota^*B_V\iota-\widehat B_{U;V})
\]

were recorded **before** the present target-space calculation.  Hence the comparator is not introduced retroactively in response to the sign outcome below.  It remains an auxiliary refinement, not a silent redefinition of canonical `COND`.

---

## 1. Block notation and exact residual-Schur collapse

Write the terminal-`V` source space as

\[
\mathcal H_V=\operatorname{Ran}\iota\oplus\mathcal N,
\qquad P_{\mathcal N}=I-\iota\iota^*,
\]

and put

\[
A_T:=R_T^*R_T,
\qquad B_T=(I+A_T)^{-1}.
\]

Define the two source blocks of the same frozen residual operator `R_V` by

\[
\boxed{
M:=R_V\iota:\mathcal H_U\to\mathcal K_V,
\qquad
S:=R_VP_{\mathcal N}:\mathcal N\to\mathcal K_V.
}
\tag{RS1}
\]

Then

\[
\iota^*A_V\iota=M^*M,
\qquad
\iota^*A_VP_{\mathcal N}=M^*S,
\qquad
P_{\mathcal N}A_VP_{\mathcal N}=S^*S.
\tag{RS2}
\]

The previous compression criterion used

\[
\Delta A:=M^*M-A_U,
\qquad
\Sigma:=M^*S(I+S^*S)^{-1}S^*M.
\tag{RS3}
\]

By the push-through identity

\[
S(I+S^*S)^{-1}=(I+SS^*)^{-1}S
\]

and hence

\[
I-S(I+S^*S)^{-1}S^*=(I+SS^*)^{-1},
\]

we obtain the exact collapse

\[
\boxed{
\Delta A-\Sigma
=M^*(I+SS^*)^{-1}M-R_U^*R_U.
}
\tag{RS4}
\]

Therefore the canonical order criterion becomes

\[
\boxed{
\iota^*B_V\iota\preceq B_U
\iff
M^*(I+SS^*)^{-1}M\succeq R_U^*R_U.
}
\tag{RS5}
\]

Equivalently, with the shielded old-source residual map

\[
\boxed{
T_{U,V}:=(I+SS^*)^{-1/2}M,
}
\tag{RS6}
\]

we have

\[
\boxed{
\iota^*B_V\iota\preceq B_U
\iff
T_{U,V}^*T_{U,V}\succeq R_U^*R_U
}
\tag{RS7}
\]

or pointwise

\[
\boxed{
\|T_{U,V}x\|^2\ge\|R_Ux\|^2
\qquad\forall x\in\mathcal H_U.
}
\tag{RS8}
\]

### Local booking

```text
R43-COND-RESIDUAL-SCHUR-REDUCTION ✓[M]
```

This is an exact operator identity; it does not decide the sign of the canonical COND term.

---

## 2. The Schur correction is a regularized target projection

Define

\[
\Phi_S:=SS^*(I+SS^*)^{-1}.
\tag{RS9}
\]

Then

\[
\boxed{
\Sigma=M^*\Phi_SM.
}
\tag{RS10}
\]

Functional calculus for `SS^*\succeq0` with `f(t)=t/(1+t)` gives

\[
\boxed{
0\preceq\Phi_S\preceq P_{\overline{\operatorname{Ran}S}}\preceq I.
}
\tag{RS11}
\]

In particular

\[
0\preceq\Sigma\preceq M^*M.
\tag{RS12}
\]

Moreover, because

\[
\ker\Phi_S=\ker S^*,
\]

we have the exact vanishing characterization

\[
\boxed{
\Sigma=0
\iff
S^*M=0
\iff
M^*S=0
\iff
\overline{\operatorname{Ran}M}\perp\overline{\operatorname{Ran}S}.
}
\tag{RS13}
\]

Thus `\iota\ne I` is **not** by itself an obstruction to `\Sigma=0`; the correct condition is target-space orthogonality.

### Local bookings

```text
R43-COND-SIGMA-AS-REGULARIZED-PROJECTION ✓[M]
R43-COND-SIGMA-VANISHING-CHARACTERIZATION ✓[M]
```

---

## 3. Canonical residual nesting on old source directions

The frozen P11 residual operator is

\[
(R_Tf)(u)
=\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Tf(u)\otimes\mathsf Q_T(u)\eta_{p,k}.
\tag{RS14}
\]

For `U<V`, zero extension gives

\[
E_V\iota=E_U.
\tag{RS15}
\]

For every prime and every `|u|<U`, the martingale depths satisfy

\[
J_{p,U}(u)\le J_{p,V}(u),
\]

so the old residual mark projection is nested inside the terminal-`V` one.  Let

\[
\Pi_{U,V}:\mathcal K_V\to\mathcal K_V
\]

be the orthogonal projection that keeps exactly

1. the old spatial window `|u|<U`, and
2. the old martingale levels `j<J_{p,U}(u)` in each prime sector.

Then the frozen definitions give the exact intertwining

\[
\boxed{
\Pi_{U,V}M=\jmath_{U,V}R_U,
}
\tag{RS16}
\]

where `\jmath_{U,V}` is the canonical isometric embedding of the old residual field into the terminal-`V` residual field.

Consequently, with

\[
C_{U,V}:=(I-\Pi_{U,V})M,
\]

we have an orthogonal decomposition

\[
M=\jmath_{U,V}R_U+C_{U,V}
\]

and therefore

\[
\boxed{
M^*M-R_U^*R_U=C_{U,V}^*C_{U,V}\succeq0.
}
\tag{RS17}
\]

Thus the **same-old-source residual energy itself is monotone**.  The only possible obstruction in the full compressed resolvent criterion is the source-extension Schur coupling encoded by `\Sigma`.

Equivalently,

\[
\widehat B_{U;V}:=(I+M^*M)^{-1}\preceq(I+R_U^*R_U)^{-1}=B_U.
\tag{RS18}
\]

### Local booking

```text
R43-COND-OLD-SOURCE-RESIDUAL-NESTING ✓[M]
```

This is a theorem about the frozen residual definitions.  It does not imply `\iota^*B_V\iota\preceq B_U`, because compression of the full inverse still contains `\Sigma`.

---

## 4. Governance-clean two-submechanism refinement inside canonical COND

Combining the already pre-existing auxiliary comparator with (RS18) gives the exact split

\[
\boxed{
\iota^*B_V\iota-B_U
=
\underbrace{(\widehat B_{U;V}-B_U)}_{\preceq0\;\text{old-source conditioning}}
+
\underbrace{(\iota^*B_V\iota-\widehat B_{U;V})}_{\succeq0\;\text{source-extension Schur coupling}}.
}
\tag{RS19}
\]

Both terms remain, by definition in this note, **inside canonical `COND`**.  No part is silently moved to the pre-existing `BMIX` or `BDRY` nodes.

This refinement is motivated by the canonical source decomposition and residual nesting, not by the eventual sign of the total term.  It may be referred to as

```text
COND-INNER   = old-source residual deepening / target enlargement
COND-SCHUR   = coupling to the newly added source strip before compression
```

but `B-METINC-COND` itself remains one OPEN gate.

---

## 5. Principal-angle sufficient criterion

Let

\[
c_{U,V}:=
\left\|
P_{\overline{\operatorname{Ran}S}}
P_{\overline{\operatorname{Ran}M}}
\right\|\in[0,1].
\tag{RS20}
\]

Since `\Phi_S\preceq P_{\overline{\operatorname{Ran}S}}`, for every `x`

\[
\langle x,\Sigma x\rangle
\le
\|P_{\overline{\operatorname{Ran}S}}Mx\|^2
\le
c_{U,V}^2\|Mx\|^2.
\]

Hence

\[
\boxed{
\Sigma\preceq c_{U,V}^2M^*M
=c_{U,V}^2(A_U+\Delta A).
}
\tag{RS21}
\]

Therefore

\[
\boxed{
(1-c_{U,V}^2)\Delta A\succeq c_{U,V}^2A_U
\Longrightarrow
\Delta A\succeq\Sigma
\Longrightarrow
\iota^*B_V\iota\preceq B_U.
}
\tag{RS22}
\]

This is **sufficient only**, not necessary.  In particular it cannot be used to falsify canonical PSD realization when it fails.

### Local booking

```text
R43-COND-PRINCIPAL-ANGLE-SUFFICIENT ✓[M]
```

---

## 6. Douglas reconstruction form

By Douglas factorization applied to (RS7),

\[
T_{U,V}^*T_{U,V}\succeq R_U^*R_U
\]

is equivalent to the existence of a contraction

\[
K_{U,V}:\overline{\operatorname{Ran}T_{U,V}}	o\overline{\operatorname{Ran}R_U}
\]

(extended by zero on the orthogonal complement if desired) such that

\[
\boxed{
R_U=K_{U,V}T_{U,V},
\qquad \|K_{U,V}\|\le1.
}
\tag{RS23}
\]

Thus canonical COND antitonicity is also equivalent to contractive recovery of the old residual data from the shielded terminal-`V` residual data on old source directions.

### Local booking

```text
R43-COND-DOUGLAS-RECONSTRUCTION-CRITERION ✓[M]
```

---

## 7. Target-space orthogonality is not available for fine terminal steps

The favorable shortcut `\Sigma=0` would require `M^*S=0`.  The frozen residual geometry does not have a disjoint-row structure of this kind.  In fact, for sufficiently late fine steps it fails exactly.

Put

\[
t:=\frac12\log2,
\qquad 0<h:=V-U<t,
\qquad U>t.
\tag{RS24}
\]

Choose `0<\delta<h` away from the finitely many window/translation threshold coincidences, and choose a sufficiently short interval `I_Q\subset(U,V)` centered at `V-\delta`.  Put

\[
I_P:=I_Q-2t\subset(-U,U),
\qquad
f:=1_{I_P},
\qquad
g:=1_{I_Q}.
\tag{RS25}
\]

Because the fixed-`V` residual sum is finite, the interval may be chosen so short that two translated copies of `I_P` and `I_Q` overlap only when their net source displacement agrees exactly.  Different prime sectors are orthogonal in frozen P11.  A prime-`p` overlap between these two source intervals requires

\[
\frac n2\log p=2t=\log2
\]

for an integer `n\ge1`, hence `p^n=4`.  The only possibility is

\[
p=2,\qquad n=2.
\tag{RS26}
\]

For the `p=2` sector, write the residual coefficient

\[
a_k:=\sqrt{\log2}\,2^{-k/4}.
\]

There are two types of surviving overlaps with source displacement `2t`:

1. `k=l=1`, at the outer overlap interval `I_Q-t`, with opposite translation signs;
2. `l=k+2`, `k\ge1`, at the interior intervals `I_Q-(k+2)t`, with equal translation signs.

The first interval has terminal depth `J_{2,V}=1`, so

\[
\langle q_1,q_1\rangle=\frac12.
\]

On the `k`-th interior interval one has `J_{2,V}=k+2`, and therefore

\[
\langle q_k,q_{k+2}\rangle
=\frac12-2^{-(k+1)}.
\]

Let `K\ge0` be the number of fully retained interior overlap intervals before the left terminal boundary.  Up to the positive factor `|I_Q|\log2`, the exact cross coefficient is

\[
\boxed{
F_K
=-2^{-3/2}
+\sum_{k=1}^{K}
2^{-(k+1)/2}
\left(\frac12-2^{-(k+1)}\right).
}
\tag{RS27}
\]

This coefficient never vanishes.  Indeed,

\[
F_0<0,
\]

\[
F_1=\frac18-\frac{\sqrt2}{4}<0,
\qquad
F_2=\frac18-\frac{5\sqrt2}{32}<0,
\]

while

\[
F_3=\frac{15-10\sqrt2}{64}>0.
\]

Every summand added after `K=3` is strictly positive, so

\[
F_K>0\qquad(K\ge3).
\]

Hence

\[
\boxed{
\langle R_V\iota f,\,R_VP_{\mathcal N}g\rangle\ne0.
}
\tag{RS28}
\]

Therefore

\[
\boxed{
M^*S\ne0,
\qquad
\Sigma\ne0
}
\tag{RS29}
\]

for every sufficiently late fine step satisfying (RS24), with the harmless generic choice of the short witness intervals made above.

This is a **negative result only for the exact target-orthogonality shortcut**.  It does **not** show `\Delta A\not\succeq\Sigma`; the positive old-source increment may still dominate the nonzero Schur correction.

A related stronger structural observation is that the old residual component itself also couples to strip input.  In the same witness geometry, the `k=l=1` outer term disappears after projection to the old residual depth because `J_{2,U}=0` there, while the `l=k+2` interior terms survive with positive Gram coefficients.  Thus, once at least one such interior interval lies in the old window,

\[
\boxed{
(\jmath_{U,V}R_U)^*S\ne0.
}
\tag{RS30}
\]

So the source-strip coupling is not confined to the newly added martingale layer.

### Local negative bookings

```text
R43-COND-TARGET-ORTHOGONALITY-SHORTCUT ×[M]
R43-COND-OLD-RESIDUAL-STRIP-ORTHOGONALITY ×[M]
```

Equivalently: the corresponding orthogonality claims are theorem-level false in the fine-step frozen model.

---

## 8. Erratum to the previous rank-one heuristic

The previous abstract statement

```text
if DeltaA has rank one and DeltaA >= Sigma, then rank Sigma <= 1
```

is mathematically correct.

However, it must **not** be applied to the canonical terminal-window increment merely because one pointwise martingale-depth layer is rank one in the `k`-Gram variables.  With

\[
M=R_V\iota
\]

the global operator

\[
\Delta A=M^*M-R_U^*R_U=C_{U,V}^*C_{U,V}
\]

aggregates all newly visible residual rows/layers on old source directions and is generically not rank one.

Therefore the earlier rank-one obstruction is withdrawn as an argument against canonical `R43-COND-CANONICAL-PSD-REALIZATION`.

---

## 9. Cheap witness tests after the reduction

The exact target is now

\[
\boxed{
K_{U,V}^{\rm Schur}
:=M^*(I+SS^*)^{-1}M-R_U^*R_U
\succeq0\;?
}
\tag{RS31}
\]

The residual nesting theorem immediately kills the cheapest kernel obstruction:

\[
Mx=0\Longrightarrow R_Ux=\Pi_{U,V}Mx=0.
\tag{RS32}
\]

Hence no witness of the form `Mx=0`, `R_Ux\ne0` exists in the frozen model.  In finite cutoffs this also implies

\[
\operatorname{rank}R_U\le\operatorname{rank}M.
\]

The next nontrivial test is therefore the actual shielded Rayleigh inequality (RS8), not a kernel/rank shortcut.

Numerical finite prime/depth/channel cutoffs may be used diagnostically, but no numerical sign is a `✓[M]` theorem.

---

## 10. Current live status

```text
B-METINC-COND [OPEN]
├─ COND-INNER (old-source residual deepening)
│  ├─ R43-COND-OLD-SOURCE-RESIDUAL-NESTING ✓[M]
│  └─ pairwise sign of Bhat_{U;V}-B_U: nonpositive ✓[M]
├─ COND-SCHUR (source-extension Schur coupling)
│  ├─ R43-COND-RESIDUAL-SCHUR-REDUCTION ✓[M]
│  ├─ R43-COND-SIGMA-AS-REGULARIZED-PROJECTION ✓[M]
│  ├─ R43-COND-SIGMA-VANISHING-CHARACTERIZATION ✓[M]
│  ├─ R43-COND-PRINCIPAL-ANGLE-SUFFICIENT ✓[M]
│  ├─ R43-COND-DOUGLAS-RECONSTRUCTION-CRITERION ✓[M]
│  ├─ R43-COND-TARGET-ORTHOGONALITY-SHORTCUT ×[M]
│  └─ shielded-energy sign K_Schur >= 0 ? [OPEN]
└─ R43-COND-FIXED-SOURCE-REANCHOR [OPEN]
```

The canonical PSD-realization node is now exactly

\[
\boxed{
R43\text{-}COND\text{-}CANONICAL\text{-}PSD\text{-}REALIZATION
\iff
K_{U,V}^{\rm Schur}\succeq0.
}
\]

No gate-level promotion follows.

---

## 11. Next mathematical step

The next calculation should exploit the exact orthogonal nesting

\[
M=\jmath R_U+C_{U,V}
\]

together with the nonzero decomposition of strip coupling

\[
S=\Pi_{U,V}S+(I-\Pi_{U,V})S.
\]

The decisive question is whether the extra energy `C_{U,V}^*C_{U,V}` always compensates the damping of the old residual component caused by `S`, or whether one can construct `x` with

\[
\|C_{U,V}x\|^2
<
\langle Mx,\Phi_SMx\rangle.
\]

A negative Rayleigh witness would falsify canonical COND antitonicity.  A positive theorem would close `R43-COND-CANONICAL-PSD-REALIZATION` and leave reanchor/summability as the next COND task.

---

## 12. Governance

Still OPEN: `R43-COND-CANONICAL-PSD-REALIZATION`, `R43-COND-FIXED-SOURCE-REANCHOR`, `B-METINC-COND`, `B-METINC-NORMMIX`, `B-METINC-GEO-BMIX`, `B-METINC-GEO-BDRY`, `B-METINC-NEW`, `B-METINC-WIDTH`, `B-METINC`, `B-FLAGMOD`, `B-FLAGPHASE`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, R43, Object X, RH.  R38–R42 remain frozen as before; R37/G4c remains separate and OPEN.  No freeze and no new formal independent GREEN.