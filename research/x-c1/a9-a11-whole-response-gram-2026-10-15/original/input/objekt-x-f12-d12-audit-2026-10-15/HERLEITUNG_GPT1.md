# Objekt X — Ganzfunktions-Gegenprüfung, Momentprojektion und Fehlertransport

15. Oktober 2026. **Bedingte Autorenableitung; externe mathematische Gesamtprüfung offen.**

## 0. Ergebnis und tatsächlicher Prüfumfang

Das Eingangsarchiv `Objekt-X-A9-A11-Ganze-Kraftfunktionen-und-D12-2026-10-15.zip`
mit SHA256

```
0a7bda3d2d896801f757c3b658d9ad559529409c64dd489283e656b95710d3d3
```

besteht im unveränderten frischen Originalreplay. Die drei neuen Ausgaben
`FUNCTIONS12.json`, `FRESH_A12.json` und `IDENTITY_CHECKS.json` sind roh bytegleich.
19 Manifestdateien und sieben Quellenbindungen sind kontrolliert. Das eingebettete
Hauptanteils-Gegenprüfarchiv ist bytegleich mit dem zuvor übermittelten Original
(SHA256 `931176c9b9f42d66fb4debf76cea46e92c2814f2c01ffbf8c53afc17e78aba7b`).

Die neue **getrennte** Rechnung importiert keine arithmetischen Module des
Eingangspakets. Sie verwendet 300-stellige gerichtete Ganzzahlarithmetik,
Rodrigues-Koeffizienten, Euler-/Bernoullizahlen für die Kernelkoeffizienten,
direkte Mellin-Taylorintegration bis Grad 180 und eine andere Eulerkonstanten-
Einschließung (N=1024, 100 statt N=256, 80 Glieder). Das sind unabhängige
Rechenwege für die bezeichneten Eingaben, keine externe Gesamtbegutachtung.

Neu unabhängig geprüft wurden:

- der ganze Grad-320-Kernelpreis und sein Radius 6/5;
- sämtliche 48 ganzen D-/F-Spalten, nicht nur Punktwerte: 8052 D-Polynom-,
  348 D-Log-, 2436 D-Shift-, 7704 F-Polynom- und 348 F-Logkoeffizienten
  sowie die gemeinsamen Momentkoeffizienten und physischen Rieszkorrekturen;
- alle 24 Kappa-Einschließungen (die eigenen Intervalle liegen in den gelieferten);
- alle 288 neuen Formpaarungen und die volle Matrixfehlerordnung;
- alle 24 exakten unteren A12-Pivots;
- die vollständigen Fehlerpreise der gespeicherten Funktionsdarstellungen.

**Ein Zusatz ist für die Anwendung auf W9 nötig:** Die separat gerundeten
D-Spalten sind nicht exakt momentfrei. Alle 24 entsprechenden Momente sind
mit von null getrennten rationalen Intervallen nachgewiesen. Die Daten sind
als Modelle im gesamten Paritäts-L2-Raum korrekt. Vor ihrer Verwendung als
Elemente von H_a muss die exakte orthogonale Momentprojektion mitgeführt
werden. Diese Korrektur vergrößert die nachgewiesenen Funktionsfehler nicht.

Außerdem sind zwei feste rationale Antwortkandidaten und deren direkte
K-Modellfehler konkret zertifiziert. Die gesamte gewichtete Residualenergie,
ein neuer A9→A11-Abschluss und eine neue A11-Inversmajorante bleiben offen.

## 1. Geerbte Form- und Operatorgrundlagen

Es gelten die im Eingang gebundenen Räume, Operatoren und Formdomänen. Mit

a=log(3), b=log(11)/2, X=L²((a,b),2dy),
H_a={u in L²((0,a),2dx): <m,u>=0},

ist m=cosh(x/2) beziehungsweise sinh(x/2). Der volle neue Quelloperator C
enthält Gamma-, sieben Prim- und Momentkorrekturanteile. Als geerbter
Hilbertquellennachweis wird ||C||_(X,W→H_a)<150 benutzt. Dieser Betrag ist
kein behauptetes Schurverlustbudget.

