# Full lifted-shell pivot and the trace redundancy in the completed Schur problem

2026-09-18. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.
Coordinate anchor: `0ec5276b2e0a2fe0aa700503e40b4a6a0acb65ff`.
Publication parent, incorporating the concurrent form-interface package:
`ea06f01cc40911d67955065a51ff7bd7b7c1f720`.

## 1. Precise result and limits

Put B=log(5)/2, epsilon=10^-13, h0=10^-20, b=B+h and 0<h<=h0.
Use the complete even shell lift of the parent package, with H(x)=cosh(x/2),
H_B=H(B), A_B^mass=(B+sinh B)/2, A_T=A_B^mass/H_B,
M_B=4(H_B-1)/B, phi_T=H/H_B, phi_M=1-x/B on (0,B).
The superscript on A_B^mass distinguishes this scalar from the core operator.
Define, with even reflection and zero extension,

\[
 \chi=\phi_M/M_B,\qquad \psi=\phi_T-A_T\chi,\qquad
 m_s=\int_B^b sH,\quad t=s(B),\quad p=\|s\|_{L^2(B,b)}.
\]

Thus integral_0^B chi H=1, integral_0^B psi H=0, chi(B)=0 and psi(B)=1.
For S equal to s on the positive shell and its even reflection on the negative shell,

\[
 Ls=t\psi-m_s\chi+S.
\tag{1}
\]

The first result is the genuine full-shell estimate

\[
\boxed{
 D_b(s,s)=Q_W[Ls]\ge {1\over32\,10^{13}}|s(B)|^2+70\|s\|_2^2
}\qquad(s\in H^1(B,b),\ s(b)=0).
\tag{2}
\]

It includes arbitrary free inner trace and the entire infinite shell space.
It is uniform on a right interval, not a finite matrix or a sampled-point claim.
The interval is deliberately conservative. There is no claim of an optimal shell width.

The second result is a correction required before a quantitative full-core Schur gate:
on the natural completed trace-plus-L2 shell realization the uncompressed Schur
operator has the exact zero direction psi. Removing this coordinate redundancy
by transferring the psi direction wholly to the shell gives a complete, bounded
coordinate isomorphism. This changes no source class and adds no Mellin condition.

Neither (2) nor the coordinate correction proves positivity for all sources at
any b>B. The reduced full-core Schur estimate remains open in Section 9.

## 2. Fixed nonpole form, domain and the inherited core direction

Throughout calculations on individual pieces use the NONPOLE form

\[
 q_b[f]=\mathcal E[f]-\kappa\|f\|_2^2
 -\sum_{q\in\{2,3,4,5\}}w_q\langle f,(\tau_{\log q}+\tau_{-\log q})f\rangle,
\quad
 \mathcal E[f]=\int_0^\infty k(r)\|\tau_r f-f\|_2^2\,dr,
\tag{3}
\]

where k(r)=exp(-r/2)/(1-exp(-2r)), kappa=log(8*pi)+gamma+pi/2,
and w_(p^j)=log(p)/p^(j/2). The q=4 weight is log2/2.
Every function is zero extended on the real line. The pole term vanishes for
Ls and psi, but generally NOT for chi and S separately. No claim that those
individual pieces are admissible Weil sources is used.

The common-jump identity identifies (3) with Q_W on the two-moment kernel.
The difference-map argument makes E a nonnegative closed form on L2; the
remaining terms are bounded. Restriction to supported even functions and
then to the closed moment kernel gives a closed lower-bounded form.
Here log2>h and 2b<log7; the active channels are exactly 2,3,4,5.
There are no other prime powers in this range.

We need the inherited gap for the zero-extended psi although it jumps at +/-B.
This extension is proved, rather than obtained from an H1 trace projection.
If f is bounded, piecewise Lipschitz and supported in [-B,B], its Gamma energy
is finite: the internal Lipschitz estimate is integrable at zero, and the
exterior leakage has only an integrable logarithmic boundary singularity.
Cut off f in boundary strips of width eta with continuous affine ramps.
For the resulting difference r_eta, support length is O(eta), its supremum
and total variation stay bounded, and

\[
 \|\tau_r r_\eta-r_\eta\|_2^2\le C\min(r,\eta).
\]

