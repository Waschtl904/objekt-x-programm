# P11 End-to-End Referee R29 — small-source constraint-normal mismatch

Date: 2026-08-15

## Target

Decide the fixed R28 normal obstruction
\[
s_{R,S,T_0}:=(I-WW^*)r_S
\]
for at least a nontrivial concrete region of P11 source triples.  Here
\[
0<R<S<T_0
\]
is fixed, \(W=B_S^{1/2}J_{R,S}B_R^{-1/2}\) is the normalized baseline isometry, and \(r_X\) is the Riesz vector of the transported first boundary functional
\[
\widehat\beta_X(x)=\beta_X^{(0)}(B_X^{-1/2}x)
\]
in the baseline-whitened source Hilbert space.

No polar-gauge conclusion is permitted.

## Verdict

For every fixed \(0<S<T_0\), the concrete P11 normal mismatch is nonzero for all sufficiently small \(R>0\).  In fact
\[
\boxed{
\|r_R\|^2\le\frac23R^3,
}
\]
while \(\|r_S\|>0\) is fixed.  Since R28 gives
\[
\|s_{R,S,T_0}\|^2=\|r_S\|^2-\|r_R\|^2,
\]
one obtains
\[
\boxed{
\|s_{R,S,T_0}\|^2
\ge\|r_S\|^2-\frac23R^3.
}
\]
Therefore
\[
\boxed{
s_{R,S,T_0}\ne0
\qquad\text{whenever}\qquad
0<R<\min\left\{S,\left(\frac32\|r_S\|^2\right)^{1/3}\right\}.
}
\]

Combining with the R28 full-space lower bound yields a genuine concrete P11 asymptotic defect:
\[
\boxed{
\|D_\infty^-(R,S,T_0)\|
\ge
\sqrt{1-\frac{2R^3}{3\|r_S\|^2}}
>0
}
\]
throughout that small-source region.  In particular
\[
\boxed{
\liminf_{R\downarrow0}
\|D_\infty^-(R,S,T_0)\|\ge1.
}
\]
Thus the full inverse-root limit is provably non-intertwining for a whole family of actual P11 triples.

An explicit computable lower substitute for \(\|r_S\|\) is available: for any fixed smooth odd \(h\in C_c^\infty((-S,S))\) with \(\beta_S^{(0)}(h)\ne0\),
\[
c_h:=\frac{|\beta_S^{(0)}(h)|}
{q_{T_0}^X(J_{S,T_0}h)^{1/2}}>0
\]
satisfies \(\|r_S\|\ge c_h\).  Hence the sufficient explicit condition
\[
0<R<\min\left\{S,\left(\frac32c_h^2\right)^{1/3}\right\}
\]
already forces \(s\ne0\).

This is a modulus/inverse-functional-calculus no-go only.  R14 still forbids promotion to a polar-gauge or strong-terminal-transport no-go.

## Canonical statuses

- [R29-A] dual-norm representation of \(\|r_X\|\): **✓[M]**.
- [R29-B] universal small-window estimate \(\|r_R\|^2\le 2R^3/3\): **✓[M]**.
- [R29-C] nonzero normal mismatch for every fixed \(S<T_0\) and all sufficiently small \(R\): **✓[M]**.
- [R29-D] concrete lower bound for the full limiting inverse-root defect and \(\liminf_{R\downarrow0}\|D_\infty^-\|\ge1\): **✓[M]**.
- [R29-E] explicit test-vector threshold via \(c_h\): **✓[M]**.
- [R29-F] decide whether \(s\ne0\) for every \(0<R<S<T_0\), or determine the exact critical support/range threshold: **?[O]**.

No conclusion about \(\Gamma_U\), the R22 polar angle defect, strong terminal transport, or a global Object X follows.

---

## 1. Dual-norm formula for the constraint normal

For \(X\in\{R,S\}\), put
\[
B_X:=G_{X,T_0}^-.
\]
If \(x=B_X^{1/2}f\), then
\[
\|x\|_{X,X}^2
=\langle B_Xf,f\rangle_{X,X}
=q_{T_0}^X(J_{X,T_0}f).
\]
By definition of the Riesz vector \(r_X\),
\[
\widehat\beta_X(x)
=\beta_X^{(0)}(f)
=\langle x,r_X\rangle.
\]
Therefore
\[
\boxed{
\|r_X\|
=
\sup_{0\ne f\in\mathcal K_{X,X}^-}
\frac{|\beta_X^{(0)}(f)|}
{q_{T_0}^X(J_{X,T_0}f)^{1/2}}.
}
\tag{R29.1}
\]
This proves [R29-A].

---

## 2. Universal small-source upper bound

