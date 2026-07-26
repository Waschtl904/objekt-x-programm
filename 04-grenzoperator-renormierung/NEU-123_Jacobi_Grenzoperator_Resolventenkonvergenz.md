# NEU-123 — Jacobi-Grenzoperator und starke Resolventenkonvergenz

**Datum:** 4. Juli 2026
**Anschluss:** NEU-60, NEU-77–87, NEU-119–122
**Status:** ?[O] — reines Operator-Fundament, keine RH-Behauptung

---

## 123.0 — Leitwarnung

Die Aussage

$$\sigma(A_N^{\mathrm{Jac},-}) \to \{\operatorname{Im}\rho\}$$

ist ohne gemeinsame Operator-Topologie nicht wohldefiniert.

Vor jeder Spektralaussage muss geklärt werden:
Konvergieren die $A_N^{\mathrm{Jac},-}$ als Operatoren?

Die erste Aufgabe ist daher **nicht** der Vergleich mit Zeta-Nullstellen,
sondern die Konstruktion eines Grenzoperators $A_\infty$ auf einem gemeinsamen Hilbertraum.

✓[M]

---

## 123.1 — Gemeinsamer Hilbertraum

Alle endlichen Jacobi-Operatoren werden auf

$$\ell^2(\mathbb{N}_0) = \overline{\operatorname{span}\{e_0, e_1, e_2, \ldots\}}$$

verglichen. Sei $d_N = \dim \mathcal{H}_N$. Die kanonische Einbettung ist

$$\mathcal{H}_N \simeq \operatorname{span}\{e_0, \ldots, e_{d_N-1}\} \subset \ell^2(\mathbb{N}_0).$$

Der Jacobi-Operator $A_N^{\mathrm{Jac},-}$ wirkt durch

$$A_N^{\mathrm{Jac},-}\,e_j = b_{j,N}\,e_{j+1} + a_{j,N}\,e_j + b_{j-1,N}\,e_{j-1}$$

für die inneren Indizes $0 < j < d_N - 1$, mit Randbedingungen

$$b_{-1,N} = 0, \qquad b_{d_N-1,N} = 0$$

(Nullrand). Damit liegt $A_N^{\mathrm{Jac},-}$ als endlicher selbstadjungierter Jacobi-Block in $\ell^2(\mathbb{N}_0)$.

✓[M] als Vergleichsrahmen

---

## 123.2 — Koeffizientenkonvergenz als erster Kern

Die grundlegende Bedingung:

Für jedes feste $j \ge 0$ existieren Grenzwerte

$$a_j = \lim_{N\to\infty} a_{j,N} \in \mathbb{R}, \qquad b_j = \lim_{N\to\infty} b_{j,N} > 0.$$

Der formale Grenzoperator wirkt dann auf $\mathcal{D}_0 = c_{00}(\mathbb{N}_0)$ durch

$$A_\infty^{\min}\,e_j = b_j\,e_{j+1} + a_j\,e_j + b_{j-1}\,e_{j-1}.$$

Damit entsteht ein symmetrischer Jacobi-Operator $A_\infty^{\min}$ auf dem Raum
$\mathcal{D}_0$ endlich unterstützter Folgen.

Status: ?[O] für die konkreten Koeffizienten aus NEU-77–87

---

## 123.3 — Wesentliche Selbstadjungiertheit (Carleman-Bedingung)

Damit $A_\infty^{\min}$ einen eindeutigen selbstadjungierten Abschluss $A_\infty$ besitzt,
genügt die **Carleman-Bedingung**:

$$\sum_{j=0}^{\infty} \frac{1}{b_j} = \infty.$$

Falls diese gilt: $A_\infty^{\min}$ ist wesentlich selbstadjungiert;
der Abschluss wird mit $A_\infty$ bezeichnet.

Falls Carleman scheitert: $A_\infty^{\min}$ hat möglicherweise eine
ein-parametrische Familie selbstadjungierter Erweiterungen.
Die Spektraltheorie hängt dann von einer Randbedingung im Unendlichen ab,
und Weg (b) verliert seine kanonische Form.

Status: ?[O]

---

## 123.4 — Starke Resolventenkonvergenz