Indeed the first bound follows from the L1 translation estimate for bounded
variation and ||g||_2^2<=||g||_infinity ||g||_1, and the second from its L2 mass.
Consequently E[r_eta]=O(eta(1+|log eta|)) -> 0; use k(r)<=1/(2r)+1/4
for r<=1 and exponential decay beyond 1. The L2 error also tends to zero.
For psi, subtract the small remaining core H-moment times chi. The corrected
cutoffs lie in W_B^even and converge to psi in the form norm. The parent
endpoint theorem therefore implies, without requiring a third moment,

\[
 q_B[\psi]\ge\epsilon\|\psi\|_2^2.
\tag{4}
\]

The same approximation defines the inherited closed core form A on the
form-norm closure of W_B^even in K_B, the even L2 core moment kernel.
It is densely defined, closed and A>=epsilon I. In particular psi belongs
to this form domain. Adding channel 5 at b changes no core-core pairing,
because its core overlap has measure zero.

## 3. Elementary constants and complete Gamma estimates

The directed checker verifies

\[
 4/5<B<81/100,\quad A_T<1,\quad M_B>2/5,\quad
 \cosh(1/2)<6/5,\quad\kappa<6,\quad 46<\log(2/h_0)<47.
\tag{5}
\]

For kappa it suffices to use gamma<1 and the directed bound
log(8*pi)+1+pi/2<6. All active weights are <1: log x/sqrt x has maximum
2/e<1 for x>0, and w4<1 separately. Thus the non-Gamma part of (3)
has operator norm at most 14 (6+2*4).

The parent formulas and (5) give

\[
 \|\psi\|_\infty\le4,\quad\operatorname{Lip}(\psi|_{[-B,B]})\le4,
 \quad\|\chi\|_\infty\le3,\quad\operatorname{Lip}(\chi|_{[-B,B]})\le4.
\tag{6}
\]

For example A_T/M_B<5/2, |phi_T'|<=1/2 and 1/B<5/4.
The cusp from even reflection at zero is Lipschitz and allowed. Since psi(B)=1,
psi>=1/2 on the final 1/8 of each core half, so

\[
 \|\psi\|_2^2\ge1/16,\quad\|\psi\|_2^2\le32,\quad
 \|\chi\|_2^2\le18,\qquad
 a_*=\epsilon/16\le q_B[\psi].
\tag{7}
\]

The identity

\[
 k(r)=\tfrac14\bigl(\operatorname{csch}(r/2)+\operatorname{sech}(r/2)\bigr)
 \le {1\over2r}+\tfrac14
\tag{8}
\]

is valid for every r>0. For a zero-extended core function of supremum M and
internal Lipschitz constant K, internal pairs contribute at most K^2:

\[
 \int_0^2(2-r)(r/2+r^2/4)\,dr=1.
\]

Let T(x)=integral_x^infinity k(r)dr. Exterior pairs contribute at most
2 M^2 integral_0^(2B) T(x)dx <=2 M^2 integral_0^infinity r k(r)dr <10 M^2.
To see the last bound without quadrature, expand k as
sum_(n>=0) exp(-(2n+1/2)r); its first reciprocal-square term is 4 and its
remaining decreasing sum is bounded by integral_0^infinity (2x+1/2)^-2 dx=1.
Hence

\[
 \mathcal E[\psi]\le176,\quad\mathcal E[\chi]\le106,
 \quad |q_B(\psi,\chi)|\le(176+106)/2+14\sqrt{32\cdot18}<500,
 \quad q_B[\chi]\ge-252.
\tag{9}
\]

Every tail here is integrated over the whole real line. No Gamma truncation occurs.

## 4. Pure shell and all core-shell interactions

The two components of S have width h. Their same-side distances are <h<log2;
their opposite-side distances are >2B=log5. Thus ALL arithmetic self-correlations
of S in (3) vanish. Channel 5 still contributes to the core-shell interaction
below and is not discarded there.

A single shell interval has exterior Gamma leakage at least 2 T(h/2) pointwise,
by convexity of T. The interaction of the two even shells subtracts at most
2h k(2B) p^2. Since ||S||^2=2p^2,

\[
 q_b[S]\ge2\bigl(2T(h/2)-\kappa-hk(2B)\bigr)p^2.
\]

For 0<r<=1, k(r)>=1/(2r)-1/4, using 1-exp(-2r)<=2r and exp(-r/2)>=1-r/2.
Therefore 2T(h/2)>=log(2/h)-1/2. Also k(2B)<=1/(4B)+1/4<1.
Writing L=log(2/h), we obtain the convenient conservative estimate

