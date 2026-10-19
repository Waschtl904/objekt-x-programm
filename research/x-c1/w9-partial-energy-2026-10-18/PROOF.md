# Gemeinsame W9-Teilenergie auf dem Grad-11-Schalenraum

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Fortsetzung des Inventars #237. Die arithmetische Formidentifikation,
Operator-/Domänenannahmen und die gebundenen alten Quellenzertifikate bleiben
Voraussetzungen. Diese Rechnung ist keine unabhängige Prüfung dieser Herkunft.

## 1. Scope und vorab festgelegte Abnahme

Berechnet werden die vollständige hohe U8-Energie, die endliche U8-Energie,
die Zwölferenergie und der P_upper-Anteil. Der positive R_L-Dualterm wird
**nicht** ersetzt oder gleich null gesetzt: Er fehlt in der Teilenergie.
Eine untere Teilenergie kann zum Ausschluss genügen. Eine obere Grenze der
Teilenergie ist keine obere Grenze der vollständigen W9-Energie.

Verpflichtende Abnahme: Eingabebindungen und unveränderliche Byte-Snapshots;
beide Paritäten; alle zwölf Residuen; alle 191 B-Paarungen, zwölf alten
Quellenpaarungen und 84 Basis-Paarungen; analytische Quadraturreste einschließlich
beider logarithmischer Ränder; separate Regular-Gamma- und Antwortmodellfehler;
gemeinsame Differenzidentität in 1008 Einträgen; Norm-/Cauchy-Kontrollen;
Vergleich mit den gebundenen alten Residualmaps; exakte Gamma-Primitiven als
separate Implementierungskontrolle; Kontrolle der neuen K_P-Implementierung
an den beiden bereits gebundenen alten Richtungszertifikaten;
deterministischer frischer Archiv-Replay;
Registry-Validator, generierte Ansichten und zugehörige Tests. Ein laufender
oder fehlgeschlagener Pflichtcheck ist kein Abnahmeerfolg.

## 2. Gemeinsame Funktionsintegration

Die neuen Schalenpolynome sind die zwölf physisch L2-normierten Legendre-
Polynome auf (a9,a11); ihr W-Gram G_W wird mit den exakten Mellin-Momenten
gebildet. Die feste Antwortmatrix X_fix bleibt unverändert. Die Koeffizienten
T=X_fix Fhat werden zunächst eingeschlossen und für den Integrationslauf als
exakte dyadische Mittelpunkte eingefroren. Ihre Abweichung wird anschließend
als ganzer Funktionsfehler bezahlt. Die Auslöschung in Rhat=C-Dhat T erfolgt
vor jeder Energiebildung.

Für diesen T-Preis wird jede Dhat-Spalte durch die Summe ihrer absoluten
Polynom-/Verschiebungskoeffizienten, zweimal die Summe der V-Koeffizienten
und exp(a9/2) mal den absoluten Momentkoeffizienten abgeschätzt. In der
normierten Variablen t gilt V(t)=−log(1−t²)/2 und
0<=V(t)<=−log(1−t)/2, also ||V||_L2(0,1)<=1/sqrt(2)<2.
Indikatoren der Primstücke vergrößern die benutzte Supremumsmajorante nicht.
Die gemeinsame physische Vorfaktornorm reduziert sich genau auf L2(0,1).

Die alten Kernfunktionen werden aus den gebundenen analytischen Definitionen
rekonstruiert, in der Reihenfolge Q8 Phi (191), Q9 z (4), Q9 Lambda Y (8),
Q9 Lambda J (84). J=Q[D;I84] benutzt die physische alte Geometrie; es ist
keine orthonormale 84er-Basis. Die Nebenbedingung S* [D;I84]=0 wird geprüft.
Sämtliche logarithmischen Faktoren und Prim-Verschiebungen bleiben Funktionen.
Nur die regulären Gamma-Kerne werden durch ihre gebundenen Taylorpolynome
ersetzt; ihre vollständigen Fehler werden separat transportiert.