Unter den Bedingungen von 123.2 und 123.3 gilt das folgende Konvergenzlemma:

**Lemma (Kern von NEU-123):**

*Wenn $a_{j,N} \to a_j$, $b_{j,N} \to b_j > 0$ für jedes feste $j$,
und $A_\infty^{\min}$ ist wesentlich selbstadjungiert, dann*

$$A_N^{\mathrm{Jac},-} \;\xrightarrow{\mathrm{s.r.}}\; A_\infty.$$

Das bedeutet: Für jedes $z \in \mathbb{C} \setminus \mathbb{R}$ und jedes $f \in \ell^2(\mathbb{N}_0)$:

$$(A_N^{\mathrm{Jac},-} - z)^{-1}f \;\longrightarrow\; (A_\infty - z)^{-1}f.$$

Diese Aussage ist der präzise Operatorersatz für die informelle Konvergenz
$A_N^{\mathrm{Jac},-} \to A_\infty$.

**Referenzrahmen:** Das Lemma folgt aus dem allgemeinen Satz über Jacobi-Trunkierungen
(vgl. Akhiezer, *The Classical Moment Problem*; Simon, *Spectral Theory and Orthogonal Polynomials*).
Der Schritt von Koeffizientenkonvergenz zur starken Resolventenkonvergenz
nach Carleman ist klassisch.

Status: ?[O] für die Anwendung auf den konkreten Operator aus NEU-77–87

---

## 123.5 — Konsequenz für Weyl-Funktionen

Sei $\Omega_N \to \Omega_\infty$ in $\ell^2(\mathbb{N}_0)$. Dann folgt
aus starker Resolventenkonvergenz:

$$\langle \Omega_N, (A_N^{\mathrm{Jac},-} - z)^{-1} \Omega_N\rangle
\;\longrightarrow\;
\langle \Omega_\infty, (A_\infty - z)^{-1} \Omega_\infty\rangle,
\qquad z \in \mathbb{C} \setminus \mathbb{R}.$$

Also:

$$m_{\Omega,N}(z) \;\longrightarrow\; m_{\Omega,\infty}(z).$$

Das ist der saubere Anschluss an NEU-119 (Spektralmaß-Definition) und NEU-120 (Herglotz-Grenzübergang).

**Aber:** $m_{\Omega,\infty} = m_{\mathrm{arith}}$ folgt daraus noch nicht.
Dafür braucht man zusätzlich:

$$\mu_{\Omega_\infty}^{A_\infty} \;\stackrel{?}{=}\; \mu_\xi.$$

- Logische Struktur: ✓[M]
- Identifikation mit $\mu_\xi$: ?[O]

---

## 123.6 — Konsequenz für Spektralnäherung

Starke Resolventenkonvergenz liefert **nicht automatisch** punktweise Eigenwertkonvergenz.

Für eine kontrollierte Spektralaussage braucht man zusätzlich:

1. $A_\infty$ hat reines Punktspektrum.
2. Die Eigenwerte sind einfach.
3. $A_N^{\mathrm{Jac},-}$ approximiert die Eigenprojektionen von $A_\infty$.
4. Es geht keine Spektralmasse im Limes verloren.

Erst dann ist die Frage

$$\sigma_p(A_\infty) \;\stackrel{?}{=}\; \{\operatorname{Im}\rho : \xi(\rho) = 0\}$$

sinnvoll formulierbar.

Ohne diese Zusatzbedingungen ist die Spektralspur logisch schwächer als Spur A. ✓[M]

Status: ?[O] für das Programm

---

## 123.7 — Spektralmaß statt bloßes Spektrum

Für den RH-Pfad genügt **nicht**

$$\sigma(A_\infty) \stackrel{?}{=} \{\gamma_k\}.$$

Benötigt wird stärker:

$$\mu_{\Omega_\infty}^{A_\infty} = \sum_\gamma c_\gamma\,\delta_\gamma$$

mit den richtigen Hadamard/Bombieri-Gewichten $c_\gamma$. Denn die Weyl-Funktion ist

$$m_{\Omega_\infty}(z) = \int_{\mathbb{R}} \frac{d\mu_{\Omega_\infty}^{A_\infty}(t)}{t - z}.$$

