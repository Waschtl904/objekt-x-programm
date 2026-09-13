# Abhängigkeitsgraph (DAG) — Objekt X / POS-DIL

> **Stand:** 13. September 2026; Registry unverändert.  
> **Rolle:** kompakte operative Abhängigkeits- und Firewall-Struktur.  
> **Keine Beweisautorität.** Status/Provenienz: [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md), aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md), Strategie: [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md).

---

## 1. Kantenregel

- `A ⇔ B` — bewiesene Äquivalenz;
- `A ⇒ B` — bewiesene Implikation;
- `A ?⇒ B` — offene Implikation.

Forschungs-/Beweisabhängigkeiten: `uses`, `reduces-to`, `candidate-input`, `requires`, `open-bridge`, `sufficient-route`.

Ein PR ist Provenienz/Container, kein mathematischer DAG-Knoten.

---

## 2. Verfügbarer Strong-Terminal-Baustein

```text
fixed-pair Strong Terminal / C6
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
```

Scope: jedes feste `0<R<S`, ungerader P11-Graphraum; keine Radienuniformität oder Object-X-/RH-Folgerung.

---

## 3. Prime-Power-/AR(1)-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

```text
Prime-Power AR(1) / Weil-Tail structure  ✓[M] in documented scope
        |
        | --candidate-input-->
        v
OX-GEN / POS-DIL
```

---

## 4. OX-GRAM positive Featureform

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

```text
finite OX-GRAM identity
        |
        | --reformulation only-->
        v
arbitrary backward contractor [closed/vacuous as X-gate]
```

Gesucht bleibt eine vorwärts definierte gemeinsame Geometrie.

---

## 5. OX-GEN-A `✓[M]`

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle,
\qquad J=-P.
```

```text
2D translation representation rho
        |
        + --odd finite difference--> Prime channel K_n
        + --negative character-----> archimedean r_0''
        + --reflection pullback----> R_0
```

Prime-only-A2 aus `{w_n,lambda_n}`: `×[M]` im engen Scope.

---

## 6. POS-DIL-1 — positive Quotientenumgebung

Mit

```math
S=D_n/\lambda_n=2\rho'(0),
```

gilt in der natürlichen Companion-Klasse

```text
PMP=M and SMS=M
        |
        | --rigidity-->
        v
M=tI
        |
        | --minimal block positivity-->
        v
M_min=I  ✓[M]
```

Volle positive `rho`-Invarianz:

```text
rho(t)^* M rho(t)=M, M>=0
        |
        v
M=0
        |
        v
exact unitary same-space Hilbertization ×[M]
```

Prime-moment-Abbildung:

```math
V_Nv=\kappa_N^{-1/2}
(\sqrt{w_n}\,\mathcal EK_nv)_{n\in N}.
```

```text
Prime channels + Weil weights + E
        |
        | --normalized moment map-->
        v
positive H_N
   |                 |
   | norm            | involution P_N
   v                 v
||Ev||^2 ✓[M]       R_0 ✓[M]
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

`OX-GEN-A2' overall`: `✓[M]_part`.

---

## 7. POS-DIL-2A — unit-gain FEATURE-SHORTING `×[M]`

Vorab definierter Gate:

```text
existing G_a^+ feature norm
        |
        | --contractive shorting?-->
        v
minimal E-mass / R_0
```

Notwendige Bedingung:

```math
|R_0(v,v)|\le G_a^+(v).
```

Bei `a=1/2` liefert eine zulässige gerade Plateaufolge

```math
|R_0(v_\varepsilon,v_\varepsilon)|
\to32\sinh^2\frac14,
```

```math
G_{1/2}^+(v_\varepsilon)
\to1+\sqrt2(\log2)^2,
```

mit

```math
32\sinh^2\frac14>2>1+\sqrt2(\log2)^2.
```

Also:

```text
unit-gain C F^+=V                         ×[M]
contractive target-observable for R_0     ×[M]
unit-diagonal positive Schur block        ×[M]
```

Dieser No-Go betrifft die bestehende `G_{1/2}^+`-Masse; POS-DIL-1 bleibt erhalten.

---

## 8. Notwendiger Massendefekt

```math
\delta_0
=32\sinh^2\frac14
-1-\sqrt2(\log2)^2
>\frac5{32}>0.
```

```text
any positive augmentation H enabling unit-gain shorting
        |
        | --must satisfy on plateau sequence-->
        v
liminf H(v_epsilon,v_epsilon) >= delta_0  ✓[M]
```

---

## 9. Aktuelle Hauptfront — POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION

```text
POS-DIL-2A no-go  ×[M]
        |
        | --forces extra positive mass-->
        v
INTRINSIC-MASS-AUGMENTATION ?[O]
        |
        +-----------------------------------+
        |                                   |
        | construct canonical mass          | further class no-go
        v                                   v
positive augmented environment         narrower admissible class
        |
        | --candidate-input only-->
        v
OX-GEN-B ?[O]
```

Candidate inputs, not conclusions:

```text
AR(1) root/hub u_k=q_p^k
prime-moment complement 1-u_k
global prime channels outside local Suzuki cutoff
existing positive log|D| geometry
```

Forbidden shortcuts: arbitrary diagonal mass, finished Weil form, RH, backward positivity root, or silently identifying the deficit with `c_aI`.

---

## 10. True Object-X path

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

No candidate-input edge is a theorem implication.

---

## 11. Separate / parked routes

- R37/G4c: separat offen.
- Historische R43-COND-/FD23-/Flagfragen: eigene Quantoren, nicht aktuelle Voraussetzung.
- PR #91: Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- PR #49 / SW1 salvage: Candidate-only; kein stiller Merge.

---

## 12. Gate-Regel

Ein Falsifikationsgate zählt nur, wenn beide Ausgänge vorher logisch möglich waren. POS-DIL-2A erfüllt diese Bedingung: die unit-gain Shorting-Klasse wurde in POS-DIL-1 vor der Plateau-Gegenrechnung als nächster Gate definiert.

---

## Kanonische Einstiegspunkte

- [CURRENT-FRONT](../CURRENT-FRONT.md)
- [AKTUELLER_STAND](AKTUELLER_STAND.md)
- [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md)
- [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)
- [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
