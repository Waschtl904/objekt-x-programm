# NEU-33 — X.3: BC-Konstruktion der endlichen Approximanten D_{X,N}^{BC}

> Datum: 28. Juni 2026 | Aufbauend auf NEU-32 (Connes-Kompass, Checkliste C1–C4)
> Status: ✓ [M] Konstruktion (C1)+(C3) | ❓ [O] Selbstadjungiertheit (C2), Konvergenz (C4)

---

## Aufgabe

NEU-32 hat die Checkliste (C1)–(C4) für die endlichen Approximanten gestellt.
NEU-33 liefert die explizite Konstruktion und trägt die ersten Checkboxen ab.

---

## 1. Konstruktion von D_{X,N}^{BC} — (C1)

### 1.1 Zwei Bausteine aus der BC-Struktur

Der Kandidat für D_{X,N}^{BC} kombiniert zwei natürliche Operatoren aus
(B_{3,N}, [ω̃₂], [L₃^N], Wres_BC^{top}):

**Baustein 1 — Modularer KMS-Generator H_N:**

Die KMS-Zeitentwicklung σ_t^{β=1} (formaler Grenzwert) erzeugt einen
selbstadjungierten Generator auf B_{3,N}:

```
H_N(e_r V_n) := log(n) · e_r V_n.
```

Das ist der Multiplikationsoperator mit log(n) (Monoidgewicht-Operator),
eingeschränkt auf B_{3,N}.

**Eigenschaften:**

- H_N ist selbstadjungiert bzgl. des KMS-Skalarprodukts ⟨a,b⟩_φ = φ_1(a*b).
- Spec(H_N) = { log(n) : Ω(n)=3, alle Primteiler ≤ N } ⊂ ℝ_{≥0}.
- H_N kodiert die **Primzahllogarithmen** der trunkierten Theorie.

**Baustein 2 — L₃-Kopplungsterm K_N:**

Das Element L₃^N ∈ B_{3,N} (Projektion der Hochschild-Klasse) definiert
einen Kopplungsoperator über die Wres-Paarung:

```
K_N : B_{3,N} → B_{3,N},   K_N(a) := L₃^N · a − a · L₃^N
    = [L₃^N, a]_{Hochschild}.
```

K_N ist der Kommutator mit L₃^N — er misst die **Nicht-Kommutativität**
der L₃-Klasse mit dem Algebra-Element a.

**Eigenschaften:**

- K_N ist schief-selbstadjungiert: K_N* = −K_N (Kommutator eines
  selbstadjungierten Elements ist schief-selbstadjungiert, wenn L₃^N
  selbstadjungiert, d.h. (L₃^N)* = L₃^N).
- K_N kodiert die **ω̃₂-Krümmungsinformation** über die Hochschild-Klasse.

### 1.2 Definition D_{X,N}^{BC}

```
D_{X,N}^{BC} := ½·I + i·(H_N + α_N · K_N),
```

wobei α_N ∈ ℝ ein Kopplungsparameter ist (zu bestimmen in §2).

**Struktur:**

- Der Realteil ½·I setzt Re(Spec) = ½ per Konstruktion.
- Der Imaginärteil i·(H_N + α_N·K_N) soll selbstadjungiert sein, damit
  D_{X,N}^{BC} − ½·I schief-selbstadjungiert ist.
- H_N + α_N·K_N ist selbstadjungiert, wenn H_N selbstadjungiert und K_N
  schief-selbstadjungiert — und α_N ∈ iℝ (imaginär).

**Korrektur:** Für reelles Spektrum von H_N + α_N·K_N muss:

```
α_N ∈ ℝ   und   H_N selbstadjungiert + α_N·K_N schief-adjungiert.
```

Dann ist H_N + α_N·K_N weder selbst- noch schief-adjungiert, sondern
**normal** (Kombination eines selbstadjungierten und eines schief-adjungierten
Operators, die kommutieren oder im Normalitätssinn verträglich sind).

**Revisierte Definition:**

```
A_N := H_N + α_N · K_N   (normal auf B_{3,N})
D_{X,N}^{BC} := ½·I + i·A_N.
```

Dann: D_{X,N}^{BC} − ½·I = i·A_N schief-selbstadjungiert ⟺ A_N selbstadjungiert.

A_N ist selbstadjungiert, wenn α_N ∈ iℝ (imaginärer Kopplungsparameter)
und [H_N, K_N] = 0 (Kommutativität der Bausteine).

**Marker:** ✓ [M] Konstruktion formal | ❓ [O] Selbstadjungiertheit von A_N

---

## 2. Selbstadjungiertheit von A_N — (C2)

### 2.1 Bedingung [H_N, K_N] = 0

Berechne den Kommutator auf Basiselementen:

```
[H_N, K_N](e_r V_n)
= H_N(K_N(e_r V_n)) − K_N(H_N(e_r V_n))
= H_N([L₃^N, e_r V_n]) − [L₃^N, H_N(e_r V_n)]
= H_N([L₃^N, e_r V_n]) − [L₃^N, log(n)·e_r V_n]
= H_N([L₃^N, e_r V_n]) − log(n)·[L₃^N, e_r V_n].
```

Also:

```
[H_N, K_N](e_r V_n) = (H_N − log(n)·I)([L₃^N, e_r V_n]).
```

Das verschwindet, wenn H_N([L₃^N, e_r V_n]) = log(n)·[L₃^N, e_r V_n],
d.h. wenn [L₃^N, e_r V_n] im log(n)-Eigenraum von H_N liegt.

**Explizit:** [L₃^N, e_r V_n] = L₃^N · e_r V_n − e_r V_n · L₃^N.

L₃^N = Σ_{m: Ω(m)=3, p|m⟹p≤N} a_{0,m} · e_0 V_m.

Also:

```
L₃^N · e_r V_n = Σ_m a_{0,m} · (e_0 V_m)(e_r V_n)
               = Σ_m a_{0,m} · e_{r} V_{mn}   (Multiplikationsregel).

e_r V_n · L₃^N = Σ_m a_{0,m} · (e_r V_n)(e_0 V_m)
               = Σ_m a_{0,m} · e_r V_{nm}   (gleich, da V_n V_m = V_{nm}).
```

Also [L₃^N, e_r V_n] = 0 — der Kommutator verschwindet!

**Folgerung:**

```
K_N = [L₃^N, ·] = 0   auf B_{3,N}.
```

**Das ist ein Problem:** K_N = 0 bedeutet, dass der L₃-Kopplungsterm
keinen Beitrag liefert.

### 2.2 Ursache und Korrektur

Der Kommutator [L₃^N, e_r V_n] = 0 weil L₃^N und e_r V_n bzgl. V-Multiplikation
kommutieren (V_m V_n = V_{mn} = V_n V_m im abelschen Teil N×).

**Korrektur:** Der Kopplungsterm muss aus der **nicht-kommutativen** Struktur
von B₃ kommen — also aus dem Hochschild-Rand ∂ oder aus der ω̃₂-Klasse,
nicht dem simplen Kommutator.

**Revidierter Kopplungsterm:**

Nutze den ω̃₂-Krümmungsoperator Θ aus NEU-27 §3.1:

```
Θ(e_r V_n) = r·log(n) · e_{r+n} V_n.
```

Θ ist nicht durch den einfachen Kommutator gegeben, sondern durch die
**Hochschild-Kozykel-Wirkung** von ω̃₂. Θ ist nicht schief-selbstadjungiert
(reelles Spektrum, NEU-27 §3.2).

**Definition (revidiert):**

```
A_N := H_N + i·β_N · Θ_N,   β_N ∈ ℝ,
D_{X,N}^{BC} := ½·I + i·(H_N + i·β_N · Θ_N)
             = ½·I + i·H_N − β_N · Θ_N.
```

Für Selbstadjungiertheit von A_N = H_N + i·β_N·Θ_N:

- H_N selbstadjungiert ✓
- i·β_N·Θ_N: Θ_N selbstadjungiert → i·β_N·Θ_N schief-adjungiert → nicht selbstadjungiert.

**Ergebnis:** A_N ist nicht selbstadjungiert mit diesem Ansatz.

### 2.3 Normalitäts-Kompromiss

Statt Selbstadjungiertheit fordere **Normalität** von A_N:

```
[A_N, A_N*] = 0.
```

A_N = H_N + i·β_N·Θ_N mit A_N* = H_N − i·β_N·Θ_N (da H_N, Θ_N selbstadjungiert).

```
[A_N, A_N*] = [H_N + iβ_NΘ_N, H_N − iβ_NΘ_N]
            = −iβ_N[H_N,Θ_N] + iβ_N[Θ_N,H_N]
            = −2iβ_N[H_N,Θ_N].
```

A_N ist normal ⟺ [H_N, Θ_N] = 0.

**Berechnung [H_N, Θ_N]:**

```
H_N(Θ_N(e_r V_n)) = H_N(r·log(n)·e_{r+n}V_n)
                   = r·log(n)·log(n)·e_{r+n}V_n
                   = r·log(n)²·e_{r+n}V_n.

Θ_N(H_N(e_r V_n)) = Θ_N(log(n)·e_r V_n)
                   = log(n)·r·log(n)·e_{r+n}V_n
                   = r·log(n)²·e_{r+n}V_n.
```

Also: [H_N, Θ_N] = 0. ✓

**A_N = H_N + i·β_N·Θ_N ist normal.** ✓ [M]

### 2.4 Spektrum von A_N

Da A_N normal mit H_N = log(n)·id und Θ_N = r·log(n)·e_{r+n}V_n:

Auf dem Basiselement e_r V_n (mit Ω(n) = 3, p|n ⟹ p ≤ N):