Für die Funktionsauswertung werden die bereits gebundenen rationalen
Mittelpunkte der lokalen Y-/J-Koeffizienten verwendet. Ihr Abstand zu Q S
bzw. Q[D;I84] wird vor der Monomumrechnung eingeschlossen und ist <10^-60.
Die physische Liftungsnorm beträgt höchstens sqrt(mu9/mu8). Die bare
Paarungsabweichung wird mit dieser Norm bezahlt; für die alte Kernkopplung
wird zusätzlich die geerbte Schranke ||g||<1000 verwendet. Die eingefrorene
Arbeitsbasis wird dadurch nicht als exakt in T liegend ausgegeben.

Die Zellgrenzen werden symbolisch als rationale Kombinationen von log 2,
log 3, log 5, log 7 und log 11 identifiziert. Verschiedene Grenzvektoren
müssen gerichtet strikt geordnet sein. Bloß überlappende Zahlenintervalle
werden nicht als Beweis für identische Schnittstellen verwendet.

Auf jeder glatten Zelle ist die n-Punkt-Gaussregel bis Grad 2n-1 exakt.
Für ein holomorphes F mit |F|<=M auf der Bernstein-Ellipse rho=2 ist der
hier benutzte Restpreis

    |Integral F - Gauss_n F| <= 8 (hi-lo) M 2^(-2n).

Er folgt aus der Chebyshev-Reihe: Der gleichmäßige Rest nach Grad 2n-1
ist höchstens 2 M rho^(-2n)/(1-rho^-1); Integral und positive Gaussregel
haben jeweils Masse hi-lo. Das umschließende komplexe Rechteck wird vor
Verwendung gegen alle logarithmischen Singularitäten geprüft. Polynom-
verschiebungen zum Rand werden vor der Absolutwertbildung ausgeführt.

Die letzten dyadischen Intervalle werden nicht verworfen. Für u>0 und
|f(a-u)|<=A|log u|+B gelten die exakten Majoranten

    Integral_0^d |f| <= d[A(1-log d)+B],
    Integral_0^d |f_i f_j| <= d[A_i A_j(log²d-2log d+2)
        +(A_i B_j+B_i A_j)(1-log d)+B_i B_j].

Alle zwölf Residuen teilen dieselben Momentmatrizen. Alte Quellpolynome
werden erst mit diesen gemeinsamen Momenten multipliziert. Dies ist eine
lineare Umordnung derselben Gaussregel, keine unabhängige Quadratur je Quelle.

Für die alten Y-/J-Quellen wird die analytische Hülle direkt aus dem
Quellenintegral gebildet. Die gespiegelten lokalen Polynome werden hierfür
nicht einzeln extrapoliert. Ist N eine obere Supremumsnorm des eingefrorenen
Schalenpolynoms (aus der Summe seiner 96 normierten Legendrekoeffizienten),
h=a9-a8 und l<=Re x<=u innerhalb des Kerns, so ist der Cauchy-Anteil höchstens

    (N/2) [log((a9-u)/(a8-u))+log((a9+l)/(a8+l))].

Für den regulären Modellkern ist B224=sum |c_k| (11/10)^k eine komplexe
Polynommajorante; der gesamte reguläre Schalenanteil ist <=2h N B224.
Der Radius (a9+|x|)/2<11/10 wird auf jeder Ellipse geprüft. Die
Momentkorrektur und das ganze Primverschiebungspolynom werden hinzugefügt.
Die Identität mit der benutzten Log-Polynomdarstellung gilt zunächst auf
dem reellen Kern und dann durch analytische Fortsetzung im Streifen
|Re x|<a8; die logarithmischen Zweige werden über positive reelle Argumente
festgelegt.
Am Rand liefert dieselbe Integraldarstellung N|log(a8-x)|/2 plus einen
expliziten konstanten Preis. So bleibt auch der vollständige letzte Randrest
kontrolliert. Diese Modellhüllen sind von den separat bezahlten Fehlern des
regulären Kernpolynoms zu unterscheiden.

## 3. Vollständige hohe Paarungen

Für h=Pi8 r und g=Pi8 s seien ell_h=Phi* h, ell_g=Phi* g und
e_h=<e_sigma,U h>, e_g=<e_sigma,U g>. Mit gamma_M=||m||²/|<m,e_sigma>|²:

    <T_h g,T_h h> = <g,h> + gamma_M conjugate(e_g)e_h - ell_g*ell_h.

