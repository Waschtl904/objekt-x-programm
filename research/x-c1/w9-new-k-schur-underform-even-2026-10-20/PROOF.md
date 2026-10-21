# Feste Young-Familie ausgeschlossen; gekoppelter K_new-Schurtest offen

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `bf9375b26ecb2ad3060c91824501f460c060fc43`.
Es gelten die gebundenen Operator-, Formdomänen-, Quellenmodell- und
Integrationsvoraussetzungen der bisherigen Kette.

## 1. Zwei getrennte Ergebnisse

| Frage | Gerichteter Befund |
| --- | --- |
| Kann eine andere Gewichtung derselben Young-Familie den Vergleich retten? | Nein: Familienenergie >65.23831878691e-6, Budget <54.11716937864e-6 |
| Überschreitet schon die Inverse der neuen Unterform das Budget? | Dieser Untertest entscheidet das nicht: Untergrenze >53.19341255729e-6; `SCHUR_LOWER_TEST_OPEN` |

Die Gewichtsfolgerung gilt bei unverändertem K_new, P_new_upper, physischem
Zeugen, äußerer Antwortregel und Budget. Sie betrifft nicht alle Majoranten
der neuen Unterform. Die tatsächliche A9-Inverse ist nicht ausgeschlossen.

Die Differenz der veröffentlichten Schur-Untergrenze zur Budgetobergrenze
beträgt etwa **-0.923756821331e-6**. Das ist kein negativer Abstand der
tatsächlichen Inversenergie und keine positive Dualreserve. Es liegt keine
obere Einschließung dieser Inversenergie vor. Auch die Aussage, allein die
Young-Abschätzung verursache das Hindernis, wäre daher noch unbegründet.
Punkt 4, N12, Objekt X und externe Prüfung bleiben offen.

## 2. Kurzer Ausschluss der festen Young-Gewichtsfamilie

Aus #246/#247 werden die unveränderten tatsächlichen nichtnegativen
Energieanteile übernommen:

    C = <h,U8 h> + v* K_new^-1 v >= 0,
    B = (J*nu_new)* P_new_upper (J*nu_new) >= 0,
    D = <nu_new,R_L nu_new> >= 0.

Hier sind Quellen, K_new, P_new_upper, beta und der vollständige Dualterm
unabhängig von der Wahl der Young-Gewichte. Die Vergleichsenergie ist

    E(a,b) = C + b B + (a/beta) D,
    E_partial(b0) = C + b0 B,       b0 = 51/50.

Die zugelassene Familie erfüllt mit c=1977/500000

    a,b > t = 1/(1-c),
    (a(1-c)-1)(b(1-c)-1) >= c.

Für die folgende Untergrenze werden nur die beiden ersten strikten
Ungleichungen benötigt. Zusätzlich gilt hier exakt **t <= b0**. Deshalb:

    E(a,b) - t(E_partial(b0)/b0 + D/beta)
      = (1-t/b0) C + (b-t) B + ((a-t)/beta) D >= 0.        (1)

Die Bedingung t<=b0 ist wesentlich für das Vorzeichen des C-Koeffizienten.
Es wird keine unbekannte Größe mit negativem Gewicht nach unten abgeschätzt.
Mit den gerichteten unteren Endpunkten aus #246 und #247 folgt

    E(a,b) >= (E_partial,lo / b0 + D_lo / beta)/(1-c)
            > 65.23831878691e-6
            > K_P,upper.

`WEIGHTS.json` enthält den exakten rationalen Wert, seine Quellenhashes und
den Abstand >11.12114940828e-6 zur Budgetobergrenze. `audit.py` prüft (1),
die Konstanten und die rationalen Endpunkte ohne Arb. Es gab keine
Gewichtssuche, Optimierung oder neue Integration. Andere P-Matrizen,
Unterformen und Antwortregeln gehören nicht zu dieser festen Familie.

## 3. Übertragung des variationalen Schur-Untertests

Die [K_new-Zulässigkeit](../w9-matrix-error-selection-2026-10-20/PROOF.md)
und der [P-/Restanschluss](../w9-matrix-error-pilot-even-2026-10-20/PROOF.md)
bleiben gebundene Voraussetzungen:

    Q_star <= Q_new <= A9,       K_new > K_star > 0.

