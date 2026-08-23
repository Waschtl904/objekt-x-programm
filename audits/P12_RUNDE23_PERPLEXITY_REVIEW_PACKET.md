# P12 Runde 23 — adversarial review packet: exact 42x42 overlap seed below rho

Please review this as a hostile raw-operator referee.

## Target cell

Use
\[
\omega=\tfrac14\log(27/25),\quad
\eta=\tfrac12\log(256/243),\quad
\chi=\tfrac12\log(2187/2048),
\]
\[
\delta=\tfrac12\log(9/8),\quad
\kappa=\tfrac12\log(32/27).
\]

Assume
\[
0<R<x<\sigma<\varepsilon<\varepsilon_{\max}
\]
and

\[
\omega<R,\quad
\eta<x<\chi,
\]
\[
R+x<\delta<\sigma+x<\kappa,
\]
\[
\sigma-x<\eta,\qquad
\kappa<\varepsilon+x,\qquad
x+\eta<\varepsilon.
\]

A concrete interior point is
\[
(R,x,\sigma,\varepsilon)=(0.020,0.030,0.040,0.060).
\]

## Sources

In coordinates \(u=sx+me+n\delta\), independently reconstruct the rows for

Negative sheet:
```
(-1,0,1) (-1,0,2)
(-1,1,0) (-1,1,1) (-1,1,2) (-1,1,3)
(-1,2,0) (-1,2,1) (-1,2,2) (-1,2,3) (-1,2,4)
(-1,3,0) (-1,3,1) (-1,3,2) (-1,3,3) (-1,3,4)
(-1,4,0) (-1,4,1) (-1,4,2) (-1,4,3)
(-1,5,1)
```

Positive sheet:
```
(1,0,0) (1,0,1)
(1,1,-1) (1,1,0) (1,1,1) (1,1,2)
(1,2,-1) (1,2,0) (1,2,1) (1,2,2) (1,2,3)
(1,3,-1) (1,3,0) (1,3,1) (1,3,2) (1,3,3)
(1,4,-1) (1,4,0) (1,4,1) (1,4,2)
(1,5,0)
```

Canonical operator:
\[
Lh(u)=p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)].
\]

Do not trust a reduced table.  Check:

1. all 42 source positions are horizon-legal throughout the stated cell;
2. all six arguments at every source;
3. every odd-reflection sign;
4. every lower/upper support deletion;
5. that the live set has exactly 42 coordinates and gives a fixed
   \(42\times42\) matrix throughout the cell.

## Determinant

Independently reproduce
\[
\det M_{42}=-p^{14}r^4 F_-F_+.
\]

Normalize
\[
\beta=q/p,\qquad v=(r/p)^2.
\]

Check that \(F_\pm=p^{12}(A\pm C)\), where

\[
\begin{aligned}
A={}&3\beta^{12}-\beta^{10}v-18\beta^{10}
-7\beta^8v+45\beta^8\\
&-\beta^6v^3-3\beta^6v^2+38\beta^6v-60\beta^6\\
&-\beta^4v^3+21\beta^4v^2-62\beta^4v+45\beta^4\\
&+8\beta^2v^3-33\beta^2v^2+43\beta^2v-18\beta^2\\
&+2v^4-9v^3+15v^2-11v+3,
\end{aligned}
\]
\[
C=2\beta^3v^2(\beta^2-1)(2\beta^2+v-2).
\]

For the actual weights,
\[
\beta=2^{-3/4},\qquad
v=\frac{\log3}{\log2}\sqrt{8/27}.
\]

Verify by your own exact/high-precision method that both \(A-C\) and
\(A+C\) are strictly negative and safely away from zero.

## Verdict

Return `GREEN`, `PARTIAL`, or `FAIL` for the local statement

\[
(C23)\Longrightarrow h(x)=0.
\]

Do **not** promote a full \(R\ge\omega\) descent from this one cell.
No Object-X or RH consequence is under review.