Zwei Spektralmaße können denselben Träger besitzen, aber verschiedene Weyl-Funktionen erzeugen.

Die eigentliche Zielaussage ist:

$$\mu_{\Omega_\infty}^{A_\infty} = \mu_\xi, \qquad \text{nicht nur } \sigma(A_\infty) \ni \{\gamma_k\}.$$

✓[M]

---

## 123.8 — Einbettung in die Gesamtstruktur (Drei-Stufen-Programm)

| Stufe | Aussage | Anschluss |
|-------|---------|----------|
| **1** | $a_{j,N} \to a_j$, $b_{j,N} \to b_j$ für jedes feste $j$ | NEU-77–87, konkrete Rechnung |
| **2** | Carleman-Bedingung $\sum 1/b_j = \infty$ $\Rightarrow$ $A_\infty^{\min}$ wesentl. s.a. $\Rightarrow$ starke Resolventenkonvergenz | 123.3/4 |
| **3** | $\sigma(A_\infty) \stackrel{?}{=} \{\gamma_k\}$ und $\mu_{\Omega_\infty}^{A_\infty} \stackrel{?}{=} \mu_\xi$ | NEU-124 |

NEU-123 behandelt ausschließlich Stufe 1 und 2.
Stufe 3 ist NEU-124 vorbehalten.

---

## 123.F — Fazit

NEU-123 ist ein **reines Operator-Fundament**. Es enthält keine RH-Behauptung.

Zentraler Prüfsatz:

$$\boxed{a_{j,N} \to a_j,\quad b_{j,N} \to b_j > 0 \;(\forall\,\text{festes }j),\quad \sum_j \frac{1}{b_j} = \infty
\;\Longrightarrow\; A_N^{\mathrm{Jac},-} \xrightarrow{\mathrm{s.r.}} A_\infty.}$$

Drei Engpunkte:

| Bedingung | Status |
|-----------|---------|
| K1: $a_{j,N} \to a_j$, $b_{j,N} \to b_j$ | ?[O] für konkreten Operator |
| K2: Carleman $\sum 1/b_j = \infty$ | ?[O] |
| K3: starke Resolventenkonvergenz | ?[O] (folgt aus K1+K2) |

Erst danach (NEU-124):

$$\sigma(A_\infty) \stackrel{?}{=} \{\operatorname{Im}\rho\}, \qquad
\mu_{\Omega_\infty}^{A_\infty} \stackrel{?}{=} \mu_\xi.$$

---

## 123.N — Nächste Aufgabe

Die nächste konkrete Rechenaufgabe:

$$\boxed{\text{Extrahiere aus } A_N^{\mathrm{Jac},-} \text{ die Koeffizienten } a_{j,N},\, b_{j,N} \text{ aus NEU-77–87.}}$$

Dann prüfe für kleine feste $j = 0, 1, 2, \ldots$:

$$a_{j,N} \xrightarrow{N\to\infty} a_j, \qquad b_{j,N} \xrightarrow{N\to\infty} b_j.$$

Erst wenn diese Stabilisierung sichtbar ist, lohnt der Vergleich mit Zeta-Ordinaten.

Der numerische KMS-Test (122.C, $N = 5, 10, 20$) kann parallel als
Diagnose laufen, entscheidet aber nicht über Spur A oder B.

---

## Querverweise

- NEU-60: Core-Konvergenz, Resolventenstabilität ✓[M]
- NEU-77–87: Feshbach-Kollaps $\to$ $A_N^{\mathrm{Jac},-}$ ✓[M]
- NEU-119: $m_{\Omega,N}$ als Spektralmaß-Objekt ✓[M]
- NEU-120: WARNSATZ, Herglotz-Grenzübergang ⚠[M]
- NEU-121: Negativbefund K1/K3 ✗[M]; K2 offen ?[O]
- NEU-122: Eintrittstest P1/P2/P3, Anti-Fitting-Axiom ?[O]
- NEU-124: Spektrum und Spektralmaß von $A_\infty$ (geplant)

---

*Katalog: rh-fragenkatalog | Einheit: NEU-123 | Erstellt: 2026-07-04*
