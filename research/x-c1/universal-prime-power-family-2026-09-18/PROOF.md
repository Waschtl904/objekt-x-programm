# X-C1 UNIVERSAL PRIME-POWER FAMILY

**Date:** 2026-09-18  
**Status:** AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN  
**Parent:** PR #137 head a18f90a867bfba2798068d5566a4e38a09013c01.  
**Scope:** structural theorem only. No new positive endpoint beyond a=log(2).

## Theorem

Put
\[
H=L^2((-1,1),d\mu),\qquad d\mu=d\xi/2,\qquad
(U_au)(\xi)=\sqrt{2a}\,u(a\xi).
\]
For
\[
\mathcal W_a=H^1_0((-a,a))\cap\ker E_+\cap\ker E_-,
\qquad
E_\pm u=\int_{-a}^a u(x)e^{\pm x/2}dx,
\]
the connected Weil form is transported to
\[
\boxed{
q_a=D_H+V+q_0(a)I-K_a-
\sum_{\substack{q=p^k\\ \log q<2a}}
\frac{\Lambda(q)}{\sqrt q}\,T_{\log q/a}.
}
\tag{U}
\]
Here
\[
D_HP_n=H_nP_n,\quad
V(\xi)=-\tfrac12\log(1-\xi^2),\quad
q_0(a)=-\log(2\pi a)-\gamma,
\]
\[
(K_af)(\xi)=2a\int_{-1}^1g(a|\xi-\eta|)f(\eta)d\mu(\eta),
\quad
g(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t},
\]
and
\[
(T_df)(\xi)=f(\xi+d)1_{\xi+d<1}+f(\xi-d)1_{\xi-d>-1}.
\tag{1}
\]
At \(d=2\), \(T_2=0\) a.e.

For \(0<a\le b\), physical zero extension induces
\[
(J_{a,b}f)(\xi)=
\sqrt{\frac ba}\,f\!\left(\frac ba\xi\right)1_{|\xi|<a/b},
\tag{2}
\]
and
\[
\boxed{q_b[J_{a,b}f]=q_a[f]},
\qquad
\boxed{
M_{b,\pm}(J_{a,b}f)=\sqrt{\frac ab}\,M_{a,\pm}(f)
},
\tag{3}
\]
where
\[
M_{a,\pm}(f)=\int_{-1}^1 f(\xi)e^{\pm a\xi/2}d\mu.
\]

Together with the parent ACTIVE-SET SEGMENT-SCHUR theorem, (U) has one prime-label-independent complete low/tail Gram interface for every finite active prime-power set and every shift length \(0<d<2\).

## 1. Unitary scaling and the two moments

Direct substitution gives
\[
\|U_au\|_H^2
=\frac12\int_{-1}^1 2a|u(a\xi)|^2d\xi
=\|u\|_{L^2(-a,a)}^2.
\]
Also
\[
(U_au)'=a\sqrt{2a}\,u'(a\xi),
\qquad
\|(U_au)'\|_H^2=a^2\|u'\|_2^2,
\]
so \(H^1_0\) and zero traces are preserved. Finally
\[
E_\pm u=\sqrt{2a}\,M_{a,\pm}(U_au).
\tag{4}
\]
Thus there remain exactly two Mellin conditions.

## 2. Exact derivation of (U)

The scaled connected nonpole identity is
\[
\begin{aligned}
q_a[f]
={}&2a\int_{\xi<\eta}
h(a(\eta-\xi))|f(\eta)-f(\xi)|^2d\mu d\mu\\
&+\int
\left[
H_\Gamma(a(1+\xi))+H_\Gamma(a(1-\xi))-\kappa
\right]|f(\xi)|^2d\mu\\
&-\sum_{\log q<2a}w_q\langle f,T_{\log q/a}f\rangle,
\end{aligned}
\tag{5}
\]
where
\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
H_\Gamma(s)=\int_s^\infty h(t)dt,\quad
\kappa=\log(8\pi)+\gamma+\pi/2.
\]
The factor \(2a\) follows from
\(dx\,dy=4a^2d\mu d\mu\) and
\(|u(y)-u(x)|^2=(2a)^{-1}|f(\eta)-f(\xi)|^2\).

For \(q=p^k\), the centered physical prime term is
\[
w_q(\|K_{\log q}u\|^2-2\|u\|^2)
=
-w_q\langle u,(\tau_{\log q}+\tau_{-\log q})u\rangle,
\]
and
\[
U_a(\tau_\ell+\tau_{-\ell})U_a^{-1}=T_{\ell/a}.
\]
Hence
\[
w_q=\frac{\Lambda(q)}{\sqrt q}
=\frac{\log p}{p^{k/2}},
\tag{6}
\]
so in particular \(w_4=\log2/2\).

