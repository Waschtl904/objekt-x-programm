# NEU-211 — Nichtteilerfremder Faktorialaudit und geladene äußere Derivation

**Status:** [O-211-1] ✓[M], [O-211-2] ✓[M], [O-211-3] ✓[M], [O-211-4] ✓[M], [O-211-5] ✓[M]_neg; [O-211-6] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-210 ([O-210-5] ✓[M]_part, [O-210-6] ?[O])  
**Schließt:** [O-210-6a] ✓[M], [O-210-6b] ✓[M], [O-210-6c] ✓[M]_neg  
**Ziel:** Vollständiger nichtteilerfremder Generatoraudit; Nachweis der geladenen äußeren Derivation $D_g : A_{\mathrm{alg}} \to A_{C^*}$; Nichtinnerheitstest; Zieltypdiagnose; Zieltypbrücke als offener Flaschenhals

---

## 211.0 — Ausgangslage

NEU-210 hat den Faktorialkandidaten $Y_N = \mu_m X_N \mu_n^*$ im teilerfremden Sektor $(k,mn)=1$ vollständig positiv abgeschlossen. Offen blieb [O-210-6]: der nichtteilerfremde Sektor, der Nichtinnerheitstest und der Zieltyp.

NEU-211 schließt alle drei Teile. Das zentrale Ergebnis:

$$\boxed{\exists\, D_g : A_{\mathrm{alg}} \to A_{C^*}, \quad g = m/n \neq 1, \quad D_g \text{ geladen, nicht } A_{C^*}\text{-inner}.}$$

Der Kandidat liefert jedoch keine Klasse in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$, weil $D_g(A_{\mathrm{alg}}) \not\subseteq A_{\mathrm{alg}}$. Die offene Frage ist die Zieltypbrücke über ein intermediares Koeffizientenmodul.

---

## 211.A — Exakte nichtteilerfremde Formeln

**Setup.** Setze $Y_N := \mu_m X_N \mu_n^*$ und für einen Generator $\mu_k$:
$$d := (n,k), \quad n = d\,n_0, \quad k = d\,k_0, \quad (n_0,k_0)=1.$$

**BC-Nica-Relation:**
$$\boxed{\mu_n^*\mu_k = \mu_{k_0}\mu_{n_0}^*.} \tag{211.1}$$

**Transportoperatoren** auf $B_{C^*} \cong C(\widehat{\mathbb Z})$:
$$T_a(E_L) := E_{L/(L,a)}, \qquad \rho_d(E_L) := \mu_d E_L \mu_d^* = E_{dL}.$$

**Satz ([O-211-1]).** *Es gilt exakt:*
$$\boxed{[Y_N, \mu_k] = \mu_{mk_0}\bigl(T_{k_0}(X_N) - \rho_d(X_N)\bigr)\mu_{n_0}^*.} \tag{211.2}$$

**Beweis.** Erster Term:
$$Y_N\mu_k = \mu_m X_N\mu_n^*\mu_k = \mu_m X_N\mu_{k_0}\mu_{n_0}^* = \mu_{mk_0}T_{k_0}(X_N)\mu_{n_0}^*.$$
Zweiter Term: Mit $\mu_k = \mu_{k_0}\mu_d$ und $\mu_n^* = \mu_d^*\mu_{n_0}^*$ (da $n = dn_0$, $k = dk_0$):
$$\mu_k Y_N = \mu_{mk_0}\mu_d X_N \mu_d^*\mu_{n_0}^* = \mu_{mk_0}\rho_d(X_N)\mu_{n_0}^*.$$
Differenz ergibt (211.2). Für $d=1$: $\rho_1(X_N) = X_N$, Reduktion auf den teilerfremden Fall. $\square$

**Adjungierter Sektor.** Mit $e := (m,k)$, $m = em_0$, $k = ek_1$, $(m_0,k_1)=1$:
$$\boxed{[Y_N, \mu_k^*] = \mu_{m_0}\bigl(\rho_e(X_N) - T_{k_1}(X_N)\bigr)\mu_{nk_1}^*.} \tag{211.3}$$

Beide Generatorfamilien reduzieren sich auf denselben analytischen Kern $T_a(X_N) - \rho_d(X_N)$.

