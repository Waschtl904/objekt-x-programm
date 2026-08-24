# P12 Runde 26 — Promotion nach unabhängiger GREEN-Prüfung

**Status:** A15.1b2k / Round 26 `✓[M]_part`.  
**Review basis:** Round-26 candidate chain ending at `main@3e71024455f078a0045d157594d9861305c4e793`.  
**Input:** A15.1b2j / Round 25, promoted `✓[M]_part`, with independently verified invertible `92×92` raw matrix.  
**Firewall:** P11 FROZEN; R14 unchanged; no Polar Gauge, Terminal Transport, Objekt X or RH claim.

## 1. Independent verdict

Perplexity independently rebuilt the Round-26 core from the canonical raw operator and returned **GREEN**.

Independently confirmed:

1. the enlarged fixed-92 minus chamber `C26-` reconstructs the same `92×92` raw matrix as Round 25;
2. the eight symbolic raw facets are complete: all `C(9,4)` vertex candidates were checked, exactly 20 feasible vertices were found, and all **1628** source/sign/support/horizon raw inequalities were certified at those 20 vertices with rational interval bounds, with **0 violations** and **0 unresolved signs**;
3. the exact `J`-mirror chamber `C26+` carries the same coefficient matrix;
4. the rational overlap box
   `0.014<R<0.016`, `0.0293<x<0.0296`, `0.041<sigma<0.043`, `0.065<epsilon<0.075`
   lies strictly inside both chambers; all 13 overlap inequalities have positive margin.

No new determinant computation is required: throughout both chambers the selected source system reconstructs coefficient-for-coefficient the already promoted and independently GREEN Round-25 matrix `M92`, with `det M92 != 0`.

## 2. Promoted minus chamber

Retain

\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\delta=\eta+\chi,
\]

and

\[
\kappa=e-\delta=2\eta+\chi.
\]

Define `C26-` by

\[
\eta<x<\chi,
\]

\[
\chi<R+x<2\eta,
\qquad
x-R<\eta,
\]

\[
\chi-\eta<\sigma-x,
\qquad
\sigma+x<3\eta,
\]

\[
x+\eta<\varepsilon<\varepsilon_{\max}.
\]

These inequalities imply

\[
0<R<x<\sigma<\varepsilon<\varepsilon_{\max},
\qquad R<\eta<\rho.
\]

For every parameter point in `C26-`, the selected 92 sources reconstruct exactly the promoted Round-25 matrix `M92`. Hence every kernel vector satisfies

\[
\boxed{h(x)=h(\delta-x)=0}.
\]

Status:

\[
\boxed{\mathrm{R26\!-\!A}:\checkmark[M]_{\rm part}.}
\]

## 3. Complete raw-facet certificate

Within the P12 arithmetic chamber, the connected constant-pattern chamber of this fixed minus-92 certificate is controlled by the following eight genuine raw events:

\[
x=\eta,
\qquad x=\chi,
\]

\[
R+x=\chi,
\qquad R+x=2\eta,
\qquad x-R=\eta,
\]

\[
\sigma-x=\chi-\eta,
\qquad \sigma+x=3\eta,
\]

\[
\varepsilon=x+\eta.
\]

The external P12 arithmetic ceiling `epsilon=epsilon_max` remains the ambient chamber boundary, not a newly discovered local raw threshold.

The retained verifier certifies all 1628 raw inequalities over the polyhedral closure using its 20 feasible vertices and rigorous rational enclosures for the logarithmic constants. The independent GREEN review reproduced the same 20 vertices and the same complete no-violation result.

In particular, the Round-25 decimal box boundaries were only convenient inner coordinates; they are not mathematical facets.

## 4. Horizon-wall consequence

The former minus-horizon equation

\[
\varepsilon+x=\kappa
\]

is not a facet of the fixed 92-row certificate. The source whose horizon legality changes there, `(-1,5,1)`, is not among the selected 92 rows. Therefore the same invertible raw certificate passes locally through that horizon wall.

This is a **local certificate statement only**. It does not say that the complete horizon wall is globally closed.

## 5. Exact `J` mirror and open gluing

Under

\[
J(s,m,n)=(-s,m,n+s),
\qquad x\mapsto\delta-x,
\]

`C26-` maps to the plus chamber `C26+`, equivalently described by

\[
\eta<x<\chi,
\]

\[
R+x>\chi,
\qquad
\chi-\eta<x-R<\eta,
\]

\[
\sigma+x>2\chi,
\qquad
\sigma-x<2\eta-\chi,
\]

\[
\varepsilon+x>\kappa,
\qquad
\varepsilon<\varepsilon_{\max}.
\]

The mirrored 92 rows and columns reconstruct coefficient-for-coefficient the same `M92`. Thus

\[
\boxed{h(x)=h(\delta-x)=0}
\]

throughout `C26+` as well.

The open rational box

\[
0.014<R<0.016,
\]

\[
0.0293<x<0.0296,
\]

\[
0.041<\sigma<0.043,
\]

\[
0.065<\varepsilon<0.075
\]

lies strictly in

\[
C_{26}^{-}\cap C_{26}^{+}.
\]

Therefore

\[
\boxed{C_{26}^{-}\cup C_{26}^{+}}
\]

is an open connected local horizon corridor, with no seam gap between its minus and plus certificate sides.

Status:

\[
\boxed{\mathrm{R26\ horizon\ corridor}:\checkmark[M]_{\rm part}.}
\]

## 6. Scope firewall

Round 26 does **not** prove:

- the full residual overlap `0<R<rho`, `sigma>R`;
- full coverage of either entire horizon wall;
- a new global radius threshold;
- significance of `omega`, search depth 21, or any newly appearing decimal value;
- Polar Gauge, Strong/Terminal Transport, Objekt X, or RH.

P11 remains FROZEN and the R14 firewall is unchanged.
