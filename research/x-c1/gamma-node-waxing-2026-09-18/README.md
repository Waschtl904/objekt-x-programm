# Gamma-plus-Node waxing: optimize s, theta, and z

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.** New append-only method-class
certificate on PR #137, following `5de865932827d45aa119fa0e1b74eaab635624c8`.
The accepted point certificates remain unchanged. No merge.

For the full three-parameter Gamma-plus-Node estimate:

- There is exactly one crossing on the certified interval:
  **0.3931224 < a_Gamma-node < 0.3931226**.
- The global parameter maximizer is unique throughout that interval.
- A compact admissible box encloses all three optimizing parameters.
- 297 adaptive interval boxes exhaust the split search, using value and
  derivative signs. This is not a point-grid maximum.
- The local envelope derivative lies between **-5.216461935993** and
  **-5.212359791482**. No global-first-crossing claim is made.
- Odd gap remains **> 1/4**.

[PROOF.md](PROOF.md) defines the functions on the Prime-2-only domain,
including the correct piecewise Node floor; proves compactness,
uniqueness, infinite-tail control, and endpoint signs; and retains the
division of the whole moment-subtracted numerator by **1 + beta_even**.
This envelope uses Gamma and Node energy only. The earlier joint
Prime-2 certificate is a separate stronger estimate and remains valid.

Run from this directory, or use the script's full path:

```text
python check_gamma_node_waxing.py --verify
```

The standard-library checker reproduces **19 named rational checks**,
the complete adaptive covers, and the saved JSON/log, then verifies all
five SHA-256 entries. All arithmetic and displayed endpoints are
integer/Fraction based; there are no floats, quadrature, finite
differences, or imported decimal transcendental bounds.

`--write` regenerates JSON and log. A default run is read-only. The six
files are proof, checker, log, JSON, README, and SHA256SUMS. The manifest
covers the five payloads, excluding itself. Verify repository LF bytes
without checkout line-ending conversion.
