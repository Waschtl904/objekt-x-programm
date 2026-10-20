# Gerichteter Teilpass des festen geraden Matrixfehler-Piloten

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Auswahlstand: #245, `a60f7602335f654ca7b42e8362e47af243e20462`.
Die gebundenen Operator-, Formdomänen-, Quellen- und
Integrationsvoraussetzungen bleiben Voraussetzungen dieses Ergebnisses.

## 1. Ergebnis und genaue Reichweite

**PILOT_PARTIAL_PASS**, ausschließlich für den eingefrorenen geraden
physischen Zeugen. Alle zusätzlichen Fehler der hier betrachteten
Teilenergie sind eingeschlossen. Die maßgeblichen rationalen Endpunkte
stehen in `RESULT.json`; folgende Anzeigen sind nach außen gerundet:

| Gerichtete Größe | Intervall, jeweils mal 10^-6 |
| --- | ---: |
| Tatsächliche neue Teilenergie | [53.68719767242, 53.90213205365] |
| Unverändertes tatsächliches K_P-Budget | [54.11716936070, 54.11716937864] |

Die Teilenergieobergrenze E_hi ist strikt kleiner als K_lo.
Die verbleibende Reserve r=K_lo-E_hi erfüllt

    r > 2.15037307060e-7.

Das ist eine gerichtete Reserve **vor dem vollständigen Dualterm**.
Die vollständige zulässige Majorante enthält zusätzlich

    (a/beta) <nu_new, R_L nu_new>,
    a/beta = 91095000000000000000 / 8067286322727467113.

Die exakte hinreichende Schwelle beta*r/a steht in `RESULT.json` und ist
größer als 1.90434988323e-8. Somit wäre zum vollständigen Vergleich
**an diesem einen Zeugen** beispielsweise ausreichend:

    <nu_new, R_L nu_new> < 1.90434988323e-8.

Diese Ungleichung wurde nicht berechnet oder bewiesen. Die gespeicherten
84 J-Koordinaten ersetzen den vollständigen Formdualterm nicht.
Es liegt weder eine vollständige Energieobergrenze noch ein positiver
Anschluss für den Grad-11-Raum oder beide Paritäten vor. Punkt 4, N12,
Objekt X und externe Prüfung bleiben offen.

## 2. Eingefrorene Auswahl und übernommenes Restzertifikat

Die [Auswahlherleitung](../w9-matrix-error-selection-2026-10-20/PROOF.md)
beweist unter den gebundenen Voraussetzungen

    0 < K_star < K_new <= K_actual.

K_new wird unverändert aus dem dortigen `EXPECTED.json` übernommen.
Kanonischer SHA-256 der rationalen Zeilen:
`89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8`.
Der Prüfer rekonstruiert genau dieselbe Matrix-Young-Einschließung bei
festem epsilon; er wählt keine neue Matrix. Ein unabhängiger Fraction-Audit
prüft erneut zwölf positive Pivots für K_new-K_star und zwölf für den
gerichteten Rundungsabstand. Die alte K_star-Zulässigkeit wird ebenfalls
aus ihren gebundenen Eingaben reproduziert.

Unverändert bleiben U8, der physische Zeuge aus #238, die äußere
Antwortmatrix, ihre Quellenfunktionen, X_ans und das separate K_P-Zertifikat.
Es gibt keine neue Integration, Richtungs- oder Gewichtsoptimierung.
Die festen Gewichte sind

    b=51/50, c=1977/500000, a=500000/399173.

Die Gleichung (a(1-c)-1)(b(1-c)-1)=c und beide positiven Faktoren
werden exakt rational geprüft. beta und c sind mit der unabhängigen
vollständigen Restabnahme des erneuerten A9-Vergleichs gebunden.

Bei unverändertem internem Residuum R gilt monoton

    E_new = E0 + diag(0_191, K_new-K_old) >= E_star,
    R* R_L R <= c beta E_star <= c beta E_new.

Damit wird das vorhandene vollständige Restzertifikat übernommen.
K_new-K_star darf nicht direkt zu E0 addiert werden; der Prüfer verwendet
ausdrücklich K_new-K_old. Der Ausschluss der anderen K_star-Unterform
aus #239 bleibt gültig.

## 3. Neue rationale P-Obermatrix und gemeinsames nu

Ein 1024-bit-Intervallsolve mit 84 rechten Seiten berechnet

    E_new Y = X_ans*,  P_exact = X_ans Y.

Die symmetrisierte Lösung wird eintragsweise auf einem 60-stelligen
Dezimalraster eingeschlossen. Zum rationalen Mittelpunkt kommt diagonal
die jeweilige Summe der Zeilenradien plus 10^-40. Die resultierende
Matrix P_upper steht vollständig in `SCHUR.json`.

Zusätzlich prüft der gebundene Integer-Intervallauditor auf einem
120-stelligen Dezimalraster den gesamten rationalen Block

    [ E_new    X_ans* ]
    [ X_ans    P_upper ] > 0.

