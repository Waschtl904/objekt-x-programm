# NEU-219d — Getwisteter Rand und Ladungsobstruktion

**DAG-Position:** Nachfolger von NEU-219c (Commit bebe4cc).  
**Abgeschlossen:** [O-219-5b3σ] ✓[K/M]; [O-219-5b4]$_{\mathrm{standard}}$ ✓[M]$_{\mathrm{neg}}$.  
**Neuer struktureller Engpass:** Geladene modulare Koeffizientenlinie [O-219-5c1–5c4].

---

## 1. Zwei Twistkonventionen — Inversionskorrektur

Die Bost–Connes-Zeitentwicklung wirkt auf homogenen Elementen durch
$$
\alpha_t(a_h) = h^{it} a_h.
$$

Die in NEU-219a verwendete analytische Fortsetzung war $\theta_\beta := \alpha_{i\beta}$, also $\theta_\beta(a_h) = h^{-\beta}a_h$.
Die KMS-Gleichung lautet in dieser Orientierung:
$$
\omega_{\beta,\chi}(xy) = \omega_{\beta,\chi}\!\left(y\,\theta_\beta(x)\right). \tag{1.1}
$$

Der Standardrand der getwisteten zyklischen Kohomologie verwendet die Konvention $\omega(xy) = \omega(\sigma(y)x)$. Der dort einzusetzende Twist ist daher:
$$
\boxed{ \sigma_\beta := \theta_\beta^{-1} = \alpha_{-i\beta}, \qquad \sigma_\beta(a_h) = h^\beta a_h. } \tag{1.3}
$$

Aus (1.1) folgt:
$$
\omega_{\beta,\chi}(xy) = \omega_{\beta,\chi}\!\left(\sigma_\beta(y)x\right). \tag{1.4}
$$

Der $\sigma_\beta$-getwistete Hochschildrand ist:
$$
\begin{aligned}
(b^{\sigma_\beta}\varphi)(a_0,\ldots,a_{n+1})
={}&
\sum_{j=0}^{n}(-1)^j \varphi(a_0,\ldots,a_ja_{j+1},\ldots,a_{n+1})\\
&+ (-1)^{n+1}\varphi(\sigma_\beta(a_{n+1})a_0,a_1,\ldots,a_n).
\end{aligned} \tag{1.5}
$$

**Konsequenz:** Die frühere Schreibweise $b^{\theta_\beta}\Phi_{\beta,\chi}=0$ in der Standard-Letztrandkonvention ist zu korrigieren zu:
$$
\boxed{ b^{\sigma_\beta}\Phi_{\beta,\chi}=0, \qquad \sigma_\beta = \theta_\beta^{-1}. }
$$

---

## 2. Die skalare Fünffachform

Setze $L := L^{\mathrm{cup}}_{g;\mathbf{p}} \in Z^4(A_{\mathrm{alg}}, M)_g$ und definiere:
$$
\boxed{
\Phi_{\beta,\chi}(a_0,a_1,a_2,a_3,a_4)
= \omega_{\beta,\chi}\!\left( a_0 L(a_1,a_2,a_3,a_4) \right).
} \tag{2.1}
$$

Alle algebraischen homogenen Elemente sind für die Zeitentwicklung analytisch; die Werte von $L$ liegen in endlichen homogenen Komponenten von $M \subseteq A_{C^*}$.

---

## 3. Vollständige Randrechnung

Für $a_0, \ldots, a_5 \in A_{\mathrm{alg}}$ gilt mit $n=4$:
$$
\begin{aligned}
&(b^{\sigma_\beta}\Phi_{\beta,\chi})(a_0,a_1,a_2,a_3,a_4,a_5)\\
={}&\Phi(a_0a_1,a_2,a_3,a_4,a_5)\\
&- \Phi(a_0,a_1a_2,a_3,a_4,a_5)\\
&+ \Phi(a_0,a_1,a_2a_3,a_4,a_5)\\
&- \Phi(a_0,a_1,a_2,a_3a_4,a_5)\\
&+ \Phi(a_0,a_1,a_2,a_3,a_4a_5)\\
&- \Phi(\sigma_\beta(a_5)a_0,a_1,a_2,a_3,a_4).
\end{aligned} \tag{3.1}
$$

