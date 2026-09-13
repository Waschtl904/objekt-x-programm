# Abhängigkeitsgraph (DAG) — Objekt X / COMMON-JUMP → NP-GAP

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Nullpol-Filter

```text
E_-(v)=M(v)(0), E_+(v)=M(v)(1)
        |
        v
D_NP = ker M(0) ∩ ker M(1)
        |
        v
R_0 = 0, E = 0
```

Globaler Criterion-Import:

```text
Connes–Consani Prop. C.1
        |
        v
global Weil sign criterion on D_NP
        <=> RH
```

Keine Kante `fixed a <=> RH`.

## 2. Eine gemeinsame Operatorfamilie

```math
K_t=T_{t/2}-T_{-t/2},
\qquad
K_t^*K_t=2I-T_t-T_{-t}.
```

```text
                        K_t
                     /       \
                    /         \
                   v           v
archimedean h(t)dt             prime atoms w_n delta_log n
continuous feature energy      discrete feature energies
                   \           /
                    \         /
                     v       v
                X_a^* X_a >= 0   ✓[M]
```

mit

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}.
```

## 3. Exakte Schwelle

```text
gamma-factor scalar log(4pi)+gamma
        +
2 integral h(t)(1-e^{-t/2}) dt
        |
        v
kappa_* = log pi - psi(1/4)
```

Prime-Diagonalledger:

```math
2\sum_{\log n\le2a}w_n.
```

Daher

```math
\Gamma_a
=2\sum_{\log n\le2a}w_n+\log\pi-\psi(1/4).
```

## 4. Exact COMMON-JUMP normal form

```text
pole block <Ev, P Ew>
        +
positive common Gram <X_a v, X_a w>
        -
Gamma_a <v,w>
        |
        v
Q_W(v,w) exactly, all a>0   ✓[M]
```

Restriktion auf Nullpol:

```text
E=0
 |
 v
Q_W|NP = X_a^* X_a - Gamma_a I   ✓[M]
```

## 5. Frühere offene Knoten werden subsumiert

```text
NP-R1 ?[O] -----> continuous K_t channel -----> closed/subsumed ✓[M]
NP-COMMON ?[O] -> mixed common measure --------> ✓[M]
NP-SCALAR ?[O] -> Gram/threshold covariance ---> ✓[M] (structural)
```

Die scharfe Schwellenungleichung bleibt offen.

## 6. Cutoff-Gauge edge

Für `0<a<b` und `supp v,w subset [-a,a]`:

```text
new prime atom, 2a<log n<=2b
        |
        v
<K_log n v,K_log n w> = 2<v,w>
        |
        +---------------------------+
        |                           |
        v                           v
Gram increases by 2w_n I     Gamma increases by 2w_n
        |                           |
        +-------------+-------------+
                      v
centered form unchanged ✓[M]
```

Damit ist die frühere Exterior-shell-Gauge ein Spezialfall der Common-Jump-Kovarianz.

## 7. Neuer Hauptpfad

```text
COMMON-JUMP positive geometry ✓[M]
        |
        v
forward Object-X architecture ✓[M]_part
        |
        v
NP-GAP ?[O]
        |
        | prove lambda_NP(a) >= Gamma_a for all a
        v
global null-pole Weil positivity
        |
        v
RH
```

## 8. NP-GAP Unterpfade

```text
null-pole moments
M(v)(0)=M(v)(1)=0
        |
        +--> support-preserving Q_0=-d^2/dx^2+1/4 factorization
        |
        +--> Fourier zeros at z=±i/2
        |
        +--> nonlocal Poincare / frame / Paley-Wiener tests
        |
        v
sharp lower bound for X_a^*X_a ?[O]
```

Keine Weil-Positivität darf als Input in diese Kante zurückgeschleift werden.

## 9. Auxiliary edges

```text
OX-GEN-A -> exact pole-layer geometry
POS-DIL #101-#105 -> auxiliary full-class route
Prime AR(1) -> independent positive structure
```

PR #91, PR #49 und R37/G4c bleiben separat.

## 10. Firewalls

- common geometry != sharp frame bound;
- exact difference-of-Gram-and-threshold != positive Weil-Gram realization;
- global null-pole criterion != fixed-window criterion;
- publication novelty `?[O]`;
- Registry unchanged.