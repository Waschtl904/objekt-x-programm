# NEU-31 — X.3: Wres-GNS-Raum und regularisierte Determinante

> Datum: 28. Juni 2026 | Aufbauend auf NEU-30 (RH-Äquivalenzsatz)
> Status: ✓ [M] Konstruktionsrahmen | ❓ [O] det_Wres = ξ(s)-Identität

---

## Aufgabe

NEU-30 hat zwei offene Voraussetzungen isoliert:

```
(V1) D_X^{BC} aus BC-Strukturdaten (geometrische Realisierung)   ❓ [O]
(V2) Positive Hilbertisierung auf dem Nullstellensektor           ❓ [O]
```

NEU-31 verfolgt einen Ansatz, der beide simultan adressiert:

**Ziel:**

```
det_Wres(s − D_X^{geom}) ~ ξ(s),
```

d.h. die **Wres-Fredholm-Determinante** des geometrischen Operators ist
(proportional zu) der vollständigen ξ-Funktion. Die Nullstellen von ξ
wären dann intrinsisch als Nullstellen der Determinante definiert —
keine tautologische Spektrumswahl.

---

## 1. Wres-GNS-Raum: Konstruktion

### 1.1 GNS-Konstruktion für das Wres-Funktional

Das Wres_BC^{top}-Funktional auf B₃ ist ein lineares Funktional:

```
τ := Wres_BC^{top} : B₃ → ℂ.
```

Die **GNS-Konstruktion** für τ liefert:

- Den **Wres-prä-Hilbertraum** H_τ als Vervollständigung von B₃/N_τ,
  wobei N_τ := { a ∈ B₃ : τ(a*a) = 0 } der Nullraum ist.
- Das **innere Produkt**: ⟨[a],[b]⟩_τ := τ(a*b).
- Den **zyklischen Vektor** Ω_τ := [1] ∈ H_τ.

**Problem:** τ = Wres_BC^{top} ist **nicht positiv** — τ(a*a) kann
negativ sein (indefinite Frobenius-Paarung). Die Standard-GNS setzt
positives Funktional voraus.

### 1.2 Regularisierung: KMS-gemittelte Positivität

**Ansatz:** Ersetze τ durch das regularisierte Funktional:

```
τ_reg(a) := lim_{s→1⁺} (s−1)² · φ_s(a · Δ_s^{-1})
           = Wres_BC^{(2,0)}(a · L₃°),
```

wobei φ_s der KMS_s-Zustand ist (positiv für alle s > 1).

Für festes s > 1 ist φ_s positiv, also ist H_{φ_s} ein echter Hilbertraum.
Im Limes s → 1⁺ degeneriert die Positivität — aber der Nullstellensektor
bleibt nicht-degeneriert, weil K_ξ(s) Doppelpole bei den Nullstellen trägt
(die Polresidue ist positiv-semidefinit für einfache Nullstellen).

**Marker:** ⚠ [M] (Positivität im Limes noch offen)

### 1.3 Nullstellensektor als spektrale Teilraum

Der Nullstellensektor ist der spektrale Teilraum:

```
H_Z := Ran( P_Z ),
```

wobei P_Z der spektrale Projektor von D_{X,rec}^{BC} auf die
Nullstellenmenge Z_ζ ist (aus NEU-30 §1.2).

Auf H_Z ist das Skalarprodukt:

```
⟨e_{ρ,j}, e_{ρ',j'}⟩_{H_Z} := δ_{ρ,ρ'} δ_{j,j'}   (Standard-ℓ²).
```

Die Verbindung zu Wres_BC^{top}: Die Wres-Residue bei den Nullstellen ist
positiv (da K_ξ(s) = Σ_ρ m_ρ/(s−ρ)² mit m_ρ > 0). Das gibt:

```
⟨v, v⟩_{H_Z} ≥ 0   für alle v ∈ H_Z.   ⚠ [M]
```

---

## 2. Regularisierte Wres-Fredholm-Determinante

### 2.1 Definition

