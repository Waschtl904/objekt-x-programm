# P11 End-to-End Referee R36-A14.3a — canonical three-shift boundary injectivity

Date: 2026-08-20

## Purpose / firewall

This note closes the exact first three-shift boundary

\[
T_0=2a=\log 2,
\qquad
0<R<S<2a,
\]

for the canonical folded finite-shift operator with active shifts

\[
a=\tau_{2,1}=\frac{\log2}{2},
\qquad
b=\tau_{3,1}=\frac{\log3}{2},
\qquad
2a=\tau_{2,2}=\log2.
\]

The theorem proved below is

\[
\boxed{
0<R<S<2a
\Longrightarrow
\ker L_{\{a,b,2a\}}=\{0\}.
}
\]

This is an exact boundary theorem only.  It does **not** imply injectivity in every higher-shift chamber `T_0>2a`, global typed-pseudogroup termination, R36-A, R30-F, Objekt X, or RH.

Start head:

`885489d482b43ce5024a4d655a00322c7935e258`

---

## 1. Constants and order relations

Put

\[
a=\frac{\log2}{2},\qquad
b=\frac{\log3}{2},\qquad
T:=2a=\log2,
\]

\[
d:=b-a=\frac12\log\frac32,
\qquad
e:=2a-b=\frac12\log\frac43,
\]

and

\[
\delta:=d-e=2b-3a=\frac12\log\frac98.
\]

Then

\[
a=d+e=2e+\delta,
\qquad
d=e+\delta.
\]

Since

\[
1<\frac98<\frac43<\frac32<2,
\]

one has

\[
0<\delta<e<d<a<T.
\tag{A14.3a.1}
\]

Write the three positive coefficients as

\[
p:=c_{2,1}=\sqrt{\log2}\,2^{-3/4},
\]

\[
r:=c_{3,1}=\sqrt{\log3}\,3^{-3/4},
\]

\[
q:=c_{2,2}=\sqrt{\log2}\,2^{-3/2}.
\]

In particular

\[
0<q<p,
\qquad p^2-q^2\ne0.
\tag{A14.3a.2}
\]

---

## 2. Canonical boundary operator and exact E/U split

Extend `h in L^2(R,S)` by zero to all of `(0,T)`.

At `T_0=T=2a`, the canonical three-shift operator is

\[
(Lh)(u)
=
\sum_{\tau\in\{a,b,T\}}c_\tau
\Bigl[
\operatorname{sgn}(u-\tau)h(|u-\tau|)-h(u+\tau)
\Bigr],
\]

where every value outside `(R,S)` is understood as zero.

For `x in (0,a)` there are two source charts.

### 2.1 Lower source family: `u=a+x`

The `a`-shift contributes `+p h(x)`, the `b`-shift contributes

\[
r\operatorname{sgn}(x-d)h(|x-d|),
\]

and the new `T=2a` fold contributes `-q h(a-x)`.
All forward branches are outside `(0,T)`.
Thus every kernel vector satisfies

\[
\boxed{
E(x):\quad
p h(x)
+r\operatorname{sgn}(x-d)h(|x-d|)
-q h(a-x)=0
}
\tag{A14.3a.3}
\]

for a.e. `x in (0,a)`.

### 2.2 Upper source family: `u=a-x`

A direct branch check gives

\[
\boxed{
U(x):\quad
p\bigl[h(x)+h(2a-x)\bigr]
+r\bigl[h(d+x)+h(a+b-x)\bigr]
+q h(a+x)=0
}
\tag{A14.3a.4}
\]

for a.e. `x in (0,a)`, again with zero extension outside `(R,S)`.

The proof will first use `E` to kill the whole lower half `(0,a)`, and then use the reduced `U` equation to kill the upper half `(a,2a)`.

Status:

\[
\boxed{\text{exact E/U source decomposition}\quad\checkmark[M].}
\]

---

## 3. Abstract typed irrational-rotation unique-continuation lemma

The same lemma will be used twice.

### Lemma A14.3a-UC

Let `ell>0`, `0<alpha<ell`, and assume

\[
\frac{\alpha}{\ell}\notin\mathbb Q.
\]

