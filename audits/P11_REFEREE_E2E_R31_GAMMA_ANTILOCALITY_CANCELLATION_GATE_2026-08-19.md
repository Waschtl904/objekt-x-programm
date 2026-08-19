# P11 End-to-End Referee R31 — Gamma anti-locality and the exact annular cancellation gate

Date: 2026-08-19

## Target

Continue R30-F at fixed
\[
0<R<S<T_0
\]
without importing an unverified elliptic/pseudodifferential UCP theorem.
The target remains
\[
R_*(S,T_0)=S\ ?
\]
for the baseline Riesz representative \(\rho_{S,T_0}\), equivalently nonvanishing of the normal mismatch for every strict source inclusion.

No conclusion in this audit is a polar-gauge, terminal-transport, Object-X, or RH conclusion.

## Repo sync

The `main` head checked before this audit is

`80cf872e3cbde425bd1bf1cb2cddff6f6ed438f5` — `Tighten R30 support-domain typing`.

The R30 paper module and reconciliation are therefore the current inputs.

---

## 1. Exact Gamma symbol available from the frozen P02 layer

P02 fixes the Fourier convention
\[
\widehat f(\xi)=\int_{\mathbb R}f(u)e^{i\xi u}\,du,
\qquad
f(u)=\frac1{2\pi}\int_{\mathbb R}\widehat f(\xi)e^{-i\xi u}\,d\xi,
\]
and the archimedean logarithmic derivative
\[
\gamma_\infty(\xi)
=-\frac12\log\pi
+\frac12\psi\!\left(\frac14+\frac{i\xi}{2}\right).
\]
Thus the exact even diagonal Gamma symbol is
\[
q_\Gamma(\xi)
:=2\operatorname{Re}\gamma_\infty(\xi)
=-\log\pi+\operatorname{Re}\psi\!\left(\frac14+\frac{i\xi}{2}\right).
\tag{R31.1}
\]

P11 itself currently records only
\[
m_\Gamma=1+g_\infty,
\qquad m_\Gamma(\xi)\asymp\log(2+|\xi|),
\]
so the exact identification of its symbol with an affine renormalisation of (R31.1) must be kept explicit below.

---

## 2. Off-diagonal kernel of the exact Gamma symbol

For \(a=1/4\), the classical digamma series on \(\operatorname{Re}z>0\) gives
\[
\psi(z)
=-\gamma+\sum_{n=0}^\infty
\left(\frac1{n+1}-\frac1{n+z}\right).
\]
Hence, modulo an additive constant in the multiplier,
\[
q_\Gamma(\xi)
\equiv
-\sum_{n=0}^\infty
\frac{n+a}{(n+a)^2+\xi^2/4}.
\tag{R31.2}
\]
For
\[
\lambda_n:=2(n+a)=2n+\frac12,
\]
one has
\[
\frac{n+a}{(n+a)^2+\xi^2/4}
=\frac{2\lambda_n}{\lambda_n^2+\xi^2}.
\]
Under the binding P02 Fourier convention,
\[
\mathcal F(e^{-\lambda|u|})(\xi)
=\frac{2\lambda}{\lambda^2+\xi^2}.
\]
Therefore the inverse Fourier kernel of \(q_\Gamma\), away from the diagonal \(u=0\), is
\[
\boxed{
K_\Gamma(u)
=-\sum_{n=0}^\infty e^{-\lambda_n|u|}
=-\frac{e^{-|u|/2}}{1-e^{-2|u|}},
\qquad u\ne0.
}
\tag{R31.3}
\]
The omitted multiplier constant contributes only a multiple of \(\delta_0\); it has no effect off the support of the input.
More generally any affine renormalisation
\[
m(\xi)=c_0+c_1q_\Gamma(\xi),\qquad c_1\ne0,
\tag{R31.4}
\]
has off-diagonal kernel \(c_1K_\Gamma\).

Status:
\[
\boxed{\text{R31-A (exact P02 Gamma off-diagonal kernel)}\quad\checkmark[M].}
\]

---

## 3. Pure-Gamma anti-locality

### Theorem R31-B

Let \(f\in L^2(\mathbb R)\) satisfy
\[
\operatorname{ess\,supp}f\subset[-R,R],
\qquad f\ne0.
\]
Let \(M_\Gamma\) be the full-line multiplier with symbol (R31.4).
Then \(M_\Gamma f\) cannot vanish on a nonempty open interval contained in \((R,\infty)\). The analogous statement holds on the left of \(-R\).

