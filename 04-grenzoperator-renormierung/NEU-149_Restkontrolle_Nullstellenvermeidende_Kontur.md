# NEU-149 — Restkontrolle auf nullstellenvermeidenden Mellin-Konturen

> Stand: 9. Juli 2026.
> Anschluss: NEU-148 (Mellin-Darstellung, Residuenformel, [O-148-1]), NEU-147 (Randfall, Nullstellen-Terme).
> **Kernbefund:** Nicht der Abfall von $\widehat\varphi$ ist der erste Prüfpunkt, sondern die Lage der Linkskontur relativ zu den Polen von $F(\beta+s) = -\zeta'/\zeta(\beta+s)$. Ohne Auskerbung ist das Restintegral nicht definiert.

---

## Leitmotiv

$$\boxed{\text{Mellin-Abfall} + \text{nullstellenvermeidende Kontur} + \text{moderates Wachstum von }-\zeta'/\zeta \;\Longrightarrow\; R_{\varphi,X}(\beta)\to 0.}$$

Ein gerader linker Strich $\Re s = -M$ ist nur zulässig, wenn er keine Pole von $F(\beta+s)$ schneidet. Im Allgemeinen braucht man eine **ausgekerbte oder gebrochene Kontur**.

---

## Korrektur zu NEU-148: Pol bei $s=0$

In NEU-148 wurde über die Normierung $\widehat\varphi(0)=1$ geschrieben. Das ist unpräzise.

Für $\varphi \in C_c^\infty([0,\infty))$ mit $\varphi = 1$ nahe $0$ und $\varphi = 0$ nahe $\infty$ hat die Mellin-Transformierte

$$\widehat\varphi(s) = \int_0^\infty \varphi(x)\,x^{s-1}\,dx$$

bei $s=0$ einen **einfachen Pol** (wegen $\int_0^1 x^{s-1}\,dx = 1/s$), mit

$$\operatorname{Res}_{s=0}\widehat\varphi(s) = 1.$$

Nicht der Wert $\widehat\varphi(0)$, sondern das **Residuum** bei $s=0$ liefert den Hauptterm:

$$\operatorname{Res}_{s=0}\bigl[\widehat\varphi(s)\,X^s\,F(\beta+s)\bigr] = \operatorname{Res}_{s=0}\widehat\varphi(s)\cdot X^0\cdot F(\beta) = F(\beta) = -\frac{\zeta'}{\zeta}(\beta).$$

$$\boxed{\operatorname{Res}_{s=0}\widehat\varphi(s) = 1, \quad \text{nicht } \widehat\varphi(0) = 1. \quad (\text{Korrektur zu NEU-148.0})}$$

---

## 149.1 Lokaler Kompaktbereich

Alle Aussagen werden **lokal gleichmäßig** formuliert. Sei $K \subset \mathbb{C}$ kompakt mit

$$K \cap \{1, \rho, -2n\} = \varnothing,$$

wobei $\rho$ alle nichttrivialen Nullstellen von $\zeta$ und $-2n$ ($n\geq 1$) die trivialen Nullstellen sind.

Für $\beta \in K$ liegen die Pole des Integranden $\widehat\varphi(s)\,X^s\,F(\beta+s)$ bei $s = \omega - \beta$ für $\omega \in \{1, \rho, -2n\}$. Da $\beta \in K$ diese Werte nicht annimmt, haben die Pole $s_\omega = \omega - \beta$ einen positiven Abstand von $0$.

---

## 149.2 Mellin-Abfall von $\widehat\varphi$

Für $\varphi \in C_c^\infty([0,\infty))$ gilt: Auf jeder vertikalen Geraden $\Re s = \sigma \neq 0$ fällt $\widehat\varphi$ **schnell** in der Imaginärvariablen:

$$|\widehat\varphi(\sigma + it)| = O_{\sigma,N}\bigl((1+|t|)^{-N}\bigr) \qquad\text{für jedes } N\geq 1,\; t\to\pm\infty.$$

Dies folgt aus Integration by parts: $\widehat\varphi(\sigma+it) = (it)^{-N}\int_0^\infty (\partial_x^N(x^{\sigma-1}\varphi(x)))\,e^{it\log x}\,d\log x$.

**Wichtig:** Dieser Abfall gilt nur für $\sigma \neq 0$. Bei $\sigma = 0$ (d.h. auf der imaginären Achse) hat $\widehat\varphi$ den Pol.

---

## 149.3 Zulässige Linkskontur

**Definition:** Eine Kontur $\Gamma_{-M}$ heißt **zulässig für $K$**, wenn:

1. $\Re s \leq -M < 0$ auf ganz $\Gamma_{-M}$,
2. $\beta + s \notin \{1, \rho, -2n\}$ für alle $\beta \in K$, $s \in \Gamma_{-M}$,
3. $\Gamma_{-M}$ ist eine rektifizierbare Kurve, die den Halbstreifen $\Re s \leq -M$ von $\Re s = c$ trennt.

**Existenz:** Da die Polmenge $\{\omega - \beta : \omega \in \{1,\rho,-2n\}, \beta \in K\}$ abgeschlossen und diskret ist, existiert für jedes $M$ eine zulässige Kontur (z.B. ein gebrochener Streckenzug oder eine Folge vertikaler Streifen mit horizontalen Verbindungen, die Pole umfahren).

**Standardkonstruktion:** Statt einer einzigen vertikalen Geraden $\Re s = -M$ wählt man eine Folge $M_j \to \infty$, so dass $-M_j$ kein Realteil eines Poles $\omega - \beta$ ist. Die klassische Wahl (vgl. Zeta-Theorie) ist: Wähle $M_j$ so, dass $|M_j - \Re(\rho - \beta)| > \delta$ für alle $\rho, \beta \in K$ und ein festes $\delta > 0$.

$$\boxed{\text{Gerader Strich } \Re s=-M \text{ ist im Allgemeinen nicht zulässig. Ausgekerbte oder Standardfolgen-Kontur nötig.}}$$

---

## 149.4 Wachstum von $F(\beta+s)$ auf der Kontur

Für $\Re(\beta+s) = \Re\beta - M < 0$ liegt man links von allen nicht-trivialen Nullstellen. Die Funktion $F(w) = -\zeta'/\zeta(w)$ ist auf einem Vertikalstreifen $|\Re w - \sigma_0| < \delta$ außerhalb der Pole durch die **vertikale Nullstellendichte** kontrolliert.

Klassisches Resultat (Backlund, Titchmarsh):

$$|F(\sigma + it)| = O(\log^2(2+|t|)) \qquad\text{für } \sigma \notin \{\Re\omega\}\text{, lokal gleichmäßig.}$$

Genauer: auf einer zulässigen Kontur $\Gamma_{-M}$ (die Pole meidet) gilt

$$|F(\beta+s)| = O_K((1+|\Im s|)^A) \qquad\text{für ein } A = A(K),$$

lokal gleichmäßig in $\beta \in K$.

---

## 149.5 Restintegral-Schranke

Nach Konturverschiebung von $\Re s = c$ auf $\Gamma_{-M}$:

$$R_{\varphi,X}(\beta) = \frac{1}{2\pi i}\int_{\Gamma_{-M}} \widehat\varphi(s)\,X^s\,F(\beta+s)\,ds.$$

Auf $\Gamma_{-M}$: $|X^s| \leq X^{-M}$. Mit dem Mellin-Abfall (149.2) und dem moderaten Wachstum (149.4):

$$|R_{\varphi,X}(\beta)| \leq X^{-M} \cdot \frac{1}{2\pi}\int_{\Gamma_{-M}} |\widehat\varphi(s)|\,|F(\beta+s)|\,|ds|$$

$$\leq X^{-M} \cdot O_K\!\left(\int_{-\infty}^\infty (1+|t|)^{-N+A}\,dt\right) = O_K(X^{-M}) \qquad\text{für } N > A+1.$$

Für $X\to\infty$ (mit $M$ fest):

$$\boxed{R_{\varphi,X}(\beta) = O_K(X^{-M}) \to 0 \qquad (X\to\infty),}$$

lokal gleichmäßig für $\beta \in K$.

**Marker:** $\checkmark[M]$ modulo Konstruktion der zulässigen Kontur. Der Schritt von einem einzelnen $M$ zur vollständigen Konturverschiebung $M\to\infty$ und der Nachweis, dass alle gekreuzten Residuen korrekt gezählt wurden, ist $?[O]$.

---

## 149.6 Schlussformel

Unter den Voraussetzungen (zulässige Kontur, moderates Wachstum) gilt:

$$\boxed{\lim_{X\to\infty}\Bigl(S_{\varphi,X}(\beta) - D_{\varphi,X}^{\mathrm{expl}}(\beta)\Bigr) = -\frac{\zeta'}{\zeta}(\beta),}$$

lokal gleichmäßig auf kompakten Mengen $K \subset \mathbb{C}\setminus\{1,\rho,-2n\}$.

$$\checkmark[M] \text{ modulo zulässiger Kontur und Wachstum.} \qquad ?[O] \text{ als formaler Beweis.}$$

---

## 149.7 Statusdiagnose und Arbeitsplan

| Eintrag | Inhalt | Status |
|---|---|---|
| **Korrektur NEU-148** | $\operatorname{Res}_{s=0}\widehat\varphi(s)=1$, nicht $\widehat\varphi(0)=1$ | ✅ |
| **149.A** | Lokaler Kompaktbereich $K$, Polabstand | ✅ |
| **149.B** | Mellin-Abfall: $|\widehat\varphi(\sigma+it)| = O_N((1+|t|)^{-N})$ für $\sigma\neq 0$ | ✅ |
| **149.C** | Zulässige Kontur: Definition, Existenz, Standardkonstruktion | ✅[M] |
| **149.D** | Moderates Wachstum $|F(\beta+s)| = O_K((1+|\Im s|)^A)$ auf Kontur | ✅[M] |
| **149.E** | $|R_{\varphi,X}| = O_K(X^{-M}) \to 0$ | ✅[M] |
| **149.F** | Schlussformel lokal gleichmäßig | ✅[M] |
| **[O-149-1]** | Kanonische Konstruktion der nullstellenvermeidenden Kontur | ❓[O] |
| **[O-149-2]** | Vollständige Residuenzählung bei Konturverschiebung $M\to\infty$ | ❓[O] |
| **[O-149-3]** | Quantitative Schranke für $A = A(K)$ (Wachstumsexponent von $-\zeta'/\zeta$) | ❓[O] |

$$\boxed{\text{[O-148-1] ist } \checkmark[M] \text{ abgeschlossen. Formaler Beweis via [O-149-1]+[O-149-2].}}$$

$$\boxed{\text{Nächste Nummer: NEU-150.} \quad \text{Kandidat: Rückbindung an Operator }R\text{ — Verbindung Mellin-Finite-Part mit }\operatorname{Tr}_{\mathrm{reg}}(R\Sigma).}$$

---

## Verweise

- **NEU-148**: Mellin-Darstellung, Residuenformel, [O-148-1] (jetzt $\checkmark[M]$)
- **NEU-147**: Randfall, Nullstellen-Terme, RH-Verbindung
- **NEU-146**: Schichtzerlegung $T_k$ (jetzt Korollar)
- **NEU-145**: Regulierte Spur: Definition vs. operatorielle Realisierung
- Titchmarsh: *The Theory of the Riemann Zeta-Function*, Ch. 3 (Nullstellenfreie Region, Wachstum von $\zeta'/\zeta$)
- Backlund: Klassische Schranken für $|\zeta'/\zeta(\sigma+it)|$
