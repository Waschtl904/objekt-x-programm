# NEU-187 — Restriktionssatz für geladene äußere Derivationen und Gruppenalgebra-Reduktion (rev2)

## 187.0 — Ausgangslage

Sei $A := A_\mathbb{Q}^{\mathrm{alg}}$, $\Gamma = \mathbb{Q}_+^\times$,
$B := \mathbb{C}[\mathbb{Q}/\mathbb{Z}]$ (neutrale Unteralgebra).

Offener Knoten aus NEU-186:
$$[O\text{-}186\text{-}3b]: \quad HH^1(A,A)_g \neq 0 \quad \text{für ein } g \neq 1_\Gamma\,?$$

NEU-187 (a) beweist die Injektivität der Restriktionsabbildung (Satz 187.3),
(b) zeigt, dass die entstehende Gruppenalgebra-Kohomologie nichttrivial ist ([O-187-2] $\checkmark[M]$),
und (c) benennt die verbleibende Erweiterungsfrage als neuen Kernknoten [O-188].

---

## 187.A — Abschluss: Satz 186.1 im DAG

| Knoten | Inhalt | Status |
|---|---|---|
| [O-186-3a] | $a \mapsto u_g D_p(a)$ oder $D_p(a) u_g$, $g \neq 1_\Gamma$ | ✓[M]\_neg — Satz 186.1 (bikonditional) |

---

## 187.B — Generatorvariablen einer homogenen Derivation

Sei $\delta \in \operatorname{Der}_g(A,A)$. Setze:
$$x_r := \delta(e(r)) \in A_g, \qquad y_n := \delta(\mu_n) \in A_{gn}, \qquad z_n := \delta(\mu_n^*) \in A_{g/n}.$$

$\delta$ ist durch $(x_r, y_n, z_n)$ eindeutig bestimmt. Die Ableitungen der Relationen liefern Kompatibilitätsbedingungen; für Satz 187.3 werden die folgenden als **hinreichendes Constraint-Teilsystem** verwendet (nicht notwendig vollständig bezüglich aller Relationen (R1)–(R7)):

$$\text{(K1)} \quad x_{r+s} = x_r e(s) + e(r) x_s \qquad \text{[aus (R1)]}$$
$$\text{(K2)} \quad z_n \mu_n + \mu_n^* y_n = 0 \qquad \text{[aus (R2)]}$$
$$\text{(K3)} \quad y_{mn} = y_m \mu_n + \mu_m y_n \qquad \text{[aus (R6)]}$$
$$\text{(K4)} \quad x_s \mu_n + e(s) y_n = y_n e(ns) + \mu_n x_{ns} \qquad \text{[aus (R4)]}$$
$$\text{(K5)} \quad z_n e(s) + \mu_n^* x_s = x_{ns} \mu_n^* + e(ns) z_n \qquad \text{[aus adj. (R4)]}$$

---

## 187.C — Restriktionssatz

**Satz 187.3.** Sei $g \neq 1_\Gamma$. Die Restriktionsabbildung
$$\rho_g: HH^1(A,A)_g \longrightarrow HH^1(B,A)_g$$
ist injektiv.

*Beweis.* Sei $\delta \in \operatorname{Der}_g(A,A)$ mit $\delta|_B = \operatorname{ad}_{u_g}|_B$.
Setze $\delta' := \delta - \operatorname{ad}_{u_g}$. Dann $x_r := \delta'(e(r)) = 0$ für alle $r$.

**Schritt 1: $y_n = 0$.**
Aus (K4) mit $x_s = x_{ns} = 0$: $e(s) y_n = y_n e(ns)$.
Schreibe $y_n = \sum_{m/\ell = gn} c_{m,\ell,r}\, \mu_m e(r) \mu_\ell^*$ (Normalform).
Koeffizientenvergleich erzwingt $c_{m,\ell,r+(m-\ell n)s} = c_{m,\ell,r}$ für alle $s$.
Da $g \neq 1_\Gamma$ ist $m - \ell n \neq 0$; Surjektivität + endlicher Träger $\Rightarrow$ $c_{m,\ell,r} = 0$ (Satz 184.1 rev2). Also $y_n = 0$.

