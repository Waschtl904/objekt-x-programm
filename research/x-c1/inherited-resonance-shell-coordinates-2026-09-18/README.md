# Inherited resonance: shell coordinates

2026-09-18 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

This package starts the separate post-PR-#137 research branch. It does not modify or extend the frozen positive milestone.

It proves two source-space lemmas to the right of

`B = log(5)/2`:

1. **Orthogonal shell lemma.**  The `L2`-orthogonal subspace
   `Z_b = W_b^even intersect E_(B,b)^perp`
   is exactly parameterized by `r in H1_0(B,b)`. Its old-core restriction is one forced mode `alpha(r) cosh(x/2)`, with `alpha = O((b-B)^(3/2))` in derivative scale.

2. **Complete shell-lift lemma.**  The whole even constrained source space has a nonorthogonal but surjective topological decomposition

   `W_b^even = E_(B,b) dotplus L_(B,b) S_(B,b)`,

   where `S_(B,b)={s in H1(B,b): s(b)=0}` and the lift uses two explicit fixed core functions to match the trace and cancel the global Mellin moment. Its core correction is `O((b-B)^(1/2))` in derivative scale.

This repairs the domain gap identified by the consolidation audit: the orthogonal space `Z_b` is a useful test class but is not asserted to be an `H1` complement of the old core.

No new endpoint positivity is claimed. The next gate is the actual lifted-shell block `D_b`, core-shell coupling `C_b`, and the full-core Schur form `A_B-C_b^*D_b^{-1}C_b`.
