# NEU-220l — Weil-Quadratik, Autokorrelation und Positiver Kegel

**Katalog-ID:** NEU-220l  
**Knoten:** [O-220-1-PD5a2-Weil-quadratic-autocorrelation-positivity]  
**Vorgänger:** NEU-220k (Commits 73ea17d, cc4345b) — Masterform ✓[K/M]  
**Status:** ?[O]

---

## Audit-Vorbemerkung

Der nächste Knoten beginnt **nicht** mit
$$
W_g = \sum_\rho m_\rho |h(\gamma)|^2
$$
als Definition. Das ist die RH-Spezialisierung, nicht die allgemeine Weil-Quadratik. Der NEU-220k-Testkern ist reell-gerade; die allgemeine Weil-Quadratik beginnt auf einem **komplexen Amplitudenraum**. Diese Datei behandelt die fünf atomaren Teilaufgaben PD5a2a–e.

---

## PD5a2a — Amplitudenraum, Involution und zentrierter Mellinkern

### Amplitudenraum

$$
\mathcal{A}_{\mathrm{PW}} = C_c^\infty(\mathbb{R};\mathbb{C}).
$$

Für $a \in \mathcal{A}_{\mathrm{PW}}$ sei
$$
A_a(z) = \int_{\mathbb{R}} a(u)\,e^{izu}\,du,
\qquad
\mathcal{M}_a(s) = A_a\!\left(\frac{s-\tfrac12}{i}\right)
= \int_{\mathbb{R}} a(u)\,e^{(s-\frac12)u}\,du.
$$

### Additive Involution

$$
a^\sharp(u) := \overline{a(-u)}.
$$

**Lemma:** $\mathcal{M}_{a^\sharp}(s) = \overline{\mathcal{M}_a(1-\bar s)}$.

*Beweis:*
$$
\mathcal{M}_{a^\sharp}(s)
= \int \overline{a(-u)}\,e^{(s-\frac12)u}\,du
\overset{u\mapsto -u}{=}
\int \overline{a(v)}\,e^{-(s-\frac12)v}\,dv
= \overline{\int a(v)\,e^{-(\bar s - \frac12)v}\,dv}
= \overline{\mathcal{M}_a(1-\bar s)}. \quad\square
$$

### Autokorrelation

$$
c_a := a * a^\sharp, \qquad c_a(x) = \int_{\mathbb{R}} a(v)\,\overline{a(v-x)}\,dv.
$$

**Korollar (off-axis Quadratik):**
$$
\boxed{\mathcal{M}_{c_a}(s) = \mathcal{M}_a(s)\,\overline{\mathcal{M}_a(1-\bar s)}.}
$$

Der einzelne Summand $m_\rho \mathcal{M}_a(\rho)\,\overline{\mathcal{M}_a(1-\bar\rho)}$ ist off-axis im Allgemeinen **kein Betragsquadrat**.

---

## PD5a2b — Unbedingte Weil-Quadratik

**Definition (RH-frei):**
$$
\boxed{\mathfrak{W}(a) := \sum_\rho m_\rho\, \mathcal{M}_a(\rho)\,\overline{\mathcal{M}_a(1-\bar\rho)}.}
$$

Für $\rho = \beta + i\gamma$:
- $\mathcal{M}_a(\rho) = A_a\!\left(\gamma - i(\beta-\tfrac12)\right)$
- $\mathcal{M}_a(1-\bar\rho) = A_a\!\left(\gamma + i(\beta-\tfrac12)\right)$

Erst **unter RH** gilt $1-\bar\rho = \rho$, sodass
$$
\mathfrak{W}(a) = \sum_\rho m_\rho |\mathcal{M}_a(\rho)|^2 = \sum_\rho m_\rho |A_a(\gamma)|^2 \geq 0.
$$

Das ist die korrekte Bedeutung der RH-Spezialisierung.

---

## PD5a2c — Evenisierung und Einbettung in NEU-220k

Da $c_a$ hermitesch ($c_a(-u) = \overline{c_a(u)}$), aber im Allgemeinen nicht reell-gerade, definiere:
$$
g_a(u) := \tfrac12(c_a(u) + c_a(-u)) = \operatorname{Re}\, c_a(u).
$$

Dann $g_a \in C_c^\infty(\mathbb{R};\mathbb{R})$, $g_a(-u) = g_a(u)$. Setze
$$
h_a(z) = \int_{\mathbb{R}} g_a(u)\,e^{izu}\,du, \qquad F_a(s) = h_a\!\left(\frac{s-\tfrac12}{i}\right).
$$

$F_a(1-s) = F_a(s)$ gilt, sodass **NEU-220k unmittelbar anwendbar** ist.

**Explizite Darstellung:**
$$
F_a(s) = \tfrac12\left[\mathcal{M}_a(s)\,\overline{\mathcal{M}_a(1-\bar s)}
+ \mathcal{M}_a(1-s)\,\overline{\mathcal{M}_a(\bar s)}\right].
$$

Da die Nullstellenmultimenge unter $\rho \mapsto 1-\rho$ invariant ist:
$$
\sum_\rho m_\rho F_a(\rho) = \mathfrak{W}(a).
$$

Die Evenisierung verändert die **gesamte Nullstellensumme nicht**; sie bringt den Kern nur in den geschlossenen NEU-220k-Raum.

