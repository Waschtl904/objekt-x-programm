# P11/R32 — IMG4 Small-R M1-ND Negative Candidate: External Review Packet

**Date:** 31 August 2026  
**Repository:** \`Waschtl904/objekt-x-programm\`  
**Branch:** \`research/sw1-m1-nd-img3-eliminator\`  
**Current claim:** candidate only; no promotion.

## Claim to review

At the explicit SW1 point
\[
\varepsilon_0=\Delta/4,\qquad
R_0=T/100000,\qquad
\sigma_0=R_0/2,
\]
the effective Cross-Gram operator satisfies
\[
\boxed{\ker\mathscr N_{R_0}\neq\{0\}.}
\]

Do **not** review the arithmetic \(\pm14\) coverage from scratch unless desired; it is already exact-certificate GREEN. The review target is the analytic bridge.

---

## Gate A — A8 graph dominates the actual Horizon offdiagonal graph

Please verify independently:

1. A1-R0..R7 contain no nonidentity Horizon source maps beyond
   \[
   \tau_{\pm a},\tau_{\pm T},r_a,r_T,r_{3a},r_{4a},r_{2b}.
   \]
2. Their lower-chamber activity-domain unions are exactly A7.1–A7.9.
3. In particular the full R6/R7 five-arm rows are included:
   \[
   R6:\ r_T,r_{3a},r_{4a},\tau_{-a},r_{2b},
   \]
   \[
   R7:\ \tau_{-T},r_{3a},r_{4a},\tau_{-a},r_{2b}.
   \]
4. Under the positive-half unitary model
   \[
   \mathscr T_B=V^*(I+A)V,
   \]
   this implies
   \[
   \operatorname{Graph}_{\rm off}(\mathscr T_B)\subseteq\mathcal G_{\rm A8}.
   \]
   Coefficient aggregation/cancellation may delete edges but cannot create new affine source maps.

Relevant files:
- \`audits/P11_R32_SW1_A1_FINITE_CELL_RAW_OPERATOR_CANDIDATE.md\`
- \`audits/P11_R32_SW1_A7_FINITE_STATE_COCYCLE_CANDIDATE.md\`
- \`audits/P11_R32_SW1_A8_LOWER_FINITE_COMPONENTS_CANDIDATE.md\`
- \`scripts/certify_sw1_m1_nd_img4_gate1_gate9_graph_p12.py\`

Verdict:
\[
\boxed{\text{GATE A: GREEN / PARTIAL / FAIL}}
\]

---

## Gate B — Uniform physical component bound and Mass Transport

Inputs:

- arithmetic separator coverage gives at most 65 index layers per **formal** A8 component;
- at most six formal lift states per layer, hence at most 390 states;
- A8.10B proves a physical sheet-collision quotient glues at most
  \[
  C\cup J_K(C),
  \]
  hence
  \[
  \boxed{\#C_{\rm phys}\le780.}
  \]

Let \(U_R\) be the six KNF half-windows, so \(|U_R|=6R\). Let
\[
V_R=\operatorname{Sat}_{\mathcal E}(U_R)
\]
for the physical A8 equivalence relation.

Please verify that the nine A7 generators form a countable pmp Borel graphing:
translations/reflections with Jacobi \(1\), with inverse branches included.

Then check the mass-transport calculation
\[
|V_R|
\le
\int_X\#([x]\cap U_R)\,dx
=
\int_{U_R}\#[y]\,dy
\le
780|U_R|
=
4680R.
\]

Verdict:
\[
\boxed{\text{GATE B: GREEN / PARTIAL / FAIL}}
\]

---

## Gate C — Reducing-subspace argument

For every active weighted pullback
\[
(T_\phi f)(x)
=
c_\phi(x)1_{D_\phi}(x)f(\phi(x)),
\]
saturation of \(V_R\) gives
\[
1_{V_R}(x)=1_{V_R}(\phi(x))
\]
on the active graph.

Please verify
\[
P_{V_R}T_\phi=T_\phi P_{V_R}
\]
for every offdiagonal term and trivial commutation for diagonal multipliers. Therefore
\[
P_{V_R}\mathscr T_B=\mathscr T_BP_{V_R}.
\]

Since
\[
\mathscr T_B=V^*(I+A)V\ge I,
\]
it is invertible and
\[
\boxed{
P_{V_R}\mathscr T_B^{-1}
=
\mathscr T_B^{-1}P_{V_R}.
}
\]

Please check especially that no KNF reconstruction operator \(J_R\) has been inserted here: IMG4 acts on the **physical Horizon block \(\mathscr T_B\)** before restricting the constructed solution to \(\mathscr B_K\). A9's warning about \(J_R^*(I+A)J_R\) is therefore not an objection to this step.

Verdict:
\[
\boxed{\text{GATE C: GREEN / PARTIAL / FAIL}}
\]

---

## Gate D — Blindset and actual Domain kernel

From Gate B:
\[
|V_{R_0}|\le4680R_0.
\]

The positive odd-folded Hub has at most six source branches
\[
|x-a|,\ x+a,\ |x-b|,\ x+b,\ |x-T|,\ x+T.
\]
Each branch does not increase Lebesgue measure, hence
\[
|W^{\rm vis}_{R_0}|
\le6|V_{R_0}|
\le28080R_0
=
\frac{351}{1250}T.
\]

The positive Annulus length is
\[
S_0-R_0
=
\left(1-\frac1{200000}\right)T,
\]
so the complement \(B_0\) has positive measure.

Choose
\[
0\neq w\in L^2(B_0)
\]
and odd-fold it. Then
\[
P_{V_{R_0}}\mathcal H_{R_0}w=0.
\]

Define
\[
f=-\mathscr T_B^{-1}\mathcal H_{R_0}w.
\]
Gate C gives
\[
P_{V_{R_0}}f=0.
\]

Since the six KNF sampling half-windows \(U_{R_0}\subset V_{R_0}\),
\[
f|_{U_{R_0}}=0
\]
and therefore the KNF descriptor vanishes:
\[
f\in\mathscr B_K.
\]

Finally IMG2 gives
\[
\mathscr N_R(f,w)
=
\mathscr T_Bf+\mathcal H_Rw,
\]
hence
\[
\mathscr N_{R_0}(f,w)=0.
\]
Because \(w\neq0\), the kernel pair is nonzero.

Please verify that this is genuinely on
\[
\mathscr B_K\oplus\mathscr B_W
\]
and not on the ambient slot space.

Verdict:
\[
\boxed{\text{GATE D: GREEN / PARTIAL / FAIL}}
\]

---

## Optional compatibility check — P12

This is **not needed** for \(\ker\mathscr N_{R_0}\neq0\).

It is needed only for the stronger interpretation that the candidate is an indirect Schur/Cross-Gram annihilator rather than a trivial outer Hub kernel.

At the witness point:
\[
\sigma_0<R_0,\qquad
T_0=T+\Delta/4<\frac12\log5.
\]
The last inequality is exactly
\[
2^5 3^2=288<625=5^4.
\]

Thus P12 all-radius restricted-tail injectivity gives
\[
\ker(HE_{\mathcal A}|_-)=0.
\]

Verdict:
\[
\boxed{\text{P12 COMPATIBILITY: GREEN / PARTIAL / FAIL}}
\]

---

## Promotion rule

Promote only if Gates A–D are all independently GREEN.

Then the permissible status is
\[
\boxed{
\mathrm{M1\!-\!ND\!-\!SMALLR}:\checkmark[M]_{\rm neg}
}
\]
for the explicit witness parameter point, and therefore a No-Go against the claim that M1-ND holds on the **entire** SW1 scope.

Do not infer:
- failure for every SW1 parameter;
- failure of every finite-level geometry;
- failure of Object X as a whole;
- any RH conclusion.
