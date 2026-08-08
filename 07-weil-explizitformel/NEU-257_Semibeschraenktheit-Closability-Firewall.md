# NEU-257 — Semibeschränktheit-Closability-Firewall für $B_W$ auf $L^2(\mathbb{R})$

**Katalog-ID:** NEU-257  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07; Patch 2: 2026-08-08; Patch 3: 2026-08-08)  
**Auftrag:** Vier Buchungen: (1) $L^2$-Semibeschränktheit $\Leftrightarrow$ RH; (2) Nicht-Abschließbarkeit auf Haar-$L^2$ unter RH via Alpay-Jorgensen; (3) Kato/KLMN $\times[M]$; (4) $H_0=L^2$ Reinterpretation, $\mathcal{H}_W\cong L^2(\tau)$.  
**Patch:** Reed-Simon-Kurzschluss $\times[M]$; Alpay-Jorgensen als Hauptbeweis; explizite Folge mit Form-Cauchy-Nachweis; $\pm\gamma_0$-Indexfehler korrigiert; $\mathcal{H}_W\cong L^2(\tau)$ via Suzuki 2025.  
**Patch 2:** §2.3 vollständig geschlossen: Schwartz-Majorante mit $|\gamma-\gamma_0|$-Abhängigkeit; Summierbarkeit via Riemann–von Mangoldt ohne $m_\gamma=O(1)$; $(2\text{-DiffOther})$-$1/n$-Fehler und $(2\text{-FCauchy})$-Lücke behoben.  
**Patch 3:** §2.1 Spektralindexierung korrigiert: $\Gamma$ war fälschlich auf positive Ordinaten eingeschränkt. Jetzt signed set $\Gamma:=\{\gamma\in\mathbb{R}:\xi(1/2-i\gamma)=0\}$ (ohne Multiplizität); $N_\Gamma(T)=O(T\log T)$ angepasst. Kein Einfluss auf den Nichtabschließbarkeitsmechanismus.  
**Status:** Alle Buchungen $\checkmark[K/M]$; vollständig nach Patch 3.  
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

Nach Benedetto-Joyner; vgl. auch Bombieri 2000 §3, Weil 1952. Die Rückrichtung RH $\Rightarrow$ $W\in\mathcal{S}'$ folgt aus dem Weil-Positivitätskriterium (Suzuki 2011, Formel (0.1)):
$$
\text{RH}\Longrightarrow B_W(a,a)\ge0\quad\forall a\in C_c^\infty(\mathbb{R}). \qquad (1\text{-WeilPos})
$$

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

### 2.1 Atomare Spektraldarstellung unter RH — signed set (Patch 3)

Unter RH sind alle nichttrivialen Nullstellen $\rho=\tfrac{1}{2}+i\gamma$ mit $\gamma\in\mathbb{R}$. Sei
$$
\boxed{\Gamma := \{\gamma\in\mathbb{R}:\xi(1/2-i\gamma)=0\},} \qquad (2\text{-Gamma})
$$
die Menge aller Nullstellen von $\xi(1/2-iz)$ ohne Multiplizität. Unter RH ist $\Gamma\subset\mathbb{R}$, und wenn $\gamma\in\Gamma$ dann $-\gamma\in\Gamma$ (Symmetrie der Zetafunktion). $m_\gamma>0$ bezeichnet die Multiplizität.

Nach Suzuki (2011, Formel (1.2); 2025, §2) hat $B_W$ die Spektraldarstellung:
$$
\boxed{B_W(a,b)=\sum_{\gamma\in\Gamma}m_\gamma\,\hat a(-\gamma)\,\overline{\hat b(-\gamma)},} \qquad (2\text{-Spec})
$$
mit dem representierenden Spektralmaß:
$$
\mu_W=\sum_{\gamma\in\Gamma}m_\gamma\,\delta_{-\gamma}. \qquad (2\text{-Meas})
$$

$\mu_W$ ist rein atomar und singulär gegen Lebesgue: $\mu_W\perp dt$.

