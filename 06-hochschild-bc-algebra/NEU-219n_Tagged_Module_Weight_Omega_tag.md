# NEU-219n — Orbit-markiertes KMS-Modulgewicht und Audit der Multiplikatorwirkung

## 0. Ergebnis

Es sei
$$
R = \widetilde{A}_{\mathrm{alg}}, \qquad N_0 = RM_0R, \qquad \mathcal{N}_{\mathrm{tag}} = \bigoplus_{k\in\mathbb{Z}}^{\mathrm{alg}} N_0\delta_k,
$$
mit
$$
\tau = \operatorname{Ad}(U_g)\circ\widetilde{\sigma}_\beta,
$$
$$
r\cdot(x\delta_k)\cdot s = \tau^{-k}(r)\,x\,\tau^{-k}(s)\,\delta_k, \qquad T(x\delta_k) = x\delta_{k+1}.
$$

Das korrekte Basismodulgewicht ist
$$
\boxed{\varpi_{\beta,\chi}(x) = \widetilde{\omega}_{\beta,\chi}(U_{g^{-1}}x)},
$$
und die Eigenfamilie auf der markierten Orbitsumme lautet
$$
\boxed{\Omega_\lambda\!\left(\sum_k x_k\delta_k\right) = \sum_k \lambda^k\,\varpi_{\beta,\chi}(x_k), \qquad \lambda\in\mathbb{C}^\times.}
$$

Sie erfüllt
$$
\boxed{\Omega_\lambda(\eta\cdot a) = \Omega_\lambda(\tau(a)\cdot\eta)}
$$
und
$$
\boxed{\Omega_\lambda(T\eta) = \lambda\,\Omega_\lambda(\eta)}.
$$

Für die verlangte Shift-Eigenrelation $\Omega(T\eta) = g^{-\beta}\Omega(\eta)$ ist daher
$$
\boxed{\lambda = g^{-\beta}, \qquad c_k = g^{-k\beta}}.
$$

Damit gilt
$$
[O\text{-}219\text{-}5e1g\text{-tagged-module-weight}] \quad \checkmark[K/M].
$$

Die endgültige zyklische Orientierung des Eigenwerts bleibt offen.

---

## 1. Negativaudit des vorgeschlagenen Funktionals $\varphi_\beta\circ\Phi$

Der Kandidat $\omega = \varphi_\beta\circ\Phi$, $\Phi: N_0\to R$, ist im bisherigen DAG nicht konstruiert.

### 1.1 Keine kanonische bedingte Erwartung $N_0\to R$

Der Raum $N_0 = RM_0R$ ist ein $R$-Bimodul bzw. Koeffizientenunterraum, nicht eine etablierte $C^*$-Unteralgebra von $R$. Der Ausdruck \u201ebedingte Erwartung $\Phi: N_0\to R$\u201c ist nicht automatisch typisiert. Eine bedingte Erwartung ist insbesondere keine formale Folge der Sättigung $N_0 = RM_0R$.

### 1.2 Die Formel $rms\mapsto r\varphi_M(m)s$ ist nicht wohldefiniert

Ein Element von $N_0$ besitzt im Allgemeinen viele Darstellungen als endliche Summe $\sum_\nu r_\nu m_\nu s_\nu$. Damit $\Phi(rms) = r\varphi_M(m)s$ auf $N_0$ wohldefiniert wäre, müsste zunächst ein ausgeglichenes Funktional $\varphi_M: M_0\to\mathbb{C}$ konstruiert und bewiesen werden, das sämtliche Tensor- und Bimodulrelationen respektiert. Ein solches Funktional gehört nicht zum bisher bewiesenen Stand.

### 1.3 Kein etabliertes Element $1_M$

Der Koeffizientenmodul $M_0 = j_M(M)$ ist nicht als unitale Algebra mit einem Element $1_M$ definiert. Die Normierung $\varphi_M(1_M) = 1$ ist daher untypisiert.

### 1.4 Keine Eindeutigkeit bei $\beta > 1$

Im Bost\u2013Connes-Pfad werden für $\beta > 1$ extremale KMS-Zustände $\omega_{\beta,\chi}$ verwendet. Es liegt eine $\chi$-abhängige Familie vor, keine im bisherigen Stand bewiesene eindeutige skalare KMS-Auswertung. Das korrekte Funktional muss den Parameter $\chi$ bewahren.

### 1.5 Falsche Nichtverschwindensbehauptung

Selbst ein treues positives Funktional erfüllt nicht $x\neq 0\Rightarrow\omega(x)\neq 0$ für beliebige nichtpositive $x$. Die Nichtverschwindung muss am konkreten Cup-Zeugen bewiesen werden, nicht allgemein.

---

## 2. Das korrekte Basismodulgewicht

Setze $u := U_{g^{-1}}$. Da $u\in M(\widetilde{A})$ und $x\in\widetilde{A}$ impliziert $ux\in\widetilde{A}$, ist die folgende Definition auf $N_0$ typkorrekt:

$$
\boxed{\varpi_{\beta,\chi}(x) = \widetilde{\omega}_{\beta,\chi}(U_{g^{-1}}x)}.
$$

Das KMS-Gewicht $\widetilde{\omega}_{\beta,\chi}$ erfüllt
$$
\widetilde{\omega}_{\beta,\chi}(ab) = \widetilde{\omega}_{\beta,\chi}(\widetilde{\sigma}_\beta(b)\,a).
$$

**Satz 2.1 — Modulare Bimodulidentität.** Für $x\in N_0$, $a\in R$ gilt
$$
\boxed{\varpi_{\beta,\chi}(xa) = \varpi_{\beta,\chi}(\tau(a)x)}.
$$

*Beweis.* Da $u\tau(a) = \widetilde{\sigma}_\beta(a)\,u$, folgt
$$
\begin{aligned}
\varpi_{\beta,\chi}(xa) &= \widetilde{\omega}_{\beta,\chi}(uxa) \\
&= \widetilde{\omega}_{\beta,\chi}(\widetilde{\sigma}_\beta(a)\,ux) \\
&= \widetilde{\omega}_{\beta,\chi}(u\tau(a)x) \\
&= \varpi_{\beta,\chi}(\tau(a)x). \quad\square
\end{aligned}
$$

**Satz 2.2 — $\tau$-Invarianz.**
$$
\boxed{\varpi_{\beta,\chi}(\tau(x)) = \varpi_{\beta,\chi}(x)}.
$$
Dies folgt aus $u\tau(x) = \widetilde{\sigma}_\beta(x)\,u$ und der inversen KMS-Relation. $\square$

---

## 3. Eigenfamilie auf der markierten Orbitsumme

$$
\boxed{\Omega_\lambda\!\left(\sum_{k\in F} x_k\delta_k\right) = \sum_{k\in F} \lambda^k\,\varpi_{\beta,\chi}(x_k)}, \qquad F\subset\mathbb{Z}\text{ endlich}.
$$

**Satz 3.1 — Modulare Relation.** Für $a\in R$ und $\eta\in\mathcal{N}_{\mathrm{tag}}$ gilt
$$
\boxed{\Omega_\lambda(\eta\cdot a) = \Omega_\lambda(\tau(a)\cdot\eta)}.
$$

*Beweis.* Für $\eta = x\delta_k$:
$$
\begin{aligned}
\Omega_\lambda(\eta\cdot a) &= \lambda^k\,\varpi_{\beta,\chi}(x\,\tau^{-k}(a)) \\
&= \lambda^k\,\varpi_{\beta,\chi}(\tau^{1-k}(a)\,x) \\
&= \Omega_\lambda(\tau(a)\cdot\eta). \quad\square
\end{aligned}
$$

**Satz 3.2 — Shift-Eigenwert.**
$$
\boxed{\Omega_\lambda(T\eta) = \lambda\,\Omega_\lambda(\eta)}.
$$

*Beweis.* $\Omega_\lambda(T(x\delta_k)) = \Omega_\lambda(x\delta_{k+1}) = \lambda^{k+1}\varpi_{\beta,\chi}(x) = \lambda\cdot\lambda^k\varpi_{\beta,\chi}(x) = \lambda\,\Omega_\lambda(x\delta_k)$. $\square$

---

## 4. Exakte Rekursion der Gewichte

Für $\Omega(\sum_k x_k\delta_k) = \sum_k c_k\,\varpi_{\beta,\chi}(x_k)$ gilt
$$
\Omega(T\eta) = q\,\Omega(\eta)
$$
genau dann, wenn $c_{k+1} = q\,c_k$, also $c_k = c_0\,q^k$.

Unter $c_0 = 1$ und $q = g^{-\beta}$:
$$
\boxed{c_k = g^{-k\beta}}.
$$

**Bemerkung.** Die modulare Bimodulidentität allein erzwingt die $c_k$ nicht; die Rekursion folgt erst aus der zusätzlich festgelegten Shift-Eigenrelation $\Omega\circ T = g^{-\beta}\Omega$.

---

## 5. Keine Faktorisierung durch die Summenabbildung

Setze $\Sigma(\sum_k x_k\delta_k) = \sum_k x_k$. Dann gilt:

$$
\Omega_\lambda \text{ faktorisiert durch }\Sigma \quad\Longleftrightarrow\quad \lambda = 1.
$$

*Beweis.* Für $\lambda = 1$ ist $\Omega_1 = \varpi_{\beta,\chi}\circ\Sigma$. Für $\lambda\neq 1$ wähle $x$ mit $\varpi_{\beta,\chi}(x)\neq 0$. Dann $\Sigma(x\delta_0) = x = \Sigma(x\delta_1)$, aber
$$
\Omega_\lambda(x\delta_0) = \varpi_{\beta,\chi}(x) \neq \lambda\,\varpi_{\beta,\chi}(x) = \Omega_\lambda(x\delta_1).
$$
Insbesondere faktorisiert $\Omega_{g^{-\beta}}$ für $g\neq 1$ nicht durch $\Sigma$. $\square$

