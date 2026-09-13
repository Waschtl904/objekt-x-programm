# P11 A1-LEGENDRE — orthonormal finite certificate route

**Date:** 2026-09-13  
**Status:** theorem-level alternative finite-reduction audit; numerical constants candidate until exact-head CI.  
**Parent main:** `096ab135a19dc6b905358c396c1441e4e7024392` / PR #115.  
**Registry:** unchanged.  
**Object-X working definition:** unchanged.

---

## 1. Purpose

PR #115 reduces the canonical `a=1` completion to a finite lower bound on a moment-augmented PSWF resolved space.  That route is dimension-efficient (`<=1212`) but a rigorous final computation would still need certified PSWF basis vectors and a nontrivial Gram matrix or a certified orthonormalization.

This audit gives a second, deliberately more conservative route whose basis is **exactly orthonormal** from the start: normalized Legendre polynomials on `[-1,1]`.

The gain is computational-certification simplicity:

- exact parity split;
- Gram matrix exactly `I`;
- explicit Fourier transforms by spherical Bessel functions;
- explicit super-exponential band-tail bound;
- explicit moment coefficients by modified spherical Bessel functions;
- no PSWF eigenvector enclosure is needed.

The cost is a somewhat larger finite head: `1075 x 1075` per parity at the predeclared cut `M=2150`.

No final finite positivity claim is made in this audit.

---

## 2. Lower operator inherited from PR #115

At `a=1` use the already certified frequency split

```math
c=0.1,
\qquad
\Omega=1551,
```

and

```math
r(\xi)=(m_1(\xi)-c)\mathbf 1_{[-\Omega,\Omega]}(\xi),
```

with certified

```math
m_1(\xi)>0.1\quad(|\xi|\ge1551),
\qquad
\|r\|_\infty<12.
```

Let

```math
K=P_I\mathcal F^{-1}M_r\mathcal F P_I,
\qquad I=(-1,1),
```

and

```math
L_1=cI+K+\mathcal E^*\mathcal E.
```

From PR #114/#115,

```math
A_1=q_1+\mathcal E^*\mathcal E\succeq L_1.
```

Therefore proving `L_1>=0` proves the canonical `a=1` completion.

---

## 3. Exact orthonormal Legendre basis

Set

```math
\phi_n(x)=\sqrt{n+\tfrac12}\,P_n(x),
\qquad n=0,1,2,\ldots,
```

on `[-1,1]`.  Since

```math
\int_{-1}^{1}P_n(x)P_m(x)dx
=\frac{2}{2n+1}\delta_{nm},
```

we have exactly

```math
\boxed{\langle\phi_n,\phi_m\rangle=\delta_{nm}.}
```

Parity is exact:

```text
n even  -> phi_n even,
n odd   -> phi_n odd.
```

With the nonunitary Fourier transform

```math
F_n(t)=\int_{-1}^{1}\phi_n(x)e^{itx}dx,
```

Zhu's standard formula gives

```math
\boxed{
F_n(t)=2i^n\sqrt{n+\tfrac12}\,j_n(t),
}
```

where `j_n` is the spherical Bessel function.

This basis removes the Gram-matrix caveat raised in the external review: on every finite leading block the metric is literally the identity.

---

## 4. Legendre band-tail concentration theorem `✓[M]`

Let `B_\Omega` be orthogonal Fourier projection to `[-Omega,Omega]`, and let

```math
C_\Omega=P_I B_\Omega P_I.
```

For the orthogonal Legendre tail

```math
H_M
=\overline{\operatorname{span}}\{\phi_n:n\ge M\},
```

positivity of `C_Omega` gives

```math
\|B_\Omega|_{H_M}\|^2
=\|P_{H_M}C_\Omega P_{H_M}\|
\le\operatorname{tr}(P_{H_M}C_\Omega P_{H_M}).
```

Now

```math
\langle\phi_n,C_\Omega\phi_n\rangle
=\frac1{2\pi}\int_{-\Omega}^{\Omega}|F_n(t)|^2dt
=\frac{4(n+1/2)}{\pi}\int_0^\Omega j_n(t)^2dt.
```

Use the elementary spherical-Bessel inequality quoted as Eq. (12) in Zhu, arXiv:2608.24827v2,

```math
|j_n(t)|\le\frac{t^n}{(2n+1)!!},\qquad t\ge0.
```

Then

```math
\boxed{
\langle\phi_n,C_\Omega\phi_n\rangle
\le d_n
:=\frac{2}{\pi}
\frac{\Omega^{2n+1}}{((2n+1)!!)^2}.
}
```

The ratio is exact:

```math
\frac{d_{n+1}}{d_n}
=\frac{\Omega^2}{(2n+3)^2}.
```

For `M` with `2M+3>Omega`, this ratio decreases, hence

```math
\boxed{
\eta_M
:=\|B_\Omega|_{H_M}\|^2
\le\sum_{n\ge M}d_n
\le
\frac{d_M}{1-\Omega^2/(2M+3)^2}.
}
```

This is a completely explicit elementary alternative to computing PSWF eigenvectors.

---

## 5. Bounded multiplier tail and crossblock `✓[M]`

Let

```math
R_M=\operatorname{span}\{\phi_0,\ldots,\phi_{M-1}\},
\qquad
T_M=R_M^\perp.
```

Because `r` is supported in the band and `||r||_infty<=R`, with `R=12`,

```math
\boxed{
\|P_{R_M}KP_{T_M}\|
\le R\sqrt{\eta_M}.
}
```

Indeed `K=P_I F^{-1}M_r B_\Omega F P_I`, so the only small factor needed on the tail is the band leakage `||B_\Omega P_T||<=sqrt(eta_M)`.

Likewise, for `v in T_M`,

