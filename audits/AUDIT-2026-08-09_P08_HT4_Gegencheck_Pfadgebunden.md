# P08 Pass A — H-T4 Gegencheck, pfadgebunden

**Datum:** 9. August 2026  
**Scope:** hochgeladener H-T4-Gegencheck zu NEU-132–145  
**Bindende Oberquellen:** P05/P06, H-T2, H-T3 sowie Live-Dateien NEU-132–145 und NEU-44/44.X/44.R.

## 0. Urteil zum Gegencheck

Der Gegencheck ist als Triage hilfreich, aber nicht als H-T4-Endaudit übernehmbar. Er erklärt H-T4 für `COMPLETE`, obwohl mehrere Dateien noch als `TARGETED-REAUDIT` oder sogar nur vermutet klassifiziert werden. Die Live-Prüfung liefert mehrere stärkere mathematische Gegenbefunde.

## 1. NEU-132/133 — Primclock-Cancellation

Die vorgeschlagene ungewichtete Schranke

\[
\left|\sum_{p\in[P,2P]}p^{-iu}\right|\le C/|u|
\]

ist in dieser P-unabhängigen Form falsch. Für festes `u` liefert PNT/partielle Summation eine Größe derselben Hauptordnung wie `P/log P` bis auf einen u-abhängigen komplexen Faktor; über eine dyadische Schale wächst die Phasenlänge `u log 2` nicht mit P.

NEU-133 verschärft den Fehler durch die Behauptung

\[
\sum_{p\le X}p^{-iu}=o(\pi(X))
\]

für festes `u != 0`. Auch das ist falsch.

Mit zusätzlichem Gewicht `1/p` ist die Lage anders: auf der m-ten Primschale ist die natürliche Größenordnung typischerweise harmonisch `O(1/m)`, nicht `O(2^{-m})`.

**Bindung:** Der konkrete H1-rel-/Abel-Kern aus NEU-132/133 ist `×[M]`; die bloße dyadische Primschalenorganisation bleibt als Methodenrahmen verwendbar.

## 2. NEU-134/135/135D — Kanalgewicht

Die Formel

\[
|c_p|^2=(\log p)^2 B_p
\]

ist nur im historischen induzierten relativen Modell zu lesen. Der entscheidende quantitative Schritt

\[
B_p=O(1/p)
\]

wird in NEU-134/135D nicht bewiesen. Daher ist

\[
|c_p|^2=O((\log p)^2/p)
\]

keine unbedingte P05-Aussage.

Die Welt-2-Norm `||epsilon_p||=1` ist als Modellkonvention zulässig, nicht als Beweis des quantitativen p-Abfalls.

## 3. NEU-136 — drei Gegenbefunde

Die algebraische Zerlegung

\[
\frac1{1-p^{-\beta}}=1+\frac{p^{-\beta}}{1-p^{-\beta}}
\]

und damit `Sigma = Sigma^infty + Sigma^ren` ist korrekt.

Dagegen sind drei weitere Aussagen zu korrigieren:

1. PNT ergibt
   \[
   \sum_{p\le N}\frac{(\log p)^2}{p}\sim \frac12(\log N)^2,
   \]
   nicht `(log N)^3/3`.
2. Aus einer bloßen Obergrenze `||C_p^rel||^2 = O((log p)^2/p)` folgt keine Divergenz des rohen Anteils. Dafür wäre eine Untergrenze oder Asymptotik nötig.
3. Allgemein gilt nicht `||CC^#||_{S1} <= ||C||_op^2`. Für Hilbert-Schmidt-C gilt `||CC^*||_{S1}=||C||_{S2}^2`; die Gleichheit mit der Operatornormquadratur ist rang-eins-spezifisch.

**Bindung:** Zerlegung `✓[M]`; behaupteter log-kubischer Grad `×[M]`; Rohdivergenz aus dem vorliegenden Upper Bound `?[O]`; S1-Route nur im P05-modellrelativen Rang-eins-Scope und unter quantitativer c_p-Schranke conditional.

## 4. NEU-137 — Spurklasse nur conditional/model-relative

Für festes `beta>0` ist der Majorantenbeweis korrekt, **wenn** zugleich gelten:

- die induzierte Rang-<=1-Realisierung aus P05,
- die quantitative Schranke `|c_p|^2=O((log p)^2/p)`.

