# P11 R43 multi-model review synthesis reconciliation — B-TIGHT front

Date: 2026-09-03

## Provenance

User-supplied multi-model review synthesis received after the R43 GC-AC / \(b_U\) hardening.

This document records useful mathematical/reviewer input only.  It is **not** booked as a
formal \`independent GREEN\` verdict because the synthesis combines multiple prior model
assessments and does not provide one fresh blind exact-head review with the full provenance
required by the registry.

## High-confidence review conclusions

The synthesis agrees that:

1. the explicit singular-support repair in Section 3K.5 is mathematically correct;
2. the exact identity
   \[
   L_{R,S}^{T,U}
   =
   b_Tb_U+\operatorname{Re}\langle h_T,h_U\rangle
   \]
   and the B-TIGHT reduction are correct;
3. opposite asymptotic signs force the maximal orbit separation \(2\);
4. the Clark/boundary-parameter firewall is necessary;
5. B-TIGHT is now the primary mathematical front;
6. fixed-\(m\) holomorphy alone cannot justify a weighted jet moment uniformly in the jet
   order.

The synthesis also recommends one presentation hardening for the GC-AC contradiction:
density, scalar representatives, the measure decomposition, and
\(d\gamma_m=|G_m|^2d\nu_S\) should all be read in one fixed scalar
\(L^2((0,S),d\nu_S)\) model.  This has been incorporated in mathematical-content head
\`6614895dcddb55c24c473f98a55be831f590f56b\`.

## Resolution of the coordinate-structure question

The synthesis asks whether the coefficients used in B-TIGHT are ONB coefficients,
Riesz-basis coefficients, or merely analysis coefficients of a total family.

For the actual R43 definitions this question is already settled by canonical C6a:

\[
e_{S,0}=\varepsilon_S,
\qquad
\{e_{S,n}:n\ge1\}
\text{ is an orthonormal basis of }H_S^0.
\]

Therefore
\[
c_{n,U}
=
\langle W_Ue_{R,0},e_{S,n}\rangle
\]
are genuine ONB coefficients and
\[
1-b_U^2
=
\sum_{n\ge1}|c_{n,U}|^2
\]
is exact Parseval.

This family must not be confused with the Section-3K higher-jet Gamma-Riesz family
\(\{g_{m,S}\}\), whose totality is used for GC-AC but for which no Riesz-basis statement is
booked.

## Canonical compact-resolvent formulation

The C6a ONB canonically defines the positive selfadjoint jet-number operator
\[
N_Se_{S,n}=ne_{S,n}.
\]
It has compact resolvent.

Thus B-JMOM is exactly
\[
\sup_U
\|(I+N_S)^{1/2}h_U\|^2<\infty.
\]

More generally, any coercive weight \(\rho_n\uparrow\infty\) defines
\[
N_{S,\rho}e_{S,n}=\rho_ne_{S,n}
\]
with compact resolvent, and
\[
\sup_U
\langle(I+N_{S,\rho})h_U,h_U\rangle<\infty
\]
implies B-TIGHT because the orbit is then relatively compact while already converging
weakly to zero.

Hence a polynomial moment is only one sufficient route; no particular growth law is
mathematically privileged.

## Fixed-m holomorphy firewall

The Section-3K estimates
\[
\|\partial_Q^k b_{m,Q}\|
\le C_{m,k,Q_0}
\]
have the quantifier structure
\[
\forall m\;\exists C_{m,k,Q_0}<\infty.
\]

They provide no summability or coercive weight control as \(m\to\infty\).  Moreover they
refer to the higher-jet Riesz data rather than directly to the C6a ONB coefficients
\(c_{n,U}\).

Therefore no implication from fixed-\(m\) holomorphy to B-JMOM is currently booked.  A
positive route would require either:

- a quantitative controlled change-of-basis/triangular estimate from higher-jet Riesz data
  to the C6a ONB; or
- a direct uniform bound for a compact-resolvent energy of \(h_U\).

## B-SIGN regularity

Full continuity is stronger than necessary.  Under B-TIGHT one eventually has
\(|b_U|>1/2\).  On the connected real terminal tail, the Darboux/intermediate-value property
already prevents a sign change without a zero.

Thus
\[
\text{B-TIGHT + eventual Darboux property}
\Longrightarrow
\text{B-SIGN}
\Longrightarrow
\text{Strong Terminal}.
\]

Continuity or real analyticity are sufficient special cases.  None is currently proved for
the concrete terminal coefficient; arithmetic cutoff/floor changes in the finite-adic
terminal formulas mean regularity must be established rather than assumed.

## Current decision

The operative order remains
\[
\boxed{
\text{GC-AC candidate-closed}
\longrightarrow
\textbf{B-TIGHT}
\longrightarrow
\textbf{B-SIGN/B-ORIENT}.
}
\]

The next research target is **uniform compactness of the normal remainder \(h_U\)** in fixed
C6a coordinates.

No freeze, formal independent-GREEN promotion, \(\checkmark[M]\), Strong-Terminal, Object-X,
or RH conclusion follows from this synthesis.
