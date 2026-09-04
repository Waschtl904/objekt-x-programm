# P11 R43 — flag-tightness, terminal partial cocycle, and sign hardening

Date: 2026-09-03

## Purpose

Harden the B-TIGHT / B-SIGN front after the multi-model review of mathematical head
`366c5e3dcdd2b2f16bf8b2663c0284a4db9538f5`.

This module is part of the R43 candidate mathematics.  It creates no freeze, no formal
independent-GREEN booking, no `✓[M]`, no Strong-Terminal/C6 closure, and no Object-X/RH
promotion.

---

## 1. Primary B-TIGHT gate is flag tightness, not finite jet energy

Let
\[
h_U=\sum_{n\ge1}c_{n,U}e_{S,n}\in H_S^0,
\qquad
h_U\rightharpoonup0,
\]
and let
\[
\mathcal H_S^{[m]}
=\overline{\operatorname{span}}\{e_{S,n}:n\ge m\},
\qquad
P_S^{[m]}:=P_{\mathcal H_S^{[m]}}.
\]
Then exactly
\[
\boxed{
\|P_S^{[m]}h_U\|^2
=\sum_{n\ge m}|c_{n,U}|^2.
}
\tag{R43.FT1}
\]
Therefore the canonical ONB tail criterion R43.57 is equivalently
\[
\boxed{
\textbf{B-FLAGTIGHT:}
\qquad
\lim_{m\to\infty}
\limsup_{U\to\infty}
\|P_S^{[m]}h_U\|
=0.
}
\tag{R43.FT2}
\]
This is the exact primary B-TIGHT formulation.

A warning about quantifiers is necessary.  The stronger statement
\[
\exists U_0:\qquad
\lim_{m\to\infty}
\sup_{U\ge U_0}\|P_S^{[m]}h_U\|=0
\tag{R43.FT3}
\]
is sufficient, but it is not silently identified with R43.FT2 unless additional uniformity
on the whole fixed tail is proved.  The exact asymptotic criterion remains R43.FT2.

The jet-number energy identity from R43.59e0 is
\[
\langle N_Sh,h\rangle
=\sum_{m\ge1}\|P_S^{[m]}h\|^2.
\tag{R43.FT4}
\]
Hence the uniform energy estimate
\[
\sup_{U\ge U_0}\langle N_Sh_U,h_U\rangle<\infty
\tag{R43.FT5}
\]
implies
\[
M\,\|P_S^{[M]}h_U\|^2
\le
\sum_{m=1}^{M}\|P_S^{[m]}h_U\|^2
\le C,
\]
so
\[
\boxed{
\sup_{U\ge U_0}\|P_S^{[M]}h_U\|^2\le \frac{C}{M}.
}
\tag{R43.FT6}
\]
Thus finite jet energy is a convenient sufficient tool, but it is strictly stronger than
B-FLAGTIGHT.

Indeed the abstract orbit
\[
h_U=(\log U)^{-1/2}e_{S,\lceil(\log U)^2\rceil}
\]
satisfies \(\|h_U\|\to0\), hence B-TIGHT, while
\[
\langle N_Sh_U,h_U\rangle
\asymp \log U\to\infty.
\tag{R43.FT7}
\]
No inference
\[
\text{failure of R43.FT5}\Longrightarrow\text{failure of B-TIGHT}
\]
is permitted.

More flexible sufficient targets include any profile
\[
\lim_{m\to\infty}\limsup_{U\to\infty}\|P_S^{[m]}h_U\|=0
\]
directly, a uniform majorant \(\|P_S^{[m]}h_U\|\le\varphi(m)\to0\), or a recursive
flag estimate of the form
\[
q_{m+1}(U)\le\theta q_m(U)+r_m,
\qquad
0\le\theta<1,
\qquad
(r_m)\in\ell^1,
\tag{R43.FT8}
\]
for \(q_m(U)=\|P_S^{[m]}h_U\|^2\).

---

## 2. The terminal partial-isometry cocycle already exists algebraically

