# NEU-229 — Objekt X: Arbeitsdefinition, Hypothese und offene Beweispflichten

**Status:** `❓ [O]` — Arbeitsdefinition und Forschungshypothese  
**Datum:** 2026-08-04  
**Strang:** 00 — Grundlegung  
**Vorgänger:** ebene-XVI-objekt-x.md, objekt_x_minimalaxiome.md  

---

## 1. Analytischer Ausgangspunkt

Seien $\rho = \beta + i\gamma$ die nichttrivialen Nullstellen der Riemannschen
Zetafunktion. Die erste Nullstelle mit positivem Imaginärteil ist

$$
\rho_1 = \frac{1}{2} + i\gamma_1,
\qquad
\gamma_1 = 14{,}134725141734693\ldots
$$

In der expliziten Formel für die Chebyshev-Funktion

$$
\psi(x) = \sum_{p^m \le x} \log p
$$

erscheinen die nichttrivialen Nullstellen durch Terme der Form $-x^\rho/\rho$.
Für ein konjugiertes Paar $\rho = \beta + i\gamma$, $\overline\rho = \beta - i\gamma$
ergibt sich ein reeller oszillierender Beitrag

$$
-\frac{2x^\beta}{\sqrt{\beta^2 + \gamma^2}}
\cos\!\left(\gamma \log x - \arctan\frac{\gamma}{\beta}\right).
$$

Unter der Annahme $\beta = \tfrac{1}{2}$ lautet dieser Beitrag

$$
-\frac{2\sqrt{x}}{\sqrt{\gamma^2 + \tfrac{1}{4}}}
\cos\!\left(\gamma \log x - \arctan(2\gamma)\right).
$$

Das erste konjugierte Nullstellenpaar erzeugt somit den **niedrigsten positiven
Nullstellenmodus** in der logarithmischen Variablen $u = \log x$.

> **Vorsicht.** Die explizite Formel ist nicht als gewöhnliche absolut konvergente
> Fourierreihe zu verstehen. Die Nullstellensumme muss je nach Fassung symmetrisch
> abgeschnitten, geglättet oder distributionell interpretiert werden.

---

## 2. Arithmetische und spektrale Daten

Die explizite Formel verbindet zwei Arten von Daten.

**Arithmetische Seite.** Für jede Primzahl $p$ und jedes $m \ge 1$ erscheinen die
Prime-Power-Zeiten

$$
\ell_{p,m} = m \log p
$$

mit Gewichten

$$
w_{p,m} = \frac{\log p}{p^{m/2}}.
$$

**Spektrale Seite.** Auf der Nullstellenseite erscheinen die Frequenzen

$$
\gamma_1, \gamma_2, \gamma_3, \ldots
$$

der nichttrivialen Nullstellen $\rho_n = \beta_n + i\gamma_n$.

Die gesicherte explizite Formel zeigt eine **Identität** zwischen geeigneten
Auswertungen dieser beiden Datensysteme. Sie liefert jedoch noch keine intrinsische
Konstruktion eines gemeinsamen Trägerobjekts.

---

## 3. Arbeitsdefinition von Objekt X

**Arbeitsdefinition.** *Objekt X* bezeichnet ein hypothetisches, kanonisch gegliedertes
System

$$
X = \Bigl(
  \mathcal{K}_X,\;
  \mathcal{D}_X,\;
  \{U_t\}_{t \in \mathbb{R}},\;
  \mathcal{T}_\infty,\;
  \{\mathcal{T}_p\}_{p\;\text{prim}},\;
  \mathcal{T}_{\mathrm{pole}},\;
  \mathcal{G}
\Bigr)
$$

mit folgenden Bestandteilen:

| Bestandteil | Beschreibung |
|---|---|
| $\mathcal{K}_X$ | Hilbert-, Prä-Hilbert- oder Positivitätsraum |
| $\mathcal{D}_X$ | geeigneter Raum von Testdaten |
| $U_t : \mathcal{K}_X \to \mathcal{K}_X$ | stark stetiger Skalierungsfluss |
| $\mathcal{T}_p : \mathcal{D}_X \to \mathcal{K}_p$ | lokale arithmetische Kanäle |
| $\mathcal{T}_\infty : \mathcal{D}_X \to \mathcal{K}_\infty$ | archimedischer Kanal |
| $\mathcal{T}_{\mathrm{pole}} : \mathcal{D}_X \to \mathcal{K}_{\mathrm{pole}}$ | Kanal für Pol- und Randterme |
| $\mathcal{G} : \mathcal{K}_\infty \oplus \bigoplus_p \mathcal{K}_p \oplus \mathcal{K}_{\mathrm{pole}} \to \mathcal{K}_X$ | globale Gluungsabbildung |

Der **globale Kanal** ist formal

$$
\mathcal{T} = \mathcal{G}\!\left(
  \mathcal{T}_\infty
  \oplus \bigoplus_p \mathcal{T}_p
  \oplus \mathcal{T}_{\mathrm{pole}}
\right).
$$

> **Hinweis.** Diese Arbeitsdefinition beschreibt zunächst nur die verlangte
> Architektur. Sie ist noch keine intrinsische Konstruktion von Objekt X.

---

## 4. Objekt-X-Hypothese

**Hypothese.** Es existiert eine kanonische Realisierung von Objekt X mit den
folgenden Eigenschaften.

### X1 — Lokale arithmetische Reproduktion

Für jede Primzahl $p$ reproduziert der lokale Kanal $\mathcal{T}_p$ die vollständige
Prime-Power-Familie $m\log p$, $m \ge 1$, mit den Gewichten $\log p / p^{m/2}$.

> Die höheren Primzahlpotenzen und ihre korrekten Normierungen dürfen *nicht*
> nachträglich von außen eingesetzt werden.

### X2 — Archimedischer Kanal

Der Kanal $\mathcal{T}_\infty$ reproduziert exakt den archimedischen Beitrag der
expliziten Formel, einschließlich der durch den Gammafaktor bestimmten Terme.

### X3 — Pol- und Randterme

Der Kanal $\mathcal{T}_{\mathrm{pole}}$ erzeugt die Beiträge, die den Polen
beziehungsweise Randtermen der vervollständigten Zetafunktion entsprechen.

### X4 — Globale Gluung

Die Abbildung $\mathcal{G}$ verbindet die lokalen, archimedischen und polaren Daten
zu einer einzigen globalen Struktur. Diese Gluung darf nicht bloß die bekannte
explizite Formel neu notieren, sondern muss aus der inneren Struktur von $X$ folgen.

### X5 — Gram-Realisierung der Weil-Form

Für geeignete Testfunktionen $f, g$ gilt

$$
Q_W(f,g) = \langle \mathcal{T} f,\, \mathcal{T} g \rangle_{\mathcal{K}_X},
$$

oder zunächst in einer approximativen Form

$$
\langle \mathcal{T}_S f,\, \mathcal{T}_S g \rangle = Q_W(f,g) + R_S(f,g),
$$

wobei für eine gerichtete Familie endlicher Datenmengen $S$

$$
R_S \ge -\varepsilon_S, \qquad \varepsilon_S \longrightarrow 0.
$$

### X6 — Skalierungsdynamik

Der Fluss $U_t$ besitzt einen Generator $H_X$, formal etwa durch $U_t = e^{itH_X}$.
Der Operator $H_X$, eine kanonische Kompression von ihm oder eine zugehörige
Resonanzkonstruktion trägt die Frequenzen

$$
\sigma_{\mathrm{relevant}}(H_X) = \{\gamma_n\} = \{\operatorname{Im}\rho_n\}.
$$

### X7 — Kanonizität

Alle wesentlichen Bestandteile von $X$ müssen aus natürlichen mathematischen Daten
hervorgehen. Insbesondere dürfen die bekannten Nullstellen nicht als Eingabedaten
in die Definition des Operators, des Raumes oder der Gluung eingebaut werden.

---

## 5. Spektrale Objekt-X-Hypothese

Eine stärkere Fassung lautet:

**Spektralhypothese.** Es existiert ein kanonisch bestimmter selbstadjungierter
Operator $H_X$ oder eine äquivalente positive Spektralkonstruktion, so dass

