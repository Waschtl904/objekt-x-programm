# NEU-219o — Setup: Skalare Rotation und zyklische Orientierung

## 0. Ausgangslage und Entscheidungskriterium

Nach NEU-219n ist die Eigenfamilie
$$
\Omega_\lambda\!\left(\sum_k x_k\delta_k\right) = \sum_k \lambda^k\,\varpi_{\beta,\chi}(x_k)
$$
konstruiert und erfüllt $\Omega_\lambda \circ T = \lambda\,\Omega_\lambda$.

Der primäre offene Knoten lautet:
$$
\boxed{[O\text{-}219\text{-}5e1h1\text{-scalar-rotation}]}
$$

**Pflichtaufgabe:** Berechne direkt
$$
(t\Phi_\lambda)(a_0,\ldots,a_4) = \widehat{\Omega}_\lambda\bigl(a_4\cdot\widetilde{L}(a_0,a_1,a_2,a_3)\bigr)
$$
ausschlie\ss{}lich mit bereits bewiesenen Relationen und bestimme daraus $(\varepsilon, s)$.

**Entscheidungskriterium:**
$$
\boxed{C(g,\beta,\lambda) = \lambda^\varepsilon\,g^{s\beta} = 1,}
$$
wobei $\varepsilon \in \{-1,0,1\}$ und $s \in \{-1,0,1\}$ **unabhängig** aus der Rechnung folgen müssen.

---

## 1. Vollständige Fallmatrix

Aus $C(g,\beta,\lambda) = \lambda^\varepsilon g^{s\beta}$ mit $\varepsilon, s \in \{-1,0,1\}$ entstehen neun Fälle:

| $(\varepsilon, s)$ | $C(g,\beta,\lambda)$ | Lösung von $C=1$ | Bemerkung |
|---|---|---|---|
| $(1,-1)$ | $\lambda g^{-\beta}$ | $\lambda = g^{+\beta}$ | |
| $(-1,-1)$ | $\lambda^{-1}g^{-\beta}$ | $\lambda = g^{-\beta}$ | |
| $(0,-1)$ | $g^{-\beta}$ | unmöglich für $g\neq 1$ | strukturell auszuschließen |
| $(1,0)$ | $\lambda$ | $\lambda = 1$ | kein Orbitgewicht |
| $(-1,0)$ | $\lambda^{-1}$ | $\lambda = 1$ | kein Orbitgewicht |
| $(0,0)$ | $1$ | jedes $\lambda$ | kein Twist; trivial |
| $(1,+1)$ | $\lambda g^{+\beta}$ | $\lambda = g^{-\beta}$ | |
| $(-1,+1)$ | $\lambda^{-1}g^{+\beta}$ | $\lambda = g^{+\beta}$ | |
| $(0,+1)$ | $g^{+\beta}$ | unmöglich für $g\neq 1$ | strukturell auszuschließen |

**Bemerkung.** Die vier Zeilen mit $s \in \{-1,0\}$ bilden die bisher notierte Teilmatrix. Der Fall $s = +1$ bleibt formal offen bis zur vollständigen Modulrechnung.

---

## 2. Zwei Wege — Weg A ist kanonisch

Ein modulwertiger zyklischer Operator $\mathcal{T}_{\mathrm{mod}}$ auf $C^4(A, \widetilde{M}_{\mathrm{orb}})$ ist **nicht automatisch definiert**. Eine Bimodulstruktur und der Automorphismus $\tau$ allein bestimmen keine kanonische Rotation des modulwertigen Kozykelwerts.

### Weg A — Direkte skalare Rotation (kanonisch)

Definiere zuerst das skalare Funktional
$$
\Phi_\lambda(a_0,\ldots,a_4) = \widehat{\Omega}_\lambda\bigl(a_0\cdot\widetilde{L}(a_1,\ldots,a_4)\bigr).
$$

Dann ist der skalare zyklische Operator **eindeutig** definiert:
$$
(t\Phi_\lambda)(a_0,\ldots,a_4) = (-1)^4\,\Phi_\lambda(a_4,a_0,a_1,a_2,a_3).
$$

Da $(-1)^4 = 1$:
$$
\boxed{(t\Phi_\lambda)(a_0,\ldots,a_4) = \widehat{\Omega}_\lambda\bigl(a_4\cdot\widetilde{L}(a_0,a_1,a_2,a_3)\bigr).}
$$

An diesem Ausdruck werden ausschließlich bereits bewiesene Relationen angewandt:
- Modulare Bimodulidentität: $\varpi_{\beta,\chi}(xa) = \varpi_{\beta,\chi}(\tau(a)x)$
- $\tau$-Invarianz: $\varpi_{\beta,\chi}\circ\tau = \varpi_{\beta,\chi}$
- Shift-Eigenschaft: $\Omega_\lambda\circ T = \lambda\,\Omega_\lambda$
- Hochschild-Kozykelgleichung von $\widetilde{L}$

Dieser Weg benötigt **keinen vorab postulierten modulwertigen zyklischen Operator**.

