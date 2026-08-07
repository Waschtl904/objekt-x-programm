# NEU-257 — Semibeschränktheit-Closability-Firewall für $B_W$ auf $L^2(\mathbb{R})$

**Katalog-ID:** NEU-257  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Vier Buchungen: (1) $L^2$-Semibeschränktheit $\Leftrightarrow$ RH; (2) Nicht-Abschließbarkeit von $B_W$ auf Haar-$L^2$ unter RH; (3) Kato/KLMN auf $H_0=L^2(\mathbb{R})$ $\times[M]$; (4) $H_0=L^2$ als Referenzgeometrie reinterpretiert.  
**Status:** Buchungen (1)–(4) teils $\checkmark[K/M]$, teils $?[O]$ (Normierungsabgleich ausstehend).  
**Vorgänger:** NEU-256 (Patch), NEU-255 (Patch 2), NEU-220l

---

## 0. Ausgangspunkt

Aus NEU-256 $\checkmark[K/M]$:
- $B_{\rm fin}$ ist nicht separat nach unten $L^2$-beschränkt (Skalierungsfolge).
- $B_\Gamma\ge-C\|\cdot\|_2^2$ (nach unten $L^2$-beschränkt).
- $R_{\rm arith}=B_{\rm pole}+B_{\rm fin}$ als gemeinsamer Auftrag.

Aus NEU-256: Der KLMN-Kandidat $|R_{\rm arith}|\le\alpha q_\Gamma^++C\|\cdot\|_2^2$ wurde als atomarer Test eingetragen. Dieser Commit zeigt, dass dieser Test prinzipiell scheitern muss.

---

## 1. $L^2$-Semibeschränktheit von $B_W$ $\Longleftrightarrow$ RH

### 1.1 Weil-Form als Distribution

Schreibe die Weil-Form distributionsartig:
$$
B_W(a,a)=W(a*\tilde a),\qquad\tilde a(u):=\overline{a(-u)}. \qquad (1\text{-Distr})
$$

Hier ist $W\in\mathcal{D}'(\mathbb{R})$ die Weil-Distribution (NEU-252 §3). Das Faltungsprodukt $a*\tilde a$ ist eine positiv definite glatte kompakt getragene Testfunktion.

### 1.2 Bochner-Schwartz-Argument

**Annahme:** $\exists\lambda<\infty$ mit $B_W(a,a)\ge-\lambda\|a\|_2^2$ für alle $a\in C_c^\infty(\mathbb{R})$.

Da $\delta_0(a*\tilde a)=\|a\|_2^2$, ist
$$
W_\lambda:=W+\lambda\delta_0 \qquad (1\text{-Wlam})
$$
eine positiv-semidefinite Distribution auf $\mathbb{R}$:
$$
W_\lambda(a*\tilde a)=B_W(a,a)+\lambda\|a\|_2^2\ge0\quad\forall a\in C_c^\infty. \qquad (1\text{-PosDef})
$$

