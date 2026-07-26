# NEU-219m — Negativaudit der Orbit-Direktheit und orbit-markierte Ersatzrealisierung

## 0. Ausgangslage

Es sei
$$
R := \widetilde{A}_{\mathrm{alg}}, \qquad B := eRe = j_A(A_{\mathrm{alg}}),
$$
und
$$
\tau = \operatorname{Ad}(U_g) \circ \widetilde{\sigma}_\beta, \qquad e_k = \tau^k(e) = \gamma_{g^k}(e),
$$
$$
A_k = e_k R e_k, \qquad M_k = \tau^k(M_0), \qquad M_0 := j_M(M),
$$
$$
I_k := R e_k \otimes_{A_k} M_k \otimes_{A_k} e_k R, \qquad N_k := R M_k R.
$$

Nach NEU-219l ist für jedes $k$
$$
\Pi_k : I_k \xrightarrow{\cong} N_k
$$
die durch Multiplikation induzierte $R$-Bimodulisomorphie.

Zu auditieren ist der vorgeschlagene positive Schluss
$$
\sum_{k \in \mathbb{Z}} N_k \stackrel{?}{=} \bigoplus_{k \in \mathbb{Z}}^{\mathrm{alg}} N_k.
$$

## 1. Ergebnis

Der vorgeschlagene Direktheitsbeweis ist **falsch**. Tatsächlich gilt das stärkere negative Resultat:

$$
\boxed{N_k = N_0 \qquad \text{für alle } k \in \mathbb{Z}.}
$$

Folglich ist die globale Multiplikationsabbildung
$$
\Pi : \bigoplus_{k \in \mathbb{Z}}^{\mathrm{alg}} I_k \longrightarrow \widetilde{\mathcal{A}}^{\log}, \qquad (\xi_k)_k \longmapsto \sum_k \Pi_k(\xi_k),
$$
nicht injektiv, sofern $M \neq 0$.

Damit werden geschlossen:
$$
[O\text{-}219\text{-}5e1f\text{-orbit-directness}] \quad \checkmark[M]_{\mathrm{neg}},
$$
$$
[O\text{-}219\text{-}5e1d3] \quad \checkmark[M]_{\mathrm{neg}}.
$$

Die abstrakte Orbitsumme bleibt typkorrekt; ausgeschlossen ist nur ihre unmarkierte Multiplikationsrealisierung in einem einzigen Exemplar von $\widetilde{\mathcal{A}}^{\log}$.

---

## 2. Erster Fehler: Die adelischen Ecken sind nicht disjunkt

Für $g = p$ prim gilt
$$
\gamma_{p^k}(e) = \mathbf{1}_{p^k \widehat{\mathbb{Z}}}.
$$

Für alle $j, k \in \mathbb{Z}$ gilt
$$
p^j \widehat{\mathbb{Z}} \cap p^k \widehat{\mathbb{Z}} = p^{\max(j,k)} \widehat{\mathbb{Z}}.
$$

Daher
$$
\boxed{e_j e_k = e_{\max(j,k)} \neq 0.} \tag{2.1}
$$

Die Gitter $p^k \widehat{\mathbb{Z}}$ sind nicht scharf getrennt, sondern vollständig **verschachtelt**:
$$
j < k \quad \Longrightarrow \quad p^k \widehat{\mathbb{Z}} \subsetneq p^j \widehat{\mathbb{Z}}.
$$

Die Behauptung $p^j \widehat{\mathbb{Z}} \cap p^k \widehat{\mathbb{Z}} = \varnothing$ für $j \neq k$ ist somit falsch.

**Expliziter Gegenzeuge.** Setze $x = e_k = \gamma_{p^k}(\iota(1))$. Dann gilt für $j \neq k$:
$$
e_j e_k e_j = e_{\max(j,k)} \neq 0.
$$

