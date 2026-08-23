# P12 Runde 16 — complete hard-horizon mode kill

**Status:** ✓[M] after independent second review; local hard-horizon theorem only.    
**Repo basis:** `Waschtl904/objekt-x-programm`, `main`,
HEAD `de350bfa44d6607b4ea57be01071a43c82020bd4`.  
**Scope:** closes only the remaining Runde-15H hard-horizon local mode.  
**P11:** FROZEN. **R14:** untouched.

## 0. Starting point from committed Runde 15H

Let
\[
\Delta:=p^2-q^2,\qquad
\Psi:=\Delta^2-p^2r^2.
\]

The committed 18-source reduction gives, in the hard-horizon chamber,
\[
\rho\le R<e/2,\qquad
R<x<\min\{\sigma,d-\sigma,e-\varepsilon\},
\]
an exact rank-18 system with one local mode and
\[
h(e-x)=\gamma h(x),\qquad
\gamma=-\frac{qr\Delta}{\Psi}.
\]

It also gives
\[
h(2\delta+x)=h(a-2\delta-x)=h(3e-x)=0.
\]

The task is to prove
\[
h(x)=0.
\]

No claim about the full \(\rho\)-descent is promoted in this draft.

---

## 1. New involution

Define
\[
\theta:=2e-3\delta
=\frac12\log\frac{2^{13}}{3^8},
\qquad
y:=\theta-x,
\qquad
z:=e-y.
\]

Numerically,
\[
\theta\approx0.11100751896720523,
\qquad
\theta/2\approx0.05550375948360262.
\]

Since \(x>R\ge\rho\) and
\[
\theta-\rho<\delta
\]
(the last inequality is \(\theta<\varepsilon_{\max}\), exactly
\(32768<32805\)), whenever \(y>R\) one has
\[
R<y<\delta.
\]

We split only by whether the new reflected value is below support and
whether its associated tail value is live:

1. \(y\le R\);
2. \(y>R\) and \(z\ge\sigma\);
3. \(y>R\) and \(z<\sigma\).

These cases exhaust the hard-horizon chamber.

---

# Part A. Twenty-nine-source transfer system

Add the following eleven sources to the committed Runde-15H eighteen:

\[
\begin{aligned}
v_1&=3e-x,\\
v_2&=x+3e+4\delta=T+x-\eta,\\
v_3&=e-\delta-x,\\
v_4&=2e-\delta-x,\\
v_5&=x+2\delta,\\
v_6&=x+e+3\delta,\\
v_7&=5e-x,\\
v_8&=x+2e+4\delta,\\
v_9&=4e-\delta-x,\\
v_{10}&=5e-\delta-x,\\
v_{11}&=x+e+4\delta,
\end{aligned}
\]
where
\[
\eta=e-2\delta.
\]

### A.1 Horizon legality

All are positive.  Only \(v_2\) lies above \(T\):
\[
v_2=T+(x-\eta).
\]
Because
\[
x<\sigma<\varepsilon,\qquad \eta>0,
\]
\[
0<x-\eta<x<\sigma<\varepsilon,
\]
hence
\[
v_2<T+\varepsilon=T_0.
\]
All other ten are below \(T\), by direct subtraction from
\(T=4e+2\delta\).

Thus all eleven sources are horizon-legal.

### A.2 Master support facts

The repeated low slots are controlled by

\[
x-\eta<R.
\]

Indeed \(x<e/2\) and
\[
\rho+\eta>e/2.
\]
So
\[
x-\eta<e/2-\eta<\rho\le R.
\]

The first new reflected value is
\[
y=\theta-x=2e-3\delta-x.
\]

Every other support decision in the eleven-source table is fixed by
the hard-horizon inequalities together with either \(y\le R\),
or \(R<y\) and the live/dead status of the single tail
\[
H(z)=h(T+z),\qquad z=e-y.
\]

The attached verifier reconstructs all rows from the raw operator and
tests the complete support pattern separately in all three chambers.

---

## 2. Case A: \(y\le R\)

Here the 18 old rows plus the 11 new rows involve exactly 29 live
visibility variables.

Let the resulting coefficient matrix be \(M_{29}\).  Direct exact
calculation gives

\[
\boxed{
\det M_{29}
=
2p^{11}qr^3(p-q)^2(p+q)^2
(\Delta-pr)^2(\Delta+pr)^2
(2p^2-2q^2-r^2).
}
\tag{A.1}
\]

