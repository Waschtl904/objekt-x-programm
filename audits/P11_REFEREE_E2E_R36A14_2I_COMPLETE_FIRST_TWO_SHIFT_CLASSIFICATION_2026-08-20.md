# P11 End-to-End Referee R36-A14.2i — complete first two-shift chamber classification

Date: 2026-08-20

## Purpose / firewall

This note classifies the kernel of the folded two-shift operator throughout the entire first genuine two-shift chamber

\[
0<R<S<T_0,
\qquad
b<T_0<2a,
\]

where

\[
a:=\tau_2=\frac{\log2}{2},
\qquad
b:=\tau_3=\frac{\log3}{2},
\qquad
d:=b-a,
\qquad
c:=a+b.
\]

Because the next shift after `b` is `2a=log 2`, the condition `T_0<2a` means that only the shifts `a,b` are active.

The conclusion is a complete sharp phase diagram:

\[
\boxed{
\ker L_{R,S,T_0}=\{0\}
\iff
\bigl(S\le b\bigr)\ \text{or}\ \bigl(R\ge a\bigr).
}
\]

Equivalently,

\[
\boxed{
R<a<b<S
\iff
\ker L_{R,S,T_0}\ne\{0\}.
}
\]

In the nontrivial region the kernel is not merely nonzero: it contains a closed copy of an infinite-dimensional `L^2` space.

This is a two-shift classification only.  It does **not** imply a global all-shift typed-pseudogroup termination theorem, R36-A, R30-F, Objekt X, or RH.

Start head:

`3b22ce3b7368b7619454e7053893cbea4a7cdca1`

---

## 1. Operator and constants

The folded operator is

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

A14.2b gives

\[
\left(\frac{c_2}{c_3}\right)^2\ne1,
\qquad
\left(\frac{c_3}{c_2}\right)^2\ne1.
\tag{A14.2i.1}
\]

Put

\[
\rho:=\frac{c_3}{c_2}.
\]

We will also use

\[
d=b-a>0,
\qquad
a>d,
\qquad
c=a+b.
\]

---

## 2. Symmetric `b`-chart relation across `S=b`

For every `y in (R,S)` define

\[
u:=|b-y|.
\]

Because `0<R<S<T_0` and `b<T_0`, one has `0\le u<T_0` a.e.  The point `y=b`, where `u=0`, is null and irrelevant.

A direct branch check gives one relation valid on both sides of `b`:

\[
\boxed{
 c_3h(y)
 +c_3\mathbf1_{(R,S)}(2b-y)h(2b-y)
 +c_2\operatorname{sgn}(y-d)\mathbf1_{(R,S)}(|y-d|)h(|y-d|)
 +c_2\mathbf1_{(R,S)}(c-y)h(c-y)
 =0.
}
\tag{A14.2i.2}
\]

For `y<b`, the term `h(y)` comes from the `b`-folded branch and `h(2b-y)` from the `b`-forward branch.  For `y>b`, these roles are reversed.  The `a`-branches become `|y-d|` and `c-y` in both cases.

Thus the relation is typed on the actual source chart.  No abstract untyped composition is used.

Status:

\[
\boxed{\text{symmetric `b`-chart relation (A14.2i.2)}\quad\checkmark[M].}
\]

For `S<b`, the `2b-y` term is invisible and this reduces to A14.2h.

---

## 3. The endpoint `S=b`

A14.2h proves kernel triviality for `S<b`.  The endpoint `S=b` also has trivial kernel.

### 3.1 `R<a`

For `y in (R,b)` the `2b-y` term in (A14.2i.2) is invisible because `2b-y>b=S`.

On `(R,a)`, the reflection `c-y` is also invisible because `c-y>b=S`.

If `R<d`, the A14.2h folded-descent lemma with upper endpoint `a` kills `(R,a)`.

If `d\le R<a`, then for `y in (R,a)` one has

\[
y-d<a-d<d\le R,
\]

so even the folded predecessor is invisible and the relation is one-term.  Again

