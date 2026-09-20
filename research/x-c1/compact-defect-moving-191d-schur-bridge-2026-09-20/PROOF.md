# Compact-defect contraction: a uniform 191D Schur bridge

2026-09-20. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `5557d94d048dc05e7c3b4534a5a2d1711bdc71dc`.

This package connects the existing moving physical High-Tail theorem to the
specific coupled spectral defect model. It proves a uniformly contractive
complete high defect block, bounds the critical singular multiplicity by
191 per parity, and identifies the remaining defect Schur matrix with the
physical moving-191D Schur form by an exact congruence. It also proves
continuity and monotonicity of the moving defect singular values on the
fixed horizon band, including Prime-channel activation endpoints.

It does **not** certify the remaining finite matrix or full contraction at
a=1. No larger positive window, negative full Weil source, moving profile
renewal, unrestricted-horizon geometry, positive C1 closure, or Objekt X is
claimed. A finite critical reduction is not its positive solution.

## 1. Fixed candidate and inherited hypotheses

Let B=log(5)/2 and B<=a<=1. All sources retain the original two physical
Mellin conditions E_+u=E_-u=0. Write F_a for the closed form completion of
the actual zero-extended H1_0((-a,a)) sources in q_a+17||.||_2^2.

Use exactly the candidate of 5557d94:

\[
 Tu={g+\omega-c\over\sqrt{g+s}}\widehat u,\qquad
 Du={\kappa+\omega+c\over\sqrt{g+s}}\widehat u,
 \quad s=\kappa+2\omega<23/2.
 \tag{1}
\]

Here g is the full Gamma symbol, and omega,c use the fixed horizon channels
2,3,4,5,7 with weights Lambda(q)/sqrt(q). The letter D in (1) always means
the bounded defect output, not a physical high-block operator. The positive
target H_a=closure(T W_a) is isomorphic to F_a, and

\[
 q_a(u,v)=\langle Tu,Tv\rangle-\langle Du,Dv\rangle,
 \quad\|Du\|^2\le s\|u\|_2^2,\quad
 \|Tu\|^2\ge{2\over15}\|u\|_2^2.                 \tag{2}
\]

The compact injective transfer R_a(Tu)=Du has norm squared <=90. Set
C_a=R_a^*R_a. It is compact positive on H_a. Reflection splits all these
objects into even and odd parts, denoted p=0,1. All Hilbert pairings below
are conjugate-linear in their first argument.

The inherited moving-tail theorem, with no global positivity hypothesis,
supplies a complete physical high space V_{a,p} with

\[
 q_a[u]\ge {1\over41}\|u\|_2^2\quad(u\in V_{a,p}),
 \qquad\operatorname{codim}_{F_a^p}V_{a,p}=191.    \tag{3}
\]

The construction and domain interpretation of this space are specified next.
The original strict bound implies the displayed weak bound, which is enough.

## 2. Closed physical domains and the exact low-coordinate count

Let U_a u(x)=sqrt(2a)u(ax), mapping physical L2(dx) to the reference space
L2((-1,1),dx/2). Put e_n=sqrt(2n+1)P_n. In parity p, let

\[
 I_0=\{2,4,\ldots,382\},\qquad I_1=\{3,5,\ldots,383\},
 \qquad |I_p|=191.                                  \tag{4}
\]

The raw high indices start at 384, respectively 385. Set
m_{0,a}(x)=cosh(ax/2), m_{1,a}(x)=sinh(ax/2), and use the complex-linear
moment functional

\[
 \ell_{p,a}(y)=\int_{-1}^1 y(x)m_{p,a}(x)\,dx/2,
 \qquad M_{p,a}y=y-\frac{\ell_{p,a}(y)}{\ell_{p,a}(e_p)}e_p.
 \tag{5}
\]

Both denominators are nonzero on this band. The high space V_{a,p} is
U_a^{-1}M_{p,a} applied to the raw high reference form space. Equivalently,
it is the kernel in F_a^p of the 191 continuous coordinate functionals

\[
 u\longmapsto\langle e_n,U_a u\rangle\quad(n\in I_p). \tag{6}
\]

Indeed, the Mellin correction only changes the e_p coefficient, which is
uniquely determined by the moment condition. The reference low representatives

\[
 z_{n,a}=U_a^{-1}M_{p,a}e_n\quad(n\in I_p)            \tag{7}
\]

have identity low-coordinate matrix. Thus (6) is surjective and its kernel
has exactly codimension 191. Finite-rank removal of (7) preserves the form
domain. This is not an extra Mellin constraint: it is a complete coordinate
decomposition with all 191 low coordinates retained.