Every factor is nonzero.

For the arithmetic factors, put
\[
\beta:=q/p,\qquad u:=\beta^2,\qquad t:=r/p,\qquad v:=t^2.
\]

Exactly
\[
u=2^{-3/2}.
\]

The elementary prime-power bounds
\[
3^{12}>2^{19},
\qquad
3^5<2^8,
\]
and
\[
(2/3)^{3/2}>27/50,
\qquad
(2/3)^{3/2}<9/16
\]
give
\[
\boxed{\frac{171}{200}<v<\frac9{10}.}
\tag{A.2}
\]

Also
\[
\boxed{\frac7{20}<u<\frac38,\qquad \beta<\frac35.}
\tag{A.3}
\]

Hence
\[
2-2u-v
>
2-\frac34-\frac9{10}
=
\frac7{20}>0.
\]
Therefore
\[
2p^2-2q^2-r^2>0.
\]

Moreover
\[
\alpha^2:=\frac{p^2r^2}{\Delta^2}
=\frac{v}{(1-u)^2}
>
\frac{171/200}{(13/20)^2}
=
\frac{342}{169}>1.
\]
Thus
\[
\Delta-pr<0,\qquad
\Delta+pr>0.
\]

Consequently
\[
\det M_{29}\ne0,
\]
so the complete local visibility vector vanishes, in particular

\[
\boxed{h(x)=0.}
\tag{A.4}
\]

Note that \(x>\delta\) automatically lies in this case, because then
\[
y<\theta-\delta=2\eta<\rho\le R.
\]

---

# Part B. Short reflected case: \(y>R,\ z\ge\sigma\)

Now precisely one additional lower visibility value is live:
\[
Y:=h(y).
\]
The tail \(H(z)\) is zero because \(z\ge\sigma\).

The same 29 rows therefore form a \(29\times30\) matrix of exact rank
29.

Let \(X:=h(x)\), and let
\[
Z_y:=h(z)=h(e-y).
\]

Three exact maximal minors give:

\[
D_Y
=
2p^{11}qr^3(p-q)^2(p+q)^2
(\Delta-pr)^2(\Delta+pr)^2
(2p^2-2q^2-r^2),
\]

\[
D_X
=
-p^{10}q^2r^5(p-q)^2(p+q)^2
(\Delta-pr)^2(\Delta+pr)^2,
\]

and

\[
D_{Z_y}
=
2p^{11}q^2r^4(p-q)^3(p+q)^3
(\Delta-pr)(\Delta+pr)
(2p^2-2q^2-r^2).
\]

The signed cofactor ratios give

\[
\boxed{
Y=\lambda X,\qquad
\lambda=
-\frac{2p(2p^2-2q^2-r^2)}{qr^2},
}
\tag{B.1}
\]

and

\[
\boxed{
Z_y=\gamma Y,\qquad
\gamma=-\frac{qr\Delta}{\Psi}.
}
\tag{B.2}
\]

### B.1 Non-degeneracy of \(\lambda\)

Using (A.2)--(A.3),
\[
|\lambda|
=
\frac{2(2-2u-v)}{\beta v}
>
\frac{2(7/20)}{(3/5)(9/10)}
=
\frac{35}{27}>1.
\]
Hence
\[
\boxed{\lambda^2\ne1.}
\tag{B.3}
\]

### B.2 If \(y<\sigma\)

The same 29-source short-transfer system is valid at the point \(y\):
its reflected point is
\[
\theta-y=x>R,
\]
and its associated tail offset is
\[
e-x>\varepsilon>\sigma.
\]
Therefore
\[
X=\lambda Y.
\]
Together with \(Y=\lambda X\),
\[
X=\lambda^2X.
\]
By (B.3),
\[
\boxed{X=Y=0.}
\tag{B.4}
\]

### B.3 If \(y\ge\sigma\)

Now the E-source equation is homogeneous at \(y\), \(a-y\),
\(d-y\), and \(e+y\).

Because \(R<y<\delta\),
\[
0<\delta-y<\delta-R<R,
\]
so \(h(\delta-y)=0\).

Write
\[
D_y:=h(d-y),\qquad A_y:=h(a-y),\qquad Z_y:=h(e-y).
\]

