# A coupled spectral C1 candidate with a compact Gram defect

2026-09-20. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `f77116a890410dfbb2c612956dee9e5342247cd7`.

This package constructs a specific candidate, rather than another broad
exclusion class. It gives an infinite-dimensional positive target, an explicit
common Prime/Gamma spectral readout, actual readout transition maps, and an
exact nonzero Gram error. The error becomes a compact operator of infinite
rank on the new target. No positivity of the desired Weil form is used in
the construction.

**Closed:** the stated candidate-construction and transition interfaces.
**Not closed:** C1c (exact positive Weil-Gram identity), a positive C1 mediator
for the full band, Moving-191D Low/Profile renewal, or Objekt X.

The construction has a fixed physical horizon 1. All windows below share
the same spectral functions. It is intrinsic to the physical Prime/Gamma
data and this declared horizon, not claimed uniquely canonical among all
possible constructions or compatible with arbitrarily larger horizons.

## 1. Physical sources and the exact joint symbol

Use the inherited full-line zero-extended spaces

\[
 W_a=H^1_0((-a,a))\cap\ker E_+\cap\ker E_-,\qquad
 E_\pm u=\int u(x)e^{\pm x/2}\,dx,
 \qquad B=\tfrac12\log5\le a\le1.
\]

The two constraints are unchanged. The inherited near-null source is not
modified or renormalized. Use the unitary Fourier convention
\(\widehat u(\xi)=(2\pi)^{-1/2}\int e^{-ix\xi}u(x)dx\), and inner products
conjugate-linear in their first argument. Reflection and parity have their
usual physical meanings.

The inherited physical form is

\[
 q_a(u,v)=\Gamma(u,v)-\kappa\langle u,v\rangle
 -\sum_{q\in Q}w_q\langle u,(\tau_{\ell_q}+\tau_{-\ell_q})v\rangle,
 \tag{1}
\]
\[
 k(r)=\frac{e^{-r/2}}{1-e^{-2r}},\quad
 \Gamma(u,v)=\int_0^\infty k(r)
 \langle\tau_ru-u,\tau_rv-v\rangle dr,
 \quad\kappa=\log(8\pi)+\gamma+\pi/2,
\]
\[
 Q=\{2,3,4,5,7\},\qquad \ell_q=\log q,\qquad
 w_q=\Lambda(q)/\sqrt q.
\]

In particular, \(w_4=\log2/2\), not \(\log4/2\). Since
\(\log7<2<\log8\), every omitted prime power has zero correlation on
sources supported in \([-a,a]\), \(a\le1\). A channel in Q that is inactive
on a smaller window likewise contributes zero to (1). At an exact activation
endpoint the contact has measure zero.

Write \(\lambda_j=2j+1/2\). Geometric expansion of k, Tonelli on quadratic
energies, and polarization give

\[
 g(\xi)=2\int_0^\infty k(r)(1-\cos(r\xi))dr
 =\sum_{j=0}^\infty\frac{2\xi^2}{\lambda_j(\lambda_j^2+\xi^2)},
 \qquad \Gamma(u,v)=\int g\,\overline{\widehat u}\widehat v.
 \tag{2}
\]

The entire infinite Gamma series is retained. Its sum is continuous, even,
nonnegative, strictly positive off zero, and increasing in \(|\xi|\).
For fixed real M and N>=1 its omitted tail obeys

\[
 0\le g(M)-\sum_{j=0}^{N-1}
 \frac{2M^2}{\lambda_j(\lambda_j^2+M^2)}
 \le 2M^2\left(\lambda_N^{-3}+\frac1{4\lambda_N^2}\right).
 \tag{3}
\]

Indeed, bound each summand by \(2M^2/\lambda_j^3\), then bound the
decreasing series by its first term plus its integral. Also
\(g(\xi)\le(131/8)\xi^2\): the j=0 coefficient is 16, and the remaining
coefficient is at most \(\tfrac14\sum_{j\ge1}j^{-3}\le3/8\).
If \(M\ge\lambda_{n-1}\), then

\[
 g(M)\ge\sum_{j=0}^{n-1}\lambda_j^{-1}
 >\tfrac12\sum_{j=1}^n j^{-1}\longrightarrow\infty.
 \tag{4}
\]

Put

\[
 \omega=\sum_{q\in Q}w_q,\quad
 c(\xi)=\sum_{q\in Q}w_q\cos(\ell_q\xi),\quad
 s=\kappa+2\omega.
\]

The exact interval ledger proves

\[
 5<\kappa<11/2,\qquad 5/2<\omega<3,\qquad
 10<s<23/2<12.                                      \tag{5}
\]

