# Merge-Review: numerische Proxy-Regressionen PR69/70/72/76/83/84

**Entscheidung: PR69 READY · PR70 READY · PR72 READY · PR76 READY · PR83 READY · PR84 READY.** Kein konkreter Merge-Blocker innerhalb des jeweils ausdrücklich ausgewiesenen Diagnose-/Proxy-Umfangs; keine notwendige Korrektur vor Integration. Die Freigabe beruht auf Originalausführungen **und** unabhängigen Gegenrechnungen, nicht allein auf den eingebauten `PASS`-Meldungen. (Original- und Kopfmetadaten (`numeric_69_84_metadata.json`), Gegenrechnung PR69/70 (`numeric_69_70_independent.log`), Matrixgegenrechnung (`numeric_independent_matrix_results.json`), 49 exakte Assertion-Nachprüfungen (`numeric_independent_exact_assertions.log`))

Stand: 07.09.2026. Beauftragter Repository-Tip: `a7f00fd6ef4824f2aecc934b52088127112a2b5f`; Gegenstand sind ausschließlich die sechs jeweils neu hinzugefügten Skripte, nicht andere PRs, GitHub-PR-Beschreibungen oder die gesamte analytische Beweiskette. (Prüfmetadaten (`numeric_69_84_metadata.json`), abschließende Read-only-Kontrolle (`numeric_final_readonly_check.log`))

## Exakte Köpfe und Blobs

Jeder der sechs Diffs gegen seine gestapelte Basis fügt genau das angegebene Skript hinzu; dessen Blob am jeweiligen PR-Kopf stimmt mit dem Blob am beauftragten Integrationstip und dem ausgeführten Arbeitsbaum überein. (Diff-/Blobprotokoll (`numeric_69_84_metadata.json`), abschließende Hashprüfung (`numeric_final_readonly_check.log`))

