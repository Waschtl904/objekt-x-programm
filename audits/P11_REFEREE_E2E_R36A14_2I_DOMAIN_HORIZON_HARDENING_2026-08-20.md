# P11 End-to-End Referee R36-A14.2i — domain / horizon hardening

Date: 2026-08-20

## Purpose / firewall

This note hardens two points around the completed first two-shift classification A14.2i:

1. the four-chart negative construction is an honest element of the operator domain for arbitrary `f in L^2(I)`; no hidden continuity, endpoint, or representative assumption is present;
2. at the source-horizon boundary `T_0=2a`, the old four-chart channel disappears already from horizon extension, before one attributes anything to the newly active prime-power shift `tau_{2,2}=2a`.

The second statement is formulated using an **auxiliary truncated two-shift operator** at horizon `2a`, retaining only the old shifts `a,b`.  This is a diagnostic operator, not the canonical full operator at `T_0=2a`, because the canonical operator has the additional active shift `2a`.

No claim is made here that the full three-shift boundary operator at `T_0=2a` is injective.  That remains open.

Start head:

`9950e590950106e07ca712dd6ef7f0fa976cb436`

---

## 1. Constants and two-shift operator

Put

\[
a=\frac{\log2}{2},\qquad
b=\frac{\log3}{2},\qquad
d=b-a,\qquad c=a+b,
\]

and

\[
c_2=\sqrt{\log2}\,2^{-3/4},\qquad
c_3=\sqrt{\log3}\,3^{-3/4}.
\]

For `0<R<S<T_0` define

\[
(L_{a,b}h)(u)=\sum_{\tau\in\{a,b\}}c_\tau\Bigl[
\operatorname{sgn}(u-\tau)\mathbf1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-\mathbf1_{(R,S)}(u+\tau)h(u+\tau)
\Bigr].
\]

The ambient domain is `L^2(R,S)` and the target is `L^2(0,T_0)`.

---

## 2. Operator-domain boundedness

For one shift `tau`, write

\[
(F_\tau h)(u)=\mathbf1_{(R,S)}(|u-\tau|)h(|u-\tau|)
\]

and

\[
(P_\tau h)(u)=\mathbf1_{(R,S)}(u+\tau)h(u+\tau).
\]

The forward map `u -> u+tau` has at most one preimage, so

\[
\|P_\tau h\|_{L^2(0,T_0)}\le \|h\|_{L^2(R,S)}.
\tag{DH.1}
\]

The fold map `u -> |u-tau|` has at most two preimages, `u=tau-y` and `u=tau+y`.  Therefore

\[
\|F_\tau h\|_{L^2(0,T_0)}^2
\le 2\|h\|_{L^2(R,S)}^2,
\]

hence

\[
\|F_\tau h\|_{L^2(0,T_0)}\le \sqrt2\|h\|_{L^2(R,S)}.
\tag{DH.2}
\]

The sign factor has modulus one away from one null point and changes no norm.  Thus

\[
\boxed{
\|L_{a,b}h\|_{L^2(0,T_0)}
\le (1+\sqrt2)(c_2+c_3)\|h\|_{L^2(R,S)}.
}
\tag{DH.3}
\]

Consequently `L_{a,b}` is a bounded operator on the entire `L^2(R,S)` space.

Status:

\[
\boxed{\text{full }L^2\text{ domain / boundedness}\quad\checkmark[M].}
\]

### Representative firewall

If two representatives of `h` differ on a null set `N`, then after any affine branch map `u -> u+tau`, `u -> tau-u`, or `u -> u-tau`, they differ only on the affine preimage of `N`, which is again null.  A finite union over finitely many branches remains null.

Hence `Lh` is well-defined as an `L^2` equivalence class; no pointwise representative convention is hidden.

---

## 3. A14.2i four-chart construction is domain-valid

In the A14.2i nontrivial region

\[
0<R<a<b<S<T_0<2a,
\]

put

\[
\rho=\frac{c_3}{c_2},\qquad
m=a-\frac d2,
\]

\[
\lambda=\max\{R,T_0-a,c-S,m\}<a,
\qquad I=(\lambda,a).
\]

For arbitrary `f in L^2(I)`, A14.2i defines `h_f` on

\[
J_0=I,\qquad
J_1=2a-I,\qquad
J_2=I+d,\qquad
J_3=c-I
\]

by

\[
h_f(x)=f(x),
\]

\[
h_f(2a-x)=-f(x),
\]

\[
h_f(x+d)=\rho f(x),
\]

\[
h_f(c-x)=-\rho f(x),
\]

and zero elsewhere.