$$\boxed{[O\text{-}211\text{-}1] \quad \checkmark[M]}$$

---

## 211.B — Normkonvergenz des gemischten Transportdefekts

**Notation.** Mit $h_N(x) := X_N(x) = c_{\min(\nu(x),N)}$ wirken die Operatoren als:
$$(T_a h_N)(x) = h_N(ax), \tag{211.4}$$
$$(\rho_d h_N)(x) = \begin{cases} h_N(x/d), & x \in d\widehat{\mathbb Z},\\ 0, & x \notin d\widehat{\mathbb Z}. \end{cases} \tag{211.5}$$

**Satz ([O-211-2]).** *Der Normgrenzwert*
$$\boxed{G_{a,d} := \lim_{N\to\infty}\bigl(T_a(X_N) - \rho_d(X_N)\bigr) \in B_{C^*}} \tag{211.6}$$
*existiert für alle $a, d \ge 1$.*

**Beweis.** *Auf $d\widehat{\mathbb Z}$:* Schreibe $x = dy$. Dann
$$G_{a,d;N}(dy) = h_N(ady) - h_N(y).$$
Da $\nu(ady) - \nu(y)$ gleichmäßig durch $ad$ beschränkt ist (Faktorialband aus NEU-210), gilt für tiefe Schalen:
$$|G_{a,d;N}(dy)| \le c_{\nu(y)+ad} - c_{\nu(y)} = \log\left(\frac{\nu(y)+ad+2}{\nu(y)+2}\right) \longrightarrow 0.$$

*Außerhalb von $d\widehat{\mathbb Z}$:* Ist $x \notin d\widehat{\mathbb Z}$, so existiert ein Primteiler $p \mid d$ mit $v_p(x) < v_p(d)$. Dann $v_p(ax) \le v_p(a) + v_p(d) - 1$. Da $v_p((j+1)!) \to \infty$, existiert ein von $a,d$ abhängiger Index $J(a,d)$ mit $\nu(ax) < J(a,d)$ für alle $x \notin d\widehat{\mathbb Z}$. Damit stabilisiert $T_a(X_N)$ dort gleichmäßig; $\rho_d(X_N) \equiv 0$. In beiden Fällen konvergiert $G_{a,d;N}$ gleichmäßig, also in Norm. $\square$

$$\boxed{[O\text{-}211\text{-}2] \quad \checkmark[M]}$$

---

## 211.C — Vollständige geladene Derivation

**Satz ([O-211-3]).** *Die Abbildung*
$$D_g(e(r)) := 0,$$
$$D_g(\mu_k) := \mu_{mk_0}\, G_{k_0,d}\, \mu_{n_0}^*, \qquad d=(n,k),\; n=dn_0,\; k=dk_0,$$
$$D_g(\mu_k^*) := -\mu_{m_0}\, G_{k_1,e}\, \mu_{nk_1}^*, \qquad e=(m,k),\; m=em_0,\; k=ek_1,$$
*definiert eine wohldefinierte Derivation $D_g : A_{\mathrm{alg}} \to A_{C^*}$ mit geladenem Grad $g = m/n$.*

**Beweis.** Da jedes $\operatorname{ad}(Y_N)$ eine Derivation ist und sämtliche Generatorkommutatoren in Norm konvergieren (211.B und NEU-210.D), ist $D_g$ als gleichmäßiger Grenzwert von Derivationen eine Derivation. Die Homogenität folgt aus $Y_N \in (A_{C^*})_g$:
$$\boxed{D_g\bigl((A_{\mathrm{alg}})_h\bigr) \subseteq (A_{C^*})_{gh}.} \tag{211.8}$$
$\square$

$$\boxed{[O\text{-}211\text{-}3] \quad \checkmark[M]}$$

---

## 211.D — Nichtinnerheit durch Offdiagonaltest

**Satz ([O-211-4]).** *$D_g$ besitzt keinen Implementierer aus $A_{C^*}$:*
$$\boxed{D_g \notin \operatorname{Inn}(A_{\mathrm{alg}}, A_{C^*})_g.} \tag{211.11}$$

