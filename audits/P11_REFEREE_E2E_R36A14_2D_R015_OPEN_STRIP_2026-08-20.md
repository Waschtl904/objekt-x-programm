# P11 End-to-End Referee R36-A14.2d — R=0.15 mechanism, nilpotent-DAG refutation, and open kernel-trivial strip

Date: 2026-08-20

## Purpose / firewall

This note audits the proposed interpretation of the regression case

\[
(R,S,T_0)=(0.15,0.50,0.56)
\]

as a purely combinatorial nilpotent-DAG / finite-escape mechanism.

The nilpotent-DAG interpretation is false for the natural typed affine transition graph: after the
one-term cascade a genuine domain-preserving reflection remains, so the graph contains a two-cycle.
However, the regression point belongs to a nonempty open parameter region on which kernel
triviality follows by an exact three-stage argument:

1. two one-term cells kill a left/central interval;
2. a two-term cell propagates that killed interval across `a`;
3. the final three-term cell reduces to a weighted involution on the right remainder.

This yields an open two-shift kernel-triviality theorem strictly stronger than the isolated
`R=0.15` regression.

No global two-shift kernel classification, no global typed-pseudogroup termination theorem,
no R36-A, and no R30-F conclusion is made.

Start head:

`207992ce02fc76ea43fa40757b8d9f506e20424d`

---

## 1. Setup

Write

\[
a:=\tau_2=\frac{\log2}{2},\qquad
b:=\tau_3=\frac{\log3}{2},\qquad
d:=b-a=\frac12\log\frac32.
\]

Thus

\[
a\approx0.346573590280,\qquad
b\approx0.549306144334,\qquad
d\approx0.202732554054.
\]

The first genuine two-shift chamber is

\[
b\le T_0<2a=\log2.
\]

The two positive weights are

\[
c_2=\sqrt{\log2}\,2^{-3/4},\qquad
c_3=\sqrt{\log3}\,3^{-3/4},
\]

and A14.2b already proves

\[
c_2\ne c_3,\qquad
\left(\frac{c_2}{c_3}\right)^2\ne1.
\]

The canonical folded operator is

\[
(Lh)(u)=
\sum_{\tau\in\{a,b\}}c_\tau
\Bigl[
\operatorname{sgn}(u-\tau)\mathbf1_{(R,S)}(|u-\tau|)
h(|u-\tau|)
-\mathbf1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr].
\]

---

## 2. Audit of the proposed nilpotent-DAG argument

A proposed abstraction asserted that, when the `q`-domain is empty, rational independence of
`a,b` prevents cycles, so the typed cell-transition graph is a DAG and a finite adjacency matrix
`M` should satisfy `M^N=0`.

That implication is false.

For the regression point, after the left part of the annulus has been killed, the `C2` constraint
reduces on

\[
H:=(a+b-S,S)
\]

to

\[
c_2 h(z)+c_3 h(p(z))=0,
\qquad
p(z):=a+b-z.
\]

The interval is invariant:

\[
p(H)=H,\qquad p^2=\mathrm{id}.
\]

Therefore the typed transition graph contains the genuine two-cycle

\[
z\longleftrightarrow p(z).
\]

Its multiplier is

\[
h(p(z))=-\frac{c_2}{c_3}h(z).
\]

Applying the same relation at `p(z)` gives

\[
h(z)=\left(\frac{c_2}{c_3}\right)^2h(z).
\]

Thus the cycle kills because its total multiplier is not `1`; it does not disappear because the
graph is acyclic.

On the natural two-chart representation, the underlying adjacency matrix contains the block

\[
A_p=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad
A_p^2=I,
\]

which is not nilpotent. A weighted transfer block likewise has nonzero square.

The irrationality

\[
\frac ab=\frac{\log2}{\log3}\notin\mathbb Q
\]

excludes nontrivial pure-translation identities of the form

\[
x+k_1a+k_2b=x
\]

with integers `k_1,k_2` not both zero. It does not exclude reflection cycles. An involution such
as `p` satisfies `p^2=id` identically, independently of any arithmetic relation between `a,b`.

Therefore

\[
\boxed{
\text{irrationality }a/b\notin\mathbb Q
\not\Longrightarrow
\text{typed affine transition graph acyclic}.
}
\]

Status:

\[
\boxed{\text{nilpotent-DAG inference from }a/b\notin\mathbb Q\quad\times[M].}
\]