No positivity of q enters these bounds. Thus (1) has symbol
\(w(\xi)=g(\xi)-\kappa-2c(\xi)\) on the declared compact-source class.
This finite-horizon symbol is not an assertion about the unrestricted global
Weil test class.

## 2. Explicit positive target and coupled readout

Define the three real, even spectral functions

\[
 A=g+s,\qquad m=g+\omega-c,\qquad n=\kappa+\omega+c.
 \tag{6}
\]

They satisfy pointwise

\[
 A>0,\quad m\ge g\ge0,\quad \kappa\le n\le s,\quad
 m+n=A,\quad m-n=w.                                  \tag{7}
\]

Use the fixed positive Hilbert space \(H=L^2(\mathbb R,d\xi)\). The
candidate and defect outputs are the concrete linear maps

\[
 \boxed{Tu=\frac{m}{\sqrt A}\widehat u,\qquad
 Du=\frac{n}{\sqrt A}\widehat u.}                    \tag{8}
\]

These formulas are defined before any sign decision for q. The only square
root is that of the explicitly positive archimedean envelope \(g+s\).
They are not square roots or GNS completions of a presumed positive q.

The numerator m is itself the joint jump-energy symbol:

\[
 \int m|\widehat u|^2=\Gamma[u]
 +\frac12\sum_{q\in Q}w_q\|\tau_{\ell_q}u-u\|^2.
 \tag{9}
\]

However, T is one common spectral output, not the orthogonal sum of features
representing the individual signed Prime contributions. Its Gram multiplier
is \((g+\omega-c)^2/(g+s)\), including Gamma/Prime and Prime/Prime cross
terms. For example the numerator contains \(-2gc\) and \(c^2\), with
\(c^2=\sum_{p,q}w_pw_q\cos(\ell_p\xi)\cos(\ell_q\xi)\).
The same denominator organizes both outputs. Indefinite individual Prime
observations therefore cause no contradiction with positivity of H.

The crucial exact identity is the difference of two squares:

\[
 \frac{m^2-n^2}{A}=\frac{(m-n)(m+n)}A=w.
\]

Consequently, for all actual sources,

\[
 \boxed{q_a(u,v)=\langle Tu,Tv\rangle_H-\langle Du,Dv\rangle_H.}
 \tag{10}
\]

In particular the requested Gram error is explicit:

\[
 \boxed{E_a(u,v)=q_a(u,v)-\langle Tu,Tv\rangle_H
 =-\int\frac{(\kappa+\omega+c)^2}{g+s}
 \overline{\widehat u}\widehat v.}                  \tag{11}
\]

Since n>=kappa>0, D is injective and \(E_a[u]<0\) for every nonzero u.
Thus this uncorrected T is definitively not an exact Weil-Gram readout.
Negative representation error says nothing about the sign of q[u]. The
two-output realization is a signed realization; its ambient positive norm
\(\|Tu\|^2+\|Du\|^2\) must not be confused with q.

## 3. Uniform source control and the actual form completion

Pointwise, \(n^2/A\le s^2/(g+s)\le s<12\), so

\[
 \|Du\|^2\le s\|u\|_2^2<12\|u\|_2^2.           \tag{12}
\]

Every source supported in [-1,1] obeys a physical Gamma floor independent
of any Mellin constraint. For r>2 its translated support is disjoint, hence

\[
 \Gamma[u]\ge 2\|u\|_2^2\int_2^\infty k(r)dr
 >4e^{-1}\|u\|_2^2>\tfrac43\|u\|_2^2.           \tag{13}
\]

The strict inequality uses k(r)>exp(-r/2) and e<3. On normalized Fourier
mass, Jensen applies to the convex function \(f_s(x)=x^2/(x+s)\), since
\(f_s''(x)=2s^2/(x+s)^3>0\). From m>=g and s<12,

\[
 \boxed{\|Tu\|^2\ge\int\frac{g^2}{g+s}|\widehat u|^2
 >\frac{(4/3)^2}{4/3+12}\|u\|_2^2
 =\frac2{15}\|u\|_2^2.}                           \tag{14}
\]

The non-strict version extends to completions. Let
\(F_a=\overline{W_a}^{q_a+17\|\cdot\|_2^2}\), the inherited C0 form
space, with the endpoint 1 included by the same semibound. Equations
(10), (12), and (14) give

\[
 \|Tu\|^2\le q_a[u]+17\|u\|_2^2
 \le\frac{257}{2}\|Tu\|^2.                        \tag{15}
\]

Thus T extends to a bounded isomorphism from F_a onto the closed space

\[
 \boxed{H_a=\overline{T(W_a)}^{H}.}                 \tag{16}
\]

