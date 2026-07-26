# NEU-101 — Goldston–Montgomery-Transfer und Varianzkanal

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-100 (\(\mathcal{V}_{N,H}\), \(R_{N,H}(k)\); Nullstellenpaar-Kanal nur in \(|\widehat{\Delta}_N|^2\))  
**Nächste Nummer:** NEU-102

---

## Ausgangspunkt

NEU-100 zeigt: Der erste plausible Weil-Kandidat ist das Shift-Spektrum \(|\widehat{\Delta}_N|^2\) bzw.\ \(\mathcal{V}_{N,H}\). NEU-101 stellt dieses Objekt dem klassischen Goldston\u2013Montgomery-Varianzkanal gegenüber.

**Normalisierungskorrektur:** Die klassische Goldston\u2013Montgomery-Formel gilt für den Kurzintervallfehler \(\psi(x+H)-\psi(x)-H\), nicht unmittelbar für \(\Delta_N(h)\). Ein Transferlemma ist nötig.

---

## Satz NEU-101.1 — Kurzintervallvarianz (Goldston\u2013Montgomery)

Der normalisierte Hauptterm der dyadischen Kurzintervallvarianz lautet:

$$
\mathcal{V}(M, H)
:= \frac{1}{M} \int_M^{2M}
\left(\psi(x+H) - \psi(x) - H\right)^2 dx
\sim \frac{H}{M} \log\frac{M}{H}.
$$

Dies gilt bedingt unter RH (Goldston\u2013Montgomery 1987). Chan (2003) präzisiert die zweiten Hauptterme.

Für die Skalenleiter \(T = M^\theta\), \(H = M^{1-\theta}\):

$$
\mathcal{V}_\theta(M)
\sim \frac{M^{1-\theta}}{M} \log\frac{M}{M^{1-\theta}}
= M^{-\theta} \cdot \theta \log M.
$$

An der **selbstdualen Skala** \(H = \sqrt{M}\) (\(\theta = 1/2\)):

$$
\boxed{\mathcal{V}_{1/2}(M) \sim \frac{\log M}{2\sqrt{M}}.}
$$

Das ist ein präziser Testwert für NEU-101.

**Status: \(\warning[M]\)** (Goldston\u2013Montgomery unter RH; nicht bedingunsglos bewiesen)

---

## Satz NEU-101.2 — Transferlemma (Ziel)

Das Transferlemma verbindet die Shift-Residual-Varianz mit der Kurzintervallvarianz:

$$
\mathcal{V}_{N,H}^{\Delta}
:= \frac{1}{H} \sum_{|h| \leq H} |\Delta_N(h)|^2
\quad\stackrel{?}{\sim}\quad
\frac{H}{M_N} \log\frac{M_N}{H}.
$$

Die formale Identifikation läuft über:

$$
\sum_{m \sim M_N} \Lambda(m)\Lambda(m+h)
\longleftrightarrow
\int_M^{2M} (\psi(x+h) - \psi(x)) \, dx / M,
$$

d.h. die Summation über \(m\) entspricht einer dyadischen Mittelung des Kurzintervalls.

**Offene Punkte:**
- Die Sum-Integral-Approximation trägt Fehlerterme der Größe \(O(\sqrt{M_N})\)
- Randbeschnitt von \(m \sim M_N\) vs.\ \(x \in [M,2M]\) muss abgeglichen werden
- Glättungsgewicht \(\omega\) muss mit dem dyadischen Integral kompatibel sein

**Status: \(?[O]\)** (zentraler offener Schritt für NEU-101)

---

## Satz NEU-101.3 — Skalenabhängiger Testwert

Falls das Transferlemma gilt, liefert die Skalenleiter die folgende Wertetabelle:

