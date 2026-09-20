# Full even width amplification by a core/profile three-block certificate

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `8f5b711145b28b6dbfc8280d8e51625f3d2f1532`.
Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.
Tail origin: `6a16d90b551588572c87e622c21c2df7f7b1adc2`,
`prime-power-segment-4-2026-09-18/PROOF.md`, Sections 2, 3, 6 and 7.
The 73 input files are bound by byte length, SHA-256 and Git blob hash.
Publication also preserves the concurrent high-tail commit
`7d269c7bd3d3507e0109181fcad0b02ddddb2d14` unchanged; its new package
is not needed as a mathematical input for this calculation.

## 1. Statement

Put B=log(5)/2 and h0=10^-20. On the FULL original interval

\[
                    0<h=b-B\le h_0
\]

every nonzero actual even H1_0((-b,b)) source with exactly the two
original Mellin conditions satisfies

\[
             \boxed{Q_W[u]>3\,10^{-15}\|u\|_{L^2(dx)}^2.}       \tag{1}
\]

The full reduced A-gauge and original physical-L2-gauge operators obey

\[
 \boxed{\Theta_A(b)<1-9\,10^{-23}},\qquad
 \boxed{\Theta_0(b)<1-2\,10^{-29}},                              \tag{2}
\]
\[
 \boxed{R_A\succeq\sigma_* I,\quad R_0\succeq\sigma_* I,
 \qquad \sigma_*={3\,10^{-15}\over140000000}.}                  \tag{3}
\]

The margins in (2) are intentionally conservative consequences of (1).
They are NOT sharp estimates of either operator. On the previously
certified much smaller interval the previous stronger relative bounds
remain available unchanged.

The proof uses a precisely defined 31-dimensional low core, the ENTIRE
infinite coretail, and the ENTIRE shell profile. It retains the signed
low/high coupling, bounds the high/profile coupling, and pays the complete
low/profile coupling. Sections 9-10 transfer this certificate to the
requested complete A-energy near/low/high Gram operator, including every
mixed block. No finite shell matrix or discarded coretail is used.

This is an EVEN theorem. Odd continuation beyond B remains open, as do
larger right widths, log(7)/2, a=1, C1-GEOM, Object X and RH. There is no
A1 and no additional condition on the physical source. Reproduction is
not an independent external audit.

## 2. Full core plus profile coordinates, with no duplicated trace

All physical inner products use dx and are linear in the first argument.
Import the fixed H(x)=cosh(x/2), chi, psi, the closed core space F_B and
the full shell space X=C direct-sum L2(B,b) from the pinned coordinate
theorems. Write

\[
 m_s=\int_B^b sH,\quad Y_s=-m_s\chi+S_s,\qquad
 \widetilde L(t,s)=t\psi+Y_s,
\]

where S_s is the even physical shell extension and ||S_s||^2=2||s||^2.
Set p=||s|| on the RIGHT shell. The imported bounds are

\[
 |m_s|\le(6/5)\sqrt h\,p,\quad \|\chi\|_\infty\le3,
 \operatorname{Lip}\chi\le4,\quad \|\chi\|^2\le18,
 \quad \chi(B)=0.                                             \tag{4}
\]

The normalized triangular chi has positive-half moment one, so Y_s has
exactly zero global H moment. The nonpole form q agrees with Q_W on that
moment kernel. Evenness makes the two original Mellin conditions
equivalent to this H condition; it does not replace them by an extra one.

Let F_D be the parent's full closed shell form domain, e=(1,0) in F_D,
and define

\[
 F_Y=\{s\in L^2(B,b):(0,s)\in F_D\},\qquad d_Y[s]=d[(0,s)].
\]

This is a closed dense form subspace: the bounded projection
(t,s) -> (0,s)=(t,s)-t e preserves F_D and is continuous in its graph
norm. Density follows by projecting the dense shell form domain. Thus
F_D=C e direct-sum ({0} times F_Y), as topological form spaces.
The prior complete isomorphism Phi_0(w,(t,s)) now gives