### 2.2 Hauptbeweis: Alpay-Jorgensen-Absolutstetigkeitssatz

Für translationsinvariante Formen der Gestalt $q_\sigma(f)=\int_{\mathbb{R}}|\hat f(t)|^2\,d\sigma(t)$ gilt nach Alpay-Jorgensen (2012, Thm. 3.4):
$$
\boxed{q_\sigma\text{ ist auf }L^2(\mathbb{R},dx)\text{ abschließbar}\quad\Longleftrightarrow\quad\sigma\ll dx.} \qquad (2\text{-AJ})
$$

Anwendung: $B_W(a,a)=q_{\mu_W}(a)$ mit $\mu_W\perp dt$. Also:
$$
\boxed{B_W\text{ ist auf }H_0=L^2(\mathbb{R},du)\text{ nicht abschließbar.}\quad\checkmark[K/M]\text{ (unter RH)}} \qquad (2\text{-NonClose})
$$

### 2.3 Explizite Folge (vollständiger Beweis, Patch 2+3)

**Keine** Annahme $m_\gamma=O(1)$. Vollständiges signed Spektrum.

**Setup.** Sei $\Phi:=\widehat\varphi$ mit $\varphi\in C_c^\infty(\mathbb{R})$, $\varphi\ge0$, $\Phi(0)\neq0$. Fixiere $\gamma_0\in\Gamma$, $\gamma_0>0$ und setze:
$$
a_n(u):=\frac{1}{n}\,e^{+i\gamma_0 u}\varphi(u/n),\qquad n\ge1. \qquad (2\text{-Folge})
$$

**Fouriertransformation.** Für alle $\gamma\in\mathbb{R}$:
$$
\hat a_n(-\gamma) = \Phi(n(\gamma_0-\gamma)). \qquad (2\text{-Four})
$$

**$L^2$-Norm:** $\|a_n\|_2^2=\frac{1}{n}\|\varphi\|_2^2\longrightarrow0. \qquad (2\text{-L2})$

**Atomwert:** $\hat a_n(-\gamma_0) = \Phi(0)\neq0\quad\forall n. \qquad (2\text{-Atom})$

**Formwert unter RH:**
$$
B_W(a_n,a_n) = m_{\gamma_0}|\Phi(0)|^2 + \sum_{\gamma\in\Gamma,\,\gamma\neq\gamma_0}m_\gamma|\Phi(n(\gamma_0-\gamma))|^2 \longrightarrow m_{\gamma_0}|\Phi(0)|^2>0. \qquad (2\text{-FormLimit})
$$

**Form-Cauchy-Nachweis.** Für $\gamma=\gamma_0$: $(\hat a_n-\hat a_m)(-\gamma_0) = 0$ exakt. $(2\text{-DiffAtom})$

Für $\gamma\in\Gamma$, $\gamma\neq\gamma_0$, $M:=\min(n,m)$, Schwartz-Abschätzung $|\Phi(x)|\le C_N(1+|x|)^{-N}$:
$$
|\hat a_n(-\gamma)-\hat a_m(-\gamma)| \le 2C_N(1+M|\gamma-\gamma_0|)^{-N}. \qquad (2\text{-DiffBound})
$$
$$
\boxed{B_W(a_n-a_m,a_n-a_m)\le 4C_N^2\sum_{\gamma\in\Gamma,\,\gamma\neq\gamma_0}m_\gamma(1+M|\gamma-\gamma_0|)^{-2N}.} \qquad (2\text{-FCMaj})
$$

**Summierbarkeit via Riemann–von Mangoldt.** Isolation: $\delta_{\gamma_0}:=\inf_{\gamma\in\Gamma,\,\gamma\neq\gamma_0}|\gamma-\gamma_0|>0$. $(2\text{-Sep})$

Die angepasste Zählfunktion:
$$
\boxed{N_\Gamma(T) := \sum_{\substack{\gamma\in\Gamma\\|\gamma|\le T}}m_\gamma = O(T\log T).} \qquad (2\text{-NTadj})
$$

