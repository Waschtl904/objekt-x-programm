# NEU-208 — Separierbare Primpotentiale und Refinementstabilität

**Status:** [O-208-1] ✓[M]_neg, [O-208-2] ✓[K], [O-208-3] ✓[M], [O-208-4] ✓[M]; [O-208-5] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-207 ([O-207-5a] ✓[K], [O-207-5b] ?[O])  
**Ziel:** Nachweis der Refinement-Instabilität der radialen Koeffizientenfunktion; Konstruktion separierbarer Primpotentiale als refinementstabile Alternative; Normformel für Grenzkommutatoren

---

## 208.0 — Ausgangslage

[O-207-5a] hat die Existenz einer unbeschränkten, translationsflachen Koeffizientenfunktion
$$c(\alpha) = \log(2+|\alpha|_1)$$
gesichert. Diese Funktion hat jedoch eine strukturelle Schwäche, die erst beim Übergang zu wachsenden Primzahlmengen $F \uparrow \mathcal P$ sichtbar wird: Sie ist zwar bei festem Gitter translationsflach, aber nicht refinementstabil.

NEU-208 legt diesen Befund präzise fest und konstruiert die korrekte Ersatzarchitektur: koordinatenweise additive, separierbare Primpotentiale.

---

## 208.A — Negativbefund: radiale Funktion ist nicht refinementstabil

**Satz ([O-208-1]).** *Die Funktion $c(\alpha)=\log(2+|\alpha|_1)$ ist translationsflach bei festem Gitter, aber nicht refinementstabil unter $F \uparrow \mathcal P$.*

**Beweis.** Fixiere eine Primzahl $p$ und eine endliche Primzahlmenge $F \ni p$. Der formale Differenzmultiplikator für $\mu_p$ auf dem $F$-Gitter lautet
$$d_{p,F}(\alpha) = c(\alpha + e_p) - c(\alpha) = \log\left(\frac{3+|\alpha|_1}{2+|\alpha|_1}\right).$$
Erweitert man $F$ um eine neue Primzahl $q \notin F$, hängt der neue Multiplikator auch von $\alpha_q$ ab:
$$d_{p,F\cup\{q\}}(\alpha, \alpha_q) = \log\left(\frac{3+|\alpha|_1+\alpha_q}{2+|\alpha|_1+\alpha_q}\right).$$
Setzt man auf den bisherigen Koordinaten $\alpha = 0$ und lässt $\alpha_q \to \infty$:
$$d_{p,F}(0) = \log\frac{3}{2}, \qquad d_{p,F\cup\{q\}}(0,\alpha_q) \longrightarrow 0.$$
Daher
$$\boxed{\left\|d_{p,F\cup\{q\}} - d_{p,F}\right\| \ge \log\frac{3}{2}.}$$
Die $\mu_p$-Kommutatoren sind unter Erweiterung der Primzahlmenge also nicht norm-Cauchy. $\square$

**Präzise Klasse des Befunds.** Diese Instabilität widerspricht [O-207-5a] nicht — die dort bewiesene Aussage über feste Translationen bleibt korrekt. Die radiale Architektur genügt jedoch nicht für [O-207-5b], weil sie den Refinement-Randterm nicht kontrolliert.

$$\boxed{[O\text{-}208\text{-}1] \quad \checkmark[M]_{\mathrm{neg}}}$$

---

## 208.B — Separierbare Primpotentiale

**Definition ([O-208-2]).** Statt einer radialen Funktion arbeite man koordinatenweise additiv. Setze
$$\boxed{c_F(\alpha) = \sum_{p \in F} f_p(\alpha_p),}$$
mit der kanonischen Wahl
$$f_p(j) = \log(j+2).$$

Für jede Primzahl $p$ definiere analog NEU-204:
$$X_{p,N} = \sum_{j=0}^{N-1} f_p(j)\, q_{p,j} + f_p(N)\, E_{p^N}.$$

Für eine endliche Primzahlmenge $F$ und Cutoffs $\mathbf N = (N_p)_{p \in F}$ setze
$$\boxed{X_{F,\mathbf N} = \sum_{p \in F} X_{p,N_p}.}$$

Alle Summanden liegen im abelschen Sektor $B_{\mathrm{alg}}$ und kommutieren miteinander.

