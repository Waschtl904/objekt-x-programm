# Aktueller Stand — Objekt X / OX-GEN-B

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md), [Registry](ACTIVE_THEOREM_REGISTRY.md).

## 1. Basis

Fixed-pair Strong Terminal/C6 liegt im ungeraden P11-Graphraum vor. Die Prime-Power-Seite besitzt die exakte AR(1)/Weil-Tail-Struktur. Für `0<a<=1`:

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

## 2. OX-GEN-A / POS-DIL-1

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Die Prime-moment-Hilbertisierung erfüllt

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

## 3. Erster Außenshell und Radius

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
```

```math
H_a^{out}=2B_a^{out}I.
```

Für alle `0<a<=1` gilt

```math
A_a^{out}:=G_a^++H_a^{out}
\succeq \mathcal E^*\mathcal E.
```

## 4. Exakte Prime-cutoff-Gauge `✓[M]`

Für jede endliche Außenkanalmenge `J` mit `c_n>a` gilt polarisiert

```math
H_{a,J}=b_JI,
\qquad
b_J=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Damit exakt

```math
Q_{B_a}
=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1.
```

Für den ersten Außenshell:

```math
\boxed{
Q_{B_a}=A_a^{out}-c_a^{out}I-R_0-R_1,
}
```

```math
c_a^{out}=c_a+2B_a^{out}
=c_a+A_{e^{4a}}-A_{e^{2a}}.
```

Der isolierte Skalar `c_a` ist damit cutoff-gaugeabhängig; die vollständige Differenzbuchung ist invariant.

## 5. Exakte positive `R_0`-Absorption `✓[M]`

Setze

```math
D_a^{out}:=A_a^{out}-\mathcal E^*\mathcal E\succeq0,
```

```math
L_+(v)=E_+(v)+E_-(v)
=2\int_{-a}^a\cosh(x/2)v(x)\,dx.
```

Dann polarisiert

```math
\mathcal E^*\mathcal E-R_0=L_+^*L_+.
```

Folglich

```math
\boxed{
P_a^{(0)}:=A_a^{out}-R_0
=D_a^{out}+L_+^*L_+\succeq0.
}
```

Die volle lokalisierte Form lautet jetzt exakt

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1,
\qquad0<a\le1.
}
```

Damit ist der elementare `r_0`-/`R_0`-Layer positiv absorbiert, ohne die Weilform zu verändern.

## 6. Neue Hauptfrage

**OX-GEN-B / `R_1` + gaugeinvarianter Skalarrest `?[O]`**.

Zu klären:

1. `R_1` auf dieselbe Generator-/Featuregeometrie zurückführen oder eine natürliche Klasse ausschließen;
2. den Skalarrest gaugeinvariant formulieren oder einen kanonischen cutoff-Gauge fixieren;
3. `R_1` und Skalarledger möglichst gemeinsam behandeln.

Weiter offen: `R_1`, gaugeinvarianter Skalarrest, genuine X candidate, volle Weil-Gram-Identität, Object X und RH.
