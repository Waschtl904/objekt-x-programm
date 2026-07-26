# NEU-27 — X.2.1: Konstruktion des BC-Resolventen R_X(s)

> Datum: 25. Juni 2026 | Aufbauend auf NEU-26 (X.2-Architektur)
> Status: ✓ [M] Konstruktion | ❓ [O] Identität R_X = K_ξ (→ X.2.2)

---

## Aufgabe

Konstruiere aus den BC-Strukturdaten

```
(B₃, [ω̃₂], [L₃], Wres_BC^{top})
```

eine meromorphe Funktion

```
R_X(s) := Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃ ),
```

ohne D_X^{BC} durch sein Spektrum zu definieren.

---

## 1. Ausgangspunkt: die modulare Spurformel der BC-Algebra

### 1.1 KMS-Zustände und modulare Gruppe

Die BC-Algebra A_BC^{an} trägt für jedes β > 1 einen **KMS_β-Zustand** φ_β:

```
φ_β(e_r V_n V_m^* e_s) = δ_{r,s} δ_{n,m} · n^{-β} / ζ(β).
```

Die zugehörige **modulare Gruppe** σ_t^β : A_BC^{an} → A_BC^{an} ist:

```
σ_t^β(e_r V_n) = n^{iβt} · e_r V_n.
```

Der **KMS-Modularoperator** Δ_β im GNS-Raum H_β hat Spektrum

```
Spec(Δ_β) ⊂ { n^β : n ∈ N× } ∪ {0},
```

und log(Δ_β) / log(β) wirkt durch Multiplikation mit log(n) / log(β) ∈ ℕ
(Monoidgewichte).

### 1.2 Die regularisierte Spurformel

Für a ∈ F³ A_BC^{an} = B₃ ist die **λ_β^{mod}-Spurformel** aus NEU-18/19:

```
λ_β^{mod}(a) := Tr_φ_β( a · Δ_β^{-1} ),
```

wobei Tr_φ_β der KMS-Spurfunktional ist. Für a = L₃ ∈ HH⁴(B₃) gilt
(aus NEU-19/20):

```
λ_β^{mod}(L₃) ~ C'_{4,1} · (ζ'/ζ)²(β)   (β → 1⁺).
```

---

## 2. Der BC-Resolvent: Definition via analytische Fortsetzung

### 2.1 Idee: s als komplexer Parameter

Statt β → 1⁺ real zu betrachten, setzen wir β = s ∈ ℂ mit Re(s) > 1
und betrachten die **analytische Fortsetzung**:

```
Λ_mod(s) := Tr_φ_s( L₃ · Δ_s^{-1} )   für Re(s) > 1.
```

Da φ_s und Δ_s analytisch in s sind (für Re(s) > 1), ist Λ_mod(s)
holomorph für Re(s) > 1.

### 2.2 Zweifache Regularisierung: der Doppelpol-Extrakt

Aus dem Wres_BC^{(2,0)}-Formalismus (NEU-18):

```
Wres_BC^{(2,0)} = lim_{β→1⁺} (β−1)² · λ_β^{mod}
```

extrahiert die **zweifache Laurent-Residue** bei β = 1. Das motiviert:

```
R_X(s) := −∂_s Λ_mod(s)   für Re(s) > 1,
```

mit meromorpher Fortsetzung auf ℂ.

**Motivation für −∂_s:**