Equivalently, for every \(S>R\), the restriction of the Gamma tail to \((R,S)\) is not identically zero.

### Proof

For \(x>R\), the local/delta part vanishes and (R31.3) gives
\[
(M_\Gamma f)(x)
=-c_1\sum_{n=0}^\infty
 e^{-\lambda_nx}M_n(f),
\tag{R31.5}
\]
where
\[
M_n(f):=\int_{-R}^{R}f(y)e^{\lambda_n y}\,dy.
\tag{R31.6}
\]
For every \(\delta>0\), the series in (R31.5) converges normally on
\(\operatorname{Re}x\ge R+\delta\), since
\[
|M_n(f)|
\le \|f\|_{L^1(-R,R)}e^{\lambda_nR}.
\]
Thus the right tail is real analytic on \((R,\infty)\). If it vanishes on one nonempty open subinterval, the identity theorem gives zero on all of \((R,\infty)\).

Multiply (R31.5) by \(e^{\lambda_0x}\) and let \(x\to\infty\). Normal convergence gives \(M_0(f)=0\). Remove the first term and repeat inductively; hence
\[
M_n(f)=0\qquad(n\ge0).
\tag{R31.7}
\]
Since \(\lambda_n=2n+1/2\), put
\[
h(y):=e^{y/2}f(y).
\]
Then (R31.7) becomes
\[
\int_{-R}^{R} h(y)e^{2ny}\,dy=0
\qquad(n\ge0).
\]
With \(t=e^{2y}\), this says that the finite complex measure
\[
d\mu(t)
=\frac{h(\frac12\log t)}{2t}\,dt
\]
on the compact interval \([e^{-2R},e^{2R}]\) annihilates every polynomial. By uniform density of polynomials in the continuous functions on this compact interval, \(\mu=0\), hence \(h=0\) a.e. and therefore \(f=0\), contradiction.

The left-tail statement follows identically.
\(\square\)

Status:
\[
\boxed{\text{R31-B (pure exact-Gamma anti-locality)}\quad\checkmark[M].}
\]

### Firewall

R31-B is a theorem for the exact P02 Gamma symbol and every affine renormalisation (R31.4).
It must not be silently transferred from the mere asymptotic statement
\(m_\Gamma\asymp\log(2+|\xi|)\).
The current P11 equation (2.7) does not itself display the exact affine bridge (R31.4).

Thus the manuscript-level interface
\[
\boxed{
m_\Gamma=c_0+c_1q_\Gamma\quad(c_1\ne0)
}
\tag{R31.8}
\]
should be made explicit before R31-B is cited as a theorem about the concrete P11 operator \(C_{\Gamma,S}\).
This is an interface/documentation obligation, not an uncertainty about the frozen P02 formula.

---

## 4. Exact annular residual for the actual P11 Riesz problem

Put
\[
A_X^{[T_0]}:=C_{\Gamma,X}+\Sigma_X^{[T_0]},
\qquad
A_X^{[T_0]}\rho_{X,T_0}=\phi_X.
\]
For \(0<R<S<T_0\), define the inherited old-source candidate
\[
j_{R,S}:=E_{R,S}\rho_{R,T_0}
\tag{R31.9}
\]
and its full S-level residual
\[
\boxed{
\Delta_{R,S}^{[T_0]}
:=\phi_S-A_S^{[T_0]}j_{R,S}.
}
\tag{R31.10}
\]
Because the fixed-\(T_0\) forms obey exact pullback compatibility and
\(E_{R,S}^*\phi_S=\phi_R\),
\[
E_{R,S}^*\Delta_{R,S}^{[T_0]}=0.
\tag{R31.11}
\]
Hence \(\Delta_{R,S}^{[T_0]}\) vanishes a.e. on \((-R,R)\) and is an annular defect supported in
\[
\mathcal A_{R,S}:=(-S,-R)\cup(R,S).
\]

### Theorem R31-C — exact cancellation criterion

For every \(0<R<S<T_0\),
\[
\boxed{
\Delta_{R,S}^{[T_0]}=0
\iff
\rho_{S,T_0}=E_{R,S}\rho_{R,T_0}
\iff
s_{R,S,T_0}=0.
}
\tag{R31.12}
\]
Consequently, for fixed \(S<T_0\),
\[
\boxed{
R_*(S,T_0)=S
\iff
\Delta_{R,S}^{[T_0]}\ne0
\quad\text{for every }0<R<S.
}
\tag{R31.13}
\]