Each chart map has derivative `+1` or `-1`, hence preserves Lebesgue measure.  The four charts are pairwise disjoint up to endpoints.  Therefore

\[
\|h_f\|_2^2
=\|f\|_2^2+\|f\|_2^2+\rho^2\|f\|_2^2+\rho^2\|f\|_2^2
=2(1+\rho^2)\|f\|_2^2.
\tag{DH.4}
\]

Thus

\[
\boxed{h_f\in L^2(R,S)}
\]

for every `f in L^2(I)`.

The finitely many chart endpoints may be assigned arbitrary values.  They form a null set and do not affect either the `L^2` class or the equation `Lh_f=0` a.e.

Together with (DH.3), every such `h_f` is in the operator domain and `Lh_f` is well-defined in `L^2(0,T_0)`.

Status:

\[
\boxed{\text{A14.2i four-chart domain regularity}\quad\checkmark[M].}
\]

No continuity, Sobolev regularity, boundary trace, or pointwise matching condition is required.

---

## 4. What actually changes at `T_0=2a`

A14.2i works under

\[
T_0<2a.
\]

Its kernel channel deliberately uses

\[
\lambda\ge T_0-a
\tag{DH.5}
\]

so that for `x in I=(lambda,a)` the upper source

\[
u=a+x
\]

satisfies

\[
u>T_0.
\]

This is the source firewall excluding the dangerous upper `a`-fold source of the base chart `J_0`.

At the horizon boundary

\[
T_0=2a,
\]

condition (DH.5) becomes

\[
\lambda\ge a.
\]

But the construction requires `lambda<a`.  Hence the interval `I=(lambda,a)` is forced empty.

Therefore the A14.2i four-chart constructor cannot extend nontrivially to the boundary merely by continuity in `T_0`.

More concretely, for any `x<a` the source

\[
u=a+x<2a
\]

becomes available.  On the old four-chart geometry with `x>m>d`, its `a`-fold evaluates exactly `h(x)`, while the other old support values do not supply the cancellation that was present on the three interior source families.  This is the mechanism hidden by the strict inequality `T_0<2a`.

Status:

\[
\boxed{\text{old four-chart channel degenerates at }T_0=2a\quad\checkmark[M].}
\]

Firewall: this is a **horizon-opening statement**, not yet a statement about the newly active shift `tau_{2,2}=2a`.

---

## 5. Auxiliary boundary two-shift theorem

Define the auxiliary boundary-horizon operator

\[
\widetilde L_{a,b}^{(2a)}:L^2(R,S)\to L^2(0,2a)
\]

by the same formula as `L_{a,b}`, retaining only the old shifts `a,b`, with

\[
0<R<S<2a.
\]

### Proposition

For every

\[
\boxed{0<R<S<2a}
\]

one has

\[
\boxed{\ker \widetilde L_{a,b}^{(2a)}=\{0\}.}
\tag{DH.6}
\]

### Step 1: kill the lower part `y<a`

For `y in (R,min\{S,a\})`, choose

\[
u=a+y<2a.
\]

The `a`-forward argument is `2a+y>S`, and the `b`-forward argument is `a+b+y>2a>S`.  The exact equation is

\[
c_2h(y)
+c_3\operatorname{sgn}(y-d)
\mathbf1_{(R,S)}(|y-d|)h(|y-d|)=0.
\tag{DH.7}
\]

For `y<d`, the only possible cycle is the involution

\[
q(y)=d-y.
\]

On its common typed domain,

\[
h(q(y))=\frac{c_2}{c_3}h(y),
\]

and `q^2=id`.  Since

\[
(c_2/c_3)^2\ne1,
\]

the common domain is killed.  Outside it the equation is one-term.  Thus the whole part below `d` is killed.

For `y>d`, the active predecessor is `y-d<y`.  Finite upward `d`-layer induction then kills all of

\[
(R,\min\{S,a\}).
\tag{DH.8}
\]

### Step 2a: if `S<=a`, we are done

This is immediate from (DH.8).

### Step 2b: `a<S<=b`

The lower part `(R,a)` is dead.  For `y in (a,S)`, choose

\[
u=y-a.
\]

The `a`-folded value `2a-y<a` is dead.  The `b`-forward value is

\[
y+d>b\ge S,
\]

so it is invisible.  The only possible remaining partner is

\[
p(y)=c-y.
\]

If `S<=c/2`, then `p(y)>=S` and every equation is one-term.  If `S>c/2`, the interval

\[
H=(c-S,S)
\]

is `p`-invariant; below `H` the equation is one-term, and on `H` it reduces to

\[
c_2h(y)+c_3h(p(y))=0.
\]

