# NEU-256 — Semibeschränktheit und Abschließbarkeit der Weil-Form auf $L^2(\mathbb{R})$

**Katalog-ID:** NEU-256  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** Vier atomare Tests A–D; Leitstruktur $B_W=B_\Gamma+R_{\rm arith}$ mit relativem Formperturbationsansatz.  
**Patch:** $B_{\rm fin}$-Formel auf M3-Form korrigiert; $|B_{\rm fin}|\le C\|\cdot\|_2^2$ $\times[M]$ (Skalierungsfolge); Gamma-Dominanz auf Hochfrequenzregime beschränkt; Gårding $\Rightarrow$ Abschließbarkeit $\times[M]$; neuer M4-A-Mechanismus $R_{\rm arith}=B_{\rm pole}+B_{\rm fin}$ gemeinsam relativ abzuschätzen.  
**Status:** $B_\Gamma\ge-C\|\cdot\|_2^2$ $\checkmark[K/M]$; alle weiteren Tests $?[O]$.  
**Vorgänger:** NEU-255 (Patch 2), NEU-253, NEU-252, NEU-220l

---

## 0. Ausgangslage

Aus NEU-255 $\checkmark[K/M]$:
- $H_0=L^2(\mathbb{R},du)$: kanonischer positiver Hintergrundhilbertraum.
- $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$: dicht definierte hermitesche Form auf $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R})$.
- $B_W$ nach oben unbeschränkt: $B_W(a_N,a_N)=C_\Gamma\log N+O(1)\to+\infty$ (Hochfrequenzregime).

**Fourierkonvention** (NEU-220k): $\hat f(t)=\int e^{itu}f(u)\,du$, $\|\hat f\|_2^2=2\pi\|f\|_2^2$.

**Zentralfrage:**
$$
\boxed{\text{Ist }B_W\text{ semibeschränkt und abschließbar auf }H_0?\quad\text{Falls ja: kanonisches }A_X=A_X^*\text{ auf }L^2(\mathbb{R},du).} \qquad (0\text{-Goal})
$$

**Logische Kette (Kato-Voraussetzungen):**
$$
\underbrace{B_W+\lambda\langle\cdot,\cdot\rangle_2\ge0}_{\text{(A) Semibeschränktheit}}+\underbrace{\text{Abschließbarkeit}}_{\text{(C)}}\Longrightarrow\overline{B_W}\text{ geschlossene Form}\Longrightarrow\underbrace{A_X=A_X^*}_{\text{(D) Kato}}. \qquad (0\text{-Chain})
$$

Beide Bedingungen unabhängig zu prüfen.

---

## RH-Firewall (NEU-220l)

$$
\boxed{B_W(a,a)<0\text{ für auch nur ein }a\in\mathcal{A}_{\rm PW}\Longrightarrow\neg\text{RH}.} \qquad (\text{Fire-RH})
$$

Auftrag von Test A: ausschließlich positiver Nachweis einer unteren Schranke. Kein Versuch, ein negatives Beispiel zu konstruieren.

---

## Leitstruktur: $B_W=B_\Gamma+R_{\rm arith}$

$$
\boxed{R_{\rm arith}:=B_{\rm pole}+B_{\rm fin}.} \qquad (\text{Leit-R})
$$

Die **positive geschlossene Gamma-Referenzform** (bereits wohldefiniert, NEU-252):
$$
q_\Gamma^+(a,a):=\int_{\mathbb{R}}|\hat a(t)|^2\log(1+|t|)\,dt+\|a\|_2^2. \qquad (\text{Leit-qGam})
$$

Domäne: $D(q_\Gamma^+)=\{a\in L^2(\mathbb{R}):\int|\hat a(t)|^2\log(1+|t|)\,dt<\infty\}$; $q_\Gamma^+$ ist abgeschlossen und positiv. Das ist die Referenztopologie für die Formperturbation.

**Neuer M4-A-Kernauftrag:**
$$
\boxed{|R_{\rm arith}(a,a)|\le\alpha\,q_\Gamma^+(a,a)+C\|a\|_2^2,\quad\alpha<1.} \qquad (\text{Leit-Rel})
$$