\[
             \Psi:F_B\oplus F_Y\longrightarrow F_b,
             \qquad \Psi(v,s)=Jv+Y_s.                         \tag{5}
\]

Indeed v=w+t psi is the complete physical-L2 splitting of F_B into
psi-perp and C psi. Its inverse is t=<v,psi>/||psi||^2, w=v-t psi;
all maps preserve the form domains because psi belongs to F_B. Equation
(5) is consequently a form-space isomorphism, not a restriction of the
source class. At Hilbert level, s=u|_(B,b) and v=u_core+m_s chi give its
unique inverse. In particular the trace direction occurs exactly once.

For actual H1 sources the exact preimage is v in internal even H1 on
(-B,B), with its core moment zero, s in H1(B,b), and

\[
                        v(B)=s(B),\qquad s(b)=0.              \tag{6}
\]

The jump of the separate zero extensions is canceled in the physical
sum. Separate core zero boundary values are NOT imposed. Both directions
of (6) follow from chi(B)=0 and the ordinary H1 gluing theorem. This
also follows directly from the parent's condition w(B)+t=s(B).

## 3. The canonical tail floor: exact space and physical normalization

Use the physical isometry U_B f(x)=sqrt(2B) f(Bx) onto
H_ref=L2((-1,1),dx/2). Let P_n be the unnormalized Legendre polynomials,
||P_n||^2=1/(2n+1), and E_n=sqrt(2n+1)P_n. Work in the even space
X_ref=P_0-perp, and define

\[
 L_0=\operatorname{span}\{P_2,P_4,\ldots,P_{62}\},\qquad
 Y=\overline{\operatorname{span}\{P_{64},P_{66},\ldots\}}^{L^2}.
                                                               \tag{7}
\]

All form restrictions to Y also impose the reference form domain. With
m(x)=cosh(Bx/2), the EXACT moment map is

\[
 Mx=x-{\langle x,m\rangle\over\langle1,m\rangle}1,
 \quad x\in X_{\rm ref},\qquad v=U_B^{-1}Mx.                    \tag{8}
\]

It maps onto the complete moment kernel. Its inverse there deletes the
constant coefficient. Polynomials belong to the reference form domain,
and the finite-rank moment correction preserves it. The reference domain
is the harmonic-diagonal form domain intersected with L2(V dx/2),
V=-log(1-x^2)/2. The split (7) preserves this domain.

The origin package proves, and the present engine recomputes,

\[
 \|Mx\|^2\le(1+\beta)\|x\|^2<2\|x\|^2,
 \quad \beta=\left[{(B/2)^2\over2(1-(B/2)^2/12)}\right]^2,
\]
\[
 \epsilon_m={(B/2)^{64}\over64!\,[1-(B/2)^2/(65\cdot66)]},
 \qquad \|My\|^2\le(1+\epsilon_m^2)\|y\|^2\quad(y\in Y).       \tag{9}
\]

The second inequality uses orthogonality of y to 1; the small constant
component is orthogonal to y. Let p_G be the pinned degree-64 regular
Gamma polynomial, with directed uniform error epsilon_G on [0,5/3].
With M0=M on L0 and M0=I on Y, its complete bounded form error is

\[
 e_c=2(2B)\epsilon_G+80\epsilon_m,
 \quad\|M^*q_BM-(M^0)^*q_B^{p_G}M^0\|\le e_c.                 \tag{10}
\]

Here and below the physical isometry is implicit in reference q_B.
The canonical even tail floor is

\[
 \delta_c=H_{64}-\log(2\pi B)-\gamma
 -2B\bigl(1/4-g(2B)+\epsilon_G\bigr)
 -\bigl(\log2+\log3/\sqrt3+\log2/2\bigr)-e_c,
\]
\[
 a[U_B^{-1}My]\ge\delta_c\|y\|^2,\qquad
              \delta_c=0.719448628450052179\ldots .            \tag{11}
\]

