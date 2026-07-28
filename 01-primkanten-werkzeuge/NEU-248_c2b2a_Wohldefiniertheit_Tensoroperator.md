# NEU-248 — [c.2b.2a] Wohldefiniertheit von $L_{\delta_q}^{(3)}$

**Knoten:** `[O-229-3B.1f-c.2b.2a-delta-primary-type-and-tensor-domain]` | Status: `?[O]`  
**Vorgänger:** NEU-247b (Domänenpräzisierung und Auditplan)  
**Entscheidungsgegenstand (einziger):**

$$
\boxed{\text{Existiert ein typkorrekt definierbarer Tensoroperator }L_{\delta_q}^{(3)}\text{ auf einem Raum, der }\mathcal{D}_p^{\mathrm{lift}}\text{ enthält?}}
$$

Dieser Knoten behauptet noch **keine** Invarianz von $\mathcal{D}_p^{\mathrm{lift}}$ oder $K_p^{\mathrm{alg}}$.

---

## 1 — Quellfrage A: Exakter Typ von $\delta_q$ aus NEU-195

### 1.1 Zu extrahierende Merkmale

| Merkmal | Prüfpunkt |
|---|---|
| $\operatorname{Dom}\delta_q$ | Ganz $A_{\mathrm{alg}}$ oder nur kleinere Unteralgebra / Erzeugerraum / dichte Teilmenge? |
| $\operatorname{Codom}\delta_q$ | $\subseteq A_{\mathrm{alg}}$? |
| $\mathbb{C}$-Linearität | Explizit belegt oder nur auf Erzeugern? |
| Wirkung auf Erzeuger | Vollständige Formel |
| Graduierungserhaltung | $\delta_q(A_{\mathrm{alg}}^{(n)}) \subseteq A_{\mathrm{alg}}^{(n)}$ oder Gradshift? |
| Kommutator $[\delta_q, \delta_\ell] = 0$ | Operatoridentität auf gemeinsamer Domäne oder nur Erzeugerrechnung? |
| Tensor-/Hochschild-/Lie-Ableitung | Bereits in NEU-195 definiert oder nicht? |

### 1.2 Kritische Unterscheidung

Es ist streng zu trennen:

- **Rechnung auf Erzeugern** (nicht ausreichend für Wohldefiniertheit auf ganz $A_{\mathrm{alg}}$)
- **Bewiesene Operatoridentität auf der gesamten Domäne** (erforderlich für die Tensorfortsetzung)

Nur falls $\delta_q : A_{\mathrm{alg}} \to A_{\mathrm{alg}}$ $\mathbb{C}$-linear und auf ganz $A_{\mathrm{alg}}$ definiert ist, ist die Summenformel

$$
L_{\delta_q}^{(3)} = \sum_{j=0}^{3} \mathbf{1}^{\otimes j} \otimes \delta_q \otimes \mathbf{1}^{\otimes(3-j)}
$$

ohne weitere Prüfung als linearer Endomorphismus auf $A_{\mathrm{alg}}^{\otimes_{\mathrm{alg}} 4}$ wohldefiniert.

**Ergebnis Frage A:** offen — Quellenlektüre NEU-195 ausstehend.

---

## 2 — Quellfrage B: Primärdefinition von $B_3$

### 2.1 Zu identifizierende Datei und zu extrahierende Merkmale

Es muss die Datei gefunden und vollständig gelesen werden, in der $B_3$ erstmals definiert wird.

| Merkmal | Prüfpunkt |
|---|---|
| $B_3 = ?$ | Explizite Formel / Definitionsort |
| Zugrundeliegende Algebra | $A_{\mathrm{alg}}$, eine Vervollständigung, oder anderes? |
| Tensorprodukt-Typ | algebraisch $\otimes_{\mathrm{alg}}$ oder topologisch $\widehat{\otimes}$? |
| Grundkörper | $\mathbb{C}$, $\mathbb{R}$, anderes? |
| Norm / Topologie | falls vorhanden |
| Einbettung $A_{\mathrm{alg}}^{\otimes 4} \hookrightarrow B_3$ | explizit / implizit / nicht vorhanden |
| Aufenthaltsraum von $\mathcal{D}_p^{\mathrm{lift}}$ | in $A_{\mathrm{alg}}^{\otimes 4}$, in $B_3 \setminus A_{\mathrm{alg}}^{\otimes 4}$, oder unklar? |

**Ergebnis Frage B:** offen — Primärdatei für $B_3$ noch nicht identifiziert.

---

## 3 — Abschlussfallstruktur

| Fall | Bedingung | Marker für [c.2b.2a] | Reichweite |
|---|---|---|---|
| **A** | $B_3 = A_{\mathrm{alg}}^{\otimes_{\mathrm{alg}} 4}$ und $\delta_q$ linear auf ganz $A_{\mathrm{alg}}$ | $\checkmark[K/M]$ | Nur lineare Wohldefiniertheit; keine Liftbereichsinvarianz |
| **B** | $A_{\mathrm{alg}}^{\otimes 4} \subsetneq B_3$, aber $\mathcal{D}_p^{\mathrm{lift}} \subseteq A_{\mathrm{alg}}^{\otimes 4}$ | $\checkmark[K/M]$ | $L_{\delta_q}^{(3)}$ auf algebraischem Kernraum; keine Erweiterung auf ganz $B_3$ |
| **C** | $B_3 = A^{\widehat{\otimes}4}$, keine Liftbereich-Inklusion belegt | $?[O]$ | Eigener analytischer Erweiterungsknoten (Stetigkeit / Beschränktheit / Abschließbarkeit) |
| **D** | Keine vorhandene Tensorwirkung, keine typkorrekte algebraische Neukonstruktion | $\checkmark[M]_{\mathrm{neg,Quelle}}$ | Spätere Erweiterung nach Domänen- oder Topologiekonstruktion offen |

**Wichtig (Fall B):** Zusätzlich zu prüfen:
$$
\mathcal{D}_p^{\mathrm{lift}} \subseteq A_{\mathrm{alg}}^{\otimes 4}?
$$
Ohne diese Inklusion erreicht $L_{\delta_q}^{(3)}$ den Liftbereich nicht → Fall D.

**Wichtig (Fall C):** Aus algebraischer Wohldefiniertheit folgt nicht automatisch $L_{\delta_q}^{(3)} : B_3 \to B_3$.

---

## 4 — Nachfolge-Knotenstruktur (gesperrt bis [c.2b.2a] geschlossen)

$$
[c.2b.2a]\;\text{(Wohldefiniertheit)}
\;\longrightarrow\;
[c.2b.2b]\;\bigl(L_{\delta_q}^{(3)}(\mathcal{D}_p^{\mathrm{lift}}) \subseteq \mathcal{D}_p^{\mathrm{lift}}\bigr)
\;\longrightarrow\;
[c.2b.2c]\;\bigl(L_{\delta_q}^{(3)}(K_p^{\mathrm{alg}}) \subseteq K_p^{\mathrm{alg}}\bigr)
$$

NEU-014 und NEU-042 werden erst nach Abschluss von [c.2b.2a] inhaltlich ausgewertet.
