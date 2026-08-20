# P11 End-to-End Referee R36-A14.2f — unified sub-b two-shift strip

Date: 2026-08-20

## Purpose / firewall

This note audits the two apparent A14.2e flank barriers

\[
S=2d+R,
\qquad
S=2a-R,
\]

where

\[
a:=\tau_2=\frac{\log2}{2},
\qquad
b:=\tau_3=\frac{\log3}{2},
\qquad
d:=b-a=\frac12\log\frac32.
\]

The conclusion is that neither flank is a genuine kernel boundary.  A single larger sufficient region crosses both of them and also reaches into the small-`R` `q`-regime.

No global two-shift classification, no global typed-pseudogroup termination theorem, no R36-A, no R30-F, and no RH consequence is claimed.

Start head:

`2727d49531f659344aed0847d29010b1f5825b7e`

---

## 1. Setup

Work in the first genuine two-shift chamber

\[
b<T_0<2a=\log2.
\]

Only the two shifts `a,b` are active.  The folded operator is

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

A14.2b already proves

\[
\left(\frac{c_2}{c_3}\right)^2\ne1.
\]

Put

\[
L_*:=\frac{a+b}{2}
\]

and

\[
M(R):=\max\{L_*,\,2a-d-R\}.
\]

Numerically,

\[
a\approx0.346573590280,
\quad
b\approx0.549306144334,
\quad
d\approx0.202732554054,
\quad
L_*\approx0.447939867307.
\]

The two lower bounds cross at

\[
R_*=2a-d-L_*=\frac{5a-3b}{2}\approx0.042474759199.
\]

Since

\[
5a>3b
\iff
2^5>3^3
\iff
32>27,
\]

we have `R_*>0`.  Hence for every `R>=R_*`, the lower condition `S>M(R)` is simply `S>L_*`.

Two elementary inequalities will be used repeatedly:

\[
L_*>2d
\iff
5a>3b
\iff
32>27,
\tag{A14.2f.1}
\]

and

\[
2d>a
\iff
2b>3a
\iff
3>2\sqrt2.
\tag{A14.2f.2}
\]

---

## 2. Main theorem

### Proposition R36-A14.2f — unified sub-`b` strip

Assume

\[
\boxed{
0<R<d,
\qquad
M(R)<S<b,
\qquad
b<T_0<2a.
}
\tag{A14.2f.3}
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A14.2f.4}
\]

The proof is split only according to the actual cell-order changes.  The old A14.2e flanks are not kernel barriers.

---

## 3. Case I: `0<R<d/2` — `q`-kill plus propagation

Because `2R<d`, the middle cell

\[
u\in(a+R,b-R)
\]

is nonempty.  On it both forward branches are invisible and the exact equation is

\[
c_2h(u-a)-c_3h(b-u)=0.
\]

Set

\[
x:=u-a\in(R,d-R),
\qquad
q(x):=d-x=b-u.
\]

Then

\[
h(q(x))=\frac{c_2}{c_3}h(x),
\qquad
q^2=\mathrm{id},
\qquad
q(R,d-R)=(R,d-R).
\]

The weighted-involution lemma gives

\[
h=0\quad\text{a.e. on }(R,d-R).
\tag{A14.2f.5}
\]

The adjacent one-term cells give the rest of the central block.  On

\[
u\in(a-R,a)
\]

only the `b` folded branch survives and its image is `(d,d+R)`.  On

\[
u\in(a,a+R)
\]

only the `b` folded branch survives and its image is `(d-R,d)`.

Indeed `a`-folded arguments are below `R`; all forward branches are above `S`; and `b<2a-R` here because `R<d/2` and (A14.2f.1).

Thus

\[
\boxed{h=0\quad\text{a.e. on }K:=(R,d+R).}
\tag{A14.2f.6}
\]

Now use the two-term cell

\[
u\in(S-a,a-R).
\]

It is nonempty because `S<b<2a-R`.  Its exact equation is

\[
-c_2h(a-u)-c_3h(b-u)=0.
\tag{A14.2f.7}
\]

The first image is

\[
a-u\in(R,2a-S).
\]

By `S>2a-d-R`, which is part of `S>M(R)`, we have

\[
2a-S<d+R.
\]

Hence the first image lies inside `K`, so (A14.2f.7) kills the second image

\[
b-u\in(d+R,a+b-S).
\]

Therefore

\[
\boxed{h=0\quad\text{a.e. on }(R,A),
\qquad A:=a+b-S.}
\tag{A14.2f.8}
\]

Finally take

\[
u\in(b-S,S-a),
\]

which is nonempty because `S>L_*`.  The exact equation is

\[
-c_2h(a-u)-c_2h(a+u)-c_3h(b-u)=0.
\tag{A14.2f.9}
\]

Its low image is

\[
a-u\in(2a-S,S-d).
\]

This lies inside `(R,A)`: the lower endpoint exceeds `R` because `S<2a-R`, and the upper endpoint is below `A` because

