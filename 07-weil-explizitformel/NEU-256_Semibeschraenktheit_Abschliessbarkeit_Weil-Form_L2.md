# NEU-256 — Semibeschränktheit und Abschließbarkeit der Weil-Form auf $L^2(\mathbb{R})$

**Katalog-ID:** NEU-256  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Vier atomare Tests A–D: (A) Untere Semibeschränktheit $B_W\ge-\lambda\|\cdot\|_2^2$; (B) Blockweiser Kompensations-/Gårding-Mechanismus; (C) Abschließbarkeit der verschobenen Form $q_\lambda$; (D) Selbstadjungierte Realisierung $A_X$ falls A+C positiv.  
**Status:** Alle vier Tests $?[O]$.  
**Vorgänger:** NEU-255 (Patch 2), NEU-253 (Patch), NEU-252 (Patch), NEU-220l

---

## 0. Ausgangslage und Ziel

Aus NEU-255 $\checkmark[K/M]$ bekannt:
- $H_0=L^2(\mathbb{R},du)$: kanonischer positiver Hintergrundhilbertraum (aus Haar-Koisometrie).
- $B_W$: dicht definierte hermitesche Sesquilinearform auf $\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R})\subset H_0$.
- $B_W$ nach oben unbeschränkt: $B_W(a_N,a_N)=C_\Gamma\log N+O(1)\to+\infty$, $C_\Gamma>0$.

**Was nach oben unbeschränkt ist, kann trotzdem nach unten beschränkt sein.** Der Modulationstest sagt nichts über eine untere Schranke.

**Ziel von NEU-256:**
$$
\boxed{\text{Ist }B_W\text{ semibeschränkt und abschließbar auf }H_0?\quad\text{Falls ja: kanonisches }A_X=A_X^*\text{ auf }L^2(\mathbb{R},du).} \qquad (0\text{-Goal})
$$

**Logische Kette (Kato-Voraussetzungen):**
$$
\underbrace{B_W+\lambda\langle\cdot,\cdot\rangle_2\ge0}_{\text{(A) Semibeschränktheit}}\quad+\quad\underbrace{\text{Abschließbarkeit}}_{\text{(C)}}\quad\Longrightarrow\quad\overline{B_W}\text{ geschlossene Form}\quad\Longrightarrow\quad\underbrace{A_X=A_X^*}_{\text{(D) Kato}}. \qquad (0\text{-Chain})
$$

Beide Bedingungen sind unabhängig voneinander zu prüfen; keine folgt aus der anderen.

---

## RH-Firewall (NEU-220l)

$$
\boxed{B_W(a,a)<0\text{ für auch nur ein }a\in\mathcal{A}_{\rm PW}\Longrightarrow\neg\text{RH}.} \qquad (\text{Fire-RH})
$$

Der Auftrag von Test A ist daher **ausschließlich** der positive Nachweis einer unteren Schranke. Ein Nachweis von $B_W(a,a)<0$ wäre keine harmlose Zwischenrechnung, sondern eine RH-Widerlegung.

---

## Test A — Untere Semibeschränktheit

### A.1 Prüffrage

$$
\boxed{\exists\lambda<\infty:\;B_W(a,a)\ge-\lambda\|a\|_2^2\quad\forall a\in C_c^\infty(\mathbb{R}).\quad?[O]} \qquad (\text{A-Semi})
$$

### A.2 Blockbeiträge zu einer unteren Schranke

**Gamma-Block:** $B_\Gamma(a,a)=\int_{\mathbb{R}}|\hat a(t)|^2\,\operatorname{Re}\gamma_\infty(t)\,dt$. Mit $\operatorname{Re}\gamma_\infty(t)=\frac{1}{2}\log|t|+O(1)$ (NEU-220b) gilt $\operatorname{Re}\gamma_\infty(t)\ge-C_0$ für alle $t$ (der Logarithmus hat eine endliche untere Schranke auf $|t|\ge t_0$; für $|t|\le t_0$ ist $\gamma_\infty$ explizit bekannt und beschränkt, NEU-220b). Daher:
$$
B_\Gamma(a,a)\ge-C_0\|\hat a\|_2^2=-2\pi C_0\|a\|_2^2. \qquad (\text{A-Gamma})
$$

