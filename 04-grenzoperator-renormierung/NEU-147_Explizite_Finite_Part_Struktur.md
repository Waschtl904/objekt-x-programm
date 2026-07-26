# NEU-147 — Explizite-Finite-Part-Struktur der Mangoldt-Spur

> Stand: 9. Juli 2026.
> Anschluss: NEU-146 (Schichtzerlegung, heuristischer Divergenzterm), NEU-145 (regulierte Spur, zwei Ebenen).
> **Kernbefund:** Hauptterm-Finite-Part $\neq$ expliziter Finite-Part. Der Unterschied ist im kritischen Streifen genau der Ort, an dem die Nullstellenstruktur von $\zeta$ — und damit die RH — sitzt.

---

## Leitmotiv

$$\boxed{D_X^{(1)}(\beta) \text{ entfernt nur Pol bei }1. \qquad D_X^{\mathrm{expl}}(\beta) \text{ entfernt zusätzlich Nullstellen-Terme.} \qquad \text{Nur letzteres liefert } -\zeta'/\zeta.}$$

$$\boxed{\text{Hauptterm-Finite-Part} \neq \text{expliziter Finite-Part.}}$$

---

## 147.0 Ausgangslage nach NEU-146

Die Schichtzerlegung

$$S_X(\beta) = \sum_{k\geq 1} T_k(X,\beta), \qquad T_k(X,\beta) := \sum_{p\leq X} \log p\, p^{-k\beta}$$

liefert für $\Re\beta > 1$ im Grenzwert $X\to\infty$ die gewöhnliche Spur $-\zeta'/\zeta(\beta)$. Für $0 < \Re\beta \leq 1$ divergiert $S_X(\beta)$, und NEU-146 hat den heuristischen Divergenzterm

$$D_X^{(1)}(\beta) = \sum_{\substack{k\geq 1\\ \Re(k\beta)<1}} \frac{X^{1-k\beta}}{1-k\beta} + \sum_{\substack{k\geq 1\\ k\beta=1}} \log X$$

(Hauptpol-Subtraktion via PNT-Hauptterm) identifiziert.

NEU-147 zeigt, warum $D_X^{(1)}$ **nicht ausreicht** und formuliert die robustere Route.

---

## 147.1 Präzisierung: Randfall $\Re(k\beta)=1$, $k\beta\neq 1$

Der in NEU-146 formulierte Divergenzterm muss korrigiert werden. Für $\Re(k\beta)=1$, $k\beta \neq 1$ ist der Term

$$\frac{X^{1-k\beta}}{1-k\beta} = \frac{X^{i\cdot\Im(k\beta)}}{1-k\beta}$$

nicht wachsend, aber **oszillierend** in $X$ und besitzt im Allgemeinen **keinen Grenzwert**. Er ist also weder ein Divergenzterm im klassischen Sinne noch vernachlässigbar.

**Korrektur des Divergenzterms aus NEU-146:**

$$\boxed{D_X^{(1)}(\beta) := \sum_{\substack{k\geq 1\\ \Re(k\beta)\leq 1\\ k\beta\neq 1}} \frac{X^{1-k\beta}}{1-k\beta} + \sum_{\substack{k\geq 1\\ k\beta=1}} \log X.}$$

Diese Summe enthält für $\Re(k\beta)=1$, $k\beta\neq 1$ die oszillierenden Terme $X^{i\cdot\Im(k\beta)}/(1-k\beta)$, die explizit mitgeführt werden müssen.

**Status:** $D_X^{(1)}$ entfernt nur den Hauptterm des PNT. Ein Grenzwert $\lim_{X\to\infty}(S_X-D_X^{(1)})$ existiert **nicht** ohne weitere Subtraktion.

---

## 147.2 Hauptterm-Finite-Part: Grenze und Defekt

Sei formal

$$\operatorname{FP}^{(1)}_{X\to\infty} S_X(\beta) := \lim_{X\to\infty}\bigl(S_X(\beta) - D_X^{(1)}(\beta)\bigr).$$

Nach PNT-Hauptterm $(\psi(X) \sim X)$ gilt:

$$T_k(X,\beta) - \frac{X^{1-k\beta}}{1-k\beta} = -\sum_\rho \frac{X^{\rho-k\beta}}{\rho-k\beta} + O(X^{-k\Re\beta}\cdot\mathrm{ET}),$$

wobei $\sum_\rho$ über die nicht-trivialen Nullstellen von $\zeta$ läuft und ET für die trivialen Nullstellen- und Randterme steht.

Der Defekt von $D_X^{(1)}$ im Streifen $0 < \Re\beta \leq 1$ ist genau:

$$S_X(\beta) - D_X^{(1)}(\beta) = -\sum_{k:\,\Re(k\beta)\leq 1}\sum_\rho \frac{X^{\rho-k\beta}}{\rho-k\beta} + (\text{stabile Terme}) + O(\ldots)$$

Diese Nullstellen-Terme $X^{\rho-k\beta}$ sind **nicht** vernachlässigbar, falls

$$\Re(\rho-k\beta) \geq 0 \iff \Re\rho \geq k\,\Re\beta.$$

Für $\Re\beta = 1/2$ und $k=1$: Bedingung $\Re\rho \geq 1/2$ — das ist genau die Grenze der RH.

$$\boxed{\operatorname{FP}^{(1)} S_X = -\zeta'/\zeta(\beta) \text{ gilt im Allgemeinen nicht. Der Rest enthält } X^{\rho-k\beta}\text{-Terme.}}$$

---

## 147.3 Expliziter Finite-Part: vollständige Divergenzsubtraktion

### 147.3.1 Der vollständige Divergenzterm

Ein expliziter Finite-Part muss alle $X$-wachsenden oder -oszillierenden Terme subtrahieren. Aus der expliziten Formel für $\psi(X)$ ergibt sich in jeder Schicht $k$:

$$D_{X,k}^{\mathrm{expl}}(\beta) := \frac{X^{1-k\beta}}{1-k\beta} - \sum_{\rho:\,\Re(\rho-k\beta)\geq 0} \frac{X^{\rho-k\beta}}{\rho-k\beta} + D_{X,k}^{\mathrm{triv}}(\beta),$$

wobei $D_{X,k}^{\mathrm{triv}}$ die Beiträge der trivialen Nullstellen $\rho = -2n$ enthält (falls $\Re(-2n-k\beta)\geq 0$, was für $k\Re\beta$ klein möglich ist).

### 147.3.2 Summation über alle Schichten

$$D_X^{\mathrm{expl}}(\beta) := \sum_{k:\,\Re(k\beta)\leq 1} D_{X,k}^{\mathrm{expl}}(\beta).$$

### 147.3.3 Ziel

$$\boxed{\operatorname{FP}_{X\to\infty}^{\mathrm{expl}} S_X(\beta) := \lim_{X\to\infty}\bigl(S_X(\beta) - D_X^{\mathrm{expl}}(\beta)\bigr) \stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta).}$$

**Status:** $?[O]$ — formaler Beweis erfordert:
1. Konvergenz der $\rho$-Summe nach Subtraktion (hängt von der Anordnung der Nullstellen ab).
2. Nachweis, dass der Limes tatsächlich $-\zeta'/\zeta(\beta)$ ergibt.
3. Behandlung der Sonderfälle $k\beta = 1$ und $\rho = k\beta$.

---

## 147.4 RH-Relevanz der Nullstellen-Terme

Die Bedingung $\Re(\rho-k\beta) \geq 0$ hängt von der Lage der Nullstellen $\rho$ ab:

| Situation | Nullstellen-Term | Verhalten |
|---|---|---|
| $\Re\rho > k\Re\beta$ | $X^{\rho-k\beta} \to \infty$ | Muss subtrahiert werden |
| $\Re\rho = k\Re\beta$ | $|X^{\rho-k\beta}| = 1$ | Oszilliert, muss subtrahiert werden |
| $\Re\rho < k\Re\beta$ | $X^{\rho-k\beta} \to 0$ | Vernachlässigbar |

Unter RH gilt $\Re\rho = 1/2$ für alle nicht-trivialen Nullstellen. Für $k=1$ und $\Re\beta > 1/2$ wäre dann $\Re(\rho-\beta) = 1/2 - \Re\beta < 0$ — **alle** $\rho$-Terme verschwinden, und $D_X^{(1)}$ wäre für $\Re\beta > 1/2$ ausreichend.

Ohne RH: Es gibt (potenziell) Nullstellen mit $\Re\rho > 1/2$, die für $\Re\beta \in (1/2, \Re\rho)$ zusätzliche Divergenzterme liefern.

$$\boxed{D_X^{(1)} \text{ ist genau dann ausreichend für } 1/2 < \Re\beta < 1, \text{ wenn RH gilt.}}$$

Das ist keine Trivialität — es verknüpft die Finite-Part-Stabilität des Cutoffs direkt mit der RH.

---

## 147.5 Robustere Route: Geglätteter Cutoff

### 147.5.1 Motivation

Der scharfe Cutoff $p \leq X$ erzeugt Sprungterme, Rand-Oszillationen und konvergiert schlecht gegen die analytische Fortsetzung. Besser: eine glatte Abschneidefunktion.

### 147.5.2 Definition

Sei $\varphi \in C_c^\infty(0,\infty)$ mit $\varphi(t) = 1$ für $t \leq 1$ und $\varphi(t) = 0$ für $t \geq 2$, normiert durch

$$\int_0^\infty \varphi(t)\,\frac{dt}{t} = 1.$$

Definiere

$$S_{\varphi,X}(\beta) := \sum_p \varphi\!\left(\frac{p}{X}\right) \frac{\log p\, p^{-\beta}}{1-p^{-\beta}}.$$

### 147.5.3 Mellin-Darstellung

Die Mellin-Transformation von $\varphi$ sei $\hat{\varphi}(s) = \int_0^\infty \varphi(t)\, t^{s-1}\,dt$. Dann

$$S_{\varphi,X}(\beta) = \sum_{k\geq 1} \sum_p \varphi\!\left(\frac{p}{X}\right) \log p\, p^{-k\beta}.$$

Mit der Mellin-Inversion auf der Schale $\mathcal{P}_m$ kann jede Schicht als

$$\sum_p \varphi(p/X)\log p\, p^{-k\beta} = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} \hat{\varphi}(s)\, X^s \left(-\frac{d}{ds}\log L_k(s+k\beta)\right)\,ds$$