Alle **287 Pivots sind positiv**. Dies beweist
P_upper >= X_ans E_new^-1 X_ans*. Die Prüfung erfolgt am ganzen Block,
nicht nur an seinen Teilblöcken; der kleinste Pivotboden und der
Digest aller Pivotintervalle sind veröffentlicht.

Mit Ki=K_new^-1 wird

    nu_new = f_T - g* U8 h - a_fin* Ki v

als gemeinsame Differenz neu gebildet. Zwei algebraisch äquivalente
Rechenwege überlappen in sämtlichen 84 mal 12 Einträgen.
Die Teilenergie enthält hohe U8-, endliche U8-, Ki-v- und
b-P_upper-Energie. Der vollständige R_L-Anteil bleibt ausgelassen.

## 4. Vollständige Fehler der Teilenergie

Die bereits veröffentlichten, in K, P und b parametrisierten Module
`pilot_weights.py` und `pilot_energy.py` des alten K-Piloten werden
bytegebunden wiederverwendet. Ihre Formeln sind in der
[alten Pilot-Herleitung, Abschnitte 4 und 5](../w9-k-pilot-even-2026-10-18/PROOF.md)
ausgeführt. Die hier eingesetzten K-, P- und Gewichtsargumente sind neu;
die gemeinsamen alten Paarungsdaten bleiben unverändert.

Insbesondere werden d_U, d_D und d_a=d_U+d_D aus den **vollen alten
F-J-/96-Quellenfehlern** neu gebildet und gegen die ursprünglichen
Einschließungen abgeglichen. Der kleinere F-F-Preis der neuen
K-Zulässigkeit wird dort nicht eingesetzt. Der a_fin-Fehler wird einmal
in der nu-Featuregrenze bezahlt, einschließlich des v-Fehler-Kreuzterms.
Ki, P_upper und b gehen auch in sämtliche gewichteten Fehler ein.

Für die ganze Hilbert-Residualabweichung wird die vollständige
Teilnormmajorante erneut mit denselben neuen Argumenten berechnet.
Gamma-, Antwortmodell- und eingefrorene T-Koeffizientenfehler werden
gemeinsam über diese Teilnorm bezahlt. Es wird keine globale Normschranke
der vollständigen Majorante einschließlich R_L behauptet.

Mit den eingeschlossenen Modellenergien E0, dem gemeinsamen
Featurefehler e_f und dem gewichteten ganzen Residualfehler e_r gilt

    E_lo = max(0, sqrt(max(0,E0_lo))-e_f,up-e_r,up)^2,
    E_hi = (sqrt(E0_hi)+e_f,up+e_r,up)^2.

Alle Endpunkte werden nach außen rational gerundet. Diese Endpunkte,
nicht engere interne Zwischenwerte, bestimmen den Ausgang.
Die Modellteilenergie liegt in etwa [53.73328,53.85598] mal 10^-6;
die größere Breite gegenüber der Auswahl ist in der Endentscheidung
enthalten. Der größte zusätzliche Featurefehler liegt beim P-Anteil
(etwa 3.144e-6 in Norm), hauptsächlich beim a_fin-Preis
(etwa 3.113e-6 vor dem Faktor sqrt(b)).
Diese Normfehler sind keine Energiefehler in gleicher Größe.
Der gewichtete ganze Residualmodellfehler beträgt etwa 1.158e-10 in Norm.

## 5. Abnahme und Stopplinie

Der Rechenplan wurde vor dem Lauf festgelegt. Ein Elternprozess beendet
jeden vollständigen Aufruf nach 1800 Sekunden; es gibt keine automatische
Nachschärfung oder Kandidatenwiederholung. Der erste vollständige Lauf
dauerte hier 96.388 Sekunden. Die Pflicht-Reproduktion verwendet dasselbe
eingefrorene Paket und dieselben Hashbindungen, ohne neue Integration.
Lauf- und Archivbindung stehen nach Abschluss in `ACCEPTANCE.json`.

`audit.py` prüft unabhängig mit der Standardbibliothek die exakten
Gewichte, die veröffentlichten Intervallrelationen, das Restbudget,
die Dualschwelle und die Aussagegrenzen. Der eigentliche 287er-Audit
ist Bestandteil jedes vollständigen Replays. Hashgeprüfte Eingaben
werden nur aus ihren geprüften Bytes ausgewertet.

Abgeschlossen ist der festgelegte gerade Teiltest. Als nächste, getrennt
zu begründende Aufgabe kommt die vollständige Dualkontrolle an demselben
Zeugen mit derselben neuen Unterform in Betracht. Die zulässige Schwelle
ist nun gerichtet beziffert; eine praktikable Abschätzung dafür ist noch
offen. Keine Dualrechnung wurde gestartet. Die äußere Antwortmatrix-Suche
ruht. Auch ein künftiger vollständiger Pass dieses Zeugen ersetzt nicht
den gesamten Raumvergleich.
