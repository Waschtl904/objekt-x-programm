# [NEU-3] Werkzeugblatt — Schweitzer-Mechanismus und starke Spektralinvarianz

> Angelegt: 16. Juni 2026 — Anlass: Abgleich mit OP-1.6d

---

## 1. Zweck

Dieses Werkzeugblatt fixiert die **genauen Hypothesen** des Schweitzer-Mechanismus
im OP-1-Programm. Ziel ist der Abgleich zwischen der für A_2D^r bewiesenen
Mehrfachprodukt-Abschätzung (OP-1.6c) und den Hypothesen der starken Spektralinvarianz.

---

## 2. Schweitzers starke Spektralinvarianz

Sei A eine dichte Fréchet-Unteralgebra einer Banach-Algebra B.
A heißt **stark spektralinvariant** in B, wenn für jedes m eine Konstante D_m, C > 0
und ein p_m ∈ ℕ existieren, so dass für alle n und alle a_1,...,a_n ∈ A gilt:
```
|a_1 ··· a_n|_m  ≤  D_m C^n Σ_{k_1+···+k_n ≤ p_m} |a_1|_{k_1} ··· |a_n|_{k_n}
```

**Entscheidende Bedingung:**
```
|a|_0 = |a|_B       (Basisnorm = Norm der umgebenden Banach-Algebra)
```

Im C*-Fall: |a|_0 = |a|_{C*}.

**Konsequenz (Theorem 1.17 bei Schweitzer):**
Starke Spektralinvarianz => Spektralinvarianz:
```
σ_A(a) = σ_B(a)   für alle a ∈ A.
```

---

## 3. Vergleich mit OP-1.6c

Für A_2D^r wurde bewiesen (OP-1.6c):
```
r_k^(2)(F_1···F_N) ≤ C_k^N N^k Σ_{i=1}^N r_{k+2}^(2)(F_i) Π_{j≠i} r_2^(2)(F_j)
```

Diese Abschätzung ist eine **starke Fréchet-Produktabschätzung**, aber **keine
Schweitzer-Abschätzung** im technischen Sinn. Der Unterschied liegt in der Basisnorm:

```
r_2^(2)(·)  ≠  |·|_{C*}
```

Zwar gilt die stetige Einbettung (OP-1.6b):
```
|F|_{C*}  ≤  C_k r_k^(2)(F)     (k > 1)          [eine Richtung]
```

Aber die umgekehrte Kontrolle
```
r_2^(2)(F)  ≤  C |F|_{C*}                          [andere Richtung]
```
ist im Allgemeinen **nicht zu erwarten** (r_2^(2) ist eine Schalen-ℓ¹-Norm und
im Allgemeinen deutlich stärker als die C*-Norm).

---

## 4. Status von OP-1.6d

Der direkte Schweitzer-Transfer aus OP-1.6c ist **blockiert**:
```
┌────────────────────────────────────────────────────────────┐
│  Direkter Schweitzer-Transfer aus r_2^(2): ✗ [M]           │
│  Spektralinvarianz von A_2D^r bleibt offen.                 │
└────────────────────────────────────────────────────────────┘
```

Der verbleibende Knoten ist nicht mehr die Algebra A_2D^r
(vollständig konstruiert), sondern der passende Spektralinvarianz-Mechanismus.

---

## 5. Anschlussoptionen

### OP-1.6e — C*-verankerte starke Produktabschätzung

Zu zeigen wäre eine Abschätzung der Form
```
r_k^(2)(F_1···F_N) ≤ D_k C^N Σ_{k_1+···+k_N ≤ p_k} |F_1|_{k_1} ··· |F_N|_{k_N}
```
mit |F|_0 = |F|_{C*}. Das wäre der direkte Schweitzer-Weg.

Herausforderung: |F|_{C*} liefert keine Schalenkontrolle; der Sprung von
‖·‖_{C*} zu r_2^(2) ist im Allgemeinen unbeschränkt.

**OP-1.6e: offen.  ❓ [O]**

### OP-1.6f — Wiener-/Beurling-/Groupoid-Weg

Da A_2D^r eine schalen-ℓ¹-artige Algebra ist, könnte Spektralinvarianz besser
über einen Wiener- oder Beurling-Mechanismus laufen.

Mögliche Strategie:
- Reduzierte Normalform als Q_+×-graduierte Algebra auffassen.
- A_2D^r als glatte Beurling-/Schwartz-Unteralgebra einer amenablen
  Groupoid- oder Fell-Bundle-C*-Algebra interpretieren.
- Spektralinvarianz über symmetrische ℓ¹-/Beurling-Algebren oder
  étale Groupoid-Techniken beweisen.

Vorteil: ℓ¹-gewichtete Gruppenalgebren sind klassisch spektralinvariant
(Beurling, Gelfand-Raikov-Shilov). BC-Struktur passt zu amenablen étalen Groupoids.

**OP-1.6f: offen, vermutlich natürlicher als OP-1.6e.  ❓ [O]**

---

## 6. Katalog-Konsequenz

Der OP-1-Block ist analytisch stark:
- p_k widerlegt ✗ [M]
- q_k^♯ widerlegt ✗ [M]
- r_k^♯ konstruiert ✓ [M]
- A_2D^r als Fréchet-*-Algebra, kanonische Normalform ✓ [M]
- Dichte und stetige Einbettung in A_BC^{C*} ✓ [M]
- Mehrfachprodukt-Abschätzung ✓ [M]

Aber:
```
┌────────────────────────────────────────────────────────────┐
│  Spektralinvarianz folgt noch nicht direkt aus Schweitzer.  │
│  Offene Routen: OP-1.6e (C*-verankert) oder               │
│                OP-1.6f (Beurling/Groupoid).               │
└────────────────────────────────────────────────────────────┘
```
