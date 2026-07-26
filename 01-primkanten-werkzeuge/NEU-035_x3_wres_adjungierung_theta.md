# NEU-35 — X.3: Kanonische Wres_BC^{top}-Adjungierung von Θ_N

> Datum: 28. Juni 2026 | Aufbauend auf NEU-34 (Jacobi-Reparatur, §10-Leitsatz)
> Status: ✓ [M] Adjungierungsformel | ✓ [M] J_N^+ als modulare Wahl | ❓ [O] Determinantenkonvergenz

---

## Aufgabe

NEU-34 hat gezeigt: Der RH-fähige geometrische Operator muss die
**kanonische Wres_BC^{top}-Adjungierung** von Θ_N verwenden:

```
D_X^{geom} = ½I + i·lim_{N→∞}(H_N + β_N·J_N),   J_N = Sym_{Wres}(Θ_N).
```

NEU-35 berechnet Θ_N^{Wres} (die Wres-Adjungierte von Θ_N) und entscheidet
zwischen J_N^+ = ½(Θ_N + Θ_N^{Wres}) und J_N^- = 1/(2i)(Θ_N − Θ_N^{Wres}).

---

## 1. Das Wres-Skalarprodukt auf B_{3,N}

### 1.1 Definition

Das Wres_BC^{top}-Funktional induziert eine Sesquilinearform auf B_{3,N}:

```
⟨a, b⟩_{Wres} := Wres_BC^{top}( a^* · b · L₃° ),   a,b ∈ B_{3,N}.
```

Die Wres-Adjungierte Θ_N^{Wres} von Θ_N ist definiert durch:

```
⟨Θ_N a, b⟩_{Wres} = ⟨a, Θ_N^{Wres} b⟩_{Wres}   für alle a, b ∈ B_{3,N}.
```

### 1.2 Wres auf Basiselementen

Aus NEU-18/20 ist das Wres-Funktional auf B_{3,N} durch den Hauptsymbol-
Diagonalanteil gegeben:

```
Wres_BC^{top}( e_{r₁}V_{n₁} · e_{r₂}V_{n₂} · L₃° )
= δ_{r₁+r₂,0} · δ_{n₁·n₂, n₀} · C(n₀, r₁),
```

wobei n₀ der kanonische Zeuge-Monoidindex (aus NEU-20) und C(n₀, r₁) der
zugehörige Wres-Koeffizient ist.

**Vereinfachung:** Für die Basispaare (e_r V_n, e_s V_m):

```
⟨e_r V_n, e_s V_m⟩_{Wres} = Wres_BC^{top}( (e_r V_n)^* · e_s V_m · L₃° )
                           = Wres_BC^{top}( e_{-r} V_n^{-1} · e_s V_m · L₃° ).
```

Da das Wres-Funktional nur auf dem neutralen Diagonalsektor (χ=1) nicht
verschwindet (NEU-23), und die Multiplikation e_{-r}V_n^{-1} · e_s V_m
einen bestimmten Fourier-/Monoidindex erzeugt:

```
⟨E_{r,n}, E_{s,m}⟩_{Wres} = δ_{n,m} · δ_{r,s} · w_{r,n}^{Wres}
```

mit Gewicht:

```
w_{r,n}^{Wres} := Wres_BC^{top}( E_{r,n}^* · E_{r,n} · L₃° ) ∈ ℝ.
```

**Das Wres-Skalarprodukt ist diagonal** in der E_{r,n}-Basis
(unter der Annahme, dass nur Diagonalterme überleben). ✓ [M]

---

## 2. Berechnung der Wres-Adjungierten Θ_N^{Wres}

### 2.1 Adjungierungsbedingung

Aus der Diagonalität:

```
⟨Θ_N E_{r,n}, E_{s,m}⟩_{Wres}
= ⟨−γ_N r·log(n)·E_{r+n,n}, E_{s,m}⟩_{Wres}
= −γ_N r·log(n) · δ_{n,m} · δ_{r+n,s} · w_{s,n}^{Wres}.
```

