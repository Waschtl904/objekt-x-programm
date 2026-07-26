# NEU-156 — Rekonstruktion und Eindeutigkeit der verbundenen Restspurform

> Stand: 14. Juli 2026. (Revision: Präzisierung §156.B)  
> Vorgänger: NEU-155 (Drei-Operatoren-Typisierung), NEU-153 §D.0.5.A, NEU-154 §154.A.  
> Typ: **Definitionslücken-Audit**.  
> Zweck: Entscheiden, ob (155.F.1) ein **zu beweisender Folgesatz** oder eine **neue Strukturannahme** ist.

---

## DAG-Position

```
NEU-155  ──►  NEU-156  ──►  NEU-157 (Rohkopplung nichttrivial?)
                    └──►  NEU-158 (Symmetrieeindeutigkeit)
                    └──►  NEU-153, NEU-154 (Revisionshinweise)
```

---

## 156.A — Quellenstatus von $\operatorname{Tr}^{\mathrm{conn}}$

| Symbol / Ausdruck | Fundstelle | Klassifikation |
|---|---|---|
| $\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(x^\#x) = 1$ | NEU-41 §3 | **Normierungsaxiom** — einzige Bedingung, keine konstruktive Definition |
| $x^\#y$ | NEU-41 §3, NEU-153 §D.0.5.A | **Formale Notation** — Hermitizität auf Liftraum unbewiesen |
| $W_{\mathrm{res}}^{\mathrm{conn}}$ | NEU-153 §D.0.5.A | **Formale Notation** — nicht konstruiert |
| $\operatorname{Res}_W$, $\operatorname{Tr}_{W_{\mathrm{res}}}$ | NEU-137, NEU-138 | Wodzicki-Residuenspur; **nicht** mit $\operatorname{Tr}^{\mathrm{conn}}$ identifiziert |
| $|c_p|^2 = \|\widetilde\Psi_p\|^2$ | NEU-44 §44.2, NEU-134 | Normierungskonsequenz; nur bei Identifikation mit $B_p^{\mathrm{raw}}$ relevant |

$$\boxed{\operatorname{Tr}^{\mathrm{conn}} \text{ ist im bisherigen Katalog weder konstruktiv definiert noch hergeleitet.}}$$

Die einzige Bedingung ist das Normierungsaxiom:
$$\operatorname{Tr}^{\mathrm{conn}}_{W_{\mathrm{res}}}(\widehat\varepsilon_p^\#\widehat\varepsilon_p) = 1.\tag{156.A.1}$$

**Statusmarker:** ✅[M]

---

## 156.B — Unterbestimmtheitstest (revidiert: Zerlegungsargument, positiv definit)

### 156.B.1 — Satz (Unterbestimmung bei festgehaltener Hebung)

Sei
$$V = \mathbb{C}x_0 \oplus U, \qquad U \neq \{0\}.\tag{156.B.0}$$

**(a) Semidefinite Klasse.** Für jeden beschränkten positiven Operator $A \geq 0$ auf $U$ definiert
$$q_A(ax_0 + u) := |a|^2 + \langle Au, u\rangle_U\tag{156.B.1}$$
eine positive semidefinite Hermiteform auf $V$ mit $q_A(x_0) = 1$. Die Abbildung $A \mapsto q_A$ ist injektiv.

**(b) Positiv definite Klasse.** Soll die Unterbestimmung bereits in der Klasse **positiv definiter** Hermiteformen gezeigt werden, so genügt die eindimensionale Familie
$$q_t(ax_0 + u) := |a|^2 + t\|u\|_U^2, \qquad t > 0.\tag{156.B.2}$$
Jedes $q_t$ ist positiv definit, $q_t(x_0) = 1$ für alle $t > 0$, und $q_{t_1} \neq q_{t_2}$ für $t_1 \neq t_2$.

*Beweis.* (a) Aus Linearkombination folgt Sesquilinearität und Hermitizität; $q_A(x_0) = |1|^2 + \langle A\cdot0,0\rangle = 1$; für $A \neq A'$ existiert $u_0 \in U$ mit $\langle Au_0,u_0\rangle \neq \langle A'u_0,u_0\rangle$. (b) $q_t(u_0) = t\|u_0\|^2 \neq t'\|u_0\|^2 = q_{t'}(u_0)$ für $u_0 \neq 0$ und $t \neq t'$. $\square$

**Kernpunkt:** Das Normierungsaxiom (156.A.1) schränkt $q$ einzig auf der Geraden $\mathbb{C}x_0$ ein. Die gesamte Struktur auf dem Komplement $U$ (Voraussetzung: $U \neq \{0\}$, d.h. $\dim V \geq 2$) bleibt frei. Dies ist auch dann gültig, wenn $\mathcal{A}_p$ keine beliebige Reskalierung von $v_p$ als Hebung enthält.

$$\boxed{\text{Die Bedingung (156.A.1) allein bestimmt }q_{\mathrm{conn}}\text{ nicht eindeutig, selbst innerhalb der positiv definiten Hermiteformen (sofern }\dim V \geq 2).}$$

**Statusmarker:** ✅[M]

### 156.B.2 — Verschräfung: Kein weiterer Eindeutigkeitserzwinger im Katalog

Bedingungen, die $q_{\mathrm{conn}}$ eindeutig festlegen könnten:
- Symmetrieverträglichkeit $\to$ NEU-158
- Spurklassenbedingung (NEU-138/145)
- Wodzicki-Eindeutigkeit (Voraussetzungen nicht erfüllt, vgl. NEU-158 §158.D)
- GNS-Konstruktion (selektiert Darstellungen, nicht Formen)

Keiner dieser Punkte ist auf dem Liftraum $B_3^{\mathrm{adm}}$ im bisherigen Katalog durchgeführt.

**Statusmarker:** ❓[O] → NEU-158.

---

## 156.C — Kanonischer Rohkopplungskandidat $B_p^{\mathrm{raw}}$

$$q_p^{\mathrm{raw}}(x) := \|T_px\|_{H_{J,N}}^2,\qquad B_p^{\mathrm{raw}}(x,y) := \langle T_px, T_py\rangle_{H_{J,N}}.\tag{156.C.1}$$

| Eigenschaft | Status |
|---|---|
| Wohldefiniertheit, Hermitizität, pos. Semidefinitheit | ✅[M] |
| Nullraum $= \ker T_p$ | ✅[M] |
| Verträglichkeit mit $\#$, Symmetrieverträglichkeit, Spurklassen | ❓[O] → NEU-158 |

---

## 156.D — Residuenvergleich auf Basisvektoren

Rechte Seite $B_p^{\mathrm{raw}}(e_uV_p, e_vV_p)$: **vollständig berechenbar** aus NEU-41 (41.6) und NEU-143.

$$\boxed{\operatorname{Tr}^{\mathrm{conn}}((e_uV_p)^\#(e_vV_p)) \text{ ist eine Definitionslücke, keine offene Rechnung.}}\tag{156.D.1}$$

**Statusmarker:** ✅[M]

---

## 156.E — Normierungsverträglichkeit des Rohkandidaten

Für $q_{\mathrm{conn}} = \alpha_p q_p^{\mathrm{raw}}$, $\alpha_p > 0$:
$$\alpha_p\|T_p\widehat\varepsilon_p\|^2 = 1 \iff \|T_p\widehat\varepsilon_p\| = \alpha_p^{-1/2}.\tag{156.E.1}$$

Die Liftfaser ist eine Sphäre des Radius $\alpha_p^{-1/2}$ im Rohkopplungsquotienten. Fixierung von $\alpha_p$: ❓[O] → NEU-158.

---

## 156.F — Zwei Ausgänge

$$\boxed{\text{Ausgang A: }\pi(G_p)' = \mathbb{C}I \Rightarrow q_{\mathrm{conn}} = \alpha_p q_p^{\mathrm{raw}} \text{ bis auf Skalierung eindeutig.}}$$
$$\boxed{\text{Ausgang B: Kommutante nichtskalarer }\Rightarrow \operatorname{Tr}^{\mathrm{conn}}\text{ muss als Axiom gewählt werden.}}$$

Entscheidung: ❓[O] → **NEU-158**.

---

## 156.H — Endbefund

$$\boxed{\operatorname{Tr}^{\mathrm{conn}}\text{ ist unterbestimmt. (155.F.1) ist eine neue Strukturannahme, kein Folgesatz.}}\tag{156.H.1}$$

- NEU-153 §D.0.5.A: $q_p^{\mathrm{raw}}$ ist kanonischer Kandidat; Eindeutigkeit offen.
- NEU-154 §154.A: (155.F.2) als Strukturannahme kennzeichnen.
- NEU-152: Unberührt.
- Nachfolger: **NEU-157**, **NEU-158**, **NEU-159**.

---

## Verweise

NEU-41 §3, NEU-44 §44.1–4, NEU-122, NEU-137–138, NEU-143, NEU-153 §D.0.5.A/D.2, NEU-154 §154.A, NEU-155 §155.F–H, NEU-157, NEU-158, NEU-159.
