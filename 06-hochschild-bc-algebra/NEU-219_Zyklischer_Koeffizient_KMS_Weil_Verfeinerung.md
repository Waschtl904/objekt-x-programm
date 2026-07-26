# NEU-219 — Zyklischer Koeffiziententyp und Weil-/KMS-Verfeinerung der geladenen Cup-Klasse

**DAG-Position:** Direkter Nachfolger von NEU-218 (Commit 9e1dd12).  
**Voraussetzung:** $[D_g] \smile [\Theta^\wedge_{p_1,p_2,p_3}] \neq 0 \in HH^4(A_{\mathrm{alg}}, \mathfrak{M}^{\log}_{\mathrm{glob}})_g$ — vollständig bewiesen.  
**Status gesamt:** Audit-Knoten; Einzelknoten teils ?[O].

---

## Korrektur zu NEU-218: Wachstumsaussage

In NEU-218 wurde das Wachstum von $\mathcal{F}_N(G_q)(x_N)$ unpräzise als „Superpolynomial“ bezeichnet. Die korrekte Aussage ist:

Bewiesen ist
$$
\mathcal{F}_N(G_q)(x_N) \ge N^3\bigl(c_{J_N} - c_{K_N}\bigr),
$$
mit $c_{J_N} - c_{K_N} \to \infty$, also
$$
N^{-3}\|\mathcal{F}_N(G_q)\|_\infty \longrightarrow \infty.
$$

Mit der bekannten Abschätzung $v_q((J+1)!) \sim J/(q-1)$ ergibt sich $J_N \asymp N$, $K_N = O(\log N)$, und damit
$$
\mathcal{F}_N(G_q)(x_N) \gtrsim N^3 \log N.
$$

Das Wachstum ist **superkubisch**, aber nicht superpolynomial. Für den Widerspruchsbeweis genügt dies vollständig, da die Koinvariantenschranke nur $O(N^3)$ erlaubt.

---

## Typbefund: Koeffizientenmodul

$M = \mathfrak{M}^{\log}_{\mathrm{glob}}$ ist zunächst nur ein $A_{\mathrm{alg}}$-Bimodul. Für einen allgemeinen Bimodul existiert **keine** kanonische zyklische Struktur und kein unmittelbar anwendbarer Connes-$B$-Operator auf den $M$-wertigen Hochschildkochains. Die Frage, ob $[L^{\mathrm{cup}}_{g;\mathbf{p}}]$ eine zyklische oder getwistete zyklische Verfeinerung besitzt, ist daher eigenständig.

Strategische Reihenfolge:
$$
\boxed{
HH^4\text{-Klasse} \;\longrightarrow\; \text{globaler zyklischer Koeffizient} \;\longrightarrow\; \text{KMS-/Weil-Paarung} \;\longrightarrow\; \text{Operatorrealisierung}.
}
$$

---

## [O-219-0] — Direktaudit: Anwendbare zyklische Koeffiziententheorie

**Status:** ?[O] — Klassifikationsknoten

Zu entscheiden: Welche zyklische Koeffiziententheorie ist auf $M$ anwendbar?

- **(A) Gewöhnlich zyklisch:** Es existiert $\tau_M: M \to \mathbb{C}$ mit globaler Tracialität
$$
\boxed{\tau_M(am) = \tau_M(ma) \quad \forall a \in A_{\mathrm{alg}},\ m \in M.} \tag{T}
$$
Dann faktorisiert $\tau_M$ über $M/[A_{\mathrm{alg}}, M]$, und die skalare Form
$$
\Phi_{g;\mathbf{p}}(a_0, \ldots, a_4) := \tau_M\!\left(a_0 L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1, \ldots, a_4)\right)
$$
wird ein Kandidat für einen periodisch-zyklischen Kozykel.

- **(B) KMS/twisted-cyclic:** Kein global traciales Funktional erfüllt (NV). Dann muss ein Twistautomorphismus $\sigma_{i\beta}$ konstruiert werden mit
$$
\tau_\beta(am) = \tau_\beta\!\left(m\,\sigma_{i\beta}(a)\right).
$$
Dies erfordert einen eigenen Typwechsel: getwisteter Rand, getwistete Zyklizität, Paarung mit $L^{\mathrm{cup}}$. Eine gewöhnliche KMS-Identität darf **nicht** ohne diesen Typwechsel als zyklischer Beweis verwendet werden.

