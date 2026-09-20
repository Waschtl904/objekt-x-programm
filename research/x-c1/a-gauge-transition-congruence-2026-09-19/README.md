# Quantitative A-gauge transition and exact congruence

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

On the full original interval 0<h=b-log(5)/2<=10^-20, this append-only
package supplies the explicit transition between the two REDUCED
coordinate spaces and its actual inverse:

```text
T_A(w,z)     = (w-ell_A(w) psi, z+ell_A(w)e)
T_A^-1(f,z)  = (f-k(f) psi, z+k(f)e),  k(f)=<f,psi>/||psi||^2
```

- Uniform physical product conditioning:
  ||x||^2/3 <= ||T_A x||^2 <= 3111^2 ||x||^2.
- Exact closed form-domain, joint H1 trace and block congruence.
- Exact Schur congruence R_0[w]=R_A[P_A w], without assuming invariance
  of associated operator domains.
- The fixed source's full A-gauge directional quotient is <7.55e-6,
  extracted from the existing complete residual certificate.
- An explicit sufficient criterion for the entire energy-orthogonal
  complement, with all mixed terms, is stated conditionally.

The supplied review used the older d145ba88 state. The preserved A-gauge
theorem at 4ab3341 and tiny-window all-core theorem at 04bc246 are already
closed author-side. The full h<=10^-20 all-core gate remains UNDECIDED;
the existing even all-source theorem covers only h<=2^(-10^16). Odd
continuation remains open. This package does not enlarge that width.

From the repository root, using standard-library Python 3:

```text
python research/x-c1/a-gauge-transition-congruence-2026-09-19/check_transition.py --verify
```

`--write` regenerates the JSON, log and SHA256SUMS. Verification makes
38 new exact checks, binds
65 inherited files, replays the preceding 40-check package and its
31/28/43/9 prerequisite checks, and compares the new outputs and seven
payload hashes. Preserve repository blob bytes when checking out inputs;
LF-to-CRLF conversion causes hash failures.

No new source, physical normalization or Riesz solve; no finite shell
replacement, quadrature, numerical eigenvalue proof, third Mellin
condition or A1. Reproduction is not an independent external audit.
No new PR, merge or main change.
