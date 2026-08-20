# P11 End-to-End Referee R36-A14.2b — typed incidence regression at `(0.10,0.50,0.56)`

Date: 2026-08-20

## Purpose and firewall

This note performs the first concrete R36-A14.2 regression with the domain typing demanded by
R36-A14.2a.  It starts from the canonical folded odd-sector operator

\[
(Lh)(u)=\sum_{\tau}c_\tau\Bigl[
\operatorname{sgn}(u-\tau)\mathbf 1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf 1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr]
\]

and treats every visibility cell as a typed affine constraint before any scalar compression.

The result is specific to

\[
(R,S,T_0)=(0.10,0.50,0.56).
\]

It does **not** prove a global two-shift kernel classification, R36-A, R30-F, strong terminal
transport, Object X, or RH.

---

## 1. Architecture hardening: constraints first, transitions second

Let a visibility cell `C` carry the exact relation

\[
\sum_{j=1}^{m_C} a_j h(\chi_j(u))=0,
\qquad u\in C,
\]

where each chart `\chi_j(u)=\alpha_j u+\beta_j` is typed by its source cell `C` and image interval
`I_j=\chi_j(C)\subset(R,S)`.

The exact A14.2 object is therefore most safely represented as a **domain-typed weighted affine
constraint hypergraph / pseudogroup**:

- vertices: typed branch charts `(C,\chi_j,I_j,a_j)`;
- hyperedges: the full cell relations, with all simultaneously surviving terms retained;
- one surviving term: its image interval is killed;
- two surviving terms: and only then, a genuine weighted affine transition may be formed;
- three or more surviving terms: no pairwise multiplier relation may be inferred without an
  additional elimination step.

Indeed

\[
a h(x)+b h(y)+c h(z)=0
\]

does not imply `h(y)=-(a/b)h(x)` unless the third term is already known to vanish.

Hence the naive rule

> every pair of co-visible branches may immediately be joined by a weighted transition edge

is false if interpreted as a mathematical consequence of the cell equation.

Status:

\[
\boxed{\text{naive pairwise-edge reduction on }m_C\ge3\quad\times[M].}
\]

The typed constraint-hypergraph formulation above is an exact repackaging of A14.1 and is the
working architecture used below.

Status:

\[
\boxed{\text{typed affine constraint-hypergraph reduction}\quad\checkmark[M].}
\]

---

## 2. Regression constants

Write

\[
a:=\tau_2=\frac{\log2}{2}\approx0.346573590280,
\qquad
b:=\tau_3=\frac{\log3}{2}\approx0.549306144334,
\]

\[
d:=b-a=\frac12\log\frac32\approx0.202732554054.
\]

The only active shifts are `a,b`, because

\[
b<T_0=0.56<\log2=2a.
\]

The corresponding positive weights are

\[
c_2=\sqrt{\log2}\,2^{-3/4},
\qquad
c_3=\sqrt{\log3}\,3^{-3/4},
\qquad
r:=\frac{c_2}{c_3}.
\]

Moreover `c_2>c_3`.  One exact proof is to consider

\[
f(x)=\frac{\log x}{x^{3/2}}.
\]

For `x\ge2`,

\[
f'(x)=x^{-5/2}\left(1-\frac32\log x\right)<0,
\]

because `\log2>2/3`.  Hence `f(2)>f(3)`, i.e. `c_2^2>c_3^2`, so

\[
\boxed{r^2\ne1.}
\tag{A14.2b.1}
\]

Numerically `r\approx1.07661133648`.

---

## 3. Complete visibility-cell table

For `(R,S,T_0)=(0.10,0.50,0.56)` the complete positive breakpoint list is

\[
0,\ b-S,\ S-a,\ a-R,\ a,\ a+R,\ b-R,\ b,\ T_0,
\]

i.e.

\[
\begin{aligned}
0
&<0.049306144334
<0.153426409720
<0.246573590280
<0.346573590280\\
&<0.446573590280
<0.449306144334
<0.549306144334
<0.56.
\end{aligned}
\]

Thus there are eight visibility cells.  The exact equations and chart images are:

| Cell | `u`-interval | exact cell equation | chart images in `(R,S)` |
|---|---|---|---|
| `C1` | `(0,b-S)` | `-c2 h(a-u)-c2 h(a+u)=0` | `a-u in (S-d,a)`, `a+u in (a,a+b-S)` |
| `C2` | `(b-S,S-a)` | `-c2 h(a-u)-c2 h(a+u)-c3 h(b-u)=0` | `a-u in (2a-S,S-d)`, both other charts in `H=(a+b-S,S)` |
| `C3` | `(S-a,a-R)` | `-c2 h(a-u)-c3 h(b-u)=0` | `a-u in (R,2a-S)`, `b-u in (d+R,a+b-S)` |
| `C4` | `(a-R,a)` | `-c3 h(b-u)=0` | `b-u in (d,d+R)` |
| `C5` | `(a,a+R)` | `-c3 h(b-u)=0` | `b-u in (d-R,d)` |
| `C6` | `(a+R,b-R)` | `+c2 h(u-a)-c3 h(b-u)=0` | both charts in `J=(R,d-R)` |
| `C7` | `(b-R,b)` | `+c2 h(u-a)=0` | `u-a in (d-R,d)` |
| `C8` | `(b,T_0)` | `+c2 h(u-a)=0` | `u-a in (d,T_0-a)` |

The narrow cell `C6` is nonempty because

\[
d>2R,
\qquad
0.202732554054>0.20.
\tag{A14.2b.2}
\]

No determinant or untyped orbit closure is used.

---

## 4. Mechanical typed closure

