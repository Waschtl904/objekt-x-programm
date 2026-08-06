# NEU-250a — Typisierung und explizite Dirichletresiduumsform auf dem relativen Primkantenraum

**Knoten:**  
\[
[O\text{-}221\text{-}1c1a0\text{-B}]
\]

**Status:**  
\[
\checkmark[M]_{\mathrm{part}}
\]

**Datum:** 6. August 2026

> **Vorgänger:** NEU-250 (Ausgang E — keine auswertbare relative Gramform im Minimalblock).  
> Dieser Knoten untersucht die tiefere Ursache und schließt mit Ausgang B.

---

## 0. Ziel des Knotens

Zu entscheiden ist, ob die in NEU-15 bis NEU-25 entwickelte BC-Residuenarchitektur bereits eine wohldefinierte sesquilineare Paarung

\[
h_{p,N}:
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
\times
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
\longrightarrow
\mathbb C
\]

auf dem relativen Primkantenraum liefert.

Insbesondere ist zu prüfen, ob ein Ausdruck der Form

\[
\left\langle
E^{\mathrm{rel}}_{R;1\to p},
E^{\mathrm{rel}}_{R';1\to p}
\right\rangle_{\mathrm{Wres,rel}}
\]

aus den vorhandenen Quellen tatsächlich berechnet werden kann.

Die entscheidende Typfrage lautet:

\[
\boxed{
\text{Existiert eine explizite lineare Abbildung }
j_{p,N}:
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
\longrightarrow
F^3A_{\mathrm{BC}}^{\mathrm{an}}
\text{ oder in einen äquivalenten Residuumsraum?}
}
\]

Nur nach Konstruktion einer solchen Abbildung kann die BC-Residuenstruktur auf den relativen Primkantenraum zurückgezogen werden.

---

## 1. Geprüfte Quellen

Für diesen Knoten sind insbesondere relevant:

- NEU-015: modulares Frobenius-Funktional auf \(A_{2D}^r\);
- NEU-016: renormierte modulare Spur bei \(\beta=1\);
- NEU-017 bis NEU-020: Massey-/Hochschildkonstruktion und BC-Residuen-Nichtverschwindenszeuge;
- NEU-021 bis NEU-025: Graduiertenprojektion \(R_3\), Ladungszerlegung, Symbolfiltration und modulare Frobenius-Wodzicki-Struktur;
- NEU-044: symbolische relative Paarung;
- NEU-221e: relativer Rohzielraum, formal bezeichnetes Wres-Radikal und offener Hebungsabstieg;
- NEU-246 bis NEU-250: Direktaudits der behaupteten Wres-Hilbertbrücke und des fehlenden Minimalgramblocks.

---

## 2. Kein klassischer Wodzicki-Symbolkalkül

NEU-15 definiert für \(\beta>1\) das modulare Funktional

\[
\varepsilon_\beta(F)
=
\sum_{m\ge1}m^{-\beta}F_{m,m,0}.
\]

Die zugehörige Paarung lautet

\[
\beta_{\varepsilon,\beta}(F,G)
=
\varepsilon_\beta(FG).
\]

Dabei wird ausdrücklich kein klassischer Pseudodifferentialoperator-Kalkül auf einer kompakten Mannigfaltigkeit vorausgesetzt.

Insbesondere liegt keine homogene Symbolkomponente

\[
\sigma_{-d}(P)(x,\xi)
\]

und kein Kosphärenintegral der Form

\[
\int_{S^*M}
\operatorname{tr}\sigma_{-d}(P)\,d\Sigma
\]

vor.

Status:

\[
\boxed{
\text{Klassische Wodzicki-Symbolformel in NEU-15–25: }
\checkmark[M]_{\mathrm{neg,Quelle}}
}
\]

Die Verwendung des Ausdrucks „Wodzicki" bezeichnet in diesem Strang eine arithmetische Dirichlet-/Laurent-Residuenanalogie, nicht die klassische Restspur auf einer \(\Psi\)DO-Algebra.

---

## 3. Tatsächlich vorhandene BC-Residuenstruktur

### 3.1 Modulare Diagonalspur

Für \(\beta>1\) ist definiert:

\[
\varepsilon_\beta(F)
=
\sum_{m\ge1}m^{-\beta}F_{m,m,0}.
\]

Für geeignete \(F\) wird anschließend die meromorphe beziehungsweise asymptotische Fortsetzung bei

\[
\beta=1
\]

untersucht.

### 3.2 Renormierter einfacher Pol

NEU-16 betrachtet formal den Koeffizienten

\[
\varepsilon_1^{\mathrm{ren}}(F)
=
\operatorname*{Res}_{\beta=1}
\sum_m m^{-\beta}F_{m,m,0}.
\]

Dieser ist nur formal analog zur klassischen Wodzicki-Restspur und wird als eigenständige monoidanisotrope Spurform behandelt.

### 3.3 Allgemeine Laurentkoeffizienten

Für

\[
F\in F^3A_{\mathrm{BC}}^{\mathrm{an}}
\]

wird in NEU-19 eine Expansion der Form

\[
\lambda_\beta^{\mathrm{mod}}(F)
\sim
\sum_{q\ge1,\ell\ge0}
c_{q,\ell}(F)
(\beta-1)^{-q}
\left(
\log\frac1{\beta-1}
\right)^\ell
+O(1)
\]

verwendet.

Daraus werden die Koeffizienten

\[
Wres_{\mathrm{BC}}^{(q,\ell)}(F)
:=
c_{q,\ell}(F)
\]

und der führende Koeffizient

\[
Wres_{\mathrm{BC}}^{\mathrm{top}}(F)
\]

definiert.

Für die \(L_3\)-Konstruktion ist der relevante Typ ein Doppelpol:

\[
Wres_{\mathrm{BC}}^{(2,0)}.
\]

Status:

\[
\boxed{
\text{Dirichlet-/Laurent-Residuenstruktur auf }
F^3A_{\mathrm{BC}}^{\mathrm{an}}:
\checkmark[M]
}
\]

---

## 4. Was NEU-20 tatsächlich beweist

NEU-20 konstruiert den Zeugen

\[
(n,m,r,s,t,k)
=
(2,3,4,1,-1,1)
\]

und berechnet

\[
C'_{4,1}
=
\left(
R_3\Phi_3
(e_4V_2,e_1V_3,e_{-1}V_1)
\right)_{6,6,0}
=
-\frac{24\log 2\log 6}
{\mu_{4,1,2,3}}
\neq0.
\]

Damit wird ein Nichtverschwindenszeuge für die BC-Hochschild-/Residuenkonstruktion gewonnen.

Bewiesen wird insbesondere eine Aussage der Form

\[
Wres_{\mathrm{BC}}^{(2,0)}
\bigl(L_3(c_4)\bigr)
\neq0.
\]

Das Resultat betrifft jedoch:

- ein konkretes Hochschild-/Massey-Objekt;
- eine Graduiertenprojektion \(R_3\);
- einen Diagonalkoeffizienten im BC-Komplex;
- die Auswertung eines Doppelpolkoeffizienten.

Es betrifft nicht zwei relative Primkantenerzeuger

\[
E^{\mathrm{rel}}_{R;1\to p},
\qquad
E^{\mathrm{rel}}_{R';1\to p}.
\]

Insbesondere wird keine Zahl der Form

\[
h_{p,N}
\left(
E^{\mathrm{rel}}_{R;1\to p},
E^{\mathrm{rel}}_{R';1\to p}
\right)
\]

berechnet.

Status:

\[
\boxed{
\text{NEU-20 liefert eine relative Wres-Grammatrix: }
\checkmark[M]_{\mathrm{neg,Quelle}}
}
\]

---

## 5. Die fehlende Typbrücke

Der relative Rohzielraum besitzt die algebraische Form

\[
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
=
\operatorname{span}_{\mathrm{fin}}
\left\{
E^{\mathrm{rel}}_{R;m\to pm}
\right\}.
\]

Die BC-Residuenfunktionale sind dagegen auf Elementen beziehungsweise Kozykeln in

\[
F^3A_{\mathrm{BC}}^{\mathrm{an}}
\]

oder einem daraus konstruierten Hochschildraum definiert.

Damit ein Ausdruck wie

\[
Wres_{\mathrm{BC}}^{\mathrm{top}}
\left(
E_a^*E_b
\right)
\]

typkorrekt wäre, müsste mindestens eine konkrete Repräsentation

\[
j_{p,N}:
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
\longrightarrow
F^3A_{\mathrm{BC}}^{\mathrm{an}}
\]

definiert sein.

Alternativ wäre eine Abbildung in einen expliziten Operator-, Kozykel- oder Bimodulraum zulässig, sofern auf diesem:

1. ein Produkt oder eine sesquilineare Komposition definiert ist;
2. die Projektion \(R_3\) angewendet werden kann;
3. ein Diagonalkoeffizient \((M,M,0)\) existiert;
4. die zugehörige Dirichletreihe konvergiert oder eine kontrollierte Laurententwicklung besitzt.

Keine der geprüften Dateien NEU-15 bis NEU-25 definiert eine solche Abbildung für die relative Primkantenbasis.

Status:

\[
\boxed{
\text{Existenz einer bereits definierten Abbildung }j_{p,N}:
\checkmark[M]_{\mathrm{neg,Quelle}}
}
\]

---

## 6. Warum die bisherige relative Wres-Paarung untypisiert ist

NEU-044 und spätere Dateien verwenden symbolisch eine Paarung

\[
\left\langle
E_a,E_b
\right\rangle_{\mathrm{Wres,rel}}.
\]

Eine solche Paarung kann nicht allein dadurch definiert werden, dass auf einem anderen Raum ein Funktional

\[
Wres_{\mathrm{BC}}^{\mathrm{top}}
\]

existiert.

Erforderlich ist ein typkorrekter Pullback:

\[
h_{p,N}(E_a,E_b)
=
\mathcal W
\left(
j_{p,N}(E_a),
j_{p,N}(E_b)
\right),
\]

wobei \(\mathcal W\) eine tatsächlich definierte sesquilineare BC-Paarung bezeichnet.

Solange \(j_{p,N}\) fehlt, sind insbesondere nicht definiert:

\[
G_{p,N}(R,R')
=
h_{p,N}
\left(
E^{\mathrm{rel}}_{R;1\to p},
E^{\mathrm{rel}}_{R';1\to p}
\right),
\]

\[
\mathcal N_{\mathrm{Wres,rel}}
=
\operatorname{Rad}(h_{p,N}),
\]

und

\[
\mathscr H_{\mathrm{Wres,rel}}
=
\overline{
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
/
\mathcal N_{\mathrm{Wres,rel}}
}.
\]

Damit sind auch Aussagen über Positivität, Nichtverschwindung, Trivialität des Radikals, Hebungsunabhängigkeit, Sektionsunabhängigkeit und Hilbertvervollständigung noch nicht aus den BC-Residuenquellen ableitbar.

---

## 7. Konditional zulässiger Paarungskandidat

Falls eine Abbildung \(j_{p,N}\) konstruiert wird, könnte ein Kandidat zunächst formal durch

\[
h_{p,N}(E_a,E_b)
:=
Wres_{\mathrm{BC}}^{(q,\ell)}
\left(
R_3
\bigl(
j_{p,N}(E_a)^*
j_{p,N}(E_b)
\bigr)
\right)
\]

definiert werden.

Dabei müssen \(q,\ell\) vorab festgelegt werden. Insbesondere dürfen \(Wres_{\mathrm{BC}}^{\mathrm{top}}\) und \(Wres_{\mathrm{BC}}^{(2,0)}\) nicht ohne Nachweis miteinander identifiziert werden.

Status des Paarungskandidaten:

\[
\boxed{\checkmark[K/M]}
\]

als typkorrekte konditionale Vorlage, nicht als vorhandene Konstruktion.

---

## 8. Harte Entscheidung A/B

### Ausgang A

Ausgang A würde verlangen:

1. eine explizite Formel für \(j_{p,N}(E_R)\);
2. eine wohldefinierte BC-Komposition;
3. einen festgelegten Laurentkoeffizienten;
4. vier konkret berechnete Einträge eines Minimalgramblocks;
5. den Nachweis von Hermiteschheit und Endlichkeit.

Diese Voraussetzungen sind im geprüften Quellenbestand nicht erfüllt.

### Ausgang B

Die Quellen stellen die BC-Dirichlet-/Laurent-Residuenarchitektur bereit, definieren aber keine Repräsentationsabbildung \(j_{p,N}\) vom relativen Primkantenraum in ihren Definitionsbereich.

Daher ist die relative Wres-Paarung bislang nicht typisiert.

\[
\boxed{
\textbf{Ausgang B ist bewiesen.}
}
\]

Status:

\[
\boxed{
\checkmark[M]_{\mathrm{neg,Quelle}}
}
\]

für die Behauptung, die vorhandenen Quellen definierten bereits eine relative Wres-Paarung.

---

## 9. Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---:|
| \([O\text{-}221\text{-}1c1a0\text{-B1}]\) | Klassischer Wodzicki-\(\Psi\)DO-Symbolkalkül vorhanden | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-B2}]\) | Modulare Diagonalspur \(\varepsilon_\beta\) definiert | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-B3}]\) | BC-Laurentkoeffizienten \(Wres_{\mathrm{BC}}^{(q,\ell)}\) definiert | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-B4}]\) | Nichtverschwindenszeuge aus NEU-20 | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-B5}]\) | NEU-20 berechnet relative Gramwerte | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-B6}]\) | Explizite Repräsentation \(j_{p,N}\) vorhanden | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) |
| \([O\text{-}221\text{-}1c1a0\text{-B7}]\) | Relative Wres-Paarung typisiert | \(?[O]\) |
| \([O\text{-}221\text{-}1c1a0\text{-B8}]\) | Relative Wres-Grammatrix berechenbar | \(?[O]\) |
| \([O\text{-}221\text{-}1c1a0\text{-B9}]\) | Wres-Radikal bestimmbar | \(?[O]\) |
| \([O\text{-}221\text{-}1c1a0\text{-B10}]\) | Hebungsabstieg prüfbar | \(?[O]\) |

