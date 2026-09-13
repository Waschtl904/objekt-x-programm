# P11 A1-TAIL — exact Fourier multiplier, high-frequency positivity, and rigorous Prolate tail

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent main:** `c85f231153b9ad3154a860b792597700f6770a7c` / PR #112.  

## 1. Purpose

The A1-CERT front left one theorem-level obstruction: a rigorous lower bound on the unresolved infinite-dimensional tail at `a=1`.

This audit closes that tail problem in a concrete Prolate decomposition. It proves:

1. `q_1` is **exactly** the restriction of a whole-line Fourier multiplier; there are no additional window remainder terms in the quadratic form;
2. the multiplier is uniformly positive for `|xi|>=2300`, with a certified lower bound `m_1(xi)>0.04`;
3. the Karnik--Romberg--Davenport non-asymptotic PSWF bound gives `lambda_1490(c=2300)<0.0035`;
4. therefore the orthogonal Prolate tail after the first `1490` timelimited PSWF modes satisfies

```math
q_1(v)>0.01\|v\|_2^2.
```

The remaining A1-CERT problem is now finite-dimensional plus a resolved--tail coupling/Schur-complement estimate.

No fixed-window positivity theorem at `a=1`, no all-window NP-GAP, and no RH claim is made.

---

## 2. Exact Fourier multiplier for `q_a` `✓[M]`

Use the unitary Fourier transform

```math
\widehat v(\xi)
=(2\pi)^{-1/2}\int_{\mathbb R}v(x)e^{-i\xi x}\,dx.
```

From COMMON-JUMP,

```math
q_a(v)
=\|X_av\|^2-\Gamma_a\|v\|^2,
```

with

```math
K_t=T_{t/2}-T_{-t/2},
\qquad
\widehat{K_t^*K_t}(\xi)=2(1-\cos(\xi t)).
```

The archimedean jump energy has multiplier

```math
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)-\psi(1/4),
```

and each active prime power contributes

```math
2w_n(1-\cos(\xi\log n)),
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}.
```

Since

```math
\Gamma_a
=2\sum_{n\in\mathcal P_a}w_n+\log\pi-\psi(1/4),
```

we obtain the exact whole-line symbol

```math
\boxed{
m_a(\xi)
=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)
-\log\pi
-2\sum_{n\in\mathcal P_a}w_n\cos(\xi\log n).
}
```

Thus for every zero-extended `v` supported in `(-a,a)` in the form domain,

```math
\boxed{
q_a(v)
=\int_{\mathbb R}m_a(\xi)|\widehat v(\xi)|^2\,d\xi.
}
```

### Window firewall

The compressed interval operator is of course not diagonal in an arbitrary interval basis, but the **quadratic form is exactly the whole-line Fourier multiplier restricted to time-limited functions**. There is no additional non-diagonal or boundary remainder to add to the identity above.

This closes the precondition raised for a direct Prolate tail argument.

---

## 3. The `a=1` multiplier

At `a=1`, the active prime powers are exactly

```text
2, 3, 4, 5, 7,
```

because `log 7<2<log 8`.

Set

```math
W_1
=
\frac{\log2}{\sqrt2}
+\frac{\log3}{\sqrt3}
+\frac{\log2}{2}
+\frac{\log5}{\sqrt5}
+\frac{\log7}{\sqrt7}.
```

Then

```math
\boxed{
m_1(\xi)
=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)
-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
}
```

Also, since the positive COMMON-JUMP feature part is nonnegative,

```math
\boxed{
m_1(\xi)\ge-\Gamma_1,}
```

where

```math
\Gamma_1
=\kappa_*+2W_1,
\qquad
\kappa_*=\log\pi-\psi(1/4).
```

---

## 4. Elementary digamma lower bound `✓[M]`

DLMF 5.7.6 gives, for `x>0`,

```math
\psi(z)
=-\gamma+\sum_{k=0}^{\infty}
\left(\frac1{k+1}-\frac1{k+z}\right).
```

Taking `z=x+iy` and subtracting the real value `psi(x)` gives

```math
\boxed{
\operatorname{Re}\psi(x+iy)-\psi(x)
=
\sum_{k=0}^{\infty}
\frac{y^2}{(k+x)((k+x)^2+y^2)}.
}
```

For fixed `y`, define

