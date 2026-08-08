# NEU-107 — Lokale Formfaktor-Annahme und Rampen-Äquivalenz

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe C, Patch 3/5)
**Vorgänger:** NEU-106 (No-Go punktweise Nullstellenformel; \(\mathcal{E}_{N,H}\) Träger; RH \(\not\Rightarrow\) GUE-Rampe)
**Nächste Nummer:** NEU-108

---

## Ausgangspunkt

NEU-106 zeigt: Der Rampen-Test benötigt eine Paarstatistik-Annahme, die über RH allein hinausgeht. NEU-107 isoliert die minimal nötige Annahme präzise und bestimmt ihren Charakter.

---

## Definition NEU-107.1 — Lokale Formfaktor-Annahme \(\mathrm{LFF}_{N,H}(A)\)

Für festes \(0 < A \leq 1\) und jede kompakt getragene Testfunktion \(\Phi\) mit \(\mathrm{supp}\,\Phi \subset (-A, A)\) gelte nach korrekter Entfaltung (NEU-103):

$$
\boxed{
\mathrm{LFF}_{N,H}(A):\quad
\int_{-A}^{A}\Phi(\alpha)\,\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)\,d\alpha
\sim c_{N,H}\int_{-A}^{A}\Phi(\alpha)\,|\alpha|\,d\alpha
}
$$

für eine von \(\Phi\) unabhängige Konstante \(c_{N,H} > 0\).

**Status:** Definition

---

## ~~Satz NEU-107.2 (ursprünglich)~~ — ~~Rampen-Äquivalenz~~ — **×[M] SUPERSEDED**

> **Audit-Befund (Pass-A, 8. Aug. 2026):** Die ursprüngliche Biimplikation
>
> $$\mathrm{LFF}_{N,H}(A) \;\Longleftrightarrow\; R_{N,H,A}(\varepsilon) \sim \varepsilon^2/A^2$$
>
> ist **als Biimplikation ×[M]**. Die Rückwärtsrichtung
> \(R(\varepsilon) \sim \varepsilon^2/A^2 \Rightarrow \mathrm{LFF}\)
> ist nicht bewiesen und im Allgemeinen falsch:
> \(R(\varepsilon)\) kontrolliert nur die Masse symmetrischer Intervalle um 0;
> viele verschiedene Maße/Spektralprofile können dieselbe \(\varepsilon\)-Massenasymptotik besitzen,
> ohne distributionell das Profil \(|\alpha|\) zu haben.

## Satz NEU-107.2 (korrigiert) — Einseitige Implikation

$$
\boxed{\mathrm{LFF}_{N,H}(A) \;\Rightarrow\; R_{N,H,A}(\varepsilon) \sim \frac{\varepsilon^2}{A^2}. \quad \checkmark[M]}
$$

$$
\boxed{R_{N,H,A}(\varepsilon) \sim \frac{\varepsilon^2}{A^2} \;\not\Rightarrow\; \mathrm{LFF}_{N,H}(A). \quad \times[M]}
$$

Der Rampen-Test \(R \sim \varepsilon^2/A^2\) ist eine **notwendige, aber nicht hinreichende** Bedingung für \(\mathrm{LFF}\).

**Status: ✓[M]** (Vorwärtsrichtung) + **×[M]** (Rückwärtsrichtung zurückgezogen)

---

## ~~Satz NEU-107.3 (ursprünglich)~~ — ~~Stärke-Hierarchie~~ — **×[M] als Satz**

> **Audit-Befund (Pass-A, 8. Aug. 2026):** Die ursprüngliche strikte Ordnung
>
> $$\mathrm{RH} < \text{Varianzskala} < \mathrm{LFF}_{N,H}(A) < \text{volle Montgomery/GUE-Paarstatistik}$$
>
> als bewiesener Satz ist **×[M]**. Goldston–Montgomery (1987) zeigt unter RH eine Äquivalenz
> zwischen starker Paarkorrelationsaussage und Varianzaussagen in Kurzintervallen;
> eine einfache Richtungsordnung Varianz < Paarkorrelation darf nicht als
> allgemeine mathematische Hierarchie etablierter Vermutungsstärken postuliert werden,
> ohne präzise Definitionen aller Terme.

## Bemerkung NEU-107.3 (korrigiert) — Informationsgehalt

Eine einzelne skalare Varianzbeobachtung bei einer Skala \((M,H)\) enthält weniger strukturelle Information über das lokale Spektralprofil als eine distributionelle Formfaktorannahme \(\mathrm{LFF}_{N,H}(A)\) für alle kompakt getragenen Testfunktionen. Das ist eine **Informations- und Typaussage**, kein bewiesener Satz über Vermutungsstärken.

**Status: ?[O]** (als allgemeine Stärkehierarchie unbewiesen; Informationsinhalt plausibel aber nicht als Satz formulierbar)

---

## Satz NEU-107.4 — Implikation

$$
\text{explizite Formel} + \mathrm{LFF}_{N,H}(A)
\;\Longrightarrow\;
\text{NEU-105-Rampe } R \sim \varepsilon^2/A^2.
$$

Ohne \(\mathrm{LFF}_{N,H}(A)\) kann die korrekte Varianzskala durch ein Poisson-artiges Plateau entstehen und wäre dann kein Weil-Signal.

**Status: ✓[M]**

---

## Satz NEU-107.5 (korrigiert) — Goldston–Montgomery-Kanal und LFF

> **Patch-Notiz:** Die ursprüngliche Fassung verwendete die falsche Normierung
> \((H/M)\log(M/H)\) aus dem nicht-gepatchten NEU-101.1.
> Nach Patch von NEU-101 (Patch 1/5) lautet die korrekte Goldston–Montgomery-Formel:

$$
\mathcal{V}(M,H) \sim H\log\frac{M}{H}.
$$

Diese Formel liefert ein **skalares zweites Moment**. Ob daraus \(\mathrm{LFF}_{N,H}(A)\) (lokales Spektralprofil für alle Testfunktionen) folgt, hängt davon ab, ob die volle Paarkorrelationsstruktur mitgeführt wird — das ist im Goldston–Montgomery-Transfer offen.

**Status: ✓[M]** (Normierung korrigiert) + **?[O]** (Transferinterpretation)

---

## Tabellarische Statusklassifikation (korrigiert)

| Satz | Inhalt | Status |
|------|--------|--------|
| 107.1 | \(\mathrm{LFF}_{N,H}(A)\) Definition | Def. |
| 107.2 | LFF \(\Rightarrow\) Rampe ✓[M]; Umkehrung ×[M] | ✓[M] + ×[M] |
| 107.3 | Informations-/Typaussage (kein Satz) | ?[O] |
| 107.4 | expl. + LFF \(\Rightarrow\) Rampe | ✓[M] |
| 107.5 | GM-Normierung korrigiert auf \(H\log(M/H)\); Transfer offen | ✓[M] + ?[O] |

---

## Verweise

- NEU-106: No-Go punktweise; epistemisch RH \(\not\Rightarrow\) GUE
- NEU-105: Binärer Rampen-Test \(R \sim \varepsilon^2/A^2\)
- NEU-104: \(\mathcal{P}^{\mathrm{unf}}_{N,H}\) und No-Go global (korrigiert)
- **NEU-101 (Patch 1/5):** Goldston–Montgomery-Normierung \(H\log(M/H)\) (korrigiert)
- **Goldston & Montgomery:** *Pair correlation of zeros and primes in short intervals* (1987)
- **Chan:** *Short intervals* (2003)
- Connes: *Trace formula* (1999)
- Keating & Snaith: *Random matrix theory and L-functions* (2000)
