# P11 End-to-End Referee Audit R1 — Reconciliation

**Date:** 2026-08-13  
**Original audit:** `audits/P11_REFEREE_E2E_R1_SHARP_ODD_ASYMPTOTIC_2026-08-13.md`  
**Theorem:** `thm:odd`, sharp fixed-vector odd Schur asymptotic

## Repair chain

### R1-A — full-rest factorization

Closed by the R10 structural paper repair

`cdca16d0119dca0b91f27f5dc2daee7e81c73dcb`.

The paper now derives the `psi_{p,a}` coordinates of `R_R f` and proves

\[
\widetilde R_R^*\widetilde R_R=R_R^*R_R.
\]

Status: `✓[M]`.

### R1-B — sesquilinear proof typing

Repaired in

`37e92a926f7b44f8fcd8c8adf4e43a1917569017`.

Equations (6.8), (6.15), and (6.16) now use the complex conjugates required by the convention that the Hilbert-space scalar product is linear in the first argument. In particular,

\[
\langle h_T^{\rm grow},e\rangle
=\int_0^T k_T(t)\overline{b_T(t)}\,dt,
\]

and the anchored signed-edge identity is typed consistently. All norm and absolute-value estimates are unchanged.

Status: `✓[M]`.

### R1-C — explicit Hilbert-valued source representer

Repaired in

`952ca337b609b8f52cc8e3f36d8fa627212e9efb`.

Step 5 now defines explicitly

\[
\Phi_T(r)(v)
=C_T^-(r,v)-C_T^-(r,2r-v)
\]

and records the exact pairing

\[
\langle\Phi_T(r),b\rangle_{L^2(0,T)}
=\int C_T^-(r,t)\overline{\bigl(b(t)-b(2r-t)\bigr)}\,dt.
\]

For

\[
C_T^-(r,t)=2k_T^0(t)\alpha(2r-t),
\]

the paper now computes

\[
\partial_r\Phi_T(r)(v)
=4k_T^0(v)\alpha'(2r-v)
-4(k_T^0)'(2r-v)\alpha(v).
\]

Thus the prime-cell quadrature is applied to the source representer, whose Hilbert-space Lipschitz norm is controlled by the already established bounds on `k_T` and `k_T'`; no operator-norm Lipschitz assertion for the raw reflection operator is used.

Status: `✓[M]`.

## Build verification

GitHub Actions run `31715165575` on paper commit `952ca337b609b8f52cc8e3f36d8fa627212e9efb` completed successfully:

- two `pdflatex` passes;
- unresolved-reference/citation rejection passed;
- multiply-defined-label rejection passed.

The temporary insertion helper used during the connector fallback was removed in commit

`4263da48a92173f240fa264829dfa2b39e3b3984`.

## Final referee verdict

The three mandatory proof-completion items from R1 are now closed. No counterexample, wrong exponent, wrong coefficient, or remaining paper-internal proof gap was found in the audited chain

\[
\text{boundary jets}
\to d_T=2T+O(1)
\to\text{signed mean-zero certificate}
\to\text{prime-cell quadrature}
\to\text{full-rest lift}
\to\text{dual squeeze}.
\]

Therefore

\[
\boxed{[\mathrm{P11\text{-}R1\text{-}T6.1}]\;\checkmark[M].}
\]

**R1: PASS — REFEREE HOLD CLOSED.**

The conclusion remains strictly fixed-vector and smooth-odd. The `o(1)` is not uniform on the odd unit sphere and gives no strong control of `G_{R,T}^{-1/2}` on `T`-dependent vectors.

Accordingly the following remain open and untouched:

\[
?[O]_{\rm uniform\ finite\text{-}jet\ Gram/square\text{-}root\ control},
\qquad
?[O]_{K_{R,S}^{T,U}\to I},
\qquad
?[O]_{W_{R,S,-}^{[T]}\ \mathrm{strong\ Cauchy}},
\]

together with the polar-gauge problem and the wider global Object-X obligations.

No SYN, Seal, Object-X closure, or RH conclusion follows from R1.
