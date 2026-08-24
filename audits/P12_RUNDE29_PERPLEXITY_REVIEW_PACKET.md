# P12 Runde 29 — unabhängiges Review-Paket zur ε-Brücke

**Status:** Review-Anforderung; **keine Promotion**.  
**Repo:** `Waschtl904/objekt-x-programm`, Branch `main`.  
**Kandidatenkette:**

- `cffe06b0d7d5e7da8151340d19822d9f3d7a9af8` — `audits/P12_RUNDE29_EPSILON_BRIDGE_AUDIT.md`
- `269380b8c4670a6333d170cfd30248767428c738` — `consolidation/round29_epsilon_bridge_verify.py`

**Zu prüfender Kandidat:** R29-A, ε-invarianter `M68`-Korridor durch beide `V`-Horizonwände.  
**Firewall:** P11 FROZEN; R14 unverändert; kein globaler `rho`-Descent, keine vollständige Schließung der Next-Shell-Horizon-Front, keine Objekt-X-/RH-Aussage.

---

## 1. Review-Auftrag

Bitte **nicht** lediglich den retained verifier ausführen und dessen `PASS` übernehmen.

Die Kernbehauptung von Round 29 soll unabhängig aus dem kanonischen Rohoperator

\[
Lh(u)=p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)]
\]

mit odd reflection sowie Support-/Horizon-Cutoffs neu rekonstruiert werden.

Der methodische Punkt von R29 ist bewusst anders als R28:

- Round 28 konstruierte und bewies die Nichtsingularität eines neuen `68 x 68`-Blocks.
- Round 29 behauptet **keinen neuen Determinantenblock**, sondern eine Invarianz desselben promovierten `M68` beim Hochfahren von `epsilon` durch beide `V`-Horizonwände.

Zu prüfen ist daher vor allem, ob diese Wände für das ausgewählte `M68` tatsächlich rohoperatorisch unsichtbar sind.

---

## 2. Exakte Box B29

Schreibe

\[
x=\frac\delta2+y.
\]

Der Kandidat verwendet

\[
\frac{19}{2000}<R<\frac{21}{2000},
\]

\[
|y|<\frac1{5000},
\]

\[
\frac{119}{2000}<\sigma<\frac{121}{2000},
\]

\[
\frac{139}{2000}<\varepsilon<\frac{11}{100}.
\]

Bitte mit eigenen rigorosen Schranken bestätigen:

1. `B29` liegt vollständig in
   \[
   0<R<\rho,\qquad R<x,\qquad R<\sigma<\varepsilon<E;
   \]
2. beide ersten Supportvariablen sind auf ganz `B29` live:
   \[
   \sigma+x>\kappa,\qquad \sigma-x>\eta;
   \]
3. auf ganz `B29` gilt `sigma>2 eta`;
4. die Box ist unter `J: y -> -y` invariant.

---

## 3. Beide Horizonwände und die Einzel-V-Zellen

Definiere

\[
\Phi_-:=\varepsilon+x-2\delta,
\qquad
\Phi_+:=\varepsilon-x-\delta.
\]

`Phi_->0` bedeutet Horizon-Legalität von

\[
V_-=(-1,4,4),
\]

`Phi_+>0` die von

\[
V_+=(1,4,3).
\]

Bitte unabhängig bestätigen:

### 3.1 Unterer B28-Slice

Für

\[
\frac{139}{2000}<\varepsilon<\frac{141}{2000}
\]

auf der gesamten `(R,y,sigma)`-Basis:

\[
\Phi_-<0,\qquad \Phi_+<0.
\]

### 3.2 Minus-only-Witness

Für

\[
\frac1{10000}<y<\frac1{5000},
\qquad
\frac{883}{10000}<\varepsilon<\frac{221}{2500}
\]

muss gelten

\[
\Phi_->0,\qquad \Phi_+<0.
\]

### 3.3 Plus-only-Witness

Für

\[
-\frac1{5000}<y<-\frac1{10000}
\]

und dasselbe ε-Intervall muss gelten

\[
\Phi_-<0,\qquad \Phi_+>0.
\]

Damit soll unabhängig bestätigt werden, dass `B29` beide offenen Einzel-`V`-Orientierungen tatsächlich durchquert und nicht nur die simultanen Endzustände enthält.

---

## 4. Vollständigen C44-Overlap prüfen

Der Kandidat behauptet, dass der gesamte Slab

\[
\frac{181}{2000}<\varepsilon<\frac1{10}
\]

über derselben `(R,y,sigma)`-Basis vollständig in der promovierten C44-Kammer liegt.

Bitte alle C44-Ungleichungen unabhängig prüfen:

\[
R<x<\delta-R,
\qquad
\chi-R<x<\eta+R,
\]

\[
\max\{\kappa-x,x+\eta\}<\sigma
<\min\{2\delta-x,x+\delta\},
\]

\[
\max\{2\delta-x,x+\delta\}<\varepsilon<E.
\]

Dieser Punkt ist wichtig: R29 soll nicht bloß eine Einzel-`V`-Witnessbox liefern, sondern einen **offenen Faser-Korridor vom promovierten B28-Slice bis in C44 hinein**.

---

## 5. Die zentrale Invariante adversarial prüfen

Verwende exakt dieselbe 68-Quellen-Menge `S68` wie in Round 28.

Bitte unabhängig bestätigen:

