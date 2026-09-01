# P11 End-to-End Referee R37 — two-shift Gamma pairing rigidity and strict normal mismatch

Date: 2026-09-01

## Purpose / firewall

Continue the Strong-Terminal / modulus branch after R27--R36 in the first genuine two-shift chamber

\[
0<R<S<T_0,\qquad b<T_0<2a,
\]

with

\[
a=\frac{\log2}{2},\qquad
b=\frac{\log3}{2},\qquad
d=b-a,\qquad
c=a+b.
\]

R36-A14.2i gives the exact odd folded-kernel phase diagram and, in the open region

\[
\boxed{0<R<a<b<S<T_0<2a,}
\tag{R37.1}
\]

an explicit closed infinite-dimensional four-chart kernel.

The present target is to decide whether that exact kernel detects the concrete annular defect

\[
d_{R,S}=P_A(\phi_S-C_{\Gamma,S}j_{R,S}),
\qquad
j_{R,S}=E_{R,S}\rho_{R,T_0},
\]

and therefore forces the R28/R30 constraint-normal mismatch

\[
s_{R,S,T_0}\neq0.
\]

This note is **modulus / inverse-functional-calculus only**.  By the R14 firewall, no polar-gauge or Strong-Terminal no-go is promoted from this mismatch alone.

Current status of this note: **AI-GREEN candidate**, no promotion.

Canonical inputs:

- R28 — fixed Gamma crossblock and normal mismatch;
- R30/R31 — support-radius and exact annular residual gate;
- R33 — exact P02-to-P11 Gamma symbol bridge;
- R36-A13c.1 — localized Hub-kernel vectors annihilate the full restricted Schur range;
- R36-A14.2i — complete first two-shift odd-kernel classification.

---

## 1. The A14.2i four-chart kernel

Assume (R37.1).  Put

\[
\rho:=\frac{c_3}{c_2}>0,
\qquad
c_2=\sqrt{\log2}\,2^{-3/4},
\qquad
c_3=\sqrt{\log3}\,3^{-3/4}.
\]

A14.2i defines

\[
m=a-\frac d2,
\qquad
\lambda=\max\{R,\ T_0-a,\ c-S,\ m\},
\qquad
I=(\lambda,a),
\]

and proves \(I\neq\varnothing\).

For arbitrary \(f\in L^2(I)\), the exact kernel vector \(h_f\) is supported on the four pairwise disjoint charts

\[
J_0=I,\qquad
J_1=2a-I,\qquad
J_2=I+d,\qquad
J_3=c-I,
\]

with values

\[
h_f(x)=f(x),
\tag{R37.2a}
\]

\[
h_f(2a-x)=-f(x),
\tag{R37.2b}
\]

\[
h_f(x+d)=\rho f(x),
\tag{R37.2c}
\]

\[
h_f(c-x)=-\rho f(x),
\tag{R37.2d}
\]

for \(x\in I\), and \(h_f=0\) elsewhere.

A14.2i proves

\[
h_f\in\ker L_{R,S,T_0}
\]

for every \(f\in L^2(I)\).

Via R36-A9,

\[
U_-(\ker L_{R,S,T_0})
=
\ker(H_{T_0}E_A)\cap L^2_{\mathrm{odd}}(A).
\tag{R37.3}
\]

---

## 2. Exact four-chart pairing reduction

The annular defect \(d_{R,S}\) is odd.  Since \(U_-h_f\) is odd,

\[
\langle U_-h_f,d_{R,S}\rangle_A
=
\sqrt2\int_R^S
h_f(y)\overline{d_{R,S}(y)}\,dy.
\tag{R37.4}
\]

Changing variables on the four charts gives

\[
\boxed{
\langle U_-h_f,d_{R,S}\rangle_A
=
\sqrt2\int_I
f(x)\overline{\mathcal F_{R,S}(x)}\,dx,
}
\tag{R37.5}
\]

where

\[
\boxed{
\mathcal F_{R,S}(x)
=
d_{R,S}(x)
-d_{R,S}(2a-x)
+\rho\,d_{R,S}(x+d)
-\rho\,d_{R,S}(c-x).
}
\tag{R37.6}
\]

Therefore

\[
\boxed{
\langle U_-h_f,d_{R,S}\rangle_A=0
\quad\forall f\in L^2(I)
\iff
\mathcal F_{R,S}=0
\quad\text{a.e. on }I.
}
\tag{R37.7}
\]

All four arguments in (R37.6) lie in the positive annulus \((R,S)\) by the A14.2i chart construction.

---

## 3. Concrete Gamma tail

R31/R33 give, for every \(x>R\),

\[
d_{R,S}(x)
=
2+e^{-x/2}G(e^{-2x}),
\tag{R37.8}
\]

