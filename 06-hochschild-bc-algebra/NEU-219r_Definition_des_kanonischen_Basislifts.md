# NEU-219r — Definition des kanonischen Basislifts $\widetilde{L}_0$

**DAG-Position:** Nachfolger von NEU-219q (Orbitindexaudit).  
**Charakter:** ⚠️ **Neue Definition** — kein Quellenaudit. $\widetilde{L}$ wurde im bisherigen DAG benutzt, aber nie explizit definiert. Dieser Knoten schließt die Lücke erstmals typkorrekt.  
**Gesperrter Vorgängerknoten:** [O-219-5e1h1a] — aufgehoben durch diese Definition.

---

## 0. Quellenlage und Motivation

**Befund (Audit-Ergebnis vom 2026-07-24):**

$$
\boxed{\widetilde{L} \text{ wurde im bisherigen DAG benutzt, aber nie explizit definiert.}}
$$

Vorhanden waren:
- $L^{\mathrm{cup}}_{g;\mathbf{p}} = D_g \smile \Theta^\wedge \in Z^4(A_{\mathrm{alg}}, M)_g$ (NEU-218/NEU-219)
- Die Eckeneinbettung $j_M: M \hookrightarrow e\widetilde{\mathcal{A}}^{\log}e$ (NEU-219j)
- Die Orbitsummanden $I_k$ und $\mathcal{N}_{\mathrm{tag}} = \bigoplus_k N_0\delta_k$ (NEU-219m/n)
- Die Aussage $\widetilde{L}(\ldots) \in \widetilde{M}_{\mathrm{orb}}$ (NEU-219m, vorausgesetzt)

**Nicht vorhanden:** Eine Formel, die aus $L^{\mathrm{cup}}$ konkret ein Element von $I_k$ oder einer Summe von $I_k$ erzeugt.

NEU-219r darf daher **nicht** als Quellenaudit auftreten. Es führt eine neue typkorrekte Definition ein.

---

## 1. Setup und Notation

Setze
$$
R = \widetilde{A}_{\mathrm{alg}}, \qquad B = eRe = j_A(A_{\mathrm{alg}}), \qquad M_0 = j_M(M),
$$
und den Orbit-Null-Summanden
$$
I_0 = Re \otimes_B M_0 \otimes_B eR.
$$

Die Einbettungen $j_A$ und $j_M$ wurden in NEU-219j/l etabliert; $I_0$ ist der $k=0$-Summand der Orbitzerlegung aus NEU-219m.

---

## 2. Kanonische Eckeneinbettung $\eta_0$

**Definition.**
$$
\eta_0: M_0 \longrightarrow I_0, \qquad m \longmapsto e \otimes_B m \otimes_B e.
$$

### 2.1 Injektivität

Die Multiplikationsrealisierung aus NEU-219l liefert den Isomorphismus
$$
\Pi_0: I_0 \xrightarrow{\;\cong\;} N_0, \qquad x \otimes_B m \otimes_B y \mapsto xmy.
$$

Für $m \in M_0 = eM_0e$ gilt
$$
\Pi_0(\eta_0(m)) = \Pi_0(e \otimes_B m \otimes_B e) = eme = m.
$$

Daher $\Pi_0 \circ \eta_0 = \mathrm{id}_{M_0}$, also ist $\eta_0$ **injektiv**. ✓[K]

### 2.2 Bimodulverträglichkeit

Für $a, b \in B$ gilt wegen der ausgeglichenen Tensorprodukte
$$
\eta_0(amb) = e \otimes_B amb \otimes_B e = a \cdot (e \otimes_B m \otimes_B e) \cdot b.
$$

Somit ist $\eta_0$ ein $B$-Bimodulhomomorphismus, und $\eta_0 \circ j_M$ ist ein $A_{\mathrm{alg}}$-Bimodulhomomorphismus. ✓[K]

---

## 3. Erstdefinition des Liftoperators $\widetilde{L}_0$

$$
\boxed{
\widetilde{L}_0(a_1, a_2, a_3, a_4)
:= e \otimes_B j_M\!\left( L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1, a_2, a_3, a_4) \right) \otimes_B e.
}
$$

**Typkontrolle:**
$$
\widetilde{L}_0: A_{\mathrm{alg}}^{\otimes 4} \longrightarrow I_0 \subseteq \widetilde{M}_{\mathrm{orb}}.
$$

Dies ist die Komposition
$$
\widetilde{L}_0 = \eta_0 \circ j_M \circ L^{\mathrm{cup}}_{g;\mathbf{p}}.
$$

