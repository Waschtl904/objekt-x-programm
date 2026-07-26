# NEU-15: OP-4 — Frobenius-Funktional auf A_2D^r

> Datum: 19. Juni 2026 | Status: ⚠ [M] — Hauptstruktur klar; zwei technische Punkte offen

---

## 1. Die Frage (OP-4)

Aus NEU-14:

> Existiert auf A_2D^r ein Frobenius-Funktional im strikten algebraischen Sinn,
> d.h. eine nicht-ausgeartete symmetrische Paarung ⟨·,·⟩: A_2D^r ⊗ A_2D^r → ℂ,
> die mit der Hochschild-Struktur verträglich ist?

---

## 2. Was Frobenius bedeutet — präzise Definition

### 2.1 Algebraische Definition (endlich-dimensional)

Eine k-Algebra A ist **Frobenius**, wenn es ein lineares Funktional ε: A → k gibt
(die **Frobenius-Form**), dessen Kern kein nicht-triviales Linksideal enthält.

Äquivalent: Die Paarung β: A ⊗ A → k, β(a ⊗ b) = ε(ab), ist nicht-ausgeartet.

**Problem für A_2D^r**: Die klassische Definition verlangt endliche Dimension.
A_2D^r ist unendlich-dimensional (Fréchet-Raum). Direkter Transfer unmöglich.

### 2.2 Topologische Verallgemeinerung

Für unendlich-dimensionale Fréchet-Algebren gibt es zwei relevante Verallgemeinerungen:

**Definition (schwaches Frobenius-Funktional):**
Ein stetiges lineares Funktional ε: A_2D^r → ℂ heißt schwaches Frobenius-Funktional,
wenn die Paarung β(F, G) = ε(F * G) auf einem dichten Teilraum nicht-ausgeartet ist.

**Definition (KMS-Frobenius nach Connes):**
Ein KMS-Gewicht Ψ auf (A, σ_t) heißt Frobenius-Gewicht, wenn:
```
Ψ(F * G) = Ψ(σ_{iβ/2}(G) * σ_{iβ/2}(F))    (KMS-Symmetriebedingung)
```
und die GNS-Darstellung (H_Ψ, π_Ψ, Λ_Ψ) nicht-ausgeartetes inneres Produkt trägt.

### 2.3 Frobenius und BV-Struktur

**Schlüsselfund aus der Literatur** (Tradler 2008, Menichi 2009):

> *Wenn A eine symmetrische Frobenius-Algebra ist, dann trägt HH*(A, A)
> eine natürliche **Batalin-Vilkovisky (BV)-Algebra-Struktur**,
> deren BV-Operator dem Connes-Operator B entspricht.*

Das ist eine direkte Brücke von Frobenius zu HH²(A_2D^r) — und damit zu X.3!

**Bedeutung für unser Programm**: Wenn A_2D^r eine (verallgemeinerte) Frobenius-Algebra ist,
trägt HH²(A_2D^r, A_2D^r) automatisch eine BV-Struktur mit Connes-B-Operator.
Das wäre eine strukturelle Vertiefung von X.3, weit über den bisherigen Stand hinaus.

---

## 3. Der kanonische Kandidat: Das modulare Funktional ε_β

### 3.1 Konstruktion

Definiere für β > 1:

```
ε_β: A_2D^r → ℂ,   ε_β(F) = φ_{β,triv}(F) · ζ(β)
```

wobei φ_{β,triv} der eindeutige KMS_β-Zustand bei β > 1 auf der trivialen
Einbettung χ = id ist, und ζ(β) die Normierungskonstante.

Explizit auf der Basis V_m e(r) V_n* (Erinnerung: F_{m,n,r} = Koeffizient bei V_m e(r) V_n*):

```
ε_β(F) = Σ_{m ∈ N×} m^{-β} · F_{m,m,0}
```

Das ist der **diagonale β-gewichtete Trace**: Summe über Diagonalelemente mit
Gewicht n^{-β}.

### 3.2 Stetigkeit

ε_β ist stetig auf A_2D^r:

```
|ε_β(F)| ≤ Σ_m m^{-β} |F_{m,m,0}|
          ≤ (Σ_m m^{-β}) · sup_m |F_{m,m,0}|
          ≤ ζ(β) · r_0^(2)(F)     [für β > 1]
```

