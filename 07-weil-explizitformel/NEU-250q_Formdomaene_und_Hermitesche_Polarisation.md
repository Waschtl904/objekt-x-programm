# NEU-250q — Direktaudit: Formdomäne und hermitesche Polarisation

**Katalog-ID:** NEU-250q  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Auftrag:** Vier Aufgaben: (1) Gauß-Gegenbeweis vollständig ins Repo; (2) Konvergenzbereich von $B_{\rm fin}$ auf $\mathcal{S}_\infty$ bestimmen; (3) Q-A/B/C-Entscheidung; (4) strategische Konsequenz für M3.  
**Gesamtausgang:** Formdomänen-Engpass bestätigt; Q-A vorrangig; M3-Freigabe erst nach Q-A-Prüfung.  
**Vorgänger:** NEU-250m (M2-Patch), NEU-250p ($J_{1/2}$-Kette $\checkmark$), NEU-220l (Weil-Quadratik)

---

## 0. Der neue Engpass in einem Satz

$$
\boxed{J_{1/2}P_{\rm Haar}:\mathcal{S}(\mathbb{A}_\mathbb{Q})\to\mathcal{S}_\infty\text{ typkorrekt, aber }\mathcal{S}_\infty\not\subset\operatorname{Dom}(B_{\rm fin}).} \qquad (0\text{-Gap})
$$

---

## 1. Gauß-Gegenbeweis (vollständig)

**Testelement:**
$$
F(x_\infty,x_{\rm fin})=e^{-x_\infty^2}\mathbf{1}_{\hat{\mathbb{Z}}}(x_{\rm fin}). \qquad (1\text{-Test})
$$

**Kette $J_{1/2}\circ P_{\rm Haar}$:**
$$
P_{\rm Haar}F(x)=e^{-x^2},\qquad
a(y):=(\Phi J_{1/2}P_{\rm Haar}F)(y)=e^{y/2}e^{-e^{2y}}\in\mathcal{S}_\infty. \qquad (1\text{-Image})
$$

**Autokorrelation exakt:**
$$
g_a(t)=\int_{\mathbb{R}}a(v)\overline{a(v-t)}\,dv
=\frac{\sqrt{\pi}}{2}\frac{e^{-t/2}}{\sqrt{1+e^{-2t}}}\qquad(t>0). \qquad (1\text{-Autocorr})
$$

*Herleitung:* Substitution $u=e^v$, $w=e^{v-t}=e^{-t}u$:
$$
g_a(t)=\int_0^\infty u^{1/2}e^{-u^2}\cdot(e^{-t}u)^{1/2}e^{-e^{-2t}u^2}\,\frac{du}{u}
=e^{-t/2}\int_0^\infty e^{-(1+e^{-2t})u^2}\,du
=\frac{\sqrt{\pi}}{2}\frac{e^{-t/2}}{\sqrt{1+e^{-2t}}}.
$$

**Wert bei $t=\log n$:**
$$
g_a(\log n)=\frac{\sqrt{\pi}}{2}\frac{n^{-1/2}}{\sqrt{1+n^{-2}}}. \qquad (1\text{-Value})
$$

**Primterm mit $B_{\rm fin}$ (NEU-250m M2.3):**
$$
B_{\rm fin}(a,a)=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,g_a(\log n)
=-\sqrt{\pi}\sum_{n\ge2}\frac{\Lambda(n)}{n\sqrt{1+n^{-2}}}. \qquad (1\text{-Sum})
$$

**Divergenz:**
$$
\frac{\Lambda(n)}{n\sqrt{1+n^{-2}}}\sim\frac{\Lambda(n)}{n}\qquad(n\to\infty),
\qquad\sum_{n\ge2}\frac{\Lambda(n)}{n}=+\infty. \qquad (1\text{-Div})
$$

$$
\boxed{B_{\rm fin}(a,a)=-\infty\text{ für }a=J_{1/2}P_{\rm Haar}F.\quad B_{\rm fin}\text{ nicht auf ganz }\mathcal{S}_\infty\text{ definiert.}} \qquad (1\text{-NoGo})
$$

---

## 2. Konvergenzbereich von $B_{\rm fin}$ auf $\mathcal{S}_\infty$

$B_{\rm fin}(a,a)$ konvergiert genau dann absolut, wenn
$$
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\,|g_a(\log n)|<\infty. \qquad (2\text{-Conv})
$$