There is a domain point that must not be skipped. Individual polynomials
(7), after zero extension, need not lie in H1_0 because their endpoint
traces need not vanish. They are used in the **closed form space**, not
declared actual H1 sources. The following density fact justifies this and
will also control moving endpoints.

Let G be the full-line Gamma form domain, with norm
\(\int(1+g(\xi))|\widehat u(\xi)|^2d\xi\). Then

\[
 F_a=\{u\in G:\operatorname{supp}u\subset[-a,a],\ E_+u=E_-u=0\}.
 \tag{8}
\]

To prove (8), first q+17||.||^2 and the Gamma norm are equivalent, since the
non-Gamma remainder has operator norm at most s<12. The right side is
closed: support is closed in L2, and the two moments are continuous on the
fixed compact interval. For density, shrink a source by unitary dilation
u_r(x)=r^{-1/2}u(x/r), r<1. The Gamma series gives
g(t xi)<=max(1,t^2)g(xi), so dilations are uniformly bounded near r=1 on G
and converge strongly there, by density of functions with smooth compact
Fourier support. The two moments of u_r approach zero. Remove their errors
using two fixed smooth interior functions with invertible moment matrix;
the correction tends to zero in G. Finally convolve with a sufficiently
narrow smooth compact nonnegative even mollifier. This stays inside (-a,a),
converges in G by Fourier dominated convergence, and preserves each zero
moment because E_+(u*rho)=E_+(u)E_+(rho), and similarly for E_-.
The result is an actual smooth compact source with exactly the two moments.
In a fixed parity only its one nonautomatic moment needs correction.

The representatives (7) have finite Gamma energy. For a compact
piecewise-smooth function their translation increments obey
||tau_r u-u||_2^2<=C min(r,1); since k(r)=O(1/r) near zero and is integrable
at infinity, the Gamma integral is finite. Thus (8) applies to them.
It also applies to the moment carrier. The inherited high-tail theorem
therefore acts on precisely the closed high subspace used here, with no
hidden trace restriction or enlargement of the physical form domain.

## 3. Uniform contraction of the complete high defect block

Write H=H_a^p for this section and define

\[
 \mathcal H=T(V_{a,p})\subset H,\qquad
 \mathcal L=\mathcal H^\perp\cap H.                 \tag{9}
\]

T is an isomorphism of the completed spaces, so H_high is closed and
dim L=191. Let P be the orthogonal projection onto H_high and Q=I-P.
For u in V_{a,p}, (2)-(3) give

\[
 \|Du\|^2\le41s q_a[u],\qquad
 \|Tu\|^2=q_a[u]+\|Du\|^2\le(1+41s)q_a[u].
\]

Since s<23/2, define the uniform rational constants

\[
 \boxed{\delta={2\over945},\qquad\theta={943\over945}=1-\delta.}
 \tag{10}
\]

It follows for the **entire** high subspace that

\[
 \boxed{q_a[T^{-1}h]\ge\delta\|h\|^2,\qquad
 \|R_a h\|^2\le\theta\|h\|^2\quad(h\in\mathcal H).} \tag{11}
\]

This is a new defect-tail contraction bound, obtained from the independent
physical high-tail estimate. It does not assume q nonnegative on the whole
window or import the tiny known All-Source gap.

The explicitly defined rank-191 approximation is
R_a^low=R_a Q. Its complete operator remainder obeys

\[
 \boxed{\|R_a-R_a^{low}\|^2\le\theta.}             \tag{12}
\]

For decreasing singular values (counted with multiplicity), the min-max
principle or rank-191 approximation bound gives

\[
 \boxed{s_{192}(R_a^p)^2\le{943\over945},\qquad
 s_{192}(R_a^p)<{999\over1000}.}                    \tag{13}
\]

Across both parities the same bound holds for s_383(R_a). The elementary
last comparison is theta<(999/1000)^2. Thus at most 191 singular values in
each parity can reach one. This bounds the dimension of the critical space;
it does not assert that the chosen low vectors are singular vectors.

## 4. The exact 191-dimensional contraction gate

Choose any isometry U:C^191 -> L. In H=L direct-sum H_high, write

\[
 C_a=\begin{pmatrix}\alpha&\beta^*\\\beta&K\end{pmatrix},
 \quad\alpha=U^*C_aU,\quad\beta=PC_aU,\quad
 K=PC_a|_{\mathcal H}.                              \tag{14}
\]

These are bounded blocks of the actual compact operator, not finite
truncations of its kernel. In particular

\[
 0\le K\le\theta I,\quad 0\le\alpha\le90I,\quad
 \beta^*\beta\le\theta\alpha\le90\theta I.       \tag{15}
\]

For the mixed inequality, write beta=R_high^* R_low and use
||R_high||^2<=theta. All Low/High couplings are retained.

