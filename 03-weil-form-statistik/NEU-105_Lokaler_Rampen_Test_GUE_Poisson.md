# NEU-105 — Lokaler Rampen-Test: GUE oder Poisson?

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-104 (No-Go global; \(\mathcal{P}^{\mathrm{unf}}_{N,H}\); Fenstertest \(\mathcal{S}^{\mathrm{unf}}_{N,H,A} \to K_A\); GUE-Rampe vs.\ Poisson-Plateau)  
**Nächste Nummer:** NEU-106

---

## Ausgangspunkt

NEU-104 definiert den lokalen Formfaktortest. NEU-105 macht den Restkanal **erstmals falsifizierbar**: Nicht „Ist das irgendwie Montgomery-kompatibel?“, sondern exakt:

$$
\boxed{R_{N,H,A}(\varepsilon) \stackrel{?}{\sim} \frac{\varepsilon^2}{A^2} \quad\text{(GUE)} \quad\text{statt}\quad \frac{\varepsilon}{A} \quad\text{(Poisson)}.}
$$

---

## Definition NEU-105.1 — Lokal normierte Fensterdichte

Für festes Fenster \(0 < A \leq 1\) und korrekte Entfaltung \(\alpha = \tau T\rho_T\):

$$
\mathcal{S}^{\mathrm{unf}}_{N,H,A}(\alpha)
:= \frac{\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha)}{\int_{-A}^{A}\mathcal{P}^{\mathrm{unf}}_{N,H}(u)\,du},
\qquad |\alpha| \leq A.
$$

Diese Dichte hat Gesamtmasse 1 auf \([-A,A]\) und ist sinnvoll vergleichbar mit dem fenster-normierten Formfaktor

$$
K_A(\alpha) := \frac{K(\alpha)}{\int_{-A}^{A} K(u)\,du}.
$$

**Status: \(\checkmark[M]\)** (Definition)

---

## Definition NEU-105.2 — Lokales Massengewicht

Für \(0 < \varepsilon < A \leq 1\) setze das lokale Massengewicht nahe \(\alpha = 0\):

$$
R_{N,H,A}(\varepsilon)
:= \int_{-\varepsilon}^{\varepsilon}
\mathcal{S}^{\mathrm{unf}}_{N,H,A}(\alpha)\,d\alpha.
$$

**Status: \(\checkmark[M]\)** (Definition)

---

## Satz NEU-105.3 — Poisson-Test

Unter Poisson-Statistik (unkorrelierte Nullstellen, \(K_{\mathrm{Pois}}(\alpha) = 1\)):

$$
\mathcal{S}^{\mathrm{unf}}_{N,H,A}(\alpha) \to K_{A,\mathrm{Pois}} = \frac{1}{2A}
\quad\Longrightarrow\quad
R_{N,H,A}(\varepsilon) \sim \frac{\varepsilon}{A}.
$$

D.h.\ das Massengewicht wächst **linear** in \(\varepsilon\): Plateau-Profil, keine Repulsion.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-105.4 — GUE/Montgomery-Test

Unter GUE-/Montgomery-Statistik (\(K_{\mathrm{GUE}}(\alpha) \sim |\alpha|\) bei \(\alpha \approx 0\)):

$$
\int_{-A}^{A} |u|\,du = A^2,
\quad
K_{A,\mathrm{GUE}}(\alpha) = \frac{|\alpha|}{A^2}
\quad\Longrightarrow\quad
R_{N,H,A}(\varepsilon) \sim \frac{\varepsilon^2}{A^2}.
$$

D.h.\ das Massengewicht wächst **quadratisch** in \(\varepsilon\): Rampe, Nullstellenrepulsion.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-105.5 — Binärer Falsifizierbarkeitssatz

$$
\boxed{
\text{Plateau bei }\alpha=0\;(R \sim \varepsilon/A)
\quad\Longleftrightarrow\quad
\text{Poisson-artig, kein Montgomery-Signal.}
}
$$
$$
\boxed{
\text{Rampe bei }\alpha=0\;(R \sim \varepsilon^2/A^2)
\quad\Longleftrightarrow\quad
\text{GUE-/Montgomery-artige Repulsion.}
}
$$

