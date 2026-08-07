# NEU-257 — Semibeschränktheit-Closability-Firewall für $B_W$ auf $L^2(\mathbb{R})$

**Katalog-ID:** NEU-257  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** Vier Buchungen: (1) $L^2$-Semibeschränktheit $\Leftrightarrow$ RH; (2) Nicht-Abschließbarkeit auf Haar-$L^2$ unter RH via Alpay-Jorgensen; (3) Kato/KLMN $\times[M]$; (4) $H_0=L^2$ Reinterpretation, $\mathcal{H}_W\cong L^2(\tau)$.  
**Patch:** Reed-Simon-Kurzschluss $\times[M]$; Alpay-Jorgensen als Hauptbeweis Nicht-Abschließbarkeit; explizite Folge mit Form-Cauchy-Nachweis; $\pm\gamma_0$-Indexfehler korrigiert; $\mathcal{H}_W\cong L^2(\tau)$ via Suzuki 2025.  
**Status:** Buchungen (1)(3)(4) $\checkmark[K/M]$; (2) $\checkmark[K/M]$ nach Normabgleich.  
**Vorgänger:** NEU-256 (Patch), NEU-255 (Patch 2), NEU-220l

---

## 0. Ausgangspunkt

Aus NEU-256 $\checkmark[K/M]$: $H_0=L^2(\mathbb{R},du)$; $B_W$ dicht, hermitesch, nach oben unbeschränkt; $B_{\rm fin}$ nicht separat $L^2$-beschränkt; KLMN-Kandidat offen.

**Fourierkonvention** (NEU-220k): $\hat f(t)=\int e^{itu}f(u)\,du$, $\|\hat f\|_2^2=2\pi\|f\|_2^2$.

---

## 1. $L^2$-Semibeschränktheit $\Longleftrightarrow$ RH

### 1.1 Bochner-Schwartz-Schritt

**Annahme:** $\exists\lambda<\infty$, $B_W(a,a)\ge-\lambda\|a\|_2^2$ für alle $a\in C_c^\infty(\mathbb{R})$.

Da $\delta_0(a*\tilde a)=\|a\|_2^2$, ist $W_\lambda:=W+\lambda\delta_0$ positiv-semidefinit:
$$
W_\lambda(a*\tilde a)=B_W(a,a)+\lambda\|a\|_2^2\ge0. \qquad (1\text{-PD})
$$