This is an explicit positive candidate target. It is not defined by using q
as a positive inner product. The C0 norm only identifies its correct source
completion after the spectral construction. Each H_a is infinite-dimensional:
W_a contains arbitrarily many independent compact Mellin-annihilated bumps,
and (14) makes T injective. Let

\[
 S_a:H_a\longrightarrow L^2([-a,a]),\qquad S_a(Tu)=u.
\]

Then \(\|S_a\|\le\sqrt{15/2}\). All formulas extend by density to F_a.
There is no separate trace condition or replacement of the physical source
domain hidden in (16).

## 4. Exact candidate transitions and defect naturality

For a<=b<=1, the fixed spectral functions in (6) give
\(T(J_{a,b}u)=Tu\), not merely equality of source forms. Hence H_a is a
closed subspace of H_b. Define I_{a,b} to be this literal Hilbert-space
inclusion. Then

\[
 \boxed{I_{b,c}I_{a,b}=I_{a,c},\qquad
 T_bJ_{a,b}=I_{a,b}T_a.}                            \tag{17}
\]

Here T_a is (8) with its codomain H_a. This proves the requested transition
identity for a constructed, genuinely nonlocal Prime/Gamma readout. Parity
commutes with all these maps because all spectral multipliers are even.

It is essential that Q is fixed by horizon 1. Replacing Q by the active set
at each a would change T on old sources: vanishing of an inactive channel's
quadratic correlation does not imply vanishing of its spectral multiplier
or of the new cross terms. This package makes no such replacement.

Define the defect transfer on the target by

\[
 R_a:H_a\to H,\qquad R_a(T_au)=Du=D S_a(T_au).
 \tag{18}
\]

It is bounded, with \(\|R_a\|^2\le90\), and satisfies

\[
 \boxed{R_b I_{a,b}=R_a.}                           \tag{19}
\]

The inverse and defect maps also have explicit formulas, without an abstract
inversion of q:

\[
 S_a h=\mathcal F^{-1}\left(\frac{\sqrt A}{m}h\right),
 \qquad R_a h=\frac{n}{m}h\quad\hbox{a.e. on }\mathbb R.
\]

The single point xi=0 is immaterial in L2. These multipliers are not asserted
bounded on all of H; their domains here are the constructed closed subspaces
H_a, where (12)-(15) provide the required control. Nor is R_a(H_a) assumed
contained in H_a. Its codomain is the common H.

For \(C_a=R_a^*R_a\), the correct resulting law is compression:

\[
 \boxed{I_{a,b}^*C_b I_{a,b}=C_a.}                  \tag{20}
\]

We do not assert the stronger and generally invalid equation
\(C_bI_{a,b}=I_{a,b}C_a\). Likewise local square roots of I-C_a cannot be
assumed to intertwine merely from (20).

## 5. Compactness, infinite rank, and a constructive approximation

The multiplier \(d(\xi)=n(\xi)/\sqrt{g(\xi)+s}\) is bounded and tends
to zero at both frequency infinities by (4). The operator D restricted to
L2([-a,a]) is compact. Indeed, its cutoff to |xi|<=M has kernel

\[
 K_M(\xi,x)=\frac{1_{[-M,M]}(\xi)d(\xi)e^{-ix\xi}}{\sqrt{2\pi}}
 \quad (|x|\le a),
\]

which is square-integrable on that rectangle. The omitted operator norm is
at most \(s/\sqrt{g(M)+s}\), tending to zero. Finite-rank approximations
can also be made explicit: replace the exponential by its Taylor polynomial
of degree N. Call this map D_{M,N,a}; it has rank at most N+1. Its coordinates
are ordinary source moments used as features, **not additional constraints**.

For real t, integral Taylor remainder gives
\(|e^{-it}-\sum_{j=0}^N(-it)^j/j!|\le |t|^{N+1}/(N+1)!\).
The frequency supports of the tail and cutoff errors are disjoint, so

\[
 \|D-D_{M,N,a}\|^2\le
 \frac{s^2}{g(M)+s}
 +\frac{2aMs}{\pi}\frac{(aM)^{2N+2}}{((N+1)!)^2}.
 \tag{21}
\]

Let R_{M,N,a}=D_{M,N,a}S_a. Using a<=1, s<12, s>10, pi>3,

\[
 \boxed{\|R_a-R_{M,N,a}\|^2\le\frac{15}{2}
 \left[\frac{144}{g(M)+10}
 +8M\frac{M^{2N+2}}{((N+1)!)^2}\right].}           \tag{22}
\]

