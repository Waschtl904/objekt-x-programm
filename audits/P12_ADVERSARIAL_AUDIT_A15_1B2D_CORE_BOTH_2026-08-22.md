# P12 adversarial audit — Runde 14 full b2d closure

**Date:** 2026-08-22  
**Repo base:** `Waschtl904/objekt-x-programm`, `main`, parent `14890e2127cffe6798db4deb62cfcb3929deeab5`  
**Scope:** P12 A15.1b2d core-both and propagation to full b2d  
**Firewall:** P11 FROZEN; R14 unchanged

## Status

- `✓[M]` full b2d core-both local kill.
- `✓[M]` full A15.1b2d injectivity for
  \[
  e/2\le R<d/2,\qquad T<S<T_0<c.
  \]
- `?[O]` remains only for the mixed strip with `0<R<e/2`.
- No polar-gauge, terminal-transport, Object-X, or RH implication is claimed.

## Core-both geometry

For
\[
e/2\le R<d/2,\qquad
R<\sigma<\varepsilon<\varepsilon_{\max},\qquad
\sigma>d/2,
\]
the genuine core-both interval is
\[
I_{\rm both}=\bigl(\max\{R,d-\sigma\},\min\{\sigma,d-R\}\bigr).
\]
For `x∈I_both`, set `y=d-x` and `κ=e-δ`. Then `x,y∈(R,σ)`, and the interval is invariant under `x↦d-x`.

Uniform support bounds used in the reduction:
\[
0<e-x,e-y,x-\delta,y-\delta,2\delta-x<R,
\]
and
\[
y+\delta>\sigma,\qquad x+\kappa>\sigma.
\]
The elementary constants checks are
\[
e>2\delta\iff256>243,
\]
\[
\varepsilon_{\max}<e\iff15<16,
\]
\[
\varepsilon_{\max}<2\delta\iff80<81,
\]
\[
\varepsilon_{\max}-\delta<e/2\iff100<108.
\]

## Thirteen horizon-legal sources

\[
\begin{aligned}
u_1&=d-x,&u_2&=2d-x,&u_3&=b-x,&u_4&=3d-x,\\
u_5&=T-x,&u_6&=T+\delta-x,&u_7&=T+d-x,\\
u_8&=e+x,&u_9&=a+x,&u_{10}&=3e+x,\\
u_{11}&=b-\delta+x,&u_{12}&=T-\delta+x,&u_{13}&=T+x.
\end{aligned}
\]
All are in `(0,T0)`. The only three above `T` are `T+y`, `T+(x-δ)`, `T+x`, all `<T+σ<T0`.

Direct reduction of the canonical operator gives:
\[
\begin{aligned}
Q_1:\;&-p h(e+x)-p h(b-x)-r h(a+x)-r h(T+\delta-x)-q l(y)-qH(y)=0,\\
Q_2:\;&-p h(T+\delta-x)-r h(e+x)-q h(2e+x)=0,\\
Q_3:\;&p h(y)-pH(y)-r h(x)-q h(e+x)=0,\\
Q_4:\;&p h(y+\delta)-q h(x+\kappa)=0,\\
Q_5:\;&p h(a-x)-q h(x)=0,\\
Q_6:\;&p h(2d-x)+r h(y)=0,\\
Q_7:\;&p h(b-x)+r h(a-x)+q h(y)=0,\\
Q_8:\;&-p h(y)-p l(y)-r h(2d-x)-rH(x)-q h(b-x)=0,\\
Q_9:\;&p h(x)-pH(x)-r h(y)-q h(a-x)=0,\\
Q_{10}:\;&p h(x+\kappa)-q h(y+\delta)=0,\\
Q_{11}:\;&p h(e+x)-q h(y)=0,\\
Q_{12}:\;&p h(2e+x)+r h(x+\kappa)=0,\\
Q_{13}:\;&p h(a+x)+r h(e+x)+q h(x)=0.
\end{aligned}
\]

## Triangular elimination

