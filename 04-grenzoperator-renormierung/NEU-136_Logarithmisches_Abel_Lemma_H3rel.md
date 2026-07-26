# NEU-136 — Renormalisierte Selbstenergie: Zerlegung, Konvergenz und Topologietest

> Stand: 7. Juli 2026 (finale Form nach NEU-135.D, Spurklassen-Schärfung → NEU-137).  
> Anschluss: NEU-135.D (Welt 2), NEU-133 (Abel-Lemma), NEU-44 (Formel 44.10).

---

## 136.0 Die entscheidende Zerlegung

Aus NEU-44 Formel 44.10:

$$\Sigma_{rel}(\beta) = \sum_p \frac{C_p^{rel}(C_p^{rel})^\sharp}{1-p^{-\beta}}.$$

Mit der kanonischen Identität

$$\frac{1}{1-p^{-\beta}} = 1 + \frac{p^{-\beta}}{1-p^{-\beta}}$$

zerfällt die Selbstenergie in zwei strukturell verschiedene Teile:

$$\boxed{\Sigma_{rel}(\beta) = \underbrace{\sum_p C_p^{rel}(C_p^{rel})^\sharp}_{=:\,\Sigma_{rel}^{\infty}\text{ (roher, }\beta\text{-unabh. Anteil)}} + \underbrace{\sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,C_p^{rel}(C_p^{rel})^\sharp}_{=:\,\Sigma_{rel}^{ren}(\beta)\text{ (renormalisierter Anteil)}}.}$$

**Kritischer Punkt:** Der Euler-Faktor $(1-p^{-\beta})^{-1} \approx 1$ für großes $p$ — er liefert **keine** Dämpfung als Ganzes. Die Dämpfung steckt ausschließlich im zweiten Term durch das explizite $p^{-\beta}$-Gewicht.

$$\boxed{\text{Nicht }\Sigma_{rel}(\beta)\text{ ist endlich, sondern }\Sigma_{rel}^{ren}(\beta).}$$

---

## 136.1 Der rohe Anteil divergiert

$$\Sigma_{rel}^{\infty} := \sum_p C_p^{rel}(C_p^{rel})^\sharp.$$

Mit $\|C_p^{rel}\|^2 = O((\log p)^2/p)$ (Welt-2-Abschätzung, NEU-135.D, vorausgesetzt $R_p = O(1/p)$):

$$\sum_{p\leq N}\|C_p^{rel}\|^2 \sim \sum_{p\leq N}\frac{(\log p)^2}{p} \sim \frac{(\log N)^3}{3} \to \infty.$$

$$\boxed{\Sigma_{rel}^\infty\text{ divergiert (log-kubisch). Er ist der abzuziehende, }\beta\text{-unabhängige Renormierungsanteil.}}$$

---

## 136.2 Der renormalisierte Anteil konvergiert

$$\Sigma_{rel}^{ren}(\beta) := \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,C_p^{rel}(C_p^{rel})^\sharp.$$

Für festes $\beta_0 > 0$ gilt $\frac{p^{-\beta_0}}{1-p^{-\beta_0}} \sim p^{-\beta_0}$ für $p \to \infty$. Damit:

$$\sum_p \left\|\frac{p^{-\beta_0}}{1-p^{-\beta_0}}\,C_p^{rel}(C_p^{rel})^\sharp\right\| \lesssim \sum_p \frac{(\log p)^2}{p^{1+\beta_0}} < \infty.$$

Diese Abschätzung gilt für jedes $\beta_0 > 0$ und jedes $k \geq 0$ (mit $(\log p)^k$ statt $(\log p)^2$).

$$\boxed{\|C_p^{rel}\|^2 = O\!\left(\frac{(\log p)^2}{p}\right) \quad\Longrightarrow\quad \Sigma_{rel}^{ren}(\beta)\text{ konvergiert für jedes feste }\beta > 0\text{, gleichmäßig für }\beta \geq \beta_0 > 0.}$$

---

## 136.3 Verhalten bei $\beta \downarrow 0$ — keine Reparatur

Für $\beta \downarrow 0$ wird $\frac{p^{-\beta}}{1-p^{-\beta}} \to \infty$ für relevante $p$-Bereiche, und die Rohdivergenz kehrt zurück:

$$\Sigma_{rel}^{ren}(\beta) \xrightarrow{\beta \downarrow 0} \text{divergent.}$$

