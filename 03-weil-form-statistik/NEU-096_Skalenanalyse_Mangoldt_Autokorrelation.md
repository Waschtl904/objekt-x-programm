# NEU-96 — Skalenanalyse der gef\u00e4nsterten Mangoldt-Autokorrelation

**Stand:** 1. Juli 2026  
**Vorg\u00e4nger:** NEU-95 (Fensterpflicht; \(\Psi_{N,T}\) als Log-Autokorrelation; keine automatische Nullstellenkonzentration)  
**N\u00e4chste Nummer:** NEU-97

---

## Ausgangspunkt

Aus NEU-95:

$$
\Psi_{N,T}(t)
\sim
\sum_{m,n \leq M_N}
\frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}\,
w_N(m)w_N(n)\,
\widehat{\eta}\!\left(T\!\left(t+\log\frac{n}{m}\right)\right).
$$

Das Fenster \(\widehat{\eta}(T \log(n/m))\) lokalisiert auf \(|\log(n/m)| \lesssim T^{-1}\), also f\u00fcr \(m,n \sim M_N\) auf

$$
|m - n| \lesssim \frac{M_N}{T}.
$$

Die Skalenwahl \(T = T(N)\) entscheidet, welche Paare \((m,n)\) miteinander korrelieren. NEU-96 klassifiziert die drei Regime.

---

## Satz NEU-96.1 \u2014 Diagonalregime

**Regime:** \(T(N) \gg M_N\).

Dann ist

$$
\frac{M_N}{T} \ll 1,
$$

also bleibt nur \(m = n\) \u00fcbrig. Der Kern kollabiert auf die Diagonalmasse:

$$
\Psi_{N,T}(t) \to \sum_{n \leq M_N} \frac{\Lambda(n)^2}{n} w_N(n)^2 \cdot \widehat{\eta}(Tt).
$$

Das reproduziert NEU-92/NEU-95, liefert aber keine echte Kreuzstruktur.

$$
\boxed{T \gg M_N \;\Longrightarrow\; \text{Diagonal-Kollaps.}}
$$

**Status: \(\checkmark[M]\)**

---

## Satz NEU-96.2 \u2014 Vollkorrelationsregime

**Regime:** \(1 \ll T(N) \ll M_N\).

Dann korrelieren f\u00fcr jedes \(n\) viele Nachbarn \(m\) mit

$$
|m - n| \lesssim \frac{M_N}{T} \gg 1.
$$

Echte Kreuzterme \(\Lambda(m)\Lambda(n)\) mit \(m \neq n\) entstehen. Dies ist der einzige Bereich, in dem Weil-relevante Kreuzstruktur sichtbar werden kann.

Aber: Der Kern h\u00e4ngt jetzt von der Paarstatistik der Mangoldt-Funktion in kurzen multiplikativen Fenstern ab. Kontrolle \u00fcber gemittelte Mangoldt-Korrelationen ist notwendig.

$$
\boxed{1 \ll T(N) \ll M_N \;\Longrightarrow\; \text{einziger nichttrivialer Kandidatenbereich.}}
$$

**Status: \(\warning[M]\) / \(?[O]\)**

---

## Satz NEU-96.3 \u2014 Grobfenster / Rang-eins-Gefahr

**Regime:** \(T(N) \to 1\) oder \(T(N) = O(1)\).

Dann wird \(\widehat{\eta}(T \log(n/m))\) breit: zu viele Paare korrelieren fast gleich stark. Der Kern n\u00e4hert sich einem Rang-eins-Objekt:

$$
B_{N,T}^{\mathrm{arith}}(f,f)
\approx
\left|\sum_{n \leq M_N} \frac{\Lambda(n)}{\sqrt{n}} w_N(n)\, f(n)\right|^2.
$$

Das ist positiv und hat Kreuzterme, aber die Korrelationsstruktur ist zu grob f\u00fcr eine Weil-kompatible Grenzform.

$$
\boxed{T = O(1) \;\Longrightarrow\; \text{Rang-eins-/Grobmittelungs-Kollaps.}}
$$

**Status: \(\warning[M]\)**

---

## Satz NEU-96.4 \u2014 Kanonischer Skalenbereich

Die Skalentriage ergibt:

| Regime | Korrelationsweite | Kreuzterme | Weil-tauglich |
|---|---|---|---|
| \(T \gg M_N\) | \(\leq 1\) (nur Diag.) | \(\times\) | \(\times\) |
| \(1 \ll T \ll M_N\) | \(M_N/T \gg 1\) | \(\checkmark\) | \(?\) |
| \(T = O(1)\) | \(\sim M_N\) (alle) | \(\checkmark\) | \(\times\) (zu grob) |

Der kanonische Kandidatenbereich ist das Zwischenregime:

$$
\boxed{1 \ll T(N) \ll M_N.}
$$

Die Frage f\u00fcr NEU-97 lautet:

$$
\boxed{\text{Welche log-Aufl\u00f6sung }T^{-1}\text{ verlangt }Q_{\mathrm{Weil}}?}
$$

**Status: \(\warning[M]\) / \(?[O]\)**

---

## Satz NEU-96.5 \u2014 Explizite Formel nur nach Linearisierung

Die klassische explizite Formel wirkt auf **lineare** Mangoldt-Summen:

$$
\sum_{n} \Lambda(n) F(\log n)
= -\sum_{\rho} \widehat{F}(\rho) + \text{arkm. Terme}.
$$

Der Kern \(\Psi_{N,T}\) ist jedoch **quadratisch**. Der \u00dcbergang zur Weil-Form erfordert daher eine der beiden Varianten:

**Variante A \u2014 Autokorrelationsanalyse:**

$$
\sum_{m,n} \Lambda(m)\Lambda(n)\, \widehat{\eta}\!\left(T\log\frac{n}{m}\right)
$$

direkt \u00fcber Paarstatistik analysieren (Goldston\u2013Y\u0131ld\u0131r\u0131m-Methode oder \u00e4hnliche Techniken).

**Variante B \u2014 Spektrale Linearisierung:**

$$
A_N(\xi) \approx -\frac{\zeta'}{\zeta}\!\left(\tfrac{1}{2}+i\xi\right)\quad (\text{regularisiert}),
$$

dann wird \(|A_N(\xi)|^2\) zum Mittelwertobjekt der logarithmischen Ableitung. Nullstellen erscheinen \u00fcber Pole/Resonanzen von \(\zeta'/\zeta\), nicht automatisch.

**Diagnose:** Ein einzelner Aufruf der expliziten Formel gen\u00fcgt nicht. Der Flaschenhals ist die Kontrolle \u00fcber **quadratische Mangoldt-Korrelationen im Zwischenregime**.

**Status: \(\warning[M]\) / \(?[O]\)**

---

## Skalentriage \u2014 Gesamtzusammenfassung

$$
\underbrace{T \gg M_N}_{\text{Diagonal-Kollaps}} \qquad\longleftarrow\qquad \underbrace{1 \ll T \ll M_N}_{\text{kanonischer Bereich}} \qquad\longrightarrow\qquad \underbrace{T = O(1)}_{\text{Rang-eins-Kollaps}}
$$

---

## Neue Leitfrage f\u00fcr NEU-97

$$
\boxed{\text{Welche konkrete Skala }T(N)\text{ im Zwischenregime macht die Mangoldt-Autokorrelation explizite-Formel-kompatibel?}}
$$

Konkrete Teilfragen:
1. Ist \(T(N) = \log M_N\) oder \(T(N) = \sqrt{M_N}\) kanonisch?
2. Welche Paarstatistik \(\sum_{|m-n| \leq M_N/T} \Lambda(m)\Lambda(n)\) ist analytisch kontrollierbar?
3. Kann Variante B (spektrale Linearisierung \u00fcber \(\zeta'/\zeta\)) im Zwischenregime die Nullstellenstruktur sichtbar machen?

---

## Status\u00fcbersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Diagonalregime \(T \gg M_N\): Kollaps auf \(\Lambda(n)^2\) | \(\checkmark[M]\) |
| (B) | Vollkorrelationsregime \(1 \ll T \ll M_N\): Kreuzterme m\u00f6glich | \(\warning[M]\) |
| (C) | Grobregime \(T = O(1)\): Rang-eins-Kollaps | \(\warning[M]\) |
| (D) | Kanonischer Bereich: \(1 \ll T \ll M_N\) | \(\warning[M]\) / \(?[O]\) |
| (E) | Expl. Formel braucht Linearisierung (Var. A oder B) | \(\warning[M]\) / \(?[O]\) |

---

## Verweise

- NEU-95: Fensterpflicht; \(\nu_{N,T}^{\mathrm{arith}}\); Autokorrelationsexpansion
- NEU-93: Korrelationskern-Lift; Rang-eins-Faserkern
- NEU-84: Skalentrennung \(M_N^{\mathrm{path}}/M_N^{\mathrm{op}}\) (strukturelle Analogie)
- Weil: *Sur les formules explicites* (log-Aufl\u00f6sung der Testfunktionen)
- Goldston & Y\u0131ld\u0131r\u0131m: *Higher correlations of divisor sums* (Paarstatistik \(\Lambda(m)\Lambda(n)\))
- Iwaniec & Kowalski: *Analytic Number Theory* Kap. 5 (Meanvalue-S\u00e4tze f\u00fcr Dirichlet-Polynome)
- Montgomery: *The pair correlation of zeros of the zeta function* (1973)
