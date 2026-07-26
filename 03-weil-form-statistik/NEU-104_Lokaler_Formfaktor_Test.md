# NEU-104 — Lokaler Formfaktor-Test in der entfalteten Variable

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-103 (Entfaltungskarte \(\gamma \sim \tau T\); \(\rho_T = \log T/2\pi\); \(\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha)\))  
**Nächste Nummer:** NEU-105

---

## Ausgangspunkt

NEU-103 liefert die korrekte Entfaltungskarte \(\alpha = \tau T \rho_T\). NEU-104 präzisiert, in welchem Sinn der Formfaktorvergleich formuliert werden darf.

**Schutzsatz vorweg:** Der Montgomery/GUE-Formfaktor \(K(\alpha) = |\alpha|\mathbf{1}_{|\alpha|\leq 1} + \mathbf{1}_{|\alpha|>1}\) ist auf \(\mathbb{R}\) **nicht integrierbar**. Ein global normiertes Spektralprofil kann nicht gegen \(K\) konvergieren.

---

## Satz NEU-104.1 — No-Go: Globaler Formfaktorvergleich

$$
\boxed{\text{Ein global normiertes Spektralprofil }\mathcal{S}^{\mathrm{unf}}_{N,H}\text{ (Gesamtmasse 1) kann nicht global gegen }K(\alpha)\text{ konvergieren.}}
$$

Begründung: Die entfaltete normierte Dichte ist

$$
\frac{1}{T\rho_T}\mathcal{S}_{N,H}\!\left(\frac{\alpha}{T\rho_T}\right),
$$

mit Gesamtmasse \(1\). Aber \(\int_{-\infty}^{\infty} K(\alpha)\,d\alpha = +\infty\). Globale Konvergenz ist dimensionswidrig.

**Status: \(\checkmark[M]\)** (No-Go)

---

## Definition NEU-104.2 — Unnormalisiertes entfaltetes Leistungsspektrum

Definiere das **unnormalisierte** entfaltete Leistungsspektrum:

$$
\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)
:= \left|\mathcal{E}_{N,H}\!\left(\frac{\alpha}{T\rho_T}\right)\right|^2 \cdot \frac{1}{T\rho_T},
$$

wobei \(\alpha = \tau T\rho_T\), \(T = M/H\), \(\rho_T = \log T/2\pi\).

Dieses Objekt trägt keine globale Normierung und kann lokal gegen \(K(\alpha)\) verglichen werden.

**Status: \(\checkmark[M]\)** (Definition)

---

## Satz NEU-104.3 — Lokaler/distributioneller Formfaktor-Test

Der korrekte Formfaktortest ist **lokal**: Für kompakt getragene Testfunktionen \(\Phi \in C_c^\infty(\mathbb{R})\):

$$
\int \Phi(\alpha)\,\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha
\;\stackrel{?}{\longrightarrow}\;
c \int \Phi(\alpha)\,K(\alpha)\,d\alpha,
$$

für eine von \(\Phi\) unabhängige Normierungskonstante \(c = c_{N,H}\).

**Äquivalente Fensterversion:** Auf festem Fenster \([-A, A]\):

$$
\mathcal{S}^{\mathrm{unf}}_{N,H,A}(\alpha)
:= \frac{\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)}{\int_{-A}^{A}\mathcal{P}^{\mathrm{unf}}_{N,H}(u)\,du}
\;\stackrel{?}{\longrightarrow}\;
K_A(\alpha) := \frac{K(\alpha)}{\int_{-A}^{A} K(u)\,du}.
$$

Dann lautet der **Montgomery-Test**:

$$
\mathcal{S}^{\mathrm{unf}}_{N,H,A} \;\stackrel{?}{\longrightarrow}\; K_A
\quad\text{für jedes feste }A,
$$

unter der Entfaltung \(\alpha = \tau T \log T / 2\pi\).

**Status: \(?[O]\)** (Test offen)

---

## Satz NEU-104.4 — GUE vs. Poisson: Rampe-Plateau-Test

Der entscheidende diagnostische Test ist das Verhalten bei kleinen \(\alpha\):

| Statistik | Formfaktor | Verhalten bei \(\alpha \approx 0\) |
|---|---|---|
| Poisson (unkorreliert) | \(K_{\mathrm{Pois}}(\alpha) = 1\) | Plateau |
| GUE / Montgomery | \(K_{\mathrm{GUE}}(\alpha) \sim |\alpha|\) | **Rampe** (Nullstellenrepulsion) |

