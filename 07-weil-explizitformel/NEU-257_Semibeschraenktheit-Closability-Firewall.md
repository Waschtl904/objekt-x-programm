# NEU-257 — Semibeschränktheit-Closability-Firewall für $B_W$ auf $L^2(\mathbb{R})$

**Katalog-ID:** NEU-257  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07; Patch 2: 2026-08-08)  
**Auftrag:** Vier Buchungen: (1) $L^2$-Semibeschränktheit $\Leftrightarrow$ RH; (2) Nicht-Abschließbarkeit auf Haar-$L^2$ unter RH via Alpay-Jorgensen; (3) Kato/KLMN $\times[M]$; (4) $H_0=L^2$ Reinterpretation, $\mathcal{H}_W\cong L^2(\tau)$.  
**Patch:** Reed-Simon-Kurzschluss $\times[M]$; Alpay-Jorgensen als Hauptbeweis Nicht-Abschließbarkeit; explizite Folge mit Form-Cauchy-Nachweis; $\pm\gamma_0$-Indexfehler korrigiert; $\mathcal{H}_W\cong L^2(\tau)$ via Suzuki 2025.  
**Patch 2:** §2.3 vollständig geschlossen. Fehler in $(2\text{-DiffOther})$ ($1/n$-Vorfaktor) und $(2\text{-FCauchy})$ (fehlende $|\gamma-\gamma_0|$-Abhängigkeit) behoben. Neue Majorante mit Schwartz-Abfall und Summierbarkeit via Riemann–von Mangoldt. Annahme $m_\gamma=O(1)$ wird nicht benötigt und nicht verwendet.  
**Status:** Alle Buchungen $\checkmark[K/M]$; Normierungsvorbehalt $(1\text{-Norm})$ durch NEU-258 Patch 1 geschlossen.  
**Vorgänger:** NEU-256 (Patch), NEU-255 (Patch 2), NEU-220l, NEU-258 (Patch 1)

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

