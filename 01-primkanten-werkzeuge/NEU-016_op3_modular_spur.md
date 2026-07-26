# NEU-16: OP-3 — Modulare Spur auf F³ A_BC^{an}

> Datum: 20. Juni 2026 | Status: ⚠ [M] — Strategie geklärt, Konstruktion offen
> Grundlage: GPT Pro Konsultation (20. Juni 2026) + Katalogsynthese

---

## 1. Ausgangslage

**OP-3** (kritischer Engpass nach NEU-15/R3):

> [L₃] ∈ HH⁴(F³ A_BC^{an}) — trivial oder nicht?

Aus dem Katalog (F48): Das eigentliche Problem ist nicht die Berechnung von [L₃],
sondern die Konstruktion eines Funktionals λ: HH⁴(F³ A_BC^{an}) → ℂ mit λ(Im δ) = 0.

**Neue Ressource (NEU-15):**
A_2D^r trägt eine modulare Frobenius-Paarung:
```
ε_β(F) = Σ_m m^{-β} F_{m,m,0},   ε_β(ab) = ε_β(b · σ_{iβ}(a))
```

**Frage (NEU-15/R3 → NEU-16):**
Kann ε_β als Startpunkt für λ auf F³ A_BC^{an} verwendet werden?

---

## 2. Diagnose: Warum naive Einschränkung nicht reicht

### 2.1 Das Twisted-Trace-Problem

ε_β ist kein gewöhnlicher Trace — es gilt nur die KMS-Symmetriebedingung:

```
ε_β(ab) = ε_β(b · σ_{iβ}(a))   (Nakayama-Automorphismus ν = σ_{iβ})
```

Für einen gewöhnlichen Hochschild-Rand δ(ψ) = bψ gilt:

```
ε_β(δψ(a₀,...,a₄)) = ε_β(Σ ±a₀...a_i a_{i+1}...a₄)
```

Die zyklische Verschiebung, die bei gewöhnlichen Traces λ(Im δ) = 0 erzwingt,
funktioniert hier **nicht** — weil ε_β(ab) ≠ ε_β(ba).

**Konsequenz** ✓ [M]:
```
ε_β|_{F³}(Im δ) = 0   ist im gewöhnlichen HH⁴(F³, F³) falsch oder unbegründet.
```

### 2.2 Was ε_β tatsächlich tötet

ε_β tötet nur **modular verdrehte Ränder**:

```
ε_β(Im δ_ν) = 0,   wobei δ_ν der ν-twisted Hochschild-Rand.
```

Das heißt: Die natürliche Heimat von ε_β ist nicht HH⁴(F³, F³), sondern:

```
HH⁴(F³ A_BC^{an}, (F³ A_BC^{an})^{σ_{iβ}})
```

der modular verdrehte Koeffizientenmodul.

---

## 3. Zwei Strategien für OP-3

### Strategie A: OP-3 in den modular verdrehten Komplex verschieben

Reformuliere OP-3 als Frage in HH⁴(F³, (F³)^ν):

> Ist [L₃] ∈ HH⁴(F³ A_BC^{an}, (F³ A_BC^{an})^{σ_{iβ}}) nicht-trivial?

Falls [L₃] natürlich in diesem verdrehten Komplex lebt, ist ε_β|_{F³} direkt eine
Paarung mit [L₃] — und die Bedingung λ(Im δ_ν) = 0 ist automatisch erfüllt.

**Vorteil**: Technisch sauber, nutzt ε_β direkt.
**Risiko**: [L₃] ist ursprünglich als Klasse in HH⁴(F³, F³) konstruiert — der
Übergang in den verdrehten Komplex erfordert einen Vergleichsmorphismus.

### Strategie B: Nachweis ν([L₃]) = [L₃]

Falls der sekundäre Obstruktionsgenerator [L₃] unter dem Nakayama-Automorphismus
ν = σ_{iβ} invariant ist:

```
ν([L₃]) = [L₃]   in HH⁴(F³ A_BC^{an})
```

dann fallen twisted und ordinary pairing auf [L₃] zusammen:

```
⟨ε_β, [L₃]⟩_{twisted} = ⟨ε_β, [L₃]⟩_{ordinary}
```

**Vorteil**: OP-3 bleibt in seiner ursprünglichen Form, kein Komplex-Wechsel nötig.
**Schlüsselfrage**: Ist [L₃] σ_{iβ}-invariant?

[L₃] = ∂([Φ₃]) ist quadratisch in [ω̃₂]. Da [ω̃₂] N×-invariant ist und σ_t die
N×-Gradierung erhält, könnte [L₃] tatsächlich σ_{iβ}-invariant sein.
**Status**: ⚠ [M] — plausibel, nicht bewiesen.

---

## 4. Der kanonische Kandidat: λ_β^{mod}

Aus der GPT-Konsultation (20. Juni 2026), Synthese:

```
λ_β^{mod} = ε_β ∘ Π_{diag,0} ∘ R₃
```

wobei:
- R₃: F³ A_BC^{an} → F³/F⁴ A_BC^{an}  (Symbol-Grad-3-Restriktion/Projektion)
- Π_{diag,0}: Projektion auf den diagonalen (m,n) = (m,m)-Anteil mit r = 0
- ε_β: KMS-Gewichtung Σ_m m^{-β} (·)_{m,m,0}

**Eigenschaften:**

(i) **Twisted-Trace-Eigenschaft:**
```
λ_β^{mod}(ab) = λ_β^{mod}(b · σ_{iβ}(a))   ⚠ [M]
```
(Folgt aus ε_β-Eigenschaft, falls R₃ und Π_{diag,0} mit σ_{iβ} verträglich sind.)

