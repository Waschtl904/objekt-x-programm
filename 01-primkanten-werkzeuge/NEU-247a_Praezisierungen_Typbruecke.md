# NEU-247a — Präzisierungen zur Typbrücke (Korrekturen zu NEU-247)

**Knoten:** `[O-229-3B.1f-c.2b.2-tensor-lift-of-valuation-derivations]` — Präzisierungsanhang  
**Bezug:** NEU-247 (Tensor-Lift von Bewertungsableitungen: Typbrücke)  
**Nächster Zwischenknoten:** `[O-229-3B.1f-c.2b.2a-delta-primary-type-and-tensor-domain]` | Status: `?[O]`

---

## P1 — Statusmarker-Korrektur

Der in NEU-247 angekündigte Marker $\checkmark[M]_{\mathrm{pos,Quelle}}$ gehört **nicht** zum etablierten Statussystem und wird gestrichen.

Das gültige Markersystem lautet:

| Situation | Marker |
|---|---|
| Positiv aus den Quellen bewiesener Befund | $\checkmark[M]$ |
| Fehlen im auditierten Quellenbestand | $\checkmark[M]_{\mathrm{neg,Quelle}}$ |

Alle weiteren Differenzierungen sind nicht einzuführen, solange das System sie nicht enthält.

---

## P2 — Alternativzweigstruktur (Fragen 1 und 2)

NEU-247 formulierte die Abhängigkeit fälschlicherweise als Konjunktion. Korrekte Struktur:

$$
\begin{cases}
\text{Frage 1 positiv:} & \text{vorhandenen }\Delta_q\text{ auditieren (Brückenverträglichkeit prüfen)} \\
\text{Frage 1 negativ:} & L_{\delta_q}^{(3)}\text{ neu konstruieren (Wohldefiniertheit prüfen)}
\end{cases}
$$

In **beiden Zweigen** folgt anschließend die Brückenverträglichkeit aus Frage 3 (NEU-247 §2.3). Die Konjunktionsbedingung

$$
\text{Frage 1 positiv} \land \text{Frage 2 positiv} \Longrightarrow \text{Frage 3}
$$

ist damit aufgehoben.

---

## P3 — Linearität vs. Leibniz-Regel

Für die **bloße Wohldefiniertheit** von

$$
L_{\delta_q}^{(3)} = \sum_{j=0}^{3} \mathbf{1}^{\otimes j} \otimes \delta_q \otimes \mathbf{1}^{\otimes(3-j)}
$$

auf einem algebraischen Tensorprodukt genügt die **$\mathbb{C}$-Linearität** von $\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}}$.

Die Leibniz-Regel wird erst benötigt, wenn die Verträglichkeit mit algebraischen Multiplikationen oder dem Hochschild-Randoperator nachgewiesen werden soll, etwa

$$
[b, L_{\delta_q}] = 0.
$$

Das sind zwei strikt getrennte Prüfschritte:

$$
\text{lineare Tensorfortsetzung} \neq \text{Hochschild-Kettenwirkung}.
$$

Der Leibniz-Test gehört damit **nicht** zur Wohldefiniertheitsprüfung in Frage 2, sondern zu einer nachgelagerten Kompatibilitätsprüfung.

---

## P4 — B₃-Typ: Gleichheit vs. Inklusion vs. topologische Vervollständigung

Bisher festgehalten: $B_3 = A^{\otimes 4}$.  
NEU-247 formuliert die Neukonstruktion auf $A_{\mathrm{alg}}^{\otimes 4}$.

Drei zu unterscheidende Situationen:

| Fall | Relation | Konsequenz für $L_{\delta_q}^{(3)}$ |
|---|---|---|
| **A** | $B_3 = A_{\mathrm{alg}}^{\otimes 4}$ | Konstruktion direkt auf $B_3$ |
| **B** | $A_{\mathrm{alg}}^{\otimes 4} \subsetneq B_3$ | $L_{\delta_q}^{(3)}$ zunächst nur auf $A_{\mathrm{alg}}^{\otimes 4}$, Fortsetzung auf $B_3$ gesondert zu klären |
| **C** | $B_3$ ist topologische Vervollständigung von $A_{\mathrm{alg}}^{\otimes 4}$ | Stetigkeitsfrage hinzukommend; $L_{\delta_q}^{(3)}$ zunächst nur auf dem algebraischen Kern |

In Fall B und C entsteht zunächst nur

$$
L_{\delta_q}^{(3)} : A_{\mathrm{alg}}^{\otimes 4} \longrightarrow A_{\mathrm{alg}}^{\otimes 4},
$$

**nicht** automatisch ein Operator auf dem gesamten $B_3$. Die Primärdefinition von $B_3$ muss diesen Punkt klären, bevor die Liftambienz des Operators typisiert werden kann.

**Prüfquellen:** NEU-195 (Primärdefinition $\delta_q$), NEU-229 (Liftbereich), NEU-221e (Tensorstruktur — gezielter Re-Audit).

---

## P5 — Minimale Intertwining-Bedingung

Für die Kerninvarianz

$$
L_{\delta_q}^{(3)}(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}
$$

muss **nicht** vorab ein Operator $\delta_{q,\mathrm{prim}}$ konstruiert werden. Die minimale Bedingung lautet:

$$
\pi_{\mathrm{prim},p} \circ L_{\delta_q}^{(3)}(k) = 0 \qquad \forall\, k \in K_p^{\mathrm{alg}},
$$

oder äquivalent:

$$
L_{\delta_q}^{(3)}(\ker \pi_{\mathrm{prim},p}) \subseteq \ker \pi_{\mathrm{prim},p}.
$$

Falls $\pi_{\mathrm{prim},p}$ surjektiv ist, induziert diese Kerninvarianz **automatisch** einen eindeutig bestimmten Quotienten-Operator:

$$
\delta_{q,\mathrm{prim}}(\pi_{\mathrm{prim},p} x) := \pi_{\mathrm{prim},p} L_{\delta_q}^{(3)} x.
$$

Die Intertwining-Relation

$$
\pi_{\mathrm{prim},p} \circ L_{\delta_q}^{(3)} = \delta_{q,\mathrm{prim}} \circ \pi_{\mathrm{prim},p}
$$

ist dann eine **Konsequenz** der Kerninvarianz, nicht deren Voraussetzung.

**Reihenfolge:**
1. Kerninvarianz via minimale Bedingung prüfen.
2. Falls positiv + $\pi_{\mathrm{prim},p}$ surjektiv: $\delta_{q,\mathrm{prim}}$ als induzierten Operator definieren.
3. Intertwining-Relation als Folgerung festhalten.

---

## 6 — Nächster Zwischenknoten

$$
\boxed{[O\text{-}229\text{-}3B.1f\text{-}c.2b.2a\text{-delta-primary-type-and-tensor-domain}] \quad ?[O]}
$$

Dieser Knoten entscheidet **ausschließlich**, ob ein wohldefinierter Tensoroperator auf einem Raum existiert, der den Liftbereich tatsächlich enthält. Er entscheidet noch nicht die Kerninvarianz.

**Extraktionsziele für NEU-195:**

- $\operatorname{Dom}\delta_q$ und $\operatorname{Codom}\delta_q$ (exakter Typ)
- $\mathbb{C}$-Linearität
- Leibniz-Regel (vorhanden / fehlend / implizit)
- Wirkung auf homogene Erzeuger
- Kommutator $[\delta_q, \delta_\ell]$ (falls definiert)
- Ob bereits eine Hochschild-Lie-Ableitung oder tensorweise Fortsetzung definiert wird

**Danach:** Primärdefinition von $B_3$ (Fall A / B / C aus P4) klären.  
**Erst anschließend:** NEU-014 und NEU-042 als Kandidaten für eine bestehende tensorweise Wirkung auswerten.