Die ganze Hilbertpaarung und die e_sigma-Momente werden mitintegriert.
Damit wird kein hoher Legendre-Abbruch als vollständige Projektion ausgegeben.
Die alten niedrigen Modellkoordinaten werden mit ihren Fehlern benutzt.
Insbesondere lautet die hohe U8-Energie

    H_high = (H8 + gamma_M e_h*e_h - ell_h*ell_h)/delta.

Aus B y_h, y_F* y_h und y_J* y_h entstehen die gewichteten endlichen
Features w_h=V8 h/sqrt(1-rho), w_F und w_J. Setze k0=K^-1 a0 mit dem
eingeschlossenen alten a_fin-Modell a0. Der Basisvektor wird gemeinsam gebildet:

    nu0_J = (Lambda J - F k0)* f
      - (y_J-y_F k0)* y_h/delta - (w_J-w_F k0)* w_h.

Dies wird komponentenweise gegen die alternative Formel mit v geprüft.
Die vier Modellenergiegrame sind H_high, w_h*w_h, v*K^-1 v und
(11/10) nu0_J* P_upper nu0_J.

## 4. Neue brauchbare gewichtete Modellschranke

Hier wird ausschließlich die Norm der vier berechneten Features kontrolliert.
G=diag(G_F,G_J) ist die alte gemeinsame 96er-Fehlermetrik. Aus den gebundenen
Featurefehlern bilden wir konservativ E=2 diag(E_F+E_hF/delta,
(e_J²+e_hJ²/delta) I84). Der Faktor zwei deckt unbekannte Kreuzfehler.
Mit dem vollständigen Modellgram U0 folgt

    d_U = 2 sqrt(tr(G^-1 E) tr(G^-1 U0)) + tr(G^-1 E),
    -d_U G <= U_actual-U0 <= d_U G.

Für D0=(D_lower+D_upper)/2 ist
d_D=tr(G^-1(D_upper-D_lower))/2 ein gültiger relativer Preis. Somit
d_a=d_U+d_D und

    |x*(a_fin-a0)y| <= d_a sqrt(x*G_F x) sqrt(y*G_J y).

Die mit „model“ benannten gespeicherten D96-Matrizen enthalten bereits die
beidseitigen direkten Zuschläge: Der gebundene Erzeuger
`refine_old_majorant.py` benutzt die physischen z-Unter-/Obergrenzen und
subtrahiert bzw. addiert den Kreuzpreis sowie 96·10^-25 I. Sie sind somit
unter den geerbten Integrationsvoraussetzungen ein tatsächliches Sandwich.
Die gespeicherten Featurefehler E_F/E_J enthalten bereits einen hohen Anteil;
dessen hier nochmalige Addition ist eine konservative Überdeckung.

Diese gemeinsame Metrik ist wesentlich günstiger als getrennte euklidische
Normen von K^-1 und a_fin. Insbesondere

    ||(K^-1 a_fin-k0) P_upper^(1/2)||_HS
       <= d_a sqrt(tr(K^-1 G_F K^-1) tr(P_upper G_J)) =: d_k.

Für S0=[-k0;I84], U_F^+=U0_FF+d_U G_F gilt

    U_S^+ = [sqrt(tr(P S0*U0 S0)+d_U tr(P S0*G S0))
             +sqrt(tr U_F^+) d_k]².

Unter den geerbten Normen ||F||<16, ||Lambda J||²<1.000502 und der
gerichteten U8-Norm u folgt für die Teilmajorante

    v_* = 16 sqrt(tr K^-1) + sqrt(u tr(K^-1 U_F^+)),
    j_* = sqrt(1.000502 tr P)+16[sqrt(tr(P k0*k0))+d_k]+sqrt(u U_S^+),
    ||W_partial|| <= u+v_*²+(11/10)j_*².

Die tatsächlich berechneten Oberwerte sind kleiner als 2.791e41 gerade und
7.877e37 ungerade. Für den gebundenen ganzen Antwortmodellfehler auf der
W-Einheitssphäre ergeben sich Fehlerenergien unter 1.645e-20 bzw. 6.104e-26.
Dies sind obere Preise für die **Teilenergie**, keine Aussage zur vollständigen
W9-Norm und keine Abschätzung von unten für tatsächliche Modellfehler.

## 5. Weitere Fehler und gerichteter früher Vergleich

