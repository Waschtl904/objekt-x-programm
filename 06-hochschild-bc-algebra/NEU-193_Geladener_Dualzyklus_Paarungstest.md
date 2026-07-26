# NEU-193 — Geladener Dualzyklus und Paarungstest
*(Revision 2: Alternierungsfilter und Teilbefunde [O-193-4a/b], 2026-07-19)*

## Vorbemerkung

Dieser Knoten folgt dem DAG-Stand nach AUDIT-2026-07-19 (Rev. 2). [O-193-2] war als offen (nicht gesperrt) klassifiziert; die Konstruktion des Dualzyklus ist unabhängig von der noch unvollständigen auswertbaren Formel für $L_{3,\lambda}$.

---

## Ausgangsdaten

Sei
$$A = \bigoplus_{q\in\Gamma} A_q, \qquad \Gamma = \mathbb{Q}_+^\times,$$
mit $\alpha_t(a_q) = q^{it}a_q$, und $P_q: A \to A_q$ die homogene Projektion.

Der in NEU-185 konstruierte Augmentationscharakter:
$$\varepsilon: A \longrightarrow \mathbb{C}, \qquad \varepsilon(e(r)) = \varepsilon(\mu_n) = \varepsilon(\mu_n^*) = 1.$$

Für jedes $q \in \Gamma$ sei:
$$\boxed{\varepsilon_q := \varepsilon \circ P_q \in A^\vee.}$$

---

## 1. Nichtverschwindung von $\varepsilon_q$

Für $q = a/b \in \mathbb{Q}_+^\times$ liegt $x_q := \mu_a \mu_b^* \in A_q$ und
$$\varepsilon_q(x_q) = \varepsilon(\mu_a\mu_b^*) = 1.$$

Also: $\varepsilon_q \neq 0$.

---

## 2. Duales Gewicht

Für $x \in A_q$: $\alpha_{-t}(x) = q^{-it}x$. Damit:
$$(\alpha_t^\vee \varepsilon_q)(x) = \varepsilon_q(\alpha_{-t}(x)) = q^{-it}\varepsilon_q(x).$$

$$\boxed{\alpha_t^\vee \varepsilon_q = q^{-it}\varepsilon_q,}$$

additives Gewicht $-\log q$.

---

## 3. Ausgeglichene Modulwirkung

Für die duale Bimodulwirkung $(a \cdot f \cdot b)(x) = f(bxa)$ gilt:

$$(\varepsilon_q \cdot \mu_n)(x) = \varepsilon_q(\mu_n x) = \varepsilon(\mu_n P_{q/n} x) = \varepsilon(P_{q/n}x),$$
$$(\mu_n \cdot \varepsilon_q)(x) = \varepsilon_q(x\mu_n) = \varepsilon(P_{q/n}x\,\mu_n) = \varepsilon(P_{q/n}x).$$

Somit gilt die exakte Identität:

$$\boxed{\varepsilon_q \cdot \mu_n = \mu_n \cdot \varepsilon_q = \varepsilon_{q/n}.} \tag{193.1}$$

---

## 4. Gewichtskorrektur

Seien $p_1, p_2, p_3, p_4$ paarweise verschiedene Primzahlen, $P := p_1 p_2 p_3 p_4$.

Die vier Faktoren $\mu_{p_i}$ tragen zusammen das Gewicht $\log P$. Das Dualfunktional muss das Gewicht $-\lambda - \log P = -\log(gP)$ tragen. Daher:
$$h := gP, \qquad \varepsilon_h = \varepsilon_{gP}.$$

---

## 5. Expliziter Kandidat

$$\boxed{z_{-\lambda}^{\,g,\mathbf{p}} := \sum_{\pi\in S_4} \operatorname{sgn}(\pi)\, \varepsilon_{gP} \otimes \mu_{p_{\pi(1)}} \otimes \mu_{p_{\pi(2)}} \otimes \mu_{p_{\pi(3)}} \otimes \mu_{p_{\pi(4)}}.} \tag{193.2}$$

**Endlichkeit:** $|S_4| = 24$ Summanden. Algebraisch endlich.

**Nichtverschwindung:** Die $\mu_{p_i}$ liegen in verschiedenen homogenen Komponenten $A_{p_i}$; die 24 Tensoren liegen in verschiedenen Multigradkomponenten von $A^{\otimes 4}$. Gegenseitige Auslöschung unmöglich. Da $\varepsilon_{gP} \neq 0$: $z_{-\lambda}^{\,g,\mathbf{p}} \neq 0$.

