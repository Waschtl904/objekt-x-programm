# P11-C1f — Source-induced Cutoff: Trägerfenster koppelt kanonisch an Prime-Power-Cutoff

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1f]`  
**Vorgänger:** P11-C1d, P11-C1e  
**Primärbasis:** P02-Korrelationskern `g_{a,b}\in C_c^\infty`, P05/P02 Prime-Power-Zeiten `m\log p`  

**Urteil:**

\[
\boxed{[P11-C1f]\quad\checkmark[K/M]}
\]

Die gemeinsame Testfunktionsquelle bestimmt bereits **kanonisch** den relevanten endlichen Prime-Power-Cutoff. Für Testfunktionen mit Träger in `[-R,R]` können nur Prime-Powers mit `p^m\le e^{2R}` zum Primblock beitragen. Quellfenster und arithmetischer Cutoff sind daher nicht unabhängige Regler.

Dies liefert einen natürlichen source-first Induktiv-/Cutoff-Pfad für P11. Positivität entlang dieses Pfads ist nicht bewiesen.

---

## 1. Träger des Korrelationskerns

Für

\[
C_{a,b}(u)
:=
\int_{\mathbb R}a(u+t)\overline{b(t)}\,dt
\]

gilt allgemein

\[
\operatorname{supp}C_{a,b}
\subset
\operatorname{supp}a-\operatorname{supp}b.
\]

P02 definiert

\[
g_{a,b}(u)
=\frac12\bigl(C_{a,b}(u)+C_{a,b}(-u)\bigr).
\]

Daher

\[
\operatorname{supp}g_{a,b}
\subset
(\operatorname{supp}a-\operatorname{supp}b)
\cup
(\operatorname{supp}b-\operatorname{supp}a).
\]

Status: `✓[M]`.

---

## 2. Symmetrisches Quellfenster

Setze

\[
\mathcal D_R
:=
C_c^\infty([-R,R];\mathbb C).
\]

Für `a,b\in\mathcal D_R` gilt

\[
\operatorname{supp}a-\operatorname{supp}b
\subset[-2R,2R],
\]

also

\[
\boxed{
\operatorname{supp}g_{a,b}
\subset[-2R,2R].
}
\]

Folglich

\[
g_{a,b}(s)=0
\qquad(s>2R).
\]

---

## 3. Kanonischer Prime-Power-Cutoff

Der Primblock lautet

\[
B_{\rm fin}(a,b)
=-2\sum_p\sum_{m\ge1}
\frac{\log p}{p^{m/2}}
\,g_{a,b}(m\log p).
\]

Für `a,b\in\mathcal D_R` verschwindet jeder Summand mit

\[
m\log p>2R.
\]

Äquivalent:

\[
\boxed{
p^m>e^{2R}\Longrightarrow\text{kein Beitrag}.}
\]

Definiere daher

\[
\boxed{
F_R
:=
\{(p,m):m\log p\le2R\}
=
\{(p,m):p^m\le e^{2R}\}.
}
\]

`F_R` ist endlich, und auf `\mathcal D_R` gilt exakt

\[
\boxed{
B_{\rm fin}(a,b)
=
B_{\rm fin}^{F_R}(a,b).
}
\]

Status: `✓[K/M]`.

---

## 4. Keine unabhängige Cutoff-Wahl

Damit besitzt das Programm einen kanonischen Zusammenhang

\[
\boxed{
R\quad\longleftrightarrow\quad X_R=e^{2R}.
}
\]

Ein Testfenster auf logarithmischer Länge `2R` sieht genau Prime-Powers bis zur natürlichen Größe `e^{2R}`.

Für P11 ist daher die freie Wahl

\[
(R,X)
\]

als zwei voneinander unabhängige Cutoffs methodisch unnötig, sofern der Primblock direkt aus P02 auf dem gemeinsamen Quellfenster berechnet wird.

---

## 5. Verschachtelte source-first Familie

Für

\[
0<R<S
\]

gilt

\[
\mathcal D_R\subset\mathcal D_S,
\qquad
F_R\subset F_S.
\]

Damit entsteht eine kanonische verschachtelte Familie

\[
(\mathcal D_R,F_R)_{R>0}.
\]

Der algebraische Gesamtkern ist

\[
\boxed{
\mathcal A_{\rm PW}
=
\bigcup_{R>0}\mathcal D_R.
}
\]

Für jedes feste Paar `a,b\in\mathcal A_{PW}` existiert ein `R_0`, so dass für alle `R\ge R_0`

\[
B_{\rm fin}^{F_R}(a,b)=B_{\rm fin}(a,b).
\]

Der Primblock stabilisiert also **punktweise exakt** entlang der source-induced Trunkierung.

Status: `✓[K/M]`.

---

## 6. Reconciliation mit C1e

C1e beweist für **festes endliches `F`** auf dem gesamten Testkern

\[
\operatorname{ind}_-(B_W^F)=\infty.
\]

Dieser Befund darf nicht überdehnt werden zu

\[
\text{„jede source-induced Familie }(\mathcal D_R,F_R)\text{ ist unbrauchbar“.}
\]

Der C1e-Beweis konstruiert beliebig stark frequenzlokalisierte Testfunktionen; die dazu nötigen räumlichen Träger wachsen. Im source-induced Pfad wächst dann gleichzeitig

\[
F_R.
\]

Damit wird **nicht** behauptet, dass `B_W^{F_R}` auf `\mathcal D_R` positiv sei; nur die logische Übertragung des fixed-`F`-No-Gos ist gesperrt.

\[
\boxed{
\text{fixed }F\text{ auf wachsendem Quellraum}
\neq
\text{source-induced }F_R\text{ auf }\mathcal D_R.
}
\]

---

## 7. Source-induced Inzidenzmodell

Für jedes `R` existiert jetzt kanonisch die endliche Prime-Power-Inzidenzfamilie

\[
\{D_{m\log p}:(p,m)\in F_R\}.
\]

Der latente Gramkern aus C1c beschränkt sich auf

\[
G_R
=
\bigl(G_{\alpha\beta}\bigr)_{\alpha,\beta\in F_R}.
\]

Diese Matrix ist PSD als operatorwertiger Gramkern und benötigt keine zusätzliche Auswahl der Labelmenge.

Damit sind für einen endlichen P11-Pilot nun **beide** Dimensionen kanonisch festgelegt:

1. Quellraum `\mathcal D_R`;
2. Prime-Power-Labelmenge `F_R`.

Offen bleibt ausschließlich die **Kopplungs-/Synthesestruktur innerhalb dieses festgelegten Gramkerns**.

---

## 8. Verbindung zur adelischen Quelle

P02 liefert surjektiv

\[
R_{\rm PW}:\mathcal S_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal A_{\rm PW}.
\]

Definiere den source-window Unterraum

\[
\mathcal S_{{\rm adel},R}^{\rm amp}
:=
R_{\rm PW}^{-1}(\mathcal D_R).
\]

Dann wird der Cutoff `F_R` bereits auf der adelischen Amplitudenquelle durch das Bildfenster bestimmt.

**Firewall:** Wegen des großen Kerns von `R_{PW}` ist dies noch keine kanonische Auswahl eines einzelnen adelischen Lifts. P11-C1f benötigt aber auch keine solche Auswahl; der Cutoff hängt nur vom Bild `a=R_{PW}F` ab.

---

## 9. Bedeutung für K6 (Cutoff-Kompatibilität)

NEU-250 fordert in K6 cutoff-kompatible endliche Modelle. C1f liefert hierfür erstmals eine konkrete natürliche Kandidatenfamilie:

\[
\boxed{
\mathcal D_R=C_c^\infty([-R,R]),
\qquad
F_R=\{(p,m):p^m\le e^{2R}\}.
}
\]

Sie ist

- verschachtelt;
- vollständig prime-power-typisiert;
- aus der gemeinsamen Quelle abgeleitet;
- frei von extern gewählter Prime-Cutoff-Skala;
- punktweise exakt stabilisierend für den Primblock.

---

## 10. Was noch nicht folgt

C1f beweist nicht:

1. Positivität von `B_W^{F_R}` auf `\mathcal D_R`;
2. einen positiven globalen Grenzraum;
3. Mosco-/Resolventenkonvergenz;
4. eine kanonische Aktivierung der Off-Diagonalblöcke `G_{\alpha\beta}`;
5. dass `R\mapsto e^{2R}` die einzig mögliche sinnvolle Skalierung in anderen Modellarchitekturen ist.

Die Exaktheit gilt für die **P02-Korrelations-/Primblockstruktur**.

---

## 11. Statusmatrix

| Aussage | Status |
|---|---|
| `supp g_{a,b}\subset[-2R,2R]` für `a,b\in D_R` | `✓[M]` |
| Prime-Powers mit `p^m>e^{2R}` tragen nicht bei | `✓[K/M]` |
| `B_fin=B_fin^{F_R}` auf `D_R` | `✓[K/M]` |
| `(D_R,F_R)` verschachtelt | `✓[M]` |
| Primblock stabilisiert punktweise exakt entlang `R\to\infty` | `✓[K/M]` |
| fixed-F-No-Go aus C1e schließt source-induced Pfad | `×[M]` als Implikation |
| Positivität auf `(D_R,F_R)` | `?[O]` |
| kanonische Off-Diagonal-Synthese auf `G_R` | `?[O]` |
| positiver Grenzabschluss | `?[O]` |

---

## 12. Wichtigster P11-Befund

Die bisher scheinbar zwei freien Grenzparameter

\[
\text{Testfenstergröße}
\quad\text{und}\quad
\text{Prime-Power-Cutoff}
\]

sind in der exakten P02/P05-Struktur **nicht unabhängig**.

\[
\boxed{
\text{Die gemeinsame Quelle selbst synchronisiert analytische und arithmetische Skala.}
}
\]

Dies ist genau die Art source-first Kopplung, die P11 gesucht hat: keine frei angepasste Matrix, sondern eine Relation, die bereits aus dem Träger der gemeinsamen Testfunktion folgt.

---

## 13. Nächster Knoten

\[
\boxed{[P11\text{-}C1g]\quad\text{Kanonische Labelkopplung auf dem source-induced Gramkern }G_R.}
\]

Jetzt ist präzise zu testen, welche positiven Kopplungen der endlichen Prime-Power-Labels überhaupt möglich sind und welche davon durch Symmetrie/Skalierungsfluss/adelische Struktur ausgezeichnet werden können.
