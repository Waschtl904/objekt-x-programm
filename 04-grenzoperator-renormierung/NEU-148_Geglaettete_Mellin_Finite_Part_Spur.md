# NEU-148 — Geglättete Mellin-Finite-Part-Spur

> Stand: 9. Juli 2026.
> Anschluss: NEU-147 (explizite Finite-Part-Struktur, Randfall, Nullstellen-Terme), NEU-146 (Schichtzerlegung), NEU-145 (regulierte Spur).
> **Kernidee:** Die gesamte Euler-Struktur steckt in $-\zeta'/\zeta(\beta+s)$. Mellin-Inversion liefert die Residuenformel direkt — ohne Schicht-für-Schicht-Analyse von $T_k$.

---

## Leitmotiv

$$\boxed{\text{Nicht }T_k\text{ einzeln zuerst. Erst geglättete Mellin-Spur.}}$$

$$\boxed{S_{\varphi,X}(\beta) = \frac{1}{2\pi i}\int_{(c)} \widehat\varphi(s)\,X^s\,\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds, \qquad c > 1-\Re\beta.}$$

Die $T_k$-Schichtformel aus NEU-146/147 ist die **entfaltete** Version davon (nach $\sum_k$-Entwicklung von $1/(1-p^{-\beta-s})$) und kann als Korollar nachgereicht werden.

---

## 148.0 Setup: Testfunktion und Mellin-Transformierte

Sei $\varphi \in C_c^\infty([0,\infty))$ mit

$$\varphi(x) = 1 \quad\text{für }x\text{ nahe }0, \qquad \varphi(x) = 0 \quad\text{für }x\geq 2.$$

Die Mellin-Transformierte sei

$$\widehat\varphi(s) := \int_0^\infty \varphi(x)\,x^{s-1}\,dx.$$

Da $\varphi \in C_c^\infty$, ist $\widehat\varphi$ **ganz** — es gibt keine Pole. Insbesondere ist $\widehat\varphi(s)$ für alle $s\in\mathbb{C}$ definiert und fällt in vertikalen Streifen schnell ab.

**Normierung:**
$$\widehat\varphi(1) = \int_0^\infty \varphi(x)\,dx = 1.$$

*Bemerkung:* Im Gegensatz zu einer Heaviside-Funktion (scharfer Cutoff) ist $\widehat\varphi$ ganz und dämpft Residuen-Terme durch den schnellen Abfall von $\widehat\varphi$ auf vertikalen Geraden.

---

## 148.1 Definition der geglätteten Spur

$$S_{\varphi,X}(\beta) := \sum_p \varphi\!\left(\frac{p}{X}\right) \frac{\log p\, p^{-\beta}}{1-p^{-\beta}}.$$

Da $\varphi$ kompakten Träger hat, ist die Summe endlich für jedes $X < \infty$. Für $X\to\infty$: wachsende endliche Summe, die für $\Re\beta > 1$ gegen $-\zeta'/\zeta(\beta)$ konvergiert.

---

## 148.2 Mellin-Darstellung

**Satz (Mellin-Inversion):**

Für $c > 1-\Re\beta$ gilt

$$\boxed{S_{\varphi,X}(\beta) = \frac{1}{2\pi i}\int_{(c)} \widehat\varphi(s)\,X^s\,\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds.}$$

**Beweis:**

Die Mellin-Inversionsformel gibt
$$\varphi(p/X) = \frac{1}{2\pi i}\int_{(c)} \widehat\varphi(s)\,X^s\,p^{-s}\,ds.$$

Einsetzen:
$$S_{\varphi,X}(\beta) = \sum_p \frac{\log p\,p^{-\beta}}{1-p^{-\beta}} \cdot \frac{1}{2\pi i}\int_{(c)} \widehat\varphi(s)\,X^s\,p^{-s}\,ds.$$

Für $c > 1-\Re\beta$ gilt $\Re(\beta+s) > 1$ auf der Integrationslinie. Daher konvergiert $\sum_p \log p\, p^{-(\beta+s)}/(1-p^{-(\beta+s)})$ absolut und gleichmä\xdfig auf kompakten Teilmengen der Integrationslinie. Vertauschen von Summe und Integral:

$$S_{\varphi,X}(\beta) = \frac{1}{2\pi i}\int_{(c)} \widehat\varphi(s)\,X^s \underbrace{\left(\sum_p \frac{\log p\,p^{-(\beta+s)}}{1-p^{-(\beta+s)}}\right)}_{= -\zeta'/\zeta(\beta+s)}\,ds. \qquad \square$$

---

## 148.3 Residuenformel

Sei $F(w) := -\zeta'/\zeta(w)$. Die Pole von $F$ sind:

| Pol $\omega$ | Typ | Residuum $r_\omega$ |
|---|---|---|
| $\omega = 1$ | einfach (Pol von $\zeta$) | $r_1 = 1$ |
| $\omega = \rho$ (nichttriviale Nullstelle) | einfach (Nullstelle $m_\rho$-fach) | $r_\rho = -m_\rho$ |
| $\omega = -2n$, $n\geq 1$ (triviale Nullstellen) | einfach | $r_{-2n} = -1$ |

Nach Konturverschiebung von $\Re(s)=c$ nach $\Re(s)\to -\infty$ überquert die Kontur die Pole von $F(\beta+s)$, die bei $s = \omega - \beta$ liegen.

**Residuenbeiträge:**

Jeder Pol $\omega$ von $F$ mit $s_\omega := \omega - \beta$ liefert

$$\operatorname{Res}_{s=s_\omega}\bigl[\widehat\varphi(s)\,X^s\,F(\beta+s)\bigr] = r_\omega\,\widehat\varphi(\omega-\beta)\,X^{\omega-\beta}.$$

**Residuenentwicklung:**

$$S_{\varphi,X}(\beta) = -\frac{\zeta'}{\zeta}(\beta)\cdot\widehat\varphi(0) + \sum_{\omega} r_\omega\,\widehat\varphi(\omega-\beta)\,X^{\omega-\beta} + R_{\varphi,X}(\beta),$$

wobei der erste Term vom Pol $s=0$ des Integranden stammt (falls $\widehat\varphi(0) \neq 0$, was von der Normierung abhängt) und $R_{\varphi,X}$ das Restkontur-Integral ist.

**Normierungskonvention für sauberes Ergebnis:**

Wähle $\varphi$ so, dass
$$\widehat\varphi(0) = 1, \qquad \int_0^\infty \varphi(x)\,\frac{dx}{x} = 1.$$

Dann:

$$\boxed{S_{\varphi,X}(\beta) = -\frac{\zeta'}{\zeta}(\beta) + \sum_{\omega} r_\omega\,\widehat\varphi(\omega-\beta)\,X^{\omega-\beta} + R_{\varphi,X}(\beta).}$$

---

## 148.4 Expliziter Divergenzterm und Finite-Part-Satz

### 148.4.1 Definition des expliziten Divergenzterms

$$\boxed{D_{\varphi,X}^{\mathrm{expl}}(\beta) := \sum_{\substack{\omega \\ \Re(\omega-\beta)\geq 0}} r_\omega\,\widehat\varphi(\omega-\beta)\,X^{\omega-\beta}.}$$

Hierbei:
- **Terme mit $\Re(\omega-\beta) > 0$:** $X^{\omega-\beta} \to \infty$ (wachsend, müssen subtrahiert werden)
- **Terme mit $\Re(\omega-\beta) = 0$:** $|X^{\omega-\beta}| = 1$, aber oszillierend in $X$ (kein Grenzwert, müssen ebenfalls subtrahiert werden)
- **Terme mit $\Re(\omega-\beta) < 0$:** $X^{\omega-\beta} \to 0$ (vernachlässigbar, nicht in $D_{\varphi,X}^{\mathrm{expl}}$)

### 148.4.2 Geglätteter expliziter Finite-Part

$$\boxed{\operatorname{FP}_{X\to\infty}^{\varphi}\bigl(S_{\varphi,X}(\beta)\bigr) := \lim_{X\to\infty}\Bigl(S_{\varphi,X}(\beta) - D_{\varphi,X}^{\mathrm{expl}}(\beta)\Bigr) \stackrel{?}{=} -\frac{\zeta'}{\zeta}(\beta).}$$

**Status:** $?[O]$ — gilt, **falls** das Restkontur-Integral $R_{\varphi,X}(\beta) \to 0$ für $X\to\infty$.

### 148.4.3 Prüfpunkt: Restkontrolle

$$\boxed{?[O] \quad R_{\varphi,X}(\beta) \to 0 \quad\text{für die gewählte Klasse von }\varphi.}$$

Konkret: Man schiebt die Kontur nach $\Re(s) = -M$ und muss zeigen, dass

$$\left|\frac{1}{2\pi i}\int_{(-M)} \widehat\varphi(s)\,X^s\,F(\beta+s)\,ds\right| \to 0 \qquad (X\to\infty \text{ oder } M\to\infty).$$

Dies hängt von der Balance zwischen $|X^s| = X^{-M}$ (dämpfend für $M>0$, $X$ fest) und dem Wachstum von $F(\beta+s)$ auf der vertikalen Linie $\Re(s)=-M$ ab.

---

## 148.5 RH-Verbindung (Präzisierung von NEU-147.D)

Unter RH gilt $\Re\rho = 1/2$ für alle nichttrivialen Nullstellen $\rho$. Daher:

$$\Re(\rho - \beta) = 1/2 - \Re\beta \begin{cases} < 0 & \text{falls } \Re\beta > 1/2 \\ = 0 & \text{falls } \Re\beta = 1/2 \\ > 0 & \text{falls } \Re\beta < 1/2 \end{cases}$$

Für $\Re\beta > 1/2$ verschwinden unter RH alle $\rho$-Terme in $D_{\varphi,X}^{\mathrm{expl}}$, und nur der Pol bei $\omega=1$ trägt bei:

$$D_{\varphi,X}^{\mathrm{expl}}(\beta) = r_1\,\widehat\varphi(1-\beta)\,X^{1-\beta} + (\text{triviale Nullstellen, falls }\Re\beta<1/2+2n).$$

**Quantifizierter Satz (vgl. NEU-147.D):**

$$\boxed{\forall\beta\text{ mit }1/2 < \Re\beta < 1,\;\beta\text{ kein Pol von }F:\quad D_X^{(1)}\text{ ausreichend} \iff \text{RH}.}$$

Die Aussage gilt **punktweise für alle** $\beta$ im offenen Streifen $(1/2,1)$ au\xdferhalb der Polstellen, nicht nur für ein einzelnes $\beta$.

---

## 148.6 Vorstufe: $\psi$-Summe und Rückkehr zur Primsumme

Für die spätere Prüfung der Restkontrolle empfiehlt sich der Umweg:

1. **Schritt 1:** Geglättete $\psi$-Summe
$$\Psi_{\varphi,X}(\beta) := \sum_{n\geq 1} \Lambda(n)\,\varphi(n/X)\,n^{-\beta},$$
wobei $\Lambda$ die von-Mangoldt-Funktion ist ($\Lambda(p^k) = \log p$, sonst $0$).

2. **Schritt 2:** Möbius-/Primpotenzen-Korrektur: $S_{\varphi,X}(\beta)$ und $\Psi_{\varphi,X}(\beta)$ unterscheiden sich um die höheren Primpotenzen $p^k$, $k\geq 2$:
$$\Psi_{\varphi,X}(\beta) = S_{\varphi,X}(\beta) + \sum_{k\geq 2}\sum_p \log p\,\varphi(p^k/X)\,p^{-k\beta}.$$
Die Korrekturterme konvergieren für $\Re\beta > 1/2$ (die Reihe ist dann absolut konvergent).

3. **Schritt 3:** Für $\Psi_{\varphi,X}$ ist die explizite Formel und die Mellin-Analyse über $-\zeta'/\zeta(\beta+s)$ direkt anwendbar (kein Primpotenzen-Overhead).

$$\boxed{\Psi_{\varphi,X}(\beta) = S_{\varphi,X}(\beta) + O(X^{1/2-\Re\beta}) \quad (\Re\beta > 1/2),}$$

sodass Finite-Part für $\Psi$ und Finite-Part für $S$ asymptotisch äquivalent sind.

**Status:** $\checkmark[M]$ als Strukturaussage, $?[O]$ als quantitativer Beweis der Resttermkontrolle.

---

## 148.7 Statusdiagnose und Arbeitsplan

| Eintrag | Inhalt | Status |
|---|---|---|
| **148.A** | Mellin-Darstellung $S_{\varphi,X}(\beta) = \int_{(c)} \widehat\varphi(s)X^s(-\zeta'/\zeta(\beta+s))\,ds$ | ✅ |
| **148.B** | Residuenformel: Pole bei $\omega=1,\rho,-2n$ | ✅ |
| **148.C** | Expliziter Divergenzterm $D_{\varphi,X}^{\mathrm{expl}}$, Oszillations-Randfall | ✅ |
| **148.D** | Normierungskonvention $\widehat\varphi(0)=1$ | ✅ |
| **148.E** | RH-Verbindung quantifiziert: $\forall\beta\in(1/2,1)$ au\xdferhalb Pole | ✅[M] |
| **148.F** | $\psi$/$S$-Korrektur via Primpotenzen | ✅[M] |
| **[O-148-1]** | Restkontrolle: $R_{\varphi,X}(\beta)\to 0$ | ❓[O] |
| **[O-148-2]** | $\operatorname{FP}_{X\to\infty}^{\varphi}(S_{\varphi,X}-D_{\varphi,X}^{\mathrm{expl}}) = -\zeta'/\zeta$ | ❓[O], setzt [O-148-1] voraus |
| **[O-148-3]** | Quantitative Präzisierung von $O(X^{1/2-\Re\beta})$ in Schritt 3 | ❓[O] |

$$\boxed{\text{Nächste Nummer: NEU-149.}\quad \text{Kandidat: Restkontrolle }R_{\varphi,X}(\beta)\to 0 \text{ für }\varphi\in C_c^\infty\text{ via Phragmén-Lindelöf oder }\widehat\varphi\text{-Abfall.}}$$

---

## Verweise

- **NEU-147**: Hauptterm-Finite-Part $\neq$ expliziter Finite-Part, Randfall, RH-Verbindung
- **NEU-146**: Schichtzerlegung $T_k$, heuristischer Divergenzterm (jetzt Korollar)
- **NEU-145**: Regulierte Spur als analytische Fortsetzung; $(R+\varepsilon)^{-1}$ ungeeignet
- **NEU-144**: $R$ primdiagonal, Spurformel
- von Mangoldt: Explizite Formel für $\psi(X)$
- Mellin-Inversion: klassisches Werkzeug für glättungsbasierte Primzahltheorie