Gesamtstatus:

\[
\boxed{
[O\text{-}221\text{-}1c1a0\text{-B}]
:
\checkmark[M]_{\mathrm{part}}
}
\]

---

## 10. Konsequenz für die letzten Knoten

Die folgenden offenen Fragen sind keine voneinander unabhängigen Barrieren:

\[
[O\text{-}221\text{-}1c1a0],
\quad
[O\text{-}246/0\mathrm{corr}\text{-}2],
\quad
\text{Bestimmung von }
\mathcal N_{\mathrm{Wres,rel}},
\quad
\text{Hebungsunabhängigkeit von }J_{p,b}.
\]

Sie setzen sämtlich eine typisierte relative Paarung voraus.

Der gemeinsame fehlende Vorläufer ist:

\[
\boxed{
j_{p,N}:
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
\longrightarrow
F^3A_{\mathrm{BC}}^{\mathrm{an}}
\quad
\text{oder in einen gleichwertigen BC-Residuenraum}.
}
\]

Damit wird der DAG korrigiert zu:

\[
\text{BC-Residuenarchitektur}
\longrightarrow
\boxed{\text{Repräsentation }j_{p,N}}
\longrightarrow
\text{relative Paarung }h_{p,N}
\longrightarrow
\text{Grammatrix}
\longrightarrow
\text{Radikal}
\longrightarrow
\text{Hebungsabstieg}.
\]