Die 12 exakten alten Quellen Phi gehören zur Operatordomäne von A9. Es gilt
D=A9 Phi, F=Phi* C und A=Phi* A9 Phi. Die bereits gebundene Majorante W9 ist
auf H_a beschränkt und positiv; A9^{-1}≤W9. Die tatsächliche Schranke für
||W9|| wird in diesem Prüflauf NICHT neu berechnet. Ein oberer Boden für
A9^{-1} wäre übrigens nicht automatisch eine obere Schranke für W9.

Die Hintergrundform aus dem vorangehenden Hauptanteilsvergleich bleibt ein
geerbter Baustein. Ihr Rang-eins-Ausgleich +Pi_0/-Pi_0 wird nicht verändert.
Die hier geprüften Funktionsdaten schließen die noch fehlende gemeinsame
kompakte Korrektur nicht.

## 2. Analytische Prüfung der ganzen Funktionen

Die Eingangsformeln in PROOF.txt §§3–4 sind mit den angegebenen Faktoren
schlüssig. Für phi_j=P_j(x/a)/sqrt(2a) gilt

D_j=[Q P_j-kappa_j m]/sqrt(2a),
kappa_j=(mu/a)^{-1} int_0^1 m(at) QP_j(t) dt.

Die neue rohe Kraft ist

f_j(y)=[-P_j(v)log((v+1)/(v-1))/2 + Q_j(v)/2
        -Gamma_out P_j(v)-sum_q w_q P_j(v-log(q)/a)
        -kappa_j m(y)]/sqrt(2a),  v=y/a.

Das Vorzeichen der Primfortsetzung ist bereits durch die Parität von P_j
enthalten. Ein zusätzliches Paritätszeichen wäre falsch. Der ganze
polynomiale Logarithmuskoeffizient bleibt stehen; die Ersetzung durch seinen
Randwert wäre kein gleiches Modell. Der identische Kappa-Faktor in D und F
folgt aus dem alten momentprojizierten Operator, einschließlich des Faktors
1/(2mu) im rohen Adjunkt.

Für die äußere singuläre Wirkung benutzt man exakt

int_-1^1 P(u)/(v-u) du = P(v) log((v+1)/(v-1))
                        -int_-1^1 [P(v)-P(u)]/(v-u) du.

Der Quotient im zweiten Integral ist ein Polynom. Diese Identität folgt
unmittelbar durch Addition und Subtraktion von P(v), nicht aus Punktkontrollen.

Der W-Rieszwechsel lautet exakt

f^W=f-m int_a^b m f/(mu+nu).

Bei getrennt gerundeten Ausgaben gilt diese Beziehung nur bis zu den
bezahlten Rundungsfehlern. Die unabhängige Rechnung bestätigt deren volle
W-Normpreise; sie erklärt die gerundeten Versionen nicht für identisch.

Der Radius 6/5 deckt beide benötigten halben Gammaabstände, a und (a+b)/2.
Die Grenze 11/10 deckt den zweiten nicht. Die analytische Defektmethode
kontrolliert die gesamten unendlichen Reihen. In der unabhängigen Rechnung
werden die endlichen reziproken Koeffizienten über Euler- und Bernoullizahlen
gewonnen; die gesamten Produktdefekte und Reihenreste liefern exakt denselben
rationalen Epsilonwert wie im Original.

Die verwendete Digamma-Restregel ist für positive reelle Argumente durch
NIST DLMF 5.11.2 und 5.11(ii) gedeckt: Betrag des Restes höchstens der erste
ausgelassene Term. Die eigene Kontrollrechnung verwendet andere Parameter.

Quellen für diese Standardidentitäten (keine Quelle der Objekt-X-Positivität):
https://dlmf.nist.gov/5.11#ii
https://dlmf.nist.gov/18.5

## 3. Die notwendige Modellraum-Präzisierung

Sei b_j(t) die gesamte **gespeicherte gerundete** D-Klammer: Polynom,
V-Multiplikator, alle stückweisen Primterme und der gerundete Momentterm.
Definiere

zeta_j=int_0^1 m(at)b_j(t) dt,   M_a=mu/a.

Die unabhängigen Ganzintervallintegrationen zeigen bei ALLEN 24 Spalten
zeta_j != 0. Beispielsweise, nur dezimal zur Orientierung:

- gerade, erste Spalte: zeta ≈6.32992152699·10^-121;
- ungerade, erste Spalte: zeta ≈2.86187248240·10^-121.

