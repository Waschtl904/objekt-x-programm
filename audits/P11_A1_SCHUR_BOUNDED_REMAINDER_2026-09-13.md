# P11 A1-SCHUR — bounded-band lower operator and explicit resolved--tail penalty

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent main:** `8497eaff59b7b61ec227ac596615278d53aa37fc` / PR #113.  

## 1. Purpose

PR #113 closed the entire infinite Prolate tail for `q_1`, but left a formally unbounded Fourier multiplier in the resolved--tail crossblock.

This audit removes that obstruction. It constructs a **bounded bandlimited lower operator** by discarding only a positive high-frequency piece. After augmenting the resolved PSWF space with the two moment Riesz vectors, the rank-2 completion has no crossblock at all. The remaining crossblock is bounded explicitly by a PSWF concentration eigenvalue.

With `N=1680`, the intended exact-head Arb gate certifies a Schur penalty below

```math
4.1\times10^{-36}.
```

Therefore a rigorous resolved-space lower bound

```math
\mu_R\ge5\times10^{-36}
```

would be sufficient to prove the full canonical `a=1` completion.

No such resolved lower bound is claimed here. Hence no `a=1` positivity theorem is yet promoted.

---

## 2. Imported `a=1` multiplier facts

On `L^2(-1,1)`, after zero extension and with the unitary Fourier transform,

```math
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2d\xi,
```

where

```math
m_1(\xi)=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

From PR #113:

```math
m_1(\xi)>c:=0.04
\qquad(|\xi|\ge\Omega:=2300),
```

and globally

```math
m_1(\xi)\ge-\Gamma_1.
```

---

## 3. Bounded-band lower operator `✓[M]`

Define

```math
r(\xi)
:=(m_1(\xi)-c)\mathbf1_{[-\Omega,\Omega]}(\xi),
```

and

```math
s(\xi)
:=(m_1(\xi)-c)\mathbf1_{\mathbb R\setminus[-\Omega,\Omega]}(\xi).
```

By the high-frequency theorem,

```math
s(\xi)\ge0.
```

Let `P_I` denote time restriction/zero extension for `I=(-1,1)`, and let

```math
K=P_I\mathcal F^{-1}M_r\mathcal F P_I.
```

Then `K` is a bounded self-adjoint bandlimited compressed multiplier and

```math
q_1
=
cI+K+P_I\mathcal F^{-1}M_s\mathcal F P_I.
```

Therefore

```math
\boxed{q_1\succeq cI+K.}
```

For the canonical completion

```math
A_1=q_1+\mathcal E^*\mathcal E
```

we consequently have

```math
\boxed{
A_1\succeq L_1:=cI+K+\mathcal E^*\mathcal E.
}
```

Thus it is sufficient to prove `L_1>=0`.

This step is crucial: the unbounded positive high-frequency growth of `m_1` is discarded, so every remaining nontrivial crossblock comes from the bounded multiplier `r`.

---

## 4. Rigorous compact-band bound for `r`

The lower side is immediate from `m_1>=-Gamma_1`:

```math
r(\xi)\ge-(\Gamma_1+c)
\qquad(|\xi|\le\Omega).
```

For the upper side, use the exact positive series

```math
\operatorname{Re}\psi(x+iy)-\psi(x)
=
\sum_{k=0}^\infty
\frac{y^2}{(k+x)((k+x)^2+y^2)}.
```

Each summand is increasing in `|y|`. For decreasing

```math
f_y(u)=\frac{y^2}{u(u^2+y^2)},
```

the tail satisfies

```math
\sum_{k=N}^{\infty}f_y(k+x)
\le
f_y(N+x)+\int_N^\infty f_y(t+x)dt.
```

At `x=1/4`, `|y|<=1150`, `N=64`, and using the worst prime cosine sign, this gives a finite interval upper bound for `m_1` on the full compact band.

The exact-head Arb checker

```text
scripts/check_a1_schur_cross_arb.py
```

is designed to certify

```math
\boxed{\|r\|_{L^\infty}<12.}
```

Status is `✓[K/M]` only after that exact-head gate succeeds.

---

## 5. Prolate subspaces and moment augmentation

Let

```math
B=B_{\Omega}
```

be Fourier projection to `[-Omega,Omega]`, and

```math
C=P_I B P_I
```

the time-band concentration operator. Let

```math
C\psi_k=\lambda_k\psi_k,
\qquad
1>\lambda_0>\lambda_1>\cdots>0,
```

with normalized timelimited PSWFs `psi_k`.

Set

```math
R_N^0=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\}.
```

The moment map

```math
\mathcal Ev=(E_+(v),E_-(v))
```

has Riesz range

```math
\mathcal M
=\operatorname{span}\{e^{x/2},e^{-x/2}\}
\subset L^2(-1,1).
```

Define the **augmented resolved space**

```math
\boxed{R_N=R_N^0+\mathcal M}
```

and

```math
\boxed{T_N=R_N^\perp.}
```

Then

```math
T_N\subset(R_N^0)^\perp,
```

so for every `t in T_N`,

```math
\|Bt\|^2\le\lambda_N\|t\|^2.
```

Moreover, because `T_N` is orthogonal to both moment Riesz vectors,

```math
\boxed{\mathcal E t=0\qquad(t\in T_N).}
```

Hence the completion term `E^*E` has **zero tail block and zero resolved--tail crossblock** in this augmented decomposition.

---

## 6. Tail lower bound for the bounded lower operator `✓[M]`

Let `t in T_N`. Since `Et=0`,

```math
L_1(t)=c\|t\|^2+\langle t,Kt\rangle.
```

Because `r>=-(Gamma_1+c)` on the band,

```math
\langle t,Kt\rangle
\ge-(\Gamma_1+c)\|Bt\|^2.
```

Therefore

```math
\boxed{
L_1|_{T_N}
\succeq
\tau_N I,
\qquad
\tau_N:=c-(\Gamma_1+c)\lambda_N.
}
```

---

## 7. Explicit resolved--tail crossblock bound `✓[M]`

Let `u in R_N`, `t in T_N`. Orthogonality kills the scalar `cI` cross term, and `Et=0` kills the completion cross term. Thus

```math
\langle u,L_1t\rangle=\langle u,Kt\rangle.
```

Since `r` is supported in the band,

```math
\langle u,Kt\rangle
=\int_{-\Omega}^{\Omega}
r(\xi)\widehat u(\xi)\overline{\widehat t(\xi)}d\xi.
```

Hence

```math
|\langle u,Kt\rangle|
\le\|r\|_\infty\|Bu\|\|Bt\|
\le\|r\|_\infty\sqrt{\lambda_N}\|u\|\|t\|.
```

Therefore

```math
\boxed{
\|(L_1)_{RT}\|
\le\|r\|_\infty\sqrt{\lambda_N}.
}
```

This is the quantitative crossblock estimate missing from PR #113.

---

## 8. Finite Schur criterion `✓[M]`

Assume

```math
(L_1)_{RR}\succeq\mu_R I
```

and `tau_N>0`. Then the Schur complement gives `L_1>=0` provided

```math
\mu_R
\ge
\frac{\|(L_1)_{RT}\|^2}{\tau_N}.
```

Using the previous bound, it suffices that

```math
\boxed{
\mu_R
\ge
\frac{\|r\|_\infty^2\lambda_N}
{c-(\Gamma_1+c)\lambda_N}.
}
```

Since `A_1>=L_1`, this condition proves the full canonical completion `A_1>=0`, and hence `q_1>=0` on the null-pole class.

---

## 9. Explicit `N=1680` target

Keep

```text
Omega=2300,
c=0.04,
N=1680.
```

Karnik--Romberg--Davenport Corollary 3 gives the same explicit PSWF eigenvalue upper bound as in PR #113, now at `k=1680`.

The new exact-head Arb checker is designed to certify simultaneously

```math
\boxed{\|r\|_\infty<12,}
```

```math
\boxed{\lambda_{1680}(2300)<1.1\times10^{-39},}
```

```math
\boxed{\tau_{1680}>0.039,}
```

and

```math
\boxed{
\frac{\|r\|_\infty^2\lambda_{1680}}
{\tau_{1680}}
<4.1\times10^{-36}.
}
```

Consequently the single finite target

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I
}
```

