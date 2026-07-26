# NEU-218 — Grad-3-Partner und geladener Cup-Aufstieg: Vollständiger Abschluss

**DAG-Position:** Direkter Nachfolger von NEU-217 / [O-217-2c-6d] (Commit 604e6c6).  
**Status gesamt:** ✓[K/M]

---

## Voraussetzung (aus NEU-217, vollständig bewiesen)

$$
[D_g] \in HH^1\!\left(A_{\mathrm{alg}},\, \mathfrak{M}_{\mathrm{glob}}^{\log}\right)_g \setminus\{0\}.
$$

---

## 1. Ausgangsdaten

Setze
$$
A := A_{\mathrm{alg}},
\qquad
M := \mathfrak{M}_{\mathrm{glob}}^{\log}.
$$

Die Faktorialdaten lauten
$$
L_j = (j+1)!,
\qquad
c_j = \log(j+2),
$$
$$
P_j = E_{L_j},
\qquad
q_j = P_j - P_{j+1},
$$
$$
X_N = \sum_{j=0}^{N-1} c_j q_j + c_N P_N.
$$

Das rohe Profil $(c_{\nu(x)})$ ist unbeschränkt und **kein** Element von $B^{\log}$; die normkonvergenten Transportdifferenzen $G_{a,d}$ liegen dagegen in $B^{\log}$. Die Schiebaktion wirkt stabil:
$$
(\sigma_k f)(x) = f(kx).
$$

Schreibe den geladenen Grad reduziert als $g = m/n$, $(m,n)=1$. Wähle vier paarweise verschiedene Primzahlen $q, p_1, p_2, p_3$ mit $q, p_1, p_2, p_3 \nmid mn$. Setze
$$
P := p_1 p_2 p_3,
\qquad
R := \{q, p_1, p_2, p_3\}.
$$

Im teilerfremden Generatorsektor liefert die NEU-211-Formel
$$
D_g(\mu_q) = \mu_{mq} G_q \mu_n^*,
\qquad
G_q := G_{q,1} = \lim_{N\to\infty}\bigl(\sigma_q(X_N) - X_N\bigr) \in B^{\log}.
$$

Da $(P,n)=1$ gilt $\mu_n^* \mu_P = \mu_P \mu_n^*$. Ferner gilt für $F \in B^{\log}$: $F\mu_P = \mu_P \sigma_P(F)$. Daher:
$$
\boxed{
D_g(\mu_q)\mu_P = \mu_{mqP}\,\sigma_P(G_q)\,\mu_n^*.
}
\tag{1.1}
$$

---

## 2. Der dynamische Koinvariantenknoten

$$
\boxed{
[\mathrm{SO\text{-}Q}_\sigma]:\quad
\sigma_P(G_q) \notin \sum_{r \in R}(1-\sigma_r)B^{\log}.
}
\tag{2.1}
$$

Da die $\sigma_r$ kommutieren:
$$
\sigma_P(G_q) - G_q
= (\sigma_{p_1}-1)\sigma_{p_2 p_3}(G_q)
+ (\sigma_{p_2}-1)\sigma_{p_3}(G_q)
+ (\sigma_{p_3}-1)G_q.
$$

Wegen der Stabilität von $B^{\log}$ folgt $\sigma_P(G_q) - G_q \in \sum_{i=1}^3 (1-\sigma_{p_i})B^{\log}$. Somit:

$$
\boxed{
[\sigma_P(G_q)] = [G_q]
\quad \text{in} \quad
B^{\log}\big/\sum_{r \in R}(1-\sigma_r)B^{\log}.
}
\tag{2.2}
$$

Es genügt, $G_q$ zu behandeln.

---

## 3. Punktweise Formel für $G_q$

Für $x \in \widehat{\mathbb{Z}} \setminus \{0\}$ definiere
$$
\nu(x) := \max\{j \ge 0 \mid L_j \mid x\}.
$$
Dies ist für jedes $x \neq 0$ endlich. Das rohe punktweise Hilfsprofil sei
$$
\mathscr{X}(x) := c_{\nu(x)} \qquad (x \neq 0).
$$

