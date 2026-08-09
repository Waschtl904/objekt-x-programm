# P09 / I2 — Äußere Derivationen und singuläre Potentialroute: Pass-A-Reconciliation

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Paket:** I2 — NEU-192–211  
**Prüfart:** `AUDIT-RECONCILED` / `AUDIT-REUSED` mit gezielten `TARGETED-REAUDIT`-Punkten  
**Status:** **`I2 PASS A COMPLETE — GEGENCHECK AUSSTEHEND`**

---

## 0. Scope und autoritative Leserichtung

I2 umfasst die Live-Quellen NEU-192–211 im Ordner `06-hochschild-bc-algebra/`, einschließlich der Doppeldatei NEU-193. Für NEU-202–211 wurden zusätzlich die vorhandenen historischen `ARCHIV-AUDIT-*`-Blätter herangezogen. Spätere Statusanker sind `AUDITSTAND-2026-08-03.md`, `NEU-222_Trassenaudit...` sowie — bei Konflikten — der August-Endanker `NEU-219_Finalaudit_Gesamtabschluss.md`.

Verbindliche Präzedenzregel:

```text
August-Finalaudit / AUDITSTAND
    > ARCHIV-AUDIT des konkreten Knotens
    > revidierte Live-NEU-Datei
    > ältere Zwischenfassung / Zwischenbehauptung.
```

### 0.1 Provenienzlücke NEU-198

Mehrere Formeln in NEU-199 referenzieren einen Knoten `NEU-198` und dort angeblich abgeschlossene Teilknoten `[O-198-1/2/3]`. Im aktuellen Live-Inventar von `06-hochschild-bc-algebra/` und in der Repo-Suche existiert **keine NEU-198-Datei**.

Daher gilt für P09:

```text
NEU-198: MISSING-SOURCE / keine eigenständige SYN-Provenienz.
```

Die tatsächlich benötigte Quotienten-/Detektorarchitektur wird direkt aus NEU-197 und NEU-199 migriert. Keine Aussage wird allein mit einer nicht vorhandenen NEU-198-Quelle begründet.

---

## 1. I2-Kernresultat in einem Satz

Die singuläre Potentialroute entwickelt sich von mehreren negativen Modelltests zu einem echten positiven analytischen Resultat:

\[
\boxed{
[D_g^{\rm corr}]\neq0
\quad\text{in}\quad
HH^1(A_{\rm alg},A_{C^*})_g,
\qquad g\neq1.
}
\]

Die geladene Derivation ist als punktweiser Normgrenzwert der inneren Derivationen

\[
\operatorname{ad}(Y_N),
\qquad
Y_N=\mu_m X_N\mu_n^*,
\]

mit faktorialem Ursprungspotential `X_N` konstruiert. Der **geschriebene** NEU-211-Knoten mit `D_g(e(r)):=0` ist falsch; der korrigierte Knoten `[O-211-3corr]` verwendet den nichtverschwindenden Charakterterm und ist `✓[M]`.

Nicht bewiesen ist damit:

\[
[D_g]\neq0\text{ in }HH^1(A_{\rm alg},A_{\rm alg})_g,
\]

und ebenso wenig bereits ein geladener nichttrivialer `HH^4`-Satz. Die Koeffizientenbrücke und der Cup-Aufstieg gehören nach I3.

---

## 2. Reconciliation-Matrix NEU-192–211