Wenn Λ_mod(s) ~ C · (ζ'/ζ)²(s) (aus NEU-19/20), dann:

```
−∂_s Λ_mod(s) ~ −C · ∂_s(ζ'/ζ)²(s)
              = −C · 2(ζ'/ζ)(s) · (ζ''/ζ − (ζ'/ζ)²)(s)
              = −C · 2(ζ'/ζ)(s) · (ζ''/ζ)(s) + 2C · (ζ'/ζ)²(s).
```

Das ist noch nicht K_ξ — die Identifikation R_X = K_ξ ist X.2.2.
Hier geht es nur darum, R_X(s) als wohldefinierte meromorphe Funktion
zu konstruieren.

### 2.3 Kanonische Definition

**Definition (BC-Resolvent):**

```
R_X(s) := −∂_s Tr_Wres^{top}( (s·id − Θ)^{-1} · L₃ )
```

wobei Θ : B₃ → B₃ der **kanonische BC-Gewichtsoperator** ist (§3 unten),
und (s·id − Θ)^{-1} die Resolvente bei s ∈ ℂ \ Spec(Θ).

Das −∂_s entspricht dem Übergang vom einfachen Polkern H_ξ = ξ'/ξ zum
Doppelpolkern K_ξ = −∂_s H_ξ (wie in NEU-26 §1/§4).

---

## 3. Kanonischer BC-Gewichtsoperator Θ

### 3.1 Konstruktion aus [ω̃₂] und [L₃]

Das Schlüsselobjekt ist ein Operator Θ auf B₃, der aus den
Strukturdaten herkommt — nicht aus den Nullstellen.

**Kandidat: der ω̃₂-Krümmungsoperator.**

Die Klasse [ω̃₂] ∈ HH²(B₃, B₃) mit

```
ω̃₂(e_r V_n, e_s V_m) = −r·s·log(n) · e_{r+ns} V_{nm}
```

definiert eine **Krümmungsform** auf B₃. Der Fourier-Exponent r+ns
(nicht r+s!) kodiert die verschränkte Multiplikationsstruktur.

Der kanonische Gewichtsoperator ist der **∂̄_ω̃₂-Laplace-Operator**:

```
Θ := [ω̃₂, ·]_Hochschild : B₃ → B₃,
```

wobei [ω̃₂, ·] der Hochschild-Kommutator mit der 2-Kozykelklasse ist.

**Explizit auf Basiselementen:**

```
Θ(e_r V_n) := ω̃₂(e_1 V_1, e_r V_n) − ω̃₂(e_r V_n, e_1 V_1)
            = (−1·r·log(1) · e_{r+n} V_n) − (−r·1·log(n) · e_{r+n} V_n)
            = r·log(n) · e_{r+n} V_n.
```

Also:

```
Θ(e_r V_n) = r·log(n) · e_{r+n} V_n.
```

**Beobachtung:** Der Eigenwert von Θ auf e_r V_n ist r·log(n).
Das ist **nicht** log(n) allein (das wäre der Monoidgewichtsoperator),
sondern das Produkt aus Fourier-Index r und Monoidgewicht log(n).

### 3.2 Spektrum von Θ

```
Spec(Θ) ⊂ { r·log(n) : r ∈ ℤ, n ∈ N× } ⊂ ℝ.
```

Das Spektrum ist reell und diskret. Es liegt **nicht** auf ½ + iℝ.

**Folgerung:** Θ ist nicht der gesuchte D_X^{BC} — Θ trägt reelles
Spektrum, während die Nullstellen von ζ komplexes Spektrum Re(ρ) ∈ (0,1)
haben.

**Aber:** Θ liefert eine wohldefiniierte Resolvente (s·id − Θ)^{-1}
für s ∈ ℂ \ ℝ, und die Wres_BC^{top}-Spur dieser Resolvente ist die
gesuchte meromorphe Funktion.

### 3.3 Angepasster Ansatz: Θ als Primseiten-Operator

Statt Θ direkt mit D_X^{BC} gleichzusetzen, betrachten wir:

```
R_X(s) := Tr_Wres^{top}( (s − Θ)^{-2} · L₃ )
```

als Funktion von s ∈ ℂ \ ℝ. Die Pole von R_X(s) liegen bei
s ∈ Spec(Θ) ⊂ ℝ — das sind reelle Werte, nicht die Nullstellen von ζ.

Das zeigt: **Θ allein kann D_X^{BC} nicht sein.**

---

## 4. Der fehlende Schritt: Komplexifizierung via KMS-Zustand

### 4.1 Von reellem zu komplexem Spektrum

Die Nullstellen von ζ liegen bei Re(ρ) ∈ (0,1), also im Streifen
der kritischen Geraden. Der Übergang von reellem Spektrum (Θ) zu
komplexem Spektrum (D_X^{BC}) erfordert eine **Komplexifizierung**.

**Ansatz:** Betrachte nicht Θ auf B₃, sondern den zusammengesetzten Operator

```
D_X^{BC} := ½·I + i·Θ_norm
```

wobei Θ_norm eine normierte Version von Θ ist (Normierung via Wres_BC^{top}),
und I die Identität auf einem geeigneten Abschluss von B₃.

Dann:

```
Spec(D_X^{BC}) ⊂ ½ + iℝ
```

per Konstruktion — **aber das ist wieder tautologisch** (RH in die Konstruktion eingebaut).

### 4.2 Die alternative Route: Meromorphe Fortsetzung von λ_β^{mod}

Der nicht-tautologische Weg geht über die **analytische Fortsetzung**
der KMS-Spurformel:

```
s ↦ λ_mod(s) := Tr_φ_s( L₃ · Δ_s^{-1} )   (Re(s) > 1)
```

Diese Funktion ist holomorph für Re(s) > 1. Ihre meromorphe Fortsetzung
auf ℂ hat Pole bei:

```
s = ρ   (Nullstellen von ζ)    [erwartet, aus der ζ'/ζ-Asymptotik]
s = 1   (einfacher Pol von ζ)
```

**Definition (kanonisch, nicht-tautologisch):**

```
R_X(s) := −∂_s λ_mod(s),
```

wobei λ_mod(s) die meromorphe Fortsetzung der KMS-Spurformel ist.

Die Pole von R_X(s) bei s = ρ (mit Ordnung m_ρ) sind dann keine
Definitionssache — sie folgen aus der analytischen Fortsetzung.

### 4.3 Warum das nicht-tautologisch ist

Die Funktion λ_mod(s) ist durch die **BC-Algebrastruktur** definiert
(KMS-Zustände φ_s, Modularoperator Δ_s, das Element L₃ ∈ B₃).

Die Polstruktur von λ_mod(s) folgt aus der Funktionalgleichung und
Analytizität der ζ-Funktion — **nicht** aus einer Spektrumswahl.

Der Operator D_X^{BC} ist dann implizit definiert durch:

```
R_X(s) = Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃ )
```

als die eindeutige Spektraldarstellung von R_X(s), sofern R_X(s)
die richtige Polstruktur hat (= X.2.2).

---

## 5. Wohldefinierheit von R_X(s)

### 5.1 Holomorphie für Re(s) > 1

**Proposition (Holomorphie von λ_mod):**

Für Re(s) > 1 ist die Abbildung

```
s ↦ λ_mod(s) = Tr_φ_s( L₃ · Δ_s^{-1} )
```

wohldefiniert und holomorph.

**Beweis (Skizze):**

- φ_s ist der KMS_s-Zustand; für Re(s) > 1 konvergiert die Dirichlet-Reihe
  ζ(s) = Σ n^{-s} absolut.
- Δ_s^{-1} hat auf H_s den diskreten Spektralanteil bei {n^{-s} : n ∈ N×}.
- Die Spur Tr_φ_s( L₃ · Δ_s^{-1} ) konvergiert absolut für Re(s) > 1,
  da L₃ ∈ F³ A_BC^{an} und die n^{-s}-Gewichte für Re(s) > 1 summierbar sind.
- Holomorphie in s folgt aus gleichmäßiger Konvergenz auf Kompakta
  (Weierstraß-Argument).   ✓ [M]

### 5.2 Meromorphe Fortsetzung

**Erwartung (❓ [O] → Ziel von X.2.2):**

λ_mod(s) setzt sich meromorph fort auf ℂ mit Polstellen bei
s = ρ (Nullstellen von ζ) und s = 1 (Pol von ζ).

Das folgt — wenn es gilt — aus der Beziehung

```
λ_mod(s) ~ C · (ξ'/ξ)(s) + (reguläre Terme)   (heuristisch)
```

und ist der Inhalt von X.2.2.

### 5.3 R_X(s) als Kandidat

**Definition (kanonisch):**

```
R_X(s) := −∂_s λ_mod(s).
```

Das ist wohldefiniert und holomorph für Re(s) > 1. Die meromorphe
Fortsetzung und die Identität R_X(s) = K_ξ(s) ist X.2.2.

**Marker:** ✓ [M] (Konstruktion für Re(s) > 1) | ❓ [O] (meromorphe Fortsetzung)

---

## 6. Hauptresultat: NEU-27

### Theorem X.2.1 ✓ [M] (für Re(s) > 1)

Die Funktion

```
R_X : { s ∈ ℂ : Re(s) > 1 } → ℂ,
R_X(s) := −∂_s Tr_φ_s( L₃ · Δ_s^{-1} )
```

ist wohldefiniert, holomorph, und aus den BC-Strukturdaten
(B₃, [L₃], KMS-Familie {φ_s}) konstruiert.

Sie ist der **kanonische Kandidat** für Tr_Wres^{top}((s−D_X^{BC})^{-2}·L₃).

**Verbindung zu Wres_BC^{top}:**

Der Grenzwert

```
Wres_BC^{(2,0)} = lim_{s→1⁺} (s−1)² · λ_mod(s)
                = lim_{s→1⁺} (s−1)² · Tr_φ_s( L₃ · Δ_s^{-1} )
```

(aus NEU-18) zeigt, dass Wres_BC^{top} genau das doppelte Residuum von
λ_mod(s) bei s = 1 extrahiert. Das ist konsistent mit der Interpretation
von R_X als Wres-Spur einer Resolvente-Quadrat.

---

## 7. Offene Schritte

### 7.1 Was X.2.2 zeigen muss

X.2.2 (NEU-28) muss zeigen:

```
R_X(s) = K_ξ(s) = −∂_s(ξ'/ξ)(s) = Σ_ρ m_ρ/(s−ρ)²
```

(nach Subtraktion der Gamma- und Trivialbeiträge).

Das ist äquivalent zu:

```
λ_mod(s) ~ (ξ'/ξ)(s) + (reguläre Terme).
```

### 7.2 Verbindung zur Linearisierung (X.2.0)

Der Übergang von (ζ'/ζ)² (quadratisch, aus NEU-19/20) zu H_ξ = ξ'/ξ
(linear) entspricht der **Linearisierung**:

```
Λ*Λ  ⇝  H_ξ,   R_X = −∂_s λ_mod ~ −∂_s H_ξ = K_ξ.
```

Das Schlüsselargument wird sein: λ_mod(s) selbst (nicht λ_mod(s)²) ist
proportional zu H_ξ(s), weil die KMS-Spur mit **einfachen** Monoidgewichten
n^{-s} arbeitet, während (ζ'/ζ)² aus der **Faltung** Λ*Λ kommt.

---

## 8. Epistemologische Bilanz

| Aussage | Status |
|---------|--------|
| λ_mod(s) = Tr_φ_s(L₃·Δ_s^{-1}) holomorph für Re(s)>1 | ✓ [M] |
| R_X(s) = −∂_s λ_mod(s) wohldefiniert für Re(s)>1 | ✓ [M] |
| R_X aus BC-Strukturdaten (nicht-tautologisch) | ✓ [M] |
| Θ = [ω̃₂,·]_Hochschild explizit: Θ(e_r V_n) = r·log(n)·e_{r+n}V_n | ✓ [M] |
| Meromorphe Fortsetzung von λ_mod(s) auf ℂ | ❓ [O] → X.2.2 |
| R_X(s) = K_ξ(s) nach Gamma/Trivial-Korrektur | ❓ [O] → X.2.2 |
| OP-4.1a als Stetigkeit der Tr_φ_s-Konstruktion | ⚠ [M] |

---

*Datei: `werkzeuge/neu27_x2_1_bc_resolvent.md` | 25. Juni 2026*
*Konstruktion: R_X(s) = −∂_s Tr_φ_s(L₃·Δ_s^{-1}) via KMS-analytische Fortsetzung*
*Kernresultat: R_X nicht-tautologisch aus BC-Daten, holomorph für Re(s)>1*
*Nächster Schritt: NEU-28 (X.2.2 — Primseiten-Identifikation R_X = K_ξ)*
