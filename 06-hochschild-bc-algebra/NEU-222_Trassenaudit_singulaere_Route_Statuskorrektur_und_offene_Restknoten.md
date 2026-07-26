# NEU-222 — Trassenaudit der singulären Route: Statuskorrektur und offene Restknoten

**Katalog-ID:** NEU-222
**Knoten:** `[O-222-1-singular-route-boundary-and-character-kernel-audit]`
**Stand:** 26. Juli 2026
**Typ:** Reines Quellenaudit — keine neue Konstruktion, keine neue Behauptung
**Anlass:** Vorbereitung des Entscheidungstests G4 (Tragfähigkeit der singulären Potentialroute)

---

## 0. Auditurteil — die Fragestellung war überholt

Der Auftrag lautete, `[O-207-5b]` (Randtermkontrolle) und `[O-209-5/6]`
(Charakterkernmenge, Ursprungssingularität) quellenseitig aufzubereiten, um zu entscheiden,
ob die singuläre Route trägt. Der Quellenabgleich ergibt:

$$
\boxed{\ \text{Beide Knoten sind seit dem 20. Juli 2026 geschlossen. Die singuläre Route wurde beschritten und trägt bis } HH^4.\ }
$$

- **`[O-209-5]` ✓[M]** — geschlossen durch NEU-210, Satz [O-210-1]: $Z_g = \{0\}$ ist **exakt bewiesen**, nicht nur erwartet.
- **`[O-209-6]` ✓[M]** — geschlossen durch NEU-210, [O-210-2]: das faktoriale Ursprungspotential ist konstruiert, $\operatorname{Sing}(X) = \{0\}$.
- **`[O-207-5b]`** gehört zu einer **anderen**, verlassenen Konstruktion (mehrdimensionale Gitterpartitionen mit Rechteckschalen $Q_{F,\alpha}$). Die faktoriale Route von NEU-210 benötigt sie nicht: Sie erreicht Normkonvergenz der Kommutatoren direkt über das Transportband (210.18/210.19).

Die singuläre Route ist danach **nicht stehengeblieben**, sondern über NEU-211 bis NEU-218
durchgelaufen und erst in NEU-219u auf die Zyklizitätsobstruktion getroffen. Ein
Entscheidungstest „trägt die singuläre Route?" ist damit gegenstandslos — er ist positiv
beantwortet, bis $HH^4$.

$$
\boxed{\ [O\text{-}222\text{-}1] \quad \checkmark[M] \ \text{(Statuskorrektur, keine neue Mathematik)}}
$$

---

## 1. Belegte Trasse der singulären Route

Alle Statusangaben wörtlich aus den Kopfzeilen der Quelldateien.