Let `Δ=p²-q²`. From `Q4,Q10`, `h(y+δ)=h(x+κ)=0`. Then successively:
\[
h(2e+x)=0,
\]
\[
h(e+x)=\frac qp h(y),\qquad h(T+\delta-x)=-\frac{rq}{p^2}h(y),
\]
\[
h(2d-x)=-\frac rp h(y),\qquad h(a-x)=\frac qp h(x),
\]
\[
h(a+x)=-\frac qp h(x)-\frac{rq}{p^2}h(y),
\]
\[
h(b-x)=-\frac{rq}{p^2}h(x)-\frac qp h(y),
\]
\[
H(y)=\frac{\Delta}{p^2}h(y)-\frac rp h(x),\qquad
H(x)=\frac{\Delta}{p^2}h(x)-\frac rp h(y).
\]
From `Q8`,
\[
l(y)=-\frac{r(p^2-2q^2)}{p^3}h(x)-\frac{\Delta-2r^2}{p^2}h(y).
\]
Finally `Q1` becomes
\[
\frac{2qr(2p^2-q^2)}{p^3}h(x)=0.
\]
Since `p,q,r>0` and `2p²-q²>0`, `h(x)=0`. The involution gives `h(y)=0`, then `H(x)=H(y)=l(x)=l(y)=0`.

## Exact row certificate

With `Δ=p²-q²`, the polynomial row multiplier
\[
\begin{aligned}
\widetilde C=(&p^3\Delta,-p^2r\Delta,-p^2q\Delta,pq^2r^2,-r\Delta(p^2-2q^2),\\
&-pqr\Delta,p\Delta^2,-p^2q\Delta,pqr\Delta,p^2qr^2,\\
&p\Delta(\Delta-2r^2),-pqr\Delta,p^2r\Delta)
\end{aligned}
\]
satisfies identisch
\[
\sum_{j=1}^{13}\widetilde C_jQ_j=2qr\Delta(2p^2-q^2)h(x).
\]

## Propagation to full b2d

If `σ≤d/2`, Runde 11 already gives kernel triviality.

For `σ>d/2`:
- if `d/2<σ≤d-R`, the defect strip is core-single plus core-both;
- if `σ>d-R`, the defect strip is core-both plus b2d-upper.

The existing full core-single and upper kills plus the new core-both theorem give
\[
h=H=l=0\quad\text{on }(R,\sigma).
\]
The E-equation is then homogeneous on `(R,a)`, and b2b Steps 1--5 give `h=0` there.

For `0<t<R`, P2 gives `H(t)=l(t)` because `D(t)=0`. In P1, `z=d-t>d-R>R`; either `z≥σ` and tail support kills `H(z)`, or `R<z<σ` and the already killed defect strip kills it. Hence P1 gives `H(t)+l(t)=0`, so `H(t)=l(t)=0`. The full tail disappears and b1 closes the residual support.

Therefore
\[
\boxed{e/2\le R<d/2,\quad T<S<T_0<c\Longrightarrow\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}.}
\]

## Independent verification record

Before promotion, an independent second reviewer reproduced:
- the triangular closing residual;
- the polynomial row certificate;
- the 20,000-point support/horizon stress over sharp cases B and C;
- all four elementary support inequalities;
- an independently rewritten raw-operator reconstruction from the six canonical slots `u±a,u±b,u±T`.

The raw reconstruction returned:
```text
EXACT_ROW_MATCH Q1: PASS
...
EXACT_ROW_MATCH Q13: PASS
ALL_13_RAW_OPERATOR_ROWS_MATCH_EXACTLY = PASS
```

The unified verifier committed with this audit returns:
```text
TRIANGULAR_Q1_CLOSING = 2*q*r*x*(2*p**2 - q**2)/p**3
ROW_CERTIFICATE_MINUS_TARGET = 0
RANDOM_PATTERN_STRESS = PASS 16658 3342
ALL_13_RAW_OPERATOR_ROWS_MATCH_EXACTLY = PASS
ROUND14_FULL_VERIFY = PASS
```

## Firewall

P11 is unchanged and remains FROZEN.  
R14 is unchanged.  
This is a localized-hub modulus-layer result only.