Die reguläre Kernelmajorante wird über die Residuen der reziproken
cosh-/sinhc-Reihen bewiesen. Auf der reellen Achse sind beide Nenner >=1.
Der ganze Rest der zugrunde liegenden cosh-/sinhc-Reihen wird geometrisch
mitbezahlt. Die Grade 160/224/360 werden auf |r/2|<=21/20,11/10,6/5
eingeschlossen. Die Kernpolynomkoeffizienten werden gegen die gebundene
alte Gamma-Darstellung identifiziert. Der alte Moment-Taylorrest und sein
erster Ableitungsrest liegen einschließlich des Formoperators unter dem
separat vergebenen Preis 10^-200.

Der B-Paarungsfehler wird zuerst durch C8 transportiert. Alte Quellfehler
werden in den K^-1- bzw. P_upper-Metriken bezahlt. Im P-Block wird die
gemeinsame Quelle g_J-g_F k0 und ihre endliche Wirkung w_J-w_F k0 verwendet.
Der Fehler a_fin-a0 tritt genau einmal auf, angewandt auf das tatsächliche
K^-1 v; dessen bereits kontrollierter Fehler wird eingeschlossen.

Explizit sei L_h=||h||+gamma_M |e_h| und ell=||Phi*h||. Für die
rohen QPhi- und niedrigen A-Modellfehler e_A bzw. e_Alow ist

    e_w = ||C8||_HS (e_A L_h+e_Alow ell)/(delta sqrt(1-rho)).

Seien e_F,e_J die rohen ganzen Quellenfehler, E_LF der niedrige F-Fehlergram,
e_LJ die niedrige J-Fehlernorm, E_F der endliche F-Featurefehlergram und
e_VJ die endliche J-Featurefehlernorm. Die reinen Basisrundungen in den
baren Paarungen heißen e_bF,e_bJ. Dann wird der K^-1-gewichtete Preis

    e_v = e_bF sqrt(tr K^-1)||f||
        + [e_F sqrt(tr K^-1)L_h+sqrt(tr(K^-1 E_LF))ell]/delta
        + sqrt(tr(K^-1 w_F*w_F)) e_w
        + sqrt(tr(K^-1 E_F)) (||w_h||+e_w).

Mit k_P=sqrt(tr(P k0*k0)), w_S=w_J-w_F k0 und

    r_S=e_J sqrt(tr P)+e_F k_P,
    l_S=e_LJ sqrt(tr P)+sqrt(tr(P k0* E_LF k0)),
    s_S=e_VJ sqrt(tr P)+sqrt(tr(P k0* E_F k0))

lautet der P-gewichtete Preis zunächst

    e_nu = (e_bJ sqrt(tr P)+e_bF k_P)||f||
         + (r_S L_h+l_S ell)/delta
         + sqrt(tr(P w_S*w_S))e_w+s_S(||w_h||+e_w).

Genau einmal kommt hinzu

    d_a sqrt(tr(P G_J)) [sqrt((K^-1 v0)*G_F(K^-1 v0))
                         +sqrt(tr(K^-1 G_F))e_v].

Diese letzte Zeile benutzt bereits das tatsächliche v innerhalb seiner
e_v-Hülle. Der Gesamtfeaturefehler ist
sqrt(e_w²+e_v²+(11/10)e_nu²). Die hohe U8-Projektion selbst hat keine
zusätzliche alte Quellenapproximation; ihr Integrationsintervall und der
ganze Residualfunktionsfehler werden getrennt eingeschlossen.

Für eine festgefrorene W-normierte Richtung sei [e_lo,e_hi] die gerichtete
Modellteilenergie, e_features die Norm der direkten Summe aller Featurefehler,
und e_res=sqrt(||W_partial||) mal der ganze verbleibende Hilbertfehler aus
Antwortmodell, neuer Gamma-Funktion und eingefrorenen T-Koeffizienten. Dann

    E_partial_actual >= max(0,sqrt(max(0,e_lo))-e_features-e_res)²,
    E_partial_actual <= (sqrt(e_hi)+e_features+e_res)².

Nur wenn die erste Zahl eine gerichtete K_P-Obergrenze strikt übersteigt,
ist das frühe Ausschlusskriterium erfüllt. Andernfalls ist dieser frühe
Vergleich ohne Ausschluss; der fehlende positive RL-Anteil bleibt offen.
Ein endlicher RL-Galerkinwert wäre seinerseits nur eine Untergrenze.

## 6. Statusgrenzen

