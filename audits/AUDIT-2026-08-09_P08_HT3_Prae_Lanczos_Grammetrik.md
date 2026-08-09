# P08 Pass A — H-T3 Prä-Lanczos-Grammetrik

**Datum:** 9. August 2026  
**Paket:** H-T3  
**Prüfart:** `AUDIT-RECONCILED` + lokale `TARGETED-REAUDIT`s  
**Scope:** NEU-127, NEU-128A, NEU-128b, NEU-130, NEU-131; superseding P05/P06; Quellcheck `prolate-gram-coercivity/paper7_skeleton.tex`

## 0. Endstatus vorweg

\[
\boxed{\text{H-T3 COMPLETE — keine intrinsische Prä-Lanczos-Metrik konstruiert; mehrere historische Typ-/Scope-/Cancellationaussagen demotiert.}}
\]

Der positive Kern lautet: Die Suche nach einer positiven nichtskalaren Prä-Lanczos-Form ist methodisch sinnvoll. Der historische Klasse-B-/PSWF-Strang liefert dafür aber noch keinen kanonischen globalen Operator.

---

## 1. Bindende Firewalls

### P05

Rang- und Gewichtsaussagen werden nur im zulässigen relativen Modellscope übernommen:

\[
\operatorname{rank}C_p^{\rm rel}[\widehat\varepsilon_p]\le1,
\qquad
P_p=|c_p|^2\Pi_p^{(1)}.
\]

`P_p` ist im Allgemeinen kein orthogonaler Projektor. Nichtentartung `c_p\neq0`, Hebungsunabhängigkeit und eine termweise Asymptotik für `|c_p|^2` bleiben offen.

### P06

Der historische antisymmetrische Anteil und der relative Transportgenerator werden nicht identifiziert:

\[
J_N^-\text{ schiefadjungiert},
\qquad
S_N=-iJ_N^-\text{ selbstadjungiert},
\]

während `D_rel` in den auditierten Primfasern separat als Transportgenerator charakterisiert ist.

---

## 2. NEU-127 — Triage bleibt, Doppelbarrierenstatus korrigiert

NEU-127 ist als Suchregister nützlich. Die sechs Kriterien — Prä-Lanczos-Lage, Positivität, Nichtskalarität, Intrinsizität, Selbstadjungiertheits/Herglotz-Kompatibilität und Zweistufen-Kontrolle — bleiben als methodische Filter erhalten.

### 2.1 Überstarker Eingangssatz

NEU-127 behandelt

\[
b_{1,N}\to0,
\qquad
b_{2,N}/b_{1,N}\to\infty
\]

als feststehende Doppelbarriere.

Nach H-T2 gilt jedoch:

- `b_{1,N}->0`: `✓[M]`;
- finite wachsende Daten für `b2/b1`: `✓[M]_{num}`;
- `b2/b1->infinity`: `?[O]` streng.

Die Zweistufen-Kontrolle bleibt deshalb ein sinnvoller notwendiger Kandidatentest, darf aber nicht auf einem bereits bewiesenen zweiten Grenzwert aufgebaut werden.

### 2.2 Klasse-B-Typisierung

Historische Einträge `C_p^#C_p`, `C_pC_p^#` und `Sigma_N(beta)` werden nicht als global gesicherte Rang-eins-Geometrie gelesen. P05 erlaubt Rang-eins nur für die induzierte relative Modellrealisierung.

**Status NEU-127:** `✓[M]` als Triage; einzelne historische Kandidatenbeschreibungen `SUPERSEDED_part` durch P05/H-T2.

---

## 3. NEU-128A — formale Self-Energy-Struktur, kein globaler Rang-eins-Satz

NEU-128A schreibt historisch

\[
C_pC_p^\#=|\Psi_p\rangle\langle\Psi_p|
\]

und nennt dies einen Rang-eins-Projektor. Zwei Korrekturen sind bindend:

1. selbst im Rang-eins-Modell ist der gewichtete Operator im Allgemeinen **kein orthogonaler Projektor**;
2. P05 friert die Rang-eins-Aussage nur für `C_p^rel` im induzierten relativen Modell ein, nicht für den vollen historischen Kanaloperator `C_p`.

Die formale endliche Faktorisierung

\[
\Sigma_N(\beta)=C_NE_N(\beta)^{-1}C_N^\#
\]

kann als Modellformel relativ zu den historischen Typannahmen und einer gewählten Hebung weiterverwendet werden. Sie ist aber kein intrinsischer globaler Objekt-X-Gramsatz.

