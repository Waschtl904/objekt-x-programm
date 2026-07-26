# NEU-32 — X.3: Connes-Kompass und Minimalbedingungen für D_X^{geom}

> Datum: 28. Juni 2026 | Aufbauend auf NEU-30+31 (RH-Äquivalenzsatz, det_Wres)
> Status: ✓ [M] Minimalbedingungen extrahiert | ❓ [O] Konvergenz det_Wres → ξ(s)

---

## Funktion von NEU-32

Vor dem direkten Konstruktionsversuch (NEU-33) muss geklärt sein, welche
**Minimalbedingungen** D_X^{geom} erfüllen muss — und welche Fehler der
direkte Bau typischerweise macht. Connes' Analogiekonstruktion liefert
diesen Kompass.

**Leitfrage:** Was lehrt Connes' Ansatz über die Struktur eines legitimen
D_X^{geom}, und wie übersetzen sich seine Bedingungen in unser BC-Programm?

---

## 1. Connes' Analogiekonstruktion: Extrakt

### 1.1 Endliche Eulerprodukt-Operatoren

In den Arbeiten von Connes–Consani–Moscovici (ab 2010, aktuell 2026-Survey)
werden selbstadjungierte Approximanten über **endliche Eulerprodukte** konstruiert.

Für eine endliche Primzahlmenge P_N = {p : p ≤ N} definiere:

```
ξ_N(s) := ½ · s(s−1) · π^{−s/2} · Γ(s/2) · Π_{p ≤ N} (1 − p^{-s})^{-1}.
```

Das ist die **N-trunkierte ξ-Funktion** (Euler-Produkt bis N).

Der zugehörige selbstadjungierte Operator A_N auf einem geeigneten
L²-Raum hat die Eigenschaft:

```
det(s − A_N) ~ ξ_N(s).
```

Die Konvergenz A_N → A (und det(s−A_N) → ξ(s)) für N → ∞ würde RH implizieren,
weil das Spektrum von A_∞ dann auf ½+iℝ liegt.

### 1.2 Die Rang-eins-Störungs-Konstruktion

Connes–Moscovici konstruieren A_N als **Rang-eins-Störung** eines
Skalierungs-Spektraltripels:

```
A_N = D_scale + |e_N⟩⟨e_N|,
```

wobei D_scale der Skalierungsoperator (mit Spec = log(N×)) ist und
|e_N⟩ ein Rang-eins-Störungsvektor, der die endlichen Primzahlen enkodiert.

**Kern-Eigenschaft (Connes):**

A_N ist selbstadjungiert per Konstruktion (D_scale selbstadjungiert +
symmetrische Rang-eins-Störung). Die Determinante det(s−A_N) hat die
gewünschte Form, und A_N trägt **reelles** Spektrum.

**Anmerkung:** Connes' A_N hat reelles Spektrum — RH entspricht dann
der Bedingung Spec(A_∞ − ½) ⊂ iℝ, d.h. Re(Spec A_∞) = ½.

### 1.3 Der ungelöste Grenzschritt

Der Übergang N → ∞ (von endlichen Eulerprodukten zum vollen ξ(s)) ist
der zentrale harte Schritt, den Connes bis heute nicht vollständig gelöst hat.

Die Schwierigkeit: Die endlichen Operatoren A_N sind selbstadjungiert und
ihr Spektrum ist reell. Die Grenzfunktion ξ(s) hat Nullstellen mit
(vermutlich) Re = ½ — aber der Grenzoperator A_∞ könnte spektrale
Instabilitäten entwickeln.

**Lehre für unser Programm:** Derselbe Grenzschritt ist unser Kernproblem.

---

## 2. Übersetzung in das BC-Programm

### 2.1 Trunkierte BC-Algebra B_{3,N}

Definiere die **N-trunkierte BC-Algebra**:

```
B_{3,N} := F³ A_BC^{an} |_{Ω(n) = 3, p|n ⟹ p ≤ N}
         = span{ e_r V_n : Ω(n) = 3, alle Primteiler von n sind ≤ N }.
```

Das ist der Teilraum von B₃, der nur Primrichtungen p ≤ N enthält.

