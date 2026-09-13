# Abhängigkeitsgraph (DAG) — Objekt X / POS-DIL

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Basis

```text
fixed-pair Strong Terminal / C6
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
```

```text
Prime-Power AR(1) / Weil-Tail  ✓[M]
        |
        v
OX-GEN / POS-DIL
```

## 2. OX-GEN-A / POS-DIL-1

```text
translation/reflection generator plane  ✓[M]
        |
        +--> Prime channels K_n
        +--> archimedean r_0
        +--> R_0=<E.,J E.>
```

```text
Prime channels + Weil weights + E
        |
        v
Prime-moment Hilbertization V_N  ✓[M]
        |
        +--> ||V_N v||^2=||Ev||^2
        +--> R_0 via target involution
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

## 3. POS-DIL-2A

```text
existing G_{1/2}^+
        |
        | --unit-gain shorting?-->
        v
moment mass / R_0
```

```text
FAIL ×[M]
necessary extra mass delta_0>5/32
```

## 4. Erster äußerer Prime-Shell

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}.
```

```text
actual outer Prime channels
        |
        | --disjoint shifted supports-->
        v
||K_n v||^2=2||v||^2  ✓[M]
        |
        v
H_a^{out}=2B_a^{out} I
```

Die Skalarmasse ist ein Resultat echter Prime-Kanalenergie, kein freier Diagonalparameter.

## 5. POS-DIL-2C-R — Radiusfrage geschlossen

```text
log multiplier:       G_a^+ >= (-log a) I
outer shell:           H_a^{out}=2B_a^{out} I
moment upper bound:    ||E.||^2 <= 4 sinh(a) I
```

Sieben elementare Radiusintervalle liefern

```math
-\log a+2B_a^{out}>4\sinh a,
\qquad 0<a\le1.
```

Daher

```text
A_a^{out}=G_a^++H_a^{out}
        |
        | --uniform on every 0<a<=1-->
        v
||Ev||^2  ✓[M]
        |
        v
positive R_0 Schur block  ✓[M]
```

Radius extension: `✓[M]`.

## 6. Aktueller Engpass — EXACT-SHELL-BOOKING

```text
positive outer-shell geometry  ✓[M]
        |
        | --must preserve exact Weil form-->
        v
POS-DIL-2C-B exact booking ?[O]
        |
        +-----------------------------+
        |                             |
        | exact counterbooking        | class obstruction
        v                             v
common geometry                  narrower architecture
```

Priorisierte mögliche Mechanismen:

```text
pre-cutoff outer-channel identity mass
shell differences / telescoping
AR(1) root-hub: T_q^*T_q+uu^*=R_q
POS-DIL-1 amplitude 1-u_k
```

Nur eine exakte Bilanz zählt; bloßes Addieren von `H_a^{out}` zur Weilform nicht.

## 7. Object-X-Pfad

```text
exact shell booking ?[O]
        |
        v
OX-GEN-B / genuine X candidate ?[O]
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

- Radiuspositivität != exakte Weil-Buchung.
- Außenshellmasse != bereits `c_aI`.
- `r_1` offen.
- Registry unverändert.
- PR #91, PR #49, R37/G4c separat.