For fixed source pair \(0<R<S\), every
\[
W_U:=W_{R,S}^{[U]}:H_R\to H_S
\]
is an isometry.  For terminals \(U<V\), define
\[
\boxed{
\mathcal T_{U\to V}
:=W_VW_U^*
:\operatorname{Ran}W_U\longrightarrow\operatorname{Ran}W_V.
}
\tag{R43.TC1}
\]
Because \(W_U^*W_U=I_{H_R}\), this is a unitary map between the two closed ranges and
\[
\boxed{
\mathcal T_{U\to V}W_U=W_V.
}
\tag{R43.TC2}
\]
In particular
\[
\boxed{
\mathcal T_{U\to V}w_U=w_V.
}
\tag{R43.TC3}
\]
For \(U<V<Z\), on \(\operatorname{Ran}W_U\),
\[
\begin{aligned}
\mathcal T_{V\to Z}\mathcal T_{U\to V}
&=W_ZW_V^*W_VW_U^*\\
&=W_ZW_U^*\\
&=\mathcal T_{U\to Z}.
\end{aligned}
\]
Hence
\[
\boxed{
\mathcal T_{V\to Z}\mathcal T_{U\to V}
=\mathcal T_{U\to Z}
\quad\text{on }\operatorname{Ran}W_U.
}
\tag{R43.TC4}
\]
So the algebraic cocycle prerequisite for a discrete telescoping argument is already
available; no new terminal generator is required for this part.

This does **not** solve B-TIGHT.  The hard problem is quantitative flag leakage of
\(\mathcal T_{U\to V}\).  Since \(P_S^{[m]}\varepsilon_S=0\) for \(m\ge1\),
\[
P_S^{[m]}h_V=P_S^{[m]}w_V
=P_S^{[m]}\mathcal T_{U\to V}w_U.
\tag{R43.TC5}
\]
Thus one legitimate discrete route is to prove one-step estimates which say that
\(\mathcal T_{U\to V}\) cannot inject appreciable mass from shallow jet layers into very
deep ones.

For example, fix a terminal chain
\[
U_0<U_1<U_2<\cdots\to\infty.
\]
A sufficient schematic leakage estimate is
\[
\boxed{
\|P_S^{[m]}\mathcal T_{U_k\to U_{k+1}}x\|
\le
\|P_S^{[r(m)]}x\|
+\epsilon_k\eta(m)\|x\|,
}
\tag{R43.TC6}
\]
for \(x\in\operatorname{Ran}W_{U_k}\), where
\[
r(m)\to\infty,
\qquad
\eta(m)\to0,
\qquad
\sum_k\epsilon_k<\infty.
\tag{R43.TC7}
\]
Together with TC4, such an estimate can be iterated/telescoped to produce B-FLAGTIGHT.
The precise usable form of TC6 is open; it is now the natural quantitative terminal-dynamics
target.

R40/R41's \(U^{-1}\) normal scale may only be used here after an actual finite-increment
estimate links it to \(\epsilon_k\).  A bare \(U_k^{-1}\) sequence is not summable for a
linearly spaced chain; one needs additional decay or a terminal chain whose spacing makes
the resulting increment bounds summable.  No such estimate is currently booked.

---

## 3. B-SIGN: chain condition and optimal two-terminal scalar criterion

Under candidate GC-AC plus B-TIGHT,
\[
L_{R,S}^{T,U}=b_Tb_U+o(1)
\qquad(T,U\to\infty),
\tag{R43.SG1}
\]
and \(|b_U|\to1\).

### 3.1 Local increment criterion requires a cofinal chain

Suppose there exist \(\Delta,\eta>0\) and a cofinal terminal set \(\mathfrak T\) such that
for all sufficiently large \(U,V\in\mathfrak T\),
\[
|U-V|\le\Delta
\Longrightarrow
|b_V-b_U|\le2-\eta.
\tag{R43.SG2}
\]
To infer a single global terminal sign one also needs the sufficiently late part of
\(\mathfrak T\) to have one cofinal \(\Delta\)-chain component: any two sufficiently late
terminals can be connected by finitely many terminals in \(\mathfrak T\), with consecutive
gaps at most \(\Delta\).

Under B-TIGHT, choose \(\varepsilon<\eta/2\) so that \(|b_U|>1-\varepsilon\) eventually.
Opposite signs at neighboring chain points would force
\[
|b_V-b_U|>2-2\varepsilon>2-\eta,
\]
contradicting SG2.  Chain connectivity then propagates one sign through the whole cofinal
component.

For the present P11 formulation the terminal horizon \(U\) is a real parameter with
\(U>S\), so the ambient terminal parameter set itself is connected.  Nevertheless SG2 is
stated with the chain hypothesis because any future restriction to arithmetic/checkpoint
terminal subsets must reverify it.

### 3.2 The positive-correlation threshold can be weakened to the sharp threshold \(-1\)