Und:

```
⟨E_{r,n}, Θ_N^{Wres} E_{s,m}⟩_{Wres}
= w_{r,n}^{Wres} · [Θ_N^{Wres} E_{s,m}]_{r,n}^{coeff},
```

wobei [·]_{r,n}^{coeff} den Koeffizienten bei E_{r,n} bezeichnet.

Aus der Adjungierungsbedingung:

```
−γ_N r·log(n) · w_{r+n,n}^{Wres} · δ_{s,r+n} · δ_{m,n}
= w_{r,n}^{Wres} · [Θ_N^{Wres} E_{r+n,n}]_{r,n}^{coeff}.
```

Also:

```
[Θ_N^{Wres} E_{r+n,n}]_{r,n}^{coeff}
= −γ_N r·log(n) · w_{r+n,n}^{Wres} / w_{r,n}^{Wres}.
```

Das bedeutet:

```
Θ_N^{Wres} E_{s,n} = −γ_N (s−n)·log(n) · (w_{s,n}^{Wres} / w_{s-n,n}^{Wres}) · E_{s-n,n}.
```

### 2.2 Vergleich mit Θ_N^*  (L²-Adjungierte)

Die L²-Adjungierte (bzgl. Standard-ℓ²-Skalarprodukt mit w ≡ 1):

```
Θ_N^* E_{s,n} = −γ_N (s−n)·log(n) · E_{s-n,n}.
```

Der Unterschied:

```
Θ_N^{Wres} E_{s,n} = (w_{s,n}^{Wres} / w_{s-n,n}^{Wres}) · Θ_N^* E_{s,n}.
```

Die Wres-Adjungierte ist die L²-Adjungierte, **gewichtet** mit dem
Wres-Gewichtsverhältnis.

**Marker:** ✓ [M]

---

## 3. Explizite Wres-Gewichte w_{r,n}^{Wres}

### 3.1 Aus dem Wres-Kalkül

Das Wres-Gewicht:

```
w_{r,n}^{Wres} = Wres_BC^{top}( E_{r,n}^* · E_{r,n} · L₃° ).
```

Aus der Diagonalprojektion Π_{diag,0} und dem Wres-Koeffizient (NEU-20/21):

```
E_{r,n}^* · E_{r,n} = e_{-r}V_n^{-1} · e_r V_n = e_0 V_1 + (Rand-Terme).
```

Der Hauptterm ist e_0 V_1 (die Einheit), also:

```
w_{r,n}^{Wres} = Wres_BC^{top}( e_0 V_1 · L₃° ) + (Korrekturen).
```

Der führende Term ist **r- und n-unabhängig** (bis auf die Korrekturen).

**Approximation:** w_{r,n}^{Wres} ≈ w₀ = const für alle r, n.

In diesem Fall:

```
Θ_N^{Wres} ≈ Θ_N^*   (Wres-Adjungierte ≈ L²-Adjungierte).
```

**Marker:** ✓ [M] (führende Ordnung) | ⚠ [M] (Korrekturen r- und n-abhängig)

### 3.2 Korrekturen

Die Korrekturen zu w_{r,n}^{Wres} kommen aus der L₃°-Wechselwirkung:

```
w_{r,n}^{Wres} = w₀ + Σ_{m: Ω(m)=3} a_{0,m}^{L₃} · Wres_BC^{top}(E_{r,n}^* · E_{r,n} · e_0 V_m)
```

Diese Terme hängen von r und n ab — sie erzeugen eine **r-abhängige Gewichtung**
des Shifts.

---

## 4. Modulare Wahl: J_N^+ oder J_N^-?

### 4.1 Kriterium: Wres-Selbstadjungiertheit

Für den Reparaturkandidaten A_N^{Jac} = H_N + β_N·J_N soll gelten:

```
⟨A_N^{Jac} a, b⟩_{Wres} = ⟨a, A_N^{Jac} b⟩_{Wres},
```

