# P11 NP-DUAL-A1 — Morse-index filters, parity completion, and a=1 diagnostic

**Date:** 2026-09-13  
**Status:** theorem-level structural audit plus explicitly non-certified finite Galerkin diagnostics.  
**Parent main:** `56dbcd57adfd84fd0f7f7e7a65e3e40dfb1120b6` / PR #111.  
**Registry:** unchanged.  
**Object-X working definition:** unchanged.

---

## 1. Purpose

PR #111 recast fixed-window null-pole positivity as the completion problem

```math
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
\qquad
\mathcal Ev=(E_+(v),E_-(v))^T,
```

with

```math
D_{NP}(a)=\ker\mathcal E.
```

This audit adds four exact structural consequences and one non-certified stress test at `a=1`:

1. a Morse-index obstruction for arbitrary rank-2 completions;
2. a stronger Morse-index obstruction for the physical Weil pole matrix `P`;
3. reflection/parity reduction of the Hermitian completion from four real parameters to two;
4. the canonical scalar completion `lambda=1` identity;
5. a predeclared finite Dirichlet-Galerkin diagnostic at `a=1`.

The diagnostic does **not** certify the infinite-dimensional tail and therefore has no theorem or strict-numerical status.

---

## 2. Bibliographic erratum to the parent audit

Section 4 of `P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md` attributes arXiv:2608.24827v2 to **Xuefeng Zhu**.

That attribution is incorrect.

The correct paper is:

> **Marcus Chuk**, *Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*, arXiv:2608.24827.

The mathematical claims imported from that paper remain the same:

```text
full-class certificate at L=0.8: 8.9e-18
certified upper bound at L=2:     3.2e-283
Landau--Widom plunge law:         yes
doubly-exponential envelope barrier: yes
```

Thus this is a bibliographic correction, not a mathematical change.

Status:

```text
attribution to Xuefeng Zhu      ×[M]
correct attribution Marcus Chuk ✓[K/M]
```

The parent audit should be read with this erratum.

---

## 3. Morse index notation

Let `n_-(q_a)` denote the negative Morse index of the closed lower-bounded form `q_a`: the maximal dimension of a subspace on which `q_a` is strictly negative definite.

For a Hermitian matrix `H in M_2(C)`, the finite-rank correction

```math
\mathcal E^*H\mathcal E
```

has rank at most two. Its positive part has rank at most `n_+(H)<=2`.

---

## 4. General rank-2 completion obstruction `✓[M]`

### Theorem

If there exists a Hermitian `2x2` matrix `H` such that

```math
q_a+\mathcal E^*H\mathcal E\succeq0,
```

then

```math
\boxed{n_-(q_a)\le n_+(H)\le2.}
```

In particular, fixed-window NP-GAP implies the necessary condition

```math
\boxed{n_-(q_a)\le2.}
```

whenever it is realized by a fixed rank-2 completion.

### Proof

Assume `q_a` has a negative subspace `N` of dimension strictly larger than `n_+(H)`.

Write `H=H_+-H_-` with `H_\pm>=0`. Since

```math
\operatorname{rank}(\mathcal E^*H_+\mathcal E)
\le n_+(H),
```

there exists a nonzero `v in N` annihilated by the positive correction.

For such `v`,

```math
q_a(v)<0,
```

and

```math
\langle H\mathcal Ev,\mathcal Ev\rangle
=-\langle H_-\mathcal Ev,\mathcal Ev\rangle\le0.
```

Hence the completed form is negative on `v`, contradiction.

---

## 5. Stronger obstruction for the physical Weil pole block `✓[M]`

The actual Weil pole matrix is

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

Its eigenvalues are `+1` and `-1`, so

```math
n_+(P)=1.
```

Therefore

```math
Q_W^a=q_a+\mathcal E^*P\mathcal E\succeq0
```

implies

```math
\boxed{n_-(q_a)\le1.}
```

This yields two rigorous falsification gates:

```text
certified n_-(q_a) >= 3  => fixed-window NP-GAP impossible at that a
certified n_-(q_a) >= 2  => physical P-completion impossible at that a
```

The second statement does **not** rule out an arbitrary rank-2 completion.

---

## 6. Reflection symmetry and parity reduction `✓[M]`

Let

```math
(Jv)(x)=v(-x).
```

The centered COMMON-JUMP form is reflection invariant:

```math
q_a(Jv,Jw)=q_a(v,w).
```

The moment map transforms by the swap matrix

```math
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}=P,
```

because

```math
\mathcal E(Jv)=S\mathcal Ev.
```

Suppose a Hermitian completion `H` works:

```math
q_a+\mathcal E^*H\mathcal E\succeq0.
```

Applying the same inequality to `Jv` gives another valid completion `SHS`. Averaging preserves positivity, so

```math
H_{sym}:=\frac12(H+SHS)
```

also works.

Every Hermitian matrix commuting with `S` has the form

```math
\boxed{
H_{sym}=\begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix},
\qquad \alpha,\beta\in\mathbb R.
}
```

Thus an optimized completion needs only **two real parameters**, not four.

In the even/odd moment basis

```math
E_e=\frac{E_++E_-}{\sqrt2},
\qquad
E_o=\frac{E_+-E_-}{\sqrt2},
```

one has

```math
\boxed{H_{sym}\sim\operatorname{diag}(h_e,h_o).}
```

The actual Weil pole matrix becomes

```math
\boxed{P\sim\operatorname{diag}(+1,-1).}
```

A scalar completion `lambda I` becomes

```math
\operatorname{diag}(\lambda,\lambda).
```

This is the preferred dual parametrization for any future `a=1` certificate.

---

## 7. Parity consequences of physical Weil positivity `✓[M]`

For real or complex even `v`,

```math
E_+(v)=E_-(v).
```

For odd `v`,

```math
E_+(v)=-E_-(v).
```

Hence the pole block is positive on the even moment channel and negative on the odd moment channel.

If

```math
Q_W^a\succeq0,
```

then on the odd sector

```math
Q_W^a(v)=q_a(v)-2|E_+(v)|^2\ge0,
```

so

```math
\boxed{q_a(v)\ge2|E_+(v)|^2\ge0\qquad(v\text{ odd}).}
```

Therefore, under full fixed-window Weil positivity, every negative direction of `q_a` must lie in the **even** sector.

This refines the index obstruction:

```text
physical P-completion positive
=> q_a odd sector nonnegative
=> at most one negative direction, necessarily even
```

---

## 8. Canonical scalar completion `lambda=1` `✓[M]`

The scalar completion with `lambda=1` satisfies the exact identity

```math
\boxed{
q_a+\mathcal E^*\mathcal E
=Q_W^a+\mathcal E^*(I-P)\mathcal E.
}
```

Since

```math
I-P=\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\succeq0,
```

full Weil positivity implies

```math
\boxed{q_a+\mathcal E^*\mathcal E\succeq0.}
```

Thus `lambda=1` is a canonical sufficient completion under the stronger physical Weil inequality; it is not a fitted numerical parameter.

Parity makes the identity transparent:

- on the even sector, `E_+=E_-`, hence
  ```math
  q_a+\mathcal E^*\mathcal E=Q_W^a;
  ```
- on the odd sector, `E_+=-E_-`, and the scalar completion adds an extra positive penalty to the physical form.

This makes `lambda=1` the first predeclared completion candidate for the `a=1` stress test.

---

## 9. Predeclared non-certified `a=1` Galerkin diagnostic

### 9.1 Basis

Fix `a=1` and use the orthonormal Dirichlet basis

```math
\phi_n(x)=\sin\left(\frac{n\pi(x+1)}2\right),
\qquad -1<x<1,
\quad n=1,2,\ldots .
```

The subspaces are nested:

```math
V_N=\operatorname{span}\{\phi_1,\ldots,\phi_N\}.
```

Odd `n` are even about the origin; even `n` are odd about the origin.

### 9.2 Fourier multiplier

At `a=1`, the active Prime powers satisfy `log n<=2`, hence

```text
n = 2, 3, 4, 5, 7.
```

The centered non-pole multiplier used for the diagnostic is

```math
m_1(\xi)
=\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)
-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
```

The finite form matrix is sampled from

```math
(Q_N)_{jk}
=\frac1{2\pi}\int_{\mathbb R}
m_1(\xi)\widehat\phi_k(\xi)
\overline{\widehat\phi_j(\xi)}\,d\xi.
```

The two moment rows are

```math
(E_N)_{\pm,j}
=\int_{-1}^1\phi_j(x)e^{\pm x/2}dx.
```

### 9.3 Numerical method firewall

