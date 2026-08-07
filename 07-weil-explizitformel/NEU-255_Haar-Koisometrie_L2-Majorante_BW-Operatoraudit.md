# NEU-255 — Haar-Koisometrie, kanonischer $L^2$-Hintergrundhilbertraum und $B_W$-Operatoraudit

**Katalog-ID:** NEU-255  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07 (Patch: 2026-08-07)  
**Auftrag:** (1) Koisometrie $\overline{R}_{\rm PW}=S_{\rm PW}^*$ vollständig beweisen; (2) $H_0=L^2(\mathbb{R},du)$ als kanonischen positiven Hintergrundhilbertraum buchen; (3) Unbeschränktheit $B_W$ via Modulationsfolge $a_N=e^{iNu}\varphi$ beweisen (alle drei Blöcke kontrolliert); (4) Formklasse von $B_W$ klären: Semibeschränktheit offen, keine naive Kato-Anwendung.  
**Patch:** $\overline{R}_{\rm PW}$ als $P_{\rm fin}$-Paarung sauber definiert; $\overline{R}_{\rm PW}=S_{\rm PW}^*$ bewiesen; „Hilbertmajorante" $\times[M]$ $\to$ „Hintergrundhilbertraum"; Unbeschränktheitsnachweis via Modulationsfolge $\checkmark[K/M]$; Kato-Fehler korrigiert.  
**Vorläufiger Status:** Koisometrie $\checkmark[K/M]$; $H_0=L^2(\mathbb{R},du)$ $\checkmark[K/M]$; $B_W$ unbeschränkt $\checkmark[K/M]$; Semibeschränktheit $?[O]$; Formklasse $?[O]$; $A_X$ $?[O]$.  
**Vorgänger:** NEU-254 (Patch), NEU-253, NEU-252 (Patch), NEU-250r (Patch)

---

## 0. Ausgangslage

Aus NEU-254 §5:
$$
\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)},\qquad L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).
$$

**Zentralfrage M4-A** (NEU-253 §3):
$$
\boxed{B_W(a,b)=\langle a,A_Xb\rangle_0\,?\qquad\text{Welche Operator-/Formklasse besitzt }B_W\text{ relativ zu }H_0=L^2(\mathbb{R},du)?} \qquad (0\text{-Goal})
$$

---

## 1. Koisometriebeweis: $\overline{R}_{\rm PW}=S_{\rm PW}^*$

### 1.1 Kanonischer Lift $S_{\rm PW}$ (NEU-250r)

$$
\boxed{S_{\rm PW}a=h_a\otimes\mathbf{1}_{\widehat{\mathbb{Z}}},\qquad h_a(x)=\begin{cases}x^{-1/2}a(\log x),&x>0,\\0,&x\le0,\end{cases}\qquad R_{\rm PW}S_{\rm PW}=I.} \qquad (1\text{-Lift})
$$

### 1.2 $P_{\rm fin}$: saubere Definition von $\overline{R}_{\rm PW}$

**Typkorrektur** (erste Fassung $\times[M]$): $F(\cdot,\mathbf{1}_{\widehat{\mathbb{Z}}})$ ist für ein $L^2(\mathbb{A})$-Element kein typkorrekter Ausdruck.

**Korrekte Definition:** Sei $\mathbb{A}=\mathbb{R}\times\mathbb{A}_f$ mit $\mathbb{A}_f=\widehat{\mathbb{Q}}$ (endlicher Adel). Definiere die **endliche Paarung**:
$$
\boxed{(P_{\rm fin}F)(x):=\int_{\mathbb{A}_f}F(x,y)\,\mathbf{1}_{\widehat{\mathbb{Z}}}(y)\,d\mu_{\rm fin}(y)\in L^2(\mathbb{R}_+,dx),} \qquad (1\text{-Pfin})
$$
wohldefiniert für $F\in L^2(\mathbb{A})$ als $L^2(\mathbb{R}_+)$-Wert nach Cauchy-Schwarz (endliche Paarung mit $\mathbf{1}_{\widehat{\mathbb{Z}}}\in L^2(\mathbb{A}_f,d\mu_{\rm fin})$, $\|\mathbf{1}_{\widehat{\mathbb{Z}}}\|^2=\mu_{\rm fin}(\widehat{\mathbb{Z}})=1$).

Sei $P_+$ die Beschränkung auf $x>0$. Dann:
$$
\boxed{\overline{R}_{\rm PW}:=J_{1/2}\circ P_+\circ P_{\rm fin}:L^2(\mathbb{A}_{\mathbb{Q}})\longrightarrow L^2(\mathbb{R},du).} \qquad (1\text{-Rbar})
$$

