# NEU-93 — Korrelationskern-Lift der diagonalen Mangoldt-Masse

**Stand:** 30. Juni 2026  
**Vorgänger:** NEU-92 (\(\mu_N\) positives Maß; \(\Lambda(n)^2\) nur Diagonalmasse; \(B_N(f,f)\) als echter Positivitätsbegriff)  
**Nächste Nummer:** NEU-94

---

## Ausgangspunkt

Aus NEU-92: Die Masse \(\mu_N\) trägt ausschließlich Diagonalterme \(\kappa_a := \gamma^2\Lambda(n)^2 W_N(r,n) \geq 0\) für \(a=(r,n)\). Ein Weil-kompatibler Lift erfordert Kreuzterme \(\Lambda(m)\Lambda(n)\). Der Schlüssel ist ein **Korrelationskern**.

---

## Satz NEU-93.1 — Gewichte und Diagonalmasse

Setze

$$
\kappa_a := \gamma^2\Lambda(n)^2 W_N(r,n) \geq 0, \qquad a=(r,n).
$$

Die NEU-92-Masse ist

$$
Q_N(\varphi) = \sum_a \kappa_a\, \varphi(a).
$$

Insbesondere: \(Q_N(1) \to \gamma^2/2\) aus NEU-90. **Status: \(\checkmark[M]\)**

---

## Satz NEU-93.2 — Kanonischer Korrelationskern-Lift

Sei \(\rho_N = (\rho_N(a,b))_{a,b}\) eine positiv semidefinite (PSD) Matrix mit

$$
\rho_N(a,a) = 1 \quad\text{für alle }a.
$$

Definiere den **Korrelationskern**

$$
K_N(a,b) := \sqrt{\kappa_a}\,\sqrt{\kappa_b}\,\rho_N(a,b),
$$

und die bilineare Form

$$
B_N(f,g) := \sum_{a,b} K_N(a,b)\, f(a)\,\overline{g(b)}.
$$

Dann gilt:

1. **Diagonalreproduktion:** \(K_N(a,a) = \kappa_a\), also \(B_N(f,f)|_{\text{diag}} = Q_N(|f|^2)\).
2. **Positivität:** \(B_N(f,f) \geq 0\) für alle \(f\), da \(\rho_N\) PSD.
3. **Kreuzterme:** Für \(a=(r,m)\), \(b=(s,n)\) mit \(m\ne n\) erscheinen echte Terme \(\Lambda(m)\Lambda(n)\).

$$
\boxed{\text{Jeder PSD-Korrelationskern }\rho_N\text{ mit }\rho_N(a,a)=1\text{ hebt }\mu_N\text{ kanonisch zur positiven Quadratform.}}
$$

**Damit ist der Flaschenhals nicht mehr die Existenz von \(B_N\), sondern die kanonische Wahl von \(\rho_N\).**

**Status: \(\checkmark[M]\)**

---

## Drei Kandidaten für \(\rho_N\)

### Kandidat 1 — Diagonalkern

$$
\rho_N(a,b) = \delta_{ab}.
$$

$$
B_N(f,f) = \sum_a \kappa_a |f(a)|^2.
$$

- \(\checkmark\) Positiv, \(\checkmark\) reproduziert \(\mu_N\)
- \(\times\) Keine Kreuzterme: identisch mit NEU-92 in Quadratformsprache
- **Status: \(\checkmark[M]\) / nicht Weil-tauglich**

### Kandidat 2 — Rang-eins-Faserkern

Innerhalb jeder \(r\)-Faser:

$$
\rho_N((r,m),(r,n)) = 1 \quad \text{(alle }m,n\text{ in derselben Faser)},
$$

für verschiedene Fasern \(r \ne s\): \(\rho_N((r,m),(s,n)) = 0\).

Dann:

$$
B_N(f,f) = \sum_r \left|\sum_n \gamma\Lambda(n)\sqrt{W_N(r,n)}\, f(r,n)\right|^2.
$$

Kreuzterme explizit:

$$
\sum_r \sum_{m,n} \gamma^2\Lambda(m)\Lambda(n)\sqrt{W_N(r,m)W_N(r,n)}\, f(r,m)\overline{f(r,n)}.
$$

- \(\checkmark\) Positiv (Quadrat einer Linearkombination)
- \(\checkmark\) Reproduziert \(\mu_N\)
- \(\checkmark\) Kreuzterme \(\Lambda(m)\Lambda(n)\) für \(m\ne n\)
- \(\warning\) Alle \(m,n\) in derselben Faser gleichstark korreliert: zu grob für Weil-Grenze
- **Status: \(\checkmark[M]\) / \(\warning[M]\)**