\[
h=0\quad\text{a.e. on }(R,a).
\]

On `(a,b)`, every folded predecessor `y-d` lies below `a` and is already killed.  The map

\[
p(y):=c-y
\]

preserves `(a,b)` and satisfies `p^2=id`.  Hence the relation reduces to

\[
c_3h(y)+c_2h(p(y))=0.
\]

By (A14.2i.1), the weighted involution kills `(a,b)`.

Thus `S=b`, `R<a` has trivial kernel.

### 3.2 `R\ge a`

This is contained in the high-`R` theorem proved in Section 4 below.

Therefore

\[
\boxed{S=b\Longrightarrow\ker L=\{0\}.}
\tag{A14.2i.3}
\]

Combining with A14.2h,

\[
\boxed{S\le b\Longrightarrow\ker L=\{0\}.}
\tag{A14.2i.4}
\]

---

## 4. High-`R` triviality for `R\ge a`

Assume

\[
a\le R<S<T_0,
\qquad
S\ge b.
\]

For `y in (R,S)` put

\[
u:=y-a.
\]

Then `0<u<T_0-a<a<b`.  At this source point the `a`-folded argument is

\[
2a-y<2a-R\le a\le R,
\]

so it is invisible a.e.

The surviving exact relation is

\[
\boxed{
 c_2h(y)
 +c_3\mathbf1_{(R,S)}(c-y)h(c-y)
 +c_3\mathbf1_{(R,S)}(y+d)h(y+d)
 =0.
}
\tag{A14.2i.5}
\]

### Case I: `R\ge c/2`

For `y>R`,

\[
c-y<c-R\le R,
\]

so the reflection is invisible.  Hence

\[
c_2h(y)+c_3\mathbf1_{(R,S)}(y+d)h(y+d)=0.
\]

The shift is strictly upward.  The top layer `(\max\{R,S-d\},S)` has no successor and is killed.  Iterating downward in finitely many `d`-layers kills all of `(R,S)`.

### Case II: `a\le R<c/2`

Put

\[
P:=c-R.
\]

Then

\[
R<P\le b\le S.
\]

On `(P,S)`, `c-y<R`, so the reflection is invisible.  The same finite upward-layer argument kills

\[
h=0\quad\text{a.e. on }(P,S).
\tag{A14.2i.6}
\]

On `(R,P)`, the reflection `p(y)=c-y` preserves the interval.  Moreover

\[
y+d>R+d\ge a+d=b\ge P,
\]

with strict inequality a.e. at the boundary case `R=a`.  Thus every active shifted value `y+d` lies in the already killed upper region.

Therefore (A14.2i.5) reduces on `(R,P)` to

\[
c_2h(y)+c_3h(p(y))=0.
\]

Since `p^2=id` and `(c_2/c_3)^2\ne1`, the weighted-involution lemma kills `(R,P)`.

Hence

\[
\boxed{
R\ge a\Longrightarrow\ker L_{R,S,T_0}=\{0\}
}
\tag{A14.2i.7}
\]

throughout the whole first two-shift chamber.

Status:

\[
\boxed{\text{high-`R` triviality}\quad\checkmark[M].}
\]

---

## 5. Explicit infinite-dimensional kernel for `R<a<b<S`

Assume now

\[
\boxed{
0<R<a<b<S<T_0<2a.
}
\tag{A14.2i.8}
\]

This is exactly the region not covered by (A14.2i.4) or (A14.2i.7).

Define

\[
m:=a-\frac d2=\frac{3a-b}{2}
\]

and

\[
\lambda:=\max\{R,\ T_0-a,\ c-S,\ m\}.
\tag{A14.2i.9}
\]

Every entry in the maximum is strictly below `a`:

- `R<a` by assumption;
- `T_0-a<a` because `T_0<2a`;
- `c-S<a` because `S>b`;
- `m<a` because `d>0`.

Therefore

\[
\boxed{\lambda<a.}
\tag{A14.2i.10}
\]

Put

\[
I:=(\lambda,a).
\]

This is a nonempty open interval.