would be sufficient to close the entire `a=1` canonical completion.

This is a genuine quantitative target, not a fitted threshold: `5e-36` is chosen before any resolved-space computation and only to dominate the certified Schur penalty.

---

## 10. Parity dimensions

The first `1680` PSWF modes contain

```text
840 even,
840 odd.
```

The moment range splits as

```math
\operatorname{span}\{\cosh(x/2)\}
\oplus
\operatorname{span}\{\sinh(x/2)\}.
```

Thus the augmented resolved space has dimension at most

```text
841 even + 841 odd = 1682.
```

The finite certification can therefore be performed parity by parity.

---

## 11. What remains

After this audit and a successful exact-head Arb gate, the `a=1` theorem problem reduces to one finite statement:

```math
\boxed{
(L_1)_{RR}\succeq5\times10^{-36}I
\quad\text{on }R_{1680}.
}
```

No separate infinite-tail or unresolved crossblock theorem remains: both are absorbed by the explicit Schur penalty.

The remaining computational challenge is to represent/certify the finite PSWF resolved operator and moment augmentation with sufficient interval accuracy.

---

## 12. Status

```text
bounded-band lower operator q_1 >= cI+K                   ✓[M]
moment-augmented Prolate decomposition                     ✓[M]
completion crossblock vanishes on augmented tail            ✓[M]
abstract K_RT <= ||r|| sqrt(lambda_N)                        ✓[M]
finite Schur criterion                                       ✓[M]
||r||_infty<12                                               candidate ✓[K/M]
lambda_1680(c=2300)<1.1e-39                                 candidate ✓[K/M]
tau_1680>0.039                                               candidate ✓[K/M]
Schur penalty <4.1e-36                                      candidate ✓[K/M]
resolved target 5e-36 sufficient                            candidate ✓[K/M]
resolved finite lower bound >=5e-36                         ?[O]
a=1 completion certificate                                  ?[O]
all-a NP-GAP / Object X / RH                                 ?[O]
```

Registry and Object-X working definition remain unchanged.

## 13. Firewalls

Do not claim:

- the resolved lower bound has been proved;
- `5e-36` is an observed eigenvalue or fitted value;
- the PSWF basis diagonalizes `K` or `q_1`;
- the physical Weil matrix `P` is being certified here;
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
