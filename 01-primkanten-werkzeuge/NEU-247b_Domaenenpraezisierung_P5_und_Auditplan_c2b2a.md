# NEU-247b — Domänenpräzisierung zu P5 und Auditplan [c.2b.2a]

**Bezug:** NEU-247a P5 (minimale Intertwining-Bedingung)  
**Nächster Knoten:** `[O-229-3B.1f-c.2b.2a-delta-primary-type-and-tensor-domain]` | Status: `?[O]`

---

## 1 — Domänenpräzisierung zu P5

In NEU-247a P5 wurde die Kernbedingung formuliert als

$$
L_{\delta_q}^{(3)}(\ker\pi_{\mathrm{prim},p}) \subseteq \ker\pi_{\mathrm{prim},p}.
$$

Diese **stärkere Aussage** darf nur verwendet werden, wenn Definitionsbereich und Bedeutung des unbeschränkten Kerns zuvor festgelegt sind. Korrekte minimale Bedingung:

$$
K_p^{\mathrm{alg}} = \ker\!\left(\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}\right)
$$

ist **nicht notwendig** der gesamte Kern von $\pi_{\mathrm{prim},p}$ auf dessen maximalem Definitionsbereich.

Die tatsächlich benötigten Bedingungen lauten daher:

$$
\text{(i)}\quad L_{\delta_q}^{(3)}\bigl(\mathcal{D}_p^{\mathrm{lift}}\bigr) \subseteq \mathcal{D}_p^{\mathrm{lift}},
$$

$$
\text{(ii)}\quad \pi_{\mathrm{prim},p} \circ L_{\delta_q}^{(3)}(k) = 0 \qquad \forall\, k \in K_p^{\mathrm{alg}}.
$$

Die stärkere Inklusionsaussage
$$
L_{\delta_q}^{(3)}(\ker\pi_{\mathrm{prim},p}) \subseteq \ker\pi_{\mathrm{prim},p}
$$
bleibt gesperrt, bis Definitionsbereich und Bedeutung des unbeschränkten Kerns festgelegt sind.

### Induzierte Abbildung

Die induzierte Abbildung ist zunächst nur auf dem Bild der **eingeschränkten** Projektion zu definieren:

$$
\delta_{q,\mathrm{prim}}: \operatorname{Ran}\!\left(\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}\right) \longrightarrow \operatorname{Ran}\!\left(\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}\right).
$$

Eine Wirkung auf dem **gesamten primitiven Zielraum** folgt erst aus zusätzlicher Surjektivität von $\pi_{\mathrm{prim},p}\big|_{\mathcal{D}_p^{\mathrm{lift}}}$.

---

## 2 — Knoten [c.2b.2a]: Auditplan

**Kernfrage:**

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2b.2a] : \text{Ist }L_{\delta_q}^{(3)}\text{ auf einem den Liftbereich enthaltenden Tensorraum wohldefiniert?}}
$$

Dieser Knoten schliesst **ausschließlich** zwei Primärfragen. NEU-014 und NEU-042 werden noch **nicht** inhaltlich ausgewertet.

---

### Frage A — NEU-195: Exakter Typ von $\delta_q$

Zu extrahieren:

| Merkmal | Prüfpunkt |
|---|---|
| $\operatorname{Dom}\delta_q$, $\operatorname{Codom}\delta_q$ | exakter Typennachweis |
| $\mathbb{C}$-Linearität | Wohldefiniertheit der Tensorfortsetzung |
| Leibniz-Regel | vorhanden / fehlend / implizit (nachgeordnet) |
| Wirkung auf die Erzeuger | explizit / nur auf dichter Unteralgebra |
| Erhaltung von $A_{\mathrm{alg}}$ | $\delta_q(A_{\mathrm{alg}}) \subseteq A_{\mathrm{alg}}$ oder schwächer |
| Wirkung auf homogene Komponenten | vorhanden / fehlend |
| Kommutator $[\delta_q, \delta_\ell]$ | falls definiert |
| Tensor-/Hochschild-/Lie-Ableitung | bereits definiert oder nicht |

**Kritische Unterscheidung:**