| Quelle | Prüfart | P09-Endstatus | Kanonischer I2-Befund |
|---|---|---|---|
| NEU-192 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Algebraische Separations-/Nichtrandlogik ist korrekt. Ein beliebiger Dualzeuge ist nur äquivalente Umformulierung der Nichtrandbedingung; zeitinvariante Funktionale sind bei gewichtserhaltender Kontraktion für geladenes Gewicht blind. Kein konkreter geladener HH4-Nachweis. |
| NEU-193 `Dualer_Hochschildzyklus...` | `AUDIT-RECONCILED` | `SUPERSEDED_part` | Rahmen-/Blockierungsfassung. Duale Zeitwirkung und Gewichtskomplementarität bleiben als korrekte Vorarbeit; konkrete Zykluskonstruktion wird durch die zweite NEU-193-Revision ersetzt. |
| NEU-193 `Geladener_Dualzyklus_Paarungstest` | `AUDIT-RECONCILED` | `INCORPORATED` + `P09-CORE-NOGO` | Expliziter geladener Dualzyklus `z_{-lambda}^{g,p}` konstruiert, `partial z=0`. Paarung detektiert exakt `Alt_4 L`. Daher ist die vollständig symmetrische NEU-176-Schablone für diesen Nichtrandzeugen strukturell blind: Paarung identisch null `✓[M]_neg`. |
| NEU-194 | `AUDIT-RECONCILED` | `P09-CORE-NOGO` | Determinantischer Vierkochain besitzt Paarung `24`, scheitert aber am Hochschildrand: `bL_det !=0`. Endlicher isolierter Multigradträger + fixer Zielvektor wird als Kandidatenklasse ausgeschlossen; kein globaler No-go gegen geladene Vierkozyklen. |
| NEU-195 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Bewertungsderivationen liefern neutralen Cup-Kozykel. Geladene HH4-Frage wird sauber auf eine nichtinnere homogene HH1-Quelle reduziert. Innere geladene Derivationen liefern triviale Cup-Klassen. |
| NEU-196 | `AUDIT-RECONCILED` | `INCORPORATED` | Für punktierte Potentiale mit regulären Differenzen gilt `F_k(0)=0`; daher ist der Augmentationszeuge blind. Dies beweist weder `D_g=0` noch `[D_g]=0`. |
| NEU-197 | `AUDIT-RECONCILED` | `INCORPORATED` | Partieller Kommutatorquotient `Q_{h,p}` klassifiziert die antisymmetrischen Dualzyklusfunktionale. Detektion ist äquivalent zu Nichtnullheit der Quotientenklasse des Zielelements `Y`. Universeller algebraischer Detektorrahmen, aber noch kein Nichtverschwindensresultat. |
| NEU-198 | Repo-Scan | `MISSING-SOURCE` | Keine Live-Datei auffindbar. Referenzen aus NEU-199 werden nicht als eigenständige Beweisquelle migriert. |
| NEU-199 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Teilerfremde Generatorformeln der punktierten Potentialderivation und konkrete Reduktion auf `B / sum_j(1-alpha_{p_j})B` sind gültig. Nichtteilerfremder Sektor bleibt dort offen und wird erst NEU-210/211 geschlossen. |
| NEU-200 | `AUDIT-RECONCILED` | `P09-CORE-NOGO` | Alle global regulären Potentiale `H in B` sind im relevanten Quotiententest unsichtbar: Zielelement expliziter Kommutator. Ausschluss nur des regulären Untersektors. |
| NEU-201 | `AUDIT-RECONCILED` | `SUPERSEDED / P10-NOGO-CANDIDATE` | Vorgeschlagener unendlicher Primreihenkandidat und KMS-Detektor nicht belastbar; durch NEU-202 vollständig zurückgebaut. Nicht in die P09-SYN als positive Struktur übernehmen. |
| NEU-202 rev. | `AUDIT-REUSED` | `INCORPORATED-NOGO` | Drei Fehler des NEU-201-Kandidaten geschlossen: keine Normkonvergenz, keine behauptete Orthogonalität, KMS-Zustände nicht als Spuren verwendbar und auf geladenen homogenen Komponenten zeitinvariant blind. Übergeordnete singuläre Route bleibt offen. |
| NEU-203 | `AUDIT-REUSED` | `INCORPORATED_part` | Normkonvergente Potentiale liefern nur innere/traziell unsichtbare Beiträge. Korrektes Singularitätsprinzip: Potentialfolge darf divergieren, während jeder feste Generatorkommutator normkonvergiert. |
| NEU-204 | `AUDIT-REUSED` | `INCORPORATED_part` | Dyadische Schalen realisieren dieses Prinzip positiv: neutrale normunbeschränkte Derivation `A_alg -> A_C*`, nicht inner bzgl. bounded/A_C*-Implementierer. Ziel liegt nicht in `A_alg`; Kandidat ist neutral. |
| NEU-205 | `TARGETED-REAUDIT` + Archiv | `SUPERSEDED_part / P09-CORE-NOGO` | Drei konkrete dyadische geladene Platzierungen sind kandidatenspezifisch ausgeschlossen, aber mehrere Formeln der Live-Datei sind falsch. Insbesondere Sandwichformel und „Divergenz für jedes r“ sind `×[M]`. Architektur III (`N`-abhängiger relationsangepasster Twist) ist **nicht** ausgeschlossen und bleibt `?[O]`. |
| NEU-206 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Charakterkern-Erschöpfung, biorthogonale geladene Partialisometrieschalen und `E_L`-Transportformeln sind tragfähige Struktur. Allgemeine Transport-/Grenzkonvergenz noch nicht erreicht. |
| NEU-207 | `AUDIT-RECONCILED` | `INCORPORATED` + `P09-CORE-NOGO` | Exakter No-go nur für **totale eindimensionale** Teilbarkeitsketten mit mehreren Primrichtungen. Bewertungsgitter ist korrekter Transportindex; mehrdimensionale/approximative Routen bleiben offen. |
| NEU-208 | `AUDIT-REUSED` | `INCORPORATED_part` | Separierbare Primpotentiale liefern refinementstabilen neutralen mehrprimigen analytischen Kanal. Alte Max-Norm ist `×[M]`; korrekt ist die Summennorm. Naiver geladener separierbarer Sandwichansatz später negativ; allgemeine gemeinsam lokalisierte geladene Architektur offen. |
| NEU-209 | `AUDIT-REUSED` | `INCORPORATED_part` + `P09-CORE-NOGO` | Primweise Singularitäten sitzen auf `K_p` und werden von Charakterfehlern gesehen; naiver positiver separierbarer Sandwichansatz ist ausgeschlossen. `Z_g={0}` wird durch Folgeaudit/NEU-210 geschlossen. Reiner Tailkandidat scheitert. |
| NEU-210 | `AUDIT-REUSED` | `INCORPORATED_part` | Faktorielle Schalen konzentrieren die Singularität auf `{0}`, besitzen kontrolliertes Transportband und `M(0)=0 => MX_N` schließlich exakt konstant. **Nicht** korrekt ist `MX_N ->0`; dieser stärkere Punkt ist `×[M]`. |
| NEU-211 | `TARGETED-REAUDIT` / Archiv | `SUPERSEDED_part` + `INCORPORATED_corr` | Nica-/gcd-Formeln und gemischte Transportdefekte konvergieren. Geschriebenes `D_g(e(r))=0` und darauf beruhender Knoten sind `×[M]`. Korrigierte Derivation `D_g^corr` ist geladen, äußer und definiert eine nichttriviale Klasse in `HH^1(A_alg,A_C*)_g`. Algebraischer Zieltyp scheitert für diesen Kandidaten. |

