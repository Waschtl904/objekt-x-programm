# NEU-255 — Haar-Koisometrie, kanonischer $L^2$-Hintergrundhilbertraum und $B_W$-Operatoraudit

**Katalog-ID:** NEU-255  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch 2: 2026-08-07)  
**Auftrag:** (1) Koisometrie $\overline{R}_{\rm PW}=S_{\rm PW}^*$ vollständig beweisen; (2) $H_0=L^2(\mathbb{R},du)$ als kanonischen positiven Hintergrundhilbertraum buchen; (3) Unbeschränktheit $B_W$ via Modulationsfolge $a_N=e^{iNu}\varphi$ rigoros beweisen; (4) Formklasse $B_W$ klären: Semibeschränktheit offen.  
**Patch 2:** $P_{\rm fin}\to L^2(\mathbb{R},dx)$ typisiert, erst $P_+\to L^2(\mathbb{R}_+,dx)$; kein kompakter Fourier-Support für $\hat\varphi\in\mathcal{S}$ (Paley-Wiener); zweibumpige Evenisierungsformel für $h_{a_N,a_N}$; Plancherel mit $2\pi$; Gamma-Asymptotik via Kern/Schwanzzerlegung; $C_\Gamma>0$ gebucht, exakter Wert $\to$ NEU-220k.  
**Status:** Koisometrie $\checkmark[K/M]$; $H_0=L^2(\mathbb{R},du)$ $\checkmark[K/M]$; $B_W$ unbeschränkt $\checkmark[K/M]$ (mit $C_\Gamma>0$); Semibeschränktheit $?[O]$; Formklasse $?[O]$; $A_X$ $?[O]$.  
**Vorgänger:** NEU-254 (Patch), NEU-253, NEU-252 (Patch), NEU-250r (Patch)

---

## 0. Ausgangslage

Aus NEU-254 §5:
$$
\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)},\qquad L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).
$$

**Zentralfrage M4-A** (NEU-253 §3):
$$
\boxed{\text{Welche Operator-/Formklasse besitzt }B_W\text{ relativ zu }H_0=L^2(\mathbb{R},du)?} \qquad (0\text{-Goal})
$$

**Fourierkonvention** (fixiert in NEU-252/NEU-220k):
$$
\boxed{\hat f(t)=\int_{\mathbb{R}}f(u)e^{itu}\,du,\qquad\|\hat f\|_2^2=2\pi\|f\|_2^2.} \qquad (0\text{-Four})
$$

---

## 1. Koisometriebeweis: $\overline{R}_{\rm PW}=S_{\rm PW}^*$

### 1.1 Kanonischer Lift $S_{\rm PW}$ (NEU-250r)

$$
\boxed{S_{\rm PW}a=h_a\otimes\mathbf{1}_{\widehat{\mathbb{Z}}},\qquad h_a(x)=\begin{cases}x^{-1/2}a(\log x),&x>0,\\0,&x\le0,\end{cases}\qquad R_{\rm PW}S_{\rm PW}=I.} \qquad (1\text{-Lift})
$$

### 1.2 $P_{\rm fin}$ und $P_+$: korrekte Typkette

**Schritt 1 — endliche Paarung** $P_{\rm fin}:L^2(\mathbb{A}_{\mathbb{Q}})\to L^2(\mathbb{R},dx)$:
$$
\boxed{(P_{\rm fin}F)(x):=\int_{\mathbb{A}_f}F(x,y)\,\mathbf{1}_{\widehat{\mathbb{Z}}}(y)\,d\mu_{\rm fin}(y),\qquad P_{\rm fin}:L^2(\mathbb{A})\longrightarrow L^2(\mathbb{R},dx).} \qquad (1\text{-Pfin})
$$
Wohldefiniert und kontraktiv nach Cauchy-Schwarz mit $\|\mathbf{1}_{\widehat{\mathbb{Z}}}\|_{L^2(\mathbb{A}_f)}^2=\mu_{\rm fin}(\widehat{\mathbb{Z}})=1$.