Die Ergebnisdateien unterscheiden Quadraturen analytischer Modelle,
vollständig bezahlte Teilenergie und ungerichtete Kandidatenauswahl.
Ein bytegleicher Replay prüft Implementierung und Eingabebindung; er ersetzt
keine externe mathematische Prüfung. Keine Regelbestätigung, kein voller
Energievergleich, kein N12-Abschluss, keine A9->A11-Positivität und keine
Objekt-X- oder RH-Folgerung werden aus einem bloßen Nichtausschluss abgeleitet.

Ein positiver Ausschlussbefund beträfe den **festgelegten W9-Vergleich**.
Aus A9^-1<=W9 und einer zu großen W9-Energie folgt keine negative Richtung
der tatsächlichen Weil-Form. Eine andere Inversmajorante oder ein anderes
Antwortverfahren würde dadurch ebenfalls nicht ausgeschlossen.

## 7. Verworfener Entwicklungslauf

Im ersten Integrationsversuch wurden die alten lokalen Basisintervalle
direkt in Monomkoeffizienten umgerechnet. Die gemeinsamen Abhängigkeiten
gingen durch wiederholte Intervallkopien verloren. Eine Kontrolle nahe dem
alten Kernrand ergab Intervalloberwerte bis etwa 7.8e167 für Funktionswerte
und 4.6e197 für eine komplexe Zellhülle. Diese Größen betreffen die
aufgeblähten Intervalle und haben keine Aussage über tatsächliche Funktionen.
Beide Läufe wurden abgebrochen; es wurde daraus keine Paarungs- oder
Energieergebnisdatei übernommen.

Die Korrektur übernimmt das in der gebundenen alten Funktionsrekonstruktion
bereits verwendete Verfahren: rationale lokale Koeffizienten einfrieren,
ihre Abweichung in der physischen Norm bezahlen und erst dann in Monome
umrechnen. Vor jedem großen Integrationslauf prüfen jetzt 861 Punktkontrollen
die Darstellung. Die gültige gewichtete Normrechnung aus §4 benutzt die
unveränderten gebundenen Gramdaten und ist von diesem verworfenen Lauf unabhängig.

Ein späterer Lauf wurde vor der zweiten Zwischenspeicherung durch eine
nichtendliche Intervallhülle gestoppt. Ursache war die komplexe Boxauswertung
von log((b-x)/(a-x)) auf einer regulären Zelle: Die Zwischenbox des Quotienten
verlor die gemeinsame Abhängigkeit. Die äquivalente Differenz
log(b-x)-log(a-x) benutzt die einzeln in der rechten Halbebene liegenden
Faktoren. Nichtendliche analytische Hüllen werden jetzt unmittelbar vor der
Restberechnung abgewiesen. Der verworfene Lauf liefert keine Ergebnisdatei.

Bei der folgenden Laufzeit- und Restprüfung wurde außerdem eine unbrauchbare
Hülle der gespiegelten Schalenpolynome festgestellt: getrennte Terme bis etwa
10^204 hoben sich erst nach gemeinsamer Auswertung auf. Ihre getrennte
Intervallabschätzung hätte auch den letzten Randrest unbrauchbar gemacht.
Der Lauf wurde ohne Ergebnisübernahme gestoppt. Die direkte Integralmajorante
aus §2 behebt dieses Darstellungsproblem; die großen Zwischenhüllen belegen
keine großen tatsächlichen Fehler.

Zwischenzeitliche Verbindungsabbrüche führten außerdem zur Einführung exakter,
hashgebundener Zellzwischenstände. Diese sind ausschließlich Fortsetzungsdaten;
die Abnahme verlangt weiterhin einen frischen vollständigen Archivlauf.

Die unabhängigen Kontrollen enthalten zwölf direkte alte Schalenintegrale
(je sechs pro Parität, mit Differenzen unter 3.5e-47) sowie vier vollständige
absolute Kernaktionen auf P2, P3, P382 und P383. Der Rest für die letzteren
benutzt auf |r|=3 die Produktabschätzung
|sinh r| >= sin(3) > 1/10 und damit |k_reg(r)|<24. Der Maximumsatz gilt
auch am analytisch hebbaren Ursprung. Diese Kontrollen ersetzen keine der
gemeinsamen Integrationsrestschranken.

## 8. Erster gerichteter Schwellenvergleich: gerade Parität

