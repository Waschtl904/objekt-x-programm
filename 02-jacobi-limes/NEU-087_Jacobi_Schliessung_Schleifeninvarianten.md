# NEU-87 — Jacobi-Schließung und erste Schleifeninvarianten

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-86 (Nilpotenz-Barriere; Spur/Det trivial für reinen Vorwärtsshift)  
**Nächste Nummer:** NEU-88

---

## Ausgangspunkt

Aus NEU-86: \(J_N^{\Lambda}\) ist nilpotent, daher

$$
\operatorname{Tr}\bigl((J_N^{\Lambda})^k\bigr) = 0, \qquad \det(I + z J_N^{\Lambda}) = 1.
$$

Ein nichttrivialer Determinantenpfad verlangt eine Jacobi-Schließung.

---

## Definition: Jacobi-Abschluss

$$
B_N^{\Lambda} := J_N^{\Lambda} + (J_N^{\Lambda})^*.
$$

\(B_N^{\Lambda}\) ist selbstadjungiert auf \(\ell^2(I_N)\).
Der geschlossene Jacobi-Kandidat für NEU-88 lautet

$$
A_N^{\Lambda} := H_N + B_N^{\Lambda} = H_N + J_N^{\Lambda} + (J_N^{\Lambda})^*.
$$

---

## Matrixelemente

Mit Mangoldt-Gewichtung \(\lambda_{n,N} = \gamma\Lambda(n)/N\):

$$
\langle\delta_s, J_N^{\Lambda}\,\delta_r\rangle = \frac{\gamma r}{N}\Lambda(s-r) \cdot \mathbf{1}_{s>r,\, s-r \leq N-r}.
$$

Die symmetrisierten Matrixelemente:

$$
\langle\delta_s, B_N^{\Lambda}\,\delta_r\rangle
= \frac{\gamma\min(r,s)}{N}\Lambda(|s-r|) \cdot \mathbf{1}_{|s-r| \geq 2},
$$

mit Trunkierung durch \(I_N\). **Status: \(\checkmark[M]\)**

---

## Nilpotenz gebrochen: Rückwärts-Vorwärts-Schleifen

Während \(J_N^{\Lambda}\) nilpotent ist, erzeugt \(B_N^{\Lambda}\) Rückwärts-Vorwärts-Schleifen:

$$
\delta_r \xrightarrow{J_N^{\Lambda}} \delta_{r+n} \xrightarrow{(J_N^{\Lambda})^*} \delta_r.
$$

Diese Schleifen erzeugen nichttriviale Spurterme. **Status: \(\checkmark[M]\)**

---

## Satz NEU-87.1 — Erste nichttriviale Spur

Da \(J_N^{\Lambda}\) strikt oberdreieckig ist:

$$
\operatorname{Tr}(J_N^{\Lambda}) = 0, \quad
\operatorname{Tr}((J_N^{\Lambda})^2) = 0, \quad
\operatorname{Tr}(((J_N^{\Lambda})^*)^2) = 0.
$$

Daher:

$$
\operatorname{Tr}\bigl((B_N^{\Lambda})^2\bigr)
= \operatorname{Tr}(J_N^{\Lambda}(J_N^{\Lambda})^*) + \operatorname{Tr}((J_N^{\Lambda})^* J_N^{\Lambda})
= 2\|J_N^{\Lambda}\|_{HS}^2.
$$

Explizit:

$$
\boxed{
\operatorname{Tr}\bigl((B_N^{\Lambda})^2\bigr)
= \frac{2\gamma^2}{N^2}\sum_{r \leq M_N} r^2 \sum_{n \leq N-r} \Lambda(n)^2.
}
$$

**Der erste nichttriviale Invariant ist quadratisch in \(\Lambda(n)\), nicht linear.**  
**Status: \(\checkmark[M]\)**

---

## Asymptotische Größe

Mit \(\sum_{n \leq N}\Lambda(n)^2 \asymp N\log N\):