```math
f_y(u)=\frac{y^2}{u(u^2+y^2)},\qquad u>0.
```

It is positive and strictly decreasing. Therefore, for every integer `N>=0`,

```math
\sum_{k=N}^{\infty}f_y(k+x)
\ge
\int_N^\infty f_y(t+x)\,dt
=
\frac12\log\left(1+\frac{y^2}{(N+x)^2}\right).
```

Hence

```math
\boxed{
\begin{aligned}
\operatorname{Re}\psi(x+iy)-\psi(x)
\ge{}&
\sum_{k=0}^{N-1}
\frac{y^2}{(k+x)((k+x)^2+y^2)}\\
&+\frac12\log\left(1+\frac{y^2}{(N+x)^2}\right).
\end{aligned}
}
```

Every term on the right is increasing in `|y|`. Thus a lower bound checked at one boundary value remains valid for all larger `|y|`.

For `x=1/4` we also use the exact special value

```math
\psi(1/4)=-\gamma-\frac\pi2-3\log2.
```

---

## 5. Certified high-frequency positivity `✓[K/M]`

Take

```text
N = 64,
Omega = 2300.
```

Since every cosine is at most `1`,

```math
m_1(\xi)
\ge
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)
-\log\pi-2W_1.
```

Apply the monotone lower bound of Section 4 at `|xi|=Omega`.

The exact-head Arb checker

```text
scripts/check_a1_highfreq_multiplier_arb.py
```

certifies at 256-bit precision that

```math
\boxed{
m_1(\xi)>0.04
\qquad(|\xi|\ge2300).
}
```

The certificate uses only rational operations, `pi`, Euler's constant, logarithms, square roots and Arb interval arithmetic. No floating-point conversion enters an acceptance test.

---

## 6. Band/time concentration operator

Let

```math
B_\Omega
```

be the orthogonal Fourier projection to `[-Omega,Omega]`, and let

```math
P=P_{[-1,1]}
```

be time restriction/zero extension.

On `L^2(-1,1)`, define the standard time-band concentration operator

```math
\boxed{
C_\Omega=P B_\Omega P.
}
```

Its kernel is

```math
C_\Omega(x,y)
=\frac{\sin(\Omega(x-y))}{\pi(x-y)}.
```

Let its eigenvalues be

```math
1>\lambda_0>\lambda_1>\cdots>0
```

and its normalized timelimited PSWF eigenfunctions be `psi_k`.

For

```math
\mathcal R_N
=\operatorname{span}\{\psi_0,\ldots,\psi_{N-1}\},
\qquad
\mathcal T_N=\mathcal R_N^\perp,
```

min-max gives for every `v in T_N`

```math
\boxed{
\|B_\Omega v\|_2^2
\le\lambda_N\|v\|_2^2.
}
```

The operator commutes with reflection, so both `R_N` and `T_N` may be chosen parity invariant.

---

## 7. Abstract Prolate-tail coercivity lemma `✓[M]`

Suppose

```math
m_1(\xi)\ge c>0
\quad\text{for }|\xi|>\Omega,
```

and globally

```math
m_1(\xi)\ge-\Gamma_1.
```

For a unit vector `v in T_N`, set

```math
\rho=\|B_\Omega v\|_2^2\le\lambda_N.
```

Then

```math
\begin{aligned}
q_1(v)
&=\int_{|\xi|\le\Omega}m_1(\xi)|\widehat v(\xi)|^2d\xi
 +\int_{|\xi|>\Omega}m_1(\xi)|\widehat v(\xi)|^2d\xi\\
&\ge -\Gamma_1\rho+c(1-\rho).
\end{aligned}
```

Therefore

```math
\boxed{
q_1(v)
\ge
\left[c-(c+\Gamma_1)\lambda_N\right]\|v\|_2^2.
}
```

In particular, tail positivity follows whenever

```math
\lambda_N<\frac{c}{c+\Gamma_1}.
```

This is an exact operator inequality, not a Galerkin heuristic.

---

## 8. Explicit PSWF eigenvalue bound and tail index `✓[K/M]`

Karnik--Romberg--Davenport, *Improved bounds for the eigenvalues of prolate spheroidal wave functions and discrete prolate spheroidal sequences* (arXiv:2006.00427v2), Corollary 3, gives for the continuous PSWF parameter `c>0`

