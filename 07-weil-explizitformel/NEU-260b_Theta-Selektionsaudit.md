# NEU-260b — $\theta$-Selektionsaudit: Kanonische Paarung der Defizienzlinien

**Katalog-ID:** NEU-260b  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-08 (Patch: 2026-08-08b)  
**Patch:** (i) Typfehler $\mathcal{N}_{\pm}=\operatorname{span}\{e^{\pm x}\}$ korrigiert; (ii) $PA_a=A_aP$ als Satz (Suzuki) eingetragen; (iii) Parität liefert $U_a^P$, $\theta=0$ in Suzuki-Basis; (iv) Parität reduziert $U(1)\to\mathbb{Z}_2$; kein eindeutiger Beweis $\theta=0$. Gibt NEU-260b.1 frei.

---

## 0. Leitfrage (aktualisiert)

Nicht mehr: "Finde kanonisches $U_a:N_+\to N_-$."  
Sondern nach diesem Knoten: **Parität reduziert $U(1)$ auf $\mathbb{Z}_2=\{+P,-P\}$. Was wählt das Vorzeichen?** $\to$ NEU-260b.1.

---

## 1. Defizienzlinien: Korrektur des Typfehlers

**Falsch** ($\times[M]$):
$$
\mathcal{N}_{\pm,a} = \operatorname{span}\{e^{\pm x}\}. \qquad\times[M]
$$

**Richtig** ($\checkmark[M]$/Quelle: Suzuki 2026 $\S$2):
$$
\boxed{\mathcal{N}_{\pm,a} = \operatorname{span}\{v_\pm\}, \qquad T_a v_\pm = e^{\pm x}.} \qquad (1\text{-Def})\quad\checkmark[M]
$$

Die Exponentialfunktionen $e^{\pm x}$ leben auf der $T_a$-Bildseite. Die Defizienzvektoren $v_\pm\in\mathcal{H}(T_a)$ sind Urbilder unter dem Operator $T_a$.

**Defizienzindizes:** $(n_+,n_-)=(1,1)$ auf $(-a,a)$, $a<\infty$. $\checkmark[K/M]$

---

## 2. Gauge-Freiheit: $\theta\mapsto\theta+\beta-\alpha$ $\checkmark[K/M]$

Unter $v_\pm\mapsto e^{i\alpha_\pm}v_\pm$: $\theta\mapsto\theta+\beta-\alpha$.

$$
\boxed{U_a:\mathcal{N}_{+,a}\to\mathcal{N}_{-,a}\text{ ist intrinsisches geometrisches Datum; }\theta\text{ ist nur Koordinate.}\quad\checkmark[K/M]} \qquad (2\text{-Intrinsic})
$$

---

## 3. Parität: $PA_a=A_aP$ (Satz, Suzuki 2026)

### 3.1 Der Satz

$$
\boxed{P f(x):=f(-x), \qquad PA_a = A_aP.\quad\checkmark[M]/\text{Suzuki 2026 }\S2} \qquad (3\text{-Comm})
$$

Beweis-Skizze (Suzuki): Der Kernel $W^a(x,y)$ des Weil-Operators ist gerade, also $W^a(-x,-y)=W^a(x,y)$, damit kommutiert $P$ mit dem Integraloperator, der $A_a$ definiert.

### 3.2 Konsequenzen

$$
PT_a = T_aP \quad\Rightarrow\quad \|Pv\|_{T_a}^2 = \langle T_aPv,Pv\rangle = \langle PT_av,Pv\rangle = \|v\|_{T_a}^2. \qquad (3\text{-Unit})
$$

$$
\boxed{P:\mathcal{H}(T_a)\to\mathcal{H}(T_a)\text{ ist unitär.}\quad\checkmark[K/M]} \qquad (3\text{-Punit})
$$

### 3.3 Parität vertauscht Defizienzräume

