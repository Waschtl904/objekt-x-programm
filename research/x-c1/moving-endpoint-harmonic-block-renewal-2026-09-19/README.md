# Finite-band moving-endpoint harmonic block renewal

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.
Anchor: `b1c01860fef2a960cae57634041f75b29d37f836`.

For B=log(5)/2, all original two-Mellin H1 sources supported in (-b,b),
0<b<=B+10^-10, satisfy Q_W[u]>2*10^-15||u||^2. The odd bound is
>10^-12. The added width is 200 times the preceding outer window.

For every a in [B,B+10^-10], the actual form admits a uniform harmonic
decomposition with 31 soft coordinates per parity and a complete growing
hard space containing the infinite core tail and all accumulated profiles.
Its reference hard floor is >2/5, physical hard floor >1/15, low/hard
coupling norm <3, and full harmonic-coordinate squared norm bounds are
1/162 and 486. Nested form projections give an exact endpoint cocycle
and a total energy budget for the fixed inherited near-null direction.

This is finite-band renewal. It does not reset the accumulated profile,
certify a new band beyond B+10^-10, or prove non-summable transport,
the 7-channel threshold, a unit window, Object X or RH.

Read `PROOF.md` for the sharpened Gamma profile floor, complete operators,
domains, actual Riesz lifts and scope. `STATUS_DE.md` gives a German status.
`moving_results.json` and `moving_checks.log` are exact reproducible ledgers.

From the repository root:

```text
python -B research/x-c1/moving-endpoint-harmonic-block-renewal-2026-09-19/check_moving.py --verify
```

Only the Python standard library is needed. The checker binds 111 input
files, reproduces b1c0186 and its entire chain, reconstructs both full-tail
Grams and all low/profile vectors, checks 62 new rational positive pivots,
passes 80 new exact checks, and verifies byte-identical results and seven
payload hashes. There is no
quadrature, numerical eigenvalue sign test, or finite shell substitution.
Infinite form-projection identities are proved analytically; they are not
claimed to have been numerically constructed. Reproduction is not audit.
