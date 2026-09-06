# P11 / R43 — prime-band escape for the resolvent-transported terminal collar

**Date:** 2026-09-06  
**Status:** exact/local quantitative reduction on top of PR #61; direct FLAGDYN composition and Strong Terminal remain OPEN  
**Exact parent head:** `e29545a6040640e754e885888826d1cf235df58c`

## 0. Purpose and scope

PR #61 reduces the positive structured scalar conditioning increment to the transported terminal collar:

\[
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
C_{\rm ret}^2
\left(
\|\chi_{U,r}x_{U,V}(f)\|
+e^{-r/8}\|x_{U,V}(f)\|
\right)^2,
\tag{CE0}
\]

where

\[
x_{U,V}(f)=\mathcal Q_{U,V}H_U^*E_{X,U}f,
\qquad
\chi_{U,r}=1_{\{U-r<|u|<U\}}.
\]

The nonlocality of `\mathcal Q_{U,V}` prevents one from simply importing the raw hub-shell support theorem.  This note proves a different statement: every old-source vector with controlled old residual graph energy must lose mass from a collar whose relative width tends to zero.  The proof uses only the level-0, `k=1` prime channel, grouped into logarithmic prime bands, while all `k\ge2` terms are absorbed as an absolutely summable error.

Combining that escape inequality with the exact geometric-mean Riccati identity and CE0 closes the collar estimate by a self-consistency argument.

No operatorwide `B-METINC-COND`, no direct COND-to-FLAGDYN bridge, no B-FLAGTIGHT, no Strong Terminal/C6, no Object-X realization, and no RH claim is made.

---

## 1. Prime-band weight lower bound

For a prime `p` define the level-0 primitive weight

\[
\boxed{
 w_p:=(\log p)(p-1)p^{-3/2}.
}
\tag{CE1}
\]

Only a coarse prime-counting theorem is needed.

### Lemma 1 — fixed multiplicative prime bands

There exist fixed constants

\[
\Lambda>1,
\qquad
c_{\rm pb}>0,
\qquad
t_{\rm pb}>0,
\]

such that for every `t\ge t_{\rm pb}`,

\[
\boxed{
\sum_{e^t\le p\le \Lambda e^t} w_p
\ge c_{\rm pb}e^{t/2}.
}
\tag{CE2}
\]

### Proof

Classical Chebyshev prime-counting bounds give constants `c_1,c_2>0` such that, for large `x`,

\[
c_1\frac{x}{\log x}
\le\pi(x)\le
c_2\frac{x}{\log x}.
\]

Choose once and for all `\Lambda` large enough that the lower bound at `\Lambda x` dominates the upper bound at `x`.  Then

\[
\pi(\Lambda x)-\pi(x)
\ge c_3\frac{x}{\log x}
\]

for all sufficiently large `x`.

For `x\le p\le\Lambda x`,

\[
\log p\asymp\log x,
\qquad
(p-1)p^{-3/2}\asymp p^{-1/2}\asymp x^{-1/2},
\]

with constants depending only on the fixed `\Lambda`. Therefore

\[
\sum_{x\le p\le\Lambda x}w_p
\gtrsim
\frac{x}{\log x}\,(\log x)x^{-1/2}
=\sqrt{x}.
\]

Taking `x=e^t` proves CE2.  The prime number theorem would give the same conclusion, but is stronger than needed.  \(\square\)

Put

\[
\delta_0:=\log\Lambda.
\tag{CE3}
\]

### Local draft booking

```text
R43-COND-PRIME-BAND-WEIGHT-LOWER-BOUND ✓[M]
```

This uses only the classical Chebyshev prime-counting theorem as external standard input.

---

## 2. Level-0 factor and extraction of the k=1 difference

Use the exact martingale-level factorization from PR #56.  At horizon `U`,

\[
T_{p,0;U}
=
\sqrt{(\log p)(p-1)}\,
1_{\Omega_{p,0,U}}
\sum_{k\ge1}p^{-3k/4}K_{p,k;U},
\tag{CE4}
\]

with

\[
\Omega_{p,0,U}=\{u:|u|+a_p\le U\},
\qquad
a_p=\frac12\log p,
\]

and

\[
A_U=R_U^*R_U
=\sum_p\sum_{a\ge0}T_{p,a;U}^*T_{p,a;U}.
\tag{CE5}
\]

Hence

\[
\boxed{
\|R_Ux\|^2
\ge\sum_{p\in\mathcal P}\|T_{p,0;U}x\|^2
}
\tag{CE6}
\]