Die vollständige Positivität und die Formdomänen werden aus diesen Paketen
und der ursprünglichen Inversherleitung übernommen. Das ist eine tatsächlich
geänderte Unterform gegenüber dem alten K_star-Untertest.

Mit dem unveränderten physischen Residualzeugen f gelten nun gemeinsam

    v = F*f - g_F*U8 h,
    nu_new = Lambda_T*f - g*U8 h - a_fin*K_new^-1 v,
    H_new = B_JJ - a_fin*K_new^-1 a_fin - eta q,
    E_base = <h,U8 h> + v*K_new^-1 v,
    <f,Q_new^-1 f> = E_base + <nu_new,H_new^-1 nu_new>.

Sterne in diesen Formeln bezeichnen die jeweiligen Adjungierten; B_JJ
bezeichnet die Restriktion der vollständigen direkten Form minus U8-Energie.
Für jeden zulässigen Jw aus der gebundenen exakten 84er-Basis gilt

    E_base + 2 Re<nu_new,Jw> - H_new[Jw]
        <= <f,Q_new^-1 f>.                              (2)

Die Formdomäne und Momentprojektion von J werden übernommen. Die
Positivität von eta q erlaubt, diesen Gewinn im unteren Test wegzulassen.
Der unendliche Rest wird nicht gleich null gesetzt: Die Einschränkung des
Variationsprinzips auf einen Testvektor liefert die richtige Unterrichtung.
Eine obere Vollenergie folgt daraus nicht.

## 4. Genau ein eingefrorener Testvektor

Der physische Zeuge bleibt identisch zu #246/#247. Neu ist nur der interne
variationale 84er-Testvektor für K_new. Es wird einmal das Mittelpunktsystem

    H0 w = (J*nu_new)_0,
    H0 = (D_mid-U0)_JJ - a0*K_new^-1 a0

gelöst und auf 50 Dezimalstellen rational gerundet. Diese Auswahl ist keine
gerichtete Optimierung. (2) gilt für jeden solchen rationalen Vektor; ein
Optimalitätsfehler wird nicht als Beweis benötigt.

`CANDIDATE.json` wurde vor der gerichteten Zertifizierung im Commit
`06d4c41` eingefroren, SHA-256
`70e8f72ab0cb8ca1ac0d254392384a2040a9d76d04ebf82587c48771e9f34628`.
Es gab keinen zweiten Vektor, keine adaptive Suche und keine Nachschärfungsserie.
Der Replay vergleicht Auswahl und Zertifikat getrennt bytegleich.

## 5. Fehlerkontrolle mit vorhandenen gemeinsamen Daten

Alle Quellen- und Paarungsdaten stammen unverändert aus dem gemeinsamen
Teilenergiepaket. Die 84 nu_new-Koordinaten überlappen die in #246 gebundenen
Koordinaten. K_new^-1, nu_new, Basisenergie, Paarung, Formwerte und ganze
Residualnormpreise werden gemeinsam neu ausgewertet.

Die Basis- und Paarungsfehler folgen den vollständigen Formeln des
[alten variationalen Tests, Abschnitte 5–6](../w9-schur-variational-even-2026-10-19/PROOF.md),
jetzt mit K_new. Darin bleiben die ursprünglichen F-J-Fehler, die direkte
Sandwichbreite, alle hohen Quellenpreise sowie der ganze physische
Residualmodellfehler enthalten. Die kleinere F-F-Abschätzung der
K_new-Zulässigkeit ersetzt keinen F-J-Fehler.

Für den a_fin-Formterm wird unmittelbar die bereits hergeleitete
[richtungsbezogene Fehlerschärfung](../w9-schur-form-error-even-2026-10-19/PROOF.md)
verwendet. Setze z=a0 w, r=K_new^-1 z und d=(a_fin-a0)w. Dann

    (z+d)*K_new^-1(z+d)
      >= z*K_new^-1 z - 2|r*(a_fin-a0)w|.                (3)

Der quadratische Fehler ist nichtnegativ. Aus den vorhandenen vollständigen
Fehlergramen mit **unverändertem Faktor zwei und hoher Fehlerüberdeckung**
folgt der Kreuzpreis

    e_cross = d_D sqrt((r*G_F r)(w*G_J w))
              + sqrt(u_F e_J) + sqrt(e_F u_J) + sqrt(e_F e_J).

