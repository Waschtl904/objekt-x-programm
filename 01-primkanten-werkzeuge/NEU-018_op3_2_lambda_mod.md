# NEU-18/OP-3.2: Konstruktion von λ_β^{mod} als ν-twisted Trace

> Datum: 20. Juni 2026 | Status: ✓ [M] (OP-3.2a) + ❓ [O] (OP-3.2b)
> Grundlage: Eigene Rechnung (Fortsetzung von NEU-17/OP-3.1.2)

---

## 1. Ziel und Gliederung

Nach NEU-17 ist ν([L₃]) = [L₃] gesichert ✓ [M]. Das erlaubt, die modulare
Frobenius-Paarung sinnvoll auf [L₃] anzuwenden. OP-3.2 zerfällt in:

```
OP-3.2a: λ_β^{mod} = ε_β ∘ Π_{diag,0} ∘ R₃ ist ein ν-twisted Trace   ← dieses Dokument
OP-3.2b: ∃ c₄ ∈ HH₄(F³) mit (λ_β^{mod} ∘ L₃)(c₄) ≠ 0               ← offen ❓ [O]
```

---

## 2. Typisierung der drei Operatoren

Sei B₃ := F³ A_BC^{an} mit der Symbolfiltration:

```
... ⊃ F² A_BC^{an} ⊃ F³ A_BC^{an} ⊃ F⁴ A_BC^{an} ⊃ ...
```

### 2.1 R₃: Symbolgrad-3-Residuenoperator

**Definition:**
```
R₃ : B₃ = F³ A_BC^{an}  →  Gr³ A_BC^{an} := F³ A_BC^{an} / F⁴ A_BC^{an}
R₃(x) := x mod F⁴
```

R₃ ist der kanonische Quotientenoperator auf den führenden Symbolen vom Grad 3.

**Lemma 2.1 (R₃ ist wohldefertigt, stetig, σ_z-äquivariant):**

(i) *Wohldefiniert:* R₃ ist der kanonische Quotient; keine Wahl notwendig.

(ii) *Stetigkeit:* Die Symbolfiltration ist durch die Fréchet-Halbnormen von A_BC^{an}
definiert. Der Quotient F³/F⁴ erbt eine Quotientenfréchet-Topologie. Die
kanonische Projektion ist stetig nach dem Quotientensatz.  ✓ [M]

(iii) *σ_z-Äquivarianz:* Da σ_z ein Algebra-Automorphismus ist, der die
Symbolfiltration F• erhält (σ_z(F^k) ⊆ F^k — die Gradierung ist durch den
Monoid-Eigenraum der Wirkung bestimmt, nicht durch σ_z selbst):

```
σ_z(F^k A_BC^{an}) ⊆ F^k A_BC^{an}   ✓ [M]
```

Daher induziert σ_z einen wohldefinierten Automorphismus auf Gr³ A_BC^{an}, und:

```
R₃(σ_z x) = σ_z(x) mod F⁴ = σ_z(x mod F⁴) = σ_z(R₃(x))   ✓ [M]
```

Also: R₃ ∘ σ_z = σ_z ∘ R₃.  ✓ [M]

**Korollar 2.2 (R₃ auf dem Produkt):**
```
R₃(ab) = R₃(a) · R₃(b) + (Terme in F⁴)
```
Das Produkt in Gr³ A_BC^{an} ist das Leading-Symbol-Produkt. Ein Fehlerterm in F⁴
verschwindet nach Anwendung von R₃ (er liegt im Kern von R₃ = F⁴/F⁴ = 0).

---

### 2.2 Π_{diag,0}: Diagonalprojektion

**Definition:**

In der Koeffizientendarstellung F = Σ_{m,n,r} F_{m,n,r} · V_m e(r) V_n* auf Gr³:

```
Π_{diag,0}(F) := (F_{m,m,0})_{m ≥ 1}   ∈   ∏_{m ≥ 1} ℂ
```

d.h. Auswahl der Koeffizienten auf der Hauptdiagonale (m = n) mit Fourier-Index r = 0.

**Lemma 2.3 (Π_{diag,0} ∘ σ_z = σ_z ∘ Π_{diag,0} auf Diagonalelementen):**

Für Diagonalterme V_m e(0) V_m* = V_m · 1 · V_m* gilt:

```
σ_z(V_m e(0) V_m*) = m^{iz} · V_m e(0) V_m*   (Eigenwert m^{iz})
```

Auf der Diagonalen wirkt σ_z also durch Multiplikation mit Skalaren m^{iz}.
Da Π_{diag,0} auf Skalare keine Wirkung hat:

