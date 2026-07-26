# NEU-94 — Bochner-Tor für logarithmische Korrelationskerne

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-93 (Korrelationskern-Lift; \(\Psi_N(\log m/n)\) als Weil-Kandidat)  
**Nächste Nummer:** NEU-95

---

## Ausgangspunkt

Aus NEU-93: Der Freiheitsgrad ist der logarithmische Korrelationskern

$$
\rho_N((r,m),(r,n)) = \Psi_N\!\left(\log\frac{m}{n}\right).
$$

Die Frage lautet: Welche \(\Psi_N\) sind zulässig, und welche tragen Zeta-spezifische Information?

---

## Satz NEU-94.1 — Bochner-Zulässigkeit

Die korrekte Zulässigkeitsbedingung für \(\Psi_N : \mathbb{R} \to \mathbb{C}\) ist **positive Definitheit** auf der additiven Log-Achse. Nach dem Satz von Bochner gilt äquivalent:

$$
\Psi_N(t) = \int_{\mathbb{R}} e^{it\xi}\, d\nu_N(\xi)
$$

für ein positives endliches Maß \(\nu_N\) auf \(\mathbb{R}\), mit Normalisierung \(\Psi_N(0) = \nu_N(\mathbb{R}) = 1\).

Damit verschiebt sich die Frage: Nicht Wahl einer Funktion \(\Psi_N\), sondern Wahl eines **positiven Spektralmaßes** \(\nu_N\).

**Status: \(\checkmark[M]\)**

---

## Satz NEU-94.2 — Glättungskerne als Kontrollmodelle

Reine Glättungskerne sind Bochner-admissibel und PSD:

| Kern \(\Psi_N(t)\) | Spektralmaß \(d\nu_N(\xi)\) | PSD | RH-Gehalt |
|---|---|---|---|
| \(e^{-a\|t\|}\), \(a>0\) | Cauchy-Maß \(\sim (a^2+\xi^2)^{-1}d\xi\) | \(\checkmark\) | \(\times\) |
| Gauß \(e^{-\sigma^2 t^2/2}\) | Gauß \(\sim e^{-\xi^2/2\sigma^2}d\xi\) | \(\checkmark\) | \(\times\) |
| \(\widehat{\phi}(t/\log N)\) | Skalierung von \(\phi\) | \(\checkmark\) (falls \(\phi \geq 0\)) | \(\times\) |

**Diagnose:** Wenn Positivität vollständig durch Konstruktion eingebaut ist (beliebiges glattes \(\nu_N\)), trägt der Kern noch keine RH-Information. Der RH-Gehalt liegt dann ausschließlich in der Grenzform-Aussage \(B_N \to Q_{\mathrm{Weil}}\).

**Status: \(\checkmark[M]\)**

---

## Definition NEU-94.3 — Arithmetisches Bochner-Maß

Der eigentliche Kandidat ist ein **arithmetisch konstruiertes** Spektralmaß. Definiere das Mangoldt-Dirichlet-Polynom

$$
A_N(\xi) := \sum_{n \leq N} \frac{\Lambda(n)}{\sqrt{n}}\, w_N(n)\, n^{-i\xi},
$$

wobei \(w_N(n)\) ein Abschneidekern (etwa \(w_N(n) = \mathbf{1}_{n \leq M_N}\) auf der pathwise Skala) ist. Setze

$$
d\nu_N(\xi) := \frac{|A_N(\xi)|^2\, d\xi}{\int |A_N(\xi)|^2\, d\xi}.
$$

Dann ist \(\nu_N\) ein positives Wahrscheinlichlichkeitsmaß, und

$$
\Psi_N(t) := \int e^{it\xi}\, d\nu_N(\xi) = \widehat{\nu}_N(t)
$$

ist automatisch positiv definit.

**Explizit:**

$$
\Psi_N(t) \propto \sum_{m,n \leq M_N} \frac{\Lambda(m)\Lambda(n)}{\sqrt{mn}}\, w_N(m)w_N(n)\, \left(\frac{m}{n}\right)^{it}.
$$

Das sind echte **Mangoldt-Kreuzterme** \(\Lambda(m)\Lambda(n)\) auf der multiplikativen Achse \((m/n)^{it} = e^{it\log(m/n)}\).

$$
\boxed{\Psi_N(t) = \widehat{\nu}_N^{\mathrm{arith}}(t): \text{ arithmetisches Bochner-Maß aus Mangoldt-Dirichlet-Polynom.}}
$$

**Status: \(\warning[M]\) / \(?[O]\)** (Normierung und Grenzform offen)

---

## Vergleich: Zwei Klassen von \(\nu_N\)

| Klasse | Beispiel | Positivität | RH-Gehalt |
|---|---|---|---|
| Glättungskerne | \(e^{-|t|/2}\), Gauß, \(\widehat{\phi}(t/\log N)\) | \(\checkmark\) (eingebaut) | \(\times\) |
| Arithmetische Spektralkerne | \(\nu_N^{\mathrm{arith}}\) aus \(|A_N|^2\) | \(\checkmark\) (aus Konstruktion) | \(?[O]\) |

---

## Neue Leitfrage für NEU-95

$$
\boxed{\text{Finde ein kanonisches positives arithmetisches Spektralmaß }\nu_N\text{, dessen Grenzform mit }Q_{\mathrm{Weil}}\text{ kompatibel ist.}}
$$

Konkrete Teilfragen:

1. Konvergiert \(\nu_N^{\mathrm{arith}}\) schwach zu einem Grenzmaß \(\nu_\infty\)?
2. Ist \(\nu_\infty\) auf die Nullstellen \(\operatorname{Im}(\rho)\) von \(\zeta\) konzentriert?
3. Kodiert \(\Psi_\infty(t) = \widehat{\nu}_\infty(t)\) die Nullstellenstruktur?
4. Stimmt der Grenzkern \(B_\infty(f,g) = \int \widehat{f}(\xi)\overline{\widehat{g}(\xi)}\, d\nu_\infty(\xi)\) mit der Weil-Quadratform überein?

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Bochner-Zulässigkeit: \(\Psi_N = \widehat{\nu}_N\), \(\nu_N \geq 0\) | \(\checkmark[M]\) |
| (B) | Glättungskerne admissibel, aber ohne RH-Gehalt | \(\checkmark[M]\) |
| (C) | Arithmetisches \(\nu_N^{\mathrm{arith}} = |A_N|^2 d\xi / \|A_N\|^2\) PSD und arithmetisch | \(\warning[M]\) |
| (D) | Grenzmaß \(\nu_\infty\) und Weil-Kompatibilität | \(?[O]\) |
| (E) | Nullstellenkonzentration von \(\nu_\infty\) | \(?[O]\) |

---

## Verweise

- NEU-93: Korrelationskern-Lift; \(K_N = \sqrt{\kappa}\,\rho_N\,\sqrt{\kappa}\)
- NEU-88: Resolvent-Gewicht \(W_N(r,n)\)
- NEU-67: \(\Lambda = \mu * \log\); Mangoldt-Arithmetik
- Weil: *Sur les formules explicites* (Quadratform auf \(L^2\))
- Connes: *Trace formula* (1999) (Weil-Verteilung; Nullstellenspektrum)
- Meyer: Duke Math. J. 127 (2005) (explizite Formel; Spektralmaß)
- Bochner: *Lectures on Fourier Integrals* (PSD-Kerne und Spektralmaße)
- Iwaniec & Kowalski: *Analytic Number Theory* (Dirichlet-Polynome; \(|A_N|^2\)-Mittelwertsätze)
