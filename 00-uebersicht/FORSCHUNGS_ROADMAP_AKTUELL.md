# Objekt X — kanonische Forschungsroadmap v3.5

> **Stand:** 13. September 2026; Registry unverändert.

## Gate C0 — Gesicherte Architektur

```text
COMMON-JUMP / Q0                    ✓[M]
centered Prime-overlap              ✓[M]
per-prime AR(1) fibers             ✓[M]
```

Auf Nullpol ist `Q_W=q_a` mit `q_a=X_a^*X_a-Gamma_a I`.

## Gate C1 — Screw redundancy `✓[M] / ×[M]`

Die pole-cleared Diskrepanz ist der Prime+Polar-Ableitungsblock von Suzukis Screw-Funktion:

```math
D=(g_0+r_0)'.
```

Die Identität bleibt gültig; Neuheit des arithmetischen Objekts wird verworfen.

## Gate C2 — Autocorrelation relaxation

Nullpol erzeugt zwei notwendige lineare Autokorrelationsbedingungen

```math
L_0(C)=0,
\qquad
L_1(C)=0.
```

Sie sind nicht hinreichend für `E_+=E_-=0` auf Faktorebene.

```text
scalar Turan relaxation as sufficient certificate      allowed
scalar Turan relaxation as exact equivalence           ×[M]
```

## Gate C3 — Exact finite-rank completion `✓[M]`

Mit `E=(E_+,E_-)`:

### strict

```math
q_a\ge\delta I\text{ on ker E}
\Longrightarrow
\exists\lambda>0:\ q_a+\lambda E^*E\succeq0.
```

### semidefinite

```math
q_a\ge0\text{ on ker E}
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon E^*E\succeq0.
```

A general Hermitian `2x2` completion may be optimized, but scalar `lambda I` already suffices for existence in the strict theorem.

## Gate C4 — Pole matrix relation

The actual Weil pole block is

```math
E^*PE,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

`H=P` would certify the full fixed-window Weil form. Existence of some completion `H` is weaker and only certifies null-pole positivity.

## Gate C5 — Rigorous fixed-window SDP `?[O]`

Target first:

```text
a_test = 1.0
```

because certified full-class literature positivity already reaches `a=0.8`.

Required:

1. predeclared basis/truncation;
2. Arb matrix entries and exact moment rows;
3. optimize `H=H*` or scalar `lambda`;
4. certify resolved PSD;
5. certify the unresolved tail / Schur complement.

A finite positive Ritz matrix without tail control is not a theorem.

## Gate C6 — all-window completion `?[O]`

```text
fixed-a exact completion certificates
        |
uniform/structural mechanism for every a
        |
all-a NP-GAP
        |
global restricted Weil criterion
        |
RH
```

Landau--Widom remains calibration for expected tiny gaps; it is not itself the missing certificate.

## Auxiliary

- scalar Turán/Fejer--Riesz = sufficient relaxation / exploratory dual;
- pole-cleared discrepancy = canonical gauge but literature-known Prime+polar component;
- AR(1) = independent local structure;
- Prolate = extremal/falsification calibration.

## Firewalls

- do not claim `D` is new;
- do not identify scalar autocorrelation moments with exact null-pole factor constraints;
- do not call finite SDP exact without tail control;
- fixed-window positivity is not RH-equivalent;
- Registry/Arbeitsdefinition unchanged.
