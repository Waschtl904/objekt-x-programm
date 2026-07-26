# NEU-179 — Transfertriage und geladene Nullkozykel auf A_Q

## Vorbemerkung: Warum "Transfer" zu unspezifisch war

NEU-178 hat einen vollständigen algebraischen Modellbeweis geliefert: HH⁴(S_p, S_p)_ch ≠ 0. Der offen gelassene Knoten [O-178-transfer] ("Lässt sich [L_ν] übertragen?") war jedoch zu unspezifisch, um direkt bearbeitet zu werden. Dieses Dokument entscheidet zunächst, auf welchem funktoriellen Mechanismus eine Klasse überhaupt nach A_Q gelangen könnte, bevor ein konkreter Transferversuch unternommen wird.

---

## Zentrale Warnung: Eine Retraktion genügt nicht automatisch

Aus einer Algebreninklusion i: S_p ↪ A_Q entsteht **keine** natürliche kovariante Abbildung HH⁴(S_p,S_p) → HH⁴(A_Q,A_Q).

Auch eine Algebrenretraktion r: A_Q → S_p mit r∘i = id_{S_p} reicht für reguläre Koeffizienten nicht aus. Sie liefert zunächst nur eine Inflation mit Koeffizienten im zurückgezogenen Bimodul:

```
HH⁴(S_p, S_p) ⟶ HH⁴(A_Q, _rS_{p,r})
```

Um daraus eine Klasse in HH⁴(A_Q, A_Q) zu erhalten, wäre zusätzlich eine A_Q-Bimodulabbildung j: _rS_{p,r} → A_Q erforderlich. Eine bloße Algebreneinbettung i ist im Allgemeinen **keine** solche Bimodulabbildung.

**Konsequenz:** Der naive Ansatz φ ↦ i∘φ∘r^{⊗4} sollte **nicht ohne Prüfung** als Hochschild-Kettenabbildung verwendet werden. Die äußeren Randterme enthalten beliebige Elemente von A_Q, während die konstruierte Kochainformel nur deren r-Bilder sieht.

---

## Effizientere Route: direkte Konstruktion auf A_Q

Statt [L_ν] zu transportieren, wird geprüft, ob der **Konstruktionsmechanismus** — vier kommutierende neutrale Derivationen plus ein geladener Nullkozykel — unmittelbar auf A_Q verfügbar ist.

### Primderivationen

Seien D_{p₁},…,D_{p₄}: A_Q → A_Q vier paarweise kommutierende Hochschild-1-Kozykel (Derivationen). Der natürliche Kandidat ist eine Primvaluationswirkung:

```
D_p(μ_n) = v_p(n) μ_n
```

ergänzt durch Definitionen auf allen übrigen Erzeugern. Entscheidend ist **nicht nur** diese Formel, sondern der Nachweis, dass D_p sämtliche Relationen von A_Q respektiert.

### Antisymmetrisierte Cup-Komponente

```
Ω_p := Alt(D_{p₁} ⌣ D_{p₂} ⌣ D_{p₃} ⌣ D_{p₄})
```

ist ein 4-Kozykel. Da die Primvaluationsderivationen typischerweise die BC-Zeitgewichte erhalten, trägt Ω_p zunächst **Gewicht null**. Für eine geladene Klasse benötigt man daher zusätzlich einen geladenen 0-Kozykel.

---

## Koeffizientenentscheidung

### Reguläre Route

Für M = A_Q sind die 0-Kozykel genau die zentralen Elemente: Z⁰(A_Q,A_Q) = Z(A_Q). Man benötigt:

```
u_λ ∈ Z(A_Q),   α_t(u_λ) = e^{itλ}u_λ,   λ ≠ 0
```

Dann wäre L_{u,p} = u_λ ⌣ Ω_p ein geladener 4-Kozykel.

**Strukturelle Blockade:**

> Z(A_Q)_λ = 0 für alle λ ≠ 0 ⟹ die einfache reguläre HKR-Route scheitert.

Das beweist **nicht**, dass die gesamte geladene HH⁴-Komponente verschwindet; nur diese spezielle Konstruktion wäre ausgeschlossen.

### Verdrehte Route

Für M_σ = _id A_{Q,σ} ist die 0-Kozykelbedingung nicht Zentralität, sondern

```
a·u = u·σ(a)  für alle a ∈ A_Q
```

Ein geladenes Intertwiner-Element u_λ ∈ M_σ mit α_t(u_λ) = e^{itλ}u_λ liefert einen verdrehten Kandidaten:

```
L_{u,p} = u_λ ⌣ Ω_p ∈ Z⁴(A_Q, M_σ)
```

Dies könnte strukturell näher an modular verdrehten Koeffizienten liegen. Es darf aber **nicht vorausgesetzt** werden, dass das relevante σ tatsächlich durch ein vorhandenes geladenes Element implementiert wird.

---

## Atomare Struktur von NEU-179

### 179.A — Algebraischer Realitätsaudit

