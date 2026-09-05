# P11/R32 — SALVAGE-A1/A2 Uniform Blind Wedge Review Packet

**Date:** 1 September 2026  
**Branch:** \`research/sw1-m1-nd-salvage-phase-diagram\`  
**Status:** candidate only; no promotion.

## Claim

Let

\[
\varepsilon_c=\frac{T-10\Delta}{8}.
\]

Review whether

\[
0<\varepsilon<\varepsilon_c,\qquad
0<R<\varepsilon,\qquad
0<\sigma<R
\]

implies

\[
\ker\mathscr N_R\ne\{0\}.
\]

Primary proof:
\`audits/P11_R32_SW1_M1_ND_SALVAGE_A1_A2_UNIFORM_BLIND_WEDGE_CANDIDATE.md\`

Exact certificate:
\`scripts/certify_sw1_m1_nd_salvage_a1_a2_uniform_blind_wedge.py\`

---

## Gate A — uniform sign and chamber control

Verify independently:

\[
h=\frac{T-10\Delta}{4}=d-3\Delta>0,
\qquad
\varepsilon_c=\frac h2,
\]

and

\[
\boxed{\varepsilon_c<\Delta/2.}
\]

The certificate reduces these signs to exact integer comparisons
\(2^m\) versus \(3^n\).

For every affine-in-\(\varepsilon\) comparison, check that endpoint signs at
\(\varepsilon=0\) and \(\varepsilon=\varepsilon_c\) suffice to determine the
sign on the open interval and that endpoint zeros are handled correctly.

**Verdict:** GREEN / PARTIAL / FAIL

---

## Gate B — graph-invariant Horizon complement

The 24 forbidden gaps are

\[
F_{s,k,j}
=
(s+k\Delta+jh+\varepsilon,\,
s+k\Delta+(j+1)h-\varepsilon)
\]

for \(s\in\{0,a\}\), \(k=0,\ldots,5\), \(j=0,1\).

Check:

1. all 24 gaps are nonempty, ordered, disjoint and lie in \((0,T)\);
2. \(U_\varepsilon^{\max}\) avoids them;
3. the loop over all 24 gaps and every A7 domain component is exhaustive;
4. each nonempty image is covered by \(F_\varepsilon\);
5. the reported count 70 is only a checksum, not the reason for exhaustivity;
6. the verified inverse graphing relations imply
   \(K_\varepsilon=F_\varepsilon^c\) is invariant a.e.;
7. boundary points form only a finite null set;
8. the saturation is measurable as a countable union of partial-Borel word
   images, and the word-saturation of the boundary null set remains null.

Relevant upstream:
- \`audits/P11_R32_SW1_A7_FINITE_STATE_COCYCLE_CANDIDATE.md\`
- \`scripts/certify_sw1_m1_nd_img4_gateB_pmp_graphing.py\`

**Verdict:** GREEN / PARTIAL / FAIL

---

## Gate C — 14-gap Hub exclusion

Check the 14 intervals

\[
B_{\varepsilon,c}=(c+\varepsilon,c+h-\varepsilon)
\]

for

\[
\mathcal C=
\{
0,\Delta,2\Delta,3\Delta,
d,d+\Delta,d+2\Delta,
a,a+\Delta,a+2\Delta,a+3\Delta,
b,b+\Delta,b+2\Delta
\}.
\]

Verify:

1. they are nonempty, ordered, disjoint and lie in \((\varepsilon,T)\);
2. the complement \(K_\varepsilon\) has exactly 25 cells;
3. for every cell and each \(\tau\in\{a,b,T\}\), the code includes:
   - the left piece of \(|x-\tau|\),
   - the right piece of \(|x-\tau|\),
   - the full \(x+\tau\) piece;
4. these are exactly the six physical positive Hub source maps;
5. all 153 nonempty pieces avoid all 14 blind intervals;
6. 153 is again only a checksum after exhaustive looping.

Verify also

\[
|B_\varepsilon|
=
14(h-2\varepsilon)
=
\frac72(T-10\Delta-8\varepsilon)>0.
\]

**Verdict:** GREEN / PARTIAL / FAIL

---

## Gate D — parameter-uniform analytic handoff

Use

\`audits/P11_R32_SW1_M1_ND_SALVAGE_A1_A2_ANALYTIC_HANDOFF_CANDIDATE.md\`.

Check that the proof uses only parameter-uniform statements:

\[
\mathscr T_B=V^*(I+A)V,\qquad
\mathscr T_B\ge I,
\]

the reducing projection for any A7-saturated measurable set,

\[
\mathcal H_R=V^*HW,
\]

and the IMG2/KNF characterization of \(\mathscr B_K\).

Confirm explicitly that no 780 bound, Mass Transport, \(\pm14\) separator
cover or special \(\varepsilon=\Delta/4\) value is imported.

**Verdict:** GREEN / PARTIAL / FAIL

---

## Promotion criterion

Only if A–D are GREEN may the wedge be considered for

\[
\checkmark[M]_{\rm neg}.
\]

No claim that \(\varepsilon_c\) is the exact global phase transition.  
No injectivity claim for \(\varepsilon\ge\varepsilon_c\).  
No Object-X or RH conclusion.
