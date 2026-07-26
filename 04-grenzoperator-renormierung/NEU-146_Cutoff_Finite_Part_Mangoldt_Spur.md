# NEU-146 — Cutoff-Finite-Part der Mangoldt-Spur

> Stand: 9. Juli 2026.
> Anschluss: NEU-145 (regulierte Mangoldt-Spur, zwei Ebenen), NEU-144 ($R$ primdiagonal), NEU-135D ($|c_p|^2$-Wachstum).
> **Kernaufgabe:** Divergenzstruktur von $S_X(\beta) = \sum_{p\leq X} \frac{\log p\, p^{-\beta}}{1-p^{-\beta}}$ für $0<\Re\beta\leq 1$ isolieren und Finite-Part-Test gegen $-\zeta'/\zeta(\beta)$ formulieren.

---

## Leitmotiv

$$\boxed{\operatorname{FP}_{X\to\infty}\, S_X(\beta) \stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta) \qquad (0 < \Re\beta \leq 1).}$$

Dies ist **nicht** sofort behauptet, sondern als offener Test formuliert. NEU-146 isoliert zunächst die Divergenzstruktur präzise.

---

## 146.0 Ausgangslage und Schichtung

Nach NEU-143/144 gilt $P_pP_q = 0$ und $\operatorname{Tr}(RP_p) = \log p$, also

$$\operatorname{Tr}\bigl(R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\bigr) = \sum_p \frac{\log p\, p^{-\beta}}{1-p^{-\beta}}, \qquad \Re\beta > 1.$$

Schreibe mit $\frac{1}{1-p^{-\beta}} = \sum_{k\geq 0} p^{-k\beta}$:

$$\sum_p \frac{\log p\, p^{-\beta}}{1-p^{-\beta}} = \sum_{k\geq 1} \sum_p \log p\, p^{-k\beta}.$$

Jede $k$-te Schicht ist für sich die Dirichlet-Reihe

$$L_k(\beta) := \sum_p \log p\, p^{-k\beta} = -\frac{d}{d(k\beta)}\log\prod_p (1-p^{-k\beta})^{-1}\bigg|_{\text{prim-Anteil}},$$

die im Halbraum $\Re(k\beta) > 1$ konvergiert.

$$\boxed{\text{Die }k\text{-te Schicht ist divergent genau dann, wenn }\Re(k\beta) \leq 1.}$$

---

## 146.1 Zwei-Schichten-Warnung: $R$-Cutoff vs. Primzahl-Cutoff

### 146.1.1 Der $R$-Cutoff (NEU-145)

Der in NEU-145 definierte Cutoff

$$\operatorname{Tr}_\Lambda\bigl(R\Sigma(\beta)\bigr) := \sum_{p:\, R_p\leq \Lambda} \frac{\log p\, p^{-\beta}}{1-p^{-\beta}}$$

ist der theoretisch sauberere, weil er direkt am Operator $R$ ansetzt.

### 146.1.2 Der Primzahl-Cutoff (Modellfall)

Für konkrete Rechnungen ersetzen wir vorläufig durch den Primzahl-Cutoff:

$$S_X(\beta) := \sum_{p\leq X} \frac{\log p\, p^{-\beta}}{1-p^{-\beta}}.$$

### 146.1.3 Übersetzung: Wann sind beide Cutoffs äquivalent?

Die Bedingung $R_p \leq \Lambda$ bedeutet $\frac{\log p}{|c_p|^2} \leq \Lambda$. Nach NEU-135D gilt nur

$$|c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right) \implies R_p \gtrsim \frac{p}{\log p}.$$

Daraus folgt: $\{p : R_p \leq \Lambda\} \subseteq \{p : p \lesssim \Lambda\log\Lambda\}$.

Aber **ohne** eine schärfere Asymptotik von $|c_p|^2$ kann man nicht schreiben:

$$R_p \leq \Lambda \quad\sim\quad p \leq \Lambda\log\Lambda.$$

$$\boxed{\text{Zusätzliche Annahme [ZA] erforderlich: } R_p \asymp \frac{p}{\log p}, \text{ d.h. } |c_p|^2 \asymp \frac{(\log p)^2}{p}.}$$

Unter [ZA] sind $R$-Cutoff und Primzahl-Cutoff asymptotisch äquivalent:

$$R_p \leq \Lambda \iff p \leq (c + o(1))\,\Lambda\log\Lambda \qquad (\Lambda\to\infty).$$

**Status von [ZA]:** $\checkmark[M]$ als strukturelle Erwartung aus der Feshbach-/Schur-Konstruktion, aber $?[O]$ als formaler Beweis.

---

## 146.2 Modellfall: Primzahl-Cutoff $S_X(\beta)$

### 146.2.1 Schichtzerlegung des Cutoffs

$$S_X(\beta) = \sum_{k\geq 1} T_k(X,\beta), \qquad T_k(X,\beta) := \sum_{p\leq X} \log p\, p^{-k\beta}.$$

Jede Schicht $T_k$ divergiert, falls $\Re(k\beta) \leq 1$.

### 146.2.2 Haupttermheuristik via PNT

Aus dem Primzahlsatz $\psi(X) = \sum_{p\leq X}\log p + O(\text{höhere Potenzen}) \sim X$ folgt formal:

$$T_k(X,\beta) = \sum_{p\leq X} \log p\, p^{-k\beta} \sim \int_2^X t^{-k\beta}\,dt \quad (\Re(k\beta) < 1).$$

Daher:

$$T_k(X,\beta) \sim \frac{X^{1-k\beta}}{1-k\beta}, \qquad \Re(k\beta) < 1.$$

Für $k\beta = 1$ (Sonderfall): $T_k(X,\beta) \sim \log X$.

### 146.2.3 Divergente Schichten im kritischen Streifen

Im Streifen $0 < \Re\beta \leq 1$ sind genau diejenigen $k$ divergent, für die

$$\Re(k\beta) \leq 1 \iff k \leq \frac{1}{\Re\beta}.$$

Die Menge der divergenten Schichten ist $\{1, 2, \ldots, k_{\max}\}$ mit

$$k_{\max} = \left\lfloor \frac{1}{\Re\beta} \right\rfloor.$$

Beispiele:

| $\Re\beta$ | Divergente Schichten | $D_X(\beta)$ Hauptterm |
|---|---|---|
| $1/2 < \Re\beta \leq 1$ | nur $k=1$ | $\frac{X^{1-\beta}}{1-\beta}$ |
| $1/3 < \Re\beta \leq 1/2$ | $k=1,2$ | $\frac{X^{1-\beta}}{1-\beta} + \frac{X^{1-2\beta}}{1-2\beta}$ |
| $1/4 < \Re\beta \leq 1/3$ | $k=1,2,3$ | $\sum_{k=1}^3 \frac{X^{1-k\beta}}{1-k\beta}$ |
| allgemein | $k = 1,\ldots, k_{\max}$ | $\sum_{k=1}^{k_{\max}} \frac{X^{1-k\beta}}{1-k\beta}$ |

Für $k\beta \in \mathbb{Z}$ (Sonderfälle) tritt logarithmische Divergenz auf; die Formel ist durch $\log X$ zu ersetzen.

---

## 146.3 Heuristischer Divergenzterm

**Definition (heuristisch):**

$$\boxed{D_X(\beta) := \sum_{\substack{k\geq 1 \\ \Re(k\beta) < 1}} \frac{X^{1-k\beta}}{1-k\beta} + \sum_{\substack{k\geq 1 \\ k\beta = 1}} \log X.}$$

Diese Summe hat endlich viele Terme (da $k\leq 1/\Re\beta < \infty$).

**Finite-Part-Test:**

