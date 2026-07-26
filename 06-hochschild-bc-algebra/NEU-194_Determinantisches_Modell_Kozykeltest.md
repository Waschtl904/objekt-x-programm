# NEU-194 — Determinantisches Modell: Paarung und Kozykeltest

## Vorbemerkung

Nach [O-193-4b] ist die symmetrische NEU-176-Schablone durch die Paarungsroute ausgeschlossen (Alt₄L = 0). Dieser Knoten konstruiert das einfachste alternierende Testmodell mit getrennten Slotfunktionalen, berechnet die Paarung explizit und prüft die Hochschild-Kozykelbedingung.

---

## 1. Explizite Slotfunktionale

Seien $p_1, p_2, p_3, p_4$ paarweise verschiedene Primzahlen, $P := p_1 p_2 p_3 p_4$.

Für jedes $i \in \{1,2,3,4\}$ wähle ein algebraisches Funktional $f_i \in A^\vee$ mit:
$$f_i|_{A_q} = 0 \quad (q \neq p_i), \qquad f_i(\mu_{p_i}) = 1.$$

Da die $p_i$ verschieden sind: $f_i(\mu_{p_j}) = \delta_{ij}$.

Duales Gewicht: $\alpha_t^\vee f_i = p_i^{-it} f_i$.

---

## 2. Homogener Zielvektor

Sei $g = a/b \in \mathbb{Q}_+^\times$, $\lambda = \log g$. Setze:
$$m_{gP} := \mu_{aP}\mu_b^* \in A_{gP}.$$

**Nichtverschwindung:** $m_{gP}\mu_b = \mu_{aP}\mu_b^*\mu_b = \mu_{aP} \neq 0$, also $m_{gP} \neq 0$.

**Augmentationswert:** $\varepsilon(m_{gP}) = 1$.

---

## 3. Determinantischer Vierkochain

$$\boxed{L_{\lambda}^{\det}(a_1,a_2,a_3,a_4) := \det\!\bigl(f_i(a_j)\bigr)_{i,j=1}^4\, m_{gP}.} \tag{194.1}$$

Dies ist ein wohldefiniertes Element von $C^4(A,A)$. Es ist **vollständig alternierend**: $\operatorname{Alt}_4 L_\lambda^{\det} = L_\lambda^{\det}$.

**Gewicht:** Die Determinante erhält unter $\alpha_t$ den Faktor $P^{-it}$; $\alpha_t(m_{gP}) = (gP)^{it}m_{gP}$. Zusammen:
$$\alpha_t^C L_\lambda^{\det} = g^{it} L_\lambda^{\det}.$$

$$\boxed{L_\lambda^{\det} \in C^4(A,A)_\lambda.} \tag{194.2}$$

---

## 4. Explizite Paarungsrechnung [O-193-4c]

Für jede Permutation $\pi \in S_4$:
$$\det\!\bigl(f_i(\mu_{p_{\pi(j)}})\bigr)_{i,j=1}^4 = \operatorname{sgn}(\pi),$$

da die Matrix $(\delta_{i,\pi(j)})$ eine Permutationsmatrix mit Determinante $\operatorname{sgn}(\pi)$ ist. Also:
$$L_\lambda^{\det}(\mu_{p_{\pi(1)}}, \mu_{p_{\pi(2)}}, \mu_{p_{\pi(3)}}, \mu_{p_{\pi(4)}}) = \operatorname{sgn}(\pi)\, m_{gP}.$$

Die Paarung mit dem Zyklus aus NEU-193:
$$\left\langle L_\lambda^{\det}, z_{-\lambda}^{g,\mathbf{p}} \right\rangle = \sum_{\pi\in S_4} \operatorname{sgn}(\pi)^2\, \varepsilon_{gP}(m_{gP}) = \sum_{\pi\in S_4} 1 = 24.$$

$$\boxed{\left\langle L_\lambda^{\det}, z_{-\lambda}^{g,\mathbf{p}} \right\rangle = 4! \neq 0.} \tag{194.3}$$

$$\boxed{[O\text{-}193\text{-}4c] \quad \checkmark[M]}$$

Ein expliziter gewichteter, alternierender Vierkochain mit nichtverschwindender Paarung existiert. Dies schließt die Paarungsfrage für $L_{3,\lambda}$ selbst noch nicht, solange keine Identifikation $L_{3,\lambda} = L_\lambda^{\det}$ oder eine kontrollierte alternierende Komponente vorliegt.

---

## 5. Hochschild-Kozykeltest

Die Hochschild-Korandformel:

$$(bL)(a_0,a_1,a_2,a_3,a_4) = a_0 L(a_1,a_2,a_3,a_4) - L(a_0a_1,a_2,a_3,a_4) + L(a_0,a_1a_2,a_3,a_4) - L(a_0,a_1,a_2a_3,a_4) + L(a_0,a_1,a_2,a_3a_4) - L(a_0,a_1,a_2,a_3)a_4. \tag{194.4}$$

Testtupel: Sei $q \notin \{p_1,p_2,p_3,p_4\}$ eine weitere Primzahl. Werte $(bL_\lambda^{\det})$ auf $(\mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4})$ aus.