### 1.3 Unitarität von $J_{1/2}$

$$
J_{1/2}:L^2(\mathbb{R}_+,dx)\to L^2(\mathbb{R},du),\qquad(J_{1/2}f)(u)=e^{u/2}f(e^u). \qquad (1\text{-J12})
$$

$$
\|J_{1/2}f\|^2=\int_{\mathbb{R}}|e^{u/2}f(e^u)|^2\,du\underset{x=e^u}{=}\int_0^\infty|f(x)|^2\,dx=\|f\|^2. \qquad (1\text{-Isom})
$$

$$
\boxed{J_{1/2}\text{ unitär.}\quad\checkmark[K/M]} \qquad (1\text{-Unit})
$$

### 1.4 $\overline{R}_{\rm PW}=S_{\rm PW}^*$: Beweis

Für $F\in L^2(\mathbb{A})$, $a\in\mathcal{A}_{\rm PW}\subset L^2(\mathbb{R},du)$:
$$
\langle\overline{R}_{\rm PW}F,a\rangle_{L^2(\mathbb{R})}=\langle J_{1/2}P_+P_{\rm fin}F,a\rangle_{L^2(\mathbb{R})}=\langle P_+P_{\rm fin}F,J_{1/2}^*a\rangle_{L^2(\mathbb{R}_+)}. \qquad (1\text{-Adj1})
$$

Da $J_{1/2}$ unitär: $J_{1/2}^*=J_{1/2}^{-1}$, $(J_{1/2}^{-1}a)(x)=x^{-1/2}a(\log x)=h_a(x)$. Also:
$$
=\int_0^\infty\overline{(P_{\rm fin}F)(x)}\cdot h_a(x)\,dx=\int_0^\infty\int_{\mathbb{A}_f}\overline{F(x,y)}\,\mathbf{1}_{\widehat{\mathbb{Z}}}(y)\,d\mu_{\rm fin}(y)\cdot h_a(x)\,dx. \qquad (1\text{-Adj2})
$$

Andererseits:
$$
\langle F,S_{\rm PW}a\rangle_{L^2(\mathbb{A})}=\int_{\mathbb{A}}\overline{F(x,y)}(h_a\otimes\mathbf{1}_{\widehat{\mathbb{Z}}})(x,y)\,d\mu_{\rm Haar}=\int_0^\infty\int_{\mathbb{A}_f}\overline{F(x,y)}\,\mathbf{1}_{\widehat{\mathbb{Z}}}(y)\,d\mu_{\rm fin}(y)\cdot h_a(x)\,dx. \qquad (1\text{-Adj3})
$$

Beide Ausdrücke stimmen überein:
$$
\boxed{\langle\overline{R}_{\rm PW}F,a\rangle_{L^2(\mathbb{R})}=\langle F,S_{\rm PW}a\rangle_{L^2(\mathbb{A})},\quad\text{also }\overline{R}_{\rm PW}=S_{\rm PW}^*.\quad\checkmark[K/M]} \qquad (1\text{-Adj})
$$

Da $\langle S_{\rm PW}a,S_{\rm PW}b\rangle=\langle a,b\rangle_{L^2(\mathbb{R})}$ (NEU-254 §5.3), ist $S_{\rm PW}$ isometrisch, $\overline{R}_{\rm PW}S_{\rm PW}=I$, also $\overline{R}_{\rm PW}$ **Koisometrie**:
$$
\boxed{L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (1\text{-Quot})
$$

---

## 2. Kanonischer positiver Hintergrundhilbertraum $H_0=L^2(\mathbb{R},du)$

**Terminologiekorrektur** (erste Fassung $\times[M]$): „Hilbertmajorante" suggeriert, dass die Form $B_W$ durch die Norm kontrolliert wird. Da $B_W$ bzgl. $\|\cdot\|_2$ unbeschränkt ist (§3), ist $H_0$ keine $B_W$-Majorante im Formsinne.

$$
\boxed{H_0=L^2(\mathbb{R},du)\text{ ist der kanonische positive }\textbf{Hintergrundhilbertraum}.\quad\checkmark[K/M]} \qquad (2\text{-H0})
$$

Eigenschaften:
- **RH-unabhängig**: aus Haar-Maß und $J_{1/2}$, ohne $B_W$.
- **Kanonisch adelisch**: kein Fitten auf $\mu_k$; Normierung durch Lebesgue-Maß vollständig fixiert.
- **Dichte**: $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R})\subset H_0$ dicht.
- **Kein Formkontroll-Anspruch**: $B_W$ kann unbeschränkt oder indefinit auf $H_0$ sein.