**Beispiel N=2:** Nur n = 8 = 2³ beiträgt (ν(8) = 3, einziger Primteiler 2).
**Beispiel N=3:** n ∈ {8, 12, 18, 27} (Primteiler aus {2,3}).
**Beispiel N=5:** n ∈ {8, 12, 18, 20, 27, 45, 50, ...} (Primteiler aus {2,3,5}).

### 2.2 Trunkierte Spurformel

Die trunkierte KMS-Spurformel:

```
λ_mod^N(s) := Tr_φ_s( L₃^N · Δ_s^{-1} ),
```

wobei L₃^N die Projektion von L₃ auf B_{3,N} ist.

Aus dem Kürzungsmechanismus (NEU-28 §3.2):

```
λ_mod^N(s) = C_L^N / ζ_N(s),
```

wobei:

```
ζ_N(s) := Π_{p ≤ N} (1 − p^{-s})^{-1}   (endliches Euler-Produkt)
C_L^N := Tr_Hilbert(L₃^N|_{diag})         (endliche Summe, wohldefiniert).
```

**Marker:** ✓ [M]

### 2.3 Trunkierte regularisierte Determinante

Analog zu NEU-31:

```
det_Wres^N(s − D_{X,N}^{BC}) ~ ξ_N(s)
```

wobei ξ_N(s) = ½·s(s−1)·π^{−s/2}·Γ(s/2)·ζ_N(s) die N-trunkierte ξ-Funktion ist.

**Marker:** ✓ [M] (formal, relativ zu λ_mod^N = C_L^N/ζ_N)

---

## 3. Minimalbedingungen für D_X^{geom} (Connes-Kompass)

Aus der Connes-Analogie und der BC-Übersetzung extrahieren wir die
**Minimalbedingungen**, die D_X^{geom} (bzw. seine Approximanten D_{X,N}^{BC})
erfüllen müssen:

### (M1) Intrinsische Konstruktion aus BC-Primärdaten

```
D_{X,N}^{BC} wird aus (B_{3,N}, [ω̃₂]|_N, [L₃^N], Wres_BC^{top}|_N)
konstruiert — nicht aus den Nullstellen von ζ_N.
```

**Konsequenz:** Spec(D_{X,N}^{BC}) folgt aus der Konstruktion, nicht als Input.

### (M2) Selbstadjungiertheit / Normalität bzgl. endlicher Paarung B_N

```
B_N([Ψ],[c]) := Wres_BC^{top}( R₃(Ψ(c)) · L₃^N )
```

ist die N-trunkierte Frobenius-Paarung.

D_{X,N}^{BC} soll wesentlich normal (oder selbstadjungiert modulo ½·I)
bzgl. B_N sein.

### (M3) Determinantenkonvergenz

```
det_Wres^N(s − D_{X,N}^{BC})  →  C · ξ(s)   (N → ∞),
```

und diese Konvergenz soll aus der BC-Struktur folgen, nicht per Definition.

**Das ist der Kern-❓ [O]-Punkt** — Connes hat den Grenzschritt für seine
A_N ebenfalls nicht vollständig gelöst.

### (M4) Positive Hilbertisierung im Limes

```
⟨·,·⟩_{B_N}  →  ⟨·,·⟩_{Wres}   (positiv-semidefinit im Limes N → ∞).
```

Für festes N ist B_N auf B_{3,N} (endlich-dimensionaler Anteil) positiv
oder kontrollierbar — die Positivität im Limes ist die schwierige Bedingung.

---

## 4. Typische Fehler und ihre Diagnose

### Fehler 1: Nullstellen als Eigenwerte per Konstruktion einsetzen

```
D_{X,N}^{BC}(e_{ρ,j}) := ρ · e_{ρ,j}   (D_Z aus NEU-26)
```

→ tautologisch: Spec eingesetzt, keine Determinantenkonvergenz aus BC-Daten.

**Diagnose:** det_Wres(s−D_{X,N}^{BC}) = Π_ρ (s−ρ) per Definition —
das ist nicht ξ(s) aus einer nicht-tautologischen Berechnung.

### Fehler 2: Reelles Spektrum per ½+i-Trick einbauen