Einsetzen von (2.1) ergibt für die ersten fünf Terme:
$$
\omega_{\beta,\chi}\Bigl(a_0\bigl[
a_1L(a_2,a_3,a_4,a_5)
-L(a_1a_2,a_3,a_4,a_5)
+L(a_1,a_2a_3,a_4,a_5)
-L(a_1,a_2,a_3a_4,a_5)
+L(a_1,a_2,a_3,a_4a_5)
\bigr]\Bigr). \tag{3.2}
$$

Da $bL = 0$, gilt die Standardidentität:
$$
a_1L(a_2,a_3,a_4,a_5)
-L(a_1a_2,\ldots)
+\cdots
+L(a_1,a_2,a_3,a_4a_5)
= L(a_1,a_2,a_3,a_4)\,a_5. \tag{3.3}
$$

(3.1) reduziert sich damit auf:
$$
(b^{\sigma_\beta}\Phi)(a_0,\ldots,a_5)
= \omega_{\beta,\chi}\!\left(a_0 L(a_1,a_2,a_3,a_4)\,a_5\right)
- \omega_{\beta,\chi}\!\left(\sigma_\beta(a_5)\,a_0 L(a_1,a_2,a_3,a_4)\right).
\tag{3.4}
$$

Mit $x = a_0 L(a_1,a_2,a_3,a_4)$, $y = a_5$ liefert die KMS-Identität (1.4):
$$
\omega_{\beta,\chi}(xy) = \omega_{\beta,\chi}(\sigma_\beta(y)x).
$$

Die beiden Terme in (3.4) sind identisch. Folglich:

$$
\boxed{ b^{\sigma_\beta}\Phi_{\beta,\chi} = 0. } \tag{3.5}
$$

Für diese Randrechnung wird keine zusätzliche $\sigma_\beta$-Äquivarianz von $L$ benötigt. Es genügen $bL=0$ und die KMS-Identität.

$$\boxed{ [O\text{-}219\text{-}5b3^\sigma] \quad \checkmark[K/M]. }$$

---

## 4. Warum $b^{\theta_\beta}$ die falsche Orientierung ist

Mit $\theta_\beta$ statt $\sigma_\beta$ im letzten Randterm ergibt sich:
$$
(b^{\theta_\beta}\Phi)(a_0,\ldots,a_5)
= \omega_{\beta,\chi}\!\left((\sigma_\beta(a_5)-\theta_\beta(a_5))\,a_0 L(a_1,\ldots,a_4)\right).
\tag{4.1}
$$

Für homogenes $a_5 \in A_h$ ist $\sigma_\beta(a_5) - \theta_\beta(a_5) = (h^\beta - h^{-\beta})a_5 \neq 0$ im Allgemeinen.

$$
\boxed{ \text{Die Behauptung } b^{\theta_\beta}\Phi_{\beta,\chi}=0 \text{ (Standard-Letztrandkonvention)} \quad \checkmark[M]_{\mathrm{neg}}. }
$$

---

## 5. Standardmäßige getwistete Zyklizität verlangt drei Bedingungen

Ein $\sigma$-getwisteter zyklischer 4-Kozykel muss erfüllen:
1. $b^\sigma\Phi = 0$,
2. $\Phi(a_0,\ldots,a_4) = \Phi(\sigma(a_4),a_0,a_1,a_2,a_3)$,
3. $\Phi(a_0,\ldots,a_4) = \Phi(\sigma(a_0),\ldots,\sigma(a_4))$.

Bedingung 1 ist bewiesen. Bedingung 3 scheitert wegen der Ladung.

---

## 6. Transformationsgesetz des geladenen Cup-Kozykels

Für homogene Eingaben $a_j \in A_{h_j}$ gilt $L(a_1,a_2,a_3,a_4) \in M_{g h_1 h_2 h_3 h_4}$. Für die reelle Zeitwirkung:
$$
\alpha_t\!\left(L(a_1,a_2,a_3,a_4)\right) = g^{it}\,L(\alpha_t(a_1),\ldots,\alpha_t(a_4)). \tag{6.1}
$$