Die Primzahlarithmetik steckt nach dem Quotient nicht sichtbar in $H_0$, sondern vollständig im Realisierungsoperator $A_X$ bzw. seiner Formstruktur.

---

## 3. Unbeschränktheit $B_W$: Modulationstest

**Typkorrektur** (erste Fassung $\times[M]$): Unbeschränktheitsnachweis über getrennte Konzentrationsfolgen für $B_{\rm pole}$ und Hochfrequenzfolgen für $B_\Gamma$ ist ungültig, weil Blockkompensationen möglich sind. Unbeschränkte Summanden $\Rightarrow$ unbeschränkte Summe gilt nicht.

**Korrekte Folge: Modulationstest.** Sei $\varphi\in C_c^\infty(\mathbb{R})$ mit $\|\varphi\|_2=1$, $\operatorname{supp}\varphi\subset[-R,R]$. Setze:
$$
\boxed{a_N(u):=e^{iNu}\varphi(u),\qquad N\in\mathbb{R},\quad\|a_N\|_2=1,\quad\operatorname{supp}a_N=\operatorname{supp}\varphi.} \qquad (3\text{-aN})
$$

Der Träger ist für alle $N$ gleich; die Frequenz wird verschoben.

### 3.1 Primzahlpotenzblock $B_{\rm fin}$

$g_{a_N,a_N}\in C_c^\infty(\mathbb{R})_{\rm even}$ mit $\operatorname{supp}g_{a_N,a_N}\subset[-2R,2R]$ für alle $N$. Die Primzahlpotenzsumme enthält daher nur endlich viele $p^k$ mit $\log p^k\le 2R$. Die Summanden oszillieren in $N$, aber die Anzahl und die $\Lambda(p^k)$-Gewichte sind von $N$ unabhängig:

$$
\boxed{B_{\rm fin}(a_N,a_N)=O(1)\quad(N\to\infty).} \qquad (3\text{-Bfin})
$$

### 3.2 Polblock $B_{\rm pole}$

Aus NEU-252 hat $B_{\rm pole}$ die Form $B_{\rm pole}(a,b)=h_{a,b}(i/2)+h_{a,b}(-i/2)$ (bzw. entsprechende Symmetrisierung). Hier ist $h_{a_N,a_N}(z)=\int_\mathbb{R} g_{a_N,a_N}(u)e^{izu}\,du$. Für $z=\pm i/2$ fest ist das ein Fourier-Integral einer kompakt getragenen $C_c^\infty$-Funktion, deren Träger in $N$ konstant bleibt; die Amplitude skaliert durch die hochfrequente Phase $e^{iNu}$ in $g_{a_N,a_N}$ per Riemann-Lebesgue gegen Null:

$$
\boxed{B_{\rm pole}(a_N,a_N)\to0\quad(N\to\infty).} \qquad (3\text{-Bpole})
$$

### 3.3 Gamma-Block $B_\Gamma$

Aus NEU-252/NEU-220b hat das Gamma-Symbol asymptotisch:
$$
\gamma_\infty(t)=\tfrac{1}{2}\log|t|+O(1)\quad(|t|\to\infty). \qquad (3\text{-GamAsy})
$$

Das Fourierbild $\widehat{a_N}(t)=\hat{\varphi}(t-N)$ ist nach $t=N$ verschoben mit $\|\hat{a_N}\|_2=\|\hat\varphi\|_2=1$. Daher:
$$
B_\Gamma(a_N,a_N)=\int_\mathbb{R}|\hat\varphi(t-N)|^2\,\gamma_\infty(t)\,dt=\int_\mathbb{R}|\hat\varphi(s)|^2\,\gamma_\infty(s+N)\,ds. \qquad (3\text{-BGam1})
$$

Mit $\gamma_\infty(s+N)=\frac{1}{2}\log|s+N|+O(1)=\frac{1}{2}\log N+O(1)$ gleichmäßig auf $\operatorname{supp}\hat\varphi$ (für $N\gg\|\hat\varphi\|_{\rm supp}$):
$$
\boxed{B_\Gamma(a_N,a_N)=\tfrac{c}{2}\log N+O(1),\quad c=\int_\mathbb{R}|\hat\varphi(s)|^2\,ds=\|\hat\varphi\|_2^2=1>0.} \qquad (3\text{-BGam2})
$$

