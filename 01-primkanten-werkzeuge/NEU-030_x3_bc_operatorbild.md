# NEU-30 — X.3: BC-Operatorbild und RH-Äquivalenz

> Datum: 28. Juni 2026 | Aufbauend auf NEU-29 (Cauchy-Spurformel)
> Status: ✓ [M] abstrakter Äquivalenzsatz | ❓ [O] geometrische Realisierung

---

## Aufgabe

X.3 isoliert den logischen Äquivalenzsatz:

```
D_X^{BC} − ½·I  schief-selbstadjungiert bzgl. Wres_BC^{top}
                                              ⟺  RH.
```

Wichtig: Dieser Satz gilt **nicht automatisch** aus der Spurformel allein —
er erfordert drei explizite Voraussetzungen, die in NEU-30 präzisiert werden.

---

## 1. Rekonstruktion des zyklischen Spektralmaßes aus K_ξ

### 1.1 Spektralmaß aus der Resolventenfunktion

NEU-28/29 liefern:

```
Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃° ) = K_ξ(s) = Σ_ρ m_ρ/(s−ρ)².
```

Die Funktion K_ξ(s) bestimmt eindeutig ein **zyklisches Spektralmaß**:

```
μ_ξ := Σ_ρ m_ρ · δ_ρ   (diskrete Maß auf ℂ, Träger = Nullstellen von ζ)
```

durch die Inversion:

```
K_ξ(s) = ∫ 1/(s−ρ)² dμ_ξ(ρ).
```

Das Spektralmaß μ_ξ ist eindeutig durch K_ξ bestimmt (Stieltjes-Inversion
auf der kritischen Geraden, Carleson-Theorem für diskrete Maße). ✓ [M]

### 1.2 Rekonstruierter Operator D_{X,rec}^{BC}

Aus μ_ξ konstruieren wir den **rekonstruierten Spektraloperator**:

Sei H_μ := L²(ℂ, μ_ξ) = ℓ²(Z) mit Z = {(ρ,j) : 1 ≤ j ≤ m_ρ}.

```
D_{X,rec}^{BC} : H_μ → H_μ,   D_{X,rec}^{BC}(e_{ρ,j}) := ρ · e_{ρ,j}.
```

Das ist der minimale normale Operator mit Spektralmaß μ_ξ.

**Für die Spurformel gilt dann:**

```
Tr_Wres^{top}( f(D_{X,rec}^{BC}) · L₃° )
= ∫ f(ρ) dμ_ξ(ρ) = Σ_ρ m_ρ · f(ρ).
```

**Marker:** ✓ [M] relativ zu NEU-28/29

---

## 2. Abstrakter RH-Äquivalenzsatz

### 2.1 Formulierung

**Theorem X.3.abstract ✓ [M]:**

Sei D ein normaler Operator auf einem Hilbertraum H mit

```
Spec(D) = { ρ : ζ(ρ) = 0, nichttrivial }.
```

Dann gilt:

```
D − ½·I  ist schief-selbstadjungiert
⟺  D − ½·I  ist rein imaginär (d.h. i-selbstadjungiert)
⟺  Spec(D) ⊂ ½ + iℝ
⟺  RH.
```

**Beweis:**

Da D normal: D − ½·I ist schief-selbstadjungiert (d.h. (D−½I)* = −(D−½I))
genau dann, wenn für alle Eigenwerte λ ∈ Spec(D):

```
(λ − ½)* = −(λ − ½)
⟺  λ̄ − ½ = −λ + ½
⟺  λ + λ̄ = 1
⟺  Re(λ) = ½.
```

Also: D − ½·I schief-selbstadjungiert ⟺ Spec(D) ⊂ ½ + iℝ ⟺ RH.   □

### 2.2 Warum das nicht trivial ist

Der Satz ist logisch korrekt, aber **tautologisch** ohne die Verbindung zu
den BC-Strukturdaten: Wir haben bisher nur einen formal rekonstruierten
Operator D_{X,rec}^{BC} auf H_μ, der per Konstruktion Spec = Z_ζ hat.

Die nicht-tautologische Version braucht:

```
(V1) D_X^{BC} aus (B₃, [ω̃₂], [L₃], Wres_BC^{top}) konstruiert
     (nicht aus den Nullstellen direkt).

(V2) Die Wres_BC^{top}-Paarung hat auf dem Nullstellensektor
     eine positive Hilbertisierung.

(V3) Mehrfachnullstellen werden semisimpel realisiert
     (Eigenräume, nicht Jordanblöcke).
```

---

## 3. Die drei Voraussetzungen expliziert

### 3.1 (V1) — BC-intrinsische Konstruktion ❓ [O]

D_X^{BC} muss aus den Strukturdaten kommen — nicht aus den Nullstellen.

Das ist der Kern-❓ [O]-Punkt des gesamten Programms.

**Bisheriger Stand:** D_{X,rec}^{BC} ist über das Spektralmaß μ_ξ rekonstruiert
(§1.2) — aber μ_ξ wurde aus K_ξ gewonnen, und K_ξ kam aus NEU-28
über λ_mod(s) = C_L/ζ(s). Das ist keine tautologische Zirkeldefinition,
weil λ_mod(s) unabhängig von den Nullstellen definiert ist — aber der
Schritt von λ_mod zur Spektralidentifikation erfordert die meromorphe
Fortsetzung, die in NEU-28 als ✓ [M] gesetzt wurde.

