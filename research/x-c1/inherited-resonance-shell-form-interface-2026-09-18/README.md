# Inherited resonance: shell form interface

2026-09-18 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

This package is the second gate on the separate shell-Schur research branch. It uses the already proved complete nonorthogonal lift

`W_b^even = J_(B,b) W_B^even dotplus L_(B,b) S_(B,b)`

and closes the **form-domain interface** without claiming a new positive endpoint.

Main points:

- the lifted shell block is exactly `D_b(s,t)=Q_b(Ls,Lt)`;
- its positive shift is the common-jump Gram
  `D_b + Gamma_b <Ls,Lt> = <X_b Ls, X_b Lt>`;
- the induced common-jump graph norm gives a canonical closed shell-energy completion;
- uniformly for `B<b<=1`, `D_b[s] >= -12 ||Ls||^2`;
- strict shell positivity is equivalent to a restricted common-jump frame bound;
- a new **inverse-free relative form-Schur theorem** shows that an all-source continuation follows from a shell gap plus
  `|C_b(w,s)|^2 <= theta A_B[w] D_b[s]` with `theta<1`.

The inverse-free formulation avoids introducing an unjustified bounded operator `D_b^{-1}` and also avoids any reuse of the invalid `L^2`-orthogonal `H^1` decomposition found during the PR #137 audit.

No positivity to the right of `B=log(5)/2` is claimed. The next gate is the strict shell frame bound `D_b >= delta_sh ||Ls||^2`.