ζ(β) < ∞ für β > 1, also ε_β stetig. ✓ [M]

### 3.3 Paarung

Die zugehörige Paarung:

```
β_ε(F, G) = ε_β(F * G) = Σ_m m^{-β} · (F * G)_{m,m,0}
```

Für die Faltung (F * G)_{m,m,0} = Σ_k F_{m,k,r} · G_{k,m,-r} (Summe über Zwischenindizes):

```
β_ε(F, G) = Σ_{m,k} m^{-β} · F_{m,k,r} · G_{k,m,-r}
```

---

## 4. Nicht-Ausgeartheit — die entscheidende Rechnung

### 4.1 Was zu zeigen ist

β_ε ist nicht-ausgeartet iff:

```
β_ε(F, G) = 0 für alle G ∈ A_2D^r  ⟹  F = 0
```

### 4.2 Gegenbeispiel-Analyse

Nehme F = u_{(p,q)} (Einheitsvektor bei (m,n) = (p,q), r = 0):

```
β_ε(u_{(p,q)}, G) = Σ_m m^{-β} · (u_{(p,q)} * G)_{m,m,0}
                  = p^{-β} · G_{q,p,0}
```

Das ist Null für alle G genau dann, wenn p^{-β} = 0 — aber p^{-β} > 0 für alle p ∈ N×.

**Konsequenz**: Für jeden Einheitsvektor F = u_{(p,q)} ist β_ε(u_{(p,q)}, G) = p^{-β} · G_{q,p,0}.
Das kann nicht für alle G verschwinden (wähle G = u_{(q,p)}: ergibt p^{-β} ≠ 0).

Also: **kein Einheitsvektor liegt im linken Radikal von β_ε**. ✓

### 4.3 Dichte Nicht-Ausgeartheit

Für allgemeines F = Σ_{m,n} F_{m,n} u_{(m,n)} (endliche Summe):

```
β_ε(F, G) = Σ_{m,n} F_{m,n} · m^{-β} · G_{n,m,0}
```

Das ist Null für alle G iff F_{m,n} · m^{-β} = 0 für alle (m,n) — was F = 0 erzwingt
(da m^{-β} > 0). ✓

**Für unendliche Summen**: Die Nicht-Ausgeartheit gilt auf dem dichten Teilraum
der finiten Elemente (endliche Linearkombinationen von Basisvektoren).
Ob sie auf ganz A_2D^r gilt (vollständige topologische Nicht-Ausgeartheit),
hängt davon ab, ob das Radikal abgeschlossen ist — das ist die offene Restfrage.

**Status Nicht-Ausgeartheit**: ✓ [M] auf dichtem Teilraum; ⚠ [M] topologisch vollständig.

---

## 5. Symmetrie: Ist β_ε symmetrisch?

### 5.1 Berechnung

```
β_ε(F, G) = Σ_{m,k} m^{-β} F_{m,k} G_{k,m}
β_ε(G, F) = Σ_{m,k} m^{-β} G_{m,k} F_{k,m}
           = Σ_{m,k} k^{-β} G_{k,m} F_{m,k}   [Umbenennung m↔k]
```

**Vergleich**:

```
β_ε(F, G) - β_ε(G, F) = Σ_{m,k} (m^{-β} - k^{-β}) F_{m,k} G_{k,m}
```

Das verschwindet **nicht** im Allgemeinen (falls m ≠ k und F_{m,k}, G_{k,m} ≠ 0).

**Ergebnis**: ε_β ist **nicht symmetrisch** — β_ε(F, G) ≠ β_ε(G, F) für allgemeines F, G.

### 5.2 Die KMS-Symmetriebedingung als Ersatz

Statt klassischer Symmetrie gilt die **KMS-Symmetrie**:

```
β_ε(F, G) = β_ε(σ_{iβ}(G), F)
```

denn:

```
ε_β(F * G) = φ_{β}(F * G) · ζ(β)
           = φ_{β}(G * σ_{iβ}(F)) · ζ(β)    [KMS-Bedingung für φ_β]
           = β_ε(σ_{iβ}(G), F)   [nach Berechnung]
```

Das ist das **modulare Pendant** zur Symmetriebedingung.