Die richtige Varianzskala aus NEU-101 ist **notwendig, aber nicht hinreichend**. Erst die lokale Rampe \(K(\alpha) \sim |\alpha|\) bei \(\alpha \to 0\) zeigt Montgomery-Kompatibilität. Ein korrektes Varianzniveau mit Plateau-Profil ist Poisson-artig und schwächt den Restkanal als Weil-Kandidat.

**Status: \(\checkmark[M]\)** (Falsifizierbarkeitssatz)

---

## Offener Test NEU-105.6

$$
\boxed{\text{Zeigt }\mathcal{P}^{\mathrm{unf}}_{N,H}\text{ Rampe oder Plateau bei }\alpha=0?}
$$

Der Test verlangt eine explizite Entwicklung von \(\Delta_N(h)\) nach der expliziten Formel:

$$
\Delta_N(h) \leadsto \sum_\rho M_N^{\rho-1} e^{i\gamma h/M_N} + \text{Fehlerterme}.
$$

Dann:
1. \(\mathcal{P}^{\mathrm{unf}}_{N,H}(\alpha) \approx \left|\sum_\rho M_N^{\rho-1}\widehat{\omega}(\alpha - \gamma/T)\right|^2 / (T\rho_T)\)
2. Paarweise \(|\sum_{\rho,\rho'} \cdots|^2\)-Terme bei \(\alpha \approx 0\) auswerten
3. Vergleich mit \(K_{\mathrm{GUE}}(\alpha) \sim |\alpha|\)

**Status: \(?[O]\)** \(\leftarrow\) zentraler offener Schritt für NEU-106

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 105.1 | Lokales Fenster \(0<A\leq1\); \(\mathcal{S}^{\mathrm{unf}}_{N,H,A}\) | \(\checkmark[M]\) |
| 105.2 | \(R_{N,H,A}(\varepsilon)\) Massengewicht | \(\checkmark[M]\) |
| 105.3 | Poisson: \(R \sim \varepsilon/A\) | \(\checkmark[M]\) |
| 105.4 | GUE: \(R \sim \varepsilon^2/A^2\) | \(\checkmark[M]\) |
| 105.5 | Falsifizierbarkeitssatz (binär) | \(\checkmark[M]\) |
| 105.6 | Offener Test: Rampe oder Plateau? | \(?[O]\) |

---

## Neue Leitfrage für NEU-106

$$
\boxed{\text{Explizite-Formel-Entwicklung von }\Delta_N(h):\quad \Delta_N(h) \leadsto \sum_\rho M_N^{\rho-1}e^{i\gamma h/M_N}.}
$$

Konkrete Schritte:
1. Perron-Formel / explizite Formel für \(\sum_{m\sim M_N}\Lambda(m)\Lambda(m+h)\)
2. Kontrolle der Fehlerterme (Randbeschnitts-, Glättungs- und Konvergenzfragen)
3. Paarweise Nullstellenbeiträge \(|\sum_{\rho}|^2\) in \(\mathcal{P}^{\mathrm{unf}}\) identifizieren
4. Vergleich des \(\alpha \approx 0\)-Profils mit GUE-Rampe

---

## Verweise

- NEU-104: \(\mathcal{P}^{\mathrm{unf}}_{N,H}\); No-Go global; Fenstertest
- NEU-103: Entfaltungskarte \(\alpha = \tau T\rho_T\)
- NEU-101: Varianzskala \(\mathcal{V}(M,H) \sim (H/M)\log(M/H)\) (notwendig, nicht hinreichend)
- **Montgomery:** *Pair correlation of zeros* (1973)
- **Goldston & Montgomery:** *Pair correlation, primes in short intervals* (1987)
- Keating & Snaith: *Random matrix theory and \(L\)-functions* (2000)
