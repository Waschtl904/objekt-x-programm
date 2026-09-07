# P11 / R43 — Hard11 level-0 positive-channel saturation reduction

**Date:** 2026-09-06  
**Status:** exact/local reduction on top of PR #58; hard-channel decay and Strong Terminal remain OPEN  
**Exact parent head:** `0e57cf230291abd16ce88b0ceed95d68036799e5`

## 0. Purpose and firewall

PR #58 isolates exactly two nontrivially hard diagonal sum-sign families in the normal old-to-new block:

\[
(k,\ell)=(1,1),\qquad (k,\ell)=(2,2).
\]

This note attacks only the first family.  It proves that the raw primewise divergence of the `(1,1)` numerator is not the right obstruction after saturation: the whole hard11 family is the unique non-good old-to-new component of one **positive martingale level-0 channel**, and the saturated hard11 output is controlled by the corresponding old level-0 residual energy plus a horizon-uniform collar/exponential-tail remainder.

It does **not** prove that this old level-0 residual energy tends to zero on the actual transported structured vector.  Hence it does not close

```text
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY
B-FLAGDYN / B-FLAGTIGHT
Strong Terminal / C6
```

and it has no Object-X or RH consequence.

A second firewall is essential: the R40/R42 future dual normal

\[
v_{X,U}=A_X(U)^{-1/2}r_X
\]

has norm `O(U^{-1})`, but PR #57/#58 uses the resolvent-transported structured vector

\[
x_{U,V}(f)=\mathcal Q_{U,V}H_U^*E_{X,U}f.
\]

No identification between these two vectors is assumed here.

---

## 1. Input: orthogonal martingale-level factorization

Use PR #56 notation.  For every prime `p` and martingale level `a\ge0`,

\[
T_{p,a;V}
:=
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,V}}
\sum_{k\ge a+1}p^{-3k/4}K_{p,k;V}.
\tag{H11.1}
\]

The exact residual normal factorization is

\[
\boxed{
A_V=R_V^*R_V
=\sum_p\sum_{a\ge0}T_{p,a;V}^*T_{p,a;V}.
}
\tag{H11.2}
\]

Define the positive level-0 channel

\[
\boxed{
B_{0,V}:=\sum_pT_{p,0;V}^*T_{p,0;V}.
}
\tag{H11.3}
\]

Then immediately

\[
\boxed{0\preceq B_{0,V}\preceq A_V.}
\tag{H11.4}
\]

Relative to

\[
L^2(-V,V)=\iota L^2(-U,U)\oplus\mathcal N_{U,V},
\]

write the blocks

\[
X_{0}:=\iota^*B_{0,V}\iota,
\qquad
Y_{0}:=P_{\mathcal N}B_{0,V}\iota,
\qquad
Z_{0}:=P_{\mathcal N}B_{0,V}P_{\mathcal N}.
\tag{H11.5}
\]

Thus

\[
\begin{pmatrix}
X_0&Y_0^*\\
Y_0&Z_0
\end{pmatrix}\succeq0.
\tag{H11.6}
\]

Since PR #55/#57 notation gives

\[
S=R_VP_{\mathcal N},
\qquad
S^*S=P_{\mathcal N}A_VP_{\mathcal N},
\]

(H11.4) yields

\[
\boxed{0\preceq Z_0\preceq S^*S.}
\tag{H11.7}
\]

---

## 2. Exact identification of hard11 with the primitive part of level 0

Expanding one fixed prime sector in (H11.3) gives the coefficient

\[
(\log p)(p-1)p^{-3(k+\ell)/4}
\tag{H11.8}
\]

for the `(k,\ell)` pair, with the same half-shift sign decomposition used in PR #58.

This is exactly the `a=0` summand in the projected-mark coefficient from PR #58.  Indeed

\[
p^m-1=(p-1)\sum_{a=0}^{m-1}p^a,
\qquad m=\min\{J,k,\ell\},
\tag{H11.9}
\]

and the `a`-level term occurs only when `a\le k-1` and `a\le\ell-1`.

For `(k,\ell)=(1,1)` this forces

\[
\boxed{a=0\text{ only}.}
\tag{H11.10}
\]

Hence the complete hard11 normal family is contained in `B_{0,V}` and has exact scalar size

\[
(\log p)(p-1)p^{-3/2}
=(\log p)(p^{-1/2}-p^{-3/2}),
\tag{H11.11}
\]

which is precisely the non-absolutely-summable `\asymp(\log p)p^{-1/2}` scale isolated by PR #58.

For `k=\ell=1`, the two zero-displacement sign terms are killed exactly in the old-to-new block by PR #58 GN10.  Denote the remaining two sum-sign old-to-new terms, summed over primes, by

\[
Y_{11}^{\rm sum}.
\tag{H11.12}
\]

Define the remainder

\[
E_{0}:=Y_0-Y_{11}^{\rm sum}.
\tag{H11.13}
\]

Every nonzero-displacement sign term in `E_0` has `(k,\ell)\ne(1,1)`, hence