A finite partial sum in (2) can replace g(M) in the denominator to give
an entirely rational bound for rational M. First increase M, using (4),
then N. This proves norm-convergent finite-rank approximation uniformly
over a<=1. The displayed constants are conservative and do **not** certify
\(\|R_1\|\le1\); a bound above one is UNDECIDED.

It follows that R_a and C_a are compact. They have infinite rank: D is
injective on the infinite-dimensional source space, and S_a is injective.
Thus the exact defect cannot be removed as a finite-rank form adjustment
on H_a. This assertion is about the present explicit defect; it is not a
new universal exclusion of all nonlocal readouts.

## 6. The candidate is genuinely long-range

The spectral target is already global. A physical nonlocality statement is
also provable: even the inverse Fourier output of T on suitable smooth
compact sources is not compactly supported. Therefore (8) is not just a
finite-propagation operator written in spectral coordinates.

The series (2) is holomorphic on |Im z|<1/2. On z=iy, 0<=y<1/2,

\[
 g(iy)=-\sum_{j\ge0}\frac{2y^2}{\lambda_j(\lambda_j^2-y^2)}
\]

decreases strictly from zero to minus infinity. Consequently A(iy)=g(iy)+s
has a unique simple zero y=beta in (0,1/2). The exact ledger locates it:

\[
 \boxed{2/5<\beta<9/20.}                            \tag{23}
\]

At y=2/5, the absolute value of the first term is 64/9, while the remaining
sum is at most
\((3y^2/8)/(1-4y^2/25)\); their sum is <8<s. At y=9/20 the first term
alone has absolute value 324/19>12>s. These are rational inequalities,
not a sampled numerical root.

At i beta, every cos becomes cosh, so

\[
 n(i\beta)=\kappa+\omega+\sum_qw_q\cosh(\beta\ell_q)>0,
 \qquad m(i\beta)=-n(i\beta)\ne0.                 \tag{24}
\]

Choose a nonnegative, nonzero, even smooth bump psi supported strictly in
(-a,a), and put \(u=(D_x^2-1/4)\psi\). Then u lies in W_a by integration
by parts, and

\[
 \widehat u(i\beta)
 =(\beta^2-1/4)(2\pi)^{-1/2}\int\psi(x)e^{\beta x}dx\ne0.
\]

If the inverse Fourier transform of Tu had compact support, its Fourier
transform F(z) would be entire, directly by integration over compact support.
For real xi, (8) gives
\(A(\xi)F(\xi)^2=m(\xi)^2\widehat u(\xi)^2\).
Both sides are holomorphic in the strip, so the equality extends there.
At i beta its left side vanishes and its right side does not: contradiction.
The same argument with n proves noncompact support for the D output.
Using u' instead gives an odd smooth two-Mellin source and the same
contradiction, since beta>0. No third Mellin condition has been imposed.

## 7. Common channel observations on the positive target

Write U_q=w_q(tau_{ell_q}+tau_{-ell_q}) on physical L2. Its induced
observation on H_a is the bounded self-adjoint operator

\[
 P_{q,a}^{H}=S_a^*U_q S_a,\qquad M_a=S_a^*S_a.
 \tag{25}
\]

These need not be positive; the channel sign result in f77116a is respected.
The Gamma observation is the bounded positive form
\(G_a^{H}(T_au,T_av)=\Gamma(u,v)\). To see boundedness without assuming
q positive, use (10), (12), (14), and \(\|\sum U_q\|\le2\omega\).
In fact \(\Gamma[u]\le\|Tu\|^2+s\|u\|_2^2\le91\|Tu\|^2\).
Thus on the same H_a,

\[
 \boxed{G_a^{H}-\kappa M_a-\sum_q P_{q,a}^{H}=I_{H_a}-C_a.}
 \tag{26}
\]

All these observations are natural under compression by I_{a,b}. They are
observations of one source-linked positive spectral target, not independent
positive Gram components for the signed terms.

For completeness S_a is compact into physical L2. A bounded set in H_a has
uniformly bounded Gamma energy by the preceding inequality. Equation (4)
makes its L2 Fourier tail uniformly small. The cutoff Fourier restriction
from the fixed compact source interval is Hilbert-Schmidt. Approximation by
cutoff operators proves compactness. Hence M_a and the finitely many
P_{q,a}^{H} are compact; (26) is consistent with G_a^{H} being I plus a
compact operator. None of these compactness statements is a finite-rank
truncation of the exact Gamma or Prime data.

## 8. The precise remaining positivity obligation

The exact normalized form on H_a is

\[
 q_a(S_ah,S_ak)=\langle h,(I-C_a)k\rangle_H.
 \tag{27}
\]

Therefore

