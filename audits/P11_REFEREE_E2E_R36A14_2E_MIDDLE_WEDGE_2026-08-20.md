# P11 End-to-End Referee R36-A14.2e — middle-wedge kernel theorem and typed Dieder firewall

Date: 2026-08-20

## Purpose / firewall

This note audits the proposed next step after R36-A14.2d: the strip

\[
\frac d2\le R\le 2a-b,
\qquad
 a:=\tau_2=\frac{\log2}{2},
\quad b:=\tau_3=\frac{\log3}{2},
\quad d:=b-a.
\]

The proposed explanation via a nilpotent DAG has already been refuted in A14.2d. A second proposed explanation uses two reflections

\[
p_1(x)=2a-x,
\qquad
p_2(x)=a+b-x,
\]

whose abstract composition is the translation `x -> x+d`.

The algebraic identity is correct, but the concrete typed domains produced by the relevant cells do not compose in the proposed order. More importantly, no such Dieder composition is needed: a larger open parameter wedge admits a direct three-stage proof of kernel triviality.

No global typed-pseudogroup termination theorem, no global two-shift classification, no R36-A, and no R30-F conclusion is made.

Start head:

`ec39dec6e4d5681f5e4bed3891ee7404af9b9203`

---

## 1. Setup

Work in the first genuine two-shift chamber

\[
b<T_0<2a.
\]

Only the shifts `a,b` are active. The canonical folded operator is

\[
(Lh)(u)=\sum_{\tau\in\{a,b\}}c_\tau
\Bigl[
\operatorname{sgn}(u-\tau)\mathbf 1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf 1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr],
\]

with positive weights

\[
c_2=\sqrt{\log2}\,2^{-3/4},
\qquad
c_3=\sqrt{\log3}\,3^{-3/4}.
\]

A14.2b proves

\[
c_2\ne c_3,
\qquad
\left(\frac{c_2}{c_3}\right)^2\ne1.
\]

Set

\[
L_*:=\frac{a+b}{2},
\qquad
U_R:=\min\{2d+R,\,2a-R\}.
\]

---

## 2. The wedge is nonempty

Assume

\[
\frac d2<R<d.
\tag{A14.2e.1}
\]

The two affine upper bounds cross exactly at

\[
2d+R=2a-R
\iff
R=a-d=2a-b.
\]

For `R <= a-d`,

\[
U_R=2d+R,
\]

while for `R >= a-d`,

\[
U_R=2a-R.
\]

The lower bound lies strictly below `U_R` throughout (A14.2e.1).

On the left side it is enough to check `R=d/2`:

\[
\frac{5d}{2}>\frac{a+b}{2}
\iff
2b>3a
\iff
3>2^{3/2},
\]

which follows from `9>8`.

On the right side it is enough to check `R=d`:

\[
2a-d>\frac{a+b}{2}
\iff
5a>3b
\iff
2^5>3^3,
\]

which is `32>27`.

Hence

\[
\boxed{L_*<U_R\quad\text{for every }d/2<R<d.}
\]

Also `U_R<=b`: for `R<=a-d`, `2d+R<=b`; for `R>=a-d`, `2a-R<=b`. Thus `S<U_R` automatically implies `S<b`.

---

## 3. Proposition R36-A14.2e — middle-wedge kernel triviality

Assume

\[
\boxed{
\frac d2<R<d,
\qquad
\frac{a+b}{2}<S<\min\{2d+R,2a-R\},
\qquad
b<T_0<2a.
}
\tag{A14.2e.2}
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A14.2e.3}
\]

### Proof — Stage 1: two one-term cells

Because `R<d`, the interval `(a,b-R)` is nonempty. Because `R>d/2`,

\[
d-R<R.
\]

First take

\[
u\in(a-R,a).
\]

The `a` folded argument lies in `(0,R)`. The `a` forward argument satisfies

\[
u+a>2a-R>S,
\]

because `S<2a-R`. The `b` forward argument is larger than `b>S`.

The remaining folded argument satisfies

\[
b-u\in(d,d+R).
\]

This whole interval lies in `(R,S)`: `R<d`, and `d+R<S` follows from

\[
S>L_*=\frac{a+b}{2}>d+R.
\]

For the last strict inequality note that `R<d` and

\[
d<\frac{3a-b}{2}
\iff
3b<5a
\iff
3^3<2^5,
\]

which is `27<32`.

Hence on this cell

