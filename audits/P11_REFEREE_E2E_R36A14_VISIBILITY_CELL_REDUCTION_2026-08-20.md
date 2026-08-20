# P11 End-to-End Referee R36-A14 — finite visibility-cell reduction

Date: 2026-08-20

## Purpose and firewall

This note starts the A14 multi-shift analysis from the canonical folded odd-sector operator of
R36-A9/A10.  Its purpose is reduction only: make the visibility geometry finite and typed before
any determinant, orbit-rank, or kernel-classification claim is attempted.

It does **not** prove two-shift kernel triviality, full R36-A, R30-F, terminal transport,
polar gauge, Object X, or RH.

Canonical source formula (R36-A9/A13): for `0<u<T_0`,

\[
(L_{R,S,T_0}h)(u)
=\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[
\operatorname{sgn}(u-\tau_{p,k})\mathbf1_{(R,S)}(|u-\tau_{p,k}|)
 h(|u-\tau_{p,k}|)
-\mathbf1_{(R,S)}(u+\tau_{p,k})h(u+\tau_{p,k})
\Bigr],
\]

with

\[
\boxed{\tau_{p,k}=\frac{k\log p}{2}},
\qquad
\boxed{c_{p,k}=\sqrt{\log p}\,p^{-3k/4}}.
\]

The off-support formula O3AE.2 is **not** used as the A14 visibility source: O3AE.2 assumes a
source supported in `[-R,R]`, whereas here `E_Ah` is supported on the annulus
`A=(-S,-R)\cup(R,S)`.

---

## 1. A14.1 — finite visibility-cell reduction

Let the active shift set at fixed `T_0` be

\[
\Theta(T_0)=\{\tau_1,\dots,\tau_n\}.
\]

For a fixed active shift `\tau`, the folded term can change its visibility or affine form only
when one of the following events occurs:

\[
|u-\tau|=R,\qquad |u-\tau|=S,\qquad u=\tau,
\qquad u+\tau=R,\qquad u+\tau=S.
\]

Thus a complete candidate breakpoint set for that shift is

\[
\boxed{
\mathcal B_\tau
=\{\tau-R,\tau+R,\tau-S,\tau+S,\tau,R-\tau,S-\tau\}.
}
\tag{A14.1}
\]

Intersect

\[
\mathcal B
=\{0,T_0\}\cup\bigcup_{\tau\in\Theta(T_0)}\mathcal B_\tau
\]

with `[0,T_0]`, remove repetitions, and sort the remaining numbers.  The connected components
of `(0,T_0)\setminus\mathcal B` will be called **visibility cells**.

### Proposition R36-A14.1 (constant branch signature on each visibility cell)

On every visibility cell `C`, for every active shift `\tau`,

1. the sign of `u-\tau` is constant;
2. the truth values of
   `R<|u-\tau|<S` and `R<u+\tau<S` are constant;
3. every visible argument is affine in `u`, of one of the forms

\[
\tau-u,\qquad u-\tau,\qquad u+\tau.
\]

Consequently, on `C`, the equation `Lh=0` has a fixed finite affine-functional form

\[
\boxed{
\sum_{j=1}^{m_C} a_j\,h(\alpha_j u+\beta_j)=0,
\qquad u\in C,
}
\tag{A14.2}
\]

where

\[
1\le m_C\le 2n,
\qquad
\alpha_j\in\{-1,+1\},
\qquad
a_j\in\{\pm c_{p,k}\}.
\]

If no branch is visible on a cell, the equation there is identically zero and the cell can be
discarded.

### Proof

The indicator `1_(R,S)(|u-\tau|)` can change only at
`u=\tau\pm R` or `u=\tau\pm S`; the sign can change only at `u=\tau`.
The indicator `1_(R,S)(u+\tau)` can change only at `u=R-\tau` or `u=S-\tau`.
By construction no such point lies in the interior of a visibility cell.  Hence all branch
signatures are constant there.  Resolving `|u-\tau|` with the constant sign of `u-\tau` gives
one of the three displayed affine arguments.  Summing the visible terms gives (A14.2).
`\square`

Status:

\[
\boxed{\text{R36-A14.1}\quad\checkmark[M].}
\]

### Corollary R36-A14.1a (linear cell-count bound)

Each active shift contributes at most seven candidate breakpoints.  Therefore, with `n` active
shifts, there are at most `7n` interior breakpoints and hence at most

\[
\boxed{7n+1}
\tag{A14.3}
\]