**Bochner-Schwartz** (Reed-Simon II, Thm. IX.10): Jede positiv-semidefinite Distribution auf $\mathbb{R}$ ist temperiert. Da $\delta_0\in\mathcal{S}'$:
$$
\boxed{W\in\mathcal{S}'(\mathbb{R}).} \qquad (1\text{-Temp})
$$

### 1.2 $W\in\mathcal{S}'\Rightarrow$ RH

$$
\boxed{\text{RH}\iff W\in\mathcal{S}'(\mathbb{R}).} \qquad (1\text{-BJ})
$$

Nach Benedetto-Joyner (\emph{If $W$ is tempered then the Riemann hypothesis holds}); vgl. auch Bombieri 2000 §3, Weil 1952. Die Rückrichtung RH $\Rightarrow$ $W\in\mathcal{S}'$ folgt aus dem Weil-Positivitätskriterium (Suzuki 2011, Formel (0.1)):
$$
\text{RH}\Longrightarrow B_W(a,a)\ge0\quad\forall a\in C_c^\infty(\mathbb{R}). \qquad (1\text{-WeilPos})
$$

Insbesondere $B_W\ge0\ge-\lambda\|\cdot\|_2^2$ mit $\lambda=0$.

### 1.3 Äquivalenz

$$
\boxed{\exists\lambda<\infty:\;B_W(a,a)\ge-\lambda\|a\|_2^2\;\forall a\in C_c^\infty\quad\Longleftrightarrow\quad\text{RH}.} \qquad (1\text{-Equiv})
$$

Der Normierungsabgleich $W_{\rm NEU-252}=W_{\rm Weil-Lit}$ ist durch NEU-258 Patch 1 $(6\text{-ID})$ geschlossen.

$$
\boxed{L^2\text{-Semibeschränktheit von }B_W\Leftrightarrow\text{RH.}\quad\checkmark[K/M]} \qquad (1\text{-Final})
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
gilt nach Alpay-Jorgensen (2012, Thm. 3.4; vgl. auch Fukushima-Oshima-Takeda, Rmk. 1.3.5):
$$
\boxed{q_\sigma\text{ ist auf }L^2(\mathbb{R},dx)\text{ abschließbar}\quad\Longleftrightarrow\quad\sigma\ll dx.} \qquad (2\text{-AJ})
$$

Anwendung: $B_W(a,a)=q_{\mu_W}(a)$ mit $\mu_W\perp dt$. Absolutstetigkeitsbedingung $(2\text{-AJ})$ ist verletzt:
$$
\boxed{B_W\text{ ist auf }H_0=L^2(\mathbb{R},du)\text{ nicht abschließbar.}\quad\checkmark[K/M]\text{ (unter RH)}} \qquad (2\text{-NonClose})
$$

### 2.3 Explizite Folge (vollständiger Beweis)

Die explizite Folge ergänzt Alpay-Jorgensen mit einem direkten Konstruktionsbeweis. **Keine** Annahme über Multiplizitäten ($m_\gamma=O(1)$ ist unbekannt und wird nicht benötigt).

**Setup.** Sei $\Phi:=\widehat\varphi$ mit $\varphi\in C_c^\infty(\mathbb{R})$, $\varphi\ge0$, $\Phi(0)=\int\varphi\,dv\neq0$. Fixiere $\gamma_0\in\Gamma$ und setze:
$$
a_n(u):=\frac{1}{n}\,e^{+i\gamma_0 u}\varphi(u/n),\qquad n\ge1. \qquad (2\text{-Folge})
$$

**Fouriertransformation.** Für alle $\gamma\in\mathbb{R}$:
$$
\hat a_n(-\gamma) = \int_{\mathbb{R}} e^{-i\gamma u}\cdot\frac{1}{n}e^{+i\gamma_0 u}\varphi(u/n)\,du = \int_{\mathbb{R}} e^{i(\gamma_0-\gamma)nv}\varphi(v)\,dv = \Phi(n(\gamma_0-\gamma)). \qquad (2\text{-Four})
$$
(Substitution $v=u/n$, $du=n\,dv$, Faktor $1/n$ kürzt sich.)

**$L^2$-Norm:**
$$
\|a_n\|_2^2=\frac{1}{n^2}\int|\varphi(u/n)|^2\,du=\frac{1}{n}\|\varphi\|_2^2\longrightarrow0. \qquad (2\text{-L2})
$$

**Atomwert am ausgewählten Atom.** Für $\gamma=\gamma_0$:
$$
\hat a_n(-\gamma_0) = \Phi(0)\neq0\quad\forall n. \qquad (2\text{-Atom})
$$

**Formwert.** Unter RH und mit der Spektraldarstellung $(2\text{-Spec})$:
$$
B_W(a_n,a_n) = \sum_{\gamma\in\Gamma} m_\gamma|\hat a_n(-\gamma)|^2 = m_{\gamma_0}|\Phi(0)|^2 + \sum_{\gamma\neq\gamma_0}m_\gamma|\Phi(n(\gamma_0-\gamma))|^2. \qquad (2\text{-Form})
$$

Der zweite Term verschwindet für $n\to\infty$ (Summierbarkeitsargument, siehe Form-Cauchy unten), also:
$$
B_W(a_n,a_n)\longrightarrow m_{\gamma_0}|\Phi(0)|^2>0. \qquad (2\text{-FormLimit})
$$

**Form-Cauchy-Nachweis** ($B_W(a_n-a_m,a_n-a_m)\to0$).

Für $\gamma=\gamma_0$:
$$
(\hat a_n-\hat a_m)(-\gamma_0) = \Phi(0)-\Phi(0) = 0. \qquad (2\text{-DiffAtom})
$$
Der problematische Atomterm verschwindet exakt.

Für $\gamma\neq\gamma_0$ und $M:=\min(n,m)$: Da $\varphi\in C_c^\infty(\mathbb{R})$ ist $\Phi=\hat\varphi\in\mathcal{S}(\mathbb{R})$. Für jedes $N\ge1$ gilt die Schwartz-Abschätzung
$$
|\Phi(x)|\le C_N(1+|x|)^{-N}. \qquad (2\text{-Schwartz})
$$

Daher:
$$
|\hat a_n(-\gamma)-\hat a_m(-\gamma)| \le |\Phi(n(\gamma_0-\gamma))|+|\Phi(m(\gamma_0-\gamma))| \le 2C_N\bigl(1+M|\gamma-\gamma_0|\bigr)^{-N}. \qquad (2\text{-DiffBound})
$$

Somit:
$$
\boxed{B_W(a_n-a_m,a_n-a_m)\le 4C_N^2\sum_{\gamma\neq\gamma_0}m_\gamma\bigl(1+M|\gamma-\gamma_0|\bigr)^{-2N}.} \qquad (2\text{-FCMaj})
$$

**Summierbarkeit von $S_N$.** Da die Nullstellen von $\xi$ isoliert sind, gilt für das feste $\gamma_0$:
$$
\delta_{\gamma_0}:=\inf_{\gamma\neq\gamma_0}|\gamma-\gamma_0|>0. \qquad (2\text{-Sep})
$$

Auf der Menge $|\gamma-\gamma_0|\ge\delta_{\gamma_0}$ ist $(1+M|\gamma-\gamma_0|)^{-2N}\le M^{-2N}|\gamma-\gamma_0|^{-2N}$, also genügt die Konvergenz von
$$
S_N := \sum_{\gamma\neq\gamma_0}m_\gamma|\gamma-\gamma_0|^{-2N}. \qquad (2\text{-SN})
$$

Für große $|\gamma|$ gilt $|\gamma-\gamma_0|\asymp|\gamma|$, also genügt die Konvergenz von $\sum_{\gamma}m_\gamma(1+|\gamma|)^{-2N}$.

Nach **Riemann–von Mangoldt** zählt $N(T):=\#\{\gamma\in\Gamma:\gamma\le T\}$ (mit Multiplizitäten) die Nullstellen mit
$$
N(T) = O(T\log T). \qquad (2\text{-RvM})
$$

Mittels partieller Summation (Stieltjes-Integration) für $s=2N>1$:
$$
\sum_{\gamma}m_\gamma(1+|\gamma|)^{-s} = s\int_1^\infty N(t)\,(1+t)^{-s-1}\,dt \ll \int_1^\infty t\log t\cdot t^{-s-1}\,dt = \int_1^\infty t^{-s}\log t\,dt < \infty. \qquad (2\text{-Abel})
$$

Das Integral konvergiert für $s>1$, also bereits für $N\ge1$. Somit $S_N<\infty$ für alle $N\ge1$, und:
$$
B_W(a_n-a_m,a_n-a_m) \le 4C_N^2 S_N\cdot M^{-2N} = O\!\left(\min(n,m)^{-2N}\right) \longrightarrow 0. \qquad (2\text{-FCauchy})
$$

**Zusammenfassung der expliziten Folge.**

$$
\boxed{a_n\to0\text{ in }L^2,\quad B_W(a_n-a_m,a_n-a_m)\to0,\quad B_W(a_n,a_n)\longrightarrow m_{\gamma_0}|\Phi(0)|^2>0.\quad\checkmark[K/M]\text{ (unter RH)}} \qquad (2\text{-Illust})
$$

Das ist das klassische Abschließbarkeitswiderlegungsschema: $(a_n)$ ist $B_W$-Cauchy mit $a_n\to0$ in $L^2$, aber $B_W(a_n,a_n)\not\to0$. Also ist $B_W$ nicht abschließbar auf $L^2(\mathbb{R})$.

**Der Hauptbeweis bleibt Alpay-Jorgensen** $(2\text{-AJ})$; die explizite Folge ist vollständiger eigenständiger Direktbeweis.

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

Nach Suzuki (2025, §2, Thm. 2.1): Definiere das Spektralmaß
$$
d\tau(\lambda):=\sum_{\gamma\in\Gamma}m_\gamma\,\delta(\lambda-\gamma)\,d\lambda,\qquad L^2(\tau):=\left\{(S(\gamma))_\gamma:\sum_\gamma m_\gamma|S(\gamma)|^2<\infty\right\}. \qquad (4\text{-tau})
$$

Suzuki beweist einen expliziten isometrischen Isomorphismus:
$$
\boxed{\mathcal{H}_W\cong L^2(\tau)\cong\ell^2(\Gamma,m_\gamma),\qquad a\mapsto(\sqrt{m_\gamma}\,\hat a(-\gamma))_{\gamma\in\Gamma}.} \qquad (4\text{-HW})
$$

**Konditional:** $(4\text{-HW})$ gilt unter RH. Das passt zu unserem Befund: $H_0=L^2$ ist RH-frei korrekt konstruiert; der Schritt $H_0\to\mathcal{H}_W$ ist der RH-abhängige Sprung.

$$
\boxed{\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\quad\checkmark[K/M]\text{ (konditional unter RH, via Suzuki 2025)}} \qquad (4\text{-Final})
$$

### 4.2 Strategische Folge

$$
\boxed{\text{Kann man }\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ RH-frei aus BC/Adelen konstruieren, ohne Nullstellen einzusetzen?}} \qquad (4\text{-ObjX})
$$

---

## 5. Weil-Kriterium: Operatorbild

Falls $\mathcal{H}_W$ RH-frei konstruierbar ($(4\text{-ObjX})$ positiv):
$$
\text{RH}\iff\|\cdot\|_W\text{ ist Hilbertnorm auf }\mathcal{A}_{\rm PW}\iff\mathcal{H}_W\text{ wohldefiniert positiv.} \qquad (5\text{-Weil})
$$

**M4-C-Anschluss:** Existiert auf $\mathcal{H}_W$ ein $A_X=A_X^*$ mit $\sigma(A_X)\subset[0,\infty)$? Das wäre Objekt X in stärkster Form.

---

## 6. Statusbuchungen

$$L^2\text{-Semibeschränktheit }B_W\Leftrightarrow\text{RH}\quad\checkmark[K/M]\qquad(6\text{-a})$$
$$\text{Bochner-Schwartz: Semibeschränktheit}\Rightarrow W\in\mathcal{S}'\Rightarrow\text{RH (Benedetto-Joyner)}\quad\checkmark[K/M]\qquad(6\text{-b})$$
$$\text{Reed-Simon-Kurzschluss }a_n\to0+q(a_n)\ge c>0\Rightarrow\text{Nichtabschließbarkeit}\quad\times[M]\qquad(6\text{-c})$$
$$\text{Alpay-Jorgensen: }q_\sigma\text{ abschließbar}\Leftrightarrow\sigma\ll dx\quad\checkmark[K/M]\qquad(6\text{-d})$$
$$\mu_W\perp dt\Rightarrow B_W\text{ nicht abschließbar auf }L^2\text{ (unter RH)}\quad\checkmark[K/M]\qquad(6\text{-e})$$
$$\text{Explizite Folge: vollständiger Direktbeweis (Schwartz-Majorante + Riemann-von-Mangoldt)}\quad\checkmark[K/M]\text{ (unter RH)}\qquad(6\text{-f})$$
$$\pm\gamma_0\text{-Indexfehler korrigiert: }e^{+i\gamma_0 u}\Rightarrow\hat a_n(-\gamma_0)=\Phi(0)\quad\checkmark[K/M]\qquad(6\text{-g})$$
$$\text{Semibeschränktheit + Abschließbarkeit auf }L^2\text{ unvereinbar}\quad\checkmark[K/M]\qquad(6\text{-h})$$
$$\text{Kato/KLMN auf }H_0=L^2\quad\times[M]\qquad(6\text{-i})$$
$$\text{KLMN-Kandidat NEU-256 unter RH}\quad\times[M]\qquad(6\text{-j})$$
$$H_0=L^2\text{: Referenzraum ja, Abschlussraum nein}\quad\checkmark[K/M]\qquad(6\text{-k})$$
$$\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ (konditional RH, Suzuki 2025)}\quad\checkmark[K/M]\qquad(6\text{-l})$$
$$\text{Normierungsabgleich NEU-220k: geschlossen durch NEU-258 Patch 1}\quad\checkmark[K/M]\qquad(6\text{-m})$$
$$\text{RH-freie Konstruktion }\mathcal{H}_W\text{ aus BC/Adelen}\quad?[O]\to\text{NEU-259}\qquad(6\text{-n})$$