\[
-c_3h(b-u)=0,
\]

and therefore

\[
h=0\quad\text{a.e. on }(d,d+R).
\tag{A14.2e.4}
\]

Now take

\[
u\in(a,b-R).
\]

The forward branches are invisible by the A14.2c forward-branch firewall. The `a` folded argument lies in

\[
(0,d-R)\subset(0,R),
\]

whereas

\[
b-u\in(R,d)\subset(R,S).
\]

Thus again only the `b` folded branch survives, and

\[
h=0\quad\text{a.e. on }(R,d).
\tag{A14.2e.5}
\]

Combining (A14.2e.4) and (A14.2e.5),

\[
\boxed{h=0\quad\text{a.e. on }K:=(R,d+R).}
\tag{A14.2e.6}
\]

### Proof — Stage 2: terminal weighted reflection `p_2`

Because `S>(a+b)/2`, the cell

\[
u\in(b-S,S-a)
\]

is nonempty. Its exact equation is

\[
-c_2h(a-u)-c_2h(a+u)-c_3h(b-u)=0.
\tag{A14.2e.7}
\]

The low folded image is

\[
a-u\in(2a-S,S-d).
\]

It lies entirely in `K`. Indeed,

\[
2a-S>R
\]

because `S<2a-R`, while

\[
S-d<d+R
\]

because `S<2d+R`.

Thus the first term in (A14.2e.7) vanishes a.e. Set

\[
H:=(a+b-S,S),
\qquad
z:=a+u\in H.
\]

Then

\[
b-u=a+b-z=:p_2(z),
\]

and (A14.2e.7) reduces to

\[
c_2h(z)+c_3h(p_2(z))=0.
\]

The interval is invariant:

\[
p_2(H)=H,
\qquad p_2^2=\mathrm{id}.
\]

Hence

\[
h(p_2(z))=-\frac{c_2}{c_3}h(z).
\]

Applying the same relation at `p_2(z)` gives

\[
h(z)=\left(\frac{c_2}{c_3}\right)^2h(z).
\]

Since `(c_2/c_3)^2 != 1`, the weighted-involution lemma yields

\[
\boxed{h=0\quad\text{a.e. on }H=(a+b-S,S).}
\tag{A14.2e.8}
\]

### Proof — Stage 3: propagate across the remaining middle interval

Because `S<2a-R`, the cell

\[
u\in(S-a,a-R)
\]

is nonempty. The forward branches are invisible, and the exact equation is

\[
-c_2h(a-u)-c_3h(b-u)=0.
\tag{A14.2e.9}
\]

The first image is

\[
a-u\in(R,2a-S).
\]

It lies inside `K=(R,d+R)`. It is enough to show

\[
2a-S<d+R
\iff
S>2a-d-R.
\]

But `S>L_*`, and for `R>d/2`,

\[
L_*>2a-d-R.
\]

Indeed the latter is equivalent to

\[
R>\frac{5a-3b}{2},
\]

while

\[
\frac d2>\frac{5a-3b}{2}
\iff
2b>3a,
\]

already established from `9>8`.

Therefore the first term in (A14.2e.9) vanishes a.e., and the cell forces

\[
h=0\quad\text{a.e. on }(d+R,a+b-S).
\tag{A14.2e.10}
\]

This interval is nonempty because `S<2a-R`, and it lies in `(R,S)` because `d+R<S` and `a+b-S<S`.

Finally,

\[
(R,S)
=(R,d+R)\cup(d+R,a+b-S)\cup(a+b-S,S)
\]

up to endpoints. Equations (A14.2e.6), (A14.2e.10), and (A14.2e.8) therefore give

\[
h=0\quad\text{a.e. on }(R,S).
\]

This proves (A14.2e.3).

Status:

\[
\boxed{\text{R36-A14.2e middle-wedge theorem}\quad\checkmark[M].}
\]

---

## 4. Relation to A14.2d

A14.2d assumed

\[
2a-b<R<d
\]

and

\[
\max\{(a+b)/2,d+R\}<S<\min\{b,2a-R\}.
\]

For `R<d`, one has

\[
d+R<\frac{a+b}{2}
\]

by the `27<32` inequality used above. Hence the lower maximum in A14.2d is simply `(a+b)/2`.

For `R>2a-b=a-d`, one also has

\[
2a-R<b<2d+R,
\]

so the A14.2e upper bound becomes exactly `2a-R`.

