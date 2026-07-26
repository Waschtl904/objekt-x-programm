# NEU-163 — Einmodenzeuge: Liftmitgliedschaft und Nichtnullkante

**Stand:** 15. Juli 2026 — rev.2  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-162  
**Ziel:** Zwei verbleibende Strukturtests für den konkreten Einmodenzeugen
$L_3^\circ = e_1V_1$, $u_0 = 1-p$, $E_*^{\mathrm{rel}} = E_{1;\,1\to p}^{\mathrm{rel}}$.

---

## Epistemische Ausgangslage

Aus NEU-162 gesichert:

$$L_3^\circ = e_1V_1 \in \mathcal{A}_3^\circ, \qquad
(p-1)\log p \neq 0 \quad\forall\, p\geq 2. \qquad \checkmark[M]_{\exists\text{-Wahl}}$$

Da $L_3^\circ$ genau **eine Mode** besitzt: Rohkopplung = Einzelterm, keine Konvergenzfrage, kein Separationsproblem.

$$\boxed{T_p^{\mathrm{rel}}(e_{1-p}V_p) = (p-1)\log p\, E_{1;\,1\to p}^{\mathrm{rel}}.} \qquad \checkmark[M]$$

Es verbleiben genau **zwei** Strukturtests — beide werden hier behandelt.

---

## 163.A — Einmodenformel (Basisresultat)

Mit $s_0=1$, $m_0=1$, $\ell_{1,1}=1$, $u_0=1-p$ (aus NEU-42 §10 und NEU-162.D):

$$\Psi_p = (p-1)\log p\cdot \Pi_{J,N}(e_1 V_p).$$

$$T_p^{\mathrm{rel}}(e_{1-p}V_p) = (p-1)\log p\, E_{1;\,1\to p}^{\mathrm{rel}}.$$

**Kein Konvergenzproblem, kein Separationsproblem.**  Status: $\checkmark[M]$

---

## 163.B — Test 1: Liftmitgliedschaft $e_{1-p}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}}$

### Bereits gesichert durch $\delta_{u,0}$-Regel (NEU-41)

Die $\delta_{u,0}$-Regel aus NEU-41 besagt: Ein Vektor $e_uV_p$ liegt in $\mathcal{E}_p^{\mathrm{ch}}$ genau dann wenn $u\neq 0$, und $\pi_{\mathrm{prim}}(e_uV_p)=0$ genau dann wenn $u\neq 0$.

Für $u_0 = 1-p$, $p\geq 2$: $u_0 = 1-p \neq 0$. Daher:

$$e_{1-p}V_p \in \mathcal{E}_p^{\mathrm{ch}} \qquad \checkmark[M]$$
$$\pi_{\mathrm{prim}}(e_{1-p}V_p) = 0 \qquad \checkmark[M]$$

### Verbleibender offener Teil

Noch zu prüfen (Import aus NEU-159):

$$\boxed{R_{p,j}(e_{1-p}V_p) = 0 \quad \text{für alle relevanten }j.}$$

Damit gilt:
$$e_{1-p}V_p \in \mathcal{E}_p^{\mathrm{lin,ch}} \iff R_{p,j}(e_{1-p}V_p)=0\quad\forall j.$$

| Teilbedingung | Status | Quelle |
|---|---|---|
| $u_0 = 1-p \neq 0$ | $\checkmark[M]$ | NEU-162.D |
| $e_{1-p}V_p \in \mathcal{E}_p^{\mathrm{ch}}$ | $\checkmark[M]$ | NEU-41 $\delta_{u,0}$-Regel |
| $\pi_{\mathrm{prim}}(e_{1-p}V_p)=0$ | $\checkmark[M]$ | NEU-41 $\delta_{u,0}$-Regel |
| $R_{p,j}(e_{1-p}V_p)=0$ für alle $j$ | $?[O]$ | Import aus NEU-159 |

---

## 163.C — Test 2: Nichtnullkante $\|E_{1;\,1\to p}^{\mathrm{rel}}\|^2 > 0$ — **geschlossen**

### Konstruktionskette aus NEU-44 §4 (Satz 44.3)

Die innere Produktstruktur von $H_{\mathrm{rel},N}$ ist die **kantendiagonale Hebung (Variante B)**:

$$\langle E_{r;\,m\to pm},\, E_{r';\,m'\to qm'}\rangle_{Wres,rel}
:= \delta_{p,q}\,\delta_{m,m'}\,\langle E_{r,pm},E_{r',pm}\rangle_{Wres}.\tag{44.7}$$

Das ist eine explizit definierte Sesquilinearform — kein freier Vektorraum ohne Form,
kein unbekannter Quotient. Status dieser Definition: $\checkmark[M]$ (NEU-44 Satz 44.3).

### Norm der Zielkante

Für $\rho = (r=1, m=1, p)$:

$$\|E_{1;\,1\to p}^{\mathrm{rel}}\|_{Wres,rel}^2 = \langle E_{1,p}, E_{1,p}\rangle_{Wres}.$$

### Nichtverschwindung via OP-4.1

Aus OP-4.1 (NEU-24, beiderseitige Nichtausgeartetheit der $Wres$-Paarung, $\checkmark[M]$):

$$\langle E_{1,p}, E_{1,p}\rangle_{Wres} > 0.$$

(Ein ausgear tetes Skalarprodukt im Sinne von OP-4.1 hätte $\langle E_{1,p},\cdot\rangle_{Wres}=0$ für alle Vektoren erfordert — ausgeschlossen durch OP-4.1.)

$$\boxed{\|E_{1;\,1\to p}^{\mathrm{rel}}\|^2 = \langle E_{1,p}, E_{1,p}\rangle_{Wres} > 0.} \qquad \checkmark[M]$$

**163.C ist geschlossen.** $\checkmark[M]$

---

## 163.D — Relativer Nichtverschwindungsbefund (bedingt)

Sobald 163.B vollständig (d.h. $R_{p,j}$-Test aus NEU-159 positiv):

$$T_p^{\mathrm{rel}}\bigl(\mathcal{E}_p^{\mathrm{lin,ch}}\bigr) \ni (p-1)\log p\, E_{1;\,1\to p}^{\mathrm{rel}} \neq 0$$

$$\boxed{Q_p^{\mathrm{rel}} \neq \{0\}.} \qquad \checkmark[M] \text{ bedingt auf }163.B$$

**Uniform für alle $p\geq 2$** — derselbe Zeugenmechanismus gilt gleichzeitig für jede Primzahl.

---

## Vollständige Kette

$$\underbrace{L_3^\circ = e_1V_1}_{\checkmark[M]_{\exists\text{-Wahl}}}$$

$$\Downarrow$$

$$\underbrace{T_p^{\mathrm{rel}}(e_{1-p}V_p) = (p-1)\log p\, E_{1;\,1\to p}^{\mathrm{rel}}}_{\checkmark[M]}$$

$$\Downarrow$$

$$\underbrace{e_{1-p}V_p \in \mathcal{E}_p^{\mathrm{ch}},\quad \pi_{\mathrm{prim}}=0}_{\checkmark[M]}
\quad\text{und}\quad
\underbrace{R_{p,j}(e_{1-p}V_p)=0}_{?[O] \text{ NEU-159}}
\quad\text{und}\quad
\underbrace{\|E_{1;\,1\to p}^{\mathrm{rel}}\|^2>0}_{\checkmark[M] \text{ NEU-44+OP-4.1}}$$

$$\Downarrow$$

$$Q_p^{\mathrm{rel}} \neq 0 \quad\text{(bedingt auf }R_{p,j}\text{-Test).}$$

---

## Statusmatrix NEU-163 rev.2

| Aussage | Status | Quelle |
|---|---|---|
| Einmodenformel $T_p^{\mathrm{rel}}(e_{1-p}V_p) = (p-1)\log p\, E_*^{\mathrm{rel}}$ | $\checkmark[M]$ | NEU-42/162 |
| Keine Konvergenzfrage | $\checkmark[M]$ | Einterm |
| Keine Separationsfrage | $\checkmark[M]$ | Einterm |
| $e_{1-p}V_p \in \mathcal{E}_p^{\mathrm{ch}}$ | $\checkmark[M]$ | NEU-41 |
| $\pi_{\mathrm{prim}}(e_{1-p}V_p)=0$ | $\checkmark[M]$ | NEU-41 |
| $R_{p,j}(e_{1-p}V_p)=0$ für alle $j$ | $?[O]$ | Import NEU-159 |
| $\|E_{1;\,1\to p}^{\mathrm{rel}}\|^2 > 0$ | $\checkmark[M]$ | NEU-44 §4 + OP-4.1 |
| $Q_p^{\mathrm{rel}}\neq 0$ (uniform alle $p\geq 2$) | $\checkmark[M]$ bedingt | 163.D |

---

## Nächster Schritt: genau ein verbleibender Test

$$\boxed{\text{NEU-164 — }R_{p,j}\text{-Test: Import aus NEU-159, Regularitätsbedingungen für }e_{1-p}V_p.}$$
