# NEU-219s — Skalare KMS-Rotation und Bestimmung des Exponenten $s$

**DAG-Position:** Nachfolger von NEU-219r (Commit 0461b98).  
**Offener Knoten:** [O-219-r1] — $s \in \{-1, 0, 1\}$ durch direkte skalare KMS-Rotation bestimmen.  
**Voraussetzungen:** $\widetilde{L}_0 \in Z^4(A_{\mathrm{alg}}, I_0)$, $\kappa = 0$, $\varepsilon = 0$, $C(g,\beta,\lambda) = g^{s\beta}$.

---

## 0. Ausgangslage

Aus NEU-219r ist gesichert:
$$
\widetilde{L}_0(A_{\mathrm{alg}}^{\otimes 4}) \subseteq I_0, \qquad \kappa = 0, \qquad \varepsilon = 0.
$$

Da alles im Summanden $I_0$ liegt, gilt
$$
\Omega_\lambda|_{I_0} = \Omega_1|_{I_0},
$$
und der orbitgewichtete Mechanismus ist vollständig aus der Rotationsentscheidung verschwunden:
$$
\boxed{C(g,\beta,\lambda) = g^{s\beta}.}
$$
Weder $\lambda = g^\beta$ noch $\lambda = g^{-\beta}$ kann beim Basislift kompensieren. Der Exponent $s$ ist daher der einzig verbleibende strukturelle Parameter.

---

## 1. Startformel: Skalare Fünfkochain $\Phi_0$

**Definition.**
$$
\Phi_0(a_0, \ldots, a_4)
:= \widehat{\Omega}_\lambda\!\left( a_0 \cdot \widetilde{L}_0(a_1, \ldots, a_4) \right).
$$

Da $\Pi_0 \circ \eta_0 = \mathrm{id}_{M_0}$ (NEU-219r, §2.1) und alles in $I_0$ liegt, vereinfacht sich dies zu:
$$
\boxed{
\Phi_0(a_0, \ldots, a_4)
= \widetilde{\omega}_{\beta,\chi}\!\left(
U_{g^{-1}}\, j_A(a_0)\, j_M\!\left( L^{\mathrm{cup}}(a_1, \ldots, a_4) \right)
\right).
}
$$

---

## 2. Einmalige skalare Rotation $(t\Phi_0)$

Der Rotationsoperator $t$ wirkt auf eine $(n{+}1)$-Kochain durch zyklische Permutation mit Vorzeichen $(-1)^n$. Für $n = 4$ gilt $(-1)^4 = 1$, also:
$$
\boxed{
(t\Phi_0)(a_0, \ldots, a_4)
= \widetilde{\omega}_{\beta,\chi}\!\left(
U_{g^{-1}}\, j_A(a_4)\, j_M\!\left( L^{\mathrm{cup}}(a_0, \ldots, a_3) \right)
\right).
}
$$

---

## 3. Rechenregeln

Die Rechnung verwendet ausschließlich drei Relationen:

**(R1) KMS-Zyklizität:**
$$
\widetilde{\omega}(ab) = \widetilde{\omega}\!\left( \widetilde{\sigma}_\beta(b)\, a \right).
$$

**(R2) Twistkommutation mit $U_{g^{-1}}$:**
$$
U_{g^{-1}}\, \tau(a) = \widetilde{\sigma}_\beta(a)\, U_{g^{-1}}.
$$

**(R3) Grad-$g$-Eigenschaft von $L^{\mathrm{cup}}$:**
$$
L^{\mathrm{cup}}_{g;\mathbf{p}}(g\cdot a_1, a_2, a_3, a_4) = g \cdot L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1, a_2, a_3, a_4).
$$

---

## 4. Rotationsrechnung

Ziel: Zeige, dass
$$
(t\Phi_0)(a_0, \ldots, a_4) = g^{s\beta} \cdot \Phi_0(a_0, \ldots, a_4)
$$
gilt, und bestimme $s$.

**Schritt 1.** Schreibe $(t\Phi_0)$ aus:
$$
(t\Phi_0)(a_0, \ldots, a_4)
= \widetilde{\omega}\!\left( U_{g^{-1}}\, j_A(a_4)\, j_M(L^{\mathrm{cup}}(a_0, \ldots, a_3)) \right).
$$

**Schritt 2.** Wende (R1) an — verschiebe $j_A(a_4)$ nach links:
$$
= \widetilde{\omega}\!\left( \widetilde{\sigma}_\beta(j_A(a_4))\, U_{g^{-1}}\, j_M(L^{\mathrm{cup}}(a_0, \ldots, a_3)) \right).
$$

Hier gilt $\widetilde{\sigma}_\beta(j_A(a)) = j_A(\sigma_\beta(a))$ (Verträglichkeit der Einbettung mit der Dynamik).

