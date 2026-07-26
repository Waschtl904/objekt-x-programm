# NEU-178 — Vier-Prim-Polynommodell: explizite geladene HH⁴-Klasse und Dualzyklus

## Vorbemerkung: Zwei Knoten aus NEU-177 waren bereits allgemein geschlossen

Sobald B₃^mod eine assoziative Algebra und M ein Bimodul ist, sind M^∨, C_•(B₃^mod, M^∨) und ∂ definiert, und die Adjungiertheitsidentität ⟨bψ,z⟩ = ⟨ψ,∂z⟩ folgt durch direkten Vergleich der Randterme. Damit gilt allgemein, unabhängig vom konkreten Modell:

```
[O-177-3]   ✓[K]
[O-177-4]   ✓[K]
```

Offen blieben nur die objektspezifischen Knoten [O-177-1/2] und [O-177-5/6], mithin [O-177-7]. Dieses Dokument schließt diese Knoten explizit in einem **lokalen Vier-Prim-Modell** — einem eigenständigen Testmodell, das zunächst nicht als nachgewiesene Unteralgebra von A_Q gilt.

---

## Das Modell

Wähle vier verschiedene Primzahlen p₁,…,p₄ und setze

```
S_p := C[x₁,x₂,x₃,x₄],   α_t(x_j) = e^{itℓ_j} x_j,   ℓ_j := log p_j
```

Dies ist ein eigenständiges Polynommodell mit einer natürlichen kommutativen Algebrastruktur und einer diagonalen Zeitwirkung α_t.

---

## 1. Expliziter geladener Vier-Kozykel

### Definition

Mit den kommutierenden Euler-Derivationen D_j := x_j ∂/∂x_j und einem Multiindex ν = (ν₁,…,ν₄) ∈ N⁴\{0\}, x^ν := x₁^{ν₁}⋯x₄^{ν₄}:

```
L_ν(a₁,a₂,a₃,a₄) := x^ν · det(D_i(a_j))_{i,j=1}^4
            = x^ν Σ_{π∈S₄} sgn(π) ∏_{i=1}^4 D_i(a_{π(i)})
```

### [O-177-1]_{S_p} — Explizite Formel

Status: **✓[K]** — vollständig explizit gegeben.

### [O-177-2]_{S_p} — Kozykelbedingung

Da L_ν eine alternierende Multiderivation ist (Determinante kommutierender Derivationen, komponiert mit einem festen Skalarfaktor x^ν), gilt bL_ν = 0. Dies folgt aus der Standardtatsache, dass Determinanten kommutierender Derivationen Hochschild-Kozykel definieren (verallgemeinerte HKR-Konstruktion).

Status: **✓[K]**

---

## 2. Gewicht des Kozykels

Die D_j kommutieren mit der Skalierungswirkung α_t, daher trägt der Determinantenteil Gewicht 0, während x^ν das Gewicht

```
λ_ν = Σ_{j=1}^4 ν_j log p_j
```

trägt. Wegen ν ≠ 0 folgt λ_ν > 0. Somit:

```
α_t^C(L_ν) = e^{itλ_ν} L_ν
```

Der Kozykel ist tatsächlich **geladen** (λ_ν ≠ 0).

---

## Expliziter Dualzyklus

Sei 1 = (1,1,1,1) und f_{ν+1} ∈ S_p^∨ das Koeffizientenfunktional:

```
f_{ν+1}(x^κ) = 1  falls κ = ν+1,   0 sonst
```

Definiere:

```
z_{-λ_ν} := f_{ν+1} ⊗ Σ_{π∈S₄} sgn(π) x_{π(1)} ⊗ x_{π(2)} ⊗ x_{π(3)} ⊗ x_{π(4)}
```

### [O-177-5]_{S_p} — Zyklusbedingung ∂z = 0

Da S_p kommutativ ist, ist S_p^∨ ein symmetrisches Bimodul. Die antisymmetrisierten inneren Randterme heben sich paarweise auf; die beiden äußeren Randterme stimmen wegen der symmetrischen Modulwirkung überein. Daher ∂z_{-λ_ν} = 0.

Status: **✓[K]**

### Gewichtskontrolle

```
wt(f_{ν+1}) = -Σ_{j=1}^4 (ν_j+1) log p_j
```