Für $\sigma_\beta = \alpha_{-i\beta}$:
$$
\boxed{ L(\sigma_\beta(a_1),\ldots,\sigma_\beta(a_4)) = g^{-\beta}\,\sigma_\beta\!\left(L(a_1,\ldots,a_4)\right). } \tag{6.2}
$$

Da KMS-Zustände unter der reellen Zeitentwicklung invariant sind:
$$
\begin{aligned}
\Phi_{\beta,\chi}(\sigma_\beta(a_0),\ldots,\sigma_\beta(a_4))
&= \omega_{\beta,\chi}\!\left(\sigma_\beta(a_0)\,L(\sigma_\beta(a_1),\ldots,\sigma_\beta(a_4))\right)\\
&= g^{-\beta}\,\omega_{\beta,\chi}\!\left(\sigma_\beta\!\left(a_0 L(a_1,\ldots,a_4)\right)\right)\\
&= g^{-\beta}\,\Phi_{\beta,\chi}(a_0,\ldots,a_4).
\end{aligned} \tag{6.3}
$$

Damit ist $\Phi_{\beta,\chi}$ kein invariantes Element, sondern ein Eigenkochain:
$$
\boxed{ T_{\sigma_\beta}\Phi_{\beta,\chi} = g^{-\beta}\Phi_{\beta,\chi}. } \tag{6.4}
$$

Da $g \neq 1$ und $\Phi_{\beta,\chi} \neq 0$ (NEU-219c):
$$
\boxed{ T_{\sigma_\beta}\Phi_{\beta,\chi} \neq \Phi_{\beta,\chi}. } \tag{6.5}
$$

---

## 7. Konsequenz: Zyklizitätsobstruktion

Der getwistete zyklische Operator in Grad 4:
$$
(\lambda_{\sigma_\beta}\Phi)(a_0,a_1,a_2,a_3,a_4) = \Phi(\sigma_\beta(a_4),a_0,a_1,a_2,a_3).
$$

Im parazyklischen Komplex gilt $\lambda_{\sigma_\beta}^5 = T_{\sigma_\beta}$. Würde $\lambda_{\sigma_\beta}\Phi_{\beta,\chi} = \Phi_{\beta,\chi}$ gelten, so folgte $T_{\sigma_\beta}\Phi_{\beta,\chi} = \Phi_{\beta,\chi}$. Dies widerspricht (6.4) wegen $g^{-\beta} \neq 1$ und $\Phi_{\beta,\chi} \neq 0$.

$$
\boxed{ \lambda_{\sigma_\beta}\Phi_{\beta,\chi} \neq \Phi_{\beta,\chi}. } \tag{7.1}
$$

$$\boxed{ [O\text{-}219\text{-}5b4]_{\mathrm{standard}} \quad \checkmark[M]_{\mathrm{neg}}. }$$

Der strukturelle Engpass ist nicht ein schwer auszuwertender Rotationsterm, sondern die globale Ladung:
$$
\boxed{ T_{\sigma_\beta}\Phi = g^{-\beta}\Phi. }
$$

---

## 8. Beweisstand

Für jedes $\beta > 1$ und jeden extremalen KMS-Zustand $\omega_{\beta,\chi}$:

$$
\Phi_{\beta,\chi} \neq 0, \qquad b^{\sigma_\beta}\Phi_{\beta,\chi} = 0, \qquad T_{\sigma_\beta}\Phi_{\beta,\chi} = g^{-\beta}\Phi_{\beta,\chi} \neq \Phi_{\beta,\chi}.
$$

$\Phi_{\beta,\chi}$ ist ein nichtverschwindender getwisteter Hochschildkozykel, aber kein standardmäßiger getwisteter zyklischer Kozykel:

$$
\boxed{ \Phi_{\beta,\chi} \in Z^4_{\sigma_\beta,\mathrm{Hoch}}(A_{\mathrm{alg}}) }
$$
$$
\boxed{ \Phi_{\beta,\chi} \notin Z^4_{\sigma_\beta,\lambda}(A_{\mathrm{alg}}) \qquad (g \neq 1). }
$$

---

