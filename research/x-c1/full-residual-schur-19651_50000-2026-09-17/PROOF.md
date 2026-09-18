# FULL-RESIDUAL-SCHUR at a = 19651/50000

Date: 2026-09-17. Status: **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Mathematical anchor: corrected Node-Schur head
`9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb`, PR #137.

## 1. Result and precise meaning of the full block

Put \(a=19651/50000=0.39302\), \(L=2a\), and
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad E_\pm u=\int_{-a}^a u(t)e^{\pm t/2}\,dt.
\]
The certificate proves
\[
\boxed{Q_W[u]>\frac1{150}\|u\|_2^2\quad(0\ne u\in\mathcal W_a).}
\tag{1}
\]
In particular, this rational point exceeds the upper endpoint 0.3930110 of
the corrected local Node-Schur crossing bracket. No global assertion about
the Node-only crossing is used here.

The retained operator on the even high-mode space is exactly
\[
R=\mu P_J+R_\Gamma+R_2,\qquad
\theta=\tfrac34,\quad \mu=\theta m.
\tag{2}
\]
Both difference operators in (2) are the **entire** nonconstant Gamma
residual and Prime-2 difference operator. Neither is discarded, replaced
by a finite matrix, or omitted from the actual full off-diagonal coupling.
The Node term is the certified outer-slab reserve after the stated
constant-mode split. The remaining nonnegative variable Node potential
is not needed; no claim of exhausting that larger potential is made.

We prove a lower bound for the actual Schur complement of (2) by form
comparison, then bound the actual full Schur shear. These two steps must
not be confused with identifying a comparison pivot with the exact pivot.
No A1, third Mellin condition, quadrature, sampled eigenvalue, or imported
floating-point enclosure is used.

## 2. Exact starting identity and domains

Use the connected-edge identity from the anchor and its connected parents:
\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
g(t)=h(t)-\frac1{2t},\quad H(s)=\int_s^\infty h(t)\,dt,
\]
\[
\ell=\log2,\quad w=\ell/\sqrt2,\quad
\kappa=\log(8\pi)+\gamma+\pi/2.
\]
The checker verifies \(a<\ell<L<\log3\). Thus Prime 2 is the only
active prime-power shift, and its two endpoint bands are disjoint.
On the stated NULLPOL class,
\[
Q_W[u]=\int_{x<y\in I_a}h(y-x)|u(y)-u(x)|^2\,dx\,dy
+w\int_{-a}^{a-\ell}|u(x+\ell)-u(x)|^2\,dx
+\int_{I_a}\rho(x)|u(x)|^2\,dx,
\tag{3}
\]
where \(I_a=(-a,a)\),
\[
\rho(x)=H(a+x)+H(a-x)-\kappa
-w\bigl(1_{I_a}(x-\ell)+1_{I_a}(x+\ell)\bigr).
\]

The normalized basis is \(e_n(x)=\sqrt{(2n+1)/L}P_n(x/a)\).
The singular difference kernel \(1/(2t)\) has the Legendre eigenvalues
\(\mathsf H_n=\sum_{j=1}^n1/j\), with \(\mathsf H_0=0\).
Equivalently, its operator acts through
\(\frac12\int_{-1}^1(P_n(z)-P_n(v))/|z-v|\,dv=\mathsf H_nP_n(z)\).
The constant kernel \(c=g(L)\) contributes \(Lc\) to every nonconstant
mode and zero to \(e_0\). These are the same normalization conventions
as in the connected and corrected Node-Schur packages.

All bounded residual operators below act on \(L^2(I_a)\). The diagonal
operator with eigenvalues growing like \(\mathsf H_n\) is treated as a
closed form on \(\{u:\sum_n(1+\mathsf H_n)|u_n|^2<\infty\}\).
The source class is contained in this form domain. The auxiliary
Legendre modes and constant subtraction need not themselves belong to
\(H^1_0\); they do belong to this larger form domain. Identities for the
diagonal part extend from polynomials by form closure. The nonnegative
remaining Node potential is retained on its natural form domain and
then discarded only in a lower bound.

## 3. Node reserve and constant-mode cost

The function \(H(a+x)+H(a-x)\) is even and increasing for \(x>0\),
since \(h\) decreases. The two candidate minima of \(\rho\) are its
center value and the inner edges of its active endpoint bands. Set
\[
C=\kappa+w-H(L-\ell)-H(\ell).
\]
The checker proves
\[
2H(a)-H(L-\ell)-H(\ell)+w>0,
\]
so \(V=\rho+C\ge0\) throughout the interval. For
\[
J=\{x\in I_a:|x|\ge\ell/2\},\qquad
m=H(a+\ell/2)+H(a-\ell/2)-H(L-\ell)-H(\ell),
\]
one has \(V\ge m1_J\), and the checker proves \(m>3/10\).

