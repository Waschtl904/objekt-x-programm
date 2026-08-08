# NEU-101 — Goldston–Montgomery-Transfer und Varianzkanal

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe C, Patch 1/5)
**Vorgänger:** NEU-100 (\(\mathcal{V}_{N,H}\), \(R_{N,H}(k)\); Nullstellenpaar-Kanal nur in \(|\widehat{\Delta}_N|^2\))
**Nächste Nummer:** NEU-102

---

## Ausgangspunkt

NEU-100 zeigt: Der erste plausible Weil-Kandidat ist das Shift-Spektrum \(|\widehat{\Delta}_N|^2\) bzw.\ \(\mathcal{V}_{N,H}\). NEU-101 stellt dieses Objekt dem klassischen Goldston–Montgomery-Varianzkanal gegenüber.

**Normalisierungskorrektur:** Die klassische Goldston–Montgomery-Formel gilt für den Kurzintervallfehler \(\psi(x+H)-\psi(x)-H\), nicht unmittelbar für \(\Delta_N(h)\). Ein Transferlemma ist nötig.

---

## ~~Satz NEU-101.1 (ursprünglich)~~ — **×[M] SUPERSEDED**

> **Audit-Befund (Pass-A, 8. Aug. 2026):** Die ursprüngliche Formel
>
> $$\mathcal{V}(M, H) := \frac{1}{M}\int_M^{2M}(\psi(x+H)-\psi(x)-H)^2\,dx \sim \frac{H}{M}\log\frac{M}{H}$$
>
> ist **falsch normiert**. Die \(1/M\)-Normierung steht bereits auf der linken Seite; der Hauptterm auf der rechten Seite fehlt daher um den Faktor \(M\). Korrekte Formel:
>
> $$\boxed{\mathcal{V}(M, H) \sim H\log\frac{M}{H}.}$$
>
> Ebenso war der selbstduale Testwert bei \(H = \sqrt{M}\) falsch:
> \(\mathcal{V}_{1/2}(M) \sim \frac{\log M}{2\sqrt{M}}\) **×[M]** — korrigiert:
>
> $$\boxed{\mathcal{V}_{1/2}(M) \sim \tfrac{1}{2}\sqrt{M}\log M.}$$

## Satz NEU-101.1 (korrigiert) — Kurzintervallvarianz (Goldston–Montgomery)

Der Hauptterm der dyadischen Kurzintervallvarianz lautet:

$$
\mathcal{V}(M, H)
:= \frac{1}{M} \int_M^{2M}
\left(\psi(x+H) - \psi(x) - H\right)^2 dx
\sim H\log\frac{M}{H}.
$$

Dies gilt bedingt unter RH (Goldston–Montgomery 1987). Chan (2003) präzisiert die zweiten Hauptterme.

Für die Skalenleiter \(T = M^\theta\), \(H = M^{1-\theta}\):

$$
\mathcal{V}_\theta(M) \sim M^{1-\theta}\cdot\theta\log M.
$$

An der **selbstdualen Skala** \(H = \sqrt{M}\) (\(\theta = 1/2\)):

$$
\boxed{\mathcal{V}_{1/2}(M) \sim \tfrac{1}{2}\sqrt{M}\log M.}
$$

**Status: ✓[M]** (unter RH; Normierung korrigiert)

---

## Satz NEU-101.2 — Transferlemma (Ziel, offen)

Das Transferlemma verbindet die Shift-Residual-Varianz mit der Kurzintervallvarianz:

$$
\mathcal{V}_{N,H}^{\Delta}
:= \frac{1}{H} \sum_{|h| \leq H} |\Delta_N(h)|^2
\quad\stackrel{?}{\sim}\quad
H\log\frac{M_N}{H}.
$$

Die formale Identifikation läuft über:

$$
\sum_{m \sim M_N} \Lambda(m)\Lambda(m+h)
\longleftrightarrow
\int_M^{2M} (\psi(x+h) - \psi(x))\,dx / M,
$$

d.h. die Summation über \(m\) entspricht einer dyadischen Mittelung des Kurzintervalls.

