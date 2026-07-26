# NEU-220m — Gesamt-Weilform, Rigged-Operator und Randkanäle

**Katalog-ID:** NEU-220m  
**Knoten:** [O-220-1-PD5a3-total-Weil-form-rigged-operator-realization]  
**Vorgänger:** NEU-220l (Commit ddac5ff) — Weil-Quadratik ✓[K/M]  
**Revision:** rev.2 (Commit 27e7dd5 = rev.1, dort PD5a3a ✓[M]_neg)  
**Status:** ✓[K/M]_part (PD5a3a–e) / ?[O] (PD5a3f–g)

---

## Auditprotokoll rev.1 → rev.2

Commit 27e7dd5 enthielt zwei Hauptfehler in PD5a3a:

1. **Polterm falsch polarisiert:** Der off-diagonale Block $\begin{pmatrix}0&1\\1&0\end{pmatrix}$ wurde irrtümlich durch den positiven Block $\begin{pmatrix}1&0\\0&1\end{pmatrix}$ ersetzt.
2. **Beide Primterme identisch:** Durch Substitution $w = v+\log n$ folgt $B_n(a,b)=A_n(a,b)$; die hermitesche Symmetrie war damit unbewiesen und im Allgemeinen falsch.

Zusätzliche Korrekturen in PD5a3c, PD5a3d, PD5a3f (siehe unten).

---

## PD5a3a — Polarisierte Gesamtform ✓[K/M]

### Funktionale

$$
\ell_-(a) = \mathcal{M}_a(0) = \int_{\mathbb{R}} a(u)\,e^{-u/2}\,du, \qquad
\ell_+(a) = \mathcal{M}_a(1) = \int_{\mathbb{R}} a(u)\,e^{u/2}\,du.
$$

### Korrekte Gesamtform

Für $a, b \in \mathcal{D} = C_c^\infty(\mathbb{R};\mathbb{C})$, antilinear im ersten, linear im zweiten Argument:

$$
\boxed{\begin{aligned}
\mathfrak{W}(a,b) ={}&
  \overline{\ell_-(a)}\,\ell_+(b) + \overline{\ell_+(a)}\,\ell_-(b) \\
&+ \int_{\mathbb{R}} \gamma_\infty^{\mathrm{sym}}(t)\,\overline{(\mathcal{F}a)(t)}\,(\mathcal{F}b)(t)\,dt \\
&- \sum_{n\ge2} \frac{\Lambda(n)}{\sqrt{n}} \int_{\mathbb{R}} \overline{a(v)}\,b(v-\log n)\,dv \\
&- \sum_{n\ge2} \frac{\Lambda(n)}{\sqrt{n}} \int_{\mathbb{R}} \overline{a(v)}\,b(v+\log n)\,dv.
\end{aligned}}
$$

**Hermitizität:** $\mathfrak{W}(b,a) = \overline{\mathfrak{W}(a,b)}$ gilt exakt.

**Diagonale:** $\mathfrak{W}(a,a) = q_{\mathrm{pole}}(a) + q_\Gamma(a) + q_{\mathrm{fin}}(a)$ mit

$$
q_{\mathrm{pole}}(a) = 2\operatorname{Re}\bigl(\overline{\ell_-(a)}\,\ell_+(a)\bigr),
$$
$$
q_\Gamma(a) = \int_{\mathbb{R}} \gamma_\infty^{\mathrm{sym}}(t)\,|(\mathcal{F}a)(t)|^2\,dt,
$$
$$
q_{\mathrm{fin}}(a) = -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\operatorname{Re}\int_{\mathbb{R}}\overline{a(v)}\,a(v-\log n)\,dv.
$$

**Warum die rev.1-Formel falsch war:**
- Polterm $\overline{\ell_-(a)}\ell_-(b)+\overline{\ell_+(a)}\ell_+(b)$ liefert auf der Diagonalen $|\ell_-|^2+|\ell_+|^2 \ne 2\operatorname{Re}(\overline{\ell_-}\ell_+)$.
- Zweiter Primterm $\int\overline{a(v+\log n)}b(v)\,dv = \int\overline{a(w)}b(w-\log n)\,dw$ ist identisch mit dem ersten; auf der Diagonalen entsteht ein komplexwertiger Ausdruck ohne garantierte Hermitizität.

---

## PD5a3b — Lokale Endlichkeit und LF-Stetigkeit des Primterms ✓[M]

Für $\operatorname{supp}(a) \subseteq K$ kompakt:

$$
\int_{\mathbb{R}} \overline{a(v)}\,a(v\pm\log n)\,dv \ne 0
\quad\Longrightarrow\quad \log n \le \operatorname{diam}K.
$$

Daher ist $q_{\mathrm{fin}}(a)$ auf jedem $\mathcal{D}_K$ **endlich**. $q_{\mathrm{fin}}$ ist eine stetige hermitesche Form auf dem LF-Raum $C_c^\infty(\mathbb{R})$.

