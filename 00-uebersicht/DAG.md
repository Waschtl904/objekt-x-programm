# Abhängigkeitsgraph (DAG) — Objekt X / POS-DIL

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md), Strategie: [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md).

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
        | --candidate-input-->
        v
OX-GEN / POS-DIL
```

## 2. OX-GEN-A

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

```text
2D generator plane  ✓[M]
        |
        +--> Prime channels K_n
        +--> archimedean r_0
        +--> indefinite R_0
```

Prime-only-A2: `×[M]` im engen Scope.

## 3. POS-DIL-1

```text
PMP=M, SMS=M
        |
        v
M=tI
        |
        v
M_min=I  ✓[M]
```

```text
rho(t)^*M rho(t)=M, M>=0
        |
        v
M=0
        |
        v
exact unitary same-space Hilbertization ×[M]
```

Prime-moment-Abbildung:

```text
Prime channels + Weil weights + E
        |
        v
V_N
   |                 |
   | norm            | target involution
   v                 v
||Ev||^2 ✓[M]       R_0 ✓[M]
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

## 4. POS-DIL-2A — bestehende G-Masse fällt

```text
existing G_{1/2}^+
        |
        | --unit-gain shorting?-->
        v
||E v||^2 / R_0
```

Plateaufolge:

```math
\|\mathcal Ev_\varepsilon\|^2\to32\sinh^2\frac14,
```

```math
G_{1/2}^+(v_\varepsilon)\to1+\sqrt2(\log2)^2,
```

mit strikt größerem Momentgrenzwert.

```text
unit-gain shorting inside existing G^+  ×[M]
necessary extra mass delta_0>5/32       ✓[M]
```

## 5. POS-DIL-2B — erster äußerer Prime-Shift-Shell

Geometrisch definierte Klasse:

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}.
```

Für jedes `n` darin:

```math
\|K_nv\|^2=2\|v\|^2.
```

Also

```text
actual outer Prime channels
        |
        | --restriction to the window-->
        v
pure positive local mass 2 B_a^{out} I  ✓[M]
```

Bei `a=1/2`:

```text
existing G_{1/2}^+
        +
first exterior shell H_{1/2}^{out}
        |
        | --uniform domination-->
        v
||Ev||^2
```

Exakt:

```math
G_{1/2}^+(v)+H_{1/2}^{out}(v)
>\frac83\|v\|^2
>\|\mathcal Ev\|^2.
```

Damit

```text
first exterior shell unit-gain repair   ✓[M]
contractive R_0 Schur block             ✓[M]
```

## 6. Der neue Engpass ist Buchung, nicht bloß Positivität

```text
outer-shell positive repair  ✓[M] at a=1/2
        |
        | --needs exact accounting-->
        v
POS-DIL-2C SHELL-BOOKING ?[O]
        |
        +---------------------------+
        |                           |
        | exact counterbooking      | obstruction
        v                           v
common positive geometry        narrower class
```

Die Shellenergie darf nicht einfach zur lokalisierten Weilform addiert werden. Gesucht ist eine kanonische Gegenbuchung, Teleskopierung oder Root/Hub-Zerlegung, die die **volle Form unverändert** lässt.

Kandidateninputs:

```text
outer channels c_n>a as pure local mass
AR(1) root/hub T_q^*T_q+uu^*=R_q
POS-DIL-1 amplitude 1-u_k
shell differences / telescoping
```

## 7. Parallelfrage — Radiusfortsetzung

```text
first exterior shell theorem at a=1/2
        |
        | --extend?-->
        v
for which 0<a<=1:
||Ev||^2 <= G_a^+(v)+H_a^{out}(v) ?[O]
```

Algebraische Analyse an Prime-Power-Ein-/Austrittsschwellen vor bloßem Numeriksweep.

## 8. True Object-X path

```text
OX-GEN / POS-DIL partial geometry
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
        |
        v
EXACT FULL WEIL-GRAM IDENTITY ?[O]
        |
        v
OBJECT-X REALIZATION ?[O]
        |
        v
WEIL-CRITERION-SCOPE ?[O]
        |
        v
RH
```

Keine candidate-input-Kante ist eine Theoremimplikation.

## 9. Firewalls

- Außenshellmasse ist **nicht** bereits `c_aI`.
- Shell-Positivität ist **nicht** exakte Weil-Buchung.
- POS-DIL-2A ist kein globaler No-Go gegen positive Erweiterungen.
- Registry bleibt unverändert.
- PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten.