---

## 11. Repository-Korrekturen

### 11.1 NEU-044

Die dort verwendete relative Wres-Paarung ist als symbolischer Kandidat zu kennzeichnen. Es ist ausdrücklich zu ergänzen:

> Eine typkorrekte Ableitung aus \(Wres_{\mathrm{BC}}^{\mathrm{top}}\) setzt eine noch fehlende Repräsentationsabbildung \(j_{p,N}\) voraus.

### 11.2 NEU-221e

Vor der Definition des Wres-Radikals ist einzufügen:

> Das Radikal ist derzeit nur formal bezeichnet. Eine konkrete sesquilineare Form auf dem relativen Rohzielraum ist erst nach Konstruktion von \(j_{p,N}\) verfügbar.

### 11.3 NEU-246 bis NEU-250

Alle Aussagen, die eine bereits vorhandene Wres-Norm oder Wres-Grammatrix voraussetzen, sind auf den neuen Vorläuferknoten zurückzubinden:

\[
[O\text{-}221\text{-}1c1a0\text{-C}].
\]

### 11.4 Terminologie

Die Bezeichnung „Wres" ist künftig zu unterscheiden in:

- \(Wres_{\mathrm{BC}}^{(q,\ell)}\) — tatsächlich definiertes BC-Dirichletresiduum;
- \(h_{\mathrm{Wres,rel}}\) — erst noch zu konstruierende relative Paarung.

