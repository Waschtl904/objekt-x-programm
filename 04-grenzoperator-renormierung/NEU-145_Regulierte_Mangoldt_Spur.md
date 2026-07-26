# NEU-145 — Regulierte Mangoldt-Spur im kritischen Streifen

> Stand: 9. Juli 2026.
> Anschluss: NEU-144 (R primdiagonal, Mangoldt-Spurformel für ℜβ>1), NEU-141 (drei Spurklassen-Ebenen), NEU-137 (Σ ∈ S₁).
> **Kernbefund:** RΣ ist für 0<ℜβ≤1 nicht spurklassig — aber die Mangoldt-Spur besitzt eine meromorphe regulierte Fortsetzung.

---

## Leitmotiv

$$\boxed{\operatorname{Tr}_{\mathrm{reg}}\bigl(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) := \operatorname{AC}_{\Re z>1}\!\left[\operatorname{Tr}\bigl(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(z)\bigr)\right](\beta) = -\frac{\zeta'}{\zeta}(\beta)}$$

als meromorphe Funktion auf $\mathbb{C} \setminus \{\text{Pole von } {-\zeta'/\zeta}\}$.

**Wichtige Grenze:** Es wird **nicht** behauptet, dass $R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ für $0 < \Re\beta \leq 1$ gewöhnlich spurklassig wird. Das wäre falsch. Die regulierte Spur ist eine analytisch fortgesetzte Größe, keine gewöhnliche Operatorspur.

---

## 145.0 Ausgangssituation nach NEU-144

### Drei Ebenen — jetzt scharf getrennt

| Ebene | Objekt | Status | Bereich |
|---|---|---|---|
| **Topologisch** | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1$ | ✅ NEU-137 | $\Re\beta > 0$ |
| **Mangoldt-Spur (gewöhnlich)** | $\operatorname{Tr}(R\Sigma) = -\zeta'/\zeta(\beta)$ | ✅ NEU-144 | $\Re\beta > 1$ |
| **Regulierte Spur** | $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma)$ | Definition ✅, Realisierung ❓[O] | $0 < \Re\beta \leq 1$ |

Diese drei Ebenen kollabieren **nicht**. Insbesondere ist die dritte Ebene definitorisch, nicht operatoriell: Die regulierte Spur ist zunächst durch analytische Fortsetzung definiert — ihre operatorielle Realisierung ist das eigentliche offene Problem.

---

## 145.1 Gewöhnliche Mangoldt-Spur: Wiederholung und Grenze

Nach NEU-143/144 gilt $P_pP_q = 0$ für $p \neq q$ und $\operatorname{Tr}(RP_p) = \log p$. Damit:

$$\operatorname{Tr}\!\left(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)
= \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,\log p
= -\frac{\zeta'}{\zeta}(\beta), \qquad \Re\beta > 1.$$

Für $0 < \Re\beta \leq 1$: Die Reihe $\sum_p \frac{\log p \cdot p^{-\beta}}{1-p^{-\beta}}$ divergiert. $R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ ist **nicht** in $\mathcal{S}_1$ (NEU-141.6). Eine direkte Spurbildung ist nicht möglich.

$$\boxed{R\Sigma \notin \mathcal{S}_1 \text{ für } 0 < \Re\beta \leq 1. \quad \text{Keine gewöhnliche Spur.}}$$

---

## 145.2 Ebene 1: Definition durch analytische Fortsetzung

### 145.2.1 Die regulierte Spur

Die Funktion

$$\beta \mapsto \operatorname{Tr}\!\left(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right) = -\frac{\zeta'}{\zeta}(\beta)$$

ist für $\Re\beta > 1$ wohldefiniert und holomorph. $-\zeta'/\zeta$ besitzt eine meromorphe Fortsetzung auf ganz $\mathbb{C}$.

**Definition:**

$$\boxed{\operatorname{Tr}_{\mathrm{reg}}\!\left(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)
:= \operatorname{AC}_{\Re z>1}\!\left[-\frac{\zeta'}{\zeta}(z)\right](\beta)
= -\frac{\zeta'}{\zeta}(\beta).}$$

Diese Definition ist **sofort verfügbar**: Die meromorphe Fortsetzung von $-\zeta'/\zeta$ ist ein klassisches Resultat der analytischen Zahlentheorie.

### 145.2.2 Polstruktur

Die regulierte Spur besitzt Pole bei:

| Pol | Ordnung | Ursprung |
|---|---|---|
| $\beta = 1$ | einfach, Residuum $= 1$ | Pol von $\zeta$ bei $s=1$ |
| $\beta = \rho$ (Nullstelle von $\zeta$) | einfach, Residuum $= -1$ | Aus $\log\zeta = \sum_\rho \log(\beta-\rho) + \ldots$ |
| $\beta = -2k$, $k\in\mathbb{N}$ | einfach | Triviale Nullstellen von $\zeta$ |

Die Nullstellen von $\zeta$ im kritischen Streifen $0 < \Re\beta < 1$ sind genau die Pole der regulierten Spur im interessantesten Bereich.

### 145.2.3 Verbindung zur Riemannschen Hypothese

Die RH besagt, dass alle nicht-trivialen Pole von $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma(\beta))$ auf der Linie $\Re\beta = 1/2$ liegen. In dieser Formulierung ist die RH eine **spektrale Aussage über die Polgeometrie der regulierten Mangoldt-Spur.**

$$\boxed{RH \iff \text{alle Pole von } \operatorname{Tr}_{\mathrm{reg}}(R\Sigma(\beta)) \text{ im Streifen } 0<\Re\beta<1 \text{ liegen auf } \Re\beta = 1/2.}$$

---

## 145.3 Ebene 2: Operatorielle Realisierung (offenes Problem)

### 145.3.1 Warum $(R+\varepsilon)^{-1}$ nicht geeignet ist

Die naheliegende Resolventenregularisierung

$$\operatorname{Tr}\!\left((R+\varepsilon)^{-1} R\,\Sigma(\beta)\right)$$

hat den Defekt: $(R+\varepsilon)^{-1} R = \frac{R}{R+\varepsilon} \to \mathrm{id}$ nur für $\varepsilon \to 0$ auf $\mathcal{D}(R)$. Aber:

$$\frac{R_p}{R_p + \varepsilon} = \frac{1}{1 + \varepsilon/R_p} \approx 1 - \frac{\varepsilon \log p}{p} \to 1 \quad (p\to\infty).$$

Die Regularisierung dämpft $R$ für große $p$ nicht ausreichend — und entfernt damit gerade die Mangoldt-Normierung $R_p \sim p/\log p$ in einem $\varepsilon$-abhängigen, unkontrollierten Maß.

$$\boxed{(R+\varepsilon)^{-1}\text{-Regularisierung ist ungeeignet: sie verzerrt die Mangoldt-Gewichte.}}$$

### 145.3.2 Cutoff-Regularisierung

Sei $\chi_\Lambda : \mathbb{R}_{>0} \to [0,1]$ eine glatte Abschneidefunktion mit $\chi_\Lambda(t) = 1$ für $t \leq \Lambda$ und $\chi_\Lambda(t) = 0$ für $t \geq 2\Lambda$. Dann:

$$\operatorname{Tr}_\Lambda\!\left(R\Sigma(\beta)\right)
:= \operatorname{Tr}\!\left(\chi_\Lambda(R)\,R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)
= \sum_{p:\, R_p \leq \Lambda} \frac{\log p \cdot p^{-\beta}}{1-p^{-\beta}}.$$

Da $R_p \gtrsim p/\log p$, entspricht die Bedingung $R_p \leq \Lambda$ grob der Bedingung $p \lesssim \Lambda \log\Lambda$. Damit ist

$$\operatorname{Tr}_\Lambda\!\left(R\Sigma(\beta)\right) \approx \sum_{p \leq \Lambda\log\Lambda} \frac{\log p \cdot p^{-\beta}}{1-p^{-\beta}}.$$

Das divergiert für $\Lambda\to\infty$ (für $0 < \Re\beta \leq 1$), aber der **endliche Teil** nach Subtraktion des Divergenzterms könnte die regulierte Spur realisieren.

### 145.3.3 Wärme-Regularisierung

Alternativ:

$$\operatorname{Tr}_\varepsilon\!\left(R\Sigma(\beta)\right)
:= \operatorname{Tr}\!\left(e^{-\varepsilon R}\,R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)
= \sum_p e^{-\varepsilon R_p}\,\frac{\log p \cdot p^{-\beta}}{1-p^{-\beta}}.$$

Mit $R_p \sim p/\log p$ ist $e^{-\varepsilon R_p} \sim e^{-\varepsilon p/\log p}$ — das ist eine Primzahlsumme mit exponentiellem Cutoff, analog zur Wärme-Spur im klassischen Spektralzeta-Formalismus.

Das asymptotische Verhalten für $\varepsilon \to 0^+$ ist das eigentliche Problem:

$$\sum_p e^{-\varepsilon p/\log p}\,\frac{\log p \cdot p^{-\beta}}{1-p^{-\beta}} \;\stackrel{?}{=}\; -\frac{\zeta'}{\zeta}(\beta) + \text{(Divergenzterme in } \varepsilon\text{)} + O(\varepsilon).$$

Den endlichen Teil (Hadamard-Renormierung) zu identifizieren und mit der analytischen Fortsetzung $-\zeta'/\zeta(\beta)$ zu verbinden — das ist die offene Frage.

### 145.3.4 Zwei-Ebenen-Trennung

$$\boxed{\underbrace{\operatorname{Tr}_{\mathrm{reg}}(R\Sigma) := -\zeta'/\zeta}_{\text{Ebene 1: Definition, sofort}} \qquad\text{vs.}\qquad \underbrace{\operatorname{Tr}_\varepsilon(R\Sigma)\big|_{\varepsilon\to 0,\,\text{fin.Teil}} \stackrel{?}{=} -\zeta'/\zeta}_{\text{Ebene 2: Realisierung, offen [O]}}}$$

---

## 145.4 Statusdiagnose

| Eintrag | Inhalt | Status |
|---|---|---|
| **145.A** | $\operatorname{Tr}(R\Sigma) = -\zeta'/\zeta$ für $\Re\beta>1$ | ✅ NEU-144 |
| **145.B** | $R\Sigma \notin \mathcal{S}_1$ für $0<\Re\beta\leq 1$: keine gewöhnliche Spur | ✅ |
| **145.C** | Definition $\operatorname{Tr}_{\mathrm{reg}} := \operatorname{AC}[-\zeta'/\zeta]$ | ✅[def] |
| **145.D** | Polstruktur: $\beta=1$, Nullstellen $\zeta$, triviale Nullstellen | ✅ |
| **145.E** | RH ↔ Polgeometrie von $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma)$ auf $\Re\beta=1/2$ | ✅[def] |
| **145.F** | $(R+\varepsilon)^{-1}$-Regularisierung ungeeignet | ✅ |
| **[O-145-1]** | Cutoff-Finite-Part: $\operatorname{Tr}_\Lambda(R\Sigma)\big|_{\text{fin}} = -\zeta'/\zeta$? | ❓[O] |
| **[O-145-2]** | Wärme-Regularisierung: $\operatorname{Tr}_\varepsilon(R\Sigma)\big|_{\varepsilon\to 0,\text{fin}} = -\zeta'/\zeta$? | ❓[O] |
| **[O-145-3]** | Operatorielle Realisierung mit korrekter Mangoldt-Normierung | ❓[O] |

$$\boxed{\text{Nächste Nummer: NEU-146.}\quad \text{Kandidat: Cutoff-Finite-Part-Rechnung für }\operatorname{Tr}_\Lambda(R\Sigma).}$$

---

## Verweise

- **NEU-144**: $R$ primdiagonal, $\operatorname{Tr}(R\Sigma) = -\zeta'/\zeta$ für $\Re\beta>1$
- **NEU-143**: T2-Abschluss (Edge-Label)
- **NEU-141**: Drei Spurklassen-Ebenen, $R_p \gtrsim p/\log p$
- **NEU-137**: $\Sigma_{\mathrm{rel}}^{\mathrm{ren}} \in \mathcal{S}_1$ für $\Re\beta > 0$
- **NEU-135D**: $|c_p|^2 = O((\log p)^2/p)$
- **NEU-128B**: Warnung $\beta = s$: Weyl-Funktion, keine Metrik
