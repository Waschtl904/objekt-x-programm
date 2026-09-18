# Active-set segment Schur theorem

2026-09-18 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

This package isolates the prime-label-independent certificate theorem implicit in the current connected C1 program.

Main point: for any finite active set of prime-power shifts with arbitrary `0<d<2`, including overlapping shift bands, the complete low/tail Gram of

`V - K_gamma - sum_q w_q T_dq`

is given by exact band-intersection polynomial integrals plus the already analytic logarithmic moments. No new operator architecture is needed when `4`, `5`, `7`, ... enter.

If one endpoint `B` satisfies the stated infinite-dimensional Schur/LDL conditions, exact zero extension transfers the same gap to every `0<a<=B`.

The theorem is a sufficient-condition/certificate architecture. It does **not** claim positivity at `log(5)/2` or beyond the currently certified endpoint `log(2)`.

`check_active_set_gram.py` is an algebra-regression checker for the generic shift-band formulas across both `d<1` and `d>1`. The analytic operator proof is in `PROOF.md`.
