# NEU-104 — Lokaler Formfaktor-Test in der entfalteten Variable

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe C, Patch 2/5)
**Vorgänger:** NEU-103 (Entfaltungskarte \(\gamma \sim \tau T\); \(\rho_T = \log T/2\pi\); \(\mathcal{S}^{\mathrm{unf}}_{N,H}(\alpha)\))
**Nächste Nummer:** NEU-105

---

## Ausgangspunkt

NEU-103 liefert die korrekte Entfaltungskarte \(\alpha = \tau T \rho_T\). NEU-104 präzisiert, in welchem Sinn der Formfaktorvergleich formuliert werden darf.

**Schutzsatz vorweg:** Der Montgomery/GUE-Formfaktor \(K(\alpha) = |\alpha|\mathbf{1}_{|\alpha|\leq 1} + \mathbf{1}_{|\alpha|>1}\) ist auf \(\mathbb{R}\) **nicht integrierbar** (\(\int_{\mathbb{R}} K(\alpha)\,d\alpha = +\infty\)). Ein global normiertes Spektralprofil mit Gesamtmasse 1 kann daher nicht gegen \(K\) konvergieren.

---

## Satz NEU-104.1 — No-Go: Globaler Formfaktorvergleich

**Abstrakter Kern (repariert):**

$$
\boxed{\text{Kein nicht-negatives normiertes Maß mit Gesamtmasse 1 kann schwach gegen }K(\alpha)\text{ konvergieren, da }\int_{\mathbb{R}}K(\alpha)\,d\alpha = +\infty.}
$$

Dieser No-Go gilt **unabhängig von der konkreten Wahl des Spektralprofils** und erfordert kein spezifisches Eingabeobjekt.

> **Patch-Notiz (Pass-A, 8. Aug. 2026):** Die ursprüngliche Fassung dieses Satzes verwendete die normierte Dichte \(\mathcal{S}_{N,H}\) aus NEU-102.1 als konkretes Objekt. Da \(\mathcal{E}_{N,H}(\tau)\) ein endliches trigonometrisches Polynom und damit periodisch ist, gilt
>
> $$\int_{\mathbb{R}}|\mathcal{E}_{N,H}(\tau)|^2\,d\tau = \infty,$$
>
> sofern \(\mathcal{E}_{N,H}\not\equiv 0\). Der Nenner im Ausdruck für \(\mathcal{S}_{N,H}\) ist daher undefiniert.
>
> **\(\mathcal{S}_{N,H}\) aus NEU-102.1 als globale \(L^2(\mathbb{R})\)-Normierung: SUPERSEDED.**
>
> Der abstrakte No-Go (Gesamtmasse 1 gegen nichtintegrierbares \(K\)) bleibt vollständig gültig: **✓[M]_part** in aktueller Fassung; nach expliziter Retypisierung auf ein Periodenmittel oder endliches Fenster: **✓[M]_neg**.

**Status: ✓[M]_part** (abstraktes No-Go korrekt; Typisierung auf \(\mathcal{S}_{N,H}\) SUPERSEDED)

---

## Definition NEU-104.2 — Unnormalisiertes entfaltetes Leistungsspektrum

Das korrekte Ersatzobjekt (unabhängig von \(\mathcal{S}_{N,H}\)) ist das **unnormalisierte** entfaltete Leistungsspektrum:

$$
\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)
:= \left|\mathcal{E}_{N,H}\!\left(\frac{\alpha}{T\rho_T}\right)\right|^2 \cdot \frac{1}{T\rho_T},
$$

wobei \(\alpha = \tau T\rho_T\), \(T = M/H\), \(\rho_T = \log T/2\pi\).

Dieses Objekt trägt keine globale Normierung und ist für lokalen Vergleich mit \(K(\alpha)\) auf kompakten Fenstern geeignet.

**Status: ✓[M]** (Definition; gültiges Ersatzobjekt für SUPERSEDED \(\mathcal{S}_{N,H}\))

---

## Satz NEU-104.3 — Lokaler/distributioneller Formfaktor-Test

Der korrekte Formfaktortest ist **lokal**: Für kompakt getragene Testfunktionen \(\Phi \in C_c^\infty(\mathbb{R})\):

$$
\int \Phi(\alpha)\,\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha
\;\stackrel{?}{\longrightarrow}\;
c \int \Phi(\alpha)\,K(\alpha)\,d\alpha,
$$

für eine von \(\Phi\) unabhängige Konstante \(c = c_{N,H}\).

**Fensterversion:** Auf festem Fenster \([-A, A]\):

$$
\mathcal{S}^{\mathrm{unf}}_{N,H,A}(\alpha)
:= \frac{\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)}{\int_{-A}^{A}\mathcal{P}^{\mathrm{unf}}_{N,H}(u)\,du}
\;\stackrel{?}{\longrightarrow}\;
K_A(\alpha) := \frac{K(\alpha)}{\int_{-A}^{A} K(u)\,du}.
$$

**Status: ✓[M]** (Definition; Test offen)

---

## Satz NEU-104.4 — GUE vs. Poisson: Rampe-Plateau-Test

| Statistik | Formfaktor | Verhalten bei \(\alpha \approx 0\) |
|---|---|---|
| Poisson | \(K_{\mathrm{Pois}}(\alpha) = 1\) | Plateau |
| GUE / Montgomery | \(K_{\mathrm{GUE}}(\alpha) \sim |\alpha|\) | Rampe |

$$
\boxed{K_{\mathrm{GUE}}(\alpha) \sim |\alpha| \text{ bei } \alpha \approx 0 \quad\text{vs.}\quad K_{\mathrm{Pois}}(\alpha) = 1.}
$$

**Status: ?[O]** (Entscheidungstest \(\to\) NEU-105)

---

## Satz NEU-104.5 — Bogomolny–Keating: Semiklassische Deutung

| Kanal | Rolle | Status |
|---|---|---|
| Goldston–Montgomery | arithmetischer Transferkanal | Primär ✓[M] (konditional) |
| Bogomolny–Keating | semiklassische Deutung | Heuristisch ?[H] |

**Status: ?[H]** (heuristisch; nicht als Beweisschritt zitieren)

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | No-Go: kein global normiertes Maß \(\to K\) — abstrakt korrekt; \(\mathcal{S}_{N,H}\) SUPERSEDED | ✓[M]_part |
| (B) | \(\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\) unnorm. Leistungsspektrum (gültiges Ersatzobjekt) | ✓[M] |
| (C) | Lokaler Test mit \(\Phi\) oder Fenster \([-A,A]\) | ✓[M] |
| (D) | \(\mathcal{S}^{\mathrm{unf}}_{N,H,A} \to K_A\) | ?[O] |
| (E) | GUE Rampe \(\sim|\alpha|\) vs.\ Poisson Plateau | ?[O] |
| (F) | BK semiklassisch, heuristisch | ?[H] |

---

## Verweise

- NEU-103: Entfaltungskarte \(\alpha = \tau T\rho_T\)
- **NEU-102:** \(\mathcal{S}_{N,H}\) — globale \(L^2(\mathbb{R})\)-Normierung **SUPERSEDED** (Integrabilitatsfehler)
- **Montgomery:** *Pair correlation of zeros* (1973)
- **Goldston & Montgomery:** *Pair correlation, primes in short intervals* (1987)
- **Montgomery & Soundararajan:** *Primes in short intervals* (2004)
- Bogomolny & Keating: *Gutzwiller's trace formula* (heuristisch)
- Keating & Snaith: *Random matrix theory and L-functions* (2000)
- Connes: *Trace formula* (1999)