1. `V_- = (-1,4,4)` und `V_+ = (1,4,3)` gehören nicht zu `S68`;
2. für jede ausgewählte Quelle hängt die Sichtbarkeit der sechs Shift-Slots nur von `(R,x,sigma)`, nicht von `epsilon`, ab;
3. `epsilon` tritt im ausgewählten Rohzertifikat nur in den Source-upper-Bedingungen
   \[
   T+\varepsilon-u_s>0
   \]
   auf;
4. davon gibt es genau 68;
5. ihr `epsilon`-Koeffizient ist jeweils exakt `+1`;
6. daher ist Source-Horizon-Legalität der ausgewählten 68 Quellen beim Erhöhen von `epsilon` monoton;
7. weder
   \[
   \varepsilon+x-2\delta
   \]
   noch
   \[
   \varepsilon-x-\delta
   \]
   ist eine Rohwand des ausgewählten `M68`-Zertifikats.

Insbesondere bitte prüfen, dass keine indirekte Shift-Slot-Bedingung doch eine der beiden `V`-Wände reproduziert.

---

## 6. Alle 1204 Rohbedingungen über B29 neu prüfen

Der retained Kandidat erzeugt wie R28 insgesamt

\[
\boxed{1204}
\]

Source-/Sign-/Support-/Horizon-Bedingungen.

Bitte unabhängig rekonstruieren:

- 68 Source-lower;
- 68 Source-upper;
- Vorzeichen sämtlicher sechs Shift-Slots pro Quelle;
- korrekte odd reflection;
- live / dead-lower / dead-upper Klassifikation;
- obere Supportgrenze `T+sigma`;
- Source-Horizongrenze `T+epsilon`.

Bitte die gesamte Box `B29` rigoros zertifizieren, nicht nur Referenzpunkte sampeln.

Retained Zielwert für die kleinste positive Rohmarge:

\[
>0.00157927617278058.
\]

Da die ε-Untergrenze dieselbe wie in B28 ist und alle ε-abhängigen Rohbedingungen monoton steigen, sollte die minimale Rohmarge identisch zur Round-28-Marge sein. Dies bitte unabhängig bestätigen oder widerlegen.

---

## 7. Identität mit dem promovierten M68

Am Referenzpunkt

\[
(R,x,\sigma,\varepsilon)
=\left(0.010,\frac\delta2,0.060,0.070\right)
\]

muss die Round-29-Rekonstruktion exakt dieselben

- 68 Quellen,
- 68 Variablen,
- Koeffizienten und
- Zeilen-/Spaltenordnung

wie der promovierte Round-28-Block liefern.

Bitte anschließend mindestens je einen inneren Punkt aus allen vier Horizonorientierungen prüfen:

1. beide `V` illegal;
2. nur `V_-` legal;
3. nur `V_+` legal;
4. beide `V` legal.

Die behauptete Aussage ist coefficient-for-coefficient

\[
M_{68}^{(1)}=M_{68}^{(2)}=M_{68}^{(3)}=M_{68}^{(4)}.
\]

Wenn diese Identität und die vollständige Boxstabilität stimmen, darf die bereits unabhängig geprüfte und promovierte Round-28-Nichtsingularität

\[
\det M_{68}\ne0
\]

übernommen werden; eine neue Determinantenpolynomrechnung ist dann logisch nicht erforderlich.

---

## 8. Gewünschtes Verdict

Bitte am Ende getrennt ausgeben:

```text
R29-A B29 AMBIENT / C44 OVERLAP: GREEN / PARTIAL / FAIL
R29-A SINGLE-V ORIENTATIONS:      GREEN / PARTIAL / FAIL
R29-A EPSILON INVARIANT:          GREEN / PARTIAL / FAIL
R29-A 1204 RAW PATTERN:           GREEN / PARTIAL / FAIL
R29-A SAME PROMOTED M68:          GREEN / PARTIAL / FAIL
R29-A OVERALL:                    GREEN / PARTIAL / FAIL
```

Bei `PARTIAL` oder `FAIL` bitte die **erste konkrete mathematische Stelle** nennen, an der die unabhängige Rekonstruktion vom Kandidaten abweicht.

---

## 9. Erlaubte Aussage bei vollständig unabhängigem GREEN

Bei vollständigem GREEN darf formal gesagt werden:

> Auf der exakten `J`-symmetrischen Box `B29` bleibt der promovierte invertierbare Round-28-Rohblock `M68` beim Erhöhen von `epsilon` coefficient-for-coefficient unverändert. Die Box enthält offene Bereiche mit beiden illegalen `V`-Quellen, genau einer legalen `V`-Quelle auf jeder `J`-Seite und beiden legalen `V`-Quellen; ihr oberer Slab überlappt offen mit C44. Daher gilt auf ganz `B29` lokal `h(x)=h(delta-x)=0`. Dies ist ein lokaler `✓[M]_part`-ε-Korridor.

Nicht erlaubt sind daraus folgende stärkere Formulierungen:

- vollständige Schließung aller Einzel-`V`-Zellen;
- vollständige Schließung der gesamten Next-Shell-Horizon-Front;
- globaler `rho`-Descent;
- neue globale Radius-Schwelle;
- Schließung des tiefen Horizon- oder Outer-Core-Rests;
- P11-/R14-Konsequenzen;
- Polar Gauge, Strong/Terminal Transport, Objekt X oder RH.

**Promotion ausschließlich nach unabhängigem GREEN.**