| Schritt | Quelle | Ergebnis | Status |
|---|---|---|---|
| Ketten-No-go, exakt abgegrenzt | NEU-207 `[O-207-1]` | Keine **totale** Teilbarkeitskette ist unter allen Primtransporten exakt geschlossen. **Nicht** ausgeschlossen: approximative Ketten mit normkontrollierten Randtermen, verzweigte Indexmengen, mehrdimensionale Gitter, endliche gesättigte Kastenmodelle | `✓[M]_neg` |
| Bewertungsgitter | NEU-207 `[O-207-2/3/4]` | $\Lambda = \mathbb N_0^{(\mathcal P)}$; exakte Transportformeln; Charakterkerne als obere Mengen | `✓[K]`, `✓[M]`, `✓[M]` |
| Koeffizientenfunktion | NEU-207 `[O-207-5a]` | $c(\alpha) = \log(2+\lvert\alpha\rvert_1)$ unbeschränkt und translationsflach | `✓[K]` |
| Singularität separierbarer Kanäle | NEU-209 `[O-209-1/2]` | $\widetilde X_{p,N}\vert_{K_p} = c_N - c_0 \to \infty$; Fehlermultiplikatoren sehen $K_p$ für $p\nmid L$ | `✓[M]` |
| Sandwich-No-go | NEU-209 `[O-209-3]` | Naiver Ansatz $\mu_m(\sum_p \widetilde X_{p,N_p})\mu_n^*$ ausgeschlossen | `✓[M]_neg` |
| Definition $Z_g$ | NEU-209 `[O-209-4]` | $Z_g := \bigcap_{r}Z(M_{g,r})$; notwendige Bedingung $\operatorname{Sing}(X)\subseteq Z_g$ | `✓[K]` |
| **$Z_g = \{0\}$** | **NEU-210 `[O-210-1]`** | **exakt bewiesen** via Pontrjagin-Dualität; schließt `[O-209-5]` | **`✓[M]`** |
| **Faktoriales Potential** | **NEU-210 `[O-210-2]`** | $L_j=(j+1)!$, $X_N = \sum_{j<N}c_jq_j + c_NP_N$, $\operatorname{Sing}(X)=\{0\}$; schließt `[O-209-6]` | **`✓[K]`** |
| Transportband | NEU-210 `[O-210-3]` | $P_j \le E_{L_j/k} \le P_{j-k}$; $\mu_k$- und $\mu_k^*$-Kommutatoren normkonvergent | `✓[M]` |
| Charakterabsorption | NEU-210 `[O-210-4]` | $M(0)=0 \Rightarrow MX_N$ stabilisiert exakt | `✓[M]` |
| Geladener Kandidat, teilerfremd | NEU-210 `[O-210-5]` | $[Y_N,\mu_k] \to \mu_{mk}B_k\mu_n^*$ für $(k,mn)=1$ | `✓[M]_part` |
| Nichtteilerfremder Sektor | NEU-211 `[O-211-1/2/3]` | Exakte Formeln via BC-Nica-Relation; $G_{a,d}\in B_{C^*}$; **$D_g : A_{\mathrm{alg}}\to A_{C^*}$ wohldefinierte geladene Derivation** | `✓[M]` |
| Nichtinnerheit | NEU-211 `[O-211-4]` | Offdiagonaltest mit Matrixelementen $c_j\to\infty$ | `✓[M]` |
| Zieltyp | NEU-211 `[O-211-5]` | $B_\ell \notin B_{\mathrm{alg}}$ — **kein** algebraischer Zieltyp; $[D_g]\in HH^1(A_{\mathrm{alg}},A_{C^*})_g$ | `✓[M]_neg` |
| Zieltypbrücke | NEU-212 | $\mathcal A^\infty$ konstruiert; schließt `[O-211-6]` teilweise | `✓[K/M]` |
| Bimodul-No-go | NEU-214/215 | Zentralisatorbeweis, $Z(A_{C^*}) = \mathbb C1$; schließt `[O-213-4]`, `[O-214-2/3]` | `✓[M]` / `✓[M]_neg` |
| Koeffiziententyp | NEU-216 rev.6 | **„Alle Knoten geschlossen."** $\mathcal B^{\log}$, $\mathcal A^{\log}$, $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$ | `✓[M]` |
| Lokal-global | NEU-217 | Lokaler $p$-Block; **globale Nichtinnerheit**; Grad-1-Pfad geschlossen | `✓[K/M]` |
| Cup-Aufstieg | NEU-218 | $L^{\mathrm{cup}}_{g;\mathbf p}\in Z^4(A_{\mathrm{alg}},M)_g$ | `✓[K/M]` |
| **Terminierung** | **NEU-219u** | $t\Phi_0 = g^{-\beta}\Phi_0$, $g^{-\beta}\neq 1$ — **keine gewöhnliche zyklische Klasse in $HC^4$** | **`✓[M]_neg`** |

### Warum die faktoriale Kette am Ketten-No-go vorbeikommt

$L_j = (j+1)!$ ist eine **totale** Teilbarkeitskette, fällt also formal unter NEU-207
`[O-207-1]`. NEU-210 beansprucht jedoch **keine exakte Schließung**, sondern beweist ein
**Transportband** mit beschränkter Bandbreite:

$$P_j \le E_{L_j/k} \le P_{j-k}, \qquad \nu(x) \le \nu(kx) \le \nu(x) + k. \tag{210.12/210.13}$$

Damit fällt sie exakt in die von NEU-207 ausdrücklich offengelassene Klasse der
**approximativen Ketten mit normkontrollierten Randtermen** (207.A, Liste „Nicht
ausgeschlossen werden"). Die beiden Resultate stehen nicht im Widerspruch.

---

## 2. Extrahierte Primärdefinitionen

Zur Vollständigkeit, wörtlich aus den Quellen.

### 2.1 Fehlermultiplikator und Charakterkernmenge

$$[Y, e(r)] = \mu_m\bigl(e(nr)-e(mr)\bigr)b\,\mu_n^*, \qquad Y = \mu_m b\mu_n^* \tag{210.1}$$

$$M_{m,n;r} = e(nr) - e(mr) \tag{210.2}$$

$$Z(M_{g,r}) = \{x\in\hat{\mathbb Z} : M_{g,r}(x)=0\}, \qquad Z_g := \bigcap_{r\in\mathbb Q/\mathbb Z} Z(M_{g,r})$$

**Satz [O-210-1].** Für jeden nichtneutralen reduzierten Grad $g=m/n\neq 1$ gilt $Z_g = \{0\}$.
*Beweis (210.A):* $M_{m,n;r}(x)=0$ für alle $r$ bedeutet $e(r)((n-m)x)=1$ für alle $r$; da
$\mathbb Q/\mathbb Z$ die Punkte von $\hat{\mathbb Z}$ trennt (Pontrjagin), folgt $(n-m)x=0$;
da $\hat{\mathbb Z}\cong\prod_p\mathbb Z_p$ torsionsfrei und $m\neq n$, folgt $x=0$. $\square$

> **Audithinweis der Quelle (210.A).** Falls in NEU-205 oder NEU-209 stattdessen
> $e(mnr)-e(mr)$ steht, ist das zu korrigieren: für $n=1$ verschwände jener Ausdruck
> identisch, obwohl $g=m\neq 1$ geladen sein kann. — Geprüft: NEU-209 §209.E schreibt
> $M_{g,r} = e(nr)-e(mr)$, ist also konsistent mit (210.2).

> **Statuspräzisierung.** Die Herleitung in NEU-209 §209.E („Konzeptionell ist dies zu
> erwarten") war eine **Heuristik** mit Status `?[O]`. Der Beweis steht erst in NEU-210.
> Beim Zitieren ist NEU-210 §210.A die Quelle, nicht NEU-209 §209.E.

### 2.2 Faktoriale Kette und Potential

$$L_j := (j+1)!, \quad P_j := E_{L_j}, \quad q_j := P_j - P_{j+1} \tag{210.4}$$

$$P_0 = 1, \quad P_{j+1}\le P_j, \quad q_jq_\ell = 0\ (j\neq\ell), \qquad \bigcap_{j\ge 0}L_j\hat{\mathbb Z} = \{0\} \tag{210.5}$$

$$c_j := \log(j+2), \qquad X_N := \sum_{j=0}^{N-1}c_jq_j + c_NP_N \tag{210.6}$$

$$\nu(x) := \max\{j : x\in L_j\hat{\mathbb Z}\}\ (x\neq 0), \qquad X_N(x) = c_{\min(\nu(x),N)} \tag{210.7}$$

$$\operatorname{Sing}(X) = \{0\} \tag{210.8}$$

### 2.3 Transportdifferenzen und Grenzkommutatoren

$$B_k(x) := c_{\nu(kx)} - c_{\nu(x)}, \qquad B_k(0) := 0 \tag{210.14}$$

$$0 \le B_k(x) \le \log\Bigl(\frac{\nu(x)+k+2}{\nu(x)+2}\Bigr) \longrightarrow 0 \quad (\nu(x)\to\infty) \tag{210.16}$$

$$[X_N,\mu_k] = \mu_k\bigl(T_k(X_N)-X_N\bigr), \qquad T_k(E_L) := E_{L/(L,k)} \tag{210.17}$$

$$\lim_N [X_N,\mu_k] = \mu_kB_k, \qquad \lim_N [X_N,\mu_k^*] = -B_k\mu_k^* \tag{210.18/19}$$

Da $X_N\in B_{\mathrm{alg}}$: $[X_N,e(r)] = 0$.

### 2.4 Charakterabsorption

**Satz [O-210-4].** Sei $M\in B_{\mathrm{alg}}$ lokal konstant mit $M(0)=0$. Dann existiert
$J$ mit $MP_J = 0$, und für alle $N\ge J$ gilt exakt
$$MX_N = \sum_{j=0}^{J-1}c_jMq_j. \tag{210.21}$$

### 2.5 Was NEU-210 zur Reichweite selbst sagt

> **Typologische Vorbemerkung (210.0), wörtlich.** Ein positiver Befund aus [O-210-6] würde
> $D_g : A_{\mathrm{alg}}\to A_{C^*}$ mit geladenem Grad $g=m/n$ liefern. *„Das ist noch
> nicht $[L_3]\in HH^4$."* Erforderlich blieben: $D_g(A_{\mathrm{alg}})\subseteq A_{\mathrm{alg}}$,
> $[D_g]\neq 0\in HH^1(A_{\mathrm{alg}},A_{\mathrm{alg}})_g$, und anschließend ein
> typkorrekter Cup-Pfeil nach $HH^4_g$. Der Faktorialkandidat wäre ein *„konstruktiver
> Vorläufer der Schicht $X.3$, nicht bereits ihre Realisierung."*

Diese drei Anschlussforderungen wurden inzwischen bearbeitet: die Zieltypfrage negativ
(NEU-211 `[O-211-5]`: kein algebraischer Zieltyp), dann über $\mathcal A^\infty$ (NEU-212)
und $\mathcal A^{\log}$ (NEU-216) repariert, die globale Nichtinnerheit in NEU-217, der
Cup-Pfeil in NEU-218.

---

## 3. Was tatsächlich noch offen ist

Erhoben durch Abgleich aller Kopfzeilenstatus in NEU-206 bis NEU-219 gegen alle
„Schließt:"-Deklarationen.

### 3.1 Knoten der verlassenen Gitterroute

Diese Knoten sind formal offen, gehören aber zur **mehrdimensionalen Gitterkonstruktion**,
die NEU-210 durch die faktoriale Kette ersetzt hat. Sie sind für die aktive Trasse
gegenstandslos, solange nicht jemand zur Gitterroute zurückkehrt.

| Knoten | Quelle | Inhalt |
|---|---|---|
| `[O-206-4]` | NEU-206 | arithmetische Transportgeometrie |
| `[O-207-5b]` | NEU-207 | Tail- und Refinement-Randtermkontrolle bei wachsenden Gitterpartitionen |
| `[O-207-5c]` | NEU-207 | Grenzderivation der geladenen Atome $w_{F,\alpha}=\mu_mQ_{F,\alpha}\mu_n^*$ |
| `[O-208-5]` | NEU-208 | Kopplung des neutralen separierbaren Kanals an geladene Charakterkerne |

> **Präzisierung zu `[O-207-5b]`.** Die Quelle formuliert **keinen** expliziten Randterm
> $R_N$ mit $R_N\to 0$, sondern eine **Norm-Cauchy-Bedingung** für die Differenz zweier
> Kommutatoren auf verschiedenen Partitionsstufen:
> $$\Bigl\lVert\Bigl[\sum_{\alpha\in\mathcal A_N}c(\alpha)w_{F_N,\alpha},\mu_k\Bigr] - \Bigl[\sum_{\alpha\in\mathcal A_M}c(\alpha)w_{F_M,\alpha},\mu_k\Bigr]\Bigr\rVert \longrightarrow 0 \quad (N,M\to\infty).$$
> Die im Auftrag angenommene Trennung „algebraische Identität bei festem $N$ gegen
> analytische Randtermkontrolle für $N\to\infty$" liegt in der Quelle **nicht** in dieser
> Form vor.

### 3.2 Aktive Restknoten der faktorialen Trasse

| Knoten | Quelle | Inhalt | Status |
|---|---|---|---|
| `[O-212-5]` | NEU-212 | Restknoten der Zieltypbrücke | `?[O]` |
| `[O-213-3]`, `[O-213-5]` | NEU-213 | Restknoten des Revisionsaudits | `?[O]` |
| `[O-214-4b]` | NEU-214 | Restknoten des Bimodul-Rigiditätslemmas | `?[O]` |
| `[O-217-1d]` | NEU-217 rev.3 | Restknoten nach dem Faithfulness-Negativresultat | `?[O]` |

> Diese vier bis fünf Knoten sind die einzigen formal offenen Punkte der faktorialen Trasse
> unterhalb von NEU-218. Sie sind sämtlich **technische Restknoten**, keine
> Existenzentscheidungen. `[O-210-6]` selbst gilt über die Teilknoten 6a/6b/6c als durch
> NEU-211 abgearbeitet; `[O-217-2b]` und `[O-217-2c]` sind durch die Nachfolgedateien
> NEU-217 `[O-217-2b]` und `[O-217-2c-6]` geschlossen (aggregiert `✓[K/M]`).

### 3.3 Der eigentliche Flaschenhals

$$
\boxed{\ [O\text{-}219\text{-}6] \quad \text{Weil-/Gammafaktorpaarung} \ }
$$

Die Trasse endet nicht an der singulären Konstruktion, sondern an der **Zyklizität**
(NEU-219u): Der kanonische Basislift ist ein typkorrekter Hochschildkozykel, aber
$t\Phi_0 = g^{-\beta}\Phi_0$ mit eingabeunabhängigem $g^{-\beta}\neq 1$. Die in NEU-219u
benannten Reparaturpfade sind Orbitshift $\kappa\neq 0$, Ladungsneutralisation, andere
Koeffizientenkategorie oder die Weil-/Gammafaktorpaarung `[O-219-6]` — letztere ist ab
NEU-220 aktiv beschritten.

---

## 4. Konsequenzen für das Kontrollblatt

Ebene XVI Revision 2 führt in XVI-D/P4 die Knoten `[O-207-5b]` und `[O-209-5/6]` als offene
Anforderungen der singulären Potentialroute und bezeichnet P4 als „letzten bekannten
Konstruktionsweg" mit Entscheidungscharakter. Das ist nach diesem Audit **unzutreffend**:

| Aussage in XVI-D/P4 (Rev. 2) | Korrektur |
|---|---|
| P4.3 `[O-207-5b]` offen | gehört zur verlassenen Gitterroute; für die faktoriale Trasse gegenstandslos |
| P4.4 `[O-209-5/6]` offen | **geschlossen** durch NEU-210 `[O-210-1]` und `[O-210-2]` |
| „letzter bekannter Konstruktionsweg, vor weiterer Investition zu entscheiden" | Die Route wurde beschritten und trägt bis $HH^4$. Die Entscheidung ist gefallen — positiv bis zum Cup-Aufstieg, negativ erst bei der Zyklizität |

Die Formulierung in der Bestandsaufnahme §4.1 („die kohomologische Schicht steuert auf Leere
zu; übrig bleibt allein die singuläre Route") ist entsprechend zurückzunehmen. Der
Möglichkeitsraum war zum Zeitpunkt jener Analyse bereits durch NEU-210–218 erweitert.

$$
\boxed{\ \text{Die kohomologische Schicht ist nicht leer. Sie ist bis } HH^4 \text{ gebaut und an der Zyklizität blockiert.}\ }
$$

---

## 5. Revidierter Entscheidungstest

Der im Auftrag vorgeschlagene Zieltest

$$\exists H_{\mathrm{sing}}:\ \operatorname{Sing}(H_{\mathrm{sing}})\subseteq Z_g=\{0\},\quad R_N\to 0,\quad [D_g]\neq 0$$

ist in seinen ersten drei Komponenten **bereits erfüllt**:

| Komponente | Status | Quelle |
|---|---|---|
| $Z_g = \{0\}$ | `✓[M]` | NEU-210 `[O-210-1]` |
| $\operatorname{Sing}(X)=\{0\}$ | `✓[K]` | NEU-210 `[O-210-2]` |
| Normkonvergenz der Kommutatoren | `✓[M]` | NEU-210 `[O-210-3]`, NEU-211 `[O-211-2]` |
| $[D_g]\neq 0$, nicht $A_{C^*}$-inner | `✓[M]` | NEU-211 `[O-211-4]`, global NEU-217 |
| Cup-Pfeil nach $HH^4_g$ | `✓[K/M]` | NEU-218 |
| **Zyklizität in $HC^4$** | **`✓[M]_neg`** | **NEU-219u** |

Der sinnvolle Nachfolgetest ist daher **nicht** ein Test der singulären Route, sondern:

$$
\boxed{\ \text{Existiert eine Koeffizientenkategorie, in der } L^{\mathrm{cup}}_{g;\mathbf p} \text{ eine nichttriviale Klasse liefert, ohne dass } t\Phi = \Phi \text{ verlangt wird?}\ }
$$

Das ist `[O-219-6]` beziehungsweise XVI-D/P3.3, und es wird ab NEU-220 über die
Weil-/Gammafaktorpaarung verfolgt.

---

## 6. Statusbilanz

| Aussage | Status |
|---|---|
| `[O-209-5]`, `[O-209-6]` geschlossen durch NEU-210 | `✓[M]` |
| `[O-207-5b]` gehört zur verlassenen Gitterroute | `✓[M]` (Quellenbefund) |
| Faktoriale Kette umgeht das Ketten-No-go als approximative Kette | `✓[M]` (207.A + 210.12/13) |
| Singuläre Route trägt bis $HH^4$ | `✓[K/M]` (NEU-211–218) |
| Route blockiert an der Zyklizität, nicht an der Konstruktion | `✓[M]_neg` (NEU-219u) |
| Offene Restknoten der Trasse: `[O-212-5]`, `[O-213-3/5]`, `[O-214-4b]`, `[O-217-1d]` | `?[O]`, technisch |
| G4 als Entscheidungstest der singulären Route | **gegenstandslos** |
| **Gesamtstatus `[O-222-1]`** | **`✓[M]`** |

---

## Abhängigkeiten

| Referenz | Verwendet für |
|---|---|
| NEU-206 | Fehlermultiplikatoren $M_{g,r}$, Charakterkern-Erschöpfungskette |
| NEU-207 | Ketten-No-go und seine Abgrenzung, Bewertungsgitter, `[O-207-5b/5c]` |
| NEU-208 | neutraler separierbarer Kanal, `[O-208-5]` |
| NEU-209 | $K_p$, Sandwich-No-go, Definition $Z_g$ |
| NEU-210 | $Z_g=\{0\}$, faktoriales Potential, Transportband, Charakterabsorption |
| NEU-211 | nichtteilerfremder Sektor, $D_g$, Nichtinnerheit, Zieltyp-Negativbefund |
| NEU-212–215 | Zieltypbrücke $\mathcal A^\infty$, Bimodul-No-go |
| NEU-216/217/218 | $\mathcal B^{\log}$/$\mathcal A^{\log}$, globale Nichtinnerheit, Cup-Aufstieg |
| NEU-219u | Zyklizitäts-No-Go, Reparaturpfade |