### Proof

If \(\Delta_{R,S}^{[T_0]}=0\), then \(j_{R,S}\) solves the S-level Riesz equation. Coercivity gives uniqueness, so
\(j_{R,S}=\rho_{S,T_0}\). Conversely, if
\(\rho_{S,T_0}=j_{R,S}\), its defining equation gives \(\Delta=0\). The equivalence with \(s=0\) is exactly the R30 support-compatibility theorem. The last statement follows from the one-threshold R30 classification.
\(\square\)

Status:
\[
\boxed{\text{R31-C (annular residual gate)}\quad\checkmark[M].}
\]

This is terminal-parameter free once \(S,T_0\) are fixed.

---

## 5. What a compactly supported baseline normal would force

Assume the exact-symbol bridge (R31.8), and suppose for contradiction that
\[
R_*(S,T_0)\le R<S.
\]
Then R30 gives
\[
\rho_{S,T_0}=j_{R,S}.
\]
On the annulus \(\mathcal A_{R,S}\), equation (R31.10) therefore becomes the exact cancellation identity
\[
\boxed{
1_{\mathcal A_{R,S}}\Sigma_S^{[T_0]}j_{R,S}
=
1_{\mathcal A_{R,S}}\phi_S
-
1_{\mathcal A_{R,S}}C_{\Gamma,S}j_{R,S}.
}
\tag{R31.14}
\]
The Gamma term on each connected half-annulus is real analytic by R31-B, with explicit exponential expansion (R31.5). The forcing \(\phi_S\) is real analytic away from the origin. Therefore compact support of the baseline normal would force the concrete Feshbach tail to coincide on an open annulus with a very specific analytic function.

R31-B also shows that the Gamma tail itself cannot vanish on any open subannulus for a nonzero inherited vector.

But this is not yet a contradiction: the Schur/Feshbach term is nonlocal and may, in principle, cancel the Gamma tail together with the explicit forcing.

---

## 6. Coarse Schur information is insufficient — explicit countermodel

The present repo proves for the concrete fixed-horizon Schur term:

- boundedness and positivity on \(L^2\);
- parity compatibility;
- boundedness on a small Sobolev window via O3k;
- a positive Feshbach factorisation.

These properties alone cannot imply R30-F.

### Theorem R31-D — method no-go

Let \(H=L^2(-S,S)\) on the real odd sector, let \(C\ge I\) be the exact even Gamma multiplier restricted to the window, and let \(\phi=\phi_S\ne0\) be the odd R30 forcing. Fix any \(0<R<S\).
Then there exist

1. a nonzero \(\rho\in C_c^\infty((-R,R))\) in the odd sector, and
2. a bounded positive selfadjoint rank-one operator \(\Sigma\ge0\), parity preserving and bounded on every sufficiently small Sobolev scale \(H^s\),

such that
\[
(C+\Sigma)\rho=\phi.
\tag{R31.15}
\]
Moreover \(\Sigma\) has an abstract positive Feshbach factorisation
\[
\Sigma=H_0B_0H_0^*,
\qquad
B_0=(I+0^*0)^{-1}=I.
\tag{R31.16}
\]

### Proof

Choose a real odd \(h\in C_c^\infty((-R,R))\) with
\[
\langle h,\phi\rangle>0.
\]
Such an \(h\) exists because \(\phi\) is a nonzero real odd function on every strict source interval.
For \(\varepsilon>0\) put
\[
\rho:=\varepsilon h,
\qquad
d:=\phi-C\rho.
\]
Since \(h\) is a smooth interior vector, \(h\in\mathcal D(C)\) and \(Ch\in L^2\). For sufficiently small \(\varepsilon\),
\[
\langle\rho,d\rangle
=
\varepsilon\langle h,\phi\rangle
-
\varepsilon^2\langle h,Ch\rangle
>0.
\tag{R31.17}
\]
Work in the real Hilbert space of real odd vectors. Put
\[
e:=\frac{\rho}{\|\rho\|},
\qquad
y:=\frac d{\|\rho\|},
\qquad
a:=\langle e,y\rangle>0,
\qquad
z:=y-ae\perp e.
\]
Define
\[
v:=\sqrt a\,e+\frac1{\sqrt a}z,
\qquad
\Sigma f:=\langle f,v\rangle v.
\tag{R31.18}
\]
Then \(\Sigma\) is positive, selfadjoint and rank one, and
\[
\Sigma e
=\langle e,v\rangle v
=\sqrt a\,v
=ae+z
=y.
\]
Hence \(\Sigma\rho=d\), proving (R31.15).