**Schritt 2 — Positivitätsbeschränkung** $P_+:L^2(\mathbb{R},dx)\to L^2(\mathbb{R}_+,dx)$:
$$
(P_+f)(x):=f(x)\cdot\mathbf{1}_{x>0}. \qquad (1\text{-Pplus})
$$

**Vollständige Typkette:**
$$
\boxed{\overline{R}_{\rm PW}:=J_{1/2}\circ P_+\circ P_{\rm fin}:L^2(\mathbb{A}_{\mathbb{Q}})\xrightarrow{P_{\rm fin}}L^2(\mathbb{R},dx)\xrightarrow{P_+}L^2(\mathbb{R}_+,dx)\xrightarrow{J_{1/2}}L^2(\mathbb{R},du).} \qquad (1\text{-Rbar})
$$

### 1.3 Unitarität von $J_{1/2}$

$$
(J_{1/2}f)(u):=e^{u/2}f(e^u),\qquad\|J_{1/2}f\|_{L^2(\mathbb{R},du)}^2=\int_\mathbb{R}|e^{u/2}f(e^u)|^2\,du\underset{x=e^u}{=}\int_0^\infty|f(x)|^2\,dx=\|f\|_{L^2(\mathbb{R}_+)}^2.
$$
$$
\boxed{J_{1/2}:L^2(\mathbb{R}_+,dx)\overset{\sim}{\longrightarrow}L^2(\mathbb{R},du)\text{ unitär.}\quad\checkmark[K/M]} \qquad (1\text{-Unit})
$$

### 1.4 $\overline{R}_{\rm PW}=S_{\rm PW}^*$: Beweis

Für $F\in L^2(\mathbb{A})$, $a\in\mathcal{A}_{\rm PW}$:
$$
\langle\overline{R}_{\rm PW}F,a\rangle_{L^2(\mathbb{R},du)}=\langle J_{1/2}P_+P_{\rm fin}F,a\rangle=\langle P_+P_{\rm fin}F,J_{1/2}^{-1}a\rangle_{L^2(\mathbb{R}_+)}.
$$

$(J_{1/2}^{-1}a)(x)=x^{-1/2}a(\log x)=h_a(x)$ für $x>0$. Damit:
$$
=\int_0^\infty\overline{(P_{\rm fin}F)(x)}\cdot h_a(x)\,dx=\int_0^\infty\int_{\mathbb{A}_f}\overline{F(x,y)}\,\mathbf{1}_{\widehat{\mathbb{Z}}}(y)\,d\mu_{\rm fin}(y)\cdot h_a(x)\,dx=\langle F,S_{\rm PW}a\rangle_{L^2(\mathbb{A})}.
$$
$$
\boxed{\overline{R}_{\rm PW}=S_{\rm PW}^*.\quad\checkmark[K/M]} \qquad (1\text{-Adj})
$$