Die vollständigen rationalen Intervalle stehen in
`reports/INDEPENDENT_FUNCTIONS.json`. Es handelt sich um Referenzmomente,
nicht um punktweise Funktionsfehler oder um ein neues Residualbudget.

Die Größen sind winzig; die Typfrage ist trotzdem exakt: W9 ist zunächst
nur auf dem alten Momentnullraum H_a definiert. Daher muss man setzen

D_hat=Pi_a D_tilde,
Pi_a u=u-m int_0^a m(x)u(x)dx/mu.

In den vorhandenen Referenzkoordinaten ist das genau

D_hat,j(x)=[b_j(x/a)-alpha_j m(x)]/sqrt(2a),
alpha_j=zeta_j/M_a.

**Alpha bezeichnet diesen exakten Integralwert, nicht den Mittelpunkt seiner
Intervallhülle.** Die auswertbaren Einschließungen stehen im Antwortbudget.
`evaluate_projected_D.py` wertet dieses projektierte Modell gerichtet aus.
Seine Werte sind Modellintervalle, keine punktweisen Intervalle der echten
Wirkungsfunktion. Der tatsächliche Funktionsabstand ist weiterhin global L2.

Weil D im Momentnullraum liegt und Pi_a orthogonal ist,

||D-D_hat||=||Pi_a(D-D_tilde)||≤||D-D_tilde||.

Somit bleiben die ganzen D-Fehlerpreise unverändert gültig. Alternativ darf
man eine Erweiterung W_ext=i W9 Pi_a auf den gesamten Paritätsraum definieren,
mit i:H_a→L² als isometrischer Einbettung. Als Energieform schreibt man
<u,W_ext u>=<Pi_a u,W9 Pi_a u>. Ohne Angabe dieser Erweiterung darf W9 nicht
auf einen beliebigen unprojizierten Modellvektor angewandt werden.

Die 288 A12-Paarungen konnten diese Leckage nicht erkennen: Phi* m=0, also
Phi*(D_tilde+m c*)=Phi*D_tilde für jede endliche Zeile c*. Der neue Momenttest
prüft deshalb eine zusätzliche Eigenschaft, nicht nochmals dieselbe Matrix.
Originaldateien und historische Statusfelder bleiben unverändert. Dieser
Abschnitt ist der nachvollziehbare neue Zusatz zum Modellraum.

## 4. Ergänzung zur vollen A12-Fehlerordnung

Die im Originaltext genannte grobe Schranke ||Phi||<2 allein würde den
Kernelpreis der Paarungsmatrix noch nicht mit dem Faktor 22/5 begründen:
bei Phi* DeltaQ Phi tritt ||Phi||² auf. Die wirklich vorliegende Gramform
liefert aber eine stärkere, hier unabhängig zertifizierte Schranke:

||Phi||² = 1+||c||² <501/500<2.

Genauer liegen die beiden Werte bei
1.001912004638773087... und 1.000168867630409769....
Daraus folgen beide benötigten Aussagen:

||Phi||<1001/1000,
||Phi* DeltaGamma Phi||≤2a eps ||Phi||² < (22/5)eps.

Damit bleibt der gespeicherte ganze A12-Radius gültig; seine Vergrößerung
ist nicht nötig. Die unabhängige gerichtete Integration benutzt sogar
2a eps mal die eigene enge Gramobergrenze. Einschließlich aller Eintragsfehler
liegt sie innerhalb des gelieferten Loewner-Radius. Alle 24 rationalen
Pivots der gelieferten unteren Matrix stimmen exakt überein.

Die neuen Funktionsfehler betragen je Parität ungefähr

delta_D=3.550187016160035·10^-38,
delta_F=2.904698467767301·10^-37.

Die angegebene Veröffentlichungsschranke 10^-35 ist damit bestätigt.
Für Folgepreise werden die vollständigen rationalen, nicht die gerundeten
Dezimalwerte verwendet.

## 5. Ein fester rationaler Antwortkandidat — kein unbezahlter inverser Austausch

Seien L_inv und U_inv die geerbten gerichteten unteren/oberen A12-Inversmatrizen.
Wir fixieren genau die rationalen Matrizen

S=(L_inv+U_inv)/2.

Das ist eine Definition eines Kandidaten. S wird weder mit A12^{-1}
identifiziert noch in wechselnden Kreuztermen als exakte Inverse behandelt.
Für beide S sind je zwölf zusätzliche rationale Positivitätspivots berechnet.
Daher gilt ||S||≤tr S. Die Werte sind etwa

