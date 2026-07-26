# NEU-122 — KMS/GNS-Jacobi-Eintrittstest und spektrale Ausweichspur

**Datum:** 4. Juli 2026
**Anschluss:** NEU-119, NEU-120, NEU-121
**Status:** ?[O] — Entscheidungsblatt, kein Beweisblatt

---

## 122.W — Übernommener Warnsatz (NEU-120.W)

Für jeden endlichen selbstadjungierten Jacobi-Operator gilt:

$$m_{\Omega,N}(z) = \langle \Omega_N,(A_N^{\mathrm{Jac},-}-z)^{-1}\Omega_N\rangle$$

ist eine Herglotz-Funktion. Daher:

$$m_{\Omega,N} \longrightarrow m_{\mathrm{arith}} \quad\text{(lokal gleichmäßig)} \quad\Longrightarrow\quad m_{\mathrm{arith}}\text{ ist Herglotz} \quad\Longleftrightarrow\quad \mathrm{RH}.$$

Der Grenzübergang $m_{\Omega,N}\to m_{\mathrm{arith}}$ ist kein technischer Approximationstrick,
sondern bereits der harte RH-Kern. ✓[M]

---

## 122.0 — Anti-Fitting-Axiom

**Vor allen weiteren Schritten wird festgehalten:**

Die Objekte

$$\mathcal{H}_N, \quad A_N^{\mathrm{Jac},-}, \quad \Omega_N^{\mathrm{KMS}}$$

dürfen **nicht** nachträglich anhand von $C_\xi$, Bombieri-Gewichten oder
Nullstelleninformationen gewählt oder angepasst werden.

Geschieht das dennoch, wiederholt NEU-122 exakt den leeren K1/K3-Mechanismus:
der Moment ist dann wieder ein freier Parameter, keine arithmetische Aussage.

---

## 122.C — Normalisierungskonflikt bei $C_\xi$

NEU-121 verwendet den Momentzielwert