u_F,u_J sind die Modell-Featurequadrate, e_F,e_J die richtungsbezogenen
Fehlerquadrate. Die konkreten Grame stehen in `RESULT.json`.
Der Preis p=2 e_cross wird nach oben auf das rationale Raster 10^-24
gerundet. Der direkte gemeinsame D/U-Formfehler bleibt separat erhalten:

    a_square,lo = max(0, (z*K_new^-1 z)_lo - p),
    H_up = B0[Jw]_up + (d_D+d_U)(w*G_J w)_up - a_square,lo,
    E_test,lo = E_base,lo + 2 pairing_lo - H_up.          (4)

Es gibt keinen Betragstrick für negative Normquadrate. Die Auswertung
verwendet Arb bei 1024 Bit; (4) wird anschließend exakt rational gebildet.
Der unabhängige Audit schließt die Quadratwurzeln mit Integerarithmetik ein.

| Beitrag | Nach außen gerundete Anzeige |
| --- | ---: |
| Basisenergie | [15.47986480760; 15.60255832995]e-6 |
| Paarung <nu_new,Jw> | [38.27724687119; 38.30811288050]e-6 |
| Gemeinsamer D/U-Formfehler | <0.533596882148e-6 |
| Richtungsbezogener a_fin-Formpreis | <0.014669234698e-6 |
| Obergrenze H_new[Jw] | <38.84094599270e-6 |
| Vollständige Inversenergie, Untergrenze | >53.19341255729e-6 |
| K_P-Budget | [54.11716936070; 54.11716937864]e-6 |

Die ursprünglichen Eingaberadien der Basisenergie sind ebenfalls vorhanden.
Das Modell des Variationsausdrucks ohne zusätzliche physische Fehler liegt
bei [53.77254469957; 53.89523818961]e-6. Es ist keine volle
Inversenergieeinschließung. Unter den zusätzlich berechneten Fehlerpreisen
dominiert der gemeinsame D/U-Formpreis; sein Betrag ist keine gemessene
tatsächliche Abweichung.

## 6. Konsequenz und feste Stopplinie

Die Familie aus Abschnitt 2 ist ausgeschlossen. Weitere Gewichtsexperimente
innerhalb dieser Familie sind nicht begründet.

Der neue Schur-Untertest bleibt dagegen offen. Er beweist weder, dass
Q_new^-1 bereits zu teuer ist, noch, dass eine bessere Obermajorante genügt.
Die fehlende obere Kontrolle umfasst den ungenutzten eta-q-Anteil und
den variationalen Gewinn außerhalb des eingefrorenen Tests, einschließlich
des unendlichen Raums. Der Abstand 0.923756821331e-6 ist daher keine Reserve.

Vor einer aufwendigen oberen Einschließung müsste eine gesonderte
quantitative Vorprüfung diese bislang nicht nach oben kontrollierten
Beiträge und deren Fehlerpreise untersuchen. Eine solche Rechnung, eine
Antwortmatrix-Suche oder ein weiterer Variantenlauf wird hier nicht begonnen.

## 7. Reproduktion und Abnahme

`INPUT_BINDINGS.json` bindet #246/#247, die übernommene Inversgeometrie,
die alte variationale Fehlerherleitung und die gemeinsame Formfehlerschärfung.
Alle Recheneingaben werden als hashgeprüfte Bytes gelesen. `MANIFEST.json`
bindet das Paket. Die bestehenden 287er-Pivots und großen Integrationen
bleiben gebundene Voraussetzungen und werden lokal nicht erneut gerechnet.

Der vorab festgelegte Abnahmeplan umfasst einen frischen vollständigen
Git-Archiv-Replay, getrennten Auswahl-/Zertifikatsvergleich, unabhängigen
rationalen Audit, Negativkontrollen und Registerprüfungen. Jede vollständige
Ausführung ist auf 600 Sekunden begrenzt. `ACCEPTANCE.json` hält die tatsächlich
ausgeführten Prüfungen, Laufzeiten und Archivbindung fest. CI, Merge und
externe mathematische Prüfung bleiben davon getrennt.