### Kandidat 3 — Logarithmischer PSD-Kern *(Weil-Kandidat)*

In erster Näherung innerhalb einer Faser:

$$
\rho_N((r,m),(r,n)) = \Psi_N\!\left(\log\frac{m}{n}\right),
$$

allgemeiner mit faserübergreifenden Korrekturen:

$$
\rho_N((r,m),(s,n)) = \Psi_N\!\left(\log\frac{m}{n},\, \log\frac{r}{s}\right).
$$

Voraussetzung: \(\Psi_N\) ist positiv definit (etwa als charakteristische Funktion eines Maßes auf \(\mathbb{R}\)).

Kreuzterme werden dann:

$$
\gamma^2\Lambda(m)\Lambda(n)\, W_N(r,n)\, \Psi_N\!\left(\log\frac{m}{n}\right):
$$

eine echte **Mangoldt-Korrelation auf der multiplikativen/logarithmischen Achse**.

$$
\boxed{\Psi_N\!\left(\log\frac{m}{n}\right) \text{ ist der natürliche Weil-Kandidat für }\rho_N.}
$$

Die explizite Formel lebt natürlich in logarithmischen Variablen (\(n \mapsto \log n\)), und der Grenz-PSD-Kern auf \(\mathbb{R}\) sollte mit der Weil-Quadratform auf \(L^2(\mathbb{R})\) kompatibel sein.

- \(\checkmark\) Positiv (falls \(\Psi_N\) PSD)
- \(\checkmark\) Reproduziert \(\mu_N\)
- \(\checkmark\) Kreuzterme mit logarithmischer Gewichtung
- \(?\) Weil-Grenzform: zu klären
- **Status: \(\warning[O]\)**

---

## Kandidatenvergleich

| Kandidat | Positiv | Kreuzterme | Weil-tauglich |
|---|---|---|---|
| Diagonalkern | \(\checkmark\) | \(\times\) | \(\times\) |
| Rang-eins-Faserkern | \(\checkmark\) | \(\checkmark\) | \(\warning\) |
| Logarithmischer Kern \(\Psi_N(\log m/n)\) | \(\checkmark\) (falls PSD) | \(\checkmark\) | \(?[O]\) |

---

## Neue Leitfrage für NEU-94

Nicht mehr: „Finde \(B_N\).“

Sondern:

$$
\boxed{\text{Gibt es eine kanonische PSD-Familie }\Psi_N\text{, deren Grenzform mit der Weil-Quadratform kompatibel ist?}}
$$

Konkret:
- Ist \(\Psi_N(t) = e^{-|t|/2}\) oder \(\Psi_N(t) = \hat{\phi}(t/\log N)\) ein Kandidat?
- Wie sieht der Grenzkern \(\Psi_\infty(t) = \lim_N \Psi_N(t)\) aus?
- Kodiert \(\Psi_\infty\) die Nullstellenstruktur der Zetafunktion?

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | \(\kappa_a = \gamma^2\Lambda(n)^2 W_N(r,n)\) als Gewichte | \(\checkmark[M]\) |
| (B) | PSD \(\rho_N\) mit \(\rho_N(a,a)=1\) hbt \(\mu_N\) kanonisch | \(\checkmark[M]\) |
| (C) | Diagonalkern: positiv, keine Kreuzterme | \(\checkmark[M]\) |
| (D) | Rang-eins-Faserkern: Kreuzterme \(\Lambda(m)\Lambda(n)\) | \(\checkmark[M]/\warning\) |
| (E) | Logarithmischer Kern \(\Psi_N(\log m/n)\): Weil-Kandidat | \(\warning[O]\) |
| (F) | Kanonische Wahl \(\Psi_N\) und Weil-Grenzform | \(?[O]\) |

---

## Verweise

- NEU-92: Diagonalmasse \(\mu_N\); Testkegel; \(B_N(f,f)\) als Zielobjekt
- NEU-90: \(Q_N(1) \to \gamma^2/2\) (Eichung)
- NEU-88: \(W_N(r,n)\) Resolvent-Gewicht (explizite Formel)
- Weil: *Sur les formules explicites* (Quadratform auf \(L^2\))
- Connes: *Trace formula* (1999) (logarithmische Skala, multiplikative Gruppe)
- Meyer: Duke Math. J. 127 (2005) (Weil-Distribution als PSD-Kern)
- Bochner: *Monotone Funktionen, Stieltjes-Integrale* (positiv definite Kerne auf \(\mathbb{R}\))
