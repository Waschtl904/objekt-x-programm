# Offene Probleme — aktuelle OX-GEN-B-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

## Geschlossen im dokumentierten Scope

### OX-GEN-A / POS-DIL-1

Gemeinsame Translation-/Reflexions-Generator-Ebene und Prime-moment-Hilbertisierung sind konstruiert.

### POS-DIL-2A

Die unveränderte lokale `G_{1/2}^+`-Norm ist für unit-gain Shorting zu klein.

### POS-DIL-2B/2C-R

Der erste äußere Prime-Shell

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}
```

liefert echte Prime-Kanalmasse und dominiert zusammen mit `G_a^+` die Momentmasse für **alle** `0<a<=1`.

### POS-DIL-2C-B — exakte Shell-Buchung `✓[M]`

Für jede endliche Außenkanalmenge `J` gilt

```math
H_{a,J}=b_JI,
\qquad
b_J=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Daher

```math
Q_{B_a}
=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1.
```

Die volle Weilform bleibt exakt unverändert. Der isolierte `c_a`-Wert ist cutoff-gaugeabhängig.

### Positive `R_0`-Absorption `✓[M]`

Für den ersten Außenshell setze

```math
A_a^{out}=G_a^++H_a^{out},
```

```math
D_a^{out}=A_a^{out}-\mathcal E^*\mathcal E\succeq0,
```

```math
L_+=E_++E_-.
```

Dann

```math
P_a^{(0)}
=A_a^{out}-R_0
=D_a^{out}+L_+^*L_+\succeq0.
```

Die exakte Normalform lautet

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1,
\qquad0<a\le1.
}
```

Kanonische Quelle: `audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md`.

---

## Priorität 0 — OX-GEN-B / R1-GENERATOR `?[O]`

Bestimme die exakte mathematische Struktur von `R_1` und teste vorab definierte natürliche Generator-/Featureklassen.

Zu klären:

1. exakter Kernel bzw. die polarisierte Formel für `R_1`;
2. Parität und Symmetrien;
3. Darstellung als Integral/Superposition natürlicher Translation-/Reflexionskanäle;
4. mögliche positive Absorption zusammen mit bereits vorhandenen Features;
5. andernfalls ein enger, vorab definierter Klassen-No-Go.

Keine fertige Weil-Positivität und keine rückwärts definierte Positivitätswurzel als Input.

---

## Priorität 1 — GAUGE-INVARIANT-SCALAR `?[O]`

Der nackte Wert `c_a` ist unter der exakten Außen-Prime-Gauge nicht invariant.

Gesucht ist daher entweder:

- ein geometrisch kanonischer cutoff-Gauge; oder
- eine gaugeinvariante Kombination von Skalarledger und `R_1`.

Bevorzugt ist eine gemeinsame Lösung von `R_1` und Skalarrest statt zweier unabhängiger post-hoc Korrekturen.

---

## Priorität 2 — vollständiger Object-X-Pfad

- genuine X candidate `?[O]`;
- exakte volle Weil-Gram-Identität `?[O]`;
- Object-X-Realisierung `?[O]`;
- Weil-Kriterium-Scope `?[O]`;
- RH `?[O]`.

---

## Separate Nebenfronten

- Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständiger RH-unabhängiger Satz;
- R37/G4c separat offen;
- PR #91 analytischer Draft;
- PR #49 Candidate-only.

---

## Gesperrte Überdehnungen

Nicht behaupten:

- `c_a` sei ohne Gauge-Fixierung ein kanonischer isolierter Skalar;
- die Prime-cutoff-Gauge erlaube beliebige positive Diagonalergänzungen;
- `P_a^{(0)}` sei bereits die volle Weil-Gram-Realisierung;
- `R_1` sei gelöst;
- Object X oder RH seien bewiesen.