**Auf der kritischen Linie:**
$$
h_a(t) = \tfrac12\left(|A_a(t)|^2 + |A_a(-t)|^2\right) \geq 0.
$$

---

## PD5a2d — Vollständige arithmetische Weil-Quadratik

Die NEU-220k-Masterform liefert:

$$
\boxed{\mathfrak{W}(a) = h_a(i/2) + h_a(-i/2) + 2\Lambda_\Gamma(h_a)
- 2\sum_{n\geq2} \frac{\Lambda(n)}{\sqrt{n}}\,g_a(\log n).}
$$

Mit $g_a(x) = \operatorname{Re}\int_{\mathbb{R}} a(v)\,\overline{a(v-x)}\,dv$ wird der Primzahlpotenzanteil zur echten quadratischen Korrelationsform:

$$
\boxed{-2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt{n}}\operatorname{Re}\int_{\mathbb{R}} a(v)\,\overline{a(v-\log n)}\,dv.}
$$

Wegen $\operatorname{supp}(a)$ kompakt ist die Summe **tatsächlich endlich**.

---

## PD5a2e — Exakte Übersetzung des klassischen Weil-Kriteriums

Für $f \in C_c^\infty(0,\infty;\mathbb{C})$ setze
$$
a(u) = e^{u/2}f(e^u), \qquad \text{umgekehrt: } f(x) = x^{-1/2}a(\log x).
$$

Dann
$$
\tilde f(s) = \int_0^\infty f(x)\,x^{s-1}\,dx = \mathcal{M}_a(s).
$$

Die multiplikative Involution $f^\star(x) = x^{-1}\overline{f(x^{-1})}$ entspricht exakt $a^\sharp(u) = \overline{a(-u)}$. Damit ist die klassische Weil-Quadratik (Bombieri 2000) **typgleich** mit $\mathfrak{W}(a)$.

In dieser Form gilt: **Positivität von $\mathfrak{W}$ für alle $a \in \mathcal{A}_{\mathrm{PW}}$ ist äquivalent zu RH.**

---

## PD5a2f — Trennung: hermitesche Form vs. positive GNS-Realisierung

**Bedingungslos verfügbar:**
- Die hermitesche sesquilineare Form $(a,b) \mapsto \mathfrak{W}(a,b)$ (Polarisierung)
- Der zugehörige hermitesche Kern $K(u,v) = \sum_\rho m_\rho A_a(\cdot) \overline{A_b(\cdot)}$
- Eventuell eine **indefinite** bzw. Krein-artige Vervollständigung

**Nicht bedingungslos verfügbar:**
- Ein positiver Hilbertraumquotient $\mathcal{H}_{\mathfrak{W}}$ via GNS

Denn: $\mathfrak{W}(a) \geq 0$ für alle $a$ ist gerade der RH-Inhalt. Eine positive GNS-Konstruktion aus $\mathfrak{W}$ wäre entweder
- **konditional unter RH**, oder
- **selbst bereits ein RH-Beweis**.

**Konsequenz für $X_\infty$:** Die Reihenfolge muss strikt sein:

$$
\boxed{\text{Autokorrelationskegel}
\longrightarrow \text{Weil-Quadratik}
\longrightarrow \text{RH-Positivitätsäquivalenz}
\longrightarrow \text{erst dann Hilbert-/GNS-Realisierung}.}
$$

Ein direkter Sprung von $X_\infty$ zur GNS-Konstruktion wäre zirkulär.

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|-------------|--------|--------|
| PD5a2a | $a^\sharp$, $c_a = a*a^\sharp$, $\mathcal{M}_{c_a}$ off-axis | ✓[M] |
| PD5a2b | Unbedingte Definition $\mathfrak{W}(a)$; RH-Spezialisierung | ✓[M] |
| PD5a2c | Evenisierung $g_a$, Einbettung in NEU-220k-Raum | ✓[M] |
| PD5a2d | Vollständige arithmetische Korrelationsform | ✓[M] |
| PD5a2e | Exakte Übersetzung klassisches Weil-Kriterium (Bombieri) | ✓[M] |
| PD5a2f | Trennung hermitesche Form / positive GNS-Realisierung | ✓[M] |

```
[O-220-1-PD5a2-Weil-quadratic-autocorrelation-positivity]  →  ✓[K/M]
```

---

## Nächster offener Knoten

**PD5a3:** Kann die arithmetische rechte Seite der Weil-Quadratik
$$
\mathfrak{W}(a) = h_a(i/2)+h_a(-i/2) + 2\Lambda_\Gamma(h_a)
- 2\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt{n}}\,g_a(\log n)
$$
aus der **adelisch-operatorischen Architektur** von $X_\infty$ heraus als positive Form erzwungen werden — ohne RH als Prämisse einzusetzen?

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220k (cc4345b) | Masterform $\Lambda_{\mathrm{zeros}}(h) = F_h(0)+F_h(1)+2\Lambda_\Gamma(h)-2I_{\mathrm{fin}}(h)$ |
| Bombieri (2000), Weil explicit formula | Klassische Weil-Quadratik und RH-Äquivalenz |
| Connes (1999), Trace formula | Spurformel-Interpretation von $\mathfrak{W}$ |
| NEU-220j (de04247) | $X_\infty$-Architektur, archimedische Seite |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