**Offene Punkte:**
- Die Sum-Integral-Approximation trägt Fehlerterme der Größe \(O(\sqrt{M_N})\)
- Randbeschnitt von \(m \sim M_N\) vs.\ \(x \in [M,2M]\) muss abgeglichen werden
- Glättungsgewicht \(\omega\) muss mit dem dyadischen Integral kompatibel sein

**Status: ?[O]** (zentraler offener Schritt für NEU-101)

---

## Satz NEU-101.3 — Skalenabhängiger Testwert (korrigiert)

| \(\theta\) | \(H = M^{1-\theta}\) | \(\mathcal{V}_\theta(M)\) |
|---|---|---|
| \(1/4\) | \(M^{3/4}\) | \(\sim \frac{1}{4} M^{3/4} \log M\) |
| \(1/2\) | \(\sqrt{M}\) | \(\sim \frac{1}{2} \sqrt{M} \log M\) |
| \(3/4\) | \(M^{1/4}\) | \(\sim \frac{3}{4} M^{1/4} \log M\) |

> **Patch-Notiz:** Die ursprünglichen Einträge (z.B. \(\frac{1}{2}M^{-1/2}\log M\)) waren um den Faktor \(M\) zu klein. Korrigierte Werte entsprechen \(\mathcal{V}_\theta(M) \sim M^{1-\theta}\theta\log M\).

**Status: ✓[M]** (bedingt unter Transferlemma und korrigierter GM-Formel)

---

## Satz NEU-101.4 — Kein direkter Sprung \(\Delta_N \to Q_{\mathrm{Weil}}\)

Die Kette muss sequentiell laufen:

$$
\Delta_N(h)
\;\longrightarrow\;
\underbrace{\mathcal{V}_{N,H}^{\Delta} \stackrel{?}{\sim} H\log\frac{M}{H}}_{\text{Transferlemma (NEU-101)}}
\;\longrightarrow\;
\underbrace{\text{Spektralvergleich Montgomery}}_{\text{NEU-102}}
\;\longrightarrow\;
\underbrace{Q_{\mathrm{Weil}}}_{\text{später}}.
$$

**Status: ✓[M]** (methodische Schutzaussage; unabhängig von Normierungsfrage)

---

## Neue Leitfrage für NEU-102

$$
\boxed{\text{Stimmt die spektrale Dichte von }\mathcal{E}_{N,H}\text{ mit Montgomery-Paarkorrelation überein?}}
$$

Konkrete Schritte:
1. Goldston–Montgomery: Varianzformel \(\leftrightarrow\) Nullstellenpaarkorrelation unter RH
2. Spektrale Dichte von \(\mathcal{E}_{N,H}(\tau)\): Montgomery-Ansatz \(r(u) = 1 - (\sin(\pi u)/(\pi u))^2\)?
3. Falls ja: Schnittstelle zu \(Q_{\mathrm{Weil}}\) über Connes-Spurformel

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\mathcal{V}(M,H) \sim H\log(M/H)\) (G.-M. unter RH) — **korrigiert** | ✓[M] (konditional) |
| (B) | \(\mathcal{V}_\theta(M) \sim M^{1-\theta}\theta\log M\) — **korrigiert** | ✓[M] (konditional) |
| (C) | Testwert: \(\mathcal{V}_{1/2}(M) \sim \frac{1}{2}\sqrt{M}\log M\) — **korrigiert** | ✓[M] (konditional) |
| (D) | Transferlemma \(\mathcal{V}_{N,H}^\Delta \sim \mathcal{V}(M,H)\) | ?[O] |
| (E) | Kein Direktsprung \(\Delta_N \to Q_{\mathrm{Weil}}\) | ✓[M] |

---

## Verweise

- **Goldston & Montgomery:** *Pair correlation of zeros and primes in short intervals* (1987) ← Hauptquelle
- **Chan:** *Short intervals containing numbers with at most two prime factors* (2003)
- Montgomery: *The pair correlation of zeros of the zeta function* (1973)
- NEU-100: \(\mathcal{V}_{N,H}\), \(\Delta_N(h)\) Definitionen
- NEU-97: Skalenleiter \(T = M_N^\theta\)
- Connes: *Trace formula in noncommutative geometry* (1999)