Wenn $(\text{Leit-Rel})$ gilt, folgt durch klassische Formperturbationstheorie: $B_W=B_\Gamma+R_{\rm arith}$ ist semibeschränkt und abschließbar; Kato anwendbar. Pol- und Primblock dürfen dabei **nicht** separat abgeschätzt werden: ihre gemeinsame arithmetische Kompensation ist Teil des zu untersuchenden Mechanismus.

**Regimeunterscheidung:** $\times[M]$ die Aussage, $B_\Gamma$ sei stets der dominante Block.

| Folge | Dominantes Regime | Dominant |
|---|---|---|
| $a_N=e^{iNu}\varphi(u)$ | Hochfrequenz ($N\to\infty$) | $B_\Gamma\sim C_\Gamma\log N$ |
| $a_L=L^{-1/2}\varphi(u/L)$ | Dilatation/Gro\ss{}träger ($L\to\infty$) | $B_{\rm pole}+B_{\rm fin}$ (massiv) |

---

## Test A — Untere Semibeschränktheit

### A.1 Prüffrage

$$
\boxed{\exists\lambda<\infty:\;B_W(a,a)\ge-\lambda\|a\|_2^2\quad\forall a\in C_c^\infty(\mathbb{R}).\quad?[O]} \qquad (\text{A-Semi})
$$

### A.2 Korrekte Blockformeln (verbindlich nach M3/NEU-252)

**Gamma-Block** (NEU-252 §3):
$$
B_\Gamma(a,a)=\int_{\mathbb{R}}|\hat a(t)|^2\operatorname{Re}\gamma_\infty(t)\,dt,\qquad\operatorname{Re}\gamma_\infty(t)=\tfrac{1}{2}\log|t|+O(1)\text{ (NEU-220b)}. \qquad (\text{A-Gamma})
$$

**Polblock** (NEU-252 §3):
$$
B_{\rm pole}(a,a)=h_{a,a}(i/2)+h_{a,a}(-i/2),\qquad h_{a,a}(z)=\widehat{g_{a,a}}(z). \qquad (\text{A-Pole})
$$

**Primblock** (verbindlich, M3/NEU-252; $\times[M]$ erste Fassung ohne $-2/\sqrt{n}$-Vorfaktor):
$$
\boxed{B_{\rm fin}(a,a)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_{a,a}(\log n).} \qquad (\text{A-Fin})
$$

### A.3 Einzelblock-Schranken: Stand

**Gamma nach unten:**
Aus $\operatorname{Re}\gamma_\infty(t)\ge-C_0$ (NEU-220b, $\gamma_\infty$ auf $|t|\le t_0$ explizit beschränkt; für $|t|>t_0$ folgt aus $\frac{1}{2}\log|t|\ge-C_0$):
$$
B_\Gamma(a,a)\ge-C_0\cdot2\pi\|a\|_2^2.\quad\checkmark[K/M] \qquad (\text{A-GammaLB})
$$

**Primblock $\times[M]$ als $L^2$-beschränkt:**
Sei $\varphi\in C_c^\infty(\mathbb{R})$, reell, nichtnegativ, $\varphi\neq0$, $\|\varphi\|_2=1$. Skalierungsfolge:
$$
a_L(u):=L^{-1/2}\varphi(u/L),\qquad\|a_L\|_2=\|\varphi\|_2=1. \qquad (\text{A-aL})
$$

Korrelation: $C_{a_L,a_L}(t)=\langle a_L,U_ta_L\rangle=\int a_L(u)a_L(u-t)\,du$. Substitution $u=Lv$:
$$
g_{a_L,a_L}(t)=C_{\varphi,\varphi}(t/L)=:C_\varphi(t/L). \qquad (\text{A-gL})
$$

