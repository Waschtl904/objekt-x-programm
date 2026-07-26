# NEU-66 — Geschlossene Divisorpfade und Trace-/Feshbach-Expansion

**Status:** Tr(A_N)=0 ✓[M]; Tr(A_N^2) explizit ⚠[M]; Bipartit ≠ r-Gradierung ✗[M] korrigiert  
**Datum:** 2026-06-29 (Korrektur: log(p^k) ≠ Λ(p^k) für k>1; Bipartit-Bedingung präzisiert)  
**Aufbaut auf:** NEU-65 (Spur = geschlossene Pfade), NEU-64 (Log-Derivat-Rahmen)

---

## Zentralfrage

```
Tr(A_N^k) = welche arithmetische geschlossene-Pfad-Summe?
```

Entscheidender Test:

```
Erzeugen die geschlossenen Pfade Primorbit-Gewichte log(p)
oder nur Divisorenergie log^2(n) mit log(p^k) = k·log(p) ≠ Λ(p^k)?
```

---

## Korrektur 1: log(p^k) ≠ Λ(p^k) für k > 1 ✗[M]

**Fehler in früherer Fassung:** Die Aussage

```
n = p^k  =>  log(n) = Λ(n)    [FALSCH für k > 1]
```

ist falsch. Korrekt:

```
log(p^k) = k·log(p)
Λ(p^k)   =   log(p)      [unabhängig von k]
```

Also:

```
log^2(p^k) = k^2·log^2(p)
Λ(p^k)^2   =      log^2(p)    [nur k=1: gleich]
```

Der Übergang log(n) ~> Λ(n) ist für k > 1 **nicht durch Selektion auf Primzahlpotenzen
allein** gelöst. Die natürlichen Operatorgewichte log(n) liefern

```
Tr(A_N^2) = Σ_{a,n|m} r^2 log^2(n)
           = Σ_{a, n=p^k|m} r^2 k^2 log^2(p)  +  Σ_{zusammengesetzt n|m} r^2 log^2(n)
```

Die Mangoldt-Gewichtung Λ(n) würde stattdessen k^2 -> 1 erfordern (Primitive-Orbit-
Reduktion). Das ist der **neue Kernmechanismus** -> NEU-67. ✗[M] (korrigiert)

---

## Korrektur 2: r-Gradierung ≠ Bipartit ✗[M]

**Früherer Fehler:** "Falls der Divisorgraph r-graduiert ist, folgt Tr(A_N^{2j+1}) = 0."

**Korrekt:** A_N^{Jac,-} ist selbstadjungiert, enthält also **Rückkanten** r+n -> r.
Der relevante Graph ist symmetrisiert (ungerichtet). Dann können Dreieckszyklen
existieren, sobald n_1 + n_2 = n_3 für Divisoren n_1, n_2, n_3 | m.

**Beispiele für Dreieckszyklen:**

```
S = {2, 4}: Zyklus 0 -> 2 -> 4 -> 0  (weil 2+2=4)  => NICHT bipartit
S = {2, 3, 5}: Zyklus 0 -> 2 -> 5 -> 0  (weil 2+3=5)  => NICHT bipartit
S = {2}: Zyklus 0 -> 2 -> 0 nur (Hin-Rück)  => bipartit
```

**Bipartit-Kriterium (präzise):** Der Divisorgraph auf Z mit Schrittmenge
S_m = {n ≥ 2 : n | m} ist bipartit genau dann, wenn keine ungerade Relation

```
±n_1 ± n_2 ± ... ± n_{2q+1} = 0    mit n_i ∈ S_m
```

existiert. Nach Division durch g = gcd(S_m): alle n/g müssen ungerade sein.

**Konsequenz:** Bipartitheit ist eine echte arithmetische Bedingung
an die Divisorschrittmenge, nicht automatisch aus r-Gradierung. ✗[M] (korrigiert)

---

## Satz NEU-66.1 — Tr(A_N) = 0 ✓[M]

