# NEU-81 — Feshbach-Skalierung vs. Jacobi-Gewichts-Stabilität

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-80 (\(\beta_N\) frei; neue Normierungsbedingung \(\beta_N \kappa_N \to \gamma\))  
**Nächste Nummer:** NEU-82

---

## Ausgangspunkt

Aus NEU-80 liegt vor:

$$
b_j = \frac{\beta_N}{2}(a + jn)\log n \qquad (\gamma_N = 1, \text{ NEU-62})
$$

Kandidat F aus NEU-80:

$$
\beta_N := \frac{\gamma}{\kappa_N}
$$

Einsetzen liefert:

$$
\boxed{b_j = \frac{\gamma}{2\kappa_N}(a+jn)\log n}
$$

---

## Zwei verschiedene Stabilitätsforderungen

### (F) Feshbach-Stabilität

$$
\beta_N \kappa_N \to \gamma \in (0,\infty)
\quad\Longleftrightarrow\quad
\beta_N \sim \frac{\gamma}{\kappa_N}
$$

Diese Bedingung sichert, dass der normierte Feshbach-Kollaps eine endliche,
nichttriviale Kopplungsstärke hat. **Status: \(\checkmark[M]\) (Kandidat F)**

### (J) Jacobi-Gewichts-Stabilität

$$
\beta_N \cdot \sup_{\substack{n \in \Sigma_N \\ r+n \leq N}} r \log n = O(1)
$$

Diese Bedingung sichert, dass die Offdiagonal-Gewichte \(b_j\) der Jacobi-Matrix
beschränkt bleiben (notwendig für gutartigen Jacobi-Limes).

Typischerweise gilt:

$$
\sup_{\substack{n \leq N \\ r+n \leq N}} r \log n \sim N \log N
$$

Damit fordert (J):

$$
\beta_N \lesssim \frac{1}{N \log N}
$$

---

## Echter Normierungskonflikt

Die beiden Bedingungen sind **nicht kompatibel** für dieselbe Wahl von \(\beta_N\):

| Bedingung | Forderung an \(\beta_N\) | Skalenverhalten |
|---|---|---|
| (F) Feshbach-Stabilität | \(\beta_N \sim \gamma/\kappa_N\) | \(\sim 1/N\) oder \(\sim \log N/N\) |
| (J) Jacobi-Gewichts-Stabilität | \(\beta_N \lesssim 1/(N\log N)\) | \(\sim 1/(N\log N)\) |

### Konsequenzen der Kollision

**Kandidat F (\(\beta_N = \gamma/\kappa_N\)):**
- \(\checkmark\) stabilisiert normierten Feshbach-Kollaps
- \(\warning\) Jacobi-Gewichte \(b_j \sim \frac{\gamma}{2\kappa_N} r \log n\) können wachsen

**Kandidat J (\(\beta_N \sim 1/(N\log N)\)):**
- \(\checkmark\) stabilisiert Jacobi-Gewichte \(b_j = O(1)\)
- \(\warning\) Feshbach-Koppling: \(\beta_N \kappa_N \sim 1/\log N \to 0\) (Unterkopplung, Fall 2)

---

## Detailanalyse je nach Labelmenge

### Volle Labelmenge \(\Sigma_N = \{1,\ldots,N\}\), \(\kappa_N = N\)

$$
b_j = \frac{\gamma}{2N}(a+jn)\log n
$$

- Für festes \(n\): \(b_j \sim \frac{\gamma}{2} \cdot \frac{r}{N} \cdot \log n\) — stabil (\(r/N \leq 1\))
- Für wachsendes \(n\) bis \(N\): \(b_j \sim \frac{\gamma}{2} \cdot \frac{r}{N} \cdot \log N\) — \(O(\log N)\)-Wachstum

**Status:** Schwaches Wachstum; möglicherweise durch Jacobi-Limes absorbierbar. \(\warning[M]\)

### Primlabel \(\Sigma_N = \{p \leq N\}\), \(\kappa_N \sim N/\log N\)

$$
b_j = \frac{\gamma \log N}{2N}(a+jn)\log p
$$

- Für festes \(p\): \(b_j \sim O(\log N)\)
- Für \(p\) wachsend bis \(N\): \(b_j \sim O((\log N)^2)\)

