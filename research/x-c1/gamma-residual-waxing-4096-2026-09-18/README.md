# Gamma-residual waxing 4096 — 2026-09-18

Status: `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

This append-only X-C1 package continues the live PR #137 Gamma-Node waxing work with a sharper dyadic Gamma-residual energy enclosure and a sharper infinite-dimensional degree bound. It is based on head `c87dbcb37c250bd6f420d1688f275ae2a4e7f5ab` and explicitly checks the current-head global Node-floor branch on its full bracket.

Main result:

- at `a=0.3934355`, the full connected NULLPOL form is certified by
  `Q_W[u] > (1/1500000)||u||_2^2`;
- at `a=0.3934360`, the optimized **named certificate class** is globally negative for every admissible `(s,theta)`, even after replacing the exact Gamma `e_2` energy by its 4096-cell upper Riemann enclosure;
- therefore the certificate has a local sign-change bracket
  `0.3934355 < a_Gamma,4096^cert < 0.3934360`.

The upper endpoint is not a Weil no-go and does not exhaust the actual Gamma residual operator. The Prime-2 difference residual remains unused and C15 remains unnecessary at the positive endpoint.

Files:

- `X_C1_GAMMA_RESIDUAL_WAXING_4096.md` — proof note and scope;
- `generate_gamma_residual_waxing_4096_intervals.py` — 70-decimal interval input generator;
- `check_x_c1_gamma_residual_waxing_4096.py` — exact Fraction gate checker;
- `gamma_residual_waxing_4096_checks.log` — actual checker stdout;
- `gamma_residual_waxing_4096_results.json` — machine-readable result;
- `SHA256SUMS` — SHA-256 hashes of the five content/certificate files plus the interval generator.

No A1 import. No third Mellin condition. No finite matrix in place of the infinite-dimensional operator. No numerical quadrature as proof. No merge or registry change.
