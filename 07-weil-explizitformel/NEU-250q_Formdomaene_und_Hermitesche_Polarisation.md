# NEU-250q — Direktaudit: Formdomäne und hermitesche Polarisation

**Katalog-ID:** NEU-250q  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** Vier Aufgaben: (1) Gauß-Gegenbeweis; (2) Konvergenzbereich $B_{\rm fin}$; (3) Q-A/B/C-Entscheidung; (4) Strategische Konsequenz. Patch: Q-A korrigiert; zwei Zielräume unterschieden; Realitäts-Firewall.  
**Gesamtausgang:** Q-A in erster Fassung $\times[M]$; korrigierter Q-A mit $\mathcal{C}_W$ $\checkmark[K/M]$; $\widetilde{\mathcal{S}}_{\rm adel}^W$ nicht dicht $\to$ NEU-250r.  
**Vorgänger:** NEU-250m (M2-Patch), NEU-250p ($J_{1/2}$-Kette), NEU-220l, NEU-220j

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

## 2. Konvergenzbereich von $B_{\rm fin}$

$B_{\rm fin}(a,a)$ konvergiert absolut genau dann, wenn
$$
\sum_p\frac{\log p}{\sqrt{p}}|g_a(\log p)|<\infty. \qquad (2\text{-Conv})
$$

Hinreichend: $|g_a(t)|\le Ce^{-(1/2+\varepsilon)t}$ für ein $\varepsilon>0$.

$$
\boxed{\operatorname{Dom}(B_{\rm fin})\supset\mathcal{S}_{\infty,W},\quad\operatorname{Dom}(B_{\rm fin})\not\supset\mathcal{S}_\infty.} \qquad (2\text{-Dom})
$$

---

## 3. Q-A — Fehlerkorrektur

### 3.1 Erste Fassung (zurückgezogen)

Die erste Fassung definierte
$$
\mathcal{S}_{\rm adel}^W:=\{F\in\mathcal{S}(\mathbb{A}_\mathbb{Q}):P_{\rm Haar}F\in C_c^\infty(\mathbb{R})\}
$$
und behauptete $C_c^\infty(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}$.

$$
\boxed{C_c^\infty(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}\quad\times[M].} \qquad (3\text{-OldNoGo})
$$

### 3.2 Gegenbeispiel

Nehme $h\in C_c^\infty(\mathbb{R})$ mit $h(x)=1$ in einer Umgebung von $0$. Dann:
$$
(\Phi J_{1/2}h)(y)=e^{y/2}h(e^y).
$$
Für alle hinreichend negativen $y$ gilt $e^y\approx0$, also $h(e^y)=1$, also
$$
(\Phi J_{1/2}h)(y)=e^{y/2}\neq 0\quad\text{für beliebig negative }y.
$$

Kein kompakter Träger in der Logkoordinate:
$$
\boxed{J_{1/2}h\notin\mathcal{S}_{\infty,W}.} \qquad (3\text{-Cex})
$$

Dieselbe $h(0)\neq0$-Situation erzeugt überdies den Grenzabfall $e^{-t/2}$ in der Autokorrelation — denselben Mechanismus wie im Gauß-Beispiel. $P_{\rm Haar}F\in C_c^\infty(\mathbb{R})$ reicht also nicht einmal allgemein für $B_{\rm fin}$-Konvergenz.

### 3.3 Zwei korrekte Zielräume

**Für $B_{\rm fin}$-Konvergenz** (ohne Realität/Geradheit):
$$
\boxed{\mathcal{C}_{\rm conv}:=C_c^\infty((0,\infty);\mathbb{C}).} \qquad (3\text{-Cconv})
$$
Für $h\in\mathcal{C}_{\rm conv}$ gilt $h(e^y)=0$ für alle $|y|>R$ (kompakt weg von $0$), also hat $\Phi J_{1/2}h$ kompakten Träger $\Rightarrow$ $B_{\rm fin}$-Konvergenz.

**Für den reell-selbstdualen Weil-Kern:**
$$
\boxed{\mathcal{C}_W:=\{h\in C_c^\infty((0,\infty);\mathbb{R}):h(1/x)=x\,h(x)\}.} \qquad (3\text{-CW})
$$

Herleitung der Selbstdualitätsbedingung: $g:=\Phi J_{1/2}h$ gerade bedeutet $g(y)=g(-y)$, d.h.\
$$
e^{y/2}h(e^y)=e^{-y/2}h(e^{-y}).
$$
Mit $x=e^y$:
$$
h(1/x)=x\,h(x).\qquad\checkmark
$$

**Bijektion:**
$$
\boxed{J_{1/2}:\mathcal{C}_W\xrightarrow{\;\sim\;}\mathcal{S}_{\infty,W}.\quad\checkmark[K/M]} \qquad (3\text{-Bij})
$$

Rückrichtung: Für $g\in C_{c,\rm even}^\infty(\mathbb{R};\mathbb{R})$ setze $h(x):=x^{-1/2}g(\log x)$. Dann $h\in\mathcal{C}_W$ und $\Phi J_{1/2}h=g$.

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

