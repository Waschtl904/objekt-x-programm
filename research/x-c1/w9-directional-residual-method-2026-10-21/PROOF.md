# Richtungsbezogene F-Hülle und direkte Kontrolle des ganzen Residuums

21. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `639d25e38b453f2e10b859553ca49a7a0e4fafdb`.
Alle gebundenen analytischen, Operator-, Domänen-, Quellenmodell- und
Integrationsvoraussetzungen der Vorgänger bleiben Voraussetzungen.

## 1. Entscheidung und Reichweite

**METHOD_PILOT_REQUIRES_FULL_RESIDUAL.** Der feste gerade Zeuge, der rationale
84er-Vektor w, K_new, die äußere Antwortregel und das K_P-Budget bleiben
unverändert. Keine Integration, neue physische Richtung oder Änderung von
A1. Die kleine Rechnung verwendet vorhandene gemeinsame Fehlergrame.

| Größe | Konservative äußere Anzeige |
| --- | --- |
| Alter pauschaler B-Formfehler | <5.33596882148e-7 |
| Neuer richtungsbezogener B-Formfehler | <2.16264682725e-9 |
| F(Jw) | [53.72572497758; 53.94381657431]e-6 |
| Budget | [54.11716936070; 54.11716937864]e-6 |
| Budget_unten minus F_oben | >1.73352786406e-7 |
| Endliche Restenergie (J*r)*P_upper(J*r) | <4.50077994523e-11 |
| Hinreichendes Arbeitsziel für die GANZE L-Dualenergie von r | <=1.9e-8 |
| Gesamtabstand zum Budget, NUR WENN dieses Arbeitsziel erfüllt ist | >9.95058e-10 |

Das Arbeitsziel 1.9e-8 ist **kein berechneter Restwert**. Es schließt alle
Modell-, Koeffizienten- und Integrationsfehler des tatsächlichen ganzen
Residuums ein. Dessen unendlicher Anteil ist hier nicht berechnet.
Insbesondere wird kein vollständiger Inversvergleich, Teilpass, Abschluss
von Punkt 4/N12 oder externer Audit behauptet.

Die Methodenentscheidung lautet: Ein direkter, gemeinsamer Residualpilot ist
mathematisch sinnvoll begrenzt. Zuerst müssen seine vollständige Darstellung
und Fehlerpreise gegen das Ziel geprüft werden. Die alte Darstellung
X_ans u=w mit riesigem E-Preis und der alte globale kappa-Boden werden für
diesen Kontrollweg nicht benötigt. Die alten No-Gos bleiben gültig.

## 2. Erster Gewinn: den J-Formfehler in seiner tatsächlichen Richtung bezahlen

Im bisherigen Test ist B=D-U, U=Phi*Phi und U0=Phi0*Phi0. Die gebundene
vollständige Feature-Fehlermatrix E schließt (Phi-Phi0) ein. Sie enthält
unverändert Faktor zwei und die hohe Fehlerüberdeckung; siehe
[Teilenergie §4](../w9-partial-energy-2026-10-18/PROOF.md) und
[Formfehlerschärfung §4](../w9-schur-form-error-even-2026-10-19/PROOF.md).

Für den festen w seien

    u_J = w*U0_JJ w, e_J = w*E_JJ w, g_J = w*G_J w.

Aus dem Quadrat von Phi0 Jw+(Phi-Phi0)Jw folgt ohne Unabhängigkeitsannahme

    |U[Jw]-U0[Jw]| <= 2 sqrt(u_J e_J)+e_J.

Die vorhandene direkte Sandwichschranke liefert weiterhin

    |D[Jw]-D0[Jw]| <= d_D g_J.

Damit ist

    delta_B,new = d_D g_J + 2 sqrt(u_J e_J)+e_J

ein zweiseitiger Formfehler. Die in #248 gespeicherten gerichteten Grame sind
u_J ungefähr 1.43938987463, e_J ungefähr 1.23121712034e-28 und
g_J ungefähr 1.22202019103. `verify.py` prüft ihre Überlappung mit der neuen
Auswertung der unveränderten, hashgebundenen vollständigen Quellenmatrizen.
Alle Quadratwurzeln der skalaren F-Rechnung werden rational nach oben
eingeschlossen. Die kleinere reine F-F-K-Grenze wird NICHT auf J übertragen.

Im vollständigen F-Intervall von #250 ändern wir ausschließlich diesen Preis:

    F_neu,lo = F_alt,lo + delta_B,alt - delta_B,neu,
    F_neu,hi = F_alt,hi - delta_B,alt + delta_B,neu.

Basis-, Paarungs-, a_fin-Quadrat- und eta-q-Grenzen bleiben genau erhalten.
Auch der positive quadratische a_fin-Fehler bleibt in der oberen Hülle.
Dies erklärt den Gewinn, ohne zusätzliche Präzision oder neue Integration.
Die positive Differenz Budget_lo-F_neu,hi ist nur ein zulässiger Preis für
den noch offenen Rest, keine schon bestandene Gesamtenergieprüfung.

## 3. Zweiter Ansatz: die vorhandene Inversabschätzung auf r anwenden

