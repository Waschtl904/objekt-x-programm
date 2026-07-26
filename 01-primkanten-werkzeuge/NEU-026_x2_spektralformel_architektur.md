# NEU-26 — X.2 Spektralformel: korrekter Kern, Minimalrealisierung, BC-Engpass

> Datum: 20. Juni 2026 | Aufbauend auf OP-4.1 (vollständig, NEU-21–25)
> Status: ✓ [M] formale Realisierung | ❓ [O] BC-intrinsische Konstruktion

**Kontext:** Objekt X — Vierschicht-Profil
(A_2D^r,  [ω̃₂],  [L₃],  Wres_BC^{top})

**Ziel von X.2:** Konstruktion einer Spektralformel

```
Tr_Wres( f(D_X) · L₃ ) = Σ_ρ f(ρ),   ζ(ρ)=0, 0<Re(ρ)<1.
```

**Status von NEU-26:** Reduktions- und Korrekturblatt.
NEU-26 konstruiert eine mathematisch saubere minimale Spektralrealisierung
und isoliert den echten nicht-tautologischen BC-Engpass.

---

## 1. Zentrale Korrektur: (ζ'/ζ)² ist nicht direkt die Nullstellen-Spur

Setze für die abgeschlossene ξ-Funktion:

```
ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s).
```

Die Nullstellen von ξ sind genau die nichttrivialen Nullstellen von ζ,
mit Vielfachheiten m_ρ.

Der logarithmische Ableitungs-Kern:

```
H_ξ(s) := (ξ'/ξ)(s).
```

Hadamard liefert lokal und meromorph:

```
H_ξ(s) = B + Σ_ρ m_ρ · ( 1/(s−ρ) + 1/ρ ),
```

und daher:

```
K_ξ(s) := −∂_s H_ξ(s) = Σ_ρ m_ρ / (s−ρ)².
```

Dagegen gilt für das Quadrat:

```
H_ξ(s)² = Σ_ρ m_ρ² / (s−ρ)² + (einfache Pole und reguläre Terme).
```

**Folgerung:**

