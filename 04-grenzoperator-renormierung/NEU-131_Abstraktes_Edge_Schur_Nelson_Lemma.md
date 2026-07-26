# NEU-131 — Abstraktes Edge-Schur-Nelson-Lemma

> Stand: Juli 2026. Technische Auflösung von NEU-130 Leitfrage 4:
> Ist B-strong eine Instanz derselben Schur-/Nelson-Kontrolle wie NEU-54/55?
> Basiert auf Paper VII (`paper7_skeleton.tex`), Assumption 3.1 (B-strong).

---

## Ergebnis: B-strong ist eine **Zeilennorm-Schranke**, nicht eine summierte Schalenenergie

Die exakte Definition aus Paper VII, Assumption 3.1:

$$P_{kl} := c\cdot \frac{|\lambda_l^{(c)}-\lambda_k^{(c)}|}{(1-\lambda_k^{(c)})(1-\lambda_l^{(c)})} \leq C_2\,c^{1/2}.$$

Das ist ein **einzelner Blockeintrag** — eine punktweise Schranke für jedes Paar $(k,l)$.

Aber: Der Übergang zur Zeilennorm läuft explizit über Remark 2.2 (Scaling):

$$\|D\mathcal{T}_c^{(N)}\|_{\ell^\infty \to \ell^\infty}
\leq \sup_i \sum_{j\neq i}|P_{ij}|
\leq C\,c^{-1/2}\log c.$$

Der kritische Schritt ist also:

$$P_{kl} \leq C_2 c^{1/2} \;\Rightarrow\; \sup_i\sum_{j\neq i}|P_{ij}| \leq C\,c^{-1/2}\log c.$$

Dieser Schritt geht **nicht punktweise**, sondern über dyadische Kancellation
(Theorem 2.1, Abel-Summation über Blöcke). Erst die Kombination von
punktweiser Schranke + Kancellation ergibt die summierte Kontrolle.

---

## Die genaue Struktur: Quelle, Zielschale, kontrollierte Energie

| Größe | PSWF (B-strong + Kancellation) | Nelson/Schur (NEU-54/55) |
|---|---|---|
| **Quelle** $\alpha$ | Index $i$ (Zeile) | Index $a$ (Kanal) |
| **Zielschale** | Dyadischer Block $\mathcal{B}_m(i)$ | Alle Zielindizes $b$ |
| **Kopplung** | $P_{ij} \cdot c^{1/2} = A_{ij}$ (normiert) | $\Theta_{ba}$ |
| **Punktschranke** | $A_{ij} \leq C_2$ (H3, $\equiv$ B-strong nach Normierung) | — |
| **Summierte Energie** | $\sup_i \sum_j \|A_{ij}\|^2 \leq C^2 c^{-1}(\log c)^2$ | $\sum_b|\Theta_{ba}|^2 \leq C^2\ell(a)^2$ |
| **Intrinsische Skala** | $\Lambda \sim c^{-1/2}\log c$ (nach Kancellation) | $\Lambda = \ell(a)$ |

**Schlüsselbeobachtung:** B-strong allein ist *nicht* die Nelson-Bedingung.
Nelson ist die summierte Kontrolle — die im PSWF-Fall erst durch Theorem 2.1
(Dyadische Kancellation) aus B-strong gefolgert wird.

---

## Die präzise Äquivalenzaussage

Nach Renormierung $A_{ij} := P_{ij} \cdot c^{1/2}$ ist die Struktur:

$$\underbrace{A_{ij} \leq C_2}_{\text{H3 = B-strong normiert}}
+ \underbrace{\text{Dyadische Kancellation (Thm 2.1)}}_{\text{Phasen- + Regularitätsbedingung}}
\Rightarrow
\underbrace{\sup_i\sum_j|A_{ij}| \leq C\cdot \log N}_{\text{Nelson-artige Zeilennorm-Kontrolle}}.$$

Das abstrakte Muster ist:

$$\boxed{\text{Punktweise Amplitudensperre} + \text{Kancellationsstruktur} \Rightarrow \text{summierte Schalenenergie kontrolliert}.}$$

