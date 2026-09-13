# Objekt X — kanonische Forschungsroadmap v2.8

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Gesicherte lokale Normalform

Für `0<a<=1`:

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

Prime-Power-AR(1), OX-GEN-A und die Prime-moment-Hilbertisierung bleiben als importierte positive Struktur verfügbar.

## 2. Exterior-shell Geometrie

Der geometrisch definierte erste Außenshell ist

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}.
```

Für jeden äußeren Kanal gilt exakt

```math
\|K_nv\|^2=2\|v\|^2.
```

Damit

```math
H_a^{out}=2B_a^{out}I.
```

Für alle `0<a<=1` wurde bewiesen

```math
A_a^{out}:=G_a^++H_a^{out}
\succeq\mathcal E^*\mathcal E.
```

## 3. Exakte Prime-cutoff-Gauge `✓[M]`

Für jede endliche Außenkanalmenge `J`:

```math
H_{a,J}=b_JI,
\qquad
b_J=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Deshalb bleibt die vollständige Form invariant unter

```math
G_a^+\mapsto G_a^++H_{a,J},
\qquad
c_a\mapsto c_a+b_J.
```

Exakt:

```math
Q_{B_a}
=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1.
```

Für den ersten Shell:

```math
c_a^{out}=c_a+A_{e^{4a}}-A_{e^{2a}}.
```

**Konsequenz:** `c_a` ist als isolierter Zahlenwert innerhalb dieser Prime-feature-Gauge nicht kanonisch. Zukünftige Arbeit muss eine Gauge-Fixierung oder eine gaugeinvariante Skalarstruktur adressieren.

## 4. Exakte positive Absorption des elementaren archimedischen Layers `✓[M]`

Setze

```math
D_a^{out}=A_a^{out}-\mathcal E^*\mathcal E\succeq0,
```

und

```math
L_+(v)=E_+(v)+E_-(v).
```

Da

```math
\mathcal E^*\mathcal E-R_0=L_+^*L_+,
```

folgt

```math
\boxed{
P_a^{(0)}:=A_a^{out}-R_0
=D_a^{out}+L_+^*L_+\succeq0.
}
```

Die lokalisierte Weilform besitzt damit die exakte neue Normalform

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1,
\qquad0<a\le1.
}
```

Der `r_0`-/`R_0`-Layer ist innerhalb der unveränderten Weilform positiv absorbiert.

## 5. Aktuelle Default-Priorität: OX-GEN-B / R1-SCALAR

Der verbleibende Rest ist

```math
\boxed{c_a^{out}I+R_1.}
```

### 5.1 `R_1`-Generatorfrage

Bestimme die exakte Struktur von `R_1` auf der OX-GEN-Ebene:

- besitzt `R_1` eine Darstellung durch dieselben `E_\pm`, Translation/Spiegelung oder deren natürliche Erweiterung?
- ist `R_1` ein Integral/Superposition von Translationcharakteren oder positiven/indefiniten Rang-endlichen Kanälen?
- welche Paritätsstruktur besitzt `R_1`?
- lässt sich eine vorab definierte natürliche Absorptionsklasse konstruieren oder ausschließen?

### 5.2 Gaugeinvarianter Skalarrest

Nicht mehr den nackten Wert `c_a` als kanonisch behandeln. Zu suchen ist entweder:

1. ein geometrisch kanonischer cutoff-Gauge, oder
2. eine gaugeinvariante Kombination aus Skalarledger und `R_1`.

### 5.3 Gemeinsame Behandlung bevorzugt

`R_1` und Skalarrest nicht reflexartig getrennt lösen. Möglich ist, dass ihre natürliche gemeinsame Geometrie erst nach korrekter Gauge-Fixierung sichtbar wird.

## 6. Danach: echter X-Kandidat

```text
positive common block P_a^(0)  ✓[M]
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
Weil-criterion scope ?[O]
        |
        v
RH
```

## 7. Firewalls

- Gauge-Invarianz ist keine Erlaubnis für beliebige Diagonalmasse; zulässig war die vorab definierte Klasse echter Außen-Prime-Kanäle mit Weilgewichten.
- `P_a^{(0)}` ist ein positiver gemeinsamer Baustein, noch nicht die vollständige Weil-Gram-Realisierung.
- `Q_{B_a}`-Positivität folgt nicht allein aus der neuen Normalform.
- `R_1` und der endgültige Skalarrest bleiben offen.
- Keine Registry-Promotion durch Merge/CI.

## 8. Explizit offen

```text
OX-GEN-B / R1 generator-feature structure
gauge fixing or gauge-invariant scalar remainder
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope
RH
R37/G4c [separate]
```
