# Dual-Vorprüfung: der gesamte feste Vergleich scheitert am geraden Zeugen

20. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: #246, `93cf629d5efdbf93d6a3cfef8cb849134f1f72ff`.
Es gelten die gebundenen Operator-, Formdomänen-, Quellen- und
Integrationsvoraussetzungen der bisherigen Kette.

## 1. Ergebnis und Stopplinie

**FULL_FIXED_COMPARISON_EXCLUDED_BY_DUAL_LOWER.**
Der unveränderte geradparitätische Zeuge genügt, um den vollständigen
in #245 ausgewählten W_new-Vergleich auszuschließen. Die Begründung ist
eine gerichtete **Untergrenze der gesamten Vergleichsenergie**:

| Größe | Gerichtete, konservative Dezimalanzeige |
| --- | ---: |
| Vollständige Dualenergie, Untergrenze | > 1.369503316340e-6 |
| Gesamte Vergleichsenergie, Untergrenze | > 69.15149379521e-6 |
| Tatsächliches K_P-Budget, Obergrenze | < 54.11716937864e-6 |
| Abstand der Gesamtuntergrenze zur Budgetobergrenze | > 15.03432441658e-6 |

Die maßgeblichen rationalen Endpunkte stehen in `EXPECTED.json`.
Die bloße Überschreitung einer hinreichenden Passschwelle durch eine
Obergrenze wird an keiner Stelle als Ausschluss gewertet.

Der gerichtete Teilpass aus #246 bleibt gültig. Er enthielt den Dualterm
ausdrücklich nicht. Bereits dessen auf Basis84 gestützte variationale
Untergrenze ist hier groß genug, um die volle Entscheidung zu treffen.
Eine vollständige obere Dualeinschließung oder neue Restintegration ist
deshalb für diesen Ausschluss nicht erforderlich und wurde nicht begonnen.

Ausgeschlossen ist **die ausgewählte vollständige W_new-Majorante mit
den festen Gewichten, der eingefrorenen äußeren Antwort und dem Budget
am festen geraden Zeugen**. Es ist kein Ausschluss der tatsächlichen
A9-Inverse, aller Majoranten der neuen Unterform, anderer Gewichte
oder anderer Antwortregeln. Keine negative Weil-Richtung, kein
N12-Abschluss. Punkt 4 und externe Prüfung bleiben offen.

## 2. Warum endliche Daten hier ausreichen

R_L ist die inverse L-Form auf dem gesamten exakten T. Für jedes
L-formdualstetige nu gilt

    D_full = <nu,R_L nu>
           = sup_(t in D(L) intersect T) (2 Re nu(t)-L[t]).

Die exakte Basis84 J liegt in T und in der Formdomäne. Mit n=J*nu und
E_L=L[J,J]>0 folgt durch Einschränken des Supremums auf t=Jx

    D_full >= n* E_L^-1 n.                              (1)

Das ist eine Untergrenze auf dem ganzen Raum. Die 84 Koordinaten
liefern damit keine obere Schranke des ganzen Dualterms.
Weder der unendliche Rest noch seine Momentkorrekturen werden als null
gesetzt. Variational ist die Differenz zwischen vollständiger Energie
und endlicher Galerkinenergie nichtnegativ; einzelne Summanden einer
anderen Darstellung mit Rang-eins-Korrektur werden nicht verworfen.

Der Prüfer bildet eine rationale Obermatrix E_plus >= E_L. Für
M=E_plus^-1 folgt die inverse Formordnung

    0 < M <= E_L^-1,  D_full >= n* M n.                  (2)

Es genügt deshalb eine gerichtete Untergrenze des endlichen Ausdrucks
rechts in (2), einschließlich sämtlicher Fehler von n.

## 3. Welche vorhandenen Daten wiederverwendet werden