Therefore the open A14.2d strip is contained in A14.2e. A14.2d remains a correct theorem and a useful independent proof architecture, but its parameter hypotheses are not maximal.

In particular the regression point

\[
(R,S,T_0)=(0.15,0.50,0.56)
\]

is covered by both A14.2d and A14.2e.

---

## 5. The former `R`-gap is closed on a nonempty `S`-wedge

The previously isolated interval

\[
\frac d2\le R\le a-d=2a-b
\]

was singled out because the `q`-domain is empty while the A14.2d overhang condition `d+R>a` has not yet begun.

A14.2e shows that this is not a separate obstruction. For every

\[
\frac d2<R<a-d
\]

there is the nonempty open `S`-interval

\[
\frac{a+b}{2}<S<2d+R
\]

on which the kernel is trivial.

At the crossing value `R=a-d`, the two upper bounds meet at

\[
2d+R=2a-R=b.
\]

Thus the left and right parameter mechanisms are joined continuously at the level of the sufficient region.

For the canonical slice `S=0.50`, the inequality

\[
0.50<2d+R
\]

already holds at `R=d/2` numerically with margin about `0.00683`; hence the entire former intermediate `R` strip is contained in the A14.2e wedge on that slice (apart from the open endpoint convention used in the theorem statement).

This is a sufficient-region theorem, not a complete classification of all `(R,S)` in the two-shift chamber.

---

## 6. Typed Dieder firewall

The proposed algebraic reflections are

\[
p_1(x)=2a-x,
\qquad
p_2(x)=a+b-x.
\]

Abstractly,

\[
\boxed{p_2\circ p_1(x)=x+d.}
\]

Status of the algebraic identity:

\[
\boxed{\checkmark[M].}
\]

However the proposed operative composition must be domain-typed.

The low-`u` cell

\[
u\in(0,b-S)
\]

has the two `a`-charts

\[
x=a-u\in D_1:=(S-d,a),
\]

and

\[
p_1(x)=a+u\in I_1:=(a,a+b-S).
\]

Thus the typed low-`u` transition is

\[
p_1:D_1\to I_1.
\]

The terminal weighted reflection `p_2` used above is realised only on

\[
H=(a+b-S,S).
\]

But

\[
I_1=(a,a+b-S),
\qquad
H=(a+b-S,S),
\]

so

\[
I_1\cap H=\varnothing
\]

as open intervals. They meet only at the excluded endpoint `a+b-S`.

Therefore the concrete typed composition

\[
p_2\circ p_1
\]

has empty domain for these two realised transitions.

Status:

\[
\boxed{
\text{`p_2 o p_1 = +d' as an operative transition for these cells}
\quad\times[M].
}
\]

This is exactly the distinction between the abstract affine group and the domain-typed pseudogroup. Other cell realisations of related affine maps would require their own domain audit; none is inferred here.

---

## 7. Mechanical regression targets

A conservative regression sweep should verify complete killing at interior points from both sides of the crossing, for example

\[
R\in\{0.105,0.12,0.14,0.15,0.18,0.20\},
\]

with `S` chosen strictly between `L_*` and `U_R`, and `T_0=0.56` whenever admissible.

The regression is evidence only; Proposition A14.2e is proved analytically above.

---

## 8. Status ledger

| Claim | Status |
|---|---|
| A14.2d uses `(c_2/c_3)^2 != 1` in the canonical audit | `checkmark[M]` |
| Algebraic identity `p_2 o p_1(x)=x+d` | `checkmark[M]` |
| Proposed low-`u` `p_1` followed by terminal `p_2` is a realised typed composition | `times[M]` |
| A14.2e wedge is nonempty for every `d/2<R<d` | `checkmark[M]` |
| `ker L_{R,S,T_0}={0}` under (A14.2e.2) | `checkmark[M]` |
| Former intermediate `R` strip is closed on the stated nonempty `S`-wedge | `checkmark[M]` |
| Full two-shift parameter classification | `?[O]` |
| Global recursive pseudogroup termination | `?[O]` |
| R36-A | `?[O]` |
| R30-F | `?[O]` |

---

## 9. Firewall

A14.2e is a finite two-shift sufficient-region theorem for the folded source operator `L`. It does not prove that every admissible `(R,S,T_0)` in the first two-shift chamber has trivial kernel. It does not establish global termination of recursively refined typed affine constraints. It does not prove R36-A, R30-F, strong terminal transport, a polar gauge, Object X, or RH.
