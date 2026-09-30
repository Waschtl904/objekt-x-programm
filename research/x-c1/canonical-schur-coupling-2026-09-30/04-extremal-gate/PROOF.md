# Symmetrisches Extremalproblem und Grenzen der vorhandenen Einschließungen

30. September 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Beweisbasis: `Waschtl904/objekt-x-programm` auf
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b`.

## Ergebnis

**Die vier vorgeschlagenen verbesserten Restgrenzen sind als Korollar exakt
bestätigt. Die tatsächliche Extremalrichtung bei A₉→A₁₁ ist weiterhin nicht
isoliert.**

Das vorgeschlagene symmetrisch-definite Verfahren wurde auf die vorhandenen
Momentfamilien angewandt. Die Cholesky-Einschließung des positiven Nenners
gelingt. Die resultierenden K-Intervalle liefern jedoch in beiden Paritäten
keinen positiven unteren Eigenwertabstand und keinen isolierenden Winkelbereich.

Darüber hinaus wurden **exakte Alternativen in einer ausdrücklich definierten
gemeinsamen endlichen Zertifikatsrelaxation** konstruiert. Sie behalten den
Annihilatorzusammenhang YN=0, Gram- und Energiebeziehungen, vollständige kleine
Resolventenvergleiche und zahlreiche weitere veröffentlichte Schranken bei.
In beiden Paritäten erlauben sie unterschiedliche maximierende Richtungen.
Im ungeraden Fall erlauben sie sogar R₀=βM₀ mit einer exakt doppelten Eigenzahl.

Diese Alternativen sind keine nachgewiesenen Realisierungen des ursprünglichen
Operators. Sie widerlegen weder dessen mögliche Einfachheit noch Renewal.
Sie beweisen, dass die unten aufgeführten endlichen Schranken allein die
gewünschte Isolation nicht erzwingen. Die vollständigen Operator- und
Projektorbeziehungen können zusätzliche Information liefern.

## Korollar zu den bisherigen Zeugen

Für jeden zertifizierten Zeugen gilt β≥β_v und 1−κ=β⁻¹. Der neue Prüfer liest
die **exakten rationalen** unteren Zeugenwerte des Mechanismuspakets und
vergleicht ihre Kehrwerte mit den folgenden rationalen Dezimalschranken:

| Übergang | Parität | neues Korollar |
|---|---|---:|
| A₈→A₉ | gerade | 1−κ < 1.996·10⁻⁷ |
| A₈→A₉ | ungerade | 1−κ < 2.477·10⁻⁵ |
| A₉→A₁₁ | gerade | 1−κ < 1.371·10⁻¹² |
| A₉→A₁₁ | ungerade | 1−κ < 8.005·10⁻¹² |

Die Ungleichungen sind strikt, weil der jeweils geprüfte Kehrwert bereits
strikt unter der angegebenen Zahl liegt. Die bestehenden Untergrenzen bleiben
gültig. Die früheren Pakete, Tabellen und ZIP-Dateien wurden nicht verändert.

Eine kleine Präzisierung des begleitenden Audits: Für A₉→A₁₁ ist der alte/neue
physische Trialquellenüberlapp gerade etwa 0.999915786, ungerade etwa
0.999882932. Die Aussage „größer als 0.9999“ gilt daher nur im geraden Fall.
Die gerichteten Werte des Mechanismusberichts waren bereits korrekt.

## Das symmetrisch definite Problem

In den bestehenden Rohkoordinaten des echten kanonischen E setzen wir

\[
B_0=L_0+17G,\qquad
R_0=L_0+34G+289Z_0,
\]

\[
M_0=B_0L_0^{-1}B_0
=L_0+34G+289GL_0^{-1}G>0.
\]

Mit der unteren Cholesky-Matrix C, M₀=CC*, wird

\[
K=C^{-1}R_0C^{-*},\qquad Ky=\beta y,\qquad x=C^{-*}y.
\tag{1}
\]

K ist symmetrisch positiv. Die größte Eigenzahl ist (1−κ)⁻¹.
Der Vektor V₀x maximiert die inverse Antwort. Die zugehörige Richtung des
kleinsten relativen Schurrests ist weiterhin V₀L₀⁻¹B₀x.

### Cholesky ohne vermeidbare Intervallauslöschung

Die Identität

\[
\det M_0=\frac{(\det B_0)^2}{\det L_0}
\]

liefert die gerichtete zweite Cholesky-Diagonale über

\[
C_{11}=\sqrt{(M_0)_{11}},\quad
C_{21}=(M_0)_{21}/C_{11},\quad
C_{22}=\sqrt{\det M_0/(M_0)_{11}}.
\tag{2}
\]

Dadurch muss die zweite Diagonale nicht durch die möglicherweise stark
überbreite Differenz M₂₂−M₂₁²/M₁₁ eingeschlossen werden.
Der Prüfer bestätigt beide positiven Cholesky-Diagonalen für beide
gespeicherten Präzisionsläufe.

### Eigenwertabstand und Winkelzuordnung

Für eine symmetrische 2×2-Matrix gilt exakt

\[
\Delta=\lambda_+-\lambda_-
=\sqrt{(K_{11}-K_{22})^2+4K_{12}^2}.
\tag{3}
\]

Bei Δ>0 bestimmt

\[
(\cos 2\theta,\sin 2\theta)
=\frac{(K_{11}-K_{22},\,2K_{12})}{\Delta}
\tag{4}
\]

die größte Eigenrichtung modulo Vorzeichen. Äquivalent verwendet man
½ atan2(2K₁₂,K₁₁−K₂₂) modulo π. Die Tangensgleichung allein verliert die
Quadrantenzuordnung und unterscheidet die größte nicht von der kleinsten
Eigenrichtung.

Ein Winkel in y-Koordinaten ist zudem nicht automatisch ein L²-Winkel der
physischen Quellen. Dafür müssen x=C⁻*y und die Gram-Matrix G berücksichtigt
werden.

## Ergebnis der direkten Intervalleinschließung

Die oberen und unteren Loewner-Matrizen werden zunächst in gemeinsame
symmetrische Eintragshüllen für L₀ und Z₀ überführt. Dann werden (1)–(3)
vollständig mit rationalen Intervallen ausgewertet. Die beiden Präzisionsläufe
haben dieselben nach außen gerundeten Anzeigen:

| A₉→A₁₁ | Intervall für K₁₁−K₂₂ | Intervall für K₁₂ | Intervall für Δ |
|---|---:|---:|---:|
| gerade | [−3.71903·10¹⁶, 1.48360·10¹⁶] | [−8.51590·10¹⁴, 6.50575·10¹⁴] | [0, 3.72293·10¹⁶] |
| ungerade | [−7.92490·10¹⁶, 3.85957·10¹⁶] | [−1.51959·10¹⁵, 1.32374·10¹⁵] | [0, 7.93073·10¹⁶] |

Der Ursprung liegt in beiden Einschließungen des Orientierungspaars aus (4).
Damit ist kein gerichteter isolierender Winkelbereich zertifiziert.
Negative Endpunkte einzelner K-Einträge oder Diagonalen bedeuten hier keine
negative tatsächliche Eigenzahl; sie entstehen durch die breite Intervallhülle.

Die fehlende positive Gap-Untergrenze allein wäre nur ein Scheitern dieser
direkten Auswertung. Deshalb folgt eine gesonderte Prüfung gemeinsamer
algebraischer Alternativen.

## Welche gemeinsamen Bedingungen die Alternativen erfüllen

Alle folgenden Eigenschaften werden für jede Alternative exakt rational
geprüft, gegen **beide** gespeicherten Präzisionsbelege. Es werden nicht
unabhängig Einträge von K ausgewählt.

1. **Kanonische Koeffizienten.** Y liegt in der veröffentlichten
   Annihilatorhülle; N liegt in der veröffentlichten N-Hülle. Es gelten exakt
   YN=0 und N=[−Y_l⁻¹Y_r;I₂]. Auch die gerichteten Residualschranken für YW₀
   mit der ursprünglichen zentralen Kernmatrix W₀ gelten.
2. **Gram- und Energiebeziehungen.** Mit einem symmetrischen rationalen
   S_B innerhalb der gebundenen physischen Ritzmatrix gilt
   G=N*N und L₀=E_N=N*S_BN. Dies ist der durch die bisherigen einseitigen
   Projektionsschranken zugelassene Fall mit verschwindendem Verlust auf
   diesen zwei Spalten. Gram- und E_N-Einträge liegen in den gespeicherten
   Intervallen. Die Konsequenz „kein Gram-Verlust, dann kein Energieverlust“
   wird ausdrücklich erhalten.
3. **Positive Energieschranken.** L₀ liegt zwischen den gespeicherten
   L_- und L_+. Die physischen positiven Böden, oberen kritischen
   Energieschranken und Gram-Korrekturen gelten.
4. **Gemeinsame inverse Trialantwort.** Es existiert eine einzige positive
   8×8-Matrix T_* mit Z₀=N*T_*N, die zwischen den zugelassenen unteren und
   oberen Trialresolventenmatrizen beider Läufe liegt. Zusätzlich gilt
   T_*≽S_B⁻¹. Der Existenznachweis steht im nächsten Abschnitt.
5. **Faktoren und Momentvergleiche.** Für die ausgewählten rationalen
   unteren und oberen 8×8-Vergleichsmatrizen wird eine gerichtete
   Cholesky-Einschließung nachgerechnet. Ihre Faktoren liegen in den
   ursprünglichen Faktorintervallen. Die Rohmatrizen
   N*T_-N−ν_B⁻²E_N und N*T_+N liegen in den gespeicherten Familien;
   Z₀ liegt strikt zwischen ihnen. Es gilt auch Z₀≽GL₀⁻¹G.
6. **Physische Einträge und duale Proben.** Nach der L²-Normierung mit G
   liegen L und Z in den veröffentlichten physischen Eintragshüllen und
   Z-Diagonalen in den verfeinerten rationalen Intervallen. Die gespeicherten
   dualen Proben erfüllen ihre Überlapp-, inverse Moment- und variationalen
   Energiebedingungen.
7. **Bisherige numerische Schlüsse.** Die größte Eigenzahl der Alternative
   ist mit den vier bisherigen κ-Grenzen für den jeweiligen Fall und dem
   neuen Zeugen-Korollar vereinbar.

Dies definiert die hier untersuchte **endliche Zertifikatsrelaxation**.
Nicht vorausgesetzt oder konstruiert werden die ursprünglichen unendlichen
Operatoren, ihre gemeinsamen Spektralprojektoren, die tatsächlichen
Integralmodelle und sämtliche daraus folgenden korrelierten Beziehungen.
Insbesondere wird nicht behauptet, ein in dieser Relaxation zulässiges Y
werde wirklich von b_B(JP_AU_A,P_BU_B)/17 erzeugt.

Die Alternativen schließen also nur Folgerungen aus den ausdrücklich
aufgeführten Bedingungen aus. Sie schließen eine stärkere Auswertung weiterer
Originalinformationen nicht aus.

## Eine gemeinsame Trialresolvente lässt sich tatsächlich ergänzen

Die Existenzbehauptung zu T_* verwendet folgendes elementare Matrixlemma.
Seien A<U positiv, N von vollem Spaltenrang und

\[
N^*AN<Z_0<N^*UN.
\]

Setze D=U−A, H=N*DN, T_m=(A+U)/2 und E=Z₀−N*T_mN. Dann ist

\[
T_*=T_m+DNH^{-1}EH^{-1}N^*D
\tag{5}
\]

eine rationale symmetrische Matrix mit N*T_*N=Z₀ und A<T_*<U.

Beweis: Nach Kongruenz mit D⁻¹ᐟ² hat die Korrektur den nichtverschwindenden
Spektralteil H⁻¹ᐟ²EH⁻¹ᐟ². Aus −H/2<E<H/2 liegen dessen Eigenwerte strikt
zwischen −1/2 und 1/2. Auf dem orthogonalen Komplement ist die Korrektur null.
Damit liegt D⁻¹ᐟ²(T_*−A)D⁻¹ᐟ² strikt zwischen 0 und I.

Konkret wählt der Prüfer innerhalb der Vergleichsmatrizen des 1280-Bit-Belegs

\[
A=0.51T_-+0.49T_+,\qquad U=0.49T_-+0.51T_+.
\]

Er prüft A oberhalb der zulässigen T_- beider Läufe und oberhalb S_B⁻¹,
sowie U unterhalb der zulässigen T_+ beider Läufe. Weiter prüft er die beiden
komprimierten strikten Ungleichungen für Z₀. Lemma (5) liefert damit eine
gemeinsame T_*; die Z-Kreuzterme sind nicht frei von einer Trialantwort gewählt.

## Exakte Alternativen für die Extremalrichtung

Für jeden Fall bleibt Y_l fest auf dem rationalen zentralen linken Block
des 1280-Bit-Belegs. Die Ausgangsalternative verwendet die Mittelpunkte von
Y_r. G und L₀ werden wie oben aus dem exakt gelösten N gebildet.
Z₀ startet bei N*(T_-+T_+)N/2.

Für die zweite Alternative wird nur Y₆₈ innerhalb seiner vorhandenen
Unsicherheit geändert. Danach wird der Z-Kreuzterm so festgesetzt, dass

\[
(R_0)_{12}
=\frac{(M_0)_{12}}{(M_0)_{11}}(R_0)_{11}.
\]

Damit ist e₁=(1,0) exakt eine verallgemeinerte Eigenrichtung. Ihr Eigenwert
ist nachweislich strikt größer als der zweite. Alle oben aufgeführten Bedingungen
bleiben erfüllt.

| Parität | Ausgangsalternative mit x₂=1 | zweite Alternative | obere Eigenzahl der zweiten Alternative |
|---|---:|---|---:|
| gerade | x₁∈[0.00757458, 0.00757459] | eindeutige größte Richtung (1,0) | [4.90123·10¹², 4.90124·10¹²] |
| ungerade | x₁∈[0.0177852, 0.0177853] | eindeutige größte Richtung (1,0) | [4.96825·10¹², 4.96826·10¹²] |

Die Richtungen sind in den festgelegten Rohkoeffizienten angegeben. Diese
Tabelle behauptet keine gemeinsamen physischen Winkel zwischen verschiedenen
zugelassenen Matrixfamilien.

Die verwendete Unsicherheit ist bereits im Annihilator sichtbar. Die
vorhandene Y₆₈-Hülle hat ungefähr Mittelpunkt 0.03305848 und Radius 0.02515819
gerade, beziehungsweise Mittelpunkt 0.05545467 und Radius 0.04952664 ungerade.
Die rationalen Parameter in `candidate_proposals.json` bestimmen sämtliche
Änderungen exakt; die Dezimalanzeigen dieses Absatzes sind nur Diagnosewerte.

### Eine exakt doppelte Eigenzahl im ungeraden Fall

Eine dritte Alternative verändert die letzten beiden Zeilen von Y_r innerhalb
der verfügbaren Schranken. Nachdem N, G und L₀ feststehen, wird eine positive
rationale Zahl β gewählt und

\[
Z_0=\frac{\beta M_0-L_0-34G}{289}
\tag{6}
\]

gesetzt. Der Prüfer bestätigt alle oben aufgeführten Bedingungen und die **exakte
rationale Identität** R₀=βM₀. Die gerichtete Anzeige für β lautet
**[4.95691·10¹¹, 4.95692·10¹¹]**.

Folglich ist K=βI, Δ=0 und jede Richtung maximierend. Dies ist kein
numerisch fast doppelter Eigenwert: Die Gleichheit wird rational geprüft.
Gleitkommarechnungen dienten nur dazu, die anschließend festgehaltenen
rationalen Vorschlagsparameter zu finden.

Somit kann für den ungeraden Fall aus der hier definierten Relaxation nicht
einmal Δ>0 folgen. Für den geraden Fall wird keine doppelte Eigenzahl
behauptet; dort genügen die zwei unterschiedlichen einfachen Extremalrichtungen,
um die fehlende eindeutige Richtungsbestimmung innerhalb dieser Schranken zu
zeigen.

## Fachliche Konsequenz

Das symmetrische Problem ist die geeignete Endauswertung. Die fehlende
Information liegt vor dieser Endauswertung: Die zugelassenen Änderungen der
projizierten Überlappe können die energiegewichtete Richtung stark verändern.

Der nächste gezielte Forschungsblock sollte deshalb die **gemeinsamen
Projektor- und Überlappbedingungen für Y_r, N und die Momentmatrizen** verschärfen.
Konkret muss er mindestens die oben konstruierten Alternativen ausschließen.
Mögliche zusätzliche Information sind gerichtete projizierte Überlappe oder
aus den vollständigen Operatoren abgeleitete gekoppelte Bedingungen für Gram-,
Energie- und inverse Energieverluste. Welche davon ausreicht, ist noch offen.

Ein erneuter gleichartiger Lauf mit mehr Bits beseitigt die hier nachgewiesene
Freiheit der vorhandenen Schranken nicht: Die Alternativen bestehen die
Bedingungen beider vorhandenen Präzisionsläufe. Es wird damit nicht behauptet,
dass jede künftig präzisere analytische oder numerische Einschließung wirkungslos
wäre.

Bandweise Momente eines als tatsächlich schlechtester Modus bezeichneten
Vektors werden erst nach dessen Zertifizierung ausgewertet. Die bestehenden
Zeugen- und allgemeinen Maximiereraussagen des Mechanismuspakets bleiben gültig.

## Prüfung und Reichweite

- Fünf unveränderte Eingangsdokumente sind mit SHA-256 gebunden: beide
  Resolventenbelege, der ursprüngliche rationale Resolventenprüfbeleg, die
  physische Trialraum-Datei und der Mechanismusprüfbeleg.
- Die Quellenketten und die feste Commitbasis werden im neuen Prüfer
  abgeglichen. Die 25 Git-Blobs wurden in diesem Lauf nicht erneut gelesen;
  ihr byteweiser Abgleich ist eine gebundene Prüfung des vorigen Blocks.
- Alle endgültigen Aussagen werden mit rationalen Zahlen geprüft. Die
  Cholesky-Faktorbindungen der kleinen 8×8-Matrizen verwenden zusätzlich
  gerichtete rationale Wurzeleinschließungen mit 500 Dezimalstellen.
- Die direkten symmetrischen Einschließungen und alle fünf Alternativen
  werden gegen beide ursprünglichen Präzisionsbelege geprüft. Die
  Matrixpositivität der gewählten Punkte wird durch exakte LDL-Pivots geprüft.
- Der Endlauf ist reproduzierbar; Tabellen, Eingabebindungen und Archiv werden
  separat abgeglichen. Neue große Resolventenlösungen, Terminalintegrale und
  eine vierte Kammer wurden nicht gerechnet.

**Status der Forschungsfrage:** Der Mechanismusblock bleibt bestanden.
Der Versuch der Extremalrichtungsisolation ist ausgewertet, aber das Ziel
einer tatsächlichen Isolation ist nicht erreicht. Die neue Leistung sind das
Korollar und ein genauer Nachweis, welche geprüften endlichen Schranken dafür
noch nicht ausreichen. Externer mathematischer Review bleibt offen.

Alle vier jüngsten Pakete bleiben lokal. Repository, Registry und PR #187
wurden nicht verändert. Es wird kein vorwärts gerichteter Renewal-Satz,
keine kofinale Positivität, kein globales Objekt X und keine RH-Aussage bewiesen.
