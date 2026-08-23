# P12 Runde 22 — adversarial review packet: restricted tail for all \(R>0\)

Please review from the committed raw/operator identities and theorem scopes,
not merely from this summary.

## Claim

For the P12 chamber
\[
2a<T_0<c,\qquad
\sigma=S-T,\qquad
\varepsilon=T_0-T,
\qquad 0<\sigma<\varepsilon<\varepsilon_{\max},
\]
review

\[
\boxed{
0<R<T,\qquad \sigma\le R
\Longrightarrow
\ker L_{R,T+\sigma,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

For \(R\ge e/2\), Round 14 already applies.  The new point is that the
Round-19 restricted-tail argument appears valid for **every**
\(0<R<e/2\), with no \(R\ge\rho\) assumption.

## Required independent checks

1. Reconstruct the lower E-equation in the mixed problem for
   \(x\in(R,a)\).  Confirm that \(x>R\ge\sigma\) kills every mixed-tail
   contaminant and that the repaired A14.3a lower-circle kill therefore
   applies for arbitrary \(R>0\).

2. At \(u=T+t\), \(0<t<\varepsilon\), reconstruct
   \[
   p h(a+t)+r h(e+t)+q h(t)=0
   \]
   and verify that the lower-half kill/support gives
   \(h(a+t)=0\).

3. On \(a-\varepsilon<z<a\), reconstruct/check the high-reflection
   identity and verify both possible tail offsets are dead using only
   \[
   R<e/2,\quad \sigma\le R,\quad
   d-\varepsilon_{\max}>e/2.
   \]

4. Verify P1 is unconditional in this chamber:
   \[
   H(t)+l(t)+\frac{2r}{p}H(d-t)=0.
   \]
   For \(0<t<\sigma\), confirm
   \[
   d-t>d-\sigma\ge d-R>d-e/2>e/2>\sigma,
   \]
   hence \(H(d-t)=0\), so \(H(t)=0\).

5. Verify the legal reduction to committed b1 after the tail is killed.

6. Search explicitly for any hidden use of \(R\ge\rho\) in the invoked
   A14.3a/b1/P1 statements.

## Verdict

Return `GREEN`, `PARTIAL`, or `FAIL`.

If GREEN, explicitly confirm:

> The entire restricted-tail sector \(\sigma\le R\) is closed for every
> \(0<R<T\); the lower threshold \(\rho\) is unnecessary in this sector.

No Object-X or RH consequence is under review.