$$
\boxed{K_{\mathrm{GUE}}(\alpha) \sim |\alpha| \text{ bei } \alpha \approx 0 \quad\text{vs.}\quad K_{\mathrm{Pois}}(\alpha) = 1.}
$$

Wenn das entfaltete Rest-Spektrum \(\mathcal{P}^{\mathrm{unf}}_{N,H}\) bei kleinem \(\alpha\) **nicht abfällt** (Plateau statt Rampe), ist der Restkanal Poisson-artig und **nicht** Montgomery-kompatibel.

**Status: \(?[O]\)** (Entscheidungstest, NEU-105)

---

## Satz NEU-104.5 — Bogomolny\u2013Keating: Semiklassische Deutung

Bogomolny\u2013Keating arbeiten in der Random-Matrix-/Trace-Formula-Analogie der Riemann-Nullstellen. Das ist strukturell relevant als **semiklassische Deutung** der Formfaktorstruktur, aber **kein Ersatz** für den Goldston\u2013Montgomery-Transfer.

| Kanal | Rolle | Status |
|---|---|---|
| Goldston\u2013Montgomery | arithmetischer Transferkanal (Varianz \(\leftrightarrow\) Paarkorr.) | Primär \(\warning[M]\) |
| Bogomolny\u2013Keating | semiklassische Deutung der Formfaktorstruktur | Heuristisch \(?[H]\) |

**Status: \(?[H]\)** (heuristisch; nicht als Beweisschritt zitiern)

---

## Gesamte Kette (NEU-100 bis 104)

$$
\Delta_N(h)
\;\longrightarrow\;
\mathcal{E}_{N,H}(\tau)
\;\longrightarrow\;
\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)
\;\stackrel{?}{\longrightarrow}\;
K_A(\alpha)
\;\stackrel{?}{\longrightarrow}\;
Q_{\mathrm{Weil}}.
$$

Schritt \(\mathcal{P}^{\mathrm{unf}} \to K_A\): lokal, gegen Testfunktionen oder Fenster \([-A,A]\).  
Schritt \(K_A \to Q_{\mathrm{Weil}}\): später (NEU-106+).

---

## Neue Leitfrage für NEU-105

$$
\boxed{\text{Rampe oder Plateau? }\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\text{ bei }\alpha \approx 0.}
$$

Konkrete Schritte:
1. Explizite-Formel-Entwicklung von \(\Delta_N(h)\) bis zu Termen \(\sum_\rho M_N^{\rho-1} e^{i\gamma h/M}\)
2. Paarweise \(|\sum_\rho|^2\)-Terme bei \(\alpha \approx 0\) auswerten
3. Vergleich mit \(K_{\mathrm{GUE}}(\alpha) \sim |\alpha|\)

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | No-Go: globaler \(\mathcal{S}^{\mathrm{unf}} \to K\) | \(\checkmark[M]\) |
| (B) | \(\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\) unnorm. Leistungsspektrum | \(\checkmark[M]\) (Def.) |
| (C) | Lokaler Test mit \(\Phi\) oder Fenster \([-A,A]\) | \(\checkmark[M]\) (Def.) |
| (D) | \(\mathcal{S}^{\mathrm{unf}}_{N,H,A} \to K_A\) | \(?[O]\) |
| (E) | GUE Rampe \(\sim|\alpha|\) vs.\ Poisson Plateau | \(?[O]\) (NEU-105) |
| (F) | BK semiklassisch, heuristisch | \(?[H]\) |

---

## Verweise

- NEU-103: Entfaltungskarte \(\alpha = \tau T\rho_T\)
- NEU-102: No-Go direkter \(r(u)\)-Vergleich
- **Montgomery:** *Pair correlation of zeros* (1973)
- **Goldston & Montgomery:** *Pair correlation, primes in short intervals* (1987)
- **Montgomery & Soundararajan:** *Primes in short intervals* (2004)
- Bogomolny & Keating: *Gutzwiller's trace formula* (heuristisch)
- Keating & Snaith: *Random matrix theory and \(L\)-functions* (2000)
- Connes: *Trace formula* (1999) (spätere Weil-Schnittstelle)
