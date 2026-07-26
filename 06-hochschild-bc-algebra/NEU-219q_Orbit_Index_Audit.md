# NEU-219q — Auditrahmen für die Orbitindexfunktion $\kappa$

## 0. Ausgangslage

Nach NEU-219p ist die Normalform der skalaren Rotation
$$
(t\Phi_\lambda)(a_0,\ldots,a_4) = \lambda^{k_{0123}}\,\varpi_{\beta,\chi}\!\left(x_{0123}\,\tau^{-k_{0123}-1}(a_4)\right)
$$
etabliert, und es gilt
$$
\varepsilon = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4).
$$

Der primäre offene Knoten ist:
$$
\boxed{[O\text{-}219\text{-}5e1h1a\text{-orbit-index-function}]}
$$

**Pflicht:** Aus der wortgetreuen Definition von $\widetilde{L}$ eine Stützungsformel
$$
\boxed{\widetilde{L}(a_1,a_2,a_3,a_4) \in I_{\kappa(a_1,a_2,a_3,a_4)}}
$$
für homogene Eingaben beweisen.

**Verboten:** $\kappa$ aus der $\Gamma$-Ladung des Kozykelwerts herleiten oder raten. Die Orbitmarkierung $k$ und die Gruppengraduierung $\deg(x) = h \in \mathbb{Q}_+^\times$ sind verschiedene Daten. Aus
$$
\widetilde{L}(a_1,\ldots,a_4)\text{ hat Grad }g
$$
folgt keine Aussage wie $\kappa = 1$.

---

## 1. Drei strikt zu unterscheidende Fälle

Der Audit muss zwischen folgenden Ergebnissen unterscheiden und darf keinen davon vorab ausschließen:

### Fall 1 — Konstanter Basissummand
$$
\kappa(a_1,\ldots,a_4) = 0.
$$
Dann ist $\varepsilon = 0$, und ein nichttrivialer KMS-Faktor könnte durch kein Orbitgewicht kompensiert werden. Der Knoten `5e1h1` wäre mit einem negativen Ergebnis zu schließen.

### Fall 2 — Eingabeabhängiger Orbitindex
$$
\kappa = \kappa(\deg a_1, \ldots, \deg a_4).
$$
Die Formel muss vollständig aus dem Liftmechanismus folgen; sie darf nicht postuliert werden.

### Fall 3 — Mehrere Orbitkomponenten
$$
\widetilde{L}(a_1,\ldots,a_4) = \sum_{k\in F} x_k\delta_k, \qquad |F| > 1.
$$
In diesem Fall existiert keine einzelne Indexfunktion $\kappa$. Der Eigenwertvergleich aus NEU-219p muss komponentenweise reformuliert werden. **Dieser Fall darf nicht stillschweigend ausgeschlossen werden.**

---

## 2. Minimale Orbitindex-Buchführung

Für jede in $\widetilde{L}$ verwendete Operation ist die Änderung des Orbitindex zu notieren:

| Operation | Änderung des Orbitindex |
|-----------|------------------------|
| $R$-Links-/Rechtswirkung | $0$ |
| $\tau$ | $+1$ |
| $\tau^{-1}$ | $-1$ |
| $T$ | $+1$ |
| $T^{-1}$ | $-1$ |
| Einbettung $j_M: M \to I_0$ | $0$ |

Die Anzahl der tatsächlich auftretenden $\tau^{\pm 1}$- bzw. $T^{\pm 1}$-Operationen in der Definition von $\widetilde{L}$ ist **algebraisch zu zählen**. Erst die Nettosumme dieser Zählung liefert $\kappa(a_1,\ldots,a_4)$.

---

## 3. Bindender Ablauf für Knoten `5e1h1a`

1. **Wortgetreue Definition von $\widetilde{L}$** aus dem bisherigen DAG-Stand zitieren.
2. **Buchführung** nach Tabelle §2 für jeden Operationsschritt in der Definition.
3. **Fallentscheidung** zwischen Fall 1, 2 oder 3.
4. Im Fall 2: vollständige Formel für $\kappa(\deg a_1,\ldots,\deg a_4)$.
5. Im Fall 3: komponentenweise Reformulierung des Eigenwertvergleichs.
6. **Erst dann:** $\varepsilon = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4)$ berechnen.

Ohne Schritt 1 ist keine Aussage über $\kappa$ mathematisch gestützt.

---

## 4. DAG-Status

| Knoten | Status |
|--------|--------|
| `5e1g-tagged-module-weight` | ✓[K/M] |
| Normalform $(t\Phi_\lambda)$ | ✓[K/M] |
| Linke $R$-Wirkung ändert Orbitindex nicht | ✓[K/M] |
| $\varepsilon = \kappa(a_0,a_1,a_2,a_3) - \kappa(a_1,a_2,a_3,a_4)$ | ✓[K/M] |
| Orbitindex-Buchführung (Tabelle §2) | ✓[K/M] |
| `5e1h1-scalar-rotation` | ?[O] |
| `5e1h1a-orbit-index-function` | **?[O] primär** |
| Fall 1 ($\kappa = 0$) ausgeschlossen | ?[O] |
| Fall 2 ($\kappa$ eingabeabhängig, Formel) | ?[O] |
| Fall 3 (mehrere Komponenten) ausgeschlossen | ?[O] |
| $\varepsilon$ explizit berechnet | ?[O] |
| $s$ aus KMS-Umformung bestimmt | ?[O] |
| $\lambda^*$ bestimmt | ?[O] |
