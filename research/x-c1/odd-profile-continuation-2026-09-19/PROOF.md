# Odd continuation on the full shell width and the local all-parity theorem

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Mathematical anchor: `7741eca6f14bdc3017f6a299aff06eb66db2e697`.
Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.
Endpoint tail origin: `6a16d90b551588572c87e622c21c2df7f7b1adc2`,
`prime-power-segment-4-2026-09-18/`.
The concurrent transport-ladder update `cb56df64ca60c046f99ddba2822e4e216657504d`
is preserved. The 81 mathematical input files are bound by byte length,
SHA-256 and Git blob hash.

## 1. Results and limits

Put B=log(5)/2, h0=10^-20, b=B+h. For every 0<h<=h0 and every nonzero
actual ODD source u in H1_0((-b,b);C) satisfying the ORIGINAL two Mellin
conditions E_+u=E_-u=0, this package proves

\[
                    \boxed{Q_W[u]>10^{-12}\|u\|_{L^2(dx)}^2.}  \tag{1}
\]

This is an independent odd moment, form-domain and full-block argument;
the even theorem is not assumed to imply (1). Combining (1) with the
reproduced even theorem at the anchor gives, for EVERY nonzero actual
source of either or mixed parity on the same interval,

\[
                    \boxed{Q_W[u]>3\,10^{-15}\|u\|_{L^2(dx)}^2.}\tag{2}
\]

By exact zero extension, (2) holds for all 0<b<=B+10^-20. The original
stronger gap 10^-13 for b<=B remains available. Equation (2) is a LOCAL
all-parity theorem, not a uniform result on larger or iterated windows.

In the new, nonredundant FULL ODD CORE plus PROFILE coordinates defined
below, the actual closed Schur operator additionally obeys

\[
 R_o\succeq{1\over2\,10^{12}}I,\qquad
 \Theta_o:=\|D_o^{-1/2}C_oA_o^{-1/2}\|^2<1-2\,10^{-12}.        \tag{3}
\]

This Theta_o is defined here and is not identified with either even
A-gauge or even physical-L2-gauge operator. There is no independent
trace coordinate in this odd profile space and thus no duplicated trace.

The unbounded core, its full infinite tail, the full shell profile,
every mixed term, and all physical norm costs are included. No source is
selected, no numerical eigenvalues or quadrature are used, and no A1 or
third Mellin condition is added. Larger/iterable widths, historical
P11/R43 Strong Terminal, Connected Unit-Window Coercivity, full C1-GEOM,
Object X, global Weil positivity and RH remain open. No external audit
is claimed.

## 2. Odd moment and an exact boundary-vanishing corrector

All physical scalar products use dx and are linear in the first argument.
Let H_o(x)=sinh(x/2). For odd u, its cosh moment is automatically zero;
E_+u=E_-u=0 is exactly the condition integral u H_o=0. This is the
restriction of the original two conditions to the odd invariant subspace.

For 0<=x<=B set

\[
 \rho_o(x)={x\over B}(1-x/B),\quad
 M_o=\int_0^B\rho_o(x)\sinh(x/2)\,dx,\quad
 \chi_o(x)=\rho_o(x)/M_o,
\]

and reflect chi_o ODDLY and extend by zero outside the core. It is in
H1_0((-B,B)), with chi_o(0)=chi_o(B)=0 and exact positive-half moment
one. Its normalization is exact; it is not replaced by a rounded number.
For example direct integration gives the identity

\[
 M_o={4\over B}\sinh(B/2)-{16\over B^2}(\cosh(B/2)-1).
\]

The lower bound uses no cancellation or quadrature:

\[
 M_o\ge\int_0^B\rho_o(x){x\over2}\,dx={B^2\over24}>{2\over75}.
\]

Since 4/5<B<81/100, we obtain

\[
 \|\chi_o\|_\infty<75/8<10,\quad
 \operatorname{Lip}(\chi_o)<375/8<47,\quad
                       \|\chi_o\|_2^2<200.                   \tag{4}
\]

The Lipschitz bound holds across zero and for the zero extension too.
For s in L2(B,b), let S_s^o equal s on the right shell, -s(-x) on the
left shell, and zero on the core. Write