Under B-TIGHT, Strong Terminal is equivalent to
\[
b_Tb_U\to1.
\]
If B-SIGN fails, there exist cofinal \(T_n,U_n\) of opposite sign and hence
\[
b_{T_n}b_{U_n}\to-1.
\]
By SG1,
\[
L_{R,S}^{T_n,U_n}\to-1.
\]
Therefore
\[
\boxed{
\text{under candidate GC-AC + B-TIGHT,}
\qquad
\text{Strong Terminal}
\iff
\liminf_{T,U\to\infty}L_{R,S}^{T,U}>-1.
}
\tag{R43.SG3}
\]
The forward implication is immediate because Strong Terminal gives \(L^{T,U}\to1\).
The reverse implication follows because any asymptotic sign split would force the two-parameter
liminf to equal \(-1\).

Thus the older sufficient condition \(\liminf L^{T,U}>0\) is correct but unnecessarily
strong.

---

## 4. Literature diagnostic for the higher-jet conditioning route

The numerical conditioning experiment remains route-diagnostic rather than theorem-level.
Two classical literature facts explain why the observed geometric decay is plausible:

1. H. Widom and H. Wilf, **Small eigenvalues of large Hankel matrices**, Proc. Amer. Math.
   Soc. (1966), established Szegő-class asymptotics for compact-interval Hankel moment
   matrices.  For the flat \([0,1]\) prototype, the classical dominant exponential factor is
   \((1+\sqrt2)^{-4N}\) up to polynomial/prefactor corrections.
2. C. Berg and R. Szwarc, **The Smallest Eigenvalue of Hankel Matrices**, Constructive
   Approximation 34 (2011), 107--133, DOI `10.1007/s00365-010-9109-4`, prove exponential
   decay of the smallest moment-Hankel eigenvalue for every compactly supported measure.

The earlier review attribution to “Berg--Chen--Ismail” for the general compact-support
exponential-decay theorem is therefore corrected here: the directly matching theorem is
Berg--Szwarc.

At \(S=1\), the direct-SVD normalized constrained-Gamma diagnostic gives
\[
\sigma_{\min}(4,8,12,16)
\approx
2.7688\times10^{-3},
2.4077\times10^{-6},
2.3206\times10^{-9},
2.2410\times10^{-12}.
\]
The four-index geometric factors are
\[
\left(\frac{\sigma_{8}}{\sigma_4}\right)^{1/4}\approx0.1717,
\qquad
\left(\frac{\sigma_{12}}{\sigma_8}\right)^{1/4}\approx0.1762,
\qquad
\left(\frac{\sigma_{16}}{\sigma_{12}}\right)^{1/4}\approx0.1763.
\tag{R43.LIT1}
\]
The flat-\([0,1]\) prototype has
\[
(1+\sqrt2)^{-2}\approx0.1716
\]
for the corresponding singular-value root rate.  This numerical proximity is diagnostically
interesting but **is not imported as an asymptotic theorem for the constrained-Gamma Gram**:
the latter includes Gamma whitening, the zeroth-jet projection, normalization, and is not yet
proved asymptotically comparable to a scalar compact-support moment Hankel matrix.

### Precision firewall

The reported \(\sigma_{\min}\) values are obtained by a direct SVD of the normalized synthesis
matrix \(Y_m\), not by calling an eigensolver on an explicitly formed Gram matrix
\(Y_m^*Y_m\).  The smallest reported singular value, about \(2.2\times10^{-12}\), remains
well above double-precision machine epsilon.  The displayed Gram value
\(\lambda_{\min}=\sigma_{\min}^2\sim5\times10^{-24}\) is a derived square and must not be
interpreted as an independently resolved `eigvalsh` value at that scale.  Galerkin- and
Fourier-cutoff stability of \(\sigma_{\min}\) is the relevant numerical check.

No literature theorem is currently used to promote the numerical route diagnostic to a
formal no-go for the actual constrained-Gamma family.

---

## 5. Current priority

The active quantitative problem is now
\[
\boxed{
\textbf{B-FLAGTIGHT:}
\quad
\lim_{m\to\infty}\limsup_{U\to\infty}
\|P_S^{[m]}h_U\|=0.
}
\]

The preferred structural route is:

1. use the exact terminal range cocycle \(\mathcal T_{U\to V}=W_VW_U^*\);
2. derive a one-step deep-flag leakage estimate for that cocycle;
3. telescope/iterate a summable sequence of leakage errors;
4. only after B-FLAGTIGHT, close B-SIGN through SG2 plus chain connectivity, or directly
   through the sharp two-terminal condition SG3.

Uniform jet-number energy remains a useful sufficient estimate, but is no longer the primary
gate and must not be mistaken for a necessary condition.