The homogeneous E-equations at \(d-y\) and \(e+y\) give
\[
D_y=\frac{pr}{\Delta}Y.
\]
Then E at \(y\) gives
\[
A_y=\frac{p(\Delta-r^2)}{q\Delta}Y.
\]
Finally E at \(a-y\) gives
\[
\boxed{
Z_y=\gamma^{-1}Y.
}
\tag{B.5}
\]

But the 29-source transfer system already gives (B.2),
\[
Z_y=\gamma Y.
\]

We need \(\gamma^2\ne1\).  From (A.2)--(A.3),

\[
\alpha^2
>
\frac{342}{169}
>
\frac{49}{25},
\qquad\text{so}\qquad
\alpha>\frac75.
\]

Also \(\beta<3/5\).  Since
\[
\gamma=\frac{\beta\alpha}{\alpha^2-1}>0,
\]
we have
\[
\alpha(\alpha-\beta)
>
\frac75\cdot\frac45
=
\frac{28}{25}>1,
\]
hence
\[
\alpha^2-1>\beta\alpha,
\qquad
0<\gamma<1.
\]
Thus
\[
\boxed{\gamma^2\ne1.}
\tag{B.6}
\]

Equations (B.2) and (B.5) imply
\[
(\gamma-\gamma^{-1})Y=0,
\]
so
\[
Y=0.
\]
Then (B.1), with \(\lambda\ne0\), gives

\[
\boxed{X=0.}
\tag{B.7}
\]

Thus the entire short reflected case is closed.

---

# Part C. Long-tail case: \(y>R,\ z<\sigma\)

Here \(y<\sigma\) automatically, because
\[
y<\delta<\kappa=e-\delta<z<\sigma
\]
would otherwise be impossible.

The 29 \(x\)-rows now contain two additional live values:
\[
Y=h(y),
\qquad
H(z)=h(T+z).
\]

To close them, add eleven selected source equations centred at
\(y=\theta-x\), together with one final source.

## C.1 The eleven \(y\)-sources

In \(y\)-notation they are

\[
\boxed{
b-y,\ a-y,\ T-y,\ T+y,\ a+e+y,\ e-y,\ d+y,\ 2e-y,\ \delta+y,\ T+e-y,\ d+\delta+y.
}
\tag{C.1}
\]

They are all horizon-legal.

Indeed \(0<y<\delta\), and all but \(T+y\) and \(T+e-y\) are below
\(T\).  Moreover
\[
T+y<T+\sigma<T+\varepsilon,
\]
and, because \(z=e-y<\sigma\),
\[
T+e-y=T+z<T+\sigma<T+\varepsilon.
\]

## C.2 Final source

Use
\[
\boxed{u_\star=x-\eta.}
\tag{C.2}
\]

It is positive because
\[
x>R\ge\rho>\eta,
\]
and lies below \(T\), hence is horizon-legal.

Its six live raw slots are

\[
\begin{aligned}
&-p\,h(3e-\delta-x),
&&-p\,h(x+e+3\delta),\\
&-r\,h(4e-x),
&&-r\,h(x+2e+4\delta),\\
&-q\,h(5e-x),
&&-q\,h(x+3e+4\delta).
\end{aligned}
\tag{C.3}
\]

## C.3 Exact 41x41 determinant

Take:
- the 18 committed Runde-15H rows at \(x\);
- the 11 Part-A transfer rows at \(x\);
- the 11 rows (C.1) at \(y\);
- the one final row (C.3).

The resulting visibility system is exactly \(41\times41\).

Direct symbolic calculation gives

\[
\boxed{
\det M_{41}
=
p^{16}qr^6(p-q)^2(p+q)^2
(\Delta-pr)(\Delta+pr)\,F\,G,
}
\tag{C.4}
\]
where
\[
F=
2p^4-3p^2q^2-p^2r^2+q^4-q^2r^2
\tag{C.5}
\]
and
\[
\begin{aligned}
G={}&
12p^6-24p^4q^2-14p^4r^2
+12p^2q^4+18p^2q^2r^2+4p^2r^4\\
&-4q^4r^2-3q^2r^4.
\end{aligned}
\tag{C.6}
\]

### C.4 Exact sign of \(F\)

Divide by \(p^4\):
\[
F/p^4=2-3u-v+u^2-uv.
\]

Since \(u^2=1/8\), \(u>7/20\), and \(v>171/200\),

\[
\begin{aligned}
F/p^4
&<
\frac{17}{8}-\frac{171}{200}
-\left(3+\frac{171}{200}\right)\frac7{20}\\
&=
-\frac{317}{4000}<0.
\end{aligned}
\]