während die vier Tensorfaktoren zusammen das Gewicht Σ_{j=1}^4 log p_j tragen. Folglich wt(z_{-λ_ν}) = -λ_ν — exaktes Gegengewicht wie in NEU-177 gefordert.

---

## Nichtverschwindende Paarung

Für jede Permutation π gilt L_ν(x_{π(1)},x_{π(2)},x_{π(3)},x_{π(4)}) = sgn(π) x^{ν+1}. Damit:

```
⟨L_ν, z_{-λ_ν}⟩ = Σ_{π∈S₄} sgn(π)² f_{ν+1}(x^{ν+1}) = |S₄| = 4! = 24 ≠ 0
```

### [O-177-6]_{S_p} — Nichtverschwindende Paarung

Status: **✓[K]**

---

## Schlussfolgerung: Nicht-Korand-Beweis und Nichttrivialität

Aus ∂z_{-λ_ν} = 0 und der Adjungiertheitsidentität [O-177-4] folgt für jedes ψ ∈ C³(S_p, S_p):

```
⟨bψ, z_{-λ_ν}⟩ = ⟨ψ, ∂z_{-λ_ν}⟩ = 0
```

Da ⟨L_ν, z_{-λ_ν}⟩ = 24 ≠ 0, kann L_ν kein Korand sein:

```
L_ν ∉ bC³(S_p, S_p)
```

### [O-177-7]_{S_p}

> **[L_ν] ≠ 0 in HH⁴(S_p, S_p)**

und wegen λ_ν ≠ 0:

> **[P^ch]([L_ν]) = [L_ν] ≠ 0**

Status: **✓[K]**

---

## Konsolidierte Statustabelle

| Knoten | Status im Modell S_p |
|---|---|
| [O-177-1]_{S_p} | ✓[K] |
| [O-177-2]_{S_p} | ✓[K] |
| [O-177-3] | ✓[K] (allgemein, modellunabhängig) |
| [O-177-4] | ✓[K] (allgemein, modellunabhängig) |
| [O-177-5]_{S_p} | ✓[K] |
| [O-177-6]_{S_p} | ✓[K] |
| [O-177-7]_{S_p} | ✓[K] |

Damit sind sämtliche Knoten von NEU-177 im Vier-Prim-Modell geschlossen: **[O-177-1–7]_{S_p} ✓[K]**.

---

## Strikte Reichweitengrenze

Dieses Ergebnis beweist **nicht** HH⁴(A_Q, A_Q)_ch ≠ 0. S_p ist ein eigenständiges Modell, keine nachgewiesene Unteralgebra von A_Q mit übereinstimmender Hochschild-Struktur.

### Neuer offener Transferknoten

> **[O-178-transfer]** ?[O]: Lässt sich [L_ν] von S_p auf A_Q übertragen?

Dafür wäre beispielsweise eine typkorrekte Einbettung samt geeigneter Retraktion, ein Vergleich von Auflösungen oder eine explizite Erweiterung des Kozykels erforderlich. Eine bloße Inklusion S_p ↪ A_Q liefert **nicht automatisch** eine Abbildung

```
HH⁴(S_p, S_p) ⟶ HH⁴(A_Q, A_Q)
```

da Hochschild-Kohomologie nicht funktoriell unter beliebigen Inklusionen ist (nur unter geeigneten Algebrahomomorphismen mit kompatiblen Bimodulstrukturen, oder via expliziter Restriktions-/Induktionsfunktoren).

---

## Präziser neuer Stand

> ∃ eine explizite nichttriviale geladene Modellklasse [L_ν] ∈ HH⁴(S_p, S_p);
> ihre Erweiterung auf A_Q und ihre Identifikation mit [L₃^orig] bleiben offen.

### Offene Anschlussfragen

| Frage | Status |
|---|---|
| ∃ [L_ν] ≠ 0 in HH⁴(S_p,S_p) mit Ladung λ_ν ≠ 0? | ✓[K] — beantwortet |
| Lässt sich [L_ν] auf A_Q übertragen? [O-178-transfer] | ?[O] |
| Identifikation mit [L₃^orig]? [O-176-orig] | ?[O] — weiterhin offen, unabhängig vom Transfer |
| Operatorrealisierung ρ_op | weiterhin verschoben, jetzt frühestens NEU-179 nach Klärung des Transfers |
