# X-C0 — RH-equivalent Critical-half bound for the prime-base transport displacement

**Datum:** 16. September 2026  
**Basis:** exact transport+P11-tail decomposition of `J_Delta`; critical asymptotic of the unresolved P11 Boundary tail.  
**Registry:** unverändert.  
**External classical input:** von-Koch/Chebyshev formulation `RH iff psi(x)=x+O(sqrt(x) log^2 x)`.  
**Nonclaim:** dies ist eine Reformulierung eines klassischen RH-Fehlerkriteriums in der projektspezifischen Transportgeometrie, kein neuer RH-Beweis und kein Publikationsneuheitsclaim.

---

## 0. Result

Define the prime-base transport displacement

```math
\boxed{
 d_{tr}(L)
 :=L-\gamma-
 \sum_{p<e^L}\frac{\log p}{p-1}.
}
```

Then

```math
\boxed{
RH
\iff
 d_{tr}(L)
 =O(e^{-L/2}L^2)
\qquad(L\to\infty).
}
```

Equivalently, after Critical-half amplification,

```math
\boxed{
RH
\iff
 e^{L/2}d_{tr}(L)=O(L^2).
}
```

Thus the sole signed scalar left unresolved by the positive P11 Boundary-tail geometry is not merely `RH-like`: its Critical-half growth bound is exactly equivalent to RH.

The proof uses only:

```text
- classical von-Koch criterion for psi(x);
- Stieltjes/Abel partial summation;
- the already proved unconditional tail estimate
  T(log x)=O(x^-1/2).
```

Status:

```text
RH <-> weighted full Mangoldt reciprocal error        classical / derived here
prime-base vs full p-power difference O(x^-1/2)      ✓[K/M]
RH <-> Critical-half prime-base displacement bound   ✓[K/M]
new RH theorem                                        NO
```

---

# 1. Full Mangoldt reciprocal sum

Put

```math
A(x):=\sum_{n\le x}\frac{\Lambda(n)}n.
```

Let

```math
\psi(x)=\sum_{n\le x}\Lambda(n).
```

Stieltjes partial summation gives

```math
\boxed{
A(x)
=\frac{\psi(x)}x
+\int_{1^-}^{x}
\frac{\psi(t)}{t^2}dt.
}
```

The lower-end convention only changes an absolute constant and is absorbed by the standard finite-part constant `-gamma` below.

Classically,

```math
A(x)-\log x\longrightarrow-\gamma.
```

Write

```math
R_A(x)
:=A(x)-\log x+\gamma.
```

---

# 2. RH implies the reciprocal-sum bound

Under RH, the classical von-Koch estimate is

```math
\boxed{
\psi(x)-x
=O(\sqrt x\log^2x).
}
```

Write

```math
E_\psi(x)=\psi(x)-x.
```

Subtracting the main term in the partial-summation formula and using the limiting constant gives

```math
R_A(x)
=\frac{E_\psi(x)}x
-
\int_x^\infty
\frac{E_\psi(t)}{t^2}dt.
```

Hence

```math
\frac{E_\psi(x)}x
=O(x^{-1/2}\log^2x),
```

and

```math
\int_x^\infty
O(t^{-3/2}\log^2t)dt
=O(x^{-1/2}\log^2x).
```

Therefore

```math
\boxed{
RH
\Longrightarrow
A(x)
=\log x-\gamma
+O(x^{-1/2}\log^2x).
}
```

---

# 3. Reciprocal-sum bound implies von-Koch

Conversely assume

```math
A(x)
=\log x-\gamma
+O(x^{-1/2}\log^2x).
```

Since

```math
dA(t)=\frac1t\,d\psi(t),
```

Stieltjes summation in the reverse direction gives

```math
\boxed{
\psi(x)
=xA(x)-\int_{1^-}^xA(t)dt+O(1).
}
```

Insert

```math
A(t)=\log t-\gamma+R_A(t).
```

The main terms give `x+O(1)`. The error is

```math
xR_A(x)-\int_1^xR_A(t)dt.
```

Now

