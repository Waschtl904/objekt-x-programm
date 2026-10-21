# Neue K-Unterform aus dem vollen Fehlergram: begrenzte Auswahl

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Integrationsbasis: `2e8e86770c0fde6ef5ea69b0178775eab34d5de4`.
Die gebundenen Operator-, Formdomänen-, Quellen- und Integrationsvoraussetzungen
werden übernommen. Ihr externer Nachweis wird hier nicht erneuert.

## 1. Entscheidung und neue Information

Ausgewählt wird genau ein gerader Pilot: den vollständigen matrixwertigen
Fehler der zwölf alten F-Quellen zur Konstruktion einer neuen Untergrenze
K_new verwenden und die ganze Vergleichsgeometrie konsistent erneuern.
Die äußere Antwortmatrix, der physische Zeuge, U8 und das äußere K_P-Budget
bleiben fest. K_new ist eine andere Unterform als die in #239 ausgeschlossene
K_star-Unterform.

Die Zulässigkeitsprüfung liefert **K_new > K_star** und **K_new <= K_actual**.
Der vollständige alte Restnachweis ist monoton übertragbar. Eine
Modellauswertung mit einem zulässigen geänderten Gewichtspaar liegt knapp
unter dem Budget. Das begründet einen begrenzten gerichteten Test, keinen
positiven Energieabschluss.

| Weg | Neue Auswahlentscheidung |
| --- | --- |
| Allgemeine äußere Antwortmatrix | Zurückgestellt: gewichtete D-Antwortgrame und D/R0-Kreuzgrame fehlen. Alte Mittelpunktinverse und audit_S bleiben erledigt. Die bisherige ±1-%-Transferabschätzung ist unbrauchbar, keine Verbesserungsevidenz. |
| Neue Unterform aus matrixwertigem F-Fehler | Ausgewählt: vollständige Daten vorhanden, gerichtete Zulässigkeit, monotone Restübertragung und bezifferte Modellperspektive. |

Es wird kein zweiter Suchweg parallel gestartet. Die alte Stopplinie bleibt:
Eine engere Obermajorante derselben K_star-Unterform kann #239 nicht retten.
Der hier geänderte F-F-Unterblock ändert ausdrücklich diese Voraussetzung.

## 2. Matrix-Young statt eines gemeinsamen skalaren Fehlerpreises

Im F-Block seien Psi=Psi0+DeltaPsi die vollständigen U8-Features und

    U0 = Psi0*Psi0,       DeltaPsi*DeltaPsi <= E_F.

U0 und E_F stammen unverändert aus Common96. E_F enthält den vollständigen
hohen Anteil; seine Identifikation steht in
[COMMON96, Abschnitt 5](../a9-inverse-renewal-2026-10-13/original/sources/COMMON96_HERLEITUNG.txt).
Die alten zwölf F-Quellen sind nicht die zwölf neuen D=A9 Phi12-Antworten.

Für jedes rationale epsilon>0 gilt auf allen zwölf Koeffizienten gemeinsam

    U_actual <= (1+epsilon) U0 + (1+1/epsilon) E_F.             (1)

Beweis: epsilon Psi0*Psi0 + epsilon^-1 DeltaPsi*DeltaPsi
- Psi0*DeltaPsi - DeltaPsi*Psi0 ist das Gramquadrat
(sqrt(epsilon)Psi0-epsilon^-1/2 DeltaPsi)*
(sqrt(epsilon)Psi0-epsilon^-1/2 DeltaPsi), also nicht negativ.
Anschließend DeltaPsi*DeltaPsi durch E_F majorisieren.
Es werden weder Kommutativität noch unabhängige Fehler angenommen.

Die direkte Matrix D_lower,FF ist bereits eine Untergrenze der vollständigen
direkten Form einschließlich ihrer Fehler. Deshalb ist

    K_ceiling = D_lower,FF - (1+epsilon)U0
                              - (1+1/epsilon)E_F
              <= K_actual.                                  (2)

`K_ceiling` ist die zulässige Obergrenze für unseren ausgewählten K-Kandidaten,
selbst aber eine Untergrenze von K_actual, keine Obergrenze von K_actual.

Auswahlregel für epsilon: Die vorhandenen Spuren
e2=tr(G_F^-1 E_F) und tau=tr(G_F^-1 U0) liefern den skalaren
Young-Minimierer sqrt(e2/tau). Seine einmalige Rundung auf 40 Nachkommastellen
wurde vor der Energieauswertung festgehalten:

    epsilon = 14401070947262324376501 / 10^40
            ~= 1.4401070947262324e-18.