The JSON records its outward rational endpoints; the new engine requires
them to equal the canonical `even_tail_floor` enclosure byte-value for
byte-value as rational numbers. This is not an unbound decimal imported
from a discussion. Channels 2,3,4 act on the core at B; channel 5 has
zero-measure core/core overlap and enters the new core/shell block below.

In physical norm (11) supplies the floor

\[
 \alpha_Y={\underline\delta_c\over1+\overline\epsilon_m^2}
                         >719/1000                            \tag{12}
\]

on U_B^-1 M Y ONLY. It is not asserted on an arbitrary A-gauge complement.
The valid energy high subspace to which it will be applied is specified
in Section 10.

## 4. Complete core/profile coupling below four

For disjoint core and shell supports the scalar remainder has zero cross
pairing. The Gamma cross kernel is -k(|x-y|),
k(r)=exp(-r/2)/(1-exp(-2r)). The pinned full-line normalization gives

\[
 k(r)\le{1\over2r}+{1\over4},\quad
 \int_0^\infty r k(r)\,dr<5,\quad
 \|\text{non-Gamma remainder}\|\le14.                         \tag{13}
\]

For completeness, the Carleman kernel 1/(r+z) has norm at most pi:
the weighted Schur integral with weight z^-1/2 is pi r^-1/2,
by the substitution z=r t^2. Restricting its positive input and output
intervals preserves the bound. On the same-side core/shell pair the
singular part has coefficient 1/2 and the bounded part 1/4. On the
opposite core half, distance is at least B and k(B)<1 by (13) and B>4/5.
After the two reflected shell integrals and
||f||=sqrt(2)||f|_(0,B)||, this gives

\[
 |\mathcal E(f,S_s)|\le
 \left({\pi\over\sqrt2}+{5\sqrt2\over4}\sqrt{Bh}\right)\|f\|p.
                                                               \tag{14}
\]

There are four active prime-power channels, with

\[
 (w_2,w_3,w_4,w_5)=
 (\log2/\sqrt2,\log3/\sqrt3,\log2/2,\log5/\sqrt5).
\]

At x=B+r, 0<r<h, the nonzero core samples f(x-log q), reflected to
the positive core by evenness, run respectively through the intervals

\[
\begin{array}{c|c}
2&(B-\log2,\ B-\log2+h)\\
3&(\log3-B-h,\ \log3-B)\\
4&(\log4-B-h,\ \log4-B)\\
5&(B-h,\ B).
\end{array}                                                    \tag{15}
\]

They lie in (0,B), in this order, and are disjoint for every h<=h0;
their endpoint inequalities are checked outward at h0. Therefore

\[
 \left\|\sum_q w_q f(B+r-\log q)\right\|_{L^2(0,h)}^2
 \le\left(\sum_q w_q^2\right)
        \sum_q\int_0^h|f(B+r-\log q)|^2dr
 \le{1\over2}\left(\sum_q w_q^2\right)\|f\|^2.
\]

The factor two from the physical reflected shell pairing yields

\[
 |q_{\rm prime}(f,S_s)|\le\sqrt{2\sum_qw_q^2}\,\|f\|p.         \tag{16}
\]

This is Cauchy-Schwarz on disjoint INPUT intervals. No orthogonality of
shell images is asserted, and no partial translation is assigned a norm
tending to zero.

We need a bounded physical-L2 functional for the moment correction. Put
d_x=B-|x|. The zero-extended chi obeys, for r<=d_x, a second-difference
bound 8r, and for r>d_x the bound 12. Since d_x<1, (13) implies

\[
 |G_\chi(x)|\le40+12\left({1\over2}\log(1/d_x)+{21\over4}\right)
                 =103+6\log(1/d_x).
\]

