# NEU-90 — Auswertung der zweiten relativen Schleifenspur und z-Rigidität

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-89 (höhere Schleifen verschwinden; log D_N(z) ~ -(1/2)Tr((BR)²))  
**Nächste Nummer:** NEU-91

---

## Ausgangspunkt

Aus NEU-89:

$$
\log D_N(z) = -\frac{1}{2}T_N(z) + o(1),
$$

mit

$$
T_N(z) := \operatorname{Tr}\bigl((B_N^{\Lambda} R_N(z))^2\bigr)
= \frac{2\gamma^2}{N^2}\sum_{r \leq M_N} r^2 \sum_{n \leq N-r}
\frac{\Lambda(n)^2}{(h_r-z)(h_{r+n}-z)}.
$$

**Modellannahme:** \(h_r = r\) (natürliche Diagonalskala). Allgemeiner \(h_r \sim c r\) liefert nur Skalierungsfaktor \(c^{-2}\).

---

## Satz NEU-90.1 — Hauptgrenzwert

Für \(h_r = r\), festes \(z\) außerhalb des Spektrums:

$$
(h_r - z)(h_{r+n} - z) = r(r+n)\left(1 + O_z\!\left(\tfrac{1}{r}\right)\right).
$$

Daher wird der Hauptsummand

$$
\frac{r^2}{r(r+n)}\Lambda(n)^2 = \frac{r}{r+n}\Lambda(n)^2.
$$

Mit \(\sum_{n \leq N}\Lambda(n)^2 \sim N\log N\) folgt durch partielle Summation gleichmäßig für \(r \leq N/\log N\):

$$
\sum_{n \leq N-r} \frac{\Lambda(n)^2}{r+n} \sim \frac{1}{2}(\log N)^2.
$$

Mit \(\sum_{r \leq N/\log N} r \sim \frac{1}{2} N^2/(\log N)^2\) ergibt sich:

$$
T_N(z) \sim \frac{2\gamma^2}{N^2} \cdot \frac{1}{2}\frac{N^2}{(\log N)^2} \cdot \frac{1}{2}(\log N)^2.
$$

$$
\boxed{T_N(z) \to \frac{\gamma^2}{2}.}
$$

**Status: ⚠[M]** (abhängig von PNT-Quadratabschätzung für \(\Lambda^2\))

---

## Satz NEU-90.2 — z-Rigidität

Der Grenzwert \(\gamma^2/2\) ist **unabhängig von \(z\)**.

Die \(z\)-abhängigen Korrekturen entstehen aus der Entwicklung

$$
\frac{1}{(r-z)(r+n-z)} = \frac{1}{r(r+n)}\left[1 + z\!\left(\frac{1}{r}+\frac{1}{r+n}\right) + O_z\!\left(\frac{1}{r^2}\right)\right].
$$

Der lineare \(z\)-Beitrag ist von der Größenordnung

$$
O\!\left(\frac{\log N}{N}\right) \to 0.
$$

$$
\boxed{T_N(z) = \frac{\gamma^2}{2} + o(1) \quad \text{für festes } z \notin \operatorname{Spec}(H_N).}
$$

**Status: ⚠[M]**

---

## Konsequenz: Konstante relative Determinante

Aus NEU-89 und Satz NEU-90.1–2:

$$
\log D_N(z) \to -\frac{\gamma^2}{4},
$$

also

$$
\boxed{D_N(z) \to \exp\!\left(-\frac{\gamma^2}{4}\right).}
$$

Der Grenzwert ist **endlich und nichttrivial als Konstante, aber trivial als Funktion von \(z\)**.

**Status: ✓/⚠[M]**

---

## No-Go: Direkter ξ-Anschluss blockiert

$$
\boxed{\text{Die Konstruktion findet eine stabile quadratische Mangoldt-Masse, aber noch keine }\xi\text{-Funktion.}}
$$

Ein Grenzwert \(D_N(z) \to e^{-\gamma^2/4}\) kann keine Nullstellenstruktur der Zetafunktion kodieren: \(C \cdot \xi(z)\) ist eine ganze Funktion mit nichttrivialer Nullstellenstruktur, während \(e^{-\gamma^2/4}\) eine nullstellenfreie Konstante ist.

**Status: ✗/⚠[M]**

---

## Mögliche Auswege für NEU-91

### Weg A — Zentrierte Determinante

Ziehe den konstanten Hauptterm ab:

$$
\widetilde{\log D}_N(z) := \log D_N(z) + \frac{\gamma^2}{4}.
$$

Prüfe, ob eine nachskalierte Größe \(c_N \cdot \widetilde{\log D}_N(z)\) einen nichttrivialen \(z\)-abhängigen Grenzwert besitzt.  
**Status: ❓[O]**

### Weg B — Spektral skalierendes \(z = z_N\)

Statt festem \(z\) lasse \(z\) mit \(N\) auf der Diagonalskala von \(h_r\) skalieren. Dann wirkt der Resolvent nicht mehr als asymptotisch konstante Dämpfung.  
**Status: ❓[O]**

### Weg C — Andere Diagonalskala \(h_r\)

Falls \(h_r\) nicht linear, sondern logarithmisch oder kritisch skaliert ist, kann die \(z\)-Abhängigkeit im Hauptterm überleben. Erfordert neue Begründung für die Wahl von \(H_N\).  
**Status: ❓[O]**

### Weg D — Weil-Quadratform statt ξ-Determinante

Der konstante quadratische Grenzwert ist schlecht für eine direkte \(\xi\)-Identifikation, aber nicht automatisch schlecht für eine Weil-Positivitätsstruktur. Das richtige Zielobjekt könnte eine Quadratform sein, nicht eine ganze Funktion mit Nullstellen.  
**Status: ⚠[M]**

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Hauptgrenzwert \(T_N(z) \to \gamma^2/2\) existiert | ⚠[M] |
| (B) | Grenzwert ist \(z\)-unabhängig | ⚠[M] |
| (C) | \(D_N(z) \to e^{-\gamma^2/4}\) (Konstante) | ⚠[M] |
| (D) | Direkter \(D_N(z) \to C\cdot\xi(z)\)-Anschluss blockiert | ✗/⚠[M] |
| (E) | Weg A–D für nichttriviale \(z\)-sensitive Fortsetzung | ❓[O] |

---

## Verweise

- NEU-88: Zweite relative Schleifenspur (explizite Formel)
- NEU-89: Asymptotische Quadratisierung; \(\|C_N\| \to 0\)
- NEU-65: \(Z_N^{\text{completed}} \to C \cdot \xi\)
- NEU-63D: \(m_{\text{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- Weil: *Sur les formules explicites* (Weil-Quadratform/Positivität)
- Apostol: *Analytic Number Theory* 1976 (PNT; \(\sum \Lambda(n)^2 \sim N\log N\))