### 5.1 Four disjoint support charts

For `x in I` define

\[
J_0:=I,
\qquad
J_1:=2a-I,
\qquad
J_2:=I+d,
\qquad
J_3:=c-I.
\]

Explicitly,

\[
J_0=(\lambda,a),
\]

\[
J_1=(a,2a-\lambda),
\]

\[
J_2=(\lambda+d,b),
\]

\[
J_3=(b,c-\lambda).
\]

All four lie in `(R,S)`:

- `J_0` because `\lambda\ge R`;
- `J_1` because `R<a` and `\lambda\ge c-S`, which gives `2a-\lambda\le S-d<S`;
- `J_2` because `\lambda+d>R` and `b<S`;
- `J_3` because `b>R` and `\lambda\ge c-S` gives `c-\lambda\le S`.

They are disjoint up to endpoints.  The only nontrivial ordering check is

\[
2a-\lambda\le\lambda+d,
\]

which is equivalent to

\[
\lambda\ge a-\frac d2=m.
\]

Thus

\[
\boxed{J_0,J_1,J_2,J_3\text{ are pairwise disjoint a.e.}}
\tag{A14.2i.11}
\]

### 5.2 Kernel embedding

Take arbitrary

\[
f\in L^2(I).
\]

Define `h_f` on the four charts by

\[
h_f(x)=f(x),
\qquad x\in I,
\tag{A14.2i.12a}
\]

\[
h_f(2a-x)=-f(x),
\tag{A14.2i.12b}
\]

\[
h_f(x+d)=\rho f(x),
\tag{A14.2i.12c}
\]

\[
h_f(c-x)=-\rho f(x),
\tag{A14.2i.12d}
\]

and set `h_f=0` elsewhere in `(R,S)`.

Because the four chart maps preserve Lebesgue measure and the supports are disjoint,

\[
\boxed{
\|h_f\|_2^2=2(1+\rho^2)\|f\|_2^2.
}
\tag{A14.2i.13}
\]

Hence `f\mapsto h_f` is a bounded injective map with closed range.

### 5.3 Source firewall

Put

\[
e:=2a-b=a-d.
\]

The condition `\lambda\ge m` implies

\[
\lambda>e
\]

and

\[
a-\lambda\le\lambda-e.
\]

Every original operator branch that meets the support of `h_f` comes from exactly one of the following three source families:

\[
U_0:=a-I=(0,a-\lambda),
\]

\[
U_2:=I-e=(\lambda-e,d),
\]

\[
U_1:=b-I=(d,b-\lambda).
\]

These intervals are disjoint up to endpoints.

The potentially dangerous upper `a`-fold source of `J_0` is absent because `\lambda\ge T_0-a`, hence

\[
a+x>T_0
\qquad(x\in I).
\]

All other inverse branch possibilities either lie outside `(0,T_0)` or hit values outside the four support charts.  Thus it suffices to check the three source families.

### 5.4 Exact cancellation on `U_0`

Let

\[
u=a-x,
\qquad x\in I.
\]

The four support values seen by the operator are

\[
x,
\qquad
2a-x,
\qquad
x+d,
\qquad
c-x.
\]

All four coefficients are negative, so

\[
(Lh_f)(u)
=-c_2h_f(x)-c_2h_f(2a-x)-c_3h_f(x+d)-c_3h_f(c-x).
\]

Using (A14.2i.12),

\[
(Lh_f)(u)
=-c_2f+c_2f-c_3\rho f+c_3\rho f=0.
\tag{A14.2i.14}
\]

### 5.5 Exact cancellation on `U_1`

Let

\[
u=b-x,
\qquad x\in I.
\]

The only support values are `x` from the `b`-fold and `c-x` from the `a`-forward branch.  Hence

\[
(Lh_f)(u)
=-c_3f(x)-c_2(-\rho f(x))=0
\tag{A14.2i.15}
\]

because `c_2\rho=c_3`.

### 5.6 Exact cancellation on `U_2`

Let

\[
u=x-e,
\qquad x\in I.
\]