\[
 p=\|s\|_{L^2(B,b)},\quad \|S_s^o\|^2=2p^2,\quad
 m_s^o=\int_B^b sH_o,\quad Y_s^o=-m_s^o\chi_o+S_s^o.           \tag{5}
\]

As b<1 and sinh(1/2)<3/5,

\[
 |m_s^o|\le(3/5)\sqrt h\,p,\qquad
 \int_{-b}^bY_s^oH_o=-2m_s^o+2m_s^o=0.                       \tag{6}
\]

Both original Mellin conditions therefore hold for every odd profile
Y_s^o in its form domain.

## 3. The physical form and a complete odd coupling estimate

Use the same connected nonpole identity as the endpoint and even packages:

\[
 q_b[f]=\mathcal E[f]-\kappa\|f\|^2
 -\sum_{q=2,3,4,5}w_q\langle f,(\tau_{\log q}+\tau_{-\log q})f\rangle,
 \quad \mathcal E[f]=\int_0^\infty k(r)\|\tau_rf-f\|^2dr,
\]
\[
 k(r)={e^{-r/2}\over1-e^{-2r}},\qquad
 (w_2,w_3,w_4,w_5)=(\log2/\sqrt2,\log3/\sqrt3,\log2/2,\log5/\sqrt5).
                                                               \tag{7}
\]

The common-jump identity is valid on the original two-Mellin kernel,
where q_b=Q_W. Its bounded non-Gamma part has norm <=14, kappa<6,
k(r)<=1/(2r)+1/4, and integral_0^infinity r k(r)dr<5. Thus q_b>=-14 I.
The checker verifies log5+2h0<log7, so no additional prime-power channel
is active anywhere on the stated interval.

For ANY odd physical L2 core function f, the disjoint core/shell Gamma
pairing has the same absolute bound as the even one:

\[
 |\mathcal E(Jf,S_s^o)|\le
 \left({\pi\over\sqrt2}+{5\sqrt2\over4}\sqrt{Bh}\right)\|f\|p.
                                                               \tag{8}
\]

Indeed the reflected core and shell signs change together. Alternatively
take absolute values before the two reflections. The singular same-side
kernel is a restriction of 1/[2(r+z)], whose L2 norm is <=pi/2 by the
weighted Schur integral integral z^-1/2/(r+z) dz=pi r^-1/2. The bounded
same-side kernel contributes (1/4)sqrt(Bh), and the opposite core half
contributes at most sqrt(Bh), since k(B)<1. The physical odd norm is
sqrt(2) times the positive-half norm. This proves (8) on the full L2
spaces, not only bounded or finitely expanded core functions.

At x=B+r the four reflected core samples lie in the disjoint intervals

\[
 (B-\log2,B-\log2+h),\quad
 (\log3-B-h,\log3-B),\quad
 (\log4-B-h,\log4-B),\quad (B-h,B).                            \tag{9}
\]

Odd reflection contributes signs (+,-,-,-). Those signs do not affect
the Cauchy-Schwarz bound on the INPUT intervals:

\[
 \Big\|\sum_q\varepsilon_qw_q f(\xi_q(r))\Big\|_{L^2(0,h)}^2
 \le(\sum_qw_q^2)\sum_q\int_0^h|f(\xi_q(r))|^2dr
 \le\tfrac12(\sum_qw_q^2)\|f\|^2.
\]

After the reflected physical factor two,

\[
                 |q_{\rm prime}(Jf,S_s^o)|
                    \le\sqrt{2\sum_qw_q^2}\,\|f\|p.           \tag{10}
\]

This permits perfectly aligned shell images; it is not an assertion of
orthogonality in the output shell. All four channels, including 5, remain.

To pay the exact moment correction, put d_x=B-|x|. The full Gamma action
of chi_o on the core obeys

\[
 |G_{\chi_o}(x)|
 \le2\cdot47\int_0^{d_x}rk(r)dr+4\cdot10\int_{d_x}^\infty k(r)dr
 \le680+20\log(1/d_x),
\]

using integral_d^infinity k<=log(1/d)/2+21/4 for d<1. Consequently