### 3.4 Gesamtbefund

$$
B_W(a_N,a_N)=\underbrace{B_{\rm fin}(a_N,a_N)}_{O(1)}+\underbrace{B_{\rm pole}(a_N,a_N)}_{o(1)}+\underbrace{B_\Gamma(a_N,a_N)}_{\frac{1}{2}\log N+O(1)}=\tfrac{1}{2}\log N+O(1)\longrightarrow+\infty. \qquad (3\text{-Sum})
$$

$$
\boxed{B_W(a_N,a_N)=\tfrac{1}{2}\log N+O(1)\quad\text{bei }\|a_N\|_2=1.\quad\checkmark[K/M]} \qquad (3\text{-Unbdd})
$$

$$
\boxed{B_W\text{ ist nicht beschränkt auf }H_0=L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (3\text{-Final})
$$

Fall 1 (Riesz direkt) aus NEU-253 §3 scheidet aus.

---

## 4. Formklasse von $B_W$: Semibeschränktheit und Kato

### 4.1 Dichte hermitesche Form

$$
\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R})\subset L^2(\mathbb{R},du)\text{ dicht.}\qquad B_W\text{ hermitesch auf }\mathcal{A}_{\rm PW}\times\mathcal{A}_{\rm PW}\quad(\text{NEU-252 }\checkmark). \qquad (4\text{-Dense})
$$

$B_W$ ist dicht definierte hermitesche Sesquilinearform. Das allein liefert keine selbstadjungierte Realisierung.

### 4.2 Semibeschränktheit — offene Frage

**Typkorrektur** (erste Fassung $\times[M]$): NEU-255 erster Fassung schrieb „Kato-Darstellungssatz $\Rightarrow$ $A_X\ge-\lambda I$". Das setzt Semibeschränktheit bereits voraus; sie folgt nicht aus bloßer Abschließbarkeit.

Der Kato-Darstellungssatz (Kato 1966, §VI.2) gilt für **semibeschränkte geschlossene** Formen. Er benötigt:
1. $B_W$ abschließbar,
2. $B_W\ge-\lambda\|\cdot\|_0^2$ für ein $\lambda\in\mathbb{R}$ (Semibeschränktheit),
3. Geschlossenheit der Abschließung.

Keines dieser drei Punkte ist aktuell bewiesen.

$$
\boxed{\text{Ist }B_W\text{ unterhalbbeschränkt?}\quad?[O]} \qquad (4\text{-Semi})
$$

Der Modulationstest §3 zeigt $B_W(a_N,a_N)\to+\infty$, also ist $B_W$ nach oben unbeschränkt. Über eine untere Schranke sagt das noch nichts.

### 4.3 Drei Szenarien für $B_W \rightsquigarrow A_X$

**Szenario 1 — Semibeschränkt und abschließbar:** Kato-Darstellungssatz anwendbar; $A_X\ge-\lambda I$ selbstadjungiert; $B_W$ wird von einer $H_0$-Sobolev-artigen Norm kontrolliert.

**Szenario 2 — Nicht semibeschränkt (indefinit nach unten):** Kato nicht anwendbar. Es gibt Folgen $b_n\in\mathcal{A}_{\rm PW}$, $\|b_n\|_0=1$, $B_W(b_n,b_n)\to-\infty$. Dann ist eine indefinite Operator-/Krein-Realisierung nötig (vgl. NEU-220s/t). Das wäre nach NEU-220l/253 §4 mit $\neg\text{RH}$ kompatibel oder könnte eine Block-Kompensationsstruktur zeigen.

**Szenario 3 — Abschließbarkeit scheitert:** $B_W$ ist nicht closable auf $L^2(\mathbb{R})$; die $H_0$-Topologie ist für $B_W$ ungeeignet.

$$
\boxed{\text{Formklasse }B_W\text{ relativ zu }H_0:\quad?[O]\quad\text{(Szenarien 1--3 ungeklärt)}} \qquad (4\text{-Class})
$$

### 4.4 Nächste Schritte

1. **Untere Schranke testen:** Gibt es $\lambda$ mit $B_W(a,a)\ge-\lambda\|a\|_2^2$ für alle $a\in\mathcal{A}_{\rm PW}$?
2. **Gamma-Block allein:** $B_\Gamma\ge0$ gilt wegen $\gamma_\infty(t)\ge0$ für $|t|\ge t_0$? Oder hat $B_\Gamma$ negative Richtungen?
3. **Polblock:** $B_{\rm pole}(a,a)\to0$ (§3.2) — ist $B_{\rm pole}$ kompakt relativ zu $B_\Gamma$?
4. Falls Szenario 2: $B_W$ als Kreinraumform; Verbindung zu NEU-220s/t.

