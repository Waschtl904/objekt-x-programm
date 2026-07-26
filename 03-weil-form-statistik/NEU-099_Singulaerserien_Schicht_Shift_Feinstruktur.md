# NEU-99 — Singulärserien-Schicht und shift-aufgelöste Feinstruktur

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-98 (Massenniveau-Stabilität; kein inneres \(\theta^*\); \(\widetilde{\mathcal{C}}_N \sim 1\) als Prüfobjekt)  
**Nächste Nummer:** NEU-100

---

## Ausgangspunkt

NEU-98 zeigt: Die renormierte Korrelationsdichte \(\widetilde{\mathcal{C}}_N(\theta) \sim 1\) ist massenseitig stabil. Kein inneres \(\theta^*\) auf reinem Massenniveau. Der Flaschenhals liegt in der **arithmetischen Feinstruktur** von \(\widetilde{\mathcal{C}}_N\). NEU-99 legt diese Schicht frei.

---

## Definition NEU-99.1 — Shift-Zerlegung

Schreibe \(h = n - m\) und zerlege die Korrelationsmasse nach Shifts:

$$
\mathcal{C}_N(\theta)
= \sum_{\substack{m \sim M_N \\ |h| \leq H_N}}
\frac{\Lambda(m)\Lambda(m+h)}{m(m+h)}.
$$

Für \(m \sim M_N\) und moderate \(h\) gilt \(m(m+h) \sim M_N^2\), also:

$$
\mathcal{C}_N(\theta)
\approx \frac{1}{M_N^2}
\sum_{|h| \leq H_N}
\sum_{m \sim M_N} \Lambda(m)\Lambda(m+h).
$$

**Status: \(\checkmark[M]\)**

---

## Satz NEU-99.2 — Hardy\u2013Littlewood-Hauptterm

Die Hardy\u2013Littlewood-Primzahlpaar-Heuristik liefert für festes oder moderat wachsendes \(h \neq 0\):

$$
\sum_{m \sim M_N} \Lambda(m)\Lambda(m+h)
\sim \mathfrak{S}(h) \cdot M_N,
$$

wobei \(\mathfrak{S}(h)\) die **Singulärserie** des Primzahlpaarproblems ist:

$$
\mathfrak{S}(h)
:= 2 C_2 \prod_{p \mid h,\, p > 2} \frac{p-1}{p-2},
\qquad
C_2 = \prod_{p > 2} \frac{p(p-2)}{(p-1)^2}.
$$

Für \(h = 0\):

$$
\sum_{m \sim M_N} \Lambda(m)^2 \sim M_N \log M_N.
$$

**Status: \(\warning[H]\)** (Hardy\u2013Littlewood-Vermutung; nicht bewiesen; heuristisch)

---

## Satz NEU-99.3 — Gallagher-Mittelung der Singulärserie

Einsetzen des Hauptterms in die Shift-Zerlegung:

$$
\widetilde{\mathcal{C}}_N(\theta)
= T \cdot \mathcal{C}_N(\theta)
\approx \frac{T}{M_N^2} \sum_{|h| \leq H_N} \mathfrak{S}(h) \cdot M_N
= \frac{T}{M_N} \sum_{|h| \leq H_N} \mathfrak{S}(h)
= \frac{1}{H_N} \sum_{|h| \leq H_N} \mathfrak{S}(h).
$$

(Verwendet \(T/M_N = 1/H_N\).)

Nach **Gallagher-artiger Mittelung** \((H_N \to \infty)\):

$$
\frac{1}{H_N} \sum_{|h| \leq H_N} \mathfrak{S}(h) \to 1.
$$

Das heißt: Der **skalare Grenzwert** \(\widetilde{\mathcal{C}}_N(\theta) \to 1\) ist keine Nullstelleninformation, sondern der **universelle Singulärseriendurchschnitt**.

$$
\boxed{\widetilde{\mathcal{C}}_N(\theta) \sim 1 \text{ ist kein Weil-Signal, sondern der Singulärserien-Durchschnitt.}}
$$

**Status: \(\warning/\checkmark[M]\)** (bedingt durch Hardy\u2013Littlewood-Hauptterm; Gallagher-Mittelung bewiesen für \(\mathfrak{S}\) unter Standardbedingungen)

---

## Satz NEU-99.4 — Skalar \(\widetilde{\mathcal{C}}_N\) trägt keine Nullstellenstruktur

Weil-relevante Information kann im skalaren Durchschnitt nicht sichtbar sein:
- Der skalare Hauptterm ist universell (\(\to 1\)) für alle \(0 < \theta < 1\)
- Nullstellenoszillationen wären \(o(1)\)-Korrekturen, die in der Mittelung verschwinden
- Ohne shift-Auflösung ist \(\widetilde{\mathcal{C}}_N\) blind für Spektralinformation