\[
 \|G_{\chi_o}\|^2\le2(680^2+2\cdot680\cdot20+2\cdot20^2)
 =980800<1000^2,\qquad14\sqrt{200}<200.
\]

Thus the complete nonpole functional has the L2 extension

\[
                           |q_B(f,\chi_o)|\le1200\|f\|.       \tag{11}
\]

The fixed chi_o is not itself declared an admissible Weil source; these
are nonpole pairings. Initially derive the identities on smooth tests;
the displayed bounded kernel/function estimates give the extension to
all L2 core data and agreement on the closed form domains.

Combining (6), (8), (10), (11) gives

\[
 |q_b(Jf,Y_s^o)|\le C_o(h)\|f\|p,
 \quad C_o(h)={\pi\over\sqrt2}+\sqrt{2\sum_qw_q^2}
       +{5\sqrt2\over4}\sqrt{Bh}+720\sqrt h<4.                 \tag{12}
\]

The last inequality is checked by directed logs, pi and integer-square-root
radical bounds at h0. It concerns the entire unbounded-frequency odd core
and the entire profile shell.

## 4. Positive full odd profile shell

Let L=log(2/h), so 46<L0<47. The shell components have width h<log2
and opposite-side distance >2B=log5. Hence every active arithmetic
SELF-correlation of S_s^o vanishes, although the corresponding core/shell
channels in (10) do not vanish. The full Gamma leakage estimate is

\[
 q_b[S_s^o]\ge2(2T(h/2)-\kappa-hk(2B))p^2\ge2(L-8)p^2,
 \quad T(t)=\int_t^\infty k(r)dr.                              \tag{13}
\]

For each component the exterior leakage is at least 2T(h/2) pointwise
by convexity of T. The absolute cross interaction of the two components
is <=2h k(2B)p^2. These bounds apply to either relative reflection sign.
Finally 2T(h/2)>=L-1/2 follows from
k(r)>=1/(2r)-1/4 on (0,1], and k(2B)<1. This proves (13) without
assuming an even reflection or dropping an odd cross term.

For any bounded odd core f, the same absolute kernel integration gives

\[
 |q_b(Jf,S_s^o)|\le\|f\|_\infty\sqrt h\,(L+11)p.              \tag{14}
\]

In detail the reflected bound is log(2/r)+9, whose squared integral
over (0,h) is h[(L+9)^2+2(L+9)+2]<=h(L+11)^2. The four arithmetic
weights are each below one and all have been included.

Since q_B[chi_o]>=-14||chi_o||^2>=-2800, expanding (5) and using (4),
(6), (13), (14) yields

\[
 d_o[s]:=q_b[Y_s^o]\ge[2(L-8)-h(12L+1140)]p^2
                         >(2L-17)p^2>75p^2.                  \tag{15}
\]

Here 12=2(3/5)10 and 1140=12*11+(9/25)*2800. The function
h(12L+1140) is increasing on (0,h0], and at h0 it is <1704*10^-20<1.
This is a complete profile bound. No independent shell trace coordinate
is being set to zero in an unproved larger domain.

## 5. Complete odd Hilbert and form coordinates, and actual H1 gluing

Let K_a^o be the odd physical L2 space with zero H_o moment, and let
W_a^o=K_a^o intersect H1_0((-a,a)). Define F_a^o as the closure of W_a^o
in the full closed nonpole form norm q_a+15||.||^2. This is a closed
form space densely embedded in K_a^o; L2 density follows by odd smooth
compact approximation and correction with a fixed nonzero-moment bump.
The inherited endpoint theorem gives a_o=q_B|_(F_B^o)>=10^-13 I.

Define the full profile form space directly, without any presumed trace:

\[
 F_o=\{s\in L^2(B,b):Y_s^o\in F_b^o\},\qquad d_o[s]=q_b[Y_s^o].
                                                               \tag{16}
\]

The lift has ||Y_s^o||^2=2p^2+|m_s^o|^2||chi_o||^2, so

\[
                2p^2\le\|Y_s^o\|^2\le(2+72h)p^2<4p^2.       \tag{17}
\]