Die Entscheidung (A) vs. (B) hängt direkt von [O-219-1] ab.

---

## [O-219-1] — Voller Kommutatorquotient

**Status:** ?[O] — primär

$$
\boxed{[O\text{-}219\text{-}1]: \quad \overline{D_g(\mu_q)\mu_P} \neq 0 \text{ in } M/[A_{\mathrm{alg}}, M] \quad ?[O].}
$$

Hierzu ist zu entscheiden, ob $D_g(\mu_q)\mu_P \notin [A_{\mathrm{alg}}, M]$.

In Normalform (aus NEU-218, (7.1)):
$$
D_g(\mu_q)\mu_P = \mu_{mqP}\,\sigma_P(G_q)\,\mu_n^*.
$$

**Bekannt aus NEU-218:** $D_g(\mu_q)\mu_P \notin C_{H;R}$ (partieller Quotient ✓[K/M]).  
**Offen:** Ob $[A_{\mathrm{alg}}, M]$ größer als $C_{H;R}$ ist und das Element absorbiert.

Relevanz: Ein positiver Befund liefert ein global zentrales duales Funktional und ermöglicht Pfad (A).

---

## [O-219-2] — Globales traciales Funktional und skalare Hochschildform

**Status:** ?[O] (bedingt durch [O-219-1])

Voraussetzung: $[O\text{-}219\text{-}1]$ positiv. Dann existiert
$$
\tau_M: M/[A_{\mathrm{alg}}, M] \longrightarrow \mathbb{C}
$$
mit
$$
\tau_M\!\left(D_g(\mu_q)\mu_P\right) \neq 0. \tag{NV}
$$

Zu konstruieren ist die skalare Hochschildform:
$$
\boxed{
\Phi_{g;\mathbf{p}}(a_0, \ldots, a_4)
:= \tau_M\!\left(a_0\, L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1, \ldots, a_4)\right).
}
$$

Zu prüfen: $\Phi_{g;\mathbf{p}} \in Z^5(A_{\mathrm{alg}}, \mathbb{C})$ (Hochschildgeschlossenheit der skalierten Form).

---

## [O-219-3] — Zyklizitätstest

**Status:** ?[O] (bedingt durch [O-219-2])

Zu entscheiden:
$$
\boxed{(1-\lambda)\Phi_{g;\mathbf{p}} = 0 \quad \text{oder} \quad \text{exakter Zyklizitätsdefekt.}}
$$

Hier ist $\lambda$ der Zyklizitätsoperator $(\lambda f)(a_0, \ldots, a_n) = (-1)^n f(a_n, a_0, \ldots, a_{n-1})$.

Falls $(1-\lambda)\Phi \neq 0$ aber exakt (d.h. im Bild von $b$ auf Hochschildkochains): zyklischer Normierungsdefekt, reparierbar durch Korrekturterm.  
Falls $(1-\lambda)\Phi = 0$: $\Phi$ ist direkt ein zyklischer Kozykel.

---

## [O-219-4] — Connes-$B$-Operator

**Status:** ?[O] (bedingt durch [O-219-3])

$$
\boxed{B\Phi_{g;\mathbf{p}} = 0 \quad \text{beziehungsweise negative Entscheidung.}}
$$

Falls $b\Phi = 0$ und $B\Phi = 0$: $\Phi$ definiert eine periodisch-zyklische Klasse in $HP^*(A_{\mathrm{alg}})^\vee$.  
Falls $B\Phi \neq 0$: Analyse des Defekts $B\Phi$ als eigenständiger Kozykel höherer Ordnung.

---

## [O-219-5] — KMS-/twisted-cyclic Ersatzpfad

**Status:** ?[O]\_sekundar (aktiviert falls [O-219-1] negativ oder [O-219-3] scheitert)

