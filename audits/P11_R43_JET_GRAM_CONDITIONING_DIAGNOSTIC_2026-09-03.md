# P11 R43 — constrained-Gamma jet-Gram conditioning diagnostic

Date: 2026-09-03

## Purpose

Test the multi-model review warning that the Section-3K higher-jet Riesz family may be
Hankel/Hilbert-type ill-conditioned, before spending proof effort on a global
higher-jet-to-C6a basis-conditioning theorem.

This file records a **numerical diagnostic only**.  It is not a proof, certificate,
independent GREEN verdict, or no-go theorem.

Reproducible script:

\`audits/P11_R43_JET_GRAM_CONDITIONING_DIAGNOSTIC_2026-09-03.py\`

## What is actually tested

The raw \(L^2\) moment Gram is not enough for the R43 question.  The diagnostic therefore
Galerkin-approximates the actual odd finite-window Gamma Hilbert geometry.

For fixed radius \(S\), use the \(L^2(-S,S)\)-orthonormal odd sine basis
\[
e_j(x)=S^{-1/2}\sin(j\pi x/S),\qquad j\ge1.
\]

The Gamma form matrix is built from the exact R33 symbol
\[
m_\Gamma(\xi)
=
1+\operatorname{Re}\psi\!\left(\frac14+\frac{i\xi}{2}\right)-\psi\!\left(\frac14\right).
\]

For
\[
\phi_m(x)=\operatorname{sgn}(x)I_m(|x|),
\qquad
I_m(r)=\int_0^r s^m e^{-s/2}\,ds,
\]
let \(B_{mj}=\beta_m(e_j)\).  If \(A\) is the Galerkin Gamma form matrix, then the
unconstrained Riesz Gram is
\[
K=B A^{-1}B^T.
\]

Rather than forming \(A^{-1}\) explicitly, write \(A=LL^T\) and
\[
z_m=L^{-1}B_m^T.
\]
Then
\[
\langle z_m,z_n\rangle_{\ell^2}
\]
is exactly the Galerkin Gamma inner product of the corresponding Riesz vectors.

The zeroth-jet constraint is imposed by
\[
y_m
=
z_m
-
z_0\frac{\langle z_0,z_m\rangle}{\|z_0\|^2},
\qquad m\ge1.
\]
Finally every \(y_m\) is normalized to norm one.  Thus the test removes the raw
\(M^{m+1}\) jet scaling completely.

For the first \(m\) normalized constrained vectors, let \(Y_m\) be the matrix of columns.
Then
\[
\lambda_{\min}(\mathcal G_m)
=
\sigma_{\min}(Y_m)^2,
\qquad
\mathcal G_m=Y_m^*Y_m.
\]

## Main numerical result

Using Galerkin dimension \(P=120\), the normalized constrained-Gamma family gives:

| \(S\) | \(m\) | \(\sigma_{\min}(Y_m)\) | \(\lambda_{\min}(\mathcal G_m)\) | \(\kappa(\mathcal G_m)\) |
|---:|---:|---:|---:|---:|
| 0.5 | 4  | \(2.6499\times10^{-3}\) | \(7.0221\times10^{-6}\) | \(5.58\times10^5\) |
| 0.5 | 8  | \(2.2371\times10^{-6}\) | \(5.0045\times10^{-12}\) | \(1.53\times10^{12}\) |
| 0.5 | 12 | \(2.1222\times10^{-9}\) | \(4.5037\times10^{-18}\) | \(2.51\times10^{18}\) |
| 0.5 | 16 | \(2.0293\times10^{-12}\) | \(4.1180\times10^{-24}\) | \(3.63\times10^{24}\) |
| 1.0 | 4  | \(2.7688\times10^{-3}\) | \(7.6664\times10^{-6}\) | \(5.11\times10^5\) |
| 1.0 | 8  | \(2.4077\times10^{-6}\) | \(5.7970\times10^{-12}\) | \(1.32\times10^{12}\) |
| 1.0 | 12 | \(2.3206\times10^{-9}\) | \(5.3852\times10^{-18}\) | \(2.10\times10^{18}\) |
| 1.0 | 16 | \(2.2410\times10^{-12}\) | \(5.0220\times10^{-24}\) | \(2.97\times10^{24}\) |
| 2.0 | 4  | \(3.0331\times10^{-3}\) | \(9.1998\times10^{-6}\) | \(4.25\times10^5\) |
| 2.0 | 8  | \(2.8047\times10^{-6}\) | \(7.8662\times10^{-12}\) | \(9.69\times10^{11}\) |
| 2.0 | 12 | \(2.7928\times10^{-9}\) | \(7.7997\times10^{-18}\) | \(1.44\times10^{18}\) |
| 2.0 | 16 | \(2.7514\times10^{-12}\) | \(7.5701\times10^{-24}\) | \(1.96\times10^{24}\) |
| 4.0 | 4  | \(3.6180\times10^{-3}\) | \(1.3090\times10^{-5}\) | \(2.97\times10^5\) |
| 4.0 | 8  | \(3.8065\times10^{-6}\) | \(1.4489\times10^{-11}\) | \(5.23\times10^{11}\) |
| 4.0 | 12 | \(4.0601\times10^{-9}\) | \(1.6485\times10^{-17}\) | \(6.77\times10^{17}\) |
| 4.0 | 16 | \(4.1705\times10^{-12}\) | \(1.7393\times10^{-23}\) | \(8.45\times10^{23}\) |

At \(S=1\), a least-squares fit over \(m=2,\dots,16\) gives
\[
\boxed{
\log_{10}\sigma_{\min}(Y_m)
\approx
-0.7614\,m+0.5029.
}
\]
Equivalently the normalized Gram minimum behaves diagnostically like
\[
\log_{10}\lambda_{\min}(\mathcal G_m)
\approx
-1.5228\,m+1.0058.
\]

This is strong numerical evidence of geometric/exponential conditioning loss.

## Resolution checks

At \(S=1\), the singular values stabilize with Galerkin dimension:

| \(P\) | \(m=4\) | \(m=8\) | \(m=12\) | \(m=16\) |
|---:|---:|---:|---:|---:|
| 40  | \(2.7622e{-3}\) | \(2.3740e{-6}\) | \(2.2076e{-9}\) | \(1.9306e{-12}\) |
| 60  | \(2.7663e{-3}\) | \(2.3954e{-6}\) | \(2.2826e{-9}\) | \(2.1440e{-12}\) |
| 80  | \(2.7677e{-3}\) | \(2.4026e{-6}\) | \(2.3054e{-9}\) | \(2.2042e{-12}\) |
| 100 | \(2.7684e{-3}\) | \(2.4059e{-6}\) | \(2.3153e{-9}\) | \(2.2288e{-12}\) |
| 120 | \(2.7688e{-3}\) | \(2.4077e{-6}\) | \(2.3206e{-9}\) | \(2.2411e{-12}\) |

The Fourier cutoff check at \(S=1,P=100\) is also stable:

| \(\Xi_{\max}\) | \(m=4\) | \(m=8\) | \(m=12\) | \(m=16\) |
|---:|---:|---:|---:|---:|
| 540  | \(2.768400e{-3}\) | \(2.405712e{-6}\) | \(2.314885e{-9}\) | \(2.227984e{-12}\) |
| 1620 | \(2.768435e{-3}\) | \(2.405891e{-6}\) | \(2.315315e{-9}\) | \(2.228770e{-12}\) |
| 4860 | \(2.768436e{-3}\) | \(2.405898e{-6}\) | \(2.315331e{-9}\) | \(2.228754e{-12}\) |

Thus the observed decay is not a visible truncation artifact at these resolutions.

## Numerical precision firewall

The script computes
\[
\sigma_{\min}(Y_m)
\]
**directly** with an SVD of the normalized synthesis/Galerkin matrix \(Y_m\).  It does not
form \(\mathcal G_m=Y_m^*Y_m\) and then call an eigenvalue solver on that Gram matrix.
The reported
\[
\lambda_{\min}(\mathcal G_m)
=
\sigma_{\min}(Y_m)^2
\]
is obtained only by squaring the directly computed singular value.

This distinction matters at \(m=16\): the displayed
\(\lambda_{\min}\approx5\times10^{-24}\) lies far below double-precision relative machine
epsilon if interpreted as an independently resolved eigenvalue of an explicitly formed
Gram matrix.  By contrast the directly computed
\(\sigma_{\min}\approx2.24\times10^{-12}\) is still well above machine epsilon.

Accordingly:

- the SVD singular values are the primary numerical observables;
- the Gram minima are derived squares, not independent double-precision eigensolver data;
- the Galerkin/cutoff stability tables are the present robustness check;
- no arbitrary-precision certificate is claimed in this audit.

At \(S=1\), the per-index geometric rates inferred from successive four-jet blocks are
\[
\left(\frac{\lambda_{8}}{\lambda_{4}}\right)^{1/4}\approx0.02949,
\qquad
\left(\frac{\lambda_{12}}{\lambda_{8}}\right)^{1/4}\approx0.03105,
\qquad
\left(\frac{\lambda_{16}}{\lambda_{12}}\right)^{1/4}\approx0.03108,
\]
with the \(m=4\) to \(m=16\) aggregate rate
\[
\boxed{
\left(\frac{\lambda_{16}}{\lambda_{4}}\right)^{1/12}
\approx0.03053.
}
\]
For the singular values the aggregate rate is
\[
\left(\frac{\sigma_{16}}{\sigma_4}\right)^{1/12}
\approx0.17472.
\]

## Classical Hankel comparison — literature-supported diagnostic only

The observed rate is strikingly close to the classical compact-interval moment/Hankel
scale, but this comparison must be kept at diagnostic level.

Widom and Wilf, *Small eigenvalues of large Hankel matrices*, Proc. Amer. Math. Soc.
**17** (1966), 338--344, study moment Hankel matrices for a measure on a finite interval
satisfying a Szegő condition and derive an asymptotic law with geometric decay.  Their
exponential constant is determined by the support interval.

For the standard \([0,1]\) Jacobi/Hilbert-type moment geometry, the familiar dominant
geometric factor is
\[
\boxed{
(1+\sqrt2)^{-4}
\approx0.0294373
}
\]
for the smallest Gram eigenvalue, and
\[
(1+\sqrt2)^{-2}
\approx0.171573
\]
at the singular-value level.  The present aggregate rates \(0.03053\) and \(0.17472\)
are close to those prototype constants.

A broader theorem is due to Christian Berg and Ryszard Szwarc,
*The smallest eigenvalue of Hankel matrices*, Constructive Approximation **34** (2011),
107--133: for every positive measure with compact support, the smallest eigenvalue of its
moment Hankel matrices decays exponentially to zero.

This attribution matters.  Berg--Chen--Ismail,
*Small eigenvalues of large Hankel matrices: The indeterminate case*, Math. Scand.
**91** (2002), 67--81, concerns the characterization of the indeterminate moment case by a
strict positive lower bound for the Hankel minimum; it is not the source of the general
compact-support exponential-decay theorem used in this comparison.

### Transfer firewall

None of those classical results applies automatically to the present normalized
constrained-Gamma Gram matrices.

The actual vectors include:

1. the inverse Gamma-form operation \(C_{\Gamma,S}^{-1}\) / Galerkin whitening;
2. projection off the zeroth constrained Riesz direction;
3. individual normalization of every higher-jet Riesz vector.

To promote the classical Hankel law to a theorem about the R43 family one would still need
a quantitative comparison theorem showing that these operations preserve the relevant
moment-matrix asymptotics or at least an exponential upper bound for
\(\lambda_{\min}\).

Therefore the literature comparison strengthens the **route diagnosis** but does not
upgrade it to a no-go theorem.

## Interpretation

The experiment specifically removes the objection that the earlier exponential
\(M^{m+1}\) estimate was merely a raw jet-normalization artifact: every constrained Riesz
vector is normalized before the conditioning test, yet the normalized family still becomes
extremely close to linearly dependent.

Therefore a route requiring a dimension-uniform Riesz lower bound for the full
Section-3K higher-jet family is numerically strongly contraindicated.

What the diagnostic does **not** prove:

- it does not prove an asymptotic exponential law;
- it does not prove that every possible orbit-adapted finite change-of-basis estimate fails;
- it does not prove failure of B-TIGHT or Strong Terminal;
- it says nothing negative about the canonical C6a ONB itself.

The correct operational consequence is narrower:

\[
\boxed{
\text{Do not make a global Section-3K higher-jet Riesz-conditioning theorem the primary
B-TIGHT route.}
}
\]

The preferred route remains direct control of a compact-resolvent energy of the actual
normal orbit
\[
h_U=W_U\varepsilon_R-b_U\varepsilon_S.
\]

## Status

\[
\boxed{
\text{strong numerical route diagnostic only;}
\quad
\text{no theorem/no-go promotion.}
}
\]
