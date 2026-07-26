# NEU-158 — Invariante Formen auf dem Rohkopplungsquotienten: Symmetrieeindeutigkeit

> Stand: 14. Juli 2026. (Revision: Terminologie §158.C.0/C.2 vollständig präzisiert)  
> Vorgänger: NEU-156 §156.F, NEU-157, NEU-159, NEU-160.  
> Typ: **Strukturfrage**. Entscheidet Ausgang A vs. B aus NEU-156.

---

## DAG-Position

```
NEU-156 (Ausgänge A/B)
NEU-159 (Zeuge)
NEU-160 (Quotient Q_p, Symmetrieabstieg)  ──►  NEU-158
```

---

## 158.A — Ausgangssituation

Nach NEU-156 §156.B ist $q_{\mathrm{conn}}$ durch das Normierungsaxiom allein nicht eindeutig. NEU-159 konstruiert den konkreten Nichtverschwindungsbefund $T_p(\mathcal{E}_p^{\mathrm{lin,ch}}) \neq \{0\}$. NEU-160 zeigt, dass $Q_p$ ein wohldefinierter nichttrivialer Hilbertraum ist, auf dem $G_p$ unitär wirkt. Erst auf dieser Grundlage ist das Kommutantenkriterium konkret anwendbar.

---

## 158.B — Rohkopplungsquotient (Verweis auf NEU-160)

$$Q_p \cong \overline{T_p(\mathcal{E}_p^{\mathrm{lin,ch}})} \subseteq H_{J,N}.\tag{158.B.1}$$

Wohldefiniertheit und Positivdefinitheit: ✅[M] in NEU-160 §160.A.  
$Q_p \neq \{0\}$: ❓[O] bis NEU-159 Zeuge; danach ✅[M].

---

## 158.C — Kommutantenkriterium

### 158.C.0 — Terminologische Konvention: „proportional“

| Formklasse | Skalar | Satz-Formulierung |
|---|---|---|
| Positive semidefinite Formen (einschließlich Nullform) | $c \geq 0$ | alle pos. semidefiniten invarianten Formen |
| Nichtverschwindende pos. semidefinite Formen | $c > 0$ | alle **nichtverschwindenden** pos. invarianten Formen |
| Positiv definite Formen | $c > 0$ (automatisch) | alle **positiv definiten** invarianten Formen |

In diesem Blatt werden **positive semidefinite** Formen betrachtet; die Nullform $B = 0$ ist mit $c = 0$ eingeschlossen. Der Satz lautet daher mit $c \geq 0$.

### 158.C.1 — Voraussetzungen

- $Q_p$ komplexer Hilbertraum mit Referenzskalarprodukt $\langle\cdot,\cdot\rangle_{Q_p}$ (NEU-160 §160.A).
- $\pi: G_p \to \mathcal{U}(Q_p)$ unitäre Darstellung (NEU-160 §160.C).
- Betrachtet: **beschränkte positive semidefinite $G_p$-invariante Hermiteformen** auf $Q_p$.
- $\pi(G_p)' := \{B \in \mathcal{B}(Q_p) : B\pi(g) = \pi(g)B\; \forall g\}$.

### 158.C.2 — Satz (vollständig präzise)

Jede beschränkte positive semidefinite $G_p$-invariante Hermiteform besitzt die Darstellung $B_A(x,y) = \langle Ax,y\rangle_{Q_p}$ mit $A \in \pi(G_p)' \cap \mathcal{B}^{\geq 0}(Q_p)$. Damit:

$$\boxed{\text{Alle beschränkten pos. semidefiniten }G_p\text{-invarianten Hermiteformen sind }c\langle\cdot,\cdot\rangle_{Q_p},\; c\geq 0, \iff \pi(G_p)' = \mathbb{C}I.}\tag{158.C.2}$$

**Varianten:**
- Für **nichtverschwindende** pos. Formen: $c > 0$, Satz gilt entsprechend eingeschränkt.
- Für **positiv definite** Formen: $c > 0$ automatisch.

### 158.C.3 — Beweis der nichttrivialen Richtung

Ist $\pi(G_p)' \neq \mathbb{C}I$, enthält die Kommutante einen nichtskalaren selbstadjungierten $S$. Für $0 < \varepsilon < \|S\|^{-1}$:
$$A_\varepsilon := I + \varepsilon S \geq (1-\varepsilon\|S\|)I > 0.$$
$B_{A_\varepsilon}(x,y) = \langle A_\varepsilon x,y\rangle$ ist positiv definit, $G_p$-invariant, und wegen Nichtskalarität von $S$ nicht proportional zur Referenzform. $\square$

**Bemerkung zur Äquivalenz mit Irreduzibilität:** Die Bedingung $\pi(G_p)' = \mathbb{C}I$ ist für unitäre Darstellungen auf komplexen Hilberträumen genau die Irreduzibilität (Schurs Lemma). Diese Äquivalenz ist ein **allgemeiner Satz** (✅[M]) und kein neuer offener Schritt; offen ist nur, ob die konkret konstruierte Darstellung $\pi_p$ irreduzibel ist (❓[O] → NEU-160 §160.C).

### 158.C.4 — Reichweite

Nicht automatisch erfasst: unbeschränkte Formen; algebraischer Kern; Lokalitäts-/Restspur-/$\#$-Bedingungen; eingeschränkte Zulassungsklassen. Für engere Klassen: $\pi(G_p)' = \mathbb{C}I$ hinreichend; nichtskalare Kommutante widerlegt Eindeutigkeit nur wenn $A_\varepsilon$ die Zusatzbedingungen respektiert.

---

## 158.D — Abgrenzung: GNS und Wodzicki

GNS: parametrisiert Darstellungen durch Formen, selektiert keine bevorzugte Form. Wodzicki: setzt Pseudodifferentialgebra mit Idealstruktur voraus (nicht im Katalog erfüllt). Kommutantenkriterium ist minimal voraussetzungsreich.

---

## 158.E — Zwei Ausgänge

| Ausgang | Bedingung | Konsequenz |
|---|---|---|
| **A** | $\pi(G_p)' = \mathbb{C}I$ ($\pi_p$ irreduzibel) | $q_{\mathrm{conn}} = c\cdot q_p^{\mathrm{raw}}$, $c > 0$, eindeutig bis auf Skalierung |
| **B** | Kommutante mehrdimensional | $\operatorname{Tr}^{\mathrm{conn}}$ als Axiom zu setzen |

---

## 158.F — Nächste Schritte

1. NEU-160 §160.C: Präzulässigkeitsinvarianz + Intertwining $\to$ unitäre Darstellung $\pi_p$
2. Irreduzibilität von $\pi_p$?
3. Falls irreduzibel: Bestimmung $\alpha_p$ (Isometrietest $\iota_{J,N}$)

**Statusmarker:** ❓[O] (abhängig von NEU-159 + NEU-160).

---

## Verweise

NEU-156 §156.B/F, NEU-157 §157.D, NEU-159, NEU-160, NEU-41 §3, NEU-44, NEU-122, NEU-138.