Let

\[
R_\alpha(t)=t+\alpha\pmod\ell
\]

be the irrational rotation of the circle `C_ell`.
Let `A,B in GL_2(C)` commute.
Suppose a measurable vector field

\[
X:C_\ell\to\mathbb C^2
\]

satisfies, a.e.,

\[
X(R_\alpha t)=A X(t)
\qquad (0<t<\ell-\alpha),
\tag{UC.1}
\]

and

\[
X(R_\alpha t)=B X(t)
\qquad (\ell-\alpha<t<\ell).
\tag{UC.2}
\]

Let

\[
V:=\{(0,z):z\in\mathbb C\}.
\]

Assume

1. the first component of `X` vanishes a.e. on some nonempty open interval `G subset C_ell`;
2. `A` and `B` do not both preserve `V`.

Then

\[
\boxed{X=0\quad\text{a.e. on }C_\ell.}
\tag{UC.3}
\]

### Proof

Let `k_j/n_j` and `k_{j+1}/n_{j+1}` be consecutive convergents of `alpha/ell`, with `j` large.
Then

\[
\varepsilon_j:=n_j\alpha-k_j\ell\to0,
\]

and

\[
n_jk_{j+1}-n_{j+1}k_j=\pm1.
\tag{UC.4}
\]

For sufficiently large `j`, both rotations `R_\alpha^{n_j}` and `R_\alpha^{n_{j+1}}` return a positive-length subinterval of `G` back into `G`.
After removing the finitely many itinerary-boundary points, the number of wraps is constant on each such return interval.
Because `A` and `B` commute, the two return matrices are

\[
G_j=A^{n_j-k_j}B^{k_j},
\qquad
G_{j+1}=A^{n_{j+1}-k_{j+1}}B^{k_{j+1}}.
\tag{UC.5}
\]

The exponent vectors

\[
(n_j-k_j,k_j),
\qquad
(n_{j+1}-k_{j+1},k_{j+1})
\]

also have determinant `+-1`, since the transformation `(n,k)->(n-k,k)` is unimodular.
Hence they form a `Z^2` basis.

If both `G_j` and `G_{j+1}` preserved `V`, then, because they commute and are invertible, every integer product of their powers would preserve `V`.  The unimodular basis property would therefore force both generators `A` and `B` to preserve `V`, contrary to assumption 2.

Thus for every sufficiently large consecutive pair, at least one return matrix, call it `G`, does not preserve `V`.
Choose its positive-length return interval `I subset G` with `R_\alpha^n(I) subset G` and constant itinerary.
For a.e. `t in I`,

\[
X(t)\in V,
\qquad
X(R_\alpha^n t)=G X(t)\in V.
\]

Since `G(V)` is a one-dimensional line different from `V`, one has

\[
V\cap G^{-1}V=\{0\}.
\]

Therefore

\[
X=0\quad\text{a.e. on }I.
\tag{UC.6}
\]

All one-step cocycle matrices are invertible, so zero propagates both forward and backward under every iterate of the rotation.
The irrational rotation is minimal; the translates of the nonempty interval `I` cover the circle.
After discarding the countable union of null exceptional sets,

\[
X=0\quad\text{a.e. on }C_\ell.
\]

This proves the lemma.  `square`

Firewall: the lemma uses only the **actual piecewise typed cocycle** `(UC.1)-(UC.2)`.  No untyped affine group composition is promoted.

Status:

\[
\boxed{\text{typed irrational-rotation UC lemma}\quad\checkmark[M].}
\]

---

## 4. Arithmetic irrationalities

The two circle rotations below are irrational for elementary prime-valuation reasons.

### 4.1 Lower circle

If `e/d=m/n in Q_{>0}`, then

\[
\left(\frac43\right)^n
=
\left(\frac32\right)^m.
\]

The exponent of the prime `2` would give

\[
2n=-m,
\]

impossible for positive integers `m,n`.
Thus

\[
\boxed{e/d\notin\mathbb Q.}
\tag{A14.3a.5}
\]

### 4.2 Upper circle

If `delta/e=m/n in Q_{>0}`, then