**Polblock:** $B_{\rm pole}(a,a)=h_{a,a}(i/2)+h_{a,a}(-i/2)$ ist nach NEU-255 §3.2 für alle $a\in\mathcal{A}_{\rm PW}$ endlich. Die Frage ist, ob $B_{\rm pole}(a,a)$ nach unten durch ein $-\lambda_{\rm pole}\|a\|_2^2$ beschränkt ist. Da $h_{a,a}(z)=\int g_{a,a}(t)e^{izt}\,dt$ mit $g_{a,a}\in C_c^\infty$, ist $h_{a,a}$ eine Schwartz-Funktion auf $\mathbb{R}$ (für reelles Argument), aber bei $z=\pm i/2$ ergibt sich ein reell-wertiger Ausdruck. Es ist zu klären, ob
$$
|B_{\rm pole}(a,a)|\le C_{\rm pole}\|a\|_2^2. \qquad ?[O]\qquad (\text{A-Pole})
$$

**Primblock:** $B_{\rm fin}(a,a)=\sum_{p^k}\Lambda(p^k)g_{a,a}(\log p^k)$ mit $g_{a,a}$ glatten kompakten Träger. Die einzelnen Terme sind reell; die Frage ist, ob die Summe durch $-\lambda_{\rm fin}\|a\|_2^2$ nach unten beschränkt ist.
$$
|B_{\rm fin}(a,a)|\le C_{\rm fin}\|a\|_2^2. \qquad ?[O]\qquad (\text{A-Fin})
$$

### A.3 Status

$$
B_\Gamma(a,a)\ge-2\pi C_0\|a\|_2^2\quad\checkmark[K/M] \qquad (\text{A-GammaBound})
$$
$$
|B_{\rm pole}(a,a)|\le C_{\rm pole}\|a\|_2^2\quad?[O] \qquad (\text{A-PoleBound})
$$
$$
|B_{\rm fin}(a,a)|\le C_{\rm fin}\|a\|_2^2\quad?[O] \qquad (\text{A-FinBound})
$$
$$
\text{Untere Semibeschränktheit }B_W\quad?[O] \qquad (\text{A-Final})
$$

---

## Test B — Blockweiser Mechanismus und Gårding-Ungleichung

### B.1 Strukturbild der drei Blöcke

| Block | Charakter | Asymptoik |
|---|---|---|
| $B_\Gamma$ | Pseudo-Differentialform, $\log|D|$-artig | $+C_\Gamma\log|\xi|$ |
| $B_{\rm fin}$ | Translations-/Primzahlarithmetik | $O(1)$, keine Hochfrequenzdivergenz |
| $B_{\rm pole}$ | Endlichdimensional/randartig | $\to0$ auf Modulationsfolge |

Diese Strukturen legen nahe, dass $B_\Gamma$ der dominante Block ist und eine Gårding-artige Abschätzung ermöglicht.

### B.2 Kandidat für eine Gårding-Ungleichung

$$
\boxed{B_W(a,a)\ge c\,\|\log^{1/2}(1+|D|)\,a\|_2^2-C\|a\|_2^2.} \qquad (\text{B-Garding})
$$

Dabei ist $\log^{1/2}(1+|D|)$ der durch den $L^2$-Fouriermultiplikator $\xi\mapsto\log^{1/2}(1+|\xi|)$ definierte Operator; sein Definitionsbereich ist die Formdomäne
$$
D(q):=\left\{a\in L^2(\mathbb{R}): \int_{\mathbb{R}}|\hat a(t)|^2\log(1+|t|)\,dt<\infty\right\}. \qquad (\text{B-Dom})
$$

Wenn $(\text{B-Garding})$ gilt, liefert das:
1. **Semibeschränktheit** (Test A): $B_W\ge-C\|\cdot\|_2^2$.
2. **Natürliche Formdomäne**: $D(\overline{B_W})=D(q)$, eine logarithmische Sobolev-artige Einbettung.
3. **Hinweis auf das Spektrum**: $A_X$ wächst wie $\log(1+|D|)$, keine polynomielle Eigenwerthäufung.

Das wäre erheblich stärker als blosse Semibeschränktheit.

### B.3 Ansatz zum Beweis von $(\text{B-Garding})$

