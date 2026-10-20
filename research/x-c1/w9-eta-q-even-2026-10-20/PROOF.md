# eta q[Jw] am festen K_new-Testvektor: positiv, aber nicht entscheidend

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `4e292a178bc3034049eb7abfa0c915a3c2bf815f` (#248).
Alle Aussagen stehen unter den unveränderten gebundenen analytischen,
Formdomänen-, Integrations- und Modellvoraussetzungen der Vorgängerkette.

## 1. Ergebnis und unveränderter Scope

Der ausschließlich ergänzte positive Term ist gerichtet eingeschlossen:

    8.78184963678e-10 < eta q[Jw] < 8.78184963679e-10.

Bei Übernahme aller bisherigen Grenzen ergibt sich

    <f,Q_new^-1 f> > 53.19429074226e-6.

Das Budget bleibt in [54.11716936070; 54.11716937864]e-6.
**SCHUR_LOWER_TEST_OPEN** bleibt bestehen. Die genaue Differenz zwischen
Budgetobergrenze und neuer Testuntergrenze beträgt etwa 0.922878636368e-6.
Sie ist keine obere Reserve und keine gemessene Differenz zur tatsächlichen
Inversenergie.

Schon die **obere** eta-q-Grenze ist kleiner als die bisherige Lücke
0.923756821331317...e-6; der Zusatz deckt weniger als 0.095067 % dieser
Lücke. Weitere Präzision allein an diesem Term kann sie somit nicht
schließen, solange die übrigen Grenzen unverändert bleiben.

Vektor, physischer Zeuge, K_new, äußere Antwortmatrix, Budget, Basis-,
Paarungs- und Formfehler bleiben unverändert. Keine neue Integration,
Lösung eines Gleichungssystems, Kandidatensuche oder RL-Rechnung.
Der Ausschluss der festen Young-Familie aus #248 bleibt unberührt.
Punkt 4, N12, Objekt X und externe Prüfung bleiben offen.

## 2. Identität der Form und vorhandenes Sandwich

Die gebundene `RESPONSES_PROOF.txt`, Abschnitt 1, definiert

    q[r,s] = q_b[Lambda r,Lambda s],       eta = 10^-10.

J ist die feste physische 84er-Basis auf dem exakten Rest T.
Die geordnete direkte 96er-Form hat die Basis

    (z1,...,z4, Lambda Y1,...,Lambda Y8, Lambda J1,...,Lambda J84).

Deshalb ist q[Jw] die direkte Form am Koeffizientenvektor (0_12,w).
Es wird weder die gewichtete Hilfsform L noch D-U noch eine Schurform
als q eingesetzt.

Das geerbte tatsächliche Sandwich lautet

    D96_lower <= D_actual <= D96_upper.

Die Dateinamen enthalten zwar `model`; ihre analytischen Zuschläge sind
bereits eingeschlossen. `COMMON96_HERLEITUNG.txt`, Abschnitt 6, und
`refine_old_majorant.py` binden die physischen z-Grenzen, den direkten
Kreuzpreis und die Abzüge/Zuschläge 96e-25 I96. Der JJ-Block stammt aus
der mit vollständigen analytischen Resten eingeschlossenen D92-Matrix.
Die vorhandenen numerischen Intervallradien werden zusätzlich vollständig
mitgerechnet. Diese Herkunft wird übernommen, nicht neu integriert.

Die unveränderten Daten werden aus dem hashgeprüften Stufe-3-Archiv
entnommen; der komprimierte Common96-Inhalt wird nochmals gegen seinen
bereits veröffentlichten Hash geprüft. Der Vektor ist exakt rational
und bytegleich zu #248, SHA-256
`70e8f72ab0cb8ca1ac0d254392384a2040a9d76d04ebf82587c48771e9f34628`.

## 3. Gerichtete Rechnung und Addition mit richtigem Vorzeichen

Setze d=(0_12,w). Mit exakter rationaler Intervallarithmetik:

    q_lo = lower(d* D96_lower d),
    q_hi = upper(d* D96_upper d),
    q_lo <= q[Jw] <= q_hi.

Es folgt die nach außen gerundete Anzeige

    8.78184963678289659085364
      < q[Jw] <
    8.78184963678289659085367.

Bei negativen Produkten w_i w_j werden die Eintragsendpunkte vertauscht.
Beide Kreuzterme werden mitgerechnet. Der unabhängige Audit verwendet
stattdessen Mittelpunkt und Radius und fasst transponierte Einträge
zusammen; er setzt keine exakte Symmetrie gerundeter Intervalle voraus.
Beide Wege stimmen exakt rational überein. `RESULT.json` enthält die
ungekürzten rationalen Endpunkte.

Im Vorgänger war

    H_new[Jw] = B[Jw] - (a_fin w)*K_new^-1(a_fin w) - eta q[Jw]

nach oben eingeschlossen worden, indem der letzte negative Term entfiel.
Bei unverändertem H_old,up und bisheriger Testuntergrenze E_old,lo gilt
jetzt

    H_new[Jw] <= H_old,up - eta q_lo,
    E_new,lo = E_old,lo + eta q_lo <= <f,Q_new^-1 f>.

Die Addition benötigt keine Unabhängigkeit der Unsicherheiten. Der alte
Endpunkt wird identisch übernommen, eta q genau einmal ergänzt. Die
übrigen Fehler werden weder entfernt noch verkleinert. Eine obere
Inversenergie folgt auch aus dem zweiseitigen eta-q-Intervall nicht.

## 4. Was als variationaler Rest noch fehlt

Sei t=Jw, H=H_new, nu=nu_new. Auf dem vollständigen Formraum gilt

    F(t) = E_base + 2 Re nu(t) - H[t],
    <f,Q_new^-1 f> = F(t) + Delta(t),
    Delta(t) = ||nu-Ht||^2_(H^-1) >= 0.                 (1)

Ht wird hier als **Formfunktional** verstanden; eine starke
Operatorzugehörigkeit von t wird nicht vorausgesetzt. Die duale
Schreibweise bezeichnet die durch die positive geschlossene Form
induzierte Inversenergie. (1) ist die Quadratergänzung im Formraum.
Sie enthält sowohl den verbleibenden Gewinn innerhalb des 84er-Raums
als auch den unendlichen Rest. Diese Teile dürfen ohne passende
H-orthogonale Zerlegung nicht getrennt addiert werden.

Dieser Rest ist noch nicht gerichtet ausgewertet. Für einen Ausschluss
genügte nun Delta_lo > Budget_up-E_new,lo, also ein Gewinn größer als
ungefähr 0.922878636368e-6, unter Beibehaltung der bisherigen Grenzen.
Eine kleinere Untergrenze bliebe unentschieden.

Für einen erfolgreichen oberen Vergleich bräuchte man dagegen **beides**:
einen vollständigen oberen Endpunkt F_up und eine Obergrenze Delta_up
mit F_up+Delta_up < Budget_lo. Die obige Lücke aus Untergrenzen ist
keine hinreichende Erfolgsschwelle.

## 5. Konkreter begrenzter Kontrollweg vor einer Großrechnung

Ein nächster Auftrag kann zuerst die vollständige duale Darstellbarkeit
des **festen** Residualfunktionals r=nu-HJw prüfen. Die 84 gespeicherten
Koordinaten J*r kontrollieren dessen ganzen Rest nicht.

Ein expliziter, zunächst konservativer Weg verwendet vorhandene endliche
Matrizen und die geerbte volle Residualungleichung:

    H = S-A*D_new^-1 A,
    D_new-A S^-1 A* >= (1-c) E_new,
    S >= beta L.

Wird eine rationale Konstante epsilon>0 mit E_new>=epsilon D_new
zertifiziert, folgt

    H >= kappa S >= kappa beta L,   kappa=(1-c)epsilon,
    Delta(t) <= ||r||^2_(R_L)/(kappa beta).              (2)

Das erste Ziel wäre, aus den vorhandenen 203er-Matrizen epsilon zu
bestimmen und **vor jeder neuen Integration** aufzulisten, welche
vollständigen L-dualen Funktions- und Fehlerdaten für r bereits
gebunden sind und welche fehlen. (2) verlangt die ganze L-duale Energie,
nicht eine Inverse der abgeschnittenen 84er-Matrix.

Als algebraische Wiederverwendungsprüfung kommt ferner infrage:
Für die vorhandenen Antworten Z=J X_ans und Residuen R=A*-SZ gilt,
falls eine exakte Darstellung w=X_ans u nachgewiesen wird,

    r = nu + A*(D_new^-1 A Jw-u) + R u.

Ob eine solche Darstellung existiert und brauchbare Fehlerpreise hat,
ist hier **nicht** geprüft. Sie wäre eine Prüfung des vorhandenen
Antwortbestands, keine Änderung des physischen Zeugen. Gemeinsame
Fehlergrame und Kreuzterme müssten erhalten bleiben.

Erst eine quantitative Abschätzung von F_up, kappa und dem ganzen
Residualpreis könnte eine teure obere Rechnung begründen. Alternativ
könnte eine gezielte variationale Restuntergrenze (1) einen Ausschluss
liefern. Keiner dieser Folgeaufträge wurde hier gestartet. Aus diesem
kleinen eta-q-Befund folgt keine Erfolgsaussicht der neuen Unterform.

## 6. Abnahme

Der vorab festgelegte Plan steht in `ACCEPTANCE_PLAN.md`. `verify.py`
benutzt nur die einmal gelesenen, hashgeprüften Eingabebytes. `audit.py`
prüft den neuen Skalar und die Endentscheidung unabhängig rational.
Der Replay benutzt ein frisches Git-Archiv dieses Pakets mit allen
seinen Dateiabhaengigkeiten; es ist ausdrücklich kein Vollarchiv des
Repositories und kein erneuter Nachweis der historischen Integrationen.
`ACCEPTANCE.json` dokumentiert die tatsächlich ausgeführten Prüfungen.