\[
 q_b[S]\ge2(L-8)p^2.
\tag{10}
\]

For a bounded even core function f and x=B+r in the positive shell,

\[
 \int_{-B}^B k(x-y)dy\le\tfrac12\log((2B+r)/r)+B/2
 \le\tfrac12\log(2/r)+\tfrac12.
\]

Here 2B+h<2. Each of the four active prime powers contributes at most
||f||_infinity at x: at most one of x+log q and x-log q lies in the core.
Thus the COMPLETE disjoint-support nonpole pairing obeys

\[
 |q_b(f,S)|\le M\sqrt h\,(L+11)p,\qquad M=\|f\|_\infty.
\tag{11}
\]

For verification of the factor: integrate both reflected shells, then use
integral_0^h [log(2/r)+9]^2 dr = h[(L+9)^2+2(L+9)+2]
<=h(L+11)^2. The factor two from even reflection cancels the half in the
pointwise kernel bound. This covers all prime/Gamma cross terms with signs
bounded conservatively. Finally |m_s|<=(6/5)sqrt(h)p.

## 5. Positive full-shell pivot on an explicit interval

Expand (1) in the nonpole form and use (7)-(11). All complex cross terms
are bounded by their absolute values. This yields

\[
 D_b[s]\ge a_*|t|^2-2\sqrt h(4L+644)|t|p
 +\{2(L-8)-h(8L+450)\}p^2.
\tag{12}
\]

In detail, 644=4*11+(6/5)*500. The shell-moment losses are bounded by
h[(36/5)(L+11)+9072/25] <= h(8L+450), including the possibly negative
q_B[chi] term. Nothing is dropped by labeling it a moment correction.

Young's inequality pays half the trace reserve:

\[
 D_b[s]\ge {a_*\over2}|t|^2+
 \left[2(L-8)-h(8L+450)-{2h\over a_*}(4L+644)^2\right]p^2.
\tag{13}
\]

Both h(8L+450) and h(4L+644)^2 increase with h on this interval, as their
derivatives are 8L+442 and (4L+644)(4L+636), respectively. Therefore the
square bracket is bounded below, uniformly for 0<h<=h0, by the rational number

\[
 76-826\,10^{-20}-32\,10^{13}\,10^{-20}\,832^2>70.
\tag{14}
\]

This proves (2). The bound is deliberately loose and uses the certified
uniform gap 10^-13, not the near-null Rayleigh UPPER bound 3.3e-12.

## 6. A positive closed infinite-dimensional shell realization

Use the Hilbert space X=C direct-sum L2(B,b), with norm |t|^2+||s||^2.
Initially its dense form subspace is

\[
 V=\{(s(B),s):s\in H^1(B,b),\ s(b)=0\}.
\]

Density follows by interior smooth approximation in L2 and a boundary bump
with any prescribed trace and arbitrarily small L2 mass. Define the bounded
lift on ALL of X by L_tilde(t,s)=t psi-m_s chi+S. This notation does not impose
a trace on a general L2 function. The original lift is its restriction to V.

Disjoint core/shell supports, (7), and the moment bound give

\[
 {1\over32}(|t|^2+p^2)\le\|\widetilde L(t,s)\|_2^2
 \le64(|t|^2+p^2).
\tag{15}
\]

For the upper bound use 2||psi||^2 |t|^2+(2+36*(36/25)h)p^2.
For the lower bound write t psi=core+m_s chi, obtaining
|t|^2<=32||core||^2+(20736/25)h p^2; then
1+(20736/25)h<=64. These are uniform rational inequalities at h<=h0.

Pull back the closed nonpole form and take the form-norm closure of V.
It is closable because L_tilde is bounded with bounded inverse on its closed
image by (15), and the physical form is closed and lower bounded.
This gives a densely defined closed form D on X. Estimate (2) extends to it:

\[
 D\ge\delta I_X,\qquad\delta={1\over32\,10^{13}},\qquad
 \|D^{-1}\|\le32\,10^{13}.
\tag{16}
\]

The inverse is that of the associated self-adjoint operator. In physical
lifted-source norm the weaker explicit bound is
D[z]>=||L_tilde z||^2/(2048*10^13). No finite shell truncation was introduced.

## 7. Exact trace redundancy: why the uncompressed Schur cannot have a uniform gap