where

\[
G(z)=\sum_{n=0}^\infty A_nz^n
\]

is holomorphic in

\[
|z|<e^{-2R},
\tag{R37.9}
\]

and

\[
A_0=M_0(j)-2,
\qquad
A_n=M_n(j)\quad(n\ge1),
\tag{R37.10}
\]

with

\[
M_n(j)
=
\int_{-R}^{R}
j(y)e^{(2n+1/2)y}\,dy.
\tag{R37.11}
\]

The constant \(2\) cancels identically in (R37.6).

---

## 4. Exact two-shift Gamma rigidity

Define the constants

\[
q:=e^{-4a}=\frac14,
\qquad
r:=e^{-2d}=\frac23,
\tag{R37.12}
\]

\[
\beta:=e^{-a}=\frac1{\sqrt2},
\qquad
\alpha:=\rho e^{-d/2}>0.
\tag{R37.13}
\]

Because \(c=a+b=2a+d\),

\[
e^{-2c}=qr=\frac16,
\tag{R37.14}
\]

and

\[
\rho e^{-c/2}
=
\beta\alpha.
\tag{R37.15}
\]

Assume for contradiction that \(\mathcal F_{R,S}=0\) on \(I\).
Both sides of (R37.6) are real-analytic there, so the a.e. identity becomes a pointwise identity.

Put

\[
z=e^{-2x}.
\]

Using (R37.8) at the four chart points gives

\[
z^{1/4}G(z)
-\beta z^{-1/4}G(q/z)
+\alpha z^{1/4}G(rz)
-\beta\alpha z^{-1/4}G(qr/z)
=0.
\tag{R37.16}
\]


### 4.1 Independent mode-by-mode crosscheck

There is a second way to see the same rigidity before introducing \(z\).

With

\[
\lambda_n=2n+\frac12,
\]

the \(n\)-th Gamma mode in (R37.6) contributes

\[
A_n\Bigl[
e^{-\lambda_nx}
-e^{-\lambda_n(2a-x)}
+\rho e^{-\lambda_n(x+d)}
-\rho e^{-\lambda_n(c-x)}
\Bigr].
\]

Since

\[
c=2a+d,
\]

this factors **mode by mode** as

\[
\boxed{
A_nB_n
\Bigl[
e^{-\lambda_nx}
-e^{-\lambda_n(2a-x)}
\Bigr],
}
\tag{R37.16a}
\]

where

\[
\boxed{
B_n:=1+\rho e^{-\lambda_nd}>0.
}
\tag{R37.16b}
\]

Indeed,

\[
\rho e^{-\lambda_n(x+d)}
=
\rho e^{-\lambda_nd}e^{-\lambda_nx},
\]

while

\[
\rho e^{-\lambda_n(c-x)}
=
e^{-2a\lambda_n}
\rho e^{-\lambda_nd}e^{\lambda_nx}.
\]

Thus the four-chart relation is exactly a weighted reflection relation about \(a\), with a strictly positive multiplier \(B_n\) on every Gamma mode.

Equivalently,

\[
\mathcal F_{R,S}(x)
=
\sum_{n=0}^\infty
A_nB_n
\Bigl[
e^{-\lambda_nx}
-e^{-\lambda_n(2a-x)}
\Bigr].
\tag{R37.16c}
\]

This provides an independent algebraic check of the \(H(z)\)-reduction:
the factor \(B_n\) is precisely the coefficient multiplier
\(1+\alpha r^n\), up to the common positive factor coming from
\(e^{-d/4}\).

The mode factorization is not by itself the uniqueness proof; the Laurent argument below remains the analytic step that forces all coefficients to vanish.

Define

\[
\boxed{
H(z):=G(z)+\alpha G(rz).
}
\tag{R37.17}
\]

Then on the positive real arc corresponding to \(I\),

\[
\boxed{
z^{1/2}H(z)=\beta H(q/z).
}
\tag{R37.18}
\]

Square before analytic continuation, and write

\[
K(z):=H(z)^2.
\]

Since \(\beta^2=1/2\),

\[
\boxed{
K(q/z)=2zK(z).
}
\tag{R37.19}
\]

Both sides of (R37.19) are single-valued holomorphic on

\[
\mathcal A_{R,a}
=
\left\{
z:
qe^{2R}<|z|<e^{-2R}
\right\}.
\tag{R37.20}
\]

This annulus is nonempty exactly because

\[
qe^{2R}<e^{-2R}
\iff
R<a,
\]

which is part of (R37.1).

By the identity theorem, (R37.19) holds on all of \(\mathcal A_{R,a}\).

Now write

\[
K(z)=\sum_{n=0}^\infty b_nz^n
\]

