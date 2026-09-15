# P11 Audit — Euler factors as adjoint AR(1) resolvents

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level lokale Transferidentitaet zwischen P11 und Eulerfaktoren.  
**Registry:** unveraendert.  
**Nonclaim:** Eulerprodukt/Determinantdarstellung ist klassisch; keine Publikationsneuheit.

---

## 0. Kurzurteil

Der lokale Eulerfaktor einer Primzahl ist exakt die `z`-Transferfunktion des **adjungierten P11-AR(1)-Choleskyfaktors**.

Fuer

```math
q=p^{-1/2}
```

und den einseitigen Shift `S` auf `ell^2(N_0)` gilt

```math
T_q
=\sqrt{1-q^2}(I-qS^*)^{-1},
```

also

```math
\boxed{
T_q^*
=\sqrt{1-q^2}(I-qS)^{-1}.
}
```

Am Root-Impuls `e_0`:

```math
\boxed{
\frac1{\sqrt{1-q^2}}T_q^*e_0
=(1,q,q^2,\ldots).
}
```

Dessen `z`-Transformierte ist

```math
\boxed{
\frac1{1-qz}.
}
```

Mit dem physikalischen Delay

```math
z=e^{-s\log p}
```

wird dies exakt

```math
\boxed{
\frac1{1-p^{-(s+1/2)}}.
}
```

Der Prime-Anteil der logarithmischen Ableitung ist entsprechend

```math
\boxed{
-\log p\,
\frac{p^{-(s+1/2)}}{1-p^{-(s+1/2)}}
=
-h_p\left[
\frac1{1-q_pe^{-sh_p}}-1
\right].
}
```

Damit sind P11-AR(1)-Tail und lokaler Euler-Feedbackloop nicht nur durch dieselbe geometrische Reihe verwandt: sie besitzen denselben Resolventenoperator, in adjungierter Kausalitaetsorientierung.

Status:

```text
P11 tail = anti-causal AR1 resolvent                 ✓[M]
adjoint P11 tail = causal AR1 resolvent              ✓[M]
local Euler factor = z-transfer of adjoint resolvent ✓[M]
prime log derivative = resolvent excess              ✓[M]
Euler product determinant over primes                 classical / ✓[M]
constructive global passive coupling                  ?[O]
```

---

# 1. Shift orientation

Use the unilateral right shift

```math
Se_k=e_{k+1}.
```

Then

```math
(I-qS^*)^{-1}
=\sum_{r>=0}q^r(S^*)^r.
```

Hence

```math
\left[(I-qS^*)^{-1}X\right]_m
=\sum_{k>=m}q^{k-m}X_k.
```

This is exactly the P11 tail orientation, so

```math
\boxed{
T_q=\sqrt{1-q^2}(I-qS^*)^{-1}.
}
```

Taking adjoints gives

```math
\boxed{
T_q^*=\sqrt{1-q^2}(I-qS)^{-1}.
}
```

The Gram identity remains

```math
R_q=T_q^*T_q+uu^*.
```

---

# 2. Root impulse response

Since

```math
(I-qS)^{-1}e_0
=\sum_{r>=0}q^re_r,
```

we have

```math
\boxed{
\frac1{\sqrt{1-q^2}}T_q^*e_0
=(1,q,q^2,\ldots).
}
```

This is the canonical causal impulse response of the AR(1) feedback loop.

---

# 3. Transfer function

For the sequence `z`-transform,

```math
\sum_{r>=0}q^rz^r
=\frac1{1-qz}
```

whenever `|qz|<1`.

For a physical delay step

```math
h_p=\log p,
```

the Laplace delay is

```math
z=e^{-sh_p}.
```

Since

```math
q_p=e^{-h_p/2},
```

we obtain

```math
q_pz
=e^{-(s+1/2)h_p}
=p^{-(s+1/2)}.
```

Therefore

```math
\boxed{
\mathcal Z
\left[
\frac1{\sqrt{1-q_p^2}}T_{q_p}^*e_0
\right](e^{-sh_p})
=
\frac1{1-p^{-(s+1/2)}}.
}
```

---

# 4. Logarithmic derivative

The local Euler factor is

```math
\zeta_p(s+1/2)
=(1-p^{-(s+1/2)})^{-1}.
```

Its logarithmic derivative with respect to `s` is

```math
\frac{d}{ds}\log\zeta_p(s+1/2)
=-\log p\,
\frac{p^{-(s+1/2)}}{1-p^{-(s+1/2)}}.
```

Writing `q=p^{-1/2}`, `h=log p` gives

```math
\boxed{
\frac{d}{ds}\log\zeta_p(s+1/2)
=-h\frac{qe^{-sh}}{1-qe^{-sh}}
=-h\left[
\frac1{1-qe^{-sh}}-1
\right].
}
```

Thus the arithmetic transfer in the Lagarias decomposition is the weighted resolvent excess of the adjoint P11-AR(1) loop.

---

# 5. Finite-depth / boundary remainder

For every integer `m>=0`,

```math
\boxed{
\frac1{1-qz}
=
\sum_{r=0}^{m-1}(qz)^r
+
\frac{(qz)^m}{1-qz}.
}
```

The first term is the finite resolved impulse response; the second is one boundary state carrying the unresolved geometric future.

This algebra is the scalar-transfer counterpart of the stopped-OU filtration and its boundary-tail shorting.

Firewall: for a general physical channel sequence `X_k(v)`, the exterior tail is not restricted to this single geometric mode. The positive exterior defect proved in the boundary-shortening audit measures precisely the lost orthogonal directions. Therefore the exact Euler impulse-response truncation does not undo the existing Prime-2 calibration no-go for arbitrary sources.

---

# 6. Euler determinant over the prime loops

For `Re s>1/2`, the diagonal prime operator

```math
Q(s)
=\operatorname{diag}_{p}
\left(p^{-(s+1/2)}\right)
```

is trace class because

```math
\sum_p p^{-Re(s)-1/2}<\infty.
```

Its Fredholm determinant is

```math
\boxed{
\det(I-Q(s))
=\prod_p(1-p^{-(s+1/2)})
=\zeta(s+1/2)^{-1}.
}
```

This determinant formula is simply the Euler product in operator notation and is not a novelty claim.

What is project-specific is that the same scalar resolvent denominator had already appeared from the P11 Cholesky/innovation geometry independently of this determinant notation.

---

# 7. Spatial stopping interpretation

The P11 masks set the visible depth

```math
m_p(x)=\left\lfloor\frac{2(R-|x|)}{\log p}\right\rfloor.
```

Thus, locally in the overlap cone, increasing the radius exposes more coefficients of the same AR(1)/Euler impulse response while retaining a boundary state for the unresolved future.

At `m=0` all information sits in the conditional/root boundary state. Each increase `m -> m+1` releases one new positive OU innovation, matching the finite-depth resolvent expansion.

Again, this is a structural interpretation only: the full Weil form contains source-dependent tail directions beyond the one-dimensional scalar Euler impulse mode.

---

# 8. Next gate

The sharpened constructive problem is now:

```text
Can the locally finite stopped P11/Euler feedback network be coupled to the
continuous pole compensator and higher Gamma filter bank so that the direct
limit has a positive storage realization on Re s>0?
```

The infinite product itself is only trace-class for `Re s>1/2`; extending the positive realization to the larger half-plane is precisely where the RH difficulty remains.
