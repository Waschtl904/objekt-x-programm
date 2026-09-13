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

## 2. COMMON-JUMP `✓[M]`

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

## 3. Exakte zentrierte Weil-Normalform

```math
\Gamma_a
=2\sum_{\log n\le2a}w_n+\log\pi-\psi(1/4).
```

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

Auf Nullpol:

```text
E=0
 |
 v
Q_W|NP = X_a^* X_a - Gamma_a I   ✓[M]
```

`NP-R1`, `NP-COMMON` und die cutoff-Gauge-Struktur sind in diesem Knoten geschlossen/subsumiert.

## 4. Archimedische Kanalzerlegung

```text
h(t) = sum_{m>=0} exp(-alpha_m t)
alpha_m = 2m+1/2
        |
        v
A_alpha = integral exp(-alpha t) K_t^* K_t dt
        |
        v
A_alpha = (2/alpha) L(L+alpha^2)^(-1)   ✓[M]
```

mit `L=-d^2/dx^2`.

## 5. Exakter Q0-First-Channel-Knoten `✓[M]`

```text
Q0 = L + 1/4
alpha_0 = 1/2
        |
        v
A_{1/2} = 4I - Q0^(-1)
        |
        v
A_{1/2} Q0 = 4L = -4 d^2/dx^2
```

Für `alpha>0` cancelt der Resolventennenner in `A_alpha Q0` nur bei `alpha=1/2`.

## 6. Support-preserving null-pole edge `✓[M]`

```text
Green kernel Q0^(-1): exp(-|x-y|/2)
        |
        +--> right tail = exp(-x/2) E_+(v)
        +--> left tail  = exp(+x/2) E_-(v)
        |
        v
E_+=E_-=0
        |
        v
Q0 : C_c^infty(-a,a)  <-->  D_NP(a)   support preserving
```

Damit wird der erste nichtlokale Kanal nach `v=Q0u` lokal:

```math
\langle v,A_{1/2}v\rangle
=4\|u''\|^2+\|u'\|^2.
```

## 7. Quantitative Coercivity edges

Nullpol + Dirichlet-Poincaré:

```math
\langle v,A_{1/2}v\rangle
\ge
\frac{4\pi^2}{\pi^2+a^2}\|v\|^2.
```

Jeder höhere Kanal + Schur-Test:

```math
\langle v,A_\alpha v\rangle
\ge
\frac{2}{\alpha}e^{-\alpha a}\|v\|^2.
```

Beide Kanten sind `✓[M]` und verwenden keine Weil-Positivität als Input.

## 8. Short-window NP-GAP `✓[M]_part`

```text
first-channel null-pole coercivity
        +
higher-channel Schur bounds
        |
        v
B(a) = 4pi^2/(pi^2+a^2)
       + sum_{m>=1} (2/alpha_m) exp(-alpha_m a)
        |
        v
B(a) >= kappa_* on a nonempty short-window interval
        |
        v
||X_a v||^2 >= Gamma_a ||v||^2 on D_NP(a)
        |
        v
NP-GAP short-window ✓[M]_part
```

Die Prime-Summe ist in diesem Bereich noch leer (`2a<log2`).

## 9. Verbleibender Hauptpfad

```text
COMMON-JUMP positive geometry ✓[M]
        |
        v
Q0 first-channel intertwining ✓[M]
        |
        v
short-window NP-GAP ✓[M]_part
        |
        | extend coercivity through all windows / prime thresholds
        v
NP-GAP for every a>0 ?[O]
        |
        v
global null-pole Weil positivity
        |
        v
RH
```

## 10. Numerik-Firewall

```text
finite-dimensional null-pole space V_N
        |
        v
Ritz minimum lambda_NP^(N)(a)
        |
        v
lambda_NP^(N)(a) >= true lambda_NP(a)
```

Also: positive endliche Ritz-Gaps sind keine Beweise; ein zertifizierter Wert unter der Schwelle wäre dagegen ein Falsifikator.

## 11. Auxiliary edges

```text
OX-GEN-A -> exact pole-layer geometry
POS-DIL #101-#105 -> auxiliary full-class route
Prime AR(1) -> independent positive structure
```

PR #91, PR #49 und R37/G4c bleiben separat.

## 12. Firewalls

- short-window gap != all-`a` gap;
- exact Q0 intertwining != RH;
- common geometry != vollständige positive Objekt-X-Realisierung;
- global null-pole criterion != fixed-window criterion;
- publication novelty `?[O]`;
- Registry unchanged.