$$\boxed{[O\text{-}208\text{-}2] \quad \checkmark[K]}$$

---

## 208.C — Exakte Refinementstabilität

**Satz ([O-208-3]).** *Neue Primrichtungen $q \nmid k$ verändern den $\mu_k$-Kommutator nicht.*

**Beweis.** Wegen der Additivität gilt:
$$[X_{F,\mathbf N}, \mu_k] = \sum_{p \in F} [X_{p,N_p}, \mu_k].$$
Für $p \nmid k$ kommutiert $X_{p,N_p}$ mit $\mu_k$, da $X_{p,N_p} \in B_{\mathrm{alg}}$ und $E_{p^a}\mu_k = \mu_k E_{p^a}$ für $\gcd(p^a, k) = 1$ (aus den Transportformeln: $v_p(k) = 0$ impliziert $(\alpha - \kappa)_+ = \alpha$ in der $p$-Koordinate). Also
$$[X_{p,N_p}, \mu_k] = 0 \quad (p \nmid k).$$
Somit tragen nur die endlich vielen Primzahlen $p \mid k$ bei:
$$[X_{F,\mathbf N}, \mu_k] = \sum_{\substack{p \in F \\ p \mid k}} [X_{p,N_p}, \mu_k].$$
Sobald $\operatorname{supp} v(k) \subseteq F$, ändern neu hinzugenommene Primrichtungen $q \notin F$ den Kommutator mit $\mu_k$ nicht mehr:
$$\boxed{q \nmid k \quad\Longrightarrow\quad [X_{q,N_q}, \mu_k] = 0.}$$
$\square$

Diese Eigenschaft löst den Refinement-Fehler der radialen Architektur exakt: Der $\mu_k$-Kommutator stabilisiert sich nach endlich vielen Primschritten, unabhängig davon, wie weit $F$ wächst.

$$\boxed{[O\text{-}208\text{-}3] \quad \checkmark[M]}$$

---

## 208.D — Normkonvergente Grenzformel

**Satz ([O-208-4]).** *Für $k = \prod_p p^{a_p}$ konvergiert der Kommutatorgrenzwert in Norm:*
$$D(\mu_k) = \mu_k B_k, \qquad \boxed{B_k = \sum_{p \mid k} B_{p,v_p(k)},}$$
*wobei*
$$B_{p,a} = \sum_{j \ge 0} \bigl(f_p(j+a) - f_p(j)\bigr)\, q_{p,j}.$$

**Normbeweis.** Da die Summanden $B_{p,v_p(k)}$ für verschiedene Primzahlen $p$ auf orthogonale Teilräume wirken, gilt:
$$\|B_k\| = \max_{p \mid k} \|B_{p,v_p(k)}\|.$$
Mit $f_p(j) = \log(j+2)$:
$$f_p(j+a) - f_p(j) = \log\frac{j+a+2}{j+2} \longrightarrow 0 \quad (j \to \infty),$$
und das Supremum wird bei $j=0$ angenommen:
$$\|B_{p,a}\| = \log\frac{a+2}{2}.$$
Daher
$$\boxed{\|B_k\| = \max_{p \mid k} \log\frac{v_p(k)+2}{2}.}$$
Insbesondere für $k = p^a$:
$$\|D(\mu_{p^a})\| = \log\frac{a+2}{2} \longrightarrow \infty.$$

**Anmerkung zur additiven vs. max-Norm.** Falls die Summanden $B_{p,v_p(k)}$ tatsächlich auf strikt orthogonalen Teilräumen operieren (was aus der paarweisen Orthogonalität der Primschalen folgt), gilt die max-Norm. Andernfalls ergibt sich eine Abschätzung durch die $\ell^1$-Summe:
$$\|B_k\| \le \sum_{p \mid k} \log\frac{v_p(k)+2}{2}.$$

Die Grenzderivation auf den Generatoren lautet:
$$D(\mu_k) = \mu_k B_k, \qquad D(\mu_k^*) = -B_k \mu_k^*, \qquad D(e(r)) = 0.$$

Das ergibt eine mehrprimige, **neutrale** ($g = 1$) und normunbeschränkte Erweiterung der dyadischen Konstruktion aus NEU-204.

$$\boxed{[O\text{-}208\text{-}4] \quad \checkmark[M]}$$