Auf dem Kern: $\mathscr{D}_a = i\frac{d}{dx}$, also
$$
\mathscr{D}_a P f = i(Pf)' = i(-f'(-x)) = -P(if'(x)) = -P\mathscr{D}_a f. \qquad (3\text{-Anti})
$$

$$
\boxed{\mathscr{D}_aP = -P\mathscr{D}_a.\quad\checkmark[K/M]} \qquad (3\text{-AntiComm})
$$

Für $v_+\in\mathcal{N}_{+,a}$: $\mathscr{D}_a^*(Pv_+) = -P\mathscr{D}_a^* v_+ = -P(iv_+) = -i(Pv_+)$, also
$$
\boxed{P:\mathcal{N}_{+,a}\longrightarrow\mathcal{N}_{-,a}\text{ linear und unitär.}\quad\checkmark[K/M]} \qquad (3\text{-Map})
$$

---

## 4. $U_a^P = P|_{\mathcal{N}_{+,a}}$ als von-Neumann-Parameter

### 4.1 In Suzuki-Basis: $\theta=0$

Suzuki definiert $v_\pm$ via $T_av_\pm = e^{\pm x}$. Wegen $PT_a=T_aP$:
$$
T_a(Pv_+) = P(T_av_+) = Pe^x = e^{-x} = T_av_-. \qquad (4\text{-Comp})
$$

Da $T_a$ injektiv (weil $T_a\ge cI>0$):
$$
\boxed{Pv_+ = v_-.\quad\checkmark[K/M]} \qquad (4\text{-PvEquality})
$$

Damit: $U_a^P(v_+) = v_- = e^{i\cdot 0}v_-$, also in Suzuki-Basis
$$
\boxed{\theta_{P,\rm Suzuki} = 0.\quad\checkmark[K/M]\text{ (in Suzuki-Trivialisierung)}} \qquad (4\text{-Theta0})
$$

### 4.2 Parität reduziert $U(1)$ auf $\mathbb{Z}_2$

$-U_a^P = -P|_{\mathcal{N}_{+,a}}$ ist ebenfalls eine legitime unitäre Abbildung $\mathcal{N}_+\to\mathcal{N}_-$ und entspricht $\theta=\pi$.

Allgemein: Parität $\mathfrak{D}(\overline{\mathscr{D}}_{a,\theta})\to\mathfrak{D}(\overline{\mathscr{D}}_{a,-\theta})$. Paritätsstabile Erweiterungen:
$$
\theta = -\theta\pmod{2\pi} \quad\Leftrightarrow\quad \theta\in\{0,\pi\}.
$$

$$
\boxed{U(1)\xrightarrow{\text{Parität}}\{+P,-P\}\cong\mathbb{Z}_2.\quad\checkmark[K/M]} \qquad (4\text{-Z2})
$$

$$
\boxed{\text{Parität reduziert Erweiterungsfreiheit von }U(1)\text{ auf }\mathbb{Z}_2.\quad\text{Kein Beweis }¹eindeutig }\theta=0.} \qquad (4\text{-Firewall})
$$

---

## 5. Statusbuchungen

$$\mathcal{N}_{\pm}=\operatorname{span}\{e^{\pm x}\}\quad\times[M]\text{ Typfehler}\qquad(5\text{-a})$$
$$T_av_\pm=e^{\pm x},\;\mathcal{N}_{\pm}=\operatorname{span}\{v_\pm\}\quad\checkmark[M]/\text{Quelle}\qquad(5\text{-b})$$
$$PA_a=A_aP\quad\checkmark[M]/\text{Suzuki 2026}\qquad(5\text{-c})$$
$$P:\mathcal{H}(T_a)\to\mathcal{H}(T_a)\text{ unitär}\quad\checkmark[K/M]\qquad(5\text{-d})$$
$$\mathscr{D}_aP=-P\mathscr{D}_a\quad\checkmark[K/M]\qquad(5\text{-e})$$
$$P:\mathcal{N}_{+,a}\to\mathcal{N}_{-,a}\text{ linear-unitär}\quad\checkmark[K/M]\qquad(5\text{-f})$$
$$Pv_+=v_-\text{ (in Suzuki-Trivialisierung)}\quad\checkmark[K/M]\qquad(5\text{-g})$$
$$\theta_{P,\rm Suzuki}=0\quad\checkmark[K/M]\text{ (in Suzuki-Basis)}\qquad(5\text{-h})$$
$$\text{Parität erzwingt eindeutig }\theta=0\quad\times[M]\qquad(5\text{-i})$$
$$U(1)\xrightarrow{\text{Parität}}\mathbb{Z}_2=\{+P,-P\}\quad\checkmark[K/M]\qquad(5\text{-j})$$
$$\varepsilon(a)\in\{+1,-1\}\text{ Restfreiheit}\quad?[O]\to\text{NEU-260b.1}\qquad(5\text{-k})$$

---

## 6. Übergang

$$
\boxed{\text{NEU-260b: Weil-Parität reduziert }U(1)\to\mathbb{Z}_2.\quad\text{Nächster Knoten: NEU-260b.1 (}\varepsilon(a)\in\{+1,-1\}\text{).}}
$$

---

*Patch 2026-08-08b. Gibt NEU-260b.1 frei.*