It is a bounded injection with closed Hilbert image. The pullback of the
closed form space F_b^o is therefore closed in its graph norm: a graph
Cauchy sequence Y_(s_n)^o has an L2 limit Y_s^o, by (17), and its form
limit belongs to F_b^o. Interior smooth shell functions give a dense set
in F_o because their corrected lifts are actual odd H1_0 sources.
Inequality (15) holds on F_o. To justify it without an unproved density
restriction, note that S_s^o=Y_s^o+m_s^o chi_o belongs to the full physical
form domain whenever Y_s^o does; the integral leakage inequalities apply
to every such finite-energy S_s^o. Thus d_o is a densely defined positive
closed form, with associated operator D_o>=75 I on L2(B,b).

At Hilbert level the map

\[
 \Psi_o:K_B^o\oplus L^2(B,b)\longrightarrow K_b^o,
                  \qquad\Psi_o(v,s)=Jv+Y_s^o                 \tag{18}
\]

is a bounded bijection with explicit inverse

\[
             s=u|_{(B,b)},\qquad v=u_{\rm core}+m_s^o\chi_o.   \tag{19}
\]

The two half moments cancel exactly by (6). Restriction to the shell
recovers s, and then (19) recovers v, so the kernel is zero. The boundary
degree of freedom is carried by the FULL core; there is no extra C e
coordinate in (18) that could duplicate it.

For N^2=||v||^2+p^2, (17) gives the upper bound below. For the lower bound,
||v||^2<=2||u_core||^2+144h p^2 and 1+144h<4, giving

\[
            \boxed{\tfrac12N^2\le\|\Psi_o(v,s)\|^2\le5N^2.}  \tag{20}
\]

We now prove the full form-domain identity

\[
                  \Psi_o:F_B^o\oplus F_o\ \cong\ F_b^o.       \tag{21}
\]

First J(F_B^o) lies in F_b^o by exact zero extension and passage from
actual H1 source approximants. The profile image lies there by (16).
On the product the form is

\[
 q_b[\Psi_o(v,s)]=a_o[v]+2\operatorname{Re}\langle C_ov,s\rangle+d_o[s],
                         \qquad\|C_o\|\le4,                 \tag{22}
\]

by (12). With E=a_o[v]+d_o[s], (20) and the bound of 4N^2 on the absolute
mixed term give

\[
 E+N^2\le q_b[\Psi_o(v,s)]+20\|\Psi_o(v,s)\|^2
                                      \le E+104N^2.           \tag{23}
\]

The product on the left is complete, and q_b+20||.||^2 is an equivalent
positive graph norm on F_b^o. Therefore the image is form-closed.

It contains every actual odd H1 source. Indeed, for such a u, (19)
has v in internal odd H1(-B,B), with zero H_o moment, and s in H1(B,b),
s(b)=0. The zero extension of this v belongs to F_B^o even if v(B) is
nonzero. To prove this, cut v off at +/-B by odd-compatible ramps, then
restore the small lost positive-half moment using chi_o. Each approximant
is in W_B^o. The cutoff difference has support O(eta), bounded supremum
and total variation uniformly in eta, hence
||tau_r f_eta-f_eta||^2<=C min(r,eta). Its full Gamma energy is
O(eta(1+|log eta|)); the bounded non-Gamma part and small moment correction
also tend to zero. This establishes the core form inclusion.

Similarly, cut s off only near B, preserving s(b)=0, and form the exact
profile Y_(s_eta)^o with its OWN moment m_(s_eta)^o. These lifts are actual
odd H1_0 sources. The same bounded-variation boundary-strip estimate and
vanishing moment difference show convergence to Y_s^o in form norm.
Thus s belongs to F_o. Consequently the image contains W_b^o, whose
form closure is F_b^o. Its already proved closedness gives (21), with
uniqueness and two-sided graph bounds. No parity transfer of the even
coordinate theorem is assumed.

The EXACT preimage of actual sources in (21) is

\[
 \left\{(v,s):\begin{array}{l}
 v\in H^1_{\rm odd}(-B,B),\ \int_{-B}^BvH_o=0,\\
 s\in H^1(B,b),\quad s(b)=0,\quad\boxed{v(B)=s(B)}
 \end{array}\right\}.                                        \tag{24}
\]