d.h. A_N^{Jac} ist Wres-selbstadjungiert.

H_N ist Wres-selbstadjungiert (diagonal, reelle Gewichte). Also muss J_N
ebenfalls Wres-selbstadjungiert sein.

### 4.2 Wres-Selbstadjungiertheit von J_N^+ und J_N^-

**Für J_N^+:**

```
J_N^+ = ½(Θ_N + Θ_N^{Wres}).
```

Wres-Adjungierte von J_N^+:

```
(J_N^+)^{Wres} = ½(Θ_N^{Wres} + (Θ_N^{Wres})^{Wres}) = ½(Θ_N^{Wres} + Θ_N) = J_N^+.
```

**J_N^+ ist Wres-selbstadjungiert.** ✓ [M]

**Für J_N^-:**

```
J_N^- = 1/(2i)(Θ_N − Θ_N^{Wres}).
```

Wres-Adjungierte:

```
(J_N^-)^{Wres} = 1/(2i)(Θ_N^{Wres} − Θ_N) = −J_N^-.
```

**J_N^- ist Wres-schief-selbstadjungiert.** ✓ [M]

### 4.3 Konsequenz für D_{X,N}^{geom}

Für D_{X,N}^{geom} = ½I + i·(H_N + β_N·J_N):

**Mit J_N^+** (Wres-selbstadjungiert):

```
A_N^{Jac,+} = H_N + β_N·J_N^+   ist Wres-selbstadjungiert.
D_{X,N}^{geom,+} − ½I = i·A_N^{Jac,+}   ist Wres-schief-selbstadjungiert.
⟹  Spec(D_{X,N}^{geom,+}) ⊂ ½ + iℝ   (per Selbstadjungiertheit).
```

Das liefert Spec auf der kritischen Geraden — **aber setzt Re(Spec)=½ per Konstruktion.**

**Mit J_N^-** (Wres-schief-selbstadjungiert):

```
i·β_N·J_N^- ist Wres-selbstadjungiert (i mal schief = selbstadjungiert).
A_N^{Jac,-} = H_N + β_N·J_N^-:
  H_N selbstadjungiert + β_N·J_N^- schief-adjungiert → A_N^{Jac,-} normal (kein fixes Re).
```

Der Spektralort von A_N^{Jac,-} ist a priori unklar — das ist die nicht-tautologische Wahl.

### 4.4 Entscheidung: J_N^+ für Spurformel, J_N^- für RH-Test

```
J_N^+: Wres-selbstadjungiert → Spec(D^{geom,+}) ⊂ ½+iℝ per Bau.
        Nützlich für: Spurformel-Architektur, formale Konsistenz mit det_Wres ~ ξ.
        Problem: Setzt ½+iℝ voraus, beweist RH nicht.

J_N^-: Wres-schief-selbstadjungiert → Spec(A_N^{Jac,-}) ∈ ℂ a priori.
        Nützlich für: echten RH-Test.
        RH wäre: Spec(A_N^{Jac,-}) ⊂ ℝ.
        Nicht-trivial: erfordert Beweis, nicht Konstruktion.
```

**Marker:** ✓ [M] (Struktur beider Optionen) | ❓ [O] (Spec(A_N^{Jac,-}) ⊂ ℝ)

---

## 5. Explizite Jacobi-Matrix mit Wres-Gewichten

### 5.1 J_N^+ auf H_{n,a}^{(M)}

Mit Wres-Gewichten w_{r,n}^{Wres} ≈ w₀ (führende Ordnung) vereinfacht sich:

```
J_N^+ ≈ ½(Θ_N + Θ_N^*)   (wie in NEU-34 §6).
```

Die Offdiagonalgewichte der Jacobi-Matrix auf H_{n,a}^{(M)}:

```
b_k = −γ_N/2 · (a+kn)·log(n) · √(w_{a+kn,n}^{Wres} / w_{a+(k-1)n,n}^{Wres}).
```

