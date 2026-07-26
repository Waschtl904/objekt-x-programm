# NEU-16/OP-3.1: Monoidladungs-Kriterium für σ_{iβ}-Invarianz von [L₃]

> Datum: 20. Juni 2026 | Status: ✓ [R] — Kriterium vollständig; Φ₃-Ladungsneutralität offen ❓ [O]
> Grundlage: GPT Pro Konsultation (20. Juni 2026)

---

## 1. Ziel

OP-3.1 fragt: Gilt ν([L₃]) = [L₃] für ν = σ_{iβ}?

Die GPT-Analyse hat OP-3.1 auf eine präzise rechnerische Frage reduziert.
Dieses Dokument hält das Ergebnis formal fest.

---

## 2. Monoidladung eines Hochschild-Kochains

### 2.1 Definition

Die BC-Zeitentwicklung wirkt auf homogene Elemente F = f · u_n via:

```
σ_z(f · u_n) = n^{iz} · f · u_n
```

Auf einem k-Kochain Ψ ∈ C^k(A, A) wirkt σ_z durch:

```
(σ_z · Ψ)(a₁, ..., a_k) = σ_z(Ψ(σ_{-z}(a₁), ..., σ_{-z}(a_k)))
```

Für Eingaben a_j = f_j · u_{n_j} mit Ausgabe-Monodromie u_{N_out} bekommt
jeder homogene Term den Faktor:

```
χ(Ψ)^{iz}   wobei   χ(Ψ) = N_out / (n₁ · n₂ · ... · n_k)
```

**Definition (Monoidladung):** χ(Ψ) = N_out / (n₁ · ... · n_k) ∈ Q_+×.

Für z = iβ:

```
σ_{iβ} · Ψ_χ = χ^{-β} · Ψ_χ
```

**Kernbeobachtung:** σ_{iβ} · Ψ = Ψ genau dann, wenn χ(Ψ) = 1. ✓ [M]

### 2.2 Der Hochschild-Rand erhält die Monoidladung

Da σ_z ein Algebra-Automorphismus ist, gilt:

```
σ_z · (δΨ) = δ(σ_z · Ψ)
```

Und da δ die Algebra-Multiplikation verwendet (Eingaben werden zusammengezogen
oder links/rechts multipliziert), bleibt das Verhältnis N_out / (n₀ · ... · n_k)
unter δ konstant:

```
χ(δΨ) = χ(Ψ)    ✓ [M]
```

**Konsequenz:** Die Ladung ist eine Kohomologie-Invariante:
wenn [Ψ] ∈ HH^k eine wohldefinierte Ladung χ trägt, dann ist χ unter δ stabil.

---

## 3. Lemma OP-3.1.1 — Monoidladungs-Kriterium ✓ [R]

**Lemma (OP-3.1.1):**

> Sei B = F³ A_BC^{an}, stabil unter σ_z.
> Zerfällt ein Kochain Ψ ∈ C^k(B, B) in monoid-homogene Komponenten Ψ_χ, so gilt:
>
> ```
> σ_{iβ} · Ψ_χ = χ^{-β} · Ψ_χ
> ```
>
> Eine Kohomologieklasse [Ψ] ist genau dann σ_{iβ}-invariant, wenn alle
> Ladungsanteile χ ≠ 1 kohomologisch verschwinden:
>
> ```
> [Ψ_{χ≠1}] = 0 in HH^k(B, B)
> ```

**Beweis:** Direkt aus §2.1–2.2. ✓ [M]

---

## 4. Test an ω̃₂

Für Eingaben a₁ = f · u_n, a₂ = g · u_m:

```
ω̃₂(fu_n, gu_m) ~ Ω(n) · f' · α_n(g') · u_{nm}
```

- Ausgabe-Monodromie: N_out = nm
- Eingabe-Monodromien: n₁ · n₂ = nm

```
χ(ω̃₂) = nm / nm = 1   ✓ [M]
```

**Ergebnis:** ω̃₂ ist ladungsneutral → σ_{iβ} · ω̃₂ = ω̃₂ für alle β. ✓ [M]

Das bestätigt rückwirkend: [ω̃₂] ∈ HH²(A, A) ist nicht nur N×-invariant (bekannt),
sondern monoidladungsneutral — eine stärkere Aussage.

---

## 5. Quadratische Operationen erhalten die Ladung

Für die Konstruktion von L₃ aus ω̃₂ werden verwendet:

| Operation | Ladungserhaltung |
|-----------|-----------------|
| Cup-Produkt Ψ₁ ⌣ Ψ₂ | χ(Ψ₁ ⌣ Ψ₂) = χ(Ψ₁) · χ(Ψ₂) = 1·1 = 1 ✓ |
| Gerstenhaber-Einsetzung Ψ₁ ∘_i Ψ₂ | χ multiplikativ erhalten ✓ |
| Gerstenhaber-Klammer [Ψ₁, Ψ₂]_G | χ = 1 für beide → χ = 1 ✓ |
| Massey-artige Produkte | Ladung durch Lift bestimmt — kritischer Punkt |