\[
 \boxed{q_a\ge0\ \Longleftrightarrow\ \|R_a\|\le1.} \tag{28}
\]

This is a reduction, not a proof of the inequality. C_a is compact positive,
so any eigenvalues >=1 form a finite-dimensional obstruction space. The
negative index equals the number of its eigenvalues >1, counted with
multiplicity, and its form nullspace is the eigenspace at 1. Compactness
does not decide whether any such eigenvalues exist. No numerical eigenvalue
is used as a certificate here.

On a window where an inherited physical gap delta>0 is already certified,
the construction transports that existing information into

\[
 q_a[u]\ge\delta\|u\|_2^2
 \quad\Longrightarrow\quad
 \|R_a\|^2\le\frac{s}{s+\delta}<\frac{12}{12+\delta}<1.
 \tag{29}
\]

Indeed \(\|Du\|^2\le s\|u\|_2^2\) and (10) give
\(\|Tu\|^2\ge(1+\delta/s)\|Du\|^2\). This is only a translation of
the existing gap, not a wider positive window or a replay of its old matrix
certificate. In particular the prior band B+10^-10 and the independent
uniform High-Tail result remain exactly as before.

## 9. Direct limit and why a local square-root repair is not automatic

The Hilbert direct limit of the constructed targets is concretely
\(\overline{\bigcup_{a<1}H_a}\subset H_1\). In fact it equals H_1:
smooth compact approximations to a source in H1_0((-1,1)) converge in H1;
correct their two small Mellin errors with two fixed interior smooth
functions having invertible moment matrix. Such functions exist by placing
bumps at distinct centers, since the ratios of their two moments differ.
The corrections tend to zero in H1, retain compact support inside (-1,1),
and impose exactly the original two conditions. The bound following (3)
and (10)-(12) makes H1 convergence imply T convergence. Density then
extends the claim to F_1.

Equations (17) and (19) give a concrete limit readout and one compact
defect transfer R_1 on this fixed-horizon limit. This is a positive candidate
carrier with a signed form (27), **not** a positive Weil-Gram direct limit.

If the still-open bound \(\|R_1\|\le1\) were proved independently, one
could apply the single global positive operator
\((I-C_1)^{1/2}\) to all embedded outputs T_a. The resulting maps into H_1
would have exact Gram identity and intertwine on this band. Using one
global operator matters: square roots of the compressed C_a do not in
general commute with the inclusions. This conditional observation does
not supply the missing contraction estimate and is not an unconditional
construction of the required positive readout.

## 10. Verification and scope

The standalone checker reconstructs exact rational bounds for logs,
square roots, pi and Euler's constant bounds, the coefficients in (5),
the complete formal factorization, coercivity and norm constants, the
Gamma tail estimates at explicit rational points, the bracket (23), and
the factorial finite-rank approximation bound. Input provenance is bound
to five immutable files by byte length, SHA256, and Git blob id.

More explicitly, for rational x>=1 it uses z=(x-1)/(x+1) and
\(\log x=2\sum_{j\ge0}z^{2j+1}/(2j+1)\), bounding the remainder
after N terms by \(2z^{2N+1}/((2N+1)(1-z^2))\). Square roots are enclosed
by adjacent rational grid points using integer square root. Alternating
arctangent remainders and the exact tangent identity for
\(\pi=16\arctan(1/5)-4\arctan(1/239)\) enclose pi. Integral comparison
gives \(H_8-\log9<\gamma<H_8-\log8\). The exponential Taylor remainder
is bounded by a geometric majorant on successive term ratios. All displayed
decimal endpoints are directed rational decimals, not binary floats.

The ledger contains **53 exact checks**. Its rank-at-most-129 example
(M=16,N=128) yields only a conservative squared approximation error below
70 (about 66.239 from above); it does not certify contraction. This example
checks the quantitative approximation machinery without promoting a poor
upper bound to a sign decision.

Plancherel, the exact infinite-series identities, compactness, the analytic
nonlocality proof, and the transition laws are proved above. Finite arithmetic
checks do not replace those arguments or an independent analytic audit.
No floating-point sign decisions, quadrature, numerical eigenvalues, or
prior numerical matrix-chain replay are used as a new certificate.

What this adds is a fully specified candidate H_a,T_a,I_{a,b}, a common
channel observation formula, and the exact compact residual gate R_a.
The uncorrected candidate is known to have strictly negative Gram error;
the sign of the full Weil form on new windows remains open. C1a/b are
closed **for this declared candidate interface only**. Full C1, the
Moving-191D Low/Profile gate, non-summable transport, historical Strong
Terminal, unrestricted-horizon compatibility, Objekt X, and RH remain open.
