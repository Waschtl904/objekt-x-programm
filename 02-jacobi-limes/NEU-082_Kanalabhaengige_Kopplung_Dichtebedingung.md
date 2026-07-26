# NEU-82 — Kanalabhängige Kopplung und Dichtebedingung der Labelmenge

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-81 (Konflikt Feshbach- vs. Jacobi-Stabilität)  
**Nächste Nummer:** NEU-83

---

## Ausgangspunkt

Aus NEU-81 liegt der Normierungskonflikt vor:

- **(F) Feshbach-Stabilität:** \(\beta_N \kappa_N \to \gamma\)
- **(J) Jacobi-Gewichts-Stabilität:** \(\beta_N \lesssim 1/(N \log N)\)

Natürlicher Auflösungsversuch: kanalabhängige Kopplung

$$
\beta_{n,N} := \frac{\gamma}{\kappa_N \log n}, \qquad n \in \Sigma_N \setminus \{1\}.
$$

**Hinweis:** \(n=1\) wird aus \(\Sigma_N\) ausgeschlossen (\(\log 1 = 0\), trivialer Nullkanal).

---

## Feshbach-Prüfung

Setze \(\lambda_{n,N} := \beta_{n,N} \log n\). Dann gilt

$$
\lambda_{n,N} = \frac{\gamma}{\kappa_N}.
$$

Somit

$$
\sum_{n \in \Sigma_N} \lambda_{n,N} = \sum_{n \in \Sigma_N} \frac{\gamma}{\kappa_N} = \gamma.
$$

Die kanalabhängige Kopplung stabilisiert den Feshbach-Gesamtbeitrag **exakt**.  
**Status: \(\checkmark[M]\)**

---

## Jacobi-Gewichte

Mit \(\gamma_N = 1\) (NEU-62) werden die Jacobi-Offdiagonalgewichte

$$
b_j(n) = \frac{\beta_{n,N}}{2}(a+jn)\log n = \frac{\gamma}{2\kappa_N}(a+jn).
$$

Für \(a + jn \leq N\) folgt

$$
|b_j(n)| \leq \frac{\gamma N}{2\kappa_N}.
$$

Jacobi-Gewichts-Stabilität \(b_j = O(1)\) ist daher äquivalent zur **Dichtebedingung**

$$
\boxed{\frac{N}{\kappa_N} = O(1), \quad \text{d.h. } \kappa_N \asymp N.}
$$

**Status: \(\checkmark[M]\)**

---

## Konsequenzen nach Labelmenge

| Labelmenge \(\Sigma_N\) | \(\kappa_N\) | \(|b_j(n)|\) | Status |
|---|---|---|---|
| \(\{2,\ldots,N\}\) (voll) | \(N-1 \asymp N\) | \(O(1)\) | \(\checkmark[M]\) |
| \(\{p \leq N\}\) (Prim) | \(\sim N/\log N\) | \(O(\log N)\) | \(\warning[M]\) |
| Primpotenzen | \(\sim N/\log N\) | \(O(\log N)\) | \(\warning[M]\) |

---

## Allgemeines Dichte-No-Go

**Satz NEU-82.1** (Dichte-No-Go)

Sei \(\lambda_{n,N} := \beta_{n,N} \log n\). Die Feshbach-Stabilität fordert

$$
\sum_{n \in \Sigma_N} \lambda_{n,N} \to \gamma > 0.
$$

Jacobi-Gewichts-Stabilität auf dem Orbit \(r \leq N\) fordert

$$
N \cdot \sup_{n \in \Sigma_N} \lambda_{n,N} = O(1),
\quad \text{d.h. } \lambda_{n,N} \lesssim \frac{1}{N} \text{ für alle } n.
$$

Dann:

$$
\sum_{n \in \Sigma_N} \lambda_{n,N} \lesssim \frac{\kappa_N}{N}.
$$

Damit beide Bedingungen erfullt sein können:

$$
\boxed{\text{Simultane Feshbach- und Jacobi-Stabilität erzwingt } \kappa_N \asymp N.}
$$

Da stets \(\kappa_N \leq N\) für \(\Sigma_N \subset \{1,\ldots,N\}\), ist die volle Labelmenge die
**einzige Wahl**, die beide Bedingungen gleichzeitig erfüllen kann.  
**Status: \(\checkmark[M]\)**

---

## Zwei Strategien

### Strategie I: Volle Labelmenge + spätere Mangoldt-Extraktion (Favorit)

$$
\Sigma_N = \{2, \ldots, N\}, \quad \kappa_N = N-1 \asymp N.
$$

- \(b_j(n) = O(1)\): Jacobi-Gewichte stabil \(\checkmark[M]\)
- Feshbach-Gesamtbeitrag stabil \(\checkmark[M]\)
- \(\log n\)-Terme enthalten \(\log p\), \(\log p^k\), \(\log m\) für alle \(n\)
- Mangoldt-Extraktion \(\log n \to \Lambda(n)\) erfolgt **nachträglich** durch  
  Möbius-/Primsektor-Projektion auf den arithmetischen Teilraum

**Status: \(\warning[M]\) / Favorit**

### Strategie II: Dünne Labelmenge + Orbit-Trunkierung

$$
\Sigma_N = \{p \leq N\}, \quad \text{Orbit-Trunkierung } r \lesssim \kappa_N.
$$

Dann:

$$
|b_j(p)| \leq \frac{\gamma \kappa_N}{2\kappa_N} = \frac{\gamma}{2} = O(1).
$$

- Jacobi-Gewichte stabil unter Orbit-Trunkierung \(\checkmark[M]\)
- Aber: Orbit-Trunkierung verändert den Hilbertraum; Limes-Analyse komplizierter \(?[O]\)

**Status: \(?[O]\)**

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Kanalabh. Kopplung stabilisiert Feshbach-Gesamtbeitrag exakt | \(\checkmark[M]\) |
| (B) | Jacobi-Stabilität \(\Leftrightarrow\) \(\kappa_N \asymp N\) | \(\checkmark[M]\) |
| (C) | Primlabel: Feshbach stabil, Jacobi \(O(\log N)\) | \(\warning[M]\) |
| (D) | Dichte-No-Go: simultane Stabilität \(\Rightarrow\) \(\kappa_N \asymp N\) | \(\checkmark[M]\) |
| (E) | Strategie I (volle Labelmenge + Mangoldt-Extraktion): Favorit | \(\warning[M]\) |
| (F) | Strategie II (Primlabel + Orbit-Trunkierung): offen | \(?[O]\) |

---

## Konsequenz

Der neue Satz ist nicht die Formel für \(\beta_{n,N}\), sondern das strukturelle Resultat:

> **Simultane Feshbach- und Jacobi-Stabilität erzwingt eine dichte Labelmenge  
> \(\kappa_N \asymp N\).**

Dies spricht stark für Strategie I:
- Arbeite mit \(\Sigma_N = \{2,\ldots,N\}\)
- \(\beta_{n,N} = \gamma/((N-1)\log n)\)
- Mangoldt-Struktur via Möbius-Projektion nachträglich extrahieren

Die zentrale offene Frage für NEU-83 ist:

$$
\boxed{\text{Wie wird } \log n \to \Lambda(n) \text{ aus der vollen Labelmenge durch Projektion extrahiert?}}
$$

---

## Verweise

- NEU-81: Konflikt (F) vs. (J); Kandidat \(\gamma\)
- NEU-67/75: \(\Lambda = \mu * \log\); Primsektor-Projektion \(P_{\text{prime}}\)
- NEU-68: Möbius-Feshbach, \(1/k\)-Mechanismus
- Apostol, Kap. 2 (Möbius-Funktion und Mangoldt-Formel)
- Reed & Simon II, \S X.2 (Jacobi-Operatoren, Carleman-Kriterium)