tr S_even=3.615246844214855·10^13,
tr S_odd =3.201268222121450·10^11.

F_hat sei die gelieferte gesamte physische W-Riesz-Modellabbildung. Setze

P=Phi S F_hat,      T=S F_hat.

Dieses P ist wohldefiniert, endlichdimensional und mit Werten in D(A9),
weil seine AUSGABEBASIS Phi weiterhin aus exakten alten Form-/Operatorvektoren
besteht. Seine Koeffizienten dürfen die festen approximativen Kraftmodelle
sein. Insbesondere kostet delta_F im Residuum nicht zusätzlich einen Wechsel
von P zu einer still angenommenen exakten Galerkinlösung.

Aus ||C||<150 und ||Phi||<1.001 folgt ||F_hat||<151 und damit
||T||≤t:=151 tr S. Diese grobe Quellennorm wird nur zum Modellfehlertransport
verwendet, nicht zur vollständigen Schurenergie abgeschätzt.

S ist tatsächlich eine gut zertifizierte Näherung: Mit dem neuen A-Mittelpunkt
M_A und seinem Radius delta_A werden die ganzen Normen von I-A12 S durch

||I-M_A S||_F +delta_A||S||

eingeschlossen. Die erhaltenen Obergrenzen sind etwa 1.28349·10^-24 gerade
und 1.13652·10^-26 ungerade. Daher gilt für den EXAKTEN Residualoperator
R=C-A9P=C-D S F_hat

||Phi*R||<2·10^-22 gerade,  <2·10^-24 ungerade.

Das ist **keine exakte Galerkin-Annihilation**. Abschätzungen, die Phi*R=0
verlangen, dürfen diese Kandidaten nicht ohne Restpreis verwenden.

## 6. Der direkte K-Modellfehler ist jetzt konkret bezahlt

Die vollständige direkte neue Form d[s]=q_b[Lambda s] bleibt hier exakt,
mit allen Moment- und Kreuzanteilen. Wir haben d nicht neu integriert.
Die exakte Schur-Quadratergänzung für das gerade definierte P lautet

K_P=d-F* S F_hat-F_hat* S* F+F_hat* S* A12 S F_hat.

Definiere den berechenbaren endlichen Teil (neben dem unveränderten d)

K_hat=d-F_hat* S F_hat-F_hat* S* F_hat
       +F_hat* S* M_A S F_hat.

Für DeltaF=F-F_hat gilt exakt

K_P-K_hat=-DeltaF* T-T*DeltaF+T*(A12-M_A)T.

Also als GANZE Formordnung auf (X,W)

K_P≥K_hat-e_K I,
e_K=2 delta_F t+delta_A t².

Die exakte rationale Rechnung liefert

e_K,even ≈1.0579887198164425·10^-6 <1.1·10^-6,
e_K,odd  ≈8.295627699226898·10^-11 <9·10^-11.

Das sind neue konkrete Preise für die Modellfehler im DIREKTEN K-Teil des
festgelegten Kandidaten. Sie sind weder eine Berechnung von K_P selbst noch
eine Obergrenze für R*W9R. Unter dem geerbten Hintergrundvergleich mit
B^{-1}≤25I ist die entsprechend normierte K-Fehlernorm höchstens 25 e_K.
Der Rieszwechsel muss dabei derselbe unitäre Wechsel zur rohen Vergleichsnorm
sein, der im Hintergrundbeweis verwendet wird.

Eine stärker gerichtete Alternative ohne den Skalar t benutzt für jedes theta>0

K_P≥K_hat-(delta_A+theta)T*T-(delta_F²/theta)I.

Beweis: 2 Re<DeltaF s,Ts>≤theta||Ts||²+theta^{-1}||DeltaF s||².
Kein nichtkommutierendes Produkt wird dafür vertauscht.

## 7. Fehlende W9-Verstärkung: der genaue gemeinsame Anschluss

Sei D_hat die exakt momentprojizierte Modellspalte aus §3. Definiere

R_hat=C-D_hat S F_hat,
DeltaD=D-D_hat,
R-R_hat=-DeltaD T.