```math
|\langle v,Kv\rangle|
\le R\|B_\Omega v\|^2
\le R\eta_M\|v\|^2,
```

hence

```math
\boxed{
(cI+K)|_{T_M}\succeq(c-R\eta_M)I.
}
```

---

## 6. Moment-completion tail `✓[M]`

For

```math
E_+(v)=\langle v,e^{x/2}\rangle,
\qquad
E_-(v)=\langle v,e^{-x/2}\rangle,
```

the Legendre coefficient of `e^{x/2}` is

```math
\boxed{
a_n
=\langle\phi_n,e^{x/2}\rangle
=2\sqrt{n+\tfrac12}\,i_n(1/2),
}
```

where `i_n` is the modified spherical Bessel function. Reflection gives the coefficient of `e^{-x/2}` as `(-1)^n a_n`.

The positive series

```math
i_n(z)
=z^n\sum_{k\ge0}
\frac{(z^2/2)^k}{k!(2n+2k+1)!!}
```

gives the explicit bound

```math
\boxed{
i_n(z)
\le
\frac{z^n}{(2n+1)!!}
\exp\left(\frac{z^2}{2(2n+3)}\right).
}
```

Therefore the moment-vector Legendre tail has an elementary geometric majorant.  Let

```math
\sigma_M^2
:=\sum_{n\ge M}|a_n|^2.
```

Then

```math
\|\mathcal E P_{T_M}\|
\le\sqrt{2}\,\sigma_M.
```

Also

```math
\|\mathcal E\|
\le\sqrt{\|e^{x/2}\|^2+\|e^{-x/2}\|^2}
=\sqrt{4\sinh1}.
```

Hence the completion crossblock obeys

```math
\boxed{
\|P_R\mathcal E^*\mathcal E P_T\|
\le\sqrt{4\sinh1}\,\sqrt{2}\,\sigma_M.
}
```

At the chosen large `M` this term is far smaller than the already tiny multiplier crossblock.

---

## 7. Exact Legendre Schur criterion `✓[M]`

Let `A_M` denote the exact leading `M x M` Legendre matrix of

```math
L_1=0.1I+K+\mathcal E^*\mathcal E.
```

Define

```math
b_M
:=12\sqrt{\eta_M}
+\sqrt{4\sinh1}\,\sqrt2\,\sigma_M,
```

and

```math
\tau_M:=0.1-12\eta_M.
```

Since the completion tail block is positive, it may be discarded in the tail lower bound.  Thus

```math
(L_1)_{TT}\succeq\tau_MI,
\qquad
\|(L_1)_{RT}\|\le b_M.
```

Consequently

```math
\boxed{
A_M\succeq\mu I,
\qquad
\mu>\frac{b_M^2}{\tau_M}
\quad\Longrightarrow\quad
L_1\succeq0.
}
```

Because the Legendre basis is orthonormal, this is an ordinary matrix inequality against `I`; there is **no generalized Gram matrix**.

The parity blocks decouple exactly, so it is enough to certify the even and odd leading matrices separately.

---

## 8. Predeclared numerical gate `M=2150`

Before any leading-matrix computation, fix

```text
Omega = 1551
c = 0.1
R = 12
M = 2150
head dimensions = 1075 even + 1075 odd
```

and the sufficient finite target

```math
\boxed{\mu_{\rm Leg}=10^{-35}.}
```

The new exact-head Arb checker is required to certify

```math
\eta_{2150}<4.8\times10^{-42},
```

and

```math
\boxed{
\frac{b_{2150}^2}{\tau_{2150}}<7\times10^{-39}.
}
```

Thus `1e-35` dominates the complete analytic tail/cross penalty by more than three orders of magnitude.

`1e-35` is fixed before the finite matrix is assembled and is not fitted to an observed eigenvalue.

Until exact-head CI is green, these numerical bounds are candidate `✓[K/M]` only.

---

## 9. Final finite computation required

After the tail gate, the remaining proof is purely finite and orthonormal:

```math
\boxed{
A_{\rm even}\succeq10^{-35}I_{1075},
\qquad
A_{\rm odd}\succeq10^{-35}I_{1075}.
}
```

The exact entries are

```math
(A_M)_{nm}
=0.1\delta_{nm}
+\frac1{2\pi}\int_{-1551}^{1551}
r(t)F_n(t)\overline{F_m(t)}dt
+\langle\mathcal E\phi_n,\mathcal E\phi_m\rangle_{\mathbb C^2}.
```

Within one parity block the moment term simplifies to the positive rank-one matrix

```math
2a_na_m.
```

A rigorous implementation should follow the verified-matrix pattern already demonstrated in Zhu's Section 5:

1. multiprecision assembly;
2. explicit quadrature-error matrix norm;
3. parity-separated shifted Cholesky/LDL residual;
4. adapt precision until every decisive interval/pivot is strict;
5. any inconclusive pivot is a hard failure, never a sign guess.

The published non-certified reference floor for the full even Weil window at `L=1` is about `5.88e-30`; this is context only and is **not** used as a proof input.

---

## 10. Status

```text
orthonormal Legendre alternative route                 ✓[M]
Legendre band-tail trace theorem                       ✓[M]
moment-tail theorem                                    ✓[M]
Legendre Schur criterion                               ✓[M]
M=2150 eta/cross constants                             candidate ✓[K/M]
1075x1075 even finite lower bound >=1e-35              ?[O]
1075x1075 odd finite lower bound >=1e-35               ?[O]
full a=1 canonical completion                          ?[O]
all-a NP-GAP / Object X / RH                           ?[O]
```

This route does not supersede the smaller `1212`-dimensional PSWF reduction.  It is an **alternative certificate basis** whose purpose is to eliminate the Gram/PSWF-eigenvector certification burden.