visibility cells.

This is only a cell-count bound.  It does **not** bound the number of affine orbit values after
propagating relations across cells.

Status:

\[
\boxed{\text{R36-A14.1a}\quad\checkmark[M].}
\]

---

## 2. A14.1b — overlap of a shift is never isolated in the concrete P11 active set

For a fixed shift `\tau=\tau_{p,k}`, the one-shift plus/folded image overlap discussed in the
A13 scope note can occur only if

\[
S-R>2\tau.
\]

But

\[
\boxed{2\tau_{p,k}=\tau_{p,2k}.}
\tag{A14.4}
\]

Hence

\[
S-R>2\tau_{p,k}
\Longrightarrow
S>2\tau_{p,k}
\Longrightarrow
T_0>2\tau_{p,k}=\tau_{p,2k}.
\]

Therefore the doubled prime-power shift is already active whenever the original shift enters
its overlap regime.

### Proposition R36-A14.1b (no isolated one-shift overlap in P11)

\[
\boxed{
\text{A geometric overlap regime for }\tau_{p,k}\text{ cannot occur while }
\tau_{p,k}\text{ is the only active shift.}
}
\tag{A14.5}
\]

The proof does not require `R>0`; `R\ge0` is enough for the displayed implication.

Status:

\[
\boxed{\text{R36-A14.1b}\quad\checkmark[M].}
\]

This explains structurally why the A13 no-overlap theorem exhausts the genuine one-shift P11
regime: overlap and multi-shift coupling arrive together.

---

## 3. Two distinct spacings in the first genuine two-shift chamber

Write

\[
\tau_2:=\tau_{2,1}=\frac{\log2}{2},
\qquad
\tau_3:=\tau_{3,1}=\frac{\log3}{2}.
\]

The first genuine two-shift terminal chamber is

\[
\boxed{
\tau_3\le T_0<\tau_{2,2}=\log2.
}
\tag{A14.6}
\]

Indeed `p^k<4` leaves exactly the prime powers `2` and `3` in the active set.

Two different spacings must not be conflated:

\[
\boxed{
d:=\tau_3-\tau_2
=\frac12\log\frac32
\approx0.2027325541,
}
\tag{A14.7}
\]

which is the direct separation of the two shift centres, and

\[
\boxed{
\delta:=2(\tau_3-\tau_2)
=\log\frac32
\approx0.4054651081,
}
\tag{A14.8}
\]

which is the translation generated by the composition of the two reflections

\[
\sigma_{\tau_3}\sigma_{\tau_2}(x)=x+\delta,
\qquad
\sigma_\tau(x)=2\tau-x.
\]

Status:

\[
\boxed{\text{notation / reflection composition}\quad\checkmark[M].}
\]

No global orbit-size bound is booked here.  In particular, the earlier working number `<=8`
remains a heuristic work bound until the affine-incidence closure is written down.

---

## 4. A14.1c — the full four-branch cell is uniformly narrow

In the two-shift chamber, a cell on which all four branches

\[
\tau_2-u,\quad \tau_2+u,\quad \tau_3-u,\quad \tau_3+u
\]

are simultaneously visible must satisfy, necessarily,

\[
u+\tau_3<S.
\]

Therefore

\[
u<S-\tau_3<T_0-\tau_3<\log2-\frac{\log3}{2}.
\]

Numerically,

\[
\boxed{
\log2-\frac{\log3}{2}
\approx0.1438410362.
}
\tag{A14.9}
\]

More precisely, if `R<\tau_2<\tau_3<S`, then the positive full-four-branch cell is exactly
bounded by

\[
\boxed{
0<u<\min\{S-\tau_3,\ \tau_2-R\}.
}
\tag{A14.10}
\]

### Proposition R36-A14.1c (four-branch window bound)

Every full four-branch visibility cell in the first genuine two-shift chamber has length
strictly less than

\[
\boxed{0.1438410363}.
\]

Status:

\[
\boxed{\text{R36-A14.1c}\quad\checkmark[M].}
\]

### Firewall

This does **not** imply that only four-branch cells are mathematically new.  Three-branch cells
can already permit cross-shift compensation.  For example, with

\[
R=0.10,\qquad S=0.50,
\]

at `u=0.10` one obtains a three-term relation of the form

\[
-c_2h(\tau_2-u)-c_2h(\tau_2+u)-c_3h(\tau_3-u)=0,
\]

