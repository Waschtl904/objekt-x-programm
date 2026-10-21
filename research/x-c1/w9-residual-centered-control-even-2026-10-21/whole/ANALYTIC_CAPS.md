# Analytische Restkontrolle für den festen geraden Zeugen

Autorenherleitung, externe Prüfung offen. a=3 log(2)/2, b=log(3),
B=log(11)/2, s=b-a. Alle geerbten Voraussetzungen bleiben bestehen.
Diese Herleitung gehört zum gemeinsamen Residuum r=nu-H_new Jw. Sie
überträgt keine Norm eines endlichen Koordinatenausschnitts auf die ganze
Funktion. Die Hilbertnorm auf der positiven Halbachse ist 2 int |f|² dx.

## 1. Modell und Fehlerzerlegung

Für p=K_new^-1(a_fin w-v) ist

    r = f_T -(1-eta) q Lambda Jw + q Fp + g* U8(gJw-h-gFp).

Dies folgt durch Einsetzen von nu und H_new in der gebundenen Schurform.
Im Modell werden p0 und die 191 Koeffizienten f0 eingefroren. Der ganze
U8-Ausdruck wird als Funktion dargestellt, nicht als 84 Koordinaten:

    u0 = Phi f0 + delta^-1 [Q0(Jw-Fp0-Phi f0)-h0-alpha m-low].

low ist der niedrige Legendreanteil, alpha die Momentprojektion. Alle
Prim-Schnittstellen werden durch exakte rationale Kombinationen von
log(2),log(3),log(5),log(7),log(11) beschrieben. cut_audit.py vergleicht
diese Liste mit den tatsächlich benutzten Teilintervallen.

Die Änderung p-p0 wird EINMAL als a_fin* (p-p0) bezahlt. Der vollständige
D-normierte Quellentransport aus PROOF §6 kostet höchstens 10. Ebenso
wird der Fehler des niedrigen U8-Features gemeinsam transportiert. Mit

    eta0=sqrt(1-rho) C^-1 f0

vermeidet man eine Abschätzung durch die ungewichtete Norm der fast
singulären Inverse. whole_error_inventory.py benutzt die geerbten
gemeinsamen Quellenfehler E_J,E_F einschließlich der hohen Quellenreste,
die tatsächliche K-Norm des p-Fehlers und den vollständigen physischen
h-Modellfehler. Die Differenz unabhängig eingeschlossener p-Modelle ist
ein eigener Preis (etwa 5.7651e-7 in K-Norm), keine Rundung auf Maschinenpräzision.

Nach Abzug der niedrigen Features verbleibt der rohe hohe Quellenfehler
einschließlich niedriger Projektionsleckage. Für ihn wird der vollständige
Operator g auf X benutzt. Es wird keine nur auf dem hohen Raum geltende
Schranke auf eine niedrige Leckage angewendet.

## 2. Ganze elementare Operatorgrenzen

Der rohe Kern-Schalenoperator ohne Momentlift kostet höchstens

    pi/2 + sqrt(s/a)/2 + 4 sqrt(a s) + 2 sum log(p)/sqrt(n) < 9.023.

Hier stehen der Carlemanoperator, die reflektierte Cauchykopplung, die
beiden regulären Kerne (je Absolutbetrag <2) und alle Primverschiebungen.
Für m(x)=cosh(x/2) liefert die vollständige Q8-Auswertung aus force_control.py
||Q8m||<23.401. Die Norm des Schalenmomentfunktionals ist
sqrt((s+sinh(b)-sinh(a))/4). Somit ist die gesamte rohe g-Norm <13.066;
benutzt wird 100. Diese Grenze enthält den Momentlift und gilt auch für
die niedrige Projektionsleckage.

Die geerbten Gammafehler des Grades 224 werden für g*u0 durch
100 e_Gamma ||u0||, für die direkten Q-Bilder durch
100 e_Gamma (||w||+16||p0||) bezahlt. Der Faktor 100 überdeckt die
Intervalllängen, beide Spiegelbeiträge und Momentliftfaktoren. Die alten
J- und Y-Koordinatenfehler werden mit 100000 multipliziert; die vollständige
Q-Norm auf dem lokalen Grad-95-Raum ist bereits <192, und die vier globalen
Grad-8-Quellen haben kleinere elementare Normpreise. Die alten rohen
Q8Phi-Fehler und niedrigen Gramfehler bleiben zusätzlich im Quellenrest.