The positive core trace is v(B) because chi_o(B)=0; odd reflection
supplies the matching negative trace. Thus (24) is precisely the H1
gluing condition and outer zero trace, in both directions. It imposes
neither separate core zero trace nor any new Mellin condition.

## 6. Canonical odd endpoint low space, full tail and moment normalization

Let U_B f(x)=sqrt(2B) f(Bx) be the physical isometry to
H_ref=L2((-1,1),dx/2). In its odd sector, set X_o=P_1-perp and

\[
 L_o=\operatorname{span}\{P_3,P_5,\ldots,P_{63}\},\quad\dim L_o=31,
 \qquad Y_o=\overline{\operatorname{span}\{P_{65},P_{67},\ldots\}}.
                                                               \tag{25}
\]

The unnormalized P_n have norm squared 1/(2n+1), and J_nn=1/(2n+1).
For m_o(x)=sinh(Bx/2), the exact reference moment map is

\[
 \mathcal M_ox=x-{\langle x,m_o\rangle\over\langle P_1,m_o\rangle}P_1,
                           \quad x\in X_o.                   \tag{26}
\]

It maps onto the odd moment kernel. Its inverse deletes the P1
coefficient. The reference form domain is the harmonic-diagonal domain
intersected with L2(V dx/2), V=-log(1-x^2)/2; the finite moment correction
and finite Legendre projections preserve it. The canonical endpoint
estimates apply there, hence on the physical core F_B^o. In particular
the finite images M_o P_i are internal H1 and belong to F_B^o by the
cutoff argument above; subtracting them gives the full domain split of
every core source into (25). No completion larger than the proved source
form space is silently identified with it.

The endpoint package proves, with the following explicit bounds,

\[
 \|\mathcal M_ox\|^2\le(1+\beta_o)\|x\|^2<2\|x\|^2,
 \quad\beta_o=\left[{(B/2)^2\over6(1-(B/2)^2/20)}\right]^2,
\]
\[
 \epsilon_{m,o}={4\over B}\,
 {(B/2)^{65}\over65!\,[1-(B/2)^2/(66\cdot67)]},\qquad
 \|\mathcal M_oy\|^2\le(1+\epsilon_{m,o}^2)\|y\|^2\quad(y\in Y_o).
                                                               \tag{27}
\]

The second inequality uses that the moment correction is in the P1
direction, orthogonal to the entire Y_o. It uses the operator-norm bound
epsilon_(m,o) for that correction, not a bound on a differently normalized
P1 coefficient.

Let epsilon_G be the pinned rational uniform error for the degree-64
regular Gamma polynomial p_G. Let M_o^0 equal M_o on L_o and I on Y_o.
The complete bounded form error is

\[
 e_o=2(2B)\epsilon_G+80\epsilon_{m,o},\qquad
 \|\mathcal M_o^*q_B\mathcal M_o-(\mathcal M_o^0)^*q_B^{p_G}\mathcal M_o^0\|
                                                              \le e_o.
                                                               \tag{28}
\]

Writing q0=-log(2*pi*B)-gamma and H_65=sum_(k=1)^65 1/k, the tail floor is

\[
 \delta_o=H_{65}+q_0-2B(1/4-g(2B)+\epsilon_G)
              -(\log2+\log3/\sqrt3+\log2/2)-e_o,
\]
\[
 a_o[U_B^{-1}\mathcal M_oy]\ge\delta_o\|y\|^2,\qquad
              \delta_o=0.734833243834667563796423\ldots.        \tag{29}
\]

The checker independently reconstructs these constants and requires the
directed enclosure to equal the canonical `odd_tail_floor` rational
endpoints. Thus space, parity, norm and provenance are pinned. In physical
tail norm the conservative floor is
underline(delta_o)/(1+overline(epsilon_(m,o))^2)>734/1000. It is not a
floor on an arbitrary complement of a selected near-null vector.

## 7. Complete odd low/profile and high/profile comparisons

For an odd degree i, |P_i|<=1. Put c=B/2<1/2. The positive Taylor series
shows sinh(t)/t increases for positive t, and the checker verifies
sinh(1/2)/(1/2)<6/5. Therefore the exact ratios in (26) satisfy