---

## 3. Doppeldatei NEU-193 — kanonische Leserichtung

Die erste NEU-193-Datei stellt die duale Zeitwirkung, Gewichtskomplementarität und die Blockierungslogik bereit. Die spätere Datei `NEU-193_Geladener_Dualzyklus_Paarungstest.md` schließt die zuvor offene konkrete Zykluskonstruktion:

\[
z_{-\lambda}^{g,\mathbf p}
=
\sum_{\pi\in S_4}\operatorname{sgn}(\pi)
\varepsilon_{gP}\otimes
\mu_{p_{\pi(1)}}\otimes\cdots\otimes\mu_{p_{\pi(4)}}
\]

mit

\[
\partial z_{-\lambda}^{g,\mathbf p}=0.
\]

Für jeden Vierkochain gilt

\[
\boxed{
\langle L,z_{-\lambda}^{g,\mathbf p}\rangle
=4!\,\varepsilon\!\left(
\operatorname{Alt}_4 L(
\mu_{p_1},\mu_{p_2},\mu_{p_3},\mu_{p_4})
\right).
}
\]

Daraus folgt der verbindliche Firewall-Satz:

> Die vollständig symmetrische NEU-176-Produktfamilie kann durch diesen natürlichen geladenen Dualzyklus nicht als nichttrivial detektiert werden; ihre Paarung verschwindet identisch.

Dies ist ein mathematischer `P09-CORE-NOGO`, kein bloßer Quellenmangel.

---

## 4. NEU-194 — Alternierung allein genügt nicht

