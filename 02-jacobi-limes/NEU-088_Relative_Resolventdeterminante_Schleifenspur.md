# NEU-88 — Relative Resolventdeterminante und zweite Schleifenspur

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-87 (Jacobi-Schließung; erste Spur quadratisch in \(\Lambda\); rohe Det divergiert)  
**Nächste Nummer:** NEU-89

---

## Ausgangspunkt

Aus NEU-87:
- \(B_N^{\Lambda} = J_N^{\Lambda} + (J_N^{\Lambda})^*\) bricht die Nilpotenz.
- Rohe Spur \(\operatorname{Tr}((B_N^{\Lambda})^2) \asymp M_N^3 \log N / N \to \infty\).

Die Determinante muss daher relativ zu einem Diagonaloperator gebildet werden.

---

## Äquivalenz der beiden Formen

Setze \(A_N^{\Lambda} := H_N + B_N^{\Lambda}\) und \(R_N(z) := (H_N - z)^{-1}\).

Für invertierbares \(H_N - z\):

$$
(A_N^{\Lambda} - z)(H_N - z)^{-1} = I + B_N^{\Lambda} R_N(z).
$$

Also:

$$
\boxed{\det\bigl((A_N^{\Lambda}-z)(H_N-z)^{-1}\bigr) = \det\bigl(I + B_N^{\Lambda} R_N(z)\bigr).}
$$

**Option A und Option B aus NEU-87 sind formal äquivalent. Status: \(\checkmark[M]\)**

---

## Log-Determinanten-Expansion

Definiere

$$
D_N(z) := \det\bigl(I + B_N^{\Lambda} R_N(z)\bigr).
$$

Formal:

$$
\log D_N(z) = \sum_{k \geq 1} \frac{(-1)^{k+1}}{k} \operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^k\bigr).
$$

Da \(B_N^{\Lambda}\) keine Diagonale hat (nur Off-Diagonaleinträge) und \(R_N(z)\) diagonal ist:

$$
\operatorname{Tr}(B_N^{\Lambda} R_N(z)) = 0.
$$

**Erster Term verschwindet. Status: \(\checkmark[M]\)**

---

## Satz NEU-88.1 — Zweite relative Schleifenspur

Schreibe \(H_N \delta_r = h_r \delta_r\). Die symmetrischen Matrixelemente sind

$$
B_{r+n,\, r} = B_{r,\, r+n} = \frac{\gamma r}{N}\Lambda(n).
$$

Dann:

$$
\boxed{
\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr)
= \frac{2\gamma^2}{N^2}
\sum_{r \leq M_N} r^2
\sum_{n \leq N-r}
\frac{\Lambda(n)^2}{(h_r - z)(h_{r+n} - z)}.
}
$$

**Status: \(\checkmark[M]\)**

---

## Resolventdämpfung und Kontrolle

Nimmt man \(h_r \asymp r\) (natürliche Diagonalskala), so gilt für \(z\) außerhalb des Spektrums:

$$
(h_r - z)(h_{r+n} - z) \asymp r(r+n).
$$

Der Hauptsummand wird zu

$$
\frac{r^2 \Lambda(n)^2}{N^2 \cdot r(r+n)} = \frac{r}{N^2(r+n)}\Lambda(n)^2.
$$

Mit

$$
\sum_{n \leq N} \frac{\Lambda(n)^2}{r+n} = O((\log N)^2)
$$

folgt

$$
\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr)
= O\!\left(\frac{M_N^2 (\log N)^2}{N^2}\right).
$$

### Skalenvergleich

| Skala \(M_N\) | Rohe Spur \(\operatorname{Tr}((B_N^{\Lambda})^2)\) | Rel. Spur \(\operatorname{Tr}((BR)^2)\) |
|---|---|---|
| \(N/\log N\) | \(\asymp N^2/(\log N)^2 \to \infty\) | \(O(1)\) |
| \(\sqrt{N/\log N}\) | \(\asymp \sqrt{N/\log N} \to \infty\) | \(O(1/N)\) |

**Der Resolvent \((H_N-z)^{-1}\) dämpft genau die Zeilennorm-Barriere aus NEU-84.**  
**Status: \(\warning[M]\)** (abhängig von \(h_r \asymp r\))

---

## Positives Fazit

$$
\boxed{\text{Der Resolvent }(H_N-z)^{-1}\text{ kann genau die Zeilennorm-Barriere aus NEU-84 dämpfen.}}
$$

Damit ist die relative Determinante \(D_N(z)\) der erste Kandidat, der gleichzeitig
- Mangoldt-Gewichtung,
- pathwise Jacobi-Stabilität (\(M_N = N/\log N\)),
- nichttriviale endliche Schleifenmasse

vereinbaren kann. **Status: \(\checkmark/\warning[M]\)**

---

## Warnung: Quadratische Schleifenarithmetik

Die zweite relative Spur ist weiterhin quadratisch in \(\Lambda\):

$$
\Lambda(n)^2.
$$

Der Anschluss an die Weil-Quadratform bleibt plausibel (Weil-Quadratformen sind ebenfalls quadratisch), aber nicht automatisch bewiesen. Die explizite Formel müsste über quadratische Schleifen-/Resolventterme rekonstruiert werden.

**Status: \(\warning[M]\)**

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Option A \(\equiv\) Option B (solange \(H_N - z\) invertierbar) | \(\checkmark[M]\) |
| (B) | Erster relativer Spurterm \(\operatorname{Tr}(B_N^{\Lambda} R_N(z)) = 0\) | \(\checkmark[M]\) |
| (C) | Zweite Spur: explizite Formel (Satz NEU-88.1) | \(\checkmark[M]\) |
| (D) | Bei \(h_r \asymp r\): zweite Spur \(O(1)\) auf \(M_N = N/\log N\) | \(\warning[M]\) |
| (E) | Höhere Schleifen \(\operatorname{Tr}((BR)^k)\), \(k \geq 3\), bleiben offen | \(?[O]\) |

---

## Nächster Schritt: NEU-89

NEU-89 muss die höheren relativen Schleifen

$$
\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^k\bigr), \qquad k \geq 3,
$$

kontrollieren und klären:
- Konvergiert die vollständige Log-Determinantenreihe auf \(M_N = N/\log N\)?
- Hat \(D_N(z) = \det(I + B_N^{\Lambda} R_N(z))\) einen nichttrivialen Grenzwert?
- Wie schließt dieser Grenzwert an \(Z_N^{\text{completed}} \to C \cdot \xi\) (NEU-65) an?

---

## Verweise

- NEU-87: Jacobi-Schließung; erste Spur
- NEU-84: Zeilennorm-Barriere; Orbit-Skalen
- NEU-65: \(Z_N^{\text{completed}} \to C \cdot \xi\)
- NEU-63D: \(m_{\text{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- Weil: *Sur les formules explicites* (Quadratformstruktur)
- Reed & Simon IV, \S XIII.17 (Fredholm-Determinanten)
- Simon: *Trace Ideals*, AMS 2005, \S 9
