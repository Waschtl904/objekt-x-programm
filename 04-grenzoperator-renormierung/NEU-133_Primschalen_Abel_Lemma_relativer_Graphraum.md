# NEU-133 — Primschalen-Abel-Lemma im relativen Graphraum

> Stand: Juli 2026.  
> Anschluss: NEU-132 (H1/H2/H3-rel), NEU-131 (abstraktes Lemma), NEU-130 (PSWF-Brücke).  
> **Kernfrage:** Kann die dyadische Abel-Summation aus PSWF Paper VII auf Primkanten übertragen werden?

---

## Leitmotiv

$$\boxed{NEU\text{-}132\text{ ist der Punkt, an dem die Doppelbarriere von einem Normierungsproblem zu einem Kancellationsproblem geworden ist.}}$$

Das bedeutet: Nicht mehr $W_N > 0$ ist der entscheidende Test, sondern:

$$\boxed{\text{Gibt es auf }H_{rel,N}\text{ eine Primschalen-Abel-Summation?}}$$

---

## 133.0 Die drei Schlüsselgrößen

Minimal müssen folgende drei Summen verstanden werden:

$$\boxed{\text{(I) } \sum_{p\sim 2^m}\|C_p^{rel}\|^2,
\qquad
\text{(II) } \sum_{p\sim 2^m}\frac{\|C_p^{rel}\|^2}{p},
\qquad
\text{(III) } \sum_{p\sim 2^m}e^{i\phi(p)}\|C_p^{rel}\|^2.}$$

| Summe | Was sie misst | Warum kritisch |
|---|---|---|
| **(I)** | Rohe Schalenenergie | Falls $\to \infty$: Metrik nicht summierbar |
| **(II)** | Dirichlet-gedämpfte Schalenenergie | Falls $= O(1/m)$: Schur-Kontrolle möglich |
| **(III)** | Oszillatorische Schalenenergie | Falls $= o(\text{I})$: echte Kancellation vorhanden |

Nur wenn (II) die richtige Größenordnung hat **und** (III) kleiner als (I) ist,
liefert die Primschalen-Struktur eine Schur-Kontrolle analog zu Paper VII.

---

## 133.1 Arithmetische Grundbilanz der Primschale $\mathcal{P}_m$

Die dyadische Primschale $\mathcal{P}_m = \{p \text{ prim} : 2^m \leq p < 2^{m+1}\}$ hat:

$$|\mathcal{P}_m| \sim \frac{2^m}{m} \qquad (\text{PNT})$$

Drei kanonische Summen über $\mathcal{P}_m$:

$$\sum_{p \in \mathcal{P}_m} \frac{1}{p} \sim \frac{1}{m}
\qquad \text{(log-Dämpfung, gut)}$$

$$\sum_{p \in \mathcal{P}_m} \frac{\log p}{p} \sim 1
\qquad \text{(Mangoldt-gewichtet, neutral)}$$

$$\sum_{p \in \mathcal{P}_m} 1 \sim \frac{2^m}{m}
\qquad \text{(ungedämpft, gefährlich)}$$

**Fazit:** Ohne Dirichlet-Dämpfung oder Kancellation wächst die Schalenenergie wie $2^m/m$.
Mit $1/p$-Dämpfung kollabiert sie auf $1/m$. Summation über alle $m \leq M$ gibt:

$$\sum_{m \leq M} \frac{1}{m} \sim \log M \qquad \text{(logarithmisch divergent).}$$

Das ist exakt die PSWF-Situation: $\sup_i \sum_j |P_{ij}| \leq C c^{-1/2} \log c$.
Der $\log$-Faktor ist unvermeidlich — er ist die **arithmetische Signatur der kritischen $1/p$-Zone**.

---

## 133.2 Warnung: Wo sitzt die Dirichlet-Dämpfung?

Bei der metrischen Self-Energy

