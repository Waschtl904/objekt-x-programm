# Entire reduced-core logarithmic shell gate

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

For B=log(5)/2 and **0<h<=2^(-10^16)**, b=B+h, this package proves
on the entire reduced closed core form domain:

- Theta_0(b)<1-2*10^-13;
- R_0>=(331/500)*10^-13 I;
- Q_W[u]>10^-17 ||u||^2 for every nonzero actual even H1_0 two-Mellin source.

The width is an exact positive rational written in compressed power
notation. It is vastly smaller than 10^-20. **The entire-core gate on
the full previous interval 0<h<=10^-20 remains UNDECIDED.** Odd
continuation and larger windows remain open.

The proof eliminates the shared trace response exactly for every reduced
core vector. A quantitative L2 Carleman bound includes the entire core
and all four arithmetic channels; the shell floor grows as log(2/h).
Together these give a full operator inequality, retaining all mixed
terms. The fixed near-null source and its complete energy-orthogonal
complement are also treated explicitly, without selecting a new source.
The preserved concurrent A-gauge theorem supplies complete coordinates
with Theta_A<=169/500 on this same small interval, improving the physical
gap from the original L2-gauge's >10^-30 bound to >10^-17. Theta_A and
Theta_0 are distinct operators; the original Theta_0 bound above is retained.

From the repository root, with standard-library Python 3:

```text
python research/x-c1/all-core-logarithmic-shell-gate-2026-09-19/check_all_core.py --verify
```

`--write` regenerates the package JSON, log and SHA256SUMS. `--verify`
replays 31 parent direction checks, 28 coordinate checks and 43 shell
checks, and 9 A-gauge checks, validates all 57 bound inputs, then reproduces the new outputs
and all seven payload hashes. Inputs must retain their repository blob
bytes; a checkout that converts LF to CRLF will fail the hash checks.
The checker never constructs 2^(10^16) or uses floating-point underflow.

`PROOF.md` contains the analytic infinite-dimensional proof and exact
remaining obligation. `STATUS_DE.md` gives the German result summary.
Rational checks are not an independent external audit. No quadrature,
numerical eigenvalue proof, finite shell replacement, third Mellin
condition, or A1. Append-only on the existing research branch; no new PR,
merge, main change or Registry promotion.
