# NEU-259 — Direktaudit des finite-Intervall-Grenzwertwegs als Objekt-X-Träger

**Katalog-ID:** NEU-259  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Fünf atomare Fragen zum Finite-Intervall-Grenzwertweg (Suzuki 2026). Strenge Trennung Satz/Vermutung. Identifikation des BC/Adelen-Eintrittspunkts.  
**Vorgänger:** NEU-258 $\checkmark$, NEU-257 (Patch), NEU-252 (Patch), NEU-250-Serie  
**Nachfolger:** NEU-260 (Schnittstelle BC/Adelen $\leftrightarrow$ finite Weil-Operatoren)

---

## 0. Motivation und Diagramm

NEU-257 $\checkmark[K/M]$: $H_0=L^2(\mathbb{R},du)$ ist nicht der Weil-Abschlussraum. Suzuki 2026 konstruiert RH-frei für jedes $a>0$ einen selbstadjungierten Operator $A_a$ auf einem endlichen Weil-Hilbertraum $\mathcal{H}_a$. Das führt zum Diagramm:

$$
\boxed{ \mathcal{H}_a \quad\xrightarrow[a\to\infty]{\ ?\ }\quad \mathcal{K}_X \quad\xrightarrow[\mathrm{RH}]{\sim}\quad \mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma). } \qquad (0\text{-Diag})
$$

**Objekt X** in dieser Sichtweise: nicht primär ein einzelner Operator auf Haar-$L^2$, sondern das System
$$
\boxed{\{\mathcal{H}_a,\;J_{a,b},\;A_a\}_{0<a<b},} \qquad (0\text{-Sys})
$$
mit arithmetisch bestimmten kanonischen Übergangsabbildungen $J_{a,b}:\mathcal{H}_a\to\mathcal{H}_b$ und einem kanonischen Grenzwert $\mathcal{K}_X:=\varinjlim_a\mathcal{H}_a$.

**Doppelte Aufgabe:** Suzuki liefert die globale Operatorhülle; BC/Adelen sollen die arithmetische Herkunft erklären.

---

## Frage 1 — RH-freie Existenz: $Q_W^a$, $A_a$, $\mathcal{H}(A_a)$

### 1.1 Was Suzuki 2026 beweist (Satz-Status)

Nach Suzuki (2026, Thm.~1.1 und §{}2): Für jedes $a>0$ ist die auf $C_c^\infty(-a,a)$ restringierte Weil-Quadratikform
$$
Q_W^a(f,g):=B_W(f,g)\big|_{\operatorname{supp}(f),\operatorname{supp}(g)\subset(-a,a)} \qquad (1\text{-QWa})
$$
semibeschränkt und abschließbar auf
$$
L^2(-a,a):=L^2((-a,a),du). \qquad (1\text{-L2a})
$$

**Warum das kein Widerspruch zu NEU-257 ist:** NEU-257 $\times[M]$ betrifft das volle $L^2(\mathbb{R})$; auf dem kompakten Intervall $(-a,a)$ ist das Spektralmaß $\mu_W^a:=\mu_W|_{[-a,a]}$ noch endlich und die Singularität gegenüber Lebesgue erzwingt keine Nichtabschließbarkeit, weil der Träger beschränkt ist. Die Kompaktheit regularisiert.

$$
\boxed{Q_W^a\text{ semibeschränkt und abschließbar auf }L^2(-a,a)\quad\checkmark\text{ (Suzuki 2026, Satz)}} \qquad (1\text{-Close})
$$

Die **Friedrichs-Erweiterung** von $Q_W^a$ liefert einen selbstadjungierten Operator:
$$
\boxed{A_a=A_a^*\ge-\lambda_a I\text{ auf }L^2(-a,a),\quad\text{diskretes Spektrum.}\quad\checkmark\text{ (Suzuki 2026, Satz)}} \qquad (1\text{-Aa})
$$

Der zugeordnete Weil-Hilbertraum:
$$
\mathcal{H}(A_a):=\overline{C_c^\infty(-a,a)}^{\|\cdot\|_{Q_W^a+\lambda_a+1}},\qquad\|f\|_{\mathcal{H}(A_a)}^2:=Q_W^a(f,f)+(\lambda_a+1)\|f\|_{L^2(-a,a)}^2. \qquad (1\text{-Ha})
$$

$$
\text{Domänen und Skalarprod. von }Q_W^a,A_a,\mathcal{H}(A_a):\quad\checkmark\text{ (Suzuki 2026, Satz)} \qquad (1\text{-Dom})
$$

### 1.2 Offene Punkte