\[
S-d<A
\iff
S<b.
\]

Thus (A14.2f.9) reduces to

\[
c_2h(z)+c_3h(p_2(z))=0,
\qquad
z:=a+u\in H:=(A,S),
\]

where

\[
p_2(z):=a+b-z.
\]

Since

\[
p_2(H)=H,
\qquad
p_2^2=\mathrm{id},
\]

and `(c_2/c_3)^2!=1`, the weighted-involution lemma gives

\[
h=0\quad\text{a.e. on }H=(A,S).
\tag{A14.2f.10}
\]

Together with (A14.2f.8), this proves `h=0` a.e. on `(R,S)`.

---

## 4. Case II: `R=d/2`

The `q`-interval collapses to measure zero, but the two adjacent one-term cells now meet exactly.

On `(a-R,a)` the `b` folded image is `(d,d+R)`; on `(a,b-R)` the `b` folded image is `(R,d)`.  Hence again

\[
h=0\quad\text{a.e. on }(R,d+R).
\]

By (A14.2f.2), `L_*>2a-d-R` at `R=d/2`, so `S>M(R)` implies the same strict containment used in Case I.  The remaining propagation and `p_2`-kill are therefore identical.

Thus (A14.2f.4) also holds at `R=d/2`.

---

## 5. Case III: `d/2<R<d` and `S<2a-R`

Here the `q`-cell is absent.  Because `R>d/2`,

\[
d-R<R.
\]

On

\[
u\in(a-R,a)
\]

only the `b` folded branch survives.  Its image is `(d,d+R)`.  The `a` forward branch is invisible because `S<2a-R`.

On

\[
u\in(a,b-R)
\]

the `a` folded branch lies in `(0,d-R)\subset(0,R)`, so again only the `b` folded branch survives, with image `(R,d)`.

Therefore

\[
\boxed{h=0\quad\text{a.e. on }K:=(R,d+R).}
\tag{A14.2f.11}
\]

The cell `(S-a,a-R)` has the same equation (A14.2f.7).  The hypothesis `S>M(R)` again gives

\[
2a-S<d+R,
\]

so its first image lies in `K` and its second image `(d+R,A)` is killed.  Hence

\[
h=0\quad\text{a.e. on }(R,A).
\tag{A14.2f.12}
\]

The three-term cell `(b-S,S-a)` then has its low image inside `(R,A)` exactly as in Case I, because `S<2a-R` and `S<b`.  It reduces to the invariant `p_2` relation on `H=(A,S)` and kills `H`.

Thus `h=0` a.e. on `(R,S)`.

### Consequence for the old left flank

When `R<2a-b`, A14.2e imposed `S<2d+R`.  No such upper bound appears here.  In particular there is an open set with

\[
S>2d+R
\]

and still `ker L=0`.  Therefore the left A14.2e flank is a proof-order boundary, not a kernel boundary.

Status:

\[
\boxed{\text{left A14.2e flank sharpness}\quad\checkmark[M]_{\rm neg}.}
\]

---

## 6. Case IV: `d/2<R<d` and `S>2a-R`

This is the cell-order change that the conservative helper does not close automatically because two surviving chart images are no longer identical on a single cell.

Put

\[
A:=a+b-S,
\qquad
B:=2a-R,
\qquad
C:=d+R.
\]

Because `S>2a-R`, we have

\[
A<C,
\qquad
B<S.
\tag{A14.2f.13}
\]

Because `S>L_*`, we have `A<S`.  Because `S<b`, we have `A>a>d>R`.

### Stage 1 — one-term left block

On

\[
u\in(S-a,a)
\]

the `a` folded argument lies in `(0,2a-S)\subset(0,R)`, the `a` forward argument lies above `S`, and only the `b` folded branch survives.  Its image is

\[
(d,A).
\]

On

\[
u\in(a,b-R)
\]

the `a` folded argument lies in `(0,d-R)\subset(0,R)`, and only the `b` folded branch survives, with image

\[
(R,d).
\]

Thus

\[
\boxed{h=0\quad\text{a.e. on }(R,A).}
\tag{A14.2f.14}
\]

### Stage 2 — first half of the assembled `p_2` relation

On

\[
u\in(b-S,a-R)
\]

the exact three-term equation is

\[
-c_2h(a-u)-c_2h(a+u)-c_3h(b-u)=0.
\tag{A14.2f.15}
\]

The low image is

\[
a-u\in(R,S-d).
\]

It lies inside `(R,A)` because

\[
S-d<A
\iff
S<b.
\]

Hence (A14.2f.15) reduces to

\[
c_2h(z)+c_3h(p_2(z))=0
\quad\text{for a.e. }z\in(A,B),
\tag{A14.2f.16}
\]

where again `p_2(z)=a+b-z`.

Indeed

\[
z=a+u\in(A,B),
\qquad
p_2(z)=b-u\in(C,S).
\]

### Stage 3 — second half of the assembled `p_2` relation