Das determinantische Modell erfüllt

\[
\langle L_\lambda^{\det},z_{-\lambda}^{g,\mathbf p}\rangle=24,
\]

aber ein direkter Hochschildtest liefert

\[
bL_\lambda^{\det}\neq0.
\]

Somit sind zwei verschiedene Anforderungen strikt zu trennen:

1. `Alt_4 L != 0` für die Nichtblindheit des Dualzeugen;
2. `bL=0` für eine Hochschildklasse.

Die spätere Cup-/Derivationsroute ist gerade deshalb strukturell bevorzugt: sie baut die Kozykelbedingung aus bereits kozyklischen Faktoren auf.

---

## 5. NEU-195–200 — vom Augmentationszeugen zum universellen Quotientendetektor

### 5.1 HH1-Reduktion

NEU-195 zeigt konditional:

\[
D_g\in Z^1(A,A)_g
\Longrightarrow
\Omega_{D_g,\mathbf p}\in Z^4(A,A)_g.
\]

Innere `D_g` liefern nur triviale Klassen. Damit wird eine **äußere geladene Derivation** zur atomaren Quelle des geladenen Cup-Pfads.

### 5.2 Augmentationsblindheit ist kein Klassen-No-go

NEU-196 beweist für die punktierte Potentialroute

\[
F_k(0)=0,
\]

also verschwindet die spezielle Augmentationspaarung. Die korrekte Interpretation lautet:

```text
ein bestimmter Zeuge ist blind
!=
alle möglichen Zeugen sind blind.
```

### 5.3 Universeller Quotientendetektor

NEU-197 definiert

\[
Q_{h,\mathbf p}
=
A_h\Big/\sum_{i=1}^4[\mu_{p_i},A_{h/p_i}].
\]

Der antisymmetrische Kettenkandidat mit homogenem Funktional `phi_h` ist genau dann ein Zyklus, wenn `phi_h` über `Q_{h,p}` faktorisiert. Eine nichtverschwindende Paarung existiert genau dann, wenn das relevante Zielelement in diesem Quotienten nicht null ist.

NEU-200 schließt daraufhin den **global regulären** Potentialsektor negativ: Für `H in B` ist das Zielelement explizit ein Kommutator. Echte Sichtbarkeit kann nur aus einer nicht global fortsetzbaren Rand-/Ursprungssingularität kommen.

---

## 6. NEU-201/202 — vollständiger Rückbau eines falschen Kandidaten

Die NEU-201-Primreihe

\[
\sum_p \frac1{\log p}\,\mu_p e(1/p)
\]

wird nicht migriert. NEU-202 rev. zeigt:

- die Partialsummen sind nicht norm-Cauchy;
- die behauptete Reihe `sum_p 1/(log p)^2 < infinity` ist falsch;
- die Summanden sind nicht orthogonal;
- der unendliche Kommutator ist daher nicht definiert;
- KMS-Zustände sind im Allgemeinen keine Spuren;
- Zeitinvarianz erzwingt sogar das Verschwinden des KMS-Werts auf den betreffenden geladenen homogenen Summanden.

P09-Provenienz:

```text
NEU-201 positiver Kandidat: SUPERSEDED.
NEU-202 Fehleraudit: INCORPORATED-NOGO.
```

Der spezifische gescheiterte Primreihenkandidat kann später als `P10-NOGO` gespiegelt werden; er ist nicht selbst P09-Kernarchitektur.

---

## 7. NEU-203/204 — positiver Methodenbeweis: singuläre Kommutatorregularisierung

Der belastbare Grundsatz lautet:

\[
X_N\ \text{muss nicht normkonvergieren},
\qquad
[X_N,a]\ \text{kann für jedes feste }a\in A_{\rm alg}
\text{ normkonvergieren}.
\]

NEU-204 realisiert dies dyadisch. Die Grenzabbildung

\[
D:A_{\rm alg}\to A_{C^*}
\]

ist eine neutrale, normunbeschränkte Derivation. Sie besitzt keinen beschränkten Implementierer aus `A_{C^*}`. Gleichzeitig gilt bereits

\[
D(\mu_2)\notin A_{\rm alg},
\]

also ist diese positive Route analytisch, nicht algebraisch-wertig.

