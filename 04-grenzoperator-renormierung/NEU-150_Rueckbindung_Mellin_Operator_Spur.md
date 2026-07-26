# NEU-150 — Rückbindung des Mellin-Finite-Parts an die Operator-Spur

> Stand: 9. Juli 2026.
> Anschluss: NEU-149 (Restkontrolle $\checkmark[M]$), NEU-148 (Mellin-Darstellung), NEU-145 (regulierte Spur), NEU-144 ($R$ primdiagonal).
> **Kernbefund:** Der geglättete Mellin-Finite-Part ist exakt die operatorielle Primlabel-Regularisierung der Mangoldt-Spur. Das ist jedoch **nicht** dasselbe wie ein $R$-Cutoff.

---

## Leitmotiv

$$\boxed{\operatorname{NEU\text{-}148/149} \Rightarrow \text{Primlabel-Regularisierung} \Rightarrow -\zeta'/\zeta.}$$

$$\boxed{\operatorname{NEU\text{-}148/149} \not\Rightarrow R\text{-Cutoff-Regularisierung.} \quad (\text{Setzt [ZA] voraus.})}$$

---

## 150.0 Ausgangslage

Nach NEU-143/144 gilt:

$$P_pP_q = 0 \;(p\neq q), \qquad \operatorname{Tr}(RP_p) = \log p, \qquad \Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}P_p.$$

Der geglättete Mellin-Cutoff aus NEU-148 ist

$$S_{\varphi,X}(\beta) = \sum_p \varphi(p/X)\,\frac{\log p\, p^{-\beta}}{1-p^{-\beta}}.$$

Das ist eine Primsumme über $p$, kein Cutoff am Operator $R$. Der Zusammenhang zur Operatorspur wird jetzt hergestellt.

---

## 150.1 Der Primlabel-Observable $N_{\mathbb{P}}$

**Definition:**

$$N_{\mathbb{P}}\Psi_p := p\,\Psi_p.$$

Da $\{\Psi_p\}$ ein orthogonales System in $W_{\mathrm{res,rel}}$ bildet (T2, NEU-143) und $p \in \mathbb{R}_{>0}$, ist $N_{\mathbb{P}}$ ein **positiver, selbstadjungierter, unbeschränkter Operator** auf

$$\mathcal{D}(N_{\mathbb{P}}) := \left\{\xi = \sum_p \xi_p\Psi_p \;\Big|\; \sum_p p^2|\xi_p|^2 < \infty\right\}.$$

$N_{\mathbb{P}}$ und $R$ sind beide primdiagonal, aber verschieden: $R_p = \log p/|c_p|^2 \gtrsim p/\log p$, während $N_{\mathbb{P}}$ genau den Primwert $p$ trägt.

---

## 150.2 Operatorielle Formulierung des Primlabel-Cutoffs

Für $\varphi \in C_c^\infty([0,\infty))$ definiere

$$\varphi(N_{\mathbb{P}}/X)\Psi_p = \varphi(p/X)\Psi_p.$$

Dann gilt formal:

$$\operatorname{Tr}\!\left(\varphi(N_{\mathbb{P}}/X)\cdot R\cdot\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right)
= \sum_p \varphi(p/X)\,\frac{p^{-\beta}}{1-p^{-\beta}}\,\operatorname{Tr}(RP_p)
= \sum_p \varphi(p/X)\,\frac{\log p\, p^{-\beta}}{1-p^{-\beta}}.$$

Also:

$$\boxed{\operatorname{Tr}\!\left(\varphi(N_{\mathbb{P}}/X)\cdot R\cdot\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\right) = S_{\varphi,X}(\beta).}$$

Der geglättete Mellin-Cutoff ist **exakt** die operatorielle Primlabel-Regularisierung der Mangoldt-Spur.

---

## 150.3 Zwei Cutoff-Arten: Präzise Unterscheidung

### 150.3.1 Primlabel-Cutoff (kontrolliert)

$$\operatorname{Tr}_{\varphi,X}^{N_{\mathbb{P}}}(R\Sigma) := \operatorname{Tr}\!\left(\varphi(N_{\mathbb{P}}/X)\cdot R\cdot\Sigma(\beta)\right) = S_{\varphi,X}(\beta).$$

Dieser Cutoff ist durch NEU-148/149 vollständig kontrolliert:

$$\operatorname{FP}_{X\to\infty}^{\varphi}\operatorname{Tr}_{\varphi,X}^{N_{\mathbb{P}}}(R\Sigma) = -\frac{\zeta'}{\zeta}(\beta) \qquad\checkmark[M].$$

### 150.3.2 $R$-Cutoff (offen)

$$\operatorname{Tr}_{\varphi,\Lambda}^{R}(R\Sigma) := \operatorname{Tr}\!\left(\varphi(R/\Lambda)\cdot R\cdot\Sigma(\beta)\right) = \sum_p \varphi(R_p/\Lambda)\,\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}.$$

