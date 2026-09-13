# Abhängigkeitsgraph (DAG) — Objekt X / OX-GEN-B

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Importierte Basis

```text
fixed-pair Strong Terminal / C6
Prime-Power AR(1) / Weil-Tail
OX-GEN-A common generator plane
POS-DIL-1 prime-moment Hilbertization
```

Lokale Weil-Normalform:

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

## 2. Exterior-shell Route

```text
actual outer Prime channels c_n>a
        |
        | disjoint shifted supports
        v
w_n K_n^*K_n = 2 w_n I
        |
        v
H_{a,J}=b_J I  ✓[M]
```

Daher exakte cutoff-Gauge:

```text
G_a^+  --------> G_a^+ + H_{a,J}
c_a I --------> (c_a+b_J) I
        |
        v
Q_{B_a} unchanged  ✓[M]
```

Für den ersten Außenshell:

```math
b_J=A_{e^{4a}}-A_{e^{2a}}.
```

## 3. Radiusdominanz

Für

```math
A_a^{out}=G_a^++H_a^{out}
```

gilt auf jedem `0<a<=1`

```math
A_a^{out}\succeq\mathcal E^*\mathcal E.
```

Damit

```text
A_a^{out}
        |
        | subtract E^*E
        v
D_a^{out}>=0  ✓[M]
```

## 4. Exakte `R_0`-Absorption

```math
R_0(v,w)
=-E_+(v)\overline{E_-(w)}-E_-(v)\overline{E_+(w)}.
```

Setze

```math
L_+=E_++E_-.
```

Dann

```math
\mathcal E^*\mathcal E-R_0=L_+^*L_+.
```

Folglich

```text
A_a^{out}-R_0
 = (A_a^{out}-E^*E) + (E^*E-R_0)
 = D_a^{out} + L_+^*L_+
        |
        v
P_a^(0) >= 0  ✓[M]
```

und exakt

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1.
}
```

Der `R_0`-Layer ist damit aus dem Rest entfernt.

## 5. Gauge-Konsequenz

```text
isolated c_a
        |
        | changes under exact exterior-Prime cutoff gauge
        v
not canonical by itself  ✓[M]
```

Gesucht werden muss eine Gauge-Fixierung oder eine gaugeinvariante Reststruktur.

## 6. Aktueller Engpass — OX-GEN-B / R1-SCALAR

```text
positive common block P_a^(0)  ✓[M]
        |
        | remaining exact defect
        v
c_a^{out} I + R_1  ?[O]
        |
        +------------------------------+
        |                              |
        | common generator geometry    | natural class obstruction
        v                              v
next positive block               narrower architecture
```

Prüfreihenfolge:

```text
R_1 exact kernel / parity / generator structure
        ↓
interaction with cutoff gauge
        ↓
gauge-invariant scalar remainder
        ↓
OX-GEN-B candidate
```

## 7. Object-X-Pfad

```text
P_a^(0) positive common Prime/r0 block  ✓[M]
        +
R1 / scalar remainder ?[O]
        |
        v
genuine X candidate ?[O]
        |
        v
exact full Weil-Gram identity ?[O]
        |
        v
Object-X realization ?[O]
        |
        v
RH
```

## 8. Firewalls

- cutoff-Gauge != arbitrary positive diagonal freedom;
- `P_a^(0)` != complete Object X;
- `c_a^{out}` != canonical final scalar;
- `R_1` open;
- Registry unchanged;
- PR #91, PR #49, R37/G4c separate.
