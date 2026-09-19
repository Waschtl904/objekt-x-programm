# Odd continuation and local all-parity positivity

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

For B=log(5)/2 and **0<h=b-B<=10^-20**, an independent odd proof gives

```text
Q_W[u] > 10^-12 ||u||^2                 for every actual odd source
Q_W[u] > 3*10^-15 ||u||^2               for every actual source
R_o >= (1/(2*10^12)) I
Theta_o < 1 - 2*10^-12
```

The all-parity statement combines the new odd theorem with the reproduced
even theorem at `7741eca...`, using exact reflection invariance and
orthogonal parity projections. Exactly the two original Mellin conditions
are preserved. The odd operator uses full odd core plus profile coordinates;
it is not identified with an even gauge operator.

The odd corrector is explicitly constructed and normalized by its exact
sinh moment. The full odd form-domain isomorphism and actual H1 gluing
are proved. A 31-dimensional low block (degrees 3,5,...,63) retains the
complete infinite coretail (degrees 65,67,...) and the entire shell profile.
All mixed blocks and physical norm losses are paid. The coupling is <4;
all 31 directed rational comparison LDL pivots are positive.

From the repository root with standard-library Python 3:

```text
python research/x-c1/odd-profile-continuation-2026-09-19/check_odd.py --verify
```

Verification makes 51 new exact checks, binds 81 input files, reproduces the full even certificate
and its inherited chain, independently recomputes the odd matrices and
complete infinite Gram, compares the new JSON and log byte for byte, and
checks seven payload hashes. The independent even replay and odd matrix
calculation run concurrently in separate local processes. No new source
selection is performed. Preserve repository blob bytes when checking out
inputs; automatic newline conversion changes their hashes.

`--write` regenerates the JSON, log and SHA256SUMS. Analytic domain and
infinite-dimensional assertions are proved in PROOF.md, not inferred from
finite matrix tests. No quadrature, numerical-eigenvalue proof, finite
shell surrogate, A1 or additional Mellin condition. Reproduction is not
an independent external audit.

Larger or iterable windows, historical Strong Terminal, Connected
Unit-Window Coercivity, full C1-GEOM, Object X and RH remain open.
Append-only research publication, with a separate append-only transport
ladder update. No main change, PR or merge.