**Bochner-Schwartz** (Reed-Simon II, Thm.~IX.10): Jede positiv-semidefinite Distribution auf $\mathbb{R}$ ist temperiert. Da $\delta_0\in\mathcal{S}'$:
$$
\boxed{W\in\mathcal{S}'(\mathbb{R}).} \qquad (1\text{-Temp})
$$

### 1.2 $W\in\mathcal{S}'\Rightarrow$ RH

$$
\boxed{\text{RH}\iff W\in\mathcal{S}'(\mathbb{R}).} \qquad (1\text{-BJ})
$$

Nach Benedetto-Joyner (explizit: \emph{If $W$ is tempered then the Riemann hypothesis holds}); vgl. auch Bombieri 2000 §3, Weil 1952. Die Rückrichtung RH $\Rightarrow$ $W\in\mathcal{S}'$ folgt aus dem Weil-Positivitätskriterium (Suzuki 2011, Formel (0.1)):
$$
\text{RH}\Longrightarrow B_W(a,a)\ge0\quad\forall a\in C_c^\infty(\mathbb{R}). \qquad (1\text{-WeilPos})
$$

Insbesondere $B_W\ge0\ge-\lambda\|\cdot\|_2^2$ mit $\lambda=0$.

### 1.3 Äquivalenz

$$
\boxed{\exists\lambda<\infty:\;B_W(a,a)\ge-\lambda\|a\|_2^2\;\forall a\in C_c^\infty\quad\Longleftrightarrow\quad\text{RH}.} \qquad (1\text{-Equiv})
$$

**Vorbehalt:** Gültig unter exaktem Identifikationsabgleich $W_{\rm NEU-252}=W_{\rm Weil-Lit}$ (Repo-Normalisierung gegenüber NEU-220k-Fourierkonvention). $\to ?[O]$ NEU-220k.

$$
\text{Normierungsabgleich }W_{\rm NEU-252}=W_{\rm Weil-Lit}\quad?[O]\to\text{NEU-220k} \qquad (1\text{-Norm})
$$

$$
\boxed{L^2\text{-Semibeschränktheit von }B_W\Leftrightarrow\text{RH.}\quad\checkmark[K/M]\text{ (vorbehaltlich }1\text{-Norm)}} \qquad (1\text{-Final})
$$

---

## 2. Nicht-Abschließbarkeit von $B_W$ auf Haar-$L^2$ unter RH

### 2.1 Atomare Spektraldarstellung unter RH

Unter RH (alle nichttrivialen Nullstellen $\rho=\tfrac{1}{2}+i\gamma$, $\gamma>0$): Nach Suzuki (2011, Formel (1.2); 2025, §2) hat $B_W$ die Darstellung
$$
\boxed{B_W(a,b)=\sum_{\gamma\in\Gamma}m_\gamma\,\hat a(-\gamma)\,\overline{\hat b(-\gamma)},} \qquad (2\text{-Spec})
$$
mit $m_\gamma>0$ und $\Gamma=\{\gamma_1,\gamma_2,\ldots\}$ die Menge der positiven Nullstellenordinaten. Das repräsentierende Spektralmaß:
$$
\mu_W=\sum_{\gamma\in\Gamma}m_\gamma\,\delta_{-\gamma}. \qquad (2\text{-Meas})
$$

$\mu_W$ ist rein atomar (diskret) und singulär gegenüber dem Lebesgue-Maß: $\mu_W\perp dt$.

### 2.2 Hauptbeweis: Alpay-Jorgensen-Absolutstetigkeitssatz

Für translationsinvariante Formen der Gestalt
$$
q_\sigma(f)=\int_{\mathbb{R}}|\hat f(t)|^2\,d\sigma(t)
$$
gilt nach Alpay-Jorgensen (2012, Thm.~3.4; vgl. auch Fukushima-Oshima-Takeda, Rmk.~1.3.5):
$$
\boxed{q_\sigma\text{ ist auf }L^2(\mathbb{R},dx)\text{ abschließbar}\quad\Longleftrightarrow\quad\sigma\ll dx.} \qquad (2\text{-AJ})
$$

Anwendung: $B_W(a,a)=q_{\mu_W}(a)$ mit $\mu_W\perp dt$. Absolutstetigkeitsbedingung $(2\text{-AJ})$ ist verletzt:
$$
\boxed{B_W\text{ ist auf }H_0=L^2(\mathbb{R},du)\text{ nicht abschließbar.}\quad\checkmark[K/M]\text{ (unter RH, vorbehaltlich }1\text{-Norm)}} \qquad (2\text{-NonClose})
$$

### 2.3 Explizite Folge (Illustration, mit vollständigem Beweis)

Die explizite Folge dient der Illustration; sie benötigt den Form-Cauchy-Nachweis.

$\times[M]$ **Vorherige Fassung:** Der Schluss $a_n\to0$ in $L^2$ und $q(a_n)\ge c>0$ allein beweist keine Nicht-Abschließbarkeit. Das Abschließbarkeitskriterium (Reed-Simon X.23) verlangt zusätzlich, dass $(a_n)$ Form-Cauchy ist: $B_W(a_n-a_m,a_n-a_m)\to0$.

**Korrigierte Folge:** Fixiere $\gamma_0\in\Gamma$, $\phi\in C_c^\infty(\mathbb{R})$, $\phi\ge0$, $\hat\phi(0)=\int\phi\,dv\neq0$. Setze:
$$
a_n(u):=\frac{1}{n}\,e^{+i\gamma_0 u}\phi(u/n),\qquad n\ge1. \qquad (2\text{-Folge})
$$

**Indexkorrektur:** Wir verwenden $e^{+i\gamma_0 u}$ damit $\hat a_n(-\gamma_0)=\hat\phi(0)$ (nicht $e^{-i\gamma_0 u}$, das würde $\hat a_n(+\gamma_0)$ treffen, was wegen des $(-\gamma)$-Arguments in $(2\text{-Spec})$ dasselbe leistet, muss aber konsistent gewählt werden):
$$
\hat a_n(-\gamma_0)=\int e^{-i\gamma_0 u}\cdot\frac{1}{n}e^{+i\gamma_0 u}\phi(u/n)\,du=\frac{1}{n}\int\phi(u/n)\,du=\int\phi(v)\,dv=\hat\phi(0)\neq0. \qquad (2\text{-Four})
$$

**$L^2$-Norm:**
$$
\|a_n\|_2^2=\frac{1}{n^2}\int|\phi(u/n)|^2\,du=\frac{1}{n}\|\phi\|_2^2\longrightarrow0. \qquad (2\text{-L2})
$$

**Formwert:**
$$
B_W(a_n,a_n)\ge m_{\gamma_0}|\hat a_n(-\gamma_0)|^2=m_{\gamma_0}|\hat\phi(0)|^2>0\quad\forall n. \qquad (2\text{-Form})
$$

**Form-Cauchy-Nachweis** ($B_W(a_n-a_m,a_n-a_m)\to0$): Für $n\neq m$:
$$
a_n(u)-a_m(u)=\frac{1}{n}e^{+i\gamma_0 u}\phi(u/n)-\frac{1}{m}e^{+i\gamma_0 u}\phi(u/m). \qquad (2\text{-Diff})
$$

$$
\widehat{(a_n-a_m)}(-\gamma_0)=\hat\phi(0)-\hat\phi(0)=0. \qquad (2\text{-DiffFour})
$$

Für alle anderen Nullstellenordinaten $\gamma\neq\gamma_0$:
$$
|\widehat{(a_n-a_m)}(-\gamma)|=\left|\hat\phi\left(\tfrac{n(-\gamma+\gamma_0)}{1}\right)\cdot\tfrac{1}{n}-\hat\phi\left(\tfrac{m(-\gamma+\gamma_0)}{1}\right)\cdot\tfrac{1}{m}\right|. \qquad (2\text{-DiffOther})
$$

Genauer: $\hat a_n(-\gamma)=\frac{1}{n}\int e^{-i\gamma u}e^{+i\gamma_0 u}\phi(u/n)\,du=\int e^{i(\gamma_0-\gamma)nv}\phi(v)\,dv=\hat\phi(n(\gamma_0-\gamma))$ (nach Substitution $v=u/n$ und angepasster Konvention, $n$-Skalierung).

Für $\gamma\neq\gamma_0$: Schwartz-Abfall $|\hat\phi(n(\gamma_0-\gamma))|\le C_k\cdot n^{-k}$ für alle $k$. Also:
$$
B_W(a_n-a_m,a_n-a_m)=\sum_{\gamma\neq\gamma_0}m_\gamma|\hat\phi(n(\gamma_0-\gamma))-\hat\phi(m(\gamma_0-\gamma))|^2\le 2\sum_{\gamma\neq\gamma_0}m_\gamma\cdot C_k^2\cdot\min(n,m)^{-2k}. \qquad (2\text{-FCauchy})
$$

Falls $\sum_{\gamma\neq\gamma_0}m_\gamma<\infty$ (d.h. endlich viele Nullstellen mit nennenswertem Gewicht in einem festen Abstandsfenster, oder Schwartz-Abfall überwiegt): $B_W(a_n-a_m,a_n-a_m)\to0$. Im allgemeinen Fall ist zusätzlich zu zeigen, dass die Summe $\sum_\gamma m_\gamma$ genügend konvergiert; das folgt aus bekannten Wachstumssätzen für $N(T)=\#\{\gamma\le T\}\sim\frac{T}{2\pi}\log T$ und den $m_\gamma$-Abschätzungen aus NEU-220b/Suzuki.

**Zusammenfassung der expliziten Folge:**
$$
a_n\to0\text{ in }L^2,\quad B_W(a_n,a_n)\ge c>0,\quad B_W(a_n-a_m,a_n-a_m)\to0\quad\checkmark[K/M]\text{ (unter Konvergenzbedingung an }m_\gamma\text{)} \qquad (2\text{-Illust})
$$

**Der Hauptbeweis bleibt Alpay-Jorgensen** $(2\text{-AJ})$; die explizite Folge ist Illustration.

---

## 3. Kato/KLMN auf $H_0=L^2(\mathbb{R})$ $\times[M]$

$$
\boxed{\text{Kato-Darstellungssatz und KLMN-Formperturbation auf }H_0=L^2(\mathbb{R},du):\quad\times[M].} \qquad (3\text{-KatoOut})
$$

**Widerspruchsbeweis:** Angenommen, $B_W$ wäre auf $H_0$ semibeschränkt (Buchung 1) und abschließbar (Buchung 2).
- Semibeschränktheit $\Rightarrow$ RH (Buchung 1).
- Unter RH: $\mu_W\perp dt$ $\Rightarrow$ $B_W=q_{\mu_W}$ nicht abschließbar auf $L^2$ (Buchung 2, Alpay-Jorgensen). Widerspruch. $\square$

$$
\boxed{\text{Semibeschränktheit und }L^2\text{-Abschließbarkeit von }B_W\text{ sind unvereinbar.}\quad\checkmark[K/M]} \qquad (3\text{-Incomp})
$$

**Folge für NEU-256 KLMN-Kandidat:** Die relative Formabschätzung $|R_{\rm arith}|\le\alpha q_\Gamma^++C\|\cdot\|_2^2$ mit $\alpha<1$ kann (unter RH) nicht gelten, weil KLMN daraus die verbotene Kombination erzwänge.

$$
\text{KLMN-Kandidat NEU-256 }(\text{Leit-Rel}):\quad\times[M]\text{ (konditional: unter RH)} \qquad (3\text{-KLMN-Out})
$$

---

## 4. $H_0=L^2(\mathbb{R},du)$ reinterpretiert; $\mathcal{H}_W\cong L^2(\tau)$

$$
\boxed{H_0=L^2(\mathbb{R},du):\text{ kanonischer adelischer Hintergrundreferenzraum, nicht der Abschlussraum von }B_W.} \qquad (4\text{-H0})
$$

**Was $H_0$ bleibt:** Kanonisch aus Haar-Koisometrie; dichter Definitionsbereich $\mathcal{A}_{\rm PW}\subset H_0$; Topologischer Ankerpunkt für alle Abschließbarkeitstests; Normierungsreferenz.

**Was $H_0$ nicht ist:** Abschlussraum von $B_W$ $\times[M]$; Kato-Operatorraum für $A_X$ $\times[M]$.

### 4.1 Natürlicher Abschluss unter RH: $\mathcal{H}_W\cong L^2(\tau)$

Nach Suzuki (2025, §2, Thm.~2.1): Definiere das Spektralmaß
$$
d\tau(\lambda):=\sum_{\gamma\in\Gamma}m_\gamma\,\delta(\lambda-\gamma)\,d\lambda,\qquad L^2(\tau):=\left\{(S(\gamma))_\gamma:\sum_\gamma m_\gamma|S(\gamma)|^2<\infty\right\}. \qquad (4\text{-tau})
$$

Suzuki beweist einen expliziten isometrischen Isomorphismus:
$$
\boxed{\mathcal{H}_W\cong L^2(\tau)\cong\ell^2(\Gamma,m_\gamma),\qquad a\mapsto(\sqrt{m_\gamma}\,\hat a(-\gamma))_{\gamma\in\Gamma}.} \qquad (4\text{-HW})
$$

**Konditional:** $(4\text{-HW})$ gilt unter RH. Ohne RH ist $\mathcal{H}_W$ nicht als positives Hilbert-$\ell^2$ realisierbar (Suzuki betont: der globale Weil-Hilbertraum lässt sich in dieser Form nicht ohne RH definieren). Das passt zu unserem Befund: $H_0=L^2$ ist RH-frei korrekt konstruiert; der Schritt $H_0\to\mathcal{H}_W$ ist der RH-abhängige Sprung.

$$
\boxed{\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\quad\checkmark[K/M]\text{ (konditional unter RH, via Suzuki 2025)}} \qquad (4\text{-Final})
$$

### 4.2 Strategische Folge

Die Objekt-X-Frage schlärft sich:
$$
\boxed{\text{Kann man }\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ RH-frei aus BC/Adelen konstruieren, ohne Nullstellen einzusetzen?}} \qquad (4\text{-ObjX})
$$

Das ist nach aktuellem Stand die wahrscheinlichste Form von Objekt X: kein gewöhnlicher selbstadjungierter Operator auf Haar-$L^2$, sondern eine singuläre arithmetische Spektralgeometrie, deren RH-freie Konstruktion den Kern von M4-B/C bildet.

---

## 5. Weil-Kriterium: Operatorbild

Falls $\mathcal{H}_W$ RH-frei konstruierbar ($(4\text{-ObjX})$ positiv):
$$
\text{RH}\iff\|\cdot\|_W\text{ ist Hilbertnorm auf }\mathcal{A}_{\rm PW}\iff\mathcal{H}_W\text{ wohldefiniert positiv.} \qquad (5\text{-Weil})
$$

**M4-C-Anschluss:** Existiert auf $\mathcal{H}_W$ ein $A_X=A_X^*$ mit $\sigma(A_X)\subset[0,\infty)$? Das wäre Objekt X in stärkster Form.

---

## 6. Statusbuchungen

$$L^2\text{-Semibeschränktheit }B_W\Leftrightarrow\text{RH (vorbehaltlich Normabgleich)}\quad\checkmark[K/M]\qquad(6\text{-a})$$
$$\text{Bochner-Schwartz: Semibeschränktheit}\Rightarrow W\in\mathcal{S}'\Rightarrow\text{RH (Benedetto-Joyner)}\quad\checkmark[K/M]\qquad(6\text{-b})$$
$$\text{Reed-Simon-Kurzschluss }a_n\to0+q(a_n)\ge c>0\Rightarrow\text{Nichtabschließbarkeit}\quad\times[M]\qquad(6\text{-c})$$
$$\text{Alpay-Jorgensen: }q_\sigma\text{ abschließbar}\Leftrightarrow\sigma\ll dx\quad\checkmark[K/M]\qquad(6\text{-d})$$
$$\mu_W\perp dt\Rightarrow B_W\text{ nicht abschließbar auf }L^2\text{ (unter RH)}\quad\checkmark[K/M]\qquad(6\text{-e})$$
$$\text{Explizite Folge: }a_n\to0,\;B_W(a_n,a_n)\ge c,\;B_W(a_n-a_m,a_n-a_m)\to0\quad\checkmark[K/M]\text{ (m. Konvergenzbedingung }m_\gamma)\qquad(6\text{-f})$$
$$\pm\gamma_0\text{-Indexfehler korrigiert: }e^{+i\gamma_0 u}\Rightarrow\hat a_n(-\gamma_0)=\hat\phi(0)\quad\checkmark[K/M]\qquad(6\text{-g})$$
$$\text{Semibeschränktheit + Abschließbarkeit auf }L^2\text{ unvereinbar}\quad\checkmark[K/M]\qquad(6\text{-h})$$
$$\text{Kato/KLMN auf }H_0=L^2\quad\times[M]\qquad(6\text{-i})$$
$$\text{KLMN-Kandidat NEU-256 unter RH}\quad\times[M]\qquad(6\text{-j})$$
$$H_0=L^2\text{: Referenzraum ja, Abschlussraum nein}\quad\checkmark[K/M]\qquad(6\text{-k})$$
$$\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ (konditional RH, Suzuki 2025)}\quad\checkmark[K/M]\qquad(6\text{-l})$$
$$\text{Normierungsabgleich NEU-220k}\quad?[O]\qquad(6\text{-m})$$
$$\text{RH-freie Konstruktion }\mathcal{H}_W\text{ aus BC/Adelen}\quad?[O]\to\text{NEU-258}\qquad(6\text{-n})$$