### Term 1 (erster äußerer Term)
$$a_0 L(a_1,a_2,a_3,a_4) = \mu_q \cdot L_\lambda^{\det}(\mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4}) = \mu_q m_{gP}.$$

Nichtverschwindung: aus $\mu_q m_{gP} = 0$ würde $\mu_q^* \mu_q m_{gP} = m_{gP} = 0$ folgen, Widerspruch. Also $\mu_q m_{gP} \neq 0$.

### Term 2 (erster innerer Term)
$$-L_\lambda^{\det}(\mu_q\mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4}).$$

Der erste Slot hat Grad $qp_1 \notin \{p_1,p_2,p_3,p_4\}$. Alle $f_i$ verschwinden auf $A_{qp_1}$. Also: Term $= 0$.

### Terme 3–5 (weitere innere Terme)
In jedem Term tritt entweder der fremde Grad $q$ (Slot 0 nach Aufspaltung) oder ein zusammengesetzter Grad $p_ip_j$ in einem einzelnen Slot auf. Keiner dieser Grade liegt in $\{p_1, p_2, p_3, p_4\}$. Alle weiteren inneren Terme verschwinden.

### Term 6 (letzter äußerer Term)
$$-L_\lambda^{\det}(\mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}) \cdot \mu_{p_4}.$$

Der erste Slot hat Grad $q \notin \{p_1,p_2,p_3,p_4\}$, Grad $p_4$ fehlt komplett. Determinante verschwindet. Term $= 0$.

### Gesamtergebnis

$$(bL_\lambda^{\det})(\mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4}) = \mu_q m_{gP} \neq 0. \tag{194.5}$$

$$\boxed{bL_\lambda^{\det} \neq 0.}$$

$$\boxed{[O\text{-}194\text{-}\det\text{-coc}] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 6. Strukturelle Diagnose

### Mechanismus des Scheiterns

Der erste äußere Hochschild-Face
$$a_0 L(a_1, a_2, a_3, a_4)$$
kann durch Voranstellen einer neuen Isometrie $\mu_q$ (mit $q$ außerhalb des endlichen Multigradträgers) nicht mit einem Korrektursummanden kompensiert werden: alle inneren Terme verschwinden, während $\mu_q m_{gP} \neq 0$ wegen $\mu_q^* \mu_q = 1$.

### Ausgeschlossene Klasse

> **Nichtnullige Vierkochains mit festem nichtverschwindendem Zielvektor und endlichem isoliertem Multigradträger können die Hochschild-Kozykelbedingung nicht allein durch Slotalternierung erfüllen.**

Dies ist ein struktureller Ausschluss einer Kandidatenklasse, kein globaler Ausschluss geladener Vierkozyklen.

### Notwendige Bedingungen für den nächsten Kandidaten

Ein geladener Vierkozykel mit nichtverschwindender Paarung muss mindestens eine der folgenden Eigenschaften besitzen:

| Eigenschaft | Begründung |
|---|---|
| **Unendliche oder dichte Gradfamilie** | ermöglicht Kompensation des ersten äußeren Faces über unendlich viele Gradkomponenten |
| **Derivationsartige Slotabbildungen** | $f(ab) = f(a)b + af(b)$ liefert Korrekturbeiträge bei Gradmultiplikation |
| **Cup-/Shuffle-Konstruktion** | bereits kozyklische Faktoren garantieren $b(\phi \cup \psi) = 0$ strukturell |
| **Tensorprodukt bekannter Kozykel** | falls $HH^1 \otimes HH^3$ oder $HH^2 \otimes HH^2$ einen nichttrivialen Cup-Anteil liefert |

---

## 7. DAG-Stand

| Knoten | Inhalt | Status |
|---|---|---|
| [O-193-4a] | Alternierungsreduktion: Paarung $= 4!\,\varepsilon(\operatorname{Alt}_4 L)$ | $\checkmark[M]$ |
| [O-193-4b] | Symmetrische NEU-176-Schablone: Paarung $= 0$ | $\checkmark[M]_{\mathrm{neg}}$ |
| [O-193-4c] | Determinantisches Modell: Paarung $= 4! \neq 0$ | $\checkmark[M]$ |
| [O-194-det-coc] | Determinantisches Modell: $bL_\lambda^{\det} \neq 0$ | $\checkmark[M]_{\mathrm{neg}}$ |
| [O-193-4] | Nichtverschwindende Paarung für echten Kozykel | $?[O]$ |
| [O-193-5] | Dualer Zeuge für [O-176-3] | $?[O]$ gesperrt |

```
NEU-176-Schablone (symm.)  -->  Alt_4 L = 0         -->  [O-193-4b] ✓[M]_neg
Det.-Modell (alternierende)  -->  Paarung = 4! != 0  -->  [O-193-4c] ✓[M]
Det.-Modell                  -->  bL != 0            -->  [O-194-det-coc] ✓[M]_neg

[O-193-4] ?[O]  offen fuer:  endliche Gradfamilie / Derivation / Cup-Konstruktion
```

$$\boxed{\text{Nächster Schritt: Kandidat mit echter Hochschild-Kompensation der äußeren Faces.}}$$