for every selected prime set `\mathcal P`.

Split

\[
\sum_{k\ge1}p^{-3k/4}K_{p,k;U}
=
p^{-3/4}K_{p,1;U}+G_{p,U},
\tag{CE7}
\]

where

\[
G_{p,U}:=\sum_{k\ge2}p^{-3k/4}K_{p,k;U}.
\]

Since `\|K_{p,k;U}\|\le2`,

\[
\boxed{
\|G_{p,U}\|
\le
2\frac{p^{-3/2}}{1-p^{-3/4}}
\le C_Gp^{-3/2}.
}
\tag{CE8}
\]

Therefore

\[
\sum_p(\log p)(p-1)\|G_{p,U}\|^2
\le
C\sum_p(\log p)p^{-2}
<\infty
\tag{CE9}
\]

uniformly in `U`.

This is the crucial error estimate: extracting `k=1` from the positive level-0 square costs only a horizon-uniform `L^2` error.

---

## 3. One collar and one logarithmic prime band

Let

\[
I_+(U,r):=(U-r,U)
\]

and assume

\[
0<r<U/8.
\tag{CE10}
\]

Take a prime with

\[
2r+\delta_0\le t:=\log p\le U-r.
\tag{CE11}
\]

For `z\in I_+(U,r)` set

\[
u=z-\frac t2.
\]

Because `t\le U-r<z`, one has `u>0`, and therefore

\[
|u|+\frac t2=z\le U.
\]

Thus `u\in\Omega_{p,0,U}`.  On this output interval the `k=1` difference is, up to the immaterial global sign convention,

\[
K_{p,1;U}x(u)=x(z)-x(z-t).
\tag{CE12}
\]

Restrict `T_{p,0;U}x` to these outputs.  Using

\[
\|a+b\|^2\ge\frac12\|a\|^2-\|b\|^2,
\]

CE7--CE9 give, after summing over any selected primes satisfying CE11,

\[
\boxed{
\sum_{p\in\mathcal P}w_p
\int_{I_+(U,r)}|x(z)-x(z-\log p)|^2\,dz
\le
C\bigl(\|R_Ux\|^2+\|x\|^2\bigr).
}
\tag{CE13}
\]

The constant is independent of `U,r` and of the selected prime set.

The negative collar

\[
I_-(U,r):=(-U,-U+r)
\]

satisfies the identical estimate by reflection symmetry.

### Local draft booking

```text
R43-COND-LEVEL0-K1-COLLAR-DIFFERENCE-ENERGY ✓[M]
```

---

## 4. Many disjoint shifted collar copies

Choose logarithmic band starts

\[
t_j
:=2r+\delta_0+(j-1)(r+\delta_0),
\qquad j=1,\dots,N,
\tag{CE14}
\]

where `N` is maximal subject to

\[
t_N+\delta_0\le U-r.
\tag{CE15}
\]

For all sufficiently large `U` with `r\ge r_0` and `r\le U/8`,

\[
\boxed{
N\ge c_N\frac Ur.
}
\tag{CE16}
\]

for an absolute constant `c_N>0`.

Let

\[
\mathcal P_j
:=\{p:e^{t_j}\le p\le e^{t_j+\delta_0}\},
\qquad
W_j:=\sum_{p\in\mathcal P_j}w_p.
\tag{CE17}
\]

By CE2 and `t_1\ge2r`,

\[
\boxed{
W_j\ge W_{\min}\ge c e^r.
}
\tag{CE18}
\]

For the positive collar, every interval

\[
I_+(U,r)-\log p,
\qquad p\in\mathcal P_j,
\]

is contained in

\[
J_{j,+}
:=
(U-r-t_j-\delta_0,\;U-t_j).
\tag{CE19}
\]

The intervals `J_{j,+}` are pairwise disjoint by the spacing in CE14, and CE15 keeps all of them inside `(0,U)`.  Similarly the reflected intervals `J_{j,-}` for the negative collar are pairwise disjoint inside `(-U,0)`.

For every complex numbers `a,b`,

\[
|a|^2\le2|a-b|^2+2|b|^2.
\tag{CE20}
\]

Apply CE20 with `a=x(z)`, `b=x(z-\log p)`, integrate over `I_+`, multiply by `w_p`, and sum over `p\in\mathcal P_j`.  Then

\[
W_j\|1_{I_+}x\|^2
\le
2E_j+2W_j\|1_{J_{j,+}}x\|^2,
\tag{CE21}
\]

where `E_j` is the corresponding weighted difference energy.

Summing CE21 over `j`, using pairwise disjointness and CE13,