\[
k+\ell\ge3.
\tag{H11.14}
\]

This already separates hard11 from the aggregate hard22 obstruction: the `a=0`, `(2,2)` contribution has coefficient

\[
(\log p)(p-1)p^{-3}=O((\log p)p^{-2}),
\]

so it is good; the genuinely nonsummable `k=\ell=2` scale comes from higher martingale level, in particular `a=1`.

### Local draft booking

```text
R43-COND-HARD11-LEVEL0-POSITIVE-CHANNEL ✓[M]
```

Scope: exact identification inside the PR #56/#58 factorization only; no decay claim.

---

## 3. The entire level-0 remainder has a beta=1/8 exponential displacement moment

For an individual sign term from `(p,k,\ell)` in `E_0`, multiplication/truncation does not increase the operator norm, so (H11.8) gives

\[
\|T\|
\le
(\log p)(p-1)p^{-3(k+\ell)/4}.
\tag{H11.15}
\]

Its displacement magnitude satisfies

\[
\delta(T)
\le
(k+\ell)a_p
=\frac{k+\ell}{2}\log p.
\tag{H11.16}
\]

Set

\[
\beta_*:=\frac18.
\]

Using `p-1\le p`,

\[
\begin{aligned}
e^{\beta_*\delta(T)}\|T\|
&\le
(\log p)
 p^{1-3(k+\ell)/4+(k+\ell)/16}\\
&=
(\log p)
 p^{1-11(k+\ell)/16}.
\end{aligned}
\tag{H11.17}
\]

Because `k+\ell\ge3`, the worst exponent is

\[
1-\frac{33}{16}=-\frac{17}{16}<-1.
\tag{H11.18}
\]

The geometric sum over `k,\ell` is uniformly convergent for `p\ge2`, and the prime sum is bounded by the corresponding integer sum.  Therefore there exists an absolute finite constant `C_0` such that, uniformly in `V`,

\[
\boxed{
\sum_{T\in\mathscr E_0}
e^{\delta(T)/8}\|T\|
\le C_0.
}
\tag{H11.19}
\]

Consequently, for every `r>0`,

\[
\boxed{
\left\|\sum_{\substack{T\in\mathscr E_0\\\delta(T)>r}}T\right\|
\le C_0e^{-r/8}.
}
\tag{H11.20}
\]

For `\delta(T)\le r`, the same old-to-new support argument as PR #58 GN20 gives

\[
P_{\mathcal N}T\iota
=P_{\mathcal N}T\iota\chi_{U,r},
\qquad
\chi_{U,r}:=1_{\{U-r<|u|<U\}}.
\tag{H11.21}
\]

Hence

\[
\boxed{
\|E_0x\|
\le
C_0\bigl(\|\chi_{U,r}x\|+e^{-r/8}\|x\|\bigr).
}
\tag{H11.22}
\]

Since `(I+S^*S)^{-1/2}` is a contraction, the same upper bound holds after saturation.

### Local draft booking

```text
R43-COND-HARD11-LEVEL0-REMAINDER-EXPONENTIAL-MOMENT ✓[M]
```

---

## 4. Positive block Schur absorption of the divergent level-0 offblock

From (H11.6), adding the identity on the new block preserves positivity:

\[
\begin{pmatrix}
X_0&Y_0^*\\
Y_0&I+Z_0
\end{pmatrix}
\succeq0.
\tag{H11.23}
\]

Because `I+Z_0` is boundedly invertible, its Schur complement is positive:

\[
\boxed{
Y_0^*(I+Z_0)^{-1}Y_0\preceq X_0.
}
\tag{H11.24}
\]

By (H11.7), operator monotonicity of inversion gives

\[
(I+S^*S)^{-1}\preceq(I+Z_0)^{-1}.
\tag{H11.25}
\]

Therefore, for every old-source vector `x`,

\[
\begin{aligned}
\|(I+S^*S)^{-1/2}Y_0x\|^2
&=
\langle Y_0x,(I+S^*S)^{-1}Y_0x\rangle\\
&\le
\langle Y_0x,(I+Z_0)^{-1}Y_0x\rangle\\
&\le
\langle x,X_0x\rangle.
\end{aligned}
\]

Thus

\[
\boxed{
\|(I+S^*S)^{-1/2}Y_0x\|
\le
\langle x,X_0x\rangle^{1/2}.
}
\tag{H11.26}
\]

This is the key saturation effect: the raw non-absolutely-summable prime family is not estimated prime-by-prime.  It is absorbed as the off-diagonal block of one positive residual square and controlled by the matching old diagonal energy.

---

## 5. Hard11 saturation reduction

From

\[
Y_{11}^{\rm sum}=Y_0-E_0,
\]

the triangle inequality, (H11.22), and (H11.26) give, for every `r>0`,

\[
\boxed{
\begin{aligned}
\|(I+S^*S)^{-1/2}Y_{11}^{\rm sum}x\|
\le{}&
\langle x,X_0x\rangle^{1/2}\\
&+C_0\|\chi_{U,r}x\|
+C_0e^{-r/8}\|x\|.
\end{aligned}
}
\tag{H11.27}
\]