Setze t=Jw und verwende dieselben tatsächlichen Formen wie in #248–#250:

    r = nu_new - H_new t,
    <f,Q_new^-1 f> = F(t) + <r,H_new^-1 r>.

Das Residuum ist zunächst ein Formfunktional. Die vollständige
L-Dualstetigkeit und die spätere Normschranke müssen für den direkten
Rechenweg belegt werden; es wird keine unbeschränkte Operatorwirkung auf
einen beliebigen Hilbertvektor vorausgesetzt.

Aus [Inversherleitung §2](../a9-inverse-renewal-2026-10-13/original/HERLEITUNG.txt)
und dem in #246 übertragenen vollständigen Restvergleich folgen

    <r,H_new^-1 r> <= (x²+y²+2 sqrt(c)xy)/(1-c),
    x² = beta^-1 <r,R_L r>,
    y² = (J*r)*P_new_upper(J*r),
    c = 1977/500000, beta = 20209999981781/182190000000000.

Hier ersetzen wir die beiden dortigen nichtnegativen Größen durch ihre
Obergrenzen; der Ausdruck wächst in beiden. Die Beziehung von P_upper zu
X_ans E_new^-1 X_ans* wird aus dem gebundenen 287er-Zertifikat übernommen.
Die Anwendung gilt für **das neue ganze Residuum**, nicht für die alte
Quelle nu. Der Ausschluss der Young-Familie für nu aus #248 wird dadurch
nicht aufgehoben oder erneut getestet.

Im Vergleich zu Delta<=||r||²_RL/(kappa beta) wird die schlechte globale
Konstante vermieden. Nur im hypothetischen Spezialfall J*r=0 wäre die
zulässige Restschwelle um (1-c)/kappa=307061 größer. Dieser Faktor wird
NICHT als tatsächlicher Gewinn ohne endlichen Fehler ausgegeben. Der
nächste Abschnitt bezahlt J*r ausdrücklich.

Für einen gegebenen y und m=Budget_lo-F_hi ist ein scharfes hinreichendes
Arbeitsziel dieses Vergleichs

    <r,R_L r> < beta [sqrt((1-c)(m-y²))-sqrt(c)y]²,

sofern die Wurzeln definiert und die rechte Klammer positiv sind.
Wir verwenden stattdessen die einfache rationale Schwelle 1.9e-8 und prüfen
direkt, dass der vollständige obere Ausdruck kleiner als m ist.

## 4. Endliches Restleck mit sämtlichen betroffenen Fehlern

Seien n0 das gespeicherte Modell von J*nu, a0 das vollständige F-J-Modell,
K=K_new, P=P_new_upper und

    H0 = (D0-U0)_JJ-a0*K^-1 a0,
    r0 = n0-H0 w.

Der Modellrest wird gemeinsam gebildet, bevor eine Norm genommen wird.
Die 50-stellige rationale Auswahl von w wird nicht erneut optimiert.
Alle Eingaberadien bleiben erhalten. Die eta-q-Korrektur ist separat
vollständig bezahlt. Der Modellrest ist nicht der tatsächliche Rest.

Für d=a-a0 gilt exakt

    (a*K^-1 a-a0*K^-1 a0)w
      = d*K^-1 a0 w+a0*K^-1 d w+d*K^-1 d w.

Jeder dieser drei Terme gehört zur Fehlergrenze. Definiere

    p_G=tr(P G_J), p_U=tr(P U0_JJ), p_E=tr(P E_JJ),
    r_F=K^-1 a0 w, Z_F=K^-1 a0,
    T_G=tr(P Z_F*G_F Z_F), T_U=tr(P Z_F*U0_FF Z_F),
    T_E=tr(P Z_F*E_FF Z_F).

Aus den gleichen vollständigen bilinearen Feature-Grenzen wie in §2
und Cauchy–Schwarz über die P-gewichteten Spalten folgen die Normpreise

    D_JJ: d_D sqrt(p_G g_J),
    U_JJ: sqrt(p_U e_J)+sqrt(p_E u_J)+sqrt(p_E e_J),
    a_links: d_D sqrt((r_F*G_F r_F)p_G)
             +sqrt((r_F*U0_FF r_F)p_E)
             +sqrt((r_F*E_FF r_F)p_U)+sqrt((r_F*E_FF r_F)p_E),
    a_rechts: d_D sqrt(T_G g_J)
              +sqrt(T_U e_J)+sqrt(T_E u_J)+sqrt(T_E e_J),
    a_quadratisch: d_a sqrt(tr(K^-1 G_F)p_G) e_a.

Dabei ist e_a die schon gebundene obere Norm ||K^-1/2 d w||. Der letzte
Preis folgt aus der Hilbert-Schmidt-Grenze für K^-1/2 d P^1/2. Er benötigt
keine Unabhängigkeit der zwei Kopien von d.

Der nu-Featurefehler wird vollständig aus #246 übernommen. Sein Faktor
sqrt(51/50)>1 bleibt konservativ enthalten. Zusätzlich wird der ganze
physische Residualfehler mit der gebundenen P-Feature-Operatornorm bezahlt.
Für den positiven q-Block gilt aus Cauchy–Schwarz

    ||P^1/2 q_JJ w||² <= tr(P q_JJ) q[Jw].

