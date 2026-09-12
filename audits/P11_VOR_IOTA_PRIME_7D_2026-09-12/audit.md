# Vor-iota' Zug 7D -- canonical bounded-transform cross-bridge firewall at `R=1`

## 0. Scope and non-claims

This note is a **finite-window, single-witness building-block audit**.  It studies one canonical parameter-free pre-Schur/Mediator bridge constructed solely from the existing P11 operators at `R=1`.

It does **not** claim:

- a universal no-go for cross-term or mediator geometries;
- failure of another source recoding or another bounded transform;
- a global source/descent obstruction;
- a completed Object-X realization;
- anything about RH.

The result is new relative to merged PR #96 because PR #96 explicitly left nontrivial mediators and pre-Schur cross-term geometries open.

## 1. Existing P11 data and the PR-#91 Prime-2 witness

Let

\[
\mathscr H_1=L^2(-1,1),\qquad
T:=\widetilde R_1:\mathscr H_1\to\mathscr Z_1,
\]

\[
A:=T^*T=R_1^*R_1\ge0,\qquad
B:=(I+A)^{-1},
\]

and let `H:=H_1` be the P11 neutral hub.

Use the same normalized odd PR-#91 witness pair `a,b` used by PR #96.  It satisfies

\[
B_W(a,b)-\mathfrak c_\Gamma[a,b]
=-\frac{\log2}{\sqrt2}.
\tag{7D.1}
\]

The already audited diagonal pieces on this pair are

\[
\langle Ha,Hb\rangle
=-\frac{\log2}{2\sqrt2},
\tag{7D.2}
\]

and

\[
\langle Ta,Tb\rangle
=\frac{4-7\sqrt2}{32}\log2.
\tag{7D.3}
\]

Therefore any additional symmetric cross correction attached to the lift

\[
f\longmapsto(Hf,Tf)
\]

must equal

\[
\boxed{
X_{\rm req}
=-\frac{4+\sqrt2}{32}\log2
}
\tag{7D.4}
\]

on `(a,b)` in order to reproduce the exact Prime-2 Weil calibration.

## 2. The 7D bridge

Set

\[
C:=(I+H^*H)^{-1}.
\]

Define the two canonical bounded transforms

\[
C_H:=HC,
\qquad
C_T^*:=BT^*.
\]

The 7D bridge is

\[
\boxed{
M_{7D}:=C_HC_T^*
=H(I+H^*H)^{-1}(I+A)^{-1}T^*:
\mathscr Z_1\to\mathscr H_1.
}
\tag{7D.5}
\]

It introduces no fitted scalar, no new basis and no Weil-dependent coefficient.

For every `s>=0`,

\[
\frac{s}{1+s^2}\le\frac12.
\]

Hence

\[
\|C_H\|\le\frac12,
\qquad
\|C_T^*\|\le\frac12,
\qquad
\boxed{\|M_{7D}\|\le\frac14.}
\tag{7D.6}
\]

Thus the nonorthogonal block metric

\[
G_{7D}:=
\begin{pmatrix}
I&M_{7D}\\
M_{7D}^*&I
\end{pmatrix}
\]

obeys

\[
\boxed{G_{7D}\ge\frac34I.}
\tag{7D.7}
\]

So positivity is structural and is not inferred from the desired Weil value.

## 3. Same-source pullback

Define the two positive resolvent defects

\[
P_H:=I-C=H^*H(I+H^*H)^{-1},
\]

\[
P_R:=I-B=A(I+A)^{-1}.
\]

Using

\[
BT^*T=BA=I-B
\]

and

\[
H^*HC=I-C,
\]

the cross correction of `G_7D` on the lifted vectors `(Hf,Tf)` is

\[
\boxed{
X_{7D}(f,g)
=\langle P_Hf,P_Rg\rangle
+\langle P_Rf,P_Hg\rangle.
}
\tag{7D.8}
\]

Equivalently, the source-level cross operator is the anticommutator

\[
\boxed{K_{7D}=P_HP_R+P_RP_H.}
\tag{7D.9}
\]

This is not the native Schur Gram `HBH^*` tested in PR #96.

## 4. Why the first CG number was not a certificate

A first Dictionary/CG computation suggested

\[
X_{7D}(a,b)\approx-0.070736.
\]

That value was **not accepted as proof**.  At bump half-width `epsilon=10^{-4}`, repeated `H^*H` applications already create distinct nonzero lobes whose centres are closer than `2*epsilon`; thus the former tuplewise-orthogonality shortcut fails for the Krylov resolvent calculation.  The first computation also used amplitude pruning without a global error certificate.

The 7D status was therefore reset to OPEN before the hardened calculation below.

## 5. Spectral boxes for the resolvent defects

For the five active `R=1` hub channels,

\[
\|D_s\|\le2
\]

gives

\[
\|H\|
\le
2\sum_{(p,k)\in\{(2,1),(2,2),(3,1),(5,1),(7,1)\}}
\sqrt{\log p}\,p^{-3k/4}<4.
\]

Hence