**Status: \(\warning[M]\)**

---

## Definition NEU-99.5 — Shift-aufgelöste Restdichte

Das eigentliche neue Prüfobjekt ist die **shift-aufgelöste Restdichte**:

$$
\Delta_N(h)
:=
\frac{1}{M_N}
\sum_{m \sim M_N} \Lambda(m)\Lambda(m+h)
\;-\;
\mathfrak{S}(h),
$$

d.h. die **Abweichung** vom Hardy\u2013Littlewood-Hauptterm bei festem Shift \(h\).

Alternativ, in geglätteter logarithmischer Version:

$$
\widehat{\Delta}_N(t)
:=
\sum_{|h| \leq H_N}
\Delta_N(h) \cdot \widehat{\eta}\!\left(T\!\left(t + \log\frac{M_N+h}{M_N}\right)\right).
$$

**Status: \(\checkmark[M]\)** (Definition)

---

## Satz NEU-99.6 — Weil-Brücke nur über \(\Delta_N\)

Wenn überhaupt eine Weil-kompatible Grenzform entsteht, dann nur aus der Feinstruktur \(\Delta_N(h)\):

$$
\underbrace{\widetilde{\mathcal{C}}_N(\theta) \sim 1}_{\text{kein Weil-Signal}} \qquad\longrightarrow\qquad \underbrace{\Delta_N(h)}_{\text{Kandidat für Weil-Struktur}}.
$$

Die explizite Formel verbindet lineare Mangoldt-Summen mit Nullstellen:

$$
\sum_{m} \Lambda(m) f(m) \sim -\sum_{\rho} \widehat{f}(\rho) + \ldots
$$

Ein Quadrat \(\Delta_N(h)\) könnte über **Quadrate der expliziten Formel** (Montgomery-Paarkorrelation, Rudnick\u2013Sarnak) in Nullstellenkreuzterme übersetzt werden. Das ist der Anschluss an NEU-100.

**Status: \(\warning[M]\)** / \(?[O]\)

---

## Verschiebung des Flaschenhalses

$$
\underbrace{\text{renormierte Masse } \widetilde{\mathcal{C}}_N \sim 1}_{\text{NEU-98: kein }\theta^*} \quad\longrightarrow\quad \underbrace{\text{Singulärserien-Hauptterm}}_{\text{NEU-99: universell, kein Weil-Signal}} \quad\longrightarrow\quad \underbrace{\Delta_N(h)}_{\text{NEU-100: Weil-Kandidat}}
$$

$$
\boxed{\text{Flaschenhals} = \Delta_N(h): \text{ Vergleich mit explizite-Formel-Nullstellenoszillationen.}}
$$

---

## Neue Leitfrage für NEU-100

$$
\boxed{\text{Trägt }\Delta_N(h)\text{ Nullstellenoszillationen der Riemannschen Zetafunktion?}}
$$

Konkrete Teilfragen:
1. Lässt sich \(\sum_m \Delta_N(m) \Delta_N(m+h)\) über Quadrate der expliziten Formel entwickeln?
2. Erscheinen Terme \(\sim \sum_{\rho, \rho'} n^{\rho+\rho'}\) mit Nullstellenpaaren?
3. Ist das Resultat kompatibel mit Montgomery-Paarkorrelation?

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Shift-Zerlegung \(h = n-m\) | \(\checkmark[M]\) |
| (B) | H.\u2013L.-Hauptterm \(\mathfrak{S}(h) M_N\) | \(\warning[H]\) |
| (C) | Gallagher-Mittel \(\frac{1}{H_N}\sum \mathfrak{S}(h) \to 1\) | \(\checkmark/\warning[M]\) |
| (D) | \(\widetilde{\mathcal{C}}_N \sim 1\) kein Weil-Signal | \(\warning[M]\) |
| (E) | Definition \(\Delta_N(h)\) als Restdichte | \(\checkmark[M]\) (Def.) |
| (F) | Weil-Brücke nur über \(\Delta_N\) | \(\warning[M]\) / \(?[O]\) |

---

## Verweise

- NEU-98: Massenniveau-Stabilität; \(\widetilde{\mathcal{C}}_N\) als Prüfobjekt
- Hardy & Littlewood: *Some problems of Partitio Numerorum III* (1923) (Singulärserie)
- Gallagher: *On the distribution of primes in short intervals* (1976) (Mittelung \(\mathfrak{S}\))
- Montgomery: *The pair correlation of zeros of the zeta function* (1973)
- Rudnick & Sarnak: *Zeros of principal L-functions and random matrix theory* (1996)
- Goldston, Pintz & Y\u0131ld\u0131r\u0131m: *Primes in tuples* (GPY, 2009)
- Iwaniec & Kowalski: *Analytic Number Theory*, Kap. 13