**Schritt 2: $z_n = 0$.** Analog aus (K5). $\square$

---

## 187.D — Reduktion auf Gruppenalgebra-Kozykel

Die Restriktionsabbildung reduziert [O-186-3b] auf $HH^1(B, A)_g$.

Fixiere $M_{m,n} := \mu_m B \mu_n^* \subseteq A_{m/n}$. Eine Derivation $\delta: B \to M_{m,n}$
hat die Form $\delta(e(s)) = \mu_m f_s \mu_n^*$. Die Leibnizregel liefert:
$$f_{s+t} = f_s e((n-m)t) + e(ms) f_t.$$

Setze $d := n - m$, $c_s := e(-ms) f_s$:
$$\boxed{c_{s+t} = c_s e(dt) + c_t.}$$

Dies ist eine **Gruppen-1-Kozykelgleichung** für $G := \mathbb{Q}/\mathbb{Z}$ mit Wirkung
$$\rho_d(t)(h) := h \cdot e(dt) \quad \text{(Multiplikation in } B\text{)}.$$

> **Hinweis:** $\rho_d(t) = e(dt)$ wirkt auf $B = \mathbb{C}[\mathbb{Q}/\mathbb{Z}]$ als Multiplikationsoperator,
> **nicht** als skalarer Charakter. Der Standardsatz über eindimensionale $G$-Moduln
> ($H^1(G, \chi) = 0$ für $\chi \neq 1$) ist hier **nicht anwendbar**.

Korandform (innere Derivation via $u = \mu_m h \mu_n^*$):
$$c_s = h(1 - e(ds)).$$

Zu klären:
$$[O\text{-}187\text{-}1]: \quad H^1(G, B_{\rho_d}) = 0 \quad \text{für } d \neq 0\,?$$

---

## 187.E — Fouriermodell und nichttriviale Kozykel

Setze $\widehat{G} = \widehat{\mathbb{Z}} \cong \prod_p \mathbb{Z}_p$ (Pontryagin-Duale). Unter der Fouriertransformation
$$B = \mathbb{C}[G] \cong \operatorname{LC}(\widehat{\mathbb{Z}})$$
entspricht $e(dt)$ dem Charakter $\chi_{dt}(x) := x(dt)$ und die Kozykelgleichung wird punktweise:
$$c_{s+t}(x) = c_s(x) \chi_{dt}(x) + c_t(x).$$

### Expliziter nichttrivialer Kozykel

Wähle eine Funktion $H: \widehat{\mathbb{Z}} \setminus \{0\} \to \mathbb{C}$, die lokal konstant, aber
in keiner Umgebung von $0$ fortsetzbar ist. Konkret: setze $U_k := k!\,\widehat{\mathbb{Z}}$ und
$$H(x) := k \quad \text{für } x \in U_k \setminus U_{k+1}.$$

Definiere:
$$c_t(x) := H(x)(1 - \chi_{dt}(x)) \quad (x \neq 0), \qquad c_t(0) := 0.$$

**$c_t \in B$:** Da $t$ endliche Ordnung hat, gilt $\chi_{dt}(x) = 1$ für $x$ in einer
offenen Umgebung von $0$ (d.h. für $x \in N!\,\widehat{\mathbb{Z}}$ für großes $N$).
Außerhalb dieser Umgebung nimmt $H$ endlich viele lokal konstante Werte an.
Also $c_t \in \operatorname{LC}(\widehat{\mathbb{Z}}) \cong B$.

**Kozykelrechnung:**
$$c_s \chi_{dt} + c_t = H(1-\chi_{ds})\chi_{dt} + H(1-\chi_{dt})
= H(\chi_{dt} - \chi_{d(s+t)} + 1 - \chi_{dt})
= H(1 - \chi_{d(s+t)}) = c_{s+t}. \checkmark$$