in the disk \(|z|<e^{-2R}\).  On the annulus,

\[
K(q/z)
=
\sum_{n=0}^\infty b_nq^nz^{-n},
\tag{R37.21}
\]

while

\[
2zK(z)
=
2\sum_{n=0}^\infty b_nz^{n+1}.
\tag{R37.22}
\]

The Laurent supports are disjoint:

- the left side uses powers \(0,-1,-2,\ldots\);
- the right side uses powers \(1,2,3,\ldots\).

Uniqueness of Laurent expansions forces

\[
b_n=0\qquad(n\ge0),
\]

hence

\[
K\equiv0
\quad\Longrightarrow\quad
H\equiv0.
\tag{R37.23}
\]

Using (R37.17) and the power series for \(G\),

\[
0=H(z)
=
\sum_{n=0}^\infty
A_n\bigl(1+\alpha r^n\bigr)z^n.
\]

Since

\[
\alpha>0,\qquad 0<r=\frac23<1,
\]

one has

\[
1+\alpha r^n>0
\qquad(n\ge0),
\]

so

\[
A_n=0
\qquad(n\ge0).
\tag{R37.24}
\]

Therefore

\[
M_n(j)=0\quad(n\ge1),
\qquad
M_0(j)=2.
\tag{R37.25}
\]

As in A13c, push forward the finite measure
\(e^{y/2}j(y)\,dy\) under \(t=e^{2y}\) to the compact interval
\([e^{-2R},e^{2R}]\).
The identities \(M_n=0\) for every \(n\ge1\) say that this measure annihilates
\(\{t,t^2,t^3,\ldots\}\), whose span is dense in \(C(K)\) because \(K\) is separated from \(0\).
Hence the measure is zero, so \(j=0\), forcing \(M_0(j)=0\), contradicting (R37.25).

Thus:

### Theorem R37-A — two-shift Gamma four-chart rigidity

Under (R37.1),

\[
\boxed{
\mathcal F_{R,S}\not\equiv0
\quad\text{on }I.
}
\tag{R37.26}
\]

Equivalently, the concrete Gamma defect cannot satisfy the weighted four-chart symmetry imposed by orthogonality to the entire A14.2i kernel family.

Status: **AI-GREEN candidate**.

---

## 5. Nonorthogonal odd annihilator

By (R37.7) and Theorem R37-A, choose \(f\in L^2(I)\) such that

\[
\langle U_-h_f,d_{R,S}\rangle_A\ne0.
\]

Put

\[
y:=U_-h_f.
\]

Then by (R37.3),

\[
\boxed{
y\in\ker(H_{T_0}E_A),
\qquad
\langle y,d_{R,S}\rangle_A\ne0.
}
\tag{R37.27}
\]

R36-A13c.1 is parameter-general and gives

\[
\langle y,P_A\Sigma_{T_0}F\rangle_A=0
\]

for every terminal vector \(F\).  Therefore

\[
d_{R,S}
\notin
\overline{\operatorname{Ran}(P_A\Sigma_{T_0})}.
\tag{R37.28}
\]

Status: **AI-GREEN candidate**.

---

## 6. Strict normal mismatch in the full two-shift negative region

Let

\[
\widetilde j=E_{S,T_0}j_{R,S}.
\]

As in A13c,

\[
P_A\Delta_{R,S}^{[T_0]}
=
d_{R,S}
-
P_A\Sigma_{T_0}\widetilde j.
\]

By (R37.28),

\[
\Delta_{R,S}^{[T_0]}\ne0.
\]

R31-C gives, for every \(0<R<S<T_0\),

\[
\Delta_{R,S}^{[T_0]}=0
\iff
s_{R,S,T_0}=0.
\]

Hence:

### Theorem R37-B — complete two-shift negative-region normal mismatch

If

\[
\boxed{
0<R<a<b<S<T_0<2a,
}
\tag{R37.29}
\]

then

\[
\boxed{
s_{R,S,T_0}\ne0.
}
\tag{R37.30}
\]

Status: **AI-GREEN candidate**.

This strictly extends the old first-chamber A13c mismatch theorem into the first genuine two-shift chamber.

---

## 7. Consequences for R27/R28/R30

R28 gives

\[
\|D_\infty^-\|
\ge
\frac{\|s_{R,S,T_0}\|}{\|r_S\|}.
\]

Thus (R37.30) implies

\[
\boxed{
D_\infty^-\ne0
}
\tag{R37.31}
\]

throughout the full open region (R37.29).

By R30,

\[
s_{R,S,T_0}\ne0
\iff
R<R_*(S,T_0).
\]

Since (R37.30) holds for every \(R<a\), one gets the exact structural lower bound

