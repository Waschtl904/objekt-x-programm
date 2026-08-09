# P08 Pass A — H-T2 unabhängiger Gegencheck, pfadgebunden

**Datum:** 9. August 2026  
**Scope:** Gegencheck des extern vorgelegten H-T2-Textes gegen den aktuellen Live-Repo-Stand  
**Paket:** NEU-123-Familie / NEU-124 / NEU-125  

## 1. Bestätigte Kernaussagen des Gegenchecks

Der Gegencheck trifft drei wichtige Punkte richtig:

1. Der Stamm `NEU-123_Jacobi_Grenzoperator_Resolventenkonvergenz.md` ist ein abstraktes Operatorfundament und enthält selbst keine RH-Behauptung.
2. Ein endlicher symmetrischer Jacobi-Block mit reellen Diagonalkoeffizienten und positiven reellen Offdiagonalen ist selbstadjungiert. Dieser direkt über Jacobi-Koeffizienten definierte Pfad ist typologisch von P06s schiefadjungiertem
   \[
   J_N^-=(\Theta_N-\Theta_N^\dagger)/2
   \]
   zu unterscheiden. Für P08 muss diese Notationskollision explizit aufgelöst werden.
3. `NEU-124` ist inhaltlich vollständig offen, solange die Eintrittsbedingungen aus NEU-123 nicht erfüllt sind; Spektralträger allein genügt nicht, die Spektralmaßidentifikation bleibt die stärkere offene Bedingung.

Diese drei Punkte werden in den kanonischen H-T2-Endstand übernommen.

---

## 2. Konkrete Gegenbefunde gegen den vorgelegten H-T2-Text

### G-H2-1 — NEU-123F/G/H/I sind nicht „post-Juli"

Die Live-Dateien tragen:

- `NEU-123F_Numerische_Diagnose_Dreifachsumme.md`: Stand 6. Juli 2026;
- `NEU-123F_Ergebnisse.md`: Stand 6. Juli 2026;
- `NEU-123G_Zweite_Offdiagonale_Skaleninkohaerenz.md`: Stand 6. Juli 2026;
- `NEU-123H_No_scalar_renormalization.md`: Stand 6. Juli 2026;
- `NEU-123I_Gradierte_Renormierung_Herglotz.md`: Stand 6. Juli 2026.

Für `NEU-123F_Numerische_Diagnose_Dreifachsumme.md` zeigt die Git-Historie ausschließlich den öffentlichen Import vom 26. Juli 2026; der Commit beschreibt den Import ausdrücklich als inhaltlich unverändert.

Daher ist die Klassifikation

`post-Juli -> NEW-DIRECT-AUDIT`

als Provenienzbehauptung falsch.

**Korrektur:** Diese Dateien werden direkt gegen ihren Live-Inhalt reconciliert; ein `NEW-DIRECT-AUDIT` wird nicht aus einem angeblichen Entstehungsdatum abgeleitet.

### G-H2-2 — NEU-124 enthält keine N/log N-Skalenkorrektur

Live-NEU-124 ist ausdrücklich

`GESPERRTES PLATZHALTERBLATT`.

Es enthält ausschließlich Eintrittsbedingungen und offene Zielaussagen zu

- Spektrum,
- Punktspektrum/Einfachheit,
- Spektralmaß,
- Herglotz/RH-Zielkette.

Eine Skalenkorrektur `N -> N/log N` steht dort nicht.

**Korrektur:** Kein TARGETED-REAUDIT von NEU-124 auf eine nicht vorhandene Skalenbehauptung. Das Blatt bleibt `?[O]`/gesperrt; relevant ist nur, ob NEU-123 seine Eintrittsbedingungen erfüllt.

### G-H2-3 — NEU-125 enthält keinen direkten Jacobi->D_rel-Anschluss

Live-NEU-125 untersucht:

- skalare Prä-Lanczos-Skalierung,
- Lanczos-Kovarianz,
- Quotienteninvarianz `b2/b1`,
- positive nichtskalare Prä-Lanczos-Gewichtung `W_N^{1/2}B_NW_N^{1/2}`.

Ein Übergang

\[
A_N^{Jac,-}\to D_{rel}
\]

wird in NEU-125 nicht behauptet.

**Korrektur:** P06s Transport-No-Go für `D_rel` ist als allgemeine Routing-Firewall wichtig, aber nicht der lokale Prüfkern von NEU-125.

### G-H2-4 — Auch der Stamm NEU-123 ist kein direkter Jacobi->D_rel-Limes

Der Live-Stamm definiert einen abstrakten Jacobi-Grenzoperator `A_infty` auf `ell^2(N_0)` unter Koeffizientenkonvergenz und wesentlicher Selbstadjungiertheit. `D_rel` kommt in diesem Blatt nicht als Zieloperator vor.

Die historische Aussage „direkter Jacobi-Limes -> D_rel ist durch P06 superseded“ bleibt als Programmhistorie richtig, darf aber nicht dem heutigen Live-NEU-123-Stamm als dessen eigene Behauptung zugeschrieben werden.

---

## 3. Zusätzliche Live-Befunde, die der Gegencheck übersehen hat