Da $C_\varphi(0)=\|\varphi\|_2^2=1>0$ und $C_\varphi$ stetig: $\exists c,\delta>0$ mit $g_{a_L,a_L}(t)\ge c$ für $0\le t\le\delta L$. Damit:
$$
B_{\rm fin}(a_L,a_L)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,C_\varphi\!\left(\frac{\log n}{L}\right)\le-2c\sum_{n\le e^{\delta L}}\frac{\Lambda(n)}{\sqrt{n}}. \qquad (\text{A-FinScale})
$$

Primzahlsatz (Selberg-Form, NEU-220 Referenz): $\sum_{n\le X}\Lambda(n)/\sqrt{n}\sim2\sqrt{X}$ für $X\to\infty$. Mit $X=e^{\delta L}$:
$$
\sum_{n\le e^{\delta L}}\frac{\Lambda(n)}{\sqrt{n}}\sim2e^{\delta L/2}\longrightarrow+\infty. \qquad (\text{A-PNT})
$$

Also:
$$
\boxed{B_{\rm fin}(a_L,a_L)\longrightarrow-\infty\text{ bei }\|a_L\|_2=1.\quad\times[M]} \qquad (\text{A-FinUnbdd})
$$

$$
\boxed{B_{\rm fin}\text{ ist weder }L^2\text{-beschränkt noch separat nach unten }L^2\text{-beschränkt.}\quad\times[M]} \qquad (\text{A-FinFail})
$$

**Konsequenz:** Die Strategie, $B_{\rm pole}$ und $B_{\rm fin}$ separat nach unten abzuschätzen und dann zu addieren, ist gescheitert. Die relative Abschätzung $(\text{Leit-Rel})$ für $R_{\rm arith}=B_{\rm pole}+B_{\rm fin}$ **gemeinsam** ist der einzig tragfähige Weg. Die Explizitformel muss die Kompensation zwischen Pol- und Primblock organisieren.

**Polblock-Schranke:** Ob $|B_{\rm pole}(a,a)|\le C_{\rm pole}\|a\|_2^2$ gilt, ist separat offen:
$$
|B_{\rm pole}(a,a)|\le C_{\rm pole}\|a\|_2^2\quad?[O] \qquad (\text{A-PoleBound})
$$

### A.4 Status

$$
B_\Gamma(a,a)\ge-2\pi C_0\|a\|_2^2\quad\checkmark[K/M] \qquad (\text{A-GamLBb})
$$
$$
B_{\rm fin}\text{ nicht separat }L^2\text{-beschränkt}\quad\times[M] \qquad (\text{A-FinFail2})
$$
$$
\text{Untere Semibeschränktheit }B_W\quad?[O]\text{ (erzwingt relative Abschätzung für }R_{\rm arith}\text{)} \qquad (\text{A-Final})
$$

---

## Test B — Relative Formabschätzung für $R_{\rm arith}$

### B.1 Kernfrage

$$
\boxed{\exists\alpha<1,C<\infty:\;|R_{\rm arith}(a,a)|\le\alpha\,q_\Gamma^+(a,a)+C\|a\|_2^2\quad\forall a\in\mathcal{A}_{\rm PW}.\quad?[O]} \qquad (\text{B-Rel})
$$

### B.2 Formperturbationstheorie

Falls $(\text{B-Rel})$ gilt: $q_\Gamma^+$ positiv und geschlossen; $R_{\rm arith}$ relativ formbeschränkt mit relativem Schranke $\alpha<1$. Dann ist $B_W=B_\Gamma+R_{\rm arith}$ (mit geeignetem konstanten Anteil) semibeschränkt, abschließbar, und die Abschlussdomäne liegt in $D(q_\Gamma^+)$. Kato anwendbar.

**Klassischer Rahmen:** Das ist ein KLMN-artiger Satz (Kato-Lax-Milgram-Nelson-Nenciu, vgl. Reed-Simon X, §X.2): Eine relativ formbeschränkte Störung mit $\alpha<1$ eines geschlossenen semibeschränkten Operators liefert wieder einen geschlossenen semibeschränkten Operator.

### B.3 Warum $B_{\rm pole}+B_{\rm fin}$ gemeinsam und nicht separat

