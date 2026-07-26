# NEU-203 — Projektionsdifferenzen: Normgeometrie, Kommutatortrivialität und korrigiertes Singularitätskriterium

**Status:** Mehrfach-Audit abgeschlossen (inkl. Typkorrektur 2026-07-19 v2)  
**Erstellt:** 2026-07-19  
**Vorgänger:** NEU-202 (revidiert), NEU-201 ([O-199-3]_sing ?[O])  
**Nachfolger:** NEU-204 (positive Realisierung)

---

## 203.0 — Typkorrektur (v2)

Setze $E_n := \mu_n \mu_n^*$. In der üblichen BC-Präsentation gilt
$$\rho_n(e(r)) = \frac{1}{n}\sum_{ns=r} e(s) = \mu_n e(r) \mu_n^*.$$

Für $r = 0$ folgt:
$$\boxed{E_n = \mu_n\mu_n^* = \frac{1}{n}\sum_{ns=0} e(s).} \tag{203.1}$$

Die rechte Seite ist eine endliche Summe in $B_{\mathrm{alg}} = \mathbb{C}[\mathbb{Q}/\mathbb{Z}]$. Sofern dies die in NEU-183 verwendete Relation (R1)–(R7) ist, gilt:
$$\boxed{E_n \in B_{\mathrm{alg}}, \qquad z_p = E_p - E_{p+1} \in B_{\mathrm{alg}}.}$$

**Revidierte Aussage zu NEU-203.0:** Die ursprüngliche Behauptung $z_p \notin B$ war ungenau. Der relevante Kommutatorquotient bleibt $A/[A,A]$, weil die Darstellung $z_p = [\mu_p,\mu_p^*] - [\mu_{p+1},\mu_{p+1}^*]$ Kommutatoren in der vollen Algebra verwendet.

**Zusatz:** Die Algebrazugehörigkeit liefert sofort:
$$[z_p, e(r)] = 0 \qquad \forall\, r \in \mathbb{Q}/\mathbb{Z},$$
da $B_{\mathrm{alg}}$ abelsch ist. Die Statusaussagen [O-203-1a] bis [O-203-3] bleiben unverändert.

---

## 203.A — Augmentationsneutralität

**Status: [O-203-1a] ✓[M]**

$$\boxed{\varepsilon(z_p) = 0.} \tag{203.2}$$

---

## 203.B — Exakte Norm

**Status: [O-203-1b] ✓[M]**

$$\boxed{\|z_p\| = 1.} \tag{203.3}$$

Für jede Koeffizientenfamilie $(c_p)$: $\sum_p \|c_p z_p\| = \sum_p |c_p|$.

---

## 203.C — Kommutatorstruktur

**Status: [O-203-1c] ✓[M]**

$$\boxed{z_p \in [A,A].} \tag{203.5}$$

---

## 203.D — Normkonvergenz impliziert Innerheit

**Status: [O-203-2] ✓[M]_neg**

$(c_p) \in \ell^1 \Rightarrow x = \sum_p c_p z_p \in \overline{[A,A]} \Rightarrow D_x = \operatorname{ad}(x)$, nur innere Derivation.

---

## 203.E — Kein beschränkter trazieller Detektor

**Status: [O-203-3] ✓[M]_neg**

$$\boxed{\tau(x) = 0 \quad \text{für jedes beschränkte trazielles Funktional.}} \tag{203.9}$$

**Algebraischer Vorbehalt:** $x \in \overline{[A,A]}$ impliziert nicht $x \in [A,A]$ algebraisch. Nur unstetige Funktionale könnten eine Klasse in $A/[A,A]$ detektieren.

---

## 203.F — Teleskopierung liefert keinen Ausweg

Alle drei Fälle (F.1–F.3) führen auf Grenzwerte in $\overline{[A,A]}$; (203.8) und (203.9) bleiben unverändert.

---

## 203.G — Korrigiertes Singularitätskriterium

$$\boxed{
\begin{aligned}
&x_N \text{ ist nicht norm-Cauchy in } A, \\
&[x_N, a] \text{ ist für jeden Generator } a \text{ norm-Cauchy in } A.
\end{aligned}
} \tag{203.10}$$

Die Grenzwerte $D(a) := \lim_N [x_N, a]$ müssen: unabhängig von der Darstellungswahl sein; alle BC-Relationen respektieren; homogene Ladung $g \neq 1$ besitzen (für geladene Route); nachweislich nicht durch $x \in A$ implementierbar sein.

**Methodischer Kernsatz:** Nicht das Potential selbst, sondern nur seine Kommutatorfamilie darf regularisieren.

---

## 203.H — Gesamtbilanz $z_p$

| Eigenschaft | Status | Ergebnis |
|---|---|---|
| Augmentationsneutralität | ✓[M] | $\varepsilon(z_p)=0$, $z_p \in B_{\mathrm{alg}}$ |
| Einzelnorm | ✓[M] | $\|z_p\|=1$ |
| Kommutatorstruktur | ✓[M] | $z_p \in [A,A]$ |
| Normkonvergenz | ✓[M]_neg | führt nur zu innerem Potential |
| Trazieller Detektor | ✓[M]_neg | verschwindet auf jedem Grenzwert |
| Singuläre Kommutatorregularisierung | ✓[M] | **positiv realisiert in NEU-204** |

---

## 203.I — Atomarer Knoten [O-203-4]

$$\boxed{[O\text{-}203\text{-}4]: \quad \exists\,(c_p): \; \sum_p c_p z_p \text{ divergiert}, \; \sum_p c_p [z_p,a] \text{ konvergiert}, \; D(a) \text{ nichtinner.}} \tag{203.12}$$

**Status: [O-203-4] ✓[M]** — positiv realisiert durch dyadische Schalenkonstruktion in NEU-204 (neutral, $\deg D = 1_\Gamma$).

---

## 203.J — DAG-Stand

| Knoten | Status | Inhalt |
|---|---|---|
| [O-203-1a] | ✓[M] | $\varepsilon(z_p)=0$, $z_p \in B_{\mathrm{alg}}$ |
| [O-203-1b] | ✓[M] | $\|z_p\|=1$ |
| [O-203-1c] | ✓[M] | $z_p \in [A,A]$ |
| [O-203-2] | ✓[M]_neg | normkonvergentes Potential → innere Derivation |
| [O-203-3] | ✓[M]_neg | kein beschränkter trazieller Detektor |
| [O-203-4] | ✓[M] | singuläre Kommutatorregularisierung realisiert (NEU-204) |
| [O-199-3]_sing | ?[O] | übergeordnete Frage: geladene Route noch offen |