The normalized form is I-C_a. For x in C^191 and y in H_high,

\[
 q_a[T^{-1}(Ux+y)]
 =\langle x,(I-\alpha)x\rangle-2\operatorname{Re}\langle y,\beta x\rangle
 +\langle y,(I-K)y\rangle.
\]

Completing the square yields the exact finite matrix

\[
 \boxed{S_a^p=I-\alpha-\beta^*(I-K)^{-1}\beta}       \tag{16}
\]

and the equivalence

\[
 \boxed{\|R_a^p\|\le1\ \Longleftrightarrow\ S_a^p\succeq0.}
 \tag{17}
\]

The high inverse exists with norm <=1/delta=945/2. No endpoint positivity
assumption is hidden in this inversion. Strict finite positivity is likewise
equivalent to strict relative contraction, using the bounded triangular
completion map. The negative index and nullity of I-C_a equal those of S_a^p.
No sign of S_a^p at new endpoints is certified in this package.

For any candidate eigenpair C_a(Ux+y)=lambda(Ux+y) with lambda>=1,

\[
 y=(\lambda I-K)^{-1}\beta x,\qquad x\ne0.         \tag{18}
\]

Thus the genuinely critical eigenvectors are graph lifts over the low
coordinates, with a lambda-dependent high response. The low projection is
injective on the whole spectral subspace for eigenvalues >=1: a vector
there with zero low component would have both Rayleigh quotient >=1 and
<=theta. This also proves the critical multiplicity bound without sampling.

## 5. Exact congruence with the physical moving-191D Schur form

This is the precise version of the proposed connection to transport.
Let Z:C^191 -> F_a^p have columns (7), and let F=T Z. Set

\[
 L=QF,\qquad G=L^*L\succ0,\qquad U=L G^{-1/2}.     \tag{19}
\]

L is injective because the low source representatives are independent
modulo V_{a,p}; hence G is a positive finite Gram matrix. Its inverse square
root only normalizes the already positive T geometry, not a presumed
positive Weil form. Use this U in (14).

Define the physical q-harmonic correction h(x) in V_{a,p} by

\[
 q_a(h(x),v)=q_a(Zx,v)\quad(v\in V_{a,p}).          \tag{20}
\]

Equation (11) gives coercivity in the correct complete T norm, so this
bounded Riesz problem has a unique solution. The physical Schur matrix is

\[
 S_{phys}(x,z)=q_a(Zx-h(x),Zz-h(z)).                \tag{21}
\]

Since F x=U G^{1/2}x+P F x, variation by a physical high vector is exactly
variation of its high T image. Completing the square in (16) therefore gives

\[
 \boxed{S_{phys}=G^{1/2} S_a^p G^{1/2}.}            \tag{22}
\]

In particular the physical moving-191D Schur form and the defect critical
matrix have identical inertia. This closes a coordinate-level equivalence,
not a conjectured equality of basis vectors or leading singular modes.

The comparison applies to the moving core low/high decomposition at a fixed
a. It does not identify or certify the additional shell/profile couplings
required to transport a to b. It also does not identify the earlier 31D
finite-band hard/soft charts with the present 191D spaces.

## 6. Full infinite high response with a rational remainder

Because K is positive and ||K||<=theta<1,

\[
 (I-K)^{-1}=\sum_{j=0}^N K^j+K^{N+1}(I-K)^{-1}.
\]

Put

\[
 S_N=I-\alpha-\sum_{j=0}^N\beta^*K^j\beta.
\]

All omitted terms are positive in the subtracted response, and

\[
 \boxed{S_N-\epsilon_N I\preceq S_a^p\preceq S_N,
 \quad\epsilon_N={90\theta^{N+2}\over\delta}
 =42525\left({943\over945}\right)^{N+2}.}          \tag{23}
\]

The exact ledger verifies theta^1024<1/8. Thus, for N=1024k-2,
epsilon_N<42525/8^k. Two conservative rational examples are

\[
 N=20478:\quad\epsilon_N<4\cdot10^{-14},\qquad
 N=22526:\quad\epsilon_N<6\cdot10^{-16}.           \tag{24}
\]

No such large operator-power computation is claimed to have been performed.
(23)-(24) certify the remainder law only. The finite entries alpha and
beta^*K^j beta still require rigorous enclosures before a sign verdict.
They are not to be replaced by sampled high modes.

More generally, for any rational Lambda>theta, define

\[
 F_N(\Lambda)=\Lambda I-\alpha
 -\sum_{j=0}^N\Lambda^{-j-1}\beta^*K^j\beta.
\]

Then