Consequently

\[
 \|G_\chi\|^2\le2(103^2+2\cdot103\cdot6+2\cdot6^2)
 =23834<155^2,\qquad14\sqrt{18}<60,
\]
\[
                         |q_B(f,\chi)|\le215\|f\|.            \tag{17}
\]

These identities hold first on smooth tests and extend by L2 boundedness
and the pinned form-density argument. Combining (4), (14), (16), (17)
gives on the ENTIRE even supported L2 core

\[
 |q_b(Jf,Y_s)|\le C(h)\|f\|p,
\quad C(h)={\pi\over\sqrt2}+\sqrt{2\sum_qw_q^2}
        +{5\sqrt2\over4}\sqrt{Bh}+258\sqrt h<4.                \tag{18}
\]

The checker encloses every logarithm, pi and square root and proves the
last strict inequality at h0. This is a bound for the complete nonpole
pairing, with all four prime powers and the exact moment correction.

## 5. Separate full-shell and pure-profile floors

Write L=log(2/h), so 46<L0=log(2/h0)<47. The pinned full-shell proof,
Section 5, gives

\[
 d[(t,s)]\ge\delta_{\rm sh}|t|^2+
 [2(L-8)-h(8L+450)-32\,10^{13}h(4L+644)^2]p^2,
 \quad\delta_{\rm sh}=1/(32\,10^{13}).
\]

The two losses are monotone increasing in h on this interval. Their
sum is at most h0[826+32*10^13*832^2]<3. We KEEP the stronger floor

\[
 d[(t,s)]\ge\delta_{\rm sh}|t|^2+(2L-19)p^2,
                       \qquad2L-19>73.                       \tag{19}
\]

Before paying the trace Young inequality, the same pinned expansion at
t=0 gives

\[
 d_Y[s]=q_b[Y_s]\ge[2(L-8)-h(8L+450)]p^2
                   >(2L-17)p^2>75p^2.                        \tag{20}
\]

Equation (20) is valid because the trace has been moved into the COMPLETE
core v in (5). It would be invalid to use it for arbitrary (t,s) in (19).
The projection construction in Section 2 ensures its validity on all F_Y.

## 6. Low/profile and high/profile blocks, uniformly in h

For l=sum_(i=2,4,...,62) c_i P_i, put J_ii=1/(2i+1). Its reference
norm is c*Jc. The exact moment ratios r_i=<P_i,m>/<1,m> have |r_i|<=1
because m is positive and |P_i|<=1. Thus

\[
 \|U_B^{-1}Ml\|_\infty^2
 \le{4\over2B}\sum_{i=2,4,\ldots,62}(2i+1)\,\|l\|^2
 ={4\cdot2015\over2B}\|l\|^2<72^2\|l\|^2.                   \tag{21}
\]

The imported bounded-core pairing, full-shell proof (11), is
|q(f,S_s)|<=||f||_infinity sqrt(h)(L+11)p. Equations (9), (17) and
||Ml||<2||l|| therefore give

\[
 |q_b(U_B^{-1}Ml,Y_s)|
 \le\sqrt h\,[72(L+11)+516]\|l\|p
 \le b_L\|l\|p,\qquad b_L=4692\,10^{-10}.                     \tag{22}
\]

Indeed h[72(L+11)+516]^2 has positive derivative because its bracket
exceeds 144, and at h0 the bracket is <4692. This avoids a false
uniform bound on L as h tends to zero.

For the ENTIRE y in Y, (9) and (18) instead give

\[
 |q_b(U_B^{-1}My,Y_s)|\le4\sqrt{1+\epsilon_m^2}\|y\|p
                       <{41\over10}\|y\|p.                  \tag{23}
\]

This includes all high frequencies. Pay this mixed block using

\[
 2(41/10)\|y\|p\le{1681\over6000}\|y\|^2+60p^2.
\]