Für Nelson ist die Kancellationsstruktur eine **Kommutatorbedingung**.
Für PSWF ist sie eine **Phasenbedingung** (H1 + H2, dyadische Abel-Summation).

---

## Das abstrakte Edge-Schur-Nelson-Lemma (Formulierung)

**Sei** $\mathcal{H} = \bigoplus_{\alpha \in I} \mathcal{H}_\alpha$ eine Schalen-/Kanalzerlegung,
$L$ ein positiver Skalenoperator mit $L|_{\mathcal{H}_\alpha} \sim \Lambda(\alpha)$,
und $\Theta = (\Theta_{\beta\alpha})$ ein Kopplungsoperator.

**Annahmen:**
1. **(Punktschranke)** $\|\Theta_{\beta\alpha}\|_{\mathrm{op}} \leq C \cdot f(\alpha,\beta)$ für eine geeignete Gewichtsfunktion $f$.
2. **(Kancellationsstruktur)** Für festes $\alpha$: die Folge $\beta \mapsto \Theta_{\beta\alpha}$ hat eine nicht-degenerierte Oszillations-/Kommutatoreigenschaft.

**Schluss:**
$$\sum_\beta \|\Theta_{\beta\alpha}\|^2 \leq C^2 \Lambda(\alpha)^2,
\qquad \|\Theta u\| \lesssim \|Lu\|.$$

| Instanz | Punktschranke | Kancellationsstruktur | Ergebnis $\Lambda(\alpha)$ |
|---|---|---|---|
| PSWF | B-strong: $A_{ij} \leq C_2$ | H1 (Phase) + H2 (Amplitudenregularität) | $c^{-1/2}\log c$ |
| Nelson/NEU-54/55 | $|\Theta_{ba}| \leq C\ell(a)/N$ | Kommutator-/Schur-Bedingung | $\ell(a)$ |

---

## Statusdiagnose

$$\boxed{B\text{-strong} \sim \text{Nelson/Schur} \quad \checkmark[M]\text{ als Strukturdiagnose}, \quad ?[O]\text{ als formales Brückenlemma}.}$$

- **[M] bestätigt:** Beide sind Instanzen von *Punktschranke + Kancellationsstruktur → summierte Energie*.
- **[O] offen:** Der gemeinsame abstrakte Satz erfordert eine einheitliche Kancellationsaxiomatik, die H1/H2 (Phase/Regularität) und Nelson-Kommutator als zwei Spezialfälle erfasst.

---

## Wichtige Warnung: B-strong ist noch nicht bewiesen

Aus Paper VII, Section 4 (Open Problems):
- **(O1)** `ass:gap`: $\lambda_l - \lambda_{l+1} \geq \kappa_0 c^{-1/3}$ — nächstes strukturelles Ziel.
- **(O2)** B-strong selbst: hängt von `ass:gap` + Airy-Amplitudenkontrolle ab.
- **(O3)** Amplitudenregularität H2: Paper VIII.

Das heißt: Die Zeilennorm-Kontrolle $\sup_i\sum_j|P_{ij}| \leq Cc^{-1/2}\log c$ ist
**noch bedingt** auf B-strong. Die Brücke zu Nelson ist real, aber das Fundament
steht noch auf offenen Annahmen.

---

## Konsequenz für die Gesamtstrategie

Der richtige Satz, den das abstrakte Lemma liefern würde:

$$\boxed{\text{Nicht punktweise Kleinheit rettet die kritische Schicht, sondern Punktschranke + Kancellation = summierte Energiekontrolle.}}$$

Das ist die Sprache, in der NEU-129 (Prä-Lanczos-Metrik) und das PSWF-Programm
strukturell verbunden sind — sobald die Kancellationsstruktur von $H_{\mathrm{rel},N}$ identifiziert ist.

---

## Verweise

- NEU-130: PSWF-Brücke (Überblick)
- NEU-54/55: Nelson-/Schur-Kontrollbedingungen
- `paper7_skeleton.tex`: Assumption 3.1 (B-strong), Remark 2.2 (Skalierung), Theorem 2.1 (Dyadische Kancellation)
- `paper8_scale_separated.tex`: H2-Amplitudenregularität (Paper VIII)