$$
\text{Exakte Abhängigkeit }\lambda_a\text{ von }a?\quad?[O] \qquad (1\text{-lam})
$$
$$
\text{Verhalten }\sigma(A_a)\text{ für endliche }a\text{ (numerisch, Literatur)?}\quad?[O] \qquad (1\text{-Spec})
$$

---

## Frage 2 — Identifikation $B_W|_{C_c^\infty(-a,a)}\stackrel{?}{=}Q_W^a$

### 2.1 Die Frage

$$
\boxed{B_W(f,g)\stackrel{?}{=}Q_W^a(f,g)\quad\forall f,g\in C_c^\infty(-a,a).\quad?[O]} \qquad (2\text{-ID})
$$

Das ist keine Namensgleichheit; es ist eine explizite Formelidentifikation.

### 2.2 Was zu zeigen ist

Von NEU-252/258 gilt:
$$
B_W(f,f)=B_{\rm pole}(f,f)+B_\Gamma(f,f)+B_{\rm fin}(f,f). \qquad (2\text{-BW})
$$

Suzuki definiert $Q_W^a$ über die Weil-Explizitformel auf $C_c^\infty(-a,a)$ mit derselben Fourierkonvention (NEU-258 $\checkmark[K/M]$). Da die Identifikation $W_{\rm NEU-252}=W_{\rm Lit}$ durch NEU-258 bereits $\checkmark[K/M]$ ist, ist $(2\text{-ID})$ vor allem eine Aussage über den Trägereinschränkungsoperator:
$$
B_W|_{C_c^\infty(-a,a)}\text{ bedeutet: alle drei Blöcke }B_{\rm pole},B_\Gamma,B_{\rm fin}\text{ auf }C_c^\infty(-a,a)\text{ ausgewertet.} \qquad (2\text{-Blocks})
$$

Der Gammafaktor und der Primblock sind translation- und dilatationsinvariant; ihre Einschränkung auf $C_c^\infty(-a,a)$ ergibt genau die in Suzuki verwendeten Teilformen. Der Polblock muss separat verglichen werden (Endlichdimensionalität vs. Randbeitrag).

$$
B_{\rm pole}|_{C_c^\infty(-a,a)}=Q_{W,\rm pole}^a?\quad?[O]\to\text{Polterm-Vergleich} \qquad (2\text{-Pole})
$$
$$
(B_\Gamma+B_{\rm fin})|_{C_c^\infty(-a,a)}=Q_{W,\Gamma+\rm fin}^a?\quad\checkmark\text{ (aus NEU-258 und Suzuki-Konvention)} \qquad (2\text{-GamFin})
$$
$$
B_W|_{C_c^\infty(-a,a)}=Q_W^a\quad?[O]\text{ (offen bis Polterm-Vergleich)} \qquad (2\text{-Final})
$$

---

## Frage 3 — Satz vs. Vermutung im Grenzwert $a\to\infty$

**Strikte Trennung:**

| Aussage | Status | Quelle |
|---|---|---|
| $Q_W^a$ semibeschränkt und abschließbar auf $L^2(-a,a)$ | $\checkmark$ **Satz** | Suzuki 2026 |
| $A_a=A_a^*$, diskretes Spektrum nach unten beschränkt | $\checkmark$ **Satz** | Suzuki 2026 |
| Friedrichs-Erweiterung wohldefiniert | $\checkmark$ **Satz** | Standard + Suzuki |
| $\mathcal{H}(A_a)$ wohldefinierter Hilbertraum | $\checkmark$ **Satz** | Suzuki 2026 |
| $\exists$ kanonische Einbettung $J_{a,b}:\mathcal{H}_a\hookrightarrow\mathcal{H}_b$, $a<b$ | $?[O]$ **offen** | — |
| $\varinjlim_a\mathcal{H}_a$ existiert kanonisch | $?[O]$ **offen** | — |
| $\sigma(A_a)\xrightarrow{a\to\infty}\{\gamma_n\}$ (Nullstellenordinaten) | $\mathbf{Vermutung}$ | Suzuki 2026, Conj. |
| Grenzoperator $A_\infty$ mit $\sigma(A_\infty)=\{\gamma_n\}$ | $\mathbf{Vermutung}$ | Suzuki 2026, Conj. |

$$
\boxed{\text{Satz-Bereich: Alles Endliche.}\quad\text{Vermutungs-Bereich: Grenzwert und Nullstellenspektrum.}} \qquad (3\text{-Split})
$$

---

## Frage 4 — Kanonische Übergangsabbildungen $J_{a,b}:\mathcal{H}_a\to\mathcal{H}_b$

Das ist die Schlüsselfrage für einen kanonischen globalen Grenzwert.

