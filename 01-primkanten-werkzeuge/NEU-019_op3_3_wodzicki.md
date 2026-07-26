# NEU-19/OP-3.3: Kritischer BC-Wodzicki-Koeffizient

> Datum: 20. Juni 2026 | Status: ✓ [M] (Lemma OP-3.3.1, Trace-Eigenschaft) + ⚠ [M] (Asymptotik)
> Grundlage: Eigene Rechnung (Fortsetzung von NEU-18/OP-3.2)

---

## 1. Ausgangslage und Ziel

Aus NEU-18 ist λ_β^{mod}(F) = Σ_m m^{-β} (R₃F)_{m,m,0} ein ν_β-twisted Trace
für β > 1. Bei β = 1 divergiert die Reihe naiv. OP-3.3 fragt:

> **Existiert ein wohldefinieter kritischer Grenzoperator bei β → 1⁺,
> der einen ν₁-twisted Trace auf F³ A_BC^{an} liefert?**

Die Antwort hängt vom Singularitätstyp der Funktion β ↦ λ_β^{mod}(F) ab.

---

## 2. Diagonalasymptotik von (R₃L₃){m,m,0}

### 2.1 Die L₃-Konstruktion

L₃ ∈ C⁴(F³ A_BC^{an}, F³ A_BC^{an}) entsteht aus ω̃₂ durch die Massey/BV-Sekundärkonstruktion.
Die führende Struktur ist:

```
L₃(a₀,...,a₄) = Σ_{0 ≤ i < j ≤ 4} ε_{ij} · ω̃₂(aᵢ, aⱼ) ∪_{BV} Φ₃(restliche a_k)
```

Auf homogenen Elementen a_k = f_k · V_{n_k} mit Fourier-Moden e_{r_k}:

```
ω̃₂(f V_n, g V_m) = Ω(n) · f' · α_n(g') · V_{nm}   (aus NEU-15/R3, NEU-16)
```

wobei Ω(n) = log n der arithmetische Faktor ist (Anzahl Primteiler mit Vielfachheit,
da ω̃₂ den Schritt V_n · e(r) · V_n* = e(nr) verwendet und Ω(n) = Σ_{p|n} v_p(n) · log p).

**Wichtige Präzisierung:** Ω(n) im Kontext von ω̃₂ ist tatsächlich
```
Ω̃(n) := log n  (stetige Erweiterung der Monoid-Gradierung)
```
nicht die additive Primteiler-Funktion. Für Primzahlen p: Ω̃(p) = log p = Λ(p)
(von-Mangoldt-Funktion, für Primzahlpotenzen p^k: Λ(p^k) = log p, sonst 0).

### 2.2 Führendes Diagonalelement

Für den Grad-3-Anteil von L₃, ausgewertet auf dem Kandidaten
```
c₄ = (e_{r} V_n,  e_{s} V_m,  e_{-r-s} V_1,  e_0 V_1,  e_0 V_1)
```
mit n, m Primzahlen und r, s ≠ 0:

Der führende Beitrag zu (R₃ L₃(c₄))_{N,N,0} kommt vom Term i=0, j=1:

```
ω̃₂(e_r V_n, e_s V_m) = log n · (ir) · α_n(is · e_s) · V_{nm}
                      = -rs · log n · e_{r + ns} · V_{nm}
```

