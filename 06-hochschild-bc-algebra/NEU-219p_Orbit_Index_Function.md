# NEU-219p — Normalform der skalaren Rotation und Orbitindexfunktion

## 0. Ergebnis und Ausgangslage

Nach dem Setup NEU-219o ist die Pflichtrechnung für
$$
(t\Phi_\lambda)(a_0,\ldots,a_4) = \widehat{\Omega}_\lambda\bigl(a_4\cdot\widetilde{L}(a_0,a_1,a_2,a_3)\bigr)
$$
durchgeführt. Das Ergebnis ist eine vollständig typisierte Normalform. Der Shift-Exponent $\varepsilon$ folgt nicht aus der linken Multiplikation mit $a_4$, sondern aus dem Unterschied der Orbitindizes.

Der nächste atomare Knoten ist:
$$
\boxed{[O\text{-}219\text{-}5e1h1a\text{-orbit-index-function}]}
$$

---

## 1. Normalform der skalaren Rotation

Sei
$$
\widetilde{L}(a_0,a_1,a_2,a_3) \stackrel{\Psi}{=} x_{0123}\,\delta_{k_{0123}} \in \mathcal{N}_{\mathrm{tag}}.
$$

Die linke $R$-Modulwirkung auf $\mathcal{N}_{\mathrm{tag}}$ lautet (NEU-219n, (11.2)):
$$
a_4 \cdot (x_{0123}\,\delta_{k_{0123}}) = \tau^{-k_{0123}}(a_4)\,x_{0123}\,\delta_{k_{0123}}.
$$

Daher:
$$
\widehat{\Omega}_\lambda\bigl(a_4\cdot\widetilde{L}(a_0,a_1,a_2,a_3)\bigr)
= \lambda^{k_{0123}}\,\varpi_{\beta,\chi}\!\left(\tau^{-k_{0123}}(a_4)\,x_{0123}\right).
$$

Mit der Links-Modulrelation $\varpi(ax) = \varpi(x\,\tau^{-1}(a))$ (Umkehrung von $\varpi(xa) = \varpi(\tau(a)x)$) folgt:

$$
\boxed{(t\Phi_\lambda)(a_0,\ldots,a_4)
= \lambda^{k_{0123}}\,\varpi_{\beta,\chi}\!\left(x_{0123}\,\tau^{-k_{0123}-1}(a_4)\right).}
$$

Das ist die erste vollständig typisierte **Normalform der skalaren Rotation**.

---

## 2. Hauptbefund: Linke $R$-Wirkung ändert den Orbitindex nicht

$$
\boxed{\text{Die linke }R\text{-Wirkung selbst verändert den Orbitindex nicht.}}
$$

Die Multiplikation $a_4 \cdot (x_{0123}\,\delta_{k_{0123}})$ liefert einen Wert in derselben $\delta_{k_{0123}}$-Komponente. Ein Faktor $\lambda^{\pm 1}$ gegenüber $\Phi_\lambda$ kann daher **nur** entstehen, wenn die Orbitindizes
$$
k_{0123} = \kappa(a_0,a_1,a_2,a_3) \qquad \text{und} \qquad k_{1234} = \kappa(a_1,a_2,a_3,a_4)
$$
voneinander abweichen. Präzise:

$$
\boxed{\varepsilon = k_{0123} - k_{1234} = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4).}
$$

Dies ist die vollständige Herkunft von $\varepsilon$; der externe Shift $T^\varepsilon$ entsteht beim Vergleich der beiden Funktionalwerte $\Phi_\lambda$, nicht bei der Multiplikation mit $a_4$.

---

## 3. Nächster atomarer Knoten: `5e1h1a-orbit-index-function`

**Aufgabe:** Bestimme für homogene Argumente $(a_1,a_2,a_3,a_4)$ den exakten Orbitindex
$$
\kappa(a_1,a_2,a_3,a_4)
$$
mit
$$
\widetilde{L}(a_1,a_2,a_3,a_4) \in I_{\kappa(a_1,a_2,a_3,a_4)}.
$$

Erst danach kann $\varepsilon = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4)$ berechnet werden, und erst dann folgt aus der Normalform in §1 der KMS-Exponent $s$ aus der Umformung von $\tau^{-k_{0123}-1}(a_4)$.

**Reihenfolge:**
1. Indexformel $\kappa$ aus der Definition von $\widetilde{L}$
2. $\varepsilon = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4)$
3. $s$ aus KMS-Umformung des Faktors $\tau^{-k_{0123}-1}(a_4)$
4. $C(g,\beta,\lambda) = \lambda^\varepsilon g^{s\beta} = 1 \Rightarrow \lambda^*$

---

## 4. DAG-Status

| Knoten | Status |
|--------|--------|
| `5e1g-tagged-module-weight` | ✓[K/M] |
| $\varpi_{\beta,\chi}$, Eigenfamilie $\Omega_\lambda$ | ✓[K/M] |
| Normalform $(t\Phi_\lambda)$ | ✓[K/M] |
| Linke $R$-Wirkung ändert Orbitindex nicht | ✓[K/M] |
| $\varepsilon = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4)$ | ✓[K/M] |
| `5e1h1-scalar-rotation` | ?[O] |
| `5e1h1a-orbit-index-function` | **?[O] primär** |
| $\kappa(a_1,a_2,a_3,a_4)$ bestimmt | ?[O] |
| $\varepsilon$ explizit berechnet | ?[O] |
| $s$ aus KMS-Umformung bestimmt | ?[O] |
| $\lambda^* = g^{+\beta}$ oder $g^{-\beta}$ | ?[O] |