$$C_\xi = -\frac{\xi'(0)}{\xi(0)} = 1 + \frac{\gamma_E}{2} - \frac{1}{2}\log(4\pi).$$

**Direkte numerische Auswertung:**

$$1 + \frac{\gamma_E}{2} - \frac{1}{2}\log(4\pi)
= 1 + \frac{0.5772\ldots}{2} - \frac{\log(4\pi)}{2}
\approx 1 + 0.2886 - 1.2655
\approx +0.0231,$$

**nicht** $-0.549$.

Es liegt ein Normalisierungskonflikt vor. Zwei Möglichkeiten:

| Option | Konsequenz |
|--------|-----------|
| Die Formel $C_\xi = -\xi'(0)/\xi(0)$ ist maßgeblich | Zielwert ist $\approx +0.0231$; NEU-121-Zahlenwert muss korrigiert werden |
| Zielwert $-0.549$ ist gewollt | Dieser Koeffizient stammt aus einer anderen Normierung (z.B. verschobener $z$-Variable oder anderer $\xi$-Konvention); muss explizit als $C_\xi^{\mathrm{ren}}$ ausgewiesen werden |

**Bis zur Klärung:**
Der Moment-1-Test darf nicht als numerisch bestimmter Validierungstest eingesetzt werden.

- Formelrechnung: ✓[M]
- NEU-121-Zahlenwert $-0.549$: ⚠[M] Normalisierungskonflikt, Klärung erforderlich

---

## Teil A — Harte Route: KMS/GNS $\longrightarrow$ Jacobi

### 122.1 — KMS-Gewicht versus normalisierter GNS-Zustand

Definiere das endliche KMS-artige Gewicht (unnormalisiert):

$$\tau_{\beta,N}(T) = \sum_{n \le N} n^{-\beta}\langle e_n, T e_n\rangle, \qquad Z_{\beta,N} = \tau_{\beta,N}(1) = \sum_{n \le N} n^{-\beta}.$$

Der normalisierte Zustand ist $\varphi_{\beta,N}(T) = Z_{\beta,N}^{-1}\,\tau_{\beta,N}(T)$.

Bei $\beta = 1$:

$$Z_{1,N} = H_N = \log N + \gamma_E + o(1), \qquad Z_{1,N}^{-1} \sim \frac{1}{\log N}.$$

**Schlüsselbeobachtung (Anti-Fitting):**

Wenn $\Omega_N^{\mathrm{KMS}}$ aus dem *unnormalisierten* Gewicht $\tau_{1,N}$ stammt, dann lautet der Momenttest

$$R_N \cdot \langle \Omega_N^{\mathrm{KMS}},\, A_N^{\mathrm{Jac},-}\,\Omega_N^{\mathrm{KMS}}\rangle.$$

Wenn man stattdessen den normalisierten GNS-Vektor $\widehat{\Omega}_N^{\mathrm{KMS}} = Z_{1,N}^{1/2}\,\Omega_N^{\mathrm{KMS}}$ benutzt, ist derselbe Test

$$\langle \widehat{\Omega}_N^{\mathrm{KMS}},\, A_N^{\mathrm{Jac},-}\,\widehat{\Omega}_N^{\mathrm{KMS}}\rangle.$$

Damit ist $R_N \sim 1/\log N$ **nicht** externe Bombieri-Anpassung, sondern genau die
GNS-Normalisierung des endlichen KMS-Gewichts. K2 ist sauberer als K1/K3.

✓[M] unter Dirichlet-Cutoff $n \le N$

---

### 122.2 — P1: KMS/GNS-Einbettung in den Jacobi-Formalismus

**Gesucht:** Eine kanonische Konstruktion

$$\tau_{\beta,N} \;\longrightarrow\; \bigl(\mathcal{H}_{\beta,N}^{\mathrm{GNS}},\,\pi_{\beta,N},\,\Omega_{\beta,N}\bigr) \;\longrightarrow\; A_N^{\mathrm{Jac},-}.$$

**Minimalforderung:**
Es muss ein vorab fixiertes selbstadjungiertes Element $\mathcal{A}_N^-$ in der
GNS-Darstellung existieren, sodass $A_N^{\mathrm{Jac},-}$ die Jacobi-Matrix der
*zyklischen* Darstellung von $\mathcal{A}_N^-$ bezüglich $\Omega_{\beta,N}$ ist.

Konkret erzeugt die Krylov-Kette

$$\Omega_{\beta,N},\quad \mathcal{A}_N^-\Omega_{\beta,N},\quad (\mathcal{A}_N^-)^2\Omega_{\beta,N},\;\ldots$$

nach Gram-Schmidt/Lanczos die Jacobi-Matrix $J_{\beta,N}^{\mathrm{KMS}}$ mit Koeffizienten

$$a_{j,N}^{\mathrm{KMS}} = \langle q_{j,N},\,\mathcal{A}_N^-\,q_{j,N}\rangle, \qquad b_{j,N}^{\mathrm{KMS}} = \bigl|\mathcal{A}_N^-\,q_{j,N} - a_{j,N}^{\mathrm{KMS}}\,q_{j,N} - b_{j,N}^{\mathrm{KMS}}\,q_{j-1,N}\bigr|.$$

Die Koeffizienten sind **nicht frei wählbar**; sie folgen aus $\mathcal{A}_N^-$ und $\Omega_{\beta,N}$.

**P1 bestanden**, wenn $J_{\beta,N}^{\mathrm{KMS}} \sim A_N^{\mathrm{Jac},-}$ in einer präzisen Operator- oder Formtopologie.

**P1 gescheitert**, wenn $\Omega_N^{\mathrm{KMS}}$ existiert, aber keinen kanonischen Jacobi-Operator erzeugt.

Status: ?[O]

---

### 122.3 — P2: Kompatibilität mit Bombieri-Gewichten

Aus der KMS/GNS-Konstruktion entstehen Gewichte $w_{j,N}^{\mathrm{KMS}}$,
aus der Bombieri-Normalisierung (NEU-113/118) Gewichte $w_{j,N}^{\mathrm{Bomb}}$.

P2 darf **nicht** als punktweise Gleichheit formuliert werden. Die sinnvolle Bedingung ist **Form-Konvergenz**:

$$R_N^{-1}\,Q_N^{\mathrm{KMS}} \;\Rightarrow\; Q_N^{\mathrm{Bomb}},$$

d.h. für geeignete Testvektoren $f$:

$$\left| R_N^{-1}\,Q_N^{\mathrm{KMS}}(f) - Q_N^{\mathrm{Bomb}}(f)\right| \le \varepsilon_N\,\|f\|_{\mathcal{T}_N}^2, \qquad \varepsilon_N \to 0.$$

P2 ist der eigentliche Hauptengpass von NEU-122. ⚠[M]

Status: ?[O]

---

### 122.4 — P3: Renormierungsskala

Bei Dirichlet-Cutoff $n \le N$:

$$R_N = Z_{1,N}^{-1} = \frac{1}{\log N + \gamma_E + o(1)}
\sim \frac{1}{\log N}\left(1 - \frac{\gamma_E}{\log N} + o((\log N)^{-1})\right).$$

Bei Euler-Produktcutoff $p \le N$:

$$Z_N^{\mathrm{Euler}} = \prod_{p \le N}(1-p^{-1})^{-1} \sim e^{\gamma_E}\log N,$$

was eine andere Konstantenskala liefert.

**Fixierung erforderlich:**

$$\boxed{\text{Dirichlet-Cutoff } n \le N \quad\text{oder}\quad \text{Euler-Cutoff } p \le N.}$$

Für den bisherigen Momenttest passt der Dirichlet-Cutoff, weil er direkt $R_N \sim 1/\log N$ liefert.

- Dirichlet-Cutoff: ✓[M]
- Cutoff-Wechsel: ⚠[M]

---

### 122.5 — Der eigentliche KMS-Momenttest

Nach 122.1 lautet der nicht-leere Momenttest **nicht mehr**

$$R_N\,a_1 \to C_\xi \quad\text{(leer: K1/K3-Mechanismus)},$$

sondern

$$\varphi_{1,N}(\mathcal{A}_N^-) \;=\; R_N\,\tau_{1,N}(\mathcal{A}_N^-) \;\longrightarrow\; C_\xi.$$

Das ist nicht leer, weil $\tau_{1,N}$ durch die KMS-Gewichtung $n^{-1}$ festgelegt ist
und $\mathcal{A}_N^-$ nicht nachträglich angepasst werden darf.

Status: ?[O]

---

### 122.6 — Entscheidungskriterium für Spur A

Spur A bleibt aktiv genau dann, wenn alle drei Bedingungen erfüllt sind:

$$\boxed{P1 + P2 + P3 \;\Longrightarrow\; \text{Spur A bleibt aktiv.}}$$

- P1 bestanden $\Rightarrow$ $\Omega_N^{\mathrm{KMS}}$ erzeugt kanonisch den Jacobi-Formalismus.
- P2 bestanden $\Rightarrow$ $R_N^{-1}Q_N^{\mathrm{KMS}} \Rightarrow Q_N^{\mathrm{Bomb}}$.
- P3 gesichert $\Rightarrow$ $R_N \sim 1/\log N$ unter Dirichlet-Cutoff.

Dann ist K2 der erste echte Kandidat für $m_{\Omega,N} \to m_{\mathrm{arith}}$.

$$\boxed{\neg P1\;\text{oder}\;\neg P2 \;\Longrightarrow\; \text{Wechsel zur Spektralspur 122.S.}}$$

| Bedingung | Status |
|-----------|--------|
| P3 | ✓[M] (Dirichlet-Cutoff) |
| P1 | ?[O] |
| P2 | ?[O] (Hauptengpass) |
| Spur-A-Entscheidung | ?[O] |

---

## Teil B — Weiche Route: vektorunabhängige Spektralnäherung

Falls P1 oder P2 scheitert.

### 122.S.1 — Warum Spektralnäherung logisch schwächer ist

$A_N^{\mathrm{Jac},-}$ ist selbstadjungiert, also $\sigma(A_N^{\mathrm{Jac},-}) \subset \mathbb{R}$.
Die Menge $\{\mathrm{Im}\,\rho\}$ ist ebenfalls reell, **unabhängig davon, ob RH gilt**.

Damit testet die Spektralspur nur die *Ordinaten* der Nullstellen, nicht ihre Realteile.

$$\sigma(A_N^{\mathrm{Jac},-}) \to \{\mathrm{Im}\,\rho\} \quad\text{impliziert allein nicht RH.}$$

Sie kann RH-relevant werden nur wenn zusätzlich eine Herglotz-, Weil- oder $m_{\mathrm{arith}}$-Rückbindung hergestellt wird. ✓[M]

---

### 122.S.2 — Zählfunktionstest

Definiere:

$$N_A^{(N)}(T) = \#\{\lambda \in \sigma(A_N^{\mathrm{Jac},-}) : |\lambda| \le T\}, \qquad N_\zeta(T) = \#\{\rho : 0 < \mathrm{Im}\,\rho \le T\}.$$

Erster weicher Test für ein Fenster $T_N \to \infty$:

$$N_A^{(N)}(T_N) \sim 2\,N_\zeta(T_N).$$

(Faktor 2: symmetrische positive und negative Ordinaten.) Status: ?[O]

---

### 122.S.3 — Lokaler Spektraltest

Ordne $0 < \lambda_{1,N} \le \lambda_{2,N} \le \cdots$ und $0 < \gamma_1 \le \gamma_2 \le \cdots$.

Prüfbare Tests in aufsteigender Stärke:

| Test | Formulierung | Status |
|------|-------------|--------|
| Gemittelt | $\frac{1}{J_N}\sum_{j \le J_N}|\lambda_{j,N} - \gamma_j|^2 \to 0$ | ?[O] |
| Entfaltet | Vergleich lokaler Abstände nach Entfaltung | ?[O] |
| Stark | $|\lambda_{j,N} - \gamma_j| \to 0$ für jedes feste $j$ | ?[O] |

---

### 122.S.4 — Spektralspur als Diagnose, nicht Beweis

Die Spektralspur zeigt: $A_N^{\mathrm{Jac},-}$ trägt die richtige Nullstellengeometrie.
Sie zeigt **nicht** automatisch: $m_{\mathrm{arith}}$ ist Herglotz.
Sie ist diagnostisch wertvoll, logisch aber schwächer als Spur A. ✓[M]

---

## 122.F — Gesamtfazit

NEU-121 hat K1 und K3 logisch entleert:

- K1: $M_1 = a_1$ (freier Diagonaleintrag, kein Hadamard-Bezug) ✗[M]
- K3: $M_1 = \kappa_N\,a_1$ (identisch leer) ✗[M]

Einziger verbliebener Vektorkandidat: **K2 = $\Omega_N^{\mathrm{KMS}}$**.

Ab NEU-122 darf kein frei wählbarer Vektor mehr getestet werden.
Der Vektor muss aus der KMS/GNS-Konstruktion selbst kommen.

NEU-122 reduziert K2 auf drei Eintrittsbedingungen:

$$P1:\quad \Omega_N^{\mathrm{KMS}} \text{ erzeugt kanonisch den Jacobi-Formalismus (Krylov/Lanczos).}$$

$$P2:\quad R_N^{-1}\,Q_N^{\mathrm{KMS}} \Rightarrow Q_N^{\mathrm{Bomb}} \quad\text{(Form-Konvergenz, Hauptengpass).}$$

$$P3:\quad R_N \sim 1/\log N \quad\text{(gesichert unter Dirichlet-Cutoff).}$$

Entscheidungssatz:

$$\boxed{P1 + P2 + P3 \;\Longrightarrow\; \text{Spur A aktiv.}} \qquad \boxed{\neg P1\;\text{oder}\;\neg P2 \;\Longrightarrow\; \text{Spektralspur 122.S.}}$$

---

## 122.N — Nächste Aufgabe: NEU-123

Die nächste Einheit greift **nicht** sofort $m_{\Omega,N}^{\mathrm{KMS}} \to m_{\mathrm{arith}}$ an.

**Zuerst muss gezeigt oder widerlegt werden:**

$$\boxed{A_N^{\mathrm{Jac},-} = \mathrm{Lanczos}_{\Omega_N^{\mathrm{KMS}}}(\mathcal{A}_N^-)}$$

für ein kanonisches, **vorab fixiertes** GNS-Element $\mathcal{A}_N^-$.

Das ist der präzise P1-Test.

Danach ist der Momenttest $\varphi_{1,N}(\mathcal{A}_N^-) \to C_\xi$ inhaltlich zulässig.

**NEU-123 — Jacobi-Grenzoperator und starke Resolventenkonvergenz**

Ziel:

$$A_N^{\mathrm{Jac},-} \;\xrightarrow{\mathrm{s.r.}}\; A_\infty$$

auf einem gemeinsamen Hilbertraum $\mathcal{H}_N \simeq \mathbb{C}^{d_N} \hookrightarrow \ell^2(\mathbb{N}_0)$,
kanonisch via Jacobi-Trunkierung mit Nullrand.

Drei-Stufen-Programm:

| Stufe | Aussage | Status |
|-------|---------|--------|
| 1 | $a_{j,N} \to a_j,\; b_{j,N} \to b_j$ für jedes feste $j$ (Koeffizientenkonvergenz) | ?[O] |
| 2 | $A_\infty$ wesentlich selbstadjungiert (z.B. via Carleman-Bedingung $\sum 1/b_j = \infty$) $\Rightarrow$ starke Resolventenkonvergenz | ?[O] |
| 3 | $\sigma(A_\infty) \stackrel{?}{=} \{\gamma_k\}$ und $\mu_{\Omega_\infty}^{A_\infty} \stackrel{?}{=} \mu_\xi$ | ?[O] |

NEU-123 ist das gemeinsame Fundament für Weg (a) (Weyl-Funktion) und Weg (b) (Spektrum von $A_\infty$).

---

## Querverweise

- NEU-60: Core-Konvergenz, Resolventenstabilität ✓[M]
- NEU-112: Stieltjes-Nullstellenmaß ✓[M]
- NEU-113/118: Bombieri-Normalisierung ✓[M]
- NEU-119: $m_{\Omega,N}$ als Spektralmaß-Objekt ✓[M]
- NEU-120: Bombieri-Herglotz-Grenzübergang, WARNSATZ ⚠[M]
- NEU-121: Negativbefund K1/K3 ✗[M]; K2 offen ?[O]
- Spur B: NEU-114, NEU-116 ?[O]

---

*Katalog: rh-fragenkatalog | Einheit: NEU-122 | Revision: 2026-07-04*
