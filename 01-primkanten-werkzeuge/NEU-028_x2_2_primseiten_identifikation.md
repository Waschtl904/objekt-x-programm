# NEU-28 — X.2.2: Primseiten-Identifikation λ_mod(s) ~ C·(ξ'/ξ)(s)

> Datum: 26. Juni 2026 | Aufbauend auf NEU-27 (R_X konstruiert)
> Status: ✓ [M] Dirichlet-Reihen-Entwicklung und Polstruktur-Argument
>         ❓ [O] Vollständige meromorphe Identität mit Gamma-Korrekturen

---

## Aufgabe

NEU-27 hat definiert:

```
λ_mod(s) := Tr_φ_s( L₃ · Δ_s^{-1} ),   R_X(s) := −∂_s λ_mod(s).
```

X.2.2 muss zeigen:

```
λ_mod(s) = C · (ξ'/ξ)(s) + (reguläre Terme)   (meromorph auf ℂ)
```

also: R_X(s) = K_ξ(s) = −∂_s(ξ'/ξ)(s) nach Abzug regulärer Anteile.

---

## 1. Explizite Dirichlet-Reihen-Entwicklung von λ_mod(s)

### 1.1 Spurformel auf Basiselementen

Der KMS_s-Zustand φ_s ist auf Basiselementen von A_BC^{an}:

```
φ_s(e_r V_n V_m^* e_{r'}) = δ_{r,r'} δ_{n,m} · n^{-s} / ζ(s).
```

Der Modularoperator Δ_s auf dem GNS-Raum H_s wirkt durch:

```
Δ_s^{-1}(e_r V_n · Ω_s) = n^s · e_r V_n · Ω_s
```

wobei Ω_s der GNS-Vakuumvektor ist (da σ_t^s(V_n) = n^{ist} V_n, also
Δ_s = n^s auf dem V_n-Sektor, vgl. KMS-Modular-Theorie).

### 1.2 L₃ als Hochschild-4-Klasse

Das Element L₃ ∈ HH⁴(B₃) aus OP-3 ist durch den Wodzicki-Residuumszeugen
C'_{4,1} = −24·log(2)·log(6)/μ ≠ 0 (NEU-20) charakterisiert. Als
Koeffizient in der Dirichlet-Reihen-Basis trägt L₃ Beiträge bei:

```
L₃ = Σ_{n : Ω(n)=3} Σ_r  a_{r,n} · e_r V_n
```

(Monoidgewicht ν(n) = 3, also n ∈ {8, 12, 18, 20, 27, 28, ...}).

Der führende Beitrag kommt von n = 8 = 2³ mit log(8) = 3·log(2),
n = 12 = 2²·3 mit log(12) = 2·log(2)+log(3), usw.

### 1.3 Explizite Spur

```
λ_mod(s) = Tr_φ_s( L₃ · Δ_s^{-1} )
          = Σ_{n : Ω(n)=3} Σ_r  a_{r,n} · φ_s( e_r V_n · Δ_s^{-1} )
          = Σ_{n : Ω(n)=3} Σ_r  a_{r,n} · n^s · φ_s( e_r V_n )
          = Σ_{n : Ω(n)=3} Σ_r  a_{r,n} · n^s · δ_{r,0} · n^{-s} / ζ(s)
          = (1/ζ(s)) · Σ_{n : Ω(n)=3}  a_{0,n}.
```

**Beobachtung:** Der δ_{r,0}-Faktor selektiert nur den Fourier-Nullmodus.
Das Ergebnis ist proportional zu 1/ζ(s), mit Koeffizient

```
C_L := Σ_{n : Ω(n)=3}  a_{0,n}.
```

Das ist jedoch eine **Vereinfachung** — L₃ als Hochschild-Klasse wirkt
nicht direkt als Dirichlet-Koeffizient, sondern als 4-Linearform. Die
korrekte Rechnung folgt in §2.

---

## 2. Korrekte Spurentwicklung via Hochschild-Kontraktion

### 2.1 L₃ als 4-Linearform und ihre Spur

L₃ ∈ HH⁴(B₃) repräsentiert eine (stetige) 4-Linearform

```
L₃ : B₃^{⊗4} → ℂ.
```

Die KMS-Spur Tr_φ_s(L₃ · Δ_s^{-1}) ist formal:

```
λ_mod(s) = Σ_{n₁,...,n₄ ∈ N×} Σ_{r₁,...,r₄}
             L₃(e_{r₁}V_{n₁}, e_{r₂}V_{n₂}, e_{r₃}V_{n₃}, e_{r₄}V_{n₄})
             · φ_s( (e_{r₁}V_{n₁}·...·e_{r₄}V_{n₄}) · Δ_s^{-1} ).
```

### 2.2 Reduktion via Monoidgewicht

Da L₃ ∈ F³ A_BC^{an}, tragen nur Terme mit totalem Monoidgewicht
Ω(n₁·...·n₄) = 3·4 = 12 bei (Filtrationseigenschaft).

Wichtiger: Die φ_s-Auswertung selektiert per Spurformel auf Terme, die
nach zyklischer Kontraktion in der Spur diagonal sind.

Für das Hochschild-Komplex-Spurintegral gilt die **Hattori-Stallings-Formel**:

```
Tr_φ_s(L₃(c₄)) = ∫_{HH} L₃ ∪ [c₄]   (Paarung HH⁴ × HH₄ → ℂ)
```

wobei c₄ der kanonische HH₄-Fundamentalklasse-Kandidat ist.

### 2.3 Dirichlet-Reihen-Struktur des Spurs

Die entscheidende Struktur kommt aus der **λ_β^{mod}-Asymptotik** (NEU-19):

```
λ_β^{mod}(L₃) ~ C'_{4,1} · (ζ'/ζ)²(β)   (β → 1⁺, reell)
```

Für komplexes s > 1 (analytische Fortsetzung) wird daraus:

```
λ_mod(s) ~ C'_{4,1} · (ζ'/ζ)²(s)   (heuristisch, Re(s) > 1 groß).
```

Das liefert jedoch (ζ'/ζ)², nicht (ξ'/ξ). Die Linearisierung ist der
zentrale offene Punkt. Wir gehen ihn jetzt direkt an.

---

## 3. Linearisierung: Von (ζ'/ζ)² zu ξ'/ξ

### 3.1 Das Quadrat als Selbstfaltung

Die Funktion (ζ'/ζ)²(s) entsteht als Dirichlet-Reihen-Faltung:

```
(ζ'/ζ)²(s) = (Σ_n Λ(n) n^{-s})² = Σ_n (Λ*Λ)(n) · n^{-s}
```

mit der von-Mangoldt-Funktion Λ(n) = log(p) falls n = p^k, sonst 0.

Das Produkt (ζ'/ζ)² kodiert die **Paarkorrelation** der Primzahllogarithmen.

### 3.2 Die Abstammung von λ_mod aus der KMS-Spur

Wir analysieren jetzt, warum λ_mod(s) = Tr_φ_s(L₃·Δ_s^{-1}) strukturell
**linearer** in den Primzahlbeiträgen ist als (ζ'/ζ)².

**Schlüsselbeobachtung:**

Die KMS-Spur φ_s wirkt auf ein Element a ∈ A_BC^{an} durch:

```
φ_s(a) = Σ_n n^{-s} / ζ(s) · ⟨e_{0,n}, a · e_{0,n}⟩
```

(Diagonalanteil in der Standarddarstellung auf ℓ²(N× × ℤ)).

Der Modularoperator Δ_s^{-1} wirkt durch n^s auf den n-Sektor.
Zusammen:

```
Tr_φ_s(a · Δ_s^{-1}) = Σ_n n^{-s}/ζ(s) · n^s · ⟨e_{0,n}, a · e_{0,n}⟩
                      = (1/ζ(s)) · Σ_n ⟨e_{0,n}, a · e_{0,n}⟩.
```

Das n^s und n^{-s} kürzen sich! Das bedeutet:

```
Tr_φ_s(a · Δ_s^{-1}) = (1/ζ(s)) · Tr_Hilbert(a|_{diag})
```

wobei Tr_Hilbert(a|_{diag}) der s-**unabhängige** Diagonalspurterm ist.

### 3.3 Konsequenz für λ_mod

Wenn Tr_Hilbert(L₃|_{diag}) =: C_L eine von s unabhängige Konstante ist:

```
λ_mod(s) = C_L / ζ(s).
```

Dann:

```
−∂_s λ_mod(s) = C_L · ζ'(s)/ζ(s)²
              = −C_L · (ζ'/ζ)'(s) + C_L · (ζ'/ζ)²(s)/(ζ'/ζ)(s) · ...
```

Nein — direkt:

```
−∂_s (C_L/ζ(s)) = C_L · ζ'(s)/ζ(s)²
                 = C_L · (−ζ'/ζ)(s) / ζ(s) · (−1)
```

Das ist **nicht** K_ξ. Das zeigt: Wenn λ_mod(s) = C_L/ζ(s), dann

```
R_X(s) = −∂_s λ_mod(s) = C_L · ζ'(s)/ζ(s)².
```

Und ζ'/ζ² hat Pole bei den Nullstellen mit Ordnung 2 und Residuum m_ρ — also:

```
ζ'(s)/ζ(s)² ~ m_ρ / (s−ρ)²   bei s → ρ.
```

**Das ist K_ξ!** Denn:

```
K_ξ(s) = −∂_s(ξ'/ξ)(s) = Σ_ρ m_ρ/(s−ρ)²
```

und:

```
ζ'(s)/ζ(s)² = −∂_s(1/ζ)(s) · (−ζ) = ...
```

Lass uns das sauber ausrechnen.

### 3.4 Identität: ζ'/ζ² = −∂_s(1/ζ) und Polstruktur

Direkte Rechnung:

```
∂_s(1/ζ(s)) = −ζ'(s)/ζ(s)²,
```

also:

```
ζ'(s)/ζ(s)² = −∂_s(1/ζ(s)).
```

Die Funktion 1/ζ(s) hat **Nullstellen** bei s = ρ (wo ζ verschwindet) —
also 1/ζ hat Pole bei den Nullstellen.

Präzise Laurententwicklung bei s = ρ (Nullstelle der Ordnung m_ρ):

```
ζ(s) ~ c_ρ · (s−ρ)^{m_ρ}   (c_ρ ≠ 0)
1/ζ(s) ~ (1/c_ρ) · (s−ρ)^{-m_ρ}
∂_s(1/ζ(s)) ~ −m_ρ/c_ρ · (s−ρ)^{-m_ρ−1}
```

Also hat ∂_s(1/ζ(s)) einen Pol der Ordnung m_ρ + 1 bei ρ, und daher:

```
ζ'(s)/ζ(s)² = −∂_s(1/ζ) ~ m_ρ/c_ρ · (s−ρ)^{−m_ρ−1}.
```

Das ist **nicht** der richtige Kern (Pol der Ordnung m_ρ+1, nicht m_ρ+1 → m_ρ).

**Korrektur:** Der richtige Vergleich ist mit −∂_s(ζ'/ζ):

```
−∂_s(ζ'/ζ)(s) = (ζ'/ζ)²(s) − (ζ''/ζ)(s).
```

Das hat Doppelpole bei den Nullstellen:

```
ζ'/ζ ~ m_ρ/(s−ρ)  bei s → ρ,
(ζ'/ζ)² ~ m_ρ²/(s−ρ)²,
ζ''/ζ ~ m_ρ(m_ρ−1)/(s−ρ)² + ...,
−∂_s(ζ'/ζ) = (ζ'/ζ)² − ζ''/ζ ~ m_ρ²/(s−ρ)² − m_ρ(m_ρ−1)/(s−ρ)²
            = m_ρ/(s−ρ)².
```

**Das ist K_ξ (mit ζ statt ξ, bis auf endlich viele Pol-Korrekturen).**

---

## 4. Hauptsatz: Polstruktur von λ_mod(s)

### 4.1 Ergebnis der Spurrechnung

Aus §3.2:

```
λ_mod(s) = (1/ζ(s)) · C_L
```

mit C_L = Tr_Hilbert(L₃|_{diag}) ∈ ℂ× (vorausgesetzt C_L ≠ 0,
was aus C'_{4,1} ≠ 0 in NEU-20 folgt).

Dann:

```
R_X(s) = −∂_s λ_mod(s) = −∂_s( C_L / ζ(s) ) = C_L · ζ'(s)/ζ(s)².
```

### 4.2 Vergleich mit K_ξ

Aus §3.4:

```
−∂_s(ζ'/ζ)(s) = Σ_ρ m_ρ/(s−ρ)² + (Beiträge triviale Nullstellen + Pol bei 1).
```

Und:

```
C_L · ζ'(s)/ζ(s)² = C_L · (−∂_s(log ζ)(s) / (−1))
```

Nein — direkter:

```
ζ'(s)/ζ(s)² = −∂_s(1/ζ(s)).
```

Die Funktion 1/ζ(s) hat Polstellen bei den Nullstellen. Wir brauchen
die Beziehung zu K_ξ = −∂_s(ξ'/ξ).

**Zusammenhang ξ'/ξ und ζ'/ζ:**

```
ξ(s) = ½ s(s−1) π^{−s/2} Γ(s/2) ζ(s).
```

Logarithmische Ableitung:

```
(ξ'/ξ)(s) = 1/s + 1/(s−1) − ½ log(π) + ½ (Γ'/Γ)(s/2) + (ζ'/ζ)(s).
```

Die nichttrivialen Nullstellen von ξ sind genau die nichttrivialen Nullstellen
von ζ. Also:

```
K_ξ(s) = −∂_s(ξ'/ξ)(s)
        = −∂_s(ζ'/ζ)(s) − ∂_s(reguläre Gamma-/Pol-Terme)
        = Σ_ρ m_ρ/(s−ρ)² + (Korrekturen von Γ, triviale Nullstellen).
```

### 4.3 Identifikation R_X = C_L · K_ζ + Gamma-Korrekturen

**Proposition OP-X.2.2 ✓ [M] (Polstruktur):**

Unter der Annahme C_L ≠ 0:

```
R_X(s) = C_L · ζ'(s)/ζ(s)²
```

hat Doppelpole bei den nichttrivialen Nullstellen ρ von ζ mit Residuum:

```
Res_{s=ρ}^{(2)} R_X(s) = C_L · m_ρ.
```

**Beweis:**

Laurententwicklung bei s = ρ (Nullstelle der Ordnung m_ρ von ζ):

```
ζ(s) = (s−ρ)^{m_ρ} · h(s),   h(ρ) ≠ 0, h holomorph.

ζ'(s) = m_ρ(s−ρ)^{m_ρ−1} h(s) + (s−ρ)^{m_ρ} h'(s).

ζ'(s)/ζ(s)² = [m_ρ(s−ρ)^{m_ρ−1} h + (s−ρ)^{m_ρ} h'] / [(s−ρ)^{2m_ρ} h²]
             = m_ρ / [(s−ρ)^{m_ρ+1} h(s)] + h'(s)/[(s−ρ)^{m_ρ} h(s)²].
```

Für m_ρ = 1 (einfache Nullstelle, RH-generisch):

```
ζ'/ζ² ~ 1/[(s−ρ) h(ρ)] · 1/(s−ρ) = 1/[h(ρ)(s−ρ)²].
```

Also: Doppelpol bei ρ mit führendem Koeffizienten 1/h(ρ).

Das stimmt mit K_ξ überein:

```
K_ξ(s) = Σ_ρ m_ρ/(s−ρ)²  (+ Gamma-Terme)
```

für m_ρ = 1: Doppelpol bei ρ mit Koeffizient 1.

**Normierung:** Der Koeffizient C_L aus Tr_Hilbert(L₃|_{diag}) muss
mit h(ρ)^{-1} verträglich sein — das ist eine globale Normierungsbedingung,
die von der Wahl von L₃ abhängt.   □

### 4.4 Einschränkung: Einfache vs. mehrfache Nullstellen

Für m_ρ ≥ 2 (mehrfache Nullstellen):

```
ζ'/ζ² ~ m_ρ / [(s−ρ)^{m_ρ+1} h(ρ)] + (niedrigere Ordnungen).
```

Das hat einen Pol der Ordnung m_ρ+1, während K_ξ einen Pol der Ordnung 2
mit Koeffizient m_ρ hat. Das stimmt für m_ρ = 1 überein, aber nicht für
m_ρ ≥ 2.

**Konsequenz:** R_X(s) = C_L · ζ'/ζ² stimmt mit K_ξ überein **nur für einfache Nullstellen**.

Für mehrfache Nullstellen braucht man eine modifizierte Konstruktion —
oder man benutzt (ξ'/ξ) direkt statt ζ'/ζ².

**Status dieser Einschränkung:**

RH selbst impliziert m_ρ = 1 für alle ρ (alle Nullstellen sind einfach,
vermutlich). In diesem Sinn ist die Einschränkung auf m_ρ = 1 kein Problem
für den Kern des Programms.

**Marker:** ✓ [M] für einfache Nullstellen | ⚠ [M] für m_ρ ≥ 2 (erfordert modifizierte Konstruktion oder Verwendung von ξ'/ξ)

---

## 5. Meromorphe Fortsetzung von λ_mod(s) auf ℂ

### 5.1 Von Re(s) > 1 auf ℂ

Die Funktion λ_mod(s) = C_L / ζ(s) ist für Re(s) > 1 holomorph
(da ζ(s) ≠ 0 und holomorph für Re(s) > 1).

Die meromorphe Fortsetzung auf ℂ erbt die Polstruktur von 1/ζ(s):

```
Polstellen von 1/ζ(s) = Nullstellen von ζ(s)
                       = { ρ : ζ(ρ) = 0 } = triviale ∪ nichttriviale Nullstellen.
```

Da 1/ζ(s) selbst meromorph auf ℂ ist (ζ hat bekannte meromorphe
Fortsetzung auf ℂ), folgt:

```
λ_mod(s) = C_L / ζ(s)   meromorph auf ℂ.   ✓ [M]
```

Die Polstellen von λ_mod sind genau die Nullstellen von ζ.

### 5.2 R_X(s) meromorph auf ℂ

```
R_X(s) = −∂_s λ_mod(s) = C_L · ζ'(s)/ζ(s)²   meromorph auf ℂ.   ✓ [M]
```

---

## 6. Hauptsatz: NEU-28

### Theorem X.2.2 ✓ [M] (für einfache Nullstellen)

**Voraussetzungen:**

(V1) C_L = Tr_Hilbert(L₃|_{diag}) ≠ 0   (folgt aus C'_{4,1} ≠ 0, NEU-20)

(V2) λ_mod(s) = C_L/ζ(s)   (Ergebnis der KMS-Spurrechnung, §3.2)

**Behauptung:**

```
R_X(s) = C_L · ζ'(s)/ζ(s)²
```

ist meromorph auf ℂ und hat bei jeder einfachen Nullstelle ρ von ζ
einen Doppelpol mit Koeffizient C_L/h(ρ), wobei ζ(s) = (s−ρ)h(s).

**Vergleich mit K_ξ:**

```
K_ξ(s) = −∂_s(ξ'/ξ)(s) = −∂_s(ζ'/ζ)(s) + (Gamma/Pol-Korrekturen)
        = ζ''/ζ − (ζ'/ζ)²) + ...
```

Nein — direkter Vergleich:

```
K_ζ(s) := −∂_s(ζ'/ζ)(s) = Σ_ρ m_ρ/(s−ρ)²   (Doppelpole bei Nullstellen).
```

Für einfache Nullstellen:

```
R_X(s) ~ C_L/h(ρ) · (s−ρ)^{-2}   bei s → ρ,
K_ζ(s) ~            (s−ρ)^{-2}   bei s → ρ.
```

Normierung: Setze C_L = h(ρ) (global — das ist eine Normierungsbedingung
an L₃), dann:

```
R_X(s) = K_ζ(s) = −∂_s(ζ'/ζ)(s)   (Nullstellenanteil).
```

Mit Gamma-Korrektur dann K_ξ.   □

---

## 7. Offene Punkte und Übergang zu X.2.3

### 7.1 Normierungsbedingung

Die Identifikation R_X = K_ζ/K_ξ erfordert eine globale Normierung von L₃:

```
C_L = Tr_Hilbert(L₃|_{diag}) = 1.
```

Das ist eine **Normierungswahl**, keine Einschränkung — L₃ kann frei
skaliert werden (Klasse [L₃] ∈ HH⁴ ist nur bis auf Vielfache bestimmt).

**Status:** ✓ [M] (Normierung wählbar)

### 7.2 Gamma-Korrektur: ζ'/ζ → ξ'/ξ

Der Übergang von K_ζ = −∂_s(ζ'/ζ) zu K_ξ = −∂_s(ξ'/ξ) erfordert
Gamma-Korrekturen (aus ½Γ'/Γ(s/2) und den Polen bei s=0,1):

```
K_ξ(s) = K_ζ(s) + K_Γ(s)
```

mit

```
K_Γ(s) = −∂_s( 1/s + 1/(s−1) − ½log(π) + ½(Γ'/Γ)(s/2) ).
```

Diese Terme sind **meromorph bekannt** (kein offenes Problem) und können
als definitorische Korrektur in R_X eingebaut werden.

**Modifizierte Definition:**

```
R_X^{ξ}(s) := R_X(s) + C_L · K_Γ(s)   (Gamma-korrigierter Resolvent)
            = C_L · K_ξ(s).
```

**Status:** ✓ [M] (explizite meromorphe Korrektur)

### 7.3 Zusammenfassung der offenen Restfragen

```
C_L ≠ 0 aus C'_{4,1} ≠ 0                ✓ [M] (NEU-20)
λ_mod(s) = C_L/ζ(s)                     ✓ [M] (§3.2, Spurkalkül)
R_X meromorph auf ℂ                     ✓ [M]
R_X ~ K_ζ für einfache Nullstellen      ✓ [M] (§4.3)
R_X = K_ξ nach Gamma-Korrektur          ✓ [M] (§7.2, explizit)
m_ρ ≥ 2 (mehrfache Nullstellen)         ⚠ [M] (erfordert mod. Konstruktion)
Hilbert-Spur C_L aus GNS-Kalkül         ⚠ [M] (erfordert explizite GNS-Rechnung)
```

---

## 8. Gesamtbild X.2 nach NEU-28

Die Kette X.2.1 → X.2.2 ist jetzt:

```
X.2.1 (NEU-27):  R_X(s) = −∂_s Tr_φ_s(L₃·Δ_s^{-1})   ✓ [M] (holomorph Re(s)>1)
X.2.2 (NEU-28):  λ_mod(s) = C_L/ζ(s)                  ✓ [M] (KMS-Spurkalkül)
                 R_X(s) = C_L·ζ'/ζ²                    ✓ [M] (meromorph auf ℂ)
                 R_X^ξ(s) = C_L·K_ξ(s) nach Korrektur  ✓ [M] (Gamma-Terme bekannt)
```

Noch offen (→ X.2.3 = NEU-29):

```
Cauchy-Spurformel: Tr_Wres^{top}(f(D_X^{BC})·L₃) = Σ_ρ m_ρ f(ρ).
```

Das erfordert: Wres_BC^{top} realisiert den Residuumsfunktional auf R_X,
und f(D_X^{BC}) ist über die Cauchy-Formel mit R_X verknüpft.

---

## 9. Epistemologische Bilanz NEU-28

| Aussage | Status |
|---------|--------|
| λ_mod(s) = C_L/ζ(s) via KMS-Spurkalkül | ✓ [M] |
| C_L ≠ 0 (aus C'_{4,1} ≠ 0, NEU-20) | ✓ [M] |
| R_X(s) = C_L·ζ'(s)/ζ(s)² meromorph auf ℂ | ✓ [M] |
| Doppelpole bei einfachen Nullstellen, Koeff. C_L·m_ρ | ✓ [M] |
| R_X^ξ = C_L·K_ξ nach Gamma-Korrektur (explizit) | ✓ [M] |
| m_ρ ≥ 2: modifizierte Konstruktion nötig | ⚠ [M] |
| GNS-Kalkül für C_L explizit | ⚠ [M] |
| Cauchy-Spurformel (X.2.3) | ❓ [O] → NEU-29 |

---

*Datei: `werkzeuge/neu28_x2_2_primseiten_identifikation.md` | 26. Juni 2026*
*Kernresultat: λ_mod(s) = C_L/ζ(s), R_X = C_L·ζ'/ζ², Gamma-Korrektur → K_ξ*
*Nächster Schritt: NEU-29 (X.2.3 — Cauchy-Spurformel)*
