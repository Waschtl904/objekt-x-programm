# Abhängigkeitsgraph (DAG) — Objekt X / NULLPOL-CORE

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Basis

```text
Prime-Power AR(1) / Weil-Tail
fixed-pair Strong Terminal / C6
local Suzuki/OX-GRAM normal form
```

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

## 2. Pole-functionals identification

```text
E_-(v) = M(v)(0)
E_+(v) = M(v)(1)
        |
        v
D_NP = ker M(0) ∩ ker M(1)
        |
        +----------------------+
        |                      |
        v                      v
R_0 = 0                    E^*E = 0
```

Status: exact `✓[M]`.

## 3. Imported global criterion edge

```text
Connes–Consani Prop. C.1
finite F ⊃ {0,1}, F ∩ Z = ∅
        |
        | imported theorem
        v
global Weil sign criterion on functions vanishing on F
        ⇔
RH
```

**No edge:** `fixed a null-pole positivity ⇔ RH` is **not** asserted.

## 4. Strategic filter

```text
candidate mechanism
        |
        | restrict to D_NP
        v
nontrivial? ---------------- no ---> auxiliary only
   |
  yes
   |
   v
eligible for Object-X main-front edge
```

This filter is binding for future research prioritization.

## 5. OX-GEN-A / POS-DIL after filter

```text
OX-GEN-A common generator plane ✓[M]
        |
        | target is R_0 / E-mass
        v
restrict to D_NP
        |
        v
zero
```

Therefore:

```text
OX-GEN-A -> AUX pole-layer structure
```

The same applies strategically to the POS-DIL chain #101--#105. Their mathematical statements remain valid.

```text
#101 Prime-moment Hilbertization
  ↓
#102 full-class unit-gain No-Go
  ↓
#103 exterior shell
  ↓
#104 radius domination
  ↓
#105 exact cutoff gauge + R_0 absorption
  ↓
AUX-POS-DIL [preserved]
```

No automatic Object-X main-front edge remains from this chain.

## 6. Null-pole local normal form

On the local null-pole subspace:

```math
\boxed{
Q_{B_a}|_{NP}=G_a^+|_{NP}-c_aI-R_1|_{NP}.
}
```

Thus the active exact remainder is

```text
positive Prime/log|D| geometry
        minus
scalar ledger + R_1
```

## 7. Current main-front DAG

```text
NULLPOL-CORE
    |
    +--> NP-R1 ?[O]
    |      |
    |      +--> kernel / parity / generator structure
    |      +--> natural class construction or No-Go
    |
    +--> NP-SCALAR ?[O]
    |      |
    |      +--> canonical Suzuki gauge
    |      +--> gauge-invariant remainder
    |
    +--> NP-COMMON ?[O]
           |
           | common nontrivial mechanism on D_NP
           v
      genuine X candidate ?[O]
           |
           v
      exact Weil-Gram identity on RH-equivalent class ?[O]
           |
           v
      Object-X realization ?[O]
           |
           v
      criterion-scope verification ?[O]
           |
           v
          RH
```

## 8. Gauge side edge

PR #105 remains an exact identity:

```text
outer Prime channels
    |
    v
G_a^+ -> G_a^+ + H_{a,J}
c_a   -> c_a + b_J
    |
    v
Q_Ba unchanged
```

Therefore an isolated scalar value is not invariant. NP-SCALAR must either fix the Suzuki gauge or formulate the remainder gauge-invariantly.

## 9. Firewalls

- annihilation of `R_0` != positivity of the remaining form;
- global null-pole RH equivalence != fixed-window equivalence;
- auxiliary != false;
- cutoff gauge != arbitrary diagonal freedom;
- Registry unchanged;
- PR #91, PR #49 and R37/G4c remain separate.