Das ist **kein Defekt**. Es ist die richtige Singularität des Primclock-Gewichts — $\sum_p \log p / p$ divergiert, und $\Sigma_{rel}^{ren}(\beta)$ ist das spektrale Spiegelbild davon.

---

## 136.4 Spurklassen-Schärfung

Falls $C_p^{rel}(C_p^{rel})^\sharp$ positiv und rangendlich (insbesondere rang-eins-artig) ist, gilt:

$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} = \|C_p^{rel}\|^2 \qquad (\text{Rang-1-Fall})$$

bzw. allgemein

$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} \leq \|C_p^{rel}\|^2.$$

Damit erhält NEU-136 sofort eine **Spurklassen-Version**:

$$\boxed{\sum_p \left\|\frac{p^{-\beta}}{1-p^{-\beta}}\,C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} \lesssim \sum_p \frac{(\log p)^2}{p^{1+\beta}} < \infty \quad (\beta > 0).}$$

Das ist stärker als bloße starke Konvergenz und genau passend für Determinanten- und Spurformeln. Die Verifikation dieser Schärfung ist Gegenstand von **NEU-137**.

---

## 136.5 Topologietabelle

Die logische Reihenfolge der Verifikation:

| Schritt | Aussage | Status |
|---|---|---|
| 1 | $\|C_p^{rel}(C_p^{rel})^\sharp\|_{\mathcal{S}_1} \leq \|C_p^{rel}\|^2$ (Rang-Struktur) | ❓[O] → NEU-137 |
| 2 | $\sum_p p^{-\beta_0}\|C_p^{rel}\|^2 < \infty$ (gewichtete Summierbarkeit) | ✓[M] plausibel |
| 3 | $\Sigma_{rel}^{ren}(\beta) \in \mathcal{S}_1$ gleichmäßig für $\beta \geq \beta_0 > 0$ | ❓[O] → NEU-137 |
| 4 | Singularität bei $\beta \downarrow 0$ (strukturell) | ✓[M] erwartet |

| Topologie | Anforderung | Status |
|---|---|---|
| Starke Operatortopologie | vektorweise Konvergenz | ❓[O] |
| Operatornorm | $\sum_p p^{-\beta_0}\|C_p^{rel}\|_{op}^2 < \infty$ | ❓[O] |
| Hilbert-Schmidt $\mathcal{S}_2$ | $\sum_p p^{-\beta_0}\|C_p^{rel}\|_{HS}^2 < \infty$ | ❓[O] |
| Spurklasse $\mathcal{S}_1$ | $\sum_p p^{-\beta_0}\|C_p^{rel}\|^2 < \infty$ + Rangstruktur | ❓[O] → NEU-137 |

---

## 136.6 Statusdiagnose

| Aussage | Status |
|---|---|
| Kanonische Zerlegung $\Sigma_{rel} = \Sigma_{rel}^\infty + \Sigma_{rel}^{ren}$ | ✓[M] |
| $\Sigma_{rel}^\infty$ divergiert (log-kubisch) | ✓[M] — vorausgesetzt $R_p = O(1/p)$ |
| Skalare Konvergenz $\sum_p p^{-\beta_0}\|C_p^{rel}\|^2 < \infty$ | ✓[M] — plausibel |
| Spurklassen-Konvergenz $\Sigma_{rel}^{ren}(\beta) \in \mathcal{S}_1$ | ❓[O] → NEU-137 |
| Gleichmäßigkeit in $\beta \geq \beta_0$ | ❓[O] → NEU-137 |
| Strukturelle Singularität bei $\beta \downarrow 0$ | ✓[M] erwartet |

---

## Fazit

NEU-136 etabliert die kanonische Renormierungsstruktur der relativen Selbstenergie:

$$\boxed{\Sigma_{rel}^{ren}(\beta) = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,C_p^{rel}(C_p^{rel})^\sharp \in \mathcal{S}_1 \quad (\beta > 0) \quad\text{— vorbehaltlich NEU-137.}}$$

Die Stärke: nicht bloße Konvergenz, sondern Spurklassenzugehörigkeit — das Fundament für Determinanten- und Spurformeln im weiteren Programm.

---

## Verweise

- **NEU-135.D**: Welt-2-Entscheidung, $\|\varepsilon_p\|^2 = 1$
- **NEU-44 Formel 44.10**: Selbstenergie-Darstellung
- **NEU-133**: Primschalen-Abel-Lemma (starke Version)
- **NEU-128B**: Warnung $\beta \downarrow 0$
- **NEU-137**: Spurklassen-Verifikation (Folge-Eintrag)