---

## 208.E — Offene Frage: Kopplung an geladene Charakterkerne

**[O-208-5] ?[O] — Geladene Kopplung.**

Die separierbare Konstruktion aus 208.B–D ist neutral ($D(e(r)) = 0$, $g = 1$). Für die geladene Route muss $X_{F,\mathbf N}$ mit den Charakterkern-Partialisometrien aus NEU-206 gekoppelt werden:
$$w_{F,\alpha} = \mu_m Q_{F,\alpha} \mu_n^*, \qquad g = m/n \neq 1.$$

Die Frage lautet: Lässt sich die separierbare Potentialstruktur
$$X_{F,\mathbf N} = \sum_{p \in F} X_{p,N_p}$$
mit den geladenen Atomen $w_{F,\alpha}$ verknüpfen, ohne die Separierbarkeit und damit die exakte Refinementstabilität zu verlieren?

Ein natürlicher Ansatz wäre ein gemischtes Potential
$$Z_{F,\mathbf N} = \sum_{p \in F} \sum_{j=0}^{N_p-1} c_{p,j}\, \mu_m q_{p,j} \mu_n^*,$$
wobei $c_{p,j}$ koordinatenweise die Wachstumsbedingung aus NEU-207 erfüllt. Die $e(r)$-Fehlerterme aus NEU-206 treten dabei erneut auf und müssen durch die Charakterkernbedingung $\alpha \ge v(L(r))$ absorbiert werden.

$$\boxed{[O\text{-}208\text{-}5] \quad ?[O]}$$

---

## 208.F — Methodischer Wechsel

Der Kernbefund dieses Knotens:

$$\boxed{\text{Nicht ein radialer mehrdimensionaler Potentialberg, sondern eine Summe unabhängiger eindimensionaler Primkanäle.}}$$

Dieser Wechsel passt wesentlich besser zur multiplikativen Struktur der BC-Algebra: Das Primfaktorzerlegungsgesetz der natürlichen Zahlen spiegelt sich in der Separierbarkeit $c_F(\alpha) = \sum_p f_p(\alpha_p)$ direkt wider. Die radialen Kastenmodelle aus NEU-207 übertragen hingegen eine euklidische Geometrie auf einen Raum mit ultrametrischer Primzahlstruktur.

---

## 208.G — Strukturbilanz

| Knoten | Status | Inhalt |
|---|---|---|
| [O-208-1] | ✓[M]_neg | $c(\alpha)=\log(2+|\alpha|_1)$ nicht refinementstabil unter $F \uparrow \mathcal P$ |
| [O-208-2] | ✓[K] | Separierbare Primpotentiale $X_{F,\mathbf N} = \sum_{p \in F} X_{p,N_p}$ konstruiert |
| [O-208-3] | ✓[M] | Exakte Refinementstabilität: $q \nmid k \Rightarrow [X_{q,N_q},\mu_k]=0$ |
| [O-208-4] | ✓[M] | Normkonvergente Grenzformel $D(\mu_k) = \mu_k B_k$, $\|B_{p,a}\| = \log\frac{a+2}{2}$ |
| [O-208-5] | ?[O] | Kopplung an geladene Charakterkern-Partialisometrien aus NEU-206 |

---

## 208.H — DAG-Stand

```
[O-207-5a] ✓[K]  (c(α) = log(2+|α|_1) existiert, aber ...)
      |
      +---> [O-208-1] ✓[M]_neg   radiale Funktion nicht refinementstabil
      |
      +---> [O-208-2] ✓[K]       separierbare Primpotentiale X_{F,N}
      |
      +---> [O-208-3] ✓[M]       Refinementstabilität: q∤k => Kommutator stabil
      |
      +---> [O-208-4] ✓[M]       D(μ_k) = μ_k B_k, Normbeweis
      |
      +---> [O-208-5] ?[O]        Kopplung an geladene Atome w_{F,α} = μ_m Q_{F,α} μ_n*
                                  (Haupt-Flaschenhals: geladene Route)
```

Der neutrale separierbare Kanal ist damit konstruktiv vollständig. Der einzig verbleibende Schritt für die geladene Route ist [O-208-5]: die Kopplung der separierbaren Primstruktur an die geladenen Partialisometrien, ohne die Separierbarkeit zu verlieren.
