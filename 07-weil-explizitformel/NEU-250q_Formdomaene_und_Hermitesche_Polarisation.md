# NEU-250q — Direktaudit: Formdomäne und hermitesche Polarisation

**Katalog-ID:** NEU-250q  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch 1: 2026-08-07; Patch 2 §2: 2026-08-07)  
**Auftrag:** Vier Aufgaben: (1) Gauß-Gegenbeweis; (2) exakter Konvergenzbereich $B_{\rm fin}$; (3) Q-A/B/C-Entscheidung; (4) Strategische Konsequenz. Patch 1: Q-A korrigiert; $\mathcal{C}_{\rm conv}$/$\mathcal{C}_W$ unterschieden; Realitäts-Firewall. Patch 2: §2 exakte Primzahlpotenz-Konvergenzbedingung.  
**Gesamtausgang:** Q-A erste Fassung $\times[M]$; $J_{1/2}:\mathcal{C}_W\xrightarrow{\sim}\mathcal{S}_{\infty,W}$ $\checkmark[K/M]$; $\widetilde{\mathcal{S}}_{\rm adel}^W$ nicht dicht $\checkmark[K/M]$; Realitäts-Firewall $\to$ NEU-250r.  
**Vorgänger:** NEU-250m (M2-Patch), NEU-250p, NEU-220l, NEU-220j

---

## 0. Der Engpass

$$
\boxed{J_{1/2}P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty\text{ typkorrekt, aber }\mathcal{S}_\infty\not\subset\operatorname{Dom}(B_{\rm fin}).} \qquad (0\text{-Gap})
$$

---

## 1. Gauß-Gegenbeweis (vollständig)

**Testelement:**
$$
F(x_\infty,x_{\rm fin})=e^{-x_\infty^2}\mathbf{1}_{\hat{\mathbb{Z}}}(x_{\rm fin}),\quad a(y)=e^{y/2}e^{-e^{2y}}\in\mathcal{S}_\infty. \qquad (1\text{-Test})
$$

**Autokorrelation exakt:**
$$
\boxed{g_a(\log n)=\frac{\sqrt{\pi}}{2}\frac{n^{-1/2}}{\sqrt{1+n^{-2}}}.} \qquad (1\text{-Autocorr})
$$

*Herleitung:* Substitution $u=e^v$:
$$
g_a(t)=e^{-t/2}\int_0^\infty e^{-(1+e^{-2t})u^2}\,du=\frac{\sqrt{\pi}}{2}\frac{e^{-t/2}}{\sqrt{1+e^{-2t}}}.
$$

**Primterm:**
$$
B_{\rm fin}(a,a)=-\sqrt{\pi}\sum_{n\ge2}\frac{\Lambda(n)}{n\sqrt{1+n^{-2}}}\sim-\sqrt{\pi}\sum_n\frac{\Lambda(n)}{n}=-\infty. \qquad (1\text{-Div})
$$

$$
\boxed{B_{\rm fin}(a,a)=-\infty\text{ für }a=J_{1/2}P_{\rm Haar}F.} \qquad (1\text{-NoGo})
$$

---

## 2. Exakter Konvergenzbereich von $B_{\rm fin}$ (Patch 2)

$B_{\rm fin}$ läuft über **alle Primzahlpotenzen** $n=p^k$, $p$ prim, $k\ge1$. Die exakte absolute Konvergenzbedingung für $B_{\rm fin}(a,b)$ lautet:

$$
\boxed{\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}\,|g_{a,b}(k\log p)|<\infty.} \qquad (2\text{-Conv-Exact})
$$

Die $k\ge2$-Terme dürfen nicht vernachlässigt werden. Bereits bei $k=2$ steht der Summand $(\log p)/p$, was einer konvergenten Reihe entspricht — aber das Zusammenspiel mit dem Verhalten von $g_{a,b}$ bei größeren Argumenten muss explizit kontrolliert werden.

**Rückzug der bisherigen Reduktion:** Die erste Fassung schrieb
$$
\sum_p\frac{\log p}{\sqrt{p}}\,|g_a(\log p)|<\infty \qquad \times[M]\text{ (als alleinige Bedingung)}
$$
als exakte Konvergenzbedingung. Das war eine unbe­gründete Reduktion auf $k=1$.

$$
\boxed{\sum_p\frac{\log p}{\sqrt{p}}|g_a(\log p)|<\infty\quad\text{nur als notwendige, nicht hinreichende Teilbedingung.}} \qquad (2\text{-Old-Partial})
$$

