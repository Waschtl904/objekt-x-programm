# NEU-11: Berechnung von E₂^{1,1}(A) = H¹(N×, Ω¹(T))

> Datum: 19. Juni 2026 | Status: ⚠ [M] — intern vollständig berechnet, externe Verifikation ausstehend

---

## 1. Einbettung in den Gesamtrahmen

Die Hochschild-Kohomologie HH²(A,A) zerfällt via Hodge-Zerlegung (vgl. NEU-7/NEU-9/B)
in drei Summanden des E₂-Blatts der Serre-Spektralsequenz:

```
HH²(A,A) ≅ E_∞^{2,0}(A) ⊕ E_∞^{1,1}(A) ⊕ E_∞^{0,2}(A)
```

| Summand | Bedeutung | Status (vor NEU-11) |
|---------|-----------|---------------------|
| E₂^{2,0}(A) | HH²(C∞(T), C∞(T))^{N×} | ✓ [M] — ℝ (Bott-Klasse) |
| E₂^{0,2}(A) | H²(N×, C∞(T)^{N×}) | ✓ [M] — 0 (abelsch, freie Auflösung) |
| **E₂^{1,1}(A)** | **H¹(N×, Ω¹(T))** | ❓ [O] — **Gegenstand dieser Berechnung** |

Aus NEU-9/B (Bidegree-Constraint) ist bekannt:
- E_∞^{2,0} und E_∞^{0,2} ⊕ E_∞^{1,1} sind durch kein d_r (r ≥ 2) verbunden.
- Die d₂-Differentiale ausgehend von E₂^{1,1} → E₂^{0,2} sind noch nicht ausgeschlossen.

---

## 2. Das N×-Modul Ω¹(T)

### 2.1 Definition

Sei T = ℝ/2πℤ der Kreis, A_∞ = C∞(T) die Algebra der glatten Funktionen.
Das Modul der Kähler-Differentialformen ist:

```
Ω¹(T) = { f dθ : f ∈ C∞(T) }  ≅  C∞(T)  als Fréchet-Raum
```

### 2.2 N×-Wirkung auf Ω¹(T)

Die multiplikative Gruppe N× = ⟨{p : p prim}⟩ ⊆ ℕ wirkt auf T via Skalierung:

```
α_n : T → T,   α_n(θ) = n·θ  (mod 2π)
```

Für f dθ ∈ Ω¹(T) ergibt sich durch Pullback (Kettenregel):

```
α_n*(f dθ) = (f ∘ α_n) · d(nθ) = n · (f ∘ α_n) · dθ
```

**Schlüsselunterschied zu C∞(T):** Die N×-Wirkung auf Ω¹(T) trägt den zusätzlichen
Skalierungsfaktor n gegenüber der Wirkung auf C∞(T). In Fourier-Koordinaten:

```
Wirkung auf C∞(T):   (α_n* f̂)(k) = f̂(nk)   [Frequenzverschiebung]
Wirkung auf Ω¹(T):   (α_n* ω̂)(k) = n · f̂(nk)  [Frequenzverschiebung + Skalierung]
```

---

## 3. Faktorisierung via Primzerlegung

### 3.1 Koszul-Zerlegung (aus NEU-8/OK)

Da N× = ∏_p ℕ_p (direktes Produkt über alle Primzahlen, ℕ_p ≅ ℕ additiv) und
die Gruppen-Kohomologie mit dem direkten Produkt verträglich ist:

```
H¹(N×, M)  ≅  ∏_p H¹(ℕ_p, M)
```

für jedes N×-Modul M (diskret-topologisches direktes Produkt).

Diese Faktorisierung gilt sowohl für M = C∞(T) als auch für M = Ω¹(T).

### 3.2 Reduktion auf lokale Kohomologie

Es genügt, **H¹(ℕ_p, Ω¹(T))** für jede Primzahl p zu berechnen.

---

## 4. Berechnung von H¹(ℕ_p, Ω¹(T))

### 4.1 Kozyklus-Bedingung

Ein 1-Kozyklus ist eine stetige Abbildung c : ℕ_p → Ω¹(T), d.h. eine Folge
(c_k)_{k≥0} in Ω¹(T) mit c_k = c_{k, f dθ} für f ∈ C∞(T), die die
Kozyklus-Relation erfüllt:

```
c_{k+ℓ} = c_k + α_p^k*(c_ℓ)
```

Für ℓ = 1 (Erzeugerschritt):

```
c_{k+1} = c_k + α_p^k*(c_1) = c_k + p^k · (c̃_1 ∘ α_p^k) dθ
```

wobei c_1 = c̃_1 dθ mit c̃_1 ∈ C∞(T).

### 4.2 Rekursive Auflösung

Mit c_0 = 0 (Normierung) und c_1 = f dθ ergibt sich:

```
c_k = Σ_{j=0}^{k-1} p^j · (f ∘ α_p^j) dθ
    = ( Σ_{j=0}^{k-1} p^j · f(p^j ·) ) dθ
```

In Fourier-Darstellung mit f̂(m) = (2π)^{-1} ∫_T f(θ) e^{-imθ} dθ:

```
ĉ_k(m) = Σ_{j=0}^{k-1} p^j · f̂(m / p^j)   [f̂(m/p^j) = 0 falls p^j ∤ m]
```

### 4.3 Kobrand-Bedingung

Ein Kozyklus c_k = (b ∘ α_p^k - b) für b = g dθ ∈ Ω¹(T) ist genau dann
ein Korand, wenn:

```
c_1 = α_p*(b) - b = p·(g ∘ α_p) dθ - g dθ
```

In Fourier-Koordinaten:

```
ĉ_1(m) = p · ĝ(pm) - ĝ(m)
```