$S_{\rm PW}$ isometrisch (NEU-254 §5.3) $\Rightarrow$ $\overline{R}_{\rm PW}S_{\rm PW}=I$ $\Rightarrow$ $\overline{R}_{\rm PW}$ **Koisometrie**:
$$
\boxed{L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (1\text{-Quot})
$$

---

## 2. Kanonischer positiver Hintergrundhilbertraum $H_0=L^2(\mathbb{R},du)$

$$
\boxed{\langle a,b\rangle_0:=\langle a,b\rangle_{L^2(\mathbb{R},du)}.\quad H_0=L^2(\mathbb{R},du)\text{ kanonischer positiver Hintergrundhilbertraum.}\quad\checkmark[K/M]} \qquad (2\text{-H0})
$$

Eigenschaften: RH-unabhängig; kanonisch adelisch; kein Fitten; $\mathcal{A}_{\rm PW}\subset H_0$ dicht. Kein Formkontroll-Anspruch: $B_W$ ist bzgl. $\|\cdot\|_0$ unbeschränkt (§3).

---

## 3. Unbeschränktheit $B_W$: Modulationstest (rigoros)

**Folge:** Sei $\varphi\in C_c^\infty(\mathbb{R})$, $\varphi\neq0$, $\|\varphi\|_2=1$, $\operatorname{supp}\varphi\subset[-R,R]$. Setze:
$$
\boxed{a_N(u):=e^{iNu}\varphi(u),\qquad N>0,\quad\|a_N\|_2=\|\varphi\|_2=1.} \qquad (3\text{-aN})
$$

**Paley-Wiener-Hinweis:** $\varphi\in C_c^\infty\Rightarrow\hat\varphi\in\mathcal{S}(\mathbb{R})$, insbesondere $\hat\varphi\notin C_c(\mathbb{R})$. Der Support von $\hat\varphi$ ist nicht kompakt. Das Fourierbild ist
$$
\hat a_N(t)=\hat\varphi(t-N)\in\mathcal{S}(\mathbb{R}), \qquad (3\text{-Fourier})
$$
mit Schwartz-Abfall in $t$, verschoben um $N$.

### 3.1 Primzahlpotenzblock $B_{\rm fin}$

Die Korrelationsfunktion $C_{a_N,a_N}(t)=\langle a_N,U_t a_N\rangle$ und die Evenisierung $g_{a_N,a_N}(t)=\frac{1}{2}(C_{a_N,a_N}(t)+C_{a_N,a_N}(-t))$ tragen in $t$ den Support von $C_{\varphi,\varphi}$, also $\operatorname{supp}g_{a_N,a_N}\subset[-2R,2R]$ für alle $N$. Die Primzahlpotenzsumme enthält daher nur Terme mit $\log p^k\le 2R$, endlich viele, mit $N$-unabhängigen Gewichten $\Lambda(p^k)$:
$$
\boxed{B_{\rm fin}(a_N,a_N)=O(1)\quad(N\to\infty).} \qquad (3\text{-Bfin})
$$

### 3.2 Polblock $B_{\rm pole}$

Aus NEU-252: $B_{\rm pole}(a,b)=h_{a,b}(i/2)+h_{a,b}(-i/2)$ (mit $h_{a,b}=\widehat{g_{a,b}}$, Polsymmetrisierung). Das Fouriertransformierte $h_{a_N,a_N}(z)=\int g_{a_N,a_N}(t)e^{izt}\,dt$ ist das Fourier-Integral einer für alle $N$ auf $[-2R,2R]$ getragenen glatten Funktion, ausgewertet bei den festen Werten $z=\pm i/2$. Die hochfrequente Modulation $e^{iNt}$ in $g_{a_N,a_N}$ bewirkt per Riemann-Lebesgue:
$$
\boxed{B_{\rm pole}(a_N,a_N)\to0\quad(N\to\infty).} \qquad (3\text{-Bpole})
$$

### 3.3 Gamma-Block $B_\Gamma$: zweibumpige Struktur und Kern/Schwanz

**Evenisierung:** Die Korrelation auf der Diagonale ergibt:
$$
g_{a_N,a_N}(t)=\tfrac{1}{2}\bigl(e^{iNt}C_{\varphi,\varphi}(t)+e^{-iNt}C_{\varphi,\varphi}(-t)\bigr). \qquad (3\text{-Even})
$$

Nach Fouriertransformation (Konvention $(0\text{-Four})$):
$$
h_{a_N,a_N}(s)=\widehat{g_{a_N,a_N}}(s)=\tfrac{1}{2}\bigl(\widehat{C_{\varphi,\varphi}}(s-N)+\widehat{C_{\varphi,\varphi}}(s+N)\bigr). \qquad (3\text{-TwoBump})
$$

Das Spektrum von $h_{a_N,a_N}$ besteht aus **zwei verschobenen Paketen** bei $+N$ und $-N$.

**Gamma-Block** (NEU-252 §3):
$$
B_\Gamma(a_N,a_N)=2\Lambda_\Gamma(h_{a_N,a_N})=2\cdot\frac{1}{2\pi}\tau_\infty(M_{\gamma_\infty\cdot h_{a_N,a_N}})=\frac{1}{\pi}\int_{\mathbb{R}}\gamma_\infty(s)\,h_{a_N,a_N}(s)\,ds. \qquad (3\text{-BGam0})
$$

Da $h_{a_N,a_N}$ symmetrisch und beide Pakete gleichwertig beitragen, genügt es, das Paket bei $+N$ zu betrachten (das bei $-N$ trägt durch Symmetrie von $\gamma_\infty$ denselben Beitrag):
$$
B_\Gamma(a_N,a_N)=\frac{1}{\pi}\int_{\mathbb{R}}\gamma_\infty(s)\,\widehat{C_{\varphi,\varphi}}(s-N)\,ds+\frac{1}{\pi}\int_{\mathbb{R}}\gamma_\infty(s)\,\widehat{C_{\varphi,\varphi}}(s+N)\,ds. \qquad (3\text{-BGam1})
$$

Betrachte das Paket bei $+N$ (Substitution $s=N+r$):
$$
I_+(N):=\int_{\mathbb{R}}\gamma_\infty(N+r)\,\widehat{C_{\varphi,\varphi}}(r)\,dr. \qquad (3\text{-BGam2})
$$

$\widehat{C_{\varphi,\varphi}}\in\mathcal{S}(\mathbb{R})$ (Schwartz-Abfall). **Kern/Schwanz-Zerlegung** bei $\delta=N/2$:
$$
I_+(N)=\underbrace{\int_{|r|\le N/2}\gamma_\infty(N+r)\,\widehat{C_{\varphi,\varphi}}(r)\,dr}_{I_{\rm kern}}+\underbrace{\int_{|r|>N/2}\gamma_\infty(N+r)\,\widehat{C_{\varphi,\varphi}}(r)\,dr}_{I_{\rm Schwanz}}. \qquad (3\text{-Split})
$$

**Kernteil $I_{\rm kern}$:** Für $|r|\le N/2$: $\log|N+r|=\log N+\log|1+r/N|=\log N+O(|r|/N)$ gleichmäßig. Mit $\operatorname{Re}\gamma_\infty(t)=\frac{1}{2}\log|t|+O(1)$ (NEU-220b):
$$
I_{\rm kern}=\bigl(\tfrac{1}{2}\log N+O(1)\bigr)\int_{|r|\le N/2}\widehat{C_{\varphi,\varphi}}(r)\,dr+O\Bigl(\tfrac{1}{N}\int_{\mathbb{R}}|r|\,|\widehat{C_{\varphi,\varphi}}(r)|\,dr\Bigr). \qquad (3\text{-Kern})
$$

Der Fehlerterm ist $O(N^{-1})$ weil $\widehat{C_{\varphi,\varphi}}\in\mathcal{S}$. Mit $\int_{\mathbb{R}}\widehat{C_{\varphi,\varphi}}(r)\,dr=2\pi C_{\varphi,\varphi}(0)=2\pi\|\varphi\|_2^2=2\pi>0$:
$$
I_{\rm kern}=\bigl(\tfrac{1}{2}\log N+O(1)\bigr)\cdot(2\pi+O(e^{-cN}))+O(N^{-1})=\pi\log N+O(1). \qquad (3\text{-Kern2})
$$

**Schwanzteil $I_{\rm Schwanz}$:** $|\gamma_\infty(N+r)|\le C(\log(N+|r|)+1)\le C(\log|r|+\log N+1)$ für großes $|r|$. Da $\widehat{C_{\varphi,\varphi}}$ Schwartz-Abfall hat:
$$
|I_{\rm Schwanz}|\le C\int_{|r|>N/2}(\log|r|+\log N)|\widehat{C_{\varphi,\varphi}}(r)|\,dr=O(e^{-cN})\cdot\text{poly}(N)=O(1). \qquad (3\text{-Tail})
$$

**Paket bei $-N$ (Substitution $s=-N+r$):** Liefert $I_-(N)=I_+(N)+O(1)$ durch Symmetrie $\gamma_\infty(-t)=\overline{\gamma_\infty(t)}$ und $\operatorname{Re}\gamma_\infty$ gerade.

**Gesamt:**
$$
\boxed{B_\Gamma(a_N,a_N)=C_\Gamma\log N+O(1),\qquad C_\Gamma>0,} \qquad (3\text{-BGam3})
$$
mit $C_\Gamma=\frac{2}{\pi}\cdot\pi=2$ bis zum vollständigen Normierungsabgleich mit dem in NEU-220k fixierten $2\pi$-Vorfaktor. Der exakte Wert $C_\Gamma$ ist erst nach diesem Abgleich zu buchen; die Positivität $C_\Gamma>0$ ist durch $(3\text{-Kern2})$ und $\|\varphi\|_2=1>0$ gesichert.

### 3.4 Gesamtbefund

$$
B_W(a_N,a_N)=\underbrace{B_{\rm fin}(a_N,a_N)}_{O(1)}+\underbrace{B_{\rm pole}(a_N,a_N)}_{o(1)}+\underbrace{B_\Gamma(a_N,a_N)}_{C_\Gamma\log N+O(1)}=C_\Gamma\log N+O(1)\longrightarrow+\infty. \qquad (3\text{-Sum})
$$

$$
\boxed{B_W(a_N,a_N)=C_\Gamma\log N+O(1),\quad C_\Gamma>0,\quad\|a_N\|_2=1.\quad\checkmark[K/M]} \qquad (3\text{-Unbdd})
$$
$$
\boxed{B_W\text{ ist nicht beschränkt auf }H_0=L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (3\text{-Final})
$$

Fall 1 (Riesz direkt) scheidet aus. Exakter Vorfaktor $C_\Gamma$ nach NEU-220k-Normierungsabgleich.

---

## 4. Formklasse von $B_W$: Semibeschränktheit und Szenarien

### 4.1 Dichte hermitesche Form

$\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R})\subset L^2(\mathbb{R},du)$ dicht; $B_W$ hermitesch (NEU-252 $\checkmark$).

