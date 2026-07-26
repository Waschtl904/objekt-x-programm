# NEU-89 — Höhere Schleifen und asymptotische Quadratisierung der relativen Determinante

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-88 (Relative Resolventdeterminante; zweite Spur \(O(1)\) auf \(M_N=N/\log N\))  
**Nächste Nummer:** NEU-90

---

## Ausgangspunkt

Aus NEU-88:

$$
D_N(z) = \det(I + B_N^{\Lambda} R_N(z)), \qquad R_N(z) = (H_N-z)^{-1}.
$$

$$
\log D_N(z) = \sum_{k \geq 1} \frac{(-1)^{k+1}}{k}\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^k\bigr).
$$

Erster Term: \(\operatorname{Tr}(B_N^{\Lambda} R_N(z)) = 0\). Erster nichttrivialer Term: \(k=2\), kontrolliert auf \(M_N = N/\log N\).

---

## Symmetrisierung

Setze (bei invertiblem \(R_N(z)\) mit positiv definitem \(-\operatorname{Im} z > 0\)):

$$
C_N(z) := R_N(z)^{1/2}\, B_N^{\Lambda}\, R_N(z)^{1/2}.
$$

Durch Zyklizität der Spur gilt

$$
\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^k\bigr) = \operatorname{Tr}\bigl(C_N(z)^k\bigr),
$$

und \(C_N(z)\) ist selbstadjungiert (symmetrisch). **Status: \(\checkmark[M]\)**

---

## Matrixelemente von \(C_N(z)\)

Für \(h_r \asymp r\), \(s = r+n\):

$$
(C_N(z))_{r,\, r+n}
\asymp \frac{\gamma}{N}\Lambda(n)\sqrt{\frac{r}{r+n}}.
$$

**Status: \(\checkmark/\warning[M]\)** (abhängig von \(h_r \asymp r\))

---

## Hilbert-Schmidt-Kontrolle

Aus NEU-88:

$$
\|C_N(z)\|_{HS}^2 = \operatorname{Tr}(C_N(z)^2) = O(1) \quad \text{auf } M_N = \frac{N}{\log N}.
$$

**Status: \(\checkmark[M]\)**

---

## Satz NEU-89.1 — Operatornorm-Kontrolle

Zeilensummen des symmetrisierten Operators:

$$
\sum_s |(C_N(z))_{r,s}|
\lesssim \frac{\sqrt{r}}{N}\sum_{n \leq N-r}\frac{\Lambda(n)}{\sqrt{r+n}}.
$$

Mit \(\sum_{n \leq N} \Lambda(n)/\sqrt{n} = O(\sqrt{N})\) folgt:

$$
\sum_s |(C_N(z))_{r,s}| \lesssim \sqrt{\frac{r}{N}}.
$$

Für \(r \leq M_N = N/\log N\) ergibt sich

$$
\sum_s |(C_N(z))_{r,s}| = O\!\left(\frac{1}{\sqrt{\log N}}\right).
$$

Durch den Schur-Test (Zeilen- und Spaltensummen symmetrisch):

$$
\boxed{\|C_N(z)\| = O\!\left(\frac{1}{\sqrt{\log N}}\right) \to 0.}
$$

**Status: \(\warning[M]\)** (hängt von gleichmäßigen Schur-Abschätzungen und \(h_r \asymp r\) ab)

---

## Satz NEU-89.2 — Höhere Schleifen verschwinden

Für jedes feste \(k \geq 3\):

$$
|\operatorname{Tr}(C_N(z)^k)|
\leq \|C_N(z)\|^{k-2}\|C_N(z)\|_{HS}^2
= O\!\left((\log N)^{-(k-2)/2}\right) \to 0.
$$

**Status: \(\checkmark/\warning[M]\)**

---

## Asymptotische Quadratisierung

Die Log-Determinante reduziert sich asymptotisch auf den zweiten Schleifenterm:

$$
\log D_N(z)
= -\frac{1}{2}\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr) + o(1).
$$

Also:

$$
\boxed{
D_N(z) \sim \exp\!\left(-\frac{1}{2}\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr)\right).
}
$$

**Die relative Determinante ist kontrollierbar, aber sie wird asymptotisch rein quadratisch.**  
**Status: \(\checkmark/\warning[M]\)**

---

## Strukturelle Einordnung

| Eigenschaft | Status |
|---|---|
| \(\|C_N\|_{HS}^2 = O(1)\) auf \(M_N=N/\log N\) | \(\checkmark[M]\) |
| \(\|C_N\| \to 0\) (Schur-Test) | \(\warning[M]\) |
| Höhere Schleifen \(\to 0\) für jedes feste \(k \geq 3\) | \(\checkmark/\warning[M]\) |
| Log-Det quadratisiert asymptotisch | \(\checkmark/\warning[M]\) |
| Grenzwert \(D_N(z)\) nichttrivial und \(z\)-sensitiv? | \(?[O]\) |
| Anschluss an Weil-Quadratform oder \(C \cdot \xi\) | \(?[O]\) |

---

## Warnung: Quadratische vs. Eulerprodukt-Struktur

Der Hauptterm sieht

$$
\Lambda(n)^2,
$$

nicht die lineare Mangoldt-Summe \(\Lambda(n)\). Das ist konsistent mit dem Weil-Bild (Quadratformstruktur), aber wahrscheinlich nicht ausreichend für einen direkten \(\xi\)-Anschluss über eine Eulerprodukt-Determinante.

---

## Nächster Schritt: NEU-90

NEU-90 muss den Hauptterm

$$
\operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr)
= \frac{2\gamma^2}{N^2}\sum_{r \leq M_N} r^2\sum_{n \leq N-r}
\frac{\Lambda(n)^2}{(h_r-z)(h_{r+n}-z)}
$$

auswerten und klären:

1. Besitzt dieser Ausdruck einen Grenzwert für \(N \to \infty\)?
2. Hängt der Grenzwert nichttrivial von \(z\) ab?
3. Kann dieser Grenzwert mit der Weil-Quadratform oder mit \(C \cdot \xi\) aus NEU-65 verbunden werden?

---

## Verweise

- NEU-88: Zweite relative Schleifenspur; Resolventdämpfung
- NEU-65: \(Z_N^{\text{completed}} \to C \cdot \xi\)
- NEU-63D: \(m_{\text{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- Weil: *Sur les formules explicites* (Quadratformstruktur)
- Reed & Simon IV, \S XIII.17 (Fredholm-Determinanten; Trace-Norm)
- Simon: *Trace Ideals*, AMS 2005, \S 9 (Schur-Test; HS-Norm)