### 4.1 Was benötigt wird

Für ein gerichtetes System $\{\mathcal{H}_a,J_{a,b}\}_{a<b}$ mit $\varinjlim_a\mathcal{H}_a=\mathcal{K}_X$ brauchen wir:

1. **Injektivität:** $J_{a,b}$ injektiv (oder isometrisch).
2. **Kompatibilität:** $J_{b,c}\circ J_{a,b}=J_{a,c}$ für $a<b<c$.
3. **Operator-Kompatibilität:** $J_{a,b}A_a=A_b J_{a,b}$ (oder eine schwache Version davon).
4. **Arithmetische Kanonizität:** $J_{a,b}$ soll nicht ad hoc sein, sondern aus der Struktur folgen.

### 4.2 Natürliche Kandidaten

**Kandidat I — Nullfortsetzung:** $J_{a,b}^{\rm ext}f:=f\cdot\mathbf{1}_{(-a,a)}$ als Element von $L^2(-b,b)$. Das ist wohldefiniert als $L^2$-Einbettung, aber nicht isometrisch bezüglich $\|\cdot\|_{\mathcal{H}(A_b)}$, weil $Q_W^b(J^{\rm ext}f,J^{\rm ext}f)\neq Q_W^a(f,f)$ im Allgemeinen (Randterme).

**Kandidat II — Adjungierte der Restriktion:** Falls $R_{a,b}:\mathcal{H}_b\to\mathcal{H}_a$ die Restriktionsabbildung $R_{a,b}g=g|_{(-a,a)}$ ist, dann $J_{a,b}:=(R_{a,b})^*$ adjungiert in den Form-Skalarprodukten. Ob das isometrisch ist, hängt von Randbedingungen ab.

**Kandidat III — BC/adelische Selektion:** Die kanonische $J_{a,b}$ wird nicht durch $L^2$-Geometrie, sondern durch die adelische Multiplikationsstruktur ausgewählt. Das wäre der BC/Adelen-Eintrittspunkt.

$$
\boxed{\text{Kanonische }J_{a,b}\text{ aus der Formgeometrie allein: }?[O].\quad\text{BC/adelische Selektion: }?[O]\to\text{NEU-260.}} \qquad (4\text{-Jab})
$$

### 4.3 Ohne $J_{a,b}$: was fehlt

Ohne kompatibles gerichtetes System: Kein kanonischer $\mathcal{K}_X$. Die $\mathcal{H}_a$ wären lediglich eine Folge nicht zusammenhängender endlicher Hilberträume, kein Objekt.

$$
\boxed{\text{Objekt X }=\{\mathcal{H}_a,J_{a,b},A_a\}_{a<b}\text{ mit arithmetisch kanonischen }J_{a,b}:\quad\text{Kernhypothese, }?[O].} \qquad (4\text{-ObjX})
$$

---

## Frage 5 — BC/Adelen-Eintrittspunkt

### 5.1 Was die NEU-250-Serie bereits liefert

Aus NEU-250-Serie $\checkmark[K/M]$:
$$
\frac{\Lambda(p^k)}{\sqrt{p^k}}\text{ entsteht lokal aus BC/Frobenius/Nakayama plus Energie.} \qquad (5\text{-BC})
$$

Das erklärt die arithmetische Herkunft des Primblock-Vorfaktors, nicht aber:
- Warum gerade die Suzuki-Operatorenfamilie $\{A_a\}$ arithmetisch ausgezeichnet ist.
- Wie $J_{a,b}$ aus der BC-Struktur folgt.

### 5.2 Der Eintrittspunkt

Drei mögliche Eintrittspunkte für BC/Adelen in die Suzuki-Geometrie:

| Eintrittspunkt | Beschreibung | Status |
|---|---|---|
| **E1: Vorfaktor** | $\Lambda(p^k)/\sqrt{p^k}$ als BC-Gewicht in $Q_W^a$ | $\checkmark[K/M]$ (NEU-250) |
| **E2: Ma\ss{}selektion** | BC-KMS-Zustand selektiert kanonisches Spektralma\ss{} $\mu_X^a$ auf $(-a,a)$ | $?[O]$ |
| **E3: Morphismus** | Frobenius-/Hecke-Symmetrien bestimmen $J_{a,b}$ kanonisch | $?[O]\to$NEU-260 |

$$
\boxed{\text{BC/Adelen erklären arithmetische Kanonizität der }J_{a,b};\text{ das ist der NEU-260-Auftrag.}} \qquad (5\text{-BC-Task})
$$

### 5.3 Strategisches Bild

