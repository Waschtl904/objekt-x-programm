# P11 / R43 — XBAND: Anker-Firewall und symmetrische Quellen-Nachrechnung

Datum: 7. September 2026. **Draft. Keine unabhängige externe Freigabe.**
Lokale Beweise und numerischer endlicher Proxy werden getrennt geführt.
Keine Änderung einer Registry und keine Promotion globaler Gates.

## 1. Provenienz und Abgrenzung

Die Live-Abfrage bestätigte zunächst PR #83 auf
`4abccc2dd29d87f914440478c286dbc6edf11169` und PR #84 auf
`3e4e5a73679db9f88624869587c4bd3bc3fec266`, beide offen, Draft, ungemergt.
Beide Python-Quellen wurden über den GitHub-Connector vollständig gelesen.
Die hier beigefügte Implementierung ist eine eigenständige Nachimplementierung
 ihrer Definitionen, kein byteidentischer Export dieser Elternskripte.

Der vom Nutzer genannte lokale Patch `fe907714045f35a955b8807dec4a3118224b3f13`
war in dieser Sitzung nicht als ausführbarer Anhang verfügbar. Zugänglich waren
seine Zusammenfassung und zwei Vorschau-Links. Dieser neue Stand behauptet daher
weder, dieser Commit zu sein, noch dessen berichtete unabhängige Freigabe zu erben.

Beim Veröffentlichungscheck existierte bereits der separate Branch
`r43-schur-xband-comm` auf `2980b95136886935410c7ca9b2bb2bb49c23122d`.
Er lag bei dieser Abfrage zwei Commits über #84. Vor der Veröffentlichung
bewegte er sich weiter auf `4381c73e4220953899d8484a0ed58cd4815256d9`.
Die vorliegende Ergänzung setzt als eigener Stack auf diesem zuletzt
verifizierten exakten Head auf;
der vorhandene Branch und seine Dateien bleiben unverändert. Sie ergänzt die
zwei Anker, deren symmetrische Zusammenfassung und eine neue Quellenraumprüfung.
Die bisherigen Dateien werden hier nicht als unabhängig zertifiziert bezeichnet.

Eingelesene Elternblobs:

| Quelle | Git-Blob |
| --- | --- |
| PR #83, `P11_R43_SCHUR_CORR_STRUCTURED_HUB_PROXY_2026-09-06.py` | `237bf3406debcc3d2ec757ce547d3759c55a1fc2` |
| PR #84, `P11_R43_SCHUR_VAR_DELTA_SWEEP_2026-09-06.py` | `bb0ccb9e788bb0949ab1ea01b80ad6f6ce5fef4d` |

## 2. Tatsächlich ausgeführte Rechnung

Das Modell behält U=30, V=40, die Bandzentren 10,12,14 und die ungeraden
kompakten Quellen mit X=4,6,8. Die Primgewichte und Hubamplituden werden durch
Sieb und Summation neu berechnet, nicht aus der Ergebnistabelle eingesetzt.

```text
Graphmassen: 44.59817706246725, 120.89687763600345, 329.1851915820806
Hubmassen:   1.1572520185069353, 1.7361325665411198, 2.6546513413534485
```

Die drei Transporte sind BU=A_U^(-1), BT=iota* B_V iota und Q=BU#BT.
Q wird durch die positive Quadratwurzelformel berechnet und mit vertauschten
Endpunkten, einer Cholesky-Kongruenzkonstruktion und Q A_U Q=BT verglichen.
Keines davon ist der analytische P11-Transport.

Geprüft werden beide Strip-Seiten, jedes der drei tatsächlichen Bandpaare,
beide Anker, die volle quadratische Identität und ihre Interferenz.
Für die großen Kontrollshifts +/-10,+/-12,+/-14 werden globale
Kommutatornormen, Resolventen- und Sylvesteridentitäten zusätzlich protokolliert;
sie sind keine zusätzlichen ANOVA-Paare. Der Test enthält komplexe Zufallsdaten
und die globalen Phasen i, exp(.37i), exp(1.9i). Sämtliche Energien verwenden
komplexe Konjugation im ersten Argument. Die 108 CSV-Zeilen trennen
3 Quellen x 3 Transporte x 2 Anker x 2 Seiten x 3 Paare.

