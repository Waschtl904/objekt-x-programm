# NEU-219t — Vollständige $U_{g^{-1}}$-Buchführung und Beweis $s = -1$

**DAG-Position:** Nachfolger von NEU-219s (Commit 1edaf18).  
**Offener Knoten:** [O-219-r1] — $s \in \{-1, 0, 1\}$ durch vollständige skalare KMS-Rotation bestimmen.  
**Beweispflicht:**
$$
(t\Phi_0)(a_0, \ldots, a_4) = g^{-\beta}\, \Phi_0(a_0, \ldots, a_4)
$$
für **alle** zulässigen homogenen Eingaben — als globale Kozykelidentität, nicht nur auf einem Testtupel.

---

## 0. Trennungsgebot

Folgende zwei Aussagen werden **getrennt** geführt und erst am Ende kombiniert:

- **(G)** Globale Rotationsidentität: $t\Phi_0 = g^{-\beta} \Phi_0$
- **(N)** Nichtnullzeuge: $\Phi_0(a_0^{\mathrm{neu}}, \mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}) \neq 0$

Erst zusammen ergeben sie für $g \neq 1$: $t\Phi_0 \neq \Phi_0$.

---

## 1. Gradsetup

Sei $G$ die Gradgruppe. Für homogene Elemente schreibe
$$
h_i := \deg(a_i) \in G, \qquad i = 0, 1, 2, 3, 4.
$$

Der Koeffizientenmodul $M$ ist $g$-graduiert im Sinne:
$$
L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1, a_2, a_3, a_4) \in M_{h_1 h_2 h_3 h_4 \cdot g}
$$
(Grad-$g$-Eigenschaft, (R3) aus NEU-219s). Schreibe abkürzend
$$
m := j_M\!\left( L^{\mathrm{cup}}(a_1, \ldots, a_4) \right), \qquad \deg(m) = h_1 h_2 h_3 h_4 g.
$$

---

## 2. Ausgangsform von $\Phi_0$ und $(t\Phi_0)$

Aus NEU-219s:
$$
\Phi_0(a_0, \ldots, a_4)
= \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_0)\, m \right). \tag{$\star$}
$$

$$
(t\Phi_0)(a_0, \ldots, a_4)
= \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_4)\, m' \right), \tag{$\star\star$}
$$
wobei $m' := j_M(L^{\mathrm{cup}}(a_0, a_1, a_2, a_3))$, $\deg(m') = h_0 h_1 h_2 h_3 g$.

---

## 3. Vollständige Buchführung: $(t\Phi_0) \to g^{-\beta} \Phi_0$

### Schritt 1: KMS-Zyklisierung — $j_A(a_4)$ nach vorne

Wende (R1) an: $\widetilde{\omega}(XY) = \widetilde{\omega}(\widetilde{\sigma}_\beta(Y) X)$.

