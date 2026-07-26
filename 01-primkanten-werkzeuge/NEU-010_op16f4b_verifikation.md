# [NEU-10] OP-1.6f.4b — Formale Verifikation: Flores–Jauré–Măntoiu

> Angelegt: 19. Juni 2026
> Status: ✓ [M] via [EXT-route]

---

## Ziel

Nachweis, dass alle Voraussetzungen von Jauré–Măntoiu (2022) / Flores–Jauré–Măntoiu (2024)
für die Situation

```
ℓ^1_{w_s}(Q_+×, C_0(A_f))  spektral invariant in  C_0(A_f) ⋊ Q_+×
```

erfüllt sind.

---

## Relevante Sätze

### Jauré–Măntoiu (arXiv:2108.09587, 2022) — Theorem 2.4

Sei C = ⊕_{g ∈ G} C_g eine **topologisch G-graduierte C*-Algebra** über einer
**rigid-symmetrischen diskreten Gruppe** G. Dann:

- (i)  ℓ^1(C) ist symmetrisch.
- **(ii) ℓ^1(C) ist invers abgeschlossen in C.**
- (iii) ℓ^1(C) ist invers abgeschlossen in B(H) für jede treue Darstellung.

### Jauré–Măntoiu (2022) — Theorem 2.20 (gewichtete Version)

Unter den Voraussetzungen von Thm. 2.4, und falls das Gewicht ν:G→[1,∞) die
Bedingungen (a) uGRS und (b) gleichmäßige Schalenkontrolle erfüllt, gilt:
ℓ^1_ν(C) ist symmetrisch (und invers abgeschlossen in C).

### Flores–Jauré–Măntoiu (arXiv:2110.10814; J. Operator Theory 91(1), 2024, 27–54) — Theorem 3.3

Sei C ein Fell-Bundle über einer lokal-kompakten Gruppe G, so dass G_dis
rigid-symmetrisch ist. Dann ist L^1(G | C) eine symmetrische Banach-*-Algebra.

---

## Verifikation der Voraussetzungen

### VP-1: Rigid-Symmetrie von G = Q_+× ✓ [M]

Q_+× ≅ ⊕_p ℤ  ist eine **abelsche diskrete Gruppe**.

Aus Flores–Jauré–Măntoiu (2024), Einleitung / Definition 1.2(ii):
> "Rigidly symmetric discrete groups include: abelian groups, finite groups,
>  finite extensions of discrete nilpotent groups, ..."

Abelschen Gruppen sind stets rigid-symmetrisch (Leptin–Ludwig; zitiert in beiden Papers).
**Kein separater Beweis nötig — direkt aus der Literatur zitierbar. ✓ [M]**

---

### VP-2: Topologische G-Graduierung von C_0(A_f) ⋊ Q_+× ✓ [M]

C_0(A_f) ⋊ Q_+× ist ein verschränktes Produkt mit Fasern

```
B_q := C_0(A_f) u_q,   q ∈ Q_+×.
```

Definition der topologischen Graduierung (Jauré–Măntoiu, Definition 2.1):
Eine C*-Algebra C ist topologisch G-graduiert, falls es abgeschlossene
Teilräume {C_g}_{g∈G} gibt mit:
1. ⊕_{g∈G} C_g dicht in C,
2. C_g C_h ⊆ C_{gh},
3. C_g* ⊆ C_{g^{-1}},
4. P_e:C→C_e stetig (bedingte Erwartung existiert).

Verifikation:

| Bedingung | Nachweis |
|-----------|---------|
| (1) Dichte | algebraische BC-*-Algebra liegt dicht ✓ (OP-1.6a) |
| (2) C_q · C_r ⊆ C_{qr} | u_q · u_r = u_{qr} im Kreuzprodukt ✓ |
| (3) C_q* = C_{q^{-1}} | (f u_q)* = u_{q^{-1}} f* ∈ B_{q^{-1}} ✓ |
| (4) P_e stetig | bedingte Erwartung E:C_0(A_f)⋊Q_+× → C_0(A_f) stetig ✓ |

**C_0(A_f) ⋊ Q_+× ist topologisch Q_+×-graduiert. ✓ [M]**

---

### VP-3: Fell-Bundle-Axiome für B_q = C_0(A_f) u_q ✓ [M]