Der Skalierungstest zeigt: $B_{\rm fin}(a_L,a_L)\to-\infty$, aber $B_W(a_L,a_L)$ könnte trotzdem nach unten beschränkt sein, wenn $B_{\rm pole}(a_L,a_L)\to+\infty$ mit der richtigen Rate. Die Explizitformel kodiert gerade diese Kompensation: Die Polstellen bei $\rho=\tfrac{1}{2}\pm it_\rho$ und die Primzahlpotenzen sind durch die Weil-Formel direkt verknüpft.

$$
\boxed{\text{Kompensation }B_{\rm pole}+B_{\rm fin}:\quad\text{Mechanismus offen, RH-relevant.}\quad?[O]} \qquad (\text{B-Comp})
$$

### B.4 Gårding-Kandidat (beschränkter Anspruch)

Falls $(\text{B-Rel})$ gilt:
$$
B_W(a,a)\ge(1-\alpha)\,q_\Gamma^+(a,a)-C\|a\|_2^2\ge(1-\alpha)\int|\hat a(t)|^2\log(1+|t|)\,dt-(C+1-\alpha)\|a\|_2^2. \qquad (\text{B-Garding})
$$

Das ist eine Gårding-Ungleichung, aber sie **folgt** aus $(\text{B-Rel})$, nicht umgekehrt. Die einseitige Ungleichung $(\text{B-Garding})$ allein impliziert weder die obere Abschätzung noch die Normmäquivalenz noch die Abschließbarkeit. $\times[M]$ der vorherige Schluss Gårding $\Rightarrow$ $D(\overline B_W)=D(q_\Gamma^+)$ und automatische Abschließbarkeit.

### B.5 Status

$$
\text{Relative Formabschätzung }|R_{\rm arith}|\le\alpha q_\Gamma^++C\|\cdot\|_2^2,\;\alpha<1\quad?[O] \qquad (\text{B-Final})
$$

---

## Test C — Abschließbarkeit

### C.1 Verschobene Form (falls A positiv)

$$
\boxed{q_\lambda(a,b):=B_W(a,b)+(\lambda+1)\langle a,b\rangle_2,\qquad q_\lambda(a,a)\ge\|a\|_2^2.} \qquad (\text{C-Shift})
$$

### C.2 Abschließbarkeitskriterium

Abschließbar: Wenn $a_n\to0$ in $L^2$ und $q_\lambda(a_n-a_m,a_n-a_m)\to0$, dann $q_\lambda(a_n,b)\to0$ für alle $b\in\mathcal{A}_{\rm PW}$ (Reed-Simon, Thm.~X.23).

$$
\text{Abschließbarkeit }q_\lambda\quad?[O]\qquad(\text{C-Close})
$$

### C.3 Abschließbarkeit aus relativem Test

**Korrekte Implikation:** Falls $(\text{B-Rel})$ gilt, ist $q_\lambda$ abschließbar mit $D(\overline q_\lambda)\subset D(q_\Gamma^+)$ durch KLMN. Das ist der saubere Weg.

**$\times[M]$ Vorherige Aussage:** Eine einseitige Gårding-Unterabschätzung allein liefert weder $D(\overline B_W)=D(q_\Gamma^+)$ noch automatische Abschließbarkeit noch Normäquivalenz. Dafür ist zusätzlich die Oberabschätzung $B_W(a,a)\lesssim q_\Gamma^+(a,a)+\|a\|_2^2$ nötig, also gerade $(\text{B-Rel})$.

### C.4 Status

$$
\text{Abschließbarkeit }q_\lambda\quad?[O]\text{ (folgt aus B-Rel mit KLMN)} \qquad (\text{C-Final})
$$

---

## Test D — Selbstadjungierte Realisierung $A_X$

**Vorbedingung:** Tests A und C positiv (i.e. $(\text{B-Rel})$ $\checkmark$).

$$
\boxed{B_W(a,b)=\langle a,A_X b\rangle_0\;\forall a\in D(q_\lambda),\,b\in D(A_X),\qquad A_X=A_X^*,\;A_X\ge-\lambda I.} \qquad (\text{D-AX})
$$

