# NEU-180 — Q₊ˣ-Gradierung und Primvaluationsderivationen von A_Q

## Vorbemerkung: Zwei Schärfungen gegenüber NEU-179

Die in NEU-179 vorgesehenen Primderivationen sollten **nicht einzeln ad hoc**, sondern **über eine Gruppengradierung** konstruiert werden. Zusätzlich benötigt die verdrehte Route neben dem Intertwiner eine **explizit typisierte Cup-Produkt-Abbildung**. Beide Punkte werden in diesem Dokument eingearbeitet.

---

## 1. Systematischer Mechanismus über Gruppengradierung

### Gradgruppe

Falls A_Q durch die üblichen arithmetischen Generatoren aufgebaut ist, ist die natürliche Ausgangsstruktur die Gradierung durch

```
Γ := Q₊^× ≅ ⊕_p Z
```

mit formaler Gradzuweisung:

```
deg(μ_n) = n,   deg(μ_n*) = n⁻¹,   deg(e(r)) = 1
```

### Homogenitätsaudit

Entscheidend ist der Nachweis:

> **Alle definierenden Relationen von A_Q sind bezüglich dieser Grade homogen.**

Dann entsteht auf dem algebraischen Kern eine echte Graduierung:

```
A_Q^alg = ⊕_{g∈Γ} A_g,   A_g A_h ⊆ A_{gh}
```

### Konstruktion der Derivationen

Für jede Primzahl p ist v_p: Γ → Z ein Gruppenhomomorphismus. Man setzt unmittelbar:

```
D_p(a_g) := v_p(g) a_g
```

**Nachweis der Leibnizregel:** Für homogene a_g ∈ A_g, b_h ∈ A_h:

```
D_p(a_g b_h) = v_p(gh) a_g b_h = (v_p(g) + v_p(h)) a_g b_h = D_p(a_g) b_h + a_g D_p(b_h)
```

Somit ist D_p eine Derivation.

### Simultane Folgeeigenschaften

Diese eine Konstruktion liefert **gleichzeitig**:

```
[D_p, D_q] = 0    (beide sind grad-diagonal, kommutieren also als Multiplikationsoperatoren)
```

und bei grad-diagonaler BC-Zeitwirkung α_t(a_g) = g^{it} a_g:

```
D_p α_t = α_t D_p
```

(beide Operatoren sind Multiplikation mit einer Funktion des Grades g, daher kommutieren sie).

**Konsequenz:** Die Knoten [O-179-3] bis [O-179-6] reduzieren sich auf einen **einzigen Homogenitätsaudit** — sobald [O-180-3] (Homogenität aller Relationen) bestätigt ist, folgen alle vier Knoten automatisch.

---

## 2. Präzisierung von [O-179-2]: Zwei zu unterscheidende Aussagen

Auf der positiven Unteralgebra, erzeugt von μ_{p₁},…,μ_{p₄}, gilt formal:

```
D_{p_i}(μ_{p_j}) = δ_{ij} μ_{p_j}
```

Das ist exakt die Eulerwirkung x_i∂/∂x_i aus NEU-178. Falls keine zusätzlichen algebraischen Relationen zwischen den positiven Generatoren bestehen, wäre die Abbildung

```
C[x₁,…,x₄] ⟶ A_Q^alg,   x_j ↦ μ_{p_j}
```

eine Einbettung des Polynommodells. **Zwei Aussagen sind zu trennen:**

1. **C[μ_{p₁},…,μ_{p₄}] ≅ C[x₁,…,x₄]** — für die rein positive algebraische Unteralgebra.
2. Die von μ_{p_j}, μ_{p_j}* erzeugte **volle *-Algebra**, die wegen Isometrie- und Projektionsrelationen **kein** Laurentpolynomring sein muss.

Diese Trennung präzisiert [O-179-2]: Der Transfer des Vier-Prim-Modells funktioniert möglicherweise nur auf der positiven Unteralgebra (Aussage 1), nicht notwendig auf der vollen *-Algebra (Aussage 2).

---

## 3. Korrektur der verdrehten Cup-Route: Typisierte Cup-Abbildung

Die Aussage u_λ ∈ Z⁰(A_Q, M_σ) bedeutet bei M_σ = _id A_{Q,σ} konkret:

```
a u_λ = u_λ σ(a)   für alle a ∈ A_Q
```

Ein solcher Intertwiner **genügt aber erst zusammen mit einer typisierten Cup-Abbildung**.

### Definition der Cup-Abbildung

Für u ∈ C⁰(A, M_σ), Ω ∈ C⁴(A, A):

```
C⁰(A, M_σ) ⊗ C⁴(A, A) ⟶ C⁴(A, M_σ)
(u ⌣ Ω)(a₁,…,a₄) := u · Ω(a₁,…,a₄)
```

Da die Rechtswirkung in M_σ verdreht ist, lautet dies konkret:

```
(u ⌣ Ω)(a₁,…,a₄) = u σ(Ω(a₁,…,a₄))
```

### Leibnizregel

Es muss ausdrücklich geprüft bzw. importiert werden:

```
b(u ⌣ Ω) = (bu) ⌣ Ω + u ⌣ (bΩ)
```

Aus bu = 0 und bΩ = 0 folgt anschließend b(u⌣Ω) = 0. **Ohne diese Cup-Typisierung ist der Ausdruck u_λ ⌣ Ω_p noch nicht vollständig konstruiert.**

### Neuer Knoten

> **[O-179-7σ-cup]:** C⁰(A_Q, M_σ) ⊗ C⁴(A_Q, A_Q) → C⁴(A_Q, M_σ) mit zugehöriger b-Leibnizregel.

Status: **?[O]** — die Definition der Abbildung ist gegeben, die Leibnizregel ist zu beweisen (Standardrechnung analog zur Ableitungsregel des Cup-Produkts in der Hochschild-Kohomologie, hier aber noch nicht ausgeführt).

---

## Atomare Knotenstruktur von NEU-180

| Knoten | Inhalt | Status |
|---|---|---|
| [O-180-1] | Γ = Q₊^× als Gradgruppe festlegen | ✓[K] (Definition) |
| [O-180-2] | deg(μ_n)=n, deg(μ_n*)=n⁻¹, deg(e(r))=1 | ✓[K] (Definition) |
| [O-180-3] | Jede definierende Relation ist homogen | ?[O] — zentraler Auditknoten |
| [O-180-4] | A_Q^alg = ⊕_{g∈Γ} A_g | ✓[K] \| [O-180-3] |
| [O-180-5] | D_p\|_{A_g} = v_p(g) id | ✓[K] \| [O-180-3] |
| [O-180-6] | D_p(ab) = D_p(a)b + aD_p(b) | ✓[K] \| [O-180-3] (bewiesen oben) |
| [O-180-7] | [D_p, D_q] = 0 | ✓[K] \| [O-180-3] (bewiesen oben) |
| [O-180-8] | D_pα_t = α_tD_p | ✓[K] \| [O-180-3] (bewiesen oben) |
| [O-180-9] | D_{p_i}\|_{C[μ_{p₁},…,μ_{p₄}]} entspricht der Euler-Derivation | ✓[K] \| [O-180-3] |

**Zentrales Ergebnis:** Alle Knoten [O-180-4] bis [O-180-9] sind **bedingt auf [O-180-3]** bewiesen — der gesamte Mechanismus reduziert sich auf den einen Homogenitätsaudit.

### Reduktion von [O-179-3–179-6]

Falls die Homogenität aller Relationen bestätigt wird (d.h. [O-180-3] geschlossen wird), folgt unmittelbar:

```
[O-179-3–6]   ✓[K]
```

---

## DAG-Knotenübersicht (konsolidiert)

| Knoten | Inhalt | Status |
|---|---|---|
| [O-180-1] | Γ = Q₊^× festgelegt | ✓[K] |
| [O-180-2] | Gradzuweisung definiert | ✓[K] |
| [O-180-3] | Homogenität aller Relationen | ?[O] |
| [O-180-4]–[O-180-9] | Graduierung, D_p, Kommutativität, α_t-Kommutation, Euler-Konsistenz | ✓[K] \| [O-180-3] |
| [O-179-2] (präzisiert) | Trennung positive Unteralgebra vs. volle *-Algebra | teilweise geklärt, *-Algebra-Frage offen |
| [O-179-7σ-cup] | Typisierte Cup-Abbildung mit Leibnizregel | ?[O] |

---

## Verbleibender Hauptengpass nach NEU-180

Nach Abschluss von NEU-180 wäre Ω_p = Alt(D_{p₁}⌣⋯⌣D_{p₄}) als neutraler 4-Kozykel auf A_Q^alg verfügbar. Der verbleibende Engpass konzentriert sich vollständig auf den Grad-null-Koeffizientenfaktor:

```
Z(A_Q)_λ ≠ 0        für die reguläre Route
Z⁰(A_Q, M_σ)_λ ≠ 0   für die verdrehte Route
```

Dies sollte in **NEU-181** durch einen Generatorentest entschieden werden: Für einen homogenen Kandidaten u_g lautet die verdrehte Bedingung bei grad-diagonalem σ:

```
a_h u_g = u_g σ(a_h)   für alle homogenen Generatoren a_h
```

Der Test an den Generatorfamilien μ_n, μ_n*, e(r) könnte die Intertwinerroute entweder explizit öffnen oder negativ schließen.

---

## Neue Reihenfolge

```
Gradierung ⟶ D_p ⟶ Ω_p ⟶ Zentrum/Intertwiner ⟶ Nicht-Korand-Test ⟶ ρ_op
```

Die Operatorrealisierung verschiebt sich damit sachgerecht mindestens auf **NEU-182**:

- **NEU-181**: Generatorentest für Zentrum/Intertwiner (Z(A_Q)_λ bzw. Z⁰(A_Q,M_σ)_λ)
- **NEU-182 (frühestens)**: Operatorrealisierung ρ_op, sofern NEU-181 und der Nicht-Korand-Test erfolgreich abgeschlossen sind