Für jedes $F\in\widetilde{\mathcal{S}}_{\rm adel}^W$ gilt $(P_{\rm Haar}F)(-1)=0$, weil $\mathcal{C}_W\subset C_c^\infty((0,\infty))$ auf $(0,\infty)$ getragen ist.

Das Auswertungsfunktional
$$
L:F\longmapsto(P_{\rm Haar}F)(-1)
$$
ist ein nichttriviales stetiges lineares Funktional auf $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ (Auswertung bei $x_\infty=-1$, $x_{\rm fin}\in\hat{\mathbb{Z}}$). Also:
$$
\widetilde{\mathcal{S}}_{\rm adel}^W\subset\ker L\quad\subsetneq\quad\mathcal{S}(\mathbb{A}_\mathbb{Q}).
$$

$$
\boxed{\widetilde{\mathcal{S}}_{\rm adel}^W\text{ ist nicht dicht in }\mathcal{S}(\mathbb{A}_\mathbb{Q}).} \qquad (4\text{-NoDense})
$$

Dieses Ergebnis ist vollständig vor Anlage von NEU-250r negativ entschieden.

---

## 5. Strategische Neubewertung

Nichtdichtheit bedeutet nicht Unbrauchbarkeit. Zwei Interpretationen:

$$
\boxed{\begin{aligned}
&\text{(i) Die Quelle von Objekt X ist von Anfang an ein selbstdualer Teilraum,}\\
&\quad\text{nicht dicht in der vollen Schwartz-Bruhat-Algebra — dann ist }\\
&\quad\widetilde{\mathcal{S}}_{\rm adel}^W\text{ der richtige Raum, vorausgesetzt seine Größe wird begründet.}\\
&\text{(ii) Es gibt einen weiteren kanonischen adelischen Unterraum,}\\
&\quad\text{der }\mathcal{C}_{\rm conv}\text{ oder }\mathcal{C}_W\text{ trifft und größer ist.}
\end{aligned}} \qquad (5\text{-Strat})
$$

---

## 6. Realitäts-Firewall für M3

NEU-220j definiert seinen Testkern mit **reell-geraden** $g$: das ist ein reeller Vektorraum. Für die hermitesche sesquilineare Polarisation $(a,b)\mapsto g_{a,b}(t)$ benötigt man dagegen einen **komplexen** linearen Raum, wie er in NEU-220l mit $C_c^\infty(\mathbb{R};\mathbb{C})$ erscheint.

$$
\boxed{\text{reell-gerader Weil-Kern }(\mathcal{C}_W)\neq\text{komplexe Formdomäne für }B_W(a,b).} \qquad (6\text{-Firewall})
$$

Diese Unterscheidung muss beim Übergang zu M3 explizit gemacht werden. $\to$ **NEU-250r**.

---

## 7. Statusbuchungen

$$
B_{\rm fin}(a,a)=-\infty\text{ für }a=J_{1/2}P_{\rm Haar}(e^{-x^2}\mathbf{1}_{\hat{\mathbb{Z}}})\quad\checkmark[K/M] \qquad (7\text{-a})
$$

$$
C_c^\infty(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}\quad\times[M]\qquad(\text{Gegenbeispiel \S3.2}) \qquad (7\text{-b})
$$

$$
J_{1/2}:\mathcal{C}_W\xrightarrow{\sim}\mathcal{S}_{\infty,W}\quad\checkmark[K/M] \qquad (7\text{-c})
$$

$$
\widetilde{\mathcal{S}}_{\rm adel}^W\text{ nicht dicht in }\mathcal{S}(\mathbb{A}_\mathbb{Q})\quad\checkmark[K/M]\qquad(\ker L\subsetneq\mathcal{S}(\mathbb{A}_\mathbb{Q})) \qquad (7\text{-d})
$$

$$
\text{Realitäts-Firewall: }\mathcal{C}_W\neq\text{komplexe Formdomäne}\quad\to\text{NEU-250r} \qquad (7\text{-e})
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250m | ecc1c3b | M2-Patch; $B_{\rm fin}$, Domain-Warnung |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette; Weil-Selbstdualität |
| NEU-220l | 1dc07b3 | Weil-Quadratik, $\mathcal{A}_{\rm PW}$-Domain |
| NEU-220j | 41e28cf | $\mathcal{S}_{\infty,W}$, reell-gerader Kern |
| **NEU-250r** | **neu** | **Audit: Selbstdualer adelischer Testunterraum, Nichtdichtheit, Realitäts-Firewall** |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: Q-A erste Fassung $\times[M]$; Gegenbeispiel; $\mathcal{C}_{\rm conv}$/$\mathcal{C}_W$ unterschieden; Bijektion $J_{1/2}:\mathcal{C}_W\to\mathcal{S}_{\infty,W}$; Nichtdichtheit; Realitäts-Firewall.*