\[
\left(\frac98\right)^n
=
\left(\frac43\right)^m.
\]

The exponent of `2` gives

\[
-3n=2m,
\]

again impossible.
Thus

\[
\boxed{\delta/e\notin\mathbb Q.}
\tag{A14.3a.6}
\]

---

## 5. Lower half: E is an irrational matrix cocycle on `C_d`

Let

\[
g:=h|_{(0,a)},
\qquad
w(x):=
\binom{g(x)}{g(a-x)}.
\]

Because `h` is zero below `R`, the first component satisfies

\[
g(x)=0
\quad\text{a.e. on }(0,\min\{R,a\}).
\tag{A14.3a.7}
\]

### 5.1 Two typed reflection matrices

For `0<x<d`, equations `E(x)` and `E(d-x)` give

\[
w(d-x)=R_d w(x),
\tag{A14.3a.8}
\]

where

\[
R_d=
\begin{pmatrix}
 p/r & -q/r\\[1mm]
 (p^2-r^2)/(qr) & -p/r
\end{pmatrix}.
\]

For `0<x<e`, equations `E(a-x)` and `E(d+x)` give

\[
w(e-x)=R_e w(x),
\tag{A14.3a.9}
\]

where

\[
R_e=
\begin{pmatrix}
 q/r & -p/r\\[1mm]
 (q^2-r^2)/(pr) & -q/r
\end{pmatrix}.
\]

Direct multiplication gives

\[
R_d^2=R_e^2=I.
\tag{A14.3a.10}
\]

Let