Since `p^2=id` and `(c_2/c_3)^2!=1`, `H` is killed.  Hence the whole annulus is killed.

### Step 2c: `S>b`

First kill the upper part.  For `y in (max\{R,b\},S)`, again use `u=y-a`.  Both folded partners

\[
2a-y<a,
\qquad
c-y<a
\]

lie in the dead lower region whenever active.  Thus

\[
c_2h(y)+c_3\mathbf1_{(R,S)}(y+d)h(y+d)=0.
\tag{DH.9}
\]

The top `d`-layer has no successor; finite downward induction kills all of

\[
(max\{R,b\},S).
\tag{DH.10}
\]

On the remaining middle interval `(max\{R,a\},min\{S,b\})`, the `a`-fold is below `a` and dead, while every active successor `y+d` lies above `b` and is dead by (DH.10).  The equation reduces to the weighted reflection

\[
c_2h(y)+c_3h(c-y)=0
\]

on its invariant typed part, with one-term killing outside it.  The same nonunit involution argument kills the middle interval.

This proves (DH.6).

Status:

\[
\boxed{\text{auxiliary old-shift boundary-horizon injectivity}\quad\checkmark[M].}
\]

---

## 6. The newly active prime-power shift must be separated from horizon opening

At the exact boundary `T_0=2a`, the canonical finite-shift operator also activates

\[
\tau_{2,2}=\log2=2a,
\]

with coefficient

\[
c_{2,2}=\sqrt{\log2}\,2^{-3/2}>0.
\]

Because `u in (0,2a)` and `S<2a`, its forward branch is invisible, while its folded branch is

\[
(K_{2a}h)(u)
=-c_{2,2}\mathbf1_{(R,S)}(2a-u)h(2a-u).
\tag{DH.11}
\]

The map `u -> 2a-u` is one-to-one on `(0,2a)`, so in contrast to a generic fold,

\[
\boxed{
\|K_{2a}h\|_{L^2(0,2a)}
=c_{2,2}\|h\|_{L^2(R,S)}.
}
\tag{DH.12}
\]

Hence `K_{2a}` is injective.

For the auxiliary boundary operator,

\[
h\in\ker\widetilde L_{a,b}^{(2a)}
\quad\Longrightarrow\quad
(\widetilde L_{a,b}^{(2a)}+K_{2a})h=K_{2a}h,
\]

so

\[
\ker\widetilde L_{a,b}^{(2a)}
\cap
\ker(\widetilde L_{a,b}^{(2a)}+K_{2a})
=\{0\}.
\]

This intersection statement is true but, because (DH.6) already gives a trivial first kernel, it is not the mechanism responsible for the old interior four-chart channel disappearing.

The correct causal ledger is:

- **horizon opening** `T_0<2a -> T_0=2a`: already destroys the A14.2i four-chart channel and makes the old-shift boundary truncation injective;
- **prime-power activation** `tau_{2,2}=2a`: adds the injective reflected term (DH.11), but can in principle cancel against the old-shift operator on new vectors.

Therefore one may **not** infer injectivity of the full canonical three-shift boundary operator merely from (DH.6) and injectivity of `K_{2a}`.

Status:

\[
\boxed{\text{full canonical }T_0=2a\text{ three-shift kernel classification}\quad ?[O].}
\]

---

## 7. Status ledger

\[
\boxed{L_{a,b}:L^2(R,S)\to L^2(0,T_0)\text{ bounded}\quad\checkmark[M]}
\]

\[
\boxed{\text{A14.2i four-chart construction is operator-domain valid}\quad\checkmark[M]}
\]

\[
\boxed{\text{endpoint / representative issues are null-set harmless}\quad\checkmark[M]}
\]

\[
\boxed{\text{A14.2i four-chart channel degenerates at }T_0=2a\quad\checkmark[M]}
\]

\[
\boxed{\ker\widetilde L_{a,b}^{(2a)}=\{0\}\text{ for all }0<R<S<2a\quad\checkmark[M]}
\]

\[
\boxed{K_{2a}\text{ is a scaled }L^2\text{ isometry}\quad\checkmark[M]}
\]

Still open:

\[
\boxed{\ker L_{\{a,b,2a\}}\text{ at }T_0=2a\quad ?[O]}
\]

\[
\boxed{\text{higher-shift chambers }T_0>2a\quad ?[O]}
\]

\[
\boxed{\text{global typed-pseudogroup termination}\quad ?[O]}
\]

\[
\boxed{\text{R36-A}\quad ?[O]}
\]

\[
\boxed{\text{R30-F}\quad ?[O]}
\]