## 9. Reparaturknoten: Geladene modulare Koeffizientenlinie

Die Ladung $g$ muss auf der zyklischen Koeffizientenseite kompensiert werden. Gesucht ist eine eindimensionale modulare Koeffizientenlinie
$$
\mathbb{C}_{g,\beta} = \mathbb{C}\,\mathbf{e}_{g,\beta}
\quad \text{mit} \quad
\sigma_\beta(\mathbf{e}_{g,\beta}) = g^\beta\mathbf{e}_{g,\beta}.
$$

Dann wäre für $\widetilde{\Phi}_{\beta,\chi} = \mathbf{e}_{g,\beta} \otimes \Phi_{\beta,\chi}$ formal:
$$
T_{\sigma_\beta}\widetilde{\Phi}_{\beta,\chi} = g^\beta g^{-\beta}\widetilde{\Phi}_{\beta,\chi} = \widetilde{\Phi}_{\beta,\chi}.
$$

Dies ist noch keine fertige zyklische Theorie. Zu konstruieren und zu prüfen sind:

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5c1] | Typkorrekte geladene modulare Koeffizientenlinie $\mathbb{C}_{g,\beta}$ | ?[O] |
| [O-219-5c2] | Zugehöriger para-/zyklischer Operator auf $\mathbb{C}_{g,\beta} \otimes \Phi_{\beta,\chi}$ | ?[O] |
| [O-219-5c3] | $b^{\sigma_\beta}\widetilde{\Phi} = 0$ (mit Koeffizientenlinie) | ?[O] |
| [O-219-5c4] | $\lambda_{\sigma_\beta}\widetilde{\Phi} = \widetilde{\Phi}$ | ?[O] |

$$
\boxed{
\text{KMS-Neutralisierung schließt den getwisteten Hochschildrand, aber nicht die getwistete Zyklizität.}
}
$$

---

## 10. Revidierter DAG-Status

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5b1] | Neutralisierer, Reduktionen | ✓[K/M] |
| [O-219-5b2] | $\omega_{\beta,\chi}(\sigma_P(G_q)) > 0$ | ✓[M] |
| [O-219-5b3σ] | $b^{\sigma_\beta}\Phi_{\beta,\chi} = 0$, $\sigma_\beta = \theta_\beta^{-1}$ | ✓[K/M] |
| $b^{\theta_\beta}\Phi = 0$ (falsche Orientierung) | Standard-Letztrandkonvention | ✓[M]$_{\mathrm{neg}}$ |
| **[O-219-5b4]$_{\mathrm{standard}}$** | $\lambda_{\sigma_\beta}\Phi \neq \Phi$ wegen $T_{\sigma_\beta}\Phi = g^{-\beta}\Phi$ | **✓[M]$_{\mathrm{neg}}$** |
| [O-219-5c1] | Geladene modulare Koeffizientenlinie | ?[O] primär |
| [O-219-5c2] | Para-/zyklischer Operator | ?[O] |
| [O-219-5c3] | $b^{\sigma_\beta}\widetilde{\Phi} = 0$ | ?[O] |
| [O-219-5c4] | $\lambda_{\sigma_\beta}\widetilde{\Phi} = \widetilde{\Phi}$ | ?[O] |

```
[O-219-5b3sigma]  b^{sigma_beta} Phi = 0                  [K/M]
      |
      +-- b^{theta_beta} Phi = 0 (falsch)                  [M]_neg
      |
[O-219-5b4]_standard  lambda Phi != Phi                   [M]_neg
      |                wegen T_sigma Phi = g^{-beta} Phi
      |
[O-219-5c1]  C_{g,beta}: sigma_beta(e) = g^beta * e       ?[O] PRIMAER
      |
[O-219-5c2]  para-/zyklischer Operator                    ?[O]
      |
[O-219-5c3]  b^sigma Phi_tilde = 0                        ?[O]
      |
[O-219-5c4]  lambda Phi_tilde = Phi_tilde                 ?[O]
```

**Primärer nächster Audit:** [O-219-5c1] — Konstruktion der typkorrekten geladenen modularen Koeffizientenlinie $\mathbb{C}_{g,\beta}$.