**Ergebnis:** Alle natürlichen quadratischen Operationen aus ω̃₂ liefern
Ladung χ = 1 — vorausgesetzt, die verwendeten Lifte sind ladungsneutral. ✓ [M]

---

## 6. Reduktion auf Φ₃

### 6.1 Die Formel

Da ∂ mit σ_z kommutiert (Symbolfiltration σ_z-invariant):

```
σ_{iβ} · [L₃] = σ_{iβ} · ∂([Φ₃]) = ∂(σ_{iβ} · [Φ₃])
```

Daher:

```
ν([L₃]) - [L₃] = ∂(ν([Φ₃]) - [Φ₃])
```

Wenn Φ₃ in Ladungskomponenten zerfällt:

```
ν([Φ₃]) - [Φ₃] = Σ_{χ≠1} (χ^{-β} - 1) · [Φ₃,χ]
```

Da χ^{-β} - 1 ≠ 0 für χ ≠ 1 und β > 0, folgt die **präzise Entscheidungsformel**:

```
ν([L₃]) = [L₃]   ⟺   ∂[Φ₃,χ] = 0 für alle χ ≠ 1
```

### 6.2 Die stärkere hinreichende Bedingung

```
Φ₃ ist ladungsneutral (χ(Φ₃) = 1)   ⟹   ν([Φ₃]) = [Φ₃]   ⟹   ν([L₃]) = [L₃]
```

---

## 7. OP-3.1 — Präzise Restfrage

**OP-3.1 ist jetzt reduziert auf:**

> **Kann der Symbol-Lift Φ₃ ladungsneutral gewählt werden?**

Das heißt: Existiert ein Vertreter Φ₃' ∈ [Φ₃] mit χ(Φ₃') = 1?

**Warum das plausibel ist:**

- ω̃₂ hat Ladung 1 ✓
- L₃ = ∂(Φ₃) ist quadratisch in ω̃₂ → natürliche Ladung = 1
- Falls Φ₃ durch einen non-equivarianten Lift konstruiert wurde,
  könnte er gemischte Ladungsanteile tragen — aber die Kohomologieklasse
  [Φ₃] könnte trotzdem einen ladungsneutralen Vertreter zulassen

**Warum das nicht trivial ist:**

- Der Symbol-Lift Φ₃ ist definiert über eine gefilterte Homotopie
- Diese Homotopie könnte nicht monoid-äquivariant sein
- Es braucht einen expliziten äquivarianten Liftbarkeitsnachweis

---

## 8. Gesamtresultat OP-3.1

```
OP-3.1 Reduktion (NEU-16/OP-3.1):   ✓ [R]

  [L₃] ist σ_{iβ}-invariant
  ⟺  χ([L₃]) = 1  (Ladungsneutralität)
  ⟺  ∂[Φ₃,χ] = 0 für alle χ ≠ 1
  ⟸  Φ₃ ladungsneutral wählbar

Bisheriger Status:
  ω̃₂ ist ladungsneutral:               ✓ [M]
  Quadratische Operationen erhalten χ=1: ✓ [M]
  Φ₃ ladungsneutral wählbar:            ❓ [O]  ← verbleibende Aufgabe

Wenn Φ₃ ladungsneutral wählbar:
  → ν([L₃]) = [L₃]                     ✓ [M]
  → ε_β wirkt als Spur auf [L₃]        ✓ [M]
  → ⟨ε_β, [L₃]⟩ wohldefiniert          ✓ [M]
  → OP-3 angreifbar via ⟨ε_β, [L₃]⟩   ⚠ [M]
```

---

## 9. Nächster konkreter Schritt: Äquivariante Liftbarkeit von Φ₃

**Zu zeigen:** Die gefilterte Homotopie, die Φ₃ konstruiert, kann
N×-äquivariant (= monoid-äquivariant) gewählt werden.

**Ansatz:**
Die Obstruktion zu einem äquivarianten Lift lebt in H¹(N×, C^{k-1}(F³, F³)).
Falls diese Gruppe verschwindet oder der Obstruktionskozykel trivial ist,
existiert ein ladungsneutraler Lift.

H¹(N×, C^{k-1}(F³, F³)) — das ist eine neue Kohomologiefrage,
strukturell analog zu H¹(N×, Ω¹(T)) aus NEU-11.

**Status:** ❓ [O] — nächster Schritt

---

*Datei: `werkzeuge/neu16_op3_1_monoidladung.md` | Erstellt: 20. Juni 2026 | NEU-16/OP-3.1*
*Grundlage: GPT Pro Konsultation (20. Juni 2026)*