$$
\sigma_{\mathrm{relevant}}(H_X) = \{\gamma_n : n \ge 1\}.
$$

Je nach Konstruktion bezeichnet $\sigma_{\mathrm{relevant}}$ das diskrete Spektrum,
ein Resonanzspektrum, ein Absorptionsspektrum oder das Spektrum einer kanonischen
Kompression.

In dieser starken Fassung wäre $\gamma_1 = 14{,}134725141734693\ldots$ die
**kleinste positive globale Eigenfrequenz oder Resonanz** von Objekt X.

> **Statusmarke:** `❓ [O]`  
> Gesichert ist lediglich, dass $\gamma_1$ der niedrigste positive Nullstellenparameter
> ist und in der expliziten Formel den ersten positiven logarithmischen Nullstellenmodus
> erzeugt. Die Konstruktion von $H_X$ ist offen.

---

## 6. Positivitätsfassung

Die für das Forschungsprogramm strategisch vorrangige Fassung ist die
**Positivitätshypothese**, nicht unmittelbar die Spektralhypothese:

**Positivitätshypothese.** Die Weil-Form besitzt eine kanonische globale Gram-Realisierung

$$
Q_W(f,f) = \|\mathcal{T} f\|_{\mathcal{K}_X}^{\,2}.
$$

Falls diese Identität für die relevante Testfunktionsklasse bewiesen wird, folgt
$Q_W(f,f) \ge 0$. Da die geeignete Weil-Positivität zur Riemannschen Vermutung
äquivalent ist, würde eine solche Konstruktion die Riemannsche Vermutung beweisen.

> Der selbstadjungierte Operator sollte nicht isoliert geraten werden.
> Er sollte aus der zuvor konstruierten Positivitäts- und Skalierungsstruktur
> hervorgehen.

---

## 7. Bedeutung der ersten Nullstelle innerhalb des Programms

Innerhalb der Objekt-X-Hypothese ist $\gamma_1 = 14{,}134725141734693\ldots$

- **nicht** die Signatur einer einzelnen Primzahl,
- **nicht** die Eigenfrequenz eines einzelnen lokalen Kanals,
- sondern die niedrigste positive Resonanz der vollständigen globalen Gluung

$$
\mathcal{T}_\infty
\oplus \bigoplus_p \mathcal{T}_p
\oplus \mathcal{T}_{\mathrm{pole}}
\;\overset{\mathcal{G}}{\longrightarrow}\;
\mathcal{K}_X.
$$

Ihr analytisch sichtbarer Schatten ist der Beitrag

$$
-\frac{2\sqrt{x}}{\sqrt{\gamma_1^2 + \tfrac{1}{4}}}
\cos\!\left(\gamma_1 \log x - \arctan(2\gamma_1)\right)
$$

in der expliziten Formel.

Die Zahl $\gamma_1$ entsteht — sofern die Hypothese richtig ist — nicht aus einem
einzelnen Primkanal, sondern aus der **globalen Wechselwirkung** aller lokalen
Prime-Power-Daten mit dem archimedischen Kanal und den Randtermen.

---

## 8. Bemerkung zur logarithmischen Dynamik

Die Prime-Power-Zeiten $m \log p$ und die Nullstellenfrequenzen $\gamma_n$ sind
natürliche duale Größen bezüglich der additiven Koordinate $u = \log x$.

Multiplikative Skalierung $x \mapsto e^t x$ wird in $u$ zur Translation
$u \mapsto u + t$. Daher ist ein **Skalierungsfluss** ein natürlicher Kandidat
für die dynamische Struktur von Objekt X.

> Dies allein erklärt weder die Primzahlgewichte noch die Positivität der
> Weil-Form. Beides muss zusätzlich aus der Konstruktion folgen.

---

## 9. Abgrenzung gegen zirkuläre Konstruktionen

Nicht ausreichend wäre ein Operator, der nachträglich durch
$H e_n = \gamma_n e_n$ definiert wird.

Ein solcher Operator besitzt zwar formal das gewünschte Spektrum, erklärt aber nicht:

- warum die Zahlen $\gamma_n$ auftreten;
- warum sie mit Primzahlen verbunden sind;
- warum die Prime-Power-Gewichte genau $\log p / p^{m/2}$ lauten;
- warum der Gammafaktor erscheint;
- warum die Weil-Form positiv sein sollte;
- weshalb die Konstruktion kanonisch ist.

Eine erfolgreiche Definition von Objekt X muss daher **mehr leisten** als eine
spektrale Nachbildung der Nullstellen.

---

## 10. Offene Beweispflichten

| Knoten | Inhalt | Status |
|---|---|---|
| **OX-1** | Intrinsische Definition: konkreter Raum, Komplex oder Strukturträger | `❓ [O]` |
| **OX-2** | Lokale Kanäle: alle Beiträge $\log p / p^{m/2}$, $m \ge 1$, mit korrekter Normierung | `❓ [O]` |
| **OX-3** | Archimedischer Kanal: vollständiger Gamma-Beitrag ohne formale Restzuweisung | `❓ [O]` |
| **OX-4** | Kanonische Gluung: Konvergenz, Domänenfragen, Unabhängigkeit von Hilfswahlen | `❓ [O]` |
| **OX-5** | Positivität: Weil-Form als Gramform oder Grenzwert endlicher Grammodelle | `❓ [O]` |
| **OX-6** | Grenzübergang: Formkonvergenz, Mosco-Konvergenz oder Resolventenkonvergenz | `❓ [O]` |
| **OX-7** | Skalierungsgenerator: Existenz, Domäne, Symmetrie, Selbstadjungiertheit | `❓ [O]` |
| **OX-8** | Spektrale Identifikation: $\sigma_{\mathrm{relevant}}(H_X) = \{\gamma_n\}$ | `❓ [O]` |
| **OX-9** | Nichtzirkularität: keine Nullstellen oder RH-äquivalente Positivität als versteckte Voraussetzung | `❓ [O]` |
| **OX-10** | Kanonizität und Eindeutigkeit: Universalitäts-, Funktorialitäts- oder Minimalitätseigenschaften | `❓ [O]` |

---

## 11. Forschungsprogramm in vier Stufen

| Stufe | Inhalt |
|---|---|
| **Z1 — Zerlegung** | Präzise Zerlegung $Q_W = Q_\infty + \sum_p Q_p + Q_{\mathrm{pole}}$ konstruieren |
| **Z2 — Endliche Grammodelle** | Für endliche Primzahlmengen $S$ und Cutoffs: $\langle \mathcal{T}_S f, \mathcal{T}_S g\rangle = Q_W + R_S$ |
| **Z3 — Positiver Grenzübergang** | $R_S \ge -\varepsilon_S$, $\varepsilon_S \to 0$; Konvergenz der Formen und Operatoren |
| **Z4 — Spektrale Dynamik** | Kanonischen Skalierungsfluss und Generator $H_X$ gewinnen; erst dann Spektralidentifikation |

---

## 12. Kompakte Kernhypothese

Es existiert ein kanonisch gegliederter Positivitätsraum mit lokalen Primzahlkanälen,
einem archimedischen Kanal, einem Polkanal und einem Skalierungsfluss, dessen globale
Gluung die Weil-Form als Gramform realisiert. Die arithmetische Seite dieser Konstruktion
erzeugt die Prime-Power-Daten $m \log p$ mit Gewichten $\log p / p^{m/2}$, während die
zugehörige globale Skalierungsdynamik die Imaginärteile der nichttrivialen
Zetafunktionsnullstellen als Spektral- oder Resonanzparameter hervorbringt.

> **Der neue mathematische Inhalt des Programms liegt nicht in der expliziten Formel
> selbst. Er liegt in der Konstruktion eines natürlichen gemeinsamen Trägers, aus dem
> arithmetische Seite, archimedischer Beitrag, Positivität und spektrale Seite
> gleichzeitig und intrinsisch folgen.**

---

*Erstellt: 2026-08-04 · Epistemischer Status: Arbeitsdefinition und Forschungshypothese ·
Beweispflichten OX-1–OX-10 explizit offen*
