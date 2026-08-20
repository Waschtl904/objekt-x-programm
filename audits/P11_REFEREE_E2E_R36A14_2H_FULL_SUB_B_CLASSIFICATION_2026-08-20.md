# P11 End-to-End Referee R36-A14.2h — full sub-`b` two-shift classification

Date: 2026-08-20

## Purpose / firewall

This note closes the remaining parameter region with

\[
0<R<S<b,
\qquad
b<T_0<2a,
\]

where

\[
a:=\frac{\log2}{2},\qquad
b:=\frac{\log3}{2},\qquad
d:=b-a.
\]

A14.2f and A14.2g are subsumed.  The new ingredient is one global source-chart relation valid on the entire sub-`b` annulus.  For `R<d` its folded predecessor is the tent map `y -> |y-d|`; below the reflection zone this dynamics is triangular except for the single low involution `y <-> d-y`, whose multiplier is nonunit.  Above the reflection threshold the predecessor has already been killed, leaving the familiar nonunit reflection `y <-> a+b-y`.

No assertion is made for `S>=b`, no global all-shift typed-pseudogroup termination theorem is claimed, and no R36-A, R30-F, or RH consequence is claimed.

Start head:

`f884adbc0389e989889d304de1cab571d7df469a`

---

## 1. Setup

Put

\[
c:=a+b,
\qquad
\ell:=\frac c2.
\]

The folded two-shift operator is

\[
(Lh)(u)=\sum_{\tau\in\{a,b\}}c_\tau\Bigl[
\operatorname{sgn}(u-\tau)\mathbf 1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf 1_{(R,S)}(u+\tau)h(u+\tau)
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
\tag{A14.2h.1}
\]

We also use

\[
a>d,
\tag{A14.2h.2}
\]

because

\[
a>d
\iff 2a>b
\iff \log2>\tfrac12\log3
\iff 4>3.
\]

---

## 2. Global sub-`b` source-chart relation

Assume

\[
0<R<S<b.
\]

For every `y in (R,S)` set

\[
u:=b-y.
\]

Then

\[
0<b-S<u<b-R<b<T_0.
\]

The `b`-folded argument is exactly `y`, with negative sign, while the `b`-forward branch is invisible because

\[
u+b>b>S.
\]

For the `a` branches,

\[
u-a=d-y,
\qquad
u+a=c-y.
\]

Hence

\[
|u-a|=|y-d|,
\]

and the folded sign is

\[
\operatorname{sgn}(u-a)
=-\operatorname{sgn}(y-d)
\]

away from the null point `y=d`.

Therefore `Lh(b-y)=0`, after multiplication by `-1`, is equivalent for a.e. `y in (R,S)` to

\[
\boxed{
 c_3h(y)
 +c_2\operatorname{sgn}(y-d)
 \mathbf 1_{(R,S)}(|y-d|)h(|y-d|)
 +c_2\mathbf 1_{(R,S)}(c-y)h(c-y)
 =0.
}
\tag{A14.2h.3}
\]

This is a typed identity on the actual source interval `(b-S,b-R)`.  No abstract affine composition is used.

Status:

\[
\boxed{\text{global sub-`b` source-chart relation (A14.2h.3)}\quad\checkmark[M].}
\]

For `y>d`, (A14.2h.3) reduces to the A14.2g predecessor `y-d`; for `y<d` the predecessor is the reflected value `d-y` and its coefficient changes sign.

---

## 3. Folded-descent lemma for `R<d`

### Lemma

Assume

\[
0<R<d,
\qquad R<U,
\]

and suppose `f in L^2(R,U)` satisfies for a.e. `y in (R,U)`

\[
 c_3f(y)
 +c_2\operatorname{sgn}(y-d)
 \mathbf 1_{(R,U)}(|y-d|)f(|y-d|)=0.
\tag{A14.2h.4}
\]

Then

\[
f=0\quad\text{a.e. on }(R,U).
\tag{A14.2h.5}
\]

### Proof: low part

On

\[
E_0:=(R,\min\{U,d\}),
\]

put

\[
q(y):=d-y.
\]

The common typed domain

\[
J:=E_0\cap q(E_0)
\]

is `q`-invariant.  On `E_0\setminus J`, the predecessor is outside `(R,U)`, so (A14.2h.4) gives `f(y)=0`.

On `J`, since `y<d`, (A14.2h.4) is

\[
c_3f(y)-c_2f(q(y))=0.
\]

Thus

\[
f(q(y))=\frac{c_3}{c_2}f(y).
\]

Because `q^2=id`, applying the same relation at `q(y)` yields

\[
f(y)=\left(\frac{c_3}{c_2}\right)^2f(y).
\]

By (A14.2h.1),

\[
f=0\quad\text{a.e. on }J.
\]

Hence

\[
f=0\quad\text{a.e. on }E_0.
\tag{A14.2h.6}
\]

### Proof: finite upward layers

For `y>d`, the predecessor is `y-d<y`.  Partition the remaining bounded interval `(\max\{R,d\},U)` into the finitely many `d`-layers

\[
E_k:=(kd,(k+1)d)\cap(R,U),
\qquad k\ge1,
\]

retaining only nonempty layers.

On the first nonempty layer above `d`, any active predecessor `y-d` lies either below `R` or in the already killed low part.  Thus (A14.2h.4) kills that layer.  Inductively, on every later layer any active predecessor lies in a previously killed layer.  Since there are only finitely many layers below `U`, all of `(R,U)` is killed.

This proves the lemma.

Status:

\[
\boxed{\text{folded-descent lemma}\quad\checkmark[M].}
\]

---

## 4. Proposition R36-A14.2h — full sub-`b` kernel classification

### Proposition

Assume

\[
\boxed{
0<R<S<b,
\qquad
b<T_0<2a.
}
\tag{A14.2h.7}
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A14.2h.8}
\]

