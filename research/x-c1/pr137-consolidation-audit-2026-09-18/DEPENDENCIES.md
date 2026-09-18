# Imported identities and what replay does not certify

Frozen target: `fc597f6129db57787c85ec20627ed608233187ba`.
All referenced historical files are byte-bound in frozen_inputs.json.

## I0. Explicit Weil normalization and pole elimination

`audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md` §§1-9 fixes
Q_W(v,w)=W(v*tilde(w)), K_t=tau_(t/2)-tau_(-t/2),
h(t)=exp(-t/2)/(1-exp(-2t)), w_q=Lambda(q)/sqrt(q), and
kappa=log(8*pi)+gamma+pi/2. Its full identity is
\[
Q_W(v,w)=\langle Ev,P Ew\rangle+
\int_0^\infty h(t)\langle K_tv,K_tw\rangle dt+
\sum_{q\ {
m active}}w_q\langle K_{\log q}v,K_{\log q}w\rangle
-\left(\kappa+2\sum_{q\ {
m active}}w_q\right)\langle v,w\rangle.
\]
The rank-two pole pairing vanishes on the two Mellin kernels. This is
the project's analytic starting identity, not a positivity assumption.
Its Git blob `8463e84058630c09687cc5b98681b357b1b2a805` is identical
at the frozen target and the older cited anchor
`ac164bbbd2c46623aa64e567d21f813f41f164b0`.

That audit cites a literature normalization and a global RH equivalence.
This consolidation does not independently verify those literature
imports or import the RH equivalence as a needed step. Its historical
quadrature discussion is diagnostic only and is not proof input to the
seven central checkers.

## I1. Connected edge/leakage identity and source domain

`research/x-c1/connected-3_8-2026-09-17/X_C1_CONNECTED_MOMENT_FACTORIZATION.md`
§1, equations C1-C2, supplies the physical connected edge bookkeeping.
Its Git blob is `fb8e6e568f2719fd02a957aedece34de75c4825c`, the same
at corrected historical anchor `9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb`
and at the frozen target. Extension to arbitrary finite prime-power
sets is set out in universal-prime-power-family-2026-09-18 §§2,4.

The analytic identity is distinct from that older package's numerical
3/8 certificate. No old scalar 3/8, 0.392 or Node-crossing reserve is
used as a numerical premise of P234. The old package and the adjacent
storage/sparse/three-cell notes remain provenance, not a new external
audit of all their claims.

## I2. Common-space recombination and form domain

Prime2 interval PROOF.md §§2-3 and universal family §§1-2 give the
unitary U_a u(xi)=sqrt(2a)u(a xi), harmonic Legendre diagonal D_H,
V=-log(1-xi^2)/2 and q_0=-log(2*pi*a)-gamma. The common form domain
is the harmonic diagonal form domain intersected with L2(V dmu),
with bounded regular-Gamma and finite partial-shift perturbations.
The harmonic diagonalization, closed-form identification and domain
claims are analytic proof obligations for independent review. Rational
matrix replay alone cannot establish them.

## I3. Exact shifts, weights and threshold behavior

Universal family §§2-6 and active-set theorem §§2-4 retain every
ordered mixed prime-power term. Prime powers use log(p)/p^(k/2),
not log(p^k)/p^(k/2). At d=2 the partial shift is zero a.e., but its
operator norm is 1 for 1<=d<2. Operator-norm continuity at entry is
therefore unavailable. The complete Parseval tail and logarithmic
cross moments are analytic identities; finite regression identities
support implementation, not a universal proof by finite enumeration.

## I4. Full endpoint certificate, moments and norm conversion

Prime-power-segment-4 PROOF.md §§2-10 specifies the sufficient
conditions: polynomial Gamma remainder, complete coupling Gram,
positive infinite tail, bounded error from the omitted Mellin tail,
actual infinite-dimensional Schur pivot, actual inverse shear and
final source-norm division. check_segment.py recomputes its numbers
from rational/one-sided enclosures, including the source coefficients.
The same architecture with separate parameters is used in P2/P23.
No quadrature, numerical-eigenvalue sign decision, A1, or third Mellin
condition is needed by these certificates.

## I5. Window functoriality and variational consequence

Physical zero extension preserves H1_0, both moments and Q_W. This
follows on the original real-line source and is then expressed in
reference coordinates. Universal family §5 and prime2 interval's
window section give the formula; monotonicity §§1-4 applies the
infimum over nested sets. No assertion of L2 completeness of H1_0
is required for these statements. No shell block is required either.

## Review boundary

Fresh execution verifies the executed arithmetic, saved outputs and
specified byte bindings. It is author-side reproducibility, not an
independent proof audit. Audit priorities are I0/I1's identification
with the intended Weil form, I2's form-domain claims, and I4's full
tail/error/shear/norm argument. A positive review of a different
historical commit cannot be transferred automatically to these claims.
