# Abhängigkeitsgraph (DAG) — Objekt X / A1-FINITE

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## 1. Closed base

```text
COMMON-JUMP / Q0 ✓[M]
        |
rank-2 completion / Morse / parity ✓[M]
        |
canonical lambda=1 ✓[M]
        |
exact a=1 Fourier multiplier ✓[M]
        |
Omega1551 high-frequency certificate ✓[K/M]
```

## 2. Canonical PSWF branch

```text
bounded band r, ||r||<12
        |
moment-augmented PSWF split
        |
KRD lambda_1210<1.5e-42
        |
Schur penalty <2.2e-39                     ✓[K/M]
        |
        v
R_1210 dimension <=1212
certify L_RR >=3e-39 I                     ?[O]
```

This remains the **canonical smaller finite reduction**.

## 3. Alternative Legendre branch

```text
orthonormal T_n=sqrt(n+1/2) P_n
        |
Gram I + exact parity + spherical-Bessel Fourier form
        |
M=2150 Legendre tail/cross certificate              ✓[K/M]
        |
1075 even + 1075 odd blocks, target 1e-35
```

## 4. Legendre quadrature edge

```text
analytic continuation of Re psi
        +
strip |Im xi|<=0.4
        +
|r(z)|<42
        +
|j_n(z)|<=exp(|Im z|)
        |
        v
full matrix integrand <260000
        |
width<=0.4 panels + Gauss q=40
rho=2+sqrt(5)
        |
        v
per-entry error <3.678e-41
        |
        v
parity operator quadrature error <4e-38          ✓[K/M]
```

Hence analytic quadrature truncation is already far below the `1e-35` finite-head target.

## 5. Remaining Legendre edge

```text
assemble 1075x1075 even/odd matrices
        +
rigorous special-function/rounding enclosure
        +
verified LDL/Cholesky residual
        |
        v
A_even >=1e-35 I and A_odd >=1e-35 I             ?[O]
```

## 6. A1 closure

```text
PSWF finite gate ?[O]
       OR
Legendre finite gate ?[O]
        |
        v
canonical a=1 completion ?[O]
```

No separate infinite-dimensional tail or crossblock problem remains on either certified route.

## 7. Global path

```text
a=1 completion
   |
further windows / structural scaling
   |
all-a NP-GAP
   |
restricted Weil criterion
   |
RH
```

## 8. Firewalls

- Legendre quadrature budget does not prove finite PSD.
- Pivot intervals containing zero are undecided.
- PSWF route remains canonical/smaller.
- Fixed-window a=1 and RH are not proved.
