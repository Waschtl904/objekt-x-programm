# P11 End-to-End Referee Audit R7 — Superpolynomial odd conditioning

**Date:** 2026-08-13  
**Repository:** `Waschtl904/objekt-x-programm`  
**Branch:** `main`  
**Paper under review:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Included proof module:** `papers/P11_sections/P11_TC1_MixedJet.tex`

## Correction provenance

The initial R7 commit `b81d7cdd2fa6795784bbc123b5ac70af1da2ac17` correctly reconstructed the mathematical argument but incorrectly classified the paper as missing that proof. The error was in the referee scan: the main file states Corollary `cor:conditioning` and immediately afterwards inputs `P11_sections/P11_TC1_MixedJet.tex`; that included file begins with an explicit `Proof of Corollary~\ref{cor:conditioning}` containing the required high-jet/Rayleigh comparison.

Git history preserves the erroneous first disposition. This corrected audit is authoritative.

## Executive verdict

- **[R7-A] ✓[M]** — the superpolynomial growth of the odd relative condition number is correct.
- **[R7-B] ✓[M]** — the fourth-root quantity `chi = kappa^{1/4}` is also superpolynomial.
- **[R7-C] ✓[M]** — the current paper is self-contained at this point: the required proof is present in the immediately included TC1 module.

**Overall R7 status:** **PASS — ✓[M].**

---

## 1. The nontrivial logical point

A single fixed-vector asymptotic

\[
\rho_{T_0,U}(f)
\sim C_{T_0,f}\frac{e^U}{U^{2m(f)+2}}
\]

does not by itself imply a large condition number. One needs fixed odd directions with arbitrarily separated first integral jets and then a comparison of their Rayleigh quotients.

The included proof supplies exactly this argument.

---

## 2. Arbitrarily separated smooth odd jets

On

\[
\mathcal D_R^-:=C_c^\infty((-R,R))_{\rm odd},
\]

the functionals `beta_R^(0),...,beta_R^(M)` are linearly independent. Indeed, on the positive half interval they are represented by the kernels

\[
I_j(r)=\int_0^r s^j e^{-s/2}\,ds.
\]

If

\[
\sum_{j=0}^M a_j I_j(r)=0\qquad(0<r<R),
\]

differentiation gives

\[
e^{-r/2}\sum_{j=0}^M a_j r^j=0,
\]

hence all `a_j=0`. Therefore for every `M>=1` there is a smooth odd `f_M` with

\[
\beta_R^{(0)}(f_M)=\cdots=\beta_R^{(M-1)}(f_M)=0,
\qquad
\beta_R^{(M)}(f_M)\ne0.
\]

Choose also `f_0` with `beta_R^(0)(f_0) != 0`.

Thus the first nonzero jets are exactly `0` and `M` for this pair.

---

## 3. Rayleigh quotient and condition number

For

\[
A_U:=A_{T_0,U}^{R,-}
=G_{R,T_0}^{-1/2}G_{R,U}G_{R,T_0}^{-1/2}
\]

and `x=G_{R,T_0}^{1/2}f`, the paper correctly identifies

\[
\frac{\langle A_Ux,x\rangle}{\|x\|^2}
=\rho_{T_0,U}(f)
:=\frac{\langle G_{R,U}f,f\rangle}
        {\langle G_{R,T_0}f,f\rangle}.
\]

The sharp odd asymptotic gives

\[
\rho_{T_0,U}(f_0)
\sim C_0\frac{e^U}{U^2},
\qquad
\rho_{T_0,U}(f_M)
\sim C_M\frac{e^U}{U^{2M+2}}.
\]

Since `A_U` is positive and boundedly invertible,

\[
\kappa(A_U)
=\frac{\sup\sigma(A_U)}{\inf\sigma(A_U)}
\ge
\frac{\rho_{T_0,U}(f_0)}{\rho_{T_0,U}(f_M)}.
\]

Therefore for each fixed `M`,

\[
\boxed{
\kappa(A_U)\ge c_M U^{2M}
}
\]

for all sufficiently large `U`.

Given `N>0`, choose `M>N/2`; then

\[
U^{-N}\kappa(A_U)\to\infty.
\]

Hence

\[
\boxed{
\forall N>0:\qquad
U^{-N}\kappa(A_{T_0,U}^{R,-})\to\infty.
}
\]

This is exactly the claimed superpolynomial condition-number growth.

---

## 4. Fourth-root parameter

With

\[
\chi_{T_0,U}^{R,-}:=\kappa(A_{T_0,U}^{R,-})^{1/4},
\]

choose `M>2N` in the preceding estimate. Then

\[
\chi_{T_0,U}^{R,-}\ge c_M^{1/4}U^{M/2},
\]

so

\[
\boxed{
\forall N>0:\qquad
U^{-N}\chi_{T_0,U}^{R,-}\to\infty.
}
\]

The paper's second conclusion is therefore correct.

---

## 5. Firewalls

The argument uses a test vector `f_M` depending on the desired polynomial order `M`. It supplies no uniform finite-jet Gram or square-root control and makes no statement about `T`-dependent optimizing vectors beyond the condition-number lower bound.

In particular it does not prove or disprove

\[
K_{R,S}^{T,U}\to I
\]

or strong Cauchy convergence of

\[
W_{R,S,-}^{[T]}.
\]

Those gates remain open.

---

## Final referee disposition

\[
\boxed{[R7]\quad \checkmark[M]}
\]

**PASS.** The theorem is correct and the required proof is already present in the paper through the immediately following `\input{P11_sections/P11_TC1_MixedJet}` module.