### Proof

If

\[
R\ge d,
\]

this is exactly A14.2g.  It remains to prove the previously incomplete region

\[
0<R<d.
\tag{A14.2h.9}
\]

We use only the global relation (A14.2h.3).

### Case I: `S<=ell`

For every `y in (R,S)`,

\[
c-y\ge c-S\ge S.
\]

Hence the reflection term in (A14.2h.3) is invisible a.e. and we obtain exactly the folded-descent relation

\[
 c_3h(y)
 +c_2\operatorname{sgn}(y-d)
 \mathbf 1_{(R,S)}(|y-d|)h(|y-d|)=0.
\]

The folded-descent lemma with `U=S` gives

\[
h=0\quad\text{a.e. on }(R,S).
\]

### Case II: `S>ell`

Put

\[
A:=c-S.
\]

Then `A<S`.  Moreover, because `S<b`,

\[
A=c-S>c-b=a>d>R,
\tag{A14.2h.10}
\]

using (A14.2h.2) and (A14.2h.9).

#### Stage 1: kill the lower interval `(R,A)`

For `y in (R,A)`,

\[
c-y>S,
\]

so the reflection term is invisible.

Also every active folded predecessor remains below `A`: if `y>d`, then

\[
|y-d|=y-d<y<A,
\]

while if `y<d`, then

\[
|y-d|=d-y<d<A.
\]

Therefore the indicator in (A14.2h.3) may be restricted from `(R,S)` to `(R,A)`, and on `(R,A)` we have exactly the folded-descent relation (A14.2h.4).

The lemma gives

\[
\boxed{h=0\quad\text{a.e. on }(R,A).}
\tag{A14.2h.11}
\]

#### Stage 2: kill the upper reflection interval `(A,S)`

Take `y in (A,S)`.  By (A14.2h.10), `y>d`, so the folded predecessor is `y-d`.

Because `S<b`,

\[
S-d<A.
\tag{A14.2h.12}
\]

Indeed

\[
S-d<A=c-S
\iff 2S<c+d
\iff 2S<2b
\iff S<b.
\]

Hence whenever `y-d` lies in `(R,S)`, it actually lies in the already killed interval `(R,A)`.

The reflection map

\[
p(y):=c-y
\]

preserves `(A,S)` and satisfies

\[
p(A)=S,
\qquad p(S)=A,
\qquad p^2=id.
\]

Thus (A14.2h.3) reduces on `(A,S)` to

\[
c_3h(y)+c_2h(p(y))=0.
\tag{A14.2h.13}
\]

Equivalently,

\[
h(p(y))=-\frac{c_3}{c_2}h(y).
\]

Applying (A14.2h.13) at `p(y)` gives

\[
h(y)=\left(\frac{c_3}{c_2}\right)^2h(y).
\]

By (A14.2h.1),

\[
\boxed{h=0\quad\text{a.e. on }(A,S).}
\tag{A14.2h.14}
\]

Combining (A14.2h.11) and (A14.2h.14) proves

\[
h=0\quad\text{a.e. on }(R,S).
\]

This completes the proof of (A14.2h.8).

Status:

\[
\boxed{\text{R36-A14.2h full sub-`b` two-shift classification}\quad\checkmark[M].}
\]

---

## 5. Compression / what is now absorbed

A14.2h strictly subsumes the previously proved subregions A14.2f and A14.2g:

- A14.2f is no longer needed as a parameter-domain theorem; its q/propagation analysis remains a valid local mechanism and regression history.
- A14.2g remains the clean super-`d` specialization of the global relation, but its parameter theorem is contained in A14.2h.
- the former `R=d` phase boundary is not a kernel boundary.
- the former small-`R` residual region for `S<b` is closed.

The remaining two-shift front is therefore not a sub-`b` problem.  Any further classification must address

\[
S\ge b
\]

inside the first two-shift chamber `b<T_0<2a`, where the source chart `u=b-y` no longer parametrizes the whole annulus and additional forward visibility can occur.

---

## 6. Status ledger

\[
\boxed{\text{global relation (A14.2h.3)}\quad\checkmark[M]}
\]

\[
\boxed{\text{folded-descent lemma}\quad\checkmark[M]}
\]

\[
\boxed{0<R<S<b,\ b<T_0<2a\Rightarrow\ker L=\{0\}\quad\checkmark[M]}
\]

\[
\boxed{\text{complete sub-`b` classification}\quad\checkmark[M]}
\]

Still open:

\[
\boxed{\text{two-shift classification allowing }S\ge b\quad ?[O]}
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
