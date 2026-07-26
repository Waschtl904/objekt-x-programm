# NEU-102 — Formfaktor-Kalibrierung und Montgomery-Spektraltest

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-101 (Goldston\u2013Montgomery-Transfer; \(\mathcal{V}(M,H) \sim (H/M)\log(M/H)\); Transferlemma offen)  
**Nächste Nummer:** NEU-103

---

## Ausgangspunkt

NEU-101 stellt den Varianztest \(\mathcal{V}_{N,H}^{\Delta} \sim (H/M)\log(M/H)\) als ersten notwendigen Test. Selbst wenn dieser Test besteht, folgt daraus **nicht** automatisch eine Montgomery- oder Weil-kompatible Spektralstruktur. NEU-102 kalibriert den zweiten Schritt: den Formfaktor-Vergleich.

**Schutzsatz vorweg:** \(r(u) = 1-(\sin\pi u/\pi u)^2\) ist die Montgomery-Paar**abstands**dichte auf der Nullstellenseite. Das Shift-Spektrum \(|\mathcal{E}_{N,H}(\tau)|^2\) ist eine Fourier-/Formfaktorgröße auf der Primseite. Direkter Vergleich ohne Entfaltung ist unzulässig.

---

## Definition NEU-102.1 — Normierte Spektral-Profildichte

Nach Normierung des zweiten Moments definiere die **spektrale Profildichte**:

$$
\mathcal{S}_{N,H}(\tau)
:= \frac{|\mathcal{E}_{N,H}(\tau)|^2}{\int |\mathcal{E}_{N,H}(u)|^2\, du}.
$$

Das ist eine Wahrscheinlichkeitsdichte in \(\tau\), die die normierte Verteilung der spektralen Masse des Restresiduals beschreibt.

**Status: \(\checkmark[M]\)** (Definition)

---

## Satz NEU-102.2 — No-Go: Direkter Vergleich \(\mathcal{S}_{N,H} \to r(u)\)

Der direkte Grenzwert

$$
|\mathcal{E}_{N,H}(\tau)|^2 \;\stackrel{?}{\longrightarrow}\; 1 - \left(\frac{\sin\pi\tau}{\pi\tau}\right)^2
$$

ist **nicht formulierbar**, solange \(\tau\) nicht korrekt entfaltet ist. Der Grund:

- \(r(u)\) lebt auf der **Nullstellen-Abstandsseite** (normierter Abstand zwischen Zeta-Nullstellen)
- \(\mathcal{S}_{N,H}(\tau)\) lebt auf der **Fourier-/Formfaktorseite** (Spektrum der Shift-Residuen)
- Beide gehören zu verschiedenen Fourier-Dualitäten

$$
\boxed{r(u) \text{ (Abstandsdichte)} \neq |\widehat{\Delta}|^2 \text{ (Spektrum)}
\quad\text{ohne Entfaltungskarte }\tau \mapsto \alpha_N(\tau).}
$$

**Status: \(\checkmark[M]\)** (No-Go)

---

## Satz NEU-102.3 — Montgomery/GUE-Formfaktor auf der dualen Seite

Auf der Fourier-/Formfaktorseite erscheint nicht \(r(u)\), sondern die Ramp-Plateau-Struktur:

$$
K(\alpha) = \begin{cases}
|\alpha|, & |\alpha| \leq 1, \\
1, & |\alpha| \geq 1.
\end{cases}
$$

(bis auf Konventions- und Glättungsfaktoren; GUE-Vorhersage für den Zeta-Nullstellen-Formfaktor)

Der korrekte Vergleich lautet:

$$
\mathcal{S}_{N,H}(\tau)
\;\stackrel{?}{\longrightarrow}\;
K_{\mathrm{Montgomery/GUE}}(\alpha_N(\tau)),
$$

nach geeigneter Entfaltung \(\tau \mapsto \alpha_N(\tau)\).

**Status: \(\warning[M]\)** / \(?[O]\)

---

## Definition NEU-102.4 — Entfaltungskarte (Ziel)

Gesucht ist eine Abbildung

$$
\alpha_N : \mathbb{R} \to \mathbb{R},
\qquad
\tau \mapsto \alpha_N(\tau),
$$