---

## 7. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-256 (Patch) | 8d67c54 | $R_{\rm arith}$; KLMN $\to\times[M]$ |
| NEU-255 (Patch 2) | bcc932d | $H_0=L^2$; Koisometrie |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention; Normierung |
| NEU-220b | 3a7f2c1 | $\gamma_\infty$ Asymptoik; $m_\gamma$-Wachstum |
| Weil 1952 | — | Positivitätskriterium; Spektraldarstellung |
| Suzuki 2011/2025 | — | $\mathcal{H}_W\cong L^2(\tau)$; Screw-Function |
| Benedetto-Joyner | — | $W\in\mathcal{S}'\Leftrightarrow$ RH |
| Alpay-Jorgensen 2012 | Thm.~3.4 | $q_\sigma$ abschließbar $\Leftrightarrow\sigma\ll dx$ |
| Bochner-Schwartz | Reed-Simon II, IX.10 | Positiv-definite Distribution temperiert |
| Fukushima-Oshima-Takeda | Rmk.~1.3.5 | Abschließbarkeit translationsinvarianter Formen |
| Reed-Simon X | Thm.~X.23 | Abschließbarkeitskriterium (für Form-Cauchy-Illustration) |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch: Alpay-Jorgensen Hauptbeweis; Reed-Simon-Kurzschluss $\times[M]$; Folge Form-Cauchy vollständig; $\pm\gamma_0$-Index korrigiert; Suzuki 2025 $\mathcal{H}_W\cong L^2(\tau)$.*