Sei D ein Operator auf H_τ (dem Wres-GNS-Raum oder H_Z). Die
**Wres-Fredholm-Determinante** ist:

```
det_Wres(s − D) := exp( Tr_Wres^{top}( log(s − D) · L₃° ) ),
```

wobei log(s − D) via Funktionalkalkül definiert ist (für s ∉ Spec(D)).

Äquivalent über die Resolvente:

```
∂_s log det_Wres(s−D) = Tr_Wres^{top}( (s−D)^{-1} · L₃° ) =: H_X(s).
```

### 2.2 Zusammenhang mit K_ξ und H_ξ

Aus NEU-28/29 haben wir:

```
Tr_Wres^{top}( (s−D_{X,rec}^{BC})^{-2} · L₃° ) = K_ξ(s) = −∂_s H_ξ(s).
```

Also:

```
−∂_s H_X(s) = K_ξ(s) = −∂_s H_ξ(s)
⟹  H_X(s) = H_ξ(s) + C   (C konstant).
```

Für die normierte Wahl C = 0:

```
Tr_Wres^{top}( (s − D_{X,rec}^{BC})^{-1} · L₃° ) = H_ξ(s) = (ξ'/ξ)(s).
```

### 2.3 Fredholm-Determinante und ξ

Integration von H_X = H_ξ:

```
log det_Wres(s − D_{X,rec}^{BC}) = ∫^s H_ξ(u) du = log ξ(s) + const.
```

Also:

```
det_Wres(s − D_{X,rec}^{BC}) = C_det · ξ(s).
```

**Proposition det_Wres ✓ [M] (relativ zu NEU-28/29, formal):**

```
det_Wres(s − D_{X,rec}^{BC}) ~ ξ(s).
```

Die Nullstellen von det_Wres sind genau die Nullstellen von ξ — also
die nichttrivialen Nullstellen von ζ, mit den richtigen Vielfachheiten.

**Marker:** ✓ [M] formal (relativ zu NEU-28/29) | ❓ [O] rigorose Konvergenz

### 2.4 Rigorizitätsproblem: Konvergenz der Determinante

Die Fredholm-Determinante

```
det_Wres(s−D) = exp( Tr_Wres( log(s−D) · L₃° ) )
```

konvergiert nur, wenn Tr_Wres( log(s−D) · L₃° ) absolut konvergiert.

Für die unendlich vielen Nullstellen von ζ wächst Tr an — die
Konvergenz erfordert Regularisierung (Hadamard-Regularisierung,
Zeta-Regularisierung, oder Weierstrassprodukt-Darstellung).

**Hadamard-Produktformel für ξ:**

```
ξ(s) = e^{A+Bs} · Π_ρ (1 − s/ρ) · e^{s/ρ}   (Hadamard, Ordnung 1).
```

Das regularisierte Weierstrassprodukt konvergiert. Die Wres-Determinante
sollte dasselbe Regularisierungsschema verwenden:

```
det_Wres^{reg}(s−D) := e^{A+Bs} · Π_ρ (1 − s/ρ) · e^{s/ρ}   ✓ [M] formal.
```

---

## 3. Geometrische Realisierung: D_X^{geom}

### 3.1 Anforderungen

Ein **geometrischer** Operator D_X^{geom} auf einer natürlichen
Komplettierung H von B₃ muss erfüllen:

```
(G1) D_X^{geom} ist aus (B₃, [ω̃₂], [L₃], Wres_BC^{top}) konstruiert.
(G2) det_Wres(s − D_X^{geom}) = C · ξ(s)   (intrinsisch, nicht per Definition).
(G3) D_X^{geom} ist wesentlich normal auf H.
(G4) ⟨·,·⟩_{Wres} auf H ist positiv-semidefinit.
```

### 3.2 Kandidat: Dirac-artiger Operator auf B₃

**Konstruktionsidee:** Der ω̃₂-Krümmungsoperator Θ (NEU-27 §3.1)
mit Θ(e_r V_n) = r·log(n) · e_{r+n}V_n hat reelles Spektrum.

Um komplexes Spektrum zu erzeugen, kombiniere:

```
D_X^{geom} := M_{½} + i·Θ_norm
```

wobei:
- M_{½} := ½ · id  (der Realanteil, setzt Re = ½)
- Θ_norm eine **normierte, selbstadjungierte** Version von Θ bzgl. Wres ist.

Problem: Das setzt Re(Spec) = ½ per Konstruktion — tautologisch für RH.

### 3.3 Nicht-tautologischer Ansatz: Modularer Operator

Der natürlichste Kandidat aus der BC-Theorie ist der **modulare
Operator** Δ_β bei β → 1:

```
D_X^{geom} := lim_{β→1⁺} (log Δ_β) / (log β)   (auf geeignetem Domäne).
```

Dieser Operator hat im Limes:

```
Spec(log Δ_β / log β) ⊂ log(N×) = { Σ_p k_p log(p) : k_p ∈ ℕ } ⊂ ℝ.
```

Wieder reelles Spektrum — kein direkter Weg zu den komplexen Nullstellen.

**Konklusion:** Kein Kandidat liefert bisher D_X^{geom} mit
(G1)–(G4) gleichzeitig. Das bleibt ❓ [O].

---

## 4. Was det_Wres ~ ξ bedeuten würde

Wenn (G1)–(G4) erfüllt sind:

```
det_Wres(s − D_X^{geom}) = C · ξ(s)   (non-tautologisch)
```

dann folgt:

**(a) Spektrum:** Die Nullstellen von det_Wres sind Spec(D_X^{geom}) = Z_ζ.
    Die Nullstellen wurden nicht per Definition eingesetzt — sie folgen
    aus der ξ-Funktion via Determinante.

**(b) RH-Äquivalenz:** D_X^{geom} − ½·I schief-selbstadjungiert bzgl.
    ⟨·,·⟩_{Wres} ⟺ Spec ⊂ ½ + iℝ ⟺ RH.

**(c) Spurformel:** Automatisch (aus §2.2).

Das wäre der vollständige X.3-Abschluss.

---

## 5. Epistemologische Bilanz NEU-31

| Baustein | Status |
|----------|--------|
| Wres-GNS-Raum Konstruktionsrahmen | ✓ [M] (unter Positivitätsannahme) |
| KMS-Regularisierung τ_reg | ⚠ [M] |
| H_X(s) = H_ξ(s) (einfacher Resolvent) | ✓ [M] formal (relativ NEU-28) |
| det_Wres(s−D) ~ ξ(s) formal | ✓ [M] formal |
| Hadamard-regularisierte det_Wres | ✓ [M] formal |
| Rigorizität: Konvergenz der det_Wres | ❓ [O] |
| Geometrischer Operator D_X^{geom} mit (G1)–(G4) | ❓ [O] |
| Positivität ⟨·,·⟩_{Wres} auf H_Z | ❓ [O] |

---

## 6. Gesamtbild X.3 nach NEU-30+31

```
NEU-30: Äquivalenzsatz D_X^{BC}−½I ⊥-selbstadjungiert ↔ RH   ✓ [M] unter (V1)–(V3)
NEU-31: det_Wres(s−D) ~ ξ(s)  (formal ✓ [M], rigorös ❓ [O])
        Geometrischer Operator D_X^{geom}                       ❓ [O]
```

**Verbleibender Kern-❓ [O]-Punkt:**

```
Konstruiere D_X^{geom} aus (B₃, [ω̃₂], [L₃], Wres_BC^{top})
so dass det_Wres(s − D_X^{geom}) = C · ξ(s)
und ⟨·,·⟩_{Wres} auf dem Nullstellensektor positiv ist.
```

Das ist das eigentliche offene Problem des Programms.

---

*Datei: `werkzeuge/neu31_x3_wres_gns_determinante.md` | 28. Juni 2026*
*Kernresultat: det_Wres ~ ξ(s) formal ✓ [M]; D_X^{geom} mit (G1)–(G4) ❓ [O]*
*Verbleibender Kern-Engpass: geometrischer Operator + Positivität*