```math
xR_A(x)
=O(\sqrt x\log^2x),
```

while

```math
\int_1^x
O(t^{-1/2}\log^2t)dt
=O(\sqrt x\log^2x).
```

Thus

```math
\boxed{
\psi(x)
=x+O(\sqrt x\log^2x).
}
```

By the classical von-Koch criterion this is equivalent to RH.

Consequently

```math
\boxed{
RH
\iff
A(x)=\log x-\gamma
+O(x^{-1/2}\log^2x).
}
```

---

# 4. Replace the full prime-power sum by the prime-base transport mass

Define

```math
B(x)
:=\sum_{p<x}\frac{\log p}{p-1}.
```

For non-threshold `x=e^L`, the preceding stopped-P11 theorem gives exactly

```math
\boxed{
B(x)-A(x)=T(L),
}
```

up to the harmless chosen `<`/`<=` endpoint convention, where

```math
T(L)
=\sum_{p<e^L}
\frac{(\log p)p^{-\lfloor L/\log p\rfloor}}{p-1}
```

is the unresolved safe P11 Boundary-tail mass.

The preceding asymptotic theorem proves

```math
\boxed{
e^{L/2}T(L)\to1.}
```

In particular

```math
\boxed{T(\log x)=O(x^{-1/2}).}
```

Therefore

```math
A(x)=\log x-\gamma+O(x^{-1/2}\log^2x)
```

if and only if

```math
B(x)=\log x-\gamma+O(x^{-1/2}\log^2x).
```

---

# 5. Convert to the transport coordinate

By definition

```math
 d_{tr}(L)
 =L-\gamma-B(e^L).
```

Set `x=e^L`. Then

```math
x^{-1/2}\log^2x
=e^{-L/2}L^2.
```

Hence Section 4 yields

```math
\boxed{
RH
\iff
 d_{tr}(L)
 =O(e^{-L/2}L^2).
}
```

Multiplying by `e^(L/2)` gives the equivalent Critical-half form

```math
\boxed{
RH
\iff
 e^{L/2}d_{tr}(L)
 =O(L^2).
}
```

---

# 6. Relation to `J_Delta`

The exact project identity is

```math
 e^{-L/2}J_\Delta(L)
 =d_{tr}(L)+T(L).
```

Since

```math
 e^{L/2}T(L)\to1,
```

one has

```math
\boxed{
J_\Delta(L)
=e^{L/2}d_{tr}(L)+1+o(1).
}
```

Thus the polynomial-growth RH condition for the causal arithmetic transfer `J_Delta` and the Critical-half transport-displacement condition differ only by an asymptotically universal positive P11 Boundary contribution.

This explains geometrically why the higher prime powers are not the hard continuation channel.

---

# 7. Architecture consequence

The Hard Audit has now separated the global problem into:

```text
P11 unresolved p-power Boundary tails:
  positive, explicitly realized, Critical-half normalized limit = 1;

prime-base monotone transport displacement:
  signed, exact, and its Critical-half O(L^2) bound is RH-equivalent.
```

Therefore a putative Object-X parent does **not** need a new mechanism for higher p-power tails. It needs a positive/conservative mechanism whose internal cancellation controls precisely the oriented prime-base transport displacement.

The lossless supply audit realizes this displacement as an Off-Diagonal port, but does not prove the required OUT>=IN inequality.

The remaining C1 question is thus genuinely equivalent in difficulty to RH; no elementary tail estimate can close it.

---

# 8. Literature firewall

The equivalence

```math
RH\iff\psi(x)=x+O(\sqrt x\log^2x)
```

is classical (von Koch; later explicit constants due to Schoenfeld).

The weighted reciprocal-sum form follows by elementary partial summation, and replacing the complete Mangoldt reciprocal sum by the prime-base mass uses the project-specific exact stopped-P11 tail decomposition plus its unconditional `x^-1/2` asymptotic.

No novelty is claimed for the classical prime-number-theorem error criterion. The project-specific value is the identification of its entire hard term with the signed displacement of the already constructed positive root-mass transport.

No Registry change.