Therefore
\[
\boxed{F<0.}
\tag{C.7}
\]

### C.5 Exact sign of \(G\)

Put
\[
P(u,v):=G/p^6.
\]
Then
\[
P(u,v)
=
12-24u-14v+12u^2+18uv+4v^2-4u^2v-3uv^2.
\]

For \(v\le9/10\) and \(u<3/8\),
\[
\frac{\partial P}{\partial v}
=
-14+18u+8v-4u^2-6uv
<
-14+18\frac38+8\frac9{10}
=
-\frac1{20}<0.
\]

Thus
\[
P(u,v)>P(u,9/10).
\]

A direct simplification gives
\[
P(u,9/10)
=
\frac3{100}(280u^2-341u+88)
=
\frac3{100}(123-341u),
\]
because \(u^2=1/8\).

Finally
\[
u=\frac1{2\sqrt2}<\frac{123}{341},
\]
because after squaring this is exactly
\[
116281<121032.
\]

Hence
\[
\boxed{G>0.}
\tag{C.8}
\]

All factors in (C.4) are therefore nonzero, so
\[
\det M_{41}\ne0.
\]

Consequently the complete long-tail visibility vector is zero, in
particular

\[
\boxed{h(x)=0.}
\tag{C.9}
\]

---

# 3. Candidate hard-horizon theorem

Parts A, B and C exhaust the possibilities for \(y=\theta-x\).

Therefore the committed Runde-15H one-dimensional obstruction is
killed:

\[
\boxed{
\rho\le R<e/2,\quad
R<x<\min\{\sigma,d-\sigma,e-\varepsilon\}
\Longrightarrow
h(x)=0
\quad\text{a.e.}
}
\tag{H-KILL}
\]

Status after independent review:

\[
\boxed{\text{hard-horizon mode kill }\checkmark[M]}
\]

The independent second audit reconstructed the new raw rows directly from the canonical operator, reproduced the exact 29x29 and 41x41 determinant factorizations, the three maximal minors, the coefficient identities for \(\lambda\) and \(\gamma\), all arithmetic sign checks, and all three chamber pattern stresses. No contradiction or gap was found.

---

# 4. Independent second review record

On 2026-08-23 an independent second AI audit rebuilt the verifier independently rather than importing the finished rows. It confirmed:

- all eleven new x-transfer sources and the selected y-sources from the six raw operator slots;
- horizon legality, including the final source \(u_\star=x-\eta\);
- the exact determinant \(\det M_{29}\);
- all three maximal minors in the rank-29 short-reflected system;
- the cofactor ratios for \(\lambda\) and \(\gamma\);
- the exact determinant \(\det M_{41}\);
- every stated elementary integer inequality and sign;
- the three adversarial pattern stresses with the same counts as the retained verifier.

The retained verifier uses the representative points
\[
(R_A,x_A,\sigma_A,\varepsilon_A)=(0.055,0.061,0.066,0.072),
\]
\[
(R_B,x_B,\sigma_B,\varepsilon_B)=(0.053,0.055,0.0575,0.060),
\]
and
\[
(R_C,x_C,\sigma_C,\varepsilon_C)=(0.053,0.0545,0.088,0.089).
\]
Their only role is to instantiate one interior visibility pattern per chamber; the subsequent randomized chamber-wide stress checks uniformity. The second reviewer used independently chosen interior points consistent with the same chamber inequalities, so exact equality of representative points is not required.

No full \(\rho\)-descent theorem is promoted by this audit. P11 remains frozen and R14 is untouched.

# 5. Archived review checklist

Please independently verify:

1. the eleven new \(x\)-sources and all six raw slots of each;
2. the exact \(29\times29\) determinant (A.1);
3. the three \(29\times29\) maximal minors in Part B;
4. the signed cofactor ratios producing \(\lambda\) and \(\gamma\);
5. the \(\lambda^2\ne1\) argument;
6. the homogeneous E derivation \(Z_y=\gamma^{-1}Y\);
7. the eleven selected \(y\)-sources in the long-tail chamber;
8. the final raw row at \(u_\star=x-\eta\);
9. the exact \(41\times41\) determinant (C.4);
10. the elementary sign proofs \(F<0\), \(G>0\);
11. the support/horizon pattern in all three chambers.

Do not promote the full \(\rho\)-descent yet.  This package closes only
the hard-horizon local obstruction.

No changes to P11 or R14.