```math
\widetilde\lambda_k(c)
\le
10\exp\left[
-\frac{k-\lceil2c/\pi\rceil-6}
{(2/\pi^2)\log(100c/\pi+25)}
\right]
```

for `k>=ceil(2c/pi)`.

Our interval has duration `T=2`; hence their parameter is

```math
c=\Omega T/2=2300.
```

The Arb gate certifies

```math
1464<\frac{2c}{\pi}<1465,
```

so

```math
\lceil2c/\pi\rceil=1465.
```

At

```text
k = 1490
```

it certifies the explicit KRD upper bound

```math
\boxed{
\lambda_{1490}(2300)<0.0035.
}
```

Combining this with Section 5 and the global lower bound gives

```math
\boxed{
q_1(v)>0.01\|v\|_2^2
\qquad(v\in\mathcal T_{1490}).
}
```

Thus the **entire infinite Prolate tail is rigorously coercive**.

---

## 9. Parity count

The symmetric PSWFs alternate parity, with `psi_0` even. Hence the first `1490` resolved modes split into

```text
745 even modes,
745 odd modes.
```

The tail theorem applies separately to both parity sectors.

This is compatible with the PR #112 completion reduction and its even/odd dual parameters.

---

## 10. What remains for A1-CERT

Let

```math
\mathscr H
=\mathcal R_{1490}\oplus\mathcal T_{1490}.
```

For the canonical completion

```math
A_1=q_1+\mathcal E^*\mathcal E,
```

write the block form

```math
A_1=
\begin{pmatrix}
A_{RR}&A_{RT}\\
A_{TR}&A_{TT}
\end{pmatrix}.
```

Because the completion term is positive,

```math
\boxed{
A_{TT}\succeq q_1|_{\mathcal T_{1490}}>0.01I.
}
```

Therefore an exact Schur-complement proof reduces to the finite resolved space:

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

A sufficient quantitative version is

```math
A_{RR}\succeq\mu_R I,
\qquad
\|A_{RT}\|^2\le0.01\mu_R.
```

The unresolved infinite-dimensional **tail coercivity itself is now closed**. The remaining open theorem is the resolved block plus a rigorous resolved--tail coupling estimate.

---

## 11. Relation to Chuk's compact-window program

Marcus Chuk, arXiv:2608.24827, gives the exact full-class symbol

```math
\Psi_L(t)
=\operatorname{Re}\psi(1/4+it/2)-\log\pi
-2\sum_{\log n<2L}\frac{\Lambda(n)}{\sqrt n}\cos(t\log n)
```

and certifies full Weil positivity at `L=0.8` by a different finite-reduction/envelope method.

The present A1-TAIL route does **not** claim to improve that theorem yet. Its new project-level role is different:

- it targets the null-pole/rank-2 completion at `a=1`;
- it derives an explicit high-frequency positive band directly from the exact multiplier;
- it uses non-asymptotic PSWF concentration to close the whole infinite tail;
- the remaining object is a finite resolved block plus coupling rather than an uncontrolled infinite complement.

---

## 12. Status

```text
exact a=1 whole-line Fourier multiplier                    ✓[M]
no extra window remainder in the quadratic form            ✓[M]
digamma finite-sum + integral-tail lower bound             ✓[M]
m_1(xi)>0.04 for |xi|>=2300                                ✓[K/M]
abstract Prolate-tail coercivity lemma                      ✓[M]
KRD lambda_1490(c=2300)<0.0035                              ✓[K/M]
q_1>0.01 on the full Prolate tail k>=1490                   ✓[K/M]
parity-compatible 1490-mode finite reduction                ✓[M]
resolved finite block at a=1                                ?[O]
resolved--tail coupling / final Schur complement            ?[O]
a=1 completion certificate                                 ?[O]
all-a NP-GAP / full positive Object X / RH                  ?[O]
```

Registry and Object-X working definition remain unchanged.

## 13. Firewalls

Do not claim:

- high-frequency multiplier positivity alone proves `a=1` NP-GAP;
- a positive resolved finite matrix alone is enough;
- the KRD eigenvalue estimate diagonalizes `q_1` in the PSWF basis;
- the resolved--tail crossblock has been bounded;
- fixed-window `a=1` positivity, all-window NP-GAP, Object X, or RH is proved.
