# NEU-83 — Mangoldt-Extraktion versus Jacobi-Stabilität: Dreifach-Konflikt

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-82 (Dichte-No-Go \(\kappa_N \asymp N\); Strategie I als Favorit)  
**Nächste Nummer:** NEU-84

---

## Ausgangspunkt

Aus NEU-82 (Strategie I):

$$
\Sigma_N = \{2,\ldots,N\}, \quad \kappa_N = N-1, \quad
\beta_{n,N} = \frac{\gamma}{(N-1)\log n}.
$$

Dies stabilisiert die Jacobi-Gewichte und den Feshbach-Gesamtbeitrag.  
Aber der stabilisierte Koeffizient ist

$$
\lambda_{n,N} := \beta_{n,N}\log n = \frac{\gamma}{N-1},
$$

d.h. **gleichgewichtet** über alle \(n\). Der \(\log n\)-Faktor aus \(\delta_{BC}\) wurde neutralisiert.

---

## Das Problem

Der effektiv wirkende Operator ist

$$
\frac{\gamma}{N-1}\sum_{n=2}^N V_n R,
$$

nicht Mangoldt-gewichtet. Eine Projektion auf Primpotenzen liefert

$$
\frac{\gamma}{N-1}\sum_{p^k \leq N} V_{p^k} R,
$$

aber Mangoldt verlangt

$$
\sum_{p^k \leq N} \log p \cdot V_{p^k} R.
$$

**Mangoldt-Extraktion und Jacobi-Stabilisierung kommutieren nicht automatisch.**

---

## Drei Extraktionsregime

### Fall A — Zählende Primsektor-Projektion

$$
\lambda_{n,N} = \frac{\gamma}{N-1}\mathbf{1}_{n=p^k}
$$

- Jacobi-Gewichte: \(|b_j(n)| = O(1)\) ✓
- Feshbach-Beitrag: \(\displaystyle\sum_{p^k \leq N} \frac{\gamma}{N-1} \sim \frac{\gamma}{\log N} \to 0\)

**Arithmetische Unterkopplung. Status: \(\warning[M]\)**

### Fall B — Echte Mangoldt-Gewichtung

$$
\lambda_{n,N} = \frac{\gamma}{N}\Lambda(n)
$$

- Feshbach-Beitrag: \(\displaystyle\sum_{n \leq N}\frac{\gamma}{N}\Lambda(n) \sim \gamma\) ✓  
  (da \(\sum_{n \leq N}\Lambda(n) \sim N\) nach dem Primzahlsatz)
- Jacobi-Gewichte: \(\displaystyle|b_j(n)| = \frac{\gamma}{2N}r\Lambda(n) \leq O(\log N)\)

**Arithmetisch korrekt, logarithmisch \(\ddot{u}\)berkoppelt. Status: \(\warning[M]\)**

### Fall C — Gedämpfte Mangoldt-Gewichtung

$$
\lambda_{n,N} = \frac{\gamma}{N\log N}\Lambda(n)
$$

- Jacobi-Gewichte: \(|b_j(n)| = O(1)\) ✓
- Feshbach-Beitrag: \(\displaystyle\sum_{n \leq N}\frac{\gamma}{N\log N}\Lambda(n) \sim \frac{\gamma}{\log N} \to 0\)

**Feshbach-Unterkopplung. Status: \(\warning[M]\)**

---

## Dreifach-Konflikt-Satz

**Satz NEU-83.1** (Dreifach-Konflikt)

Für den vollen Orbitbereich \(r \leq N\) sind die drei Forderungen

1. **Feshbach-Stabilität:** \(\sum_n \lambda_{n,N} \to \gamma > 0\)
2. **Jacobi-Gewichts-Stabilität:** \(\sup_n N \cdot \lambda_{n,N} = O(1)\)
3. **Mangoldt-Gewichtung:** \(\lambda_{n,N} \propto \Lambda(n)\)

**nicht gleichzeitig erfüllbar.**

