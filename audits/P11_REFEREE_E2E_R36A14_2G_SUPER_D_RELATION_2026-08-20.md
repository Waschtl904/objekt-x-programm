# P11 End-to-End Referee R36-A14.2g — super-`d` relation survival and full sub-`b` strip

Date: 2026-08-20

## Purpose / firewall

This note audits the phase boundary

\[
R=d:=b-a,
\qquad
a:=\frac{\log2}{2},
\qquad
b:=\frac{\log3}{2},
\]

and then continues into `R>d` before booking anything.

The boundary cell collapse does not create a kernel.  More strongly, after the change of variables

\[
y=b-u
\]

one exact typed relation survives on the whole annulus for every

\[
d\le R<S<b.
\]

That relation gives a direct proof of kernel triviality throughout the entire super-`d`, sub-`b` region.

No global two-shift classification, no global typed-pseudogroup termination theorem, no R36-A, no R30-F, and no RH consequence is claimed.

Start head:

`b1b322ace330ec378925a1efcfb89c46988edbdb`

---

## 1. Setup

Work in the first genuine two-shift chamber

\[
b<T_0<2a=\log2.
\]

Only the shifts `a,b` are active.  The folded operator is

\[
(Lh)(u)=\sum_{\tau\in\{a,b\}}c_\tau\Bigl[
\operatorname{sgn}(u-\tau)\mathbf1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr],
\]

with

\[
c_2=\sqrt{\log2}\,2^{-3/4},
\qquad
c_3=\sqrt{\log3}\,3^{-3/4}.
\]

A14.2b already gives

\[
\left(\frac{c_2}{c_3}\right)^2\ne1,
\]

hence equivalently

\[
\left(\frac{c_3}{c_2}\right)^2\ne1.
\tag{A14.2g.1}
\]

Put

\[
c:=a+b,
\qquad
\ell:=\frac c2=\frac{a+b}{2}.
\]

---

## 2. The relation that survives the `R=d` collapse

Assume

\[
d\le R<S<b.
\tag{A14.2g.2}
\]

For every `y\in(R,S)` set

\[
u:=b-y.
\]

Then

\[
b-S<u<b-R\le b-d=a.
\]

Thus `u\in(0,T_0)` and `u<a` except possibly at the single endpoint `R=d`, `y=R`, which is irrelevant a.e.

At this `u`, the `b`-folded branch is exactly

\[
b-u=y.
\]

The `b`-forward branch is invisible because

\[
u+b>b>S.
\]

For the `a`-branches one has

\[
a-u=a-(b-y)=y-d,
\]

and

\[
u+a=a+b-y=c-y.
\]

Since `u<a` a.e., the `a`-folded sign is negative.  Therefore `Lh(u)=0` is exactly equivalent, for a.e. `y\in(R,S)`, to

\[
\boxed{
c_3h(y)
+c_2\mathbf1_{(R,S)}(y-d)h(y-d)
+c_2\mathbf1_{(R,S)}(c-y)h(c-y)=0.
}
\tag{A14.2g.3}
\]

This is the key phase-boundary statement.

It is not an untyped group identity.  It is obtained from one actual source interval

\[
(b-S,b-R)\subset(0,a]
\]

with all indicator domains retained exactly.

Status:

\[
\boxed{\text{super-`d` surviving typed relation (A14.2g.3)}\quad\checkmark[M].}
\]

---

## 3. Proposition R36-A14.2g — full super-`d`, sub-`b` kernel strip

### Proposition

Assume

\[
\boxed{
d\le R<S<b,
\qquad
b<T_0<2a.
}
\tag{A14.2g.4}
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A14.2g.5}
\]

### Proof

We use only (A14.2g.3), the strict downward shift `y\mapsto y-d`, and the reflection

\[
p(y):=c-y.
\]

The proof splits according to the position of `(R,S)` relative to the reflection center `\ell=c/2`.

---

### Case I: `S\le\ell`

For `y\in(R,S)` one has