The remaining tail and profile constants are

\[
 \delta_*:=\underline\delta_c-1681/6000>0.439,
                              \qquad d_*=15.                 \tag{24}
\]

No sign or orientation of this mixed block has been assumed.

## 7. The exact finite Schur comparison, including the infinite core Gram

Let A^0_ij=q_B^(p_G)[MP_i,MP_j] on L0, and let C denote the ACTUAL
low-to-entire-Y coupling of M*q_BM. Let G be the model coupling Gram
from the tail-origin proof, with its moment congruence on BOTH indices.
That proof and (10) yield, as finite Hermitian form inequalities,

\[
 A_{\rm actual}\succeq A^0-e_cJ,
 \qquad C^*C\preceq G_{\rm act}:={1001\over1000}G+1001e_c^2J.  \tag{25}
\]

Here C maps reference low vectors to the full reference tail Hilbert
space. In coordinates its Gram has the basis norm matrix J exactly as
written. This is not a truncation of C to finitely many tail modes.

To recall why G contains the infinite tails, put V_ij=<P_i,V P_j>,
W_ij=<P_i,V^2 P_j>, K_ij=<P_i,K_(p_G)P_j>, S_ij=<P_i,S P_j>.
The exact pre-moment Gram is

\[
\begin{aligned}
G^0_{ij}={}&W_{ij}+\langle SP_i,SP_j\rangle
 -\langle VP_i,SP_j\rangle-\langle SP_i,VP_j\rangle\\
&-\sum_{k=0,2,\ldots,62}(2k+1)(V_{ik}-S_{ik})(V_{kj}-S_{kj})\\
&+\sum_{k=64,66,\ldots,128}(2k+1)
 [K_{ik}K_{kj}-(V_{ik}-S_{ik})K_{kj}-K_{ik}(V_{kj}-S_{kj})].
\end{aligned}                                                   \tag{26}
\]

The final upper index is exact polynomial support (degree <=j+65),
not an imposed tail cutoff. The first line contains the full infinite
V and shift images through their exact integrals. All signed shift
actions are summed on each exact interval BEFORE squaring; all channel
and Gamma/shift mixed terms are included. The new checker reconstructs
these quantities using rational Legendre recurrences, analytic logarithmic
moments and the pinned directed Gamma model. No quadrature is involved.

Let B_L map l to the Riesz representative in L2(B,b) of
s -> q_b(U_B^-1 Ml,Y_s), so ||B_L||<=b_L by (22). With x=l+y,
the original physical form is bounded below by the continuous comparison
form

\[
\begin{aligned}
\mathcal Q[l,y,s]={}&(A^0-e_cJ)[l]+2\operatorname{Re}\langle Cl,y\rangle
 +\delta_*\|y\|^2\\
 &+2\operatorname{Re}\langle B_Ll,s\rangle+15\|s\|^2.
\end{aligned}                                                   \tag{27}
\]

The conjugation convention in the representatives is chosen to give
these pairings; only their norms and Hermitian Grams enter the estimates.
The pointwise form inequality q_b[U_B^-1 M(l+y)+Y_s]>=Q follows by
(11), (20), (23)-(25). Its low/high and low/profile entries are the ACTUAL
couplings; the high/profile entry was paid with its full norm in (24).

The exact square completion of this NAMED COMPARISON form has low Schur
matrix bounded below by

\[
 R_{\rm cmp}=A^0-e_cJ-{G_{\rm act}\over\delta_*}
                    -{4692^2\over15\,10^{20}}J.                \tag{28}
\]

The directed rational LDL certificate gives 31 strictly positive pivots
and, from the upper inverse trace T=tr(J R_cmp^-1),

\[
 R_{\rm cmp}\succeq\sigma_L J,\qquad
 \sigma_L=1/\overline T>1.23769\,10^{-12}.                      \tag{29}
\]

