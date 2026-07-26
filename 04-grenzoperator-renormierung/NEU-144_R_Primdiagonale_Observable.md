# NEU-144 — $R$ als unbeschränkte primdiagonale Observable

> Stand: 9. Juli 2026.
> Anschluss: NEU-143 (T2-Abschluss, Edge-Label-Fall), NEU-141 (Mangoldt-Renormierung), NEU-133 (Primschalen-Abel).
> **Kernbefund:** Nach T2-Abschluss via Edge-Label (NEU-143) ist $R$ als primdiagonale Observable wohldefiniert — und explizit unbeschränkt mit $R_p \gtrsim p/\log p$.

---

## Leitmotiv

$$\boxed{T2 \;\checkmark \;\Longrightarrow\; R\Psi_p = R_p\Psi_p \text{ kanonisch} \;\Longrightarrow\; \operatorname{Tr}(R\Sigma) = -\frac{\zeta'}{\zeta}(\beta) \text{ für } \Re\beta > 1.}$$

Der Weg ist jetzt:

$$\underbrace{W_{\mathrm{res,rel}} = \bigoplus_{(m,p)}^\perp H_{m\to pm}}_{\text{NEU-132/133: Kantensumme}} \;\xrightarrow{\text{NEU-143}}\; T2 \;\xrightarrow{\text{NEU-141.B}}\; R \text{ primdiagonal} \;\xrightarrow{\text{NEU-144}}\; \operatorname{Sp}(R,\Sigma).$$

---

## 144.0 Voraussetzungsprüfung: Was NEU-143 geliefert hat

### 144.0.1 T2 via Edge-Label — Ergebnis

NEU-143 hat unter der Annahme

$$W_{\mathrm{res,rel}} = \bigoplus_{(m,p)}^\perp H_{m\to pm}$$

als **orthogonaler direkter Summe über Primkanten** $(m,p)$ folgendes gezeigt:

Für $p \neq q$ gilt
$$\bigoplus_m H_{m\to pm} \;\perp\; \bigoplus_n H_{n\to qn},$$
also
$$\langle \Psi_p, \Psi_q \rangle = 0 \qquad (p \neq q).$$

**T2 ist erledigt.** Die Projektoren $P_p = |\Psi_p\rangle\langle\Psi_p|$ sind paarweise orthogonal: $P_pP_q = 0$ für $p \neq q$.

### 144.0.2 Bestätigung aus NEU-132

NEU-132 definiert den Primkantenraum über Primkanten $(m \xrightarrow{p} pm)$ mit Gewichten $T_{\mathrm{rel}}(m \xrightarrow{p} pm) = \log p$. Die dyadische Schalenstruktur in NEU-132 und NEU-133 ist auf Kanten, **nicht** auf Zielindizes aufgebaut. Dies ist der Nachweis, dass Fall 1 (Edge-Label) aus NEU-142 vorliegt — nicht Fall 2 (Zielindex).

$$\boxed{\checkmark\;[M]\text{ Edge-Label-Annahme durch Konstruktion in NEU-132/133 gestützt.}}$$

**⚠️ Marker:** Die Annahme ist strukturell plausibel und durch den Aufbau von NEU-132/133 motiviert, aber noch kein formaler Beweis einer orthogonalen direkten Summe. Dieser Punkt bleibt als $\checkmark[M]$ offen für eine spätere formale Vollendung.

---

## 144.1 Definition von $R$ als primdiagonale Observable

### 144.1.1 Konstruktion

Da $T2$ gilt und $\{\Psi_p\}$ ein orthogonales System in $W_{\mathrm{res,rel}}$ bildet, definiere:

$$\boxed{R\Psi_p := R_p \Psi_p, \qquad R_p := \frac{\log p}{|c_p|^2}.}$$

Für $\xi \perp \Psi_p$ für alle $p$ setze $R\xi := 0$ (Erweiterung auf Komplementraum durch Null oder durch gesonderte Konvention — wird in NEU-145 präzisiert).

### 144.1.2 Wohldefiniertheit

Die Wohldefiniertheit folgt aus:

1. **Orthogonalität** (T2): $\langle\Psi_p, \Psi_q\rangle = 0$ für $p \neq q$ — keine Mehrdeutigkeit durch Überschneidungen.
2. **Normierung** (NEU-44.X): $\operatorname{Tr}(P_p) = |c_p|^2 > 0$ — Nenner wohldefiniert.
3. **Mangoldt-Bedingung** (NEU-141.1): $\operatorname{Tr}(R P_p) = R_p |c_p|^2 = \log p$ — Normierung konsistent.

### 144.1.3 Selbstadjungiertheit (formal)

Da $R_p \in \mathbb{R}_{>0}$ für alle $p$, gilt
$$\langle R\Psi_p, \Psi_q \rangle = R_p \langle\Psi_p, \Psi_q\rangle = 0 = \langle\Psi_p, R\Psi_q\rangle \qquad (p \neq q),$$
$$\langle R\Psi_p, \Psi_p\rangle = R_p |\Psi_p|^2 = \langle\Psi_p, R\Psi_p\rangle.$$

$R$ ist **formal selbstadjungiert** auf dem dichten Teilraum $\operatorname{span}\{\Psi_p : p \text{ prim}\}$.

---

## 144.2 Unbeschränktheit von $R$

### 144.2.1 Wachstumsordnung

Nach NEU-135D gilt $|c_p|^2 = O\!\left(\frac{(\log p)^2}{p}\right)$, daher:

$$R_p = \frac{\log p}{|c_p|^2} \gtrsim \frac{\log p}{(\log p)^2/p} = \frac{p}{\log p}.$$

$$\boxed{R_p \;\gtrsim\; \frac{p}{\log p} \;\xrightarrow{p\to\infty}\; \infty.}$$

$R$ ist **wesentlich selbstadjungiert, aber unbeschränkt.** Das ist kein Defekt, sondern die arithmetische Notwendigkeit: $R$ kodiert die Mangoldt-Gewichte $\log p$ in einem Raum, in dem die natürliche Norm wie $|c_p|^2 \sim p^{-1}(\log p)^2$ skaliert.

### 144.2.2 Operatordomäne

Der natürliche Definitionsbereich ist

$$\mathcal{D}(R) := \left\{\xi = \sum_p \xi_p \Psi_p \in W_{\mathrm{res,rel}} \;\Big|\; \sum_p R_p^2 |\xi_p|^2 < \infty \right\}.$$

Auf $\mathcal{D}(R)$ ist $R$ wohldefiniert und selbstadjungiert (im Sinne von unbeschränkten Operatoren auf Hilberträumen).

---

## 144.3 Die formale Mangoldt-Spur

### 144.3.1 Spurformel

Mit $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta) = \sum_p \frac{p^{-\beta}}{1-p^{-\beta}} P_p$ gilt formal:

$$\operatorname{Tr}(R \cdot \Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta))
= \sum_p \frac{p^{-\beta}}{1-p^{-\beta}} \operatorname{Tr}(R P_p)
= \sum_p \frac{p^{-\beta}}{1-p^{-\beta}} \log p.$$

