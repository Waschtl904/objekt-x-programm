# NEU-86 — Nilpotenz-Barriere für Spur und Determinante

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-85 (Starker Null-Limes; wandernde arithmetische Fenster)  
**Nächste Nummer:** NEU-87

---

## Ausgangspunkt

Aus NEU-85 liegt der Mangoldt-gewichtete Vorwärtsoperator

$$
J_N^{\Lambda}\delta_r
= \frac{\gamma r}{N}\sum_{n \leq N-r}\Lambda(n)\,\delta_{r+n}
$$

auf dem endlichen Raum \(\ell^2(I_N)\), \(I_N = \{1,\ldots,N\}\), vor.

---

## Satz NEU-86.1 — Nilpotenz

Für jedes \(n \geq 2\) gilt \(r + n > r\). Damit erhöht jeder Summand in \(J_N^{\Lambda}\delta_r\) den Index.
Bezüglich der natürlichen Ordnung auf \(I_N\) ist \(J_N^{\Lambda}\) **strikt oberdreieckig**.

$$
\boxed{(J_N^{\Lambda})^N = 0.}
$$

**Status: \(\checkmark[M]\)**

---

## Konsequenz für Spuren

Da alle Eigenwerte von \(J_N^{\Lambda}\) gleich \(0\) sind:

$$
\operatorname{Tr}\bigl((J_N^{\Lambda})^k\bigr) = 0 \quad (k \geq 1).
$$

Für analytische \(f\) mit \(f(z) = \sum_{k \geq 0} c_k z^k\):

$$
\operatorname{Tr}(f(J_N^{\Lambda})) = |I_N| \cdot f(0).
$$

Die naive Spur \(\operatorname{Tr}(f(J_N^{\Lambda}))\) trägt **keine nichttriviale arithmetische Information**.

**Status: \(\checkmark[M]\) (NEU-86b trivial)**

---

## Konsequenz für Determinanten

Da alle Eigenwerte \(= 0\):

$$
\det(I + z J_N^{\Lambda}) = 1.
$$

Ebenso:

$$
\det\!\left(I + z \frac{J_N^{\Lambda}}{\kappa_N}\right) = 1.
$$

Die naive Feshbach-Determinante des isolierten Vorwärtsoperators ist **trivial**.

**Status: \(\checkmark[M]\) (NEU-86c in reiner Form trivial)**

---

## Notwendige Erweiterung: Jacobi-Schließung

Ein nichttrivialer Spur- oder Determinantenpfad **muss** mindestens eine der folgenden Erweiterungen verwenden:

### Option 1 — Jacobi-Abschluss

$$
A_N^{\Lambda} = H_N + J_N^{\Lambda} + (J_N^{\Lambda})^*
$$

bzw. die skew/selfadjoint-Version aus NEU-37. Dann ist \(A_N^{\Lambda}\) selbstadjungiert und hat nichttriviales Spektrum.

### Option 2 — Relative Determinante

$$
\det\!\left(I + (J_N^{\Lambda} + (J_N^{\Lambda})^*)(H_N - z)^{-1}\right)
$$

bzw.

$$
\det\!\left((H_N + J_N^{\Lambda} - z)(H_N - z)^{-1}\right).
$$

Hier erzeugt die Diagonalresolvente \((H_N - z)^{-1}\) Rückkopplungsschleifen, die die Nilpotenz brechen.

### Option 3 — Schur-Komplement-Operator

Der echte Feshbach-Schur-Komplement-Operator (nicht der isolierte Kollaps-Shift) kann eine nichttriviale Determinantenstruktur tragen.

**Status für alle drei Optionen: \(?[O]\)**

---

## Natuerlicher Kandidat fuer NEU-65-Anschluss

Der engste Anschluss an \(Z_N^{\text{completed}} \to C \cdot \xi\) (NEU-65) ist:

$$
\boxed{
\det\!\left(I + \bigl(J_N^{\Lambda} + (J_N^{\Lambda})^*\bigr)(H_N - z)^{-1}\right)
}
$$

oder die zugehörige Feshbach-Schur-Determinante.

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(J_N^{\Lambda}\) ist strikt oberdreieckig, also nilpotent | \(\checkmark[M]\) |
| (B) | Naive Spuren \(\operatorname{Tr}((J_N^{\Lambda})^k) = 0\) | \(\checkmark[M]\) |
| (C) | Naive Determinante \(\det(I + z J_N^{\Lambda}/\kappa_N) = 1\) | \(\checkmark[M]\) |
| (D) | NEU-86b und NEU-86c in reiner Vorwärtsform trivial | \(\checkmark[M]\) |
| (E) | Nichttrivialer Pfad verlangt Jacobi-Abschluss oder relative Feshbach-Determinante | \(?[O]\) |

---

## Konsequenz für den kritischen Pfad

```
NEU-86  Nilpotenz-Barriere:
        (J_N^Lambda)^N = 0; det(I+z J_N^Lambda/kappa_N) = 1   CHECKMARK[M]

NEU-87  Jacobi-Schliessung:
        A_N^Lambda = H_N + J_N^Lambda + (J_N^Lambda)^*
        oder skew-Version aus NEU-37                           NAECHSTER SCHRITT

NEU-88  Relative Determinante:
        det(I + (J_N^Lambda+(J_N^Lambda)^*)(H_N-z)^{-1})       Kandidat zu NEU-65
```

---

## Verweise

- NEU-85: Starker Null-Limes; wandernde arithmetische Fenster
- NEU-65: \(Z_N^{\text{completed}} \to C \cdot \xi\)
- NEU-37: skew/selfadjoint-Version des Shift-Operators
- NEU-77–79: Algebraische Feshbach-Kollapsidentität
- Reed & Simon IV, \S XIII.17 (relative Determinanten; Fredholm-Determinanten)
- Simon: *Trace Ideals*, AMS 2005