---

## 5. Signatur-Firewall (NEU-253 §4)

Sobald $A_X$ in einem der drei Szenarien konstruiert ist:
$$
\sigma_-(A_X)\neq\emptyset\iff\mathcal{H}_-\neq0\iff\neg\text{RH}. \qquad (5\text{-Fire})
$$

Szenario 2 wäre mit $\neg\text{RH}$ kompatibel, aber nicht dasselbe: Das negative Spektrum müsste aus der vollständigen $B_W$ (nicht einzelner Block) stammen.

---

## 6. Verhältnis zu NEU-221-Momenten

Falls $A_X\ge0$ (Szenario 1 mit Positivität aus M4-D), dann $T_X=A_X^{-1}\ge0$:
$$
\tau_{L^2}(T_X^{k+1})\stackrel{?}{=}\mu_k\quad(k=0,1,2,\ldots). \qquad (6\text{-Moment})
$$

Normierungs-Firewall (NEU-221 §0): $A_X$ durch $B_W$ und $L^2$-Maß kanonisch fixiert — kein Fitten.

---

## 7. Statusbuchungen

$$J_{1/2}:L^2(\mathbb{R}_+,dx)\to L^2(\mathbb{R},du)\text{ unitär}\quad\checkmark[K/M] \qquad (7\text{-a})$$
$$P_{\rm fin}:L^2(\mathbb{A})\to L^2(\mathbb{R}_+,dx)\text{ sauber definiert als }L^2(\mathbb{A}_f)\text{-Paarung}\quad\checkmark[K/M] \qquad (7\text{-b})$$
$$\overline{R}_{\rm PW}=J_{1/2}P_+P_{\rm fin},\quad\overline{R}_{\rm PW}=S_{\rm PW}^*\quad\checkmark[K/M] \qquad (7\text{-c})$$
$$L^2(\mathbb{A})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du)\quad\checkmark[K/M] \qquad (7\text{-d})$$
$$H_0=L^2(\mathbb{R},du)\text{ kanonischer positiver Hintergrundhilbertraum (nicht "Majorante")}\quad\checkmark[K/M] \qquad (7\text{-e})$$
$$B_W(a_N,a_N)=\tfrac12\log N+O(1),\;\|a_N\|_2=1\quad\checkmark[K/M] \qquad (7\text{-f})$$
$$B_W\text{ unbeschränkt auf }H_0\quad\checkmark[K/M] \qquad (7\text{-g})$$
$$B_W\text{ dicht definierte hermitesche Form auf }\mathcal{A}_{\rm PW}\subset L^2\quad\checkmark[K/M] \qquad (7\text{-h})$$
$$\text{Semibeschränktheit }B_W\quad?[O] \qquad (7\text{-i})$$
$$\text{Abschließbarkeit }B_W\text{ auf }L^2(\mathbb{R})\quad?[O] \qquad (7\text{-j})$$
$$\text{Formklasse }B_W\text{ (Szenario 1--3)}\quad?[O] \qquad (7\text{-k})$$
$$\text{Selbstadjungierte/Krein-Realisierung }A_X\quad?[O] \qquad (7\text{-l})$$

---

## 8. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-254 (Patch) | 34c471d | Rollenvergleich; $S_{\rm PW}$-Transport-Satz |
| NEU-253 (Patch) | a95d3b5 | M4 Rahmen; Signatur-Firewall; M4-A Zwei-Fälle |
| NEU-252 (Patch) | 4ee78ed | $B_W$ hermitesch; $B_{\rm pole}+B_\Gamma+B_{\rm fin}$; $\gamma_\infty$ Asymptoik |
| NEU-250r (Patch) | bd1c0ab | $S_{\rm PW}$; $R_{\rm PW}S_{\rm PW}=I$ |
| NEU-221 | f678057 | Normierungs-Firewall; $T_X=B_X^{-1}$; Momente $\mu_k$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220s/t | 7c1a3f9/d8b2e51 | Kreinraum-Klassifikation; indefinite Realisierung |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07. Patch 2026-08-07: $P_{\rm fin}$ sauber; $\overline{R}_{\rm PW}=S_{\rm PW}^*$ bewiesen; „Majorante" $\times[M]$; Modulationstest $\checkmark$; Kato-Fehler korrigiert; Semibeschränktheit offen.*