\[
N\|1_{I_+}x\|^2
\le
\frac{C}{W_{\min}}
\bigl(\|R_Ux\|^2+\|x\|^2\bigr)
+2\|x\|^2.
\tag{CE22}
\]

The same argument applies to `I_-`. Hence

\[
\boxed{
\|\chi_{U,r}x\|^2
\le
C_1\frac rU\|x\|^2
+
C_2\frac rU e^{-r}
\bigl(\|R_Ux\|^2+\|x\|^2\bigr)
}
\tag{CE23}
\]

for all sufficiently large `r` and `U\ge C_0r`.

This estimate is uniform over **all** `x\in L^2(-U,U)`.

### Interpretation

The leading `r/U` term is unavoidable at this level of generality: a normalized constant vector lies in the kernel of the old residual difference operator and has exactly order `r/U` of its mass in the two terminal collars.  Thus CE23 has the correct universal scale up to constants.

### Local draft booking

```text
R43-COND-PRIME-BAND-RESIDUAL-COLLAR-ESCAPE ✓[M]
```

---

## 5. Exact graph energy of the geometric-mean transported vector

Return to

\[
v=v_U(f)=H_U^*E_{X,U}f,
\qquad
x=\mathcal Q_{U,V}v.
\tag{CE24}
\]

Use PR #57 notation

\[
\mathscr A_U=I+R_U^*R_U,
\qquad
\widetilde B_{U,V}:=\iota^*B_V\iota.
\]

The exact geometric-mean Riccati identity is

\[
\boxed{
\mathcal Q_{U,V}\,\mathscr A_U\,\mathcal Q_{U,V}
=\widetilde B_{U,V}.
}
\tag{CE25}
\]

Therefore

\[
\boxed{
\|x\|^2+\|R_Ux\|^2
=
\langle v,\widetilde B_{U,V}v\rangle.
}
\tag{CE26}
\]

Put

\[
s_U(f):=\langle v,B_Uv\rangle
\]

and

\[
\Delta:=\Delta s_{\rm cond}^{U,V}(f)
=\langle v,(\widetilde B_{U,V}-B_U)v\rangle.
\]

Then CE26 becomes the exact identity

\[
\boxed{
\|x\|^2+\|R_Ux\|^2=s_U(f)+\Delta.
}
\tag{CE27}
\]

Under the terminal-graph normalization used in PR #58/#61,

\[
q_U^X(E_{X,U}f)=1,
\]

one has

\[
0\le s_U(f)\le1.
\]

Writing

\[
\delta:=(\Delta)_+,
\]

CE27 yields

\[
\boxed{
\|x\|^2+\|R_Ux\|^2\le1+\delta.
}
\tag{CE28}
\]

In particular `\|x\|\le1`, recovering the earlier contraction statement but now with the old residual graph energy included in a self-consistent form.

### Local draft booking

```text
R43-COND-GEOMETRIC-TRANSPORT-EXACT-OLD-GRAPH-ENERGY ✓[M]
```

---

## 6. Self-closing transported collar estimate

Apply CE23 to the vector CE24 and use CE28.  There are constants independent of `U,V,f` in the normalized structured scope such that

\[
\boxed{
\|\chi_{U,r}x\|^2
\le
A\frac rU
+
A\frac rUe^{-r}(1+\delta).
}
\tag{CE29}
\]

PR #61 gives

\[
\delta
\le
C_{\rm ret}^2
\left(
\|\chi_{U,r}x\|+e^{-r/8}
\right)^2.
\tag{CE30}
\]

Hence, using `(a+b)^2\le2a^2+2b^2`,

\[
\delta
\le
A_1\frac rU
+A_1\frac rUe^{-r}(1+\delta)
+A_1e^{-r/4}.
\tag{CE31}
\]

For all sufficiently large `U` and admissible `r`, the coefficient

\[
A_1\frac rUe^{-r}
\]

is smaller than `1/2`, so the `\delta` term on the right can be absorbed. Therefore

\[
\boxed{
\delta
\le
C\left(
\frac rU+e^{-r/4}
\right).
}
\tag{CE32}
\]

Substituting back into CE29 gives

\[
\boxed{
\|\chi_{U,r}x\|^2
\le
C\left(
\frac rU+
\frac rUe^{-r}
+\frac rUe^{-r}\,e^{-r/4}
\right)
\le C'\frac rU
}
\tag{CE33}
\]

in the same asymptotic regime.

Choose

\[
\boxed{r(U):=8\log U.}
\tag{CE34}
\]