This exploratory calculation used ordinary floating-point quadrature and finite frequency cutoff. It did **not** include:

- Arb interval enclosure of every matrix element;
- a rigorous Fourier-tail bound;
- an infinite-dimensional operator tail bound;
- a certified Schur complement.

Therefore every number below is **diagnostic only** and gets no strict numerical status.

### 9.4 Null-pole Ritz minima

Let

```math
D_N=V_N\cap\ker E_N.
```

The observed smallest restricted Ritz values were approximately

```text
N=4    8.22e-4
N=6    6.21e-7
N=8    3.26e-9
N=10   2.70e-9
N=12   6.67e-11
```

They remain positive on these finite subspaces but decay rapidly toward zero.

As always,

```math
\lambda_N
=\inf_{0\ne v\in D_N}\frac{q_1(v)}{\|v\|^2}
\ge\lambda_{NP}(1).
```

Thus positive finite Ritz values do not prove the true gap.

### 9.5 Full `q_1` block and index diagnostic

For `N=12`, the finite `Q_N` block displayed one negative eigenvalue, approximately

```text
-4.15624,
```

with all other computed eigenvalues nonnegative at the working precision.

This is consistent with the necessary physical filter

```math
n_-(q_1)\le1,
```

but does not prove the infinite-dimensional index.

The negative finite direction lies in the even-parity block; the computed odd-parity block was nonnegative. This again matches the exact parity theorem above.

### 9.6 Scalar-completion diagnostic

For the same `N=12` block, the finite matrix

```math
Q_N+\lambda E_N^*E_N
```

crossed to numerical PSD at approximately

```text
lambda = 1.
```

At the predeclared canonical choice `lambda=1`, the smallest computed eigenvalue was of order

```text
1e-15,
```

while the null-pole restricted smallest Ritz value was of order `1e-11`.

This is a strong internal consistency check with Section 8, but **not** a certificate. In particular the tiny resolved-block margin makes a tail theorem the dominant obstacle.

---

## 10. Consequence for the `a=1` certificate program

The next theorem-level attempt should not optimize a large SDP. The dual space is already essentially solved:

```text
reflection-symmetric Hermitian completion -> 2 real parameters
strict existence theorem                  -> scalar lambda already sufficient
canonical first candidate                 -> lambda=1
```

The hard problem is entirely the unresolved infinite-dimensional tail.

A rigorous `a=1` certificate therefore needs:

1. a predeclared parity-adapted basis;
2. Arb enclosures for resolved form entries and moment rows;
3. a certified two-parameter completion, testing `lambda=1` first;
4. certified finite-block inertia / PSD;
5. a rigorous tail lower bound in both parity sectors;
6. a rigorous bound on resolved-tail coupling;
7. a final Schur-complement certificate.

Finite-block positivity without items 5--7 remains diagnostic.

---

## 11. Literature benchmark correction and target

The external benchmark arXiv:2608.24827 is by **Marcus Chuk**, not Xuefeng Zhu.

Its unconditional full-class certificate at `L=0.8` makes

```text
a=1.0
```

the first natural stress point for this project's completion method beyond that published lower-bound radius.

This project does **not** claim that the completion method has overcome the Landau--Widom / doubly-exponential tail barrier.

---

## 12. Status

```text
rank-2 completion framework                         ✓[M]
Morse filter: arbitrary completion => n_-(q_a)<=2  ✓[M]
Morse filter: physical P => n_-(q_a)<=1            ✓[M]
reflection-symmetrized 2-parameter completion       ✓[M]
physical positivity => q_a odd sector >=0          ✓[M]
canonical lambda=1 identity                         ✓[M]
a=1 finite Galerkin diagnostic                      non-certified
rigorous a=1 finite block                           ?[O]
rigorous a=1 tail / Schur complement                ?[O]
certified a=1 NP-DUAL completion                    ?[O]
all-a NP-GAP                                        ?[O]
forward Object-X architecture                       ✓[M]_part
full positive Object-X / RH                         ?[O]
```

---

## 13. Firewalls

Do not claim:

- the finite `a=1` Galerkin values certify positivity;
- one observed negative finite eigenvalue proves the exact Morse index;
- `lambda=1` finite-block positivity proves full-space positivity;
- the Marcus Chuk `L=0.8` result has been extended;
- the Landau--Widom barrier has been solved;
- fixed-window positivity is RH-equivalent;
- Object X or RH has been proved.