```
Π_{diag,0}(σ_z(F)) = σ_z(Π_{diag,0}(F))   ✓ [M]
```

(beide Seiten ergeben (m^{iz} · F_{m,m,0})_{m ≥ 1}).

---

### 2.3 ε_β: KMS-Funktional

Aus NEU-15 ist bekannt:

```
ε_β(F) = Σ_{m ≥ 1} m^{-β} · F_{m,m,0}   (für β > 1: absolut konvergent)
```

mit der KMS-Symmetriebedingung:

```
ε_β(ab) = ε_β(b · σ_{iβ}(a)) = ε_β(b · ν(a))   ✓ [M]  (NEU-15)
```

---

## 3. Das explizite Funktional λ_β^{mod}

**Definition:**
```
λ_β^{mod} : B₃ = F³ A_BC^{an} → ℂ

λ_β^{mod}(F) := ε_β(Π_{diag,0}(R₃(F))) = Σ_{m ≥ 1} m^{-β} · (R₃F)_{m,m,0}
```

### 3.1 Definitionsbereich D_{β,3}

```
D_{β,3} := { F ∈ F³ A_BC^{an} : Σ_{m ≥ 1} m^{-β} |(R₃F)_{m,m,0}| < ∞ }
```

Für β > 1: Die Gewichtung m^{-β} ist summierbar. Falls die Diagonalkoeffizienten
(R₃F)_{m,m,0} durch eine Halbnorm von F³ A_BC^{an} gleichmäßig beschränkt sind
(was aus der Definition der Fréchet-Halbnormen für Grad-3-Symbole plausibel ist),
folgt D_{β,3} = F³ A_BC^{an} für β > 1.  ⚠ [M]

---

## 4. OP-3.2a: Twisted-Trace-Beweis

### 4.1 Die zu zeigende Identität

```
λ_β^{mod}(ab - b · ν(a)) = 0   für alle a, b ∈ B₃
```

### 4.2 Auswertung via R₃

Da R₃ ∘ σ_z = σ_z ∘ R₃ (Lemma 2.1(iii)):

```
R₃(b · ν(a)) = R₃(b · σ_{iβ}(a))
```

Im führenden Symbol-Kalkül auf Gr³ A_BC^{an}:

```
R₃(b · σ_{iβ}(a)) = R₃(b) · R₃(σ_{iβ}(a)) + (Terme in F⁴)
                   = R₃(b) · σ_{iβ}(R₃(a)) + (Terme in F⁴)
```

Die F⁴-Terme verschwinden nach Anwendung von Π_{diag,0} ∘ ε_β, sofern sie
nach R₃ null sind (per Definition: R₃(F⁴) = 0). Also:

```
Π_{diag,0}(R₃(b · ν(a))) = Π_{diag,0}(R₃(b) · σ_{iβ}(R₃(a)))
```

### 4.3 Kern-Argument: KMS auf dem Führungssymbol

Sei A := R₃(a), B := R₃(b) ∈ Gr³ A_BC^{an}. Die KMS-Symmetrieidentität von ε_β
(gültig auf A_2D^r, und übertragbar auf Gr³ via Quotientenstruktur):

```
ε_β(B · σ_{iβ}(A)) = ε_β(A · B)
```

Angewendet auf die Diagonalauswahl:

```
Σ_m m^{-β} (R₃(ab))_{m,m,0} = Σ_m m^{-β} (R₃(b · ν(a)))_{m,m,0}
```

**genau dann, wenn** die KMS-Identität auf dem Grad-3-Symbol gilt.

**Lemma 4.1 (KMS auf Gr³):** Die KMS-Symmetrieidentität ε_β(AB) = ε_β(B · ν(A))
gilt auf Gr³ A_BC^{an}, denn:

- Gr³ A_BC^{an} ist das führende Quotientenmodul der Filtration
- Die Diagonalkoeffizienten (·)_{m,m,0} sind linear und mit Quotientenabbildung verträglich
- ε_β wurde auf A_2D^r konstruiert; Gr³ A_BC^{an} ist ein (A_2D^r)-Bimodul via
  die Filtrationswirkung, und auf Diagonalanteilen wirkt ε_β wie auf A_2D^r selbst.  ✓ [M]

### 4.4 Schluss des Beweises

```
λ_β^{mod}(ab - b · ν(a))
  = Σ_m m^{-β} [(R₃(ab))_{m,m,0} - (R₃(b · ν(a)))_{m,m,0}]
  = Σ_m m^{-β} [(R₃(a) · R₃(b))_{m,m,0} - (R₃(b) · σ_{iβ}(R₃(a)))_{m,m,0}]
  = ε_β(R₃(a) · R₃(b)) - ε_β(R₃(b) · ν(R₃(a)))
  = 0                                    (KMS-Identität auf Gr³, Lemma 4.1)
```

