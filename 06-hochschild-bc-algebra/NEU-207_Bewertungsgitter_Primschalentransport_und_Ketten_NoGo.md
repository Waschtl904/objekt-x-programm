# NEU-207 — Bewertungsgitter, Primschalentransport und Ketten-No-go

**Status:** [O-207-1] ✓[M]_neg, [O-207-2] ✓[K], [O-207-3] ✓[M], [O-207-4] ✓[M], [O-207-5a] ✓[K]; [O-207-5b], [O-207-5c] ?[O]  
**Erstellt:** 2026-07-20  
**Vorgänger:** NEU-206 ([O-206-4] ?[O] — arithmetische Transportgeometrie offen)  
**Ziel:** Präzise Abgrenzung des No-go für eindimensionale Kettenarchitektur; Einführung des Bewertungsgitters als korrektem Transportindex; Zerlegung des Koeffizientenproblems

---

## 207.0 — Ausgangslage

NEU-206 hat identifiziert, dass der Transportoperator
$$T_k(L) := \frac{L}{(L,k)}$$
auf einer eindimensionalen Teilbarkeitskette $(L_j)$ arithmetisch unvorhersehbar ist: der Transport $q_j\mu_k$ landet im Allgemeinen nicht in einer einzelnen Nachbarschale, sondern schneidet quer durch die Kettengeometrie.

NEU-207 schärft diesen Befund an drei Stellen:
1. Der No-go betrifft exakt die **totale** Kettenarchitektur bei mehr als einer Primrichtung.
2. Die Rechteckschalen $Q_{F,\alpha}$ sind bei festem $F$ orthogonal und transportstabil, aber globale Konsistenz erfordert endliche gesättigte Partitionen.
3. Das Koeffizientenproblem ist abstrakt bereits lösbar; offen ist die Kompatibilität mit den Rand- und Refinement-Termen.

---

## 207.A — No-go für exakte eindimensionale Schließung

**Satz ([O-207-1]).** *Keine totale Teilbarkeitskette, die Vielfache zweier verschiedener Primzahlen enthält, ist unter allen Primtransporten $T_p(L)=L/(L,p)$ exakt geschlossen.*

**Beweis.** Seien $p \neq q$ Primzahlen und $pq \mid L$ für ein Kettenglied $L$. Die beiden Transportierten
$$\frac{L}{p} \qquad\text{und}\qquad \frac{L}{q}$$
liegen in der Teilbarkeitsordnung unvergleichbar: Die $p$-adische Bewertung von $L/p$ ist um 1 kleiner als die von $L$, die $q$-adische Bewertung unverändert — und umgekehrt für $L/q$. Also gilt
$$\frac{L}{p} \nmid \frac{L}{q}, \qquad \frac{L}{q} \nmid \frac{L}{p}.$$
Eine totale Kette kann daher nicht beide gleichzeitig als Glieder enthalten. $\square$

**Präzise Klasse des Ausschlusses.** Der Satz schließt aus:
- exakte eindimensionale Nachbarschalen-Geometrie für alle Primrichtungen gleichzeitig.

Nicht ausgeschlossen werden:
- approximative Ketten (normkontrollierte Randterme);
- verzweigte Indexmengen;
- mehrdimensionale Gitter;
- endliche gesättigte Kastenmodelle.

$$\boxed{[O\text{-}207\text{-}1] \quad \checkmark[M]_{\mathrm{neg}}}$$

Dieser Negativbefund betrifft **ausschließlich** die exakte totale Kettenarchitektur. Er beendet die Suche nach einem eindimensionalen Nachfolger der dyadischen Konstruktion aus NEU-204, öffnet jedoch explizit die mehrdimensionale Route.

---

## 207.B — Das Bewertungsgitter als korrekter Transportindex

Sei $\mathcal P$ die Menge der Primzahlen und
$$\Lambda := \mathbb N_0^{(\mathcal P)}$$
das Gitter der endlich getragenen Bewertungsvektoren. Für $\alpha = (\alpha_p)_p \in \Lambda$ setze
$$n(\alpha) := \prod_p p^{\alpha_p}, \qquad E_\alpha := E_{n(\alpha)}.$$
Für $k = \prod_p p^{\kappa_p}$ sei $\kappa = v(k) \in \Lambda$ der Bewertungsvektor.

Die vier Transportformeln aus NEU-206 werden auf $\Lambda$ zu exakten Gittertranslationen:
$$\boxed{E_\alpha\mu_k = \mu_k E_{(\alpha-\kappa)_+},} \qquad \boxed{\mu_kE_\alpha = E_{\alpha+\kappa}\mu_k,}$$
$$E_\alpha\mu_k^* = \mu_k^*E_{\alpha+\kappa}, \qquad \mu_k^*E_\alpha = E_{(\alpha-\kappa)_+}\mu_k^*.$$
Das koordinatenweise Abschneiden lautet:
$$((\alpha-\kappa)_+)_p = \max(\alpha_p-\kappa_p, 0).$$

