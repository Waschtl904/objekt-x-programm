# NEU-80 — Extraktion der Jacobi-Kopplung aus NEU-37 und neue Normierungsbedingung

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-79 (Kanalzahl-Skalierung; \(\gamma_N = a_N \kappa_N\))  
**Liest:** NEU-37 (Jacobi-Kandidat \(A_N^-\)), NEU-62 (\(\gamma_N \equiv 1\))  
**Nächste Nummer:** NEU-81

---

## Befund aus NEU-37

NEU-37 definiert den Jacobi-Kandidaten durch

$$
A_N^- = H_N + \beta_N J_N^-.
$$

Auf einem endlichen Orbit \(\mathcal{H}_{n,a}^{(M)}\) gilt

$$
A_N^- E_j = \frac{\beta_N \alpha_j}{2} E_{j+1} + \frac{\beta_N \alpha_{j-1}}{2} E_{j-1},
$$

mit

$$
\alpha_j = \gamma_N (a + jn) \log n.
$$

Die Jacobi-Offdiagonalgewichte sind daher

$$
b_j = \frac{\beta_N \alpha_j}{2} = \frac{\beta_N \gamma_N}{2} (a + jn) \log n.
$$

Aus NEU-62 gilt \(\gamma_N \equiv 1\). Also:

$$
\boxed{b_j = \frac{\beta_N}{2} (a + jn) \log n.}
$$

### Entscheidender Befund

NEU-37 legt \(\beta_N\) **nicht asymptotisch fest**. Insbesondere findet sich:

- \(\beta_N = \kappa_N^{-1}\): **nicht** in NEU-37 gesetzt
- \(\beta_N \equiv 1\): **nicht** in NEU-37 als verbindliche Wahl
- \(\beta_N\) extern/frei: **JA** — aktueller Stand

Auch NEU-36 legt \(\beta_N\) nicht fest. Dort erscheint der Kandidat ebenfalls nur als  
\(A_N^- := H_N + \beta_N J_N^-\), während die Grenzfrage auf Resolventenspur- und  
Determinantenkonvergenz verschoben wird. Trunkierungswahl und Spursnormierung sind  
ausdrücklich als nicht-kanonische Daten markiert.

---

## Konsequenz: \(\beta_N\) als freier Kopplungsparameter

Mit \(\gamma_N \equiv 1\) und \(\beta_N\) frei gilt:

$$
a_N^{\text{eff}} = \beta_N.
$$

Die NEU-79-Prüfgleichung

$$
\beta_N \kappa_N \overset{?}{\to} \gamma \in (0, \infty)
$$

wird damit zur **neuen notwendigen Normierungsbedingung**, nicht zu einer aus NEU-37 ableitbaren Folgerung.

---

## Neue Normierungsbedingung (Jacobi-kompatibler Feshbach-Kollaps)

$$
\boxed{\beta_N \sim \frac{\gamma}{\kappa_N}}
$$

Dies ist eine **Modellwahl**, keine analytisch erzwungene Bedingung.  
Wenn sie akzeptiert wird, ist der normierte Feshbach-Kollaps skalenstabil.

### Zielbedingung je nach Labelmenge

| Labelmenge \(\Sigma_N\) | \(\kappa_N\) | Zielbedingung |
|---|---|---|
| \(\{1,\ldots,N\}\) | \(N\) | \(\beta_N \sim \gamma/N\) |
| \(\{p \leq N \text{ prim}\}\) | \(\sim N/\log N\) | \(\beta_N \sim \gamma \log N / N\) |
| Primpotenzen | \(\sim N/\log N\) | \(\beta_N \sim \gamma \log N / N\) |

---

## Statusbewertung

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\gamma_N \equiv 1\) aus NEU-62; \(a_N^{\text{eff}} = \beta_N\) | ✓[M] |
| (B) | NEU-37 zeigt \(b_j = \frac{\beta_N}{2}(a+jn)\log n\) | ✓[M] |
| (C) | NEU-37 fixiert \(\beta_N\) nicht (freier Parameter) | ✓[M] |
| (D) | Jacobi-kompatible Feshbach-Bedingung: \(\beta_N \kappa_N \to \gamma\) | neue Normierungsbedingung |
| (E) | Ohne Bedingung: \(\beta_N \kappa_N \to 0\) = Unterkopplung; \(\to \infty\) = Überkopplung | ✓[M] |
| (F) | \(\beta_N := \gamma/\kappa_N\) als Modellwahl macht Feshbach-Kollaps skalenstabil | Kandidat ⚠[M] |

---

## Offene Folgefragen

Wenn \(\beta_N := \gamma/\kappa_N\) akzeptiert wird, sind die nächsten Engpässe:

1. **Starker Feshbach-Limes** \(N \to \infty\) auf endlich-getragenen Vektoren \(\quad \mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{\mathbf{}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}\) ❓[O]
2. **Mangoldt-/Primsektor-Extraktion** \(\log n \to \Lambda(n)\) \(\quad\) ⚠[M]
3. **Wahl von \(\Sigma_N\)** (volle Labelmenge vs. Primlabel) \(\quad\) ⚠[M]

---

## Verweise

- NEU-37 (in teil2): \(A_N^- = H_N + \beta_N J_N^-\); Jacobi-Gewichte \(b_j = \frac{\beta_N \gamma_N}{2}(a+jn)\log n\)
- NEU-36 (in teil2): Resolventen-/Determinantenkonvergenz; \(\beta_N\) nicht-kanonisch
- NEU-62: \(\gamma_N \equiv 1\) als strukturelle Normalisierung
- NEU-79: Kanalzahl-Skalierung \(\gamma_N = a_N \kappa_N\)
- NEU-78: Normierungs-No-Go; isometrischer Kollaps
