# NEU-138 — Fredholm-Determinante, Spurformeln und Zeta-Rückbindung

> Stand: 8. Juli 2026.  
> Anschluss: NEU-137 (Σ_rel^ren ∈ S₁ bewiesen), NEU-136 (Zerlegung), NEU-44.R (S1–S4 geschlossen).

---

## Ausgangspunkt

NEU-137 hat gezeigt:

$$\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1 \quad (\beta > 0),$$

gleichmäßig für $\beta \geq \beta_0 > 0$, mit Singularität bei $\beta \downarrow 0$.

Die Rang-1-Kette

$$\|C_p^{\mathrm{rel}}\|^2 = O\!\left(\frac{(\log p)^2}{p}\right)
\;\Rightarrow\;
\|C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\sharp\|_{\mathcal{S}_1} = O\!\left(\frac{(\log p)^2}{p}\right)
\;\Rightarrow\;
\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$$

ist nicht heuristisch, sondern formal (Rang-1 + Spurklassennorm-Identität). Der Log-Verlust ist topologisch absorbiert — nicht durch Normwechsel oder Abel-Kancellation, sondern durch das renormalisierte $p^{-\beta}$-Gewicht.

**Dieser Eintrag behandelt den nächsten Block: Was kann man mit $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$ spektral tun?**

---

## 138.1 Fredholm-Determinante

Aus $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$ folgt die Wohldefiniertheit der Fredholm-Determinante für alle $z \in \mathbb{C}$, $\beta > 0$:

$$\det\!\left(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right) := \prod_{n \geq 1}(1 - z\,\lambda_n(\beta)),$$

wobei $(\lambda_n(\beta))_{n \geq 1}$ die (mit Vielfachheit gezählten) Eigenwerte von $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ sind.

**Eigenschaften:**
- Das Produkt konvergiert absolut, da $\sum_n |\lambda_n(\beta)| = \|\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\|_{\mathcal{S}_1} < \infty$.
- $z \mapsto \det(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))$ ist eine ganze Funktion.
- Die Nullstellen von $z \mapsto \det(\ldots)$ sind genau $z = \lambda_n(\beta)^{-1}$.

**Status:** ✓[V] — unmittelbare Konsequenz aus $\mathcal{S}_1$.

---

## 138.2 Spurformeln

### 138.2.1 Potenzspur

Für $n \geq 1$ und $\beta > 0$:

$$\mathrm{Tr}\!\left[\left(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)^n\right] = \sum_k \lambda_k(\beta)^n.$$

Aus $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$ folgt $\left(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)^n \in \mathcal{S}_1$ für alle $n \geq 1$, also ist jede Potenzspur wohldefiniert und endlich.

### 138.2.2 Logarithmische Ableitung

Aus der Fredholm-Determinante folgt formal:

$$\frac{d}{dz}\log\det\!\left(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right) = -\sum_{n \geq 0} \mathrm{Tr}\!\left[\left(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)^{n+1}\right] z^n.$$

Diese Reihe konvergiert für $|z| < \|\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\|_{\mathcal{S}_1}^{-1}$ und setzt sich meromorph fort.

### 138.2.3 Erste Spur — explizit

$$\mathrm{Tr}\!\left[\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right] = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}} \cdot \mathrm{Tr}\!\left[C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\sharp\right] = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}} \cdot |c_p|^2.$$

Dies ist eine **gewichtete Primzahlsumme** mit Gewichten $|c_p|^2 = O((\log p)^2/p)$.

**Status:** ✓[V] für $\beta > 0$; Verhalten bei $\beta \downarrow 0$ spiegelt $\sum_p (\log p)^2/p = +\infty$.

---

## 138.3 Primclock- und Zeta-Rückbindung

### 138.3.1 Verbindung zur Zetafunktion

Die erste Spur lautet:

$$\mathrm{Tr}\!\left[\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right] = \sum_p \frac{|c_p|^2\, p^{-\beta}}{1-p^{-\beta}} = \sum_p |c_p|^2 \sum_{k \geq 1} p^{-k\beta}.$$