### 4.2 RH-Firewall für Semibeschränktheit

$$
\boxed{B_W(a,a)<0\text{ für auch nur ein }a\in\mathcal{A}_{\rm PW}\Longrightarrow\neg\text{RH}.} \qquad (4\text{-Fire})
$$

(Aus NEU-220l: $B_W\ge0$ auf $\mathcal{A}_{\rm PW}$ $\Leftrightarrow$ RH.) Ein expliziter Nachweis der Verletzung der unteren Schranke wäre damit bereits eine RH-Widerlegung.

**Der RH-freie produktive Auftrag für NEU-256:**
$$
\boxed{\exists\lambda\in\mathbb{R}:\;B_W(a,a)\ge-\lambda\|a\|_2^2\quad\forall a\in C_c^\infty(\mathbb{R})\;?} \qquad (4\text{-Semi})
$$

Wenn $(4\text{-Semi})$ unabhängig von RH beweisbar ist, existiert eine geschlossene semibeschränkte Form und der Kato-Darstellungssatz liefert einen kanonischen selbstadjungierten $A_X$ auf $H_0$.

### 4.3 Drei Szenarien

**Szenario 1 — Semibeschränkt:** $B_W\ge-\lambda\|\cdot\|_0^2$; Kato anwendbar; $A_X\ge-\lambda I$ selbstadjungiert; Arithmetik im Spektrum.