For the actual PR #58 vector

\[
x=x_{U,V}(f)
=\mathcal Q_{U,V}H_U^*E_{X,U}f,
\tag{H11.28}
\]

and terminal-graph normalization, PR #58 already gives `\|x\|\le1`.  Hence

\[
\boxed{
\begin{aligned}
\|(I+S^*S)^{-1/2}Y_{11}^{\rm sum}x_{U,V}(f)\|
\le{}&
\langle x_{U,V}(f),X_0x_{U,V}(f)\rangle^{1/2}\\
&+C_0\|\chi_{U,r}x_{U,V}(f)\|
+C_0e^{-r/8}.
\end{aligned}
}
\tag{H11.29}
\]

### Local draft booking

```text
R43-COND-HARD11-LEVEL0-SATURATION-REDUCTION ✓[M]
```

The booking is **only** the exact bound (H11.27)/(H11.29).  It is not a hard11-decay theorem.

---

## 6. What remains open after H11.29

The collar term in H11.29 is already one of the PR #58 global open gates:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ?[O]
```

The genuinely new remaining hard11 scalar is

\[
\boxed{
\mathcal E_{0;U,V}(f)
:=
\langle x_{U,V}(f),X_0x_{U,V}(f)\rangle.
}
\tag{H11.30}
\]

Thus a sufficient next theorem is

\[
\boxed{
\mathcal E_{0;U,V}(f)\longrightarrow0
}
\tag{H11.31}
\]

in exactly the quantifier regime ultimately needed by the direct B-FLAGDYN/FD23 route.

Roadmap-only label until theoremized:

```text
ROADMAP-HARD11-LEVEL0-OLD-ENERGY-DECAY
  type: research-subquestion
  math_status: null
  research_status: open
```

### Quantifier firewall

This note does not choose or infer:

- the required relation between `U` and `V`;
- uniformity in intermediate `V`;
- pointwise versus uniform source control;
- a cofinal partition;
- the optimizing choice `r=r(U,V)`;
- the order of limits.

---

## 7. Useful but insufficient old-residual contraction

There is one exact auxiliary inequality that may help with H11.30.

Put

\[
A_U:=R_U^*R_U,
\qquad
B_U:=(I+A_U)^{-1}.
\]

PR #57/#58 gives

\[
\mathcal Q_{U,V}^2\preceq B_U.
\tag{H11.32}
\]

By Douglas factorization there is a contraction `C_{U,V}` such that

\[
\mathcal Q_{U,V}=B_U^{1/2}C_{U,V}.
\tag{H11.33}
\]

Since `A_U` commutes with `B_U` and

\[
\sup_{t\ge0}\sqrt{\frac{t}{1+t}}\le1,
\]

we obtain for every `y`

\[
\boxed{
\|R_U\mathcal Q_{U,V}y\|
=\|A_U^{1/2}\mathcal Q_{U,V}y\|
\le\|y\|.
}
\tag{H11.34}
\]

This controls the **old full residual energy already present at horizon `U`** after geometric transport.  It does not by itself imply H11.31, because `X_0` is the level-0 old block of the horizon-`V` residual normal, and a separate exact nesting/strip comparison is required before replacing it by an `A_U` quantity.

### Local draft booking

```text
R43-COND-GEOMETRIC-TRANSPORT-OLD-RESIDUAL-CONTRACTION ✓[M]
```

Again: no decay rate follows unless the norm of the relevant pre-transport vector is known to decay in the correct space or the horizon-`V` level-0 increment is separately controlled.

---

## 8. Relation to R40/R42 — explicit non-identification firewall

R40/R42 prove for a different future-dual-normal construction

\[
\|A_X(U)^{-1/2}r_X\|\asymp U^{-1},
\]

and R42 identifies its normalized limiting direction.

The current structured pre-transport vector is instead

\[
H_U^*E_{X,U}f.
\]

No theorem in the present stack identifies these two objects or transports the R40/R42 `U^{-1}` scale to H11.30.  Such an identification would be valuable, but until proved it is forbidden to use the R40/R42 rate in (H11.29).

Possible roadmap question:

```text
ROADMAP-HARD11-DUALNORMAL-STRUCTURED-SOURCE-BRIDGE
  type: research-question
  math_status: null
  research_status: open
```

---

## 9. Resulting front

Before this note, hard11 was an unsummed primitive prime family of raw size

\[
(\log p)p^{-1/2}.
\]

After this note, the prime divergence itself is removed from the quantitative target.  The channel is reduced to

\[
\boxed{
\text{old level-0 residual energy}
+\text{transported collar mass}
+\text{exponential tail}.
}
\]

The next mathematically honest target is therefore not another primewise summation estimate.  It is the structured energy question H11.31, preferably by exploiting exact horizon nesting and/or a proved bridge to the R40/R42 normal geometry.

No global theorem is promoted by this reduction.