Der vollständige Hybrid-Sweep aus #84 wird für alle acht Bandbreiten und alle
drei Quellen neu gerechnet, zusätzlich auch für Q. Die ursprünglichen
repräsentativen BU-/BT-Zahlen werden als Reproduktionsanker überprüft.
Das ist eine neue Ausführung derselben Mathematik, nicht die Ausführung der
Originaldateien oder ein externer unabhängiger Review.

## 3. Vorzeichen und lokale Nenner

Es gilt (tau_h x)(u)=x(u-h). Auf dem rechten Strip sind
u_i=z-t_i, u_j=z-t_j, h=t_j-t_i. Daher

```math
(T_h-I)x(u_i)=x(u_j)-x(u_i).
```

Die entgegengesetzte Differenz benötigt ein Minuszeichen. Der Test richtet beide
Anker auf d=x(u_i)-x(u_j) aus:

```math
a_\ell=-[B(T_h-I)v](u_i),\qquad
c_\ell=-[(T_hB-BT_h)v](u_i),
a_r=[B(T_{-h}-I)v](u_j),\qquad
c_r=[(T_{-h}B-BT_{-h})v](u_j).
```

Auf dem linken Strip wird h ebenfalls gespiegelt. Immer gilt
 d=a_l+c_l=a_r+c_r. Ein gleichzeitiges Vorzeichenwechseln von a und c verändert
die Interferenz nicht; der hier relevante Unterschied entsteht durch den
anderen Auswertungsanker und den zugehörigen Kommutator.

Jede Beobachtung wird mit sqrt(W_i(z) W_j(z)/W(z)) gewichtet, wobei W(z) die
Summe **aller** am selben z aktiven Kanäle ist. Erst anschließend werden die
quadratischen Größen durch G=(Bv)* A_U (Bv) dividiert. Die Beobachtungen bilden
einen euklidischen Hilbertraum; auf dem gesamten alten Fenster induzieren sie
nur eine Seminorm. Eine absichtlich falsche paarweise Nennerwahl wird verworfen.
Ein zusätzlicher Geometrietest mit äußerem Fenster 44 enthält Sterne mit zwei
und mit nur einem aktiven Band, nicht bloß drei durchgehend aktive Kanäle.

## 4. Reproduktion des gemeldeten Ankerwechsels

Für Q, X=8 liefert die neue Ausführung:

| Anker | A2/G | C2/G | Interferenz/G | V_inter/G |
| --- | ---: | ---: | ---: | ---: |
| kleineres Bandzentrum | .060840752951 | .000280036495 | -.004849137710 | .056271651736 |
| größeres Bandzentrum | .051633147833 | .000311163924 | +.004327339979 | .056271651736 |

Die gerundete Nutzertabelle wird reproduziert. Die Gesamtvarianz ist dieselbe;
die Zerlegung in Hauptanteil und Kommutator ist es nicht. Deshalb ist das
Vorzeichen der einseitig gemessenen Interferenz kein ankerinvariantes Merkmal.
Das schließt spezifisch bewiesene Kürzungen nicht aus; es widerlegt die
Interpretation eines beliebig gewählten negativen Kreuzterms als bereits
gefundenen kanonischen Kürzungsmechanismus.

## 5. Neues exaktes Lemma: Symmetrisierung und Ankerdefekt

Arbeite im oben definierten **unnormierten** Beobachtungsraum. Setze

```math
a_s=(a_\ell+a_r)/2,\quad c_s=(c_\ell+c_r)/2,\quad
 e=(a_\ell-a_r)/2=-(c_\ell-c_r)/2.
```

Dann gilt d=a_s+c_s. Die parallelogrammatischen Identitäten ergeben exakt

```math
\tfrac12(\|a_\ell\|^2+\|a_r\|^2)=\|a_s\|^2+\|e\|^2,
\tfrac12(\|c_\ell\|^2+\|c_r\|^2)=\|c_s\|^2+\|e\|^2,
\tfrac12(I_\ell+I_r)=I_s-2\|e\|^2,
\qquad I_s=2\Re\langle a_s,c_s\rangle.
```

**Beweis.** Schreibe a_l=a_s+e, a_r=a_s-e, c_l=c_s-e,
c_r=c_s+e und multipliziere aus. Die linearen Kreuzterme mit e heben sich im
Mittel auf; im gemittelten Interferenzterm bleibt -2||e||^2. Ende des Beweises.