\[
\boxed{
R_*(S,T_0)\ge a
\qquad
\text{whenever } b<S<T_0<2a.
}
\tag{R37.32}
\]

The remaining R30-F question in this chamber is therefore compressed to

\[
\boxed{
a\le R<S:
\quad
s_{R,S,T_0}\stackrel{?}{\ne}0.
}
\tag{R37.33}
\]

The odd-annihilator route cannot decide that remaining strip merely from A14.2i, because A14.2i proves the odd folded Hub kernel is trivial for \(R\ge a\).

### 7.1 Fixed-vector strong modulus no-go

Let

\[
Q_U
=
A_S(U)^{1/2}WA_R(U)^{-1/2}.
\]

By definition,

\[
D_U^-
=
A_S(U)^{-1/2}W
-
WA_R(U)^{-1/2}.
\]

Hence the exact identity

\[
\boxed{
Q_U-W
=
-A_S(U)^{1/2}D_U^-.
}
\tag{R37.34}
\]

R24 gives the uniform coercivity

\[
A_S(U)\ge a_0I,
\qquad
a_0=(1+\|H_{T_0}\|^2)^{-1}>0.
\]

Therefore, for every fixed source vector \(x\),

\[
\boxed{
\|(Q_U-W)x\|
\ge
\sqrt{a_0}\,\|D_U^-x\|.
}
\tag{R37.35}
\]

R27 gives

\[
D_U^-x\to D_\infty^-x
\]

strongly for every fixed \(x\).

Now use the fixed R28 normal witness

\[
e_R=\frac{r_R}{\|r_R\|}.
\]

R28 gives

\[
\|D_\infty^-e_R\|
\ge
\frac{\|s_{R,S,T_0}\|}{\|r_S\|}.
\]

Combining with R37-B,

\[
\boxed{
\liminf_{U\to\infty}
\|(Q_U-W)e_R\|
\ge
\sqrt{a_0}\,
\frac{\|s_{R,S,T_0}\|}{\|r_S\|}
>0
}
\tag{R37.36}
\]

throughout (R37.29).

Thus:

### Theorem R37-C — strong modulus-isometry mismatch

If

\[
0<R<a<b<S<T_0<2a,
\]

then

\[
\boxed{
Q_U\not\xrightarrow[s]{U\to\infty}W.
}
\tag{R37.37}
\]

This is strictly stronger than the old R19 lower bound
\(\|Q_U-W\|\gtrsim U^{-m-1}\), whose right-hand side tends to zero and therefore did not exclude convergence.

Status: **AI-GREEN candidate**.

This remains a modulus-layer theorem.  The moving polar factors can in principle reorganize modulus information; R14/R20 remain binding against any automatic promotion of (R37.37) to a Strong-Terminal no-go.

---

## 8. Strong-Terminal firewall

R37 proves a persistent **inverse-root / modulus orientation defect** on an explicit open two-shift region.

It does **not** prove:

- \(\Gamma_U\not\to I\);
- nonconvergence of the polar factors;
- failure of the R22 fixed-vector angle criterion;
- failure of \(W_{R,S,-}^{[U]}\) to converge strongly;
- failure of every possible terminal normalization;
- failure of Object X;
- any RH statement.

R14 remains binding: modulus and polar behavior are logically distinct.

Therefore the correct research state after R37, if independently confirmed, is:

\[
\boxed{
\text{modulus gate negative on a larger open region;}
\qquad
\text{polar Strong-Terminal gate still open.}
}
\]

---

## 9. Review gates

Before any promotion:

1. **Pairing gate:** verify (R37.5)--(R37.7) from the four A14.2i charts and the \(U_-\) normalization.
2. **Constant gate:** verify \(q=1/4\), \(r=2/3\), \(e^{-2c}=qr\), \(\rho e^{-c/2}=\beta\alpha\), \(\beta^2=1/2\).
3. **Holomorphic-domain gate:** verify all four Gamma-tail evaluations lie in \((R,S)\) and the annulus (R37.20) is nonempty exactly under \(R<a\).
4. **Laurent gate:** verify the squaring removes the local square-root branch before analytic continuation and that the Laurent supports in (R37.21)--(R37.22) are disjoint.
5. **Moment gate:** verify \(H\equiv0\Rightarrow G\equiv0\Rightarrow(M_{n\ge1}=0,M_0=2)\) contradicts moment density exactly as in A13c.
6. **Adjunction gate:** verify R36-A13c.1 applies unchanged in the two-shift chamber.
7. **Residual gate:** verify R31-C transfers nonorthogonality to \(s\neq0\) with no hidden one-shift assumption.
8. **Status firewall:** no polar/Strong-Terminal promotion from R37 alone.
