# X-C1 Node-Schur Waxing Function — corrected normalization

Append-only research package for PR #137.

Status: `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

The corrected full even gap is
`G_even=(eta-beta_e*K)/(1+beta_e)`.
The earlier committed formula omitted the division of the `eta` term by `1+beta_e`.

After correction the rigorous local crossing survives:
`0.3930108 < a_node_corr < 0.3930110`.

At the upper endpoint the unique theta maximizer is enclosed by
`0.791428 < theta_* < 0.791429`.
The odd gap remains `>1/4`.

This remains a local crossing of the continuation from the proved `a=0.392` gate;
no global monotonicity of `G_node(a)` is claimed.

Unused positive resources remain the nonconstant Gamma residual and Prime-2 difference energy.
The next research gate is `FULL-RESIDUAL-SCHUR`.