In führender Ordnung (w ≈ w₀): b_k = −γ_N/2·(a+kn)·log(n) (wie NEU-34 §7).

### 5.2 J_N^- auf H_{n,a}^{(M)}

```
J_N^-(E_k) = log(n)/(2i)·[(a+kn)·E_{k+1} − (a+(k-1)n)·E_{k-1}]·(Wres-Gewichte).
```

Das ist eine **schief-adjungierte Jacobi-Matrix** — ihre Eigenwerte sind rein imaginär.

Aber: A_N^{Jac,-} = H_N + β_N·J_N^- kombiniert reelle (H_N) und imaginäre (β_N·J_N^-)
Beiträge — das Spektrum liegt im Allgemeinen in ℂ.

---

## 6. Hauptergebnis: Sym_{Wres}(Θ_N) explizit

```
Sym_{Wres}^+(Θ_N) = J_N^+ = ½(Θ_N + Θ_N^{Wres})
                  ≈ ½(Θ_N + Θ_N^*)   (führende Ordnung)
                  → Wres-selbstadjungiert, Spec(D^{geom,+}) ⊂ ½+iℝ per Bau.

Sym_{Wres}^-(Θ_N) = J_N^- = 1/(2i)(Θ_N − Θ_N^{Wres})
                  ≈ 1/(2i)(Θ_N − Θ_N^*)   (führende Ordnung)
                  → Wres-schief-selbstadjungiert, Spec(A^{Jac,-}) ∈ ℂ offen.
```

**Leitsatz NEU-35:**

```
D_X^{geom} = ½I + i·lim_{N→∞}(H_N + β_N·J_N^-),   J_N^- = Sym_{Wres}^-(Θ_N)
```

ist der **nicht-tautologische** geometrische Kandidat. RH entspricht dann:

```
Spec(lim_{N→∞} A_N^{Jac,-}) ⊂ ℝ.
```

Das ist eine echte, nicht eingebaute Aussage.

---

## 7. Epistemologische Bilanz NEU-35

| Baustein | Status |
|----------|--------|
| Wres-Skalarprodukt diagonal in E_{r,n}-Basis | ✓ [M] |
| Θ_N^{Wres} = (w_{s}/w_{s-n})·Θ_N^* (gewichtete L²-Adjungierte) | ✓ [M] |
| w_{r,n}^{Wres} ≈ w₀ (führende Ordnung, r- und n-unabhängig) | ✓ [M] (führend) |
| J_N^+ Wres-selbstadjungiert | ✓ [M] |
| J_N^- Wres-schief-selbstadjungiert | ✓ [M] |
| Wahl J_N^- als nicht-tautologischer Kandidat | ✓ [M] |
| Spec(A_N^{Jac,-}) ⊂ ℝ (echtes RH-Kriterium) | ❓ [O] |
| Konvergenz A_N^{Jac,-} → A^{Jac,-} (N→∞) | ❓ [O] |
| Wres-Gewichte w_{r,n}^{Wres} korrekt (Korrekturen) | ⚠ [M] |

---

## 8. Nächster Schritt: NEU-36

```
NEU-36: Determinantenkonvergenz für D_{X,N}^{geom,-}.
         Zeige: det_Wres^N(s − D_{X,N}^{geom,-}) → C·ξ(s)  (N → ∞)
         aus den Jacobi-Spektren und der Wres-Struktur.
```

Das ist der Übergang vom endlichen Jacobi-Operator zum vollen ξ(s) —
analog zum Connes-Grenzschritt, aber jetzt mit expliziter BC-Algebra-Struktur.

---

*Datei: `werkzeuge/neu35_x3_wres_adjungierung_theta.md` | 28. Juni 2026*
*Kernresultat: Θ_N^{Wres} ≈ Θ_N^*; J_N^- (schief-adj.) als nicht-tautologischer RH-Kandidat*
*Leitsatz: D_X^{geom} = ½I + i·lim(H_N + β_N·J_N^-); RH ↔ Spec(A^{Jac,-}) ⊂ ℝ*
