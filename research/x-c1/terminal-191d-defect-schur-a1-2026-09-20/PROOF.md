# Terminal 191D defect-Schur diagnostic

2026-09-20. **DIAGNOSTIC / NO STATUS PROMOTION**.

Mathematical frontier: `79988874cceeb01f17e0cda67485838c0b7c4f63`.
Operative gate: `TERMINAL-191D-DEFECT-SCHUR-A1`.

This package constructs a high-precision diagnostic for the actual Even/Odd
terminal calculation. It does not claim positivity of the exact terminal
Schur matrices.

## Backend identity

At `a=1` the current nonpole Weil symbol is
\[
w(\xi)=\operatorname{Re}\psi(1/4+i\xi/2)-\log\pi
-2\sum_{q\in\{2,3,4,5,7\}}\Lambda(q)q^{-1/2}\cos(\xi\log q).
\]
The frozen Legendre backend uses `r=w-0.1` on `[-1551,1551]`; hence its
bounded lower multiplier is exactly `0.1+r=w` there. We reuse the code and
hash-fixed matrix artifacts, not the historical A1 positivity conclusion.

Frozen logical matrix SHA256:
- even: `97b761e9f89517303f557d3c18061cc1b232c821e5804fcf9071298e17e60183`;
- odd: `6cff5e4710f0f23c4b43503e5b398525898e0a034e61c25791526ad94f17e295`.

## Exact dyadic moment-neutral coordinates

The artifact satisfies
\[
\mathcal S_p=10^{38}2^{480}(A_p^{dyad}-1.005\,10^{-35}I),
\qquad
A_p^{dyad}=L_{0,p}^{dyad}+2a_pa_p^*.
\]
Let the integer moment vector be `M` with `a=2^-160 M`. For `j>=1` set
\[
y_j=M_0e_j-M_je_0.
\]
Then `M^T y_j=0` exactly. With `tau=1005*2^480`,
\[
Q_{ij}^{int}=y_i^T\mathcal S_p y_j+\tau\,y_i^Ty_j
\]
is, up to one common positive scale, the exact dyadic bounded-lower form on
the moment-neutral coordinates. No floating moment cancellation is used.

Coordinates are degrees `2,4,...,2148` (even) or `3,5,...,2149` (odd).
The first 191 are the canonical moving Low coordinates; the remaining 883
form the finite Legendre High block.

## Diagnostic Schur matrix

Write
\[
Q_p^{int}=\begin{pmatrix}A_p&B_p^T\\B_p&H_p\end{pmatrix},
\quad \dim A_p=191,\quad\dim H_p=883.
\]
The script embeds the exact integer blocks in Arb, solves `H_p X_p=B_p` with
rigorous ball arithmetic, and forms
\[
S_{p,diag}=A_p-B_p^TX_p.
\]
It records Arb eigenvalue enclosures and a SHA256 of the full 191 by 191
interval matrix. A zero-containing eigenvalue ball is `UNDECIDED_DIAGNOSTIC`.

This is not yet the exact terminal `S_1^p`.

## Hardening gaps

Before theorem promotion, directed bounds must pay:
1. exact physical moments versus the dyadic moments;
2. exact bounded multiplier versus the quadrature/evaluation/dyadic model;
3. the Legendre tail beyond degree 2149 and the omitted positive
   high-frequency contribution through a rigorous Schur/shorting comparison.

No diagnostic sign is a theorem about the exact Weil form.

## Firewall

This package does not claim exact terminal positivity, `||R_1||<=1`,
positivity through `a=1`, a positive C1 closure, unrestricted-horizon
compatibility, Objekt X, global Weil positivity, or RH.