\[
\boxed{0\le H^*H<16I.}
\tag{7D.10}
\]

For the full-rest martingale sectors `(2,0),(2,1),(3,0),(5,0),(7,0)`, use

\[
\|K_{k\log p}^{\rm tr}\|\le2
\]

and the infinite geometric majorant

\[
\|\Phi_{p,a,1}\|
\le
2\sum_{k\ge a+1}p^{-3k/4}.
\]

Then

\[
\|A\|
\le
\sum_{p,a}(\log p)(p-1)p^a\|\Phi_{p,a,1}\|^2
<32.
\]

Thus

\[
\boxed{0\le A<32I.}
\tag{7D.11}
\]

The companion Arb checker verifies both strict numerical margins using outward-rounded balls.

## 6. Chebyshev certificate

For

\[
r(t)=\frac1{1+t},\qquad0\le t\le L,
\]

set

\[
s=\sqrt{1+L},\qquad
q=\frac{s-1}{s+1},\qquad
x=\frac{2t}{L}-1.
\]

Then

\[
\boxed{
\frac1{1+t}
=\frac1s\left[1+2\sum_{n\ge1}(-q)^nT_n(x)\right].
}
\tag{7D.12}
\]

After truncation at degree `N`,

\[
\boxed{
\|r-r_N\|_{L^\infty[0,L]}
\le
\varepsilon(L,N)
:=\frac2s\frac{q^{N+1}}{1-q}.
}
\tag{7D.13}
\]

Since `P(t)=t/(1+t)=1-r(t)`, the same bound controls the polynomial approximants to `P_H` and `P_R`.

The hardened certificate uses

\[
N=13,\qquad L_H=16,\qquad L_R=32,
\qquad \epsilon_{\rm bump}=10^{-8}.
\tag{7D.14}
\]

It computes the Chebyshev recurrence on exact half-log exponent tuples

\[
(n_2,n_3,n_5,n_7)
\longleftrightarrow
\frac12(n_2\log2+n_3\log3+n_5\log5+n_7\log7)
\]

and uses Arb balls for all coefficients and transcendental constants.

No coefficient is discarded merely because it is numerically small.
Every `P_1` and `\Omega_{p,a,1}` cutoff decision is accepted only if the whole bump support is rigorously on one side of the cutoff.  Before the final tuplewise `L^2` pairing, all distinct output lobe centres are certified to be separated by more than `2*epsilon_bump`.

## 7. Certified enclosure and separation

The Arb run at precision `200` bits gives the degree-13 central value

\[
X_{13}
=-0.07161580220284683\ldots
\]

with finite arithmetic ball radius below `3\cdot10^{-56}`.

The analytic Chebyshev contribution satisfies

\[
|X_{7D}-X_{13}|
\le
2(\varepsilon_H+\varepsilon_R+\varepsilon_H\varepsilon_R)
=0.01951899370897315\ldots,
\tag{7D.15}
\]

where

\[
\varepsilon_H=\varepsilon(16,13),
\qquad
\varepsilon_R=\varepsilon(32,13).
\]

Therefore

\[
\boxed{
X_{7D}(a,b)
\in
[-0.0911347959\ldots,-0.0520968085\ldots].
}
\tag{7D.16}
\]

The required value is

\[
X_{\rm req}
=-\frac{4+\sqrt2}{32}\log2
=-0.11727646455338526\ldots.
\]

The certified lower-end separation is

\[
\boxed{
X_{\rm lo}-X_{\rm req}
=0.0261416686415652856\ldots>0,
}
\tag{7D.17}
\]

with Arb radius below `3\cdot10^{-56}` in the hardened run.  Hence

\[
\boxed{X_{\rm req}<X_{\rm lo}\le X_{7D}(a,b).}
\]

Thus equality is impossible.

## 8. Verdict

For the PR-#91 odd Prime-2 witness at `R=1`, the canonical bounded-transform bridge (7D.5) has:

- canonical / existing-P11 input only: **PASS**;
- no free calibration parameter: **PASS**;
- positive nonorthogonal block metric: **PASS**, with `G_7D >= 3/4 I`;
- Prime-2 nonzero arithmetic response: **PASS**;
- exact Weil cross calibration: **FAIL**.

In the project shorthand:

\[
\boxed{\text{7D: d-weak PASS, d-exact FAIL (Arb/Chebyshev certified).}}
\]

The FAIL is separated by a macroscopic certified gap and does not depend on interpreting the earlier approximately `0.603` ratio.

## 9. Exact scope of the negative result

This audit excludes **only** the specific bridge

\[
M_{7D}=H(I+H^*H)^{-1}(I+A)^{-1}T^*
\]

in the stated `R=1` Prime-2 calibration.

It does not exclude:

- another canonical positive bridge;
- a structurally defined class containing different bounded transforms;
- a nontrivial mediator with additional P11 data;
- a different source recoding;
- global descent/source spaces;
- Object X in another architecture;
- RH.

The global Vor-Delta route remains **STAND-BY**.  No Registry promotion follows from this local finite-window certificate.