**Szenario 2 — Nicht semibeschränkt:** $\exists b_n$, $\|b_n\|_0=1$, $B_W(b_n,b_n)\to-\infty$. Nach $(4\text{-Fire})$ wäre das $\neg$RH. Krein-Realisierung nötig (NEU-220s/t).

**Szenario 3 — Abschließbarkeit scheitert:** $H_0$ ungeeignet; andere Topologie nötig.

$$
\boxed{\text{Semibeschränktheit }B_W\text{ auf }L^2(\mathbb{R}):\quad?[O]\quad\to\text{NEU-256}} \qquad (4\text{-Open})
$$

### 4.4 Selbstadjungierte/Krein-Realisierung $A_X$

$$
\boxed{\text{Welcher Operator }A_X\text{ auf }L^2(\mathbb{R},du)\text{ repräsentiert die vollständige }B_W?\quad?[O]} \qquad (4\text{-ObjX})
$$

---

## 5. Signatur-Firewall (NEU-253 §4)

$$
\sigma_-(A_X)\neq\emptyset\iff\mathcal{H}_-\neq0\iff\neg\text{RH}. \qquad (5\text{-Fire})
$$

---

## 6. Verhältnis zu NEU-221-Momenten

Falls $A_X\ge0$ konstruiert (M4-D $\checkmark$), dann $T_X=A_X^{-1}$:
$$
\tau_{L^2}(T_X^{k+1})\stackrel{?}{=}\mu_k.\qquad\text{Normierungs-Firewall: alles durch }B_W\text{ und }L^2\text{-Maß fixiert.} \qquad (6\text{-Mom})
$$