**Status:** Logarithmisches bis quadratisch-logarithmisches Wachstum. \(\warning[M]\)/\(?[O]\)

### Primpotenzen

Asymptotisch dominieren die Primzahlen; Wachstum wie Primlabel.

---

## Auflösungsoptionen

### Option \(\alpha\): Unbeschränkte Jacobi-Gewichte akzeptieren

Wenn \(b_j \sim O(\log N)\) toleriert wird (unbeschränkter Jacobi-Operator),  
muss die Selbstadjungiertheitsfrage für unbeschränkte Jacobi-Operatoren gesondert
behandelt werden (Carleman-Kriterium, Hamburger-Momentenproblem).

**Status: \(?[O]\)**

### Option \(\beta\): Modifizierter \(\beta_N\)

Ersetzt man

$$
\beta_N := \frac{\gamma}{\kappa_N \log N}
$$

für volle Labelmenge (oder \(\beta_N \sim \frac{\gamma}{N}\) für Primlabel), dann:
- Jacobi-Gewichte: \(b_j = O(1)\) für \(r \leq N\), \(n \leq N/\log N\)
- Feshbach-Kopplung: \(\beta_N \kappa_N = \gamma/\log N \to 0\) (schwache Unterkopplung)

**Status: Kompromiss, kein klarer Gewinner. \(\warning[M]\)**

### Option \(\gamma\): Orbitabhängige Normierung

Statt eines globalen \(\beta_N\) wird eine **kanalabhängige** Normierung

$$
\beta_{n,N} := \frac{\gamma}{\kappa_N \log n}
$$

eingesetzt. Dann:

$$
b_j = \frac{\gamma}{2\kappa_N}(a+jn)
$$

ohne \(\log n\)-Faktor in den Gewichten. Feshbach-Kopplung:

$$
\sum_{n \in \Sigma_N} \beta_{n,N} \log n = \frac{\gamma}{\kappa_N} \sum_{n \in \Sigma_N} 1 = \gamma.
$$

**Status: Vielversprechendste Option. \(\warning[M]\)/\(?[O]\)**

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(b_j = \frac{\gamma}{2\kappa_N}(a+jn)\log n\) bei \(\beta_N = \gamma/\kappa_N\) | \(\checkmark[M]\) |
| (B) | Feshbach-Stabilität (F) und Jacobi-Gewichts-Stabilität (J) sind nicht identisch | \(\checkmark[M]\) |
| (C) | Konflikt: Kandidat F erfüllt (J) nicht; Kandidat J unterkoppelt Feshbach | \(\checkmark[M]\) |
| (D) | Volle Labelmenge: \(b_j = O(\log N)\) (schwaches Wachstum) | \(\warning[M]\) |
| (E) | Primlabel: \(b_j = O((\log N)^2)\) (stärkeres Wachstum) | \(\warning[M]\)/\(?[O]\) |
| (F) | Option \(\gamma\) (kanalabh. \(\beta_{n,N} = \gamma/(\kappa_N \log n)\)): \(b_j = O(1)\) und \(\sum \beta_{n,N} \log n = \gamma\) | \(\warning[M]\) |

---

## Konsequenz für den kritischen Pfad

NEU-81 macht sichtbar:

> **Feshbach-Stabilität \(\neq\) Jacobi-Gewichts-Stabilität.**

Die Entscheidung zwischen den Optionen (\(\alpha\), \(\beta\), \(\gamma\)) ist  
der nächste echte mathematische Knoten, bevor \(\beta_N\) als Konvention committet werden kann.

Option \(\gamma\) (kanalabhängige Normierung) ist der vielversprechendste Kandidat,  
weil sie gleichzeitig \(b_j = O(1)\) und \(\sum_n \beta_{n,N} \log n = \gamma\) erfüllt.

---

## Verweise

- NEU-37 (in teil2): Jacobi-Gewichte \(b_j = \frac{\beta_N \gamma_N}{2}(a+jn)\log n\)
- NEU-62: \(\gamma_N \equiv 1\)
- NEU-80: \(\beta_N\) frei; Normierungsbedingung \(\beta_N \kappa_N \to \gamma\)
- Reed & Simon II, §X.2: Jacobi-Operatoren; Carleman-Kriterium
- Akhiezer: *The Classical Moment Problem*, Kap. 2 (unbeschränkte Jacobi-Gewichte)