### G-H2-5 — Konkrete Stufe 1 des unrenormierten NEU-123-Pfads scheitert bereits

NEU-123 verlangt für einen nichtdegenerierten Jacobi-Grenzoperator bei jedem festen Index

\[
a_{j,N}\to a_j,\qquad b_{j,N}\to b_j>0.
\]

Live-NEU-123A beweist jedoch exakt

\[
b_{1,N}=\frac{\gamma}{N}\sqrt{\sum_{n=2}^{N-1}\Lambda(n)^2}
\asymp \gamma\sqrt{\frac{\log N}{N}}
\to0.
\]

Damit ist die konkrete unrenormierte Stufe-1-Bedingung bereits beim ersten Offdiagonalparameter verletzt.

**Status:** `×[M]` für den nichtdegenerierten unrenormierten NEU-87-Jacobi-Limes mit `b_1>0`.

Dies ist stärker als die im vorgelegten Gegencheck verwendete Markierung `?[O]`.

### G-H2-6 — NEU-123A überzieht die Konsequenz von b1,N -> 0

Aus `b1,N -> 0` folgt sicher, dass der Startvektor `e_0` asymptotisch vom Rest entkoppelt. Bei `a0,N=0` gilt auf Resolventenebene

\[
\langle e_0,(A_N-z)^{-1}e_0\rangle\to -1/z.
\]

Daraus folgt aber **nicht**, dass alle weiteren Offdiagonalen `b_{j,N}` verschwinden oder der gesamte Grenzoperator diagonal wird.

Daher ist die Formulierung aus NEU-123A

`b1,N -> 0 => A_infty diagonal`

zu stark.

**Bindende Korrektur:** Nur der Startvektor-/erste Kantenblock kollabiert unrenormiert; globale Diagonalität ist nicht bewiesen.

### G-H2-7 — NEU-125 liest NEU-79s Feshbach-Skala falsch

NEU-125 behauptet in §125.0/F sinngemäß, NEU-79 liefere eine intrinsische Prä-Lanczos-Skala `sqrt(N)`.

Live-NEU-79 sagt dagegen exakt:

\[
J_N^- = \kappa_N\,U_N^*\mathsf S_NR_ND_{BC,N}U_N,
\qquad
\kappa_N=|\Sigma_N|,
\]

mit

\[
\kappa_N=N
\]

für die volle Labelmenge bzw.

\[
\kappa_N\sim N/\log N
\]

für Prim- oder Primpotenzlabels. Die effektiv relevante Skala ist

\[
\gamma_N=a_N\kappa_N,
\]

und deren Grenzverhalten bleibt in NEU-79 ausdrücklich `?[O]`.

Daher ist

`NEU-79 liefert intrinsisch sqrt(N)`

`×[M]`.

Die aus NEU-123A zur bloßen Stabilisierung von `b1,N` erforderliche skalare Größe wäre vielmehr

\[
c_N\asymp b_{1,N}^{-1}\asymp \sqrt{\frac{N}{\log N}},
\]

nicht `sqrt(N)` bei präziser Logarithmusbuchhaltung.

Erhalten bleibt aus NEU-125 nur das abstrakte exakte Lemma:

\[
A_N\mapsto c_NA_N
\quad\Longrightarrow\quad
a_{j,N}\mapsto c_Na_{j,N},\quad b_{j,N}\mapsto c_Nb_{j,N},
\]

also

\[
\frac{b_{2,N}}{b_{1,N}}
\]

ist unter positiver skalarer Prä-Lanczos-Skalierung invariant.

---

## 4. Numerische Direktverifikation

Die Tabellen aus `NEU-123F_Ergebnisse.md` und `NEU-123G_Zweite_Offdiagonale_Skaleninkohaerenz.md` wurden unabhängig aus den dort angegebenen Definitionen reproduziert.

Insbesondere stimmen die veröffentlichten Werte für

\[
D_N=T_N/S_N^{3/2}
\]

für `N=100,...,5000` sowie die Lanczos-Werte `a1,N/b1,N` und `b2,N/b1,N` für `N=30,...,200` numerisch überein.

Diese Reproduktion bestätigt **die endlichen Tabellen**, nicht die asymptotischen Zeichen `~`.

Daher bleibt:

- Diagonaldrift: `heur+num`, streng `?[O]`;
- `b2,N/b1,N -> infinity`: numerisch stark indiziert, streng `?[O]`;
- Behauptung `b2,N/b1,N ~ N`: nicht als strenger asymptotischer Satz migrieren.

---

## 5. Endurteil zum Gegencheck

Der vorgelegte H-T2-Gegencheck ist **nicht als kanonischer H-T2-Endaudit übernehmbar**.

Er enthält einen wertvollen richtigen Typbefund zum direkt über reelle Jacobi-Koeffizienten definierten selbstadjungierten Block, aber vier Provenienz-/Routingfehler und übersieht drei load-bearing Live-Befunde.

\[
\boxed{\text{H-T2-GEGENCHECK RECONCILED — Teilbefunde übernommen, fehlerhafte Folgeaufträge verworfen.}}
\]

Der kanonische Endstand steht separat in `AUDIT-2026-08-09_P08_HT2_Jacobi_Grenzoperator.md`.