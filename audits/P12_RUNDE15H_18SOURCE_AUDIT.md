# P12 Runde 15H — full 18-source hard-horizon audit package

**Status:** independent-review package; NOT COMMITTED.  
**Repo:** `Waschtl904/objekt-x-programm`, `main`.  
**P11/R14:** untouched.

## 1. Hard-horizon chamber

Assume
\[
\rho\le R<e/2,\qquad
R<\sigma<\varepsilon<\varepsilon_{\max},
\]
and
\[
R<x<\min\{\sigma,d-\sigma,e-\varepsilon\}.
\]
Thus
\[
e-x>\varepsilon,
\]
so the old source
\[
u_{15}=T+e-x
\]
is outside the source horizon \(T_0=T+\varepsilon\) and is forbidden.

Here
\[
\rho=\varepsilon_{\max}-\delta=\tfrac12\log(10/9).
\]

The hard-horizon inequalities imply
\[
\sigma<\varepsilon<e-R<d/2.
\]

## 2. The 18 legal source positions

Use
\[
\begin{aligned}
u_1&=b-x,&
u_2&=b+x,&
u_3&=a-x,&
u_4&=T-x,\\
u_5&=T+x,&
u_6&=a+e+x,&
u_7&=e-x,&
u_8&=a+e-x,\\
u_9&=d+x,&
u_{10}&=3d+x,&
u_{11}&=2d+x,&
u_{12}&=2e-x,\\
u_{13}&=T-\delta-x,&
u_{14}&=\delta+x,&
u_{16}&=d+\delta+x,&
u_{17}&=a+2\delta+x,\\
u_{18}&=4e-x,&
u_{19}&=a+3e-x.
\end{aligned}
\]

All are positive.  All but \(u_5,u_{10},u_{19}\) are visibly below \(T\)
using \(x<\varepsilon_{\max}\) and the fixed order relations.

For the three potentially upper sources:
\[
u_5=T+x<T+\sigma<T+\varepsilon,
\]
\[
u_{10}=3d+x=T-\kappa+x<T+x<T+\varepsilon,
\qquad \kappa=e-\delta,
\]
and
\[
u_{19}=a+3e-x=T+\kappa-x.
\]
Since \(x>R\ge\rho\) and
\[
\kappa<2\rho
\iff d<2\varepsilon_{\max}
\iff24<25,
\]
we have
\[
\kappa-x<\kappa-\rho<\rho\le R<\varepsilon.
\]
Hence \(u_{19}<T+\varepsilon\).

Thus all 18 sources are horizon-legal.

## 3. Raw operator equations

From
\[
Lh(u)=
p[\operatorname{sgn}(u-a)h(|u-a|)-h(u+a)]
+r[\operatorname{sgn}(u-b)h(|u-b|)-h(u+b)]
+q[\operatorname{sgn}(u-T)h(|u-T|)-h(u+T)]
\]
and hard-horizon support truncation, the 18 rows are

\[
E_1:\quad p h(d-x)-r h(x)-q h(e+x)=0,
\]
\[
E_2:\quad p h(d+x)+r h(x)-q h(e-x)=0,
\]
\[
E_3:\quad -p h(x)-p h(T-x)-r h(d+x)-q h(a+x)=0,
\]
\[
E_4:\quad p h(a-x)+r h(e-x)-q h(x)=0,
\]
\[
E_5:\quad p h(a+x)+r h(e+x)+q h(x)=0,
\]
\[
E_6:\quad p h(e+x)-q h(d-x)=0,
\]
\[
E_7:\quad
-p h(d+x)-p h(a+e-x)-r h(2d+x)-r h(T-x)-q h(b+x)=0,
\]
\[
E_8:\quad p h(e-x)-r h(\delta+x)-q h(d+x)=0,
\]
\[
E_9:\quad -p h(e-x)-p h(b+x)-r h(a-x)-q h(a+e-x)=0,
\]
\[
E_{10}:\quad p h(d+\delta+x)+r h(\delta+x)=0,
\]
\[
E_{11}:\quad p h(\delta+x)-r h(e-x)-q h(2e-x)=0,
\]
\[
E_{12}:\quad
-p h(\delta+x)-p h(T-\delta-x)-r h(d+\delta+x)-q h(2d+x)=0,
\]
\[
E_{13}:\quad p h(2e-x)-q h(\delta+x)=0,
\]
\[
E_{14}:\quad
-p h(2e-x)-p h(2d+x)-r h(a+e-x)-r h(3d+x)-q h(T-\delta-x)=0,
\]
\[
E_{16}:\quad -p h(3d+x)-r h(2e-x)-q h(3e-x)=0,
\]
\[
E_{17}:\quad p h(2\delta+x)-q h(a-2\delta-x)=0,
\]
\[
E_{18}:\quad p h(a-2\delta-x)-q h(2\delta+x)=0,
\]
\[
E_{19}:\quad p h(3e-x)+r h(a-2\delta-x)=0.
\]