Die bislang „unvorhersehbare" arithmetische Operation $L \mapsto L/(L,k)$ ist auf $\Lambda$ eine vollständig kontrollierte Translation mit koordinatenweisem Abschneiden.

$$\boxed{[O\text{-}207\text{-}2] \quad \checkmark[K]}$$

---

## 207.C — Exakte Transportformeln für Prim- und Rechteckschalen

### Primschalen

Für eine Primzahl $p$ und $a \geq 0$ definiere
$$q_{p,a} := E_{p^a} - E_{p^{a+1}}.$$
Dies ist die Projektion auf die Menge mit exakter $p$-adischer Bewertung $a$.

Aus NEU-206 folgt unmittelbar:
$$\boxed{\mu_kq_{p,a} = q_{p,a+v_p(k)}\mu_k,}$$
$$\boxed{q_{p,a}\mu_k = \begin{cases}\mu_kq_{p,a-v_p(k)}, & a \ge v_p(k),\\ 0, & a < v_p(k).\end{cases}}$$
Adjungiert gilt entsprechend
$$q_{p,a}\mu_k^* = \mu_k^*q_{p,a+v_p(k)}, \qquad \mu_k^*q_{p,a} = \begin{cases}q_{p,a-v_p(k)}\mu_k^*, & a \ge v_p(k),\\ 0, & a < v_p(k).\end{cases}$$

Das ist genau die dyadische Verschiebungsgeometrie aus NEU-204, nun für jede Primzahl separat.

### Rechteckige Bewertungsschalen

Für eine endliche Primzahlmenge $F$ und $\alpha \in \mathbb N_0^F$ setze
$$Q_{F,\alpha} := \prod_{p \in F} q_{p,\alpha_p}.$$
Da die Faktoren kommutieren, ist $Q_{F,\alpha}$ eine Projektion. Für verschiedene Bewertungsvektoren gilt
$$\alpha \neq \beta \implies Q_{F,\alpha}Q_{F,\beta} = 0.$$
Für $\kappa_F = (v_p(k))_{p \in F}$ folgt exakt:
$$\boxed{\mu_kQ_{F,\alpha} = Q_{F,\alpha+\kappa_F}\mu_k,}$$
$$\boxed{Q_{F,\alpha}\mu_k = \begin{cases}\mu_kQ_{F,\alpha-\kappa_F}, & \alpha \ge \kappa_F,\\ 0, & \text{sonst.}\end{cases}}$$

Der Transport einer rechteckigen Schale ist damit weder unvorhersehbar noch diffus: Er ist eine exakte Gitterverschiebung oder Null.

$$\boxed{[O\text{-}207\text{-}3] \quad \checkmark[M]}$$

### Endliche gesättigte Partitionen

Bei wechselnden Primzahlmengen $F \subsetneq G$ sind die Familien nicht ohne Weiteres gemeinsam orthogonal: Ein $F$-Zylinder zerfällt in mehrere feinere $G$-Zylinder.

Für jedes $p \in F$ und einen Cutoff $N_p$ gilt
$$1 = \sum_{a=0}^{N_p-1}q_{p,a} + E_{p^{N_p}}.$$
Durch Produktbildung über $p \in F$ erhält man eine endliche orthogonale Zerlegung der Eins, deren Atome koordinatenweise entweder aus einer exakten Bewertungsschale $q_{p,a}$ oder aus der terminalen Tailprojektion $E_{p^{N_p}}$ bestehen. Das ist das mehrdimensionale Analogon des Sättigungsterms $c_NP_N$ aus NEU-204. Ohne Tailatome wäre die Gitterzerlegung unvollständig und der spätere Randterm nicht kontrolliert.

---

## 207.D — Charakterkerne als obere Mengen

Zu jedem Fehlermultiplikator $M_{g,r}$ existiert nach NEU-206 ein Integer $L(r)$ mit $M_{g,r}E_{L(r)} = 0$. Setze $\beta(r) := v(L(r)) \in \Lambda$.

Für jede endliche Primzahlmenge $F$, die den Primzahlsupport von $L(r)$ enthält, gilt:
$$\alpha \ge \beta(r) \implies Q_{F,\alpha} \le E_{L(r)}.$$
Daher
$$\boxed{M_{g,r}Q_{F,\alpha} = 0 \quad \text{für } \alpha \ge \beta(r).}$$

Die Charakterkernbedingung ist im Bewertungsgitter eine obere Mengenbedingung. Transport und Charakterkern sind auf demselben Indexraum formuliert.

$$\boxed{[O\text{-}207\text{-}4] \quad \checkmark[M]}$$

---

## 207.E — Koeffizientenfunktion: Existenz und Splitlung

### Positive Lösung ([O-207-5a])

Setze
$$|\alpha|_1 := \sum_p \alpha_p$$
und
$$\boxed{c(\alpha) := \log(2+|\alpha|_1).}$$