Die Grad-160-Momentreihe samt Ableitung kostet <1e-200. Dies folgt auch
rein rational aus a/2<1, exp(a/2)<2 und 2*10^6/160!<1e-200. Ihre
Koeffizientenverstärkungen und die hier auftretenden Normen sind <1e40.
Der gesonderte Quellenrest 1e-150 überdeckt diese Produkte strikt.

## 3. Die qm-Grenzen der Kernquadratur

Die Modellfunktion qm=Q8m wird mit derselben Grad-160-Reihe und dem
gebundenen regulären Gamma-Polynom aufgebaut. Auf |x/a|<=6/5 ist der
absolute Koeffizientenpreis des logarithmusfreien Polynoms <3.106<100
und derjenige von m <1.201<3. Sämtliche benutzten Radius-2-Rechtecke
einschließlich der aktiven Primargumente liegen darin. Für die beiden
Logarithmen ist der Realteil ihrer Argumente positiv; bei Abstand g zum
Rand gilt |log(1 +/- x/a)|<=10+|log g|, einschließlich des Imaginärteils.
Die Primgewichte haben Gesamtsumme <7. Daher gelten die großzügigen Caps

    |qm(x)| <= 1e6 (1+|log g|) auf den komplexen Konturen,
    |qm(a-v)| <= 1000 (1+|log v|) auf der reellen Achse.

Die gerichtete Kernquadratur prüft jede gespeicherte Gaußstelle und ihren
gewichteten h-Wert. Für eine n-Punkt-Regel auf einer glatten Zelle gilt
der konservative analytische Fehler 8*Länge*M*2^(-2n). Für den äußeren
Cauchykern wird dieser Preis als GANZE X-Norm integriert, mit
int_0^s (u+g)^(-2)du <=1/g. Der ausgelassene Kernrand ist für h glatt,
da dessen logarithmischer Rand erst bei b liegt. Eine Taylorabschätzung
auf einem Radius-0.001-Kreis bezahlt ihn. core_quadrature_control_128.py
liefert insgesamt einen äußeren X-Fehler <1e-7 (berechnet etwa 1.385e-8).

Der ursprüngliche 64-Knoten-Modellcache bleibt verwendbar: Die beiden
endlichen Gaußmaße werden durch 128 gemeinsame Momente je Zelle und
einen geometrischen Rest verglichen. Es wird kein bloßer Netzunterschied
zum Quadraturrest erklärt. core_model_bridge.py liefert für die GESAMTE
äußere Funktion einen X-Unterschied <1e-20 (berechnet <3.73e-32).

## 4. Reelle Randhüllen und Norm von u0

endpoint_preflight.py bestimmt Polynom-Suprema über exakte Quadratintegrale
und die Nikolskii-Ungleichung. Die folgenden großzügigen Grenzen gelten:
Phi f0 <1e14; ||p0||<1e7; das lokale Schalenpolynom <1e5;
niedrige Projektion <1; die Gesamtvariation des Kern-Gaußmaßes <1 und
seine Cauchysumme sum |w_i h_i|/(a-x_i)<34.

Für Q8Phi f0 begrenzen H_383<7, das logarithmische Potential, der reguläre
Kernel und die Primoperatoren den Koeffizienten von 1+|log(a-y)| durch
3e15. Die vier globalen Grad-8-Quellen sind im Kern mindestens s>0.05
von ihrem Rand entfernt und kosten zusammen <1e11. Das lokale
Schalenpolynom einschließlich eta Jw kostet dort <1e10(1+|log(a-y)|):
seine Cauchyintegrale werden als Integrale auf ihrer PHYSISCHEN Schale
begrenzt. Es werden keine Monomialsummen außerhalb dieser Schale benutzt.
Momentabzug und niedrige Projektion ergeben deshalb für den gespeicherten
statischen Teil |u_static(y)|<1e18(1+|log(a-y)|).