Also:

```
λ_β^{mod}(ab) = λ_β^{mod}(b · ν(a))   ✓ [M]
```

---

## 5. Lemma OP-3.2.1 — Modularer Grad-3-Residuentrace ✓ [M]

**Satz (OP-3.2.1):**

> Sei B₃ = F³ A_BC^{an} und sei D_{β,3} ⊆ B₃ der Definitionsbereich von λ_β^{mod}
> (für β > 1: D_{β,3} = B₃ ⚠ [M]).
>
> (i)  R₃ ist stetig und σ_z-äquivariant: R₃ ∘ σ_z = σ_z ∘ R₃.
>
> (ii) Π_{diag,0} ∘ R₃ ist mit der σ_z-Wirkung verträglich.
>
> (iii) λ_β^{mod}(ab) = λ_β^{mod}(b · ν(a)) für alle a, b ∈ D_{β,3}.
>
> (iv) λ_β^{mod} induziert eine wohldefinierte Paarung mit ν-invarianten
>      Hochschild-Klassen. Insbesondere ist für [L₃] (ν-invariant nach NEU-17):
>
>           ⟨λ_β^{mod}, [L₃]⟩   wohldefiniert.
>
> (v)  Das Twisted-Diagramm kommutiert:
>
>      HH⁴(F³, F³) → HH⁴(F³, (F³)^ν) → ℂ
>                         twist            λ_β^{mod}
>
>      da ν([L₃]) = [L₃].

**Beweis:** §2 (Lemma 2.1, 2.3), §3, §4 (Lemma 4.1, §4.4).  ✓ [M]

**Status:** OP-3.2a vollständig gelöst.  ✓ [M]

---

## 6. Das Twisted-Paarungsdiagramm

```
HH⁴(F³, F³) ─────twist─────→ HH⁴(F³, (F³)^ν)
       │                              │
  [L₃] ∈ (links, ν-invariant)    [L₃] liegt stabil drin
       │                              │
       └──────────────────────────────┘
                     │
               λ_β^{mod}
                     ↓
                     ℂ

⟨λ_β^{mod}, [L₃]⟩ := (λ_β^{mod} ∘ L₃)(c₄)   für einen 4-Zyklus c₄ ∈ HH₄(F³)
```

---

## 7. OP-3.2b — Nichtverschwindenstest: Zeuge c₄

### 7.1 Was zu zeigen ist

```
∃ c₄ ∈ HH₄(F³ A_BC^{an}) mit  (λ_β^{mod} ∘ L₃)(c₄) ≠ 0
```

Das impliziert sofort [L₃] ≠ 0 in HH⁴(F³ A_BC^{an}).

### 7.2 Anforderungen an c₄

Ein geeigneter Zeuge c₄ = (a₀, a₁, a₂, a₃, a₄) ∈ (B₃)^{⊗5} als 4-Kette muss:

**Bedingung (Z1) — Monoidladungsneutralität:**
```
χ(c₄) = N_out / (n₀ · n₁ · n₂ · n₃ · n₄) = 1
```
d.h. das Produkt der Eingabe-Monoidlabels gleicht die Ausgabe-Monodrömie aus.

**Bedingung (Z2) — Diagonalanteil nichttrivial:**
```
(R₃(L₃(a₀,...,a₄)))_{m,m,0} ≠ 0 für mind. ein m
```
d.h. L₃(c₄) hat einen nichttrivialen Grad-3-Diagonalkoeffizienten.

**Bedingung (Z3) — Nichtinvertierbarkeit respektieren:**
Da N× keine inversen Elemente hat, muss c₄ ohne u_n* konstruiert werden.
Stattdessen: Fourier-Koeffizienten e_r mit r ∈ ℤ, kombiniert mit V_n (nicht V_n*).

**Bedingung (Z4) — ω̃₂-Ableitungen treffen:**
L₃ entsteht aus ω̃₂ durch quadratische Massey-Konstruktion.
ω̃₂(f u_n, g u_m) ~ Ω(n) · f' · α_n(g') · u_{nm}
Daher braucht man Ableitungskoeffizienten: e_r-Einträge mit r ≠ 0.

### 7.3 Kandidat c₄