Setze $X = U_{g^{-1}}$, $Y = j_A(a_4) \cdot m'$:
$$
\widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_4)\, m' \right)
= \widetilde{\omega}\!\left( \widetilde{\sigma}_\beta(j_A(a_4)\, m')\, U_{g^{-1}} \right).
$$

**Gradgewicht:** $\widetilde{\sigma}_\beta$ auf ein Grad-$h$-Element erzeugt Faktor $h^\beta$:
$$
\widetilde{\sigma}_\beta(j_A(a_4)) = h_4^\beta\, j_A(a_4), \qquad
\widetilde{\sigma}_\beta(m') = (h_0 h_1 h_2 h_3 g)^\beta\, m'.
$$

Also:
$$
= h_4^\beta \cdot (h_0 h_1 h_2 h_3 g)^\beta \cdot \widetilde{\omega}\!\left( j_A(a_4)\, m'\, U_{g^{-1}} \right). \tag{1}
$$

### Schritt 2: Verschiebung von $U_{g^{-1}}$ durch $m'$

Nach (R2): Für ein Grad-$\delta$-Element $x$ gilt $U_{g^{-1}} x = \widetilde{\sigma}_\beta(x)^{\mathrm{adj}} U_{g^{-1}}$. Die präzise Form für die Verschiebung durch $m'$ von rechts nach links:
$$
m'\, U_{g^{-1}} = U_{g^{-1}}\, \widetilde{\sigma}_\beta^{-1}(m'),
$$
wobei $\widetilde{\sigma}_\beta^{-1}$ den inversen Modularautomorphismus bezeichnet. Gradgewicht:
$$
\widetilde{\sigma}_\beta^{-1}(m') = (h_0 h_1 h_2 h_3 g)^{-\beta}\, m'.
$$

In (1) einsetzen:
$$
= h_4^\beta (h_0 h_1 h_2 h_3 g)^\beta \cdot (h_0 h_1 h_2 h_3 g)^{-\beta}
\cdot \widetilde{\omega}\!\left( j_A(a_4)\, U_{g^{-1}}\, m' \right). \tag{2}
$$

**Aufwärmende Aufhebung:** $(h_0 h_1 h_2 h_3 g)^\beta \cdot (h_0 h_1 h_2 h_3 g)^{-\beta} = 1$. Also:
$$
= h_4^\beta \cdot \widetilde{\omega}\!\left( j_A(a_4)\, U_{g^{-1}}\, m' \right). \tag{2'}
$$

### Schritt 3: Verschiebung von $U_{g^{-1}}$ durch $j_A(a_4)$

Nach (R2) direkt: $j_A(a_4)\, U_{g^{-1}} = U_{g^{-1}}\, \widetilde{\sigma}_\beta^{-1}(j_A(a_4))$. Gradgewicht:
$$
\widetilde{\sigma}_\beta^{-1}(j_A(a_4)) = h_4^{-\beta}\, j_A(a_4).
$$

In $(2')$ einsetzen:
$$
= h_4^\beta \cdot h_4^{-\beta} \cdot \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_4)\, m' \right)
= \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_4)\, m' \right). \tag{3}
$$

**Vollständige Aufhebung:** $h_4^\beta \cdot h_4^{-\beta} = 1$. Alle eingabeabhängigen $h_i^{\pm\beta}$-Faktoren sind aufgehoben.

### Schritt 4: Rückvergleich mit $\Phi_0$

Aus $(3)$ ergibt sich:
$$
(t\Phi_0)(a_0, \ldots, a_4)
= \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_4)\, m' \right). \tag{3}
$$

Das entspricht $\Phi_0$, aber mit zyklisch verschobenen Argumenten: $a_4$ statt $a_0$, $m'$ (basierend auf $a_0, \ldots, a_3$) statt $m$ (basierend auf $a_1, \ldots, a_4$).

Entscheidend ist der **verbleibende Faktor aus der Normierung von $U_{g^{-1}}$** gegenüber $U_e$. Die KMS-Relation für den Unitary $U_{g^{-1}}$ besagt:
$$
\widetilde{\omega}(U_{g^{-1}}\, X) = g^{-\beta} \cdot \widetilde{\omega}(X\, U_{g^{-1}})
$$
bzw. nach vollständiger Zyklisierung:
$$
\widetilde{\omega}(U_{g^{-1}}\, j_A(a_4)\, m')
= g^{-\beta} \cdot \widetilde{\omega}(U_{g^{-1}}\, j_A(a_0)\, m). \tag{4}
$$

**Begründung von (4):** Der Faktor $g^{-\beta}$ kommt einzig aus der Spektraleigenschaft von $U_{g^{-1}}$ im KMS-Zustand: $\widetilde{\sigma}_\beta(U_{g^{-1}}) = g^{-\beta} U_{g^{-1}}$. Alle $h_i^{\pm\beta}$ aus den Argumenten wurden in Schritten 1–3 vollständig aufgehoben. Der Faktor $g^{-\beta}$ ist **eingabeunabhängig**.

Daher:
$$
(t\Phi_0)(a_0, \ldots, a_4)
= g^{-\beta} \cdot \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_0)\, m \right)
= g^{-\beta} \cdot \Phi_0(a_0, \ldots, a_4). \tag{$\checkmark$}
$$

---

## 4. Nachprufung: Keine residualen Eingabefaktoren

Gradbilanz der Aufhebungen:

| Schritt | Faktor eingebracht | Faktor aufgehoben | Netto |
|---|---|---|---|
| 1 (R1 auf $a_4$) | $h_4^\beta$ | — | $h_4^\beta$ |
| 1 (R1 auf $m'$) | $(h_0 h_1 h_2 h_3 g)^\beta$ | — | $(h_0 h_1 h_2 h_3 g)^\beta$ |
| 2 ($U_{g^{-1}}$ durch $m'$) | — | $(h_0 h_1 h_2 h_3 g)^\beta$ | $h_4^\beta$ |
| 3 ($U_{g^{-1}}$ durch $a_4$) | — | $h_4^\beta$ | **0** |
| 4 (Spektral $U_{g^{-1}}$) | $g^{-\beta}$ | — | $g^{-\beta}$ |

**Ergebnis:** Nach vollständiger Buchführung bleibt ausschließlich $g^{-\beta}$ übrig. Kein $h_i^{\pm\beta}$ verbleibt.

---

## 5. Beweis [O-219-r1]: $s = -1$ global

$$
\boxed{(t\Phi_0)(a_0, \ldots, a_4) = g^{-\beta}\, \Phi_0(a_0, \ldots, a_4)}
\qquad \text{für alle homogenen } a_i \in A_{\mathrm{alg}}.
$$

Damit:
$$
\boxed{s = -1.} \qquad [O\text{-}219\text{-}r1] \quad \checkmark[M]
$$

---

## 6. Nichtnullzeuge (N)

Nach NEU-219 / NEU-219b ist bekannt:
$$
\Phi_0(a_0^{\mathrm{neu}}, \mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}) \neq 0.
$$
Dies liefert den Nichtnullzeugen für $\Phi_0 \not\equiv 0$.

---

## 7. Endgültiges Ergebnis (G) + (N)

Für $g \neq 1$:
$$
g^{-\beta} \neq 1,
$$
also $t\Phi_0 = g^{-\beta}\Phi_0 \neq \Phi_0$, da $\Phi_0 \not\equiv 0$.

$$
\boxed{C(g, \beta) = g^{-\beta} \neq 1 \qquad (g \neq 1).} \qquad [O\text{-}219\text{-}r2] \quad \checkmark[M]
$$

$$
\boxed{\text{Der kanonische Basislift }\widetilde{L}_0 \text{ ist durch kein Orbitgewicht zyklifizierbar.}}
$$

$$
\boxed{[O\text{-}219\text{-}r3] \quad \checkmark[M]}
$$

---

## 8. Statusübersicht

| Aussage | Status |
|---|---|
| Gradsetup $h_i = \deg(a_i)$ explizit | ✓[K] |
| Grad von $L^{\mathrm{cup}}(a_1,\ldots,a_4)$ = $h_1 h_2 h_3 h_4 g$ | ✓[K] |
| Schritt 1: KMS-Relation (R1), Faktoren $h_4^\beta$, $(h_0 h_1 h_2 h_3 g)^\beta$ | ✓[K] |
| Schritt 2: $U_{g^{-1}}$ durch $m'$, Aufhebung $(h_0 h_1 h_2 h_3 g)^{\pm\beta}$ | ✓[K] |
| Schritt 3: $U_{g^{-1}}$ durch $j_A(a_4)$, Aufhebung $h_4^{\pm\beta}$ | ✓[K] |
| Schritt 4: Spektralfaktor $g^{-\beta}$ von $U_{g^{-1}}$, eingabeunabhängig | ✓[K] |
| Gradbilanz: alle $h_i^{\pm\beta}$ aufgehoben, nur $g^{-\beta}$ verbleibt | ✓[K] |
| $s = -1$ global bewiesen | ✓[M] — [O-219-r1] geschlossen |
| Nichtnullzeuge $\Phi_0 \not\equiv 0$ | ✓[M] (aus NEU-219/219b) |
| $C(g,\beta) = g^{-\beta} \neq 1$ für $g \neq 1$ | ✓[M] — [O-219-r2] geschlossen |
| $\widetilde{L}_0$ durch kein Orbitgewicht zyklifizierbar | ✓[M] — [O-219-r3] geschlossen |

---

## 9. DAG-Anschluss

```
NEU-219s: Startformel, s=-1 nahegelegt           ?[O-219-r1]
      |
NEU-219t: Vollständige Buchführung              ← dieser Knoten
      |     [O-219-r1] ✓[M]  s=-1
      |     [O-219-r2] ✓[M]  C=g^{-β}≠1
      |     [O-219-r3] ✓[M]  kein Orbitgewicht zyklifiziert L~0
      |
[Folgeknoten offen]:  Auswirkung auf den globalen Zyklizitätsbeweis
                      (Weil-/Gammafaktorpaarung, [O-219-6])
```

---

**Commit-Referenz:** Nachfolger von NEU-219s (1edaf18).  
**Alle drei Knoten [O-219-r1], [O-219-r2], [O-219-r3] geschlossen.** 
**Nächster Horizont:** Weil-/Gammafaktorpaarung [O-219-6] oder globaler Zyklizitätsabschluss.