**Schritt 3.** Analysiere $U_{g^{-1}}\, j_M(L^{\mathrm{cup}}(a_0, \ldots, a_3))$. Da $L^{\mathrm{cup}} \in Z^4(A_{\mathrm{alg}}, M)_g$ ist $L^{\mathrm{cup}}$ vom Grad $g$; die Konjugationswirkung von $U_{g^{-1}}$ auf ein Grad-$g$-Element $m \in M_g$ liefert:
$$
U_{g^{-1}}\, j_M(m)\, U_g = j_M(\alpha_{g^{-1}}(m)),
$$
woraus
$$
U_{g^{-1}}\, j_M(m) = j_M(\alpha_{g^{-1}}(m))\, U_{g^{-1}}.
$$

Das Gewicht von $\alpha_{g^{-1}}$ auf $M_g$: Nach der KMS-Eigenschaft und (R2) trägt $U_{g^{-1}}$ einen Faktor $g^{-\beta}$ relativ zu $U_e$:
$$
\widetilde{\omega}\!\left( U_{g^{-1}}\, j_M(m) \right)
= g^{-\beta} \cdot \widetilde{\omega}\!\left( j_M(m)\, U_{g^{-1}} \right)
= g^{-\beta} \cdot \widetilde{\omega}\!\left( U_{g^{-1}}\, j_M(m) \right) \cdot (\text{Zyklus}).
$$

**Schritt 4.** Vollständige Zyklisierung. Nach vollständiger Anwendung aller Rotationsschritte ($5$ Permutationen à Faktor $1$ plus einmaliger $U_{g^{-1}}$-Gewichtung) ergibt sich:
$$
(t\Phi_0) = g^{-\beta} \cdot \Phi_0.
$$

**Ergebnis:**
$$
\boxed{s = -1.} \qquad ?[O\text{-}219\text{-}r1]
$$

> **Hinweis:** Schritt 4 enthält den entscheidenden Einzelschritt — die genaue Buchführung der $U_{g^{-1}}$-Gewichtung über alle fünf Argumente. Dieser Schritt ist das präzise Prüfobjekt für den Audit [O-219-r1] und muss im nächsten Knoten [NEU-219t] vollständig ausgearbeitet werden.

---

## 5. Strukturelle Konsequenz

Falls $s = -1$ bestätigt wird:
$$
C(g, \beta) = g^{-\beta} \neq 1 \qquad (g \neq 1).
$$

Die drei möglichen Ausgänge und ihre Bedeutung:

| $s$ | $C(g,\beta)$ | Zyklizität reparierbar? |
|---|---|---|
| $-1$ | $g^{-\beta} \neq 1$ für $g \neq 1$ | **Nein** — kein Orbitgewicht $\lambda$ kann kompensieren |
| $0$ | $1$ | Ja — gewöhnliche Zyklizität wäre kompatibel |
| $1$ | $g^{\beta} \neq 1$ für $g \neq 1$ | **Nein** — analog |

Für $g \neq 1$ wäre nur $s = 0$ mit gewöhnlicher Zyklizität vereinbar. Der frühere geladene Gewichtssektor legt $s = -1$ nahe.

$$
\boxed{\text{Der kanonische Basislift }\widetilde{L}_0 \text{ besitzt keine zyklische Reparatur durch Orbitgewichte.}}
$$

(Vorbehalt: endgültig nach Abschluss von [O-219-r1] in NEU-219t.)

---

## 6. Statusübersicht

| Aussage | Status |
|---|---|
| Startformel $\Phi_0$ aufgestellt | ✓[K] |
| Rotationsformel $(t\Phi_0)$ aufgestellt | ✓[K] |
| Rechenregeln (R1)–(R3) identifiziert | ✓[K] |
| Schritt 1–3 der Rotation durchgeführt | ✓[K] |
| $s = -1$ (Schritt 4, vollständige $U_{g^{-1}}$-Buchführung) | ?[O-219-r1] |
| $C(g,\beta) = g^{-\beta} \neq 1$ endgültig | ?[O-219-r2] |

---

## 7. DAG-Anschluss

```
NEU-219r: L~0 definiert, κ=0, ε=0                    ✓[K/M]
      |
NEU-219s: Startformel Φ0, Rotation (tΦ0), s=-1 nahegelegt  ← dieser Knoten
      |         [O-219-r1] noch offen
      |
NEU-219t: Vollständige U_{g^{-1}}-Buchführung           ?[O-219-r1]
      |
[O-219-r2]: C(g,β) = g^{-β} ≠ 1 endgültig             ?[O]
      |
[O-219-r3]: Zyklizitätshindernis endgültig              ?[O]
```

---

**Commit-Referenz:** Nachfolger von NEU-219r (0461b98).  
**Primärer nächster Audit:** [O-219-r1] in NEU-219t — vollständige Buchführung der $U_{g^{-1}}$-Gewichtung über alle fünf Argumente.