The following closure uses only the exact one-term rule, typed two-term transitions, and the
already-booked weighted-involution lemma.  Null-set boundaries are irrelevant because every chart
has slope `\pm1` and therefore preserves null sets.

### Step 1 — one-term cells kill the central band

From `C4` and `C5`,

\[
h=0\quad\text{a.e. on }(d-R,d+R).
\tag{A14.2b.3}
\]

Numerically,

\[
(d-R,d+R)=(0.102732554054,0.302732554054).
\]

### Step 2 — the new reflection `q(x)=d-x` kills the small left remainder

On `C6`, set

\[
x=u-a\in J:=(R,d-R).
\]

Then

\[
b-u=d-x=:q(x),
\]

and `q(J)=J`, `q^2=id`.  The cell equation is

\[
c_2h(x)-c_3h(q(x))=0,
\]

hence

\[
h(q(x))=r h(x).
\]

By (A14.2b.1) and the weighted-involution lemma,

\[
\boxed{h=0\quad\text{a.e. on }J=(R,d-R).}
\tag{A14.2b.4}
\]

Combining (A14.2b.3) and (A14.2b.4),

\[
h=0\quad\text{a.e. on }(R,d+R).
\tag{A14.2b.5}
\]

### Step 3 — `C3` propagates the killed interval to the right

On `C3`, set

\[
x=a-u\in(R,2a-S).
\]

The first chart lies inside the already-killed interval `(R,d+R)`; numerically

\[
2a-S\approx0.193147180560<d+R\approx0.302732554054.
\]

The second chart is

\[
b-u=x+d.
\]

Therefore the two-term relation on `C3` forces

\[
\boxed{h=0\quad\text{a.e. on }(d+R,a+b-S).}
\tag{A14.2b.6}
\]

Numerically this is

\[
(0.302732554054,0.395879734614).
\]

Thus

\[
h=0\quad\text{a.e. on }(R,a+b-S).
\tag{A14.2b.7}
\]

### Step 4 — the reduced `C2` constraint gives a second weighted involution

On `C2`, the chart `a-u` ranges over

\[
(2a-S,S-d)
\approx(0.193147180560,0.297267445946),
\]

which is contained in the killed interval from (A14.2b.7).  Therefore the original three-term
constraint reduces, legitimately and domain-typed, to

\[
c_2h(a+u)+c_3h(b-u)=0.
\]

Set

\[
z:=a+u\in H:=(a+b-S,S).
\]

Then

\[
b-u=a+b-z=:p(z).
\]

The interval `H` is invariant under `p`, and `p^2=id`.  Hence

\[
h(p(z))=-r h(z).
\]

Again `r^2\ne1`, so the weighted-involution lemma gives

\[
\boxed{h=0\quad\text{a.e. on }H=(a+b-S,S).}
\tag{A14.2b.8}
\]

Numerically

\[
H=(0.395879734614,0.50).
\]

The intervals in (A14.2b.7) and (A14.2b.8) cover `(R,S)` up to their common boundary point.
Therefore

\[
\boxed{h=0\quad\text{a.e. on }(R,S).}
\tag{A14.2b.9}
\]

Cells `C1`, `C7`, and `C8` are redundant for this proof, but their independently enumerated
signatures agree with the closure and provide regression checks.

---

## 5. Independent mechanical regression certificate

A domain-typed enumerator using the canonical indicator predicates, with no hand-entered cell
signature, returns the eight cells above.  Applying only these rules

1. one surviving term -> kill its image interval;
2. two surviving terms -> form the typed affine transition;
3. invariant involution with multiplier square `!=1` -> kill the invariant interval;
4. re-evaluate the remaining constraints after each new killed interval;

produces the following proof-friendly event sequence:

```text
C4  one-term kill          (0.202732554054, 0.302732554054)
C5  one-term kill          (0.102732554054, 0.202732554054)
C6  weighted involution    (0.100000000000, 0.102732554054)
C3  propagated one-term    (0.302732554054, 0.395879734614)
C2  weighted involution    (0.395879734614, 0.500000000000)
```

The normalized killed union is exactly `(0.10,0.50)` up to endpoints.  This mechanically
reproduces the hand-derived closure without using a determinant or a global untyped group.

---

## 6. Proposition R36-A14.2b — regression-point kernel triviality

For

\[
(R,S,T_0)=(0.10,0.50,0.56),
\]

the folded two-shift odd-sector operator satisfies

\[
\boxed{
\ker L_{0.10,0.50,0.56}=\{0\}.
}
\tag{A14.2b.10}
\]

### Proof

If `Lh=0`, the eight exact visibility-cell constraints above hold a.e.  Steps 1--4 imply
`h=0` a.e. on `(R,S)`.  Hence the `L^2(R,S)` class of `h` is zero.  `\square`

Status:

\[
\boxed{\text{R36-A14.2b regression-point kernel triviality}\quad\checkmark[M].}
\]

---

## Status firewall

- A14.2 architecture as typed affine constraint hypergraph/pseudogroup: `checkmark[M]` as the exact
  reduction formalism used here.
- Naive pairwise transition edge from an unreduced `m_C>=3` cell: `times[M]`.
- Regression point `(0.10,0.50,0.56)`: `ker L={0}` `checkmark[M]`.
- The additional reflection `q(x)=d-x` is not merely a global-group obstruction here: on `C6` it
  generates a concrete weighted killing cycle.
- Global A14.2 domain-typed closure: `?[O]`.
- Global two-shift kernel classification: `?[O]`.
- R36-A: `?[O]`.
- R30-F: `?[O]`.
- Strong terminal transport / polar gauge / Object X / RH: unchanged and open.