Tr(A_N^{Jac,-}) = 0, da A_N rein off-diagonal (keine Diagonalbeiträge). ✓[M]

---

## Satz NEU-66.2 — Tr(A_N^2): symmetrisierte Hin-und-zurück-Summe ⚠[M]

```
Tr(A_N^2) = Σ_{a,b} |Θ_{ba}|^2 = Σ_{a=(p,m,r,u), n|m, n≥2} r^2 log^2(n)
```

Das sind Hin-und-zurück-Pfade im symmetrisierten Graphen. Die Gewichte log^2(n)
enthäften für n = p^k den Faktor k^2 log^2(p), nicht Λ(n)^2 = log^2(p). ⚠[M]

---

## Satz NEU-66.3 — Tr(A_N^3): Dreieckszyklen ⚠[M]

Ein Dreieckszyklus a_0 -> a_1 -> a_2 -> a_0 erfordert Schritte n_1, n_2, n_3 ∈ S_m mit

```
n_1 - n_3 = 0  und  n_2 = n_3 - n_1    [im symmetrisierten Fall]
```

bzw. allgemeiner: n_1 + n_2 = n_3 (Vorwärtsdreieck) oder ±-Kombinationen.

**Nicht automatisch null.** Tr(A_N^3) = 0 nur falls der symmetrisierte
Divisorgraph bipartit ist (arithmetische Bedingung an S_m). ⚠[M]

---

## Lemma 66.1 — Bipartit-Konsistenz mit Nullstellensymmetrie ⚠[M]

Falls der Divisorgraph bipartit ist:
```
Spec(A_N) = -Spec(A_N)    (Spektrum symmetrisch zu 0)
```

Das wäre konsistent mit {+γ_ρ, -γ_ρ} als Nullstellenpaar
(Funktionalgleichung ζ(ρ) = ζ(1-ρ̄)). ⚠[M]

Aber Bipartitheit ist **nicht automatisch** — sie muss für die
relevanten m-Sektoren geprüft werden. ⚠[M]

---

## Korrigierter Status

| Aussage | Status |
|---|---|
| Tr(A_N) = 0 | ✓[M] |
| Tr(A_N^2) = Σ r^2 log^2(n) | ✓[M] |
| log^2(p^k) = Λ(p^k)^2 für k > 1 | ✗[M] FALSCH |
| Ungerade Spuren = 0 wegen r-Gradierung | ✗[M] FALSCH (nur bei bipartitem symm. Graphen) |
| Bipartit-Kriterium: arithmetische Bedingung an S_m | ✓[M] |
| Bipartit konsistent mit γ ↔ -γ | ⚠[M] |
| Primorbit-/Mangoldt-Struktur (log(p^k) -> log(p)) | ❓[O] -> NEU-67 |

---

## Neue Hauptaufgabe

Die nächste Kernfrage ist nicht Bipartitheit, sondern:

```
Wie wird aus Divisorpfad-Gewicht log(n) = k·log(p)  [für n = p^k]
die primitive Mangoldt-Gewichtung Λ(n) = log(p)?
```

Drei mögliche Mechanismen (-> NEU-67):

| Mechanismus | Idee | Status |
|---|---|---|
| Primitive-Cycle Reduction | Wiederholungen p^k -> primitiver Orbit p | ❓[O] |
| Möbius-Inversion | μ-gewichtete Subtraktion zusammengesetzter Divisoren | ❓[O] |
| Feshbach-Projektion | relativer Determinant sieht nur primitive Sektoren | ❓[O] |

---

## Literatur

- Connes, A.: Selecta Math. 5 (1999) (geschlossene Orbits, Spurformel)
- Berry & Keating: SIAM Review 41 (1999) (Primorbits, Wiederholungen)
- Apostol, T.: *Introduction to Analytic Number Theory* (Λ vs. log, Möbius)
- Biggs, N.: *Algebraic Graph Theory*, Kap. 2 (Bipartit-Kriterien, Cayley-Graphen)
- Simon, B.: *Trace Ideals*, AMS 2005, Kap. 3
