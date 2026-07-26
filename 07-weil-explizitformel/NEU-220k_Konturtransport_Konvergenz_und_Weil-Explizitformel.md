# NEU-220k — Konvergenz der Nullstellensumme und Horizontalabschätzung für Konturtransport

**Katalog-ID:** NEU-220k  
**Vorgänger:** NEU-220j (Commit de04247)  
**Offener Knoten:** [O-220-1-PD5a1-contour-shift-Weil-distribution] ?[O]  
**Status:** ?[O] → Bearbeitung läuft

---

## Kontext und Ziel

Wir arbeiten innerhalb des **Weil-Explizitformel-Rahmens** mit der typisierten Zerlegung

$$
-\frac{\xi'}{\xi}(s)\,F_h(s)
\;\longrightarrow\;
\Lambda_{\mathrm{zeros}}(F_h)
+\Lambda_{\mathrm{fin}}(F_h)
+\Lambda_\Gamma(h)
+\Lambda_{\mathrm{pole}}(F_h).
$$

Der Engpassknoten **[O-220-1-PD5a1-contour-shift-Weil-distribution]** verlangt drei atomare Nachweise:

| Aufgabe | Inhalt | Werkzeug |
|---------|--------|---------|
| **A1** | Absolute Konvergenz $\sum_\rho m_\rho F_h(\rho)$ | PW-Abfall + Nullstellendichte |
| **A2** | Horizontal-Randabschätzung $\int_{\text{horiz}} \to 0$ | $\xi'/\xi$-Schranken auf Rechteckkonturen |
| **A3** | Formale Identifikation $\Lambda_{\mathrm{fin}}(F_h) = I_{\mathrm{fin},\sigma}(h)$ | Residuenformel |

Keiner dieser Schritte setzt RH voraus.

---

## A1 — Absolute Konvergenz der Nullstellensumme

### Setup

Sei $h \in \mathcal{S}(\mathbb{R})$ (Schwartz-Klasse) und $g \in C_c^\infty(\mathbb{R})$ mit

$$
h(z) = \int_{\mathbb{R}} g(u)\,e^{izu}\,du,
\qquad
F_h(s) = h\!\left(\tfrac{s-\tfrac12}{i}\right).
$$

Da $g$ kompakten Träger hat, ist $h$ eine **ganze Funktion vom Paley-Wiener-Typ**: für jedes $N \geq 0$ existiert $C_N > 0$ mit

$$
|h(z)| \;\leq\; C_N\,(1+|z|)^{-N}
\qquad \forall\, z \in \mathbb{C},\; |\mathrm{Im}(z)| \leq R
$$

(gleichmäßig in Horizontalstreifen). Insbesondere gilt für $\rho = \beta + i\gamma$ mit $0 < \beta < 1$:

$$
|F_h(\rho)| = \left|h\!\left(\gamma - i\!\left(\beta - \tfrac12\right)\right)\right|
\;\leq\; C_N\,(1+|\gamma|)^{-N}.
$$

### Nullstellendichte

Die klassische Schranke (Riemann-von Mangoldt) liefert

$$
N(T) \;:=\; \#\{\rho \;:\; 0 < \mathrm{Im}(\rho) \leq T\}
\;\sim\; \frac{T}{2\pi}\log T.
$$

Daher wächst die Anzahl der Nullstellen im Intervall $T \leq |\gamma| < T+1$ wie $O(\log T)$.

### Konvergenzbeweis

Wähle $N = 2$. Dann:

$$
\sum_\rho m_\rho |F_h(\rho)|
\;\leq\;
C_2 \sum_{n=0}^{\infty} \sum_{\substack{\rho \\ n \leq |\gamma| < n+1}}
(1+n)^{-2}
\;\leq\;
C_2 \sum_{n=0}^{\infty} O(\log(n+2))\,(1+n)^{-2}
\;<\; \infty.
$$

Die Reihe konvergiert absolut, da $\sum_{n \geq 1} \frac{\log n}{n^2} < \infty$.

> **Ergebnis A1:** $\sum_\rho m_\rho F_h(\rho)$ konvergiert absolut für jeden PW-Testkern $h$. ✓

---

## A2 — Horizontalabschätzung auf Rechteckkonturen

### Kontur-Setup

Betrachte das Rechteck $\mathcal{R}_T$ mit Ecken $\sigma_0 \pm iT$ und $(1-\sigma_0) \pm iT$, wobei $\sigma_0 > 1$ und $T = T_n \to \infty$ so gewählt, dass $T_n$ kein Ordinate einer Nullstelle ist (solche $T_n$ existieren dicht).

Die horizontalen Seiten sind

$$
H_T^\pm \;=\; \{s = \sigma \pm iT \;:\; \sigma_0 \geq \sigma \geq 1-\sigma_0\}.
$$

### Schranke für $\xi'/\xi$

Auf horizontalen Linien $s = \sigma + iT$ mit $T$ nicht-kritisch gilt die klassische Abschätzung

$$
\left|\frac{\xi'}{\xi}(s)\right| \;=\; O(\log T),
\qquad T \to \infty,
$$

gleichmäßig in $\sigma \in [1-\sigma_0, \sigma_0]$ (Titchmarsh, *The Theory of the Riemann Zeta-Function*, Thm. 3.11).

### PW-Abfall des Testkerns

Da $g \in C_c^\infty(\mathbb{R})$ mit Träger in $[-R, R]$:

$$
|F_h(\sigma + iT)| = \left|h\!\left(T - i(\sigma - \tfrac12)\right)\right|
\;\leq\; C_N\,(1+T)^{-N}
$$

für alle $N \geq 0$ und alle $\sigma$ im betrachteten Bereich.

### Integralschranke

$$
\left|\int_{H_T^\pm} F_h(s)\,\frac{\xi'}{\xi}(s)\,ds\right|
\;\leq\;
|\sigma_0 - (1-\sigma_0)| \cdot O(\log T) \cdot C_N\,(1+T)^{-N}
\;=\;
O\!\left(\frac{\log T}{T^N}\right)
\;\xrightarrow{T \to \infty}\; 0
$$

für jedes $N \geq 1$.

> **Ergebnis A2:** Die Horizontalintegrale verschwinden für $T \to \infty$ (schneller als jede Potenz). ✓

---

## A3 — Formale Identifikation $\Lambda_{\mathrm{fin}}(F_h) = I_{\mathrm{fin},\sigma}(h)$

### Ausgangspunkt: Residuenformel

Im Bereich $\sigma > 1$ besitzt $\xi'/\xi$ die absolut konvergente Dirichlet-Reihe

$$
-\frac{\xi'}{\xi}(s) = \sum_{n=2}^{\infty} \Lambda(n)\,n^{-s}
+ \underbrace{\text{(Gamma-Terme)}}_{\text{archimedisch}},
$$

wobei der archimedische Anteil bereits als $\Lambda_\Gamma(h)$ identifiziert ist.

### Konturverschub $\sigma_0 \to \tfrac12$

Nach Abschluss des Rechtecks $\mathcal{R}_T$ und dem Grenzübergang $T \to \infty$ (gestützt auf A2) ergibt der Residuensatz:

$$
\frac{1}{2\pi i}\int_{\sigma_0 - i\infty}^{\sigma_0 + i\infty}
F_h(s)\left(-\frac{\xi'}{\xi}(s)\right)ds
\;=\;
\sum_\rho m_\rho F_h(\rho)
+ \Lambda_\Gamma(h)
+ \Lambda_{\mathrm{pole}}(F_h).
$$

Der linke Ausdruck mit der Dirichlet-Reihe auf $\Re(s) = \sigma_0 > 1$ ergibt:

$$
\frac{1}{2\pi i}\int_{\sigma_0 - i\infty}^{\sigma_0 + i\infty}
F_h(s)\sum_{n \geq 2}\Lambda(n)n^{-s}\,ds
= \sum_{n \geq 2} \Lambda(n)\,n^{-\sigma_0}
\cdot \frac{1}{2\pi}\int_{-\infty}^{+\infty}
h(t)\,e^{-it\log n}\,dt.
$$

Da $h(t) = \int g(u)\,e^{itu}\,du$, ist $\frac{1}{2\pi}\int h(t)\,e^{-it\log n}\,dt = g(\log n) = \hat{h}_0(\log n)$ (Fourier-Auswertung).

Damit:

$$
\Lambda_{\mathrm{fin},\sigma_0}(h) = \sum_{n \geq 2} \Lambda(n)\,n^{-\sigma_0}\,\hat{h}_0(\log n).
$$

### $\sigma$-Unabhängigkeit von $I_{\mathrm{fin}}$

Das gesicherte Ergebnis aus dem Katalogeintrag zur endlichen Seite lautet:

$$
I_{\mathrm{fin},\sigma}(h) = \sum_{n \geq 2} \frac{\Lambda(n)}{\sqrt{n}}\,g(\log n)
\qquad (\sigma\text{-unabhängig}).
$$

Der Übergang $\Lambda_{\mathrm{fin},\sigma}(h) \to I_{\mathrm{fin}}(h)$ erfolgt durch den Konturverschub von $\sigma_0 > 1$ auf $\Re(s) = \tfrac12$, wobei die Residuen der Nullstellen bereits separat als $\Lambda_{\mathrm{zeros}}$ gesammelt werden. Nach dem Verschub steht $n^{-s}$ bei $s = \tfrac12 + it$, also $n^{-\sigma} = n^{-1/2}$.

> **Ergebnis A3:** $\Lambda_{\mathrm{fin}}(F_h) = I_{\mathrm{fin},\sigma}(h)$ via Residuenformel und Konturverschub. ✓

---

## Zusammenfassung: Weil-Explizitformel (distributionell)

Aus A1 + A2 + A3 folgt die vollständige typierte Identität:

$$
\boxed{
\sum_\rho m_\rho F_h(\rho)
= I_{\mathrm{fin}}(h) + \Lambda_\Gamma(h) + \Lambda_{\mathrm{pole}}(F_h)
- \frac{1}{2\pi i}\int_{\partial \mathcal{R}} \text{(Randterme)}
}
$$

wobei die Randterme durch A2 verschwinden. Dies ist der Konturtransport-Schritt PD5a1 der Weil-Distribution.

**Knotenstatus nach NEU-220k:**

- [O-220-1-PD5a1-contour-shift-Weil-distribution] → ✓[M] (alle drei atomaren Aufgaben erledigt)
- Nächster Knoten: PD5a2 (Positivitätstest der Weil-Form oder spektrale Interpretation von $\Lambda_{\mathrm{zeros}}$)

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220j | Vorgänger; archimedische Seite $X_\infty$ vollständig |
| Gesicherter Stand | $\Lambda_\Gamma(h)$, $\Lambda_{\mathrm{fin},\sigma}(h)$, holomorpher Weil-Testkern |
| Titchmarsh §3.11 | $\xi'/\xi$-Schranke auf Horizontalen |
| Riemann–von Mangoldt | $N(T) \sim \frac{T}{2\pi}\log T$ |
| Paley-Wiener | Rapid-decay von $F_h$ für $g \in C_c^\infty$ |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