$$
\text{Selbstadjungierte Realisierung }A_X\quad?[O]\text{ (Vorbedingung: B-Rel }\checkmark) \qquad (\text{D-Final})
$$

---

## 5. Weil-Kriterium als Operator-Aussage

Falls $A_X$ konstruiert (Test D $\checkmark$):
$$
\boxed{\text{RH}\iff A_X\ge0.} \qquad (\text{5-Weil})
$$

Aus NEU-220l ($B_W\ge0\Leftrightarrow$ RH) und $(\text{D-AX})$ direkt.

$$
\boxed{\text{adelische Haarstruktur}\to H_0=L^2(\mathbb{R},du)\to B_W\to A_X=A_X^*\to\text{RH}\iff A_X\ge0.} \qquad (\text{5-Chain})
$$

### 5.1 M4-C-Anschluss

$$
\boxed{E_{A_X}((-\infty,0))\stackrel{?}{=}0.} \qquad (\text{5-M4C})
$$

---

## 6. Statusbuchungen

$$B_\Gamma(a,a)\ge-2\pi C_0\|a\|_2^2\quad\checkmark[K/M]\qquad(6\text{-a})$$
$$\operatorname{Re}\gamma_\infty(t)\ge\tfrac12\log(1+|t|)-C\quad\checkmark[K/M]\qquad(6\text{-b})$$
$$B_{\rm fin}(a,a)=-2\sum_{n\ge2}\Lambda(n)n^{-1/2}g_{a,a}(\log n)\text{ (M3-Form)}\quad\checkmark[K/M]\qquad(6\text{-c})$$
$$B_{\rm fin}\text{ nicht separat }L^2\text{-beschränkt (Skalierungsfolge)}\quad\times[M]\qquad(6\text{-d})$$
$$\text{Gamma-Dominanz: nur Hochfrequenzregime}\quad\checkmark[K/M];\;\text{Dilatationsregime: }R_{\rm arith}\text{ dominant}\quad\checkmark[K/M]\qquad(6\text{-e})$$
$$\text{Gårding einseitig}\Rightarrow D(\overline B_W)=D(q_\Gamma^+)\text{ oder Abschließbarkeit}\quad\times[M]\qquad(6\text{-f})$$
$$\text{Relative Formabschätzung }|R_{\rm arith}|\le\alpha q_\Gamma^++C\|\cdot\|_2^2,\;\alpha<1\quad?[O]\qquad(6\text{-g})$$
$$\text{Semibeschränktheit }B_W\quad?[O]\text{ (hängt von B-Rel ab)}\qquad(6\text{-h})$$
$$\text{Abschließbarkeit }q_\lambda\quad?[O]\text{ (folgt aus B-Rel per KLMN)}\qquad(6\text{-i})$$
$$A_X=A_X^*\quad?[O]\qquad(6\text{-j})$$
$$\text{RH}\iff A_X\ge0\text{ (sobald }A_X\checkmark\text{, logisch aus NEU-220l)}\quad\checkmark[K/M]\qquad(6\text{-k})$$

---

## 7. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-255 (Patch 2) | bcc932d | $H_0$; Koisometrie; $B_W$ unbeschränkt; $C_\Gamma>0$ |
| NEU-252 (Patch) | 4ee78ed | $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$ M3-Formeln |
| NEU-253 (Patch) | a95d3b5 | M4 Rahmen; Signatur-Firewall |
| NEU-220b | 3a7f2c1 | $\operatorname{Re}\gamma_\infty(t)=\tfrac12\log|t|+O(1)$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention |
| Kato 1966 | — | Darstellungssatz semibeschränkte geschlossene Formen |
| Reed-Simon X | — | Abschließbarkeitskriterium Thm.~X.23; KLMN §X.2 |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch: $B_{\rm fin}$-Formel M3-korrigiert; Skalierungsfolge $a_L$; $B_{\rm fin}$ nicht $L^2$-beschränkt $\times[M]$; Gamma-Dominanz nur Hochfrequenz; Gårding-Implikation $\times[M]$; $R_{\rm arith}$ als neuer atomarer Auftrag.*