Die Funktion h hat die Form aus residuals.py. Auf 0<=x<b sind
|ell(x)|<7e15, |quot(x)|<6e14, |Gamma(x)|<18, |D_poly|<7e6,
|D_v|<4e6 und die beiden Momentkoeffizienten <1. Wichtig: Die Kombination
ell(-x)log((B+x)/(b+x))+quot(-x) wird als reflektiertes Integral
int_b^B ell(y)/(x+y)dy begrenzt (<1), nicht durch eine Fortsetzung von ell.
Alle Primargumente von ell liegen auf ihrer physischen Schale, wo
|ell|<100. Die elementaren jp/jm-Terme kosten <100(1+|log(b-x)|).
Daraus folgt |h(x)|<1e17(1+|log(b-x)|), im Kern also <4e17.

Aus 2 int_0^a(1+|log(a-y)|)^2dy<16 folgt damit ||u0||<1e20.
Für x=a+v und t=-log v ist

    int_0^a (1+|log u|)/(v+u) du <= 3+2t+t²/2.

Die reflektierte Kopplung und reguläre Faltung kosten zusammen <14e18.
Die endlich vielen Primargumente haben entweder Randabstand v oder einen
festen Abstand >1e-6; analytic_caps.py prüft diese Alternative. Auf
den ausgelassenen äußeren Randstücken ist t>100. Die Primbeiträge kosten
höchstens 7[1e18(1+t)+4e17]. Das h-Glied kostet 1e17(1+t), die übrigen
Schalen-, globalen Polynom- und Momentglieder zusammen <1e12(1+t).
Dies gilt ebenso bei b-v; dort ist der Kern-Cauchyoperator vom Rand a
entfernt, während die h- und Schalenlogarithmen durch t kontrolliert sind.
Insgesamt ist der Koeffizientenpreis nach t<= (1+t²)/2 kleiner als
3.196e19. Benutzt wird an BEIDEN äußeren Rändern

    |r0(a+v)|, |r0(b-v)| <= 1e20(1+log(v)^2).

Das explizite Quadratintegral über ein Randstück der Länge d ist höchstens
2*1e40*d*(29+28t+14t²+4t³+t⁴), t=-log d. Der Faktor 2 gehört zur
Hilbertnorm; der konstante Term ist 29. Endliche Prim-Sprünge liegen
an den separat behandelten exakten Schnittstellen.

## 5. Gesamter Abschluss, erst nach vollständiger Abschnittsrechnung

Die analytische Taylorrechnung integriert alle glatten äußeren Abschnitte.
Auf jedem Radius-2-Kreis wird die gesamte Funktion eingeschlossen; aus
Cauchys Koeffizientenabschätzung folgt M*2^(1-N) für den Rest. Die
endliche Gaußmaßreihe erhält zusätzlich ihren expliziten geometrischen
Rest. Das Quadrat des Taylorpolynoms wird exakt mit Ballarithmetik
integriert. Keine Stichprobennorm ersetzt diesen Schritt.

Erst wenn ALLE 411 Abschnittsbelege, beide Randhüllen, die Kernquadratur,
der Modellvergleich und das vollständige Quellenfehlerinventar vorliegen,
werden sie mit

    ||r||_Ldual <= sqrt(5/21) [||r0||_X+e_bridge+e_core]+e_operator

verbunden. Hier wird L>=21/5 W_X>=21/5 X verwendet. Ein konservativer
vorgesehener Abnahmewert ist d<=1e-9. Zusammen mit den endlichen Caps
F<=0.000053941654, z<=0.00001 ergibt er einen oberen Vergleichswert
<0.000053950925 und liegt unter der Budgetuntergrenze >0.00005411716936070.
Diese letzte Aussage ist bis zur vollständigen Abschnittsabnahme bedingt.
Ein Bestehen betrifft nur diesen festen geraden Zeugen; Punkt 4 und N12
bleiben auch dann offen.