The H1 direct sum in the parent remains correct. A NEW issue appears only
when forming the Hilbert completions required for a bounded inverse in (16).
Let e=(1,0) in X. Boundary ramps s_eta(B)=1 with support (B,B+eta)
have shell L2 norm tending to zero and bounded variation. By the cutoff
argument in Section 2, L(s_eta) -> psi in the physical form norm.
Consequently e lies in the D form domain and

\[
 \widetilde L e=\psi,\qquad D[e]=q_B[\psi]>0.
\tag{17}
\]

The completed old core K_B also contains psi. The completed joint coordinate
map Phi(w,z)=Jw+L_tilde z therefore has the exact kernel

\[
 \boxed{\ker\Phi=\operatorname{span}\{(-\psi,e)\}.}
\tag{18}
\]

Indeed a zero image has zero shell component s, hence m_s=0 and w=-t psi.
The kernel does not contradict H1 injectivity: psi has nonzero endpoint trace,
while e has no shell function with trace one, so this pair is outside the
original H1 product space.

For precision the cross form extends to a bounded operator C:K_B -> X.
To see this, expand L_tilde into t psi, -m_s chi and S. The functionals
q_B(w,psi), q_B(w,chi) are L2-bounded in w: on the core the Gamma action of
each fixed Lipschitz function is bounded internally plus a logarithmic
boundary term, which lies in L2; the scalar and arithmetic terms are bounded.
The disjoint core-shell Gamma kernel is L2-bounded. Its singular part is a
sum of restrictions of 1/[2(r+z)] across the two interfaces. The weighted
Schur test follows from

\[
 \int_0^\infty{z^{-1/2}\over r+z}\,dz=\pi r^{-1/2},
\]

proved by z=r v^2; its operator norm is at most pi before the factor 1/2.
The remainder from (8) is bounded on finite intervals. All arithmetic shifts
are bounded, and m_s and t are bounded coordinate functionals on X.
This proves boundedness of C without asserting a small coupling norm.

Equality (17), polarization and continuity now give in form/operator sense

\[
 C\psi=De,\qquad A\psi=C^*e,\qquad
 (A-C^*D^{-1}C)\psi=0.
\tag{19}
\]

In particular e and psi belong to the operator domains used in these identities:
the respective form functionals are bounded in X and K_B, as just proved.
The Schur form A-C^*D^-1 C is closed because its subtraction is bounded.
Thus an estimate A-C^*D^-1 C>=sigma I on the ENTIRE completed old core with
sigma>0 is impossible in these coordinates. The relative strict subtraction
C^*D^-1 C <= (1-rho)A with rho>0 is also impossible on psi. Approximating psi
by the original H1 core sources shows that a uniform such inequality cannot
be recovered by simply restricting the written domain back to H1.

This is a coordinate null direction, not a negative physical Weil source:
Phi(-psi,e)=0. No negative source or failure of positivity follows.

## 8. Complete coordinates without the redundancy

Set K_B^0=K_B intersect psi^perp in L2, and restrict the inherited core form
to this closed codimension-one subspace. Its form domain is preserved by
projection because psi belongs to the core form domain. Write this restricted
operator/form A_0. Its lower bound epsilon is inherited unchanged.

Use

\[
 \Phi_0:K_B^0\oplus X\longrightarrow\mathcal K_b,
 \qquad\Phi_0(w,(t,s))=Jw+t\psi-m_s\chi+S,
\tag{20}
\]

where K_b is the even L2 kernel of the global H moment. This is a bounded
bijection, not a restriction on physical sources. Given u in K_b, take its
shell restriction s, put v=u_core+m_s chi in K_B, and set

\[
 t={\langle v,\psi\rangle\over\|\psi\|^2},\qquad w=v-t\psi.
\tag{21}
\]

The trace mode has moved completely into X. Exactly one core coordinate was
removed and the identical shell coordinate retained. The global cosh moment
and parity supply precisely the same two Mellin conditions as before.
No additional Mellin condition is imposed on u.

The norm bounds are

\[
 {1\over32}(\|w\|^2+|t|^2+p^2)\le\|\Phi_0(w,(t,s))\|^2
 \le65(\|w\|^2+|t|^2+p^2).
\tag{22}
\]