(ii) **Stetigkeit auf F³ A_BC^{an}:**
Hängt davon ab ob F³ A_BC^{an} ⊆ Dom(ε_β) — d.h. ob die Diagonalkoeffizienten
von Elementen aus F³ β-summierbar sind. Für β > 1 plausibel. ⚠ [M]

(iii) **Paarungsbedingung:**
```
λ_β^{mod}(Im δ_ν) = 0   ✓ [M]   (aus twisted-trace Eigenschaft)
λ_β^{mod}(Im δ) = 0     ⚠ [M]   (nur falls ν([L₃]) = [L₃] oder Komplex-Verschiebung)
```

---

## 5. Der kritische Fall β = 1 (Phasenübergang)

Bei β = 1 ist Z(β) = ζ(1) = ∞ — die naive Summe Σ_m m^{-1} divergiert.

**Renormalisierte Version:**

Analog zum Wodzicki-Residuum (Pol bei s = 0 der ζ-Funktion):

```
ε_1^{ren}(F) = Res_{β=1} ε_β(F) = Res_{β=1} Σ_m m^{-β} F_{m,m,0}
             = lim_{β→1⁺} (β-1) · Σ_m m^{-β} F_{m,m,0}
```

Falls Σ_m F_{m,m,0}/m eine Polstelle bei β = 1 hat:

```
ε_1^{ren}(F) = (Residuum der Dirichlet-Reihe D_F(β) = Σ_m m^{-β} F_{m,m,0} bei β=1)
```

**Verbindung zu Wodzicki**: Das ist formal analog zur Wodzicki-Restspur
(Residuum der Zeta-Funktion des Operators), aber für das BC-Monoid N× statt
für Pseudodifferentialoperatoren. Das ist genau der "asymptotische Wodzicki-Typ Trace
mit Monoid-Anisotropie" aus F48!

```
ε_1^{ren}  =  "monoid-anisotroper Wodzicki-Typ Trace"   ⚠ [M]
```

Das ist ein neues Objekt — weder klassischer Wodzicki noch Standard-Tsygan.

---

## 6. Drei Unterprobleme für OP-3 (revidierte Agenda)

Die ursprüngliche Forschungsagenda (F50) wird durch NEU-16 präzisiert:

### OP-3.1: σ_{iβ}-Invarianz von [L₃]

> Gilt ν([L₃]) = σ_{iβ}([L₃]) = [L₃] in HH⁴(F³ A_BC^{an})?

**Ansatz**: [L₃] = ∂([Φ₃]) ist quadratisch in [ω̃₂]. Da [ω̃₂] N×-invariant und
σ_t die N×-Gradierung erhält, transformiert [L₃] unter σ_{iβ} wie [ω̃₂]² → 1.
Aber: Die analytische Fortsetzung t → iβ ist nicht trivial.

**Status**: ❓ [O] — erste Priorität

### OP-3.2^{mod}: Twisted Paarung auf HH⁴(F³, (F³)^ν)

> Konstruiere λ_β^{mod}: F³ A_BC^{an} → ℂ mit λ_β^{mod}(ab) = λ_β^{mod}(b·σ_{iβ}(a))
> und verifiziere F³ A_BC^{an} ⊆ Dom(ε_β) für β > 1.

**Ansatz**:
1. Zeige σ_{iβ}(F³) ⊆ F³ (Symbolfiltration σ_t-invariant)
2. Zeige R₃ und Π_{diag,0} sind mit σ_{iβ} verträglich
3. Dominanzbedingung: Diagonalkoeffizienten von F³-Elementen sind β-summierbar

**Status**: ❓ [O] — zweite Priorität

### OP-3.3: Monoid-anisotroper Wodzicki-Trace

> Ist ε_1^{ren}(F) = Res_{β=1} Σ_m m^{-β} F_{m,m,0} ein wohldefiniiertes
> Funktional auf F³ A_BC^{an}, das Im δ tötet?

**Ansatz**: Zeta-Funktions-Renormierung analog Wodzicki, aber für N×.
Verbindung zu Etappe 1 der alten Agenda (zyklische Theorie für Gr A_BC^{an}).

**Status**: ❓ [O] — dritte Priorität, aber konzeptuell am tiefsten

---

## 7. Gesamtstatus OP-3 nach NEU-16

```
OP-3 (ursprünglich): [L₃] ≠ 0 in HH⁴(F³ A_BC^{an})?   ✗ offen

NEU-16 Beitrag:
  – Naive ε_β|_{F³} reicht nicht für λ(Im δ) = 0          ✓ [M]  (negatives Resultat)
  – Twisted-Trace λ_β^{mod} ist richtiger Kandidat          ⚠ [M]
  – Drei präzise Unterprobleme identifiziert                 ✓ [R]
  – Verbindung ε_1^{ren} ↔ monoid-anisotroper Wodzicki     ⚠ [M]

Nächste Priorität: OP-3.1 (σ_{iβ}-Invarianz von [L₃])
```

---

## 8. Zusammenfassung

```
NEU-16 Hauptresultat:

Die modulare Frobenius-Spur ε_β liefert keinen fertigen
klassischen Trace für OP-3 — aber sie liefert den besten
bisher bekannten Ausgangspunkt für eine modulare Reparatur.

Kernstruktur:
  λ_β^{mod} = ε_β ∘ Π_{diag,0} ∘ R₃  ist Kandidat für Etappe 2  ⚠ [M]
  ε_1^{ren} = Res_{β=1} ε_β            ist Kandidat für Etappe 3  ⚠ [M]

Schlüsselfrage: ν([L₃]) = [L₃]?  → OP-3.1  ❓ [O]
```

---

*Datei: `werkzeuge/neu16_op3_modular_spur.md` | Erstellt: 20. Juni 2026 | NEU-16*
*Grundlage: GPT Pro Konsultation (20. Juni 2026)*
