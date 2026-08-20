# P11 End-to-End Referee R36-A14.2c — exact q-domain kill and untyped-density firewall

Date: 2026-08-20

## Purpose / firewall

This note audits the post-A14.2b synthesis concerning the additional middle-`u` reflection

\[
q(x)=d-x,\qquad d:=\tau_3-\tau_2.
\]

It separates: (i) the exact domain where `q` is realised, (ii) the weighted killing mechanism on that domain, and (iii) the behaviour of the **untyped global affine group** obtained by adjoining `q` to the local four-branch group `G_4`.

No global typed-pseudogroup termination theorem, no global two-shift kernel classification, no R36-A, and no R30-F conclusion is made.

Start head:

`7425b5013124e1bc4efc33431ae8658695bf7e53`

---

## 1. Setup

Write

\[
a:=\tau_2=\frac{\log2}{2},\qquad
b:=\tau_3=\frac{\log3}{2},\qquad
d:=b-a=\frac12\log\frac32.
\]

Work in the first genuine two-shift chamber

\[
b\le T_0<2a=\log2,\qquad 0<R<S<T_0.
\]

The canonical folded operator is

\[
(Lh)(u)=\sum_{\tau}c_\tau\Bigl[
\operatorname{sgn}(u-\tau)\mathbf1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr].
\]

Only `a,b` are active.

---

## 2. R36-A14.2c.1 — forward-branch firewall

### Lemma
For every `u>a`, both forward branches are invisible.

Indeed, because `S<T_0<2a`,

\[
u+a>2a>S.
\]

Also `b>a`, hence

\[
u+b>a+b>2a>S.
\]

Therefore neither `u+a` nor `u+b` lies in `(R,S)`.

Status:

\[
\boxed{\text{forward-branch firewall for }u>a\quad\checkmark[M].}
\]

### Audit correction
A proposed proof line used `u+b>2b` for `u\in(a,b)`.  This is false when `u<b`.  The conclusion remains true by the argument above.

---

## 3. R36-A14.2c.2 — exact q-domain

Take `a<u<b` and set

\[
x:=u-a\in(0,d).
\]

Then

\[
b-u=d-x=q(x).
\]

By the forward firewall only the two folded branches can occur.  They are simultaneously visible exactly when

\[
R<x<S,\qquad R<d-x<S.
\]

Hence the exact common visibility domain is

\[
\boxed{
J=(R,S)\cap(d-S,d-R)
=(\max\{R,d-S\},\min\{S,d-R\}).
}
\tag{A14.2c.1}
\]

Since `q` exchanges the two intervals,

\[
q(J)=J,\qquad q^2=\mathrm{id}.
\]

Moreover

\[
\boxed{J\ne\varnothing\iff R<\frac d2<S.}
\tag{A14.2c.2}
\]

Proof: if `x\in J`, then `x>R` and `d-x>R`, hence `d>2R`; likewise `x<S` and `d-x<S`, hence `d<2S`.  Conversely, if `R<d/2<S`, then `d/2\in J`.

Status:

\[
\boxed{\text{exact q-domain and midpoint criterion}\quad\checkmark[M].}
\]

### Negative audit result
The stronger statement

> `J` is nonempty iff `R<d/2`; `S<T_0<\log2` supplies the other inequality

is false.  For example

\[
R=0.02,\qquad S=0.08,\qquad T_0=0.56
\]

has `R<d/2` but `S<d/2`, hence `J=\varnothing`.

Thus

\[
\boxed{\text{R-only q-threshold }R<d/2\quad\times[M].}
\]

The correct condition is `R<d/2<S`.

---

## 4. R36-A14.2c.3 — q is a weighted killing involution

On `J` one has

\[
\operatorname{sgn}(u-a)=+1,\qquad \operatorname{sgn}(u-b)=-1.
\]

Therefore `Lh=0` gives

\[
c_2h(x)-c_3h(q(x))=0,
\]

so

\[
h(q(x))=\lambda h(x),\qquad \lambda:=\frac{c_2}{c_3}.
\]

A14.2b already proves `c_2\ne c_3`, hence `\lambda^2\ne1`.  Since `q:J\to J` is a measure-preserving involution,

\[
h(x)=h(q^2(x))=\lambda h(q(x))=\lambda^2h(x)
\]

for a.e. `x\in J`.  Therefore

\[
\boxed{h=0\quad\text{a.e. on }J.}
\tag{A14.2c.3}
\]

Status:

\[
\boxed{\text{R36-A14.2c q-killed zone}\quad\checkmark[M].}
\]

Thus the additional reflection which destroys the global `G_4` identification is, whenever it is realised on a nonempty common domain, automatically a killing cycle.

The exact visibility/kill statement is

