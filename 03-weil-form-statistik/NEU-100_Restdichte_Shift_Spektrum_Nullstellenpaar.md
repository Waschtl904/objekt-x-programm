# NEU-100 — Restdichte, Shift-Spektrum und Nullstellenpaar-Kanal

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-99 (Singulärserien-Schicht; \(\widetilde{\mathcal{C}}_N \sim 1\) kein Weil-Signal; \(\Delta_N(h)\) Restdichte)  
**Nächste Nummer:** NEU-101

---

## Ausgangspunkt

NEU-99 zeigt: \(\widetilde{\mathcal{C}}_N(\theta) \sim 1\) ist der universelle Singulärserien-Durchschnitt, kein Weil-Signal. Das neue Prüfobjekt ist die Restdichte \(\Delta_N(h)\). NEU-100 fragt, über welchen Kanal ein Weil-Signal in dieser Restdichte sichtbar werden könnte.

**Indexkorrektur:** \(\Delta_N\) ist eine Funktion des Shifts \(h\), nicht der Primvariablen \(m\). Eine Autokorrelation muss als
$$
R_{N,H}(k) = \frac{1}{H}\sum_h \omega\!\left(\frac{h}{H}\right) \Delta_N(h)\overline{\Delta_N(h+k)}
$$
formuliert werden, nicht als \(\sum_m \Delta_N(m)\Delta_N(m+k)\).

---

## Definition NEU-100.1 — Restdichte (Präzisierung)

Setze

$$
E_N(h) := \sum_{m \sim M_N} \Lambda(m)\Lambda(m+h) - \mathfrak{S}(h)M_N,
\qquad
\Delta_N(h) := \frac{E_N(h)}{M_N}.
$$

Damit ist \(\Delta_N(h)\) das normierte Residual der Paarkorrelation nach Abzug des Hardy\u2013Littlewood-Hauptterms.

**Strukturwarnung:** \(\Delta_N(h)\) ist bereits ein **quadratisches** Mangoldt-Residual (Produkt zweier \(\Lambda\)-Summen abzüglich Hauptterm). Eine Autokorrelation von \(\Delta_N\) ist arithmetisch ein **quartisches** Objekt. Direktes Einsetzen der expliziten Formel auf punktweise \(\Delta_N(h)\) ist daher nicht sauber.

**Status: \(\checkmark[M]\)** (Definition und Warnung)

---

## Definition NEU-100.2 — Geglättete Shift-Transformierte

Für ein Glättungsgewicht \(\omega \geq 0\), \(\int \omega = 1\), und Fensterbreite \(H\) setze:

$$
\mathcal{E}_{N,H}(\tau)
:= \sum_h \omega\!\left(\frac{h}{H}\right) \Delta_N(h)\, e^{-i\tau h/H}.
$$

Das ist die **geglättete Fourier-Transformierte** von \(\Delta_N\) in der Shift-Variablen.

**Status: \(\checkmark[M]\)** (Definition)

---

## Definition NEU-100.3 — Zweites Moment (Shift-Varianz)

Das natürliche quadratische Objekt ist:

$$
\mathcal{V}_{N,H}
:= \int |\mathcal{E}_{N,H}(\tau)|^2\, d\tau.
$$

Äquivalent über Parseval:

$$
\mathcal{V}_{N,H}
= \sum_h \omega\!\left(\frac{h}{H}\right)^2 |\Delta_N(h)|^2.
$$

Und die geglättete Shift-Autokorrelation:

$$
R_{N,H}(k)
:= \frac{1}{H} \sum_h \omega\!\left(\frac{h}{H}\right) \Delta_N(h)\overline{\Delta_N(h+k)}.
$$

**Status: \(\checkmark[M]\)** (Definition; \(\mathcal{V}_{N,H} = R_{N,H}(0) \cdot H\))

---

## Satz NEU-100.4 — Nullstellenpaar-Kanal

Wenn ein Weil-relevantes Signal in \(\Delta_N\) existiert, dann **nicht** in:
- \(\widetilde{\mathcal{C}}_N \sim 1\) (universell, NEU-99)
- \(\frac{1}{H}\sum_{|h| \leq H} \mathfrak{S}(h) \to 1\) (Gallagher, NEU-99)
- dem punktweisen Wert \(\Delta_N(h)\) für festes \(h\)