**Wichtig:** $\mathscr{X} \notin B^{\log}$ und wird ausschließlich als punktweise Hilfsfunktion auf nichtverschwindenden Testpunkten verwendet.

Für $x \neq 0$ stabilisiert $\sigma_q(X_N)(x) - X_N(x)$ ab $N > \max\{\nu(x), \nu(qx)\}$, und es folgt:

$$
\boxed{
G_q(x) = \mathscr{X}(qx) - \mathscr{X}(x).
}
\tag{3.1}
$$

Am Ursprung: $G_q(0) = 0$, da $X_N(q \cdot 0) - X_N(0) = c_N - c_N = 0$.

Die Formel (3.1) ist eine punktweise Beschreibung des bereits in $B^{\log}$ konstruierten beschränkten Transportdefekts, keine Behauptung, das rohe Profil selbst sei stetig.

---

## 4. Mehrparameter-Følneroperatoren

Für $r \in R$ und $N \ge 1$ setze $S_{r,N} := \sum_{k=0}^{N-1} \sigma_r^k$ und

$$
\boxed{
\mathcal{F}_N := S_{q,N}\, S_{p_1,N}\, S_{p_2,N}\, S_{p_3,N}.
}
\tag{4.1}
$$

Die Operatoren kommutieren. Da $|S_{r,N} F|_\infty \le N|F|_\infty$ und $S_{r,N}(1-\sigma_r) = 1 - \sigma_r^N$, gilt für jedes $F \in B^{\log}$:

$$
\left|\mathcal{F}_N\bigl((1-\sigma_r)F\bigr)\right|_\infty
= \left|\prod_{\substack{t \in R \\ t \neq r}} S_{t,N}\cdot (1-\sigma_r^N)F\right|_\infty
\le 2N^3 |F|_\infty.
\tag{4.2}
$$

Falls $G_q = \sum_{r \in R}(1-\sigma_r)F_r$ mit $F_r \in B^{\log}$, müsste daher:

$$
\boxed{
\left|\mathcal{F}_N(G_q)\right|_\infty
\le 2N^3 \sum_{r \in R} |F_r|_\infty.
}
\tag{4.4}
$$

Insbesondere wäre $N^{-3}|\mathcal{F}_N(G_q)|_\infty$ gleichmäßig beschränkt.

---

## 5. Konstruktion der Testpunkte

Sei $J_N$ der kleinste Index mit
$$
v_q(L_{J_N}) \ge N.
\tag{5.1}
$$

Dann $q^N \mid L_{J_N}$, und wir setzen den Testpunkt:

$$
\boxed{
x_N := \frac{L_{J_N}}{q^N}
}
\tag{5.2}
$$

als Element von $\widehat{\mathbb{Z}} \setminus \{0\}$. Setze $d_N := v_q(L_{J_N}) - N$. Aus der Minimalität von $J_N$ folgt $v_q(L_{J_N - 1}) < N$, daher $0 \le d_N < v_q(J_N+1)$, also

$$
d_N < \log_q(J_N+1).
\tag{5.5}
$$

Definiere $K_N := q(d_N + 1)$. Dann gilt:

$$
K_N = O(\log J_N),
\tag{5.7}
$$

und da $J_N \to \infty$:

$$
\frac{K_N}{J_N} \longrightarrow 0.
\tag{5.8}
$$

---

## 6. Gleichmäßige Kontrolle der Anfangstiefe

Sei $s = p_1^{k_1} p_2^{k_2} p_3^{k_3}$ mit $0 \le k_i < N$. Da $q$ von allen $p_i$ verschieden ist:
$$
v_q(sx_N) = d_N.
\tag{6.1}
$$