geschrieben werden (formal), wobei $L_k(s) = \sum_p \log p\, p^{-s}$.

### 147.5.4 Ziel

$$\boxed{\lim_{X\to\infty} S_{\varphi,X}(\beta) \stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta), \qquad\text{unter geeigneter Normierung von }\varphi.}$$

Der geglättete Cutoff hat den Vorteil, dass die Nullstellen-Terme $X^{\rho-k\beta}$ durch den schnellen Abfall von $\hat{\varphi}$ gedämpft werden, falls $\hat{\varphi}$ auf der Linie $\Re(s) = \Re(\rho-k\beta)$ klein ist.

**Status:** $?[O]$ — robustere Route als scharfer Cutoff, aber vollständiger Beweis erfordert Analyse von $\hat{\varphi}$ und Konvergenz der Residuen-Summe.

---

## 147.6 Statusdiagnose und Arbeitsplan

| Eintrag | Inhalt | Status |
|---|---|---|
| **147.A** | Randfall $\Re(k\beta)=1$, $k\beta\neq 1$: Oszillation, kein Grenzwert | ✅ Präzisierung |
| **147.B** | $D_X^{(1)}$ korrigiert: Summe über $\Re(k\beta)\leq 1$, $k\beta\neq 1$ | ✅ |
| **147.C** | $D_X^{(1)}$ liefert Defekt $\sum_\rho X^{\rho-k\beta}/(\rho-k\beta)$ | ✅ |
| **147.D** | RH-Verbindung: $D_X^{(1)}$ ausreichend $\iff$ RH (für $1/2<\Re\beta<1$) | ✅[M] |
| **[O-147-1]** | Vollständiger expliziter Finite-Part $\operatorname{FP}^{\mathrm{expl}}(S_X-D_X^{\mathrm{expl}})=-\zeta'/\zeta$ | ❓[O] |
| **[O-147-2]** | Geglätteter Cutoff: $\lim_{X\to\infty} S_{\varphi,X}(\beta) = -\zeta'/\zeta$ | ❓[O] |
| **[O-147-3]** | Sonderfall $\rho = k\beta$: Residuum-Behandlung | ❓[O] |

$$\boxed{\text{Nächste Nummer: NEU-148.}\quad \text{Kandidaten: (a) formale explizite Formel für }T_k(X,\beta)\text{ via Mangoldt/Selberg; (b) Mellin-Rechnung für }S_{\varphi,X}.}$$

---

## Verweise

- **NEU-146**: Schichtzerlegung, $D_X^{(1)}$ heuristisch (wird hier präzisiert und als unzureichend identifiziert)
- **NEU-145**: Regulierte Spur: Definition (AC) und operatorielle Realisierung (offen)
- **NEU-144**: $R$ primdiagonal, Spurformel
- **NEU-143**: T2-Abschluss
- Riemann-von Mangoldt: Explizite Formel für $\psi(X) = X - \sum_\rho X^\rho/\rho - \log 2\pi - \frac{1}{2}\log(1-X^{-2})$
