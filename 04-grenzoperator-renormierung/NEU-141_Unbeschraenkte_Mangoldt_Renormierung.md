# NEU-141 — Unbeschränkte Mangoldt-Renormierung

> Stand: 8. Juli 2026.  
> Anschluss: NEU-137 (Spurklassen-Summierbarkeit), NEU-135D (Welt-2-Entscheidung), NEU-134 (relative Kanalgewichte).  
> **Kernbefund:** $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$ für $\beta>0$, aber $R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)\in\mathcal{S}_1$ gilt im Mangoldt-normalisierten Sinn **nur** für $\Re\beta>1$.

---

## Leitmotiv

$$\boxed{\mathcal{S}_1\text{-Existenz} \;\neq\; \text{Mangoldt-Spur} \;\neq\; \text{analytisch fortgesetzte Zeta-Spur}.}$$

Das ist die neue scharfe Grenze: Drei konzeptuell verschiedene Spurklassen-Ebenen, die nicht kollabiert werden dürfen.

---

## 141.0 Ausgangssituation

Setze
$$P_p := C_p^{\mathrm{rel}}(C_p^{\mathrm{rel}})^\# .$$

Nach NEU-44.X gilt
$$P_p = |\Psi_p\rangle\langle\Psi_p|, \qquad \operatorname{Tr} P_p = |c_p|^2.$$

Nach NEU-135D gilt
$$|c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right).$$

---

## 141.1 Die Mangoldt-Normierung und ihre Konsequenz

Die direkte Mangoldt-Normierung fordert
$$\operatorname{Tr}(R\,P_p) = \log p.$$

Falls $R$ primkanaldiagonal ist, d.h.
$$R\big|_{\mathbb{C}\Psi_p} = R_p \cdot \mathrm{id},$$
dann folgt
$$R_p\,|c_p|^2 = \log p \implies R_p = \frac{\log p}{|c_p|^2}.$$

Mit dem Wachstum aus NEU-135D ergibt sich
$$\boxed{R_p \;\gtrsim\; \frac{p}{\log p}.}$$

**$R$ ist also unbeschränkt.** Das ist kein Defekt, sondern die korrekte arithmetische Notwendigkeit.

---

## 141.2 Die formale Mangoldt-Spur

Für
$$\sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,P_p$$
ergibt sich formal
$$\operatorname{Tr}\!\left(R \cdot \sum_p \frac{p^{-\beta}}{1-p^{-\beta}}\,P_p\right) = \sum_p \frac{\log p\; p^{-\beta}}{1-p^{-\beta}}.$$

Diese Reihe ist (als gewöhnliche positive Reihe) identisch mit
$$-\frac{\zeta'}{\zeta}(\beta)$$
im Konvergenzbereich $\Re\beta > 1$.

---

## 141.3 Die drei Spurklassen-Ebenen

| Ebene | Objekt | Konvergenzbereich | Status |
|---|---|---|---|
| **S1-Existenz** | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ | $\Re\beta > 0$ | ✅ NEU-137 |
| **Mangoldt-Spur** | $R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ | $\Re\beta > 1$ | ✅ gewöhnlich |
| **Zeta-Spur (reguliert)** | $\operatorname{Tr}_{\mathrm{reg}}(R\,\Sigma)$ | $0 < \Re\beta \leq 1$ | ❓[O] |

**Kritischer Befund:** Sobald $R$ die fehlende Größenordnung $\sim p/\log p$ zurückmultipliziert, verliert man genau die Spurklassen-Summierbarkeit, die NEU-137 gewonnen hatte. Der natürliche Bereich für die Mangoldt-Spur ist zunächst $\Re\beta > 1$.

---

## 141.4 Konsequenz für T2

Falls T2-Orthogonalität gilt:
$$\langle\Psi_p, \Psi_q\rangle = 0 \qquad (p \neq q),$$
dann kann $R$ sauber primkanaldiagonal definiert werden:
$$R\Psi_p = R_p\Psi_p.$$

Falls T2 **scheitert**, ist selbst die Definition eines kanaldiagonalen $R$ nicht mehr kanonisch. Man bräuchte eine biorthogonale oder Gram-invertierte Renormierung — deutlich instabiler. **T2 wird dadurch noch wichtiger.**

---

## 141.5 Arbeitsplan

| Eintrag | Inhalt | Voraussetzung |
|---|---|---|
| **NEU-141.A** | T2-Orthogonalität prüfen | NEU-134, NEU-44.X |
| **NEU-141.B** | $R$ als unbeschränkte primdiagonale Observable definieren | T2 aus 141.A |
| **NEU-141.C** | Gewöhnliche Spur nur für $\Re\beta > 1$ — Dirichlet-Konvergenzbereich | 141.B |
| **NEU-141.D** | Regulierte Spur für $0 < \Re\beta \leq 1$ als Folgeproblem | 141.C + analytische Fortsetzung |

---

## 141.6 Statusdiagnose

$$\boxed{R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) \in \mathcal{S}_1 \text{ im Mangoldt-Sinn} \iff \Re\beta > 1.}$$

Für $0 < \Re\beta \leq 1$ ist eine **regulierte Spur** erforderlich: analytische Fortsetzung, resolventenartige Regularisierung, oder Hadamard-Renormierung. Das ist kein Versagen des Programms — es ist der Punkt, an dem die Zeta-Funktion ihre eigentliche Natur zeigt.

---

## Verweise

- **NEU-137**: Spurklassen-Summierbarkeit $\Sigma_{\mathrm{rel}}^{\mathrm{ren}} \in \mathcal{S}_1$
- **NEU-135D**: Wachstum $|c_p|^2 = O((\log p)^2/p)$
- **NEU-134**: Relative Kanalgewichte
- **NEU-133**: Primschalen-Abel-Mechanismus, H1/H2/H3-rel
- **NEU-128B**: Warnung $\beta = s$: Weyl-Funktion, keine Metrik
