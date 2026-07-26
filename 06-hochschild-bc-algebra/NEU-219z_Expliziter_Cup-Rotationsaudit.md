# NEU-219z — Expliziter Cup-Rotationsaudit

**Status:** Global freigegeben  
**Primärer Unterknoten:** `[O-219-5e1j-unit-slot-witness]`

---

## 1. Homogene Normalform von Θ∧

Für homogene Elemente $a_i \in (A_{\mathrm{alg}})_{h_i}$ gilt

$$\delta_p^{(0)}(a_i) = v_p(h_i)\log(p)\, a_i.$$

Daher haben alle sechs Summanden von $\Theta^\wedge$ dieselbe Produktreihenfolge $a_i a_j a_k$. Definiere

$$\Delta_{\mathbf{p}}(h_i, h_j, h_k) := \det \begin{pmatrix}
v_{p_1}(h_i)\log p_1 & v_{p_1}(h_j)\log p_1 & v_{p_1}(h_k)\log p_1 \\
v_{p_2}(h_i)\log p_2 & v_{p_2}(h_j)\log p_2 & v_{p_2}(h_k)\log p_2 \\
v_{p_3}(h_i)\log p_3 & v_{p_3}(h_j)\log p_3 & v_{p_3}(h_k)\log p_3
\end{pmatrix}.$$

Dann gilt exakt:

$$\boxed{\Theta^\wedge(a_i, a_j, a_k) = \Delta_{\mathbf{p}}(h_i, h_j, h_k)\, a_i a_j a_k.}$$

Äquivalent:

$$\Delta_{\mathbf{p}}(h_i,h_j,h_k) = \left(\prod_{r=1}^3 \log p_r\right) \det \begin{pmatrix}
v_{p_1}(h_i) & v_{p_1}(h_j) & v_{p_1}(h_k) \\
v_{p_2}(h_i) & v_{p_2}(h_j) & v_{p_2}(h_k) \\
v_{p_3}(h_i) & v_{p_3}(h_j) & v_{p_3}(h_k)
\end{pmatrix}.$$

Der Cup-Kozykel reduziert sich damit auf:

$$L^{\mathrm{cup}}(a_1,a_2,a_3,a_4) = \Delta_{\mathbf{p}}(h_2,h_3,h_4)\, D_g(a_1) a_2 a_3 a_4.$$

---

## 2. Die beiden Rotationsseiten

Für homogene Eingaben gilt typkorrekt:

$$\boxed{\Phi_0(a_0,\ldots,a_4) = \Delta_{\mathbf{p}}(h_2,h_3,h_4)\, \varpi_{\beta,\chi}\!\left(j_A(a_0)\, j_M(D_g(a_1)a_2 a_3 a_4)\right).}$$

Dagegen:

$$\boxed{(t\Phi_0)(a_0,\ldots,a_4) = \Delta_{\mathbf{p}}(h_1,h_2,h_3)\, \varpi_{\beta,\chi}\!\left(j_A(a_4)\, j_M(D_g(a_0)a_1 a_2 a_3)\right).}$$

Diese Formeln zeigen, dass **zwei unabhängige Hindernisse** auftreten:

$$\Delta_{\mathbf{p}}(h_1,h_2,h_3) \quad \text{gegen} \quad \Delta_{\mathbf{p}}(h_2,h_3,h_4),$$

und

$$D_g(a_0) \quad \text{gegen} \quad D_g(a_1).$$

Eine universelle Proportionalität ist daher keineswegs strukturell vorgegeben.

---

## 3. Erster und stärkster Test: $a_4 = 1$

Setze $a_4 = 1$. Wegen $\delta_p^{(0)}(1) = 0$ gilt

$$\Theta^\wedge(a_2, a_3, 1) = 0,$$

also

$$\boxed{\Phi_0(a_0,a_1,a_2,a_3,1) = 0.}$$

Auf der rotierten Seite gilt hingegen:

$$\boxed{(t\Phi_0)(a_0,a_1,a_2,a_3,1) = \Delta_{\mathbf{p}}(h_1,h_2,h_3)\, \varpi_{\beta,\chi}\!\left(j_M(D_g(a_0)a_1 a_2 a_3)\right).}$$