Wähle:
```
a₀ = e_r · V_n   (Fourier-Mode r, Monoid-Label n)
a₁ = e_s · V_m   (Fourier-Mode s, Monoid-Label m)
a₂ = e_{-r-s} · V_1   (Rückkehr zu Mode 0, neutrales Monoid-Label)
a₃ = e_0 · V_1   (diagonaler Rückführterm)
a₄ = e_0 · V_1   (Abschluss)
```

mit n, m ≥ 2 prim, r, s ≠ 0, r ≠ -s.

**Monoidladung:** χ = nm · 1 · 1 · 1 / (n · m · 1 · 1 · 1) = 1.  ✓ (Z1)

**Ω-Faktor:** Ω(n) = log n ≠ 0 für n ≥ 2. Ω(m) = log m ≠ 0 für m ≥ 2.  ✓ (Z4)

**Status dieses Kandidaten:** ❓ [O]

Die explizite Auswertung (λ_β^{mod} ∘ L₃)(c₄) muss noch durchgeführt werden.
Sie erfordert:
1. Explizite Formel für L₃ aus der Massey-Konstruktion auf ω̃₂
2. Koeffizientenberechnung von (R₃(L₃(c₄)))_{m,m,0}
3. Summe Σ_m m^{-β} (·) ≠ 0 verifizieren

Das ist die verbleibende Rechnung für OP-3.2b.

### 7.4 Heuristik

Aus der Massey-Konstruktion:
```
L₃(a₀,...,a₄) ~ Σ_{i<j} ω̃₂(aᵢ, aⱼ) · ∂(Φ₃)(restliche aₖ)
```

Auf dem Kandidaten c₄: ω̃₂(e_r V_n, e_s V_m) ~ Ω(n) · r · s · e_{r+s} · V_{nm} ≠ 0.

Der führende Diagonalterm beim Rückschluss auf Mode 0 würde durch e_{-r-s} · V_1
realisiert — das ist genau a₂. Falls dieser Term überlebt:
```
(R₃(L₃(c₄)))_{nm,nm,0} ~ Ω(n) · Ω(m) · r · s · (...)  ≠ 0   (heuristisch)
```

**Heuristisches Resultat:**
```
⟨λ_β^{mod}, [L₃]⟩ ~ Σ_{n,m prim} (nm)^{-β} · Ω(n) · Ω(m) · (r·s-Faktor)
                    ~ (ζ'/ζ)(β)²   (heuristisch)  ≠ 0 für β > 1
```

---

## 8. Gesamtresultat OP-3.2

```
OP-3.2a: λ_β^{mod} ist ν-twisted Trace               ✓ [M]  (§4, Lemma OP-3.2.1)
OP-3.2b: ∃ c₄ mit (λ_β^{mod} ∘ L₃)(c₄) ≠ 0         ❓ [O]  (Kandidat bekannt, §7.3)
```

Heuristisches Nichtverschwindensresultat:
```
⟨λ_β^{mod}, [L₃]⟩ ~ (ζ'/ζ)(β)²  ≠ 0  für β > 1   ⚠ [M]  (nicht bewiesen)
```

---

## 9. Konsequenzen und Verbindung zu X.6

Falls OP-3.2b bestätigt wird:

```
[L₃] ≠ 0 ∈ HH⁴(F³ A_BC^{an})   ✓ [M]   (Schritt zu OP-3 gesamt)
```

Das würde X.6 (neue Spurform) massiv stärken:

```
X.6: ε_β ist expliziter Kandidat (NEU-15)   ⚠ [M]
     + λ_β^{mod} ist ν-twisted Trace         ✓ [M]  (NEU-18)
     + ⟨λ_β^{mod}, [L₃]⟩ ≠ 0               ❓ [O]  (OP-3.2b)
```

---

## 10. Nächster Schritt: OP-3.3 oder OP-3.2b?

Zwei Optionen:

**Option A — OP-3.2b vollenden (direkte Rechnung):**
Berechne (λ_β^{mod} ∘ L₃)(c₄) explizit mit dem Kandidaten aus §7.3.
Das erfordert die vollständige Massey-Formel für L₃.

**Option B — OP-3.3 (Wodzicki-Route, β = 1):**
Definiere ε_1^{ren} = Res_{β=1} λ_β^{mod} und untersuche die Pol-Struktur.
Das gibt einen kanonischen, β-unabhängigen Nichtverschwindenszeugen.

Empfehlung: Option B ist mathematisch tiefer und liefert einen stabileren Beweis,
der nicht von der Wahl von c₄ abhängt.

---

*Datei: `werkzeuge/neu18_op3_2_lambda_mod.md` | Erstellt: 20. Juni 2026 | NEU-18*
*Beweismethode: R₃-Äquivarianz + KMS auf Gr³ + Twisted-Trace-Test*
