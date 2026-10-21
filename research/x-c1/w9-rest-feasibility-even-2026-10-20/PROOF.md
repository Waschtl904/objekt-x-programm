# Machbarkeitsprüfung des ganzen Restanschlusses am festen geraden Zeugen

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `34aad090a5a05037cae3e783e07c8382fa47f4b6` (#249).
Alle geerbten analytischen, Formdomänen-, Integrations- und Modellannahmen
bleiben Voraussetzungen. Die Rechnung verändert weder den physischen
Zeugen noch w, K_new, die äußere Antwortregel oder das Budget.

## 1. Entscheidung

**UPPER_CONTROL_ROUTE_TOO_COARSE.** Die vorgeschlagene Kontrolle mit den
unveränderten Fehlerhüllen und dem vorhandenen E_new-Residualpreis reicht
nicht für einen vollständigen oberen Vergleich. Das ist eine Entscheidung
über diesen Kontrollweg, kein Ausschluss der Unterform.

| Frage | Gerichtetes Ergebnis / konservative Anzeige |
| --- | --- |
| Vollständiger Testausdruck F(Jw) | [53.19429074226; 54.47525080963]e-6 |
| Budget | [54.11716936070; 54.11716937864]e-6 |
| Budget_lo minus F_up | etwa -0.358081448914e-6 |
| Exakte Antwortdarstellung X_ans u=w | Ja, Rang 84; rationale Definition unten |
| Kleinste gewichtete Koeffizientenenergie u*E_new u | [5.78117496215; 5.78117496216]e40 |
| Zertifizierter Formboden kappa | >3.24380497686e-6 |
| Preis aus R*R_L R <= c beta E_new für diese Darstellung | <2.53568064334e37 |
| Erforderliche obere ganze L-Dualenergie mit diesem F_up | negativer Zielwert, etwa -1.288481938752e-13 |

Bereits F_up lässt keinen Platz für eine positive Restobergrenze.
Die exakte Antwortdarstellung existiert, ihr bestmöglicher Preis in der
vorhandenen E_new-Metrik ist aber sehr groß. Andere Koeffizienten u bei
unverändertem X_ans und w können **diesen E-Preis** nicht verbessern.
Das besagt nichts über die tatsächliche Größe von R u oder über mögliche
Aufhebungen im ganzen Residuum. Keine neue Integration ist durch diese
Vorprüfung begründet. Punkt 4, N12 und externe Prüfung bleiben offen.

## 2. Vollständiger oberer Endpunkt des Testausdrucks

Auf dem ganzen Formraum gilt unverändert

    <f,Q_new^-1 f> = F(t)+Delta(t),       t=Jw,
    F(t)=E_base+2 Re nu(t)-H[t],
    Delta(t)=||nu-Ht||²_(H^-1)>=0.

Die bisherigen zweiseitigen Grenzen für E_base und nu(t) sowie alle
Formfehler stammen aus #248, der eta-q-Term aus #249. Bezeichne

    a0=a_fin,model w, d=(a_fin-a_fin,model)w,
    N0=a0*K_new^-1 a0,
    e >= ||K_new^-1/2 d||,
    p >= 2 |(K_new^-1 a0)*d|.

Der richtungsbezogene Kreuzpreis p aus #248 kontrolliert den Betrag
und gilt daher in beiden Richtungen. Für eine **obere** Grenze des
Quadrats darf der positive quadratische Fehler nicht entfallen:

    (a0+d)*K_new^-1(a0+d) <= N0_up+p+e².

Mit delta_B als unverändertem gemeinsamen D/U-Formpreis folgt

    H_lo = B0_lo-delta_B-N0_up-p-e²-(eta q)_up,
    F_up = E_base,up+2 pairing_up-H_lo.                 (1)

Die untere Grenze bleibt exakt die aus #249. Es wurde keine alte
Fehlergrenze verkleinert. Abhängigkeiten zwischen den Eingabefehlern
beeinträchtigen diese Summenabschätzung nicht.

Die vollständige Breite von F ist exakt die Summe folgender Beiträge:

| Beitrag zur Intervallbreite | Größenordnung |
| --- | ---: |
| Basisenergiebreite | 0.122693522346e-6 |
| Doppelte Paarungsbreite | 0.0617320186081e-6 |
| Doppelte gemeinsame D/U-Formfehlerschranke | 1.067193764296e-6 |
| Einschließung des a_fin-Quadrats, einschließlich e² | 0.0293407621104e-6 |
| Numerische B0-Breite und eta-q-Breite | <1e-30 |

Der größte Preis ist damit die gemeinsame D/U-Formfehlerschranke
delta_B ~=0.533596882148e-6. Ihre Größe ist keine gemessene tatsächliche
Formabweichung. Der obere Endpunkt liegt schon vor Addition von Delta
über Budget_lo. Dies liefert weder F(t)>Budget noch einen Ausschluss:
Die untere Grenze liegt weiterhin darunter.

## 3. Exakte Darstellung und günstigster vorhandener Transport

E=E_new ist die gebundene positive rationale 203er-Matrix,
X=X_ans die unveränderte rationale 84x203-Antwortmatrix. Wir bilden

    P = X E^-1 X*.

Ein gerichteter Solve bei 1024 Bit und eine rationale untere Matrix
P_lo<=P ergeben einen positiven 85er-Block

    [ P_lo   w ]
    [ w*     s ] >0.                                  (2)

Die ersten 84 positiven Pivots beweisen P_lo>0, also Rang(X)=84.
Damit ist die folgende **rationale Definition** eine exakte Darstellung:

    u_min = E^-1 X* P^-1 w,       X u_min = w.

Hier wird u nicht durch eine gerundete Dezimalliste ersetzt. Seine
Definition benutzt ausschließlich die hashgebundenen rationalen Matrizen
und w. (2) gibt u_min*E u_min=w*P^-1w<s.

Für jedes andere u mit Xu=w schreibt man u=u_min+v mit Xv=0. Dann

    u*E u = w*P^-1w+v*E v >= w*P^-1w.                 (3)

Auch die untere Kostenbegrenzung wird unabhängig rational geprüft.
Aus der gerichteten P-Auswertung entsteht P_up>=P; für einen fest
rationalisierten dualen Vektor z gilt

    w*P^-1w >= 2 w*z-z*P z >= 2 w*z-z*P_up z.           (4)

FINITE.json enthält P_lo, den diagonalen Abstand zu P_up, z und die
exakten Kostenendpunkte. z dient nur (4), nicht als neue physische
Prüfrichtung. Zusammen liefern (2),(4) die veröffentlichte enge
Kostenhülle um 5.7811749621574e40.

Die geerbte vollständige Restschranke aus #246 lautet

    R*R_L R <= c beta E_new,
    c=1977/500000, beta=20209999981781/182190000000000.

Somit

    ||R u_min||²_(R_L) <= c beta s <2.53568064334e37.

Bereits der **kleinstmögliche Ausdruck** c beta u*E u über allen exakten
Darstellungen ist >2.53568064333e37. Das ist eine Untergrenze des
verfügbaren Majorantenpreises, ausdrücklich **keine Untergrenze von
||R u||²_(R_L)**. Der tatsächliche Rest kann wesentlich kleiner sein.
Die Zahl macht diesen skalaren E-Transport unbrauchbar für die hier
angestrebten Energiegrößen, ohne einen anderen gemeinsamen Fehlergram
oder einen kohärenten Ganzrestnachweis auszuschließen.

Die Antwortgeometrie hat sehr kleine positive Pivots. Der erste
technische Versuch mit 80-stelliger Matrixausgabe und 120-stelligem
Audit bewies Pivot 62 nicht. Er wurde nicht als Rankverlust interpretiert.
Mit unveränderten Eingaben und 1024 Bit werden die Matrixhüllen auf
200 Dezimalstellen und der rationale Pivotaudit auf 300 Stellen geführt.
Alle 85 Pivots sind positiv. Dies ist eine technische Korrektur der
Ausgabe-/Prüfraster, keine Änderung von Vektor oder Mathematik.

## 4. Zertifizierter Formboden und tatsächlich nötiger Restpreis

Die unveränderte Kraftmetrik ist

    D_new=diag((1-rho)I191,K_new).

E_new wird exakt aus E_old+diag(0_191,K_new-K_old) rekonstruiert und
gegen den veröffentlichten Matrixhash aus #246 geprüft. Eine konservative
Wahl epsilon=1/ceil(tr(E_new^-1 D_new)) wird direkt durch

    E_new-epsilon D_new >0

mit **203 rationalen positiven Pivots** zertifiziert. Daher gilt mit
kappa=(1-c)epsilon

    H_new >= kappa S >= kappa beta L,
    Delta(t) <= ||r||²_(R_L)/(kappa beta),   r=nu-H_new t.

Die Werte sind epsilon ~=3.25668189708234e-6 und
kappa ~=3.24380497686128e-6. Dieser Boden ist zulässig, nicht als
optimal behauptet.

Die hinreichende Bedingung für einen vollständigen oberen Vergleich
wäre

    ||r||²_(R_L) < kappa beta (Budget_lo-F_up).           (5)

Mit (1) ist die rechte Seite **negativ**, etwa -1.288481938752e-13.
Eine nichtnegative Energie kann (5) nicht erfüllen. Ein besserer
positiver Formboden allein beseitigt dieses Vorzeichenproblem nicht.
Die ganze Inversenergie wurde weder nach oben berechnet noch widerlegt.

## 5. Vorhandene Daten, fehlende gemeinsame Daten und Stopplinie

Mit Z=JX und R=A*-SZ liefert die exakte Darstellung

    r = nu + A*(D_new^-1 A Jw-u_min) + R u_min.          (6)

Vorhanden sind die rationalen Antwort-/Schurmatrizen, die 84 nu-Koordinaten,
die gerichteten Modelle von A J, die bisherigen gemeinsamen Quellenfehler
und der vollständige obere R-Gramvergleich. Diese ermöglichen die
vorliegende Rang-, Kosten- und Bodenprüfung ohne Funktionsintegration.

Der gebundene Bestand enthält hingegen keinen vollständigen gemeinsamen
L-dualen Gram für die **neue gesamte Differenz (6)**. Insbesondere
fehlen für einen brauchbaren oberen Anschluss:

- eine gerichtete vollständige Darstellung des neuen nu im L-Dualraum;
- dessen gemischte Dualpaarungen mit den beteiligten Kraft- und
  Restfunktionalen, einschließlich des unendlichen Anteils;
- ein gemeinsamer Fehlertransport für (6), der seine Aufhebungen erhält.

Die alte vollständige Schranke für R u ist vorhanden; sie ist nicht mit
fehlenden alten Daten zu verwechseln. Nur 84 gespeicherte Koordinaten
oder eine Summe isolierter grober Normpreise schließen den neuen ganzen
Rest nicht. Die alte vollständige Residualgeometrie und die Quellenmodelle
sind mögliche Bausteine für einen geänderten Nachweis, aber noch kein
solcher Nachweis für (6).

**Stopplinie:** Keine neue Integration mit dem Ziel, einen positiven
Rest unter den negativen Zielwert (5) zu drücken. Keine Suche nach
anderen u zur Rettung derselben E-Majorante; (3),(4) entscheiden deren
bestmöglichen Preis bereits. Ein neuer Auftrag braucht einen quantitativ
begründeten gemeinsamen Kontrollweg, der sowohl F_up als auch den
ganzen Residualpreis behandelt. Er wurde hier nicht begonnen.

Die zu große obere Hülle und der große Transportpreis beweisen kein
Scheitern von Q_new, der tatsächlichen A9-Inverse oder Objekt X.
Auch ein einzelner erfolgreicher oberer Zeugenvergleich wäre kein
Abschluss von Punkt 4.

## 6. Abnahme

INPUT_BINDINGS.json bindet die einmal gelesenen Eingaben und Archive.
RESULT.json hält die Entscheidung und FINITE.json die endlichen
Zertifikatsdaten fest. Der rationale Audit prüft die Endpunkte, den
unteren Mindestkostenzeugen und das Vorzeichen der Zielschranke.
Die Positivitätstests sind unabhängig von der Arb-Rechnung ganzzahlig.
Der frische Replay umfasst das Paket und alle tatsächlich verwendeten
Dateiabhaengigkeiten, nicht das ganze Repository oder frühere Integrationen.
ACCEPTANCE.json dokumentiert Prüfungen und Laufzeiten getrennt von CI,
Merge und externer mathematischer Prüfung.
