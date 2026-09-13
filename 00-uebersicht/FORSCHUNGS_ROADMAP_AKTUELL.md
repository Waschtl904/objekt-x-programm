# Objekt X — kanonische Forschungsroadmap v3.6

> **Stand:** 13. September 2026; Registry und Arbeitsdefinition unverändert.

## Gate C0 — Gesicherte Architektur

```text
COMMON-JUMP / Q0                    ✓[M]
centered Prime-overlap              ✓[M]
per-prime AR(1) fibers             ✓[M]
```

Auf Nullpol ist `Q_W=q_a` mit

```math
q_a=X_a^*X_a-\Gamma_a I,
\qquad
D_{NP}(a)=\ker\mathcal E,
\qquad
\mathcal E=(E_+,E_-).
```

## Gate C1 — Screw redundancy `✓[M] / ×[M]`

Die pole-cleared Diskrepanz ist der Prime+Polar-Ableitungsblock von Suzukis Screw-Funktion:

```math
\mathfrak D=(g_0+r_0)'.
```

Die Identität bleibt gültig; Neuheit des arithmetischen Objekts ist `×[M]`.

## Gate C2 — Autocorrelation relaxation

Nullpol erzeugt zwei notwendige lineare Autokorrelationsbedingungen

```math
L_0(C)=0,
\qquad
L_1(C)=0,
```

aber sie charakterisieren `E_+=E_-=0` auf Faktorebene nicht.

```text
scalar Turan relaxation as sufficient certificate   allowed
scalar Turan relaxation as exact equivalence        ×[M]
```

## Gate C3 — Exact finite-rank completion `✓[M]`

### strict coercive equivalence

```math
\boxed{
q_a\ge\delta I\text{ on }\ker\mathcal E
\iff
\exists\lambda,\mu>0:
q_a+\lambda\mathcal E^*\mathcal E\succeq\mu I.
}
```

### semidefinite exact equivalence

```math
\boxed{
q_a\ge0\text{ on }\ker\mathcal E
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon\mathcal E^*\mathcal E\succeq0.
}
```

Ein general Hermitian `2x2` block may be optimized; scalar `lambda I` already suffices for existence in the strict theorem.

## Gate C4 — Morse-index filters `✓[M]`

For any Hermitian completion `H`:

```math
q_a+\mathcal E^*H\mathcal E\succeq0
\Longrightarrow
n_-(q_a)\le n_+(H)\le2.
```

Hence

```text
certified n_-(q_a) >= 3  => no rank-2 NP completion
```

For the physical pole matrix

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

one has `n_+(P)=1`, so

```text
Q_W^a >= 0 => n_-(q_a) <= 1.
```

A certified second negative direction therefore rules out the physical `P`-completion at that fixed window.

## Gate C5 — Reflection/parity reduction `✓[M]`

Reflection exchanges `E_+` and `E_-`. Any valid Hermitian completion can be averaged with its reflection, so only

```math
H=\begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix}
```

with real `alpha,beta` need be considered.

In even/odd moment coordinates:

```math
H\sim\operatorname{diag}(h_e,h_o),
\qquad
P\sim\operatorname{diag}(+1,-1).
```

Thus the optimized dual has only two real parameters.

If the physical Weil form is positive, the odd sector of `q_a` is automatically nonnegative and every negative direction of `q_a` is even.

## Gate C6 — Canonical candidate `lambda=1` `✓[M]`

```math
\boxed{
q_a+\mathcal E^*\mathcal E
=Q_W^a+\mathcal E^*(I-P)\mathcal E,
\qquad I-P\succeq0.
}
```

Therefore physical fixed-window Weil positivity would automatically imply the scalar completion `lambda=1`.

`lambda=1` is the first **predeclared** completion candidate for `a=1`, not a fitted parameter.

## Gate C7 — Non-certified `a=1` diagnostic

Predeclared nested Dirichlet basis:

```math
\phi_n(x)=\sin\left(\frac{n\pi(x+1)}2\right),
\qquad -1<x<1.
```

Observed restricted Ritz minima:

```text
N=4    ~8.22e-4
N=6    ~6.21e-7
N=8    ~3.26e-9
N=10   ~2.70e-9
N=12   ~6.67e-11
```

At `N=12`, the full `q_1` block displayed one numerical negative direction, in the even sector, and the scalar completion crossed numerical PSD at `lambda≈1`.

**No strict status:** floating-point quadrature, finite Fourier cutoff, no Arb matrix enclosure, no infinite-dimensional tail.

## Gate C8 — Rigorous A1-CERT `?[O]`

Correct external benchmark:

> Marcus Chuk, arXiv:2608.24827, certifies full-class positivity at `L=0.8` with lower bound `8.9e-18` and documents Landau--Widom decay / doubly-exponential envelope barriers.

The first natural stress point beyond that published lower-bound radius is

```text
a_test=1.0.
```

Required theorem certificate:

1. predeclared parity-adapted basis/truncation;
2. Arb form entries and moment rows;
3. test `lambda=1` first, otherwise optimize only two parity dual parameters;
4. certified finite inertia/PSD;
5. rigorous tail lower bounds in even and odd sectors;
6. rigorous resolved-tail coupling bound;
7. final Schur-complement positivity.

The dual dimension is **not** the bottleneck. The unresolved infinite-dimensional tail is.

## Gate C9 — all-window completion `?[O]`

```text
fixed-a exact completion certificates
        |
uniform/structural tail mechanism
        |
all-a NP-GAP
        |
global restricted Weil criterion
        |
RH
```

Landau--Widom remains calibration for tiny gaps; it is not itself the missing tail certificate.

## Auxiliary

- scalar Turán/Fejer--Riesz = sufficient relaxation / exploratory dual;
- pole-cleared discrepancy = canonical gauge but literature-known Prime+polar component;
- AR(1) = independent local structure;
- Prolate = extremal/falsification calibration.

## Firewalls

- do not claim `D` is new;
- do not identify scalar autocorrelation moments with exact null-pole constraints;
- do not promote the `a=1` Galerkin numbers;
- do not call finite PSD exact without tail control;
- fixed-window positivity is not RH-equivalent;
- Registry/Arbeitsdefinition unchanged.
