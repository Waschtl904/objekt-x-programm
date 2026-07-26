# NEU-220k — Xi-Masterkontur: Vorzeichen, Faktor 2 und Polbuchhaltung

**Katalog-ID:** NEU-220k (Korrekturblatt zur Vorgängerversion)  
**Knoten:** [O-220-1-PD5a1b-xi-master-sign-factor2]  
**Vorgänger:** NEU-220j (Commit de04247), NEU-220k v1 (Commit 73ea17d)  
**Status:** ✓[M]_part → ✓[K/M]

---

## Revidierter Gesamtstatus (Audit-Ergebnis)

NEU-220j ist ein echter Durchbruch: der fehlerhafte Grenzübergang $\sigma \searrow \tfrac12$ aus NEU-220i wurde durch einen festen holomorphen Kern ersetzt. Die ersten fünf Aufgaben sind korrekt.

Vor dem vollständigen **✓[K/M]** muss jedoch die Masteridentität mit expliziten Vorzeichen und dem Faktor $2$ im Repository fixiert sein. Dieses Blatt schließt genau diesen Knoten.

---

## 1. Paley-Wiener-Teil ✓[M]

Für $g \in C_c^\infty(\mathbb{R})$ mit $\operatorname{supp} g \subseteq [-R,R]$ gilt

$$
|h(z)| \leq \|g\|_{L^1}\,e^{R|\operatorname{Im}z|},
$$

und durch $N$-malige partielle Integration für jedes $A, N \geq 0$:

$$
\sup_{|\operatorname{Im}z| \leq A} (1+|z|)^N |h(z)| < \infty.
$$

Der entscheidende Identitätsblock:

$$
F_h(s) = h\!\left(\frac{s-\tfrac12}{i}\right)
= \int_{\mathbb{R}} g(u)\,e^{(s-\frac12)u}\,du.
$$

Daraus folgen unmittelbar:
- $F_h\!\left(\tfrac12+it\right) = h(t)$
- $F_h(1-s) = F_h(s)$ für gerades $g$
- $F_h(\bar s) = \overline{F_h(s)}$ für reelles $g$
- Off-axis: $\rho = \beta+i\gamma \Rightarrow F_h(\rho) = h\!\left(\gamma - i(\beta-\tfrac12)\right)$ — **kein RH erforderlich**.

---

## 2. σ-Unabhängigkeit von $I_{\mathrm{fin},\sigma}$ ✓[M]

Mit $a = \sigma - \tfrac12$:

$$
I_{\mathrm{fin},\sigma}(h) = \frac{1}{2\pi}\int_{\mathbb{R}} -\frac{\zeta'}{\zeta}(\sigma+it)\,h(t-ia)\,dt.
$$

Da $h(t-ia) = \int g(u)\,e^{itu}\,e^{au}\,du$, ergibt die Fourier-Auswertung an $x = \log n$:

$$
n^{-\sigma}\,e^{(\sigma-\frac12)\log n} = n^{-1/2},
$$

also

$$
\boxed{I_{\mathrm{fin},\sigma}(h) = \sum_{n\geq 2}\frac{\Lambda(n)}{\sqrt{n}}\,g(\log n).}
$$

Da $g$ kompakten Träger hat, sind nur endlich viele $n$ beteiligt. Kein Term $g(-\log n)$ tritt auf; die symmetrische Primform entsteht erst durch den Faktor $2$ (siehe §5).

---

## 3. Absolute Konvergenz der Nullstellensumme ✓[M]

Für $0 < \beta < 1$ liegt $\operatorname{Im}\!\left(\frac{\rho-\frac12}{i}\right) = -(\beta-\tfrac12) \in [-\tfrac12, \tfrac12]$. Der Streifenabfall liefert

$$
|F_h(\rho)| \leq C_N(1+|\gamma|)^{-N}
$$

für jedes $N$. Nach Titchmarsh: $N(T+1)-N(T) = O(\log T)$. Folglich

$$
\sum_\rho m_\rho |F_h(\rho)| \ll \sum_{k\geq 1}\frac{\log(k+2)}{(1+k)^N} < \infty \qquad (N > 2). \quad \checkmark
$$

---

## 4. Horizontale Randintegrale → 0 ✓[M]

Wähle $T_j \to \infty$ mit Abstand $\geq 1/\log T_j$ zu jeder Nullstellenordinate (möglich wegen $O(\log T)$ Nullstellen pro Einheitsintervall). Titchmarsh liefert im festen Streifen:

$$
\frac{\xi'}{\xi}(\sigma + iT_j) = O(\log^2 T_j).
$$

Zugleich $F_h(\sigma + iT_j) = O_N(T_j^{-N})$, also:

$$
\text{Horizontalintegral} = O_N\!\left(T_j^{-N}\log^2 T_j\right) \to 0. \quad \checkmark
$$

---

## 5. Vorzeichen, Faktor 2 und Masterform — der kritische Fixpunkt

### 5.1 Residuenvorzeichen bei $-\xi'/\xi$

Sei $K(s) = \xi'/\xi(s)$. Aus $\xi(s) = \xi(1-s)$ folgt

$$
K(1-s) = -K(s).
$$

Der Residuenwert von $-K$ an einer Nullstelle der Vielfachheit $m_\rho$ ist $-m_\rho$. Die Residuenformel für das symmetrische Rechteck liefert daher:

$$
\sum_\rho m_\rho F_h(\rho)
= \frac{2}{2\pi i}\int_{\operatorname{Re}s=\sigma} \frac{\xi'}{\xi}(s)\,F_h(s)\,ds.
$$

Wird **$-\xi'/\xi$** verwendet:

$$
\frac{2}{2\pi i}\int_{(\sigma)} -\frac{\xi'}{\xi}(s)\,F_h(s)\,ds = -\sum_\rho m_\rho F_h(\rho).
$$

### 5.2 Zerlegung von $\xi'/\xi$

$$
\frac{\xi'}{\xi}(s) = \frac{1}{s} + \frac{1}{s-1} + \frac{\Gamma_{\mathbb{R}}'}{\Gamma_{\mathbb{R}}}(s) + \frac{\zeta'}{\zeta}(s).
$$

Da $I_{\mathrm{fin}}(h) = \frac{1}{2\pi i}\int_{(\sigma)} -\frac{\zeta'}{\zeta}(s)\,F_h(s)\,ds$, ergibt die Integration:

$$
\frac{1}{2\pi i}\int_{(\sigma)} \frac{\xi'}{\xi}(s)\,F_h(s)\,ds
= A_{\mathrm{pole}} + A_\Gamma - I_{\mathrm{fin}}.
$$

### 5.3 Polbuchhaltung

Die rationalen Faktoren $1/s$ und $1/(s-1)$ in $\xi'/\xi$ liefern beim symmetrischen Einschluss:

$$
2A_{\mathrm{pole}} = F_h(0) + F_h(1) = h(i/2) + h(-i/2).
$$

**Achtung:** Dies ist der Polbeitrag der Explizitform, nicht zu verwechseln mit

$$
\frac{1}{2\pi}\int_{\mathbb{R}} p_\infty^{\mathrm{raw}}(t)\,h(t)\,dt = 0
$$

(für reelles gerades $h$, da $p_\infty^{\mathrm{raw}}$ ungerade und rein imaginär ist). Die Null hier entsteht durch Symmetriegründe, nicht durch Verschwinden des Polterms.

### 5.4 Gammabeitrag

Nach Verschiebung auf die kritische Linie:

$$
A_\Gamma = \Lambda_\Gamma(h) = \frac{1}{2\pi}\int_{\mathbb{R}} \gamma_\infty(t)\,h(t)\,dt.
$$

Der Faktor $2$ vor $\Lambda_\Gamma$ in der Masterform folgt aus dem Faktor $2$ der symmetrischen Kontur und **darf nicht stillschweigend entfernt werden**.

### 5.5 Keine trivialen Nullstellen in der $\xi'/\xi$-Buchhaltung

In der $\xi'/\xi$-Variante werden **keine trivialen Nullstellen** zusätzlich summiert. Die trivialen Nullstellen von $\zeta$ bei $-2,-4,\ldots$ sind in $\xi$ durch den Gammafaktor so eingebaut, dass $\xi$ ausschließlich die **nichttrivialen** Nullstellen trägt. Die Summe $\sum_\rho$ läuft daher nur über $0 < \operatorname{Re}(\rho) < 1$.

---

## 6. Autoritative Masterform ✓[K/M]

$$
\boxed{
\sum_\rho m_\rho F_h(\rho)
= F_h(0) + F_h(1) + 2\Lambda_\Gamma(h) - 2I_{\mathrm{fin}}(h)
}
$$

Explizit ausgeschrieben:

$$
\boxed{
\sum_\rho m_\rho\, h\!\left(\frac{\rho-\tfrac12}{i}\right)
= h(i/2) + h(-i/2) + 2\Lambda_\Gamma(h)
- 2\sum_{n\geq 2}\frac{\Lambda(n)}{\sqrt{n}}\,g(\log n)
}
$$

**Vorzeichenkonvention:** Die Formel gilt mit $+\xi'/\xi$ im Integral (Variante B: $-\xi'/\xi$ ergibt ein globales Vorzeichenminus auf der linken Seite). Im Repository ist **Variante B** dokumentiert; die obige Darstellung mit positivem $\sum_\rho$ entspricht dem Übergang zur $+\xi'/\xi$-Formulierung.

---

## 7. Knotentabelle

| Aufgabe | Inhalt | Status |
|---------|--------|--------|
| $F_h$-Konstruktion, PW-Abfall | holomorpher Testkern, Streifenabfall | ✓[M] |
| $\sigma$-Unabhängigkeit $I_{\mathrm{fin}}$ | Primzahlpotenzform $\sum \Lambda(n)/\sqrt{n}\,g(\log n)$ | ✓[M] |
| Absolute Nullstellenkonvergenz | PW + $N(T+1)-N(T) = O(\log T)$ | ✓[M] |
| Horizontale Randkontrolle | $O_N(T^{-N}\log^2 T) \to 0$ | ✓[M] |
| **Vorzeichen + Faktor 2 + Polbuchhaltung** | **Masterform mit $F_h(0)+F_h(1)$, $2\Lambda_\Gamma$, keine trivialen NSTen** | **✓[K/M]** |

---

## 8. Abschluss-Knotenstatus

```
[O-220-1-PD5a1-contour-shift-Weil-distribution]  →  ✓[K/M]
[O-220-1-PD5a1b-xi-master-sign-factor2]           →  ✓[K/M]
```

**Nächster offener Knoten:** PD5a2 — Positivitätstest der Weil-Form

$$
W_g := \sum_\rho m_\rho |h(\gamma)|^2 \geq 0 \quad \text{(unter RH)}
$$

bzw. spektrale Interpretation von $\Lambda_{\mathrm{zeros}}$ im Rahmen des Spektralobjekts $X_\infty$.

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220j (de04247) | Holomorpher Kern, archimedische Seite $X_\infty$ |
| NEU-220k v1 (73ea17d) | A1/A2/A3 Erstfassung |
| Titchmarsh §3.11, §9.4 | $\xi'/\xi$-Schranken, $N(T+1)-N(T) = O(\log T)$ |
| Bombieri (Weil explicit formula) | Masterform-Vorlage für Variante B |
| Paley-Wiener | Rapid-decay von $F_h$ für $g \in C_c^\infty$ |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
