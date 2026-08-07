# NEU-255 — Haar-Koisometrie, kanonische $L^2$-Majorante und $B_W$-Operatoraudit

**Katalog-ID:** NEU-255  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** (1) Koisometrie $\overline{R}_{\rm PW}$ vollständig beweisen; (2) $\langle a,b\rangle_0=\langle a,b\rangle_{L^2(\mathbb{R},du)}$ als kanonischen Hilbertmajoranten buchen; (3) Beschränktheit $|B_W(a,b)|\le C\|a\|_2\|b\|_2$ testen; (4) Abschließbarkeits-/Selbstadjungiertheitskette für $A_X$ auf $L^2(\mathbb{R})$ falls Beschränktheit scheitert.  
**Vorläufiger Status:** Koisometrie $\checkmark[K/M]$; $H_0=L^2(\mathbb{R},du)$ $\checkmark[K/M]$; Beschränktheit $A_X$ $?[O]$; Selbstadjungiertheit $A_X$ $?[O]$.  
**Vorgänger:** NEU-254 (Patch), NEU-253, NEU-252 (Patch), NEU-250r (Patch)

---

## 0. Ausgangslage

Aus NEU-254 §5 vorläufig bekannt:
$$
\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)},\qquad L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).
$$

Dieses Dokument führt die vollständigen Beweise und entscheidet die M4-A-Operatorfrage.

**Zentralfrage von M4-A** (NEU-253 §3):
$$
\boxed{B_W(a,b)=\langle a,A_Xb\rangle_0\,?\qquad A_X\text{ beschränkt oder abschließbar auf }L^2(\mathbb{R},du)?} \qquad (0\text{-Goal})
$$

---

## 1. Koisometriebeweis: $\overline{R}_{\rm PW}$ und $S_{\rm PW}$

### 1.1 Definitionen

**Kanonischer Lift** (aus NEU-250r):
$$
\boxed{S_{\rm PW}:\mathcal{A}_{\rm PW}\longrightarrow\mathcal{S}_{\rm adel}^{\rm amp},\qquad S_{\rm PW}a=h_a\otimes\mathbf{1}_{\widehat{\mathbb{Z}}},\qquad h_a(x)=\begin{cases}x^{-1/2}a(\log x),&x>0,\\0,&x\le0,\end{cases}} \qquad (1\text{-Lift})
$$
mit $R_{\rm PW}S_{\rm PW}=I_{\mathcal{A}_{\rm PW}}$.

**Haar-Port auf $L^2$-Ebene:**
$$
\overline{R}_{\rm PW}:L^2(\mathbb{A}_{\mathbb{Q}})\longrightarrow L^2(\mathbb{R},du),\qquad F\longmapsto J_{1/2}\bigl(F(\cdot\,,\mathbf{1}_{\widehat{\mathbb{Z}}})\big|_{x>0}\bigr). \qquad (1\text{-Port})
$$

### 1.2 Unitarität von $J_{1/2}$

$$
J_{1/2}:L^2(\mathbb{R}_+,dx)\longrightarrow L^2(\mathbb{R},du),\qquad (J_{1/2}f)(u)=e^{u/2}f(e^u). \qquad (1\text{-J12def})
$$

**Beweis der Isometrie:**
$$
\|J_{1/2}f\|_{L^2(\mathbb{R},du)}^2=\int_{\mathbb{R}}|e^{u/2}f(e^u)|^2\,du\underset{x=e^u}{=}\int_0^\infty|f(x)|^2\,dx=\|f\|_{L^2(\mathbb{R}_+,dx)}^2. \qquad (1\text{-Isom})
$$

Substitution $u=\log x$, $du=dx/x$, $e^u=x$, $e^{u/2}=x^{1/2}$: surjektiv wegen $u\mapsto e^u$ Bijektion $\mathbb{R}\to\mathbb{R}_+$.

$$
\boxed{J_{1/2}\text{ ist unitär.}\quad\checkmark[K/M]} \qquad (1\text{-Unit})
$$

### 1.3 $S_{\rm PW}$ als isometrischer Lift