Für $\Re\beta > 1$ ist dies absolut konvergent und gleich:

$$\boxed{\operatorname{Tr}(R \cdot \Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = -\frac{\zeta'}{\zeta}(\beta), \qquad \Re\beta > 1.}$$

### 144.3.2 Konvergenzgrenze

Die Reihe $\sum_p \frac{\log p \cdot p^{-\beta}}{1-p^{-\beta}}$ divergiert für $\Re\beta \leq 1$. Dies entspricht der Lage des Konvergenzabszisse der Dirichlet-Reihe $-\zeta'/\zeta$.

Der Übergang $\Re\beta > 1 \to 0 < \Re\beta \leq 1$ erfordert die **regulierte Spur** aus NEU-141.D (analytische Fortsetzung / Hadamard-Renormierung).

---

## 144.4 Die drei Spurklassen-Ebenen (Schärfung nach NEU-141)

| Ebene | Objekt | $\mathcal{S}_1$-Status | Konvergenzbereich |
|---|---|---|---|
| **Basis** | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ | ✅ $\mathcal{S}_1$ (NEU-137) | $\Re\beta > 0$ |
| **Mangoldt** | $R\,\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ | ✅ Spurformel | $\Re\beta > 1$ |
| **Zeta-reg.** | $\operatorname{Tr}_{\mathrm{reg}}(R\,\Sigma)$ | ❓[O] | $0 < \Re\beta \leq 1$ |

**Schärfung:** $R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ liegt für $\Re\beta > 1$ in $\mathcal{S}_1$ (als positive Spur), aber $R$ selbst ist **nicht** beschränkt und $R\Sigma$ liegt **nicht** in $\mathcal{S}_1$ für $\Re\beta \leq 1$ — der $\mathcal{S}_1$-Verlust ist arithmetisch erzwungen durch $R_p \gtrsim p/\log p$.

---

## 144.5 Statusdiagnose und Arbeitsplan

$$\boxed{R \text{ primdiagonal definiert. } \operatorname{Tr}(R\Sigma) = -\zeta'/\zeta \text{ für } \Re\beta > 1. \text{ Offen: regulierte Spur für } 0 < \Re\beta \leq 1.}$$

| Eintrag | Inhalt | Voraussetzung | Status |
|---|---|---|---|
| **NEU-144.A** | $R$ primdiagonal definiert | T2 (NEU-143) | ✅ |
| **NEU-144.B** | $R_p \gtrsim p/\log p$, $R$ unbeschränkt | NEU-135D | ✅ |
| **NEU-144.C** | $\operatorname{Tr}(R\Sigma) = -\zeta'/\zeta$ für $\Re\beta > 1$ | 144.B | ✅ |
| **NEU-144.D** | $\mathcal{D}(R)$ präzisieren, Selbstadjungiertheit formal | 144.A | ✅[M] |
| **NEU-145** | Regulierte Spur für $0 < \Re\beta \leq 1$ | 144.C + analyt. Forts. | ❓[O] |

---

## 144.6 Offene Prüffragen

**[O-144-1]** Ist die Edge-Label-Annahme ($W_{\mathrm{res,rel}}$ als orthogonale Kantensumme) formal beweisbar aus der Konstruktion in NEU-44 / NEU-132? Oder bleibt sie Strukturhypothese?

**[O-144-2]** Wie präzisiert man $\mathcal{D}(R)$ im Verhältnis zu $\mathcal{D}(\Sigma_{\mathrm{rel}}^{\mathrm{ren}})$? Ist $\mathcal{D}(R) \cap \mathcal{D}(\Sigma) \neq \{0\}$ dicht in $W_{\mathrm{res,rel}}$?

**[O-144-3]** Welche Regularisierungsmethode für $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma)$, $0 < \Re\beta \leq 1$? Kandidaten:
- Analytische Fortsetzung von $\beta \mapsto \operatorname{Tr}(R\Sigma(\beta))$
- Hadamard-Renormierung (Subtraktion divergenter Terme)
- Resolventenartige Regularisierung $(R + \varepsilon)^{-1}$ und Grenzwert $\varepsilon \to 0$

**Nächste Nummer:** NEU-145 — Regulierte Spur für $0 < \Re\beta \leq 1$.

---

## Verweise

- **NEU-143**: T2-Abschluss im Edge-Label-Fall
- **NEU-142**: T2-Label-Audit, Bifurkation edge vs. vertex
- **NEU-141**: Unbeschränkte Mangoldt-Renormierung, drei Spurklassen-Ebenen
- **NEU-137**: Spurklassen-Summierbarkeit $\Sigma_{\mathrm{rel}}^{\mathrm{ren}} \in \mathcal{S}_1$
- **NEU-135D**: Wachstum $|c_p|^2 = O((\log p)^2/p)$
- **NEU-133**: Primschalen-Abel-Mechanismus
- **NEU-132**: H1/H2/H3-rel, Primkantenraum-Definition
- **NEU-44.X**: $P_p = |\Psi_p\rangle\langle\Psi_p|$, $\operatorname{Tr}P_p = |c_p|^2$