(ζ'/ζ)² trägt an den Nullstellen den Doppelpol-Träger, aber im Allgemeinen
die Gewichte m_ρ², nicht m_ρ. Für eine Spurformel mit Vielfachheit m_ρ ist
der korrekte lineare Kern:

```
K_ξ(s) = −∂_s(ξ'/ξ)(s),
```

oder äquivalent der einfache Polkern ξ'/ξ.

**Marker:** ✓ [M]

---

## 2. Zweite Korrektur: Doppelpol-Kerne liefern f'(ρ), nicht f(ρ)

Für einen Testfunktional-Ansatz mit K_ξ(s) = Σ_ρ m_ρ/(s−ρ)² gilt nach Cauchy:

```
1/(2πi) · ∫_Γ f(s) K_ξ(s) ds = Σ_ρ m_ρ · f'(ρ).
```

Um Σ_ρ m_ρ · f(ρ) zu erhalten, muss man entweder den einfachen Polkern H_ξ
verwenden:

```
1/(2πi) · ∫_Γ f(s) H_ξ(s) ds = Σ_ρ m_ρ · f(ρ),
```

oder beim Doppelpol-Kern eine primitive Testfunktion F mit F' = f:

```
1/(2πi) · ∫_Γ F(s) K_ξ(s) ds = Σ_ρ m_ρ · f(ρ).
```

**Marker:** ✓ [M]

---

## 3. Minimaler Spektraloperator D_Z

Sei Z := { (ρ,j) : ξ(ρ)=0, 1 ≤ j ≤ m_ρ } der Nullstellen-Multimengenraum.

Definiere:

```
H_Z := ℓ²(Z),   e_{ρ,j} Standardbasis.
```

Der minimale Nullstellenoperator:

```
D_Z(e_{ρ,j}) := ρ · e_{ρ,j},
Dom(D_Z) := { a=(a_{ρ,j}) : Σ_{ρ,j} |ρ|² |a_{ρ,j}|² < ∞ }.
```

D_Z ist ein abgeschlossener normaler Operator und:

```
Spec(D_Z) = { ρ : ξ(ρ) = 0 }.
```

Für jede Testfunktion f mit Σ_ρ m_ρ |f(ρ)| < ∞:

```
f(D_Z) ∈ L¹(H_Z),   Tr(f(D_Z)) = Σ_ρ m_ρ · f(ρ).
```

**Marker:** ✓ [M] als formale Spektralrealisierung.
**Warnung:** Tautologisch — D_Z wird aus den Nullstellen definiert.

---

## 4. Resolventenform der Spektralformel

Für s ∉ Spec(D_Z):

```
Tr( (s − D_Z)^{-2} ) = Σ_ρ m_ρ / (s−ρ)² = K_ξ(s).
```

Für geeignete f und primitive F mit F' = f:

```
Tr(f(D_Z)) = 1/(2πi) · ∫_Γ F(s) · Tr((s−D_Z)^{-2}) ds.
```

Das ist die saubere Resolventenform der Spurformel, wenn der
Wodzicki-Residuumsträger den Resolventen-Doppelpolkern realisiert.

**Marker:** ✓ [M]

---

## 5. Einbettung in Objekt X

Aus OP-4.1 (NEU-21–25) besitzt B₃ = F³ A_BC^{an} eine modulare
Frobenius-Wodzicki-Struktur mit beiderseitig nicht-ausgearteter Paarung:

```
B([Ψ],[c]) := Wres_BC^{top}(R₃(Ψ(c))).
```

Die minimale Spektralerweiterung von Objekt X:

```
X_min := B₃ ⊕̂ H_Z^∞
```

wobei H_Z^∞ ⊂ H_Z der Fréchet-Raum schnell fallender Nullstellenkoeffizienten ist.

Auf dem Nullstellensektor: D_X|_{H_Z^∞} = D_Z.

Der formale L₃-Einsatz im Minimalmodell:

```
L₃^{min} := Π_Z   (Projektor auf den Nullstellensektor).
```

Dann:

```
Tr_Wres,min( f(D_X) · L₃^{min} ) = Σ_ρ m_ρ · f(ρ).
```

**Marker:** ✓ [M] als Minimalmodell | ❓ [O] als BC-intrinsische Konstruktion.

---

## 6. Der eigentliche X.2-Engpass

Die nicht-tautologische Version von X.2 ist nicht die Existenz irgendeines
Operators mit Nullstellenspektrum — die ist formal leicht.

**X.2-Kernbehauptung ❓ [O]:**

> Es existiert ein aus (B₃, [ω̃₂], [L₃], Wres_BC^{top}) intrinsisch konstruierter
> Operator D_X^{BC}, so dass
>
> ```
> Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃ ) = −∂_s(ξ'/ξ)(s)
> ```
>
> nach Entfernung der trivialen/polaren Korrekturterme gilt.

Aus dieser Resolventenidentität folgt dann durch Cauchy sofort:

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃ ) = Σ_ρ m_ρ · f(ρ).
```

---

## 7. Verhältnis zu Λ*Λ

Der in OP-4.1 erreichte Zusammenhang:

```
Wres_BC^{(2,0)} = lim_{β→1⁺} (β−1)² · λ_β^{mod}
```

und die Heuristik:

```
Λ*Λ  ↔  (ζ'/ζ)²
```

ist für die Trägererkennung der Nullstellen plausibel, aber für die
Spurformel noch nicht ausreichend.

Benötigt wird eine **linearisierende Brücke**:

```
Λ*Λ  ⇝  −∂_s(ξ'/ξ),
```

oder eine Polarisations-/Quadratwurzelstruktur, die den Übergang von
quadratischen Gewichten m_ρ² zu linearen Gewichten m_ρ erklärt.

Dieser Punkt ist der neue präzise OP-4.2/X.2-Engpass.

**Marker:** ❓ [O]

---

## 8. RH-Formulierung im Operatorbild

Im Minimalmodell gilt:

```
RH  ⟺  Spec(D_Z) ⊂ ½ + iℝ
     ⟺  D_Z = ½·I + iH_Z   mit selbstadjungiertem H_Z.
```

Für Objekt X wäre die nicht-tautologische RH-Zielform:

> Konstruiere D_X^{BC} intrinsisch aus der modularen Frobenius-Wodzicki-Struktur,
> und zeige:
>
> ```
> D_X^{BC} − ½·I
> ```
>
> ist schief-selbstadjungiert bezüglich der durch Wres_BC^{top} erzeugten
> modularen Paarung.

**Marker:** ❓ [O]

---

## 9. Statusmatrix

| Aussage | Status |
|---------|--------|
| (ζ'/ζ)² hat Doppelpolgewichte m_ρ², nicht m_ρ | ✓ [M] |
| Linearer Kern: K_ξ = −∂_s(ξ'/ξ) oder ξ'/ξ | ✓ [M] |
| Doppelpolkern benötigt primitive Testfunktion F'=f | ✓ [M] |
| Minimaler D_Z realisiert Nullstellenspur formal | ✓ [M] |
| Minimalmodell X_min = B₃ ⊕̂ H_Z^∞ | ✓ [M] formal |
| BC-intrinsische Konstruktion von D_X^{BC} | ❓ [O] |
| Tr_Wres^{top}((s−D_X^{BC})^{-2}·L₃) = K_ξ(s) | ❓ [O] |
| Linearisierung Λ*Λ ⇝ −∂_s(ξ'/ξ) | ❓ [O] |
| OP-4.1a Stetigkeit als Fréchet-Spurvoraussetzung | ⚠ [M] |

---

## 10. Neuer Arbeitsauftrag nach NEU-26

**X.2.0 — Kernelkorrektur abschließen** ❓ [O]

Ersetze in der Spektralformel-Brücke (ζ'/ζ)² durch den präzisen linearen
Nullstellenkern K_ξ(s) = −∂_s(ξ'/ξ)(s), oder erkläre explizit, dass der
quadratische Kernel nur Trägerinformation beziehungsweise
einfachheits-abhängige Information liefert.

**X.2.1 — BC-Resolvent konstruieren** ❓ [O]

Konstruiere aus [L₃] und Wres_BC^{top} eine meromorphe Funktion:

```
R_X(s) := Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃ ).
```

**X.2.2 — Primseite identifizieren** ❓ [O]

Zeige:

```
R_X(s) = K_ξ(s)
```

nach Abzug der Gamma-, Pol- und Trivialnullstellenanteile.

**X.2.3 — Cauchy-Spurformel** ❓ [O]

Folgere für geeignete Testfunktionen:

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃ ) = Σ_ρ m_ρ · f(ρ).
```

---

*Datei: `werkzeuge/neu26_x2_spektralformel_architektur.md` | 20. Juni 2026*
*Methode: Architekturanalyse, Tautologie-Diagnose, Kernbehauptungs-Isolation*
*Kernbotschaft: Engpass ist D_X^{BC}-Konstruktion + Linearisierung Λ*Λ ⇝ K_ξ*
*Nächste NEU-Nummer: NEU-27 (X.2.1 — BC-Resolvent)*