\[
p(y)=c-y\ge c-S\ge S.
\]

Hence the reflection term in (A14.2g.3) is invisible a.e., and

\[
c_3h(y)+c_2\mathbf1_{(R,S)}(y-d)h(y-d)=0.
\tag{A14.2g.6}
\]

Partition `(R,S)` into the finite `d`-layers

\[
E_n:=\bigl(R+nd,\,\min\{S,R+(n+1)d\}\bigr),
\qquad n=0,1,2,\dots.
\]

On `E_0`, `y-d<R`, so (A14.2g.6) gives `h=0` a.e. on `E_0`.

Inductively, if all earlier layers vanish, then for `y\in E_n` the predecessor `y-d` is either outside `(R,S)` or lies in an already killed layer.  Thus (A14.2g.6) gives `h(y)=0`.

Hence

\[
h=0\quad\text{a.e. on }(R,S).
\]

---

### Case II: `R\ge\ell`

For `y\in(R,S)` one has

\[
p(y)=c-y\le c-R\le R.
\]

Again the reflection term is invisible a.e. and the same triangular recurrence (A14.2g.6) holds.

The identical finite `d`-layer induction gives

\[
h=0\quad\text{a.e. on }(R,S).
\]

---

### Case III: `R<\ell<S`

Set

\[
A:=c-S,
\qquad
B:=c-R.
\]

Then

\[
A<\ell<B,
\qquad
p(A)=S,
\qquad
p(R)=B.
\]

There are two typed subcases.

#### Case IIIa: `R\le A`

On the lower interval `(R,A)`,

\[
y<A=c-S
\quad\Longrightarrow\quad
p(y)=c-y>S,
\]

so the reflection branch is invisible.

Therefore the same downward recurrence (A14.2g.6) holds on `(R,A)`.  Finite `d`-layer induction gives

\[
\boxed{h=0\quad\text{a.e. on }(R,A).}
\tag{A14.2g.7}
\]

Now consider

\[
H:=(A,S).
\]

It is reflection invariant:

\[
p(H)=H,
\qquad p^2=\mathrm{id}.
\]

For `y\in H`,

\[
y-d<S-d<b-d=a.
\]

But because `S<b`,

\[
A=c-S=a+b-S>a.
\]

Hence

\[
y-d<A.
\]

Thus the predecessor `y-d` is either outside `(R,S)` or belongs to the already killed interval `(R,A)`.  Relation (A14.2g.3) therefore reduces on `H` to

\[
c_3h(y)+c_2h(p(y))=0.
\]

Equivalently,

\[
h(p(y))=-\frac{c_3}{c_2}h(y).
\]

Since `p` is a measure-preserving involution on `H` and (A14.2g.1) holds, the weighted-involution lemma yields

\[
\boxed{h=0\quad\text{a.e. on }H.}
\tag{A14.2g.8}
\]

Together with (A14.2g.7), this kills `(R,S)`.

#### Case IIIb: `R>A`

Since `S<b`,

\[
A=c-S>a.
\]

Thus `R>A` implies

\[
R>a.
\tag{A14.2g.9}
\]

Consequently

\[
S-R<b-a=d.
\]

Hence for every `y\in(R,S)`,

\[
y-d<R,
\]

so the downward-shift term in (A14.2g.3) is invisible on the whole annulus.

Because `R>A`,

\[
B=c-R<S.
\]

Since `R<\ell`, also `B>R`.  Therefore

\[
H:=(R,B)
\]

is a nonempty reflection-invariant interval:

\[
p(H)=H,
\qquad p^2=\mathrm{id}.
\]

On `H`, relation (A14.2g.3) reduces to

\[
c_3h(y)+c_2h(p(y))=0,
\]

so the weighted-involution lemma and (A14.2g.1) give

\[
h=0\quad\text{a.e. on }(R,B).
\tag{A14.2g.10}
\]

Finally, for `y\in(B,S)`,

\[
p(y)<R,
\]

and the downward predecessor is already invisible because `S-R<d`.  Thus (A14.2g.3) is one-term there:

\[
c_3h(y)=0.
\]

Hence

\[
h=0\quad\text{a.e. on }(B,S).
\tag{A14.2g.11}
\]

Combining (A14.2g.10) and (A14.2g.11) kills the whole annulus.

This completes all cases and proves (A14.2g.5).

Status:

\[
\boxed{\text{R36-A14.2g super-`d` full sub-`b` strip}\quad\checkmark[M].}
\]

---

## 4. What happens exactly at `R=d`

At `R=d`, the A14.2f source cell

\[
(a,b-R)
\]

collapses because

\[
b-R=b-d=a.
\]

That collapse removes one particular one-term chart, but it does not remove the information needed for injectivity.

The surviving relation (A14.2g.3) is valid up to the boundary because the source interval becomes

\[
(b-S,a),
\]

and the endpoint `u=a` is measure zero.

Thus

\[
\boxed{
R=d,
\quad
R<S<b,
\quad
b<T_0<2a
\Longrightarrow
\ker L=\{0\}.
}
\]

In fact A14.2g is stronger: no lower condition `S>(a+b)/2` is needed at the boundary.  Every

\[
d<S<b
\]

is covered.

This is the precise phase-boundary gain.

---

## 5. Relation-survival interpretation

The key simplification for `R\ge d` is geometric:

\[
b-R\le a.
\]

Therefore the complete source interval carrying the `b`-folded chart,

\[
(b-S,b-R),
\]

lies on one side of the fold point `a`.  The `a`-folded argument no longer changes formula or sign on that source interval; it is uniformly

\[
y-d.
\]

The entire family of cell decompositions for `R\ge d` is therefore encoded by the single typed recurrence (A14.2g.3).

This is stronger than a chamber-by-chamber proof.  It is an actual invariant relation across the cell-order changes.

Status:

\[
\boxed{
R=d\text{ is a cell-geometry phase boundary but not a kernel boundary}
\quad\checkmark[M]_{\rm neg}.
}
\]

---

## 6. Consequences for the current two-shift map

A14.2f proves kernel triviality for

\[
0<R<d,
\qquad
\max\left\{\frac{a+b}{2},2a-d-R\right\}<S<b.
\]

A14.2g now proves kernel triviality for the entire region

\[
d\le R<S<b.
\]

Thus the remaining unknown portion of the first two-shift chamber with `S<b` is confined to the small-`R` region

\[
0<R<d,
\qquad
R<S\le
\max\left\{\frac{a+b}{2},2a-d-R\right\},
\]

subject of course to `S<b`.

No claim is made here that this remaining region contains nontrivial kernels.  It is merely not covered by A14.2f/A14.2g.

The full two-shift classification remains

\[
\boxed{?[O].}
\]

---

## 7. Audit ledger

| Claim | Status |
|---|---|
| Exact surviving relation (A14.2g.3) for `d<=R<S<b` | `✓[M]` |
| `R=d` boundary kernel triviality for every `d<S<b` | `✓[M]` |
| Full region `d<=R<S<b`, `b<T0<2a` has trivial kernel | `✓[M]` |
| `R=d` is a genuine kernel boundary | `×[M]` |
| `R=d` is a cell-geometry phase boundary | `✓[M]` |
| Relation survival removes chamber-by-chamber analysis for `R>=d` | `✓[M]` |
| Full two-shift parameter classification | `?[O]` |
| Global typed-pseudogroup termination | `?[O]` |
| R36-A | `?[O]` |
| R30-F | `?[O]` |

---

## 8. Next admissible target

The next useful question is no longer `R>d`.

A14.2g has closed that entire sub-`b` side.

The unresolved region lies below the A14.2f lower envelope for `0<R<d`.  A productive next step is therefore to test whether relation-based triangularization can be constructed on the `R<d` side despite the fold crossing `u=a`.

Any further booking should require either

1. a genuine enlargement of the covered `(R,S)` region, or
2. a relation-survival theorem that compresses several existing A14 cases.