$$\Sigma_{rel,N}(\beta_0) = \sum_{p \leq N} \frac{C_p^{rel}(C_p^{rel})^\#}{1-p^{-\beta_0}}$$

ist der Faktor $(1-p^{-\beta_0})^{-1} \approx 1$ für große $p$. Die $1/p$-Dämpfung kommt hier
**nicht** aus dem Metrikfaktor, sondern müss aus $\|C_p^{rel}\|^2$ selbst kommen.

$$\boxed{\text{Man muss exakt bestimmen, wo die Dirichlet-Dämpfung in den relativen Matrixelementen sitzt.}}$$

Drei Möglichkeiten:

| Quelle der $1/p$-Dämpfung | Bedingung | Konsequenz |
|---|---|---|
| In $\|C_p^{rel}\|^2 \sim p^{-1}$ | Kanalgewichte fallen mit $1/p$ | Schale (II) = $O(1/m^2)$: gut |
| In Spurstruktur / Determinante | Implizite Normierung | Muss gesondert gezeigt werden |
| Gar nicht | $\|C_p^{rel}\|^2 = O(1)$ | Schale (I) $\sim 2^m/m$: gefährlich |

Solange unbekannt, welcher Fall vorliegt, ist $\Sigma_{rel,N}(\beta_0) > 0$ nicht ausreichend.

---

## 133.3 Der Primschalen-Abel-Mechanismus (Formulierungsversuch)

**Vorbedingung:** Sei $\mathcal{P}_m$ die $m$-te dyadische Primschale und

$$S_m^{rel} := \sum_{p \in \mathcal{P}_m} \frac{A_p^{rel}}{p}\, e^{i(\log p)\cdot u}, \qquad A_p^{rel} := p \cdot \|C_p^{rel}\|^2.$$

Dann ist $A_p^{rel}$ die **normierte Schalenenergie** (analog zu $A_{ij} = P_{ij} \cdot c^{1/2}$ in Paper VII).

**Abel-Summation auf $\mathcal{P}_m$** (analog zu Paper VII, Steps 2–5):

$$|S_m^{rel}| \leq \frac{C_u}{2^m} \cdot \sup_p A_p^{rel} + C \cdot \mathrm{TV}(A^{rel}; \mathcal{P}_m)$$

**Bedingungen:**
1. **(H3-rel)** $A_p^{rel} \leq C_3$ gleichmäßig — die normierte Schalenenergie bleibt beschränkt.
2. **(H1-rel)** $|\sum_{p \in [P,2P]} e^{i(\log p)u}| \leq C_u/|u|$ — Dirichlet-Kern-Schranke für $\log p$-Phase.
3. **(H2-rel)** $\mathrm{TV}(A^{rel}; \mathcal{P}_m) = o(1)$ — Amplitudenregularität.

**Schluss (falls alle drei gelten):**

$$\sum_{m \leq M} |S_m^{rel}| = O(\log M),$$

also Schur-Zeilennorm im Primkantenraum $= O(\log N)$ — exakt die PSWF-Signatur.

---

## 133.4 H1-rel: Ist die Primclock-Kancellation real?

Die H1-rel-Bedingung verlangt eine Dirichlet-Kern-Schranke für

$$\left|\sum_{p \in [P,2P]} e^{i(\log p)u}\right| \leq \frac{C_u}{|u|}.$$

Das ist **nicht trivial** und nicht automatisch aus PNT. Es entspricht einer Gleichverteilung
der Winkel $\log p \pmod{2\pi/u}$ — einer Weyl-Summen-Schranke für Primzahlen.

Bekannte Resultate:
- Für $u \in \mathbb{R}$, $u \neq 0$: $\sum_{p \leq X} p^{-iu} = o(\pi(X))$ — folgt aus PNT in arithmetischen Progressionen / Vinogradov.
- Für $u$ nahe $0$ (d.h. $\beta_0$ nahe Spektralparameter): potenziell gefährlich.

$$\boxed{H1\text{-rel ist real für }u \text{ weg von }0 \text{ — aber gefährdet genau dort, wo }\beta_0 \approx s.}$$

Das verbindet sich direkt mit der NEU-128B-Warnung: $\beta = s \Rightarrow \Sigma_N(s)$ ist Weyl-Funktion, keine Metrik.
Für $\beta_0$ fest und weg von $s$: H1-rel plausibel.

---

## 133.5 Statusdiagnose: Die drei Schlüsselgrößen

| Summe | Status | Abhängigkeit |
|---|---|---|
| $\sum_{p\sim 2^m}\|C_p^{rel}\|^2$ | ❓[O] | Kanalgewichte $\|C_p^{rel}\|^2$ unbekannt |
| $\sum_{p\sim 2^m}\|C_p^{rel}\|^2/p$ | ❓[O] | Voraussetzt $\|C_p^{rel}\|^2 = O(1)$ oder besser |
| $\sum_{p\sim 2^m}e^{i\phi(p)}\|C_p^{rel}\|^2$ | ❓[O] | H1-rel + H2-rel erforderlich |
| **Primschalen-Abel gesamt** | ❓[O] | Alle drei + Abel-Struktur |

$$\boxed{\checkmark[M]\text{ als Kancellationsmechanismus identifiziert.}\quad ?[O]\text{ als quantitativer Beweis.}}$$

---

## 133.6 Neue Formulierung des Gesamtprogramms

Die Kette NEU-130 → NEU-131 → NEU-132 → NEU-133 liefert jetzt:

| Eintrag | Inhalt | Fortschritt |
|---|---|---|
| NEU-130 | PSWF = Modellfall für Prä-Lanczos | Strukturanalogie |
| NEU-131 | B-strong = Punktschranken-Komponente | Dreistufige Mechanik |
| NEU-132 | H1/H2/H3-rel im Primkantenraum | Übertragungsrahmen |
| **NEU-133** | **Drei Schlüsselgrößen + Abel-Formulierung** | **Quantitativer Prüfstein** |

Die Doppelbarriere hat jetzt eine **operative Diagnose**:

$$\boxed{b_{1,N} \to 0 \iff \text{Primschalen-Schalenenergie (I) divergiert schneller als Kancellation (III) kompensiert.}}$$

Und der Test für $W_N$:

$$W_N \text{ löst die Doppelbarriere} \iff W_N \text{ erzeugt H1-rel + H2-rel + H3-rel auf } H_{rel,N}.$$

---

## Verweise

- **NEU-132**: H1/H2/H3-rel, Analogietabelle PSWF vs. Primkantenraum
- **NEU-131**: B-strong als Punktschranken-Komponente
- **NEU-128B**: Warnung $\beta = s$: Weyl-Funktion, keine Metrik
- **NEU-125**: Skalare Renormierung unzureichend
- `paper7_skeleton.tex`: Vollständiger Abel-Beweis (Appendix A)