Zu klären ist, welche Struktur vier ausgewählte Primgeneratoren tatsächlich erzeugen: C[x₁,…,x₄], C[x₁^{±1},…,x₄^{±1}], eine reine Semigruppenalgebra, oder eine Algebra mit zusätzlichen Isometrie- und Adjunktenrelationen.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-179-1] | ∃ eine BC-äquivariante Algebreneinbettung S_p ↪ A_Q | ?[O] |
| [O-179-2] | Polynom-, Laurent- oder Isometriemodell? | ?[O] |

### 179.B — Primderivationen

| Knoten | Inhalt | Status |
|---|---|---|
| [O-179-3] | D_p auf allen Erzeugern von A_Q definieren | ?[O] |
| [O-179-4] | D_p respektiert sämtliche Relationen | ?[O] |
| [O-179-5] | [D_p, D_q] = 0 | ?[O] |
| [O-179-6] | α_t^C(D_p) = D_p | ?[O] |

Erst nach Abschluss dieser Knoten ist Ω_p = Alt(D_{p₁}⌣⋯⌣D_{p₄}) auf A_Q konstruiert.

### 179.C — Koeffizientenentscheidung

| Knoten | Inhalt | Status |
|---|---|---|
| [O-179-7reg] | ∃ u_λ ∈ Z(A_Q)_λ, λ ≠ 0 | ?[O] |
| [O-179-7σ] | ∃ u_λ ∈ M_σ mit au_λ = u_λσ(a), λ ≠ 0 | ?[O] |
| [O-179-8] | L_{u,p} = u_λ ⌣ Ω_p ist ein geladener 4-Kozykel | ?[O] — impliziert durch 179-3–6 ∧ (179-7reg ∨ 179-7σ) |

### 179.D — Nicht-Korand-Test

Auch nach Konstruktion des Kozykels bleibt seine Klasse offen. Erneut wird ein Gegengewichtszyklus benötigt:

| Knoten | Inhalt | Status |
|---|---|---|
| [O-179-9] | ∃ z_{−λ}, ∂z_{−λ} = 0 | ?[O] |
| [O-179-10] | ⟨L_{u,p}, z_{−λ}⟩ ≠ 0 | ?[O] |

Erst daraus folgt HH⁴(A_Q, M)_λ ≠ 0.

---

## Das Vier-Prim-Modell bleibt entscheidend

NEU-178 hat bereits bewiesen, dass der Mechanismus **vier neutrale Derivationen + geladener Nullkozykel** in einer geeigneten Algebra funktioniert. Der Transfer auf A_Q reduziert sich damit präziser auf zwei strukturelle Fragen:

1. Existieren vier geeignete äußere Primderivationen?
2. Existiert ein geladener Nullkozykel im gewählten Koeffizientenmodul?

Die zweite Frage dürfte die schärfere sein. Im regulären Modul verlangt sie ein geladenes Zentralelement; im verdrehten Modul nur einen geladenen Intertwiner.

---

## Zusätzliche Reichweitengrenze des Dualzeugen

Der Modellzeuge f_{ν+1} liegt im algebraischen Dual S_p^∨. Das ist für NEU-178 vollständig ausreichend. Bei einem analytisch vervollständigten A_Q müsste jedoch zusätzlich geprüft werden:

> **[O-179-dual]** ?[O]: Ist der benötigte Koeffizientenextraktor im gewählten topologischen Dual stetig?

Diese Frage darf **nicht rückwirkend** den algebraischen Modellbeweis (NEU-178) schwächen; sie betrifft ausschließlich den späteren analytischen Transfer.

---

## DAG-Knotenübersicht NEU-179

| Knoten | Inhalt | Status |
|---|---|---|
| [O-179-1] | ∃ BC-äquivariante Einbettung S_p ↪ A_Q | ?[O] |
| [O-179-2] | Polynom-/Laurent-/Isometriemodell? | ?[O] |
| [O-179-3] | D_p auf Erzeugern definiert | ?[O] |
| [O-179-4] | D_p respektiert Relationen | ?[O] |
| [O-179-5] | [D_p,D_q] = 0 | ?[O] |
| [O-179-6] | α_t^C(D_p) = D_p | ?[O] |
| [O-179-7reg] | ∃ u_λ ∈ Z(A_Q)_λ, λ≠0 | ?[O] |
| [O-179-7σ] | ∃ u_λ ∈ M_σ Intertwiner, λ≠0 | ?[O] |
| [O-179-8] | L_{u,p} ist geladener 4-Kozykel | ?[O] |
| [O-179-9] | ∃ z_{−λ}, ∂z_{−λ}=0 | ?[O] |
| [O-179-10] | ⟨L_{u,p}, z_{−λ}⟩ ≠ 0 | ?[O] |
| [O-179-dual] | Koeffizientenextraktor stetig im topologischen Dual? | ?[O] (nur für späteren analytischen Transfer) |

---

## Ausblick: NEU-180

Die Operatorrealisierung ρ_op verschiebt sich sachgerecht auf **NEU-180**. Der nächste Engpass ist nicht mehr die abstrakte Existenz geladener HH⁴-Klassen (durch NEU-178 im Modell geklärt), sondern die spezifische Koeffizienten- und Derivationsstruktur von A_Q selbst.