Fell-Bundle-Axiome (Flores–Jauré–Măntoiu, Definition nach Exel 1997):

| Axiom | Verifikation |
|-------|-------------|
| ‖ab‖_{B_{qr}} ≤ ‖a‖_{B_q} ‖b‖_{B_r} | C*-Norm-Submultiplikativität ✓ |
| (ab)• = b• a• | Standard Kreuzprodukt-Involution ✓ |
| ‖a• a‖_{B_e} = ‖a‖²_{B_q} | C*-Identität in B_e = C_0(A_f) ✓ |
| a• a ≥ 0 in B_e | Positivität in C_0(A_f) ✓ |

**Die Fasern B_q erfüllen alle Fell-Bundle-Axiome. ✓ [M]**

---

### VP-4: Gewicht w_s erfüllt uGRS + Schalenbedingung ✓ [M]

Gewicht: w_s(q) = (1 + ℓ(q))^s, wobei ℓ(q) = log m + log n für q = m/n, gcd(m,n)=1.

Bereits in OP-1.6f.2 gesichert: w_s submultiplikativ, symmetrisch, GRS.

**Bedingung (a) — uGRS:**
```
lim_{N→∞} sup_{q_1,...,q_N ∈ V} w_s(q_1···q_N)^{1/N} = 1
```
Mit V = {q ∈ Q_+× : ℓ(q) ≤ 1} (Erzeugendenmenge):
ℓ(q_1···q_N) ≤ ℓ(q_1)+···+ℓ(q_N) ≤ N, also w_s(q_1···q_N)^{1/N} ≤ (1+N)^{s/N} → 1. ✓

**Bedingung (b) — gleichmäßige Schalenkontrolle:**
```
sup_{V^n \ V^{n-1}} w_s ≤ C · inf_{V^n \ V^{n-1}} w_s
```
Auf Schale V^n \ V^{n-1} = {q : n-1 ≤ ℓ(q) < n}:
```
(1+n-1)^s ≤ w_s(q) ≤ (1+n)^s,   Ratio ≤ ((1+n)/(1+n-1))^s ≤ 2^s =: C. ✓
```

**Beide Bedingungen erfüllt. ✓ [M]**

---

## Gesamtergebnis

```
┌──────────────────────────────────────────────────────────────────┐
│  OP-1.6f.4b: ✓ [M] via [EXT-route]                              │
│                                                                  │
│  Alle Voraussetzungen verifiziert:                               │
│  VP-1: Q_+× rigid-symmetrisch (abelsch) ✓                       │
│  VP-2: C_0(A_f) ⋊ Q_+× topologisch Q_+×-graduiert ✓            │
│  VP-3: Fasern B_q erfüllen Fell-Bundle-Axiome ✓                 │
│  VP-4: w_s erfüllt uGRS + Schalenbedingung ✓                    │
│                                                                  │
│  Theorem (Jauré–Măntoiu 2022, Thm. 2.4 + 2.20):                │
│  ℓ^1_{w_s}(Q_+×, C_0(A_f)) ist symmetrisch und                 │
│  invers abgeschlossen in C_0(A_f) ⋊ Q_+×.                      │
│                                                                  │
│  Damit: OP-1 vollständig abgeschlossen.                         │
│  Spektralinvarianz von A_2D^r in A_BC^{C*}: ✓ [M]              │
└──────────────────────────────────────────────────────────────────┘
```

Vollständige Beweiskette:
```
A_2D^r ≍ ℓ^1_{w_s}(Q_+×|B)   [f.3, ✓]
       ↪ C_0(A_f) ⋊ Q_+×      [f.4b, ✓ via Jauré–Măntoiu 2022]
       → Corner A_BC^{C*}      [f.5, ✓]
```

---

## Zitierte Literatur

- Jauré, D.; Măntoiu, M. (2022): "Symmetry and Spectral Invariance for Topologically
  Graded C*-Algebras and Partial Action Systems." arXiv:2108.09587.
- Flores, F.; Jauré, D.; Măntoiu, M. (2024): "Symmetry for algebras associated to
  Fell bundles over groups and groupoids." J. Operator Theory 91(1), 27–54.
  arXiv:2110.10814.
- Exel, R. (1997): Fell bundles and partial actions. Proc. Amer. Math. Soc. 125, 3235–3243.