The first boundary kernel is
\[
I_0(r)=\int_0^r e^{-s/2}\,ds=2(1-e^{-r/2}),
\]
so
\[
\beta_R^{(0)}(f)
=\int_{-R}^R\phi_R(u)f(u)\,du,
\qquad
\phi_R(u):=\operatorname{sgn}(u)I_0(|u|).
\]
The fixed-baseline P11 form satisfies
\[
q_{T_0}^X(J_{R,T_0}f)
\ge\mathfrak c_{\Gamma,R}[f]
\ge\|f\|_{L^2(-R,R)}^2
\]
because the Schur term is positive and \(C_{\Gamma,R}\ge I\).  Thus by Cauchy--Schwarz and (R29.1),
\[
\|r_R\|\le\|\phi_R\|_{L^2(-R,R)}.
\tag{R29.2}
\]
Since \(I_0(r)\le r\),
\[
\boxed{
\|r_R\|^2
\le2\int_0^Rr^2\,dr
=\frac23R^3.
}
\tag{R29.3}
\]
The exact elementary bound is
\[
\|\phi_R\|_2^2
=8\left[R-4(1-e^{-R/2})+(1-e^{-R})\right]
=\frac23R^3+O(R^4).
\tag{R29.4}
\]
Hence \(\|r_R\|\to0\) as \(R\downarrow0\).  This proves [R29-B].

---

## 3. Fixed target normal is nonzero

For fixed \(S>0\), the functional \(\beta_S^{(0)}\) is nonzero on the odd graph space: choose any smooth odd \(h\) which is positive on a nonempty subinterval of \((0,S)\).  Then
\[
\beta_S^{(0)}(h)=2\int_0^S I_0(r)h(r)\,dr>0
\]
after choosing \(h\ge0\) on the positive half-line.  Therefore its Riesz vector satisfies
\[
\boxed{\|r_S\|>0.}
\tag{R29.5}
\]
More quantitatively, (R29.1) gives
\[
\boxed{
\|r_S\|
\ge c_h
:=\frac{|\beta_S^{(0)}(h)|}
{q_{T_0}^X(J_{S,T_0}h)^{1/2}}
>0.
}
\tag{R29.6}
\]

---

## 4. Nonzero normal mismatch for small source windows

R28 proved
\[
W^*r_S=r_R
\]
and the orthogonal decomposition
\[
r_S=Wr_R+s_{R,S,T_0},
\qquad Wr_R\perp s_{R,S,T_0}.
\]
Hence
\[
\boxed{
\|s_{R,S,T_0}\|^2
=\|r_S\|^2-\|r_R\|^2.
}
\tag{R29.7}
\]
Combining (R29.3) and (R29.7),
\[
\boxed{
\|s_{R,S,T_0}\|^2
\ge\|r_S\|^2-\frac23R^3.
}
\tag{R29.8}
\]
Therefore
\[
\boxed{
s_{R,S,T_0}\ne0
\quad\text{if}\quad
R<\left(\frac32\|r_S\|^2\right)^{1/3}.
}
\tag{R29.9}
\]
Together with the standing condition \(R<S\), this proves [R29-C].  The computable sufficient threshold from (R29.6) is
\[
\boxed{
R<\left(\frac32c_h^2\right)^{1/3}
\Longrightarrow s_{R,S,T_0}\ne0.
}
\tag{R29.10}
\]

---

## 5. Persistent concrete inverse-root defect

Theorem O3AA.17 gives
\[
\|D_\infty^-\|
\ge\|D_\infty^-e_R\|
\ge\frac{\|s\|}{\|r_S\|}.
\]
Using (R29.8),
\[
\boxed{
\|D_\infty^-(R,S,T_0)\|
\ge
\sqrt{1-
\frac{2R^3}{3\|r_S\|^2}}
}
\tag{R29.11}
\]
whenever the radicand is positive.  Thus in the small-source region the full asymptotic inverse-root intertwining defect is strictly nonzero.

Since \(\|r_S\|\) is fixed while \(\|r_R\|\to0\), (R29.7) gives
\[
\frac{\|s\|}{\|r_S\|}\to1.
\]
Consequently
\[
\boxed{
\liminf_{R\downarrow0}
\|D_\infty^-(R,S,T_0)\|\ge1.
}
\tag{R29.12}
\]
This proves [R29-D].

---

## 6. Firewall and remaining question

R29 is an actual P11 result, not an abstract countermodel: for every fixed \(S<T_0\), a nonempty interval of old source windows \(0<R<R_*(S,T_0)\) has a persistent full inverse-root mismatch after \(U\to\infty\).

But this remains on the modulus/inverse-functional-calculus layer.  The actual normalized future transport contains the moving polar factors.  R14 gives abstract models in which modulus mismatch and polar behavior decouple.  Therefore R29 does not prove nonconvergence of \(W_{R,S,-}^{[U]}\), does not prove \(\Gamma_U\not\to I\), and does not obstruct a global Object X by itself.

The fixed normal question that remains is sharper:

- Is \(s_{R,S,T_0}\ne0\) for every strict inclusion \(0<R<S<T_0\)?
- Equivalently, can the baseline Riesz normal of \(\beta_S^{(0)}\) ever lie entirely in the normalized old-source range?

R29 answers this negatively for all sufficiently small old source windows.