(Ableitungsregel: (e_r)' = ir · e_r auf T; α_n(e_s) = e_{ns})

Der Rückführterm durch (e_{-r-s} V_1) auf Diagonale r = 0 erfordert:

```
r + ns = -(r + s)  ⟺  ns = -2r - s  ⟺  s(n+1) = -2r
```

Für n ≥ 2 prim und geeignete r = -s(n+1)/2 (mit r, s ∈ ℤ, r+s ≠ 0):
Das Diagonalelement (m,m) = (nm, nm) hat Koeffizient:

```
(R₃ L₃(c₄))_{nm, nm, 0} ~ rs · log n · log m · C_{r,s}
```

wobei C_{r,s} ein Normierungsfaktor aus der Φ₃-Homotopie ist.

### 2.3 Summe über m (Dirichlet-Reihe)

Die Auswertung λ_β^{mod}(L₃(c₄)) summiert über alle Monoid-Labels M = nm:

```
Σ_M M^{-β} (R₃ L₃(c₄))_{M,M,0}
~ Σ_{n,m prim} (nm)^{-β} · rs · log n · log m · C_{r,s}
= rs · C_{r,s} · [Σ_n prim n^{-β} log n]²
```

Für Primzahlen:
```
Σ_{p prim} p^{-β} log p = -ζ'(β)/ζ(β)  (primo) + Σ_{p^k, k≥2} p^{-kβ} log p · (korrektiv)
```

Genauer: Die von-Mangoldt-Reihe:
```
-ζ'(β)/ζ(β) = Σ_{n≥1} Λ(n) n^{-β}
```

Für β > 1: Λ(n) = log p wenn n = p^k, sonst 0.
Das dominante Verhalten bei β → 1⁺ kommt von Primzahlen:

```
Σ_p p^{-β} log p ~ 1/(β-1)   (aus dem Primzahlsatz / Polresiduum von -ζ'/ζ)
```

Also:

```
λ_β^{mod}(L₃(c₄)) ~ rs · C_{r,s} · [1/(β-1)]²  =  rs · C_{r,s} / (β-1)²
```

**Singularitätstyp: Doppelpol bei β = 1.** (Λ-Typ: (β-1)^{-2})

---

## 3. Der Twist-Korrekturterm bei β → 1

### 3.1 β-Abhängigkeit von ν_β

Für β > 1 gilt die twisted-trace-Eigenschaft mit ν_β = σ_{iβ}.
Für β → 1, entwickle:

```
ν_β(a) = σ_{iβ}(a) = ν₁(a) + (β-1) · ν̇₁(a) + O((β-1)²)
```

wobei ν̇₁ = ∂/∂β|_{β=1} σ_{iβ} = i · d/dz|_{z=i} σ_z.

### 3.2 Wirkung auf den Singularitätskoeffizienten

Die twisted-trace-Gleichung:
```
λ_β^{mod}(ab) - λ_β^{mod}(b ν_β(a)) = 0
```

Entwickle bei β = 1:
```
λ_β^{mod}(ab) - λ_β^{mod}(b ν₁(a)) = λ_β^{mod}(b(ν_β - ν₁)(a))
                                     = (β-1) · λ_β^{mod}(b ν̇₁(a))
```

Wenn λ_β^{mod} ~ C/(β-1)², dann λ_β^{mod}(b ν̇₁(a)) ~ D/(β-1)².
Also:

```
λ_β^{mod}(b(ν_β - ν₁)(a)) ~ (β-1) · D/(β-1)² = D/(β-1)   ← EINFACHERER Pol!
```

**Schlüsselfolgerung:** Der Twist-Korrekturterm hat eine Singularitätsordnung
niedriger als der Hauptterm. Daher:

**Lemma 3.1 (Twist-Stabilität des führenden Koeffizienten):**
Der führende Singularitätskoeffizient (Doppelpol bei β=1) der Funktion
β ↦ λ_β^{mod}(ab) stimmt mit dem von β ↦ λ_β^{mod}(b ν₁(a)) überein.
D.h.:

```
Wres_BC^{(2,0)}(ab) = Wres_BC^{(2,0)}(b ν₁(a))   ✓ [M]
```

Der führende Wodzicki-Koeffizient ist ein ν₁-twisted Trace.

---

## 4. Log-polyhomogene Expansion und Wodzicki-Koeffizienten

### 4.1 Allgemeine Expansion

Für F ∈ F³ A_BC^{an} mit (R₃F)_{m,m,0} ~ Σ_k a_k(F) · (log m)^k:

```
λ_β^{mod}(F) = Σ_m m^{-β} (R₃F)_{m,m,0}
             ~ Σ_k a_k(F) · (-1)^k ζ^{(k)}(β)   bei β → 1⁺
```

Da ζ(β) ~ 1/(β-1) und ζ^{(k)}(β) ~ (-1)^k k!/(β-1)^{k+1}:

```
λ_β^{mod}(F) ~ Σ_k a_k(F) · k! / (β-1)^{k+1}
```

**Singularitätstabelle:**

| Asymptotik von (R₃F)_{m,m,0} | Singularität von λ_β^{mod}(F) |
|---|---|
| konstant (keine log m) | (β-1)^{-1}  (einfacher Pol) |
| ~ log m | (β-1)^{-2}  (Doppelpol) |
| ~ (log m)² | (β-1)^{-3}  (dreifacher Pol) |
| ~ Λ(m) = 0 fast überall | (β-1)^{-2}  (aus -ζ'/ζ) |
| ~ Ω(m) log m | (β-1)^{-1} · (log 1/(β-1))²  (log-Pol) |

### 4.2 Diagnose für L₃

Aus §2.3: (R₃ L₃(c₄))_{M,M,0} ~ Σ_{nm=M, n,m prim} log n · log m.

Per von-Mangoldt-Faltung:
```
Σ_{nm=M} Λ(n) Λ(m) = Λ²(M)   (von-Mangoldt-Konvolution)
```

Die Dirichlet-Reihe der Konvolution Λ² = Λ * Λ:
```
Σ_M Λ²(M) M^{-β} = (-ζ'(β)/ζ(β))²  = [Σ_n Λ(n) n^{-β}]²
```

Bei β → 1⁺:
```
(-ζ'/ζ)(β) ~ 1/(β-1)   ⟹   (-ζ'/ζ)²(β) ~ 1/(β-1)²
```

**Ergebnis:** Der führende Singularitätstyp ist:

```
λ_β^{mod}(L₃(c₄)) ~ C / (β-1)²     (Doppelpol, Λ-Typ)
```

mit
```
C = rs · C_{r,s}   ≠ 0   (für r, s ≠ 0 und C_{r,s} ≠ 0)   ⚠ [M]
```

---

## 5. Definition des BC-Wodzicki-Koeffizienten

### 5.1 Log-polyhomogene Familie

**Definition (BC-Wodzicki-Koeffizient):**

Sei F ∈ F³ A_BC^{an} so dass β ↦ λ_β^{mod}(F) bei β = 1⁺ eine log-polyhomogene
Expansion besitzt:

```
λ_β^{mod}(F) ~ Σ_{q≥1, ℓ≥0} c_{q,ℓ}(F) · (β-1)^{-q} · (log 1/(β-1))^ℓ + O(1)
```

Dann definiere:
```
Wres_BC^{(q,ℓ)}(F) := c_{q,ℓ}(F)
```

Den **führenden BC-Wodzicki-Koeffizienten**:
```
Wres_BC^{top}(F) := c_{q_max, ℓ_max}(F)
```

(lexikographisch höchste nichtverschwindende Komponente).

### 5.2 Für L₃: Der kanonische Koeffizient

Aus §4.2:

```
Wres_BC^{top}(L₃) = Wres_BC^{(2,0)}(L₃) = lim_{β→1⁺} (β-1)² · λ_β^{mod}(L₃(·))
```

Das ist der **renormierte Paarungsfunktional**:

```
⟨Wres_BC^{(2,0)}, [L₃]⟩ := lim_{β→1⁺} (β-1)² · ⟨λ_β^{mod}, [L₃]⟩
```

---

## 6. Lemma OP-3.3.1 — Kritischer BC-Wodzicki-Koeffizient

**Satz (OP-3.3.1):**

> Sei λ_β^{mod} der modulare Grad-3-Trace aus NEU-18 (β > 1).
> Angenommen, für F im relevanten Symbolbereich existiert die log-polyhomogene
> Expansion von β ↦ λ_β^{mod}(F) bei β = 1⁺.
>
> (i)  **Twist-Stabilität** (Lemma 3.1): Der führende Singularitätskoeffizient
>      Wres_BC^{top} ist ein ν₁-twisted Trace:
>
>           Wres_BC^{top}(ab) = Wres_BC^{top}(b · ν₁(a))   ✓ [M]
>
>      (Beweis: Der Twist-Korrekturterm (β-1)·λ_β^{mod}(b ν̇₁(a)) hat
>      niedrigere Singularitätsordnung als der Hauptterm.)
>
> (ii) **Wohldefiniertheit:** Da nach NEU-17 ν₁([L₃]) = [L₃], ist
>
>           Wres_BC^{top} ∘ L₃
>
>      ein wohldefiniertes skalares Funktional auf HH₄(F³ A_BC^{an}).
>
> (iii) **Singularitätstyp für L₃** (Λ-Typ, Doppelpol): ⚠ [M]
>
>           Wres_BC^{(2,0)}(L₃(c₄)) = lim_{β→1⁺} (β-1)² · λ_β^{mod}(L₃(c₄))
>                                    ~ rs · C_{r,s} · [lim_{β→1⁺} (β-1)·(-ζ'/ζ)(β)]²
>                                    = rs · C_{r,s} · 1
>
>      Falls C_{r,s} ≠ 0 und rs ≠ 0 (d.h. r, s ≠ 0 beliebige ganze Zahlen),
>      dann:
>
>           ⟨Wres_BC^{(2,0)}, [L₃]⟩ ≠ 0   ⚠ [M]

**Beweis von (i):** §3.2 (Twist-Stabilitätsargument).  ✓ [M]

**Beweis von (ii):** Direkt aus NEU-17 (ν₁([L₃]) = [L₃]).  ✓ [M]

**Status von (iii):** ⚠ [M] — der C_{r,s}-Faktor aus der Φ₃-Homotopie
muss noch explizit bestimmt werden.

---

## 7. Die kritische Konstantenkontrolle: C_{r,s}

### 7.1 Woher kommt C_{r,s}?

C_{r,s} ist der Koeffizient aus der Massey-Homotopie Φ₃, der den Rückführterm
auf der Diagonale kontrolliert. Explizit:

```
C_{r,s} = ⟨Φ₃(e_{-r-s} V_1, e_0 V_1, e_0 V_1)⟩_{diag}
```

d.h. das Diagonalelement von Φ₃ ausgewertet auf den neutralen Zeugenkomponenten.

### 7.2 Nichtverschwindensheuristik

Da Φ₃ eine Homotopie zwischen ω̃₂ ∪ ω̃₂ und 0 (als Hochschild-Korand) ist,
und ω̃₂ ∪ ω̃₂ explizit nichttrivial ist (aus NEU-15/R3 folgt [ω̃₂] ≠ 0,
daher auch [ω̃₂ ∪ ω̃₂] ≠ 0 a priori), muss Φ₃ „viel korrigieren" —
d.h. seine Diagonalwerte sind generisch nichttrivial.

**Heuristik:** C_{r,s} ≠ 0 für generische r, s.  ⚠ [M]

### 7.3 Alternative: Topologischer Nichtverschwindensbeweis

Falls C_{r,s} schwer zu kontrollieren ist, gibt es einen eleganten Umweg:

Zeige direkt, dass Wres_BC^{(2,0)} als Funktional auf HH⁴(F³) nicht
identisch null ist. Das folgt aus der universellen Eigenschaft des
Wodzicki-Residuums: In einem nicht-kommutativen Ω-dimensionalen Kalkül
ist das Residuum-Funktional stets eindeutig und nicht-null.

Für den BC-Fall (N× statt Differentialoperatoren) ist die analoge Aussage:

```
Wres_BC^{(2,0)} ≢ 0   auf F³ A_BC^{an}   ⚠ [M]
```

Das wäre die stärkste Formulierung von OP-3.3.

---

## 8. Wodzicki-Vergleichstabelle

| Klassischer Wodzicki | BC-Wodzicki (OP-3.3) |
|---|---|
| ΨDO auf kompakter Mannigfaltigkeit | F³ A_BC^{an} (Grad-3-Symbol) |
| Σ-Spur (Symbolintegral auf S*M) | λ_β^{mod} (Diagonalsumme mit m^{-β}) |
| Einfacher Pol bei s=0 (ζ-Funk.) | Doppelpol bei β=1 (Λ²-Typ) |
| Gewöhnlicher Trace (symmetrisch) | ν₁-twisted Trace (KMS-Symmetrie) |
| Wres: ΨDO → ℂ eindeutig | Wres_BC^{(2,0)}: F³ A_BC^{an} → ℂ |
| Wres(ab) = Wres(ba) | Wres_BC^{top}(ab) = Wres_BC^{top}(b ν₁(a)) |

---

## 9. Gesamtresultat OP-3.3

```
OP-3.3 Hauptresultat (NEU-19):

Lemma OP-3.3.1:
  (i)  Wres_BC^{top} ist ν₁-twisted Trace            ✓ [M]
  (ii) ⟨Wres_BC^{top}, [L₃]⟩ wohldefiniert           ✓ [M]  (via NEU-17)
  (iii) Singularitätstyp: Doppelpol (β-1)^{-2}       ⚠ [M]  (Λ-Typ)
  (iv)  ⟨Wres_BC^{(2,0)}, [L₃]⟩ ~ rs · C_{r,s}      ⚠ [M]  (C_{r,s} offen)

Offene technische Frage (OP-3.3-Restaufgabe):
  C_{r,s} = ⟨Φ₃(e_{-r-s} V_1, ...)⟩_{diag} ≠ 0?   ❓ [O]
```

---

## 10. OP-3 Gesamtbilanz nach NEU-19

```
OP-3.1:  ν([L₃]) = [L₃]                           ✓ [M]   NEU-17
OP-3.2a: λ_β^{mod} ist ν_β-twisted Trace           ✓ [M]   NEU-18
OP-3.2b: ∃ c₄ mit (λ_β^{mod} ∘ L₃)(c₄) ≠ 0       ⚠ [M]   heuristisch (Kandidat bekannt)
OP-3.3:  Wres_BC^{top} ist ν₁-twisted Trace        ✓ [M]   NEU-19
         ⟨Wres_BC^{(2,0)}, [L₃]⟩ ~ rs · C_{r,s}   ⚠ [M]   C_{r,s} offen

Kritischer Restpunkt für OP-3:
  C_{r,s} ≠ 0 oder Wres_BC^{(2,0)} ≢ 0            ❓ [O]

Falls dieser Restpunkt gelöst wird:
  [L₃] ≠ 0 ∈ HH⁴(F³ A_BC^{an})                    ✓ [M]  (impliziert)
  OP-3 ABGESCHLOSSEN
```

---

## 11. Verbindung zu X.6 (Neue Spurform)

Nach NEU-19 haben wir drei miteinander verbundene Spurformen:

```
ε_β   (β > 1):    KMS-Frobenius-Trace auf A_2D^r                      ✓ [M]
λ_β^{mod} (β > 1): ν_β-twisted Trace auf F³ A_BC^{an}                ✓ [M]
Wres_BC^{top}:     ν₁-twisted Trace, kanonisch, β-unabhängig          ✓ [M]
```

Die Hierarchie:
```
ε_β  →[β→1⁺ Grenzwert]→  Wres_BC^{top}  (kanonischer Grenzoperator)
```

Wres_BC^{top} ist der natürliche Kandidat für X.6:
- Nicht Wodzicki (kein ΨDO)
- Nicht Tsygan (keine zyklische Homotopie)
- Genuiner BC-Typ: Monoid-anisotrope Dirichlet-Residuenspur  ⚠ [M]

---

*Datei: `werkzeuge/neu19_op3_3_wodzicki.md` | Erstellt: 20. Juni 2026 | NEU-19*
*Beweismethode: Dirichlet-Reihen-Asymptotik + Twist-Stabilitätsargument*
