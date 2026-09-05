# P11 / R43 — step-floor comparable-chain extension

**Date:** 2026-09-05  
**Scope:** extend the exact floor-saturating dynamics from `P11_R43_COND_ROUND2_REVIEW_AND_STEP_FLOOR_DYNAMICS_2026-09-05.md` to every two-sided floor-comparable terminal chain.  
**Status:** theorem-level quantitative extension for the epsilon-front bookkeeping only. No PSD existence, structured-vector, B-METINC-COND, Strong-Terminal/C6, Object-X or RH promotion.

## 1. Assumption

Let `0<c<=C<infinity`. Suppose a terminal chain satisfies, for all sufficiently large `j`,

\[
\boxed{
c e^{-4U_j}
\le h_j:=U_{j+1}-U_j
\le C e^{-4U_j}.
}
\tag{FC1}
\]

Set

\[
x_j:=e^{4U_j}.
\]

Then

\[
x_{j+1}-x_j
=x_j\left(e^{4h_j}-1\right).
\tag{FC2}
\]

## 2. Linear growth of `x_j`

Using `e^t-1>=t` for `t>=0` and the lower bound in (FC1),

\[
x_{j+1}-x_j
\ge 4x_jh_j
\ge 4c.
\tag{FC3}
\]

Hence `x_j->infinity`, so `h_j<=C/x_j->0`. For all sufficiently large `j`, `4h_j<=1`, and then `e^{4h_j}-1<=8h_j`. Therefore

\[
x_{j+1}-x_j
\le 8x_jh_j
\le 8C.
\tag{FC4}
\]

Thus there are positive constants `A,B` such that

\[
\boxed{Aj\le x_j\le Bj}
\tag{FC5}
\]

for all sufficiently large `j`. Equivalently,

\[
\boxed{
e^{4U_j}=\Theta(j),
\qquad
e^{-4U_j}=\Theta(1/j),
\qquad
h_j=\Theta(1/j).
}
\tag{FC6}
\]

This extension requires the **two-sided** comparability (FC1). The one-sided PSD necessary floor `h_j>=c e^{-4U_j}` alone does not imply the upper bound in (FC6).

## 3. Harmonic firewall on every comparable chain

Let `delta_j>=0`. If for some `kappa>0`, eventually

\[
\delta_j\ge\kappa e^{-4U_j},
\tag{FC7}
\]

then (FC6) gives `delta_j>=kappa'/j` for some `kappa'>0`, so

\[
\boxed{\sum_j\delta_j=\infty.}
\tag{FC8}
\]

Thus any epsilon defect that remains of the same order from below as the `e^{-4U}` floor cannot be absolutely summable on a two-sided floor-comparable chain.

Conversely, for any `eta>0`,

\[
\delta_j\le D e^{-(4+\eta)U_j}
\tag{FC9}
\]

implies by (FC6)

\[
\delta_j=O\left(j^{-1-\eta/4}\right),
\]

hence

\[
\boxed{\sum_j\delta_j<\infty.}
\tag{FC10}
\]

## 4. Booking and firewall

Book the scope extension as

```text
R43-COND-EPSILON-FLOOR-COMPARABLE-CHAIN-FIREWALL ✓[M]
```

Read together with

```text
R43-COND-STEP-FLOOR-NONOBSTRUCTION               ✓[M]
R43-COND-EPSILON-FLOOR-HARMONIC-FIREWALL         ✓[M]
```

No unconditional `delta_j=o(1/j)` theorem is booked. The one-sided PSD step floor alone does not force a floor-comparable chain and therefore does not by itself impose harmonic density on every possible partition.