Hebungsunabhängigkeit bleibt `?[O]`.

**Status:**

- historischer „Projektor“-Typ: `×[M]`;
- globale Rang-eins-Lesart für `C_p`: nicht migrieren;
- modellrelative/formale Self-Energy-Faktorisierung: `CONDITIONAL / ✓[M]_{model}`;
- kanonische Prä-Lanczos-Metrik: `?[O]`.

---

## 4. NEU-128b — Ebenendiagnose erhalten, Formel lokal korrigiert

Die starke Seite von NEU-128b bleibt die Ebenentrennung:

\[
\Sigma_N(\beta):\mathcal H_{J,N}\to\mathcal H_{J,N}
\]

ist historisch Jacobi-/Zielseiten-Self-Energy, während ein echter Prä-Lanczos-Kandidat auf der Ausgangs-/Feshbach-Ebene leben müsste.

Auch die `beta`-Firewall bleibt richtig:

- festes reelles `beta_0>0`: positive Gewichte im historischen Modell;
- mitlaufendes komplexes/spektrales `beta`: keine feste positive Metrik.

### 4.1 Operator/Skalar-Typfehler

NEU-128b schreibt

\[
\Sigma_N(\beta)x
=\sum_p w_p|\langle\Psi_p,x\rangle|^2.
\]

Das ist falsch getypt. Korrekt ist im historischen Rang-eins-Modell entweder

\[
\Sigma_N(\beta)x
=\sum_p w_p\Psi_p\langle\Psi_p,x\rangle,
\]

oder die Quadratform

\[
\langle x,\Sigma_N(\beta)x\rangle
=\sum_p w_p|\langle\Psi_p,x\rangle|^2.
\]

### 4.2 P05-Scope

Auch die korrigierte Form ist nur innerhalb eines sauber typisierten relativen/Modell-Scopes als Rang-eins-Summe zulässig. Die bloße Ersetzung „Projektor“ durch „positiver Rang-eins-Operator“ macht die historische volle `C_p`-Aussage noch nicht P05-konform.

**Status:** Ebenendiagnose und beta-Fixierungslogik `✓[M]`; Rang-eins-/Gram-Realisierung nur modellrelativ/conditional; Prä-Lanczos-Lift `?[O]`.

---

## 5. NEU-130 — PSWF nur als Methodenheuristik

NEU-130 sagt ausdrücklich, die PSWF- und Jacobi-Kontrollfragen seien formal nicht identisch. Das ist die bindende Lesart.

Erhalten bleibt die Heuristik:

> Kritische Rand-/Krylov-Schichten sollten möglicherweise über koerzive/energetische Kontrolle statt nur über punktweise Matrixelementabschätzungen behandelt werden.

Nicht als mathematischer Satz migriert werden:

- „strukturelle Äquivalenz“ im starken Sinn;
- die Behauptung, `H_lim`, `D_Edge` und `D_rel` seien nachgewiesene Projektionen desselben Objekts;
- die historische Identität
  \[
  D_{\rm rel}=\overline{iJ^-}
  \]
  als durch P06 etablierte Operatoridentität.

Dass `iJ^-` bei schiefadjungiertem `J^-` selbstadjungiert ist, ist eine reine Typaussage; sie identifiziert diesen Operator nicht mit dem separat auditierten Transportgenerator `D_rel`.

**Status NEU-130:** `HEURISTIC / methodische Analogie`; keine neue `✓[M]`-Operatorbrücke.

---

## 6. NEU-131 / Paper VII — Schur-/Nelson-Brücke nicht bewiesen

Der direkte Quellcheck von `prolate-gram-coercivity/paper7_skeleton.tex` zeigt zwei konkrete mathematische Defekte.

### 6.1 Skalierungsfehler

B-strong lautet

\[
P_{kl}\le C_2c^{1/2}.
\]

Paper VII definiert anschließend

\[
A_{ij}:=P_{ij}c^{1/2}
\]

als normalisierte O(1)-Amplitude. Aus der angegebenen B-strong-Schranke folgt aber

\[
A_{ij}\le C_2c,
\]

nicht O(1).

Damit ist die behauptete H3-Verifikation mit dieser Skalierung nicht gültig.

### 6.2 Cancellation kontrolliert signierte Summen, nicht absolute Schur-Summen

Der abstrakte Satz betrachtet

\[
T_{ij}=\frac{A_{ij}}{|i-j|}e^{i\Phi_{ij}}
\]

und leitet aus Abel-/Dirichlet-Cancellation für dyadische **signierte** Blocksummen anschließend