**Terminologie**: β_ε ist eine **modulare Frobenius-Paarung** (nicht symmetrisch,
aber KMS-symmetrisch mit Nakayama-Automorphismus σ_{iβ}).

### 5.3 Nakayama-Automorphismus

In der Frobenius-Algebra-Theorie gibt es für nicht-symmetrische Paarungen
stets einen **Nakayama-Automorphismus** ν: A → A mit:

```
ε(a · b) = ε(ν(b) · a)    für alle a, b ∈ A
```

Hier: ν = σ_{iβ} (der analytisch fortgesetzte Zeitentwicklungsoperator).

Das ist kein Problem — es ist ein Feature: Es bedeutet, A_2D^r ist eine
**Frobenius-Algebra mit Nakayama-Automorphismus σ_{iβ}**. Das ist der
unendlich-dimensionale Analog zu einer nicht-symmetrischen Frobenius-Algebra.

---

## 6. BV-Struktur auf HH²(A_2D^r)

### 6.1 Das Tradler-Menichi-Resultat

**Theorem (Tradler 2008, Menichi 2009)**:

> Sei A eine symmetrische Frobenius-Algebra (oder eine offene Frobenius-Algebra).
> Dann trägt HH*(A, A) eine BV-Algebra-Struktur mit BV-Operator Δ = B (Connes-Operator).

Für **nicht-symmetrische Frobenius** (mit Nakayama-Automorphismus ν):

> HH*(A, A^ν) trägt eine BV-Struktur, wobei A^ν das ν-verdrehte Bimodul ist.

### 6.2 Anwendung auf A_2D^r

Da A_2D^r eine modulare Frobenius-Algebra mit ν = σ_{iβ} ist:

```
HH²(A_2D^r, A_2D^r^{σ_{iβ}})  trägt eine BV-Algebra-Struktur.  ⚠ [M]
```

wobei A_2D^r^{σ_{iβ}} = A_2D^r als Bimodul mit σ_{iβ}-verdrehter Rechtsmodulstruktur.

**Bedeutung**: Der Connes-Operator B wirkt als BV-Operator auf HH²(A_2D^r, A_2D^r^{σ_{iβ}}).

Das ist eine neue, unerwartete Struktur — über die ursprüngliche X.3-Forderung hinaus.

### 6.3 Verbindung zu OP-2

OP-2 fragt: [ω̃₂] ≠ 0 in HH²(A, A)?

Die BV-Struktur könnte helfen: Wenn HH²(A_2D^r, A_2D^r^{σ_{iβ}}) eine BV-Algebra ist,
dann haben die Hochschild-Klassen eine zusätzliche Struktur (BV-Operator, Gerstenhaber-Produkt),
die zur Nicht-Trivialität von [ω̃₂] Auskunft geben könnte.

**Status**: Potentielle Verbindung zu OP-2, nicht formalisiert. ❓ [O]

---

## 7. Verbindung zu X.6

### 7.1 Was X.6 verlangt

X.6: X trägt eine neue Spurform — weder Wodzicki-Restspur noch Tsygan-Spur,
sondern eine genuinen neuen Spurform, die mit der arithmetischen Struktur (N×-Wirkung,
Skalierung) verträglich ist.

### 7.2 ε_β als Kandidat für X.6

ε_β(F) = Σ_{m ∈ N×} m^{-β} · F_{m,m,0} ist:

- **Spurartig auf dem Diagonalanteil**: ε_β(F * G) verallgemeinert die gewöhnliche Spur
- **N×-skaliert**: ε_β(σ_t(F)) = ε_β(F) (invariant unter der Zeitentwicklung)
- **β-parametrisiert**: Für β → ∞ konzentriert sich ε_β auf m = 1 (Grundzustand)
- **Zeta-normiert**: Σ_m m^{-β} = ζ(β) — die Normierung ist die Riemannsche Zetafunktion

**Vergleich mit bekannten Spurformen:**

| Spur | Definition | Gilt für A_2D^r? |
|------|-----------|-----------------|
| Wodzicki-Restspur | residualer Spurterm, Pseudodifferentialoperatoren | Nein — A_2D^r kein Pseudo-DO |
| Tsygan-Spur | Spur auf zyklischer Homologie | Verwandt, aber nicht identisch |
| **ε_β** | Σ_m m^{-β} F_{m,m,0} | **Ja** — explizit konstruiert |

