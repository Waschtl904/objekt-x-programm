# NEU-250b — BC-Repräsentation eines primitiven relativen Primkantenvektors

**Knoten:**
\[
[O\text{-}221\text{-}1c1a0\text{-C}]
\]

**Status:**
\[
\checkmark[M]_{\mathrm{part}}
\]

**Datum:** 6. August 2026

> **Vorgänger:** NEU-250a (Ausgang B) — fehlende Repräsentationsabbildung
> \(j_{p,N}: \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \to F^3A_{\mathrm{BC}}^{\mathrm{an}}\)
> als tiefste gemeinsame Lücke identifiziert.

---

## 0. Ziel und Methode

Für \(p = 2\) und einen einzigen primitiven Erzeuger
\[
E^{\mathrm{rel}}_{R;1\to2} \in \mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}
\]
ist ein explizites BC-Element oder BC-Kozykel
\[
j_{2,N}\!\left(E^{\mathrm{rel}}_{R;1\to2}\right)
\]
zu konstruieren, das die sechs Bedingungen aus NEU-250a \S12 erfüllt.

**Methode dieser Datei:** Einzig und ausschließlich den einfachsten Kandidaten
\[
j^{(0)}_{2,N}(E_R) := e_R V_2
\]
vollständig gegen alle sechs Bedingungen testen. Kein neues Konstrukt vor diesem Test.

---

## 1. Quelltyp des Primkantenvektors

Nach NEU-044 und NEU-221e ist:
\[
\mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}
= \operatorname{span}_{\mathrm{fin}}\!
\bigl\{E^{\mathrm{rel}}_{R;m\to2m} \mid m \in \mathbb N^\times,\, m \le N/2\bigr\}.
\]

Ein primitiver Erzeuger bei \(p = 2\), \(m = 1\):
\[
E^{\mathrm{rel}}_{R;1\to2} \in \mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}.
\]

**Keine Wres-Norm, kein Hilbertquotient wird vorausgesetzt.** Dies ist reine Vektorraum-Ebene.

---

## 2. Definition und Quelltyp des Kandidaten \(j^{(0)}\)

### 2.1 Kandidat

\[
j^{(0)}_{2,N}: E^{\mathrm{rel}}_{R;1\to2} \longmapsto e_R V_2
\]

wobei \(e_R\) das Fourier-Monoidelement zum Index \(R\) ist und \(V_2\) der
Isometrie-Erzeuger des BC-Monoids bei \(p = 2\).

### 2.2 Alg. Typ von \(e_R V_2\)

Nach NEU-015 (\(A_{2D}^r\)-Basis) und NEU-019 (Filtrationsstruktur) gilt:
\[
e_R V_2 \in A_{\mathrm{BC}}^{\mathrm{an}},
\]
genauer: \(e_R V_2\) ist ein Basiselement der Form
\[
(e_R V_2)_{m,n,r'} = \delta_{n,2m}\,\delta_{r',R},
\]
ein Monoid-Gewichtselement vom **BC-Grad 1**:
\[
e_R V_2 \in F^1 A_{\mathrm{BC}}^{\mathrm{an}} \setminus F^2 A_{\mathrm{BC}}^{\mathrm{an}}.
\]

**Ableitung des Filtrationsgrades.** Die Filtration \(F^k A_{\mathrm{BC}}^{\mathrm{an}}\)
ist nach NEU-019 durch die Ordnung der Laurentpol-Singularität bei \(\beta = 1\) definiert:
- Elemente mit einfachem Pol: \(F^1\)
- Elemente mit Doppelpol (\(\Lambda\)-Typ): \(F^3\) (nach der \(L_3\)-Konstruktion, NEU-019 \S5)

Das Element \(e_R V_2\) ist ein einzelner Basisvektor des Monoids. Die modulare Diagonalspur:
\[
\varepsilon_\beta(e_R V_2) = \sum_{m} m^{-\beta}\,(e_R V_2)_{m,m,0}
= \sum_{m} m^{-\beta}\,\delta_{m,2m}\,\delta_{0,R}.
\]
\(\delta_{m,2m} = 0\) für alle \(m \in \mathbb{N}^\times\), also:
\[
\varepsilon_\beta(e_R V_2) = 0 \quad \text{für alle } \beta.
\]

Ein einzelner Basisvektor \(e_R V_2\) besitzt **keine Diagonalkomponente** und damit
keine Laurentsingularität. Dies platziert ihn außerhalb des residuenfähigen Kerns.

---

## 3. Filtrationsdiagnose

**Befund:**
\[
\boxed{e_R V_2 \notin F^3 A_{\mathrm{BC}}^{\mathrm{an}}.}
\]

