# NEU-63 — Arithmetische Identifikation der Weyl-/Stieltjes-Funktion

**Status:** 63.B gesichert ✓[M] (aus NEU-59–62); 63.A, 63.C offen ❓[O]; 63.D Herglotz⇔RH ⚠[M]  
**Datum:** 2026-06-29 (korrigiert: regulierte Herglotz, Matrix-Weyl, i-Faktor)  
**Aufbaut auf:** NEU-62 (analytische Kette geschlossen), NEU-59 (Spektralmaß-Reduktion)

---

## Programmlogik

Nach NEU-58–62 steht die analytische Infrastruktur vollständig:

```
A_N^{Jac,-}  --s.r.-->  D_rel    (starke Resolventenkonvergenz, γ_N ≡ 1)
     ↓
μ_{N,ξ}  ⇒  μ_ξ            (schwache Spektralmaßkonvergenz)
     ↓
supp(μ_ξ) ⊂ Spec(D_rel) ⊂ ℝ
```

Der gesamte Druck liegt auf:

> **Welche arithmetische Funktion ist die Weyl-Funktion von D_rel?**

Angriff nicht über Spec(D_rel) direkt, sondern über die Herglotz-Funktion:

```
m_ξ(z) = ⟨ξ, (D_rel - z)^{-1} ξ⟩ = ∫_ℝ dμ_ξ(t) / (t-z)    (z ∈ ℂ\ℝ)
```

---

## Korrektur 1: Herglotz-Äquivalenz nur nach Regularisierung ⚠[M]

Die konzeptuelle Äquivalenz

```
m_arith Herglotz  ⟺  γ_ρ ∈ ℝ  ⟺  RH
```

gilt **nur nach sauberer Regularisierung**. Die rohe Partialbruchsumme
Σ_ρ 1/(γ_ρ - z) divergiert; nötige Korrekturterme:

- Gamma-Faktor und triviale Nullstellen von ζ
- Pol bei s = 1 (Subtraktion 1/(s-1))
- Symmetrisierung ρ ↔ 1-ρ (aus Funktionalgleichung)
- Konvergenzerzeugende Subtraktion (Hadamard-Regularisierung)

**Korrekter Status:** ⚠[M]

```
m_arith := regulierte Stieltjes-Transformierte
≡ Herglotz-Funktion  ⟺  alle γ_ρ ∈ ℝ  ⟺  RH.
```

Nicht die unregulierte Summe allein. ⚠[M]

---

## Korrektur 2: Richtiger i-Faktor für Herglotz-Kompatibilität ⚠[M]

Für s = 1/2 + iz:

```
s - ρ = (1/2 + iz) - (1/2 + iγ_ρ) = i(z - γ_ρ)
```

Also:

```
1/(s - ρ) = 1/(i(z - γ_ρ)) = i/(γ_ρ - z)
```

Ein Stieltjes-Term hat die Form 1/(γ_ρ - z) (mit Residuum +1 für γ_ρ ∈ ℝ).
Daher ist die relevante transformierte Größe:

```
-i ξ'/ξ(1/2 + iz)   oder eine symmetrisierte/renormalisierte Variante.
```

Das Vorzeichen muss exakt so gewählt werden, dass

```
Im m(z) > 0    für Im z > 0.
```

Formale Verifikation offen. ⚠[M]

**Merke:** Die naive Identifikation m_Ω(z) = ξ'/ξ(1/2+iz) ist falsch;
die korrekte Formel trägt einen i-Faktor und Regularisierungsterme.

---

## Korrektur 3: Matrix-Weyl-Funktion als natürlicherer Rahmen ❓[O]

Wenn D_rel in mehrere arithmetische Komponenten zerfällt
(nach m-Sektoren, Primzahl-Typen, Symmetriekomponenten), ist ein
einzelner Basisvektor vermutlich nicht zyklisch.

**Skalar:** m_Ω(z) ausreichend nur wenn D_rel irreduzibel (einfaches Spektrum).

**Matrix-Herglotz-Funktion (allgemeiner Fall):**

```
M_{αβ}(z) := ⟨Ω_α, (D_rel - z)^{-1} Ω_β⟩    (α, β = 1, ..., K)
```

Dies ist eine Matrix-Herglotz-Funktion: M(z)^* = M(z̄), Im M(z) ≥ 0 für Im z > 0.

Die Zyklizitätsbedingung wird dann:

```
span{ f(D_rel) Ω_α : α = 1,...,K, f ∈ C_c(ℝ) }  dicht in H.
```