Dies ist für P09 ein **positives Strukturresultat** und keine Lösung des geladenen Sektors.

---

## 8. NEU-205 — Targeted Reaudit: vier verbindliche Korrekturen

Das Archiv-Audit NEU-205 hat die Live-Datei deutlich revidiert.

### 8.1 Falsch orientierte Standardrelationen

Die Live-Datei schreibt in §205.1.1 die Verschiebungsrichtungen falsch. Korrekt sind unter der verwendeten Konvention u.a.

\[
e(r)\mu_k=\mu_k e(kr),
\qquad
\mu_k^*e(r)=e(kr)\mu_k^*.
\]

Die trotzdem anschließend verwendete Grundformel

\[
[V_g,e(r)]
=
\mu_m(e(nr)-e(mr))\mu_n^*
\]

ist korrekt.

### 8.2 Divergenz nicht für jedes `r`

Die Live-Datei ist zu stark. Korrekt ist nur:

> Für jedes `g!=1` existiert mindestens ein Charaktergenerator `e(r)`, dessen Kommutator für die drei konkret getesteten dyadischen Platzierungen divergiert.

Das genügt zum kandidatenspezifischen No-go. Ein universeller Satz „für jedes nichttriviale r“ ist `×[M]`.

### 8.3 Sandwichformel

Falsch in der Live-Datei:

\[
(e(mnr)-e(mr))Y_N.
\]

Korrekt:

\[
\boxed{
[\mu_mX_N\mu_n^*,e(r)]
=
\mu_mX_N(e(nr)-e(mr))\mu_n^*.
}
\]

Der konkrete dyadische Sandwichkandidat bleibt nach korrigiertem Beweis negativ; die historische Formel selbst ist `×[M]`.

### 8.4 Architektur III bleibt offen

Der in NEU-205 behauptete Ausschluss eines `N`-abhängigen relationsangepassten homogenen Twists beruht auf unbegründeten Normschlüssen. Daher:

```text
[O-205-5c] historisch ✓[M]_neg  ->  ?[O].
```

Nur die Produktabschätzung ist belastbar; beide Beiträge müssen separat kontrolliert werden.

---

## 9. NEU-206–209 — von Partialisometrieschalen zur globalen Ursprungslokalisierung

### 9.1 Geladene Partialisometrieschalen

Da ein nichtneutraler homogener Raum keine nichttrivialen Projektionen enthalten kann, benutzt NEU-206

\[
w_j=\mu_mq_j\mu_n^*.
\]

Die biorthogonale Schalenstruktur und eventuelle Kommutation mit jedem festen `e(r)` sind belastbare Teiltreffer.

### 9.2 Exakte 1D-Kette scheitert

NEU-207 beweist:

> Keine totale Teilbarkeitskette, die mindestens zwei verschiedene Primrichtungen enthält, ist unter allen Primtransporten exakt geschlossen.

Dieser Satz schließt **nicht** Bewertungsgitter, approximative Ketten oder mehrdimensionale Modelle aus. Er bleibt als `P09-CORE-NOGO` nötig, weil er die korrekte Transportgeometrie motiviert.

### 9.3 Separierbare neutrale Primkanäle

NEU-208 zeigt, dass die radiale Funktion `log(2+|alpha|_1)` unter wachsendem Primrefinement nicht stabil ist, während

\[
X_{F,\mathbf N}=\sum_{p\in F}X_{p,N_p}
\]

für jeden festen Generator nur endlich viele relevante Primrichtungen besitzt.

**Normkorrektur:** Die historische Formel

\[
\|B_k\|=\max_{p\mid k}\log\frac{v_p(k)+2}{2}
\]

ist `×[M]`. Die Primkanäle sind nicht orthogonal. Für die positiven Multiplikatoren gilt kanonisch

\[
\boxed{
\|B_k\|
=
\sum_{p\mid k}\log\frac{v_p(k)+2}{2}.
}
\]

Die Konvergenz, Neutralität und Normunbeschränktheit bleiben erhalten. Der Archiv-Audit führt entsprechend

\[
[D]\neq0\in HH^1(A_{\rm alg},A_{C^*})_1
\]

als neutralen analytischen Endbefund.

### 9.4 Warum die naive geladene Separierbarkeit scheitert