```
D_{X,N}^{BC} := ½·I + i·A_N,   Spec(A_N) ⊂ ℝ per Konstruktion.
```

→ nicht tautologisch bezüglich der Nullstellen, aber: Spec(D_{X,N}^{BC}) ⊂ ½+iℝ
per Konstruktion, d.h. RH ist eingebaut, bevor man es beweist.

**Diagnose:** Die Selbstadjungiertheit von D_{X,N}^{BC} − ½·I ist Bedingung,
nicht Resultat. Man muss zeigen, dass A_N (aus BC-Daten) selbstadjungiert
ist — ohne das vorauszusetzen.

### Fehler 3: Determinante nur formal

```
det_Wres ~ ξ(s) nur als formale Potenzreihe, ohne Konvergenz.
```

→ valide als Startpunkt (NEU-31 macht das explizit), aber für RH braucht
man analytische Konvergenz.

---

## 5. RH als Grenzproblem

**Leitsatz NEU-32:**

```
RH wird reduziert auf die Konvergenz einer BC-intrinsischen Folge
D_{X,N}^{BC} mit positiver Wres-Paarung:

  D_{X,N}^{BC} − ½·I  schief-selbstadjungiert bzgl. B_N  (für alle N)
  +
  det_Wres^N(s − D_{X,N}^{BC}) → C · ξ(s)  (N → ∞)
  ⟹  RH.
```

**Warum das stärker ist als Connes:**

Connes' Ansatz liefert A_N mit reellem Spektrum — das setzt implizit
voraus, dass D_scale selbstadjungiert ist. Unser Ansatz fordert die
Selbstadjungiertheit von D_{X,N}^{BC} − ½·I bzgl. der **Wres-Paarung**
B_N, die aus BC-Strukturdaten kommt.

Das ist nicht tautologisch, weil B_N indefinit ist — Selbstadjungiertheit
bzgl. einer indefiniten Paarung impliziert **nicht automatisch** reelles
oder ½+iℝ-Spektrum. Es ist eine echte Bedingung.

---

## 6. Checkliste für NEU-33

NEU-33 (BC-Konstruktion der endlichen Approximanten) muss:

```
(C1) D_{X,N}^{BC} explizit aus (B_{3,N}, [ω̃₂]|_N, [L₃^N]) konstruieren.
     Kandidat: modularer Generator + L₃-Kopplungsterm.

(C2) Zeigen: D_{X,N}^{BC} − ½·I ist schief-selbstadjungiert bzgl. B_N.
     Das ist die endliche Positivitätsbedingung.

(C3) Berechnen: det_Wres^N(s − D_{X,N}^{BC}) = C_N · ξ_N(s).
     Das folgt aus λ_mod^N(s) = C_L^N/ζ_N(s) (gesichert).

(C4) Konvergenzfrage stellen: det_Wres^N → C·ξ(s) für N → ∞.
     Das ist der offene Kern — analog zu Connes' ungelöstem Grenzschritt.
```

---

## 7. Epistemologische Bilanz NEU-32

| Baustein | Status |
|----------|--------|
| Connes-Extrakt: endliche Eulerprodukt-Operatoren | ✓ [M] |
| Trunkierte BC-Algebra B_{3,N} | ✓ [M] |
| λ_mod^N(s) = C_L^N/ζ_N(s) | ✓ [M] |
| det_Wres^N ~ ξ_N(s) formal | ✓ [M] |
| Vier Minimalbedingungen (M1)–(M4) isoliert | ✓ [M] |
| Drei Fehlertypen diagnostiziert | ✓ [M] |
| RH als Grenzproblem formuliert | ✓ [M] |
| Konvergenz det_Wres^N → C·ξ(s) (N → ∞) | ❓ [O] → NEU-33+ |
| Positive Hilbertisierung im Limes | ❓ [O] → NEU-33+ |

---

*Datei: `werkzeuge/neu32_x3_connes_kompass.md` | 28. Juni 2026*
*Kernresultat: Minimalbedingungen (M1)–(M4) + Checkliste (C1)–(C4) für NEU-33*
*Leitsatz: RH = Konvergenz einer BC-intrinsischen Folge D_{X,N}^{BC} mit positiver Wres-Paarung*
