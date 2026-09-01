# P11/R32 — SALVAGE-A1/A2 Uniform Blind Wedge Review Packet

**Date:** 1 September 2026  
**Branch:** `research/sw1-m1-nd-salvage-phase-diagram`  
**Current status:** AI-GREEN candidate + exact finite/algebraic certificate; no promotion.

## Claim under review

Let

[
arepsilon_c=rac{T-10Delta}{8}.
]

For every

[
0<arepsilon<arepsilon_c,
qquad
0<R<arepsilon,
qquad
0<sigma<R,
]

does the current effective operator satisfy

[
kermathscr N_R
e{0}?
]

Primary proof:
`audits/P11_R32_SW1_M1_ND_SALVAGE_A1_A2_UNIFORM_BLIND_WEDGE_CANDIDATE.md`

Primary exact certificate:
`scripts/certify_sw1_m1_nd_salvage_a1_a2_uniform_blind_wedge.py`

---

## Gate A — exact epsilon-uniform interval arithmetic

Verify the sign engine independently.

Every comparison used by the certificate is affine in (arepsilon).  The
script evaluates its sign exactly at the two endpoints
(arepsilon=0,arepsilon=arepsilon_c), with logarithmic signs reduced to
integer comparisons (2^m) versus (3^n).

Check especially:

[
h=rac{T-10Delta}{4}=d-3Delta>0,
]

and

[
0<arepsilon<h/2
Longrightarrow
h-2arepsilon>0.
]

Confirm that no comparison marked uniform can cross zero inside the open
wedge.

**Verdict:** GREEN / PARTIAL / FAIL

---

## Gate B — graph-invariant Horizon complement

The 24 forbidden gaps are

[
F_{s,k,j}
=
(s+kDelta+jh+arepsilon,,
 s+kDelta+(j+1)h-arepsilon)
]

for

[
sin{0,a},quad
k=0,ldots,5,quad
j=0,1.
]

Check:

1. all 24 gaps are ordered/disjoint and lie in ((0,T));
2. the maximal sampling majorant
   [
   U_arepsilon^{max}
   =
   (a-arepsilon,a+arepsilon)
   cup
   (b-arepsilon,b+arepsilon)
   cup
   (T-arepsilon,T+arepsilon)
   ]
   avoids them;
3. every active image of (F_arepsilon) under all nine A7 maps lies back
   in (F_arepsilon);
4. the inverse-domain facts are sufficient to conclude that
   (K_arepsilon=F_arepsilon^c) is invariant a.e.;
5. hence for every (R<arepsilon),
   [
   V_{arepsilon,R}
   =
   operatorname{Sat}_{mathcal E_arepsilon}(U_R)
   subset K_arepsilon.
   ]

The certificate reports exactly 70 nonempty forbidden-gap/map-domain pieces.

Relevant upstream:
- `audits/P11_R32_SW1_A7_FINITE_STATE_COCYCLE_CANDIDATE.md`
- `scripts/certify_sw1_m1_nd_img4_gateB_pmp_graphing.py`

**Verdict:** GREEN / PARTIAL / FAIL

---

## Gate C — 14-gap Hub exclusion

The candidate positive Annulus blind set is

[
B_arepsilon
=
igcup_{cinmathcal C}
(c+arepsilon,c+h-arepsilon)
]

with

[
mathcal C=
{
0,Delta,2Delta,3Delta,
d,d+Delta,d+2Delta,
a,a+Delta,a+2Delta,a+3Delta,
b,b+Delta,b+2Delta
}.
]

Check:

1. the 14 intervals are pairwise disjoint and contained in
   ((arepsilon,T));
2. the 24-gap complement has exactly 25 interval cells;
3. after splitting the three absolute-value maps at (a,b,T), every physical
   Hub source piece
   [
   |x-a|, x+a, |x-b|, x+b, |x-T|, x+T
   ]
   from every (K_arepsilon)-cell avoids every interval of
   (B_arepsilon);
4. the reported 153 nonempty image pieces are exhaustive;
5. therefore
   [
   H(V_{arepsilon,R})cap B_arepsilon=arnothing.
   ]

Check the exact measure identity

[
|B_arepsilon|
=
14(h-2arepsilon)
=
rac72(T-10Delta-8arepsilon)>0.
]

**Verdict:** GREEN / PARTIAL / FAIL

---

## Gate D — parameter-uniform analytic kernel handoff

This is the only non-finite gate.

Check that the already audited/promoted IMG4 mechanism used here does not rely
on the old special value (arepsilon=Delta/4) except in the discarded
Mass-Transport/780 estimate.

Needed statements:

1. for the lower chamber the actual FREE offdiagonal graph is contained in the
   nine A7 maps;
2. for any measurable A7-saturated (V),
   [
   Pi_Vmathscr T_B=mathscr T_BPi_V,
   qquad
   Pi_Vmathscr T_B^{-1}=mathscr T_B^{-1}Pi_V;
   ]
3. the unitary Annulus transport gives
   [
   mathcal H_R=V^*HW
   ]
   for all SW1 parameters;
4. if (ginmathscr B_W) is supported in (B_arepsilon), then
   [
   Pi_{V_{arepsilon,R}}mathcal H_Rg=0;
   ]
5. with
   [
   f=-mathscr T_B^{-1}mathcal H_Rg,
   ]
   one gets (f=0) on (U_R), hence (finmathscr B_K);
6. therefore
   [
   mathscr N_R(f,g)=0,
   qquad
   (f,g)
e0.
   ]

Important: no 780 component bound, no Mass Transport, and no finite-component
theorem is needed in this new proof.

Relevant files:
- `audits/P11_R32_SW1_M1_ND_IMG4_ANALYTIC_GATES_CANDIDATE.md`
- `audits/P11_R32_SW1_M1_ND_IMAGE_SPACE_CANDIDATE.md`
- `audits/P11_R32_SW1_M1_ND_IMG4_SMALLR_NEG_PROMOTION.md`

**Verdict:** GREEN / PARTIAL / FAIL

---

## Promotion criterion

Promote the wedge only if Gates A–D are all GREEN.

If promoted, the exact scope would be

[
oxed{
0<arepsilon<rac{T-10Delta}{8},
quad
0<R<arepsilon,
quad
0<sigma<R
Longrightarrow
kermathscr N_R
e{0}.
}
]

with explicit uniform blind measure

[
oxed{
|B_arepsilon|
ge
rac72(T-10Delta-8arepsilon)>0.
}
]

No claim that (arepsilon_c) is the exact global phase transition.  
No injectivity claim for (arepsilongearepsilon_c).  
No Object-X or RH conclusion.