The valid architecture remains: detect typed strongly connected components / weighted cycles,
kill those whose total multiplier is nonunit, and only then propagate through the condensation
graph. The condensation graph of a finite already-constructed graph is a DAG by graph theory,
not by irrationality; global finiteness under recursive interval refinement remains `?[O]`.

---

## 3. Exact `R=0.15` mechanism

At

\[
R=0.15,\qquad S=0.50,\qquad T_0=0.56
\]

one has `R>d/2`, so the `q`-domain is empty.

The complete positive breakpoints are

\[
0,\ b-S,\ S-a,\ a-R,\ a,\ b-R,\ a+R,\ b,\ T_0.
\]

Numerically,

\[
0
<0.049306144334
<0.153426409720
<0.196573590280
<0.346573590280
<0.399306144334
<0.496573590280
<0.549306144334
<0.56.
\]

### Stage 1 — two one-term cells

On `u\in(a-R,a)`, only the `b` folded branch survives:

\[
-c_3h(b-u)=0,
\]

so

\[
h=0\quad\text{a.e. on }(d,d+R).
\]

On `u\in(a,b-R)`, because `R>d/2` one has `d-R<R`, so the `a` folded branch is invisible and only

\[
-c_3h(b-u)=0
\]

survives. Hence

\[
h=0\quad\text{a.e. on }(R,d).
\]

Thus

\[
\boxed{h=0\quad\text{a.e. on }(R,d+R).}
\tag{A14.2d.1}
\]

### Stage 2 — low-`u` propagation across `a`

On `u\in(0,b-S)`, the exact equation is

\[
-c_2h(a-u)-c_2h(a+u)=0.
\]

The image intervals are

\[
a-u\in(S-d,a),
\qquad
a+u\in(a,a+b-S).
\]

At `R=0.15`,

\[
d+R\approx0.352732554054>a\approx0.346573590280,
\]

and `S-d>R`. Therefore the first image interval lies inside (A14.2d.1), and the cell equation
forces

\[
h=0\quad\text{a.e. on }(a,a+b-S).
\]

Since `a<d+R<a+b-S`,

\[
\boxed{h=0\quad\text{a.e. on }(R,a+b-S).}
\tag{A14.2d.2}
\]

### Stage 3 — terminal weighted reflection

On `u\in(b-S,S-a)`, the exact three-term equation is

\[
-c_2h(a-u)-c_2h(a+u)-c_3h(b-u)=0.
\]

The first image

\[
a-u\in(2a-S,S-d)
\]

lies inside (A14.2d.2). Hence the constraint reduces legitimately to

\[
c_2h(a+u)+c_3h(b-u)=0.
\]

Set

\[
z:=a+u\in H:=(a+b-S,S).
\]

Then

\[
b-u=a+b-z=p(z),
\]

so

\[
h(p(z))=-\frac{c_2}{c_3}h(z).
\]

Since `p(H)=H`, `p^2=id`, and `(c_2/c_3)^2\ne1`, the weighted-involution lemma gives

\[
h=0\quad\text{a.e. on }H.
\]

Combining with (A14.2d.2),

\[
\boxed{\ker L_{0.15,0.50,0.56}=\{0\}.}
\]

Status:

\[
\boxed{\text{R=0.15 regression kernel triviality}\quad\checkmark[M].}
\]

This proof uses no `q`-cycle and no determinant, but it still uses the terminal weighted reflection
`p`. It is therefore not a purely nilpotent finite-escape proof.

---

## 4. Proposition R36-A14.2d — open kernel-trivial strip

Assume

\[
b<T_0<2a,
\]

and

\[
2a-b<R<d.
\tag{A14.2d.3}
\]

Assume further

\[
\max\left\{\frac{a+b}{2},\,d+R\right\}
<S<
\min\{b,\,2a-R\}.
\tag{A14.2d.4}
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A14.2d.5}
\]

### Proof

First,

\[
2a-b>\frac d2.
\]

Indeed this is equivalent to

\[
5a>3b
\iff
5\log2>3\log3
\iff
2^5>3^3,
\]

which is `32>27`. Hence (A14.2d.3) implies `R>d/2`.

#### Stage 1

On `u\in(a-R,a)`, the `a` folded branch lies in `(0,R)`, while

\[
u+a>2a-R>S.
\]

The `b` forward branch is also outside `(R,S)`, and

\[
b-u\in(d,d+R)\subset(R,S)
\]

by `R<d` and `d+R<S`. Therefore

\[
h=0\quad\text{a.e. on }(d,d+R).
\]