Write the even part as \(u=u_0e_0+x\), \(x\perp e_0\). Applying
\[
|A+B|^2\ge\theta|A|^2-\frac{\theta}{1-\theta}|B|^2
\]
only to \(m\int_J|u|^2\), and using \(\|P_Je_0\|^2\le1\), gives
\[
q_{\rm even}[u]\ge F[x]-K|u_0|^2,
\qquad K=C+\frac{\theta}{1-\theta}m=C+3m.
\tag{4}
\]
Here \(F\) is the **full** block form with residual (2). Both difference
forms annihilate \(e_0\) exactly, including their mixed terms, so (4)
includes their full values on \(x\) with no additional moment penalty.

The scalar coefficients are
\[
\lambda_n=\mathsf H_n+Lg(L)-C\quad(n\ge1),\qquad
\lambda_2=1+Lh(L)-C,\qquad \delta=\lambda_2+7/12.
\tag{5}
\]
The checker proves \(\lambda_2<0\) and \(\delta>53/100\).

## 4. Entire Gamma and Prime-2 operators: diagonal and tail bounds

Set
\[
r(t)=g(t)-g(L),\qquad
R_\Gamma[u]=\int_{x<y\in I_a}r(y-x)|u(y)-u(x)|^2\,dx\,dy,
\]
\[
R_2[u]=w\int_{-a}^{a-\ell}|u(x+\ell)-u(x)|^2\,dx.
\tag{6}
\]
For completeness the local monotonicity needed here has an elementary
proof. If \(z=t/2\le1\),
\[
h(t)=\tfrac14(\operatorname{csch}z+\operatorname{sech}z),\quad
g'(t)=\tfrac18[z^{-2}-\operatorname{csch}z\operatorname{coth}z
-\operatorname{sech}z\tanh z].
\]
The positive Taylor series gives
\(\sinh z/z\le1+(10/57)z^2\), whence
\((\sinh z/z)^2\le1+(1240/3249)z^2<1+z^2/2\le\cosh z\).
Thus \(g'<0\) on \((0,2]\). Also \(g(0+)=1/4\). Consequently
\[
0\le r(t)\le r_{\max}:=1/4-g(L),\qquad
\|R_\Gamma\|\le M_\Gamma:=2Lr_{\max}.
\tag{7}
\]
Indeed each vertex degree is at most \(Lr_{\max}\); the difference-square
inequality gives (7) on **all** of \(L^2\).

For normalized \(e_2\), polynomial integration gives exactly
\[
J_2(t):=\int_{-a}^{a-t}|e_2(x+t)-e_2(x)|^2\,dx
=\frac{60t^2(L-t)^3}{L^5}.
\tag{8}
\]
In particular \(\int_0^{L/2}J_2(t)dt=21L/32\) and
\(\int_0^LJ_2(t)dt=L\). Therefore
\[
q_\Gamma:=R_\Gamma[e_2]\in
\left[\frac{21L}{32}(g(L/2)-g(L)),\ Lr_{\max}\right],
\quad q_2:=R_2[e_2]=wJ_2(\ell).
\tag{9}
\]
These are analytic integral bounds, not quadrature. The checker verifies
\(q_\Gamma>1/100\), \(q_2>3/100\), and \(M_\Gamma<27/500\).

Since the Prime-2 endpoint bands are disjoint, every vertex has at most
one Prime-2 neighbor. Integrating \(|u-v|^2\le2|u|^2+2|v|^2\) yields
\[
0\preceq R_2\preceq M_2 I,\qquad M_2=2w<1.
\tag{10}
\]
The norm bounds (7) and (10) control every high mode and the entire
infinite tail; there is no mode cutoff or omitted-series remainder.

## 5. Exact full block and a conservative comparison pivot

Let \(Y=\overline{\operatorname{span}}\{e_4,e_6,\ldots\}\),
\(x=\alpha e_2+y\), and
\(D_0e_{2k}=\lambda_{2k}e_{2k}\) for \(k\ge2\). The actual blocks are
\[
A=\lambda_2+\mu p+q_\Gamma+q_2,\quad
b=P_Y(\mu P_J+R_\Gamma+R_2)e_2,
\]
\[
D=D_0+P_Y(\mu P_J+R_\Gamma+R_2)P_Y\succeq\delta I,
\quad \sigma=A-\langle b,D^{-1}b\rangle.
\tag{11}
\]
Here \(p=\langle e_2,P_Je_2\rangle\). Bounded perturbation of the positive
diagonal form defines \(D\); its inverse is bounded and \(b\in Y\).
Thus (11) is an actual infinite-dimensional Schur complement.

With \(z_0=\ell/L\), exact Legendre integrals give
\[
p=1-\frac94z_0^5+\frac52z_0^3-\frac54z_0,
\quad |\langle e_0,P_Je_2\rangle|^2=\frac54(z_0-z_0^3)^2.
\]
Since \(P_Je_2\) is even, Parseval gives the exact entire-tail mass
\[
v:=\|P_YP_Je_2\|^2
=p-p^2-\frac54(z_0-z_0^3)^2.
\tag{12}
\]
Subtracting both orthogonal projections in (12) is justified; no
uncomputed tail coefficient is set to zero.

Now retain the sum \(T=R_\Gamma+R_2\) and take \(s=1/10\). The elementary
positive-form inequality, applied to the direct sum of the two edge maps,
is
\[
T[\alpha e_2+y]\ge s(q_\Gamma+q_2)|\alpha|^2
-\frac{s}{1-s}(M_\Gamma+M_2)\|y\|^2.
\tag{13}
\]
Define
\[
d=\delta-\frac{s}{1-s}(M_\Gamma+M_2)>\frac25.
\]
Then the full form in (11) dominates
\[
F_-[\alpha,y]=[\lambda_2+s(q_\Gamma+q_2)]|\alpha|^2
+d\|y\|^2+\mu\langle\alpha e_2+y,P_J(\alpha e_2+y)\rangle.
\]
Its tail is \(D_-=dI+\mu P_YP_JP_Y\succeq dI\). Hence
\[
\sigma_-\ge S:=\lambda_2+s(q_\Gamma+q_2)+\mu p-\frac{\mu^2v}{d}.
\tag{14}
\]
Taking the infimum over \(y\) with \(\alpha=1\) in the full form and
in its lower comparison proves
\[
\boxed{\sigma=\inf_yF[e_2+y]\ge\inf_yF_-[1,y]=\sigma_-\ge S>1/50.}
\tag{15}
\]
The full infimum is over the diagonal form domain. The comparison
infimum over all \(Y\) can only be smaller, so this domain difference
does not weaken (15). In particular we have not approximated the full
coupling \(b\) by the Node-only coupling of the comparison form.

## 6. Actual full shear and return to the source norm

The certificate produces a rational lower bound \(S_{\rm lo}>1/50\)
and an upper bound \(A_{\rm hi}\) from (9) and (11). Since \(D\ge\delta I\),
\[
\|D^{-1}b\|^2
\le\delta^{-1}\langle b,D^{-1}b\rangle
=\frac{A-\sigma}{\delta}
\le\frac{A_{\rm hi}-S_{\rm lo}}{\delta_{\rm lo}}<\frac14.
\tag{16}
\]
The last quotient is enclosed conservatively by the checker; it is
less than 0.161954579590. Both the actual Schur shear and its inverse
therefore have norm at most \(1+\|D^{-1}b\|<3/2\).

Completing the full square,
\[
F[x]=\sigma|\alpha|^2+
\|D^{1/2}(y+\alpha D^{-1}b)\|^2.
\]
Consequently
\[
F[x]\ge\eta\|x\|^2,\qquad
\eta=\frac{\min(S_{\rm lo},\delta_{\rm lo})}{(3/2)^2}
>\frac{2}{225}.
\tag{17}
\]
This explicitly accounts for the norm of the full back transformation.

## 7. Exactly two Mellin conditions and the final division

The even condition is \(\langle u,\cosh(x/2)\rangle=0\). Since
\(x\perp e_0\), subtracting the constant from cosh and using
\(\langle e_0,\cosh(x/2)\rangle\ge\sqrt L\) gives
\[
|u_0|^2\le\beta_e\|x\|^2,\qquad
\beta_e=\left[\frac{(a/2)^2}{2(1-(a/2)^2/12)}\right]^2.
\tag{18}
\]
The bracket bounds \(\cosh(a/2)-1\) by its positive Taylor series and
the geometric ratio starting at its quadratic term. Equations (4) and
(17) now yield
\[
q_{\rm even}[u]\ge(\eta-\beta_eK)\|x\|^2,
\qquad \eta-\beta_eK>7/1000>0.
\]
Only after checking this positive numerator do we use
\(\|u\|^2=\|x\|^2+|u_0|^2\le(1+\beta_e)\|x\|^2\), obtaining
\[
\boxed{G_e=\frac{\eta-\beta_eK}{1+\beta_e}>\frac1{150}.}
\tag{19}
\]
The entire numerator, including \(\eta\), is divided by \(1+\beta_e\).

For odd \(u=u_1e_1+z\), the sinh condition similarly gives
\[
|u_1|^2\le\beta_o\|z\|^2,\qquad
\beta_o=\left[\frac{(a/2)^2}{6(1-(a/2)^2/20)}\right]^2.
\]
Indeed \(|\sinh t-t|\le|t|(a/2)^2/[6(1-(a/2)^2/20)]\), while
\(\langle e_1,\sinh(x/2)\rangle\ge\|x/2\|_2\).
Discarding all positive residual energies in this sector gives
\[
G_o\ge\frac{\lambda_2+1/3-(1/2-\lambda_2)\beta_o}{1+\beta_o}
>\frac14.
\tag{20}
\]
All forms commute with reflection. The two conditions on \(E_\pm\)
give these even and odd conditions separately, so parity has no cross
term and (19)--(20) prove (1).

## 8. Rational arithmetic and reproducibility

`check_full_residual.py` is self-contained and uses only the Python
standard library. Every endpoint and every sign decision is a
`fractions.Fraction`. Each interval operation rounds outwards to the
grid \(10^{-35}\mathbb Z\), using integer floor/ceiling division. There
are no binary floats, numerical integration, numerical eigensolvers,
or asserted decimal transcendental inputs, even for display.

The transcendental enclosures are generated as follows:

* \(\exp x\), \(0\le x\le4\): Taylor terms through degree 64, with
  positive tail at most the degree-65 term divided by \(1-x/66\).
  Negative exponentials are reciprocals of these positive intervals.
* \(\operatorname{atanh}x\), \(0\le x\le1/2\): 64 positive terms and
  tail at most \(x^{129}/[129(1-x^2)]\). Thus
  \(\log2=2\operatorname{atanh}(1/3)\). Positive logarithms are reduced
  to \([1,2)\) by exact powers of two and evaluated with the same series.
* \(\arctan x\), \(0\le x\le1/2\): 64 alternating terms end negative;
  the next positive term is an upper remainder bound. Machin's identity
  gives \(\pi=16\arctan(1/5)-4\arctan(1/239)\).
* Euler's constant uses only the elementary integral bounds
  \(\mathsf H_N-\log N-1/N<\gamma<\mathsf H_N-\log N\), \(N=10000\).
  The resulting width \(10^{-4}\) is deliberately conservative and is
  propagated through every occurrence of \(C\) and \(\lambda_2\).
* \(\sqrt2\) is bounded by two explicit rationals whose squares straddle
  2; the checker verifies the squares. With \(q=e^{-s/2}\),
  \[
  H(s)=\tfrac12\log\frac{1+q}{1-q}+\frac\pi4
  -\arctan\frac{1-q}{1+q},
  \]
  which follows by substituting into the defining integral.

Directed displays from the saved run include

| Quantity | Certified statement |
|---|---|
| full tail floor \(\delta\) | \(>0.531007268806\) |
| joint comparison tail \(d\) | \(>0.416111543052\) |
| full pivot \(\sigma\) | \(>0.023959777717\) |
| full shear increment squared | \(<0.161954579590\) |
| back-transformed lower gap \(\eta\) | \(>0.010648790096\) |
| moment penalty \(\beta_eK\) | \(<0.001001186914\) |
| normalized even lower gap | \(>0.009643984631\) |
| odd lower gap | \(>0.280972617826\) |

The JSON distinguishes `full_A22` (an enclosure of an actual block
coefficient) from expressions named `*_lower_bound` or
`*_upper_bound`. An upper endpoint of a lower-bound expression is
**not** an upper bound on the exact Schur pivot or the optimal gap.

The 16 arithmetic checks support the analytic identities and operator
arguments above; they are not an independent external proof review.
The checker can regenerate byte-identical JSON and log, and verifies
all five payload hashes. The manifest does not hash itself.

## 9. Scope and provenance

This is an append-only point certificate on the full connected class
\(\mathcal W_{19651/50000}\). It closes the requested positive-pivot,
infinite-tail, full-shear, moment, and final-normalization obligations.
It does not determine a maximal full-residual window, prove C15 necessary
elsewhere, construct all-window port compatibility, or establish full
Object X/RH. External review remains open.

The equations and source normalization are based on the corrected head
`9aa5cb1...`; all numerical bounds here are recomputed. At checkout the
branch also contained staging commit
`f34c3d6118d9a7e14337abe4d096684952fa9b93`, concerning the different point
0.3930110. Before publication that separate work was finalized on the
remote branch as `be380897d0d3ee8e099d5b15682d4ee66667679b`, a direct
child of the corrected anchor. This deposit preserves that finalized
tree and adds only its own six files. It imports no numerical data from
the separate package. Existing historical files and their manifests
are not rewritten.