Der erste Entscheidungstest lautet daher:

$$\boxed{\text{Existieren } a_0,a_1,a_2,a_3 \text{ mit } \Delta_{\mathbf{p}}(h_1,h_2,h_3)\neq 0 \text{ und } \varpi_{\beta,\chi}\!\left(j_M(D_g(a_0)a_1 a_2 a_3)\right)\neq 0\,?}$$

Falls ja, folgt sofort $t\Phi_0 \neq c\,\Phi_0$ für jeden konstanten Faktor $c$. Insbesondere: $t\Phi_0 \neq \Phi_0$.

> **Stärker als früheres Ergebnis:** Wäre dies der Fall, würde es keine globale Eigenrelation $t\Phi_0 = g^{-\beta}\Phi_0$ geben — die Ungleichheit wäre aus einem stärkeren Grund belegt.

### Natürlicher erster Zeuge

$$a_1 = \mu_{p_1}, \quad a_2 = \mu_{p_2}, \quad a_3 = \mu_{p_3},$$

denn dann ist

$$\Delta_{\mathbf{p}}(p_1,p_2,p_3) = \prod_{r=1}^3 \log p_r \neq 0.$$

Für $a_0$ ist der bereits in NEU-219/219b verwendete Nichtverschwindungszeuge von $D_g$ bzw. der skalaren Paarung einzusetzen. Seine Nichtverschwindung muss wortgetreu übernommen oder neu bewiesen werden.

---

## 4. Entscheidungsgabel für NEU-219z

### Fall A — Trennzeuge existiert

Wenn $\Phi_0(a_0,a_1,a_2,a_3,1) = 0$ und $(t\Phi_0)(a_0,a_1,a_2,a_3,1) \neq 0$, dann:

$$\boxed{[O\text{-}219\text{-}5e1j\text{-explicit-cup-rotation}] \quad \checkmark[M]_{\mathrm{neg}}.}$$

Genauer:

$$\boxed{\text{Keine globale konstante Eigenrelation } t\Phi_0 = C\Phi_0.}$$

Damit wäre gewöhnliche Zyklizität des konkreten $\Phi_0$ ebenfalls endgültig ausgeschlossen — jedoch aus einem stärkeren und anderen Grund als dem früher behaupteten Faktor $g^{-\beta}$.

### Fall B — der erste Zeuge verschwindet

Nur dieser Test ist negativ. Anschließend sind andere homogene $a_0$ oder ein anderer äußerer Einheitsslot zu prüfen.

### Fall C — alle Einheitsslot-Paarungen verschwinden strukturell

Dann muss diese Vanishing-Aussage bewiesen werden. Erst danach ist der allgemeine Vergleich der beiden Determinanten- und $D_g$-Terme notwendig.

### Fall D — eine konstante Relation überlebt alle Tests

Erst dann darf versucht werden, einen Faktor $C(h_0,\ldots,h_4,g,\beta)$ zu bestimmen und seine Eingabeunabhängigkeit zu beweisen.

---

## Nächster atomarer Unterknoten

$$\boxed{[O\text{-}219\text{-}5e1j\text{-unit-slot-witness}]}$$

**Ziel:** Nichtverschwindung von

$$\varpi_{\beta,\chi}\!\left(j_M(D_g(a_0)\mu_{p_1}\mu_{p_2}\mu_{p_3})\right)$$

für einen bereits konstruierten $a_0$-Zeugen nachweisen. Dieser Test kann den gesamten Rotationsknoten schließen, bevor eine große allgemeine Normalformrechnung notwendig wird.

---

## Abhängigkeiten

| Knoten | Rolle |
|---|---|
| NEU-219 | Basisversion des Cup-Rotationsproblems |
| NEU-219b | Nichtverschwindungszeuge für $D_g$ / skalare Paarung |
| `[O-219-5e1j-explicit-cup-rotation]` | Übergeordneter Rotationsknoten |
| `[O-219-5e1j-unit-slot-witness]` | Erster atomarer Unterknoten (dieser Schritt) |