\[
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Tautologically

\[
w(a-x)=Pw(x).
\tag{A14.3a.11}
\]

### 5.2 Genuine translations

Since `delta=d-e`, composing only domain-valid reflections yields

\[
\boxed{
w(x+\delta)=M_\delta w(x),
\qquad
M_\delta:=R_dR_e,
\qquad 0<x<e.
}
\tag{A14.3a.12}
\]

Similarly, since `e=a-d`,

\[
\boxed{
w(x+e)=E_0w(x),
\qquad
E_0:=PR_d,
\qquad 0<x<d.
}
\tag{A14.3a.13}
\]

The matrices are

\[
E_0=
\begin{pmatrix}
(p^2-r^2)/(qr) & -p/r\\[1mm]
p/r & -q/r
\end{pmatrix},
\]

and

\[
M_\delta=
\begin{pmatrix}
q(p^2-q^2+r^2)/(pr^2) & (q^2-p^2)/r^2\\[1mm]
(p^2-q^2)/r^2 & p(-p^2+q^2+r^2)/(qr^2)
\end{pmatrix}.
\]

A direct algebra check gives

\[
\det E_0=\det M_\delta=1,
\qquad
E_0M_\delta=M_\delta E_0.
\tag{A14.3a.14}
\]

Moreover

\[
(E_0)_{12}=-\frac pr\ne0.
\tag{A14.3a.15}
\]

### 5.3 Circle cocycle

Restrict `w` to the circle `(0,d)` and rotate by `e` modulo `d`.
Because `d=e+delta`,

- for `0<x<delta`, there is no wrap and `(A14.3a.13)` gives
  \[
  w(x+e)=E_0w(x);
  \]
- for `delta<x<d`, the rotated point is `x-d+e=x-delta`; by inverting `(A14.3a.12)`,
  \[
  w(x-delta)=M_\delta^{-1}w(x).
  \]

Thus this is exactly the lemma A14.3a-UC with

\[
ell=d,\qquad alpha=e,\qquad A=E_0,\qquad B=M_\delta^{-1}.
\]

The matrices commute and are invertible by `(A14.3a.14)`; `e/d` is irrational by `(A14.3a.5)`; and the first component vanishes on a nonempty interval because `R>0`.
Finally `(E_0)_{12}\ne0`, so the two generators do not both preserve the vertical line.

Therefore

\[
w=0\quad\text{a.e. on }(0,d).
\tag{A14.3a.16}
\]

The first component kills `g` on `(0,d)`.  The second component kills `g(a-x)` for `x in (0,d)`, i.e. `g` on `(e,a)`.
Since `e<d`, these intervals cover `(0,a)`.
Hence

\[
\boxed{h=0\quad\text{a.e. on }(0,a).}
\tag{A14.3a.17}
\]

Status:

\[
\boxed{\text{lower-half typed irrational-rotation UC}\quad\checkmark[M].}
\]

---

## 6. Upper half after the lower kill

If `S<=a`, `(A14.3a.17)` already proves `h=0` everywhere.
Assume henceforth `S>a`.

Define

\[
k(x):=h(a+x),
\qquad 0<x<a,
\]

and extend `k` by zero outside `(0,a)`.
Since the lower half is zero, `U(x)` reduces to

\[
qk(x)+pk(a-x)+rk(x-e)+rk(b-x)=0,
\tag{A14.3a.18}
\]

with zero extension handling inactive arguments.

Now reflect

\[
l(z):=k(a-z),
\]

again with zero extension outside `(0,a)`.
Then `(A14.3a.18)` becomes

\[
\boxed{
F(z):\quad
ql(z)+pl(a-z)+rl(e+z)+rl(e-z)=0,
\qquad 0<z<a.
}
\tag{A14.3a.19}
\]

Because `h` is zero above `S`, one has the genuine left support gap

\[
\boxed{
l(z)=0
\quad\text{a.e. on }(0,2a-S).
}
\tag{A14.3a.20}
\]

---

## 7. Upper half: F is an irrational matrix cocycle on `C_e`

### 7.1 Low and high relations

For `0<z<e`, applying `F` at `a-z` gives

\[
ql(a-z)+pl(z)=0.
\tag{A14.3a.21}
\]

Substituting this into `F(z)` gives

\[
\boxed{
l(e+z)+l(e-z)=\kappa l(z),
\qquad
\kappa:=\frac{p^2-q^2}{qr}>0.
}
\tag{A14.3a.22}
\]

For `d<z<a`, both `r`-terms in `F(z)` are invisible and one has the high reflection

\[
\boxed{ql(z)+pl(a-z)=0.}
\tag{A14.3a.23}
\]

### 7.2 Delta-translation on `W`

Define

\[
W(t):=\binom{l(t)}{l(e-t)},
\qquad 0<t<e,
\]

and

\[
\mu:=\frac pq>1.
\]

For `0<t<e-delta`, use `(A14.3a.22)` at `e-t` and at `t+delta`, together with the high reflection `(A14.3a.23)`.  One obtains

\[
\boxed{
W(t+\delta)=A_UW(t),
}
\tag{A14.3a.24}
\]

where

\[
A_U=
\frac1\mu
\begin{pmatrix}
1 & -\kappa\\[1mm]
\kappa & \mu^2-\kappa^2
\end{pmatrix}.
\tag{A14.3a.25}
\]

In particular

\[
\det A_U=1,
\qquad
(A_U)_{12}=-\kappa/\mu\ne0.
\tag{A14.3a.26}
\]

### 7.3 The complementary translation `eta=e-delta`

Put

\[
\eta:=e-\delta>0.
\]

For `0<x<delta`, the two middle equations at `e+x` and `d-x`, together with the high reflection, give

\[
\binom{l(e+x)}{l(e+\delta-x)}
=N\binom{l(x)}{l(\delta-x)},
\tag{A14.3a.27}
\]

with

\[
N=\frac\mu\kappa
\begin{pmatrix}
\mu&-1\\[1mm]
-1&\mu
\end{pmatrix}.
\]

Combining `(A14.3a.27)` with the low recurrence `(A14.3a.22)`, define

\[
Q=
\begin{pmatrix}
1&0\\[1mm]
(\kappa^2-\mu^2)/\kappa & \mu/\kappa
\end{pmatrix},
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{A14.3a.28}
\]

Then

\[
W(x)=Q
\binom{l(x)}{l(\delta-x)},
\]

so

\[
W(\delta-x)=QPQ^{-1}W(x).
\]

Using the tautology `W(e-y)=PW(y)` and `x+eta=e-(delta-x)`, one gets

\[
\boxed{
W(x+\eta)=N_\eta W(x),
\qquad
N_\eta:=PQPQ^{-1},
\qquad 0<x<\delta.
}
\tag{A14.3a.29}
\]

A direct multiplication gives

\[
\det N_\eta=1,
\qquad
A_UN_\eta=N_\eta A_U.
\tag{A14.3a.30}
\]

### 7.4 Circle cocycle

Now restrict `W` to the circle `(0,e)` and rotate by `delta` modulo `e`.
Since `e=eta+delta`,

- for `0<t<eta`, no wrap occurs and `(A14.3a.24)` gives
  \[
  W(t+\delta)=A_UW(t);
  \]
- for `eta<t<e`, the rotated point is `t+delta-e=t-eta`; by inverting `(A14.3a.29)`,
  \[
  W(t-\eta)=N_\eta^{-1}W(t).
  \]

Thus A14.3a-UC applies with

\[
ell=e,\qquad alpha=\delta,\qquad A=A_U,\qquad B=N_\eta^{-1}.
\]

The matrices commute and are invertible by `(A14.3a.26)` and `(A14.3a.30)`; `delta/e` is irrational by `(A14.3a.6)`; the first component vanishes on a nonempty interval by `(A14.3a.20)`; and `(A_U)_{12}\ne0`.
Therefore

\[
W=0\quad\text{a.e. on }(0,e).
\tag{A14.3a.31}
\]

Hence `l=0` on `(0,e)`.
Then `(A14.3a.22)` gives `l(e+z)=0` for `0<z<e`, so `l=0` on `(e,2e)`.
The high reflection `(A14.3a.23)` gives `l=0` on `(d,a)`.
Since

\[
d<2e<a,
\]

these intervals cover `(0,a)`.
Thus

\[
\boxed{h=0\quad\text{a.e. on }(a,2a).}
\tag{A14.3a.32}
\]

Status:

\[
\boxed{\text{upper-half typed irrational-rotation UC}\quad\checkmark[M].}
\]

---

## 8. Main theorem

Combining `(A14.3a.17)` and `(A14.3a.32)` gives:

### Proposition R36-A14.3a — canonical first three-shift boundary injectivity

Assume

\[
\boxed{0<R<S<2a,\qquad T_0=2a.}
\]

For the canonical folded operator with shifts

\[
\{a,b,2a\},
\]

one has

\[
\boxed{
\ker L_{\{a,b,2a\};R,S,T_0=2a}=\{0\}.
}
\tag{A14.3a.33}
\]

Status:

\[
\boxed{\text{R36-A14.3a three-shift boundary injectivity}\quad\checkmark[M].}
\]

---

## 9. Structural interpretation and firewall

A14.2i showed that for `T_0<2a` the first two-shift chamber has a sharp nontrivial kernel region `R<a<b<S`.
The horizon hardening then showed that extending the source horizon to `2a` already destroys that old four-chart channel in the auxiliary two-shift truncation.

A14.3a now proves the stronger canonical statement: after the new prime-power shift `tau_{2,2}=2a` is also activated, **no new cancellation mode appears anywhere in the full boundary triangle `0<R<S<2a`**.

The proof mechanism is not contraction, coercivity, a finite chart ansatz, or an untyped dense affine orbit.  It is a typed measurable matrix cocycle over two irrational circle rotations, with open support gaps providing the unique-continuation seed.

No statement is promoted beyond the exact boundary `T_0=2a`.

---

## 10. Status ledger

\[
\boxed{\text{E/U source decomposition}\quad\checkmark[M]}
\]

\[
\boxed{\text{typed irrational-rotation UC lemma}\quad\checkmark[M]}
\]

\[
\boxed{e/d\notin\mathbb Q,\ \delta/e\notin\mathbb Q\quad\checkmark[M]}
\]

\[
\boxed{\text{lower-half UC}\quad\checkmark[M]}
\]

\[
\boxed{\text{upper-half UC}\quad\checkmark[M]}
\]

\[
\boxed{\ker L_{\{a,b,2a\}}=\{0\}\text{ at }T_0=2a\quad\checkmark[M]}
\]

Still open:

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
