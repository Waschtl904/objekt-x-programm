# NEU-132 — H1/H2/H3-rel: PSWF-Abel-Mechanismus im Primkantenraum

> Stand: Juli 2026.  
> Anschluss: NEU-131 (Abstraktes Edge-Schur-Nelson-Lemma), NEU-130 (PSWF-Brücke),
> NEU-125 (Prä-Lanczos-Skala), NEU-44 (relative Primkanten-Struktur).  
> **Kernfrage:** Gibt es im relativen Primkantenraum ein Analogon der dyadischen Abel-Summation?

---

## Leitmotiv

$$\boxed{NEU\text{-}44 \text{ liefert die richtigen Kan\xe4le.}\quad NEU\text{-}131 \text{ sagt, dass Kan\xe4le allein nicht reichen.}\quad NEU\text{-}132 \text{ sucht die Kancellation auf diesen Kan\xe4len.}}$$

---

## 132.0 Ausgangslage: Die dreistufige Struktur aus NEU-131

NEU-131 hat gezeigt: B-strong ist **nicht** selbst die Nelson-Zeilennorm,
sondern nur die erste Stufe eines dreistufigen Mechanismus:

$$\underbrace{P_{kl} \leq C_2 c^{1/2}}_{\text{H3: Punktschranke}}
+ \underbrace{\text{H1 (Phase) + H2 (Amplitudenregularit\xe4t)}}_{\text{Kancellationsstruktur}}
\Rightarrow
\underbrace{\sup_i \sum_j |P_{ij}| \leq C c^{-1/2}\log c}_{\text{Schur-/Nelson-Zeilennorm}}.$$

Für das Jacobi-/RH-Programm ergibt sich daraus: **Positivität allein reicht nicht.**
Eine positive Metrik $W_N > 0$ ohne Kancellationsstruktur kann die Doppelbarriere
konservieren oder nur verschieben.

Die vollständige dreistufige Transferaufgabe lautet:

$$\boxed{\text{relative Punktschranke} + \text{relative Primkanten-Kancellation}
+ \text{relative Schur-/Nelson-Summation}
\Rightarrow b_{1,N}^{rel}\asymp 1,\; b_{2,N}^{rel}/b_{1,N}^{rel}=O(1).}$$

---

## 132.1 Neue Lesart der Doppelbarriere

Die Doppelbarriere

$$b_{1,N} \to 0, \qquad b_{2,N}/b_{1,N} \to \infty$$

darf ab jetzt **nicht mehr nur als Gr\xf6\xdfenproblem** gelesen werden,
sondern als **Fehlen einer Kancellationsstruktur**:

$$\boxed{\text{Die Barriere entsteht, weil die ersten Lanczos-Schalen
nicht nur falsch skaliert, sondern falsch summiert sind.}}$$

Konsequenz (aus NEU-125.4):
Skalare Prä-Lanczos-Renormierung scheitert nicht nur am Quotienten $b_{2,N}/b_{1,N}$,
sondern auch daran, dass sie keine Summationsordnung auf den Primkan\xe4len erzwingt.
Eine gute $W_N$-Metrik muss nicht nur einzelne Kopplungen normalisieren,
sondern eine **primkanal-dyadische Summationsordnung** erzwingen.

---

## 132.2 PSWF-Hypothesentransfer: H1-rel, H2-rel, H3-rel

### H3-rel — Relative Punktschranke (Analogon B-strong)

Die Kopplungen $P_{pq}^{rel}$ zwischen Primkan\xe4len $p, q$ m\xfcssen gleichm\xe4\xdfig beschr\xe4nkt sein:

$$\|P_{pq}^{rel}\| \leq C \cdot \Lambda_{rel},$$

wobei $\Lambda_{rel}$ eine intrinsische Skala aus der relativen Feshbach-/Schur-Komplementstruktur ist.
**Ohne H3-rel:** kein Startpunkt f\xfcr Abel-Summation.

### H1-rel — Relative Phasen-/Clock-Kancellation

Die relativen Primkanten tragen Gewichte $T_{rel}(m \xrightarrow{p} pm) = \log p$.
Gesucht ist eine Aussage der Form:

$$\sum_{p \sim P} e^{i\phi(p,m)} \cdot (\text{rel. Kopplungsgewicht})
\quad \text{kancelliert dyadisch/primschalig,}$$

mit einer nicht-degenerierten "Primclock"-Phasenstruktur analog zu H1 (PSWF: $\alpha^{(c)} = \pi/2 + O(c^{-1/3})$).

**Schl\xfcsselfrage H1-rel:** Erzeugt $\log p$ als Primclock eine Dirichlet-Kern-Schranke
$|\sum_{p\sim P} e^{i(\log p)\cdot u}| \leq C_u < \infty$ gleichm\xe4\xdfig in $u$?

Das w\xe4re die direkte Entsprechung von $|{B}(s,t)| \leq 2/|1 - e^{i\alpha}|$ aus Paper VII.

### H2-rel — Relative Amplitudenregularit\xe4t

Die Amplituden $\|C_p^{rel}\|$, $\|\widetilde{\Psi}_p\|_{W_{res,rel}}$
d\xfcrfen nicht wild zwischen benachbarten Primschalen schwanken:

$$|A_{pq}^{rel} - A_{p'q}^{rel}| \leq \delta_m \frac{A_{pq}^{rel}}{2^m}
\quad \text{f\xfcr } p, p' \text{ in derselben Primschale.}$$

Das ist das Analogon zu H2 (PSWF): blockweise Amplitudenregularit\xe4t.
**Ohne H2-rel:** Abel-Summation bricht zusammen, weil das Total-Variation-Argument versagt.

---

## 132.3 Die Schl\xfcsselfrage

$$\boxed{\text{Gibt es im relativen Primkantenraum ein Analogon der dyadischen Abel-Summation?}}$$

Das hei\xdft konkret: Kann man die Primkan\xe4le $p_1 < p_2 < \ldots$ in dyadische Schalen

$$\mathcal{P}_m := \{p \text{ prim} : 2^m \leq p < 2^{m+1}\}$$

gruppieren und Abel-Summation auf jeder Schale $\mathcal{P}_m$ durchf\xfchren,
analoge zu $\mathcal{B}_m(i) = \{j : 2^m \leq |i-j| < 2^{m+1}\}$ in Paper VII?

Dann w\xe4re die Gesamtkontrolle:

$$\sup_m \left|\sum_{p \in \mathcal{P}_m} \frac{A_{pm}^{rel}}{p} e^{i(\log p)\cdot u}\right| = O(2^{-m}),$$

und Summation \xfcber $m$ liefert die Schur-Zeilennorm im Primkantenraum.

---

## 132.4 Analogietabelle: PSWF vs. Primkantenraum

| Strukturelement | PSWF (Paper VII) | Primkantenraum (rel.) |
|---|---|---|
| Indexraum | $\{1,\ldots,N\}$, Abstand $|i-j|$ | Primzahlen $p$, Abstand $\log p$ |
| Dyadische Schale | $\mathcal{B}_m(i) = \{j : 2^m \leq |i-j| < 2^{m+1}\}$ | $\mathcal{P}_m = \{p : 2^m \leq p < 2^{m+1}\}$ |
| Kernel | $|i-j|^{-1} e^{i\alpha(i-j)}$ | $p^{-1} e^{i(\log p)u}$ (Dirichlet-Reihe) |
| Phase (H1) | $\alpha^{(c)} = \pi/2 + O(c^{-1/3})$ | $\log p$-Clock, $u$-Richtung |
| Dirichlet-Schranke | $|{B}(s,t)| \leq 2/|1-e^{i\alpha}|$ | $|\sum_{p\in[P,2P]} p^{-iu}| \leq C/|u|$ (Mertens/PNT-analog) |
| Amplitude (H2) | Blockweise Regularit\xe4t von $A_{ij}$ | Regularit\xe4t von $\|C_p^{rel}\|$ \xfcber $\mathcal{P}_m$ |
| Punktschranke (H3) | $A_{ij} \leq C_2$ (B-strong normiert) | $\|P_{pq}^{rel}\| \leq C\Lambda_{rel}$ |
| Ergebnis | $\sup_i \sum_j |P_{ij}| \leq Cc^{-1/2}\log c$ | $\sup_m \|\text{Primschalen-Zeilennorm}\| = O(1)$ |

---

## 132.5 Warnung: Primzahlen sind kein gleichm\xe4\xdfiges Gitter

Der wesentliche Unterschied zu PSWF: Die Primzahlen bilden **kein gleichm\xe4\xdfiges Gitter**.
Der PNT gibt $|\mathcal{P}_m| \sim 2^m/m$ (statt $\sim 2^m$ f\xfcr Integers).
Daher ist das Total-Variation-Argument in H2 zust\xe4tzlich durch
die logarithmische Versd\xfcnnung der Primzahlen kontrolliert.

Das k\xf6nnte ein **Vorteil** sein: Die nat\xfcrliche $1/p$-Abnahme in Dirichlet-Reihen
kompensiert die h\xf6here Summationszahl.

Oder ein **Nachteil**: Amplitudenregularit\xe4t H2-rel zwischen benachbarten Primzahlen
ist schwerer zu erzwingen als zwischen benachbarten Integers.

**Offen:** Welche der beiden Wirkungen dominiert f\xfcr $H_{rel,N}$?

---

## 132.6 Statusdiagnose

| Hypothese | Status |
|---|---|
| H3-rel (Punktschranke $\|P_{pq}^{rel}\| \leq C\Lambda_{rel}$) | ❓[O] — h\xe4ngt von Feshbach-Skala $\Lambda_{rel}$ ab |
| H1-rel (Primclock-Kancellation) | ❓[O] — Dirichlet-Reihen-Schranke f\xfcr $\log p$-Phase |
| H2-rel (Amplitudenregularit\xe4t \xfcber $\mathcal{P}_m$) | ❓[O] — Primverteilung vs. Blockregularit\xe4t |
| **Gesamtmechanismus** H1+H2+H3-rel | ❓[O] — abstraktes Transferlemma (NEU-131) |

$$\boxed{\checkmark[M]\text{ als Strukturdiagnose.}\quad ?[O]\text{ als formaler Beweis.}}$$

---

## Verweise

- **NEU-131**: Abstraktes Edge-Schur-Nelson-Lemma (B-strong = Punktschranken-Komponente)
- **NEU-130**: PSWF-Br\xfccke (Edge-Koerzivit\xe4t als Modell)
- **NEU-125**: Pr\xe4-Lanczos-Skala (skalare vs. gradierte Feshbach-Gewichtung)
- **NEU-44**: Relative Primkanten-Struktur und Kan\xe4le
- `paper7_skeleton.tex`: Theorem 2.1 (Dyadische Kancellation), Assumption 3.1 (B-strong)
- `paper8_scale_separated.tex`: H2-Amplitudenregularit\xe4t