$$
\boxed{\text{Lokale Endlichkeit der Diagonalform}
\;\not\Rightarrow\;
\text{Konvergenz der formalen Operatorreihe auf }L^2.}
$$

### $q_{\mathrm{fin}}$ ist indefinit ✓[M]

**Negativzeuge** (reelles $\varphi \ge 0$, Trägerdurchmesser $d \in (\log 2, \log 3)$, $C = \int\varphi(v)\varphi(v-\log 2)\,dv > 0$):

$$
q_{\mathrm{fin}}(\varphi) = -\frac{2\log 2}{\sqrt{2}}\,C < 0.
$$

**Positivzeuge** ($a(v) = e^{i\pi v/\log 2}\varphi(v)$):

$$
\int\overline{a(v)}\,a(v-\log 2)\,dv = e^{-i\pi}C = -C
\quad\Longrightarrow\quad
q_{\mathrm{fin}}(a) = \frac{2\log 2}{\sqrt{2}}\,C > 0.
$$

$$
\boxed{q_{\mathrm{fin}} \text{ ist indefinit.}}
$$

---

## PD5a3c — Gammaanteil ✓[K/M]_part

### Operator- vs. Formdomäne (Korrektur gegenüber rev.1)

Für $G_\infty = \mathcal{F}^{-1}M_{\gamma_\infty^{\mathrm{sym}}}\mathcal{F}$:

$$
\mathcal{D}(G_\infty) = \{ a \in L^2 : \gamma_\infty^{\mathrm{sym}}\mathcal{F}a \in L^2 \}
\quad\text{(Operatordomäne, selbstadjungiert hier)}
$$

$$
\mathcal{Q}_\Gamma = \mathcal{D}(|G_\infty|^{1/2})
= \{ a \in L^2 : \int|\gamma_\infty^{\mathrm{sym}}(t)|\,|(\mathcal{F}a)(t)|^2\,dt < \infty \}
\quad\text{(Formdomäne)}
$$

Die in rev.1 als „Formdomäne“ bezeichnete Menge ist $\mathcal{Q}_\Gamma = \mathcal{D}(|G_\infty|^{1/2})$, nicht die Operatordomäne. Es gilt $C_c^\infty(\mathbb{R}) \subseteq \mathcal{Q}_\Gamma$.

### $q_\Gamma$ ist indefinit, aber nach unten beschränkt

$$
\gamma_\infty^{\mathrm{sym}}(t) = -\log\pi + \operatorname{Re}\psi\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right).
$$

Bei $t=0$: $\gamma_\infty^{\mathrm{sym}}(0) = -\log\pi + \psi(1/4) = -\log\pi - \gamma_E - 3\log 2 - \tfrac{\pi}{2} < 0$.

Für $|t|\to\infty$: $\gamma_\infty^{\mathrm{sym}}(t) = \log\frac{|t|}{2\pi} + O(t^{-2}) \to +\infty$.

$$
\boxed{q_\Gamma \text{ ist indefinit, aber nach unten beschränkt.}}
$$

Die Angabe „Vorzeichendefinit (zu prüfen)“ aus rev.1 ist zurückgezogen.

---

## PD5a3d — Polterm als Randform ✓[M]

### $q_{\mathrm{pole}}$ ist nicht $L^2$-stetig

Sei $0\ne\varphi\in C_c^\infty(\mathbb{R})$ reell und nichtnegativ, $a_R(u) = e^{-R/2}(\varphi(u-R)+\varphi(u+R))$.
Dann $\|a_R\|_2\to 0$, aber $\ell_\pm(a_R)\to\int\varphi(v)e^{\pm v/2}\,dv>0$, also

$$
q_{\mathrm{pole}}(a_R) \to 2\left(\int\varphi\,e^{v/2}\,dv\right)\left(\int\varphi\,e^{-v/2}\,dv\right) > 0.
$$

$$
\boxed{q_{\mathrm{pole}} \text{ besitzt keine stetige Fortsetzung auf dem ungewichteten }L^2(\mathbb{R}).}
$$

### Gewichteter Raum $L^2(\mathbb{R},e^u\,du)$ genügt nicht

$\ell_+(a)=\int a(u)e^{u/2}\,du$ ist in $L^2(w\,du)$ stetig genau dann, wenn $\int e^u/w(u)\,du<\infty$. Bei $w=e^u$: $\int 1\,du=\infty$.

$$
\boxed{\ell_+ \text{ ist auf }L^2(\mathbb{R},e^u\,du)\text{ nicht stetig.}}
$$

Beide Funktionale $\ell_\pm$ erfordern einen beidseitig exponentiell gewichteten Raum, z.B. $w_\varepsilon(u)=e^{(1+\varepsilon)|u|}$, $\varepsilon>0$. Das löst aber nur den Randterm.

---

## PD5a3e — Gesamtform auf dem Rigging $\mathcal{D}\subset L^2\subset\mathcal{D}'$ ✓[K/M]_part

### Typklassifikation