Für allgemeines $g \in \mathbb{Q}_+^\times$ gilt entsprechend
$$
\mathbf{1}_{g^j \widehat{\mathbb{Z}} \cap g^k \widehat{\mathbb{Z}}} = \mathbf{1}_{(g^j \vee g^k)\widehat{\mathbb{Z}}} \neq 0.
$$

---

## 3. Zweiter Fehler: Die transformierte Kompressionsformel hat die falsche Orientierung

Da $e_j = \gamma_{g^j}(e)$, gilt für jedes geeignete $x$:
$$
\boxed{e_j x e_j = \gamma_{g^j}\!\left(e\,\gamma_{g^{-j}}(x)\,e\right).} \tag{3.1}
$$

Für $x = \gamma_{g^k r}(\iota(f)) U_s$ folgt
$$
\gamma_{g^{-j}}(x) = \gamma_{g^{k-j} r}(\iota(f)) U_s,
$$
also
$$
\boxed{e_j x e_j = \gamma_{g^j}\!\left(e\,\gamma_{g^{k-j}r}(\iota(f))U_s\,e\right).} \tag{3.2}
$$

Die vorgeschlagene Formel mit äußerem $\gamma_{g^{-j}}$ und Parameter $g^{j-k}r$ ist doppelt orientierungsverkehrt.

Außerdem ist die Aussage
$$
g^{j-k}r \notin \widehat{\mathbb{Z}}^\times \quad \Longrightarrow \quad e\,\gamma_{g^{j-k}r}(\iota(f))U_s\,e = 0
$$
kein zulässiges Kriterium. Die Kompressionsformel aus NEU-219l erlaubt beliebige positive rationale Parameter; Nichtintegralität erzwingt kein Verschwinden.

**Einfaches Gegenbeispiel.** Für $r = p^{-1}$, $s = 1$, $f = 1$ gilt
$$
e\,\gamma_{p^{-1}}(e)\,e = e,
$$
weil $\widehat{\mathbb{Z}} \subset p^{-1}\widehat{\mathbb{Z}}$. Der Parameter $p^{-1}$ ist keine Einheit von $\widehat{\mathbb{Z}}$, die Kompression ist dennoch maximal nichtnull.

---

## 4. Dritter Fehler: $N_k$ ist kein Eckmodul

Nur der Ausgangskoeffizientenmodul erfüllt $M_k = e_k M_k e_k$. Nach der $R$-Sättigung $N_k = R M_k R$ gilt im Allgemeinen gerade **nicht**
$$
N_k \subseteq e_k \widetilde{\mathcal{A}}^{\log} e_k
$$
und ebenso wenig $e_k x e_k = x$ für $x \in N_k$.

Daher wäre selbst aus hypothetischen Relationen $e_j N_k e_j = 0$ für $j \neq k$ nicht der behauptete Schritt
$$
x_j = e_j\Bigl(\sum_k x_k\Bigr)e_j
$$
zulässig. Man hätte lediglich $e_j x_j e_j = 0$, nicht $x_j = 0$.

Die Gleichsetzung von $N_k = R M_k R$ mit einem in der Ecke $e_k$ getragenen Modul ist ein **Typfehler**.

---

## 5. Lokale Unität der gesättigten Module

**Lemma 5.1.** Jedes $N_k = R M_k R$ ist ein lokal unitärer $R$-Bimodul.

*Beweis.* Ein Element $x \in N_k$ ist eine endliche Summe $x = \sum_\nu r_\nu m_\nu s_\nu$ mit $r_\nu, s_\nu \in R$ und $m_\nu \in M_k$. Da $R$ zweiseitige lokale Einheiten besitzt, existiert $p \in R$ mit $p r_\nu = r_\nu$ und $s_\nu p = s_\nu$ für alle $\nu$. Dann $px = x = xp$. $\square$

---

## 6. Normalisiererlemma

**Lemma 6.1.** Sei $X$ ein lokal unitärer $R$-Unterbimodul und $u \in M(R)$ invertierbar mit $u R u^{-1} = R$. Dann gilt
$$
\boxed{u X u^{-1} = X.} \tag{6.1}
$$

