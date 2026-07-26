# NEU-112 — Herglotz-Weil-Test: Nullstellenterm und Renormierung

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-111 (Pfadordnung; \(m_{\mathrm{arith}}\) primär; Herglotz-Weil-Test und Jacobi-Realisierungstest)  
**Nächste Nummer:** NEU-113

---

## Ausgangspunkt

NEU-111 stellt zwei präzise Tests auf. NEU-112 führt Test 1 (Herglotz-Weil-Test) durch und trennt den strukturell positiven Befund (Nullstellenterm) vom offenen Teil (Renormierung).

---

## Satz NEU-112.1 — Stieltjes-Struktur von \(m_{\mathrm{arith}}\)

Unter RH liegen die nichttrivialen Nullstellen bei \(\rho = \frac{1}{2}+i\gamma\). Die logarithmische Ableitung liefert formal:

$$
m_{\mathrm{arith}}(z)
= -i\frac{\xi'}{\xi}\!\left(\tfrac{1}{2}+iz\right)
\sim
\sum_\gamma \frac{1}{\gamma-z}
+ m_{\Gamma,\mathrm{ren}}(z),
$$

wobei \(m_{\Gamma,\mathrm{ren}}\) die archimedischen und polaren Renormierungsbeiträge trägt. Das zugehörige Spektralmaß auf der reellen \(\gamma\)-Achse ist:

$$
\mu_\xi = \sum_\gamma \delta_\gamma + \mu_{\Gamma,\mathrm{ren}}.
$$

Das ist ein Stieltjes-Nullstellenmaß auf der richtigen Achse.

**Status: \(\checkmark[M]\)** (unter RH)

---

## Satz NEU-112.2 — Nullstellenterm-Test: strukturell positiv

Auf Bombieris Paley\u2013Wiener-Testfunktionsraum \(PW_t\) erscheint der Nullstellenterm der Weil-Form als:

$$
Q_{\mathrm{zeros}}[f] = \sum_\gamma |\widehat{f}(\gamma)|^2
$$

(in geeigneter Bombieri-Normalisierung). Der Nullstellenanteil von \(m_{\mathrm{arith}}\) liefert genau diesen Term: Die Stieltjes-Darstellung \(\sum_\gamma 1/(\gamma-z)\) wirkt auf \(\widehat{f}\) durch Residuen-Auswertung bei \(z=\gamma\) und erzeugt \(\sum_\gamma |\widehat{f}(\gamma)|^2\).

$$
\boxed{\text{Der Herglotz-Nullstellenanteil passt strukturell zu Bombieris Nullstellenterm.}}
$$

**Status: \(\checkmark/\warning[M]\)** (struktureller Befund; Normalisierungsdetails offen)

---

## Satz NEU-112.3 — Schutzformulierung

$$
\boxed{m_{\mathrm{arith}} \text{ ist nicht }Q_{\mathrm{Weil}},
\text{ sondern der Herglotz-Träger seines Nullstellenanteils.}}
$$

Die volle Weil-Form enthält zusätzlich:

$$
Q_{\mathrm{Weil}}[f]
= Q_{\mathrm{zeros}}[f]
+ Q_{\Gamma}[f]
+ Q_{\mathrm{poles/trivial}}[f]
+ Q_{\mathrm{prime}}[f],
$$

und alle Terme müssen auf demselben Testfunktionsraum mit derselben Fourier-/Mellin-Normalisierung und denselben Vorzeichenkonventionen stehen.

**Status: \(\checkmark[M]\)**

---

## Test NEU-112.4 — Renormierungstest (offen)

Der eigentliche offene Punkt ist nicht der Nullstellenterm, sondern:

$$
m_{\Gamma,\mathrm{ren}}(z)
+
\text{Pol-/triviale Nullstellen-Terme}
+
\text{Primseite}
\stackrel{?}{=}
Q_\Gamma[f] + Q_{\mathrm{poles}}[f] + Q_{\mathrm{prime}}[f]
$$

auf Bombieris Testfunktionsraum in exakter Normalisierung.

Zwei mögliche Ausfälle:
- **Test 1 scheitert:** \(m_{\mathrm{arith}}\) ist falsch normalisiert \(\Rightarrow\) Skalierungskorrektur nötig
- **Test 1 gelingt, Test 2 scheitert:** \(m_{\mathrm{arith}}\) ist nur der Nullstellenkanal; archimedische Terme fehlen noch

**Status: \(\checkmark[M]\)** (Test formuliert) / **\(?[O]\)** (Auswertung offen)

---

## Tabellarische Statusklassifikation

| Satz | Inhalt | Status |
|------|--------|--------|
| 112.1 | \(m_{\mathrm{arith}}\) Stieltjes-Nullstellenmaß \(\sum_\gamma\delta_\gamma\) | \(\checkmark[M]\) |
| 112.2 | Nullstellenterm \(\leadsto \sum_\gamma|\widehat{f}(\gamma)|^2\) strukturell | \(\checkmark/\warning[M]\) |
| 112.3 | Schutz: \(m_{\mathrm{arith}}\) = Herglotz-Träger, nicht \(Q_{\mathrm{Weil}}\) | \(\checkmark[M]\) |
| 112.4 | Renormierungstest: \(m_{\Gamma,\mathrm{ren}}+\text{Pol}+\text{Prim} \stackrel{?}{=} Q_{\Gamma}+Q_{\mathrm{poles}}+Q_{\mathrm{prime}}\) | \(?[O]\) |
| 112.5 | Jacobi-Anschluss erst nach \(m_{\Omega,N}\to m_{\mathrm{arith}}\) | \(?[O]\) |

---

## Neue Leitfrage für NEU-113

$$
\boxed{\text{Bombieri-Normalisierung exakt fixieren: }
f \mapsto \widehat{f},\;
Q_{\mathrm{zeros}}[f],\;
Q_\Gamma[f],\;
Q_{\mathrm{prime}}[f].}
$$

Konkrete Schritte:
1. Bombieri-Testfunktionsraum \(PW_t\): gerade \(L^2\)-Funktionen, Träger \([-t,t]\), Fourier-Normalisierung
2. \(Q_{\mathrm{zeros}}[f] = \sum_\rho \widehat{f}(\rho)\): Summation über alle \(\rho\) oder nur kritische?
3. \(Q_\Gamma[f]\): Welche Mellin-Normalisierung? Verbindung zu PSWF-Korrekturen Connes\u2013Consani?
4. \(Q_{\mathrm{prime}}[f] = \sum_p \sum_{k\ge1} f(k\log p)\log p / p^{k/2}\)?
5. Einsetzen: \(m_{\mathrm{arith}}\) Stieltjes in Bombieri-Form \(\Rightarrow\) Vergleich Vorzeichen und Normierung
6. Danach: \(m_{\Omega,N}\to m_{\mathrm{arith}} \Rightarrow Q_{\Omega,N}\to Q_{\mathrm{Weil}}?\)

---

## Verweise

- NEU-111: Pfadordnung; Herglotz-Weil-Test
- NEU-63D: \(m_{\mathrm{arith}}(z)\) Herglotz \(\Leftrightarrow\) RH
- **Bombieri:** *Remarks on Weil's quadratic functional in number theory* (2000)
- **Connes:** *Trace formula in noncommutative geometry* (1999)
- Connes & Consani: PSWF-Korrekturen archimedisch