\[
 F_N(\Lambda)-e_N(\Lambda)I\preceq
 \Lambda I-\alpha-\beta^*(\Lambda I-K)^{-1}\beta
 \preceq F_N(\Lambda),
\]
\[
 e_N(\Lambda)=\frac{90\theta}{\Lambda-\theta}
 \left(\frac\theta\Lambda\right)^{N+1}.            \tag{25}
\]

If a rational Hermitian approximation A_N has certified operator error
||A_N-F_N(Lambda)||<=eta, a rigorous positive-semidefinite certificate for

\[
 A_N-(\eta+e_N(\Lambda))I\succeq0                 \tag{26}
\]

proves \(\|R_a^p\|^2\le\Lambda\). For 191-by-191 entrywise error at
most rho, eta=191 rho is sufficient by the row/column norm bound. Exact
rational LDL or another rigorous PSD certificate can check (26). Lambda=1
is the intended contraction gate. Without certified entries and a passing
finite gate the result is **UNDECIDED**, even though the high response and
its infinite remainder are now uniformly controlled.

## 7. Moving endpoints and entry of Prime channels

All H_a are nested closed subspaces of the fixed H_1, and R_a=R_1|H_a.
Let P_a denote the orthogonal projection in H_1 onto H_a; this P_a is distinct
from the low/high projection P in (9). Equation (8) proves

\[
 H_a=\overline{\bigcup_{b<a}H_b}\quad(a>B),\qquad
 H_a=\bigcap_{b>a}H_b\quad(a<1).                    \tag{27}
\]

For the first identity use the compact smooth approximations with their
two exact moments from (8). For the second, the inverse T on H_1 maps an
element of every H_b to a finite-Gamma source supported in the intersection
[-a,a]; (8) then puts it in F_a. The usual monotone-projection argument
(or direct approximation by these subspaces) gives strong continuity of
P_a from both sides, with one-sided continuity at B and 1.

Compactness of R_1 upgrades this to

\[
 \|R_1(P_b-P_a)\|\longrightarrow0\quad(b\to a).
 \tag{28}
\]

To see this without assuming norm continuity of P_a, approximate R_1 by
a finite-rank operator. For each finite-rank term, strong convergence of
the self-adjoint projections controls its adjoint on finitely many vectors;
the remaining norm error is uniformly small. The same proof applies within
each parity. Therefore each ordered defect singular value is continuous.
It is also nondecreasing with a: the min-max formula for C_1 compressed to
the nested spaces H_a has an enlarging family of trial subspaces. Thus

\[
 \boxed{a\mapsto s_j(R_a^p)^2\text{ is continuous and nondecreasing}.}
 \tag{29}
\]

This includes a=log(7)/2. The readout always uses the horizon set Q; a newly
active physical Prime pairing turns on through support overlap. It does
not create a new spectral output channel or invalidate theta. The original
physical high-tail theorem already pays the complete five-channel budget.
The statement gives no explicit endpoint modulus or positive step size;
continuity alone cannot close a non-summable transport law.

The eigenvalues of a moving coordinate matrix S_a^p need not themselves be
monotone. The monotonicity assertion is for the intrinsic singular values
on nested H_a, not for arbitrary low-coordinate charts.

## 8. What has been closed and what remains

Closed independently of full-window positivity:

* uniform complete high defect contraction theta=943/945;
* rank-191 approximation and critical multiplicity bound in each parity;
* exact finite Schur criterion retaining all Low/High couplings;
* exact congruence to the existing physical moving-191D core Schur form;
* a rational bound for the entire infinite high-response remainder;
* a finite-matrix certification rule for an upper singular-value enclosure;
* continuity and monotonicity on the fixed endpoint band, including activation.

Still open:

* the rigorously enclosed entries and positive sign of the finite Schur
  matrices on endpoints beyond the already certified band;
* consequently ||R_1||<=1 and a new positive Weil-Gram realization;
* moving Low/Profile reserve renewal and a non-summable continuation law;
* compatibility of candidates at arbitrarily larger horizons, a complete
  global Weil test-class identification, Strong Terminal, Objekt X, and RH.

The inherited B+10^-10 result is not enlarged. The fixed near-null source
is untouched. No third Mellin condition, A1 import, numerical eigenvalue
sign test, or quadrature sign certificate is used.

The new ledger passes 67 checks, including 24 provenance bindings and three
inherited replay checks. The checker binds both full input packages plus their immutable dependencies
(24 files), reproduces the 53-check candidate package and both documented
high-tail modes (25-check frozen math-only replay; 26-check full provenance
run), and checks the new rational bounds and Schur identities. The high-tail
mode distinction is preserved rather than silently rewriting its old log.
Analytic domain, compactness, min-max and congruence arguments are proved
above; finite arithmetic reproduction is not independent external review.
