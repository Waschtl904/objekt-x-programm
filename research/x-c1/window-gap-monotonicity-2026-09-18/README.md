# Window-gap monotonicity and inherited near-null resonance

2026-09-18 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

This package records a direct variational consequence of the exact zero-extension identity already proved on PR #137:

- the optimal connected NULLPOL Rayleigh infimum is nonincreasing as the window grows;
- the explicit even near-null source at `B=log(5)/2` extends with **exactly the same** Rayleigh quotient to every larger window;
- therefore a rising rescaled/full-window test branch is not the global minimizing branch;
- the correct local problem to the right of `B` is a shell/domain-expansion Schur problem: can newly available directions push the inherited resonance lower?

No new endpoint positivity claim is made. In particular this package does not certify `log(7)/2` or `a=1`.

The concurrent GPT-2 transported-family package at `9d9c48de...` studies a different full-window continuation. This theorem explains why that rising test branch cannot be identified with the global lowest-even Rayleigh infimum.
