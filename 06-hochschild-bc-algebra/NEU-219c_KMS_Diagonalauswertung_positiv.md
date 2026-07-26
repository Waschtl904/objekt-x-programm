# NEU-219c — Positive diagonale KMS-Auswertung

**DAG-Position:** Nachfolger von NEU-219b (Commit 6349d51).  
**Abgeschlossen:** [O-219-5b2] ✓[M]; [O-219-5b1/2] ✓[K/M].  
**Nächster Knoten:** [O-219-5b3] — getwisteter Hochschildrand.

---

## 1. Korrektur: $G_q$ ist beschränkt

$$
G_q \in B^{\log} \subset C(\widehat{\mathbb{Z}}),
\qquad
\boxed{|G_q|_\infty < \infty.}
$$

Die frühere Formulierung, $G_q$ sei auf Folgen wachsender Faktorialtiefe unbeschränkt, ist **falsch**:

$$\boxed{\checkmark[M]_{\mathrm{neg}}.}$$

Unbeschränkt ist ausschließlich das rohe Hilfsprofil
$$
\mathscr{X}(x) = c_{\nu(x)},\qquad c_j = \log(j+2),
$$
das kein Element von $B^{\log}$ ist. Der beschränkte Transportdefekt wird für $x \neq 0$ durch
$$
G_q(x) = \mathscr{X}(qx) - \mathscr{X}(x)
$$
beschrieben.

---

## 2. Extremale KMS-Zustände bei $\beta > 1$

Für $\beta > 1$ sind die extremalen Bost–Connes-KMS-Zustände durch $\chi \in \widehat{\mathbb{Z}}^{\times,*}$ parametrisiert. In der Gibbs-Darstellung wirkt ein diagonales $F \in C(\widehat{\mathbb{Z}})$ durch $F\varepsilon_k = F(k\chi)\varepsilon_k$, und der Hamiltonoperator erfüllt $H\varepsilon_k = (\log k)\varepsilon_k$. Die normierte Gibbs-Formel lautet:

$$
\boxed{
\omega_{\beta,\chi}(F)
= \frac{1}{\zeta(\beta)} \sum_{k=1}^\infty k^{-\beta} F(k\chi).
} \tag{2.1}
$$

Für $F = \sigma_P(G_q)$:

$$
\omega_{\beta,\chi}(\sigma_P(G_q))
= \frac{1}{\zeta(\beta)} \sum_{k=1}^\infty k^{-\beta} G_q(Pk\chi).
\tag{2.2}
$$

---

## 3. Absolute Konvergenz

Da $G_q$ beschränkt ist:
$$
\sum_{k=1}^\infty k^{-\beta} |G_q(Pk\chi)|
\le |G_q|_\infty \sum_{k=1}^\infty k^{-\beta}
= |G_q|_\infty \zeta(\beta) < \infty.
$$

Die Reihe ist für jedes $\beta > 1$ absolut konvergent. Es besteht kein Konvergenzproblem aus dem rohen logarithmischen Profil.

---

## 4. Unabhängigkeit vom Symmetrieparameter

Für $\chi \in \widehat{\mathbb{Z}}^{\times,*}$ ist Multiplikation mit $\chi$ eine Einheitentransformation. Daher:
$$
L_j \mid a\chi \iff L_j \mid a,
$$
und somit:
$$
\boxed{\nu(a\chi) = \nu(a).} \tag{4.1}
$$

Insbesondere:
$$
G_q(Pk\chi) = c_{\nu(qPk)} - c_{\nu(Pk)}. \tag{4.2}
$$

Die diagonale Auswertung ist daher unabhängig von $\chi$:
$$
\boxed{
\omega_{\beta,\chi}(\sigma_P(G_q))
= \frac{1}{\zeta(\beta)} \sum_{k=1}^\infty k^{-\beta}\bigl(c_{\nu(qPk)} - c_{\nu(Pk)}\bigr).
} \tag{4.3}
$$

Alle extremalen KMS-Zustände bei derselben inversen Temperatur liefern auf diesem Element denselben Wert.

---

## 5. Nichtnegativität aller Summanden

Für jedes $x \in \widehat{\mathbb{Z}}$ gilt $L_j \mid x \Rightarrow L_j \mid qx$, also $\nu(qx) \ge \nu(x)$. Da $c_j = \log(j+2)$ streng monoton wächst:

$$
\boxed{G_q(x) \ge 0 \qquad \forall\, x \in \widehat{\mathbb{Z}}.} \tag{5.1}
$$

Jeder Summand in (4.3) ist nichtnegativ. Es kann keine Auslöschung zwischen positiven und negativen Gibbs-Beiträgen auftreten.

---

## 6. Explizit strikt positiver Summand

Wähle $J$ so groß, dass $Pq \mid L_J = (J+1)!$. Setze:

$$
\boxed{k_J := \frac{L_J}{Pq} \in \mathbb{N}^\times.} \tag{6.1}
$$

Dann $Pk_J = L_J/q$ und $qPk_J = L_J$. Da $\chi$ eine Einheit ist:
$$
\nu(qPk_J \chi) = \nu(L_J) = J. \tag{6.2}
$$

Andererseits $L_J \nmid L_J/q$, also:
$$
\nu(Pk_J \chi) = \nu(L_J/q) \le J-1. \tag{6.3}
$$

Folglich:
$$
G_q(Pk_J\chi)
= c_J - c_{\nu(L_J/q)}
\ge c_J - c_{J-1}
= \log\!\left(\frac{J+2}{J+1}\right)
> 0. \tag{6.4}
$$

Jeder hinreichend große $J$ liefert einen solchen positiven Testindex.

---

## 7. Positiver KMS-Wert

Aus Nichtnegativität (5.1) und dem strikt positiven Summand (6.4):
$$
\omega_{\beta,\chi}(\sigma_P(G_q))
\ge \frac{k_J^{-\beta}}{\zeta(\beta)}\, G_q(Pk_J\chi)
> 0.
$$

Somit gilt für jedes $\beta > 1$ und jedes $\chi \in \widehat{\mathbb{Z}}^{\times,*}$:

$$
\boxed{\omega_{\beta,\chi}(\sigma_P(G_q)) > 0.} \tag{7.1}
$$

Dies ist stärker als die verlangte Existenz eines geeigneten KMS-Zustands; das Resultat gilt **universell** in $\beta > 1$ und $\chi$.

$$\boxed{[O\text{-}219\text{-}5b2] \quad \checkmark[M].}$$

---

## 8. Nichtverschwindende neutralisierte Fünffachauswertung

Aus NEU-219b (Gleichungen (1) und (2)) und (7.1) folgt:

$$
\boxed{
\Phi_{\beta,\chi}\!\left(
a_0^{\mathrm{neu}}, \mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}
\right)
= n^{-\beta}\left(\prod_{i=1}^3 \log p_i\right)\omega_{\beta,\chi}(\sigma_P(G_q))
> 0.
} \tag{8.1}
$$

$$\boxed{[O\text{-}219\text{-}5b1/2] \quad \checkmark[K/M].}$$

---

## 9. Reichweite des Resultats

**Bewiesen:**
$$
\boxed{\text{Die neutralisierte KMS-Fünffachform ist nicht identisch null.}}
$$

**Noch nicht bewiesen:**
- $b_{\theta_\beta}\Phi_{\beta,\chi} = 0$ (getwisteter Hochschildrand)
- $\lambda_{\theta_\beta}\Phi_{\beta,\chi} = \Phi_{\beta,\chi}$ (getwistete Zyklizität)
- Nichttriviale Klasse in einer exakt definierten getwisteten zyklischen Kohomologiegruppe

Aus dem einzelnen positiven Wert (8.1) folgt noch **nicht**, dass $\Phi_{\beta,\chi}$ ein getwisteter Kozykel ist.

**Nicht behandelt:** Der Bereich $\beta = 1$. Dort ist die Gibbs-Normierung $\zeta(\beta)^{-1}$ nicht verfügbar; der kritische KMS-Zustand muss separat auditiert werden.

---

## 10. Revidierter DAG-Status

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5b1] | $a_0^{\mathrm{neu}}$, Reduktionen (1)(2) | ✓[K/M] |
| **[O-219-5b2]** | $\omega_{\beta,\chi}(\sigma_P(G_q)) > 0$ für alle $\beta>1$, alle $\chi$ | **✓[M]** |
| [O-219-5b1/2] | Neutralisierte Fünffachform $\Phi_{\beta,\chi} > 0$ | ✓[K/M] |
| **[O-219-5b3]** | $b_{\theta_\beta}\Phi_{\beta,\chi} = 0$ | **?[O] primär** |
| [O-219-5b4] | $\lambda_{\theta_\beta}\Phi_{\beta,\chi} = \Phi_{\beta,\chi}$ | ?[O] bedingt |

```
[O-219-5b1]  Neutralisierer, Reduktion                    [K/M]
      |
[O-219-5b2]  omega_{beta,chi}(sigma_P(G_q)) > 0
             fuer alle beta>1, alle chi                   [M]
      |
[O-219-5b3]  b_{theta_beta} Phi_{beta,chi} = 0            ?[O]  PRIMAER
      |
[O-219-5b4]  lambda_{theta_beta} Phi_{beta,chi} = Phi     ?[O]
```

**Primärer nächster Audit:** [O-219-5b3] — Zuerst muss genau festgelegt werden, an welcher Stelle der Twist $\theta_\beta = \alpha_{i\beta}$ im Hochschildrand wirkt. Erst danach darf $b_{\theta_\beta}\Phi_{\beta,\chi} = 0$ gerechnet werden.