This uses no numerical eigenvalues: the largest eigenvalue of a positive
inverse is at most its trace, and the trace is bounded by directed
triangular solves with the rational interval LDL factors. All entries,
all 31 pivots and the outward inverse-trace result are reproducible from
the checker; the JSON records each pivot and the reserve.

The square-completion change of variables in (27) is

\[
 (l,y,s)\longmapsto
 (l,y+\delta_*^{-1}Cl,\ s+15^{-1}B_Ll).
\]

Its inverse has norm <=1+r, with

\[
 r^2\le {\operatorname{tr}(J^{-1}G_{\rm act})\over\delta_*^2}
                    +{4692^2\over15^2\,10^{20}}.              \tag{30}
\]

Both off-diagonal maps are included in this product-space norm. Hence

\[
 q_b[U_B^{-1}M(l+y)+Y_s]
 \ge\mathcal Q[l,y,s]
 \ge{\min(\sigma_L,\delta_*,15)\over(1+r)^2}
                       (\|l\|^2+\|y\|^2+p^2).                \tag{31}
\]

This comparison shear is explicitly NOT identified with the inverse of
the actual high-core or shell operator. Such an identification is neither
used nor needed: (27) is a proved dominated quadratic form, and its own
exact completion proves its coercivity. Formula (31) then transfers that
coercivity to the original form by the displayed inequality. This
distinguishes the present argument from substituting an approximate
inverse into an identity for an actual Schur operator.

Failure of the finite comparison LDL would mean UNDECIDED for the actual
form. It would not produce a negative Weil source. In this package the
comparison succeeds.

## 8. Physical norm conversion and all-source conclusion

Equations (4) and disjoint supports give

\[
 \|Y_s\|^2=2p^2+|m_s|^2\|\chi\|^2
 \le(2+648h/25)p^2<4p^2.
\]

Together with the GLOBAL moment map bound (9), weighted Cauchy-Schwarz
therefore gives

\[
 \|U_B^{-1}Mx+Y_s\|^2
 \le(\sqrt2\|x\|+2p)^2
 \le6(\|x\|^2+p^2)
 =6(\|l\|^2+\|y\|^2+p^2).                                   \tag{32}
\]

Thus the entire physical gap furnished by (31) is

\[
 \gamma_{\rm phys}=
 {\min(\sigma_L,\delta_*,15)\over6(1+r)^2}
                         >3\,10^{-15}.                        \tag{33}
\]

The factor 6 pays the full moment-map norm as well as the profile lift
and their possible overlap on the core. No separate 1+beta division is
missing; that cost is already paid in (32). The new calculation starts
from (25) and the exact moment reconstruction, not from a prior final
physical gap whose old losses might be unwound.

The form-space isomorphism (5) extends (31)-(33) to the complete F_b;
(6) includes every actual even H1_0 source. This proves (1) uniformly in
h, including h=h0. Exact isometric zero extension also gives the same
even constant for every 0<b<=B+h0. It preserves precisely E_+=E_-=0 and
the full-line nonpole form. The stronger previously certified endpoint
constant at and below B remains available.

## 9. Full A-gauge and original-gauge operator norms

Use the pinned A-gauge theorem's complete form coordinates Phi_A and
their physical inverse norm bound

\[
 \|\Phi_A(f,z)\|^2\ge
 {\|f\|^2+\|z\|_X^2\over140000000}.                           \tag{34}
\]

By (1), the full block form F_A is >=sigma_*(||f||^2+||z||^2),
where sigma_* is defined in (3). Infimizing over the COMPLETE F_D gives

\[
 R_A[f]=a_A[f]-K_A[f]\ge\sigma_*\|f\|^2,\qquad
 K_A[f]=\|D^{-1/2}C_Af\|^2.                                   \tag{35}
\]

The infimum is legitimate for the actual positive closed D and its
Riesz solution; D^-1 is not replaced by a profile inverse. The A-gauge
forcing has zero direct trace component:
c_A(f,(t,s))=q_b(Jf,Y_s). By (18)-(19), on all z=(t,s),