Dieser Cutoff ist nur dann asymptotisch mit dem Primlabel-Cutoff vergleichbar, wenn

$$\text{[ZA]:} \quad R_p \asymp \frac{p}{\log p}, \quad\text{d.h.}\quad |c_p|^2 \asymp \frac{(\log p)^2}{p}.$$

Ohne [ZA] ist $\{p : R_p \leq \Lambda\}$ und $\{p : p \leq X(\Lambda)\}$ nicht kontrolliert vergleichbar.

$$\operatorname{FP}_{\Lambda\to\infty}^{\varphi}\operatorname{Tr}_{\varphi,\Lambda}^{R}(R\Sigma) \stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta) \qquad ?[O] \text{ (setzt [ZA] voraus)}.$$

### 150.3.3 Vergleichstabelle

| Cutoff-Art | Operator | Cutoff-Skala | Status | Abhängigkeit |
|---|---|---|---|---|
| Primlabel | $\varphi(N_{\mathbb{P}}/X)$ | $p \leq X$ | $\checkmark[M]$ NEU-148/149 | keine [ZA] |
| $R$-Cutoff | $\varphi(R/\Lambda)$ | $R_p \leq \Lambda$ | $?[O]$ | [ZA] erforderlich |

---

## 150.4 Verbindung zur Definition NEU-145

Nach NEU-145 ist die regulierte Spur definiert durch analytische Fortsetzung:

$$\operatorname{Tr}_{\mathrm{reg}}(R\Sigma(\beta)) := \operatorname{AC}_{\Re z>1}\!\left[-\frac{\zeta'}{\zeta}(z)\right](\beta) = -\frac{\zeta'}{\zeta}(\beta).$$

NEU-150 zeigt jetzt:

$$\operatorname{FP}_{X\to\infty}^{\varphi}\operatorname{Tr}\!\left(\varphi(N_{\mathbb{P}}/X)\cdot R\cdot\Sigma(\beta)\right) = -\frac{\zeta'}{\zeta}(\beta) = \operatorname{Tr}_{\mathrm{reg}}(R\Sigma(\beta)) \qquad \checkmark[M].$$

Damit ist die **operatorielle Realisierung** der regulierten Spur aus NEU-145 — dort als $?[O]$ markiert — jetzt im Primlabel-Sinn auf $\checkmark[M]$ erhoben:

$$\boxed{\operatorname{Tr}_{\mathrm{reg}}(R\Sigma(\beta)) = \operatorname{FP}_{X\to\infty}^{N_{\mathbb{P}}}\operatorname{Tr}\!\left(\varphi(N_{\mathbb{P}}/X)R\Sigma(\beta)\right) \qquad \checkmark[M].}$$

Die operatorielle Realisierung via $R$-Cutoff bleibt $?[O]$.

---

## 150.5 Statusdiagnose und Arbeitsplan

| Eintrag | Inhalt | Status |
|---|---|---|
| **150.A** | $N_{\mathbb{P}}\Psi_p = p\Psi_p$ als Primlabel-Observable | ✅ |
| **150.B** | $\operatorname{Tr}(\varphi(N_{\mathbb{P}}/X)R\Sigma) = S_{\varphi,X}(\beta)$ | ✅ |
| **150.C** | Primlabel-Finite-Part $= -\zeta'/\zeta$ | ✅[M] (setzt NEU-148/149 voraus) |
| **150.D** | $\operatorname{Tr}_{\mathrm{reg}} = $ Primlabel-FP | ✅[M] Brücke NEU-145 $\to$ NEU-150 |
| **150.E** | $R$-Cutoff $\neq$ Primlabel-Cutoff ohne [ZA] | ✅ (Unterscheidung scharf) |
| **[O-150-1]** | [ZA]: $R_p \asymp p/\log p$ formal beweisen | ❓[O] (benötigt schärfere $|c_p|^2$-Asymptotik) |
| **[O-150-2]** | $R$-Cutoff-Finite-Part $= -\zeta'/\zeta$ unter [ZA] | ❓[O] |
| **[O-150-3]** | Primlabel-Brücke formal (Vertauschung Spur/Integral) | ❓[O] |

$$\boxed{\text{Nächste Nummer: NEU-151.}\quad \text{Kandidat: [ZA] — schärfere Asymptotik von }|c_p|^2\text{, um }R_p \asymp p/\log p\text{ zu beweisen.}}$$

---

## Verweise

- **NEU-149**: Restkontrolle $R_{\varphi,X}\to 0$, $\checkmark[M]$
- **NEU-148**: Mellin-Darstellung, Residuenformel
- **NEU-145**: Regulierte Spur: Definition (AC) und operatorielle Realisierung (jetzt $\checkmark[M]$ im Primlabel-Sinn)
- **NEU-144**: $R$ primdiagonal, $R_p = \log p/|c_p|^2$
- **NEU-143**: T2-Abschluss
- **NEU-135D**: $|c_p|^2 = O((\log p)^2/p)$ (nur obere Schranke; für [ZA] wird untere Schranke benötigt)