\[
\sup_i\sum_{j\ne i}|T_{ij}|=O(1)
\]

ab.

Dieser Schluss ist falsch. Gegenbeispiel:

\[
T_{ij}=\frac{e^{i\alpha(i-j)}}{|i-j|},
\qquad \alpha\not\equiv0,\pi.
\]

H1–H3 gelten mit konstanter Amplitude. Die signierten dyadischen Summen cancellieren, aber

\[
\sum_{j\ne i}|T_{ij}|
=\sum_{j\ne i}\frac1{|i-j|}
\asymp\log N.
\]

Oszillation kann eine absolute Summe nicht durch Phasenkancellation verkleinern.

### 6.3 Konsequenz für NEU-131

Der historische Schluss

\[
\text{Punktschranke + Cancellation}
\Longrightarrow
\text{absolute Schur-/Nelson-Energiekontrolle}
\]

ist nicht bewiesen.

Erhalten bleibt nur die qualitative Beobachtung, dass eine zusätzliche Cancellation-/Kommutatorstruktur für **signierte/operatorische** Summen relevant sein kann. Für eine Nelson- oder Schurkontrolle ist ein separater, korrekt formulierter Operatornorm-, Quadratsummen- oder Orthogonalitätsmechanismus nötig.

**Status:**

- konkreter Schur-Schluss in Paper VII: `×[M]`;
- behauptete H3-Normalisierung: `×[M]`;
- NEU-131 als formales Brückenlemma: `?[O]`;
- qualitative Methodenanalogie: erhalten, nicht als Satz.

---

## 7. H-T3 Statusmatrix

| Punkt | Endstatus |
|---|---|
| NEU-127 Triagekriterien | `✓[M]` methodisch |
| `b1->0` | `✓[M]` |
| `b2/b1->infinity` | `?[O]` streng; finite Numerik vorhanden |
| historischer Rang-1-Projektor | `×[M]` |
| Rang <=1 für `C_p^rel` im Modell | `✓[M]` gemäß P05 |
| Rang-eins-Aussage für vollen `C_p` | nicht migrieren |
| NEU-128A formale `Sigma=C E^-1 C#`-Struktur | `CONDITIONAL / model-relative` |
| Hebungsunabhängigkeit | `?[O]` |
| NEU-128b Ebenendiagnose | `✓[M]` |
| NEU-128b Operator/Skalar-Formel | `×[M]`, korrigiert im Audit |
| fixer reeller positiver beta-Parameter | `✓[M]` als Positivitätsvoraussetzung im Modell |
| Prä-Lanczos-Lift von `Sigma` | `?[O]` |
| NEU-130 PSWF-Brücke | `HEURISTIC`, kein Beweissatz |
| `D_rel=closure(iJ^-)` als P06-Satz | nicht etabliert / nicht migrieren |
| Paper-VII Skalierung `A=P c^(1/2)` + B-strong | `×[M]` |
| Cancellation => absolute Schur-Zeilensumme | `×[M]` |
| NEU-131 formales Edge-Schur-Nelson-Lemma | `?[O]` |
| intrinsische positive nichtskalare Prä-Lanczos-Metrik `W_N` | `?[O]` |

---

## 8. Endurteil und Routing

\[
\boxed{\text{H-T3 COMPLETE — kein }W_N\text{ konstruiert; historische Klasse-B-/PSWF-Brücke nur partiell verwertbar.}}
\]

Der belastbare P08-Kern lautet:

1. Eine nichtskalare positive Prä-Lanczos-Geometrie bleibt ein legitimer offener Ausweg aus der skalaren H-T2-Barriere.
2. Historische Self-Energy-Faktorisierungen dürfen nur modellrelativ und P05-getypt verwendet werden.
3. Die Jacobi-seitige Self-Energy ist noch kein intrinsischer Prä-Lanczos-Operator.
4. PSWF liefert derzeit nur eine Methodenheuristik, keine Operatoridentifikation.
5. Der konkrete Schur-/Nelson-Brückenschritt aus NEU-131/Paper VII ist mathematisch fehlerhaft und darf nicht in P08-SYN migriert werden.

**Nächster P08-Pass-A-Schritt:** H-T4 = NEU-132–145. Dort sind insbesondere `c_p`-Schranken, Self-Energy/Schatten/Fredholm, T2-/Edge-Label und Mangoldt-Renormierung gegen P05/P06 zu reconciliieren. Der historische Verweis auf NEU-44 bleibt eine Provenienzreferenz, ist aber nicht der nächste P08-Prüfblock.