**Ergebnis**: ε_β ist ein neues Spurform-Funktional auf A_2D^r, das weder Wodzicki noch
Tsygan entspricht. Es ist explizit durch die Zetafunktions-Gewichtung definiert. ⚠ [M]

**X.6 für A_2D^r mit ε_β als Spurform**: VORLÄUFIG POSITIV ⚠ [M]

---

## 8. Hauptresultat NEU-15 (= OP-4 gelöst)

### Theorem (NEU-15, 19. Juni 2026) ⚠ [M]

```
A_2D^r trägt eine modulare Frobenius-Struktur:

Frobenius-Funktional:  ε_β(F) = Σ_{m ∈ N×} m^{-β} · F_{m,m,0}    (β > 1)

Paarung:              β_ε(F, G) = ε_β(F * G)

Nicht-Ausgeartheit:   ✓ [M] auf dichtem Teilraum
                      ⚠ [M] topologisch vollständig (Restfrage)

KMS-Symmetrie:        β_ε(F, G) = β_ε(σ_{iβ}(G), F)   ✓ [M]

Nakayama-Automorphismus: ν = σ_{iβ}   ✓ [M]
```

**Konsequenzen:**

```
(1) HH²(A_2D^r, A_2D^r^{σ_{iβ}}) trägt BV-Algebra-Struktur      ⚠ [M]
(2) ε_β ist natürlicher Kandidat für die neue Spurform X.6         ⚠ [M]
(3) OP-4 (schwache Version): gelöst                                ✓ [M]
(4) OP-4 (starke Version, topologisch nicht-ausgeartet): offen     ❓ [O]
```

---

## 9. Aktualisierter Stand Objekt X nach NEU-15

| Axiom | Status | Quelle |
|-------|--------|--------|
| X.1 (bornologisch-nuklearer Träger) | ✓/⚠ [M] | NEU-12 |
| X.2 (Spektrum = RH-Nullstellen) | ✗ offen | — |
| X.3 (volle HH²-Struktur) | ⚠ [M] | NEU-11, NEU-13 |
| X.4 (KMS, Phasenübergang) | ✓ [M] | NEU-14 |
| X.5 (Konvergenz formal → analytisch) | ✗ offen | — |
| **X.6 (neue Spurform)** | **⚠ [M]** | **NEU-15 — ε_β explizit** |

**Minimalversion X.1 + X.3 + X.4 + X.6**: vier von sechs Axiomen bestätigt oder
explizit konstruiert. ⚠ [M]

---

## 10. Offene Restfragen (aus NEU-15)

| Frage | Status |
|-------|--------|
| NEU-15/R1: Topologische Nicht-Ausgeartheit von β_ε auf ganz A_2D^r | ❓ [O] |
| NEU-15/R2: BV-Struktur auf HH²(A_2D^r, A_2D^r^{σ_{iβ}}) vollständig formalisieren | ❓ [O] |
| NEU-15/R3: Verbindung BV-Operator B zu OP-2 ([ω̃₂] ≠ 0) untersuchen | ❓ [O] |
| NEU-15/R4: β → ∞ Grenzwert von ε_β — Grundzustands-Spurform | ❓ [O] |

---

## 11. Zusammenfassung

```
NEU-15 (= OP-4) Hauptresultat:

A_2D^r ist eine modulare Frobenius-Algebra:
  ε_β(F) = Σ_m m^{-β} F_{m,m,0}   (ζ(β)-gewichtete Diagonalspur)
  Nakayama-Automorphismus: ν = σ_{iβ} (Zeitentwicklung)
  KMS-Symmetrie: β_ε(F,G) = β_ε(σ_{iβ}(G), F)

OP-4 (schwach): gelöst ✓ [M]
OP-4 (stark, topologisch): offen ❓ [O]

Neue unerwartete Struktur:
  HH²(A_2D^r, A_2D^r^{σ_{iβ}}) trägt BV-Algebra ⚠ [M]
  X.6 (neue Spurform): ε_β ist expliziter Kandidat ⚠ [M]

Stand Objekt X: X.1 + X.3 + X.4 + X.6 auf A_2D^r konstruiert ⚠ [M]
```

---

*Datei: `werkzeuge/neu15_op4_frobenius.md` | Erstellt: 19. Juni 2026 | NEU-15*