| Daten | Verwendung |
| --- | --- |
| #246: K_new, physischer Zeuge, Budget, Gewichte und Teilenergie | unverändert, hashgebunden; kein erneuter 287er-Pilotlauf |
| Exakte rationale D-Koeffizienten und alte momentorthogonale Q-Basis | J=Q(D;I_84), 96 lokale Legendrekoeffizienten |
| Gemeinsame gespeicherte Paarungen und ursprüngliche Quellenfehler | erneutes n=J*nu mit genau derselben K_new |
| Parametrisierte positive Feature-/Fehlerformeln des alten Piloten | Fehler in der neuen Hilfsmetrik M statt der Schur-P-Metrik |
| Ganze Residualmodellfehler | Transport durch eine erneut berechnete positive Hilfsnormmajorante |

Die Nebenbedingungen werden in den exakten Q-Koordinaten geprüft:
S* (D;I)=0 in 672 rationalen Einträgen. Die exakte W_X-Metrik von
J ist G_J=(D;I)*(D;I); ihre Normobergrenze 1.000502 wird aus
1+sum D_ij^2 bestätigt. Die Orthogonalitäts- und Domänenherleitung
der ursprünglichen Q-Basis bleibt gebundene Voraussetzung.

Mit lokalen Legendregewichten d_n=H_n+11/10 wird

    E_L = J_local* diag(d_0,...,d_95) J_local

bei 1024 Bit eingeschlossen. Symmetrische Mittelpunkte und Zeilenradien
auf einem 60-stelligen Raster liefern rationale Unter- und Obermatrizen
mit zusätzlichem Abstand 10^-40 I. Der unabhängige Integer-Intervallauditor
bestätigt alle 84 positiven Pivots von

    E_minus - (21/5) G_J > 0.

Damit sind E_L und E_plus positiv. Die vollständige rationale Obermatrix
steht in `L_UPPER.json`; der Prüfer invertiert diese exakte Matrix
mit gerichteter Intervallarithmetik. Die Matrix ist keine neue
P-Obermatrix des A9-Schurvergleichs. Sie dient ausschließlich (2).

## 4. Alle betroffenen Fehler in der richtigen Metrik

Es wird kein schlechter Normtransport über die inverse Schur-P-Matrix
benutzt. Stattdessen werden die vorhandenen parametrisierten Formeln
direkt mit dem positiven Gewicht M und Hilfsgewicht 1 ausgewertet.
Ihre Anwendung benötigt hier nur M>0, nicht eine Ordnung von M gegen
X_ans E_new^-1 X_ans*. Eine solche Ordnung wird nicht behauptet.

Das gemeinsame Modell

    n0 = J*(f_T-g*U8 h-a_fin* K_new^-1 v)

wird neu zusammengesetzt. Alle 84 gerichteten Koordinaten überlappen
denen aus #246. Beide algebraischen nu-Identitäten und die bisherigen
Quellenkontrollen werden erneut geprüft. Der physische Zeuge und seine
W-Normierung bleiben dieselben.

Die v-, Quellen-, Integrations- und a_fin-Fehler werden mit M gewichtet.
Insbesondere bleiben die vollen ursprünglichen F-J-Fehler d_U, d_D
und d_a erhalten. Die bessere F-F-Untergrenze von K_new ersetzt sie
nicht. Der a_fin-Fehler einschließlich seines Kreuzterms wird einmal
bezahlt. Für die ganze Hilbert-Residualabweichung wird eine neue
Hilfsnormmajorante w_M berechnet. Sie majorisiert die positive Summe
von U8-, K_new- und M-Feature und daher insbesondere das M-Feature.
Die Verwendung der ganzen Summe für den Residualfehler ist konservativ.

Gerichtet erhält man für m0=n0* M n0:

    m0 in [1.369631231678826e-6, 1.369631231679029e-6],
    e_feature < 5.464998567964e-8,
    e_whole   < 1.370589637939e-12.

Die letzten beiden Größen sind **Normfehler**, keine Energiefehler.
Mit e=e_feature+e_whole gilt die vollständige Einschließung des
endlichen Hilfsausdrucks

    n* M n in [(max(0,sqrt(m0_lo)-e_up))^2,
               (sqrt(m0_hi)+e_up)^2].                   (3)