Der eigentlich fehlende Schritt ist eine **geometrische Realisierung** von
D_X^{BC} auf einer natürlichen Komplettierung von B₃ — nicht auf dem
abstrakten H_μ.

### 3.2 (V2) — Positive Hilbertisierung ❓ [O] → ⚠ [M]

**Das subtile Problem:**

Die Frobenius-Paarung

```
B([Ψ],[c]) = Wres_BC^{top}(R₃(Ψ(c)))
```

ist **nicht positiv-definit** — sie ist eine indefinite Bilinearform
(modulare Frobenius-Struktur, ν₁-twisted, NEU-19).

Für „schief-selbstadjungiert bzgl. B impliziert Spektrum rein imaginär"
braucht man jedoch eine **Hilbert-Raumstruktur**, d.h. ein positiv-definites
inneres Produkt.

**Lösung: Nullstellensektör-Hilbertisierung.**

Auf dem Nullstellensektor H_μ = ℓ²(Z) ist das Standard-ℓ²-Skalarprodukt
positiv-definit. Die Verbindung zwischen Wres_BC^{top} auf B₃ und dem
ℓ²-Skalarprodukt auf H_μ muss explizit hergestellt werden.

**Ansatz (Positivitätsannahme):**

Definiere auf dem Nullstellensektor:

```
⟨e_{ρ,j}, e_{ρ',j'}⟩_{Wres} := Wres_BC^{top}( e_{ρ,j}^* · e_{ρ',j'} · L₃° )
```

als das Wres-induzierte Skalarprodukt. Die Positivität

```
⟨v, v⟩_{Wres} ≥ 0   für alle v ∈ H_μ
```

ist eine **zusätzliche Voraussetzung** — sie ist nicht aus der Frobenius-
Nicht-Ausgeartheit allein garantiert.

**Marker:** ❓ [O] (Positivität) | ⚠ [M] (indefinite Paarung bekannt)

### 3.3 (V3) — Semisimple Realisierung mehrfacher Nullstellen ⚠ [M]

Wenn m_ρ ≥ 2, könnte D_X^{BC} an ρ einen Jordan-Block der Größe m_ρ
haben — das wäre nicht normal. In diesem Fall ist „schief-selbstadjungiert"
nicht äquivalent zu „Spektrum auf ½+iℝ".

**Für das Programm:** Unter RH sind alle m_ρ = 1 (erwartet). Ohne RH
als Voraussetzung muss man für die Äquivalenz semisimple Realisierung
annehmen.

**Marker:** ⚠ [M]

---

## 4. Reformulierter Äquivalenzsatz (ehrlich)

### Theorem X.3 ✓ [M] (unter expliziten Voraussetzungen)

**Voraussetzungen:**

(V1) D_X^{BC} realisiert den Nullstellensektor: Spec(D_X^{BC}) = Z_ζ.

(V2) Die Wres-Paarung auf H_μ ist positiv-semidefinit und macht H_μ
     zu einem prä-Hilbertraum, auf dem D_X^{BC} wesentlich normal ist.

(V3) D_X^{BC} ist semisimpel: keine Jordan-Blöcke.

**Behauptung:**

```
D_X^{BC} − ½·I  schief-selbstadjungiert bzgl. ⟨·,·⟩_{Wres}
⟺  Spec(D_X^{BC}) ⊂ ½ + iℝ
⟺  RH.
```

**Beweis:** §2.1 (normaler Operator, Eigenwertkriterium).   □

---

## 5. Epistemologische Bilanz NEU-30

| Baustein | Status |
|----------|--------|
| Rekonstruktion μ_ξ aus K_ξ (Stieltjes-Inversion) | ✓ [M] |
| Rekonstruierter Operator D_{X,rec}^{BC} auf H_μ | ✓ [M] relativ NEU-28/29 |
| Abstrakter RH-Äquivalenzsatz (normal + Eigenwert) | ✓ [M] |
| Notwendigkeit positiver Hilbertisierung explizit | ✓ [M] |
| Indefinitheit von Wres_BC^{top} als Problem erkannt | ✓ [M] |
| Geometrische Realisierung auf Komplettierung von B₃ | ❓ [O] |
| Positivität ⟨·,·⟩_{Wres} auf H_μ | ❓ [O] |
| Mehrfachnullstellen semisimpel (m_ρ ≥ 2) | ⚠ [M] |

---

## 6. Nächster Schritt: NEU-31

Der natürliche nächste Schritt ist die Konstruktion des Nullstellensektors
als **Wres-GNS-Raum** oder über eine **regularisierte Determinante**:

```
det_Wres(s − D_X^{geom}) ~ ξ(s).
```

Das würde (V1) und (V2) simultan liefern: D_X^{geom} wäre der geometrische
Operator, dessen Wres-Fredholm-Determinante gerade ξ(s) ist — dann sind
die Nullstellen intrinsisch definiert, nicht eingesetzt.

---

*Datei: `werkzeuge/neu30_x3_bc_operatorbild.md` | 28. Juni 2026*
*Kernresultat: Äquivalenzsatz ✓ [M] unter (V1)–(V3); Positivität und geom. Realisierung ❓ [O]*
*Nächster Schritt: NEU-31 (Wres-GNS-Raum oder det_Wres ~ ξ(s))*