Dies ist eine Auswahlheuristik für die Matrix, keine gerichtete globale
Optimierung. Im Prüflauf ist epsilon eine exakt rationale feste Eingabe.
Der Spurpreis epsilon*tau+(1+1/epsilon)*e2 bleibt unter dem bisherigen
F-Fehlercap 3.04583464e-7. Der wesentliche Unterschied ist, dass (1) die
Matrizen U0 und E_F selbst beibehält, statt alles durch dieses Cap mal G_F
zu ersetzen.

## 3. Rationaler Kandidat und gerichtete Zulässigkeit

Die Intervallmatrix (2) wird symmetrisiert. Ihre Einträge werden nach außen
auf das Raster 10^-80 gerundet. Seien M die rationalen Mittelpunkte und
r_i die Summe der Eintragsradien in Zeile i. Definiere exakt

    K_new = M - diag(r_i) - 10^-60 I.                        (3)

Für jede symmetrische Matrix im Intervallkasten gilt
K_ceiling >= M-diag(r_i), durch die Zeilensummen-/Gershgorin-Abschätzung
des Eintragsfehlers. Daher folgt K_new < K_ceiling <= K_actual.

Ein unabhängiger Fraction-LDL-Audit bestätigt zwölf positive Pivots von
K_new-K_star und zwölf von M-diag(r_i)-K_new. Die konkrete rationale Matrix
steht vollständig in EXPECTED.json, mit kanonischem SHA-256
`89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8`.
K_star>0 bleibt eine gebundene geerbte Voraussetzung. Die Pivots werden
nicht als physischer Koerzivitätsboden ausgegeben.

Der relative Spurindikator tr(K_star^-1(K_new-K_star)) ist ungefähr
2.73739e-6. Er ist keine prozentuale Energieverbesserung.
Die gerichtete Matrixrelation ist der Zulässigkeitsnachweis.

## 4. Vollständige Restkontrolle bleibt verwendbar

Mit DeltaK=K_new-K_star>0 und der alten internen Antwort Z=J X_ans bleiben
S, A_force, R=A_force*-SZ und M unverändert. Die Bezeichnungen betreffen die
interne A9-Geometrie, nicht die äußere Antwort Phi12 X0 Fhat.

    E_new = E_star + diag(0_191, DeltaK) >= E_star > 0,
    R* R_L R <= c beta E_star <= c beta E_new,
    c = 1977/500000.

Damit gilt die gleiche vollständige Restschranke, mit demselben R_L auf
dem ganzen exakten T. Ihr Abnahmeanker und beta werden im Prüfer abgeglichen.
Keine neue globale Residualintegration ist für diese Übertragung nötig.

In der vollständigen quadratergänzten Form gilt

    Q_new = Q_star + DeltaK[z],
    Q_star <= Q_new <= A9.

Hier bezeichnet z die alte Zwölferkoordinate. Der neue physische
Schalenzeuge ist davon zu unterscheiden.

Für eine nachfolgende Energieprüfung müssen gemeinsam eingesetzt werden:

    Ki_new = K_new^-1,
    P_new_exact = X_ans E_new^-1 X_ans*,
    nu_new = f_T-g*U8 h-a_fin*Ki_new v.

Der spätere Certifier braucht eine gerichtete rationale Obermatrix für
P_new_exact und die erneuerte ganze Teilnormmajorante. Die kleineren
F-F-Preise aus (1) dürfen nicht auf F-J/a_fin oder die vollständigen
96-Quellenfehler übertragen werden.

## 5. Quantitative Modellperspektive und ihre enge Grenze

Die Auswahlauswertung benutzt die gespeicherten gemeinsamen Paarungen.
Alle gespeicherten Intervallradien bleiben enthalten; die zusätzlichen
physikalischen Modell-, Feature-, F-J- und ganzen Residualfehler werden hier
jedoch noch nicht bezahlt. Die folgende Tabelle ist ausdrücklich eine
Modellrechnung, kein tatsächliches Energieintervall.

Die alten Gewichte ergeben mit K_new noch ungefähr 54.7499e-6 und damit
weiterhin mehr als das Budget. Nach dieser Diagnose wurde genau ein neues
rationales Gewicht b=51/50 festgelegt. Es gibt keine automatische Gewichts-
oder Richtungssuche. Mit

    a = (b-1)/(b(1-c)-1) = 500000/399173

