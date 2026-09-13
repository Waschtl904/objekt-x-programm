# P11 NP-OVERLAP — exact shift fibers, single-channel No-Go, and Prime-Power AR(1)

**Date:** 2026-09-13  
**Status:** theorem-level project audit; no Registry promotion.  
**Parent:** NP-GAP review correction / centered Prime-overlap form.

## 1. Purpose

The centered null-pole Weil form is

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

where

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

This audit determines the exact finite-window geometry of the individual shift correlations and then groups all prime powers of one prime.  The result reconnects the new NP-OVERLAP front exactly to the previously discovered Prime-Power AR(1) geometry.

---

## 2. Compressed symmetric shift

Let

```math
I_a=(-a,a),
```

and for `t>0` define on `L^2(I_a)` (zero extension outside `I_a`)

```math
S_t:=\frac12(T_t+T_{-t}).
```

Then

```math
\langle v,S_tv\rangle
=\operatorname{Re}\langle T_tv,v\rangle.
```

If `t>=2a`, the shifted supports are disjoint and

```math
S_t=0.
```

Assume henceforth `0<t<2a`.

---

## 3. Exact fiber decomposition modulo `t` `✓[M]`

Decompose `I_a` into orbits of the translation lattice `t Z`.  For a residue parameter `r` in a fundamental interval of length `t`, let

```math
I_a\cap(r+t\mathbb Z)
=\{x_1(r)<\cdots<x_{N(r)}(r)\}.
```

On this fiber, translation by `±t` connects nearest neighbours.  Therefore `S_t` is unitarily equivalent to the direct integral of the finite matrices

```math
J_N
=\frac12
\begin{pmatrix}
0&1&&&\\
1&0&1&&\\
&1&0&\ddots&\\
&&\ddots&\ddots&1\\
&&&1&0
\end{pmatrix}
```

with `N=N(r)`.

The eigenvalues of `J_N` are

```math
\cos\frac{k\pi}{N+1},
\qquad k=1,\ldots,N.
```

The maximum possible fiber length is

```math
\boxed{
N_{a,t}=\left\lceil\frac{2a}{t}\right\rceil.
}
```

A set of residue parameters of positive measure has exactly this length.  Hence

```math
\boxed{
\|S_t\|_{L^2(I_a)}
=\cos\frac{\pi}{N_{a,t}+1}
=\cos\left(\frac{\pi}{\lceil2a/t\rceil+1}\right).
}
```

This formula also tends correctly to `0` at the disjoint-support boundary `t>=2a`.

---

## 4. Null-pole does not improve a single shift `✓[M]_neg`

Let

```math
D_{NP}(a)
=\{v\in C_c^\infty(I_a):E_+(v)=E_-(v)=0\}.
```

Choose an open residue subinterval on which the fiber length is constantly `N=N_{a,t}` and whose translated fiber intervals stay away from the endpoints `±a`.  Let

```math
c_j=\sin\frac{j\pi}{N+1},
\qquad j=1,\ldots,N,
```

be the positive top eigenvector of `J_N`.

For `g\in C_c^\infty` of that residue subinterval define along the fiber pieces

```math
v(x_j(r))=c_j g(r).
```

Then `v\in C_c^\infty(I_a)` and

```math
S_tv=\cos\frac{\pi}{N+1}\,v.
```

Moreover the two null-pole moments factor as

```math
E_\pm(v)
=C_\pm\int g(r)e^{\pm r/2}dr,
```

for nonzero constants `C_\pm` depending only on the fiber eigenvector and the translated positions.  Since `C_c^\infty` of the residue subinterval is infinite-dimensional, choose nonzero `g` in the joint kernel of the two linear functionals

```math
g\mapsto\int g(r)e^{r/2}dr,
\qquad
g\mapsto\int g(r)e^{-r/2}dr.
```

Then `v\in D_{NP}(a)` and still attains the top shift eigenvalue.  Consequently

```math
\boxed{
\sup_{0\ne v\in D_{NP}(a)}
\frac{\operatorname{Re}\langle T_tv,v\rangle}{\|v\|^2}
=
\cos\left(\frac{\pi}{\lceil2a/t\rceil+1}\right).
}
```

### Consequence

The two null-pole constraints do **not** lower the sharp norm of an individual compressed shift channel.

Therefore any all-window proof that bounds each Prime-Power overlap separately by its single-shift norm cannot gain anything from the null-pole restriction at the one-channel level.  A successful proof must exploit collective structure between several shifts and/or their coupling to the archimedean operator.

Status:

```text
single-shift null-pole norm improvement  ×[M]
```

This is an architecture-class No-Go, not a No-Go for NP-OVERLAP itself.

---

## 5. Group the overlap by prime

Fix a prime `p` and set

```math
\ell_p:=\log p,
\qquad
q_p:=p^{-1/2}.
```