---

## 7. Statusbuchungen

$$J_{1/2}\text{ unitär}\quad\checkmark[K/M] \qquad (7\text{-a})$$
$$P_{\rm fin}:L^2(\mathbb{A})\to L^2(\mathbb{R},dx);\;P_+:L^2(\mathbb{R})\to L^2(\mathbb{R}_+)\quad\checkmark[K/M] \qquad (7\text{-b})$$
$$\overline{R}_{\rm PW}=J_{1/2}P_+P_{\rm fin};\;\overline{R}_{\rm PW}=S_{\rm PW}^*\quad\checkmark[K/M] \qquad (7\text{-c})$$
$$L^2(\mathbb{A})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du)\quad\checkmark[K/M] \qquad (7\text{-d})$$
$$H_0=L^2(\mathbb{R},du)\text{ kanonischer positiver Hintergrundhilbertraum}\quad\checkmark[K/M] \qquad (7\text{-e})$$
$$\hat a_N=\hat\varphi(\cdot-N)\in\mathcal{S},\text{ kein kompakter Support (Paley-Wiener)}\quad\checkmark[K/M] \qquad (7\text{-f})$$
$$h_{a_N,a_N}\text{ zweibumpig bei }\pm N\text{ (Evenisierung)}\quad\checkmark[K/M] \qquad (7\text{-g})$$
$$B_{\rm fin}(a_N,a_N)=O(1);\;B_{\rm pole}(a_N,a_N)\to0\quad\checkmark[K/M] \qquad (7\text{-h})$$
$$B_\Gamma(a_N,a_N)=C_\Gamma\log N+O(1),\;C_\Gamma>0\quad\checkmark[K/M] \qquad (7\text{-i})$$
$$\text{Exakter Wert }C_\Gamma\text{ (NEU-220k-Normierungsabgleich)}\quad?[O\to\text{NEU-220k}] \qquad (7\text{-j})$$
$$B_W\text{ unbeschränkt auf }H_0\quad\checkmark[K/M] \qquad (7\text{-k})$$
$$B_W\text{ dicht definierte hermitesche Form}\quad\checkmark[K/M] \qquad (7\text{-l})$$
$$\text{Semibeschränktheit }B_W;\;\text{Formklasse}\quad?[O]\to\text{NEU-256} \qquad (7\text{-m})$$
$$A_X\text{ selbstadjungiert/Krein}\quad?[O] \qquad (7\text{-n})$$

---

## 8. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-254 (Patch) | 34c471d | $S_{\rm PW}$-Transport; Haar-Koisometrie vorl. |
| NEU-253 (Patch) | a95d3b5 | M4 Rahmen; Signatur-Firewall; M4-A Zwei-Fälle |
| NEU-252 (Patch) | 4ee78ed | $B_W$ hermitesch; Blöcke; $B_\Gamma=2\Lambda_\Gamma(h_{a,b})$ |
| NEU-250r (Patch) | bd1c0ab | $S_{\rm PW}$; $R_{\rm PW}S_{\rm PW}=I$ |
| NEU-220b | 3a7f2c1 | $\operatorname{Re}\gamma_\infty(t)=\tfrac12\log|t|+O(1)$ |
| NEU-220k | 8d4e9b2 | Fixierte $2\pi$-Fourierkonvention; $C_\Gamma$-Normierung |
| NEU-221 | f678057 | Normierungs-Firewall; $\mu_k$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220s/t | div. | Kreinraum; indefinite Realisierung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2: $P_{\rm fin}\to L^2(\mathbb{R})$ Typkette; Paley-Wiener-Warnung; zweibumpige Evenisierung; Kern/Schwanz-Beweis; $C_\Gamma>0$; Kato-Firewall.*