The only support values are `2a-x` from the `b`-fold and `x+d` from the `a`-forward branch.  Thus

\[
(Lh_f)(u)
=-c_3(-f(x))-c_2(\rho f(x))=0.
\tag{A14.2i.16}
\]

No other source point sees the support.  Therefore

\[
\boxed{Lh_f=0\quad\text{a.e.}}
\tag{A14.2i.17}
\]

for every `f in L^2(I)`.

By (A14.2i.13),

\[
\boxed{
L^2(I)\hookrightarrow\ker L_{R,S,T_0}
}
\]

as a closed subspace.  In particular,

\[
\boxed{
\dim\ker L_{R,S,T_0}=\infty
\qquad\text{whenever }R<a<b<S.
}
\tag{A14.2i.18}
\]

Status:

\[
\boxed{\text{open-region infinite-dimensional kernel construction}\quad\checkmark[M].}
\]

---

## 6. Complete classification theorem

Combining Sections 3–5 with A14.2h gives:

### Proposition R36-A14.2i — complete first two-shift chamber classification

Assume

\[
\boxed{
0<R<S<T_0,
\qquad
b<T_0<2a.
}
\tag{A14.2i.19}
\]

Then

\[
\boxed{
\ker L_{R,S,T_0}=\{0\}
\iff
\bigl(S\le b\bigr)\ \text{or}\ \bigl(R\ge a\bigr).
}
\tag{A14.2i.20}
\]

Equivalently,

\[
\boxed{
R<a<b<S
\iff
\ker L_{R,S,T_0}\ne\{0\}.
}
\tag{A14.2i.21}
\]

Moreover, in the nontrivial region

\[
\boxed{
\dim\ker L_{R,S,T_0}=\infty.
}
\tag{A14.2i.22}
\]

This is a sharp classification including both phase boundaries:

- `S=b` belongs to the trivial-kernel side;
- `R=a` belongs to the trivial-kernel side;
- crossing simultaneously into `R<a<b<S` opens an infinite-dimensional kernel channel.

Status:

\[
\boxed{\text{R36-A14.2i complete first two-shift classification}\quad\checkmark[M].}
\]

---

## 7. Compression / interpretation

A14.2i strictly compresses the earlier A14.2 sequence:

- A14.2h remains the complete `S<b` positive theorem;
- its endpoint extends to `S=b`;
- the entire region `R\ge a` is positive even for `S>b`;
- the complementary open region `R<a<b<S` is now proved negative for injectivity, with an explicit infinite-dimensional kernel.

Thus there is no remaining parameter chamber to classify inside the first two-shift window `b<T_0<2a`.

The sharp kernel phase diagram is

\[
\boxed{
\begin{array}{c|c}
\text{parameter region} & \ker L \\
\hline
S\le b & \{0\} \\
S>b,\ R\ge a & \{0\} \\
S>b,\ R<a & \text{infinite-dimensional}
\end{array}}
\]

The relation to the typed-pseudogroup viewpoint is conceptual only: A14.2i is proved directly from actual source charts and original operator branches.  No global pseudogroup-termination theorem is promoted.

---

## 8. Status ledger

\[
\boxed{\text{symmetric `b`-chart relation}\quad\checkmark[M]}
\]

\[
\boxed{S=b\text{ endpoint triviality}\quad\checkmark[M]}
\]

\[
\boxed{R\ge a\text{ high-strip triviality}\quad\checkmark[M]}
\]

\[
\boxed{R<a<b<S\text{ explicit infinite-dimensional kernel}\quad\checkmark[M]}
\]

\[
\boxed{\text{complete first two-shift chamber classification}\quad\checkmark[M]}
\]

Still open:

\[
\boxed{\text{higher-shift chambers }T_0\ge2a\quad ?[O]}
\]

\[
\boxed{\text{global typed-pseudogroup termination theorem}\quad ?[O]}
\]

\[
\boxed{\text{R36-A}\quad ?[O]}
\]

\[
\boxed{\text{R30-F}\quad ?[O]}
\]