All powers `n=p^k` contribute

```math
\frac{\Lambda(p^k)}{\sqrt{p^k}}
=(\log p)q_p^k.
```

Define the full `p`-overlap block

```math
\mathbf O_{p,a}
:=2(\log p)
\sum_{k\ell_p<2a}q_p^k S_{k\ell_p}.
```

Then

```math
\boxed{
\mathbf O_a
=\sum_{p:\ \log p<2a}\mathbf O_{p,a}.
}
```

---

## 6. Exact AR(1) fiber matrix for one prime `✓[M]`

Fiberize now modulo `ell_p=log p`.  On a fiber containing `N` points, every pair of distinct points differs by exactly `k ell_p` for some `1<=k<=N-1`, and the corresponding prime-power coefficient is `(log p)q_p^k`.

Hence the fiber matrix is

```math
\boxed{
\mathbf O_{p,a}^{(N)}
=(\log p)\left(R_{q_p}^{(N)}-I_N\right),
}
```

where

```math
\boxed{
R_q^{(N)}=(q^{|j-k|})_{1\le j,k\le N}.
}
```

This is the Kac--Murdock--Szego / AR(1) correlation matrix.

Thus the Prime-Power AR(1) structure is not merely analogous to NP-OVERLAP: it is the **exact fiberwise matrix of the complete overlap block belonging to one prime**.

---

## 7. AR(1) inverse and positive sector

For `0<q<1`, `R_q^{(N)}` is strictly positive and its inverse is the familiar tridiagonal precision matrix

```math
(R_q^{(N)})^{-1}
=\frac{1}{1-q^2}
\begin{pmatrix}
1&-q&&&\\
-q&1+q^2&-q&&\\
&\ddots&\ddots&\ddots&\\
&&-q&1+q^2&-q\\
&&&-q&1
\end{pmatrix}.
```

Equivalently, if

```math
Z(\theta)=\sum_{j=0}^{N-1}z_j e^{ij\theta},
```

then

```math
z^*R_q^{(N)}z
=\frac{1}{2\pi}\int_{-\pi}^{\pi}
P_q(\theta)|Z(\theta)|^2d\theta,
```

where the Poisson/AR(1) symbol is

```math
P_q(\theta)
=\frac{1-q^2}{1-2q\cos\theta+q^2}.
```

Therefore the centered Prime overlap block has symbol

```math
\boxed{
P_q(\theta)-1
=\frac{2q(\cos\theta-q)}{1-2q\cos\theta+q^2}.
}
```

Its positive spectral sector is exactly

```math
\boxed{\cos\theta>q,}
```

i.e.

```math
|\theta|<\arccos q
```

modulo `2pi`.

The dangerous directions for one prime are therefore low-frequency modes on that prime's logarithmic lattice.

---

## 8. Distinct primes give incommensurable lattices `✓[M]`

For distinct primes `p!=r`,

```math
\frac{\log p}{\log r}\notin\mathbb Q.
```

Indeed, a rational relation `log p/log r=m/n` would imply `p^n=r^m`, contradicting unique factorization.

Thus the exact AR(1) fiberizations for different primes live on mutually incommensurable translation lattices.

This isolates a plausible genuinely collective mechanism:

> a vector that is near the positive low-frequency sector of one prime's AR(1) block need not be simultaneously near the positive low-frequency sectors of many incommensurable prime lattices.

No quantitative multi-prime domination is claimed yet.

---

## 9. New NP-OVERLAP subfront

The all-window target remains

```math
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\sum_p\mathbf O_{p,a}|_{D_{NP}(a)}.
```

The preferred next mechanisms are now:

1. exploit the exact AR(1) matrices `R_{p^{-1/2}}^{(N)}-I` prime by prime;
2. quantify incompatibility of their positive low-frequency sectors across incommensurable `log p` lattices;
3. combine this with the `Q_0` Sobolev transport and the archimedean surplus;
4. compare with the previously proved Prime-Power AR(1)/Weil-tail factorizations and determine whether their contractive/Markov structure supplies the needed collective bound.

A proof based only on independent one-shift norm estimates is now explicitly deprioritized by Section 4.

---

## 10. Status

```text
exact compressed single-shift fiber decomposition             ✓[M]
exact single-shift norm                                       ✓[M]
null-pole single-shift norm improvement                       ×[M]
prime grouping of O_a                                         ✓[M]
exact KMS/AR(1) fiber matrix O_{p,a}^{(N)}                    ✓[M]
AR(1) low-frequency positive-sector description               ✓[M]
incommensurability of distinct prime logarithmic lattices      ✓[M]
quantitative collective multi-prime suppression                ?[O]
all-a NP-OVERLAP domination                                    ?[O]
full positive Object-X / RH                                    ?[O]
```

Registry and Object-X working definition remain unchanged.