\[
 |c_A(f,z)|^2\le16\|f\|^2p^2,
 \quad d[z]\ge\delta_{\rm sh}|t|^2+(2L-19)p^2,
\]
\[
                  0\le K_A[f]\le {16\over73}\|f\|^2.          \tag{36}
\]

This includes the possibly nonzero trace coordinate of D^-1 C_Af.
Put M_A=16/73. Combining (35)-(36), K_A<=(M_A/sigma_*)R_A, hence

\[
 K_A\preceq\theta_A a_A,\qquad
 \theta_A={M_A\over M_A+\sigma_*}<1-9\,10^{-23}.                \tag{37}
\]

Since a_A>=10^-13 I, the bounded operator
B_h=D^-1/2 C_A A_A^-1/2 is defined on the entire reduced core Hilbert
space. Equation (37) is precisely B_h*B_h<=theta_A I, proving its
FULL operator norm bound in (2).

For the original physical-L2 gauge the pinned exact congruence gives
R_0[w]=R_A[Uw], with ||Uw||>=||w|| and ||U||<=1458. Its exact trace
decomposition also gives

\[
 K_0[w]={|a(w,\psi)|^2\over a[\psi]}+K_A[Uw].
\]

Using |a(w,psi)|<=272||w|| and a[psi]>7/50,

\[
 K_0[w]\le\left({272^2\over7/50}+{16\over73}\,1458^2\right)
                   \|w\|^2<10^6\|w\|^2.
\]

Together with R_0>=sigma_* I this proves

\[
 \Theta_0\le{10^6\over10^6+\sigma_*}<1-2\,10^{-29}.            \tag{38}
\]

The two gauges and their relative constants are kept distinct. The
inverse factor in (34) is deliberately paid in this deduction of an
absolute Schur floor. The physical statement (1) was already obtained
directly in (33); it is not weakened by reapplying a relative block bound.

## 10. Precisely defined A-energy near/low/high blocks and all mixed terms

This section supplies a full operator statement in the requested energy
geometry. It does NOT treat the finite L0 matrix in (28) as a finite
surrogate for an unspecified infinite A-gauge complement.

Give F_(B,A)^0 the complete a_A energy inner product. Let v_A be the
fixed, unaltered trace-eliminated source from the pinned directional
package, and n=v_A/sqrt(a_A[v_A]). Define the exact closed high space

\[
 \mathcal H=\{f\in F_{B,A}^0:
            M^{-1}U_B f\in Y,\quad a_A(f,v_A)=0\},
\]
\[
 \mathcal L=(\mathbb C n\oplus_{a_A}\mathcal H)^{\perp_{a_A}}.
                                                               \tag{39}
\]

The 31 low reference coefficient functionals in (7) are energy-continuous
by core coercivity and boundedness of M^-1 U_B. The last functional in
(39) is energy-continuous as well. Thus H is closed with codimension at
most 32, n is energy-orthogonal to H, and L is exactly defined and has
dimension at most 31. We have the complete orthogonal sum

\[
             F_{B,A}^0=\mathbb C n\oplus_{a_A}\mathcal L
                                      \oplus_{a_A}\mathcal H.  \tag{40}
\]

The energy space is isometric to the core Hilbert space under A_A^1/2.
Let G be the representation of B_h*B_h on (40). The previously reproduced
direction certificate supplies G_nn<=nu with nu<7.55*10^-6. Equations
(12) and (36), applied to exactly the H of (39), give

\[
 G_{HH}\preceq\kappa_H I,\qquad
 \kappa_H={16\over73(719/1000)}<31/100.                         \tag{41}
\]

From the newly established FULL bound (37),

