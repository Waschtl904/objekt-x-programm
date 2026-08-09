# P08 Pass A — H-T4 Selbstenergie, Spurklasse, Mangoldt

**Datum:** 9. August 2026  
**Scope:** NEU-132–145; Quellabgleich NEU-44/44.X/44.R; P05/P06 sowie H-T2/H-T3 bindend.

## Endstatus

\[
\boxed{\text{H-T4 COMPLETE — beta-Zerlegung erhalten; Primeclock-Abelpfad fehlerhaft; Spur-/Mangoldt-Kette nur conditional/model-relative.}}
\]

## 1. NEU-132/133 — Primeclock-Abel

Die dyadische Primschalenorganisation bleibt methodisch brauchbar. Nicht haltbar ist dagegen die vorgeschlagene P-unabhängige Schranke

\[
\left|\sum_{p\in[P,2P]}p^{-iu}\right|\le C/|u|.
\]

Für festes u liefert PNT/partielle Summation eine Größe von Ordnung P/log P bis auf einen u-abhängigen Faktor; die Phase u log p durchläuft auf [P,2P] nur ein Intervall fester Länge u log 2. Ebenso ist NEU-133s Behauptung `sum_{p<=X} p^{-iu}=o(pi(X))` für festes u unzutreffend.

Mit zusätzlichem 1/p-Gewicht ist die natürliche Primschalengröße harmonisch, nicht exponentiell:

\[
\#\mathcal P_m\asymp 2^m/m,\qquad
\sum_{p\in\mathcal P_m}1/p\asymp1/m,\qquad
\sum_{p\in\mathcal P_m}(\log p)/p\asymp1.
\]

**Status:** NEU-132 Methodenrahmen `✓[M]`; ungewichtete H1-rel-Schranke `×[M]`; NEU-133 konkreter Abel/H1-Kern `×[M]`; ein korrekt gewichtetes Ersatzlemma `?[O]`.

## 2. NEU-134–135D — Kanalgewicht

Im induzierten relativen Modell gilt formal

\[
|c_p|^2=(\log p)^2B_p.
\]

Die Welt-2-Norm `||epsilon_p||=1` ist als Modellkonvention zulässig. Der quantitative Schritt

\[
B_p=O(1/p)
\]

wird jedoch nicht bewiesen. Deshalb bleibt `|c_p|^2=O((log p)^2/p)` conditional/model-relative und ist keine frozen-P05-Aussage.

**Status:** Normkonvention `✓[M]_{model}`; B_p-Abfall `?[O]`; globale termweise p-Asymptotik nicht migrieren.

## 3. NEU-136 — Zerlegung ja, Divergenzbehauptungen nein

Algebraisch korrekt ist

\[
(1-p^{-\beta})^{-1}=1+\frac{p^{-\beta}}{1-p^{-\beta}},
\]

also formal `Sigma_rel = Sigma_rel^infty + Sigma_rel^ren(beta)`.

Drei historische Aussagen werden korrigiert:

1. Nach PNT gilt
   \[
   \sum_{p\le N}\frac{(\log p)^2}{p}\sim\frac12(\log N)^2,
   \]
   nicht `(log N)^3/3`.
2. Ein Upper Bound `|c_p|^2=O((log p)^2/p)` beweist keine Divergenz des tatsächlichen rohen Anteils. Dazu fehlt eine Untergrenze/Asymptotik.
3. Allgemein gilt nicht `||CC#||_{S1} <= ||C||_op^2`. Für Hilbert-Schmidt-C gilt `||CC*||_{S1}=||C||_{S2}^2`; die Gleichheit mit der Operatornormquadratur ist rang-eins-spezifisch.

**Status:** algebraische Zerlegung `✓[M]`; log-kubischer Grad `×[M]`; Rohdivergenz `?[O]`; S1-Route nur conditional im P05-Rang-eins-Modell plus quantitative c_p-Kontrolle.

## 4. NEU-137 — Spurklasse

Unter

- `rank C_p^rel <= 1` im induzierten P05-Modell und
- `|c_p|^2=O((log p)^2/p)`