*Beweis.* Sei $x \in X$. Nach lokaler Unität existiert $p \in R$ mit $px = x = xp$. Dann
$$
u x u^{-1} = (up)\,x\,(pu^{-1}).
$$
Aus $u R \subseteq R$ und $R u^{-1} \subseteq R$ folgt $up \in R$, $pu^{-1} \in R$, somit $u x u^{-1} \in R X R = X$. Mit $u^{-1}$ erhält man die Gegeninklusion. $\square$

**Korollar 6.2.** Für jedes $q \in \mathbb{Q}_+^\times$ gilt
$$
\boxed{\operatorname{Ad}(U_q)(N_0) = N_0.} \tag{6.2}
$$

---

## 7. Modularinvarianz von $N_0$

Der Modul $M_0 = j_M(M)$ ist $\Gamma$-graduiert. Da auch $R$ graduiert ist, ist $N_0 = R M_0 R$ ein graduierter $R$-Bimodul. Auf einem homogenen Element $x_h \in (N_0)_h$ wirkt
$$
\widetilde{\sigma}_\beta(x_h) = h^\beta x_h.
$$
Da $h^\beta \neq 0$, folgt
$$
\boxed{\widetilde{\sigma}_\beta(N_0) = N_0.} \tag{7.1}
$$

---

## 8. Alle Orbitbilder stimmen überein

**Satz 8.1.** Für jedes $k \in \mathbb{Z}$ gilt
$$
\boxed{N_k = N_0.} \tag{8.1}
$$

*Beweis.* Zunächst ist $\tau(R) = R$. Daher
$$
\begin{aligned}
N_k &= R M_k R \\
&= R \tau^k(M_0) R \\
&= \tau^k(R M_0 R) \\
&= \tau^k(N_0).
\end{aligned} \tag{8.2}
$$
Nach (6.2) und (7.1) gilt $\tau(N_0) = \operatorname{Ad}(U_g)(\widetilde{\sigma}_\beta(N_0)) = N_0$. Iteration liefert $\tau^k(N_0) = N_0$. Zusammen mit (8.2) folgt (8.1). $\square$

**Bemerkung 8.2.** Das Scheitern der Direktheit ist nicht durch eine kleine Überlappung verursacht. Die $R$-Sättigung entfernt die Orbitmarkierung vollständig: $N_j = N_k$ für alle $j, k$.

---

## 9. Globale Multiplikationsabbildung ist nicht injektiv

**Satz 9.1.** Angenommen $M \neq 0$. Dann ist $\Pi : \bigoplus_k^{\mathrm{alg}} I_k \to \widetilde{\mathcal{A}}^{\log}$ nicht injektiv.

*Beweis.* Da $M \neq 0$, ist $N_0 \neq 0$. Wähle $0 \neq x \in N_0$. Für zwei verschiedene Indizes $j \neq k$ sind
$$
\Pi_j \xrightarrow{\cong} N_j = N_0, \qquad \Pi_k \xrightarrow{\cong} N_k = N_0
$$
Isomorphismen. Definiere
$$
\xi_j := \Pi_j^{-1}(x) \in I_j, \qquad \xi_k := \Pi_k^{-1}(x) \in I_k.
$$
Da $I_j$ und $I_k$ verschiedene direkte Summanden sind, ist $\xi_j - \xi_k \neq 0$. Andererseits
$$
\Pi(\xi_j - \xi_k) = x - x = 0.
$$
Also ist $\Pi$ nicht injektiv. $\square$

**Korollar 9.2 — Exakte Kernbeschreibung.** Unter den komponentenweisen Isomorphismen $\bigoplus_k I_k \xrightarrow{\oplus \Pi_k} \bigoplus_k N_0 \delta_k$ entspricht $\Pi$ der Summenabbildung
$$
\Sigma : \bigoplus_k N_0 \delta_k \longrightarrow N_0, \qquad \sum_k x_k \delta_k \longmapsto \sum_k x_k.
$$
Daher
$$
\boxed{\ker \Pi \cong \left\{ (x_k)_k : \operatorname{supp}(x_k) \text{ endlich},\ \sum_k x_k = 0 \right\}.} \tag{9.1}
$$
Der Kern wird von den elementaren Differenzen $x \delta_j - x \delta_k$ ($x \in N_0$, $j \neq k$) linear erzeugt.