**Beweis.** Betrachte die kanonische Darstellung auf $\ell^2(\mathbb N^\times)$ und den (unbeschränkten) Diagonaloperator
$$H\delta_t := c_{\nu(t)}\delta_t.$$
Der formale Grenzimplementierer ist $W := \pi(\mu_m)H\pi(\mu_n)^*$ mit
$$W\delta_{nt} = c_{\nu(t)}\delta_{mt}. \tag{211.9}$$

Angenommen, $D_g(a) = [x,a]$ für ein $x \in A_{C^*}$ mit $T := \pi(x)$ beschränkt. Dann $[W-T, \pi(e(r))] = 0$ auf dem algebraischen Basisvektorraum. Da $\{\pi(e(r))\}_r$ die Basis trennt, hat $W-T$ keine Offdiagonaleinträge:
$$s \neq t \implies \langle \delta_s, (W-T)\delta_t \rangle = 0.$$
Da $m \neq n$: $mt \neq nt$, also
$$\langle \delta_{mt}, T\delta_{nt} \rangle = c_{\nu(t)}. \tag{211.10}$$
Wähle $t = L_j = (j+1)!$, dann $\nu(t) = j$ und
$$|\langle \delta_{mL_j}, T\delta_{nL_j}\rangle| = c_j = \log(j+2) \longrightarrow \infty.$$
Dies widerspricht $|\langle \delta_s, T\delta_t\rangle| \le \|T\|$. $\square$

**Methodische Bemerkung.** Dieser Offdiagonalbeweis ist schärfer auf den geladenen Fall zugeschnitten als der diagonale Iterationsbeweis aus NEU-204: Die unbeschränkten Gewichte erscheinen direkt als Matrixelemente zwischen den beiden Orbits $m\mathbb N^\times$ und $n\mathbb N^\times$.

$$\boxed{[O\text{-}211\text{-}4] \quad \checkmark[M]}$$

---

## 211.E — Algebraischer Zieltyp scheitert

**Satz ([O-211-5]).** *$D_g(A_{\mathrm{alg}}) \not\subseteq A_{\mathrm{alg}}$; der Kandidat liefert keine Klasse in $HH^1(A_{\mathrm{alg}}, A_{\mathrm{alg}})_g$.*

**Beweis.** Wähle eine Primzahl $\ell \nmid mn$. Dann gilt im teilerfremden Fall:
$$D_g(\mu_\ell) = \mu_{m\ell}\, B_\ell\, \mu_n^*, \qquad B_\ell := \lim_N(T_\ell(X_N) - X_N).$$
Mit $B_\ell(0) = 0$: Wähle $x_j := (j+2)!/\ell$ für $\ell \mid j+2$. Dann $\nu(x_j) = j$, $\nu(\ell x_j) = j+1$, also
$$B_\ell(x_j) = c_{j+1} - c_j \neq 0, \qquad x_j \longrightarrow 0 \text{ in } \widehat{\mathbb Z}.$$
Daher ist $B_\ell$ in keiner Umgebung von $0$ konstant:
$$\boxed{B_\ell \notin B_{\mathrm{alg}}.} \tag{211.12}$$
Wäre $D_g(\mu_\ell) \in A_{\mathrm{alg}}$, so folgte $B_\ell = \mu_{m\ell}^* D_g(\mu_\ell)\mu_n \in A_{\mathrm{alg}} \cap B_{C^*} = B_{\mathrm{alg}}$, Widerspruch:
$$\boxed{D_g(\mu_\ell) \notin A_{\mathrm{alg}}.} \tag{211.13}$$
$\square$

**Korrekter positiver Typ:**
$$\boxed{[D_g] \in HH^1(A_{\mathrm{alg}}, A_{C^*})_g.}$$