folgt für jedes feste beta>0 die absolute S1-Konvergenz von `Sigma_rel^ren(beta)`, gleichmäßig für beta>=beta0>0. Das Majorantenargument ist dann korrekt.

Die behauptete S1-Divergenz bei beta downarrow 0 ist nicht aus dem Upper Bound ableitbar.

**Status:** feste-beta S1 `CONDITIONAL ✓[M]_{model}`; global/intrinsisch `?[O]`; beta→0-Divergenz `?[O]`.

## 5. NEU-138/139 — Fredholm und Kreuzterme

Falls `Sigma^ren in S1`, sind Fredholm-Determinante, Potenzspuren und die erste Spur wohldefiniert.

Ohne T2/Orthogonalität sind

\[
w_p|c_p|^2
\]

aber nicht automatisch Eigenwerte der Gesamtsumme `Sigma=sum_p w_p P_p`. Daher ist ein reines Primfaktor-/Ihara-Produkt nicht aus NEU-138 bewiesen.

NEU-139s T1/T2-Triage ist nützlich. Lokal falsch ist dort die Formel für die zweite Spur mit einem zusätzlichen Gesamtfaktor. Korrekt:

\[
\boxed{Tr(\Sigma^2)=\sum_{p,q}w_pw_qTr(P_pP_q).}
\]

Im Rang-eins-Modell gilt `Tr(P_pP_q)=|<Psi_p,Psi_q>|^2`.

**Status:** Fredholm-Basistheorie `CONDITIONAL ✓[M]`; primeweise Eigenwertlesart ohne T2 `×[M]`; T2 `?[O]`; NEU-139 zweite-Spur-Formel lokal `×[M]`.

## 6. NEU-140/141 — Mangoldt-R

Die primweise Normierung

\[
R_p^{Mang}=\frac{\log p}{|c_p|^2}
\]

benötigt zwei zusätzliche Voraussetzungen:

1. `c_p != 0` für jeden relevanten Primkanal;
2. T2 bzw. eine kanonische primdiagonale Zerlegung.

Beides bleibt nach P05 offen. Unter diesen Annahmen gilt formal `Tr(R P_p)=log p`; mit dem historischen Upper Bound folgt zusätzlich `R_p^{Mang} \gtrsim p/log p`.

Die gewöhnliche Mangoldt-Dirichletreihe konvergiert absolut für Re beta>1. Die entsprechende S1-Aussage ist aber nur innerhalb dieser bedingten diagonalisierten Modellrealisierung gültig.

**Status:** Normierungstrennung `✓[M]`; konkrete primdiagonale Operatorrealisierung `?[O]/CONDITIONAL`.

## 7. NEU-142/143 — Edge-Label und T2

NEU-142s Bifurkation ist korrekt: orthogonale Edge-Labels implizieren T2, reine Zielindex-Labels nicht.

NEU-143 beweist T2 korrekt **unter**

\[
W_{res,rel}=\bigoplus_{(m,p)}^\perp H_{m\to pm}.
\]

Die Provenienz ist jedoch nicht intrinsisch geschlossen. Der historische NEU-44-Kantendiagonalitätstest führt diese Paarung als `Variante B` **per Definition** ein und lässt ihre Herleitung aus `Wres_BC^top` offen. Die spätere rekonstruierte NEU-44-Datei übernimmt die Edge-Summe als Grunddefinition und verweist rückwärts auf NEU-143.

Damit entsteht keine unabhängige intrinsische T2-Beweiskette.

**Status:** NEU-142 `✓[M]` als Bifurkationslemma; NEU-143 `✓[M]` conditional; intrinsisches T2 `?[O]`.

## 8. NEU-144 — R noch conditional

NEU-144 stuft T2 zu stark als erledigt hoch und setzt zusätzlich `|c_p|^2>0` voraus. P05 lässt Nichtentartung offen.

Für eine orthogonale, aber nicht normierte Familie `Psi_p` ist außerdem die angegebene Domäne unvollständig. Bei `xi=sum xi_p Psi_p` lautet die natürliche Bedingung

\[
\sum_p R_p^2|\xi_p|^2\|\Psi_p\|^2<\infty.
\]