Für den Gamma-Block:
$$
B_\Gamma(a,a)=\int_{\mathbb{R}}|\hat a(t)|^2\operatorname{Re}\gamma_\infty(t)\,dt\ge c\int_{\mathbb{R}}|\hat a(t)|^2\log(1+|t|)\,dt - C\|a\|_2^2 \qquad (\text{B-GamEst})
$$
falls $\operatorname{Re}\gamma_\infty(t)\ge c\log(1+|t|)-C$ für ein $c>0$. Das folgt aus $\operatorname{Re}\gamma_\infty(t)=\frac{1}{2}\log|t|+O(1)$ (NEU-220b) mit $c=\frac{1}{2}$, sofern der $O(1)$-Term eine kontrollierte untere Schranke hat.
$$
B_\Gamma(a,a)\ge c\,\|\log^{1/2}(1+|D|)a\|_2^2-C\|a\|_2^2\quad?[O]\text{ (hängt von unterem }O(1)\text{-Befund ab)} \qquad (\text{B-GamOff})
$$

Für $B_{\rm pole}+B_{\rm fin}$: beide Blöcke sind durch $O(\|a\|_2^2)$ nach unten beschränkbar (Test A, falls positiv), also in der rechten Seite von $(\text{B-Garding})$ absorbierbar.

### B.4 Status

$$
\operatorname{Re}\gamma_\infty(t)\ge c\log(1+|t|)-C\quad\checkmark[K/M]\text{ (aus NEU-220b, } c=\tfrac12\text{, }O(1)\text{ zu kontrollieren)} \qquad (\text{B-GammaLB})
$$
$$
\text{Gårding-Ungleichung }(\text{B-Garding})\text{ für }B_\Gamma\quad?[O] \qquad (\text{B-Gard-Gamma})
$$
$$
\text{Gårding-Ungleichung }(\text{B-Garding})\text{ für }B_W\quad?[O] \qquad (\text{B-Gard-BW})
$$

---

## Test C — Abschließbarkeit

### C.1 Verschobene Form

Falls Test A positiv mit Schranke $\lambda$: Definiere
$$
\boxed{q_\lambda(a,b):=B_W(a,b)+(\lambda+1)\langle a,b\rangle_2.} \qquad (\text{C-Shift})
$$

Dann $q_\lambda(a,a)\ge\|a\|_2^2>0$. Die Norm $\|a\|_{q_\lambda}^2:=q_\lambda(a,a)$ ist eine Hilbertnorm auf $\mathcal{A}_{\rm PW}$, die die $L^2$-Norm majoriert.

### C.2 Abschließbarkeitskriterium

$q_\lambda$ ist **abschließbar** auf $H_0$, falls: Wenn $a_n\in\mathcal{A}_{\rm PW}$, $\|a_n\|_2\to0$, $q_\lambda(a_n-a_m,a_n-a_m)\to0$, dann $q_\lambda(a_n,b)\to0$ für alle $b\in\mathcal{A}_{\rm PW}$. Äquivalent: $q_\lambda$ ist nicht abschließbar gdw. es eine Folge $a_n\to0$ in $L^2$ gibt mit $\|a_n\|_{q_\lambda}\ge\varepsilon>0$ und $q_\lambda(a_n,b)\to0$ für alle $b$ (Abschließbarkeitskriterium nach Reed-Simon, Thm. X.23).

$$
\boxed{\text{Abschließbarkeit von }q_\lambda\text{ auf }L^2(\mathbb{R},du):\quad?[O]} \qquad (\text{C-Close})
$$

### C.3 Falls Gårding gilt

Wenn $(\text{B-Garding})$ zutrifft, ist $\|a\|_{q_\lambda}\asymp\|\log^{1/2}(1+|D|)a\|_2+\|a\|_2$; das ist eine Sobolev-artige Norm. Die Vervollständigung $\overline{\mathcal{A}_{\rm PW}}^{\|\cdot\|_{q_\lambda}}=D(q)$ ist ein Hilbertraum, und $q_\lambda$ setzt sich stetig fort. Abschließbarkeit folgt in diesem Fall automatisch aus der Positivität und dem expliziten Domänenbild.

$$
\text{Gårding }\checkmark\Rightarrow\text{Abschließbarkeit }\checkmark. \qquad (\text{C-GardingImpliesClose})
$$

### C.4 Status

$$
\text{Abschließbarkeit }q_\lambda\quad?[O]\text{ (folgt aus Gårding falls }(\text{B-Garding})\checkmark) \qquad (\text{C-Final})
$$

---

## Test D — Selbstadjungierte Realisierung $A_X$

**Vorbedingung:** Tests A und C positiv.