```
A_N(e_r V_n) = H_N(e_r V_n) + i·β_N·Θ_N(e_r V_n)
             = log(n)·e_r V_n + i·β_N·r·log(n)·e_{r+n}V_n.
```

Das ist **nicht** diagonal in der e_r V_n-Basis (Θ_N verschiebt den
Fourier-Index r → r+n). A_N ist also kein Multiplikationsoperator —
seine Spektraltheorie ist nicht trivial.

**Marker:** ✓ [M] (Normalität) | ❓ [O] (Spektrum von A_N und seine Lage bzgl. ½+iℝ)

---

## 3. Determinantenberechnung — (C3)

### 3.1 Aus λ_mod^N

Aus NEU-32 §2.2:

```
λ_mod^N(s) = C_L^N / ζ_N(s).
```

Analog zu NEU-31 §2.2:

```
H_X^N(s) := Tr_Wres^{top}( (s − D_{X,N}^{BC})^{-1} · (L₃^N)° ) = (ξ_N'/ξ_N)(s).
```

Dann:

```
det_Wres^N(s − D_{X,N}^{BC}) = C_N · ξ_N(s).   ✓ [M] formal
```

Das gilt relativ zur Identifikation H_X^N = ξ_N'/ξ_N (die aus der
trunkierten Version von NEU-28 folgt).

---

## 4. Konvergenzfrage — (C4)

### 4.1 Das Problem

```
det_Wres^N(s − D_{X,N}^{BC}) = C_N · ξ_N(s)
```

für festes N gesichert. Für N → ∞:

```
ξ_N(s) → ξ(s)   (lokal gleichmäßig auf {Re(s) > 1}, dann meromorph auf ℂ).
```

Das gilt für die ξ_N-Funktionen selbst (da das Eulerprodukt konvergiert).

Die Frage ist: Konvergiert auch D_{X,N}^{BC} → D_X^{geom} in einem
geeigneten Operatortopologie, so dass:

```
det_Wres^N(s − D_{X,N}^{BC}) → det_Wres(s − D_X^{geom}) = C · ξ(s)?
```

### 4.2 Analogie zu Connes

Connes' A_N konvergieren (schwach oder stark auf geeignetem Hilbertraum)
gegen einen Grenzoperator A_∞ — aber der Beweis der spektralen Konvergenz
(Spec(A_N) → Spec(A_∞) = Nullstellen von ξ) ist offen.

Für unser D_{X,N}^{BC}: Die Operatoren H_N und Θ_N wachsen mit N
(immer mehr Primzahlen beitragen). Eine natürliche Operatornorm-Konvergenz
ist unklar.

**Marker:** ❓ [O]

---

## 5. Epistemologische Bilanz NEU-33

| Baustein | Status |
|----------|--------|
| D_{X,N}^{BC} = ½I + i(H_N + iβ_N·Θ_N) explizit konstruiert | ✓ [M] |
| [H_N, Θ_N] = 0 → A_N normal | ✓ [M] |
| K_N = [L₃^N, ·] = 0 (Abelizität von N×) | ✓ [M] (Diagnose) |
| det_Wres^N(s − D_{X,N}^{BC}) = C_N·ξ_N(s) formal | ✓ [M] |
| Selbstadjungiertheit von A_N (für Spec ⊂ ½+iℝ) | ❓ [O] |
| Spektrum von A_N explizit (Θ_N nicht diagonal) | ❓ [O] |
| Konvergenz D_{X,N}^{BC} → D_X^{geom} (N → ∞) | ❓ [O] |
| Positive Hilbertisierung auf B_{3,N} | ❓ [O] |

### Wichtige Diagnose

Der naive Kopplungsterm K_N = [L₃^N, ·] = 0 wegen der Abelizität von N×.
Die nicht-kommutative Struktur von B₃ sitzt in der Fourier-Richtung (e_r-Faktor),
nicht in der Monoid-Richtung (V_n-Faktor). Der Krümmungsoperator Θ_N
(via ω̃₂) greift die Fourier-Richtung — das ist der richtige Kopplungsterm.

---

## 6. Nächste Schritte

```
NEU-34: Spektrum von A_N = H_N + iβ_N·Θ_N auf B_{3,N}.
         A_N normal → Spektralzerlegung via Normaloperator-Theorie.
         Bedingung Spec(A_N) ⊂ ℝ (für D_{X,N}^{BC}−½I schief-selbstadjungiert).

NEU-35: Konvergenzmechanismus für D_{X,N}^{BC} → D_X^{geom}.
         Analogie zu Connes: schwache Operatorkonvergenz auf dem GNS-Raum.
```

---

*Datei: `werkzeuge/neu33_x3_bc_approximanten.md` | 28. Juni 2026*
*Kernresultat: D_{X,N}^{BC} = ½I + i(H_N+iβ_N·Θ_N) normal; K_N=0 (Diagnose)*
*Offener Kern: Selbstadjungiertheit von A_N und Konvergenz N→∞*