Falls $|c_p|^2 \sim (\log p)^2/p$ (strukturell aus NEU-135.D), ergibt die Doppelsumme eine Dirichlet-Reihe mit Prim-Gewichten, die mit $-\zeta'(s)/\zeta(s)$ (dem logarithmischen Ableitungskanal) verwandt ist. Die präzise Identifikation erfordert einen weiteren Schritt (NEU-139).

### 138.3.2 Selberg/Ihara-Struktur

Die Fredholm-Determinante $\det(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))$ hat die formale Struktur eines **Ihara-Zeta-Faktors**:

$$\det(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) \;\longleftrightarrow\; \prod_p \det(1 - z\,\lambda_p(\beta)),$$

wobei $\lambda_p(\beta) = p^{-\beta}/(1-p^{-\beta}) \cdot |c_p|^2$ der primspezifische Eigenwertbeitrag ist. Dies ist ein Kandidat für eine **spektrale Zerlegung der Riemannschen Zetafunktion** in Primfaktoren.

**Status:** ❓[O] — strukturelle Analogie klar, präzise Identifikation offen (Folgeprogramm).

### 138.3.3 Primclock-Rückbindung

Der Primclock (informell: das arithmetische Taktgeber-Objekt aus dem RH-Programm) wird hier durch die Gewichtsfolge $(|c_p|^2)_p$ kodiert. Die Verbindung zur Riemannschen Vermutung lautet:

> **RH ⟺ Die Nullstellen von $z \mapsto \det(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))$ liegen auf der richtigen Linie (nach Rückbindung an $\xi$).**

Dies ist das Ziel des Gesamtprogramms. NEU-138 etabliert die notwendige analytische Infrastruktur.

**Status:** ❓[O] — Ziel des Folgeprogramms.

---

## 138.4 Offene Schritte (Folgeprogramm)

| Schritt | Inhalt | Status |
|---|---|---|
| **S1** | Präzise Identifikation $\mathrm{Tr}[\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)]$ mit $-\zeta'/\zeta$-Kanal | ❓[O] — NEU-139 |
| **S2** | Nullstellenstruktur von $\det(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))$ | ❓[O] |
| **S3** | Selberg/Ihara-Faktorisierung über Primzahlen | ❓[O] |
| **S4** | RH-Äquivalenz über Spektrallage der Determinante | ❓[O] — Endziel |

---

## 138.5 Statusdiagnose

| Aussage | Status |
|---|---|
| $\det(1 - z\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))$ existiert als ganze Funktion ($\beta > 0$) | ✓[V] |
| Potenzspuren $\mathrm{Tr}[(\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))^n]$ wohldefiniert | ✓[V] |
| Erste Spur als gewichtete Primzahlsumme explizit | ✓[V] |
| Verbindung zu $-\zeta'/\zeta$ präzisiert | ❓[O] — NEU-139 |
| RH-Rückbindung über Determinante | ❓[O] — Endziel |

---

## Fazit

NEU-138 markiert den Übergang vom **Existenzproblem** ($\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$?) zum **Verwendungsprogramm**:

$$\mathcal{S}_1 \;\Rightarrow\; \text{Fredholm-Det.} \;\Rightarrow\; \text{Spurformeln} \;\Rightarrow\; \text{Zeta-Rückbindung} \;\Rightarrow\; \text{RH.}$$

Der erste Schritt dieser Kette ist bewiesen. Alle weiteren sind offen — aber jetzt mit der richtigen analytischen Grundlage.

---

## Verweise

- **NEU-137**: $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$, S1–S4 geschlossen
- **NEU-44.X / 44.R**: Rang-1-Struktur, Spurklassennorm-Identität
- **NEU-136**: Zerlegung $\Sigma_{\mathrm{rel}} = \Sigma_{\mathrm{rel}}^\infty + \Sigma_{\mathrm{rel}}^{\mathrm{ren}}$
- **NEU-135.D**: Welt-2, Normabschätzung $|c_p|^2 = O((\log p)^2/p)$
- **NEU-139**: Zeta-Identifikation (geplant)