$$
\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}} \quad \text{(ganz }\ A_{\mathrm{alg}}\text{)}
$$

gegenüber einer nur auf einem kleineren Erzeugerraum oder einer dichten Unteralgebra definierten Abbildung. Nur im ersten Fall ist die Tensorfortsetzung unmittelbar wohldefiniert.

---

### Frage B — Primärdefinition von $B_3$

Interpretationsfrei festzustellen, welcher der drei Typen vorliegt:

| Fall | Relation | Konsequenz |
|---|---|---|
| **A** | $B_3 = A_{\mathrm{alg}}^{\otimes_{\mathrm{alg}} 4}$ | $L_{\delta_q}^{(3)}$ direkt auf $B_3$ wohldefiniert |
| **B** | $A_{\mathrm{alg}}^{\otimes_{\mathrm{alg}} 4} \subsetneq B_3$ | $L_{\delta_q}^{(3)}$ zunächst nur auf $A_{\mathrm{alg}}^{\otimes 4}$; zusätzlich nötig: $\mathcal{D}_p^{\mathrm{lift}} \subseteq A_{\mathrm{alg}}^{\otimes 4}$? |
| **C** | $B_3 = A^{\widehat{\otimes}4}$ (topol. Vervollst.) | Stetigkeits-/Beschränktheits-/Abschließbarkeitsfrage vor Erweiterung |

Zu erfassen: Tensorprodukt-Typ, Grundkörper, Topologie.

**In Fall B** muss zusätzlich geprüft werden:
$$
\mathcal{D}_p^{\mathrm{lift}} \subseteq A_{\mathrm{alg}}^{\otimes 4}?
$$
Ohne diese Inklusion erreicht der Operator den Liftbereich nicht.

**In Fall C** folgt aus algebraischer Wohldefiniertheit **nicht** automatisch $L_{\delta_q}^{(3)} : B_3 \to B_3$.

---

## 3 — Statusausgänge für [c.2b.2a]

| Ausgang | Bedingung | Marker |
|---|---|---|
| **Fall A** + $\delta_q$ linear auf ganz $A_{\mathrm{alg}}$ | $L_{\delta_q}^{(3)}$ als Endomorphismus von $B_3$ wohldefiniert | $[c.2b.2a]\; \checkmark[K/M]$ |
| **Fall B** + $\mathcal{D}_p^{\mathrm{lift}} \subseteq A_{\mathrm{alg}}^{\otimes 4}$ | $L_{\delta_q}^{(3)}$ den Liftbereich erreichend | $[c.2b.2a]\; \checkmark[K/M]$ |
| **Fall B** + $\mathcal{D}_p^{\mathrm{lift}} \not\subseteq A_{\mathrm{alg}}^{\otimes 4}$ | Operator erreicht Liftbereich nicht | $[c.2b.2a]\; \checkmark[M]_{\mathrm{neg,Quelle}}$ |
| **Fall C** | Zusätzliche Stetigkeitsprüfung erforderlich | $[c.2b.2a]\; ?[O]$ (nachgelagerter Knoten) |
| $\delta_q$ nur auf dichter Unteralgebra | Tensorfortsetzung nicht automatisch wohldefiniert | $[c.2b.2a]\; \checkmark[M]_{\mathrm{neg,Quelle}}$ |

---

## 4 — Nachfolge-Knotenstruktur

$$
[c.2b.2a]\;\text{(Wohldefiniertheit)} \longrightarrow [c.2b.2b]\;\text{(Liftbereichsinvarianz)} \longrightarrow [c.2b.2c]\;\text{(Kerninvarianz)}
$$

| Knoten | Frage |
|---|---|
| $[c.2b.2a]$ | $L_{\delta_q}^{(3)}$ auf Tensorraum mit Liftbereich wohldefiniert? |
| $[c.2b.2b]$ | $L_{\delta_q}^{(3)}(\mathcal{D}_p^{\mathrm{lift}}) \subseteq \mathcal{D}_p^{\mathrm{lift}}$? |
| $[c.2b.2c]$ | $L_{\delta_q}^{(3)}(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}$? |