Alle drei Faktoren sind typkorrekt definiert. ✓[K]

---

## 4. Kozykelerhalt

Da $\eta_0 \circ j_M$ ein $A_{\mathrm{alg}}$-Bimodulhomomorphismus ist, gilt für den Hochschildrand $b$:

$$
b L^{\mathrm{cup}}_{g;\mathbf{p}} = 0 \quad \Longrightarrow \quad b\widetilde{L}_0 = 0.
$$

**Beweis:** Der Hochschildrand wirkt durch alternierende Bimodulanwendungen; ein Bimodulhomomorphismus vertauscht mit $b$. Da $L^{\mathrm{cup}}_{g;\mathbf{p}} \in Z^4(A_{\mathrm{alg}}, M)_g$, folgt unmittelbar

$$
\boxed{\widetilde{L}_0 \in Z^4(A_{\mathrm{alg}}, I_0).} \qquad \checkmark[K/M]
$$

---

## 5. Orbitindex $\kappa = 0$ und $\varepsilon = 0$

### 5.1 Strukturelle Beobachtung

Die Definition $\widetilde{L}_0$ verwendet ausschließlich:
- $j_M(M) \subseteq I_0$ (Einbettung in den $k=0$-Summanden)
- die kanonischen Eckentensoren $e$
- **keine** $\tau^{\pm 1}$
- **keine** $T^{\pm 1}$
- **keine** orbitweise Induktion über mehrere $k$

### 5.2 Ergebnis

Da $\widetilde{L}_0$ vollständig im Summanden $I_0$ lebt ($k=0$), ist die Orbitindexfunktion $\kappa$ aus NEU-219q identisch null:

$$
\boxed{\kappa(a_1, a_2, a_3, a_4) = 0} \qquad \text{für alle } a_i \in A_{\mathrm{alg}}. \quad \checkmark[M]
$$

Und damit:

$$
\boxed{\varepsilon = 0.} \qquad \checkmark[M]
$$

### 5.3 Konsequenz für die skalare Rotation

Das $\lambda$-Gewicht verschwindet vollständig aus der skalaren Rotation:

$$
C(g, \beta, \lambda) = g^{s\beta}.
$$

Kein Orbitgewicht $\lambda$ kann die Zyklizität reparieren; die Entscheidung liegt allein beim KMS-Exponenten $s$.

---

## 6. Abgrenzung: Lifte mit $\kappa \neq 0$

Ein Lift mit $\kappa \neq 0$ ist **nicht** durch die bisherige Architektur erzwungen. Er müsste neue Daten enthalten, insbesondere explizit $T^k$ oder $\tau^k$ sowie eine gewählte orbitweise Zuordnung. Eine solche Wahl wäre keine Fortsetzung dieser Definition, sondern eine **weitere neue Konstruktion** mit eigener Natürlichkeits- und Kozykelprüfung (separater DAG-Knoten, noch unbenannt).

---

## 7. Statusübersicht

| Aussage | Status |
|---|---|
| $\widetilde{L}_0$ erstmals typkorrekt definiert | ✓[K] |
| $\eta_0$ injektiv ($\Pi_0 \circ \eta_0 = \mathrm{id}$) | ✓[K] |
| $\eta_0 \circ j_M$ Bimodulhomomorphismus | ✓[K] |
| $\widetilde{L}_0 \in Z^4(A_{\mathrm{alg}}, I_0)$ | ✓[K/M] |
| $\kappa = 0$, $\varepsilon = 0$ | ✓[M] |
| $C(g,\beta,\lambda) = g^{s\beta}$ (kein $\lambda$-Beitrag) | ✓[M] |
| **Offener Folgeknoten** | $s$ aus KMS-Rechnung bestimmen |

---

## 8. DAG-Anschluss

```
NEU-219q: Orbitindex κ, Auditrahmen          ✓[K/M]
      |
NEU-219r: Erstdefinition L~0 = η0∘jM∘L^cup   ← dieser Knoten
      |         κ=0, ε=0, L~0 ∈ Z^4(A,I_0)
      |
 [O-219-r1]  KMS-Exponent s bestimmen         ?[O]  ← nächster offener Knoten
      |
 [O-219-r2]  C(g,β) = g^{sβ} ≠ 1 für g≠1    ?[O]
      |
 [O-219-r3]  Zyklizitätshindernis endgültig   ?[O]
```

---

**Commit-Referenz:** Nachfolger von NEU-219q.  
**Primärer nächster Audit:** [O-219-r1] — KMS-Exponent $s$ in der direkten skalaren Rotationsrechnung.