**Hinreichende Bedingung für alle $k$:** Falls $|g_{a,b}(t)|\le Ce^{-(1/2+\varepsilon)t}$ für ein $\varepsilon>0$ und alle $t\ge1$, dann
$$
\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}|g_{a,b}(k\log p)|\le C\sum_p\sum_{k\ge1}\frac{\log p}{p^{k(1+\varepsilon)}}<\infty.
$$

Der Paley-Wiener-Unterraum $\mathcal{S}_{\infty,W}$ erfüllt diese Bedingung: kompakter Träger von $\Phi a$ impliziert super-exponentiellen Abfall von $g_{a,b}$.

$$
\boxed{\operatorname{Dom}(B_{\rm fin})\supset\mathcal{S}_{\infty,W},\quad\operatorname{Dom}(B_{\rm fin})\not\supset\mathcal{S}_\infty.} \qquad (2\text{-Dom})
$$

---

## 3. Q-A — Fehlerkorrektur

### 3.1 Erste Fassung (zurückgezogen)

$$
\boxed{C_c^\infty(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}\quad\times[M].} \qquad (3\text{-OldNoGo})
$$

### 3.2 Gegenbeispiel

Nehme $h\in C_c^\infty(\mathbb{R})$ mit $h(x)=1$ in einer Umgebung von $0$. Dann:
$$
(\Phi J_{1/2}h)(y)=e^{y/2}h(e^y)\xrightarrow{y\to-\infty}e^{y/2}\neq 0.
$$
Kein kompakter Träger in der Logkoordinate:
$$
\boxed{J_{1/2}h\notin\mathcal{S}_{\infty,W}.} \qquad (3\text{-Cex})
$$

Dieselbe $h(0)\neq0$-Situation erzeugt den Grenzabfall $e^{-t/2}$ in der Autokorrelation — denselben Mechanismus wie im Gauß-Beispiel. $P_{\rm Haar}F\in C_c^\infty(\mathbb{R})$ reicht nicht einmal allgemein für $B_{\rm fin}$-Konvergenz.

### 3.3 Zwei korrekte Zielräume

**Für $B_{\rm fin}$-Konvergenz** (ohne Realität/Geradheit):
$$
\boxed{\mathcal{C}_{\rm conv}:=C_c^\infty((0,\infty);\mathbb{C}).} \qquad (3\text{-Cconv})
$$
Für $h\in\mathcal{C}_{\rm conv}$: Träger weg von $0$ $\Rightarrow$ $\Phi J_{1/2}h$ kompakt getragen $\Rightarrow$ super-exponentieller Abfall $\Rightarrow$ (2-Conv-Exact) erfüllt.

**Für den reell-selbstdualen Weil-Kern:**
$$
\boxed{\mathcal{C}_W:=\{h\in C_c^\infty((0,\infty);\mathbb{R}):h(1/x)=x\,h(x)\}.} \qquad (3\text{-CW})
$$

Selbstdualitätsbedingung: $g:=\Phi J_{1/2}h$ gerade $\Leftrightarrow$ $e^{y/2}h(e^y)=e^{-y/2}h(e^{-y})$ $\Leftrightarrow$ $h(1/x)=x\,h(x)$.

**Bijektion:**
$$
\boxed{J_{1/2}:\mathcal{C}_W\xrightarrow{\;\sim\;}\mathcal{S}_{\infty,W}.\quad\checkmark[K/M]} \qquad (3\text{-Bij})
$$

Rückrichtung: $g\in C_{c,\rm even}^\infty(\mathbb{R};\mathbb{R})\Rightarrow h(x):=x^{-1/2}g(\log x)\in\mathcal{C}_W$.

### 3.4 Korrigierter Q-A-Unterraum

$$
\boxed{\widetilde{\mathcal{S}}_{\rm adel}^W:=P_{\rm Haar}^{-1}(\mathcal{C}_W)\subset\mathcal{S}(\mathbb{A}_\mathbb{Q}).} \qquad (3\text{-QA-corr})
$$

Kette:
$$
\boxed{\widetilde{\mathcal{S}}_{\rm adel}^W\xrightarrow{P_{\rm Haar}}\mathcal{C}_W\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}\xrightarrow{\mathcal{M}_\infty}\mathcal{W}.\quad\checkmark[K/M]_{\rm cond}} \qquad (3\text{-QA-Chain})
$$

---

## 4. Nichtdichtheit von $\widetilde{\mathcal{S}}_{\rm adel}^W$ in $\mathcal{S}(\mathbb{A}_\mathbb{Q})$

Für jedes $F\in\widetilde{\mathcal{S}}_{\rm adel}^W$: $(P_{\rm Haar}F)(-1)=0$ weil $\mathcal{C}_W\subset C_c^\infty((0,\infty))$. Das Auswertungsfunktional $L(F):=(P_{\rm Haar}F)(-1)$ ist stetig und nichttrivial, also:

$$
\widetilde{\mathcal{S}}_{\rm adel}^W\subset\ker L\subsetneq\mathcal{S}(\mathbb{A}_\mathbb{Q}).
$$

$$
\boxed{\widetilde{\mathcal{S}}_{\rm adel}^W\text{ ist nicht dicht in }\mathcal{S}(\mathbb{A}_\mathbb{Q}).\quad\checkmark[K/M]} \qquad (4\text{-NoDense})
$$

Vor Anlage von NEU-250r negativ entschieden.

---

## 5. Strategische Neubewertung

$$
\boxed{\begin{aligned}
&\text{(i) Die Quelle von Objekt X könnte von Anfang an ein selbstdualer Teilraum sein,}\\
&\quad\text{nicht dicht in der vollen Schwartz-Bruhat-Algebra.}\\
&\text{(ii) Der komplexe Amplitudenport }R_{\rm PW}\text{ ist der natürlichere Kandidat}\\
&\quad\text{für M3 — }\mathcal{A}_{\rm PW}\text{ braucht keine Einschränkung auf }\mathcal{C}_W.
\end{aligned}} \qquad (5\text{-Strat})
$$

M3-Freigabe nach NEU-250r: komplexer Amplitudenport und Auflösung der Realitäts-Firewall.

---

## 6. Realitäts-Firewall für M3

NEU-220j definiert seinen Testkern mit **reell-geraden** $g$ (reeller Vektorraum). Für die hermitesche sesquilineare Polarisation $(a,b)\mapsto g_{a,b}(t)$ braucht man einen **komplexen** Raum (NEU-220l: $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C})$).

$$
\boxed{\text{reell-gerader Weil-Kern }(\mathcal{C}_W)\neq\text{komplexe Formdomäne für }B_W(a,b).} \qquad (6\text{-Firewall})
$$

Auflösung: Realität und Geradheit entstehen erst diagonal durch $a\mapsto c_a\mapsto g_a$. Der Quellenraum selbst muss komplex sein. $\to$ **NEU-250r**.

---

## 7. Statusbuchungen

$$
B_{\rm fin}(a,a)=-\infty\text{ für }a=J_{1/2}P_{\rm Haar}(e^{-x^2}\mathbf{1}_{\hat{\mathbb{Z}}})\quad\checkmark[K/M] \qquad (7\text{-a})
$$

$$
C_c^\infty(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}\quad\times[M]\qquad(\text{Gegenbeispiel §3.2}) \qquad (7\text{-b})
$$

$$
J_{1/2}:\mathcal{C}_W\xrightarrow{\sim}\mathcal{S}_{\infty,W}\quad\checkmark[K/M] \qquad (7\text{-c})
$$

$$
\widetilde{\mathcal{S}}_{\rm adel}^W\text{ nicht dicht in }\mathcal{S}(\mathbb{A}_\mathbb{Q})\quad\checkmark[K/M] \qquad (7\text{-d})
$$

$$
\sum_p\frac{\log p}{\sqrt{p}}|g_a(\log p)|<\infty\quad\text{nur Teilbedingung}\quad\times[M]\text{ als alleinige Konvergenzbedingung} \qquad (7\text{-e})
$$

$$
\sum_p\sum_{k\ge1}\frac{\log p}{p^{k/2}}|g_{a,b}(k\log p)|<\infty\quad\text{exakte Bedingung}\quad\checkmark[K/M] \qquad (7\text{-f})
$$

$$
\text{Realitäts-Firewall }\mathcal{C}_W\neq\text{komplexe Formdomäne}\quad\to\text{NEU-250r Auflösung} \qquad (7\text{-g})
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250m | ecc1c3b | M2-Patch; $B_{\rm fin}$, Domain-Warnung |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette; Weil-Selbstdualität |
| NEU-220l | 1dc07b3 | Weil-Quadratik, $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C})$ |
| NEU-220j | 41e28cf | $\mathcal{S}_{\infty,W}$, reell-gerader Kern |
| **NEU-250r** | **neu** | **Komplexer Amplitudenport $R_{\rm PW}$; Surjektivität auf $\mathcal{A}_{\rm PW}$; Auflösung Realitäts-Firewall** |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 1: Q-A $\times[M]$; $\mathcal{C}_{\rm conv}$/$\mathcal{C}_W$; Bijektion; Nichtdichtheit; Firewall. Patch 2: §2 exakte Primzahlpotenz-Konvergenzbedingung; $k=1$-Reduktion zurückgezogen.*
