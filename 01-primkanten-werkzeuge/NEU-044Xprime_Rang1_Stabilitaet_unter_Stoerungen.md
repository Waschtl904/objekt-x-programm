# NEU-44.X' — Rang-1-Stabilität von $C_p^{rel}$ unter Störungen

> Stand: 8. Juli 2026.  
> Anschluss: NEU-44.X (Rang-1-Beweis), NEU-137 (Spurklasse).

---

## Fragestellung

NEU-44.X zeigt: $C_p^{rel} = c_p \cdot (e_1^{(p)} \otimes f_3^{(p)*})$ hat Rang 1 unter der Annahme, dass $c_p$ ein skalarer Koeffizient ist. Dieser Eintrag prüft: Ist die Rang-1-Eigenschaft stabil unter den Approximationen in NEU-127 (Gramform-Triage) und NEU-123 (Jacobi-Grenzoperator)?

---

## 44.X'.1 Rang-1 in der Lanczos-Hierarchie

Der Jacobi-Grenzoperator $J_\infty$ (NEU-123) hat Kanalgewichte der Form

$$c_p^{(N)} \xrightarrow{N \to \infty} c_p,$$

wobei jedes $c_p^{(N)} \in \mathbb{C}$ skalar ist. Damit gilt:

$$C_p^{rel,(N)} = c_p^{(N)} \cdot (e_1^{(p)} \otimes f_3^{(p)*}) \quad\text{(Rang 1 für jedes }N\text{)},$$

und der Grenzoperator $C_p^{rel} = \lim_{N \to \infty} C_p^{rel,(N)}$ ist wieder Rang 1, da die Rang-1-Eigenschaft unter normkonvergenten Grenzwerten erhalten bleibt.

---

## 44.X'.2 Gramform-Triage und Rang-Erhaltung

NEU-127 zerlegt die Gram-Form in Haupt- und Restanteil. Der Restanteil trägt zu $C_p^{rel}$ durch additive Korrekturen $\delta C_p^{rel}$ bei. Falls $\delta C_p^{rel}$ ebenfalls Rang $\leq 1$ hat — was aus der Projektionsstruktur folgt — bleibt $C_p^{rel} + \delta C_p^{rel}$ von Rang $\leq 2$.

**Präzisierung:** Für die Spurklassen-Abschätzung in NEU-137 genügt endlicher Rang. Selbst wenn $C_p^{rel}$ Rang $r < \infty$ hat, gilt:

$$\left\|C_p^{rel}(C_p^{rel})^\sharp\right\|_{\mathcal{S}_1} = \|C_p^{rel}\|_{\mathcal{S}_2}^2 \leq r \cdot \|C_p^{rel}\|^2.
$$

Da $r$ uniformly beschränkt ist (in $p$), bleibt die Summierbarkeit $\sum_p (\log p)^2/p^{1+\beta}$ erhalten.

---

## 44.X'.3 Statusdiagnose

| Aussage | Status |
|---|---|
| Rang-1 im Lanczos-Limes | ✓[V] |
| Rang-Erhaltung unter Gramform-Triage (Rang $\leq$ const) | ✓[M] plausibel |
| Spurklassen-Abschätzung gültig für endlichen Rang | ✓[V] |

---

## Verweise

- **NEU-44.X**: Rang-1-Beweis im idealen Fall
- **NEU-127**: Gramform-Triage
- **NEU-123**: Jacobi-Grenzoperator
- **NEU-137**: Spurklassen-Verwendung
- **NEU-44.R**: Rückbindung an NEU-137.5, Statusupdate