Für jeden fest getragenen Bewertungsvektor $\kappa \in \Lambda$ gilt:
$$c(\alpha+\kappa) - c(\alpha) = \log\left(\frac{2+|\alpha|_1+|\kappa|_1}{2+|\alpha|_1}\right) = \log\left(1+\frac{|\kappa|_1}{2+|\alpha|_1}\right) \longrightarrow 0$$
für $|\alpha|_1 \to \infty$, sogar gleichmäßig:
$$\sup_{|\alpha|_1 \ge R}|c(\alpha+\kappa)-c(\alpha)| \le \log\left(1+\frac{|\kappa|_1}{R+2}\right) \longrightarrow 0.$$

Gleichzeitig ist $c$ unbeschränkt:
$$c(Ne_p) = \log(N+2) \longrightarrow \infty.$$

Die Existenz einer geeigneten unbeschränkten, translationsflachen Koeffizientenfunktion ist damit **nicht mehr offen**.

$$\boxed{[O\text{-}207\text{-}5a] \quad \checkmark[K]}$$

### Offene Teilfragen

**[O-207-5b] ?[O] — Randtermkontrolle.**  
Konstruktion einer wachsenden Folge endlicher gesättigter Gitterpartitionen $(\mathcal{P}_{F_N, \mathbf{N}_N})_{N \geq 0}$, deren Tail- und Refinement-Randterme für jedes feste $k$ in Norm verschwinden:
$$\left\|\left[\sum_{\alpha \in \mathcal{A}_N} c(\alpha)\, w_{F_N,\alpha},\, \mu_k\right] - \left[\sum_{\alpha \in \mathcal{A}_M} c(\alpha)\, w_{F_M,\alpha},\, \mu_k\right]\right\| \longrightarrow 0 \quad (N,M \to \infty).$$

Das ist die mehrdimensionale Version der erfolgreichen Randtermkompensation aus NEU-204.

**[O-207-5c] ?[O] — Geladene Atome und Grenzderivation.**  
Einsetzen der geladenen Atome
$$w_{F,\alpha} = \mu_m Q_{F,\alpha} \mu_n^*$$
und Nachweis, dass die Grenzkommutatoren
$$D(a) := \lim_N [Z_N, a]$$
eine nichtinnere Derivation mit Ladung $g = m/n \neq 1$ ergeben, die alle BC-Relationen respektiert und nachweislich nicht durch ein Element $x \in A$ implementiert wird.

---

## 207.F — Strukturbilanz

| Knoten | Status | Inhalt |
|---|---|---|
| [O-207-1] | ✓[M]_neg | Keine totale Teilbarkeitskette unter Primtransporten zweier verschiedener Primzahlen exakt geschlossen |
| [O-207-2] | ✓[K] | Bewertungsgitter $\Lambda = \mathbb N_0^{(\mathcal P)}$ als korrekter Transportindex |
| [O-207-3] | ✓[M] | Exakte Transportformeln für $q_{p,a}$ und $Q_{F,\alpha}$ bei festem endlichem $F$ |
| [O-207-4] | ✓[M] | Charakterkerne = obere Mengen $\alpha \ge v(L(r))$ auf $\Lambda$ |
| [O-207-5a] | ✓[K] | $c(\alpha) = \log(2+|\alpha|_1)$ — unbeschränkt, translationsflach, gleichmäßig |
| [O-207-5b] | ?[O] | Tail- und Refinement-Randtermkontrolle bei wachsenden Gitterpartitionen |
| [O-207-5c] | ?[O] | Grenzderivation der geladenen Atome nichtinner und geladen |

$$\boxed{\text{Der tatsächliche neue Flaschenhals ist nicht mehr die Koeffizientenfunktion, sondern die Randtermkontrolle bei wachsenden mehrdimensionalen Gitterpartitionen.}}$$

Gelingt [O-207-5b], wäre erstmals ein ernsthafter geladener Kandidat für den direkten Weg zu Objekt $X$ (Schicht X.3, $[L_3]$-Klasse) vorhanden.

---

## 207.G — DAG-Stand

```
[O-206-4] ?[O]  (arithm. Transportgeometrie)
      |
      +---> [O-207-1] ✓[M]_neg   Ketten-No-go (exakt, nicht pauschal)
      |
      +---> [O-207-2] ✓[K]       Bewertungsgitter Λ
      |
      +---> [O-207-3] ✓[M]       Transportformeln q_{p,a}, Q_{F,α}
      |
      +---> [O-207-4] ✓[M]       Charakterkerne als obere Mengen
      |
      +---> [O-207-5a] ✓[K]      c(α) = log(2+|α|_1) — existiert
      |
      +---> [O-207-5b] ?[O]      Randtermkontrolle (Haupt-Flaschenhals)
      |
      +---> [O-207-5c] ?[O]      Grenzderivation nichtinner & geladen
```