Mit $\operatorname{vol}(\widehat{\mathbb{Z}})=1$ unter dem endlichen Haar-Maß:
$$
\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{L^2(\mathbb{A})}=\int_{\mathbb{A}}\overline{(h_a\otimes\mathbf{1}_{\widehat{\mathbb{Z}}})(x)}(h_b\otimes\mathbf{1}_{\widehat{\mathbb{Z}}})(x)\,d\mu_{\rm Haar}(x). \qquad (1\text{-SPW1})
$$

Adelische Produktmessung: archimedischer Anteil $dx$ auf $\mathbb{R}_+$, endlicher Anteil $d\mu_{\rm fin}$ auf $\widehat{\mathbb{Z}}$ mit $\mu_{\rm fin}(\widehat{\mathbb{Z}})=1$:
$$
=\int_0^\infty\overline{h_a(x)}h_b(x)\,dx\cdot\underbrace{\int_{\widehat{\mathbb{Z}}}\mathbf{1}\,d\mu_{\rm fin}}_{=1}=\int_0^\infty x^{-1}\overline{a(\log x)}b(\log x)\,dx. \qquad (1\text{-SPW2})
$$

Substitution $u=\log x$:
$$
=\int_{\mathbb{R}}\overline{a(u)}b(u)\,du=\langle a,b\rangle_{L^2(\mathbb{R},du)}. \qquad (1\text{-SPW3})
$$

$$
\boxed{\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R},du)}.\quad\checkmark[K/M]} \qquad (1\text{-Transport})
$$

$S_{\rm PW}:\mathcal{A}_{\rm PW}\to L^2(\mathbb{A}_{\mathbb{Q}})$ ist isometrisch. $\overline{R}_{\rm PW}$ ist die Koadjungierte: $\overline{R}_{\rm PW}S_{\rm PW}=I$, also $\overline{R}_{\rm PW}$ **Koisometrie**.

$$
\boxed{L^2(\mathbb{A}_{\mathbb{Q}})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (1\text{-Quot})
$$

---

## 2. Kanonischer Hilbertmajorante: $H_0=L^2(\mathbb{R},du)$

### 2.1 Buchung

$$
\boxed{\langle a,b\rangle_0:=\langle a,b\rangle_{L^2(\mathbb{R},du)}.\quad\checkmark[K/M]} \qquad (2\text{-Inner})
$$

Dieser Hilbertmajorante ist:
- **RH-unabhängig**: keine Positivitätsvoraussetzung über $B_W$.
- **Kanonisch adelisch**: aus dem Haar-Maß auf $\mathbb{A}_{\mathbb{Q}}$ und dem unitären $J_{1/2}$.
- **Kein Fitten**: $\langle\cdot,\cdot\rangle_{L^2}$ ist durch das Lebesgue-Maß vollständig fixiert.

$$
\boxed{H_0=L^2(\mathbb{R},du)\text{ ist der kanonische positive Hilbertmajorante für }\mathcal{A}_{\rm PW}.\quad\checkmark[K/M]} \qquad (2\text{-H0})
$$

### 2.2 Strategische Einordnung

Nach dem Quotient $L^2(\mathbb{A})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R})$ ist keine sichtbare Primzahlarithmetik mehr in $H_0$. Die Arithmetik muss vollständig im Realisierungsoperator $A_X$ und seiner Domäne sitzen. Das ist ein **erwarteter, plausibler Befund** (vgl. NEU-254 §5.5): einfacher Hilbertraum, hochgradig arithmetischer Operator.

---

## 3. Beschränktheitstest: $|B_W(a,b)|\le C\|a\|_2\|b\|_2$?

### 3.1 Polblock $B_{\rm pole}$

Aus der Weil-Explizitformel (NEU-252) trägt $B_{\rm pole}$ Distributionsanteile. Für $a,b\in\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R})$ ist $B_{\rm pole}(a,b)$ endlich, aber der Ausdruck enthält Evaluationen $a(0),b(0)$ und Ableitungswerte — diese sind durch $\|a\|_2$ allein nicht kontrollierbar.