NEU-209 zeigt, dass jeder einzelne Primkanal auf der Koordinatenhyperfläche

\[
K_p=\{x_p=0\}
\]

singulär ist. Charakterfehlermultiplikatoren sehen diese Hyperflächen. Daher ist der naive positive geladene Sandwichansatz mit unabhängigen Prim-Singularitäten ausgeschlossen.

Der gemeinsame Charakterkern wird später zu

\[
Z_g=\{0\}
\]

geschlossen. Dies zwingt die nächste erfolgreiche positive Architektur zur **gemeinsamen Ursprungslokalisierung**, nicht zu unabhängigen Prim-Hyperflächen.

---

## 10. NEU-210 — faktoriales Ursprungspotential

Die faktorielle Architektur setzt

\[
L_j=(j+1)!,
\qquad
P_j=E_{L_j},
\qquad
q_j=P_j-P_{j+1},
\]

und

\[
X_N=\sum_{j=0}^{N-1}c_jq_j+c_NP_N,
\qquad c_j=\log(j+2).
\]

Belastbar:

- `Z_g={0}` für `g!=1`;
- Singularität von `X` ausschließlich am globalen Ursprung;
- für festes `k` kontrolliertes Transportband und normkonvergente Transportdifferenzen;
- für jeden lokal konstanten Multiplikator `M` mit `M(0)=0` wird `MX_N` schließlich exakt konstant.

Nicht belastbar ist die stärkere alte Forderung

\[
M_{g,r}X_N\to0.
\]

Sie ist `×[M]`. Für die Derivationskonstruktion genügt die tatsächlich bewiesene Normkonvergenz/eventuelle Konstanz.

Daher ist auch eine pauschale NEU-222-Formulierung „[O-209-6] vollständig geschlossen“ zu stark und wird nicht in P09 übernommen.

---

## 11. NEU-211 — korrigierte geladene äußere Derivation

### 11.1 Gcd-/Nica-Teil

Für `d=(n,k)`, `n=dn_0`, `k=dk_0` liefert die nichtteilerfremde Rechnung die exakten gemischten Transportformeln. Die Koeffizienten

\[
G_{a,d;N}=T_a(X_N)-\rho_d(X_N)
\]

besitzen Normgrenzwerte `G_{a,d}`.

### 11.2 Geschriebene Generatorform ist falsch

NEU-211 setzt historisch

\[
D_g(e(r)):=0.
\]

Das verletzt die BC-Kreuzrelationen und ist `×[M]`.

### 11.3 Korrigierte Generatorform

Setze

\[
C_{m,n;r}:=\lim_N (e(nr)-e(mr))X_N\in B_{\rm alg}.
\]

Dann lautet die korrekte Charakterwirkung

\[
\boxed{
D_g^{\rm corr}(e(r))
=
\mu_m C_{m,n;r}\mu_n^*.
}
\]

Zusammen mit den gcd-Transportgrenzwerten auf `mu_k` und `mu_k^*` sind dies exakt die punktweisen Normgrenzen

\[
D_g^{\rm corr}(a)
=
\lim_N[Y_N,a],
\qquad
Y_N=\mu_mX_N\mu_n^*.
\]

Für jedes feste algebraische Wort enthält die Leibnizzerlegung nur endlich viele Generatorkommutatoren. Daher existiert der Grenzwert für jedes feste `a in A_alg` und die Leibnizregel bleibt erhalten.

**Wichtig:** Die Konvergenz ist **punktweise in Norm auf jedem festen algebraischen Element**, nicht uniform auf der Einheitskugel und nicht eine Operatornormkonvergenz der Derivationen.

### 11.4 Nichtinnerheit und HH1-Klasse

Der korrigierte Offdiagonaltest liefert keinen bounded/A-C*-Implementierer. Damit gilt

\[
\boxed{
[O\text{-}211\text{-}4corr]\quad\checkmark[M]
}
\]

und

\[
\boxed{
[O\text{-charged-HH1-analytic}]\quad
[D_g^{\rm corr}]\neq0
\text{ in }
HH^1(A_{\rm alg},A_{C^*})_g.
}
\]

Dies ist das stärkste positive I2-Ergebnis.

### 11.5 Zieltyp-Firewall

