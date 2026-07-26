# [NEU-10] RD-Skalenkorrektur: log N statt Ω(N)

> Sitzung: 13. Juni 2026
> Revision: 15. Juni 2026 (OP-1.1–1.3)
> Nachtrag: 16. Juni 2026 (OP-1.4, OP-1.5a, OP-1.5b, OP-1.6a–c)

---

## Problem

Die früheren RD-Halbnormen `p_k(f) = sup_N e^{kΩ(N)} ‖f_N‖_∞` sind für das BC-Crossed Product
**strukturell überkorrigiert** (exponentiell in der Primfaktoranzahl Ω(N)).

## Begründung (zusammengefasst)

- ‖π(u_n)‖ = 1 in GNS; Wachstum akkumuliert logarithmisch in n, nicht exponentiell in Ω.
- Subadditivität: log(lcm(M,N)) ≤ log M + log N — wie Wortlänge bei Gruppen-RD.

**Korrekte Skalierung:** `p_k(f) = sup_N (1 + log N)^k ‖f_N‖_∞`

---

## OP-1.1: Stern-Test — p_k widerlegt  ✗ [M]

> 15. Juni 2026

S_R = { n : e^R ≤ n < 2e^R }, f^(R) = Σ_{n∈S_R} (1+log n)^{-k} u_n:
p_k(f^(R)) ≤ 1, aber ‖π(f^(R))‖ ≍ e^{R/2}/R^k → ∞.
Ursache: exponentielles Kugelwachstum. **✗ [M]**

---

## OP-1.2: Primschalen-Test — q_k^♯ widerlegt  ✗ [M]

> 15. Juni 2026

q_k^♯(f) = sup_R (1+R)^k (Σ_{e^R≤n<e^{R+1}} ‖f_n‖_∞²)^{1/2}.
Gegenbeispiel P_R (Primschale): kommutierende Shifts, Hardy-Polydisk, z_p→1:
‖π(f^(R))‖ ~ e^{R/2}/R^{k+1/2} → ∞. **✗ [M]**

---

## OP-1.3: Kandidat r_k^♯ — Normkontrolle  ✓ [M] (k > 1)

> 15. Juni 2026

```
I_R := { n ∈ N× : R ≤ log n < R+1 }
r_k^♯(f) := sup_{R≥0} (1+R)^k Σ_{n∈I_R} ‖f_n‖_∞
```
‖π(f)‖ ≤ C_k r_k^♯(f) für k > 1. **✓ [M]**

---

## OP-1.4: Multiplikative Stabilität von r_k^♯  ✓ [M]

> 16. Juni 2026

Schalenfaltung, σ = 2:
```
 r_k^♯(f * g) ≤ C_k r_{k+2}^♯(f) r_{k+2}^♯(g)
```
**✓ [M]**

---

## OP-1.5a: Formale 2D-Schalenalgebra A_2D^r  ✓ [M]

> 16. Juni 2026

```
L(m,n) := log m + log n
r_k^(2)(F) := sup_R (1+R)^k Σ_{L(m,n)∈[R,R+1)} ‖F_{m,n}‖_∞
```
*-stabil ✓, mult. stabil (+2) ✓, Fréchet-vollständig ✓. **A_2D^r: Fréchet-*-Algebra. ✓ [M]**

---

## OP-1.5b: Kanonische BC-Normalform  ✓ [M]

> 16. Juni 2026

```
T = Σ_{gcd(m,n)=1} u_m* F_{m,n} u_n,   F_{m,n} ∈ P_{mn} B
```

**Transfer:** d = gcd(m,n), L_d(f) = u_d* f u_d, dann u_m* f u_n = u_{m₀}*(P_{m₀n₀} L_d(f)) u_{n₀}.

**Normfreundlichkeit:** L(m₀,n₀) = L(m,n) - 2 log d ≤ L(m,n), also r_k^(2)(red(F)) ≤ r_k^(2)(F).

**Eindeutigkeit:** Grad n/m isoliert jeden Summanden via Gauge-Wirkung. ✓

**Einschränkung:** Gilt für algebraische BC-*-Algebra und A_2D^r-Vervollständigung,
nicht den vollen C*-Abschluss (das ist OP-1.6). **✓ [M]**

---

## OP-1.6a: Dichte  ✓ [M]

> 16. Juni 2026

A_2D^r enthält alle endlichen reduzierten Normalformen und damit die algebraische
BC-*-Algebra (erzeugt von B und den u_n). Diese liegt C*-dicht in A_BC^{C*}.

```
A_2D^r ↪ A_BC^{C*}   (dicht)
```
**✓ [M]**

---

## OP-1.6b: Stetige Einbettung  ✓ [M]

> 16. Juni 2026

Für jedes reduzierte F gilt ‖u_m* F_{m,n} u_n‖_{C*} ≤ ‖F_{m,n}‖_∞, also:
```
‖F‖_{C*} ≤ Σ_{m,n} ‖F_{m,n}‖_∞
         = Σ_R A_R^(2)(F)
         ≤ (Σ_R (1+R)^{-k}) r_k^(2)(F)
```
┌───────────────────────────────────────────────────────┐
│  ‖F‖_{C*} ≤ C_k r_k^(2)(F)   (k > 1)                  │
└───────────────────────────────────────────────────────┘
**✓ [M]**

