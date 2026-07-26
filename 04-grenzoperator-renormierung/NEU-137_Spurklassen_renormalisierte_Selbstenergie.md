# NEU-137 — Spurklassen-Verifikation der renormalisierten Selbstenergie

> Stand: 8. Juli 2026 (finale Fassung, S1–S4 geschlossen durch NEU-44.X/X'/R).  
> Anschluss: NEU-136 (Zerlegung), NEU-135.D (Welt-2), NEU-44.X (Rang-Struktur).

---

## Hauptresultat

**Satz 137.1 (Spurklasse):**  
Unter den Annahmen von NEU-134 und NEU-135.D gilt:

$$\boxed{\Sigma_{rel}^{ren}(\beta) = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,C_p^{rel}(C_p^{rel})^\sharp \in \mathcal{S}_1 \quad \text{für alle } \beta > 0,}$$

gleichmäßig für $\beta \geq \beta_0 > 0$. Bei $\beta = 0$ divergiert die $\mathcal{S}_1$-Norm.

---

## Beweis

**Schritt 1 — Rang-1-Struktur** (NEU-44.X, Satz 44.X.1):  
$C_p^{rel} = c_p \cdot (e_1^{(p)} \otimes f_3^{(p)*})$ ist Rang-1-Operator.

**Schritt 2 — Spurklassen-Identität** (NEU-44.X, Korollar 44.X.2):  
Für Rang-1-Operatoren:
$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} = |c_p|^2 = \|C_p^{rel}\|^2.$$

**Schritt 3 — Normabschätzung** (NEU-134, NEU-135.D):  
$$|c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right).$$

**Schritt 4 — Majorantenreihe** (Standardanalysis):  
$$\sum_p \left\|\frac{p^{-\beta}}{1-p^{-\beta}}\,C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} \lesssim \sum_p \frac{(\log p)^2}{p^{1+\beta}} < \infty \quad (\beta > 0).$$

Die Majorantenreihe ist gleichmäßig beschränkt für $\beta \geq \beta_0 > 0$, also konvergiert $\Sigma_{rel}^{ren}(\beta)$ absolut in $\mathcal{S}_1$. $\square$

---

## Singularität bei $\beta \downarrow 0$

$$\left\|\Sigma_{rel}^{ren}(\beta)\right\|_{\mathcal{S}_1} \gtrsim \sum_p \frac{(\log p)^2}{p^{1+\beta}} \xrightarrow{\beta \downarrow 0} +\infty.$$

Die Divergenz spiegelt $\sum_p (\log p)/p = +\infty$ und ist **strukturell**, keine Schwäche der Methode.

---

## Anwendung: Fredholm-Determinante

Aus $\Sigma_{rel}^{ren}(\beta) \in \mathcal{S}_1$ folgt die Wohldefiniertheit der Fredholm-Determinante:

$$\det\!\left(1 - z\,\Sigma_{rel}^{ren}(\beta)\right) \quad\text{existiert für alle } z \in \mathbb{C},\; \beta > 0.$$

Dies öffnet den Weg zu Spur- und Determinantenformeln im RH-Programm (Folgeprogramm).

---

## Statusblock

| Schritt | Inhalt | Status |
|---|---|---|
| S1 | Rang-1-Struktur von $C_p^{rel}$ | ✓[V] — NEU-44.X |
| S2 | Spurklassen-Identität $\|\cdot\|_{\mathcal{S}_1} = |c_p|^2$ | ✓[V] — NEU-44.X, Kor. 44.X.2 |
| S3 | $\sum_p (\log p)^2/p^{1+\beta} < \infty$, $\beta > 0$ | ✓[M] |
| S4 | Gleichmäßigkeit für $\beta \geq \beta_0$ | ✓[V] — Majorantenargument |
| S5 | Fredholm-Determinante | ❓[O] — Folgeprogramm |

**Kernsatz vollständig bewiesen. Folgeprogramm: S5 (Determinantenformeln).**

---

## Verweise

- **NEU-136**: Zerlegung $\Sigma_{rel} = \Sigma_{rel}^\infty + \Sigma_{rel}^{ren}$
- **NEU-135.D**: Welt-2-Entscheidung, Normabschätzung
- **NEU-44.X**: Rang-1-Beweis
- **NEU-44.X'**: Stabilität unter Störungen
- **NEU-44.R**: Rückbindung, Statusupdate S1–S4
- **NEU-128B**: Warnung $\beta \downarrow 0$
