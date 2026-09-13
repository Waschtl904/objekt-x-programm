# Abhängigkeitsgraph (DAG) — Objekt X / NP-DISCREPANCY

> **Stand:** 13. September 2026; Registry unverändert.

## 1. Gesicherte Kette

```text
D_NP = ker M(0) ∩ ker M(1)
        |
        v
Q_W = A_arch - O_a                         ✓[M]
        |
        +--> per-prime AR(1) fibers       ✓[M]
        +--> Q0 support map               ✓[M]
```

## 2. Methodische Sackgassen

```text
independent single-shift norms
        |
        | near-boundary shifts have norm 1/2
        v
scalar budget >= 2 e^a(1+o(1))            ×[M] for all-window proof
```

```text
raw Prime multiplier ~ e^a
        +
constant Prolate concentration factor
        |
        v
same exponential scale                       ×[M] as sufficient mechanism
```

## 3. Null-pole correlation gauge

```text
E_+=E_-=0
        |
        v
integral exp(t/2) C_v(t) dt = 0
        |
real part
        v
integral_0^{2a} 2 cosh(t/2) Re C_v(t) dt = 0   ✓[M]
```

## 4. Pole-cleared Prime measure

```text
dnu = sum Lambda(n)/sqrt(n) delta_log n
        |
subtract 2 cosh(t/2) dt using null-pole gauge
        v
dD = dnu - 2 cosh(t/2) dt                    ✓[M]
```

and

```math
O_a(v)=2\int Re C_v(t)dD(t).
```

Cumulative form:

```math
D(T)=\sum_{\log n\le T}\frac{\Lambda(n)}{\sqrt n}-4\sinh(T/2).
```

PNT main exponential cancels.

## 5. Stieltjes separation

```text
C_v(2a)=0, D(0)=0
        |
        v
O_a(v)=-2 integral_0^{2a} D(t) d/dt Re C_v(t) dt   ✓[M]
```

```text
arithmetic side = D(t)
analytic side   = derivative of positive-definite compact-support autocorrelation
```

## 6. Pole-cleared zeta fingerprint

For `Re s>1/2`:

```math
L[dD](s)
=-zeta'/zeta(s+1/2)-1/(s-1/2)-1/(s+1/2)
```

```text
        |
        v
-d/ds log[(s^2-1/4) zeta(s+1/2)]           ✓[M]
```

The subtraction is exactly the `z=0,1` pole pair.

## 7. RH-hard scale firewall

```text
RH -> D(T)=O(T^3)
polynomial D(T)=O(T^K) for some fixed K -> RH
```

Status: imported/classical bridge `✓[K/M]`.

Therefore the next edge cannot be a mere absolute polynomial estimate for `D`.

## 8. New main edge

```text
pole-cleared D(t)
        +
positive-definite C_v with null-pole constraint
        |
        v
structured anti-correlation / signed pairing bound ?[O]
        |
        v
A_arch >= O_a on D_NP(a) for every a ?[O]
        |
        v
RH
```

AR(1), Q0 and centered Prolate/Toeplitz methods feed into this edge as auxiliary mechanisms.

## 9. Firewalls

- raw Prime amplitude is no longer the canonical arithmetic object;
- independent block norms remain excluded;
- Prolate is allowed only after arithmetic centering, not as a raw constant-factor cure;
- Registry unchanged.