Insbesondere ist das arithmetische Mittel der zwei Interferenzwerte nicht
identisch mit der Interferenz der gemittelten Amplituden. Es enthält einen
expliziten negativen Ankerdefekt. Diese Symmetrisierung ist invariant unter
Vertauschung der **beiden hier definierten Anker**. Es wird keine allgemeine
kanonische oder gauge-unabhängige Zerlegung des analytischen Modells behauptet.

Für Q, X=8:

```text
||a_s||^2/G = .0561054020170456
||c_s||^2/G = .0001640518342681
I_s/G       = +.000002197884705869
||e||^2/G   = .0001315483749129
V_inter/G   = .0562716517360197
```

Der negative Mittelwert der ursprünglichen Interferenzen wird hier durch den
Ankerdefekt erklärt; die symmetrische Interferenz ist leicht positiv.
Für Q sind die symmetrischen Interferenzen bei X=4 und X=6 ebenfalls positiv,
mit .000992078438504 und .000285035467092. Das sind numerische Befunde für diese
Quellen, kein allgemeiner Positivitätssatz.

## 6. Stärkerer Test: alle diskreten ungeraden Quellenrichtungen

Für jeden Radius X wird der vollständige Raum mit Basis
(delta_k-delta_-k), 1<=k<X, durch denselben endlichen Hub geschickt.
Die Beobachtungsmatrizen werden **vor** der Normierung mit G aufgebaut;
die Implementierung hebt die spaltenweisen Hilfsnormierungen explizit auf.
Damit sind die Quellen-Grammatrizen echte quadratische Formen:

```math
G_s=A_s^*A_s,\quad G_c=C_s^*C_s,\quad G_d=D^*D,
G_i=A_s^*C_s+C_s^*A_s,\quad G_d=G_s+G_c+G_i.
```

Ist G_s positiv definit, charakterisieren verallgemeinerte Rayleigh-Quotienten
exakt die Extremwerte von C2/A2, I/A2 und V/A2. Die Auswertung dieser Eigenwerte
ist hier Gleitkommanumerik, keine Intervallzertifizierung.

Für Q, X=8, Dimension 7, ergeben sich:

```text
sup ||c_s||/||a_s||        = .0920709415211
range I_s/||a_s||^2        = [-.0665525409727, +.1350086613201]
range V_inter/||a_s||^2    = [.9360477139967, 1.1415339673533]
range V_inter/G           = [.0046965241394, .0855379955748]
cond(G_s)                 = 66.2214435310
```

Die zu beiden Interferenzextremen gehörenden Quellenkoeffizienten werden im
JSON ausgegeben und rückgeprüft. **Auch die symmetrische Interferenz ist also
im vollständigen endlichen Quellenraum numerisch vorzeichenindefinit.** Die
positive Interferenz der drei glatten Quellen darf nicht zu einer allgemeinen
Positivitätsbehauptung hochgestuft werden. Andererseits zeigen die
Rayleigh-Zahlen keine fast vollständige Auslöschung des Quellenhauptanteils.

## 7. Exakte Reduktion auf den verbleibenden Quellenanteil

Wenn ||c_s||<=rho ||a_s|| mit rho<1, dann gilt

```math
(1-\rho)^2\|a_s\|^2\le\|d\|^2\le(1+\rho)^2\|a_s\|^2.
```

Dies folgt aus der umgekehrten und der gewöhnlichen Dreiecksungleichung. Die
Schranke wird **nach** der vollständigen Interferenzmessung ausgewertet, nicht
als Ersatz dafür. Bei einem einheitlichen rho<=rho_0<1 ist entlang einer Familie
V_inter/G -> 0 äquivalent zu ||a_s||^2/G -> 0. Kleine relative Kommutatoren
beseitigen diesen Engpass nicht; sie isolieren ihn.

Für die glatte Quelle Q, X=8 ist rho=.0540739638050. Daraus folgt mit den
numerisch ausgewerteten Größen die Untergrenze .0502017708954 für V_inter/G,
also rund 89.2% des gemessenen Wertes. Dies ist eine quantitative finite
Diagnose, keine bewiesene asymptotische Untergrenze für kanonische Daten.

## 8. Schur-Geometrie und richtige Sylvester-Skala