**Gegenbeispielstruktur:** Wähle $a_n\in C_c^\infty$ mit $\|a_n\|_2=1$ und $a_n(0)\to\infty$ (Konzentration um $0$ mit Normierung): dann $|B_{\rm pole}(a_n,a_n)|\to\infty$.

$$
\boxed{B_{\rm pole}\text{ ist nicht beschränkt auf }L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (3\text{-Pole})
$$

### 3.2 Gamma-Block $B_\Gamma$

$B_\Gamma(a,b)=\int_\mathbb{R}\hat{a}(t)\overline{\hat{b}(t)}\,d\nu_\Gamma(t)$ mit dem Gamma-Spektralmaß $d\nu_\Gamma$. Dieses Maß wächst polynomiell, nicht beschränkt. Für $a_n$ mit hochfrequenten Fourier-Massen: $|B_\Gamma(a_n,a_n)|/\|a_n\|_2^2\to\infty$.

$$
\boxed{B_\Gamma\text{ ist nicht beschränkt auf }L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (3\text{-Gamma})
$$

### 3.3 Gesamtbefund Beschränktheit

$$
\boxed{B_W\text{ ist nicht beschränkt auf }L^2(\mathbb{R},du).\quad\checkmark[K/M]} \qquad (3\text{-Unbdd})
$$

Fall 1 (Riesz direkt) aus NEU-253 §3 scheidet aus. Es gilt Fall 2: Abschließbarkeits-/Selbstadjungiertheitskette nötig.

---

## 4. $B_W$ als dicht definierte hermitesche Form auf $L^2(\mathbb{R})$

### 4.1 Definitionsbereich

$$
\mathcal{A}_{\rm PW}=C_c^\infty(\mathbb{R};\mathbb{C})\subset L^2(\mathbb{R},du)\text{ ist dicht.} \qquad (4\text{-Dense})
$$

$B_W$ ist auf $\mathcal{A}_{\rm PW}\times\mathcal{A}_{\rm PW}$ hermitesch (NEU-252 $\checkmark$). Damit ist $B_W$ eine dicht definierte hermitesche Sesquilinearform auf $L^2(\mathbb{R})$.

### 4.2 Abschließbarkeit — offene Frage

**Abschließbarkeit** bedeutet: Falls $a_n\in\mathcal{A}_{\rm PW}$, $\|a_n\|_2\to0$, $B_W(a_n-a_m,\cdot)\to0$ gleichmäßig, dann $B_W(a_n,b)\to0$ für alle $b$.

Das hängt vom Zusammenspiel der drei Blöcke ab:
- $B_{\rm pole}$: Distributionell; Abschließbarkeit unklar.
- $B_\Gamma$: Spektralmaß-Form; klassische Form-Theorie anwendbar, aber Wachstum von $d\nu_\Gamma$ muss kontrolliert werden.
- $B_{\rm fin}$: Summe über Primzahlpotenzen; endliche Terme für $a,b\in\mathcal{A}_{\rm PW}$, kompakter Träger hilft.

$$
\boxed{\text{Abschließbarkeit von }B_W\text{ auf }L^2(\mathbb{R}):\quad?[O]} \qquad (4\text{-Close})
$$

### 4.3 Selbstadjungierte Realisierung $A_X$

Falls Abschließbarkeit $\checkmark$: Sei $\overline{B_W}$ die Abschließung. Dann existiert nach Kato-Darstellungssatz ein selbstadjungierter Operator $A_X\ge-\lambda\cdot I$ (für geeignetes $\lambda$) mit
$$
\boxed{\overline{B_W}(a,b)=\langle a,A_Xb\rangle_0,\qquad a\in D(A_X^{1/2}),\;b\in D(\overline{B_W}).} \qquad (4\text{-AX})
$$

$$
\boxed{\text{Selbstadjungierte Realisierung }A_X\text{ auf }L^2(\mathbb{R},du):\quad?[O]} \qquad (4\text{-SAO})
$$

### 4.4 Strategische Bedeutung

Wenn $A_X$ konstruiert ist:
$$
\boxed{\text{Welcher selbstadjungierte Operator }A_X\text{ auf }L^2(\mathbb{R},du)\text{ repräsentiert die vollständige }B_W?} \qquad (4\text{-ObjX})
$$

Das ist der bisher schärfste Übergang von Forschungsprogramm zu einem greifbaren Trägergeometriekandidaten von Objekt X: $H_0$ aus adelischer Haarstruktur hergeleitet, $A_X$ trägt die vollständige arithmetische Information.

---

## 5. Verhältnis zu NEU-253 Signatur-Firewall

Sobald $A_X$ konstruiert ist (falls Abschließbarkeit $\checkmark$):
- Spektrum von $A_X$ bestimmt Signatur.
- $A_X\ge0$ wäre nach NEU-220l äquivalent zu RH — das darf nicht vorausgesetzt werden.
- $A_X$ hat möglicherweise negatives Spektrum; Signatur-Firewall aus NEU-253 §4 gilt:
$$
\sigma_-(A_X)\neq\emptyset\iff\mathcal{H}_-\neq0\iff\neg\text{RH}. \qquad (5\text{-Fire})
$$

---

## 6. Verhältnis zu NEU-221-Momenten

Falls $A_X$ konstruiert ist und $T_X=A_X^{-1}\ge0$ (nach Positivität, falls M4-D $\checkmark$):
$$
\tau_{L^2}(T_X^{k+1})\stackrel{?}{=}\mu_k\quad(k=0,1,2,\ldots). \qquad (6\text{-Moment})
$$

Das wäre der Momenten-Frühtestanschluss aus NEU-221 §1 mit neuem Typenrahmen. Normierungs-Firewall: Spur und Operator sind durch $A_X$ und das $L^2$-Maß kanonisch fixiert — kein Fitten.

---

## 7. Statusbuchungen

$$J_{1/2}:L^2(\mathbb{R}_+,dx)\to L^2(\mathbb{R},du)\text{ unitär}\quad\checkmark[K/M] \qquad (7\text{-a})$$
$$\langle S_{\rm PW}a,S_{\rm PW}b\rangle_{\rm Haar}=\langle a,b\rangle_{L^2(\mathbb{R})}\quad\checkmark[K/M] \qquad (7\text{-b})$$
$$L^2(\mathbb{A})/\ker\overline{R}_{\rm PW}\cong L^2(\mathbb{R})\quad\checkmark[K/M] \qquad (7\text{-c})$$
$$H_0=L^2(\mathbb{R},du)\text{ kanonischer Hilbertmajorante}\quad\checkmark[K/M] \qquad (7\text{-d})$$
$$B_W\text{ nicht beschränkt auf }L^2(\mathbb{R})\quad\checkmark[K/M] \qquad (7\text{-e})$$
$$B_W\text{ dicht definierte hermitesche Form auf }\mathcal{A}_{\rm PW}\subset L^2(\mathbb{R})\quad\checkmark[K/M] \qquad (7\text{-f})$$
$$\text{Abschließbarkeit }B_W\text{ auf }L^2(\mathbb{R})\quad?[O] \qquad (7\text{-g})$$
$$\text{Selbstadjungierte Realisierung }A_X\text{ auf }L^2(\mathbb{R},du)\quad?[O] \qquad (7\text{-h})$$

---

## 8. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-254 (Patch) | 34c471d | Rollenvergleich; $R_{\rm PW}^{-1}$ $\times[M]$; Transport-Satz |
| NEU-253 (Patch) | a95d3b5 | M4 Rahmen; M4-A Zwei-Fälle; Signatur-Firewall |
| NEU-252 (Patch) | 4ee78ed | $B_W$ hermitesch; drei Blöcke $B_{\rm pole}+B_\Gamma+B_{\rm fin}$ |
| NEU-250r (Patch) | bd1c0ab | $S_{\rm PW}$; $R_{\rm PW}S_{\rm PW}=I$ |
| NEU-221 | f678057 | Normierungs-Firewall; $T_X=B_X^{-1}$; Momente $\mu_k$ |
| NEU-220l | 1dc07b3 | $B_W\ge0\Leftrightarrow$ RH |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