On

\[
u\in(a-R,S-a)
\]

the `a` folded branch is invisible because `a-u<R`, and the exact equation is

\[
-c_2h(a+u)-c_3h(b-u)=0.
\]

Thus

\[
c_2h(z)+c_3h(p_2(z))=0
\quad\text{for a.e. }z\in(B,S).
\tag{A14.2f.17}
\]

Combining (A14.2f.16) and (A14.2f.17), the same weighted reflection relation holds for a.e.

\[
z\in(A,S)=:H.
\]

But `H` is exactly invariant under `p_2`:

\[
p_2(H)=H,
\qquad
p_2^2=\mathrm{id}.
\]

Therefore

\[
h(p_2(z))=-\frac{c_2}{c_3}h(z)
\]

on the whole `H`, and the weighted-involution lemma gives

\[
\boxed{h=0\quad\text{a.e. on }H=(A,S).}
\tag{A14.2f.18}
\]

Combining (A14.2f.14) and (A14.2f.18) yields `h=0` a.e. on `(R,S)`.

### Equality `S=2a-R`

At equality the interval `(a-R,S-a)` collapses and `A=C`.  The first relation (A14.2f.16) is then already the full invariant `p_2` relation on `(A,S)`.  Thus the theorem also holds on this internal cell-order boundary.

### Consequence for the old right flank

A14.2e imposed `S<2a-R`.  The present case proves an open set with

\[
S>2a-R
\]

and still `ker L=0`.  Therefore the right A14.2e flank is also a cell-order boundary, not a kernel boundary.

Status:

\[
\boxed{\text{right A14.2e flank sharpness}\quad\checkmark[M]_{\rm neg}.}
\]

---

## 7. Non-emptiness and parameter geometry

The region (A14.2f.3) is nonempty for every `0<R<d`.

First,

\[
L_*<b
\]

because `a<b`.

Second,

\[
2a-d-R<b
\iff
R>3a-2b.
\]

But

\[
3a-2b
=\frac12\log\frac{8}{9}<0,
\]

so this is automatic for every `R>0`.

Hence `M(R)<b` throughout `0<R<d`.

The crossover of the two lower bounds occurs at

\[
R_*=\frac{5a-3b}{2}\approx0.042474759199.
\]

Thus the theorem can be read more concretely as

\[
0<R<R_*:
\qquad
2a-d-R<S<b,
\]

and

\[
R_*\le R<d:
\qquad
L_*<S<b.
\]

In particular, for more than three quarters of the full interval `0<R<d`, the only `S` restriction is simply

\[
\frac{a+b}{2}<S<b.
\]

---

## 8. Regression anchors

The theorem contains the previously audited points

\[
(0.10,0.50,0.56),
\qquad
(0.15,0.50,0.56),
\]

and the A14.2e sweep points.

It also contains points strictly beyond both old flanks, for example

\[
(R,S,T_0)=(0.12,0.53,0.56),
\]

for which

\[
0.53>2d+0.12,
\]

and

\[
(R,S,T_0)=(0.18,0.515,0.56),
\]

for which

\[
0.515>2a-0.18.
\]

The first is closed directly by the conservative interval-kill helper.  The second requires the assembled two-cell `p_2` certificate from Case IV; a same-image-only helper intentionally stops before that refinement.

A small-`R` anchor is

\[
(R,S,T_0)=(0.01,0.50,0.56),
\]

which lies above the slanted lower bound

\[
2a-d-R\approx0.480414626506.
\]

---

## 9. Status ledger

| Item | Status |
|---|---|
| A14.2f unified sub-`b` kernel-trivial strip | ✓[M] |
| `R=0.12, S=0.53` beyond old left flank | ✓[M] |
| `R=0.18, S=0.515` beyond old right flank | ✓[M] |
| A14.2e left flank as genuine kernel boundary | ✓[M]_neg |
| A14.2e right flank as genuine kernel boundary | ✓[M]_neg |
| A14.2e theorem itself | remains ✓[M] |
| A14.2d theorem itself | remains ✓[M] |
| Complete two-shift parameter classification | ?[O] |
| Recursive typed-pseudogroup global termination | ?[O] |
| R36-A | ?[O] |
| R30-F | ?[O] |

---

## 10. Firewall / next target

A14.2f is a sufficient-region theorem only.  It does **not** prove that nontrivial kernel appears below `S=M(R)`, at `R=d`, or for `S>=b`.

The former A14.2e boundary `S=U(R)` is now ruled out as a sharp kernel boundary.  The next meaningful geometric fronts are instead:

1. the lower boundary

\[
S=M(R),
\]

especially the small-`R` slanted segment `S=2a-d-R`;

2. the vertical transition

\[
R=d;
\]

where the one-term cell `(a,b-R)` collapses and the cell ordering changes again;

3. the upper boundary

\[
S=b,
\]

where the `b`-forward visibility pattern changes.

No determinant or global untyped orbit argument is justified at this stage.
