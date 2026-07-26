# NEU-186 — Geladener Sektor von $HH^4(A_\mathbb{Q}^{\mathrm{alg}}, A_\mathbb{Q}^{\mathrm{alg}})$: Minimale Cup-Triage mit neutralem Komplementärfaktor (rev2)

## 186.0 — Zweck und Abgrenzung

NEU-185 hat $[\Omega_{\mathbf{p}}]$ mit $\deg_\Gamma(\Omega_{\mathbf{p}}) = 1_\Gamma$ als nichttrivial nachgewiesen. Offen:

$$[O\text{-}186\text{-}0]: \quad HH^4(A_\mathbb{Q}^{\mathrm{alg}},\, A_\mathbb{Q}^{\mathrm{alg}})_{\mathrm{ch}} \neq 0\,?$$

(Geladener Sektor: $\deg_\Gamma \neq 1_\Gamma$.)

**Ausgeschlossen** durch NEU-182–185:
$$HH^0_{\mathrm{ch}} \smile HH^4_{\mathrm{neu}}: \quad \text{keine geladenen Nullkozykel} \Rightarrow \text{Route erschöpft.}$$

NEU-186 führt eine **minimale Cup-Triage mit neutralem Komplementärfaktor** durch
(genau ein Faktor geladen, der andere $\deg_\Gamma = 1_\Gamma$).

> **Hinweis:** Allgemein gilt
> $$HH^i(A,A)_{g_1} \smile HH^{4-i}(A,A)_{g_2} \longrightarrow HH^4(A,A)_{g_1 g_2}.$$
> Für $g_1 g_2 \neq 1_\Gamma$ können auch **beide** Faktoren geladen sein ($g_1 \neq 1_\Gamma$, $g_2 \neq 1_\Gamma$).
> Die untenstehende Tabelle erfasst ausschließlich den Fall $g_2 = 1_\Gamma$ (neutraler Komplementärfaktor)
> und ist keine vollständige Landschaft aller möglichen Cup-Routen.

---

## 186.A — Route 1: Innere geladene Derivationen (ad)

Für $u_g \in A_g$ definiert
$$\operatorname{ad}_{u_g}(a) := u_g a - a u_g$$
einen geladenen Hochschild-1-Kozykel.

**Vorzeichenkonvention:** Bei der Standardkonvention $(bu)(a) = au - ua$ gilt
$$\operatorname{ad}_{u_g} = -b(u_g) \in B^1(A, A)_g.$$
(Falls NEU-174 das entgegengesetzte Vorzeichen für $b: C^0 \to C^1$ verwendet, gilt $\operatorname{ad}_{u_g} = b(u_g)$.
In beiden Fällen: $[\operatorname{ad}_{u_g}] = 0$ in $HH^1(A,A)$.)

Da $[\operatorname{ad}_{u_g}] = 0$, erzeugen alle Cup-Produkte $[\operatorname{ad}_{u_g}] \smile \varphi$ Nullklassen in $HH^4$.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-186-1] | $\operatorname{ad}_{u_g} = \pm b(u_g) \in B^1(A,A)_g$ | ✓[M] |
| [O-186-2] | Cup-Produkte innerer Derivationen trivial in $HH^4$ | ✓[M] — Korand-Faktor |

---

## 186.B — Route 2: Äußere geladene Derivationen

### Satz 186.1 (Klassifizierung des Ansatzes $u \cdot D_p$)

> Für $u \in A$ und Primderivation $D_p$ ist
> $$\delta_{u,p}(a) := u D_p(a)$$
> **genau dann** eine Derivation $A \to A$, wenn $u \in Z(A)$.

*Beweis.* Die Leibnizregel ergibt:
$$\delta_{u,p}(ab) = u D_p(a)b + ua D_p(b),$$
$$\delta_{u,p}(a)b + a\delta_{u,p}(b) = u D_p(a)b + au D_p(b).$$

Gleichheit $\iff$ $(ua - au)D_p(b) = 0$ für alle $a, b$.
Wähle $b = \mu_p^*$: aus der Gradierungsdefinition folgt $D_p(\mu_p^*) = -\mu_p^*$, also
$(ua - au)\mu_p^* = 0$. Rechtsmultiplikation mit $\mu_p$ und $\mu_p^*\mu_p = 1$ liefern
$ua - au = 0$ für alle $a$, d.h. $u \in Z(A)$. Umkehrung: trivial aus Leibnizregel. $\square$

Dasselbe Argument gilt für $a \mapsto D_p(a) u_g$.

**Korollar 186.2.** Für $u_g \in A_g$ mit $g \neq 1_\Gamma$ existiert keine nichttriviale
Derivation der Form $a \mapsto u_g D_p(a)$ oder $a \mapsto D_p(a) u_g$.
(Aus NEU-184: $Z(A)_g = 0$ für $g \neq 1_\Gamma$.)

| Knoten | Inhalt | Status |
|---|---|---|
| [O-186-3a] | Ansatz $u_g D_p$ und $D_p u_g$ scheitert (bikonditional) | ✓[M]\_neg — Satz 186.1 |
| [O-186-3b] | Alternative $\psi_g \in Z^1(A,A)_g$ (nicht dieser Ansatz) | ?[O] → NEU-187 |
| [O-186-3] | $HH^1(A,A)_g \neq 0$ für $g \neq 1_\Gamma$? | ?[O] |

---

## 186.C — Minimale Cup-Triage (neutraler Komplementärfaktor)

| Cup-Route | Voraussetzung | Status |
|---|---|---|
| $HH^0_{\mathrm{ch}} \smile HH^4_{\mathrm{neu}}$ | geladene Nullkozykel | ✓[M]\_neg (NEU-182–184) |
| $HH^1_{\mathrm{ch}} \smile HH^3_{\mathrm{neu}}$ | $HH^1(A,A)_g \neq 0$ | ?[O] → [O-186-3] / NEU-187 |
| $HH^2_{\mathrm{ch}} \smile HH^2_{\mathrm{neu}}$ | geladene 2-Kozykel | ?[O] |
| $HH^3_{\mathrm{ch}} \smile HH^1_{\mathrm{neu}}$ | geladene 3-Kozykel | ?[O] |

Nicht erfasst: Routen mit **beiden** Faktoren geladen ($g_1 \neq 1_\Gamma$, $g_2 \neq 1_\Gamma$,
$g_1 g_2 \neq 1_\Gamma$) sowie direkte geladene Vier-Kozykel ohne Cup-Faktorisierung.

---

## 186.D — Prioritäten

| Knoten | Priorität | Status |
|---|---|---|
| [O-186-1] | — | ✓[M] |
| [O-186-2] | — | ✓[M] |
| [O-186-3a] | — | ✓[M]\_neg |
| [O-186-3b] / [O-186-3] | Hoch | ?[O] → NEU-187 |
| $HH^2, HH^3$-Routen | Mittel | ?[O] |
| Direkte $HH^4_{\mathrm{ch}}$ | Mittel | ?[O] |
| [O-186-0] | — | ?[O] |