Die identische Benennung beider Objekte darf nicht als Beweis einer Typbrücke verwendet werden.

---

## 12. Nächster atomarer Forschungsauftrag

\[
\boxed{
[O\text{-}221\text{-}1c1a0\text{-C}]
\quad
\text{BC-Repräsentation eines primitiven relativen Primkantenvektors}
}
\]

Für \(p=2\) und einen einzelnen primitiven Erzeuger \(E^{\mathrm{rel}}_{R;1\to2}\) ist ein explizites BC-Element

\[
j_{2,N}
\left(
E^{\mathrm{rel}}_{R;1\to2}
\right)
\]

zu konstruieren, das sechs Bedingungen erfüllt:

1. **Typkorrektheit:** \(j_{2,N}(E_R) \in F^3A_{\mathrm{BC}}^{\mathrm{an}}\)
2. **Linearität:** \(j_{2,N}(\alpha E_R+\beta E_{R'}) = \alpha j_{2,N}(E_R)+\beta j_{2,N}(E_{R'})\)
3. **Indexverträglichkeit:** Indizes \(p,m,R\) aus BC-Monoid- und Fourierindizes rekonstruierbar
4. **Involutionsverträglichkeit:** \(j_{2,N}(E_R)^*\) explizit berechenbar
5. **Residuenfähigkeit:** \(\lambda_\beta^{\mathrm{mod}}\bigl(R_3(j_{2,N}(E_R)^* j_{2,N}(E_{R'}))\bigr)\) bei \(\beta=1\) auswertbar
6. **Nichttautologie:** \(j_{2,N}\) darf nicht so definiert werden, dass ein gewünschter Gramwert definitionsgemäß entsteht

Erst nach Erfüllung dieser sechs Bedingungen darf der erste konkrete Gramwert \(h_{2,N}(E_R,E_{R'})\) berechnet werden.

---

## 13. Deepest-Gap-Box

> **Tiefste gemeinsame Lücke**
>
> Die BC-Residuenmaschinerie ist nicht die derzeitige Hauptlücke. Sie besitzt eine explizite modulare Diagonalspur, eine Laurentkoeffizientenstruktur und einen Nichtverschwindenszeugen.
>
> Die tiefste gemeinsame Lücke ist die fehlende Repräsentation
>
> \[
> j_{p,N}:
> \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
> \longrightarrow
> F^3A_{\mathrm{BC}}^{\mathrm{an}}
> \]
>
> Ohne diese Abbildung existieren keine typisierte relative Wres-Paarung, keine berechenbare Grammatrix, kein bestimmbares Radikal und kein prüfbarer Hebungsabstieg.

---

## 14. Gesamturteil

Die Dateien NEU-15 bis NEU-25 liefern eine eigenständige arithmetische Dirichlet-/Laurent-Residuenarchitektur auf der BC-Seite.

Sie liefern jedoch keine Repräsentation des relativen Primkantenraums in den Definitionsbereich dieser Funktionale.

Daher ist die bisher verwendete relative Wres-Paarung \(\langle E_a,E_b\rangle_{\mathrm{Wres,rel}}\) noch kein konstruiertes mathematisches Objekt.

\[
\boxed{
\text{Endentscheidung B: }
\checkmark[M]_{\mathrm{neg,Quelle}}
}
\]

Der nächste echte Konstruktionsschritt ist die explizite Definition eines einzigen primitiven Bildes

\[
j_{2,N}
\left(
E^{\mathrm{rel}}_{R;1\to2}
\right).
\]