Zu konstruieren:
1. **Twistautomorphismus** $\sigma_{i\beta} \in \mathrm{Aut}(A_{\mathrm{alg}})$ aus der KMS-Dynamik
2. **Getwisteter Hochschildrand** $b_\sigma$ mit $b_\sigma^2 = 0$
3. **Getwistete Zyklizität** $(1-\lambda_\sigma)\Phi_\beta = 0$
4. **Paarung** $\langle L^{\mathrm{cup}}_{g;\mathbf{p}},\ z_{\varphi,\sigma}\rangle \neq 0$

Eine gewöhnliche KMS-Identität darf **nicht ohne diesen Typwechsel** als zyklischer Beweis verwendet werden.

---

## [O-219-6] — Weil-, Primzahlpotenz- und Gammafaktorpaarung

**Status:** ?[O]\_sekundar

Nach Entscheidung des zyklischen Koeffiziententyps:
- Weil-Distributions-Paarung $W(\Phi_{g;\mathbf{p}})$
- Primzahlpotenz-Kopplung via $\sigma_P$-Spektrum
- Gammafaktor-Paarung (archimedischer Beitrag)

Diese Knoten sind erst nach [O-219-3] oder [O-219-5] sinnvoll angehbar.

---

## DAG-Struktur NEU-219

```
NEU-218: [L^cup] != 0 in HH^4(A,M)_g                             [K/M]
      |
 [O-219-0]  Direktaudit zyklischer Koeffiziententyp (A) vs (B)   ?[O]
      |
      +-- Pfad (A): Gewoehnlich zyklisch
      |       |
      |   [O-219-1]  D_g(mu_q)*mu_P not in [A,M]                 ?[O] primaer
      |       |
      |   [O-219-2]  tau_M, skalare Form Phi_{g;p}                ?[O]
      |       |
      |   [O-219-3]  (1-lambda)Phi = 0 oder Defekt               ?[O]
      |       |
      |   [O-219-4]  B*Phi = 0, periodisch-zyklische Klasse       ?[O]
      |
      +-- Pfad (B): KMS/twisted-cyclic (falls (A) scheitert)
              |
          [O-219-5]  Twistautomorphismus, getwisteter Rand,
                     getwistete Zyklizitaet, Paarung              ?[O] sekundaer
              |
          [O-219-6]  Weil-/Primzahlpotenz-/Gammafaktorpaarung     ?[O] sekundaer
```

---

## Revidierte Gesamtstatustabelle (NEU-218 + NEU-219)

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-218-1a–1d] | Quellbefund, $\delta_p^{(0)}$, $\Theta^\wedge$, Paarung | ✓[M/K/M] |
| [O-218-2–3] | Bimodulisom., Cup-Kozykel | ✓[K/M] |
| [O-218-4] | Augmentationsnull, Typaudit | ✓[M]\_part |
| [SO-Q\_sigma] | Følner-Wachstum, $G_q \notin \sum(1-\sigma_r)B^{\log}$ | ✓[M] |
| [SO-Q\_part] | $D_g(\mu_q)\mu_P \notin C_{H;R}$ | ✓[K/M] |
| [O-218-4-nichtaug] | $\varphi$, $z_\varphi$, Paarung (12.1) | ✓[K/M] |
| **Cup-Aufstieg** | $[L^{\mathrm{cup}}_{g;\mathbf{p}}] \neq 0 \in HH^4(A,M)_g$ | **✓[K/M]** |
| [O-219-0] | Zyklischer Koeffiziententyp | ?[O] |
| [O-219-1] | $D_g(\mu_q)\mu_P \notin [A,M]$ (voller Quotient) | ?[O] primär |
| [O-219-2] | $\tau_M$, $\Phi_{g;\mathbf{p}}$ | ?[O] |
| [O-219-3] | $(1-\lambda)\Phi = 0$ | ?[O] |
| [O-219-4] | $B\Phi = 0$ | ?[O] |
| [O-219-5] | KMS/twisted-cyclic Ersatzpfad | ?[O]\_sek |
| [O-219-6] | Weil-/Gammafaktor-Paarung | ?[O]\_sek |

---

**Commit-Referenz:** Nachfolger von 9e1dd12 (NEU-218).  
**Primärer nächster Audit:** [O-219-1] — voller Kommutatorquotient $D_g(\mu_q)\mu_P \notin [A_{\mathrm{alg}}, M]$.