$$
\boxed{ \underbrace{\text{BC/Adelen}}_{\text{arithmetische Herkunft}}\longrightarrow\underbrace{J_{a,b}\text{ kanonisch}}_{\text{NEU-260}}\longrightarrow\underbrace{\mathcal{K}_X=\varinjlim_a\mathcal{H}_a}_{\text{Objekt X}}\xrightarrow{\text{RH}}\underbrace{\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)}_{\text{Weil-Hilbertraum}}. } \qquad (5\text{-Chain})
$$

---

## 6. Offene Punkte und Prioritäten

$$B_W|_{C_c^\infty(-a,a)}=Q_W^a\text{ vollständig (Polterm-Vergleich)}\quad?[O]\qquad(6\text{-a})$$
$$\text{Exakte }\lambda_a\text{-Abhängigkeit von }a\quad?[O]\qquad(6\text{-b})$$
$$\text{Kanonische }J_{a,b}\text{ aus Formgeometrie}\quad?[O]\qquad(6\text{-c})$$
$$\text{BC/adelische Selektion von }J_{a,b}\quad?[O]\to\text{NEU-260}\qquad(6\text{-d})$$
$$\sigma(A_a)\to\{\gamma_n\}\text{ (Suzuki-Vermutung, kein Satz)}\quad\mathbf{Vermutung}\qquad(6\text{-e})$$
$$\mathcal{K}_X=\varinjlim_a\mathcal{H}_a\text{ kanonisch wohldefiniert}\quad?[O]\qquad(6\text{-f})$$
$$\mathcal{K}_X\xrightarrow{\rm RH}\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\quad?[O]\qquad(6\text{-g})$$

---

## 7. Rangfolge der drei Wege (aktualisiert)

| Weg | Kurzfristige Chance | Tiefe für Objekt X | Empfehlung |
|---|---|---|---|
| Finite Intervalle / Suzuki | **hoch** (Operatoren existieren) | hoch | NEU-259/260 Hauptstrang |
| BC-/adelische Spektralquelle | mittel | sehr hoch | NEU-260 Eintrittspunkt |
| Moment-/Resolventenweg | mittel | mittel | Reserveoption |

---

## 8. Statusbuchungen

$$Q_W^a\text{ semibeschränkt, abschließbar auf }L^2(-a,a)\quad\checkmark[K/M]\text{ (Suzuki 2026)}\qquad(8\text{-a})$$
$$A_a=A_a^*,\text{ diskretes Spektrum, Friedrichs-Erweiterung}\quad\checkmark[K/M]\text{ (Suzuki 2026)}\qquad(8\text{-b})$$
$$\text{Kompaktintervall-Regularisierung erklärt kein Widerspruch zu NEU-257}\quad\checkmark[K/M]\qquad(8\text{-c})$$
$$(B_\Gamma+B_{\rm fin})|_{C_c^\infty(-a,a)}=Q_{W,\Gamma+\rm fin}^a\quad\checkmark[K/M]\text{ (aus NEU-258)}\qquad(8\text{-d})$$
$$\text{Polterm-Vergleich }B_{\rm pole}|_{C_c^\infty(-a,a)}=Q_{W,\rm pole}^a\quad?[O]\qquad(8\text{-e})$$
$$\text{Kanonische }J_{a,b}\quad?[O]\to\text{NEU-260}\qquad(8\text{-f})$$
$$\sigma(A_a)\to\{\gamma_n\}\quad\mathbf{Vermutung}\text{ (kein Satz)}\qquad(8\text{-g})$$
$$\text{Objekt X als System }\{\mathcal{H}_a,J_{a,b},A_a\}\text{: Kernhypothese}\quad?[O]\qquad(8\text{-h})$$

---

## 9. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-258 | 1fa3745 | $W_{\rm NEU-252}=W_{\rm Lit}$ $\checkmark$ |
| NEU-257 (Patch) | f710da3 | Kato/KLMN $\times[M]$; $\mathcal{H}_W\cong\ell^2$ |
| NEU-252 (Patch) | 4ee78ed | $B_W$-Blockformeln M3 |
| NEU-250-Serie | div. | $\Lambda(p^k)/\sqrt{p^k}$ aus BC/Frobenius |
| Suzuki 2026 | Thm.~1.1, \S{}2, Conj. | $Q_W^a$, $A_a$, $\mathcal{H}(A_a)$; Spektrum-Vermutung |
| Suzuki 2011/2025 | (1.2), Thm.~2.1 | $\mathcal{H}_W\cong L^2(\tau)$ unter RH |
| Kato 1966 | — | Friedrichs-Erweiterung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Gibt NEU-260 (BC/Adelen $\leftrightarrow$ finite Weil-Operatoren) frei.*
