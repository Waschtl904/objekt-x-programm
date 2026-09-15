# NP-PROLATE-1 root-bracket repair

Frozen source under audit: `6b5956e69dfcb8124e8e31083613fd89c5f35fb3`.

The first exact GitHub Actions run reached the rigorous checker in both parity sectors but failed before trace/Ritz evaluation because the diagnostic root brackets of half-width `1e-7` did not contain the true roots. The observed unresolved intervals were immediately outside the first even/odd brackets.

This certificate branch preserves the frozen checker byte-for-byte as:

`scripts/check_np_prolate_1_arb_base.py`

with Git blob:

`b73ab9858cbc19626fb19794ab4ce4a0a7d3dbd8`.

The existing checker path is replaced only by a wrapper which verifies that base blob and sets

`ROOT_EPS = 0.00001`

before executing the unchanged rigorous code. This is a conservative 100x enlargement. The original proof path books every complete root bracket into `root_edge_trace_upper`, so the enlarged uncertainty is not discarded.

No theorem statement, multiplier, Ritz nodes, values of `c` or `U`, tail bound, Gram test, Cholesky test, or final certificate inequality is changed.

Promotion rule: this repair is accepted only if both parity jobs pass and the logs show the verified frozen base blob plus strict final Arb gaps.