Das tatsächliche direkte obere Sandwich D96_upper bezahlt beide Faktoren;
der Faktor eta=1e-10 bleibt erhalten. Das ist eine Formpaarung auf J,
keine Behauptung über eine starke Operatordomäne.

Die nach oben eingeschlossenen Normpreise sind ungefähr:

| Beitrag | Normpreis |
| --- | ---: |
| gemeinsamer Modellrest | 1.563e-16 |
| nu-Featurefehler | 3.144e-6 |
| ganzer physischer Quellenfehler | 1.146e-10 |
| direkter JJ-Fehler | 4.363e-7 |
| U-JJ-Fehler | 5.372e-12 |
| a_links | 1.480e-6 |
| a_rechts | 1.472e-6 |
| a_quadratisch | 4.625e-10 |
| eta-q | 1.772e-7 |

Erst nach vollständiger Addition wird quadriert. `FINITE.json` bindet alle
gerichteten Summanden. Es folgt y<6.70878524417e-6 und y²<4.50077994523e-11.
Die ganze L-Dualenergie darf diese endliche Komponente ebenfalls enthalten:
beide Preise sind Bestandteile der bewiesenen Inversmajorante und werden
nicht unter einer unbelegten Orthogonalitätsannahme voneinander abgezogen.

## 5. Genau ein nächster Pilot und Abbruchkriterien

Ziel ist der unveränderte ganze Ausdruck

    r = nu_new-H_new Jw,

direkt aus den gemeinsamen Quellenfunktionen. Er darf nicht durch die
schlecht konditionierte exakte Antwortdarstellung X_ans u=w ersetzt werden.
Die alte verfügbare R-Gramschranke fehlt nicht; sie löst diese neue Aufgabe
jedoch nicht. Benötigt wird eine vollständige gemeinsame Darstellung des
neuen r mit seinen Modellfehlern. 84 Koordinaten allein genügen nicht.

Vor einer großen Integration muss ein begrenzter Darstellungspilot:

1. die gemeinsame Differenz auf allen erforderlichen Prim-/Randzellen
   symbolisch bzw. in gemeinsamen Koeffizienten zusammensetzen;
2. mit den vorhandenen 84 Paarungen abgleichen und die vollständigen
   Modell-, Quellen- und Rundungsfehler in derselben L-Dualmetrik bezahlen;
3. einen endlichen Restanteil und eine vollständige hohe Fehlermajorante
   liefern, ohne einen endlichen Schnitt als obere Norm auszugeben.

Arbeitslimit für diesen ersten Darstellungspiloten: 30 Minuten. Keine
adaptive Auswahl neuer Zeugen. Vor dem Lauf wird dessen Eingabe festgefroren.
Eine gerichtete obere Gesamt-L-Dualenergie <=1.9e-8 wäre ausreichend für
den vollständigen Vergleich **an diesem einen Zeugen**. Das beweist weder
die ganze Grad-11-Regel noch beide Paritäten oder Punkt 4.

Liegt schon ein gerichteter Rest-Unterwert über dem für diese Majorante
zulässigen Arbeitsziel, wird dieser hinreichende Nachweisweg zurückgestellt;
daraus folgt KEIN Ausschluss der tatsächlichen Inversenergie. Eine zu große
Fehlerobergrenze ist ebenfalls kein tatsächlicher Rest-Unterwert. Fehlt eine
bezahlbare vollständige Fehlerdarstellung oder endet das Zeitlimit, wird
genau dieser technische/methodische Blocker berichtet. Keine automatische
Großintegration und keine Nachkommastellenserie.

Der vorliegende Auftrag berechnet die Methode, F-Hülle und endliche
Fehlerkontrolle. Eine vollständige Residualintegration wurde nicht begonnen.

## 6. Reproduzierbarkeit und Grenzen der Prüfung

INPUT_BINDINGS.json bindet den Main-Stand, die geerbten Ergebnis-/Beweisdateien
und das Quellenarchiv. Dateien werden einmal als Bytes gelesen und vor der
Verwendung gehasht; die Archivmitglieder werden nochmals geprüft.
Die alten Zertifikate und 287 Pivots werden als gebundene Voraussetzungen
übernommen, nicht erneut groß gerechnet.

`verify.py` berechnet ausschließlich diesen Pilot mit Arb bei 1024 Bit und
rationalen skalaren Endpunkten. `audit.py` prüft die Endpunktrechnung mit
Standardbibliothek sowie das Residuallemma an einem exakten gekoppelten
Modell einschließlich eines Falls mit verschwindenden J-Koordinaten und
nichtverschwindendem Rest. Dieser Audit ist keine unabhängige Prüfung aller
Arb-Matrixprodukte oder analytischen Voraussetzungen. Der frische Replay
wiederholt nur das neue Paket und seine tatsächlich gelesenen Eingaben.
CI, Merge und externe mathematische Prüfung bleiben getrennt.
