# NEU-181 — Homogenitätsaudit, algebraischer Modular-Twist und Nullkozykeltest

## Vorbemerkung: Zwei konstruktive Abschlüsse aus der Gradierung

Sobald der Homogenitätsaudit abgeschlossen ist, ergänzen sich zwei weitere Knoten **ohne zusätzliche analytische Struktur**:

1. Der modulare Twist σ_β kann algebraisch direkt definiert werden.
2. Die verdrehte Cup-Leibnizregel [O-179-7σ-cup] kann direkt nachgerechnet werden.

Beide Punkte werden in diesem Dokument ausgeführt.

---

## 181.A — Gradierungsabschluss

### Struktur des Quotientennachweises

Es genügt nicht, einzelnen Relationen informell Grade zuzuweisen. Der saubere Quotientenbeweis erfordert:

```
F = freie algebraische Erzeugeralgebra,   A_Q^alg = F/I
```

Drei Schritte:

1. F = ⊕_{g∈Γ} F_g (freie Algebra ist graduiert)
2. I = ⊕_{g∈Γ} (I ∩ F_g) (**I ist ein homogenes Ideal**)
3. A_Q^alg = ⊕_{g∈Γ} (F_g + I)/I

Der entscheidende Punkt: **I ist ein homogenes Ideal.** Dafür muss jede definierende Relation eine Differenz bzw. Linearkombination von Termen desselben Gesamtgrades sein. Erst dann ist ausgeschlossen, dass der Quotient verschiedene Grade unkontrolliert identifiziert.

### Knotenstruktur 181.A

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-1] | Vollständige Erzeuger- und Relationenliste festlegen | ?[O] |
| [O-181-2] | Jede Relation ist homogen bezüglich deg(μ_n)=n, deg(μ_n*)=n⁻¹, deg(e(r))=1 | ?[O] |
| [O-181-3] | I ist ein homogenes Ideal | ?[O] — folgt aus [O-181-2] |
| [O-181-4] | A_Q^alg = ⊕_{g∈Γ} A_g | ✓[K] \| [O-181-3] |

**Abschluss durch diese Knoten:** [O-180-3] bis [O-180-9] werden zu ✓[K] \| [O-181-3].

---

## 181.B — Algebraischer Modular-Twist

### Definition

Sobald A_Q^alg = ⊕_{g∈Γ} A_g, setzt man für β ∈ R direkt:

```
σ_β(a_g) := g^{-β} a_g   (a_g ∈ A_g)
```

### Nachweis Algebraautomorphismus

Für a_g ∈ A_g, b_h ∈ A_h:

```
σ_β(a_g b_h) = (gh)^{-β} a_g b_h = g^{-β} h^{-β} a_g b_h = σ_β(a_g) σ_β(b_h)
```

Die inverse Abbildung ist σ_{-β}. Somit ist σ_β ein Algebraautomorphismus des algebraischen Kerns. Für β ≠ 0 muss er kein *-Automorphismus sein; für die Definition des verdrehten Bimoduls genügt die algebraische Automorphismuseigenschaft.

### Kommutation mit α_t

Da sowohl α_t als auch σ_β grad-diagonal sind:

```
α_t(a_g) = g^{it} a_g,   σ_β(a_g) = g^{-β} a_g
```

folgt unmittelbar α_tσ_β = σ_βα_t.

### Knotenstruktur 181.B

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-5] | σ_β\|_{A_g} = g^{-β} id | ✓[K] \| [O-181-4] |
| [O-181-6] | σ_β ∈ Aut_alg(A_Q^alg) | ✓[K] \| [O-181-4] (bewiesen oben) |
| [O-181-7] | α_t σ_β = σ_β α_t | ✓[K] \| [O-181-4] (bewiesen oben) |

**Abschluss durch diese Knoten:** [O-174-4σ] ✓[K] \| [O-181-3/4] auf dem algebraischen Kern. Eine analytische Fortsetzung zu einem vervollständigten C*- oder Fréchet-Modell ist dafür nicht erforderlich.

---

## Abschluss [O-179-7σ-cup]

Mit M_{σ_β} = _id A_{Q,σ_β} und der Cup-Konvention

```
(u ⌣ Ω)(a₁,…,a₄) = u σ_β(Ω(a₁,…,a₄))
```

gilt die Leibnizregel:

```
b(u ⌣ Ω) = (bu) ⌣ Ω + u ⌣ (bΩ)
```

**Direkter Nachweis:** Die erste Randkomponente wird mithilfe (bu)(a) = au − uσ_β(a) umgeschrieben; die inneren Terme folgen aus der Multiplikativität von σ_β; der letzte Randterm verwendet die verdrehte Rechtswirkung. Da σ_β ein Algebraautomorphismus ist, schließen sich alle Terme korrekt zusammen.

Daraus folgt:

```
bu = 0,  bΩ = 0  ⟹  b(u ⌣ Ω) = 0
```

**[O-179-7σ-cup] ✓[K] \| [O-181-4]**

---

## 181.C — Nullkozykeltest

### Struktur des Tests

Sei u_g ∈ A_g ein homogener Kandidat. Sein BC-Gewicht ist λ_g = log g. Er ist genau dann geladen, wenn g ≠ 1.

**Wichtig:** Die Gleichung ist auf beiden Seiten homogen vom selben Grad — der Test darf nicht allein aus dem Grad g entschieden werden.

### Reguläre Route: Zentralelement

```
a u_g = u_g a   für alle a ∈ A_Q
```

Es genügt, dies an einer vollständigen Erzeugermenge zu prüfen.

### Verdrehte Route: Intertwiner

Für σ_β lautet die Bedingung an den homogenen Erzeugern:

```
e(r) u_g = u_g e(r)            [Grad von e(r) ist 1, also 1^{-β}=1]
μ_n u_g  = n^{-β} u_g μ_n
μ_n* u_g = n^{β} u_g μ_n*
```

Diese Gleichungen sind noch kein Existenznachweis. Sie bilden aber ein **vollständiges algebraisches Kollisionssystem**, sobald e(r), μ_n, μ_n* tatsächlich eine Präsentation des verwendeten algebraischen Kerns liefern. Das Kollisionssystem entscheidet die Intertwinerroute entweder positiv (expliziter Zeuge) oder negativ (Widerspruch aus den Relationen).

### Knotenstruktur 181.C

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-8reg] | ∃ g≠1, u_g ∈ Z(A_Q^alg) ∩ A_g | ?[O] |
| [O-181-8σ] | ∃ g≠1, a_h u_g = h^{-β} u_g a_h für alle Generatoren a_h | ?[O] |

Die beiden Routen sind **unabhängig** zu entscheiden.

---

## 181.D — Geladener Kozykel

Falls eine der beiden Nullkozykelbedingungen erfüllt ist:

```
L_{u,p} = u_g ⌣ Ω_p
```

Dann gilt konstruktiv (via [O-179-7σ-cup] und [O-180-5–8]):

```
b L_{u,p} = 0
α_t^C(L_{u,p}) = e^{it log g} L_{u,p}
```

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-9] | L_{u,p} ist geladener 4-Kozykel mit Ladung log g | ✓[K] \| ([O-181-8reg] ∨ [O-181-8σ]) |

---

## Verbleibender Nicht-Korand-Nachweis

Auch ein erfolgreicher Nullkozykeltest liefert zunächst nur:

```
L_{u,p} ∈ Z^4_{log g}
```

Noch nicht bewiesen: **[L_{u,p}] ≠ 0.**

Daher sollte **NEU-182** den Gegengewichtszyklus bzw. einen geeigneten Restriktions- oder Separationszeugen konstruieren. Die Operatorrealisierung verschiebt sich folglich mindestens auf **NEU-183**.

---

## Konsolidierte DAG-Übersicht NEU-181

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-1] | Erzeuger- und Relationenliste | ?[O] |
| [O-181-2] | Homogenität jeder Relation | ?[O] |
| [O-181-3] | I homogenes Ideal | ?[O] \| [O-181-2] |
| [O-181-4] | A_Q^alg = ⊕_g A_g | ✓[K] \| [O-181-3] |
| [O-181-5] | σ_β\|_{A_g} = g^{-β} id | ✓[K] \| [O-181-4] |
| [O-181-6] | σ_β ∈ Aut_alg | ✓[K] \| [O-181-4] |
| [O-181-7] | α_tσ_β = σ_βα_t | ✓[K] \| [O-181-4] |
| [O-174-4σ] | Algebraischer Twist auf Kern | ✓[K] \| [O-181-3/4] |
| [O-179-7σ-cup] | Cup-Typisierung mit Leibnizregel | ✓[K] \| [O-181-4] |
| [O-181-8reg] | ∃ geladenes Zentralelement | ?[O] |
| [O-181-8σ] | ∃ geladener Intertwiner (Kollisionssystem) | ?[O] |
| [O-181-9] | L_{u,p} geladener 4-Kozykel | ✓[K] \| ([O-181-8reg] ∨ [O-181-8σ]) |

---

## Präzise Konstruktionskette

```
Γ-Gradierung
  ⟶ D_p, σ_β
  ⟶ u_g ∈ Z⁰(A, M_{σ_β})_{log g}
  ⟶ L_{u,p} ∈ Z⁴(A, M_{σ_β})_{log g}
  ⇢ [L_{u,p}] ≠ 0         (NEU-182: Gegengewichtszyklus)
  ⇢ ρ_op(L_{u,p})         (NEU-183: Operatorrealisierung)
```

Gestrichelte Pfeile kennzeichnen noch offene Nachweise.
