# NEU-84 — Mangoldt-kompatible Orbit-Trunkierung und Zeilennorm-Barriere

**Stand:** 30. Juni 2026 (Tabelle korrigiert)  
**Vorgänger:** NEU-83 (Dreifach-Konflikt; Weg 2 Orbit-Trunkierung als Favorit)  
**Nächste Nummer:** NEU-85

---

## Ausgangspunkt

Aus NEU-83 (Weg 2): Orbit-Trunkierung \(r \leq M_N\) mit echter Mangoldt-Gewichtung

$$
\lambda_{n,N} := \frac{\gamma}{N}\Lambda(n).
$$

Der getrunkierte Operator wirkt auf \(\delta_r\) als

$$
J_{N,M}^{\Lambda}\delta_r
= \frac{\gamma r}{N}\sum_{\substack{n \leq N \\ r+n \leq N}} \Lambda(n)\,\delta_{r+n}.
$$

---

## 1. Feshbach-Stabilität

Für \(r = o(N)\):

$$
\sum_{n \leq N-r}\lambda_{n,N}
= \frac{\gamma}{N}\psi(N-r)
\sim \gamma\bigl(1 - o(1)\bigr), \qquad \psi(x) := \sum_{n \leq x}\Lambda(n) \sim x.
$$

Der Feshbach-Gesamtbeitrag bleibt stabil solange \(M_N = o(N)\).  
**Status: \(\checkmark[M]\)**

---

## 2. Pathwise Jacobi-Stabilität

Die einzelnen Jacobi-Offdiagonalgewichte sind

$$
b_j(n) = \tfrac{1}{2}r\lambda_{n,N} = \frac{\gamma}{2N}r\Lambda(n).
$$

Da \(\Lambda(n) \leq \log N\):

$$
|b_j(n)| \leq \frac{\gamma}{2N}M_N \log N.
$$

Gleichmäßige Schranke \(O(1)\) genau dann, wenn

$$
\boxed{M_N^{\mathrm{path}} \lesssim \frac{N}{\log N}.}
$$

**Status: \(\checkmark[M]\)**

---

## 3. Zeilennorm-Barriere (neues Resultat)

Da die Ausgaben \(\delta_{r+n}\) für verschiedene \(n\) und festes \(r\) **orthogonal** sind:

$$
\|J_{N,M}^{\Lambda}\delta_r\|_2^2
= \frac{\gamma^2 r^2}{N^2}\sum_{n \leq N-r}\Lambda(n)^2.
$$

Mit \(\sum_{n \leq N}\Lambda(n)^2 \asymp N\log N\):

$$
\|J_{N,M}^{\Lambda}\delta_r\|_2 \asymp \gamma r\sqrt{\frac{\log N}{N}}.
$$

Für \(r = M_N^{\mathrm{path}} = N/\log N\):

$$
\|J_{N,M}^{\Lambda}\delta_{N/\log N}\|_2 \asymp \gamma\sqrt{\frac{N}{\log N}} \to \infty.
$$

**Der volle summierte Operator ist auf dem Fenster \(r \leq N/\log N\) nicht gleichmäßig \(\ell^2\)-beschränkt.**  
**Status: \(\warning[M]\)**

---

## 4. Strengere Operatorskala

Gleichmäßige Zeilennormkontrolle \(\|J_{N,M}^{\Lambda}\delta_r\|_2 = O(1)\) fordert

$$
\gamma M_N\sqrt{\frac{\log N}{N}} = O(1),
\quad \text{d.h.} \quad
\boxed{M_N^{\mathrm{op}} \lesssim \sqrt{\frac{N}{\log N}}.}
$$

**Status: \(\checkmark[M]\)**

### Skalenvergleich (korrigiert)

| Stabilitätsbegriff | Skala \(M_N\) |
|---|---|
| Pathwise Jacobi-Gewichte \(b_j = O(1)\) | \(N/\log N\) |
| Volle \(\ell^2\)-Zeilennorm \(O(1)\) | \(\sqrt{N/\log N}\) |

**Wichtig:** Die zweite Skala ist \(\sqrt{N/\log N}\), nicht \(N/\log N\).

---

## 5. Geometrie: Eingangsfenster, Labelgrenze, Zielraum

```
Eingangsfenster:  K_N := {1, ..., M_N}          (Quelle: r in K_N)
Labelmenge:       Sigma_N = {2, ..., N}          (Kanaele: n in Sigma_N)
Zielraum:         I_N = {1, ..., N}              (Ziel: r+n in I_N)
```

Der getrunkierte Shift:

$$
\mathsf{S}_{N,M}\eta_{r,n} =
\begin{cases}
\eta_{r+n,n}, & r \in K_N,\ r+n \in I_N, \\
0, & \text{sonst.}
\end{cases}
$$

Die algebraische Feshbach-Kollapsidentität bleibt unter dieser Trunkierung gültig.  
**Status: \(\checkmark[M]\)**

---

## 6. Randterme

Für **feste** \(r\): Randfehler \(\to 0\) stark. \(\checkmark[M]\)  
**Uniform** in \(r \leq M_N\): nicht in Operatornorm kontrolliert. \(\warning[M]\)

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Mangoldt + \(r \leq N/\log N\): einzelne \(b_j = O(1)\) | \(\checkmark[M]\) |
| (B) | Algebraische Feshbach-Identität unter Trunkierung | \(\checkmark[M]\) |
| (C) | Randterme: stark \(\to 0\); nicht uniform | \(\warning[M]\) |
| (D) | Zeilennorm bei \(r = N/\log N\) divergiert wie \(\sqrt{N/\log N}\) | \(\warning[M]\) |
| (E) | Strengere Skala \(M_N^{\mathrm{op}} = \sqrt{N/\log N}\) stabilisiert \(\ell^2\)-Norm | \(\checkmark[M]\) |
| (F) | Entscheidungspunkt: pathwise vs. \(\ell^2\)-Operator | \(?[O]\) |

---

## Verweise

- NEU-83: Dreifach-Konflikt Satz NEU-83.1
- NEU-77–79: Algebraische Feshbach-Kollapsidentität
- NEU-67/68: \(\Lambda = \mu * \log\); \(\psi(x) \sim x\)
- Apostol, Kap. 4: \(\sum_{n \leq N}\Lambda(n)^2 \asymp N \log N\)
- Reed & Simon II, \S X.2: Jacobi-Operatoren; starke Resolventenkonvergenz