Falls $L_j \mid sx_N$, so muss $v_q(L_j) \le d_N$, also $\lfloor(j+1)/q\rfloor \le d_N$, woraus $j < K_N$ folgt. Daher gleichmäßig für alle $0 \le k_i < N$:

$$
\boxed{
\nu(sx_N) \le K_N.
}
\tag{6.2}
$$

---

## 7. Gleichmäßige Kontrolle der Endtiefe

Es gilt $q^N sx_N = s L_{J_N}$. Damit $L_{J_N} \mid q^N sx_N$, und folglich:

$$
\boxed{
\nu(q^N sx_N) \ge J_N.
}
\tag{7.1}
$$

---

## 8. Wachstum der Følner-Summen

Für jedes feste $s = p_1^{k_1} p_2^{k_2} p_3^{k_3}$ teleskopiert die $q$-Richtung:
$$
\sum_{k=0}^{N-1} G_q(q^k sx_N) = \mathscr{X}(q^N sx_N) - \mathscr{X}(sx_N).
$$

Mit (6.2) und (7.1):
$$
\sum_{k=0}^{N-1} G_q(q^k sx_N) \ge c_{J_N} - c_{K_N}.
\tag{8.1}
$$

Summation über alle $N^3$ Tripel $(k_1,k_2,k_3) \in \{0,\ldots,N-1\}^3$:

$$
\boxed{
\mathcal{F}_N(G_q)(x_N) \ge N^3\bigl(c_{J_N} - c_{K_N}\bigr).
}
\tag{8.2}
$$

Wegen $c_j = \log(j+2)$:
$$
c_{J_N} - c_{K_N} = \log\!\left(\frac{J_N+2}{K_N+2}\right).
$$

Aus $K_N = O(\log J_N)$ folgt:

$$
\boxed{
c_{J_N} - c_{K_N} \longrightarrow +\infty.
}
\tag{8.3}
$$

Damit:

$$
\boxed{
N^{-3}\left|\mathcal{F}_N(G_q)\right|_\infty \ge c_{J_N} - c_{K_N} \longrightarrow +\infty.
}
\tag{8.4}
$$

Dies widerspricht der notwendigen Beschränktheit (4.4). Folglich:

$$
\boxed{
G_q \notin \sum_{r \in R}(1-\sigma_r)B^{\log}.
}
\tag{8.5}
$$

Mit (2.2):

$$
\boxed{
\sigma_P(G_q) \notin \sum_{r \in R}(1-\sigma_r)B^{\log}.
}
\tag{8.6}
$$

$$
\boxed{[\mathrm{SO\text{-}Q}_\sigma] \quad \checkmark[M].}
$$

---

## 9. Übertragung auf den partiellen Modulkommutatorquotienten

Setze $H := gqP = mqP/n$. Für $r \in R$ besitzt jedes Element der homogenen Komponente $M_{H/r}$ die eindeutige Normalform $\mu_{mqP/r} F_r \mu_n^*$ mit $F_r \in B^{\log}$.

Da $(r,n)=1$ gilt $\mu_n^* \mu_r = \mu_r \mu_n^*$. Daher:

$$
\mu_r m_r - m_r \mu_r = \mu_{mqP}(1-\sigma_r)(F_r)\mu_n^*.
\tag{9.1}
$$

Definiere den partiellen Kommutatorraum:

$$
\boxed{
C_{H;R} := \sum_{r \in R} [\mu_r, M_{H/r}] \subseteq M_H.
}
\tag{9.2}
$$

Wäre $D_g(\mu_q)\mu_P \in C_{H;R}$, so implizierte die Normalform (1.1) zusammen mit (9.1) eine Darstellung $G_q = \sum_{r}(1-\sigma_r)F_r$. Dies widerspricht (8.5). Also:

$$
\boxed{
D_g(\mu_q)\mu_P \notin C_{H;R}.
}
\tag{9.3}
$$