Dies hat eine Lösung ĝ ∈ Schwartz iff für alle m ≠ 0 mit p ∤ m (p-primitive m):

```
ĉ_1(m)  muss verschwinden!
```

denn für p-primitive m (also p ∤ m) gibt es kein Freiheitsgrad in ĝ(pm) = ĝ(p·m)
zur Auflösung des Gleichungssystems.

### 4.4 p-primitive Frequenzen

**Definition:** Eine Frequenz m ∈ ℤ \ {0} heißt p-primitiv, falls p ∤ m, d.h.
m ∉ p·ℤ. Die Menge der p-primitiven Frequenzen ist:

```
𝒫_p = { m ∈ ℤ \ {0} : p ∤ m }
```

**Kohomologische Interpretation:**

```
H¹(ℕ_p, Ω¹(T))  ≅  { nicht-auflösbare Modenfolgen }
                 ≅  { f̂ : f̂|_{𝒫_p} beliebig Schwartz-Folge, f̂|_{pℤ} = 0 }
                 ≅  𝔰(𝒫_p)
```

wobei 𝔰(𝒫_p) der Raum der Schwartz-Folgen auf 𝒫_p ist
(schnell-fallende Folgen bezüglich |m| → ∞).

**Dimension:** |𝒫_p| = ∞ (p-primitive Frequenzen sind dicht in ℤ \ {0}),
daher ist H¹(ℕ_p, Ω¹(T)) unendlich-dimensional.

---

## 5. Hauptresultat

### Theorem (NEU-11, 19. Juni 2026) ⚠ [M]

```
E₂^{1,1}(A) = H¹(N×, Ω¹(T))  ≅  ∏_p 𝔰(𝒫_p')
```

wobei:
- 𝒫_p' = p-primitive Frequenzen in ℤ \ {0} = { m ∈ ℤ \ {0} : p ∤ m }
- 𝔰(𝒫_p') = Schwartz-Folgenraum auf 𝒫_p' (lokal-konvex, Fréchet)
- Das Produkt ∏_p läuft über alle Primzahlen p

**Eigenschaften:**
- **Unendlich-dimensional**: Jeder Faktor 𝔰(𝒫_p') ist ∞-dim.
- **Nicht-trivial**: E₂^{1,1}(A) ≠ 0 (im Gegensatz zu E₂^{0,2}(A) = 0)
- **Fréchet-Produkt**: Lokal-konvex, vollständig, separierbar
- **Topologisch nicht-trivial**: Keine Hilbert-Raum-Struktur kanonisch

---

## 6. Konsequenzen für HH²(A,A)

### 6.1 Drei unabhängige Summanden

```
HH²(A,A)  ≅  ℝ  ⊕  ∏_p 𝔰(𝒫_p')  ⊕  0
           [E_∞^{2,0}]  [E_∞^{1,1}]   [E_∞^{0,2}]
```

Vorausgesetzt d₂: E₂^{1,1} → E₂^{0,2} verschwindet (noch nicht bewiesen).

### 6.2 Bidegree-Constraint (NEU-9/B, bestätigt)

Aus dem Bidegree-Constraint folgt:
- E_∞^{2,0} und E_∞^{0,2} ⊕ E_∞^{1,1} sind durch kein d_r (r ≥ 2) verbunden. ✓ [M]
- Die Bott-Klasse [ω̃₂] ∈ E_∞^{2,0} ≅ ℝ ist isoliert vom E₂^{1,1}-Anteil.

### 6.3 Status OP-2

Das neue Ergebnis **unterstützt** OP-2: Da E₂^{1,1}(A) ≠ 0, existieren
in HH²(A,A) nicht-triviale Klassen jenseits der Bott-Klasse.

OP-2 ([ω̃₂] ≠ 0) betrifft jedoch E_∞^{2,0}, nicht E_∞^{1,1} — bleibt offen `✗`.

### 6.4 Offene Folgefrage (NEU-11/F1)

**d₂-Differential:** Ist d₂: E₂^{1,1}(A) → E₂^{0,2}(A) = 0?

Da E₂^{0,2}(A) = 0 bereits festgestellt (NEU-7), gilt trivialerweise:

```
d₂: E₂^{1,1}(A) → E₂^{0,2}(A) = 0  →  0   (automatisch Null)
```

**Dieser Punkt ist damit erledigt.** Die Zielobjekte sind 0, also ist d₂ = 0.

### 6.5 Einbettung in Objekt X (NEU-11/OX)

Aus [NEU-11 / ebene-XVI-objekt-x.md]:
- Axiom X.3 verlangt nicht-triviale Hochschild-Koeffizienten in Bidegree (1,1).
- Das Ergebnis E₂^{1,1}(A) = ∏_p 𝔰(𝒫_p') ≠ 0 bestätigt X.3. ⚠ [M]

---

## 7. Zusammenfassung

| Objekt | Ergebnis | Status |
|--------|----------|--------|
| E₂^{2,0}(A) | ℝ (Bott) | ✓ [M] |
| **E₂^{1,1}(A)** | **∏_p 𝔰(𝒫_p') ≠ 0** | **⚠ [M]** |
| E₂^{0,2}(A) | 0 | ✓ [M] |
| d₂: E₂^{1,1} → E₂^{0,2} | = 0 (trivial, da Ziel = 0) | ✓ [M] |
| OP-2: [ω̃₂] ≠ 0 | offen | `✗` |

**Nächster Schritt:** Analyse der d₂-Differentiale im allgemeinen (ob weitere
d_r von E₂^{1,1} in andere Terme gehen können, r ≥ 3).

---

*Datei: `werkzeuge/neu11_e2_11_berechnung.md` | Erstellt: 19. Juni 2026 | NEU-11*