| Term | Typ | $L^2$-Status | Positivität |
|------|-----|--------------|-------------|
| $q_\Gamma$ | Selbstadjungierter Fouriermultiplikator $G_\infty$ | Operator auf $\mathcal{D}(G_\infty)$ | Indefinit, nach unten beschränkt |
| $q_{\mathrm{fin}}$ | Lokal endliche LF-Form | Kein $L^2$-Operator (gesperrt) | Indefinit |
| $q_{\mathrm{pole}}$ | Rand-/Distributionsform | Keine stetige $L^2$-Fortsetzung (gesperrt) | Indefinit |
| **$\mathfrak{W}$** | **Rigged-space-Form** | **$\mathfrak{W}:\mathcal{D}\times\mathcal{D}\to\mathbb{C}$** | **Positiv $\iff$ RH** |

$$
\boxed{\mathfrak{W}: \mathcal{D}\times\mathcal{D} \longrightarrow \mathbb{C}}
$$

als stetige hermitesche Form auf $\mathcal{D}\subset L^2(\mathbb{R})\subset\mathcal{D}'$.

---

## PD5a3f — Abschließbarkeit: revidierte Behandlung

### Zurückgezogene Definition ✓[M]_neg

Die in rev.1 verwendete Cauchy-Bedingung ist die Abschließbarkeitsprüfung für **semibeschränkte** Formen. Für eine indefinite Form ist $\mathfrak{W}(x,x)$ kein Quadrat einer Norm — positive und negative Teile können sich aufheben. Die Definition ist zurückgerollt.

### Korrekte Alternativen ?[O]

1. **Differenz zweier geschlossener positiver Formen** (falls möglich)
2. **Operator- oder Relationsgraph** eines selbstadjungierten Operators
3. **Kreinraum** mit konkret konstruierter Fundamentalsymmetrie $J = J^* = J^{-1}$
4. **Randkanalraum** $\mathcal{H}_{\mathrm{ext}} = L^2(\mathbb{R},w_\varepsilon)\oplus\mathbb{C}^2$

Keiner dieser Wege ist ohne explizite Konstruktion verfügbar. Der nächste robuste Schritt ist die lokale Fensterfamilie $(\mathcal{H}_R, W_R)_{R>0}$ — siehe NEU-220n.

---

## PD5a3g — Adelischer Intertwiner zwischen BC-Kern und Weil-Form ?[O]

### Durchbruchsziel (RH-stark)

$$
\boxed{\mathfrak{W}(a) = \langle Ja, A_X Ja\rangle_{\mathcal{H}_X},\quad A_X\ge 0,\quad \forall a\in\mathcal{D}}
$$

würde unmittelbar $\mathfrak{W}(a)\ge 0$ und damit RH liefern.

### Schwaches Zwischenziel

$\mathfrak{W}(a,b) = [Ja,\mathcal{K}Jb]_X$ für einen selbstadjungierten, nicht notwendig positiven Generator $\mathcal{K}$.

---

## Knotentabelle (rev.2)

| Teil | Inhalt | Status |
|------|--------|--------|
| PD5a3a, rev.1-Formel | Beide Polarisationsfehler | ✓[M]_neg |
| PD5a3a, korrigierte Form | Hermitesche Gesamtpolarisation | ✓[K/M] |
| PD5a3b, lokale Endlichkeit | LF-Stetigkeit | ✓[M] |
| PD5a3b, $q_{\mathrm{fin}}$ indefinit | Negativ- und Positivzeuge | ✓[M] |
| PD5a3c, Gammaoperator | Operator-/Formdomäne getrennt; $q_\Gamma$ indefinit, nach unten beschränkt | ✓[K/M]_part |
| PD5a3d, Polterm $L^2$-Audit | Keine stetige $L^2$-Fortsetzung; Gewichtungsweg $L^2(e^u)$ gesperrt | ✓[M] |
| PD5a3e, Rigged-space-Form | Typklassifikation, alle drei Kanäle indefinit | ✓[K/M]_part |
| PD5a3f, bisherige Def. | Für indefinite Form ungeeignet | ✓[M]_neg |
| PD5a3f, Alternativen | Vier Realisierungswege benannt | ?[O] |
| PD5a3g, adelischer Intertwiner | Durchbruchsziel und Zwischenziel formuliert | ?[O] (RH-stark) |

```
[O-220-1-PD5a3-total-Weil-form-rigged-operator-realization]
  → ✓[K/M]_part  (PD5a3a–e abgeschlossen, rev.2)
  → ?[O]          (PD5a3f–g offen)
  → Nächster Knoten: NEU-220n (endliche Fensteroperatoren)
```

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220l (ddac5ff) | Weil-Quadratik, Amplitudenraum, Evenisierung |
| NEU-220k (cc4345b) | Masterform |
| Bombieri (2000) | Klassische Weil-Quadratik, RH-Äquivalenz |
| Connes (1999) | Spurformel, BC-Kern |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