The attached verifier generates every row from the six raw slots before
looking at this table and returns `EXACT_RAW_ROW_MATCH` for all 18.

## 4. Exact rank 18

Order the 19 variables as
\[
\begin{aligned}
(&h(2\delta+x),h(d+\delta+x),h(\delta+x),h(3d+x),
h(2d+x),h(d-x),h(d+x),h(x),\\
&h(b+x),h(a-x),h(a+x),h(e+x),h(T-x),h(a+e-x),
h(2e-x),h(T-\delta-x),\\
&h(3e-x),h(a-2\delta-x),h(e-x)).
\end{aligned}
\]

Let \(M_{18}\) be the coefficient matrix.

Delete the final column \(Z=h(e-x)\).  Direct exact determinant
calculation gives
\[
\boxed{
\det M_{\widehat Z}
=
-p^6qr(p-q)^3(p+q)^3
(p^2-pr-q^2)(p^2+pr-q^2).
}
\]

Writing
\[
\Delta=p^2-q^2,
\]
this is
\[
-p^6qr(p-q)^3(p+q)^3(\Delta-pr)(\Delta+pr).
\]

The already proved coefficient estimate
\[
\alpha:=\frac{pr}{\Delta}>1
\]
implies
\[
\Delta-pr<0,\qquad \Delta+pr>0.
\]
Also \(p,q,r>0\) and \(p>q\). Hence
\[
\det M_{\widehat Z}\ne0.
\]

Therefore
\[
\boxed{\operatorname{rank}M_{18}=18.}
\]

Since the matrix has 19 columns, its kernel is exactly one-dimensional.

## 5. The one-dimensional mode

Put
\[
X=h(x),\qquad Z=h(e-x),\qquad
\Delta=p^2-q^2.
\]

From \(E_{11},E_{13}\),
\[
h(\delta+x)=\frac{pr}{\Delta}Z.
\]

From \(E_2\),
\[
h(d+x)=\frac{qZ-rX}{p}.
\]

Insert these into \(E_8\):
\[
\boxed{
\Psi Z+qr\Delta X=0,
}
\]
where
\[
\Psi:=\Delta^2-p^2r^2.
\]

Thus
\[
\boxed{
Z=\gamma X,\qquad
\gamma=-\frac{qr\Delta}{\Psi}.
}
\]

Because \(\alpha=pr/\Delta>1\),
\[
\Psi=(\Delta-pr)(\Delta+pr)<0,
\]
so in particular \(\Psi\ne0\).

For the actual coefficients
\[
\gamma\approx0.80257672,\qquad \gamma^2\ne1.
\]

Since the full kernel is one-dimensional, this relation fixes the
ratio of the two distinguished coordinates on the unique local mode.

## 6. Three forced zeros

Let
\[
A=h(2\delta+x),\qquad
W=h(a-2\delta-x).
\]
Then \(E_{17},E_{18}\) are
\[
pA-qW=0,\qquad pW-qA=0.
\]
Hence
\[
(p^2-q^2)A=0,
\]
so
\[
A=W=0.
\]
Then \(E_{19}\) gives
\[
\boxed{h(3e-x)=0.}
\]

Thus every hard-horizon local mode already satisfies
\[
\boxed{
h(2\delta+x)=h(a-2\delta-x)=h(3e-x)=0.
}
\]

## 7. What is and is not proved

Proved in this package, subject to independent reconstruction:

- exact horizon legality of the 18 retained sources;
- exact 18 raw rows;
- exact rank \(18\);
- exactly one local mode;
- its relation \(h(e-x)=\gamma h(x)\);
- the three forced zeros above.

Not proved:
\[
h(x)=0.
\]

The old \(u_{15}\) closure is illegal in this chamber, the direct
\(x\mapsto e-x\) mirror does not return to the same defect system, and
the previously explored 21-step representative chain is not uniform.

Status candidate:
\[
\boxed{\text{Runde 15H local reduction }\checkmark[M]_{\rm part}},
\qquad
\boxed{\text{hard-horizon mode kill }?[O]}.
\]

## 8. Independent review request

Please independently:

1. derive all 18 rows from the raw operator;
2. verify every source horizon;
3. compute the 18x18 minor after deleting \(Z\);
4. verify its factorization and nonvanishing from \(\alpha>1\);
5. verify the short \(\Gamma\)-relation;
6. verify the three forced zeros;
7. search, if possible, for a uniform horizon-legal relation that
   kills the remaining one-dimensional mode.

Do not use the withdrawn 21-step chain as a theorem.
Do not commit or modify P11/R14.