Die Quelle C bleibt hier der ganze exakte Quelloperator; E00 und die
zugehörigen gemeinsamen Energien sind noch nicht berechnet. Eine spätere
Approximation von C benötigt ihr eigenes zusätzliches Budget.

Gesucht wird jetzt eine positive endliche Matrix Q_D mit

DeltaD* W9 DeltaD ≤ Q_D.

Ein neu nachgewiesenes skalares w≥||W9|| würde die hinreichende Wahl
Q_D=w delta_D² I12 erlauben. Eine solche neue Normschranke ist hier aber
NICHT bewiesen. Ein enger gemeinsamer, gerichteter Preis ist vorzuziehen.

Sobald Q_D vorliegt, gilt für jedes alpha>0 auf dem ganzen Schalenraum

R*W9R ≤ (1+alpha) R_hat*W9R_hat
       +(1+1/alpha) F_hat* S* Q_D S F_hat.

Beweis: W9^{1/2}R=W9^{1/2}R_hat-W9^{1/2}DeltaD T; Youngs Ungleichung
wird vor einer skalaren Entkopplung auf den GANZEN Quellvektor angewandt.
Alle Prim-/Gamma- und endlichen Kreuzterme bleiben enthalten.

Falls nur ein skalares w verfügbar gemacht wird, ist separat

||(R-R_hat)*W9(R-R_hat)||≤w delta_D² t².

Der schon aus den neuen Funktionsdaten bestimmte Faktor ist

delta_D² t_even²≈3.75605781634·10^-44 <3.8·10^-44,
delta_D² t_odd² ≈2.94510297487·10^-48 <3.0·10^-48.

Dies sind **Faktoren pro Einheit von w**, keine bereits zertifizierten
W9-Fehlerenergien. Insbesondere wird aus der Kleinheit des Hilbertfehlers
nicht auf die Kleinheit der gewichteten Energie geschlossen.

Ein klarer hinreichender Folgegate lautet schließlich

K_hat -(delta_A+theta)T*T -(delta_F²/theta)I
      -(1+alpha) Gamma_hat
      -(1+1/alpha) T*Q_D T ≥ B_new>0,

wobei Gamma_hat≥R_hat*W9R_hat ein vollständiges gemeinsames Zertifikat sein
muss. B_new und seine brauchbare Inverse sind eigene Ausgaben. Der schon
vorhandene Rang-eins-Ausgleich -Pi_0 und die übrigen kompakten Beiträge dürfen
bei der Rückbindung dieses Gates nicht wegfallen.

Acht zusätzliche exakte Modelle mit nichttrivialer Hilbertmetrik prüfen
die Projektion, ihre Kontraktivitätsidentität und beide gemeinsamen Young-
Identitäten. Diese Modelle ergänzen den obigen analytischen Beweis;
sie beweisen weder die konkreten W9-Energien noch den neuen Horizont.

## 8. Reproduktion, offene Punkte und Einordnung

`verify.py --output <neues Ziel>` prüft die festen Archividentitäten,
entpackt das Eingangsarchiv neu, baut dessen drei Ergebnisdateien frisch auf,
führt die unabhängige Ganzfunktionsrechnung und den Fehlertransport aus und
vergleicht die Ergebnisquittungen. Es verändert kein Original.

Bereits überprüfte ältere Replays wurden in DIESEM Durchlauf nicht nochmals
ausgeführt. Ihre Archive und Quittungen bleiben Herkunftseingaben. Keine
große historische Integration, kein alter 574-Pivot-Lauf und keine neue
vollständige W9-Energie wird als ausgeführt behauptet.

Die nächste sachliche Aufgabe ist die vollständige gemeinsame Energie von
C und den exakt projizierten D-Modellen unter W9, einschließlich Q_D bzw.
einer anderen gültigen Verstärkungskontrolle. Die neue F-Spalte darf als
fester Teil des rationalen Antwortkandidaten eingesetzt werden. Die kleine
Galerkin-Abweichung darf nicht als exakte Orthogonalität benutzt werden.

**Offen:** E00/E10/E11, Gamma_hat, Q_D, der gesamte kompakte Gate,
A9→A11-Schurabschluss, A11-Inversmajorante, Readout-Kompatibilität,
arithmetische Erneuerbarkeit, Kofinalität und Objekt X insgesamt.

**GitHub wurde nicht verändert.** Externe mathematische Gesamtprüfung offen.
