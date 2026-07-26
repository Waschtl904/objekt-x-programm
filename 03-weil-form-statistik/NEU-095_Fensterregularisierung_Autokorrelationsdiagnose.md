# NEU-95 — Fensterregularisierung und Autokorrelationsdiagnose des arithmetischen Bochner-Kerns

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-94 (Bochner-Tor; \(\nu_N^{\mathrm{arith}} = |A_N|^2 d\xi / \|A_N\|^2\) als Hauptkandidat)  
**Nächste Nummer:** NEU-96

---

## Ausgangspunkt

NEU-94 definiert den arithmetischen Bochner-Kandidaten als \(d\nu_N^{\mathrm{arith}} \propto |A_N(\xi)|^2 d\xi\). NEU-95 zeigt, dass dieser Kandidat **ohne Spektralfenster noch kein endliches Ma\ss** ist, und gibt die korrekte regularisierte Form an.

---

## Satz NEU-95.1 — Fensterpflicht

Ein Dirichlet-Polynom

$$
A_N(\xi) = \sum_{n \leq M_N} a_n\, n^{-i\xi}, \qquad a_n = \frac{\Lambda(n)}{\sqrt{n}} w_N(n),
$$

ist **fastperiodisch** und nicht in \(L^2(\mathbb{R})\). Daher gilt im Allgemeinen

$$
\int_{\mathbb{R}} |A_N(\xi)|^2\, d\xi = +\infty.
$$

Ohne Spektralfenster definiert \(|A_N(\xi)|^2 d\xi\) **kein endliches Bochner-Ma\ss** auf \(\mathbb{R}\).

$$
\boxed{\text{Fensterpflicht: Der arithmetische Bochner-Kandidat aus NEU-94 muss regularisiert werden.}}
$$

**Status: \(\checkmark[M]\)**

---

## Definition NEU-95.2 — Fensterma\ss

Sei \(\eta \geq 0\), \(\int_{\mathbb{R}} \eta = 1\), und \(\eta_T(\xi) := T^{-1}\eta(\xi/T)\). Definiere das **gefensterte arithmetische Ma\ss**

$$
d\nu_{N,T}^{\mathrm{arith}}(\xi) := \frac{|A_N(\xi)|^2\, \eta_T(\xi)\, d\xi}{\int_{\mathbb{R}} |A_N(u)|^2\, \eta_T(u)\, du}.
$$

Dann ist \(\nu_{N,T}^{\mathrm{arith}}\) ein **positives Wahrscheinlichkeitsma\ss**, und

$$
\Psi_{N,T}(t) := \int_{\mathbb{R}} e^{it\xi}\, d\nu_{N,T}^{\mathrm{arith}}(\xi)
$$

ist automatisch positiv definit (Bochner-Theorem). Der Grenzprozess ist nun **zweiparametrig:**

$$
(N, T) \to \infty.
$$

Verschiedene Skalierungen \(T = T(N)\) k\"onnen verschiedene Grenzobjekte liefern.

**Status: \(\checkmark[M]\)**

---

## Satz NEU-95.3 — Exakte Autokorrelationsexpansion

Mit \(a_n = \Lambda(n)/\sqrt{n} \cdot w_N(n)\) gilt

$$
\int_{\mathbb{R}} e^{it\xi}\, |A_N(\xi)|^2\, \eta_T(\xi)\, d\xi
= \sum_{m,n \leq M_N} a_m \overline{a_n}\, \widehat{\eta_T}\!\left(t + \log\frac{n}{m}\right).
$$

Nach Normalisierung:

$$
\Psi_{N,T}(t) \sim \frac{\displaystyle\sum_{m,n \leq M_N} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}\, w_N(m)w_N(n)\, \widehat{\eta_T}\!\left(t + \log\frac{n}{m}\right)}{\displaystyle\sum_{n \leq M_N} \frac{\Lambda(n)^2}{n}\, w_N(n)^2 \cdot \eta_T(0)}.
$$

Der Kern \(\Psi_{N,T}\) ist damit eine **gewichtete logarithmische Autokorrelation der Mangoldt-Gewichte**, mit echten Kreuzterme \(\Lambda(m)\Lambda(n)\) f\"ur \(m \neq n\).

**Status: \(\checkmark[M]\)**

---

## Diagnose NEU-95.4 — Keine automatische Nullstellenkonzentration

F\"ur jedes feste glatte Fenster \(\eta_T\) ist