$$\operatorname{FP}_{X\to\infty}\, S_X(\beta)
:= \lim_{X\to\infty}\bigl(S_X(\beta) - D_X(\beta)\bigr)
\stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta).$$

Dies ist das zentrale offene Problem von NEU-146.

---

## 146.4 Verbindung zur expliziten Formel

Der Ansatz ist nicht neu: Die explizite Formel von Riemann-von Mangoldt liefert

$$\psi(X) := \sum_{p^k \leq X} \log p = X - \sum_\rho \frac{X^\rho}{\rho} - \log(2\pi) - \frac{1}{2}\log(1-X^{-2}),$$

wobei $\sum_\rho$ über die nicht-trivialen Nullstellen läuft. Die Finite-Part-Identität für $S_X(\beta)$ sollte ähnlich eine Summe über Nullstellen $\rho$ von $\zeta$ produzieren.

Die Verbindung ist: $-\zeta'/\zeta(\beta)$ hat Pole bei $\beta = \rho$ (Nullstellen von $\zeta$), und der Finite-Part-Limes müss genau die Pole-Residuenstruktur der analytischen Fortsetzung reproduzieren.

$$\boxed{\text{Der Finite-Part-Test ist die operative Form der expliziten Formel für den Primkantenraum.}}$$

---

## 146.5 Implikationskette und offene Punkte

$$\underbrace{\operatorname{FP}_{X\to\infty} S_X(\beta) = -\zeta'/\zeta(\beta)}_{\text{[O-146-1]: Primzahl-Cutoff}} \;+\; \underbrace{R_p \asymp p/\log p}_{\text{[ZA]}} \;\Longrightarrow\; \underbrace{\operatorname{FP}_{\Lambda\to\infty}\operatorname{Tr}_\Lambda(R\Sigma) = -\zeta'/\zeta(\beta)}_{\text{[O-146-2]: $R$-Cutoff}}.$$

---

## 146.6 Statusdiagnose und Arbeitsplan

| Eintrag | Inhalt | Status |
|---|---|---|
| **146.A** | Schichtzerlegung $S_X = \sum_k T_k$ | ✅ |
| **146.B** | Divergente Schichten: $k \leq 1/\Re\beta$ | ✅ |
| **146.C** | Haupttermheuristik $T_k \sim X^{1-k\beta}/(1-k\beta)$ via PNT | ✅[M] |
| **146.D** | Heuristischer Divergenzterm $D_X(\beta)$ | ✅[M] |
| **[ZA]** | Zusätzliche Annahme $R_p \asymp p/\log p$ | ✅[M], $?[O]$ |
| **[O-146-1]** | $\operatorname{FP}_{X\to\infty}(S_X - D_X) = -\zeta'/\zeta$ | ❓[O] |
| **[O-146-2]** | $\operatorname{FP}_{\Lambda\to\infty}\operatorname{Tr}_\Lambda(R\Sigma) = -\zeta'/\zeta$ | ❓[O], setzt [ZA] + [O-146-1] voraus |
| **[O-146-3]** | Logarithmische Sonderfälle $k\beta \in \mathbb{Z}$ präzis behandeln | ❓[O] |

$$\boxed{\text{Nächste Nummer: NEU-147.}\quad \text{Kandidat: formaler Beweis von [O-146-1] via explizite Formel oder Abel-Summation.}}$$

---

## Verweise

- **NEU-145**: Regulierte Mangoldt-Spur, zwei Ebenen; $(R+\varepsilon)^{-1}$ ungeeignet
- **NEU-144**: $R$ primdiagonal, Spurformel für $\Re\beta > 1$
- **NEU-141**: Drei Spurklassen-Ebenen, $R_p \gtrsim p/\log p$
- **NEU-135D**: $|c_p|^2 = O((\log p)^2/p)$
- Riemann-von Mangoldt: Explizite Formel für $\psi(X)$