Für den konkreten faktoriellen Kandidaten gilt

\[
D_g^{\rm corr}(A_{\rm alg})\not\subseteq A_{\rm alg}.
\]

Also bleibt

\[
HH^1(A_{\rm alg},A_{\rm alg})_g\neq0\;?
\]

offen. I2 darf die analytische Klasse nicht als algebraische Klasse umetikettieren.

---

## 12. Verhältnis zu NEU-222 und zum August-Finalaudit

NEU-222 ist für die I2/I3-Statuskontrolle nützlich, aber nicht uneingeschränkt autoritativ:

1. Seine pauschale Schließung von `[O-209-6]` ist gegenüber dem späteren Direktaudit zu stark; `M_{g,r}X_N ->0` ist `×[M]`, nur eventuelle Konstanz ist bewiesen.
2. Seine spätere Rotationsbegründung verwendet noch `tPhi_0=g^{-beta}Phi_0`; diese Formel wird im August-Finalaudit zurückgerollt und durch den stärkeren Unit-Slot-No-go `tPhi_0 != C Phi_0` ersetzt.

Für I2 wird NEU-222 daher als **Superseding-Scan mit lokalen Firewalls**, nicht als unfehlbare Endfassung gelesen.

---

## 13. P09/P10-Routingentscheidung für I2-No-Gos

### `P09-CORE-NOGO` — bleibt zwingend in P09

Diese Negativbefunde formen direkt den verbleibenden BC/Hochschild-Suchraum:

1. symmetrische NEU-176-Schablone ist für den natürlichen geladenen Alternierungszeugen blind;
2. determinantischer endlicher Multigrad-Kandidat paart nichttrivial, ist aber kein Kozykel;
3. reguläre Potentiale sind im partiellen Kommutatorquotienten unsichtbar;
4. normkonvergente Potentiale liefern keinen singulären äußeren Mechanismus;
5. keine nichttrivialen homogenen Projektionen in `A_g`, `g!=1`;
6. keine exakte totale 1D-Teilbarkeitskette für mehrere Primrichtungen;
7. radiale Gitterkoeffizienten sind unter Primrefinement instabil;
8. naive unabhängige Prim-Singularitäten scheitern an der geladenen Charakterkopplung;
9. starke Absorption `M X_N ->0` ist nicht notwendig und für den faktoriellen Kandidaten falsch.

Diese Punkte dürfen später in P10 gespiegelt werden, bleiben aber in P09, weil sie die positive faktorielle Architektur typisieren.

### `P10-NOGO` / Spiegelkandidaten

- der konkrete NEU-201-Primreihenkandidat;
- die drei konkreten dyadischen Ladungsplatzierungen aus NEU-205;
- weitere rein kandidatenspezifische Zwischenmodelle, sofern sie im finalen P09-Text nicht zur Erklärung der Architektur nötig sind.

### `SUPERSEDED`

- erste NEU-193-Blockierungsfassung soweit durch den konkreten Zyklus ersetzt;
- NEU-201 positive Kandidatenbehauptungen;
- NEU-205 falsche Relationsrichtungen, Sandwichformel und „Divergenz für jedes r“;
- NEU-205 behaupteter Ausschluss von Architektur III;
- NEU-208 Max-Normformel;
- NEU-210 starke Nullabsorption;
- NEU-211 `D_g(e(r))=0` und die auf dieser falschen Setzung basierende historische Fassung;
- NEU-222s alte skalare Rotationsformel (I5-Endanker hat Vorrang).

---

## 14. Verbindliche Firewalls für P09-SYN