Selbstadjungiertheit folgt erst nach sauberer abgeschlossener orthogonaler Zerlegung und maximaler Multiplikationsdomäne.

Die Identität `Tr(R Sigma^ren)=-zeta'/zeta` für Re beta>1 ist daher ein conditionaler Modellsatz.

## 9. NEU-145 — analytische Fortsetzung

Als Definition ist

\[
Tr_{reg}(R\Sigma)(\beta):=AC[-\zeta'/\zeta](\beta)
\]

zulässig. Sie ist aber keine unabhängige operatorielle Realisierung, sondern baut die Zielgröße per Definition ein.

Bei einer Nullstelle rho der Multiplizität m_rho lautet das Residuum von `-zeta'/zeta`

\[
\boxed{-m_\rho,}
\]

nicht automatisch -1.

Für einen glatten Cutoff `chi_Lambda` lautet die Spur formal mit Gewichten `chi_Lambda(R_p)`; sie ist nicht exakt die harte Summe über `R_p<=Lambda`, solange kein Projektionscutoff gewählt wird. Aus `R_p \gtrsim p/log p` folgt zudem keine Asymptotik `R_p ~ p/log p` für die Wärmeheuristik.

**Status:** analytische Fortsetzungsdefinition `✓[def]`; RH-Polgeometrie arithmetische Restatement; operatorielle Finite-Part-/Wärmerealisierung `?[O]`.

## 10. Statusmatrix

| Punkt | Endstatus |
|---|---|
| NEU-132 dyadische Primschalen | `✓[M]` methodisch |
| ungewichtete H1-rel-Schranke | `×[M]` |
| NEU-133 Abel/H1-Kern | `×[M]` |
| Welt-2-Norm | `✓[M]_{model}` |
| `B_p=O(1/p)` / c_p-Upper-Bound | `?[O]` / conditional |
| algebraische beta-Zerlegung | `✓[M]` |
| log-kubische Vergleichsasymptotik | `×[M]` |
| Rohdivergenz aus Upper Bound | `?[O]` |
| feste-beta S1 | `CONDITIONAL ✓[M]_{model}` |
| beta→0 S1-Divergenz | `?[O]` |
| Fredholm-Basistheorie | `CONDITIONAL ✓[M]` |
| primeweise Eigenwerte ohne T2 | `×[M]` |
| T1/T2-Prüfrahmen | `✓[M]` |
| intrinsisches T2 | `?[O]` |
| Nichtentartung `c_p!=0` | `?[O]` |
| primdiagonales Mangoldt-R | `?[O]/CONDITIONAL` |
| gewöhnliche Mangoldt-Spur Re beta>1 | `CONDITIONAL ✓[M]_{model}` |
| `Tr_reg := AC[-zeta'/zeta]` | `✓[def]`, keine Operatorrealisierung |
| operatorielle Finite-Part-Realisierung | `?[O]` |

## 11. Firewalls für H-T5

1. **Primeclock:** Keine P-unabhängige ungewichtete `sum p^{-iu}`-Schranke importieren; tatsächliches P-Wachstum und Gewichte müssen getragen werden.
2. **Rohanteil:** Aus Upper Bounds keine Divergenz oder Finite-Part-Haupttermstruktur ableiten.
3. **Schatten/Fredholm:** S1 bleibt conditional/model-relative, solange quantitative c_p-Kontrolle nicht intrinsisch bewiesen ist.
4. **Mangoldt-R:** Primdiagonalität benötigt Nichtentartung und intrinsisches T2; beide offen.
5. **Keine Zirkularität:** `Tr_reg := AC[-zeta'/zeta]` darf nicht als Beweis einer operatoriellen Zeta-Realisierung verwendet werden.

## 12. Endurteil

\[
\boxed{\text{H-T4 COMPLETE — keine offenen H-T4-Reaudits; historische Hochstufungen sind auf den tragfähigen conditional/model-relative Stand zurückgesetzt.}}
\]

Der nächste P08-Block ist **H-T5 = NEU-146–150**. Dort sind Cutoff/Finite Part, Mellin-Identität, Konturrest und Rückbindung unter diesen Firewalls sowie dem bereits gebundenen NEU-148-Cutoff-Gegenbefund zu prüfen.