Beides darf nicht als globale intrinsische Objekt-X-Aussage gelesen werden; insbesondere ist die quantitative Schranke im frozen P05 nicht bewiesen.

Die behauptete S1-Divergenz bei `beta downarrow 0` benutzt eine nicht bewiesene untere Schranke und bleibt `?[O]`.

## 5. NEU-138/139 — Fredholm und Kreuzterme

Reine Fredholm-Theorie bleibt conditional auf `Sigma^ren in S1` korrekt.

Nicht korrekt ist die primweise Eigenwert-/Produktlesart ohne Orthogonalität. Bei nichtorthogonalen Rang-eins-Bildern ist

\[
\Sigma=\sum_p w_pP_p
\]

nicht diagonal in p; `w_p|c_p|^2` sind nicht automatisch Eigenwerte der Gesamtsumme.

NEU-139 identifiziert T2 zu Recht als offene Orthogonalitätsfrage. Seine Formel für den zweiten Moment enthält jedoch einen zusätzlichen falschen Vorfaktor. Korrekt ist

\[
\operatorname{Tr}(\Sigma^2)=\sum_{p,q}w_pw_q\operatorname{Tr}(P_pP_q).
\]

## 6. NEU-140/141 — Mangoldt-Renormierung

Die Definition

\[
R_p^{Mang}=\frac{\log p}{|c_p|^2}
\]

setzt `c_p != 0` für jeden Primkanal voraus. Nach P05 ist genau diese Nichtentartung offen.

Zusätzlich benötigt eine kanonische primdiagonale Realisierung T2 bzw. eine intrinsische orthogonale Primfaserzerlegung. Diese ist ebenfalls nicht global bewiesen.

Unter diesen Zusatzannahmen ist die gewöhnliche Mangoldt-Reihe im Bereich `Re beta>1` korrekt; global bleibt die Operatorrealisierung conditional/open.

## 7. NEU-142/143/144 — Edge-Label

NEU-142s Bifurkation ist korrekt: orthogonale Edge-Labels implizieren T2; Zielindex-Labels nicht.

NEU-143 beweist T2 jedoch nur **unter** der Annahme

\[
W_{res,rel}=\bigoplus_{(m,p)}^\perp H_{m\to pm}.
\]

Der alte NEU-44-Kantendiagonalitätstest führt diese Struktur als explizite `Variante B` **per Definition** ein und lässt die intrinsische Herleitung aus `Wres_BC^top` offen. Die spätere rekonstruierte NEU-44-Datei importiert die Edge-Summe als Grunddefinition und verweist dabei auf NEU-143; das ist keine unabhängige Beweiskette.

NEU-144 stuft T2 daher zu stark auf `erledigt` hoch. Außerdem setzt es `|c_p|^2>0` voraus, was P05 offen lässt.

Die angegebene Domäne von R ist für eine nichtnormierte orthogonale Familie unvollständig: bei `xi=sum xi_p Psi_p` muss die Norm der Basisvektoren in der Summierbarkeitsbedingung erscheinen.

## 8. NEU-145 — regulierte Spur

Die Definition

\[
Tr_{reg}(R\Sigma)(\beta):=AC[-\zeta'/\zeta](\beta)
\]

ist als **Definition/arithmetic restatement** legitim, aber keine operatorielle Realisierung.

Bei einer Zeta-Nullstelle `rho` der Vielfachheit `m_rho` ist das Residuum von `-zeta'/zeta` gleich `-m_rho`, nicht automatisch `-1`.

Der glatte Cutoff `chi_Lambda(R)` führt exakt zu Gewichten `chi_Lambda(R_p)`; er ist nicht identisch mit einem harten Summationscutoff `R_p<=Lambda`, solange `chi` nicht als Projektion gewählt wird.

Die Wärmeheuristik `R_p ~ p/log p` ist ebenfalls zu stark: aus den historischen Daten folgt allenfalls conditional eine untere Wachstumsschranke, keine Asymptotik.

## 9. Gegencheck-Endurteil

\[
\boxed{\text{Der eingereichte H-T4-Gegencheck wird nicht unverändert gebunden.}}
\]

Erhalten bleiben seine richtige Scope-Triage, die Aufmerksamkeit für H-T3-Cancellation und die algebraische beta-Renormierungszerlegung. Korrigiert werden insbesondere NEU-132/133, NEU-136, die globale S1-Hochstufung, T2/Edge-Label, Nichtentartung und die operatorielle Mangoldt-Realisierung.