$$
\boxed{
\overline{D_g(\mu_q)\mu_P} \neq 0 \quad \text{in} \quad M_H / C_{H;R}.
}
\tag{9.4}
$$

$$\boxed{[\mathrm{SO\text{-}Q}_{\mathrm{part}}] \quad \checkmark[K/M].}$$

*Hinweis:* Der stärkere Vollquotientenknoten $D_g(\mu_q)\mu_P \stackrel{?}{\notin} [A,M]$ wird nicht entschieden — er ist für den Cup-Nichtverschwindensbeweis nicht notwendig.

---

## 10. Konstruktion des nichtaugmentativen Funktionals

Aus (9.4) existiert ein algebraisches lineares Funktional $\lambda: M_H/C_{H;R} \to \mathbb{C}$ mit $\lambda\!\left(\overline{D_g(\mu_q)\mu_P}\right) \neq 0$.

Definiere $\varphi_H := \lambda \circ \pi_{H;R}$ (Quotientenabbildung) und erweitere durch null auf alle anderen homogenen Komponenten. Dann $\varphi \in M^\vee$ mit:

$$
\boxed{
\varphi(D_g(\mu_q)\mu_P) \neq 0.
}
\tag{10.1}
$$

Für jedes $r \in R$ und $m \in M_{H/r}$:

$$
\boxed{
\varphi(\mu_r m) = \varphi(m\mu_r).
}
\tag{10.2}
$$

Eine Zentralität von $\varphi$ gegenüber ganz $A$ wird nicht behauptet und nicht benötigt.

---

## 11. Expliziter dualer Grad-4-Zyklus

Schreibe $\mathbf{r} = (q, p_1, p_2, p_3)$. Definiere:

$$
\boxed{
z_\varphi := \sum_{\pi \in S_4} \mathrm{sgn}(\pi)\;
\varphi \otimes \mu_{r_{\pi(1)}} \otimes \mu_{r_{\pi(2)}} \otimes \mu_{r_{\pi(3)}} \otimes \mu_{r_{\pi(4)}}.
}
\tag{11.1}
$$

**Innere Randterme:** Die Primisometrien kommutieren ($\mu_{r_i}\mu_{r_j} = \mu_{r_j}\mu_{r_i}$). Jeder innere Randterm löscht sich mit dem Term, der durch Vertauschung der benachbarten Faktoren entsteht.

**Äußere Randterme:** Die beiden äußeren Randfamilien stehen sich mit entgegengesetztem Vorzeichen gegenüber; ihre Koeffizienten stimmen wegen (10.2) überein.

$$
\boxed{
\partial z_\varphi = 0,
}
\tag{11.2}
$$

somit $z_\varphi \in Z_4(A, M^\vee)$.

---

## 12. Nichtverschwindende Paarung

Sei $L^{\mathrm{cup}}_{g;\mathbf{p}} = D_g \smile \Theta^\wedge_{p_1,p_2,p_3}$.

In der Paarung mit $z_\varphi$ überleben genau die sechs Permutationen, bei denen $\mu_q$ im ersten Eingabeslot steht. Für $\tau \in S_3$ trägt jeder Summand das Vorzeichen $\mathrm{sgn}(\tau) \cdot \mathrm{sgn}(\tau) = +1$. Folglich:

$$
\boxed{
\left\langle L^{\mathrm{cup}}_{g;\mathbf{p}},\, z_\varphi \right\rangle
= 6 \left(\prod_{i=1}^3 \log p_i\right) \varphi(D_g(\mu_q)\mu_P).
}
\tag{12.1}
$$

Wegen (10.1):

$$
\boxed{
\left\langle L^{\mathrm{cup}}_{g;\mathbf{p}},\, z_\varphi \right\rangle \neq 0.
}
\tag{12.2}
$$

Daher kann $L^{\mathrm{cup}}_{g;\mathbf{p}}$ kein Hochschildrand sein:

$$
\boxed{
[L^{\mathrm{cup}}_{g;\mathbf{p}}] \neq 0
\quad \text{in} \quad
HH^4(A, M)_g.
}
\tag{12.3}
$$

---

## 13. Revidierter DAG-Status

| Knoten | Inhalt | Status |
|--------|--------|--------|
| $[\mathrm{SO\text{-}Q}_\sigma]$ | $\sigma_P(G_q) \notin \sum_r(1-\sigma_r)B^{\log}$ | ✓[M] |
| $[\mathrm{SO\text{-}Q}_{\mathrm{part}}]$ | $D_g(\mu_q)\mu_P \notin C_{H;R}$ | ✓[K/M] |
| Vollquotient $[A,M]$ | $D_g(\mu_q)\mu_P \stackrel{?}{\notin} [A,M]$ | ?[O] optional |
| [O-218-4-nichtaug] | Ketten+Paarungsarchitektur | ✓[K/M] |
| [O-218-4] | Nichtverschwindensbeweis | ✓[K/M] |
| **Cup-Aufstieg** | $[D_g] \smile [\Theta^\wedge] \neq 0 \in HH^4(A,M)_g$ | **✓[K/M]** |

Aktualisierter DAG-Pfad:

```
[O-217-2c-6d]  [D_g] in HH^1_g \ {0}                              [M]
      |
 [O-218-1a..3]  Kozykelkonstruktion vollstaendig                   [K/M]
      |
 [O-218-4]     Augmentationsnull; Typaudit                        [M]_part
      |
 [O-218-4-nichtaug]
      |
      +-- Spurzustand: tau=0 via Tracialitaet                      [M]_neg
      |
      +-- Quotientenpfad (primaer):
          |
          SO-1a-Nica-Formel (2.3)                                  [M]
          Normalform (1.1): D_g(mu_q)*mu_P = mu_mqP*sigma_P(G_q)*mu_n*
          |
          Foelner-Wachstumsargument (Sek. 4-8):
            F_N(G_q)(x_N) >= N^3 * (c_J_N - c_K_N) -> +inf        [M]
          |
          [SO-Q_sigma]: sigma_P(G_q) not in sum_r(1-sigma_r)B^log  [M]
          |
          [SO-Q_part]: D_g(mu_q)*mu_P not in C_{H;R}              [K/M]
          |
          phi_com (10.1-10.2), z_phi (11.1-11.2), Paarung (12.1)  [K/M]
          |
          v
 [L^cup] != 0 in HH^4(A_alg, M)_g                                [K/M]
          |
          v
       Objekt X.3 (algebraischer Hochschildkern geschlossen)
```

---

## 14. Konsequenz für Objekt X.3

Der algebraische Hochschildkern der Schicht X.3 ist geschlossen:

$$[D_g] \neq 0 \in HH^1(A,M)_g,$$

$$[\Theta^\wedge_{p_1,p_2,p_3}] \neq 0 \in HH^3(A,A)_1,$$

$$\boxed{[D_g] \smile [\Theta^\wedge_{p_1,p_2,p_3}] \neq 0 \in HH^4(A,M)_g.}$$

**Nicht** automatisch geschlossen:
- Zyklische oder periodisch-zyklische Verfeinerung
- KMS- bzw. Weil-Paarung
- Gamma- und Primzahlpotenzkopplung
- Hilbertraum- oder Operatorrealisierung
- Übrige Schichten des fünfgliedrigen Objekts X

Der Følner-Beweis ersetzt den ungültigen Baker-Schritt und die unnötig starke Vollquotientenforderung. Der volle Quotient $[A,M]$ darf als Nebenfrage offen bleiben; für den nichttrivialen Cup-Aufstieg genügt der positiv geschlossene partielle Quotient $C_{H;R}$.

---

**Commit-Referenz:** Nachfolger von 604e6c6 (NEU-217).  
**Nächster Knoten:** Objekt X.3 → zyklische/KMS-Verfeinerung oder Schicht X.4.