**Bochner-Schwartz** (vgl. Reed-Simon II, Thm. IX.10): Jede positiv-semidefinite Distribution auf $\mathbb{R}$ ist temperiert, d.h. $W_\lambda\in\mathcal{S}'(\mathbb{R})$. Da $\delta_0\in\mathcal{S}'$:
$$
\boxed{W\in\mathcal{S}'(\mathbb{R}).} \qquad (1\text{-Tempered})
$$

### 1.3 Getempertheit $\Rightarrow$ RH

Nach dem Weil-Positivitätskriterium in der $\mathcal{S}'$-Form (Literatur: Bombieri 2000; Weil 1952; Suzuki 2011): Ist die Weil-Distribution $W$ temperiert, so gilt die Riemannsche Vermutung.

$$
\boxed{W\in\mathcal{S}'(\mathbb{R})\Longrightarrow\text{RH}.} \qquad (1\text{-WeilS})
$$

### 1.4 RH $\Rightarrow$ Semibeschränktheit

Unter RH liefert Weils Positivitätskriterium sogar:
$$
\text{RH}\Longrightarrow B_W(a,a)\ge0\quad\forall a\in C_c^\infty(\mathbb{R}). \qquad (1\text{-RHPos})
$$

Insbesondere $B_W\ge0\ge-\lambda\|\cdot\|_2^2$ für $\lambda=0$.

### 1.5 Äquivalenz

$$
\boxed{\exists\lambda<\infty:\;B_W(a,a)\ge-\lambda\|a\|_2^2\;\forall a\in C_c^\infty(\mathbb{R})\quad\Longleftrightarrow\quad\text{RH}.} \qquad (1\text{-Equiv})
$$

**Vorbehalt Normierungsabgleich:** Diese Äquivalenz gilt genau dann, wenn $W$ in NEU-252 exakt dieselbe normalisierte Weil-Distribution ist wie in den Quellen zu $(1\text{-WeilS})$. Der Abgleich mit der in NEU-220k fixierten $2\pi$-Fourierkonvention ist formal noch durchzuführen.

$$
\text{Normierungsabgleich }W_{\rm NEU-252}=W_{\rm Weil-Lit}\quad?[O]\to\text{NEU-220k} \qquad (1\text{-Norm})
$$

$$
\boxed{L^2\text{-Semibeschränktheit von }B_W\Longleftrightarrow\text{RH}.\quad\checkmark[K/M]\text{ (vorbehaltlich Normierungsabgleich)}} \qquad (1\text{-Final})
$$

---

## 2. Unter RH: atomare Spektraldarstellung und Nicht-Abschließbarkeit

### 2.1 Spektraldarstellung unter RH

Unter RH (alle Nullstellen auf $\operatorname{Re}(s)=\tfrac{1}{2}$, $\rho=\tfrac{1}{2}+i\gamma$) hat $B_W$ die Darstellung als positives Maß auf den Nullstellenordinaten:
$$
\boxed{B_W(a,b)=\sum_\gamma m_\gamma\,\hat a(-\gamma)\,\overline{\hat b(-\gamma)},} \qquad (2\text{-Spec})
$$
mit $m_\gamma>0$ und $\sum_\gamma$ über alle Nullstellenordinaten $0<\gamma_1\le\gamma_2\le\cdots$ (Suzuki 2011, Formel (1.2); Weil 1952 §5). Das repräsentierende Spektralmaß ist
$$
\mu_W=\sum_\gamma m_\gamma\,\delta_{-\gamma}, \qquad (2\text{-Meas})
$$
ein rein atomares (diskretes) Maß, singulär gegenüber dem Lebesgue-Maß auf $\mathbb{R}$.

### 2.2 Nicht-Abschließbarkeit auf Haar-$L^2$

**Satz:** $B_W$ ist auf $H_0=L^2(\mathbb{R},du)$ nicht abschließbar.

**Beweis (explizite Folge):** Fixiere eine Nullstellenordinate $\gamma_0>0$ und $\phi\in C_c^\infty(\mathbb{R})$ mit $\hat\phi(0)=\int\phi\neq0$. Setze:
$$
a_n(u):=\frac{1}{n}\,e^{-i\gamma_0 u}\phi(u/n),\qquad n\ge1. \qquad (2\text{-Folge})
$$

**$L^2$-Norm:** Substitution $v=u/n$:
$$
\|a_n\|_2^2=\frac{1}{n^2}\int|\phi(u/n)|^2\,du=\frac{1}{n}\|\phi\|_2^2\longrightarrow0. \qquad (2\text{-L2})
$$

**Fourierwert bei $\gamma_0$:** Unter der Konvention $\hat f(t)=\int e^{itu}f(u)\,du$:
$$
\hat a_n(\gamma_0)=\frac{1}{n}\int e^{i\gamma_0 u}e^{-i\gamma_0 u}\phi(u/n)\,du=\frac{1}{n}\int\phi(u/n)\,du=\int\phi(v)\,dv=\hat\phi(0)\neq0. \qquad (2\text{-Four})
$$

Der Fourierwert $\hat a_n(\gamma_0)$ bleibt konstant $\neq0$ für alle $n$.

**Formwert:** Aus der Spektraldarstellung $(2\text{-Spec})$:
$$
B_W(a_n,a_n)\ge m_{\gamma_0}|\hat a_n(-\gamma_0)|^2=m_{\gamma_0}|\hat\phi(0)|^2>0\quad\text{für alle }n. \qquad (2\text{-Form})
$$

**Abschließbarkeitskriterium verletzt:** $a_n\to0$ in $L^2$, aber $B_W(a_n,a_n)\ge c>0$ für alle $n$. Das verletzt genau das Reed-Simon-Kriterium (Thm.~X.23) für Abschließbarkeit.

$$
\boxed{B_W\text{ ist auf }H_0=L^2(\mathbb{R},du)\text{ nicht abschließbar.}\quad\checkmark[K/M]\text{ (unter RH)}} \qquad (2\text{-NonClose})
$$

### 2.3 Allgemeines Prinzip

Das ist kein Spezialergebnis. Für jede positiv-semidefinite Form der Gestalt
$$
q_\mu(f)=\int|\hat f(t)|^2\,d\mu(t)
$$
gilt: $q_\mu$ ist auf $L^2(\mathbb{R},dx)$ genau dann abschließbar, wenn $\mu$ absolut stetig bezüglich des Lebesgue-Maßes ist (klassische Theorie translationsinvarianter Formen, vgl. Fukushima-Oshima-Takeda, Rmk. 1.3.5). Das diskrete Maß $\mu_W=\sum_\gamma m_\gamma\delta_{-\gamma}$ verletzt diese Bedingung maximal.

---

## 3. Kato/KLMN auf $H_0=L^2(\mathbb{R})$ $\times[M]$

$$
\boxed{\text{Kato-Darstellungssatz und KLMN-Formperturbation auf }H_0=L^2(\mathbb{R},du):\quad\times[M].} \qquad (3\text{-KatoOut})
$$

**Begründung (Widerspruch):** Angenommen, $B_W$ wäre auf $H_0$ semibeschränkt und abschließbar.
- Semibeschränktheit $\Rightarrow$ RH (Buchung 1).
- Unter RH: Spektraldarstellung $(2\text{-Spec})$ mit rein atomarem Maß $\Rightarrow$ Nicht-Abschließbarkeit (Buchung 2).
- Widerspruch. $\square$

$$
\boxed{\text{Semibeschränktheit und }L^2\text{-Abschließbarkeit von }B_W\text{ können nicht gleichzeitig gelten.}\quad\checkmark[K/M]} \qquad (3\text{-Incomp})
$$

**Folge für NEU-256 KLMN-Kandidat:** Die relative Formabschätzung
$$
|R_{\rm arith}(a,a)|\le\alpha\,q_\Gamma^+(a,a)+C\|a\|_2^2,\quad\alpha<1 \qquad (\text{NEU-256, Leit-Rel})
$$
kann (unter RH) nicht gelten, weil KLMN daraus genau die verbotene Kombination (semibeschränkt + abschließbar auf $L^2$) erzwingen würde.

$$
\text{KLMN-Kandidat NEU-256 }(\text{Leit-Rel}):\quad\times[M]\text{ (konditional: unter RH)} \qquad (3\text{-KLMN-Out})
$$

---

## 4. $H_0=L^2(\mathbb{R},du)$ reinterpretiert

$$
\boxed{H_0=L^2(\mathbb{R},du):\text{ kanonischer adelischer Hintergrundreferenzraum, nicht der Abschlussraum von }B_W.} \qquad (4\text{-H0Reint})
$$

**Was $H_0$ bleibt:**
- Kanonisch aus Haar-Struktur und $J_{1/2}$: $\checkmark$ (NEU-255).
- Dichter Definitionsbereich $\mathcal{A}_{\rm PW}\subset H_0$: $\checkmark$.
- Topologischer Ankerpunkt für $a_n\to0$ in allen Abschließbarkeitstests: $\checkmark$.
- Normierungsreferenz ($\|a\|_0$ in Feuerwallformulierungen): $\checkmark$.

**Was $H_0$ nicht ist:**
- Der Hilbertraum, in dem $B_W$ eine geschlossene Form besitzt: $\times[M]$.
- Der Raum, in dem $A_X$ über Kato direkt konstruiert werden kann: $\times[M]$.

**Natur der Objekt-X-Geometrie:**

Die eigentliche Objekt-X-Hilbert-/Krein-Geometrie entsteht durch eine arithmetisch veränderte Norm. Unter RH ist das natürliche Bild:
$$
\mathcal{H}_W:=\overline{\mathcal{A}_{\rm PW}}^{\|\cdot\|_W},\qquad\|a\|_W^2:=B_W(a,a)\quad(\text{falls }B_W\ge0\text{ unter RH}). \qquad (4\text{-HW})
$$

Das ist kein $L^2$-Abschluss. Die Topologie wird durch das diskrete Spektralmaß $\mu_W=\sum_\gamma m_\gamma\delta_{-\gamma}$ definiert; Fourierwerte bei den Nullstellenordinaten sind die relevanten Koordinaten. $\mathcal{H}_W$ ist isometrisch zu einem gewichteten $\ell^2$-Raum auf den Nullstellenordinaten.

$$
\boxed{\mathcal{H}_W\cong\ell^2(\{\gamma\},\{m_\gamma\}),\qquad a\mapsto(\sqrt{m_\gamma}\,\hat a(-\gamma))_{\gamma}.} \qquad (4\text{-HWIso})
$$

**Suzuki-Verbindung (2011/2026):** Die Konstruktion selbstadjungierter Operatoren auf endlichen Intervallen mit Screw-Function-Geometrie (Suzuki) entspricht genau dem lokalen Abschnitt dieses diskreten Bildes. Der schwierige globale Grenzübergang ist der Übergang $\mathcal{H}_W\to$ vollständige Objekt-X-Geometrie. Das ist mit unserem unabhängigen Befund konsistent: $H_0=L^2$ ist natürliche Referenz; die eigentliche Geometrie ist singulär darüber.

---

## 5. Neues strategisches Bild

$$
\boxed{ \text{adelische Haarstruktur}\longrightarrow H_0=L^2(\mathbb{R},du)\underbrace{\longrightarrow}_{\text{Abschluss bzgl. }\|\cdot\|_W\text{ unter RH}}\mathcal{H}_W\cong\ell^2(\gamma)\longrightarrow A_X\text{ auf }\mathcal{H}_W. } \qquad (5\text{-Chain})
$$

Das Weil-Kriterium wird zu:
$$
\boxed{\text{RH}\iff\|\cdot\|_W\text{ ist eine Hilbertnorm auf }\mathcal{A}_{\rm PW}\iff\mathcal{H}_W\text{ wohldefiniert}.} \qquad (5\text{-Weil})
$$

**M4-C neu:** Existiert auf $\mathcal{H}_W$ (unter RH konstruiert) ein selbstadjungierter $A_X$ mit $\sigma(A_X)\subset[0,\infty)$? Das wäre Objekt X in seiner stärksten Form.

---

## 6. Offene Anschlussfragen

$$
\text{Normierungsabgleich }W_{\rm NEU-252}=W_{\rm Weil-Lit}\quad?[O]\to\text{NEU-220k} \qquad (6\text{-a})
$$
$$
\mathcal{H}_W\cong\ell^2(\gamma)\text{ rigoros (Vollständigkeit, Dichte)}\quad?[O] \qquad (6\text{-b})
$$
$$
\text{Konstruktion }A_X\text{ auf }\mathcal{H}_W\quad?[O]\to\text{NEU-258} \qquad (6\text{-c})
$$
$$
\text{Ob }\neg\text{RH}:\;\mathcal{H}_W\text{ indefinit/Krein?}\quad?[O]\to\text{NEU-220s/t} \qquad (6\text{-d})
$$

---

## 7. Statusbuchungen

$$L^2\text{-Semibeschränktheit }B_W\Leftrightarrow\text{RH (vorbehaltlich Normabgleich)}\quad\checkmark[K/M]\qquad(7\text{-a})$$
$$\text{Bochner-Schwartz: Semibeschränktheit}\Rightarrow W\in\mathcal{S}'\Rightarrow\text{RH}\quad\checkmark[K/M]\qquad(7\text{-b})$$
$$B_W\text{ nicht abschließbar auf }H_0=L^2\text{ (unter RH, explizite Folge }a_n)\quad\checkmark[K/M]\qquad(7\text{-c})$$
$$\text{Semibeschränktheit + Abschließbarkeit auf }L^2\text{ unvereinbar}\quad\checkmark[K/M]\qquad(7\text{-d})$$
$$\text{Kato/KLMN auf }H_0=L^2\quad\times[M]\qquad(7\text{-e})$$
$$\text{KLMN-Kandidat NEU-256 (Leit-Rel) unter RH}\quad\times[M]\qquad(7\text{-f})$$
$$H_0=L^2\text{: Referenzraum ja, Abschlussraum von }B_W\text{ nein}\quad\checkmark[K/M]\qquad(7\text{-g})$$
$$\mathcal{H}_W\cong\ell^2(\gamma,m_\gamma)\text{ als natürlicher Abschluss unter RH}\quad\checkmark[K/M]\text{ (formal)}\qquad(7\text{-h})$$
$$\text{Normierungsabgleich NEU-220k}\quad?[O]\qquad(7\text{-i})$$
$$A_X\text{ auf }\mathcal{H}_W\quad?[O]\to\text{NEU-258}\qquad(7\text{-j})$$

---

## 8. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-256 (Patch) | 8d67c54 | $R_{\rm arith}$; KLMN-Kandidat; $B_{\rm fin}$ M3-Formel |
| NEU-255 (Patch 2) | bcc932d | $H_0=L^2$; Koisometrie; Modulationstest |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention; Normierung |
| NEU-220s/t | div. | Kreinraum; $\neg$RH-Realisierung |
| Weil 1952 | — | Positivitätskriterium; Spektraldarstellung |
| Suzuki 2011/2026 | — | Weil-Form endliche Intervalle; Screw-Function |
| Bochner-Schwartz | Reed-Simon II, IX.10 | Positiv-definite Distribution $\Rightarrow$ temperiert |
| Fukushima et al. | FOT §1.3.5 | Abschließbarkeit translationsinvarianter Formen |
| Reed-Simon X | Thm.~X.23 | Abschließbarkeitskriterium |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