Now split \(h(t)=1/(2t)+g(t)\). The singular part is
\[
\int_{\xi<\eta}
\frac{|f(\eta)-f(\xi)|^2}{\eta-\xi}d\mu d\mu
=\langle f,D_Hf\rangle.
\tag{7}
\]
The regular difference part equals
\[
\int d_a(\xi)|f(\xi)|^2d\mu-\langle f,K_af\rangle,
\]
with
\[
d_a(\xi)=
\int_0^{a(1+\xi)}g(t)dt+
\int_0^{a(1-\xi)}g(t)dt.
\tag{8}
\]
Set
\[
F(s)=H_\Gamma(s)+\int_0^s g(t)dt.
\]
Since \(F'(s)=-1/(2s)\) and
\(F(s)=\log2+\pi/4-\frac12\log s\),
\[
d_a(\xi)+H_\Gamma(a(1+\xi))+H_\Gamma(a(1-\xi))-\kappa
=
V(\xi)+q_0(a).
\tag{9}
\]
Equations (5)--(9) prove (U), including every factor.

## 3. Partial shifts and the cutoff firewall

Write
\[
R_d^+f(\xi)=f(\xi+d)1_{\xi+d<1},\qquad
R_d^-f(\xi)=f(\xi-d)1_{\xi-d>-1}.
\]
A change of variables gives
\[
(R_d^+)^*=R_d^-,
\]
hence
\[
T_d=R_d^++R_d^-
\]
is bounded and self-adjoint for every \(0<d<2\). Each branch is a partial isometry, so \(\|T_d\|\le2\). For \(1\le d<2\), the two active endpoint bands are disjoint and \(T_d\) swaps them; therefore
\[
\|T_d\|=1.
\tag{10}
\]
At \(d=2\), the overlap has measure zero and \(T_2=0\). Thus
\[
T_d\not\to T_2
\quad\text{in }L^2\text{-operator norm as }d\uparrow2.
\tag{11}
\]
No right-neighborhood positivity may be inferred from false operator-norm continuity.

## 4. Finite active set

For fixed \(a\),
\[
\mathcal A_a=\{q=p^k:\log q<2a\}
\subset\{2,\ldots,\lfloor e^{2a}\rfloor\},
\]
so the prime-power sum in (U) is finite. At \(\log q=2a\), \(d_q=2\) and \(T_{d_q}=0\); using \(<\) or \(\le\) gives the same form.

## 5. Exact zero-extension functoriality

Let \(E_{a,b}\) be physical zero extension and define
\[
J_{a,b}=U_bE_{a,b}U_a^{-1}.
\]
This is exactly (2), isometric on \(H\), and
\[
J_{b,c}J_{a,b}=J_{a,c}.
\tag{12}
\]
Substitution \(\zeta=(b/a)\xi\) gives the moment law in (3).

For the form, \(E_{a,b}u\) is the same compactly supported real-line function as \(u\), so the physical Weil form is unchanged:
\[
Q_W[E_{a,b}u]=Q_W[u].
\]
Transport by \(U_a,U_b\) gives the first identity in (3).

Equivalently, every newly admitted prime power with
\(2a<\log q\le2b\) has disjoint translated copies of the support, hence
\[
\|K_{\log q}u\|^2=2\|u\|^2,
\]
so its centered contribution is zero. This is the exact cutoff cancellation.

## 6. Uniform tail/Parseval interface

Fix a bounded endpoint \(B\), one parity, a finite low Legendre space \(Z\), and \(Y=Z^\perp\). With a polynomial-kernel model \(K_B^p\), put
\[
C_{\rm op}
=
V-K_B^p-\sum_{q\in\mathcal A_B}w_qT_{d_q(B)}.
\]
The parent ACTIVE-SET SEGMENT-SCHUR theorem proves for arbitrary \(0<d,e<2\)
\[
\langle P_i,T_dP_j\rangle
=
\frac12\sum_{\sigma=\pm1}
\int_{I_\sigma(d)}P_i(x)P_j(x+\sigma d)dx,
\tag{13}
\]
\[
\langle T_dP_i,T_eP_j\rangle
=
\frac12\sum_{\sigma,\tau=\pm1}
\int_{I_\sigma(d)\cap I_\tau(e)}
P_i(x+\sigma d)P_j(x+\tau e)dx,
\tag{14}
\]
plus exact logarithmic/shift cross moments. Therefore
\[
\boxed{
G_{il}
=
\langle P_YC_{\rm op}P_i,P_YC_{\rm op}P_l\rangle
}
\tag{15}
\]
is obtained by complete Parseval subtraction, including every mixed prime/prime, logarithmic/prime, and Gamma-polynomial/prime term. The \(V\) and partial-shift tails are not replaced by truncated mode sums.

The parent checker gives 381/381 exact Fraction identities across both \(d<1\) and \(d>1\).

## 7. Closed structural obligations

1. Unitary scaling: §1.  
2. Exact derivation of every term and factor in (U): §2.  
3. Self-adjoint partial shifts: §3.  
4. Exact zero-extension intertwining and moment transport: §5.  
5. Finite active prime-power sum: §4.  
6. Uniform complete tail/Parseval interface: §6.  
7. Entrance \(d_q=2\) without false \(L^2\)-norm continuity: §§3--5.

So the universal prime-power family is a theorem-level structural gate within the author-derived program.

## Scope firewall

This theorem proves no positive reserve for all active sets and no new endpoint at \(\log5/2\), \(\log7/2\), or \(1\). It is not full C1-GEOM, Object X, or RH. Future endpoint failure is failure of that positive-gap certificate instance, not a need for a new prime-specific operator family.
