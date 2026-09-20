# Moving-endpoint uniform high-tail renewal through half-width one

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `b1c01860fef2a960cae57634041f75b29d37f836`.
This package addresses one precise obligation in MOVING-ENDPOINT BLOCK-ADAPTIVE
RESERVE RENEWAL: a high-tail floor which can be rebuilt at every already
reached endpoint without paying the tiny global All-Source gap.

It does not close the moving finite Low block, moving Low/High or Low/Profile
mixed blocks, non-summable transport, channel-7 endpoint positivity, Connected
Unit-Window Coercivity, Strong Terminal, C1-GEOM, Object X or RH.

## 1. Statement

Let

\[
 B={\log5\over2}\le a\le1.
\]

On the reference Hilbert space
\(H=L^2((-1,1),d\xi/2)\), let \(P_n\) be the ordinary Legendre polynomials.
For parity \(p=0,1\), let

\[
 Y_0=\overline{\mathrm{span}}\{P_{384},P_{386},\ldots\},\qquad
 Y_1=\overline{\mathrm{span}}\{P_{385},P_{387},\ldots\},
\]
intersected with the reference form domain. Let

\[
 m_0(\xi)=\cosh(a\xi/2),\qquad m_1(\xi)=\sinh(a\xi/2)
\]
and define on the complement of the moment carrier \(P_p\)

\[
 \mathcal M_{p,a}y
 =y- {\langle y,m_p\rangle\over\langle P_p,m_p\rangle}P_p.
\]

Then for every \(y\in Y_p\), uniformly for every \(B\le a\le1\),

\[
\boxed{
q_a[U_a^{-1}\mathcal M_{p,a}y]
>{1\over41}\,\|U_a^{-1}\mathcal M_{p,a}y\|_2^2.
}
\tag{1}
\]

Thus a moving-endpoint block-adaptive decomposition may choose a **fixed**
reference cutoff with only 191 low coordinates in each parity:

\[
L_0=\mathrm{span}\{P_2,P_4,\ldots,P_{382}\},\qquad
L_1=\mathrm{span}\{P_3,P_5,\ldots,P_{383}\}.
\tag{2}
\]

The complete complement after exact moment reconstruction has the uniform
physical floor (1). No global physical gap enters this floor.

## 2. Uniform reference form on the moving band

The universal active-set theorem gives, in each parity and for every
\(B\le a\le1\),

\[
q_a=D_H+V+q_0(a)I-K_a-S_a,
\tag{3}
\]
where

\[
D_HP_n=H_nP_n,\qquad V=-\tfrac12\log(1-\xi^2)\ge0,
\]

\[
q_0(a)=-\log(2\pi a)-\gamma,
\]
and \(K_a\) is the bounded regular Gamma operator. All possible active
prime-power channels on this band are

\[
2,3,4,5,7.
\]
Channel 8 remains inactive because \(\log8>2\). An inactive channel may be
included with zero overlap.

