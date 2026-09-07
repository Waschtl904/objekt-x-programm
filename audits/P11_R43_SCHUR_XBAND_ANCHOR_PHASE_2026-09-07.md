# R43 — Anchor and complex-phase supplement

**Date:** 2026-09-07. **Status:** Draft. Companion to `P11_R43_SCHUR_XBAND_COMM_2026-09-07.md`.
All inherited data, proxy limitations and no-promotion firewalls remain in force.

During this implementation the user supplied a second computation reporting an
anchor-dependent interference sign, a repaired complex normalization, and a local
head `fe907714045f35a955b8807dec4a3118224b3f13`. That local head and its claimed
independent review are **not** adopted as certification of this stack. The full
external patch was not retrieved. The supplied numerical claims were instead
recomputed here with a separate implementation. No statement that GitHub was
unchanged in that other session describes this session: this session had already
created the new branch and two commits before receiving the summary.

The supplement `P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.py` uses a second graph
construction (edge incidence matrices) and Cholesky inverses. It hash-checks the
main test's blob `61e700872e0637dbc34145bf7039f0cac3f0b3f3`. It passes **724 distinct
checks**, maximum scaled residual `4.427824871413e-14` (the second Q construction).
This is a second implementation/self-check, not an independent reviewer.

```sh
OPENBLAS_NUM_THREADS=1 python audits/P11_R43_SCHUR_XBAND_ANCHOR_PHASE_2026-09-07.py \
  --output r43-anchor-results.json
```

## 1 Both anchors and an endpoint-symmetric decomposition

For one pair let `u_j=u_i-h` and keep the oriented physical difference
`d=x(u_j)-x(u_i)`. Denote evaluation at u_i by R_i. The first anchor gives

```math
a_i=R_i B(T_h-I)v,\qquad c_i=R_i[T_h,B]v.
```

The second anchor, reoriented to the SAME d, gives

```math
a_j=-R_j B(T_{-h}-I)v,\qquad c_j=-R_j[T_{-h},B]v.
```

Both satisfy `d=a_i+c_i=a_j+c_j`. The minus signs align the physical orientation;
changing the sign of both amplitudes does not cause an interference sign change.
The measured change arises from a different splitting at a different anchor.

For Q and X=8, all pairs and both strips, normalized by the same G:

| split | A2/G | C2/G | interference/G | Vinter/G |
| --- | ---: | ---: | ---: | ---: |
| smaller-center anchor | .0608407529510 | .0002800364946 | -.0048491377096 | .0562716517360 |
| larger-center anchor | .0516331478329 | .0003111639238 | +.0043273399793 | .0562716517360 |
| endpoint-symmetric | .0561054020170 | .0001640518343 | +.0000021978847 | .0562716517360 |

The supplied two-anchor values are reproduced to their quoted precision.
Define the symmetric amplitudes and the anchor discrepancy by

```math
a_s=(a_i+a_j)/2,\quad c_s=(c_i+c_j)/2,\quad g=(a_i-a_j)/2.
```

Then `a_i=a_s+g`, `c_i=c_s-g`, `a_j=a_s-g`, `c_j=c_s+g`, and `d=a_s+c_s`.
Swapping pair endpoints reverses both symmetric amplitudes, so their energies
and interference are invariant under that swap. No invariance under every
possible operator/gauge/model choice is asserted.

For the weighted direct sum over pairs, the parallelogram identity yields

```math
\frac{\|a_i\|^2+\|a_j\|^2}{2}=\|a_s\|^2+\|g\|^2,
\qquad
\frac{\|c_i\|^2+\|c_j\|^2}{2}=\|c_s\|^2+\|g\|^2,
```

and, crucially,

```math
\boxed{\frac{I_i+I_j}{2}=2\Re\langle a_s,c_s\rangle-2\|g\|^2.}
```

Proof: substitute `a_s +/- g` and `c_s -/+ g`; the linear cross terms cancel
when the two interferences are averaged. This holds over complex Hilbert spaces.
Thus even an average of the two signed interferences has a built-in negative
anchor-discrepancy term. It is not the symmetric interference. Here
`||g||^2/G=.000131548374913`: the average interference is negative although the
endpoint-symmetric interference is slightly positive.

This is a local exact identity (`✓[M]_local`). The listed signs and constants
are numerical (`✓[M]_proxy`). Negative interference in one chosen splitting is
not a demonstrated canonical suppression mechanism.

## 2 Exact anchor-change identity, including the compression defect

Since `R_j=R_i T_h` for the active pair,

```math
\begin{aligned}
a_i-a_j
&=R_i\{B(T_h-I)+T_hB(T_{-h}-I)\}v\\
&=R_i\{[T_h,B](T_{-h}-I)+B(T_hT_{-h}-I)\}v.
\end{aligned}
```

The second equality follows by distributing the commutator. It is matrix-exact
on the entire finite old-window space, not only on the source family. The
supplement tests it before applying sources and verifies that dropping the last
term changes the full observation matrix. On the tested compact bulk hub-source
spaces the compression-defect term vanishes, and is separately checked there.
This does not license dropping it for arbitrary boundary data.

## 3 Complex-conjugation controls

The main script already uses `np.vdot`; no missing-conjugate defect was found in
its real calculations. The new suite explicitly enforces the complex definitions
`G=x^* A x`, squared norms `sum |x_k|^2`, and
`I=2 Re sum conjugate(a_k)c_k` throughout its own calculations.

For each transport it tests three real bump sources, three genuinely complex odd
sources, and one arbitrary complex old-grid vector. Each is checked against six
scalar factors: four nontrivial/unit phases including i and exp(i pi/4), the
identity, and a non-unit factor `2 exp(.73i)`. Normalized energies are invariant;
unnormalized graph energy scales by the squared modulus. Direct complex ANOVA,
both anchor sums, the symmetric split, global L2 normalization, and complex
polarization identities are checked. These phase tests cover the center graph,
not an unimplemented complex extension of the #84 off-grid sampler.

A deliberate wrong normalization `Re(x^T A x)` is rejected: for a nonzero real x,
replacing x by ix changes it to `-G`, whereas the correct Hermitian energy stays G.
This control would detect the kind of missing-conjugation error described in the
user-supplied external summary.

## 4 Entire odd source subspace, now for both anchors and the symmetric split

The supplement repeats the source-Gram generalized eigenvalue test for all
three decompositions. For Q and the seven-dimensional X=8 odd source space:

| split | epsilon_sup | min V/A2 | max V/A2 |
| --- | ---: | ---: | ---: |
| smaller-center anchor | .115752887351 | .823160815299 | .998838198267 |
| larger-center anchor | .195568269415 | 1.020884890957 | 1.353578375623 |
| endpoint-symmetric | .092070941521 | .936047713997 | 1.141533967353 |

These remain numerical spectral evaluations, not interval certificates. In
particular the finite comparison shows no near-complete cancellation in the
endpoint-symmetric split, not merely in one selected bump. A provisional test
hypothesis `epsilon_sup<.3` for every transport AND both anchors failed at BT,
X=8, larger-center anchor, where `epsilon_sup=.349990100439`. That stronger
hypothesis is not adopted; the output logs the actual values instead. This does
not invalidate any matrix identity or the reported first-anchor bounds.