\[
 |r_i|={|\langle P_i,\sinh(cx)\rangle|\over\langle x,\sinh(cx)\rangle}
 \le{(6/5)c\int_0^1x\,dx\over c\int_0^1x^2\,dx}
                                      ={9\over5}<2.           \tag{30}
\]

For l=sum_(i=3,5,...,63) c_i P_i this gives the PHYSICAL supremum bound

\[
 \|U_B^{-1}\mathcal M_ol\|_\infty^2
 \le{9\over2B}\sum_{i=3,5,\ldots,63}(2i+1)\,\|l\|^2
 ={9\cdot2077\over2B}\|l\|^2<110^2\|l\|^2.                  \tag{31}
\]

Use (14) for the direct shell pairing, and (6), (11), (27) for the exact
moment correction, with ||M_o l||<2||l||. Then

\[
 |q_b(U_B^{-1}\mathcal M_ol,Y_s^o)|
 \le\sqrt h\,[110(L+11)+1440]\|l\|p
 \le b_o\|l\|p,\qquad b_o=7820\,10^{-10}.                    \tag{32}
\]

The coefficient 1440=(3/5)*1200*2 pays the whole correction. The function
h[110(L+11)+1440]^2 increases with h since its bracket exceeds 220;
its endpoint bracket is <7820. No upper bound on L independent of h
has been falsely imposed.

For the entire y in Y_o use the L2 estimate (12), not a polynomial
supremum bound:

\[
 |q_b(U_B^{-1}\mathcal M_oy,Y_s^o)|
 \le4\sqrt{1+\epsilon_{m,o}^2}\|y\|p<{41\over10}\|y\|p.       \tag{33}
\]

Young's inequality pays this complete mixed block as

\[
 2(41/10)\|y\|p\le{1681\over6000}\|y\|^2+60p^2.
\]

The remaining diagonal floors are

\[
         \delta_{o,*}=\underline\delta_o-1681/6000>0.454,
                         \qquad75-60=15.                     \tag{34}
\]

## 8. Exact finite Schur certificate with the entire infinite core Gram

Let A^0 be the 31-by-31 model moment matrix
A^0_ij=q_B^(p_G)[M_o P_i,M_o P_j], i,j in {3,5,...,63}.
Let C_T be the ACTUAL low-to-full-Y_o coupling of M_o* q_B M_o.
The endpoint mixed-tail theorem and (28) give

\[
 A_{\rm actual}\succeq A^0-e_oJ,\qquad
 C_T^*C_T\preceq G_{o,\rm act}:={1001\over1000}G_o+1001e_o^2J.
                                                               \tag{35}
\]

G_o is the exact model Gram after moment congruence on BOTH indices.
For clarity, before that congruence it is the Gram of
P_(Y_o)(V-K_(p_G)-S)P_i. Its formula contains the exact full integrals

\[
 \langle VP_i,VP_j\rangle+\langle SP_i,SP_j\rangle
       -\langle VP_i,SP_j\rangle-\langle SP_i,VP_j\rangle,
\]

minus the projection onto P1,P3,...,P63, followed by the exact K terms

\[
 \sum_{k=65,67,\ldots,127}(2k+1)
 [K_{ik}K_{kj}-(V_{ik}-S_{ik})K_{kj}-K_{ik}(V_{kj}-S_{kj})].
                                                               \tag{36}
\]

The Gamma polynomial image has degree <=j+65<=128; its odd coefficients
therefore stop at degree 127 exactly. This is the only reason that last
sum is finite. The V and all shifted images retain their ENTIRE infinite
tails through their exact integrated products. The shift-band engine
sums all active signed shifts before squaring, so it retains all mixed
prime channels and both shift signs. All Gamma/shift signs in (36) are
retained. These calculations use rational polynomial recurrences and
analytic logarithmic moments with directed constants, without quadrature.

Let C_P denote the ACTUAL low-to-profile L2 representative from (32),
so ||C_P||<=b_o. By (15), (29), (33)-(35), the physical form at x=l+y
dominates the following specific continuous three-block comparison:

\[
\begin{aligned}
\mathcal Q_o[l,y,s]={}&(A^0-e_oJ)[l]
 +2\operatorname{Re}\langle C_Tl,y\rangle+\delta_{o,*}\|y\|^2\\
 &+2\operatorname{Re}\langle C_Pl,s\rangle+15\|s\|^2.
\end{aligned}                                                   \tag{37}
\]

The high/profile term has been paid in (34). Both remaining off-diagonal
maps are the actual ones. Completing the square of THIS comparison gives
the finite sufficient lower matrix

\[
 R_{o,\rm cmp}=A^0-e_oJ-{G_{o,\rm act}\over\delta_{o,*}}
                          -{7820^2\over15\,10^{20}}J.          \tag{38}
\]

All 31 directed rational LDL pivots are strictly positive. The trace
bound on the inverse normalized matrix yields

\[
 R_{o,\rm cmp}\succeq\sigma_oJ,\qquad
 \sigma_o={1\over\overline{\operatorname{tr}(JR_{o,\rm cmp}^{-1})}}
                                      >4.872\,10^{-10}.        \tag{39}
\]

The inverse trace uses directed triangular solves; positivity is not
inferred from numerical eigenvalues or approximate eigenvectors. No odd
source-selection iteration is run. All 31 pivots and the inverse-trace
bound are recorded in the JSON/log.

The exact square-completion map for (37) is

\[
 (l,y,s)\longmapsto
 (l,y+\delta_{o,*}^{-1}C_Tl,\ s+15^{-1}C_Pl).
\]

Its inverse norm is <=1+r_o, where BOTH off-diagonal maps are paid by

\[
 r_o^2\le{\operatorname{tr}(J^{-1}G_{o,\rm act})\over\delta_{o,*}^2}
                            +{7820^2\over15^2\,10^{20}}.       \tag{40}
\]

Consequently on the complete core/profile product,

\[
 q_b[U_B^{-1}\mathcal M_o(l+y)+Y_s^o]\ge\mathcal Q_o[l,y,s]
 \ge{\min(\sigma_o,\delta_{o,*},15)\over(1+r_o)^2}
                         (\|l\|^2+\|y\|^2+p^2).              \tag{41}
\]

This is the exact shear of a proved DOMINATED COMPARISON form. It is
not identified with an approximate inverse of the actual tail or shell
operator. Coercivity transfers to the physical form by the first inequality
in (41); no substitution into an actual inverse identity is made.
Failure of (38) would only be UNDECIDED for the actual form. Here the
comparison succeeds with positive reserve.

## 9. Physical odd gap and the actual complete odd Schur operator

The global moment norm (27) and profile norm (17) give

\[
 \|U_B^{-1}\mathcal M_ox+Y_s^o\|^2
 \le(\sqrt2\|x\|+2p)^2
 \le6(\|x\|^2+p^2).                                         \tag{42}
\]

Thus (41) yields the fully paid physical constant

\[
 \gamma_o={\min(\sigma_o,\delta_{o,*},15)\over6(1+r_o)^2}
                    >1.55\,10^{-12}>10^{-12}.                 \tag{43}
\]

The checker verifies the conservative published bound gamma_o>10^-12
directly with rational endpoints. Factor 6 pays the entire moment-map
norm and the profile lift together, including overlap on the core. An
additional 1+beta_o division is neither omitted nor needed. We start
from the endpoint matrices and exact moment map, not an old final gap
whose earlier normalization is being undone.

The exact form-space statement (21) and actual H1 preimage (24) now
prove (1) for all actual odd sources on the whole interval, including
h=h0. In fact it holds on the complete F_b^o.

Let A_o be the self-adjoint operator of a_o on the entire odd core
K_B^o. Let D_o be the operator of (16) on the entire right-profile L2
space, and C_o the bounded operator in (22). By (20) and (43), the full
block form is at least

\[
       {1\over2\,10^{12}}(\|v\|^2+\|s\|^2).
\]

Infimizing over the COMPLETE F_o uses the actual Riesz response
D_o^-1 C_o v, which exists since D_o>=75 I. Therefore