*Beweis:* (3) fordert \(\lambda_{n,N} = c_N \Lambda(n)\). (2) fordert \(c_N \Lambda(n) \lesssim 1/N\) für alle \(n\), also \(c_N \lesssim 1/(N\log N)\). Dann \(\sum_n \lambda_{n,N} \leq c_N \sum_{n \leq N}\Lambda(n) \lesssim 1/\log N \to 0\) — Widerspruch zu (1). \(\square\)

$$
\boxed{\text{Feshbach} + \text{Jacobi-Stabilität} + \text{Mangoldt-Gewichtung sind auf }r \leq N\text{ nicht frei kompatibel.}}
$$

**Status: \(\checkmark[M]\)**

---

## Drei Auflösungswege

### Weg 1 — Logarithmisches Jacobi-Wachstum akzeptieren

Verwende Fall B: \(\lambda_{n,N} = \frac{\gamma}{N}\Lambda(n)\).  
Zeige, dass \(O(\log N)\)-Jacobi-Gewichte im späteren Jacobi-Limes kontrollierbar sind  
(Carleman-Kriterium, Hamburger-Momentenproblem).

**Status: \(?[O]\)**

### Weg 2 — Orbit-Trunkierung \(r \lesssim N/\log N\) (Favorit)

Beschränke den Orbitbereich auf

$$
r \lesssim \frac{N}{\log N}.
$$

Dann gilt mit \(\lambda_{n,N} = \frac{\gamma}{N}\Lambda(n)\):

$$
r \cdot \lambda_{n,N} \lesssim \frac{N}{\log N} \cdot \frac{\log N}{N} = O(1).
$$

Damit sind Feshbach-Stabilität, Mangoldt-Gewichtung und Jacobi-Gewichts-Stabilität  
**gleichzeitig erfüllbar** auf dem trunkierten Orbitfenster.

**Status: \(\warning[M]\) / Favorit für NEU-84**

### Weg 3 — Gewichtete Hilbertraumnorm

Verändere die \(\ell^2\)-Norm auf \(I_N\) durch ein Gewicht \(w_r\), das große \(r\)-Werte dämpft.  
Die Jacobi-Gewichte bleiben groß, aber der Operator wird auf dem gewichteten Raum beschränkt.

**Status: \(?[O]\)**

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Strategie I (\(\beta_{n,N} \propto 1/\log n\)): Feshbach + Jacobi stabil, Mangoldt neutralisiert | \(\checkmark[M]\) |
| (B) | Fall B (\(\lambda_{n,N} = \gamma\Lambda(n)/N\)): Feshbach + Mangoldt, \(O(\log N)\)-Jacobi | \(\warning[M]\) |
| (C) | Fall C (gedämpft): Jacobi stabil, Feshbach unterkoppelt | \(\warning[M]\) |
| (D) | Satz NEU-83.1: Dreifach-Konflikt auf \(r \leq N\) bewiesen | \(\checkmark[M]\) |
| (E) | Weg 2 (Orbit-Trunkierung \(r \lesssim N/\log N\)): alle drei Forderungen kompatibel | \(\warning[M]\) / Favorit |
| (F) | Weg 1 (Carleman-Kontrolle) und Weg 3 (gew. Norm) | \(?[O]\) |

---

## Nächster Schritt

NEU-84 sollte Weg 2 prüfen:

$$
\boxed{\text{NEU-84 — Mangoldt-kompatible Orbit-Trunkierung } r \leq N/\log N.}
$$

Zentrale Frage: Wie verändert die Orbit-Trunkierung den Hilbertraum \(\ell^2(I_N)\),  
und bleibt die Feshbach-Kette (NEU-77–79) unter dieser Trunkierung gültig?

---

## Verweise

- NEU-82: Dichte-No-Go \(\kappa_N \asymp N\)
- NEU-67/68: \(\Lambda = \mu * \log\); Primsektor-Projektion; \(1/k\)-Mechanismus
- NEU-73: \(J_N^- = \sum_n \log(n) V_n R\)
- Apostol, Kap. 4 (Primzahlsatz, \(\sum_{n \leq N}\Lambda(n) \sim N\))
- Reed & Simon II, \S X.2 (Jacobi-Operatoren; Carleman-Kriterium)
- Akhiezer (Hamburger-Momentenproblem; unbeschränkte Jacobi-Gewichte)
