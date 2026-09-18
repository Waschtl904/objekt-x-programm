# Provenance note

This package supersedes the initial Node-Schur formula on the same research branch.

External audit identified a normalization error in the final conversion from the high-mode
coordinate `x` to the full even norm: the correct gap is
`(eta-beta_e*K)/(1+beta_e)`, not `eta-beta_e*K/(1+beta_e)`.

The corrected checker, log and JSON are regenerated from that formula. The local
`a` crossing survives, but the upper theta bracket changes to
`0.791428 < theta_* < 0.791429`.

`SHA256SUMS` in the corrected package is generated from the final UTF-8 bytes written in
this correction. The older `49/125` manifest mismatch remains a separate provenance item
unless and until its exact committed raw-byte SHA-256 is independently recomputed.