Da $\Lambda(n)/\sqrt{n}\sim (\log p)/\sqrt{p}$ auf Primzahlpotenzen und $\sim 0$ sonst, ist (2-Conv) äquivalent zu:
$$
\sum_p\frac{\log p}{\sqrt{p}}\,|g_a(\log p)|<\infty. \qquad (2\text{-Conv-Primes})
$$

**Hinreichende Bedingung:** Falls $|g_a(t)|\le C\,e^{-(1/2+\varepsilon)t}$ für ein $\varepsilon>0$ und alle $t\ge1$, dann
$$
\sum_p\frac{\log p}{\sqrt{p}}|g_a(\log p)|\le C\sum_p\frac{\log p}{p^{1+\varepsilon}}<\infty.
$$

Der Paley-Wiener-Unterraum $\mathcal{S}_{\infty,W}=\Phi^{-1}(C_c^\infty(\mathbb{R};\mathbb{R})_{\rm even})\subset\mathcal{S}_\infty$ erfüllt diese Bedingung: für kompakt getragenes $\Phi a$ ist $g_a$ schneller als jedes $e^{-ct}$.

$$
\boxed{\operatorname{Dom}(B_{\rm fin})\supset\mathcal{S}_{\infty,W},\quad\operatorname{Dom}(B_{\rm fin})\not\supset\mathcal{S}_\infty.} \qquad (2\text{-Dom})
$$

---

## 3. Q-A / Q-B / Q-C: Drei Optionen

### Q-A — Kleinerer adelischer Unterraum

**Idee:** Statt ganz $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ einen Unterraum $\mathcal{S}_{\rm adel}^W$ wählen, dessen Bild unter $J_{1/2}\circ P_{\rm Haar}$ in $\mathcal{S}_{\infty,W}$ oder zumindest im Konvergenzbereich von $B_{\rm fin}$ liegt.

**Natürlicher Kandidat:** Elemente $F\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$, für die $P_{\rm Haar}F$ kompakten Träger hat (d.h.\ $P_{\rm Haar}F\in C_c^\infty(\mathbb{R})$). Dann landet $J_{1/2}P_{\rm Haar}F$ in $\mathcal{S}_{\infty,W}$, und $B_{\rm fin}$ konvergiert.

**Offen:** Ist dieser Unterraum groß genug (dicht, separierend)? Entsteht er kanonisch aus der adelischen Struktur?

$$
\boxed{\text{Q-A: Unterraum }\mathcal{S}_{\rm adel}^W:=\{F\in\mathcal{S}(\mathbb{A}_\mathbb{Q}):P_{\rm Haar}F\in C_c^\infty(\mathbb{R})\}.} \qquad (3\text{-QA})
$$

### Q-B — Regularisierung von $B_{\rm fin}$ auf $\mathcal{S}_\infty$

**Idee:** Die Partialsumme $B_{\rm fin}^N(a,b):=-2\sum_{n=2}^{N}\frac{\Lambda(n)}{\sqrt{n}}g_{a,b}(\log n)$ divergiert für $N\to\infty$ in allgemeiner Lage. Eine Regularisierung könnte z.B.\ über Zeta-Regularisierung $\sum_n\Lambda(n)n^{-1-s}$ bei $s\to0$ oder über einen Abschneidekern $\phi_T(n)$ erfolgen.

**Nachteil:** Die Regularisierung müsste zur Weil-Explizitformel kompatibel sein. Das ist eine nicht-triviale Bedingung.

$$
\boxed{\text{Q-B: }B_{\rm fin}^{\rm reg}\text{ via Zeta-/Abschneidungsregularisierung — offen, nicht‑trivial.}} \qquad (3\text{-QB})
$$

### Q-C — $J_{1/2}\circ P_{\rm Haar}$ falscher Port

**Idee:** Der Gauß-Gegenbeweis zeigt, dass das Bild von $J_{1/2}\circ P_{\rm Haar}$ zu groß ist. Vielleicht ist der richtige adelische Port einer, der direkt in $\mathcal{S}_{\infty,W}$ landet — z.B.\ durch Wahl eines anderen endlichen Vektors $\phi_{\rm fin}^0\in\mathcal{S}(\mathbb{A}_{\mathbb{Q},\rm fin})$ mit Kompaktheit-erzwingender Eigenschaft.