(Das stimmt mit Riemann–von Mangoldt überein: die klassische $N(T)$ zählt Nullstellen des positiven Halbraums mit Multiplizität; $N_\Gamma(T)$ zählt beide Hälften, also $N_\Gamma(T)=2N(T)+O(1)=O(T\log T)$.)

Partielle Summation für $s=2N>1$:
$$
\sum_{\gamma\in\Gamma}m_\gamma(1+|\gamma|)^{-s} \ll \int_1^\infty t^{-s}\log t\,dt < \infty. \qquad (2\text{-Abel})
$$

Also $S_N<\infty$ und:
$$
B_W(a_n-a_m,a_n-a_m) = O(\min(n,m)^{-2N}) \longrightarrow 0. \qquad (2\text{-FCauchy})
$$

**Zusammenfassung:**
$$
\boxed{a_n\to0\text{ in }L^2,\quad B_W(a_n-a_m,a_n-a_m)\to0,\quad B_W(a_n,a_n)\longrightarrow m_{\gamma_0}|\Phi(0)|^2>0.\quad\checkmark[K/M]} \qquad (2\text{-Illust})
$$

---

## 3. Kato/KLMN auf $H_0=L^2(\mathbb{R})$ $\times[M]$

$$
\boxed{\text{Kato-Darstellungssatz und KLMN-Formperturbation auf }H_0=L^2(\mathbb{R},du):\quad\times[M].} \qquad (3\text{-KatoOut})
$$

$$
\boxed{\text{Semibeschränktheit und }L^2\text{-Abschließbarkeit von }B_W\text{ sind unvereinbar.}\quad\checkmark[K/M]} \qquad (3\text{-Incomp})
$$

$$
\text{KLMN-Kandidat NEU-256 }(\text{Leit-Rel}):\quad\times[M]\text{ (konditional: unter RH)} \qquad (3\text{-KLMN-Out})
$$

---

## 4. $H_0=L^2(\mathbb{R},du)$ reinterpretiert; $\mathcal{H}_W\cong L^2(\tau)$

$$
\boxed{H_0=L^2(\mathbb{R},du):\text{ kanonischer adelischer Referenzraum, nicht der Abschlussraum von }B_W.} \qquad (4\text{-H0})
$$

### 4.1 Natürlicher Abschluss unter RH: $\mathcal{H}_W\cong L^2(\tau)$

$$
d\tau(\lambda):=\sum_{\gamma\in\Gamma}m_\gamma\,\delta(\lambda-\gamma)\,d\lambda. \qquad (4\text{-tau})
$$

Suzuki (2025, §2, Thm. 2.1):
$$
\boxed{\mathcal{H}_W\cong L^2(\tau)\cong\ell^2(\Gamma,m_\gamma),\qquad a\mapsto(\sqrt{m_\gamma}\,\hat a(-\gamma))_{\gamma\in\Gamma}.} \qquad (4\text{-HW})
$$

$$
\boxed{\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\quad\checkmark[K/M]\text{ (konditional unter RH, via Suzuki 2025)}} \qquad (4\text{-Final})
$$

### 4.2 Strategische Folge

$$
\boxed{\text{Kann man }\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ RH-frei aus BC/Adelen konstruieren?}} \qquad (4\text{-ObjX})
$$

---

## 5. Weil-Kriterium: Operatorbild

$$
\text{RH}\iff\|\cdot\|_W\text{ ist Hilbertnorm auf }\mathcal{A}_{\rm PW}\iff\mathcal{H}_W\text{ wohldefiniert positiv.} \qquad (5\text{-Weil})
$$

---

## 6. Statusbuchungen