**Begründung:** Nach NEU-019 \S5 besteht \(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) aus Elementen,
für welche \(\lambda_\beta^{\mathrm{mod}}(R_3(\cdot))\) bei \(\beta \to 1^+\) eine
log-polyhomogene Expansion mit Doppelpol besitzt. Notwendige Bedingung ist das Vorhandensein
nichtverschwindender Diagonalkoeffizienten nach Anwendung von \(R_3\).

Da \(e_R V_2\) ein off-diagonales Basiselement ist (es bildet \(m\) auf \(2m\) ab, nicht auf
\(m\)), gilt:
\[
(e_R V_2)_{m,m,0} = 0 \quad \forall m,
\]
also \(\lambda_\beta^{\mathrm{mod}}(e_R V_2) = 0\), kein Pol, keine Residuumsstruktur.

Damit scheitert Kandidat \(j^{(0)}\) bereits an **Bedingung 1 (Typkorrektheit)**.

---

## 4. Sechs-Bedingungs-Tabelle für \(j^{(0)}\)

| Bedingung | \(j^{(0)}(E_R) = e_R V_2\) | Status |
|---|---|---|
| 1. Typkorrektheit | \(e_R V_2 \in F^1\setminus F^2 \subsetneq F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) | \(\checkmark[M]_{\mathrm{neg}}\) |
| 2. Linearität | \(j^{(0)}(\alpha E_R + \beta E_{R'}) = \alpha e_R V_2 + \beta e_{R'}V_2\) | \(\checkmark[M]\) |
| 3. Indexverträglichkeit | \(R\) aus Fourierindex ablesbar, \(p=2\) aus \(V_2\) | \(\checkmark[M]\) |
| 4. Involutionsverträglichkeit | \((e_R V_2)^* = V_2^* e_{-R} = V_2^{-1} e_{-R}\) explizit | \(\checkmark[M]\) |
| 5. Residuenfähigkeit | \(\lambda_\beta^{\mathrm{mod}}(e_R V_2) = 0\): kein auswertbarer Laurentkoeffizient | \(\checkmark[M]_{\mathrm{neg}}\) |
| 6. Nichttautologie | nicht anwendbar (scheitert bereits an 1 und 5) | — |

**Gesamtbefund \(j^{(0)}\):**
\[
\boxed{\text{Kandidat } j^{(0)} \text{ scheitert: } e_R V_2 \notin F^3 A_{\mathrm{BC}}^{\mathrm{an}},
\text{ keine Residuumsstruktur.}}
\]

---

## 5. Dokumentierter Scheiterungsgrund

**Warum \(j^{(0)}\) nicht reparierbar ist durch einfache Neubenennung:**

Die Filtration \(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) ist keine willkürliche Bezeichnung,
sondern beschreibt genau jene Elemente, deren \(\lambda_\beta^{\mathrm{mod}}\)-Auswertung
nach Anwendung von \(R_3\) eine kontrollierte Pol-Entwicklung bei \(\beta = 1\) besitzt.
Ein off-diagonales Einzelbasiselement hat diese Eigenschaft strukturell nicht:
- es fehlt die Diagonalkomponente;
- \(R_3\) ist eine Projektion auf den Grad-3-Anteil der \(L_3\)-Konstruktion;
- ein Basisvektor der Form \(e_R V_2\) ist im Bild von \(R_3\) nur dann nichttrivial,
  wenn er aus einem \(L_3\)-Kozykel stammt, nicht isoliert.

**Dieser Befund ist präzise und nicht durch blosse Filtrationsverschiebung zu umgehen.**

---

## 6. Die drei nachgelagerten Routen

### Route A — Direkter Kandidat (geschlossen)

\(j^{(0)}(E_R) = e_R V_2\) ist nicht typkorrekt. Route A ist **geschlossen**.

\[
\boxed{\text{Route A: }\checkmark[M]_{\mathrm{neg}}}
\]

---

### Route B — Kanonische Gradanhebung

**Kandidat:**
\[
j^{(1)}(E_R) := (e_R V_2) \cdot A^{(2)}
\]
mit einem kanonischen Gewicht-2-Element \(A^{(2)} \in F^2 A_{\mathrm{BC}}^{\mathrm{an}}\).

**Was benötigt wird:**

1. \(A^{(2)}\) muss aus der bestehenden BC-/Hochschild-/\(L_3\)-Architektur erzwungen sein
   (keine willkürliche Wahl).
2. Kanonizität: \(A^{(2)}\) muss unabhängig von \(R\) sein.
3. Ladungsneutralität: Das Produkt \((e_R V_2) A^{(2)}\) muss in
   \(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) landen, d.h.
   \[
   \lambda_\beta^{\mathrm{mod}}(R_3((e_R V_2 A^{(2)})^*(e_{R'} V_2 A^{(2)})))
   \]
   muss einen auswertbaren Laurentkoeffizienten bei \(\beta = 1\) besitzen.
4. Involutionsverträglichkeit: \((A^{(2)})^*\) muss explizit bekannt sein.
5. Indexunabhängigkeit: der Residuumswert darf nicht von einer zusätzlichen Wahl
   in \(A^{(2)}\) abhängen.

**Natürlicher Kandidat für \(A^{(2)}\):** Das Element
\[
A^{(2)} := V_2^* e_{-r_0}
\]
für einen festen Ladungsindex \(r_0\), oder das Produkt \(A^{(2)} := (e_{r_0} V_2)^*\)
das gerade \((e_R V_2)^*\) ist. Das würde aber \((e_R V_2)(e_R V_2)^* = e_R V_2 V_2^* e_{-R}\)
erzeugen, was eine Diagonalprojektion ist. Deren Residuumseigenschaft ist zu prüfen.

**Vorcheck Diagonalkomponente:**
\[
\left(e_R V_2 V_2^* e_{-R}\right)_{m,m,0} = \sum_{k} (e_R V_2)_{m,k,0}\,(V_2^* e_{-R})_{k,m,0}.
\]

\(V_2^* e_{-R}\) bildet \(k \to m\) ab genau für \(k = 2m\) (Rückschritt), also:
\[
\left(e_R V_2 V_2^* e_{-R}\right)_{m,m,0} = (e_R)_{R}\,\delta_{R,-R} + \ldots
\]

Diese Rechnung muss explizit in einem eigenen Knoten durchgeführt werden.

**Status Route B:**
\[
\boxed{\text{Route B: }?[O] \text{ — eröffnet als Knoten [O-221-1c1a0-C1]}}
\]

---

### Route C — Kozyklische Repräsentation

**Kandidat:**
\[
j^{(2)}(E_R) := \Phi_3(\ldots, e_R V_2, \ldots)
\]
für geeignete kanonische BC-Elemente als restliche Einträge.

**Motivation:** In NEU-020 entsteht der Nichtverschwindenszeuge gerade durch
Anwendung von \(\Phi_3\) und \(R_3\) auf konkrete BC-Eingaben — das Residuum ist nicht
ein einzelnes Algebraelement, sondern das Bild einer Massey-Homotopie.

**Prüfprogramm:**
1. Welche Einträge in \(\Phi_3(a_0, a_1, a_2, a_3, a_4)\) können den Index \(R\) und
   \(p = 2\) tragen?
2. Sind die restlichen Einträge kanonisch aus der BC-Struktur bestimmt?
3. Erfüllt das resultierende Element die Involutionsbedingung?
4. Ist \(\lambda_\beta^{\mathrm{mod}}(R_3(\Phi_3(\ldots)^* \Phi_3(\ldots)))\)
auswertbar?

**Status Route C:**
\[
\boxed{\text{Route C: }?[O] \text{ — eröffnet als Knoten [O-221-1c1a0-C2]}}
\]

---

## 7. Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}221\text{-}1c1a0\text{-C/0}]\) | Filtrationsgrad \(e_R V_2\) bestimmt | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C/1}]\) | Kandidat \(j^{(0)} = e_R V_2\): typkorrekt | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-C/2}]\) | Kandidat \(j^{(0)} = e_R V_2\): residuenfähig | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-C/3}]\) | Route A geschlossen | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1}]\) | Route B: Gradanhebung \(j^{(1)}\) | \(?[O]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C2}]\) | Route C: Kozyklische Darstellung \(j^{(2)}\) | \(?[O]\) |

Gesamtstatus:
\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C}]: \checkmark[M]_{\mathrm{part}} \text{ (Route A abgeschlossen; B und C offen)}}
\]

---

## 8. Korrekter nächster Schritt (Route B)

Der präzise nächste atomare Forschungsauftrag lautet:

\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1}]:
\text{ Berechne }(e_R V_2)(e_R V_2)^* = e_R V_2 V_2^* e_{-R}
\text{ und bestimme seine Diagonalkomponenten.}}
\]

Insbesondere:
1. Ist \((e_R V_2 V_2^* e_{-R})_{m,m,0} \neq 0\) für mindestens ein \(m\)?
2. Hat \(\lambda_\beta^{\mathrm{mod}}(e_R V_2 V_2^* e_{-R})\) einen Pol bei \(\beta = 1\)?
3. Ist dieser Pol aus dem BC-Monoidprodukt \(V_2 V_2^*\) direkt ableitbar?

Erst nach diesem Vorcheck ist entschieden, ob Route B weiterverfolgt werden kann.
