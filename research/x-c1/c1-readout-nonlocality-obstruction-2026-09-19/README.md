# C1 readout nonlocality and channel-Gram obstruction

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.
Anchor: `617ffe2a3bfe12bef768b536b9eeffbbfb21f1da`.

This package excludes two concrete C1 candidate classes on the actual
original two-Mellin source spaces:

* An exact positive Gram readout cannot have physical propagation R<a,
  even after adding any nonlocal correction of finite rank. The full
  Gamma mixed pairing between separated admissible source blocks has
  arbitrary rank, while such a candidate's mixed Gram rank is bounded.
* An individual signed Prime contribution cannot be a positive Gram
  component. Every strictly active channel has both signs in each parity,
  with every other Prime contribution isolated away.

For a pure finite-propagation readout with R<73/200, a fixed even/odd
pair inside the already positive B=log(5)/2 core forces relative physical
L2 representation error >10^-11. This quantitative bound is not claimed
after adding a nonlocal finite-rank correction; that larger class has
the separate exact rank obstruction.

`PROOF.md` gives the universal arguments and exact sources. The checker
rebuilds 84 exact checks, a rational rank-three example and twenty isolated
Prime/parity/sign witnesses, binds six analytic provenance files, and
verifies the JSON/log and seven payload hashes:

```text
python -B research/x-c1/c1-readout-nonlocality-obstruction-2026-09-19/check_nonlocal.py --verify
```

Only the standard library is required. No old matrix chain is rerun:
these new arithmetic witnesses are independent of its numerical data.
Infinite-rank and continuum assertions are proved analytically, not by
finite sampling. Arithmetic reproduction is not an independent audit.

General nonlocal or abstract-target C1 readouts remain open. Indefinite
Prime observables inside a common positive mediator are not excluded.
The existing complete nonlocal hard forms in 31D/191D transport proofs
are unaffected. There is no negative full Weil source and no new
transport window, C1 mediator or Object X. The width comparison is
clarified: 200 over b1c0186; 200 million over ca3849a.