$$L^2\text{-Semibeschränktheit }B_W\Leftrightarrow\text{RH}\quad\checkmark[K/M]\qquad(6\text{-a})$$
$$\text{Bochner-Schwartz: Semibeschränktheit}\Rightarrow W\in\mathcal{S}'\Rightarrow\text{RH}\quad\checkmark[K/M]\qquad(6\text{-b})$$
$$\text{Reed-Simon-Kurzschluss}\quad\times[M]\qquad(6\text{-c})$$
$$\text{Alpay-Jorgensen: }q_\sigma\text{ abschließbar}\Leftrightarrow\sigma\ll dx\quad\checkmark[K/M]\qquad(6\text{-d})$$
$$\mu_W\perp dt\Rightarrow B_W\text{ nicht abschließbar (unter RH)}\quad\checkmark[K/M]\qquad(6\text{-e})$$
$$\text{Explizite Folge: vollständiger Direktbeweis (Patch 2+3)}\quad\checkmark[K/M]\qquad(6\text{-f})$$
$$\pm\gamma_0\text{-Indexfehler korrigiert}\quad\checkmark[K/M]\qquad(6\text{-g})$$
$$\text{Semibeschränktheit + Abschließbarkeit unvereinbar}\quad\checkmark[K/M]\qquad(6\text{-h})$$
$$\text{Kato/KLMN auf }H_0=L^2\quad\times[M]\qquad(6\text{-i})$$
$$\text{KLMN-Kandidat NEU-256 unter RH}\quad\times[M]\qquad(6\text{-j})$$
$$H_0=L^2\text{: Referenzraum ja, Abschlussraum nein}\quad\checkmark[K/M]\qquad(6\text{-k})$$
$$\mathcal{H}_W\cong\ell^2(\Gamma,m_\gamma)\text{ (konditional RH, Suzuki 2025)}\quad\checkmark[K/M]\qquad(6\text{-l})$$
$$\text{Normierungsabgleich: geschlossen durch NEU-258 Patch 1}\quad\checkmark[K/M]\qquad(6\text{-m})$$
$$\Gamma\text{ korrigiert zu signed set (Patch 3)}\quad\checkmark[K/M]\qquad(6\text{-n})$$
$$N_\Gamma(T)=O(T\log T)\text{ für signed }\Gamma\quad\checkmark[K/M]\qquad(6\text{-o})$$
$$\text{RH-freie Konstruktion }\mathcal{H}_W\text{ aus BC/Adelen}\quad?[O]\to\text{NEU-259}\qquad(6\text{-p})$$

---

## 7. Abhängigkeiten

| Referenz | SHA/Quelle | Inhalt |
|---|---|---|
| NEU-256 (Patch) | 8d67c54 | $R_{\rm arith}$; KLMN $\to\times[M]$ |
| NEU-255 (Patch 2) | bcc932d | $H_0=L^2$; Koisometrie |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention |
| NEU-220b | 3a7f2c1 | $\gamma_\infty$ Asymptotik |
| NEU-258 (Patch 1) | 4eeb501 | $W_{\rm NEU-252}=W_{\rm Lit}$; schließt $(1\text{-Norm})$ |
| Weil 1952 | — | Positivitätskriterium |
| Suzuki 2011/2025 | — | $\mathcal{H}_W\cong L^2(\tau)$; signed $\Gamma$ |
| Benedetto-Joyner | — | $W\in\mathcal{S}'\Leftrightarrow$ RH |
| Alpay-Jorgensen 2012 | Thm. 3.4 | $q_\sigma$ abschließbar $\Leftrightarrow\sigma\ll dx$ |
| Bochner-Schwartz | Reed-Simon II, IX.10 | Positiv-definit $\Rightarrow$ temperiert |
| Riemann–von Mangoldt | — | $N_\Gamma(T)=O(T\log T)$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm.*  
*Erstellt 2026-08-07. Patch (2026-08-07). Patch 2 (2026-08-08): §2.3 Schwartz-Majorante + Riemann–von Mangoldt. Patch 3 (2026-08-08): signed-$\Gamma$ in §2.1; $N_\Gamma(T)$ angepasst; $m_\gamma=O(1)$ nirgends verwendet.*