---

## 7. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-256 (Patch) | 8d67c54 | $R_{\rm arith}$; KLMN $\to\times[M]$ |
| NEU-255 (Patch 2) | bcc932d | $H_0=L^2$; Koisometrie |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention; Normierung |
| NEU-220b | 3a7f2c1 | $\gamma_\infty$ Asymptotik; $m_\gamma$-Wachstum |
| NEU-258 (Patch 1) | 4eeb501 | $W_{\rm NEU-252}=W_{\rm Lit}$ $(6\text{-ID})$; schließt $(1\text{-Norm})$ |
| Weil 1952 | — | Positivitätskriterium; Spektraldarstellung |
| Suzuki 2011/2025 | — | $\mathcal{H}_W\cong L^2(\tau)$; Screw-Function |
| Benedetto-Joyner | — | $W\in\mathcal{S}'\Leftrightarrow$ RH |
| Alpay-Jorgensen 2012 | Thm. 3.4 | $q_\sigma$ abschließbar $\Leftrightarrow\sigma\ll dx$ |
| Bochner-Schwartz | Reed-Simon II, IX.10 | Positiv-definite Distribution temperiert |
| Riemann–von Mangoldt | — | $N(T)=O(T\log T)$; Summierbarkeit $(2\text{-Abel})$ |
| Reed-Simon X | Thm. X.23 | Abschließbarkeitskriterium |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch (2026-08-07): Alpay-Jorgensen Hauptbeweis; Reed-Simon-Kurzschluss $\times[M]$. Patch 2 (2026-08-08): §2.3 vollständig geschlossen; Schwartz-Majorante mit $|\gamma-\gamma_0|$-Abhängigkeit; Summierbarkeit via Riemann–von Mangoldt ohne Multiplizitätsannahme; $(2\text{-DiffOther})$-$1/n$-Fehler und $(2\text{-FCauchy})$-Lücke behoben; $m_\gamma=O(1)$ nicht verwendet.*