### Weg B — Echter $\mathcal{T}_{\mathrm{mod}}$ (nur bei separater Typisierung)

Soll
$$
\mathcal{T}_{\mathrm{mod}}: C^4(A,\widetilde{M}_{\mathrm{orb}}) \to C^4(A,\widetilde{M}_{\mathrm{orb}})
$$
verwendet werden, müssen zusätzlich konstruiert und bewiesen werden:
- eine Koeffizientenstruktur, die die Rotation wohldefiniert macht,
- Wohldefiniertheit (Unabhängigkeit von Darstellungen),
- Potenzrelation $\mathcal{T}_{\mathrm{mod}}^5 = \mathrm{id}$ oder Variante,
- Kompatibilität mit dem Hochschild-Randoperator $b$.

Links- und Rechts-Twist sind in Weg B keine blossen Konventionen, sondern zwei verschiedene Kandidaten mit verschiedenen Wohldefiniertheitspflichten. **Weg B wird nur beschritten, wenn seine Koeffizientenstruktur separat typkorrekt konstruiert wurde.**

---

## 3. Bindender Auditablauf für Knoten `5e1h1`

Für einen homogenen Testwert $\widetilde{L}(a_0,a_1,a_2,a_3)$ sind **getrennt** zu dokumentieren:

### Schritt 1 — Ausschreiben von $(t\Phi_\lambda)(a_0,\ldots,a_4)$

Explizite Umformung von
$$
\widehat{\Omega}_\lambda\bigl(a_4\cdot\widetilde{L}(a_0,a_1,a_2,a_3)\bigr)
$$
mit der linken $R$-Modulwirkung auf $\mathcal{N}_{\mathrm{tag}}$ und den Relationen aus §4.

### Schritt 2 — Bestimmung von $\varepsilon$

Aus dem Zielindex: liegt der transformierte Wert in der $\delta_{k+1}$-, $\delta_{k-1}$- oder $\delta_k$-Komponente?
$$
\Rightarrow\quad \varepsilon \in \{-1,0,1\}.
$$

### Schritt 3 — Bestimmung von $s$

Aus der KMS-Relation auf dem entstehenden Twistfaktor:
$$
\widehat{\Omega}_\lambda(\Xi) = g^{s\beta}\,\widehat{\Omega}_\lambda(\xi), \qquad s \in \{-1,0,1\}.
$$

### Schritt 4 — Entscheidung

$$
C(g,\beta,\lambda) = \lambda^\varepsilon\,g^{s\beta}.
$$
$$
\lambda^\varepsilon\,g^{s\beta} = 1 \quad\Longrightarrow\quad \lambda^*.
$$

Knoten `5e1h1` ist geschlossen, wenn $\varepsilon$, $s$ und $\lambda^*$ explizit berechnet sind.

---

## 4. Relevante Formeln aus NEU-219n

- $\tau(U_{g^{-1}}) = g^{-\beta}U_{g^{-1}}$
- $U_{g^{-1}}\cdot(x\delta_k) = g^{k\beta}U_{g^{-1}}x\,\delta_k$
- $T(x\delta_k) = x\delta_{k+1}$; $\quad T^{-1}(x\delta_k) = x\delta_{k-1}$
- $\widetilde{\omega}_{\beta,\chi}(ab) = \widetilde{\omega}_{\beta,\chi}(\widetilde{\sigma}_\beta(b)\,a)$
- $\varpi_{\beta,\chi}(xa) = \varpi_{\beta,\chi}(\tau(a)x)$
- $\varpi_{\beta,\chi}\circ\tau = \varpi_{\beta,\chi}$
- $\Omega_\lambda\circ T = \lambda\,\Omega_\lambda$

---

## 5. DAG-Status

| Knoten | Status |
|--------|--------|
| `5e1e-corner-core` | ✓[K/M] |
| `5e1f-orbit-directness` | ✓[M]\_neg |
| globale $\Pi$-Injektivität | ✓[M]\_neg |
| orbit-markierte Realisierung $\mathcal{N}_{\mathrm{tag}}$ | ✓[K/M] |
| `5e1g-tagged-module-weight` | ✓[K/M] |
| $\varpi_{\beta,\chi}$, Eigenfamilie $\Omega_\lambda$ | ✓[K/M] |
| $U_{g^{-1}} = T^{-1}$ auf $\mathcal{N}_{\mathrm{tag}}$ | ✓[M]\_neg |
| `5e1h-tagged-cyclic-orientation` (Elternknoten) | ?[O] |
| `5e1h1-scalar-rotation` | **?[O] primär** |
| $\varepsilon$ bestimmt | ?[O] |
| $s$ bestimmt | ?[O] |
| $\lambda^* = g^{+\beta}$ | ?[O] |
| $\lambda^* = g^{-\beta}$ | ?[O] |
| Weg B: echter $\mathcal{T}_{\mathrm{mod}}$ | nicht begonnen; nur bei sep. Typisierung |