Die 17-stelligen Dezimalkoeffizienten in `expected/CANDIDATE_even.json`
wurden als exakte rationale Rohkoeffizienten festgefroren. Die Richtung
ist deren Linearkombination, geteilt durch ihre exakte physische W-Norm.
Die Auswahl verglich zwölf numerische verallgemeinerte Eigenrichtungen,
zwei führende Summen/Differenzen, z0 und den bisherigen Kandidaten. Sie
berücksichtigte die untere Teilenergie nach Fehlertransport; ihr K-Modell
war dabei ausdrücklich noch ungerichtet. Erst anschließend wurde K_P
für genau die gespeicherte Richtung vollständig gerichtet berechnet.

Nach außen gerundete Anzeige der exakten rationalen Ergebnisintervalle:

    E_partial in [6.0481910, 6.0713093] · 10^-5,
    K_P       in [5.4117169360, 5.4117169380] · 10^-5.

Insbesondere E_partial,lower-K_P,upper>6.3647·10^-6 und das Verhältnis
der maßgeblichen Endpunkte ist >1.1176103. Der frühe Vergleich ist damit
für diese festgefrorene gerade Richtung **PARTIAL_ENERGY_EXCLUDES_FOR_DIRECTION**.
Es ist kein R_L-Beitrag nötig, um den festgelegten W9-Vergleich auszuschließen.

Die Modellbeiträge betragen ungefähr 2.89698·10^-6 (hohes U8),
8.58865·10^-6 (endliches U8), 4.05558·10^-6 (K-inverser Block) und
4.50562·10^-5 (P_upper-Block). Die ausgewiesene Teilenergie enthält diese
vier Beiträge. Der K-inverse Modellblock enthält bereits einen Intervallradius
von etwa 6.14·10^-8 aus Integration und Arithmetik. Zusätzlich beträgt der
gewichtete P-Featurefehler <3.485·10^-6, überwiegend aus dem gemeinsamen
a_fin-Preis; der ganze Residualmodellpreis in Featurenorm ist <1.283·10^-10.
Diese verschiedenen Preise werden gemäß §5 kombiniert, nicht verwechselt
oder als zwei unabhängige Kopien desselben Integrationsrests addiert.

Der bisherige gerade Kandidat bleibt davon getrennt: Seine Teilenergie
liegt in [0.000140526,0.000140822], während sein tatsächliches K_P-Intervall
nahe 0.00021340011455 liegt. Für ihn liegt die Teilenergie vollständig
unter dem tatsächlichen Budget. Der fehlende R_L-Term bleibt auch dort offen.

## 9. Separates tatsächliches K_P der festgefrorenen Richtung

`certify_k.py` übernimmt die analytische Autokorrelationszerlegung aus dem
gebundenen Paket `sharp-kp-frozen-directions-2026-10-17`, §§2–5, und wertet
sie für die neuen rationalen Koeffizienten neu aus. Mit a=log3, b=log11/2,
ε=±1, m=cosh(·/2) bzw. sinh(·/2), μ=(εa+sinh a)/2 wird der exakt
W-normierte Schalenpolynomlift u gebildet. Auf dem Kern ist u=A_c m,
A_c=−(Integral_a^b s m)/μ; auf den beiden Schalen steht s mit der
festgelegten Paritätsfortsetzung. Die gerichtete Normkontrolle verlangt
C(0)=||u||²=1 innerhalb des berechneten Intervalls.

Alle neun Stücküberlappungen für C(r)=Integral u(x)u(x+r) dx werden exakt
als Polynom-/Exponentialstammfunktionen ausgewertet. Die Zweige wechseln
nur bei b−a, 2a, a+b und 2b. Strikte Intervallvergleiche entscheiden den
jeweiligen Zweig; am Primkanal log9=2a wird die stetige rechte Formel benutzt.
Für A=||u'_stückweise||² und die Summe J der vier Sprungquadrate gilt auf
0<r<t=(b−a)2^-48 die Translationsschranke

    ||u(·+r)−u|| <= r sqrt(A)+sqrt(rJ).

Mit k(r)=exp(−r/2)/(1−exp(−2r))<=1+1/(2r) folgt der vollständige
Nahbereichspreis

    E_near <= A(t³/3+t²/4)
        +2 sqrt(AJ)(2t^(5/2)/5+t^(3/2)/3)+J(t²/2+t/2).