---

## 10. Eckkompressionen können keinen nichttrivialen gesättigten Modul annihilieren

**Satz 10.1.** Sei $X$ ein lokal unitärer $R$-Bimodul und $e_j$ ein volles Idempotent mit $R e_j R = R$. Dann gilt
$$
\boxed{e_j X e_j = 0 \quad \Longrightarrow \quad X = 0.} \tag{10.1}
$$

*Beweis.* Sei $x \in X$, wähle lokale Einheit $u \in R$ mit $ux = x = xu$. Aus der Vollheit: $u = \sum_i a_i e_j b_i$ und $u = \sum_\ell c_\ell e_j d_\ell$. Dann
$$
x = uxu = \sum_{i,\ell} a_i e_j(b_i x c_\ell) e_j d_\ell = 0. \quad \square
$$

Da jedes $e_j = \tau^j(e)$ voll ist und $N_k \neq 0$, folgt
$$
\boxed{e_j N_k e_j \neq 0 \qquad \text{für alle } j, k.} \tag{10.2}
$$

Die Eckkompressionen sind prinzipiell ungeeignet, die nichtnullen Orbitbilder $N_k$ voneinander zu separieren.

---

## 11. Orbit-markierte Ersatzrealisierung

Die abstrakte Orbitsumme besitzt eine kanonische externe Realisierung, welche den Index nicht vergisst. Setze
$$
\mathcal{N}_{\mathrm{tag}} := \bigoplus_{k \in \mathbb{Z}}^{\mathrm{alg}} N_0 \delta_k.
$$

Definiere
$$
\Psi_k := \tau^{-k} \circ \Pi_k : I_k \longrightarrow N_0
$$
und
$$
\Psi : \widetilde{M}_{\mathrm{orb}} \longrightarrow \mathcal{N}_{\mathrm{tag}}, \qquad \xi \in I_k \longmapsto \Psi_k(\xi)\,\delta_k.
$$

**Satz 11.1.**
$$
\boxed{\Psi : \widetilde{M}_{\mathrm{orb}} \xrightarrow{\cong} \mathcal{N}_{\mathrm{tag}}} \tag{11.1}
$$
ist ein Vektorraumisomorphismus und ein Isomorphismus für die getwisteten $R$-Bimodulstrukturen:
$$
r \cdot (x \delta_k) \cdot s = \tau^{-k}(r)\,x\,\tau^{-k}(s)\,\delta_k. \tag{11.2}
$$

*Beweis.* Jede $\Psi_k$ ist als Komposition zweier Isomorphismen bijektiv. Die Formel für die Wirkung folgt aus $\Pi_k(r\xi s) = r \Pi_k(\xi) s$ durch Anwendung von $\tau^{-k}$. $\square$

Die Orbitverschiebung wird zur reinen Indexverschiebung:
$$
T(x \delta_k) = x \delta_{k+1}. \tag{11.3}
$$
Sie erfüllt die Semilinearität
$$
T(r\eta s) = \tau(r)\,T(\eta)\,\tau(s). \tag{11.4}
$$

**Matrixrealisierung.** Die markierte Summe kann injektiv diagonal dargestellt werden:
$$
x \delta_k \longmapsto E_{kk} \otimes x
$$
in $M_{\mathrm{fin}}(\mathbb{Z}) \odot \widetilde{\mathcal{A}}^{\log}$, wobei die $R$-Wirkung durch den diagonalen Multiplikator
$$
\pi(r) = \sum_{k \in \mathbb{Z}} E_{kk} \otimes \tau^{-k}(r)
$$
implementiert wird (algebraisch wohldefiniert auf endlich unterstützten Vektoren).