**Nachteil:** Das würde den Kanonizitätsbefund von NEU-250p ($\mathbf{1}_{\hat{\mathbb{Z}}}$ ist kanonisch) aufgeben.

$$
\boxed{\text{Q-C: Alternativer Port mit Kompaktheits-Bedingung — offen; Kanonizitätsverlust.}} \qquad (3\text{-QC})
$$

---

## 4. Entscheidung: Vorrangige Option

$$
\boxed{\text{Q-A vorrangig: }
\mathcal{S}_{\rm adel}^W\text{ ist der natürlichste kleinste Unterraum, kanonisch und ohne Regularisierung.}} \qquad (4\text{-Decision})
$$

**Begründung:**
- Q-A braucht keine Regularisierungstheorie (Q-B) und keinen Kanonizitätsverlust (Q-C).
- $\mathcal{S}_{\rm adel}^W$ ist durch eine natürliche Kompaktheits-Bedingung auf der additiven Schwartz-Ebene definiert.
- Die Kette bleibt:
$$
\mathcal{S}_{\rm adel}^W\xrightarrow{P_{\rm Haar}}C_c^\infty(\mathbb{R})\xrightarrow{J_{1/2}}\mathcal{S}_{\infty,W}\xrightarrow{\mathcal{M}_\infty}\mathcal{W}. \qquad (4\text{-Chain})
$$
- Diese Kette ist vollständig typkorrekt und $B_{\rm fin}$ konvergiert.
- Offen bleibt: Ist $\mathcal{S}_{\rm adel}^W$ groß genug? $\to$ nächster Knoten.

---

## 5. Strategische Konsequenz

Der Befund ist kein Rückschritt, sondern eine Präzisierung:

$$
\boxed{\begin{aligned}
&\text{Die natürliche adelische Quelle }\mathcal{S}(\mathbb{A}_\mathbb{Q})\text{ ist größer als der bisherige Weil-Testbereich.}\\
&\text{Der selbstduale Unterraum }\mathcal{S}_{\rm adel}^W\text{ ist der Kandidat für die globale Formdomäne.}\\
&\text{Ob dieser Unterraum die richtige Größe für Objekt X hat, ist die nächste Frage.}
\end{aligned}} \qquad (5\text{-Strat})
$$

M3 (Gram-Geometrie) wird erst nach Bestätigung von Q-A freigegeben.

---

## 6. Statusbuchungen

$$
g_{a,b}(t)=\tfrac12(\langle a,U_tb\rangle+\langle U_ta,b\rangle)\quad\checkmark[K/M]\qquad(\text{NEU-250m M2-Patch}) \qquad (6\text{-a})
$$

$$
B_{\rm fin}(a,b)=-2\sum_n\frac{\Lambda(n)}{\sqrt{n}}g_{a,b}(\log n)\quad\checkmark[K/M] \qquad (6\text{-b})
$$

$$
\mathcal{S}_\infty\not\subset\operatorname{Dom}(B_{\rm fin})\quad\checkmark[K/M]\qquad(\text{Gauß-Gegenbeweis}) \qquad (6\text{-c})
$$

$$
\mathcal{S}_{\infty,W}\subset\operatorname{Dom}(B_{\rm fin})\quad\checkmark[K/M] \qquad (6\text{-d})
$$

$$
\mathcal{S}_{\rm adel}^W:=\{F\in\mathcal{S}(\mathbb{A}_\mathbb{Q}):P_{\rm Haar}F\in C_c^\infty(\mathbb{R})\}\quad?[O]\quad\to\text{Größe/Kanonizität} \qquad (6\text{-e})
$$

$$
\text{M3 Freigabe}\quad?[O]\quad\to\text{nach Q-A-Bestätigung} \qquad (6\text{-f})
$$

---

## Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-250m | ecc1c3b | M2-Patch; $g_{a,b}$, $B_{\rm fin}$, Domain-Warnung |
| NEU-250p | 56ba1f7 | $J_{1/2}$-Kette $\checkmark$; Weil-Selbstdualität |
| NEU-220l | 1dc07b3 | Weil-Quadratik, $-2$-Vorfaktor, $\mathcal{A}_{\rm PW}$-Domain |
| NEU-220j | 41e28cf | $\mathcal{S}_{\infty,W}$, $\mathcal{W}$, Paley-Wiener |
| NEU-245c | 1ef32ab | $\mathcal{S}_{\rm adel}$ $?[O]$ |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt 2026-08-07.*