Auf [t,2b] werden die 55 glatten Zellen mit 128 Gaussknoten und dem
analytischen Rest aus §2 integriert. Die komplexen Zellrechtecke liegen
strikt in Re r>0; die festgelegte Korrelationsformel ist dort ganz.
Für r>=2b gilt C(r)=0, sodass der ganze Fernrest exakt
2[atanh(exp(−b))+atan(exp(−b))] beträgt. Alle sieben Primkanäle
2,3,4,5,7,8,9 werden mit ihren Vorzeichen bezahlt. Damit

    d[s] = Integral_0^infinity 2k(r)(1−C(r)) dr
           −log(8π)−EulerGamma−π/2
           −2 sum_q log(prime(q))/sqrt(q) C(log q).

Die symmetrische Matrix S0=X_fix+X_fix*−X_fix* A12_model X_fix wird aus
den gebundenen rationalen Matrizen mit `Fraction` exakt gebildet. Der
gerichtete Fhat-Vektor wird aus den gemeinsamen Paarungsdaten übernommen.
Das volle Intervall entsteht als

    K_P[s] in d[s]−(Fhat s)*S0(Fhat s)+[−E_K,E_K],

wobei E_K der gebundene Fehler der festen Antwortregel auf der W-Einheitssphäre
ist. Er wird zweiseitig und genau einmal addiert. Der neue Rechenweg wird
zusätzlich an den beiden bisherigen Richtungen gegen deren unabhängig
gebundene K_P-Intervalle geprüft. Diese Kontrolle ersetzt keinen Restterm.

## 10. Ungerade Parität und gemeinsamer Entscheidungsstand

Nach Abschluss derselben gemeinsamen Integration und sämtlicher Kontrollen
wurde separat auch die ungerade Richtung ausgewählt und eingefroren. Die
anschließende gerichtete K_P-Rechnung liefert nach äußerer Anzeigerundung:

    E_partial in [5.3963217, 5.3979761] · 10^-6,
    K_P       in [5.2807764351, 5.2807764506] · 10^-6.

Die Differenz der maßgeblichen exakten Endpunkte ist >1.15545·10^-7,
ihr Verhältnis >1.0218803. Auch diese Richtung erfüllt daher
**PARTIAL_ENERGY_EXCLUDES_FOR_DIRECTION**. Das reine numerische
Mittelpunktmaximum 1.02203694 bleibt hiervon getrennt; ein gerichtetes
Maximum über den ganzen Raum wird nicht behauptet.

Die vier Modellbeiträge sind ungefähr 8.39329·10^-8 (hohes U8),
1.98101·10^-6 (endliches U8), 9.90636·10^-7 (K-inverser Block) und
2.34157·10^-6 (P_upper-Block). Der gewichtete P-Featurefehler ist
<1.389·10^-9. Der alte ungerade Kandidat ist ebenfalls getrennt ausgewertet:
Seine Teilenergie liegt in [3.4721367,3.4721396], unter dem tatsächlichen
alten K_P nahe 3.91114616. Dieser alte Nichtausschluss der Teilenergie
ändert nichts am neuen, für eine andere Richtung gewonnenen Ausschluss.

Beide Paritäten bestehen die 1008 gemeinsamen nu-Identitäten und die
1152 hohen F-/J-Cauchy-Kontrollen sowie die B-Kontrollen, alten Residualmaps
und die unabhängige z0-I0-Rekonstruktion. Beide alten K_P-Intervalle werden
vom neuen Implementierungsweg überlappt. Der verpflichtende vollständige
Replay vergleicht zusätzlich sämtliche veröffentlichten Ergebnisbytes.

Der Negativstatus `AUTHOR_DERIVED_NO_GO` in META bezieht sich ausschließlich
auf die **feste W9-Vergleichsbedingung mit der eingefrorenen Antwortmatrix**.
Der Beitrag bleibt im Register `PENDING_STATUS_REVIEW` und extern ungeprüft.
Keine numerische Bestimmung des fehlenden R_L-Werts, keine vollständige
Energieobergrenze und keine Negativrichtung der tatsächlichen Weil-Form
werden daraus abgeleitet. Alternative Majoranten und Antwortregeln sowie
der weitere N12-Ansatz bleiben offen.