| PR / Urteil | Exakter Kopf | Exakter Skriptblob |
|---|---|---|
| [69](https://github.com/Waschtl904/objekt-x-programm/pull/69) **READY** | `5a5776c36ed31475ef6e8a715371307f1f6b8341` | `6d9cb4b42f1b8b89867ed170e1163c94cf51c3b8` |
| [70](https://github.com/Waschtl904/objekt-x-programm/pull/70) **READY** | `1a64e9d1841de170f96dd9d9f018ec41da46e415` | `a0322e122b3ba262f5f8a69c7ba3fcc47ed459ed` |
| [72](https://github.com/Waschtl904/objekt-x-programm/pull/72) **READY** | `25c27bd7f0646e7a63c3cba109336c6414fee72b` | `eda88c7145bed4d8b7c654969a67ec736f11aed3` |
| [76](https://github.com/Waschtl904/objekt-x-programm/pull/76) **READY** | `d2d8b9077a61f5d103bcec02548fdf29fa282c2e` | `514b44ce84e27de697d1d47ab6683439ecbfb3d4` |
| [83](https://github.com/Waschtl904/objekt-x-programm/pull/83) **READY** | `4abccc2dd29d87f914440478c286dbc6edf11169` | `237bf3406debcc3d2ec757ce547d3759c55a1fc2` |
| [84](https://github.com/Waschtl904/objekt-x-programm/pull/84) **READY** | `3e4e5a73679db9f88624869587c4bd3bc3fec266` | `bb0ccb9e788bb0949ab1ea01b80ad6f6ce5fef4d` |

Die Dateipfade lauten jeweils `audits/P11_R43_<Name>_2026-09-06.py`, mit den folgenden Namen und Originalprotokollen. (Metadaten (`numeric_69_84_metadata.json`))

| PR | Name | Originalausführung |
|---|---|---|
| 69 | `REVERSE_EXTENSION_COUNTERTEST` | Exit 0; 0,015 s (`numeric_pr69_original.log`) |
| 70 | `REVERSE_EXTENSION_MULTICHANNEL_TOY` | Exit 0; 0,227 s (`numeric_pr70_original.log`) |
| 72 | `REVERSE_EXTENSION_GALERKIN_GRAPH_PROXY` | Exit 0; 0,139 s (`numeric_pr72_original.log`) |
| 76 | `REVERSE_MEAN_LOCALIZATION_DIAGNOSTIC` | Exit 0; 0,155 s (`numeric_pr76_original.log`) |
| 83 | `SCHUR_CORR_STRUCTURED_HUB_PROXY` | Exit 0; 0,239 s (`numeric_pr83_original.log`) |
| 84 | `SCHUR_VAR_DELTA_SWEEP` | Exit 0; 14,439 s (`numeric_pr84_original.log`) |

Alle Originale liefen unverändert, ohne `-O`, mit `PYTHONDONTWRITEBYTECODE=1` und `OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=NUMEXPR_NUM_THREADS=VECLIB_MAXIMUM_THREADS=BLIS_NUM_THREADS=1`; Arbeitsverzeichnis und sämtliche Logs lagen außerhalb des Repos im Merge-Verzeichnis. (Beispielprotokoll mit Umgebung (`numeric_pr84_original.log`))

## Unabhängiger Prüfpfad

- **69/70:** 60-stellige `Decimal`-Logarithmen, Lucas-Lehmer-Prüfung des verwendeten Mersenne-Primkandidaten, separat durch Probedivision erzeugte Primbandlisten und `fsum`-Summation; skalares Minimum zusätzlich durch quadratische Ergänzung und direktes Einsetzen geprüft. (Gegenrechnung (`numeric_69_70_independent.log`))
- **72/76/83/84:** Keine Imports aus den Originalskripten; Graphmatrizen unabhängig über paarweise Gitterabstände aufgebaut, NumPy-Linearsolver statt des selbstgeschriebenen Cholesky-Verfahrens, Schur-Komplement gegen direkte Energie und Sternminima geprüft. (Prüfprogramm (`numeric_independent_matrix_check.py`), Ergebnisprotokoll (`numeric_independent_matrix_check.log`))
- **84:** Alle 24 Kombinationen aus drei Quellradien und acht Bandbreiten, jeweils beide Resolventenendpunkte, mit individuellen Primverschiebungen neu gerechnet; Varianzen aus hochpräziseren zweiten Momenten und einer paarweisen Formel für die Zwischenbandkomponente kontrolliert. (48 Endpunktresultate (`numeric_independent_matrix_results.json`))
- Zusätzlich wurden **49 Original-Assertions** zu Zahlenankern und Vergleichen für 72/76/83/84 mit den unabhängig ermittelten Werten und den **unveränderten Originaltoleranzen** ausgewertet; alle waren wahr. (Assertion-Protokoll (`numeric_independent_exact_assertions.log`))

## Einzelurteile

### PR69 — READY

**Prüfung:** Bei \(U=80,V=100,u=40,p=2^{127}-1\) ergibt die unabhängige Rechnung \(r=8\log80=35{,}056213077391\), \(a_p=44{,}014845965557\), \(J_{p,U}(u)=0\), \(J_{p,V}(u)=1\); die Endpunkte sind \(-4{,}014845965557\) und \(84{,}014845965557\). Damit liegt der Ausgangspunkt außerhalb des bezeichneten Collars, ein Halbschritt-Endpunkt im alten Fenster und der andere im neuen Streifen; die Ungleichungen sind nicht rundungskritisch. (Original (`numeric_pr69_original.log`), 60-stellige Gegenrechnung (`numeric_69_70_independent.log`))

**Mathematik und Typen:** \(z_+-z_-=\log p\) ist korrekt; ein im alten Summanden unterstütztes \(\iota x_{\rm bulk}\) ist nicht selbst ein streifenwertiger Korrekturparameter \(y\in N\). Der Zeuge widerlegt die naive geometrische Implikation „außerhalb des Collars ⇒ keine neue primitive Auflösung“, nicht einen Satz über das tatsächliche \(x_{\rm rev}\). ([PR69, Skript Z. 10–26 und 60–82](https://github.com/Waschtl904/objekt-x-programm/pull/69))

**Scope:** Der explizite Ausschluss eines Theorembeweises bzw. Reverse-Normal-Zerfalls ist ausreichend; die Zahlenprüfung wird nicht als Anwendung eines asymptotischen Collar-Satzes hochgestuft. **Minimalkorrektur: keine.** ([PR69, Skript Z. 4–8](https://github.com/Waschtl904/objekt-x-programm/pull/69))

### PR70 — READY

**Mathematik:** Für \(E=\sum_p w_px_p^2\), \(S=\sum_pw_px_p\), \(W=\sum_pw_p\) hat \(F(y)=y^2+\sum_pw_p(y+x_p)^2\) eindeutig das Minimum \(E-S^2/(1+W)\) bei \(y_*=-S/(1+W)\); die Zerlegung in gewichtete Varianz und \(W/(1+W)\bar x^2\) ist korrekt. Im Skript wird jedes Profil tatsächlich auf \(E=1\) normiert, nicht auf ungewichtete Punktenergie. ([PR70, Skript Z. 14–29 und 96–118](https://github.com/Waschtl904/objekt-x-programm/pull/70), unabhängige quadratische Ergänzung (`numeric_69_70_independent.log`))

**Zahlen:** Die separat erzeugten Bänder enthalten 663, 4.074 und 25.846 Primzahlen; \(W=494{,}680246280551\), \(\log30/30=0{,}113373246055\). Die Minima sind `constant=0.002017429598`, `slow=0.088403947514`, `freq1=0.986379755204`, `freq10=0.748027195734`; damit stimmen sämtliche behaupteten Zielvergleiche. Auch die Tiefen-/Trägerbedingungen wurden für sämtliche verwendeten Primzahlen gegengeprüft. (Original (`numeric_pr70_original.log`), Gegenrechnung (`numeric_69_70_independent.log`))

**Scope:** Ein gemeinsamer Streifenpunkt und vier gewichtet normierte Profile sind eine Kohärenzdiagnose, keine uniform-asymptotische Aussage über beliebige \(U\) oder das kanonische Reverse-Normal-Problem. Der vorhandene Diagnose-/Theoremausschluss bleibt maßgeblich. **Minimalkorrektur: keine.** ([PR70, Skript Z. 4–8 und 30–32](https://github.com/Waschtl904/objekt-x-programm/pull/70))

### PR72 — READY

**Mathematik:** Der positive Graphoperator ist \(A_T=I+L_T\); die neuen Werte lösen korrekt den neuen Block der Normalgleichung. Unabhängig wurde der normierte Zusatz
\[
\frac{x^\top\left((A_V)_{OO}-(A_V)_{ON}(A_V)_{NN}^{-1}(A_V)_{NO}-A_U\right)x}
     {x^\top A_Ux}
\]
gegen die direkte Differenz aus voller minimaler Energie und alter Energie gerechnet; maximale Abweichung unter \(2{,}6\cdot10^{-14}\). Der alte Residualanteil wird genau einmal abgezogen, die neue \(L^2\)-Strafe genau einmal hinzugefügt. ([PR72, Skript Z. 116–171](https://github.com/Waschtl904/objekt-x-programm/pull/72), Matrixgegenrechnung (`numeric_independent_matrix_check.log`))

**Zahlen:** Für `constant / linear / gaussian / cos-low / cos-mid / cos-high` ergeben sich `0.327207400132 / 0.006519913360 / 0.000382711739 / 0.004518077742 / 0.267353927272 / 0.107141920815`; alle Anker und die Vergleiche `constant > 2·target`, `gaussian < 0.01·target` sind unabhängig bestätigt. (Original (`numeric_pr72_original.log`), exakte Assertion-Toleranzen (`numeric_independent_exact_assertions.log`))

**Scope:** Echte Primgewichte, aber Verschiebungen nur an den Bandzentren 10/12/14, endliches Integergitter und kein tatsächliches \(x_{\rm rev}\): ausdrücklich offengelegt und **kein Blocker**. Die \(O(\log U/U)\)-Sprache wird nur als heuristische Vergleichsskala des ausgewiesenen endlichen Tests akzeptiert, nicht als durch einen einzelnen \(U\)-Wert widerlegter asymptotischer Satz. Der Skripttext schließt insbesondere eine Anwendung des großen-\(U\)-Collars bei \(U=30\) aus. **Minimalkorrektur: keine.** ([PR72, Skript Z. 5–14, 21–30 und 49–51](https://github.com/Waschtl904/objekt-x-programm/pull/72))

### PR76 — READY

**Wesentlicher Strukturcheck:** Die Sternzerlegung wäre nicht ohne Weiteres die volle Erweiterungsenergie, wenn neue Knoten untereinander gekoppelt wären. Für **die verwendeten Eingaben** gibt es aber keine New–New-Kante: jeder Streifen hat Durchmesser 9, kleinste Verschiebung 10, und gegenüberliegende Streifen liegen weiter auseinander als 14; der unabhängig aufgebaute neue Matrixblock ist tatsächlich diagonal. Somit entsprechen die 20 lokalen Sternminima exakt dem Zusatz aus PR72. (Matrixprüfprogramm (`numeric_independent_matrix_check.py`), Ergebnisse einschließlich `no_new_new_edges` (`numeric_independent_matrix_results.json`))

**Normierung und Schranke:** Sowohl Varianz als auch Mittelwertkosten werden durch dieselbe alte Graphenergie geteilt; die gewichtete Cauchy-Schranke \(\mathrm{mean}\le \sum_iw_ix_i^2/(1+W)\) ist korrekt und wurde gegen die Stern-/Schur-Energie geprüft. ([PR76, Skript Z. 79–130](https://github.com/Waschtl904/objekt-x-programm/pull/76), Gegenrechnung (`numeric_independent_matrix_results.json`))

**Zahlen:** Mittelwert/Varianz sind für `constant` `0.327207400132 / 0`, für `center-gauss12` `0.000009270339 / 0.000373441400`, für `edge-gauss-wide` `0.001438090365 / 0.024613165831`, für `edge-gauss-narrow` `0.000570030149 / 0.076141193458`; auch das symmetrische Randprofil und alle gedruckten Cauchy-Schranken stimmen. (Original (`numeric_pr76_original.log`), unabhängige Resultate (`numeric_independent_matrix_results.json`))

**Scope:** Kontrolliert wird Masse auf verschobenen Urbildmengen, nicht ausschließlich terminale Collar-Masse; Lokalisierung kann die Mittelwertkosten senken, schließt aber weder die Varianz noch tatsächliches \(\rho_{\rm rev}\). Diese Grenze ist ausdrücklich angegeben. **Minimalkorrektur: keine.** ([PR76, Skript Z. 36–41 und 177–182](https://github.com/Waschtl904/objekt-x-programm/pull/76))

### PR83 — READY

**Mathematik und Typen:** Ungerade kompakte Quelle plus antisymmetrische Halbschrittdifferenz ergibt einen geraden Hubvektor; beide symmetrischen Resolventen erhalten diese Parität. Die Nullfortsetzung vor \(B_V\) und anschließende Kompression sind korrekt; die separat aufgebaute Kreuzblockabbildung liefert den Forcing-Vektor tatsächlich auf den 20 neuen Knoten, bis auf die offengelegte irrelevante Vorzeichenkonvention. ([PR83, Skript Z. 90–173 und 187–206](https://github.com/Waschtl904/objekt-x-programm/pull/83), Gegenrechnung (`numeric_independent_matrix_check.log`))

**Träger und Kosten:** Für \(X\le8\) liegt der rohe Hubträger strikt innerhalb \(|u|<15\), während die zentrierten Streifen-Urbildpunkte \(|u|\ge17\) haben; rohe Kopplung ist daher wirklich null und nicht bloß zufällig numerisch klein. Die Resolventen erzeugen hingegen nichtverschwindendes Forcing, und bei allen sechs Endpunkt-/Radiuskombinationen ist die Varianz mehr als 100-mal so groß wie der Mittelwertterm. ([PR83, Skript Z. 98–112 und 327–339](https://github.com/Waschtl904/objekt-x-programm/pull/83), unabhängige Endpunktresultate (`numeric_independent_matrix_results.json`))

**Zahlen bei \(X=8\):** Für \(B_UH^*\) sind Korrelation/Mittelwert/Varianz `0.664240560528 / 0.000322636158 / 0.077745751310`; für den komprimierten \(B_VH^*\)-Endpunkt `0.613995296110 / 0.000155099418 / 0.040374695619`. Sämtliche Originalanker halten auch mit unabhängig berechneten Werten und Originaltoleranzen. (Original (`numeric_pr83_original.log`), Assertion-Nachprüfung (`numeric_independent_exact_assertions.log`))

**Scope:** Quellfamilie statt kanonischem Whitening, aggregierter Hub und zwei Resolventenendpunkte statt \(Q\) sind explizit ausgewiesen; die euklidische Forcing-Korrelation ist eine ungesättigte Proxygröße, kein Ersatz für eine kanonische Schur-/Reverse-Normal-Schätzung. **Diese Nichtkanonizität ist kein Blocker. Minimalkorrektur: keine.** ([PR83, Skript Z. 7–45](https://github.com/Waschtl904/objekt-x-programm/pull/83))

### PR84 — READY

**Mathematik:** Graphgewichte und Hubamplituden werden bandweise jeweils auf ihre eigene Basismasse normiert; die unabhängige Rechnung bestätigt die Massenerhaltung bis \(5{,}7\cdot10^{-14}\) bzw. \(4{,}5\cdot10^{-16}\). Individuelle Halblogverschiebungen, lineare Interpolation nur innerhalb des alten Fensters und die Gewichtung der drei Bandmittel sind korrekt; die vollständige Varianzzerlegung wurde mit einer zweiten-Moment-/Paarformel gegengeprüft. ([PR84, Skript Z. 96–148 und 222–291](https://github.com/Waschtl904/objekt-x-programm/pull/84), Gegenrechnung (`numeric_independent_matrix_check.log`))

**Sweep:** Alle 48 Endpunktfälle stimmen; die sechs unabhängig bestimmten Log-Log-Steigungen liegen zwischen `2.001145996` und `2.002330028`, die Interband-Max/Min-Verhältnisse zwischen `1.014852481` und `1.038248648`. Bei \(\delta=0.005\) liegt `intra/inter` zwischen etwa \(5{,}45\cdot10^{-6}\) und \(6{,}68\cdot10^{-6}\), also deutlich unter der behaupteten Grenze \(10^{-4}\). (Original (`numeric_pr84_original.log`), vollständige Gegenrechnung (`numeric_independent_matrix_results.json`))

**Repräsentative Anker \(X=8\):**

| \(\delta\) | \(B_U\): intra / inter | komprimiertes \(B_V\): intra / inter |
|---|---|---|
| 0.15 | `0.000388315430266 / 0.076129657139651` | `0.000207471163287 / 0.039647220909735` |
| 0.005 | `0.000000422749374 / 0.077601820098541` | `0.000000225474316 / 0.040236080523583` |

Auch diese Anker erfüllen bei unabhängiger Berechnung die Originaltoleranzen, einschließlich \(10^{-13}\) für die kleinsten Intra-Werte. (Assertion-Protokoll (`numeric_independent_exact_assertions.log`))

**Scope:** Die Resolventen und die Graphnorm bleiben ausdrücklich auf dem Baseline-Bandzentrumsgitter eingefroren; nur Hub und Sternabtastung sind primaufgelöst. „Fixed mass“ meint die volle Bandmasse, nicht zwangsläufig die aktive Masse an jedem einzelnen Randstern, wo die Fensterbedingung Primzahlen ausschließt. Das ist die implementierte Hybrid-Diagnose und kein Fehler für die genutzten Eingaben. Der beobachtete \(\delta^2\)-Trend und die Route-A/B-Deutung werden ausschließlich für diesen endlichen Sweep akzeptiert, nicht als bewiesener Grenzübergang oder kanonisches Theorem. **Minimalkorrektur: keine.** ([PR84, Skript Z. 20–42 und 254–261](https://github.com/Waschtl904/objekt-x-programm/pull/84))

## Abschluss und Integrationsgrenze

**Integration dieser sechs exakten Skriptstände ist numerisch freigegeben.** Keine falsche Assertion, kein für die verwendeten Eingaben wirksamer Rechen-/Normierungsfehler und kein unter Berücksichtigung der ausdrücklichen Firewalls unqualifizierter Kontinuum-Theoremanspruch festgestellt; zusätzliche kanonische Quellen, feinere Gitter oder weitere Band-/Parameterforschung sind **keine Voraussetzung** dieser Freigabe. (Gegenrechnungen (`numeric_independent_matrix_results.json`), Assertion-Nachprüfung (`numeric_independent_exact_assertions.log`), [PR69](https://github.com/Waschtl904/objekt-x-programm/pull/69), [PR70](https://github.com/Waschtl904/objekt-x-programm/pull/70), [PR72](https://github.com/Waschtl904/objekt-x-programm/pull/72), [PR76](https://github.com/Waschtl904/objekt-x-programm/pull/76), [PR83](https://github.com/Waschtl904/objekt-x-programm/pull/83), [PR84](https://github.com/Waschtl904/objekt-x-programm/pull/84))

Das Review hat weder Repo-Dateien noch GitHub geändert; abschließend sind alle sechs Arbeitsbaumblobs unverändert, der Tip ist weiterhin `a7f00fd6ef4824f2aecc934b52088127112a2b5f`, und der erfasste Status getrackter Dateien ist leer. (Read-only-Abschlussprotokoll (`numeric_final_readonly_check.log`))

Alle Ergebnisse, Logs, exakten Skriptkopien und das unabhängige Prüfprogramm verbleiben in `/home/user/workspace/r43_merge_20260907/`; der maschinenlesbare Zwischenstand enthält inzwischen für alle sechs PRs `READY`. (Statusdatei (`numeric_progress_69_84.json`), Metadaten (`numeric_69_84_metadata.json`), Prüfprogramm (`numeric_independent_matrix_check.py`))