Mit alter/neuer Blockzerlegung von A_V ist

```math
A_{eff}=A_{OO}-A_{ON}A_{NN}^{-1}A_{NO}=A_U+K,\quad BT=A_{eff}^{-1}.
```

K ist positiv semidefinit: x*Kx ist das Minimum der zusätzlichen nichtnegativen
Kanten- und neuen Knotenenergie bei festgehaltenem alten x. Die alte Energie
bleibt dabei unverändert. K ist im endlichen Randkragen getragen.
Insbesondere muss für BT die Identität [T,BT]=BT[A_eff,T]BT verwendet werden.
Die falsche Ersetzung A_eff durch A_U wird als Negativkontrolle abgewiesen
(Frobenius-Abweichung für h=2 ungefähr .0364178856513).

Aus Q A_U Q=BT folgt für D=[T,Q]

```math
Q A_U D+D A_U Q=F,\quad F=[T,BT]-Q[T,A_U]Q.
```

Setze H=A_U^(1/2) Q A_U^(1/2), Z=A_U^(1/2) D A_U^(1/2),
Fhat=A_U^(1/2) F A_U^(1/2). Dann HZ+ZH=Fhat. Diagonalisieren von H zeigt:
Die inverse Sylvesterabbildung hat in diesen gewichteten Frobeniuskoordinaten
die exakte Norm 1/(2 lambda_min(H)). Diese Norm ist auf einem Rang-eins-Projektor
zum kleinsten Eigenwert erreichbar.

Ist A_eff<=Lambda A_U, dann BT>=Lambda^(-1) A_U^(-1) und
H^2=A_U^(1/2) BT A_U^(1/2)>=Lambda^(-1)I. Folglich ist die inverse Norm
höchstens sqrt(Lambda)/2. Im Proxy werden gemessen:

```text
Lambda = 1.886172828244
lambda_min(H) = .728130558158
gewichtete inverse Norm = .686690037106
```

Die kleinen absoluten Q-Eigenwerte führen hier also nicht zu einer kleinen
Sylvesterlücke in dieser Energiemetrik. Die Rückübersetzung mit einer groben
Konditionszahlabschätzung in ungewichtete Frobeniusnorm liefert dagegen etwa
1198.117697. Keiner dieser Werte ist unmittelbar eine Schranke in der
paargewichteten Beobachtungsseminorm; auch Fhat muss kontrolliert werden.
Die entsprechende Stabilitätsreduktion steht bereits im vorhandenen
XBAND-Bericht und wird hier nachgerechnet, nicht als neuer Fund beansprucht.

## 9. Randkontrollen und fehlende Distanztrennung

Die gepolsterte Matrixrechnung verifiziert
T_h T_k-T_(h+k)=-P tau_h (I-EP) tau_k E für gleich- und gegengerichtete Shifts.
T_-2 T_2-I ist minus die Projektion auf die letzten beiden Gitterpunkte.
Der Randimpuls verliert Norm 1, der ausdrücklich definierte glatte Kontrollbump
bump(u-29,3) verliert relativ .573826221104. Der rohe X=8-Hub verliert nichts.
Andere Randbump-Definitionen liefern andere Kontrollzahlen; das ist kein
Widerspruch zum vorhandenen XBAND-Test.

Für A_U=I+P L_infinity E-D_lost wird die Aufspaltung des Kommutators in
[P L_infinity E,T]-[D_lost,T] einschließlich Randzeilen und -spalten geprüft.
Die relevanten Schur-Präbilder sind genau
{-30,...,-17} union {17,...,30}, zugleich der Randkragen von D_lost.
Eine zunehmende Distanz zwischen Beobachtung und diesem Rand ist daher im
vorliegenden Modell gar nicht vorhanden. Randlokalität allein begründet
keine Unterdrückung in diesen Präbildern. Quellenabhängige Abschätzungen
bleiben davon unberührt und weiterhin erforderlich.

## 10. Numerische Kontrolle und Reproduktion

Umgebung der lokalen Ausführung: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
Alle protokollierten skalierten Residuen liegen unter 5e-11; Maximum:
2.7681355859734495e-13 bei der Sylvester-Rückrekonstruktion.
Die Skalierung lautet ||lhs-rhs||/max(1,||lhs||,||rhs||). Dies ist weder ein
Intervallbeweis noch für alle Tests dieselbe physikalische Norm.