die aus dem Goldston\u2013Montgomery-Transfer bzw.\ der expliziten Formel bestimmt wird und den Shift-Frequenzparameter \(\tau\) mit dem normierten Nullstellenabstand \(\alpha\) identifiziert. Erst nach dieser Karte ist der Formfaktorvergleich mathematisch sinnvoll.

**Offene Punkte:**
- Bestimmung von \(\alpha_N(\tau)\) aus der expliziten Formel (linearer oder logarithmischer Zusammenhang?)
- Konventionsabgleich (Nullstellendichte \(\sim \log M_N / 2\pi\) als Skalierungsfaktor)
- Kompatibilität mit dem Glättungsgewicht \(\omega\)

**Status: \(?[O]\)** (zentraler offener Schritt)

---

## Drei-Ebenen-Architektur

$$
\underbrace{\mathcal{V}_{N,H}^{\Delta} \sim \frac{H}{M}\log\frac{M}{H}}_{\text{Ebene 1: Varianzskala (NEU-101)}}
\;\longrightarrow\;
\underbrace{\mathcal{S}_{N,H}(\tau) \stackrel{?}{\to} K(\alpha_N(\tau))}_{\text{Ebene 2: Formfaktor (NEU-102)}}
\;\longrightarrow\;
\underbrace{Q_{\mathrm{Weil}}}_{\text{Ebene 3 (später)}}
$$

| Ebene | Test | Objekt | Status |
|---|---|---|---|
| 1 | Varianzskala | \(\mathcal{V}_{N,H}^{\Delta} \sim (H/M)\log(M/H)\) | \(?[O]\) |
| 2 | Formfaktorprofil | \(\mathcal{S}_{N,H} \to K_{\mathrm{GUE}}\) nach Entfaltung | \(?[O]\) |
| 3 | Weil-Schnittstelle | \(\mathcal{V} \to Q_{\mathrm{Weil}}(f,f)\) | \(?[O]\) |

---

## Neue Leitfrage für NEU-103

$$
\boxed{\text{Welche Normalisierung }\alpha_N(\tau)\text{ identifiziert }\mathcal{S}_{N,H}\text{ mit Montgomerys Formfaktor?}}
$$

Konkrete Schritte:
1. Nullstellendichte \(\rho_N = \log M_N / 2\pi\) als kanonischer Skalierungsfaktor
2. Prüfen ob \(\alpha_N(\tau) = \tau / \rho_N\) (lineare Entfaltung) konsistent ist
3. Falls ja: Vergleich \(\mathcal{S}_{N,H}(\rho_N \alpha) \stackrel{?}{\to} K(\alpha)\)

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\mathcal{S}_{N,H}(\tau)\) normierte Profildichte | \(\checkmark[M]\) (Def.) |
| (B) | No-Go: \(|\mathcal{E}|^2 \to r(u)\) direkt | \(\checkmark[M]\) |
| (C) | Formfaktor \(K(\alpha) = |\alpha|/1\) Ramp-Plateau | \(\checkmark[M]\) (bekannt) |
| (D) | Entfaltungskarte \(\tau \mapsto \alpha_N(\tau)\) | \(?[O]\) |
| (E) | \(\mathcal{S}_{N,H} \to K_{\mathrm{GUE}}\) nach Entfaltung | \(?[O]\) |
| (F) | Drei-Ebenen-Architektur vollständig | \(\checkmark[M]\) |

---

## Verweise

- **Montgomery:** *The pair correlation of zeros* (1973) \(\leftarrow\) \(r(u)\) und Formfaktor
- **Goldston & Montgomery:** *Pair correlation of zeros and primes in short intervals* (1987)
- **Montgomery & Soundararajan:** *Primes in short intervals* (2004) (Varianzskala \(H\log(N/H)\))
- **Chan:** *Short intervals* (2003) (zweite Hauptterme)
- NEU-101: Transferlemma \(\mathcal{V}_{N,H}^{\Delta}\)
- NEU-100: \(\mathcal{E}_{N,H}(\tau)\) Definition
- Connes: *Trace formula* (1999) (spätere Weil-Schnittstelle)