$$
d\nu_{N,T}^{\mathrm{arith}}(\xi)
$$

**absolut stetig** bez\"uglich \(d\xi\). Ein schwacher Grenzwert bleibt typischerweise absolut stetig oder h\"angt vom Fensterprozess ab.

Eine Konzentration auf die diskrete Menge

$$
\{\operatorname{Im}(\rho) : \zeta(\rho) = 0\}
$$

w\"are ein **singulärer Resonanzeffekt** und kann *nicht* aus Bochner-Positivit\"at allein folgen. Daf\"ur ben\"otigt man zus\"atzliche Polstruktur (etwa: \(\log \zeta\) hat Polstellen auf der kritischen Geraden).

$$
\boxed{\text{Nullstellenkonzentration von }\nu_\infty\text{ ist kein automatisches Korollar der Bochner-Konstruktion.}}
$$

**Status: \(\warning[M]\)**

---

## Diagnose NEU-95.5 — Saubere Trennung: Mangoldt-Autokorrelation vs. Weil-Form

Der Kern \(B_{N,T}^{\mathrm{arith}}(f,f)\) ist eine positive Mangoldt-Autokorrelationsform:

$$
B_{N,T}^{\mathrm{arith}}(f,f)
= \sum_{m,n} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}\, w_N(m)w_N(n)\, C_{N,T}(m,n)\, \langle f, V_{m/n} f \rangle,
$$

wobei \(C_{N,T}(m,n) = \widehat{\eta_T}(\log n/m)\) der Fensterkoeffizient ist. Das ist **nicht** dieselbe wie die Weil-Quadratform, die aus der expliziten Formel entsteht. Die Identifikation

$$
B_\infty^{\mathrm{arith}} = Q_{\mathrm{Weil}}
$$

erfordert einen separaten Transformationsschritt \u00fcber die explizite Formel:

$$
\text{Mangoldt-Autokorrelationsform}
\xrightarrow{\text{expl. Formel}}
\text{Weil-Quadratform}.
$$

**Status: \(?[O]\)**

---

## Neue Leitfrage f\"ur NEU-96

$$
\boxed{\text{Kann die explizite Formel den Autokorrelationskern }B_{N,T}^{\mathrm{arith}}\text{ in die Weil-Form transformieren?}}
$$

Konkrete Teilfragen:
1. Welche Skalierung \(T = T(N)\) liefert den kanonischen Grenzprozess?
2. Wie verhält sich \(\Psi_{N,T(N)}(t)\) unter Anwendung der expliziten Formel?
3. Entsteht dabei ein Grenzkern, der \(Q_{\mathrm{Weil}}\) approximiert?

---

## Status\"ubersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(|A_N|^2 d\xi\) ohne Fenster: nicht endlich | \(\checkmark[M]\) |
| (B) | \(\nu_{N,T}^{\mathrm{arith}}\) mit Fenster \(\eta_T\): positives Wahrscheinlichkeitsma\ss | \(\checkmark[M]\) |
| (C) | \(\Psi_{N,T}\): geglättete Log-Autokorrelation mit Kreuzterme \(\Lambda(m)\Lambda(n)\) | \(\checkmark[M]\) |
| (D) | Nullstellenkonzentration \(\nu_\infty \to \sum \delta_{\mathrm{Im}(\rho)}\): kein automatisches Korollar | \(\warning[M]\) |
| (E) | \(B_{N,T}^{\mathrm{arith}} \neq Q_{\mathrm{Weil}}\) direkt: Transformationsschritt n\"otig | \(?[O]\) |

---

## Verweise

- NEU-94: Bochner-Tor; \(A_N(\xi)\)-Kandidat
- NEU-93: Korrelationskern-Lift; \(K_N = \sqrt{\kappa}\,\rho_N\,\sqrt{\kappa}\)
- Weil: *Sur les formules explicites de la th\u00e9orie des nombres* (explizite Formel)
- Connes: *Trace formula* (1999) (Weil-Distribution; Nullstellenspektrum)
- Meyer: Duke Math. J. 127 (2005) (explizite Formel als Verteilung)
- Iwaniec & Kowalski: *Analytic Number Theory* (Dirichlet-Polynome; Meanvalue-S\"atze)
- Titchmarsh: *The Theory of the Riemann Zeta-Function* (Fastperiodizit\"at)
- Katznelson: *An Introduction to Harmonic Analysis* (Bochner-Theorem; Spektralma\ss e)