**Gesamtgewicht:**
$$\alpha_t^{C_\bullet}\!\left(z_{-\lambda}^{\,g,\mathbf{p}}\right) = g^{-it}\, z_{-\lambda}^{\,g,\mathbf{p}} = e^{-it\lambda}\, z_{-\lambda}^{\,g,\mathbf{p}}.$$

$$\boxed{z_{-\lambda}^{\,g,\mathbf{p}} \in C_4(A, A^\vee)_{-\lambda}.} \tag{193.3}$$

---

## 6. Vollständiger Randtest

$$\partial(\varphi\otimes a_1\otimes a_2\otimes a_3\otimes a_4) = (\varphi\cdot a_1)\otimes a_2\otimes a_3\otimes a_4 - \varphi\otimes a_1 a_2\otimes a_3\otimes a_4 + \varphi\otimes a_1\otimes a_2 a_3\otimes a_4 - \varphi\otimes a_1\otimes a_2\otimes a_3 a_4 + (a_4\cdot\varphi)\otimes a_1\otimes a_2\otimes a_3. \tag{193.4}$$

### 6.1 Innere Randterme

$\mu_m\mu_n = \mu_{mn} = \mu_n\mu_m$ im Isometriesektor. Für jede Permutation $\pi$ und Transposition zweier benachbarter Slots: entgegengesetztes Vorzeichen, identischer Produktterm. Alle inneren Randterme verschwinden.

### 6.2 Äußere Randterme

**Erster Rand:** $E_0 = \sum_{\pi}\operatorname{sgn}(\pi)\,(\varepsilon_{gP}\cdot\mu_{p_{\pi(1)}})\otimes\mu_{p_{\pi(2)}}\otimes\mu_{p_{\pi(3)}}\otimes\mu_{p_{\pi(4)}}$. Nach (193.1): $\varepsilon_{gP}\cdot\mu_{p_{\pi(1)}} = \varepsilon_{gP/p_{\pi(1)}}$.

**Letzter Rand:** Zyklische Umordnung $(\pi(1),\pi(2),\pi(3),\pi(4)) \mapsto (\pi(4),\pi(1),\pi(2),\pi(3))$ mit Vorzeichen $(-1)^3 = -1$; aus (193.1) folgt $\mu_{p_{\rho(1)}}\cdot\varepsilon_{gP} = \varepsilon_{gP}\cdot\mu_{p_{\rho(1)}}$. Also $E_4 = -E_0$.

$$\boxed{\partial z_{-\lambda}^{\,g,\mathbf{p}} = 0.} \tag{193.5}$$

---

## 7. Alternierungsfilter und Paarungsformel

### 7.1 Reduktion auf den alternierenden Anteil

Definiere für $L \in C^4(A,A)$:

$$\operatorname{Alt}_4 L(a_1,a_2,a_3,a_4) := \frac{1}{4!}\sum_{\pi\in S_4}\operatorname{sgn}(\pi)\, L(a_{\pi(1)}, a_{\pi(2)}, a_{\pi(3)}, a_{\pi(4)}).$$

Dann gilt exakt:

$$\boxed{\left\langle L_{3,\lambda},\, z_{-\lambda}^{\,g,\mathbf{p}} \right\rangle = 4!\, \varepsilon\!\left( \operatorname{Alt}_4 L_{3,\lambda}(\mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4}) \right).} \tag{193.6}$$

**Der Dualzyklus $z_{-\lambda}^{\,g,\mathbf{p}}$ detektiert ausschließlich den vollständig alternierenden Anteil von $L_{3,\lambda}$.**

### 7.2 Vollständige Paarungsformel (entfaltete Form)

$$\left\langle L_{3,\lambda},\, z_{-\lambda}^{\,g,\mathbf{p}} \right\rangle = \sum_{\pi\in S_4} \operatorname{sgn}(\pi)\, \varepsilon\!\left( L_{3,\lambda}(\mu_{p_{\pi(1)}}, \ldots, \mu_{p_{\pi(4)}}) \right). \tag{193.7}$$

---

## 8. Teilbefund [O-193-4b]: Negativer Ausschluss der NEU-176-Schablone

### 8.1 Symmetrie der ursprünglichen Schablone

Die ursprüngliche NEU-176-Produktformel hat die Form:

$$L_{3,\lambda}(a_1,a_2,a_3,a_4) = \sum_k c_k\, f_k(a_1)f_k(a_2)f_k(a_3)f_k(a_4)\, m_k.$$

Jeder einzelne Summand ist **vollständig symmetrisch** in den vier Eingangsslots (dasselbe Funktional $f_k$ in allen vier Positionen). Daher:

$$\operatorname{Alt}_4 L_{3,\lambda} = 0 \qquad \text{(identisch)}.$$

### 8.2 Negativer Befund

$$\boxed{\left\langle L_{3,\lambda},\, z_{-\lambda}^{\,g,\mathbf{p}} \right\rangle = 0}$$

für jeden Kandidaten des symmetrischen Produkttyps aus NEU-176.

Dies ist **kein fehlender Quellenimport**, sondern ein mathematischer Ausschluss: Die Paarungsroute mit $z_{-\lambda}^{\,g,\mathbf{p}}$ ist für die symmetrische Schablone strukturell negativ.

$$\boxed{[O\text{-}193\text{-}4b] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 9. Atomare Restfrage und strukturelle Konsequenz

### 9.1 Notwendige Bedingung für [O-193-4]

Eine nichtverschwindende Paarung erfordert zwingend:

$$\operatorname{Alt}_4 L_{3,\lambda} \neq 0.$$

Die symmetrische Schablone erfüllt dies nicht. Ein geeigneter Kandidat muss **tatsächlich antisymmetrische Slot-Abhängigkeit** besitzen, zum Beispiel durch determinantischen Aufbau:

$$L_{3,\lambda}^{\mathrm{alt}}(a_1,a_2,a_3,a_4) = \sum_k c_k\, \det\!\bigl(f_{k,i}(a_j)\bigr)_{i,j=1}^4\, m_k,$$

oder durch explizite Anwendung von $\operatorname{Alt}_4$ auf einen nichtsymmetrischen Rohkochain.

### 9.2 Geschlossene Teilknoten

$$\boxed{[O\text{-}193\text{-}4a] \quad \checkmark[M]}$$

Alternierungsreduktion der Paarung: die Formel (193.6) ist vollständig bewiesen.

$$\boxed{[O\text{-}193\text{-}4b] \quad \checkmark[M]_{\mathrm{neg}}}$$

Symmetrische NEU-176-Schablone (identisches $f_k$ in allen Slots): Paarung verschwindet identisch.

### 9.3 Globale offene Frage

$$\boxed{\text{Besitzt der intendierte Kozykelkandidat einen nichtverschwindenden alternierenden Vier-Slot-Anteil?}}$$

Der Knoten [O-193-4] bleibt offen, aber **ausschließlich für eine verallgemeinerte Formel** mit getrennten Slotfunktionalen $f_{k,1}, f_{k,2}, f_{k,3}, f_{k,4}$ und nichtverschwindendem $\operatorname{Alt}_4 L_{3,\lambda}$.

---

## DAG-Gesamtstand

| Knoten | Inhalt | Status |
|---|---|---|
| [O-193-2] | $z_{-\lambda}^{\,g,\mathbf{p}} \in C_4(A,A^\vee)_{-\lambda}$, nichtverschwindend | $\checkmark[K]$ |
| [O-193-3] | $\partial z_{-\lambda}^{\,g,\mathbf{p}} = 0$ | $\checkmark[M]$ |
| [O-193-4a] | Alternierungsreduktion: Paarung $= 4!\,\varepsilon(\operatorname{Alt}_4 L_{3,\lambda}(\ldots))$ | $\checkmark[M]$ |
| [O-193-4b] | Symmetrische NEU-176-Schablone: Paarung $= 0$ | $\checkmark[M]_{\mathrm{neg}}$ |
| [O-193-4] | $\langle L_{3,\lambda}^{\mathrm{alt}}, z_{-\lambda}\rangle \neq 0$ für alternierenden Kandidaten | $?[O]$ |
| [O-193-5] | Dualer Zeuge für [O-176-3] | $?[O]$ gesperrt an [O-193-4] |

```
[O-193-1a]  ✓[K]
[O-193-1b]  ✓[M]
[O-193-1c]  ✓[M]
[O-193-2a]  ✓[M]_part   (NEU-176: symm. Schablone; det.-Form benötigt)
[O-193-2]   ✓[K]        Kandidat z_{-λ}^{g,p}
[O-193-3]   ✓[M]        Randtest
[O-193-4a]  ✓[M]        Alternierungsreduktion
[O-193-4b]  ✓[M]_neg    symmetrische Schablone ausgeschlossen
[O-193-4]   ?[O]        offen fuer alternierende Formel mit Alt_4 L_{3,λ} != 0
[O-193-5]   ?[O]
```

$$\boxed{\text{Nächster Schritt: Konstruktion eines Kozykelkandidaten }L_{3,\lambda}^{\mathrm{alt}}\text{ mit }\operatorname{Alt}_4 L_{3,\lambda}^{\mathrm{alt}} \neq 0.}$$