while the `\tau_3+u` branch is outside `(R,S)`.

Hence the statements

> only the cell with both shifts fully inside is genuinely new,

and

> a one-sided second shift automatically increases rigidity,

are **not** valid general reductions.

---

## 5. Weight diagnostics

For the first shifts,

\[
c_{2,1}\approx0.4950399336,
\qquad
c_{3,1}\approx0.4598130419,
\qquad
\frac{c_{2,1}}{c_{3,1}}\approx1.076608\,.
\]

Thus the first two weights differ by only about `7.7%`; no dominance argument is justified by
this numerical margin alone.

Moreover

\[
c_{5,1}\approx0.3794107314
>c_{2,2}\approx0.2943525056,
\]

although

\[
\tau_{5,1}>\tau_{2,2}.
\]

Therefore the weight sequence is not monotone as a function of shift size.  Any future uniform
argument that assumes weights decrease with `\tau` is invalid.

Status:

\[
\boxed{\text{monotonicity-in-}\tau\text{ diagnostic}\quad\checkmark[M]_{\rm neg}.}
\]

---

## 6. Conditional involution lemma

The following elementary mechanism is mathematically exact, but its occurrence in the concrete
A14 cell-incidence graph remains open.

### Lemma R36-A14.1d (weighted involution kill)

Let `I` be a measurable set, let `\sigma:I\to I` satisfy `\sigma^2=\mathrm{id}` a.e., and let
`a,b>0`.  If

\[
h(\sigma(s))=-\frac{a}{b}h(s)
\quad\text{for a.e. }s\in I,
\]

then

\[
\left(1-\frac{a^2}{b^2}\right)h(s)=0
\quad\text{a.e. on }I.
\]

Hence, if `a\ne b`,

\[
\boxed{h=0\quad\text{a.e. on }I.}
\tag{A14.11}
\]

Proof: apply the relation a second time and use `\sigma^2=\mathrm{id}`.
`\square`

Status:

\[
\boxed{\text{R36-A14.1d}\quad\checkmark[M].}
\]

For prime-power weights, equality of two weights is equivalent to

\[
\sqrt{\log p}\,p^{-3k/4}
=\sqrt{\log q}\,q^{-3l/4},
\]

or, after squaring and taking logarithms,

\[
\boxed{
\log\log p-\frac32k\log p
=
\log\log q-\frac32l\log q.
}
\tag{A14.12}
\]

For a fixed pair this equality/non-equality can be certified numerically.  A uniform theorem
excluding all degeneracies is a separate arithmetic problem and is **not** claimed here.

---

## 7. What is still open: A14.2

The visibility-cell theorem does not yet produce a finite scalar matrix.  The unknowns in
(A14.2) are still values of an `L^2` function at affine arguments.  Relations from neighbouring
cells must be propagated through their common affine images before one obtains finite orbit or
incidence components.

Define the next node:

\[
\boxed{\text{R36-A14.2 — affine incidence / orbit closure}.}
\]

Target: construct the finite incidence graph generated by the affine branch maps on each
visibility cell, propagate one-term killed zones, and determine which components remain free of
killing constraints.

Only after A14.2 is closed is a determinant/rank calculation logically justified.

Status:

\[
\boxed{\text{R36-A14.2}\quad?[O].}
\]

The concrete hand-worked point

\[
(R,S,T_0)=(0.10,0.50,0.56)
\]

is reserved as a regression target for A14.2.  No theorem `\ker L=\{0\}` for this point is
booked in this note; it must be independently reproduced from the canonical cell-incidence
construction before promotion.

---

## 8. Program-level status firewall

This note changes only the local A14 reduction status:

- R36-A14.1 finite visibility-cell reduction: `checkmark[M]`;
- R36-A14.1a linear cell-count bound `<=7n+1`: `checkmark[M]`;
- R36-A14.1b no isolated one-shift overlap: `checkmark[M]`;
- R36-A14.1c full four-branch window `<0.1438410363`: `checkmark[M]`;
- R36-A14.1d conditional weighted-involution kill: `checkmark[M]`;
- global affine-orbit bound such as `<=8`: not booked, `?[O]`;
- two-shift kernel classification: `?[O]`;
- full R36-A: `?[O]`;
- R30-F: `?[O]`.

A13c remains unchanged: the odd-annihilator route in the first terminal chamber is classified,
and its positive region proves a genuine mismatch, but the universal first-chamber mismatch
statement is not claimed.