Sondern nur im **Shift-Spektrum**:

$$
|\widehat{\Delta}_N|^2 \quad\text{bzw.}\quad \mathcal{V}_{N,H}.
$$

Erst nach Glättung und quadratischer Mittelung können Terme vom Typ

$$
\sum_{\rho, \rho'} M_N^{\rho + \overline{\rho'} - 2}
$$
sinnvoll auftreten. Dabei kommen \(\rho, \rho'\) als Nullstellenpaare der Riemannschen Zetafunktion ins Spiel.

$$
\boxed{\Delta_N(h) \text{ ist nicht selbst die Weil-Form. Das Shift-Spektrum }|\widehat{\Delta}_N|^2\text{ ist der erste plausible Weil-Kandidat.}}
$$

**Status: \(\warning[M]\)** / \(?[O]\)

---

## Architektur der vier Schichten

| Schicht | Objekt | Charakter | Weil-Signal? |
|---|---|---|---|
| 0 | \(\widetilde{\mathcal{C}}_N \sim 1\) | universell | \(\times\) |
| 1 | \(\mathfrak{S}(h)\) | lokal-arithmetisch | \(\times\) |
| 2 | \(\Delta_N(h)\) | Residual | \(\times\) (direkt) |
| 3 | \(|\widehat{\Delta}_N|^2\), \(\mathcal{V}_{N,H}\) | Shift-Spektrum | \(?\) |

---

## Neue Leitfrage für NEU-101

$$
\boxed{\mathcal{V}_{N,H} \text{ vs. bekannte Varianzformeln für Primzahlen in kurzen Intervallen.}}
$$

Konkrete Vergleichsformeln:
1. **Goldston\u2013Montgomery:** \(\mathcal{V}(M,H) \sim \frac{H}{M} \log M\) (bedingt unter RH)
2. **Montgomery-Paarkorrelation:** Vergleich der spektralen Dichte von \(\mathcal{E}_{N,H}\) mit Nullstellenpaarstatistik
3. **Weil-Form:** Kann \(\mathcal{V}_{N,H}\) in eine Form \(Q_{\mathrm{Weil}}(f,f)\) für geeignetes \(f\) umgeschrieben werden?

---

## Kritischer Pfad

$$
\Delta_N(h)
\;\longrightarrow\;
\mathcal{E}_{N,H}(\tau)
\;\longrightarrow\;
\mathcal{V}_{N,H}
\;\longrightarrow\;
\text{Vergleich mit Montgomery/Weil}.
$$

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(E_N(h)\), \(\Delta_N(h)\) korrekt als Shift-Funktion | \(\checkmark[M]\) |
| (B) | \(\Delta_N\) quadratisch; Autokorr. quartisch | \(\checkmark[M]\) (Warnung) |
| (C) | \(\mathcal{E}_{N,H}(\tau)\) geglättete Shift-Transformierte | \(\checkmark[M]\) (Def.) |
| (D) | \(\mathcal{V}_{N,H}\) zweites Moment; \(R_{N,H}(k)\) Autokorr. | \(\checkmark[M]\) (Def.) |
| (E) | Nullstellenpaar-Kanal nur in \(|\widehat{\Delta}_N|^2\) | \(\warning[M]\) |
| (F) | \(\mathcal{V}_{N,H}\) vs. Goldston\u2013Montgomery/Weil | \(?[O]\) |

---

## Verweise

- NEU-99: Singulärserien-Schicht; \(\Delta_N(h)\) Definition
- Hardy & Littlewood: *Partitio Numerorum III* (1923)
- Gallagher: *Primes in short intervals* (1976)
- **Goldston & Montgomery:** *Pair correlation of zeros and primes in short intervals* (1987) \(\leftarrow\) Hauptvergleich für \(\mathcal{V}_{N,H}\)
- Montgomery: *The pair correlation of zeros* (1973)
- Rudnick & Sarnak: *Zeros of principal L-functions* (1996)
- Iwaniec & Kowalski: *Analytic Number Theory*, Kap. 13
