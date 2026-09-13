# Abhängigkeitsgraph (DAG) — Objekt X / NP-OVERLAP-AR1

> **Stand:** 13. September 2026; Registry unverändert.

## 1. COMMON-JUMP

```text
D_NP = ker M(0) ∩ ker M(1)
        |
        v
Q_W|NP = X_a^*X_a - Gamma_a I            ✓[M]
        |
        v
Q_W = A_arch - O_a                        ✓[M]
```

mit

```math
O_a(v)=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}Re\langle T_{\log n}v,v\rangle.
```

## 2. Q0/Gamma edge

```text
A_alpha=(2/alpha)L(L+alpha^2)^(-1)        ✓[M]
        |
alpha=1/2, Q0=L+1/4
        |
        v
A_{1/2}Q0=4L                              ✓[M]
Q0 : C_c^infty(-a,a) <-> D_NP(a)          ✓[M]
```

Higher channels:

```text
compressed resolvent + Schur
        |
        v
A_alpha >= (2/alpha)e^{-alpha a}I         ✓[M]
```

## 3. Single-shift fiber node

```text
S_t=(T_t+T_-t)/2 on (-a,a)
        |
fiberize modulo t
        |
path graph P_N, N<=ceil(2a/t)
        |
        v
||S_t||=cos(pi/(ceil(2a/t)+1))            ✓[M]
```

The top eigenvalue has infinite multiplicity through the residue parameter. Two null-pole moment constraints can be imposed inside that top eigenspace:

```text
D_NP restriction
        |
        v
same sharp single-shift norm               ✓[M]
        |
        v
single-shift null-pole improvement          ×[M]
```

Therefore no main edge remains from independent single-shift norm bounds.

## 4. Group by prime

```text
p fixed, ell_p=log p, q_p=p^(-1/2)
        |
all powers p^k in O_a
        |
fiberize modulo ell_p
        |
        v
O_{p,a}^{(N)}=(log p)(R_q^(N)-I_N)         ✓[M]
```

where

```math
R_q^{(N)}=(q^{|j-k|})_{j,k}.
```

This is exactly the Prime-Power AR(1)/KMS matrix.

## 5. Positive AR(1) sector

```math
P_q(theta)-1
=\frac{2q(\cos\theta-q)}{1-2q\cos\theta+q^2}.
```

```text
positive iff cos(theta)>q
        |
        v
|theta|<arccos(q) mod 2pi                  ✓[M]
```

Thus the dangerous p-block directions are low frequencies on the `log p` lattice.

## 6. Multi-prime main edge

For distinct primes:

```math
log p/log r notin Q.                        ✓[M]
```

Hence:

```text
positive low-frequency sector on log 2 lattice
positive low-frequency sector on log 3 lattice
positive low-frequency sector on log 5 lattice
                ...
                 |
                 | incommensurable lattices
                 v
simultaneous concentration bound ?[O]
                 |
                 v
sum_p O_{p,a} <= A_infty-kappa_* I ?[O]
                 |
                 v
RH
```

This is the new default Object-X path.

## 7. Reconnect to old AR(1)

The earlier project node

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}
```

now connects directly to the exact overlap fibers. The open edge is quantitative: convert the known AR(1)/Markov/Weil-tail factorization into a collective multi-prime suppression inequality.

## 8. Side nodes

- Short-window COMMON-JUMP/Q0 coercivity `✓[M]_part`, but novelty claim `×[M]`.
- Arb `a_*` certificate = side gate.
- Finite Gamma-null ladder = structurally valid auxiliary route.
- Registry unchanged.