All vectors in the construction are odd, so \(\Sigma\) preserves parity. For a smooth interior \(h\), the Gamma action is arbitrarily Sobolev regular before the fixed endpoint cutoff; after zero extension, both \(Ch\) and \(\phi_S\) lie in \(H^s(\mathbb R)\) for every sufficiently small \(|s|<1/2\). Thus the rank-one map in (R31.18) is bounded on a symmetric sufficiently small Sobolev interval. Finally take \(H_0=\Sigma^{1/2}\) and \(B_0=I\) to obtain (R31.16).
\(\square\)

### Meaning of R31-D

R31-D is **not** a counterexample to the concrete P11 operator
\[
\Sigma_S^{[T_0]}
=E_{S,T_0}^*H_{T_0}(I+R_{T_0}^*R_{T_0})^{-1}H_{T_0}^*E_{S,T_0}.
\]
It is a counterexample to the proof strategy that uses only positivity, boundedness, parity, small-Sobolev regularity, and an abstract positive Feshbach factorisation.
Any proof of R30-F must use additional **concrete** off-support structure of the P11 \(H_{T_0},R_{T_0},B_{T_0}\) combination, or a UCP/cancellation theorem whose hypotheses are checked for that exact operator.

Status:
\[
\boxed{
\text{``Gamma anti-locality + currently proved coarse Schur properties imply R30-F''}
\quad\times[M].
}
\]

---

## 7. Why finite translation support does not presently close the gate

At fixed \(T_0\), \(H_{T_0}\) and the resolved coordinates of \(R_{T_0}\) are finite sums of translations, interval cutoffs and finite coefficient maps. However
\[
B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1}
\]
is an inverse on the whole fixed window. O3k proves its boundedness on a small Sobolev interpolation strip; it does not prove finite propagation, support preservation, or analyticity preservation.

Therefore no step of the form
\[
\operatorname{supp}\rho\subset[-R,R]
\Longrightarrow
\Sigma_S^{[T_0]}\rho=0
\quad\text{near }\pm S
\]
is currently justified.

Status: finite-propagation closure for the concrete Schur term remains
\[
\boxed{?[O].}
\]

---

## 8. R31 verdict and exact next gate

| Item | Status |
|---|---|
| Exact P02 Gamma off-diagonal kernel (R31.3) | ✓[M] |
| Pure exact-Gamma anti-locality R31-B | ✓[M] |
| Exact P11 annular residual criterion R31-C | ✓[M] |
| Exact affine P02-to-P11 symbol bridge displayed in current P11 | ?[O] manuscript/interface gate |
| Gamma anti-locality + coarse Schur properties alone prove R30-F | ×[M] |
| Concrete annular noncancellation for the actual P11 Schur term | ?[O] |
| R30-F: \(R_*(S,T_0)=S\) | ?[O] |
| Polar gauge / terminal transport consequence | not obtained |

The mathematically exact next task is now:

> For every fixed \(0<R<S<T_0\), prove
> \[
> \Delta_{R,S}^{[T_0]}\ne0,
> \]
> equivalently rule out the concrete annular identity (R31.14) for
> \(j_{R,S}=E_{R,S}\rho_{R,T_0}\).

A successful route must use at least one property not present in the abstract countermodel R31-D. Candidate properties are:

1. an explicit off-support representation of
   \(H_{T_0}(I+R_{T_0}^*R_{T_0})^{-1}H_{T_0}^*\);
2. a rigidity theorem for the exact annular Schur tail;
3. an exact-symbol nonlocal UCP theorem verified against the full Gamma + Feshbach operator;
4. a direct incompatibility between the exponential-moment Gamma tail (R31.5) and the concrete prime-translation/rest-inverse tail.

Until one of these is proved,
\[
\boxed{R_*(S,T_0)=S\quad ?[O].}
\]

The R14 firewall remains unchanged: even a future positive solution of R30-F/R31 would be an inverse-functional-calculus obstruction, not a polar-gauge or terminal-transport no-go.