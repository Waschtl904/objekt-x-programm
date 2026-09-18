# GPT 2: near-null source and its exact-Mellin transport

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**

This append-only package investigates the explicit even source from
commit `6a16d90b551588572c87e622c21c2df7f7b1adc2`.

- Separate monomial/beta integration reproduces its Rayleigh quotient
  near 3.296290826616e-12 at B=log(5)/2.
- The exact-Mellin, fixed-reference-shape family stays above 10^-12
  throughout B<=a<=C=log(7)/2. This is one specified family, not an
  all-source endpoint theorem at C.
- Its squared normalized overlap with the B-source stays above
  0.9999846820525401 throughout that interval.
- Channel 5 strictly lowers this family's energy for B<a<=C.
- Every mixed 2/3/4 shift term and the complete infinite directional
  tail are recomputed at B, with cutoffs 63,79,95.
- Raising the arithmetic grid from 220 to 300 decimal places and the
  Gamma degree from 112 to 144 narrows both endpoint enclosures.

The full actual energy identity is kept separate from Schur and
moment-map certificate losses; they are not subtracted twice.
The direct source is already exactly admissible.

Run with standard-library Python:

```text
python check_near.py --verify
```

Default execution writes nothing. `--write` explicitly regenerates
the JSON, log and SHA256SUMS. Verification checks byte-identical
recomputation and all five payload hashes. The proof explains the
19-cell energy cover and 25-cell channel-sign cover, 435 exact
Gamma integration identities, and the limits of this source audit.

No quadrature, numerical eigenvalue proof, A1, third Mellin condition,
merge, main edit, or Registry promotion. A full independent external
audit and an all-source positive endpoint at C remain open.