\[
 G_{LL}\preceq\theta_A I,\quad
 \|G_{nL}\|^2\le\nu\theta_A,\quad
 \|G_{nH}\|^2\le\nu\kappa_H,\quad
 \|G_{LH}\|^2\le\theta_A\kappa_H.                             \tag{42}
\]

The mixed bounds follow from Cauchy-Schwarz for the common nonnegative
Gram form K_A, so they permit aligned shell images. More strongly, for
EVERY complex c, l in L and y in H, the WHOLE block form obeys

\[
 \begin{aligned}
 &|c|^2G_{nn}+G_{LL}[l]+G_{HH}[y]\\
 &\quad+2\operatorname{Re}\bigl(cG_{nL}(n,l)
                         +cG_{nH}(n,y)+G_{LH}(l,y)\bigr)\\
 &\hspace{25mm}\le\theta_A(|c|^2+a_A[l]+a_A[y]).
 \end{aligned}                                                 \tag{43}
\]

Notation in (43) uses the linear-in-first-argument convention; reversing
the order of a mixed pair conjugates it and leaves the real quadratic
form unchanged. Equation (43), not just three diagonal estimates,
certifies the norm of the complete 3-by-3 operator matrix strictly below
one. It follows from (37), whose proof already retained the complete
low/high and shell mixing in (27)-(31). We do NOT infer (43) by ignoring
G_LH or by combining the scalar diagonal bounds (41)-(42).

This route gives a rigorous low block and all mixed blocks without
constructing a basis of the energy-oblique finite space L. The exact
finite computation is instead performed in the explicit raw L0 basis,
then transferred through the all-source physical theorem and the actual
closed Schur/Riesz realization. The near-null source has not been
reselected or physically renormalized; n is only its energy-unit
coordinate for displaying the operator blocks.

## 11. Reproduction, editorial endpoint clarification and limitations

During this calculation the concurrent package `a-gauge-high-tail-2026-09-19`
was published at `7d269c7...`. It defines the same energy high/low spaces
as (39)-(40), proves a high-block bound 63/73, and leaves the low block
and complete mixed norm open. Its eight files are preserved unchanged.
Equations (41)-(43) sharpen its high bound and supply its remaining full
operator gate. This calculation independently recomputes its needed
endpoint data and does not import or claim an external audit of that
concurrent checker.

`check_width.py --verify` first checks the 73 input bindings and replays
the transition checker and its full 40/31/28/43/9 inherited chain. It then
recomputes the relevant EVEN endpoint matrix, complete infinite coupling
Gram, tail floor, new 31-pivot comparison, both shear contributions and
every norm-conversion loss. It does not run the original source-selection
inverse iteration or claim to re-audit its fixed source. The odd endpoint
matrix is not recomputed here and no odd right-continuation result follows.

All proof decisions use standard-library integers/Fractions and directed
intervals on the pinned 10^-200 grid. Exact radicals use integer square
roots; logs, pi, gamma and the Gamma model use the pinned proved remainder
bounds. JSON stores rational endpoints even when a 24-place displayed
decimal cannot resolve a relative margin of order 10^-29. The explicit
rational margins are recorded separately. The new JSON and log reproduce
byte for byte and the seven payload SHA-256 hashes are checked.

Analytic form closure, disjoint-interval Cauchy-Schwarz, Carleman
boundedness, the infinite Gram identity and the operator implications
are mathematical arguments above. A successful checker verifies their
arithmetic implementation and bindings, not an independent formal proof
or external peer review.

Append-only editorial clarification: the older tiny dyadic interval is
consistently understood as 0<h<=2^(-10^16), including its right endpoint.
At equality L=(10^16+1)log2>10^16/2, so its stated estimates already
include equality. Its earlier strict-inequality wording does not require
changing pinned historical files. The new result (1) also includes h=h0.

This package appends eight new files. It does not change main, Registry,
existing packages, the source class, or the two Mellin conditions, and
does not create a PR or merge. The epistemic status stays
**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