The inherited proof gives \(g'(t)<0\) for \(0<t\le2\) and \(g(0+)=1/4\). Positivity on the full interval follows as well: at \(t=2\), \(g(2)>0\) is equivalent to \(4e^3>e^4-1\), which is immediate from the elementary series bound \(e<3<4\). Hence \(0<g(t)\le1/4\) on \(0<t\le2\). By Schur's test this gives

\[
\|K_a\|\le{a\over2}\le{1\over2}.
\tag{4}
\]

For a partial translation \(T_d\), \(\|T_d\|\le2\) always. If \(d\ge1\),
the two output branches are disjoint and \(\|T_d\|\le1\). On our endpoint
band the only shift which can have \(d<1\) is q=2; q=3,4,5,7 all have
\(\log q/a>1\) whenever they are active. Therefore

\[
\|S_a\|\le2w_2+w_3+w_4+w_5+w_7.
\]

Directed logarithm and radical witnesses give

\[
 w_2<{1\over2},\quad
 w_3<{11\over17},\quad
 w_4<{7\over20},\quad
 w_5<{161\over220},\quad
 w_7<{10\over13},
\]
so exactly

\[
2w_2+w_3+w_4+w_5+w_7
<{85039\over24310}<{7\over2}.
\tag{5}
\]

The pinned Euler-gamma enclosure and \(\pi<22/7\) give uniformly

\[
\log(2\pi a)+\gamma<\log(44/7)+3/5<19/10+3/5={5\over2}.
\tag{6}
\]

## 3. Raw harmonic tail floor

For \(y\in Y_0\) or \(Y_1\), the harmonic diagonal obeys

\[
\langle y,D_Hy\rangle\ge H_{384}\|y\|^2.
\]
The potential V is nonnegative. Equations (4)--(6) therefore imply

\[
q_a[y]
>\left(H_{384}-{5\over2}-{1\over2}-{7\over2}\right)\|y\|^2
=\left(H_{384}-{13\over2}\right)\|y\|^2.
\tag{7}
\]

The rational harmonic sum satisfies

\[
H_{384}>{261\over40},
\]
hence

\[
\boxed{q_a[y]>{1\over40}\|y\|^2.}
\tag{8}
\]

This estimate already includes channel 7 through the uniform bound (5).
It uses neither an endpoint matrix nor any existing tiny All-Source gap.

## 4. Exact Mellin correction costs uniformly less than 10^-6

The high Legendre modes are orthogonal to every lower Taylor monomial.
The standard moment-tail estimate used in the endpoint packages therefore
gives, with \(a/2\le1/2\),

\[
\|\mathcal M_{0,a}y-y\|
\le\epsilon_0\|y\|,
\]

\[
\epsilon_0\le
{(1/2)^{384}\over384!\,[1-1/(4\cdot385\cdot386)]},
\tag{9}
\]
and, using \(4/a<5\),

\[
\|\mathcal M_{1,a}y-y\|
\le\epsilon_1\|y\|,
\]

\[
\epsilon_1\le
5{(1/2)^{385}\over385!\,[1-1/(4\cdot386\cdot387)]}.
\tag{10}
\]

Both are far below \(10^{-6}\); the checker verifies this using exact
Fractions.

It remains to pay the energy of the P0/P1 correction. Write e=P_p and
z=\mathcal M_{p,a}y-y=-ce. Since y is orthogonal to e,

\[
q_a(y,e)=\langle y,(V-K_a-S_a)e\rangle.
\]

A direct elementary bound is enough. Since |P_p|<=1,

\[
\|VP_p\|\le\|V\|<2,
\]
where

\[
\|V\|^2
\le{1\over2}\left(\int_0^1\log^2(1-x)dx
                   +\int_0^1\log^2(1+x)dx\right)<{3\over2}.
\]
Relative to \(\|P_p\|\), the ratio is <4 for p=0,1. Together with
(4)-(5),

\[
|q_a(y,e)|<8\|y\|\|e\|.
\tag{11}
\]

Also

\[
{|q_a[e]|\over\|e\|^2}<12,
\tag{12}
\]
by \(H_p\le1\), the same V bound, (4)-(6), and (5). If
\(\epsilon=\max(\epsilon_0,\epsilon_1)<10^{-6}\), then

\[
q_a[\mathcal M_{p,a}y]
\ge q_a[y]-16\epsilon\|y\|^2-12\epsilon^2\|y\|^2
>{1\over40}\|y\|^2-{1\over50000}\|y\|^2.
\tag{13}
\]

Moreover orthogonality gives

\[
\|\mathcal M_{p,a}y\|^2\le(1+\epsilon^2)\|y\|^2.
\tag{14}
\]
The rational comparison of (13)-(14) yields (1).

## 5. Meaning for moving-endpoint reserve renewal

This closes one of the moving-endpoint obligations independently of the
soft global gap:

\[
\boxed{
\text{the complete moving high tail can always be renewed with floor }1/41
\text{ on }B\le a\le1.
}
\]

The cost is that the fixed low block is larger than at B: its dimension is
191 in each parity rather than 31. That finite block, its moving Low/High and
Low/Profile couplings, and the rank-two/remainder data of the block-adaptive
profile map remain to be certified as functions of a.

The result therefore changes the next gate from an infinite-dimensional tail
problem to a finite-but-larger moving low-block problem. It does not prove that
the 191-dimensional block remains positive up to a=1, and it does not imply a
non-summable endpoint chain.

## 6. Scope firewall

Closed here:

* endpoint-uniform high-tail coercivity on B<=a<=1;
* both parities and exactly the original two Mellin conditions;
* all possible channels 2,3,4,5,7 paid uniformly;
* fixed moving low dimension 191 per parity;
* no dependence of the high-tail floor on the global All-Source gap.

Still open:

* positivity/conditioning of the moving 191-dimensional low block;
* moving Low/High and Low/Profile mixed terms and operator remainder;
* a moving block-adaptive restart law;
* non-summable transport and actual arrival at log(7)/2;
* Connected Unit-Window Coercivity, Strong Terminal, full C1-GEOM,
  Object X, global Weil positivity and RH.