$$
\|J_N^{\Lambda}\|_{HS}^2 \asymp \frac{\gamma^2 M_N^3 \log N}{N}.
$$

| Skala | \(M_N\) | \(\operatorname{Tr}((B_N^{\Lambda})^2)\) |
|---|---|---|
| Pathwise Jacobi | \(N/\log N\) | \(\asymp \gamma^2 N^2/(\log N)^2 \to \infty\) |
| \(\ell^2\)-Operatorstabil | \(\sqrt{N/\log N}\) | \(\asymp \gamma^2 \sqrt{N/\log N} \to \infty\) |

**Die Spur divergiert auf beiden natürlichen Skalen ohne zusätzliche Normalisierung.**  
**Status: \(\warning[M]\)**

---

## Konsequenz für Determinanten

Für \(\det(I + z B_N^{\Lambda})\) beginnt die logarithmische Entwicklung mit

$$
\log\det(I + z B_N^{\Lambda})
= - \frac{z^2}{2}\operatorname{Tr}\bigl((B_N^{\Lambda})^2\bigr) + O(z^3),
$$

da \(\operatorname{Tr}(B_N^{\Lambda}) = 0\). Der erste nichttriviale Beitrag ist also **quadratisch in den Mangoldt-Gewichten**. **Status: \(\checkmark[M]\)**

---

## Schleifenarithmetik und höhere Terme

Die erste Spur sieht \(\Lambda(n)^2\), nicht \(\Lambda(n)\). In höheren Potenzen entstehen geschlossene Pfade:

$$
r \to r+n_1 \to r+n_1-n_2 \to \cdots \to r.
$$

Diese Schleifenarithmetik kann zum Weil-Bild passen (Weil-Quadratformen sind ebenfalls quadratisch), erzwingt aber, dass der Anschluss an die explizite Formel **nicht** über eine lineare Mangoldt-Summe erfolgt, sondern über Schleifen-Quadratformterme.

$$
\boxed{\text{NEU-87 macht die Arithmetik sichtbar, aber nur als Schleifenarithmetik.}}
$$

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(B_N^{\Lambda} = J_N^{\Lambda} + (J_N^{\Lambda})^*\) ist selbstadjungiert; bricht Nilpotenz | \(\checkmark[M]\) |
| (B) | Erste Spur: \(\operatorname{Tr}((B_N^{\Lambda})^2) = 2\|J_N^{\Lambda}\|_{HS}^2\) | \(\checkmark[M]\) |
| (C) | Term ist quadratisch in \(\Lambda(n)\) | \(\checkmark[M]\) |
| (D) | Spur divergiert auf pathwise- und \(\ell^2\)-Skala ohne Normierung | \(\warning[M]\) |
| (E) | NEU-88 muss relative/normalisierte Determinante verwenden | \(?[O]\) |

---

## Nächster Schritt: NEU-88

NEU-88 muss eine der folgenden normierten Formen verwenden:

**Option A — Relative Resolventdeterminante:**

$$
\det\!\left(I + B_N^{\Lambda}(H_N - z)^{-1}\right)
$$

**Option B — Schur-Feshbach-Determinante:**

$$
\det\!\left((A_N^{\Lambda} - z)(H_N - z)^{-1}\right)
$$

**Nicht geeignet:** rohe \(\det(I + z B_N^{\Lambda})\) wegen Divergenz der Spur.

---

## Verweise

- NEU-86: Nilpotenz-Barriere
- NEU-65: \(Z_N^{\text{completed}} \to C \cdot \xi\)
- NEU-37: skew/selfadjoint-Version des Shift-Operators
- Weil: *Sur les formules explicites de la théorie des nombres* (Quadratformstruktur)
- Reed & Simon IV, \S XIII.17 (Fredholm-Determinanten; relative Determinanten)
- Simon: *Trace Ideals*, AMS 2005 (\S 9: Hilbert-Schmidt; \S 3: Spur-Klasse)
