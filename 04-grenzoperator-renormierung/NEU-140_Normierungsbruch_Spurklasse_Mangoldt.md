# NEU-140 — Normierungsbruch zwischen Spurklasse und Mangoldt-Spur

> Stand: 8. Juli 2026.  
> Anschluss: NEU-139 (T1/T2), NEU-135.D (Normabschätzung), NEU-137 ($\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$).

---

## Kernergebnis

**NEU-135.D und direkte T1-Identifikation sind inkompatibel.**

Nach NEU-44.X gilt:
$$\mathrm{Tr}_{\mathcal{S}_1}\bigl(C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\sharp\bigr) = |c_p|^2.$$

Nach NEU-135.D gilt (bewiesene obere Schranke):
$$|c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right).$$

Daher:
$$\frac{|c_p|^2}{\log p} = O\!\left(\frac{\log p}{p}\right) \to 0.$$

Folglich ist $|c_p|^2 = \log p$ für große $p$ **unmöglich** — eine bewiesene obere Schranke, die kleiner ist als $\log p$, kann nicht durch Grobheit $\log p$ noch erlauben.

---

## 140.1 Drei-Schichten-Trennung

$$\text{arithmetisches Gewicht} \quad\neq\quad \text{Hilbertraum-Norm} \quad\neq\quad \text{gewöhnliche Spur}.$$

| Schicht | Objekt | Wert |
|---|---|---|
| Hilbertraum-Norm | $\|C_p^{\mathrm{rel}}\|^2 = |c_p|^2$ | $O\bigl((\log p)^2/p\bigr)$ |
| Gewöhnliche Spur | $\mathrm{Tr}(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))$ | $\sum_p \frac{p^{-\beta}}{1-p^{-\beta}} |c_p|^2$ |
| Mangoldt-Spur | $-\zeta'/\zeta(\beta)$ | $\sum_p \frac{\log p\; p^{-\beta}}{1-p^{-\beta}}$ |

**Diagnose:** Die gewöhnliche Spur liefert eine **gedämpfte Mangoldt-Spur**, nicht die Mangoldt-Spur selbst.

---

## 140.2 Dämpfungskoeffizient $a_p$

Setze:
$$a_p := \frac{|c_p|^2}{\log p}.$$

Dann gilt unter NEU-135.D:
$$a_p = O\!\left(\frac{\log p}{p}\right) \to 0.$$

Die gewöhnliche Spur lautet damit:
$$\mathrm{Tr}\bigl(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) = \sum_p a_p \cdot \frac{\log p\; p^{-\beta}}{1-p^{-\beta}}.$$

Das ist eine **gedämpfte Version** von $-\zeta'/\zeta(\beta)$, mit primweise gegen 0 gehendem Gewicht $a_p$.

---

## 140.3 Renormierungsoperator $R$

Für eine Zeta-Identifikation ist ein zusätzlicher Renormierungsoperator $R$ nötig, der auf dem $p$-Primkanal mit

$$R_p := \frac{\log p}{|c_p|^2}$$

wirkt, sodass:
$$\mathrm{Tr}\bigl(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) = \sum_p R_p \cdot \frac{p^{-\beta}}{1-p^{-\beta}} |c_p|^2 = \sum_p \frac{\log p\; p^{-\beta}}{1-p^{-\beta}} = -\frac{\zeta'}{\zeta}(\beta).$$

Unter NEU-135.D wächst $R_p$ mindestens wie:
$$R_p \gtrsim \frac{p}{\log p}.$$

**Offene Frage:** Ist $R$ ein beschränkter, selbstadjungierter Operator auf dem relevanten Raum? Falls $R_p \sim p/\log p$, ist $R$ unbeschränkt — die renormierte Spur $\mathrm{Tr}(R\Sigma)$ ist dann kein gewöhnlicher Spurklassenausdruck mehr, sondern eine regulierte Observable.

---

## 140.4 Konsequenz für die Fredholm-Determinante (T2-Kontext)

Falls T2 gilt ($\langle\Psi_p,\Psi_q\rangle = 0$ für $p\neq q$), ist die Fredholm-Determinante diagonal:

$$\det(1-z\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = \prod_p \left(1 - z\frac{p^{-\beta}}{1-p^{-\beta}} |c_p|^2\right).$$

Aber auch dann gilt: Das ist **kein Zeta-Eulerprodukt**, sondern ein Produkt mit gedämpften Gewichten $a_p \log p$, $a_p \to 0$.

**Schluss:**

$$\boxed{\text{T2 kann die Determinante diagonalisieren, aber T1 entscheidet die Zeta-Normalisierung.}}$$

---

## 140.5 Statusdiagnose

| Aussage | Status |
|---|---|
| $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$ | ✓[V] (NEU-137) |
| $\mathrm{Tr}(\Sigma) = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}|c_p|^2$ | ✓[V] (NEU-138) |
| $|c_p|^2 = \log p$ (T1 direkt) | ✗[F] — inkompatibel mit NEU-135.D |
| $\mathrm{Tr}(\Sigma) = -\zeta'/\zeta(\beta)$ (gewöhnliche Spur) | ✗[F] — folgt aus T1-Falschheit |
| $\mathrm{Tr}(R\,\Sigma) = -\zeta'/\zeta(\beta)$ (renormierte Spur) | ❓[O] — hängt an Wohldefiniertheit von $R$ |
| $\langle\Psi_p,\Psi_q\rangle = 0$ (T2) | ❓[O] — unabhängig prüfbar |
| Fredholm-Det. = reines Zeta-Eulerprodukt | ❓[O] — erfordert T2 + renormierte T1 |

---

## 140.6 Nächste Schritte

| Schritt | Inhalt | Priorität |
|---|---|---|
| **NEU-140.T2** | Orthogonalitätstest $\langle\Psi_p,\Psi_q\rangle$ aus Kanalgeometrie | 🔴 hoch, unabhängig von T1 |
| **NEU-140.R** | Wohldefiniertheit von $R$; regulierte Observable $\mathrm{Tr}(R\Sigma)$ | 🔴 hoch |
| **NEU-141** | Falls $R$ wohldefiniert: renormierte Zeta-Identifikation | folgt aus 140.R |
| **NEU-142** | RH-Äquivalenz über Spektrallage der renormierten Det. | Endziel |

---

## Verweise

- **NEU-44 / NEU-44.X**: Definition $C_p^{\mathrm{rel}}$, $|c_p|^2$, Rang-1
- **NEU-135.D**: Normabschätzung $|c_p|^2 = O((\log p)^2/p)$
- **NEU-137**: $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$
- **NEU-138**: Fredholm-Det., erste Spur
- **NEU-139**: T1/T2-Formulierung, Kreuzterm-Test
- **NEU-140.T2**: Orthogonalitätstest (geplant)
- **NEU-140.R**: Renormierungsoperator $R$ (geplant)