Then `r(U)\to\infty`, `r(U)/U\to0`, and

\[
e^{-r(U)/4}=U^{-2}.
\]

Thus, uniformly in every `V>U`,

\[
\boxed{
\|\chi_{U,8\log U}x_{U,V}(f)\|^2
=O\left(\frac{\log U}{U}\right),
}
\tag{CE35}
\]

and

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
=O\left(\frac{\log U}{U}\right)
}
\tag{CE36}
\]

under `q_U^X(E_{X,U}f)=1`.

Equivalently,

\[
\boxed{
\|\chi_{U,8\log U}x_{U,V}(f)\|
=O\left(\sqrt{\frac{\log U}{U}}\right).
}
\tag{CE37}
\]

### Local draft bookings

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ✓[M]
R43-COND-STRUCTURED-SCALAR-POSITIVE-INCREMENT-DECAY ✓[M]
```

**Scope of both bookings:** resolvent-transported structured scalar class, terminal-graph normalization, uniformly in `V>U`, conditional on the exact parent PR #61 identities.  Neither booking is operatorwide `B-METINC-COND`.

---

## 7. Homogeneous relative formulation

The argument is quadratic in `f`.  For nonzero source data define

\[
Q_U(f):=q_U^X(E_{X,U}f)>0.
\]

Scaling CE36 gives

\[
\boxed{
\sup_{V>U}
\frac{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
}{Q_U(f)}
\le
C\frac{\log U}{U}
}
\tag{CE38}
\]

for all sufficiently large `U`.

Similarly,

\[
\boxed{
\sup_{V>U}
\frac{
\|\chi_{U,8\log U}x_{U,V}(f)\|^2
}{Q_U(f)}
\le
C\frac{\log U}{U}.
}
\tag{CE39}
\]

The constant is uniform in `V`; the statement does not assert any unrelated operator norm bound.

---

## 8. Geometric-chain normalized positive variation

Take a geometric terminal chain

\[
U_j=U_0 2^j.
\tag{CE40}
\]

Then

\[
\sum_{j\ge0}
\frac{\log U_j}{U_j}<\infty.
\tag{CE41}
\]

Hence CE38 implies

\[
\boxed{
\sum_{j\ge0}
\sup_{V>U_j}
\frac{
\bigl(\Delta s_{\rm cond}^{U_j,V}(f)\bigr)_+
}{Q_{U_j}(f)}
<\infty.
}
\tag{CE42}
\]

In particular the consecutive geometric-chain relative positive variations are summable.

### Local draft booking

```text
R43-COND-GEOMETRIC-CHAIN-RELATIVE-POSITIVE-VARIATION-SUMMABLE ✓[M]
```

### Firewall

CE42 is **normalized/relative scalar summability**.  It is not a claim that the unnormalized raw scalar increments are summable, and it is not yet the direct B-FLAGDYN/FD23 composition theorem.  The latter must still identify the exact normalized quantity needed downstream and transport the estimate through the flag dynamics with the correct quantifiers.

---

## 9. What is now open

Conditional on destructive review of this exact head and its parent stack, the structured scalar COND front is reduced further.

The following remain OPEN:

```text
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
FD23-UNIF / any required fixed-interval projected uniformity
B-FLAGDYN / B-FLAGTIGHT
B-SIGN / B-ORIENT
Strong Terminal / C6
genuine X candidate / Object-X realization
RH
```

The stronger operatorwide nodes remain OPEN:

```text
B-METINC-COND
B-METINC-GEO
B-METINC-NEW
B-METINC-WIDTH
```

No implication from failure or success of this scalar route to those operatorwide nodes is asserted.

---

## 10. Adversarial checklist

A destructive review should verify especially:

1. the fixed-multiplicative prime-band lower bound CE2 from Chebyshev prime-counting bounds;
2. extraction of the `k=1` level-0 difference and the summable `k\ge2` penalty CE8--CE13;
3. the exact collar/output eligibility used in CE12 for all selected bands;
4. disjointness and in-domain placement of the shifted intervals CE19;
5. the `N\asymp U/r` and `W_{\min}\gtrsim e^r` combination giving CE23;
6. the Riccati identity CE25 and exact graph-energy identity CE27;
7. the self-consistency absorption CE29--CE32;
8. uniformity in `V>U`;
9. the homogeneous passage CE38--CE39;
10. that CE42 is relative scalar summability only and does not silently close the direct FLAGDYN bridge.

Keep this mathematics Draft.  No Registry promotion or merge should occur without a fresh destructive review of the exact resulting head.