Dessen obere Seite ist keine Obergrenze für D_full. Für (2) wird
ausschließlich die untere Seite verwendet:

    D_full >= d_lo > 1.369503316340e-6.

Die gebundene Hilbert-Residualabweichung schließt die vollständige
Modellfunktion ein; sie ist kein Fehler nur auf 84 Abtaststellen.
Die ganzen log-/Gamma- und Primzellenfehler stammen aus den vorhandenen
Funktionszertifikaten. Neue Funktionsintegrationen erfolgen hier nicht.

## 5. Vergleich mit der gesamten Energie

Seien [e_lo,e_hi] das Teilenergieintervall und [k_lo,k_hi] das
unveränderte Budget aus #246. Für die ausgewählte vollständige Majorante
gilt definitionsgemäß

    E_full = E_partial + (a/beta) D_full.

Die Summe von Untergrenzen bleibt auch bei gemeinsam abhängigen Fehlern
eine gültige Untergrenze; es wird keine statistische Unabhängigkeit benutzt.
Aus den nach außen gerundeten rationalen Endpunkten folgt exakt

    E_full >= e_lo + (a/beta) d_lo > k_hi.               (4)

Die zwei Entscheidungsschwellen werden ausdrücklich unterschieden:

    Pass hinreichend bei D_full,upper < (k_lo-e_hi)/(a/beta)
                                     ~= 1.904349883230e-8,
    Ausschluss hinreichend bei D_full,lower > (k_hi-e_lo)/(a/beta)
                                           ~= 3.807788423766e-8.

Hier übersteigt die gerichtete Dualuntergrenze auch die zweite Schwelle
deutlich. Damit ist (4) erfüllt. Eine große Obergrenze allein hätte
diesen Schluss nicht erlaubt.

## 6. Vollständiger Rest: verfügbarer Weg und fehlende Daten

Für eine obere Dualeinschließung wäre die folgende vorhandene Identität
anwendbar. Für einen tatsächlich zulässigen t mit L_T t in T und
r=nu-L_T t gilt

    D_full = 2 Re nu(t)-L[t]+<r,R_L r>,
    0 <= <r,R_L r> <= (5/21)||r||_WX^2.

Die dazu benötigten Bausteine sind die vorhandene lokale L-Geometrie,
die exakten Nebenbedingungen und analytischen Quellmodelle.
Es fehlt für diesen neuen nu jedoch eine gerichtete vollständige
Funktionsdarstellung mit bezahltem gemeinsamen Fehler sowie die
volle WX-Residualnorm beziehungsweise ein schärferer gewichteter
unendlicher Rest. Die 84 gespeicherten Koordinaten liefern diese
Größen nicht. Ein endliches Modell oder Gradabbruch wäre kein Ersatz.

Wegen (4) wird diese obere Rechnung für den festen Vergleich nicht
beauftragt. Auch eine genauere obere Einschließung kann die bereits
zertifizierte Untergrenze nicht unterschreiten. Der nächste Forschungsweg
verlangt eine begründete Änderung einer Voraussetzung dieses konkreten
Vergleichs; diese Vorprüfung wählt keine neue Variante.

## 7. Abnahme und Grenzen

Der erste vollständige Certifierlauf dauerte 25.097 Sekunden.
Jeder vollständige Aufruf wird nach 300 Sekunden beendet; keine
Nachschärfungsserie. Frischer Paketarchiv-Replay, Bindungen, unabhängiger
rationaler Endpunktaudit und lokale Prüfungen werden in
`ACCEPTANCE.json` getrennt von der späteren Repository-CI dokumentiert.
Historische Integrationen und der bestandene Teilpilot werden nicht
erneut als Großrechnung ausgeführt.

Abgeschlossen ist eine gerichtete Dualunterprüfung mit daraus folgendem
Ausschluss des gesamten festen W_new-Vergleichs. Eine vollständige
Dualenergieeinschließung, ein allgemeines Majoranten-No-Go oder ein
negativer tatsächlicher A9-Schurrest wird nicht behauptet.