\[
 R_o[v]=a_o[v]-K_o[v]\ge\sigma_{o,*}\|v\|^2,
 \quad\sigma_{o,*}=1/(2\,10^{12}),\quad K_o=C_o^*D_o^{-1}C_o.
\]

Furthermore (12), (15) imply 0<=K_o<=K_* I, where
K_*=16/75. Hence K_o<=(K_*/sigma_(o,*))R_o and

\[
 K_o\preceq {16/75\over16/75+1/(2\,10^{12})}\,a_o,
 \quad\Theta_o\le{16/75\over16/75+1/(2\,10^{12})}<1-2\,10^{-12}.
                                                               \tag{44}
\]

This is a FULL operator bound, not merely separate low and high block
bounds. The form a_o>=10^-13 I defines A_o^-1/2 on the entire core,
and all shell modes were included in the preceding infimum. It proves
(3) in exactly the stated nonredundant coordinates.

## 10. All-parity corollary with exactly the original two moments

Reflection Ru(x)=u(-x) is a unitary self-adjoint involution preserving
the full-line Gamma form, the scalar term and each paired shift in (7).
Thus q_b(Rf,Rg)=q_b(f,g). Its projections

\[
                       u_e=(u+Ru)/2,\qquad u_o=(u-Ru)/2
\]

preserve H1_0 and the closed physical form domain. Because
E_+(Ru)=E_-(u) and E_-(Ru)=E_+(u), the original common kernel is
preserved by BOTH projections. Equivalently its cosh and sinh moment
components are precisely the sum and difference of the two original
Mellin functionals divided by two. There are no new source constraints.

For an original admissible u, therefore, u_e and u_o are admissible in
their respective parity sectors. Reflection invariance and opposite
reflection eigenvalues give q_b(u_e,u_o)=0; L2 orthogonality gives

\[
 q_b[u]=q_b[u_e]+q_b[u_o],\qquad
                 \|u\|^2=\|u_e\|^2+\|u_o\|^2.               \tag{45}
\]

The reproduced even theorem at `7741eca...` supplies gap 3*10^-15,
and (1) supplies the larger odd gap 10^-12. At least one component of a
nonzero u is nonzero. Equations (45) consequently imply the STRICT
all-parity bound (2). This is the first use of the even theorem in
the odd-to-all-parity argument; it was not used to establish odd positivity.

For smaller positive windows, ordinary physical zero extension of actual
H1_0 sources is isometric, preserves both Mellin conditions, and preserves
every full-line correlation and Gamma term. Applying (2) at B+h0 yields
the same constant for every 0<b<=B+h0. This uses the established exact
window identity, not parameter continuity or an iteration conjecture.

## 11. Certificate evidence and append-only status

The checker makes 51 new exact checks, binds 81 input files, reproduces the complete even-width
certificate (41 checks) and its 38/40/31/28/43/9 inherited chain, and
independently recomputes the odd endpoint matrices and the entire infinite
coupling Gram. It verifies the new corrector, parity-specific moment
costs, shell floor, all 31 comparison pivots, both shear contributions,
physical norm conversion, full odd Schur norm, and the exact two-moment
parity arithmetic. All decisions use integers/Fractions and outward
intervals on the pinned grid 10^-200.

The even replay and odd computation are independent local processes;
the stored result requires both to succeed. No results are inferred from
timing or concurrency. `--verify` requires byte-identical JSON and log,
and checks the seven payload hashes. The eighth package file SHA256SUMS
lists those seven files and does not purport to hash itself. The odd
endpoint trial-source selection is not repeated or used as a proof.

Analytic form closure, source gluing, Carleman bounds, exact infinite
Gram identities and reflection invariance are proved above or imported
with the indicated provenance. Successful arithmetic reproduction does
not constitute an independent external audit or a formal proof assistant
verification. Status remains AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.

This package appends eight files, and the transport ladder receives a
separate strictly appended status section. Its historical text and the
concurrent `cb56df6` Even-status addition remain intact. The new local
front is a quantitatively larger or iteratable all-parity window, with
its new constants and domains still to be proved. No later global or
Object-X stage is promoted. main remains the frozen PR-#137 milestone;
there is no new PR or merge.
