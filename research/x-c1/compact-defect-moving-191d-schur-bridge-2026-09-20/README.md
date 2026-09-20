# Uniform 191D compact-defect Schur bridge

2026-09-20. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anchor: `5557d94`.

The independent moving physical high-tail floor `q>=1/41` now gives a
complete defect high-block contraction on every `B<=a<=1`:

    ||R_a restricted to T(high)||^2 <= 943/945.

The high subspace has codimension 191 per parity. Consequently the 192nd
singular value in each parity is below `999/1000`; the joint 383rd singular
value has the same bound. All critical singular directions lie over a
finite low space, with their full high response retained.

The remaining exact matrix is

    S = I - alpha - beta* (I-K)^(-1) beta,   0<=K<=943/945.

The physical moving-191D core Schur form equals `G^(1/2) S G^(1/2)`.
This proves an exact coordinate relationship, not equality of Legendre
low vectors and singular vectors. The full high-response Neumann tail
has a rational uniform bound. A conditional finite-matrix certificate
for the largest singular value is specified.

On the fixed horizon, each ordered singular value is continuous and
nondecreasing with the endpoint, including activation of channel 7.
No quantitative endpoint step or profile-renewal law is inferred.

**Open:** actual finite Schur-entry enclosures and their positive sign on
new windows, hence full contraction, a positive C1 closure, Moving-191D
Low/Profile renewal, larger-horizon compatibility, Objekt X and RH.
There is no new positive window and no negative actual Weil source.

Reproduce with Python 3, standard library only:

    python check_bridge.py --verify

The new ledger passes 67 checks. It binds 24 immutable input files, replays the candidate's 53 checks,
the high-tail frozen 25-check math-only mode and its 26-check full-provenance
mode, and checks the new rational bounds and block algebra. `--write`
regenerates the ledger and manifest. Verification requires byte-identical
JSON/log and seven matching payload hashes. The small rational model
matrices check algebra only and are not physical 191D matrix data.

See `PROOF.md` for completed domains, all infinite tails, the exact
congruence, endpoint dependence and the remaining finite obligation.
