# P12 Runde 23 — first exact overlap seed below \(\rho\)

**Status:** local theorem candidate; not committed; independent raw-row review required.  
**Purpose:** prove a genuine nonempty overlap cell with \(R<\rho\), using a new exact two-sheet \(42\times42\) source block.  
**Firewall:** P11 FROZEN; R14 unchanged; no Object-X/RH implication.

## 1. Constants

Use
\[
\delta=\frac12\log\frac98,\qquad
e=\frac12\log\frac43,\qquad
\varepsilon_{\max}=\frac12\log\frac54,
\]
\[
\rho=\frac12\log\frac{10}{9},
\qquad
\omega:=\frac e2-\rho
=\frac14\log\frac{27}{25},
\]
\[
\eta:=e-2\delta=\frac12\log\frac{256}{243},
\]
\[
\chi:=3\delta-e=\frac12\log\frac{2187}{2048},
\qquad
\kappa:=e-\delta=\frac12\log\frac{32}{27}.
\]

Numerically,
\[
\omega\approx0.01924026028,\quad
\eta\approx0.02605800057,\quad
\chi\approx0.03283351726,
\]
\[
\rho\approx0.05268025783.
\]

Thus the cell below is genuinely below the previous global threshold \(\rho\).

---

## 2. Seed cell

Let
\[
0<R<x<\sigma<\varepsilon<\varepsilon_{\max}
\]
and assume

\[
\boxed{
\begin{aligned}
&\omega<R,\\
&\eta<x<\chi,\\
&R+x<\delta<\sigma+x<\kappa,\\
&\sigma-x<\eta,\\
&\kappa<\varepsilon+x,\\
&x+\eta<\varepsilon.
\end{aligned}}
\tag{C23}
\]

This is a nonempty open polyhedral cell in the variables
\((R,\sigma,\varepsilon,x)\); for example

\[
R=0.020,\qquad x=0.030,\qquad
\sigma=0.040,\qquad \varepsilon=0.060
\]
lies strictly inside it.

The claim is:

\[
\boxed{h(x)=0}
\tag{2.1}
\]
for every kernel vector \(h\) and a.e. \(x\) satisfying (C23).

---

## 3. Forty-two horizon-legal sources

Write sources in affine coordinates
\[
u=sx+me+n\delta
\]
as triples \((s,m,n)\).

Use exactly the following 42 sources.

### Negative sheet \(s=-1\)

\[
\begin{aligned}
&(-1,0,1),(-1,0,2),\\
&(-1,1,0),(-1,1,1),(-1,1,2),(-1,1,3),\\
&(-1,2,0),(-1,2,1),(-1,2,2),(-1,2,3),(-1,2,4),\\
&(-1,3,0),(-1,3,1),(-1,3,2),(-1,3,3),(-1,3,4),\\
&(-1,4,0),(-1,4,1),(-1,4,2),(-1,4,3),\\
&(-1,5,1).
\end{aligned}
\]

### Positive sheet \(s=+1\)

\[
\begin{aligned}
&(1,0,0),(1,0,1),\\
&(1,1,-1),(1,1,0),(1,1,1),(1,1,2),\\
&(1,2,-1),(1,2,0),(1,2,1),(1,2,2),(1,2,3),\\
&(1,3,-1),(1,3,0),(1,3,1),(1,3,2),(1,3,3),\\
&(1,4,-1),(1,4,0),(1,4,1),(1,4,2),\\
&(1,5,0).
\end{aligned}
\]

At every one of these sources reconstruct the six canonical raw slots from

\[
Lh(u)=
p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)].
\tag{3.1}
\]

Apply only odd reflection and the support cutoff
\[
R<|\cdot|<T+\sigma.
\]

The inequalities (C23) fix every source-horizon and support decision.
The resulting live visibility set contains exactly 42 coordinates.
Hence the raw equations form a square matrix \(M_{42}\).

The retained verifier reconstructs all 42 rows directly from (3.1);
no reduced row is inserted by hand.

---

## 4. Exact determinant

Exact symbolic elimination gives

\[
\boxed{
\det M_{42}
=
-p^{14}r^4\,F_-(p,q,r)\,F_+(p,q,r),
}
\tag{4.1}
\]
where \(F_\pm\) are homogeneous of degree 12.

It is cleaner to normalize
\[
\beta:=q/p,\qquad v:=(r/p)^2.
\]

Then
\[
F_\pm=p^{12}(A\pm C),
\]
with

\[
\begin{aligned}
A={}&
3\beta^{12}
-\beta^{10}v-18\beta^{10}
-7\beta^8v+45\beta^8\\
&-\beta^6v^3-3\beta^6v^2+38\beta^6v-60\beta^6\\
&-\beta^4v^3+21\beta^4v^2-62\beta^4v+45\beta^4\\
&+8\beta^2v^3-33\beta^2v^2+43\beta^2v-18\beta^2\\
&+2v^4-9v^3+15v^2-11v+3,
\end{aligned}
\tag{4.2}
\]

and the odd part factors compactly as

\[
\boxed{
C=
2\beta^3v^2(\beta^2-1)(2\beta^2+v-2).
}
\tag{4.3}
\]

For the actual P12 weights,

\[
\beta=2^{-3/4},
\qquad
v=
\frac{\log3}{\log2}\sqrt{\frac8{27}}.
\]

The exact-rational interval verifier encloses these quantities and obtains

\[
A-C\in
(-0.206613568708064,\,-0.206613568708063),
\]
\[
A+C\in
(-0.032569913367755,\,-0.032569913367754).
\]

The interval endpoints are not floating assumptions: the verifier derives
rational enclosures for \(\log2,\log3\) from the positive atanh series,
and rational brackets for the algebraic roots by exact power comparisons.

Therefore

\[
F_-F_+\ne0
\]
and, since \(p,r>0\),

\[
\boxed{\det M_{42}\ne0.}
\tag{4.4}
\]

Thus all 42 visibility coordinates vanish, in particular

\[
\boxed{h(x)=0.}
\]

---

## 5. Why this matters

This is not yet a full descent from \(\rho\) to \(\omega\).  It proves one
explicit nonempty overlap cell below \(\rho\).

Its structural significance is stronger than a random numerical rank event:

- the certificate is a closed square raw-operator block;
- it consists of 21 sources on each of two reflected lattice sheets;
- its determinant is exactly factored;
- nondegeneracy is certified with rational interval arithmetic;
- the support pattern is stable throughout the whole open cell (C23).

This is the first exact finite overlap block found below the previous
\(\rho\)-threshold.

**Booking before independent review:** `?[O] -> local theorem candidate`.

No global \(R\ge\omega\) theorem is claimed here.
