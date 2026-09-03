# P11 R43 multi-model review reconciliation — head \`7647bc25...\`

Date: 2026-09-03

## Provenance

User-supplied multi-model synthesis explicitly evaluating R43 mathematical head
\[
\texttt{7647bc257f72e9f42e5be367292f20ced2136171}.
\]

This is useful adversarial review input but is **not** booked as formal
\`independent GREEN\`: it aggregates multiple model assessments and is not one documented
fresh blind exact-head referee run under the registry definition.

## Consensus retained

The synthesis confirms the following R43 structures:

- the C6a coordinate family in R43.54 is a genuine ONB, so Parseval is exact;
- the compact-resolvent jet-number construction is correct as a **sufficient mechanism**:
  a uniform \(N_S\)-form-energy bound implies B-TIGHT;
- any coercive weight \(\rho_n\to\infty\) gives the same compactness mechanism;
- the local \(m\)-growth estimate R43.10cq1a--cq1d is mathematically consistent but does
  not control the C6a orbit coefficients;
- the fixed scalar-model formulation of the GC-AC contradiction removes the formal
  model-switch objection;
- no terminal regularity may be inferred merely from the finite-terminal floor/cutoff
  formulas.

## New review warning: global B-JCOND may be structurally wrong

One reviewer observes that the raw higher-jet kernels are monomial/Hankel-like and warns that
a dimension-uniform Riesz lower bound may fail exponentially.

Rather than book this as a theorem, the branch now contains a direct numerical test of the
**normalized constrained-Gamma Riesz family**:

- script:
  \`audits/P11_R43_JET_GRAM_CONDITIONING_DIAGNOSTIC_2026-09-03.py\`;
- report:
  \`audits/P11_R43_JET_GRAM_CONDITIONING_DIAGNOSTIC_2026-09-03.md\`.

At \(S=1\), \(P=120\),
\[
\sigma_{\min}(m=4,8,12,16)
\approx
2.77\cdot10^{-3},
2.41\cdot10^{-6},
2.32\cdot10^{-9},
2.24\cdot10^{-12},
\]
after every constrained Riesz vector has individually been normalized.

The decay is stable across \(S=0.5,1,2,4\), Galerkin dimensions \(40\) through \(120\),
and Fourier cutoffs \(540\) through \(4860\).

Booking:
\[
\boxed{
\text{strong numerical evidence against global uniform higher-jet Riesz conditioning;}
}
\]
\[
\boxed{
\text{not a theorem and not a B-TIGHT/Strong-Terminal no-go.}
}
\]

The primary B-TIGHT route is therefore reprioritized to direct compact-resolvent energy
control of the actual orbit \(h_U\).

## Commutator/Gronwall firewall

The review suggests differentiating
\[
\mathcal E(U)=\langle N_Sh_U,h_U\rangle
\]
and using a commutator/Gronwall estimate.

The current P11 stack does not yet contain the prerequisite terminal generator:

- no booked operator derivative \(dG_{X,U}/dU\);
- no booked derivative \(dW_U/dU\);
- no booked generator \(\mathcal A_U\) with
  \(\partial_UW_U=\mathcal A_UW_U\).

R40/R41 provide a \(U^{-1}\) dual-normal scale, not a terminal derivative estimate.
Therefore a commutator identity is presently formal.  A positive route must first prove a
generator/differentiability theorem or work directly with finite increments.

## B-SIGN: finite-increment replacement

The branch no longer makes Darboux the preferred B-SIGN route.

A sufficient no-regularity condition is: there exist
\(\Delta,\eta>0\) such that, for all sufficiently large nearby terminals,
\[
|b_V-b_U|\le2-\eta
\qquad(|V-U|\le\Delta).
\]
Under B-TIGHT, \(|b_U|\to1\), so two opposite signs would force a difference arbitrarily
close to \(2\), contradicting the strict gap.  Chain connectivity of the real terminal tail
then yields eventual sign coherence.

The orbit-level condition
\[
\|w_V-w_U\|\le2-\eta
\]
is stronger but intrinsic, and eventual positive two-terminal correlation
\[
\liminf_{T,U\to\infty}L_{R,S}^{T,U}>0
\]
is another sufficient B-SIGN route after B-TIGHT.

## Current research order

\[
\boxed{
\text{GC-AC candidate-closed}
\to
\textbf{direct B-TIGHT orbit energy}
\to
\textbf{B-SIGN/B-ORIENT}.
}
\]

Global higher-jet Riesz conditioning is now a secondary/diagnostic route only.
No freeze, formal independent-GREEN, \(\checkmark[M]\), Strong-Terminal, Object-X, or RH
promotion follows.