| \(\theta\) | \(H = M^{1-\theta}\) | \(\mathcal{V}_\theta(M)\) |
|---|---|---|
| \(1/4\) | \(M^{3/4}\) | \(\sim \frac{1}{4} M^{-1/4} \log M\) |
| \(1/2\) | \(\sqrt{M}\) | \(\sim \frac{1}{2} M^{-1/2} \log M\) |
| \(3/4\) | \(M^{1/4}\) | \(\sim \frac{3}{4} M^{-3/4} \log M\) |

Der \(\theta\)-Faktor im Hauptterm ist kein Nebendetail: Er codiert, wie stark das Fenster \(H\) in die logarithmische Struktur eingreift.

**Status: \(\warning[M]\)** (bedingt unter Transferlemma)

---

## Satz NEU-101.4 — Kein direkter Sprung \(\Delta_N \to Q_{\mathrm{Weil}}\)

Die Kette muss sequentiell laufen:

$$
\Delta_N(h)
\;\longrightarrow\;
\underbrace{\mathcal{V}_{N,H}^{\Delta} \stackrel{?}{\sim} \frac{H}{M}\log\frac{M}{H}}_{\text{Transferlemma (NEU-101)}}
\;\longrightarrow\;
\underbrace{\text{Spektralvergleich Montgomery}}_{\text{NEU-102}}
\;\longrightarrow\;
\underbrace{Q_{\mathrm{Weil}}}_{\text{später}}.
$$

Der direkte Sprung \(\Delta_N(h) \to Q_{\mathrm{Weil}}\) bleibt ausgeschlossen.

$$
\boxed{\mathcal{V}_{N,H}^{\Delta} \sim \frac{H}{M}\log\frac{M}{H} \text{ ist der notwendige erste Test.}}
$$

Wenn dieser Test scheitert, ist \(\Delta_N\) nicht der richtige Weil-Kanal. Wenn er gelingt, öffnet NEU-102 den Spektralvergleich mit Montgomery-Paarkorrelation.

**Status: \(\checkmark[M]\)** (methodische Schutzkorrektur)

---

## Neue Leitfrage für NEU-102

$$
\boxed{\text{Stimmt die spektrale Dichte von }\mathcal{E}_{N,H}\text{ mit Montgomery-Paarkorrelation überein?}}
$$

Konkrete Schritte:
1. Goldston\u2013Montgomery: Varianzformel \(\leftrightarrow\) Nullstellenpaarkorrelation unter RH
2. Spektrale Dichte von \(\mathcal{E}_{N,H}(\tau)\): Montgomery-Ansatz \(r(u) = 1 - (\sin(\pi u)/(\pi u))^2\)?
3. Falls ja: Schnittstelle zu \(Q_{\mathrm{Weil}}\) über Connes-Spurformel

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\mathcal{V}(M,H) \sim (H/M)\log(M/H)\) (G.-M. unter RH) | \(\warning[M]\) |
| (B) | \(\mathcal{V}_\theta(M) \sim M^{-\theta} \theta \log M\) | \(\warning[M]\) |
| (C) | Testwert: \(\mathcal{V}_{1/2}(M) \sim \log M / (2\sqrt{M})\) | \(\warning[M]\) |
| (D) | Transferlemma \(\mathcal{V}_{N,H}^\Delta \sim \mathcal{V}(M,H)\) | \(?[O]\) |
| (E) | Kein Direktsprung \(\Delta_N \to Q_{\mathrm{Weil}}\) | \(\checkmark[M]\) |

---

## Verweise

- **Goldston & Montgomery:** *Pair correlation of zeros and primes in short intervals* (1987) \(\leftarrow\) Hauptquelle
- **Chan:** *Short intervals containing numbers with at most two prime factors* (2003) (zweite Hauptterme)
- Montgomery: *The pair correlation of zeros of the zeta function* (1973)
- NEU-100: \(\mathcal{V}_{N,H}\), \(\Delta_N(h)\) Definitionen
- NEU-97: Skalenleiter \(T = M_N^\theta\)
- Connes: *Trace formula in noncommutative geometry* (1999) (spätere Weil-Brücke)