gelten exakt a(1-c)>1, b(1-c)>1 und
(a(1-c)-1)(b(1-c)-1)=c. Die gebundene vollständige Young-Herleitung liefert

    H_new^-1 <= (a/beta) R_L + b J P_new_upper J*.

| Auswahldiagnose | Größenordnung |
| --- | ---: |
| Neue Teilenergie im Modell, alte Gewichte | 54.7499e-6 |
| Neue Teilenergie im Modell, ausgewählte Gewichte | 53.7946e-6 |
| Unverändertes tatsächliches Budget | 54.11716937e-6 |
| Modellspielraum vor zusätzlichen Fehlern und Dualterm | etwa 0.3225e-6 |
| Neuer Dualkoeffizient a/beta | etwa 11.292 |

Die zusätzlichen Fehler und die gewichtete vollständige Dualenergie müssen
zusammen in diesen kleinen Spielraum passen. Sogar ohne jeden zusätzlichen
Fehler wäre nur ein Dualterm der Größenordnung 2.856e-8 bezahlbar. Dies ist
eine Rechenbedingung im Modell, **keine zertifizierte Dualreserve**.

Der zusätzliche 84er-Modelluntertest ergibt ungefähr 53.8339e-6. Auch dieser
Wert ist keine gerichtete Untergrenze für die tatsächliche neue Inversenergie,
weil die zusätzlichen Fehler fehlen. Er schließt weder die neue Klasse aus
noch beweist er einen Teilpass. Ein Modellvorteil der Unterform wird nicht
mit einem vollständigen Anschluss verwechselt.

## 6. Eingefrorener nächster Pilot und Stopkriterien

Genau K_new aus (3), epsilon, a und b aus diesem Paket, nur gerade,
unveränderte äußere Antwort und derselbe W-normierte physische Zeuge.
Keine neue Richtungsauswahl, Integration oder R_L-Rechnung.

Nächster begrenzter Liefergegenstand:

1. Eine neue P-Obermatrix aus E_new bauen und den vollen 287er-Schurblock
   rational zertifizieren.
2. Ki_new, P_new, nu_new und alle gewichteten Modell-/Feature-/F-J- sowie
   ganzen Residualfehler gemeinsam auswerten. U8, Paarungen und äußeres
   K_P-Zertifikat werden hashgebunden übernommen.
3. Die gerichtete tatsächliche Teilenergie [E_lo,E_hi] mit dem tatsächlichen
   Budget [K_lo,K_hi] vergleichen.

- E_lo>K_hi: konkreten Pilot verwerfen, keine Dualrechnung.
- E_hi<K_lo: nur für diesen Zeugen Teilpass; tatsächliche Reserve
  r=K_lo-E_hi ausweisen. Eine nachfolgende Dualprüfung müsste
  <nu_new,R_L nu_new> < beta*r/a nachweisen.
- Überlappung: unentschieden; dominierenden Fehler benennen und stoppen.
- Ungeklärte Bindung, Ordnung oder Positivität: technischer/Beweisabbruch,
  keine Energieentscheidung.

Ein Pilotlauf, keine automatische Nachschärfungsserie; Rechenlimit 30 Minuten
als Abbruchgrenze, nicht als Laufzeitversprechen. Erst ein erfolgreicher
Teiltest rechtfertigt die gesonderte Abschätzung des vollständigen Dualterms.
Für den konstruktiven Anschluss bleiben beide Paritäten, der ganze
Schalenraum, der unendliche Rest und die auswertbare neue Invershülle nötig.

## 7. Abnahmeumfang

verify.py prüft gebundene Eingaben, (3), die Modellperspektive und die
Gewichtszulässigkeit. audit.py prüft die rationalen Matrixabstände und
Gewichte unabhängig ohne Arb, einschließlich eines nichtkommutierenden
Young-Kontrollfalls. Der frische Paket-Replay rechnet ausschließlich diese
Auswahl nach. Historische Integrationen bleiben gebundene Eingaben.

Abgeschlossen ist die Auswahl eines konkret zulässigen Kandidaten mit
kleiner quantitativer Modellperspektive. Die neue gerichtete Energieprüfung
ist noch nicht ausgeführt. N12, Meilenstein 4, Objekt X und externe Prüfung
bleiben offen. #239 wird weder widerlegt noch rückwirkend eingeschränkt.