The upper bound follows from ||J||=1 and ||L_tilde||<=8. For the lower bound,
orthogonality gives ||v||^2=||w||^2+|t|^2||psi||^2, so
||w||^2+|t|^2<=16||v||^2<=32||u_core||^2+576|m_s|^2;
use the same small-h inequality as in (15).

For an actual H1 source the parent supplies coordinates (w_old,(t_old,s)).
Subtracting c psi from w_old and adding c e to its shell coordinates gives
(20)-(21). Both coordinates remain in the CLOSED form domains because psi
and e are in those domains. Thus every original H1 source is included even
though its new separate components may have jumps at +/-B.

## 9. Exact remaining obligation

Let C_0 be C restricted to K_B^0 and

\[
 R_0=A_0-C_0^*D^{-1}C_0.
\tag{23}
\]

The unresolved even gate is a rigorous uniform lower bound R_0>=sigma I>0
on the entire reduced core, including every direction outside the selected
near-null source. Equivalently one may establish the sufficient relative
bound ||D^-1/2 C_0 A_0^-1/2||^2<=1-rho with rho>0. No such numerical bound
is claimed here. A positive D alone does not establish it.

If R_0>=sigma I is proved and r>=||D^-1 C_0|| is certified, the actual inverse
Schur shear and (22) would give

\[
 Q_W[u]\ge{\min(\sigma,\delta)\over65(1+r)^2}\|u\|^2
\tag{24}
\]

for the actual even sources in this interval. The factor 65 is the source
norm conditioning of the NEW coordinates; it must not be omitted. The
inherited epsilon already includes the old endpoint's division by 1+beta.
Moments in the new lift are exact, so there is no omitted Taylor moment tail
and no reason to divide by that old factor a second time.

The odd sector beyond B would still require its own continuation certificate
before making an all-parity claim. Neither a=log7/2 nor a=1 is reached.

The mathematically established outcome of this package is:

1. full even lifted-shell pivot positive on 0<b-B<=10^-20, with a genuine
   closed infinite-dimensional inverse realization;
2. exact obstruction to an uncompressed uniformly positive full-core Schur
   estimate in that completion;
3. complete quotient coordinates and the precise reduced Schur obligation.

The branch remains research. main and the merged PR #137 are unchanged.

## 10. Consequence for the concurrent inverse-free criterion

During publication, `ea06f01cc40911d67955065a51ff7bd7b7c1f720` added
`inherited-resonance-shell-form-interface-2026-09-18/`. Its files are preserved.
Its Theorem 7.1 is a valid CONDITIONAL implication. However, the prescribed
uniform strict relative hypothesis in its equation (23) is unattainable on
the original complete H1 coordinates, even without invoking operator inverses.

For any fixed B<b<=1 choose moment-corrected core cutoffs w_n in W_B^even
converging to psi in Gamma form norm, and trace-one shell ramps s_n supported
in (B,B+eta_n) with eta_n -> 0. The cutoff arguments already given imply
Ls_n -> psi in the same physical form norm. Bounded finite arithmetic terms
preserve convergence. With a=q_B[psi]>0, therefore

\[
 A[w_n]\longrightarrow a,\qquad D[s_n]\longrightarrow a,\qquad
 C(w_n,s_n)\longrightarrow a,
\]

and for all sufficiently large n the two denominator factors are positive, with

\[
 \boxed{\frac{|C(w_n,s_n)|^2}{A[w_n]D[s_n]}\longrightarrow1.}
\tag{25}
\]

Thus no uniform theta<1 can satisfy the concurrent hypothesis for all w,s.
This obstruction holds for each fixed b>B (up to 1 here); it is not limited
to the small interval used to certify D. It neither refutes the conditional
theorem nor gives a negative physical source. It shows that its proposed
strict relative next gate must first remove the shared trace direction.
A corresponding inverse-free criterion may instead be applied to the
complete reduced coordinates of Section 8.

The positive shell frame gate in Sections 6 and 8 of the concurrent package
IS supplied on our small interval by the physical delta_sh=1/(2048*10^13).
In its graph norm ||z||_G^2=D[z]+(Gamma_b+1)||Lz||^2, Gamma_b<14 here, so

\[
 D[z]\ge{\delta_{\rm sh}\over\delta_{\rm sh}+15}\|z\|_G^2.
\]

This also supplies strict coercivity in that graph realization on the stated
small interval. It does not change the limiting ratio (25). Both the operator
and inverse-free formulations require the same correction of the coordinates.