---

## 12. Audit des vorgeschlagenen Morita-Folgeknotens

Der Ausdruck
$$
\widetilde{A}_{\mathrm{alg}} \cong j_A(A_{\mathrm{alg}}) \oplus_{\mathrm{Morita}} \widetilde{M}_{\mathrm{orb}}
$$
ist **kein standardmäßig typisierter Morita-Ausdruck**. Eine Morita-Äquivalenz ist keine direkte Summenzerlegung einer Algebra in eine Ecke und einen Koeffizientenmodul.

Der konkrete Morita-Kontext aus NEU-219l besteht aus $Re$, $eR$ und den Paarungen $Re \otimes_{eRe} eR \to R$ sowie $eR \otimes_R Re \to eRe$. Die noch offene Typbrücke betrifft nicht eine weitere algebraische Direktzerlegung, sondern die **Auswertung des orbit-markierten Koeffizientenmoduls**.

Der vorgeschlagene Folgeknoten wird als derzeit untypisiert zurückgewiesen.

---

## 13. Revidierter DAG-Status

| Knoten | Status |
|--------|--------|
| `[O-219-5e1e-corner-core]` | ✓[K/M] |
| Algebraische Vollheit $ReR = R$ | ✓[M] |
| Lokale Einheiten von $R$ | ✓[K/M] |
| Einzelne $\Pi_k : I_k \to N_k$ | ✓[K/M] |
| Ecken $e_j$ als Orbitseparator | ✓[M]_neg |
| `[O-219-5e1f-orbit-directness]` | ✓[M]_neg |
| `[O-219-5e1d3]`: globale $\Pi$-Injektivität | ✓[M]_neg |
| Orbit-markierte externe Realisierung $\mathcal{N}_{\mathrm{tag}}$ | ✓[K/M] |
| Unmarkierte Einbettung in $\widetilde{\mathcal{A}}^{\log}$ | ausgeschlossen |
| Genuines Modulgewicht auf $\mathcal{N}_{\mathrm{tag}}$ | ?[O] |

---

## 14. Nächster atomarer Knoten

$$
\boxed{[O\text{-}219\text{-}5e1g\text{-tagged-module-weight}]}
$$

**Aufgabe:** Konstruiere eine lineare Funktionalform
$$
\Omega_{\mathrm{tag}} : \bigoplus_{k \in \mathbb{Z}}^{\mathrm{alg}} N_0 \delta_k \longrightarrow \mathbb{C}
$$
oder eine äquivalente Matrixgewichtsauswertung mit folgenden Eigenschaften:

1. **Modulare Bimodulidentität.** Für die konkret benötigten $r, s \in R$ und $\eta \in \mathcal{N}_{\mathrm{tag}}$ muss eine exakt typisierte getwistete Relation gelten.

2. **Orbitkompensation.** Die Auswertung muss den Shift $T(x\delta_k) = x\delta_{k+1}$ mit der Gegenladung bzw. dem Faktor $g^{-\beta}$ kompatibel machen.

3. **Nichtverschwindende Cup-Auswertung.** Auf dem orbit-markierten Lift der bereits neutralisierten Fünffachauswertung darf $\Omega_{\mathrm{tag}}$ nicht verschwinden.

4. **Kein stilles Vergessen des Indexes.** Die Auswertung darf nicht durch die nichtinjektive Summenabbildung $\Sigma : \bigoplus_k N_0 \delta_k \to N_0$ faktorisieren, sofern dadurch die Ladungsobstruktion erneut entsteht.

Eine natürliche erste Kandidatenklasse ist
$$
\Omega_{\mathrm{tag}}\!\left(\sum_k x_k \delta_k\right) = \sum_k c_k\,\omega_k(x_k),
$$
wobei die Gewichte $c_k$ und Funktionale $\omega_k$ aus der Shift- und Modularrelation abzuleiten sind und nicht frei geraten werden dürfen.
