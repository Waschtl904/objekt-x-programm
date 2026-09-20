> [!WARNING]
> **HISTORICAL SNAPSHOT — nur die operative Navigation ist ersetzt.**
>
> As of: 2026-09-14
> Nicht zur Bestimmung der aktuellen Forschungsfront verwenden.
> Kanonischer Status: [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml).
> Lesbarer Einstieg: [CURRENT_STATE.md](CURRENT_STATE.md).
> Der folgende Originalinhalt bleibt als Provenienz unverändert erhalten.
> Mathematische Inhalte werden durch diesen Hinweis nicht pauschal verworfen.

# Abhängigkeitsgraph (DAG) — Objekt X / A1-FINITE-1104

> **Stand:** 14. September 2026; Registry und Arbeitsdefinition unverändert.

## Closed base

```text
COMMON-JUMP / Q0 ✓[M]
   |
rank-2 completion / Morse / parity ✓[M]
   |
canonical lambda=1 ✓[M]
   |
exact a=1 multiplier ✓[M]
   |
Omega1551: m_1>0.1, ||r||<12 ✓[K/M]
```

## Canonical PSWF branch

```text
Osipov Theorem 4
|lambda_n^F| <= nu(n,c)
mu_n = c|lambda_n^F|^2/(2pi)
   |
predeclared c=1551, N=1102
   |
mu_1102 <1e-43
tau >0.099
Schur penalty <1.5e-40          ✓[K/M]
   |
R_1102 dimension <=1104
   |
certify L_RR >=3e-39 I          ?[O]
```

## Independent Legendre branch

```text
orthonormal Legendre M=2150
   |
Gram I / exact parity
   |
tail/cross ✓[K/M]
quadrature op error <4e-38 ✓[K/M]
   |
1075 even +1075 odd
certify each block >=1e-35 I    ?[O]
```

## A1 closure

```text
PSWF finite gate ?[O]
      OR
Legendre finite gate ?[O]
       |
       v
canonical a=1 completion ?[O]
```

## Global path

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

## Firewalls

- No PSWF eigenvectors are numerically needed for the Osipov bound.
- `3e-39` and `1e-35` are sufficient thresholds, not fitted eigenvalues.
- Fixed-window `a=1` and RH are not proved.