On `u\in(a,b-R)`, the `a` folded argument lies in `(0,d-R)`. Because `R>d/2`, one has `d-R<R`,
so that branch is invisible. The forward branches are invisible for `u>a`, while

\[
b-u\in(R,d).
\]

Therefore

\[
h=0\quad\text{a.e. on }(R,d).
\]

Thus

\[
h=0\quad\text{a.e. on }(R,d+R).
\tag{A14.2d.6}
\]

#### Stage 2

Because `S<b`, `(0,b-S)` is nonempty. On it

\[
-c_2h(a-u)-c_2h(a+u)=0,
\]

with image intervals

\[
I_-=(S-d,a),
\qquad
I_+=(a,a+b-S).
\]

By (A14.2d.4), `S-d>R`. By (A14.2d.3),

\[
d+R>a
\iff
R>a-d=2a-b.
\]

Hence `I_-\subset(R,d+R)`, so (A14.2d.6) kills the first term and forces

\[
h=0\quad\text{a.e. on }I_+.
\]

Also

\[
a+b-S>d+R
\iff
S+R<2a,
\]

which follows from `S<2a-R`. Therefore

\[
h=0\quad\text{a.e. on }(R,a+b-S).
\tag{A14.2d.7}
\]

#### Stage 3

Because `S>(a+b)/2`, the interval `(b-S,S-a)` is nonempty. On it

\[
-c_2h(a-u)-c_2h(a+u)-c_3h(b-u)=0.
\]

The first chart has image

\[
I_0=(2a-S,S-d).
\]

Its lower endpoint satisfies `2a-S>R` because `S<2a-R`. Its upper endpoint satisfies

\[
S-d<a+b-S
\iff
S<b.
\]

Hence `I_0\subset(R,a+b-S)`, so (A14.2d.7) removes the first term.

The remaining two charts share

\[
H=(a+b-S,S)
\]

and are related by

\[
p(z)=a+b-z.
\]

Thus

\[
h(p(z))=-\frac{c_2}{c_3}h(z),
\qquad
p(H)=H,
\qquad
p^2=id.
\]

Since `(c_2/c_3)^2\ne1`, the weighted-involution lemma yields `h=0` a.e. on `H`. Together with
(A14.2d.7), this gives `h=0` a.e. on `(R,S)`, hence `ker L_{R,S,T_0}={0}`. `\square`

Status:

\[
\boxed{\text{R36-A14.2d open kernel-trivial strip}\quad\checkmark[M].}
\]

---

## 5. Regression-point check

For

\[
(R,S,T_0)=(0.15,0.50,0.56),
\]

one has

\[
2a-b\approx0.143841036226<0.15<d\approx0.202732554054,
\]

\[
\frac{a+b}{2}\approx0.447939867307<0.50,
\qquad
d+R\approx0.352732554054<0.50,
\]

\[
0.50<b\approx0.549306144334,
\qquad
0.50<2a-R\approx0.543147180560,
\]

and

\[
b<0.56<2a.
\]

Hence the regression point lies strictly inside the strip.

The conservative typed regression helper reproduces the same full killed union. Its event sequence
uses one-term kills followed by a weighted involution; no nilpotent adjacency claim is needed.

---

## Status firewall

- `q` absent at `R=0.15`: `checkmark[M]`.
- `R=0.15` kernel triviality: `checkmark[M]`.
- `a/b` irrational implies typed transition graph acyclic: `times[M]`.
- natural transition-matrix nilpotence at `R=0.15`: `times[M]`.
- terminal reflection `p(z)=a+b-z` gives a genuine typed two-cycle: `checkmark[M]`.
- R36-A14.2d strip (A14.2d.3)-(A14.2d.4): `ker L={0}` `checkmark[M]`.
- global typed-pseudogroup / recursive-partition termination: `?[O]`.
- full two-shift kernel classification: `?[O]`.
- R36-A: `?[O]`.
- R30-F: `?[O]`.
- strong terminal transport / polar gauge / Object X / RH: unchanged and open.

## Next target

The useful next question is no longer whether the `R=0.15` graph is nilpotent. It is not.

The next structural target is to compare the two proved local mechanisms:

1. `R<d/2<S`: the additional `q(x)=d-x` weighted cycle fills the left gap;
2. the A14.2d strip `R>2a-b`: one-term cells already reach past `a`, so low-`u` propagation replaces
   the `q`-cycle.

A natural next audit is whether these mechanisms can be unified across the intermediate range
`d/2 <= R <= 2a-b` by a third propagation pattern, still without any global pseudogroup
termination assumption.
