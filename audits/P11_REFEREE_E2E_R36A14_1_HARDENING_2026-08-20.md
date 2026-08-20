# P11 End-to-End Referee R36-A14.1 — hardening addendum

Date: 2026-08-20

## Purpose and firewall

This note hardens the already-canonical A14.1 visibility-cell reduction in
`P11_REFEREE_E2E_R36A14_VISIBILITY_CELL_REDUCTION_2026-08-20.md`.
It changes no R30-F, R36-A, A13, or A13c status and makes no two-shift kernel-classification claim.

The canonical folded operator remains

\[
(Lh)(u)=\sum_{\tau}c_\tau\Bigl[
\operatorname{sgn}(u-\tau)\mathbf 1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf 1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr].
\]

---

## A14.1a' — sharper visibility-cell count

For one active shift `tau`, the A14.1 candidate breakpoints are

\[
\tau-R,\ \tau+R,\ \tau-S,\ \tau+S,\ \tau,\ R-\tau,\ S-\tau.
\]

After restriction to the positive `u`-axis, the pairs

\[
\tau-R,\ R-\tau
\qquad\text{and}\qquad
\tau-S,\ S-\tau
\]

contribute at most one positive number each.  Hence the positive candidate set is contained in

\[
\boxed{\{\tau,\ \tau+R,\ \tau+S,\ |\tau-R|,\ |\tau-S|\}.}
\]

Thus each active shift contributes at most five positive breakpoints.  With `n` active shifts,
after removing repetitions and intersecting with `(0,T_0)`, there are at most `5n` interior
breakpoints and therefore at most

\[
\boxed{N_{\rm cells}\le 5n+1.}
\tag{A14.H1}
\]

Status:

\[
\boxed{\text{R36-A14.1a'}\quad\checkmark[M].}
\]

The older bound `7n+1` remains true but is superseded by (A14.H1) as the canonical working bound.
No stronger general bound such as `3n+1` is booked here.  In the two-shift regime with
`R<tau_2<tau_3<S`, the positive breakpoints `tau`, `tau+R`, `tau-R`, and `S-tau` can all remain
relevant while `tau+S` lies beyond `T_0`, so a blanket `3n+1` claim would require additional
case restrictions.

---

## A14.1c' — completion of the full-four-branch proof

Work in the first genuine two-shift chamber

\[
\tau_3\le T_0<\log2=2\tau_2,
\qquad
\tau_2=\frac{\log2}{2},\quad
\tau_3=\frac{\log3}{2}.
\]

Suppose all four branches associated with `tau_2,tau_3` are simultaneously visible at a positive
`u`.  We first show that necessarily `u<tau_2`.

If `u>tau_2`, visibility of the folded `tau_2` branch requires

\[
R<u-\tau_2,
\]

hence `u>tau_2+R>tau_2`.  Visibility of the forward `tau_3` branch requires

\[
u+\tau_3<S,
\]

so

\[
u<S-\tau_3<T_0-\tau_3<\log2-\frac{\log3}{2}\approx0.1438410362.
\]

But `tau_2+R>tau_2\approx0.3465735903`, a contradiction.  The case `u=tau_2` is a breakpoint and
not in an open visibility cell.  Therefore every full-four-branch cell lies in `0<u<tau_2`.

There the folded arguments are `tau_2-u` and `tau_3-u`.  If

\[
R<\tau_2<\tau_3<S,
\]

simultaneous visibility is therefore exactly constrained by

\[
\boxed{0<u<\min\{S-\tau_3,\ \tau_2-R\}.}
\tag{A14.H2}
\]

In particular every full-four-branch cell has length strictly less than

\[
\log2-\frac{\log3}{2}\approx0.1438410362.
\]

Status:

\[
\boxed{\text{R36-A14.1c' completeness hardening}\quad\checkmark[M].}
\]

This completes the regime split underlying the already-booked A14.1c conclusion; no status change
is required.

---

## A14.1d' — typed weighted involution / cycle lemma

The useful abstract statement is best written in multiplier form so that signs from
`sgn(u-tau)` are included.

### Lemma R36-A14.1d' (weighted involution kill)

Let `E` be a measurable set and let `sigma:E->E` be a measure-preserving involution,
`sigma^2=id` a.e.  Let `lambda` be a nonzero scalar.  If

\[
h(\sigma(s))=\lambda h(s)
\quad\text{for a.e. }s\in E,
\]

then

\[
(1-\lambda^2)h(s)=0
\quad\text{for a.e. }s\in E.
\]

Hence

\[
\boxed{\lambda^2\ne1\Longrightarrow h=0\text{ a.e. on }E.}
\tag{A14.H3}
\]

Proof: because `sigma` preserves null sets and maps `E` to itself, the relation may be applied at
`sigma(s)` for a.e. `s`; then

\[
h(s)=h(\sigma^2(s))=\lambda h(\sigma(s))=\lambda^2h(s).
\]

`\square`

For a relation written as

\[
h(\sigma(s))=-\frac ab h(s),
\]

the exact nondegeneracy condition is

\[
\boxed{a^2\ne b^2,}
\]

which reduces to `a!=b` only when `a,b>0` are known positive weights.

Status:

\[
\boxed{\text{R36-A14.1d'}\quad\checkmark[M].}
\]

### Lemma R36-A14.1e (weighted cycle kill)

More generally, let `sigma_1,...,sigma_m` be measurable nonsingular maps along a common invariant
component, and suppose successive relations multiply a value by scalars `lambda_1,...,lambda_m`.
If the composed chart map returns to the identity a.e. on a measurable set `E`, while

\[
\Lambda:=\prod_{j=1}^m\lambda_j\ne1,
\]

then

\[
\boxed{h=0\text{ a.e. on }E.}
\tag{A14.H4}
\]

This is the general weighted-cycle mechanism; the involution lemma is the two-step case.

Status:

\[
\boxed{\text{R36-A14.1e}\quad\checkmark[M].}
\]

The occurrence of such a closed weighted cycle in the concrete P11 incidence graph is **not**
asserted here; that remains part of A14.2.

---

## Status firewall

- A14.1 visibility-cell reduction: `checkmark[M]` unchanged.
- Canonical cell-count bound sharpened to `<=5n+1`: `checkmark[M]`.
- A14.1c four-branch-window conclusion: `checkmark[M]`, proof now explicitly covers/excludes
  `u>=tau_2`.
- Weighted involution/cycle lemmas: `checkmark[M]` as abstract typed lemmas.
- Realisation of an invariant involution or nontrivial weighted cycle in the concrete A14 graph:
  `?[O]`.
- Two-shift kernel classification: `?[O]`.
- Full R36-A and R30-F: `?[O]`.