1. **Geladener Dualzyklus != geladene HH4-Klasse.** Der Zyklus ist konstruiert; ein passender Kozykel und Nichtverschwindensnachweis bleiben separate Pflichten.
2. **Alternierung != Kozykeleigenschaft.** NEU-194 zeigt die Trennung explizit.
3. **Augmentationsblindheit != Kohomologieverschwindung.** NEU-196 schließt nur einen Zeugen aus.
4. **Regulär unsichtbar != singulär unmöglich.** NEU-200 betrifft nur global reguläre Potentiale.
5. **Singuläre Kommutatorregularisierung ist real.** NEU-204 liefert einen neutralen analytischen positiven Beweis.
6. **NEU-205 ist kandidatenspezifisch.** Kein universeller No-go gegen geladene Schalenpotentiale; Architektur III bleibt offen.
7. **Primkanäle sind nicht orthogonal.** In NEU-208 gilt die Summen-, nicht die Max-Norm.
8. **Charakterabsorption bedeutet eventuelle Konstanz, nicht notwendigerweise Null.**
9. **NEU-211 muss ausschließlich als `D_g^corr` gelesen werden.** `D_g(e(r))=0` ist verboten.
10. **Konvergenz von `ad(Y_N)` ist punktweise in Norm für jedes feste `a in A_alg`.** Keine uniformen Derivationsnormen behaupten.
11. **Geladene analytische HH1-Klasse ist bewiesen.** Sie darf nicht wieder auf `?[O]` zurückgestuft werden.
12. **Algebraische geladene HH1-Klasse bleibt offen.** Analytischer Zieltyp `A_C*` darf nicht stillschweigend zu `A_alg` werden.
13. **Kein I2-Schluss auf geladene HH4-Nichttrivialität.** Koeffizientenmodul und Cup-Aufstieg werden erst in I3 reconciliiert.
14. **NEU-198 ist keine verfügbare Primärquelle.** Keine SYN-Begründung darf allein auf diesen Namen verweisen.

---

## 15. Gegencheck-Auftrag — fünf atomare Fragen

Ein externer Gegencheck soll ausschließlich folgende Punkte prüfen:

### G1 — NEU-193/194
Ist die Leserichtung korrekt, dass der zweite NEU-193 einen echten geladenen Dualzyklus mit `partial z=0` konstruiert, die symmetrische NEU-176-Schablone wegen `Alt_4 L=0` nicht detektiert wird und das determinantische NEU-194-Modell trotz Paarung `24` wegen `bL!=0` keine Klasse liefert?

### G2 — NEU-205
Bestätigt der Archiv-Audit, dass (a) die Sandwichformel der Live-Datei falsch ist, (b) der konkrete dyadische L/R/S-Kandidaten-No-go nach Korrektur rettbar bleibt, (c) „Divergenz für jedes r“ zu stark ist und (d) Architektur III **offen** bleibt statt negativ geschlossen zu sein?

### G3 — NEU-208
Ist die korrekte Normformel

\[
\|B_k\|=\sum_{p\mid k}\log\frac{v_p(k)+2}{2}
\]

und nicht die historische Max-Norm, während der neutrale analytische Derivationsbefund erhalten bleibt?

### G4 — NEU-210/211
Ist der kanonische Endstand tatsächlich

\[
D_g^{\rm corr}(e(r))=\mu_m C_{m,n;r}\mu_n^*,
\qquad
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},A_{C^*})_g,
\]

mit **punktweiser Normkonvergenz auf jedem festen algebraischen Element**, während `D_g(e(r))=0`, globale Annihilation von `B_alg` und eine uniform/gleichmäßige Derivationsgrenze falsch sind?

### G5 — Provenienz / Reichweite
Ist es korrekt, NEU-198 als fehlende Live-Quelle nicht eigenständig zu migrieren, NEU-222 nur als lokalen späten Statusscan zu verwenden und weder aus I2 eine algebraische geladene `HH1`-Klasse noch bereits eine geladene `HH4`-Klasse zu folgern?

---

## 16. Endurteil I2

\[
\boxed{
\text{P09 / I2 PASS A COMPLETE — Gegencheck ausstehend.}
}
\]

Der entscheidende positive Fortschritt des Pakets ist die korrigierte faktorielle geladene analytische Klasse

\[
\boxed{
[D_g^{\rm corr}]\neq0
\in HH^1(A_{\rm alg},A_{C^*})_g.
}
\]

Die entscheidende verbleibende Grenze ist der Koeffiziententyp:

\[
A_{\rm alg}
\longrightarrow
A_{C^*}
\quad\text{ist geschafft,}
\qquad
A_{\rm alg}
\longrightarrow
A_{\rm alg}
\quad\text{nicht.}
\]

Der nächste interne P09-Block ist I3 (NEU-212–218), jedoch wird I2 analog zu I1 erst nach externem Gegencheck versiegelt.