---

## 6. Nichtverschwindung nur am konkreten Cup-Zeugen

Sei $\eta_{\mathrm{cup}}\in I_{k_0}$ der markierte Lift der neutralisierten Cup-Auswertung und $x_{\mathrm{cup}} = \Pi_{k_0}(\eta_{\mathrm{cup}})\in N_0$. Dann wird gefordert:

$$
\boxed{\Omega_{g^{-\beta}}(\eta_{\mathrm{cup}}) = \lambda^{k_0}\,\widetilde{\omega}_{\beta,\chi}(U_{g^{-1}}x_{\mathrm{cup}}) \neq 0.}
$$

Es wird **nicht** behauptet, dass $\Omega_\lambda$ auf jedem nichtnullen Element nicht verschwindet. Die Nichtverschwindung ist am konkreten Cup-Zeugen zu verifizieren.

---

## 7. Audit des vorgeschlagenen Knotens \u201e$U_{g^{-1}}$ wirkt als $T^{-1}$\u201c

Vorgeschlagen war $U_{g^{-1}}\cdot(x\delta_k) \stackrel{?}{=} \tau^{-1}(x)\delta_{k-1}$. Diese Identität ist **falsch**.

Die linke $R$-Wirkung auf der $k$-ten Komponente ist
$$
r\cdot(x\delta_k) = \tau^{-k}(r)\,x\,\delta_k.
$$
Erweitert auf geeignete Multiplikatoren:
$$
m\cdot(x\delta_k) = \tau^{-k}(m)\,x\,\delta_k.
$$
Für $m = U_{g^{-1}}$ gilt $\tau(U_{g^{-1}}) = g^{-\beta}U_{g^{-1}}$, also $\tau^{-k}(U_{g^{-1}}) = g^{k\beta}U_{g^{-1}}$. Daher:
$$
\boxed{U_{g^{-1}}\cdot(x\delta_k) = g^{k\beta}\,U_{g^{-1}}x\,\delta_k.}
$$

Die Multiplikatorwirkung **erhält den Orbitindex** $k$. Da $U_{g^{-1}}N_0\subseteq N_0$ (wegen $U_{g^{-1}}R\subseteq R$), ist dies intern wohldefiniert.

Der externe Shift $T^{-1}(x\delta_k) = x\delta_{k-1}$ ändert dagegen den Orbitindex. Daher:
$$
\boxed{\text{\u201eMultiplikation mit }U_{g^{-1}}\text{ wirkt als }T^{-1}\text{\u201c} \quad \checkmark[M]_{\mathrm{neg}}.}
$$

---

## 8. Revidierter DAG-Status

| Knoten | Status |
|--------|--------|
| `5e1e-corner-core` | \u2713[K/M] |
| `5e1f-orbit-directness` | \u2713[M]\_neg |
| globale $\Pi$-Injektivität | \u2713[M]\_neg |
| orbit-markierte Realisierung $\mathcal{N}_{\mathrm{tag}}$ | \u2713[K/M] |
| Basismodulgewicht $\varpi_{\beta,\chi}(x) = \widetilde{\omega}_{\beta,\chi}(U_{g^{-1}}x)$ | \u2713[K/M] |
| Eigenfamilie $\Omega_\lambda$ | \u2713[K/M] |
| `5e1g-tagged-module-weight` | \u2713[K/M] |
| $c_k = g^{-k\beta}$ unter $\Omega\circ T = g^{-\beta}\Omega$ | \u2713[M] |
| Kandidat $\varphi_\beta\circ\Phi$ | nicht konstruiert; verworfen |
| $U_{g^{-1}} = T^{-1}$ auf $\mathcal{N}_{\mathrm{tag}}$ | \u2713[M]\_neg |
| natürliche komponentenweise Multiplikatorwirkung | \u2713[K/M] |
| endgültige zyklische Orientierung | ?[O] |

---

## 9. Nächster atomarer Knoten

$$
\boxed{[O\text{-}219\text{-}5e1h\text{-tagged-cyclic-orientation}]}
$$

Zu berechnen ist der modulwertige zyklische oder parazyklische Operator auf dem markierten Cup-Kozykel. Für $\Phi_\lambda = \widehat{\Omega}_\lambda\circ\widetilde{L}$ muss die einmalige Rotation vollständig verfolgt werden:

1. Inverser KMS-Twist $\widetilde{\sigma}_\beta$
2. Konjugierter Twist $\tau$
3. Orbitshift $T$
4. Eigenwert $\lambda$
5. Ladungsfaktor $g^{-\beta}$
6. Vorzeichen in Grad vier

Erst diese Rechnung entscheidet, ob die endgültige zyklische Kompensation $\lambda = g^{-\beta}$ oder $\lambda = g^{\beta}$ (oder eine andere Orientierung) verlangt.