$$\boxed{[O\text{-}211\text{-}5] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 211.F — Zieltypbrücke: offener Flaschenhals

**[O-211-6] ?[O] — Intermediares Koeffizientenmodul.**

Gesucht ist ein Zwischenraum
$$A_{\mathrm{alg}} \subsetneq \mathcal A^\infty \subsetneq A_{C^*},$$
der folgende Eigenschaften gleichzeitig trägt:

1. **$D_g$-Stabilität:** $D_g(A_{\mathrm{alg}}) \subseteq \mathcal A^\infty$.
2. **Cup-Kompatibilität:** In $HH^\bullet(A_{\mathrm{alg}}, \mathcal A^\infty)_g$ existiert ein typkorrekter Cup-Pfeil nach $HH^4_g$.
3. **Analytische Kontrolle:** $\mathcal A^\infty$ ist hinreichend gut definiert (z.B. als Schnitt mit dem Domänenraum eines Diracoperators, als Sobolev-Algebra, oder als glatte Algebra im Sinne von Connes).

Natürliche Kandidaten:
- **Harmonische Analyse auf $\widehat{\mathbb Z}$:** $\mathcal A^\infty$ als Schwartz-Algebra (Koeffizienten mit schnellem Abfall unter allen Primderivationen).
- **Faktorialglättung:** Funktionen, die auf $L_j\widehat{\mathbb Z}$ polynomial in $j$ sind.
- **Spektraltriple-Ansatz:** Domäne eines Diracoperators $\partial$ auf der BC-Algebra, der mit der faktorialen Tiefenfunktion $\nu$ verträglich ist.

$$\boxed{[O\text{-}211\text{-}6] \quad ?[O]}$$

---

## 211.G — Gesamtbefund und Positionierung

$$\boxed{\begin{aligned}
&\text{NEU-204: neutrale, analytische, äußere Derivation existiert.}\\
&\text{NEU-211: geladene, analytische, äußere Derivation existiert.}
\end{aligned}}$$

Der Faktorialkandidat $Y_N = \mu_m X_N\mu_n^*$ liefert:
- $D_g : A_{\mathrm{alg}} \to A_{C^*}$ wohldef., geladen, nicht $A_{C^*}$-inner.
- Kein Implementierer in $A_{C^*}$ (Offdiagonaltest).
- Kein algebraischer Zieltyp ($B_\ell \notin B_{\mathrm{alg}}$).
- Offene Brücke: intermediares $\mathcal A^\infty$ und Cup-Pfeil nach $HH^4_g$.

Der nächste Knoten (NEU-212) sollte nicht mehr versuchen, eine geladene Derivation zu konstruieren — dieser Teil ist abgeschlossen. Er sollte die Zieltypbrücke und die Wahl von $\mathcal A^\infty$ untersuchen.

---

## 211.H — Strukturbilanz

| Knoten | Status | Inhalt |
|---|---|---|
| [O-211-1] | ✓[M] | Exakte nichtteilerfremde Formeln (211.2), (211.3) via BC-Nica-Relation |
| [O-211-2] | ✓[M] | $G_{a,d} = \lim_N(T_a(X_N)-\rho_d(X_N)) \in B_{C^*}$ normkonvergent |
| [O-211-3] | ✓[M] | $D_g : A_{\mathrm{alg}} \to A_{C^*}$, geladen, wohldef. Derivation |
| [O-211-4] | ✓[M] | Nichtinnerheit: Offdiagonaltest mit Matrixelementen $c_j \to \infty$ |
| [O-211-5] | ✓[M]_neg | $B_\ell \notin B_{\mathrm{alg}}$; kein algebraischer Zieltyp; $[D_g] \in HH^1(A_{\mathrm{alg}},A_{C^*})_g$ |
| [O-211-6] | ?[O] | Intermediares $\mathcal A^\infty$, Cup-Pfeil $\to HH^4_g$, Zieltypbrücke |

---

## 211.I — DAG-Stand

```
[O-210-6] ?[O]
      |
      +---> [O-211-1] ✓[M]      BC-Nica: μ_n*μ_k = μ_{k0}μ_{n0}*, exakte Formeln
      |
      +---> [O-211-2] ✓[M]      G_{a,d} = lim T_a(X_N) - ρ_d(X_N) ∈ B_{C*}
      |
      +---> [O-211-3] ✓[M]      D_g : A_alg → A_{C*}, geladen, Derivation
      |
      +---> [O-211-4] ✓[M]      Nichtinnerheit (Offdiagonaltest)
      |
      +---> [O-211-5] ✓[M]_neg  B_ℓ ∉ B_alg; [D_g] ∈ HH^1(A_alg, A_{C*})_g
      |
      +---> [O-211-6] ?[O]       Zieltypbrücke: A_alg ⊂ A^∞ ⊂ A_{C*},
                                 D_g(A_alg) ⊆ A^∞, Cup → HH^4_g
                                 (neuer Haupt-Flaschenhals)
```
