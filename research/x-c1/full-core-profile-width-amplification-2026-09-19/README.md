# Full even width amplification through h=10^-20

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

On B=log(5)/2 and **0<h=b-B<=10^-20**, this package proves for every
actual even H1_0 source with exactly the original two Mellin conditions:

```text
Q_W[u] > 3*10^-15 ||u||^2
Theta_A < 1 - 9*10^-23
Theta_0 < 1 - 2*10^-29
R_A, R_0 >= (3*10^-15 / 140000000) I
```

The old tail floor 0.719448628450052179... is bound to its original
commit, reference norm and exact moment map. The complete core/profile
coupling is <4, using disjoint sampled prime-power intervals, the
Carleman bound and a bounded exact moment correction. A 31-dimensional
low block retains its full infinite coretail Gram; the whole shell and
all low/high/profile mixed blocks are paid. All 31 rational LDL pivots
are positive. Physical norm conversion costs a proved factor 6.

The proof also specifies the complete energy near/low/high decomposition
and bounds its entire Gram operator, not merely its diagonal blocks.
The two gauges, actual Schur operators and the explicitly dominated
comparison form remain distinguished. The existing tiny-window theorem
and its sharper relative margins are preserved.

Run from the repository root with standard-library Python 3:

```text
python research/x-c1/full-core-profile-width-amplification-2026-09-19/check_width.py --verify
```

`--write` regenerates the JSON, log and SHA256SUMS. Verification binds
73 inputs, makes 41 new exact checks, replays the transition and inherited shell proof chain, fully
recomputes the relevant even core matrices, requires byte-identical new
outputs, and checks seven payload hashes. Preserve Git blob bytes when
checking out inputs; newline conversion changes their hashes.

No numerical-eigenvalue proof, quadrature, finite shell surrogate,
additional moment, A1, source reselection or physical renormalization.
Odd continuation and larger windows remain open. Reproduction is not
an independent external audit. Append-only research branch publication;
no main change, PR or merge.

The concurrent high-tail commit `7d269c7...` and its eight files are
preserved unchanged. This package closes the low/mixed full-operator
obligation that it leaves open.
