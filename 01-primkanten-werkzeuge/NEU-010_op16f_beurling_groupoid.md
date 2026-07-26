# [NEU-10] OP-1.6f — Beurling-/Groupoid-Route zur Spektralinvarianz

> Angelegt: 16. Juni 2026
> Aktualisiert: 16. Juni 2026 (f.4a intern bewiesen; f.4b als [EXT-route] präzisiert)

---

## Ziel

Spektralinvarianz von A_2D^r in A_BC^{C*} via Beurling-/Groupoid-Route:
```
A_2D^r  =  π B^r π  ⊆  π(C_0(A_f) ⋊ Q_+×)π  =  A_BC^{C*}
```

---

## OP-1.6f.1 — BC als Q_+×-Groupoid-Corner  ✓ [M]

```
C(Ẑ) ⋊ N×  ≅  π (C_0(A_f) ⋊ Q_+×) π,    π = 1_{Ẑ ⊆ A_f}
```
(Connes–Marcolli–Ramachandran) **✓ [M]**

---

## OP-1.6f.2 — GRS-Gewicht  ✓ [M]

Für q = m/n ∈ Q_+×, gcd(m,n) = 1:
```
ℓ(q) := log m + log n  =  Σ_p |a_p| log p
w_s(q) := (1 + ℓ(q))^s
```
Symmetrisch ✓, submultiplikativ ✓, GRS: lim_{N→∞} w_s(q^N)^{1/N} = 1 ✓. **✓ [M]**

---

## OP-1.6f.3 — Identifikation als Beurling-Algebra  ✓ [M]

```
A_2D^r  ≍  π (⋂_{s≥0} ℓ^1_{w_s}(Q_+×, C_0(A_f))) π
```
Normen r_k^(2) entsprechen Beurling-ℓ^1_{w_k}-Normen (Indexierung q = n/m). **✓ [M]**

---

## OP-1.6f.4a — GRS-Wiener für Q_+×  ✓ [M]

**Satz:**
```
ℓ^1_{w_s}(Q_+×) ist spektral invariant in C*(Q_+×).
```
**Beweis (intern):** Gelfand-Charaktertheorie. Sei χ ein Charakter mit
|χ(q)| ≤ w_s(q). Dann:
```
|χ(q)| ≤ w_s(q^N)^{1/N}  —(GRS)—>  1
```
Symmetrie: |χ(q^{-1})| ≤ 1, also |χ(q)| ≥ 1. Folglich |χ(q)| = 1.
Maximalidealspektrum = Ĝ. **✓ [M]**

Hinweis: Nicht-Kompakterzeugtheit von Q_+× ≅ ⊕_p Z ist kein Hindernis;
nur GRS und kommutative Gelfand-Theorie benötigt.

---

## OP-1.6f.4b — Koeffizienten-/Fell-Bundle-Lift  ⋄ [EXT-route]

**Zu zeigen:**
```
┌────────────────────────────────────────────────────────────┐
│  ℓ^1_{w_s}(Q_+×, C_0(A_f))  spektral invariant in              │
│  C_0(A_f) ⋊ Q_+×.                                             │
└────────────────────────────────────────────────────────────┘
```

**Fell-Bundle-Realisierung:**
C_0(A_f) ⋊ Q_+× ist eine Q_+×-graduierte C*-Algebra mit Fasern B_q = C_0(A_f) u_q.
Dies ist ein Fell-Bundle B über G = Q_+×.
Die Beurling-Algebra ist die gewichtete Querschnittsalgebra ℓ^1_{w_s}(G | B).

**Literaturroute:**

1. Exel (1997): Fell-Bundle-Unterbau, Konvolutionsalgebren und ihre C*-Abschlüsse.

2. Jauré–Măntoiu (arXiv:2108.09587, erschienen 2022):
   "Symmetry and Spectral Invariance for Topologically Graded C*-Algebras"
   Zeigt: In jeder topologisch G-graduierten C*-Algebra über einer rigid-symmetrischen
   Gruppe G existiert eine ℓ^1-artige symmetrische Banach-*-Algebra, die
   invers abgeschlossen ist. Enthält auch gewichtete Varianten.

3. Flores–Jauré–Măntoiu (arXiv:2110.10814; J. Operator Theory 91(1), 2024, pp. 27–54):
   "Symmetry for algebras associated to Fell bundles over groups and groupoids"
   Beweist: L^1(G | C) ist symmetrisch, wenn G (mit diskreter Topologie)
   rigid-symmetrisch ist. Enthält explizit gewichtete Version und Groupoid-Fall.

**Anwendung auf unser Problem:**
G = Q_+× ist abelsch, also rigid-symmetrisch (abelsche Gruppen sind stets
rigid-symmetrisch; Leptin–Ludwig, vgl. auch Jauré–Măntoiu).
Das Fell-Bundle B = (C_0(A_f) u_q)_{q ∈ Q_+×} ist ein Fell-Bundle über G.
Gewicht w_s ist symmetrisch, submultiplikativ, GRS (f.2).

Der gewichtete Satz aus Flores–Jauré–Măntoiu (2024) liefert damit:
```
ℓ^1_{w_s}(Q_+× | B)  =  ℓ^1_{w_s}(Q_+×, C_0(A_f))
ist symmetrisch und invers abgeschlossen in C*(B) = C_0(A_f) ⋊ Q_+×.
```

**Status: ⋄ [EXT-route]**
Literaturpassung sehr stark (Flores–Jauré–Măntoiu 2024, Theorem direkt anwendbar).
Interne Verifikation der Voraussetzungen (Rigid-Symmetrie von Q_+×, Fell-Bundle-
Struktur der Fasern B_q) noch formal abzuschliessen.

---

## OP-1.6f.5 — Corner-Transfer  ✓ [M] (unter f.4b)

Volles-Corner-Spektrum-Prinzip: SI in C_0(A_f) ⋊ Q_+× => SI im Corner.
```
σ_{A_2D^r}(a) = σ_{A_BC^{C*}}(a)   für alle a ∈ A_2D^r.
```
**✓ [M]** (unter f.4b)

---

## Gesamtstand

| Schritt | Inhalt | Status |
|---------|--------|--------|
| f.1 | BC als Q_+×-Groupoid-Corner (CMR) | ✓ [M] |
| f.2 | ℓ(q) GRS-Gewicht | ✓ [M] |
| f.3 | A_2D^r ≍ Beurling-Algebra | ✓ [M] |
| f.4a | GRS-Wiener für Q_+× (Gelfand) | ✓ [M] |
| f.4b | Koeffizienten-Fell-Bundle-Lift | ⋄ [EXT-route] |
| f.5 | Corner-Transfer | ✓ [M] (unter f.4b) |

**Spektralinvarianz von A_2D^r in A_BC^{C*} abhängig von einem einzigen
zitierbaren externen Theorem (Flores–Jauré–Măntoiu 2024).**