\[
\boxed{R<d/2<S\iff J\ne\varnothing\Longrightarrow h|_J=0.}
\]

This is **not** a dichotomy for full kernel triviality: cases with `J=\varnothing` may still be killed by other cells.

---

## 5. R36-A14.2d — untyped density after adjoining q

Recall

\[
G_4=\langle r,t\rangle,\qquad r(x)=2a-x,\qquad t(x)=x+d.
\]

Adjoin the global affine reflection `q(x)=d-x` **without domain typing** and write

\[
\widetilde G:=\langle r,t,q\rangle.
\]

Then

\[
q\circ r(x)=x+(d-2a).
\]

Hence the translation subgroup contains translations by `d` and `d-2a`, therefore by every element of

\[
\mathbb Zd+\mathbb Z(2a).
\]

Now

\[
\frac{2a}{d}=\frac{2\log2}{\log3-\log2}.
\]

If this ratio were `m/n\in\mathbb Q`, with integers `n\ne0`, then

\[
2n\log2=m(\log3-\log2),
\]

hence

\[
(m+2n)\log2=m\log3,
\]

and therefore

\[
2^{m+2n}=3^m.
\]

Prime valuations force `m=0` and then `n=0`, contradiction.  Thus `2a/d\notin\mathbb Q`.

The additive subgroup `\mathbb Zd+\mathbb Z(2a)` is therefore dense in `\mathbb R`.  Consequently every untyped orbit `\widetilde G\cdot s` is dense, and for every nonempty open interval `I`,

\[
\boxed{|\widetilde G\cdot s\cap I|=\infty.}
\tag{A14.2d.1}
\]

Status:

\[
\boxed{\text{untyped }\langle G_4,q\rangle\text{ has dense orbits}\quad\checkmark[M]_{\rm neg}.}
\]

Therefore a claim that adjoining `q` to the **untyped** global affine group preserves finite orbit intersection with `(R,S)` is `\times[M]`.

### Domain firewall
This does **not** imply density or nontermination for the domain-typed incidence pseudogroup.  There a composition is allowed only where all intermediate images remain in the successive domains.  Thus

\[
\boxed{\text{finite typed-pseudogroup closure / termination}\quad?[O].}
\]

The untyped group remains useful as an over-approximation and no-go diagnostic, but it is not an exact substitute for the typed incidence calculus.

---

## 6. Reproducible regression helper

The companion script

`scripts/p11_a14_typed_regression.py`

generates cells from the canonical indicator predicates and deliberately uses only these licensed rules:

1. one surviving term -> kill its image interval;
2. exactly two surviving terms with the same image interval -> compute the typed affine transition;
3. invariant involution with multiplier square different from `1` -> kill the interval;
4. re-evaluate all full cell constraints after every new kill;
5. never infer pairwise edges from a cell with three or more surviving terms.

For `(R,S,T_0)=(0.10,0.50,0.56)` it returns eight cells and closes the killed union to `(0.10,0.50)` a.e., independently reproducing A14.2b.

It also exercises the qualitative regression points

\[
(0.05,0.50,0.56),\qquad
(0.15,0.50,0.56),\qquad
(0.02,0.08,0.56).
\]

These auxiliary outputs are regression checks only, not new global parameter theorems.  The helper is not yet a global pseudogroup solver: recursive domain-refinement termination and arbitrary longer weighted-cycle search remain open.

---

## 7. Citation / numerical hardening

A synthesis note referred to `R32-C` as if it were a rational-independence input.  The current canonical R32-C is an annular Schur-rewriting statement, so that cross-reference is invalid as written and is not used here.

For reference,

\[
\frac{2a}{d}\approx3.419022582703,
\]

and

\[
|12(2a)-41d|\approx0.005731450502.
\]

Slightly different decimals in the synthesis note are noncanonical and play no role in the proof.

---

## Status firewall

- Forward branches invisible for `u>a` in chamber 2: `checkmark[M]`.
- Exact q-domain `J=(R,S)\cap(d-S,d-R)`: `checkmark[M]`.
- `J\ne\varnothing iff R<d/2<S`: `checkmark[M]`.
- R-only threshold `R<d/2` as sufficient for q-realisation: `times[M]`.
- q-weighted killed zone on `J`: `checkmark[M]`.
- Untyped `\langle G_4,q\rangle` dense-orbit theorem: `checkmark[M]_neg`.
- Finite untyped orbit intersection after adjoining q: `times[M]`.
- Exact domain-typed pseudogroup termination / finite closure: `?[O]`.
- Global two-shift kernel classification: `?[O]`.
- R36-A: `?[O]`.
- R30-F: `?[O]`.
- Strong terminal transport / polar gauge / Object X / RH: unchanged and open.
