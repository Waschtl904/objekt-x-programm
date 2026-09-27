# NEU-255 — Haar-Koisometrie, kanonischer $L^2$-Hintergrundhilbertraum und $B_W$-Operatoraudit

**Patch 3 (2026-09-27):** Gamma-Hochfrequenzaudit gegen die in NEU-258 fixierte Normierung korrigiert: bei der Fourierkonvention $\hat f(t)=\int f(u)e^{itu}du$ gilt für $a_N=e^{iNu}\varphi$ der Shift $\hat a_N(t)=\hat\varphi(t+N)$. Auf der Diagonale ist $B_\Gamma(a,a)=\pi^{-1}\int |\hat a(t)|^2\operatorname{Re}\gamma_\infty(t)dt$; für $\|\varphi\|_2=1$ folgt daher $B_\Gamma(a_N,a_N)=\log N+O(1)$. Außerdem wurde der unzulässige exponentielle Schwanzfehler für eine bloße Schwartz-Funktion durch polynomialen Schnellabfall ersetzt. Der Unbeschränktheitsbefund bleibt unverändert.

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
\hat a_N(t)=\hat\varphi(t+N)\in\mathcal{S}(\mathbb{R}), \qquad (3\text{-Fourier})
$$
mit Schwartz-Abfall in $t$, zentriert bei $t=-N$.

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

### 3.3 Gamma-Block $B_\Gamma$: korrigierte Normalisierung und Hochfrequenzasymptotik

Nach dem vollständigen Normierungsabgleich in NEU-258 gilt auf der Diagonale

$$
\boxed{
B_\Gamma(a,a)
=
\frac{1}{\pi}
\int_{\mathbb R}
|\hat a(t)|^2\operatorname{Re}\gamma_\infty(t)\,dt.
}
\qquad (3\text{-BGam0})
$$

Für $a_N(u)=e^{iNu}\varphi(u)$ und die hier fixierte Fourierkonvention ist
$$
\hat a_N(t)=\hat\varphi(t+N).
$$
Daher
$$
B_\Gamma(a_N,a_N)
=
\frac{1}{\pi}
\int_{\mathbb R}
|\hat\varphi(t+N)|^2\operatorname{Re}\gamma_\infty(t)\,dt.
$$
Mit $r=t+N$:
$$
B_\Gamma(a_N,a_N)
=
\frac{1}{\pi}
\int_{\mathbb R}
|\hat\varphi(r)|^2\operatorname{Re}\gamma_\infty(r-N)\,dr.
\qquad (3\text{-BGam1})
$$

Aus Stirling folgt
$$
\operatorname{Re}\gamma_\infty(x)
=
\frac12\log|x|+O(1)
\qquad (|x|\to\infty).
$$

Teile das Integral in $|r|\le N/2$ und $|r|>N/2$.

**Kern.** Für $|r|\le N/2$ gilt gleichmäßig
$$
\operatorname{Re}\gamma_\infty(r-N)
=
\frac12\log N+O(1)+O(|r|/N).
$$
Da $\hat\varphi\in\mathcal S(\mathbb R)$ und nach Plancherel
$$
\int_{\mathbb R}|\hat\varphi(r)|^2\,dr
=
2\pi\|\varphi\|_2^2
=
2\pi,
$$
liefert der Kern
$$
\frac1\pi\int_{|r|\le N/2}
|\hat\varphi(r)|^2\operatorname{Re}\gamma_\infty(r-N)\,dr
=
\log N+O(1).
\qquad (3\text{-Core})
$$

**Schwanz.** Schwartz-Abfall impliziert für jedes $M>0$
$$
\int_{|r|>N/2}
(1+\log(N+|r|))\,|\hat\varphi(r)|^2\,dr
=
O_M(N^{-M}).
\qquad (3\text{-Tail})
$$
Insbesondere ist der Schwanz $o(1)$. Ein exponentieller Fehler $O(e^{-cN})$ folgt aus der Schwartz-Eigenschaft allein **nicht**.

Somit:
$$
\boxed{
B_\Gamma(a_N,a_N)=\log N+O(1)
}
\qquad(\|\varphi\|_2=1).
\qquad (3\text{-BGam3})
$$

Die alternative zweibumpige Darstellung des evenisierten Kerns $h_{a_N,a_N}$ ist damit kompatibel; für den Diagonalwert ist die NEU-258-Formel oben jedoch direkter und vermeidet eine doppelte Zählung der beiden Pakete.

### 3.4 Gesamtbefund

$$
B_W(a_N,a_N)=\underbrace{B_{\rm fin}(a_N,a_N)}_{O(1)}+\underbrace{B_{\rm pole}(a_N,a_N)}_{o(1)}+\underbrace{B_\Gamma(a_N,a_N)}_{\log N+O(1)}=\log N+O(1)\longrightarrow+\infty. \qquad (3\text{-Sum})
$$

$$
\boxed{B_W(a_N,a_N)=\log N+O(1),\quad\|a_N\|_2=1.\quad\checkmark[K/M]} \qquad (3\text{-Unbdd})
$$
$$
\boxed{B_W\text{ ist nicht beschränkt auf }H_0=L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (3\text{-Final})
$$

Fall 1 (Riesz direkt) scheidet aus. Der Leitkoeffizient $1$ folgt aus der NEU-258-Normierung und Plancherel.

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
$\hat a_N=\hat\varphi(\cdot+N)\in\mathcal{S},\text{ kein kompakter Support (Paley-Wiener)}\quad\checkmark[K/M] \qquad (7\text{-f})$
$$h_{a_N,a_N}\text{ zweibumpig bei }\pm N\text{ (Evenisierung)}\quad\checkmark[K/M] \qquad (7\text{-g})$$
$$B_{\rm fin}(a_N,a_N)=O(1);\;B_{\rm pole}(a_N,a_N)\to0\quad\checkmark[K/M] \qquad (7\text{-h})$$
$B_\Gamma(a_N,a_N)=\log N+O(1)\quad\checkmark[K/M] \qquad (7\text{-i})$
$\text{Gamma-Leitkoeffizient }1\text{ durch NEU-258-Normierung geschlossen}\quad\checkmark[K/M] \qquad (7\text{-j})$
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
| NEU-220k / NEU-258 | — | Fourierkonvention und abschließender Gamma-Normierungsabgleich |
| NEU-221 | f678057 | Normierungs-Firewall; $\mu_k$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220s/t | div. | Kreinraum; indefinite Realisierung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2: $P_{\rm fin}\to L^2(\mathbb{R})$ Typkette; Paley-Wiener-Warnung; zweibumpige Evenisierung; Kern/Schwanz-Beweis; $C_\Gamma>0$; Kato-Firewall.*
