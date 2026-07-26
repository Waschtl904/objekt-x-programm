# NEU-85 — Starker Null-Limes und wandernde arithmetische Fenster

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-84 (Zeilennorm-Barriere; zwei Orbit-Skalen)  
**Nächste Nummer:** NEU-86

---

## Ausgangspunkt

Aus NEU-84 mit Mangoldt-Gewichtung \(\lambda_{n,N} = \gamma\Lambda(n)/N\):

$$
J_N^{\Lambda}\delta_r
= \frac{\gamma r}{N}\sum_{n \leq N-r}\Lambda(n)\,\delta_{r+n},
$$

$$
\|J_N^{\Lambda}\delta_r\|_2 \asymp \gamma r\sqrt{\frac{\log N}{N}}.
$$

---

## Satz NEU-85.1 — Starker Null-Limes auf festen Vektoren

Für jedes **feste** \(r\) gilt

$$
\|J_N^{\Lambda}\delta_r\|_2 \asymp \gamma r\sqrt{\frac{\log N}{N}} \to 0.
$$

Damit gilt für jeden endlich getragenen Vektor \(f = \sum_{r \leq R} c_r \delta_r\):

$$
\boxed{J_N^{\Lambda} f \to 0 \quad \text{stark in } \ell^2.}
$$

**Der naive starke Operatorlimes auf fest getragenen Vektoren ist der Nulloperator.**  
**Status: \(\checkmark[M]\)**

---

## Strukturelle Warnung

$$
\boxed{\text{Ein nichttrivialer arithmetischer Limes kann nicht im naiven starken }\ell^2\text{-Limes auf festen Vektoren liegen.}}
$$

Dies ist kein technisches Detail, sondern ein struktureller Befund: Die arithmetische Feshbach-Masse

$$
\sum_{n \leq N}\lambda_{n,N} = \frac{\gamma}{N}\psi(N) \sim \gamma
$$

bleibt stabil, aber sie steckt in **wandernden Kanalkombinationen** \((r, n)\) mit \(r + n \leq N\),
nicht in festen Basisvektoren.

---

## Zwei Orbit-Skalen (Zusammenfassung NEU-84, korrigiert)

| Regime | Skala \(M_N\) | Eigenschaft |
|---|---|---|
| A: Pathwise Jacobi | \(N/\log N\) | \(b_j(n) = O(1)\); \(\ell^2\)-Zeilennorm \(\sim \sqrt{N/\log N} \to \infty\) |
| B: \(\ell^2\)-Operatorstabil | \(\sqrt{N/\log N}\) | \(b_j(n) = O(1)\); \(\ell^2\)-Zeilennorm \(O(1)\) |

---

## Wo die arithmetische Information liegt

Da der naive starke Limes trivial ist, muss die arithmetische Struktur in einem
der folgenden Objekte kodiert sein:

### 1. Wandernde Fenster \(r = r_N \to \infty\)

Für \(r_N = \alpha\sqrt{N/\log N}\) gilt

$$
\|J_N^{\Lambda}\delta_{r_N}\|_2 \asymp \gamma\alpha = O(1).
$$

Die Zeilennorm bleibt dann endlich; der Operator ist auf dem wandernden Fenster **nicht trivial**.

### 2. Feshbach-/Kollapsfunktionale

Der Kollaps \(\Pi_N J_N^{\Lambda} \Pi_N^*\) kann eine nichttriviale Spur- oder Matrixstruktur tragen,
auch wenn die einzelnen Zeilennormen verschwinden.

### 3. Spur- und Determinantenobjekte

$$
\mathrm{Tr}\bigl(f(J_N^{\Lambda})\bigr), \quad \det(I + z J_N^{\Lambda})
$$

können für geeignetes \(f\) oder \(z\) nichttriviale Grenzwerte besitzen,
während der Operator selbst stark gegen Null konvergiert.

### 4. \(N\)-abhängige Testtopologie

Mit renormierten Testvektoren \(f_N = \delta_{r_N} / \|\delta_{r_N}\|\) oder
gewichteten Hilberträumen kann der Limes aus dem trivialen Regime herausgezogen werden.

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(M_N = N/\log N\): einzelne \(b_j = O(1)\); \(\ell^2\)-Zeilennorm divergiert | \(\checkmark[M]\) |
| (B) | \(M_N = \sqrt{N/\log N}\): \(\ell^2\)-Zeilennorm \(O(1)\) | \(\checkmark[M]\) |
| (C) | \(J_N^{\Lambda}f \to 0\) stark auf festen endlich getragenen Vektoren | \(\checkmark[M]\) |
| (D) | Nichttrivialer arithmetischer Limes braucht wandernde Fenster, Feshbach-Funktionale, Spur-/Determinantenobjekte oder \(N\)-abh. Testtopologie | \(?[O]\) |
| (E) | Wanderndes Fenster \(r_N = \alpha\sqrt{N/\log N}\): Zeilennorm \(O(1)\), Operator nicht trivial | \(\warning[M]\) |

---

## Konsequenz für den kritischen Pfad

$$
\boxed{J_N^{\Lambda}f \to 0 \text{ stark auf festen Vektoren, obwohl Feshbach-Masse stabil bleibt.}}
$$

Der **nächste Schritt** ist die Entscheidung: Welche Topologie/welches Funktional
extrahiert die arithmetische Spektralinformation?

Drei Kandidaten:
- **NEU-86a:** Wandernde Fensterskala \(r_N \sim \sqrt{N/\log N}\) und zugeordnete Spektralmaße
- **NEU-86b:** Spurformel \(\mathrm{Tr}(f(J_N^{\Lambda}))\) für geeignetes \(f\)
- **NEU-86c:** Feshbach-Determinante \(\det(I + z J_N^{\Lambda}/\kappa_N)\)

---

## Verweise

- NEU-84: Zeilennorm-Barriere; zwei Orbit-Skalen
- NEU-77–79: Algebraische Feshbach-Kollapsidentität
- NEU-65: \(Z_N^{\text{completed}} \to C \cdot \xi\) (Determinanten-Limes)
- NEU-68: Möbius-Feshbach, \(1/k\)-Mechanismus
- Reed & Simon II, \S X.6 (starke Resolventenkonvergenz unbeschränkter Operatoren)
- Simon: *Trace Ideals*, AMS 2005 (Spurformeln)