| Matrix | kleinster Eigenwert | größter Eigenwert | Konditionszahl |
| --- | ---: | ---: | ---: |
| BU | .000573140718019 | 1.000000000000 | 1744.77221485 |
| BT | .000571965891153 | .756620072696 | 1322.84124700 |
| Q | .000572612001160 | .869815439667 | 1519.03110292 |

Der zusätzliche vollständige Q-Bandbreiten-Sweep hat für X=8 den
Intra-Band-Exponenten 2.00132710665 und Inter-Band-max/min 1.01715901616.
Auch hier bleiben alle Resolventen auf den Bandzentren eingefroren.
Die exakte ANOVA- und Paaridentität wird für die aufgelösten Bandmittelwerte
separat geprüft. Diese werden nicht mit den Bandzentrum-Präbildern gleichgesetzt.

```sh
OPENBLAS_NUM_THREADS=1 python audits/P11_R43_SCHUR_XBAND_ANCHOR_RECHECK_2026-09-07.py \
  --output xband_recheck_results.json
```

Das Programm erzeugt JSON mit sämtlichen Tabellen, Phasen-/Identitätsresiduen,
Quellenraumextrema, Extremalquellen und Sweep-Ergebnissen, außerdem die
paar-/seitenaufgelöste CSV. Es ist ohne `python -O` auszuführen.
Die CI führt denselben Test an einem exakten PR-Head mit Leserechten aus;
ein CI-Erfolg ist keine externe mathematische Freigabe.

Verwendete numerische Schnittstellen: SciPy-1.17.0-Dokumentation zu
`scipy.linalg.eigh` (hermitesche und verallgemeinerte Eigenwertprobleme) und
`scipy.linalg.solve_sylvester` (AX+XB=Q). Die mathematischen Abschätzungen oben
sind im Dokument hergeleitet und werden nicht aus einer Bibliotheksroutine
als Beweis übernommen.

## 11. Status und nächster engster Gate

`✓[M]_local`: orientierte Zwei-Anker-Identität; Symmetrisierung mit explizitem
Ankerdefekt; bedingte Quellenanteil-Reduktion; Rayleigh-Charakterisierung bei
positiv definitem Quellen-Gram. Die aufgeführten Schur-/Sylvesteridentitäten
werden nachgerechnet. Dies sind lokale Beweise, keine Registry-Promotion.

`✓[M]_proxy`: Reproduktion der Zahlen; volle Phase-/ANOVA-/Kompressionskontrollen;
positive symmetrische Q-Interferenz für die drei glatten Quellen;
vorzeichenindefinite Interferenz im vollständigen endlichen Quellenraum;
die angegebenen Spektren, unteren Schranken und Bandbreitenfits.

`?[O]`: externe Exact-Head-Prüfung, gerichtete Rundung der finite Quellenraum-
Ungleichungen, Kontrolle des echten konditionierten Quellenanteils und aller
kontinuierlichen beziehungsweise bewegten-Fenster-Übertragungen.

Nächster mathematischer Gate: **R43-SCHUR-XBAND-SYM-SOURCE** als präzisierte
Unterfrage des bestehenden HUB-DIFF-Gates. Zu kontrollieren ist die wirklich
paargewichtete Energie des symmetrisch transportierten Quellenunterschieds;
ein weiteres bloßes Vorzeichenexperiment für die Interferenz genügt nicht.
Ein separater finiter Zertifikatskandidat ist für Q, X=8
G_c < .093^2 G_s und G_d > .935 G_s. Die Numerik unterstützt beides; ein
Intervallzertifikat wurde nicht erstellt.

## 12. Unveränderte globale Firewalls

Es wird nicht G_(R,cond)^(-1/2) epsilon_R berechnet, nicht das analytische Q und
nicht das kanonische x_rev. Die geraden Integer-Shifts sind eine Besonderheit
des endlichen Modells. Weder der Quellenraumtest noch der prime-resolved
Hybrid-Sweep löst diese Diskretisierung auf Ebene der Resolventen auf.
Reverse-Normal-Stretch-Decay, FD23-UNIF, FLAGDYN/TIGHT, Strong Terminal/C6,
Objekt X und RH erhalten aus diesen Rechnungen keine neue globale Buchung.