---

## OP-1.6c: Mehrfachprodukt-Abschätzung  ✓ [M]

> 16. Juni 2026

**Schlüsselungleichung (Subadditivität der Schalenliste):**
Für ein Produkt F_1 ··· F_N mit Schalenliste (L_1,...,L_N) gilt:
```
L(Produkt) ≤ L_1 + ··· + L_N.
```

**Gewichtungszerteilung:** Für das Schalensupremum-Gewicht:
```
(1 + L_1 + ··· + L_N)^k ≤ N^k Σ_{i=1}^N (1+L_i)^k.
```

**Strategie:** Genau ein Faktor (Faktor i) trägt das hohe Gewicht (k+2); alle anderen
tragen nur das summierbare 2-Gewicht:
```
‖F_1 ··· F_N‖_∞ ≤ Π_{j=1}^N ‖(F_j)_{m_j,n_j}‖_∞   (komponentenweise).
```
Summation über die Schalen mit der Gewichtszerteilung und Σ_R (1+R)^{-2} < ∞:

┌────────────────────────────────────────────────────────────────┐
│  r_k^(2)(F_1···F_N) ≤ C_k^N N^k                          │
│          × Σ_{i=1}^N r_{k+2}^(2)(F_i) Π_{j≠i} r_2^(2)(F_j)  │
└────────────────────────────────────────────────────────────────┘

Spezialfall Potenzen:
```
r_k^(2)(F^N) ≤ C_k^N N^{k+1} r_{k+2}^(2)(F) (r_2^(2)(F))^{N-1}
```

Dies ist eine polynomial-in-N, exponentiell-kontrollierte Produktabschätzung —
die strukturelle Form, die der Schweitzer-Mechanismus ([NEU-3]) benötigt. **✓ [M]**

**Bedeutung:** Kein kumulativer Indexverlust; die 2-Norm-Faktoren sind durch
Σ_R (1+R)^{-2} < ∞ summierbar, unabhängig von N.

---

## OP-1.6d: Abgleich mit [NEU-3]  ❓ [O]

> 16. Juni 2026

Die Mehrfachprodukt-Abschätzung (OP-1.6c) liefert die richtige Form für den
Schweitzer-Transfer, sofern [NEU-3] die Basis-Norm als r_2^(2) (Schalen-ℓ¹) akzeptiert.

**Kritischer Abgleichspunkt:**
- Falls [NEU-3] erlaubt: r_k(F_1···F_N) ≤ C^N N^p Σ_i r_{k+s}(F_i) Π_{j≠i} r_2(F_j)
  ⇒ OP-1.6 vollständig abgeschlossen. ❓

- Falls [NEU-3] verlangt: r_k(F_1···F_N) ≤ C^N N^p Σ_i r_{k+s}(F_i) Π_{j≠i} ‖F_j‖_{C*}
  ⇒ Echte Lücke: r_2^(2) ist deutlich stärker als ‖·‖_{C*};
     eine r_2^(2)-zu-C*-Brücke wäre dann noch nötig.

**Voraussetzung:** Expliziter Abgleich mit [NEU-3]-Hypothesen (Datei noch nicht angelegt).
Empfehlung: [NEU-3] als eigene Werkzeugdatei anlegen und genaue Voraussetzungen festhalten.

**OP-1.6d: Abgleich mit [NEU-3]-Hypothesen  ❓ [O]**

---

## Gesamtstatus (aktualisiert 16. Juni 2026)

| Aussage | Status |
|---------|--------|
| Ω-basierte Reskalierung | ✗ überkorrigiert |
| log N-Skalierung (Pfade) | ✓ [M] |
| p_k: Kerninequation | ✗ Stern-Test [M] |
| q_k^♯: Kerninequation | ✗ Primschalen-Test [M] |
| r_k^♯: Normkontrolle k>1 | ✓ [M] |
| r_k^♯: mult. Stabilität (+2) | ✓ [M] |
| A_2D^r: Fréchet-*-Algebra (OP-1.5a) | ✓ [M] |
| Kanonische Normalform gcd=1, F∈P_{mn}B (OP-1.5b) | ✓ [M] |
| Dichte A_2D^r ↪ A_BC^{C*} (OP-1.6a) | ✓ [M] |
| Stetige Einbettung ‖F‖_{C*} ≤ C_k r_k^(2)(F) (OP-1.6b) | ✓ [M] |
| Mehrfachprodukt-Abschätzung (OP-1.6c) | ✓ [M] |
| Abgleich mit [NEU-3]-Hypothesen (OP-1.6d) | ❓ [O] |

## Verbindungen

- Voraussetzt: [NEU-2] (Fréchet), [NEU-3] (Schweitzer — Hypothesen noch zu präzisieren)
- Entwicklungssequenz (15.–16. Juni 2026):
  p_k → q_k^♯ → r_k^♯ → r_k^(2) → A_2D^r → Einbettung → Produktabschätzung