### Kein Korand

Angenommen $c_t = h(1-e(dt))$ für ein $h \in B$. Im Fouriermodell:
$$(H(x) - h(x))(1 - \chi_{dt}(x)) = 0 \quad \forall t.$$

Für jedes $x \neq 0$ ist die Multiplikation mit $d \neq 0$ auf $\widehat{\mathbb{Z}}$
injektiv, und die Charaktere aus $G$ trennen Punkte: es existiert $t$ mit $\chi_{dt}(x) \neq 1$.
Also $H(x) = h(x)$ für alle $x \neq 0$.
Aber $h \in B = \operatorname{LC}(\widehat{\mathbb{Z}})$ ist in einer Umgebung von $0$ konstant,
was der Konstruktion von $H$ widerspricht. $\square$

### Klassifikation

$$\boxed{H^1(G, B_{\rho_d}) \cong \frac{\operatorname{LC}(\widehat{\mathbb{Z}} \setminus \{0\})}{\operatorname{LC}(\widehat{\mathbb{Z}})\big|_{\widehat{\mathbb{Z}} \setminus \{0\}}}.}$$

Die Kohomologie misst lokal konstante Funktionen auf $\widehat{\mathbb{Z}} \setminus \{0\}$
(Keime mit Singularität bei $0$), die nicht aus einer global lokal konstanten Funktion
durch Einschränkung entstehen. Der Endlichkeitszusatz (jeder $c_t$ hat endlichen Fourierträger)
ist nicht eine technische Nebenbedingung, sondern die Quelle der Nichttrivialität.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-187-1] | $H^1(G, B_{\rho_d}) = 0$ für $d \neq 0$? | ✓[M]\_neg |
| [O-187-2] | $H^1(G, B_{\rho_d}) \neq 0$ für $d \neq 0$ | ✓[M] — expliziter nichttrivialer Kozykel + Klassifikation |

---

## 187.F — Erweiterungsfrage und nächster Knoten

Satz 187.3 liefert nur die **Injektion** $HH^1(A,A)_g \hookrightarrow HH^1(B,A)_g$,
nicht Surjektivität. Die gefundenen Klassen $[c] \in H^1(G, B_{\rho_{m,n}})$ müssen
zusätzlich die Erweiterungsgleichungen (K4) und (K5) für $\mu_k$ und $\mu_k^*$ erfüllen.

Der neue Kernknoten lautet:
$$[O\text{-}188]: \quad \text{Welche Klassen } [c] \in H^1(B, A)_g \text{ lassen eine Erweiterung}
\;(y_k, z_k)\text{ zu } \delta \in \operatorname{Der}_g(A,A) \text{ zu?}$$

| Knoten | Inhalt | Status |
|---|---|---|
| [O-187-1] | $H^1(G, B_{\rho_d}) = 0$? | ✓[M]\_neg |
| [O-187-2] | $H^1(G, B_{\rho_d}) \neq 0$ | ✓[M] |
| [O-188] | Erweiterungsobstruktion auf BC-Algebra | ?[O] → NEU-188 |
| [O-186-3] | $HH^1(A,A)_g \neq 0$? | ?[O] — abhängig von [O-188] |

---

## 187.G — DAG-Stand nach NEU-187

```
[O-186-3a]   ✓[M]_neg   u_g⋅D_p bikonditional (Satz 186.1)
[O-187-1]    ✓[M]_neg   H¹(Q/Z, B_{ρ_d}) = 0? — nein
[O-187-2]    ✓[M]       H¹(Q/Z, B_{ρ_d}) ≠ 0 (explizit + Klassifikation)
[O-188]      ?[O]       Erweiterungsobstruktion → NEU-188
[O-186-3]    ?[O]       HH¹(A,A)_g ≠ 0?  abhängig von [O-188]
[O-186-0]    ?[O]       HH⁴(A,A)_ch ≠ 0?
```
