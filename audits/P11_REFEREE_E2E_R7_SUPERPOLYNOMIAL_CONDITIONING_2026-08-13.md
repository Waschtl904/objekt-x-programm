# P11 End-to-End Referee Audit R7 — Superpolynomial odd conditioning

**Date:** 2026-08-13  
**Repository:** `Waschtl904/objekt-x-programm`  
**Branch:** `main`  
**Paper under review:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`

## Referee mode

The corollary on superpolynomial odd conditioning is checked from the paper's own preceding statements. Earlier audit nodes are not imported as proof.

## Executive verdict

- **[R7-A] ✓[M]** — the claimed superpolynomial growth of the odd relative condition number is mathematically correct.
- **[R7-B] ✓[M]** — the fourth-root quantity `chi = kappa^{1/4}` is likewise superpolynomial.
- **[R7-C] ✓[M]_part** — as an end-to-end paper claim, the current presentation is incomplete: the corollary is stated without the finite-codimension/high-jet comparison argument that is actually needed.

**Overall R7 status:** **PAPER REPAIR REQUIRED — statement retained; missing proof bridge must be inserted.**

---

## 1. The dangerous non-implication

Immediately before the corollary, the paper records for a fixed nonzero smooth odd vector `f` with first nonzero jet `m=m(f)` the Rayleigh asymptotic

\[
\rho_{T_0,U}(f)
:=\frac{\langle G_{R,U}f,f\rangle}
        {\langle G_{R,T_0}f,f\rangle}
\sim C_{T_0,f}\frac{e^U}{U^{2m+2}}.
\]

This alone does **not** imply a large condition number. A single Rayleigh quotient can grow while all Rayleigh quotients grow at the same rate.

To prove

\[
U^{-N}\kappa(A_{T_0,U}^{R,-})\to\infty
\qquad\forall N>0,
\]

one needs Rayleigh quotients on two directions whose first-jet orders can be separated arbitrarily far.

---

## 2. Existence of arbitrarily delayed smooth odd first jets

Let

\[
\mathcal D_R^-:=C_c^\infty((-R,R))_{\rm odd}.
\]

This is an infinite-dimensional complex vector space. For every integer `M>=1`, the conditions

\[
\beta_R^{(0)}(g)=\cdots=\beta_R^{(M-1)}(g)=0
\]

are only finitely many linear equations on `\mathcal D_R^-`. Therefore

\[
\mathcal N_M
:=\mathcal D_R^-\cap\bigcap_{j=0}^{M-1}\ker\beta_R^{(j)}
\]

is nonzero (indeed infinite-dimensional). Choose `0 != g_M in \mathcal N_M`.

The paper's jet-completeness theorem and its finite-first-jet corollary imply that `g_M` has some finite first nonzero jet

\[
n_M:=m(g_M)\ge M.
\]

Thus smooth odd vectors with arbitrarily delayed first nonzero jet exist.

This finite-codimension step is the missing bridge in the current paper text.

---

## 3. Rayleigh-quotient comparison

Choose once and for all a smooth odd `f_0` with

\[
\beta_R^{(0)}(f_0)\ne0,
\]

so `m(f_0)=0`. Such a vector is obtained, for example, from a nonnegative smooth bump on `(0,R)` and its odd reflection.

The sharp odd asymptotic gives

\[
\rho_{T_0,U}(f_0)
\sim C_0\frac{e^U}{U^2},
\]

whereas for `g_M`,

\[
\rho_{T_0,U}(g_M)
\sim C_M\frac{e^U}{U^{2n_M+2}}.
\]

Let

\[
A_U:=A_{T_0,U}^{R,-}
=(G_{R,T_0}^-)^{-1/2}G_{R,U}^-(G_{R,T_0}^-)^{-1/2}.
\]

For `x_f=(G_{R,T_0}^-)^{1/2}f`, the quotient `rho_{T_0,U}(f)` is exactly the Rayleigh quotient of `A_U` at `x_f`:

\[
\rho_{T_0,U}(f)
=\frac{\langle A_Ux_f,x_f\rangle}{\|x_f\|^2}.
\]

For a positive boundedly invertible operator,

\[
\kappa(A_U)
=\frac{\sup\sigma(A_U)}{\inf\sigma(A_U)}
\ge
\frac{\rho_{T_0,U}(f_0)}{\rho_{T_0,U}(g_M)}.
\]

Hence

\[
\boxed{
\kappa(A_U)
\ge c_M U^{2n_M}(1+o(1))
\ge c_M U^{2M}(1+o(1)).
}
\]

The constant `c_M>0` may depend on the chosen pair but not on `U`.

Given any prescribed `N>0`, choose an integer `M>N/2`. Then

\[
U^{-N}\kappa(A_U)
\ge c_M U^{2M-N}(1+o(1))
\longrightarrow\infty.
\]

Therefore

\[
\boxed{
\forall N>0:\qquad
U^{-N}\kappa(A_{T_0,U}^{R,-})\to\infty.
}
\]

So the first claim of the corollary is valid.

---

## 4. Fourth-root conditioning parameter

The paper defines

\[
\chi_{T_0,U}^{R,-}:=\kappa(A_{T_0,U}^{R,-})^{1/4}.
\]

For any `N>0`, apply the already proved condition-number statement with exponent `4N`:

\[
U^{-4N}\kappa(A_U)\to\infty.
\]

Taking fourth roots gives

\[
\boxed{
U^{-N}\chi_{T_0,U}^{R,-}
=\bigl(U^{-4N}\kappa(A_U)\bigr)^{1/4}
\to\infty.
}
\]

Thus the second claim is also valid.

---

## 5. Paper repair required

The current manuscript states the superpolynomial-conditioning corollary immediately after a single fixed-vector Rayleigh asymptotic and supplies no proof environment for the corollary.

For self-containment the paper should insert the argument of Sections 2--4 above, or an equivalent concise proof containing all three indispensable ingredients:

1. existence, for every `M`, of a nonzero smooth odd vector annihilating the first `M` jets;
2. finite first nonzero jet of that vector by jet completeness;
3. comparison of two Rayleigh quotients to bound the condition number from below.

Without these steps, the displayed conclusion is not a formal consequence of the immediately preceding one-vector asymptotic.

---

## 6. Firewalls

This audit does **not** show any uniform finite-jet Gram or square-root control. The high-jet test vector may depend on `M`; no uniformity in `M` is claimed or needed for superpolynomial growth.

It also does not imply failure of strong terminal transport. A badly conditioned family can still have normalized transports with cancellations. In particular R7 does not close any of

\[
?[O]_{\text{uniform finite-jet Gram/square-root control}},
\qquad
?[O]_{K_{R,S}^{T,U}\to I},
\qquad
?[O]_{W_{R,S,-}^{[T]}\ \mathrm{strong\ Cauchy}}.
\]

---

## Final referee disposition

\[
\boxed{
[R7]\quad \checkmark[M]_{\rm part}
}
\]

The **mathematical statement is retained**, but the present paper is not yet end-to-end self-contained at this corollary. A short high-jet/Rayleigh comparison proof must be inserted.