Natürliche Kandidaten: Ω_α = η_{(p_α, m_α, r_α, u_α)} für repräsentative
Primzahl-/Divisor-Sektoren. ❓[O]

---

## Vier Teilprobleme NEU-63 (aktualisiert)

### 63.A — Zyklisches/totales Testsystem ❓[O]

Ein Ω oder Ω = {Ω_α} mit
```
span{ f(D_rel) Ω_α : f ∈ C_c(ℝ) }  dicht in H_rel^eff.
```
Offen: Existenz und Konstruktion. ❓[O]

### 63.B — Analytischer Limes m_{Ω,N}(z) → m_Ω(z) ✓[M]

Direkte Konsequenz aus NEU-59–62:
```
m_{Ω,N}(z) := ⟨Ω, (A_N^{Jac,-} - z)^{-1} Ω⟩  →  ⟨Ω, (D_rel - z)^{-1} Ω⟩ = m_Ω(z)
```
punkweise für alle z ∈ ℂ\ℝ. Starke Resolventenkonvergenz ⇒ Matrixelementen-Konvergenz. ✓[M]

### 63.C — Arithmetischer Limes m_{Ω,N}(z) → m_arith(z) ❓[O]

Kernfrage: Ist m_{Ω,N}(z) = ⟨Ω, (A_N^{Jac,-} - z)^{-1} Ω⟩ als endlicher
Euler-/Dirichlet-/Explizite-Formel-Ausdruck berechenbar?

Wenn
```
m_{Ω,N}(z) = -Q_N(z)/P_N(z)    (endlicher J-Bruch/Kettenbruch)
```
und die Polynome P_N, Q_N Divisor-/Euler-Struktur tragen, dann sollte
m_arith(z) = lim_{N→∞} m_{Ω,N}(z) explizit identifizierbar sein. ❓[O]

→ NEU-64

### 63.D — m_arith Herglotz ⟺ RH ⚠[M]

Konzeptuell gesichert (nach Regularisierung):
```
Im m_arith(z) = Σ_ρ Im(z)/|γ_ρ - z|^2  > 0    für Im z > 0
             ⟺  alle γ_ρ ∈ ℝ
             ⟺  RH.
```
Formale Verifikation mit Regularisierung: ⚠[M] → vertieft in NEU-64/65.

---

## Zwei-Seiten-Strategie (Hauptansatz)

```
m_{Ω,N}(z)  --[NEU-59-62]--->  m_Ω(z)
    ↓
    |
    +--[NEU-64]--->  m_arith(z)

        ⇓  (Eindeutigkeit Herglotz-Limes)

m_Ω(z) = m_arith(z)
```

Vorteil: Kein direkter Zugriff auf D_rel-Spektrum nötig.

---

## Status NEU-63

| Teilproblem | Inhalt | Status |
|---|---|---|
| 63.A | Zyklisches Testsystem (skalar oder Matrix) | ❓[O] |
| 63.B | m_{Ω,N}(z) → m_Ω(z) (analytisch) | ✓[M] |
| 63.C | m_{Ω,N}(z) → m_arith(z) (arithmetisch) | ❓[O] → NEU-64 |
| 63.D | m_arith Herglotz ⟺ RH (reguliert) | ⚠[M] |
| i-Faktor: -iξ'/ξ vs. rohe Partialbruchsumme | | ⚠[M] |
| Matrix-Herglotz als allg. Rahmen | | ❓[O] |

---

## Literatur

- Teschl, G.: *Jacobi Operators and Completely Integrable Nonlinear Lattices*, AMS 2000
  (Weyl-m-Funktion, J-Brüche, Kap. 2–3)
- Simon, B.: *Szegő's Theorem*, AMS 2011, Kap. 2 (Herglotz-Theorie, Matrix-Herglotz)
- Gesztesy, F. & Tsekanovskii, E.: *On Matrix-Valued Herglotz Functions*,
  Math. Nachr. 218 (2000) (Matrix-Weyl-Funktionen)
- Damanik, D., Killip, R. & Simon, B.: *Perturbations of orthogonal polynomials*
  (Jacobi-Kettenbruch, Limes-Theorie)
- Titchmarsh, E.C.: *The Theory of the Riemann Zeta-Function*, Oxford 1986
  (ξ'/ξ-Entwicklung, Hadamard-Produkt, Kap. 3)
- Connes, A.: Selecta Math. 5 (1999) (Spektral-Interpretation, Regularisierung)