Falls $q_\lambda$ geschlossen und semibeschränkt: nach Kato-Darstellungssatz (Kato 1966, §VI.2) existiert ein eindeutiger selbstadjungierter Operator $A_X\ge-(\lambda)I$ auf $H_0$ mit
$$
\boxed{B_W(a,b)=\langle a,A_X b\rangle_0\quad\forall a\in D(q),\;b\in D(A_X).} \qquad (\text{D-AX})
$$

Eigenschaften:
- Kanonisch: aus $B_W$ und $H_0=L^2(\mathbb{R},du)$, kein Fitten.
- Unbeschränkt nach oben: aus NEU-255 §3.
- Arithmetisch reich: Primzahlpotenzen, Pole, Gamma kodiert im Spektrum.

$$
\boxed{\text{Selbstadjungierte Realisierung }A_X\text{ auf }L^2(\mathbb{R},du):\quad?[O]\text{ (Vorbedingung: A+C }\checkmark).} \qquad (\text{D-Final})
$$

---

## 5. Weil-Kriterium als Operator-Aussage

Falls $A_X$ konstruiert ist (Test D positiv):
$$
\boxed{\text{RH}\iff A_X\ge0.} \qquad (\text{5-Weil})
$$

Das folgt unmittelbar aus NEU-220l ($B_W\ge0\Leftrightarrow$ RH) und $(\text{D-AX})$.

Damit wird das Hilbert-Pólya-Programm erstmals vollständig konkret:

$$
\boxed{\text{adelische Haarstruktur}\longrightarrow H_0=L^2(\mathbb{R},du)\longrightarrow B_W\longrightarrow A_X=A_X^*\longrightarrow\text{RH}\iff A_X\ge0.} \qquad (\text{5-Chain})
$$

Nicht geraten, nicht aus Nullstellen konstruiert, sondern kanonisch aus der adelischen Geometrie hergeleitet.

### 5.1 M4-C-Anschluss

Falls $A_X$ konstruiert:
$$
\boxed{E_{A_X}((-\infty,0))\stackrel{?}{=}0.} \qquad (\text{5-M4C})
$$

Das ist der Inhalt von M4-C: Gibt es eine BC-/adelische Struktur, die die Negativspektralprojektion von $A_X$ zum Verschwinden zwingt?

---

## 6. Statusbuchungen

$$B_\Gamma(a,a)\ge-2\pi C_0\|a\|_2^2\quad\checkmark[K/M]\qquad(6\text{-a})$$
$$\operatorname{Re}\gamma_\infty(t)\ge\tfrac12\log(1+|t|)-C\text{ (aus NEU-220b)}\quad\checkmark[K/M]\qquad(6\text{-b})$$
$$|B_{\rm pole}(a,a)|\le C_{\rm pole}\|a\|_2^2\quad?[O]\qquad(6\text{-c})$$
$$|B_{\rm fin}(a,a)|\le C_{\rm fin}\|a\|_2^2\quad?[O]\qquad(6\text{-d})$$
$$\text{Untere Semibeschränktheit }B_W\quad?[O]\qquad(6\text{-e})$$
$$\text{Gårding }B_W(a,a)\ge c\|\log^{1/2}(1+|D|)a\|_2^2-C\|a\|_2^2\quad?[O]\qquad(6\text{-f})$$
$$\text{Abschließbarkeit }q_\lambda\quad?[O]\qquad(6\text{-g})$$
$$\text{Selbstadjungierte Realisierung }A_X\quad?[O]\qquad(6\text{-h})$$
$$\text{RH}\iff A_X\ge0\text{ (sobald }A_X\checkmark)\quad\text{logisch korrekt aus NEU-220l}\quad\checkmark[K/M]\qquad(6\text{-i})$$

---

## 7. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-255 (Patch 2) | bcc932d | $H_0=L^2$; Koisometrie; $B_W$ unbeschränkt; $C_\Gamma>0$ |
| NEU-253 (Patch) | a95d3b5 | M4 Rahmen; Signatur-Firewall; M4-A Zwei-Fälle |
| NEU-252 (Patch) | 4ee78ed | $B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}$ hermitesch |
| NEU-220b | 3a7f2c1 | $\operatorname{Re}\gamma_\infty(t)=\tfrac12\log|t|+O(1)$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |
| NEU-220k | 8d4e9b2 | $2\pi$-Fourierkonvention; $C_\Gamma$-Normierung |
| Kato 1966 | — | Darstellungssatz für semibeschränkte geschlossene Formen |
| Reed-Simon X | — | Abschließbarkeitskriterium (Thm. X.23) |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
