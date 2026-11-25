# Gemeinsamer Test in beiden Paritäten

**Autorenbefund für Punkt 4 im Horizontschritt \(A_9\to A_{11}\).** Unter den dokumentierten physischen Form-, Quellen- und Domänenverträgen ist die vollständige Residualungleichung mit einer neuen gemeinsamen alten Inversmajorante bestanden. In beiden Paritäten gilt \(K_P-R^*UR\succeq 10^{-44}W\). Eine unmittelbar auf beliebige physische Hilbertquellen anwendbare Ausgabe ist \(A_{11}^{-1}\preceq10^{44}I_{\rm phys}\). Die externe Begutachtung und die formale Übernahme ins Forschungsregister stehen aus. [Endpunkte](ABSCHLUSS.json) · [Herkunft und Zertifikatszustand](ZERTIFIKAT.json)

Die folgende Kalibrierungsvariante verwendet eine andere alte Majorante als der ungerade Zweiraumbeweis. Sie prüft die ganze Residualungleichung als eine gemeinsame Form in einer anderen Zerlegung. Der alte Rohgenerator ist der A8-Rechenstand vom 27. September. Es werden keine A11-Vorzeichen, Spektraldaten, alten A11-Modelldateien oder Inversen des Zieloperators eingelesen.

## Vor der Abnahme festgelegte Regel

Alte Untergrenze \(\alpha=10^{-207}\) in physischem \(L^2\), festes \(P=\Phi_{12}X\widehat F\) aus dem N12-Vertrag in beiden Paritäten, \(R=C-A_9P\) als tatsächliche Hilbertquelle. Setze \(\epsilon=\beta=10^{-250}\), \(U=(A_9-\epsilon I)^{-1}\), \(b[z]=\beta W[z]\), \(V=\beta^{-1}I\) im physischen Schalenraum. Die alte Ordnung \(A_9^{-1}\preceq U\), die Positivität und \(\|U\|\le 2\,10^{207}\) folgen bereits aus dem alten Zertifikat. Eine konstruktive Darstellung steht unten.

Für \(f=J(x,z)=x+\Lambda z\) mit physischem Momentlift ist \(J\) unitär aus \(H_9\oplus(X,W)\): Der alte Teil des Lifts liegt in der alten Momentrichtung, \(x\) ist dazu orthogonal. Aus der quadratischen Ergänzung mit \(y=x+Pz\) erhält man die **eine** zu prüfende Form
\[
  \mathcal B(f)=q_{\rm roh}(f)-\epsilon\|x+Pz\|^2-\beta W[z]
   =\langle y,(A_9-\epsilon I)y\rangle+
      2\operatorname{Re}\langle y,Rz\rangle+K_P[z]-\beta W[z] .
\]
Die erste Paarung ist eine Formpaarung. Beide Seiten sind auf den geerbten vollständigen Domänen identisch, inklusive der sieben aktiven Primtranslationen. Ein Nachweis \(\mathcal B\ge0\) liefert durch Infimum über alle \(y\) genau \(K_P-R^*UR\ge\beta W\). Das Infimum wird bei \(y=-URz\) angenommen. Diese Bilanz erlaubt den Wechsel der Testkoordinaten **vor** der Minimisierung. Sie ist für die hier festgelegte Majorante notwendig und hinreichend.

Der Rechenlauf geht vom Doppelintegral mit den beiden abgezogenen Fehlerformen aus. In den ganzen momentverträglichen Legendrekoordinaten \(f=M(l+h)\) ist die Summe der beiden absichtlich eingeführten Preise höchstens \(10^{-211}(\|l\|^2+\|h\|^2)\), da \(\|M\|\le2\), \(\|P\|<10^{19}\). Für letztere Schranke genügen \(\|\Phi\|<20,\ \|X\|<5\,10^{13},\ \|\widehat F\|\le 150\|\Phi\|+1\). Der Lauf muss den ganzen Kreuzblock und den unendlichen hohen Anteil der verbleibenden Form bezahlen.

## Vollständige Integration

Die A8-Engine wird auf das Intervall \(b=\log(11)/2\), den rationalen Gammaradius \(6/5\) und die Kanäle \(2,3,4,5,7,8,9\) spezialisiert. Die Reihenfolge aller Translationszellen wird durch Arb-Kugeln geprüft. Der Kontakt \(q=11\) ist eine Nullmenge. Die niedrigen Grade enden bei 383. Nach Entfernung des Momentträgers bleiben je Parität 191 freie niedrige Koordinaten. Grad 160 ist die Approximation des regulären Gammakerns, 2304 Bit die Arbeitspräzision bei der Integration. Die bisherige A8-Formidentität \(Q=D_H+V_0+q_0-K-S\), \(V_0=-\log(1-t^2)/2\), wird mit dem neuen Horizont und den neuen Verschiebungen ausgewertet. Die endlichen Formmatrizen und die Grams der Kopplung in den **ganzen** rohen hohen Raum werden neu berechnet. Das vollständige Integral für \((V_0-S)^2\) umfasst sämtliche Translationszellen und beide Kreuzterme mit dem logarithmischen Potential. Nur vom vollständigen Gram wird die endliche niedrige Projektion abgezogen. Die Gamma-Modellspalten haben endlichen Grad. Das Integral umfasst auch ihre gemischten Grams mit \(V_0-S\). Der uniforme Kernfehler ist durch die unten hergeleitete rationale Chebyshev-Restschranke gedeckt.

Für den ganzen hohen Raum vor Momentkorrektur benutze auf \(t\in[0,1]\) ein positives, gerade fortgesetztes, stückweise konstantes Schurgewicht \(w(t)\). Die gewichtete Ungleichung \(2|uv|\le |u|^2 w(v)/w(u)+|v|^2 w(u)/w(v)\), mit den Gewichten an den beiden Translationspunkten, liefert
\[
 S-V_0\preceq \sup_t\left(\sum_{q,\pm}\frac{\log p}{\sqrt q}
 {\bf1}_{|t\pm d_q|<1}\,\frac{w(|t\pm d_q|)}{w(t)}-V_0(t)\right) I.
\]
Das Gitter hat 512 Zellen. Im Prüfer wird je Zelle und Translation der größte rationale Gewichtswert über sämtliche getroffenen Zielzellen verwendet. Die Gewichtssuche dient nur der Auswahl; der anschließende Vergleich prüft die ganze kontinuierliche Ungleichung. Es ergibt sich ein Verlust kleiner als 2.319. Die Gamma-Hochkopplung kostet unter 0.0024: Die reguläre Kernelableitung hat für \(0\le v/2\le6/5\) Betrag höchstens \(3/8\) nach der alten hyperbolischen Ableitungsschranke (\(\cosh(6/5)<2\)). Die Legendre-Differentialgleichung gibt \(2b^2(3/8)\sqrt{2/(3N(N+1))}\) für \(N=384\). Der alte Beweis verwendet die Hilbert-Schmidt-Norm der gewichteten ersten Ableitung. Somit beträgt der rohe Hochboden mehr als 1.611. Der hohe Mellinkoeffizient hat Norm unter \(10^{-800}\), durch die Taylorprojektion der beiden Momente. Mit \(\|Qe_p\|<100\) kosten der Trägerwechsel und die obige dicht beschränkte Preisform zusammen weniger als 0.001. Die Trägerschranke folgt unmittelbar aus \(p=0,1\), \(\|V_0\|_{L^2(dt/2)}<2\), den endlichen Verschiebungen und dem beschränkten regulären Kern. Es verbleibt der Nenner 1.61.

Schreibe \(L_0\) für die neu integrierte niedrige Matrix, \(G_0=B_0B_0^*\) für den vollständigen Modellgram, \(e_K=(12/5)\,e_{\rm Kern}\), \(e_B=2e_K+200e_m\). Die niedrige Momentkarte hat Norm höchstens 2, die hohe Momentkorrektur Norm höchstens \(e_m\). Deshalb ist die tatsächliche niedrige Untergrenze \(L_0-4e_KI-10^{-211}I\), und der tatsächliche Kreuzgram ist höchstens \((1+p)G_0+(1+1/p)e_B^2 I\), \(p=10^{-12}\). Von der niedrigen Matrix wird die Grammajorante geteilt durch 1.61 abgezogen. Die vollständige endgültige Abnahme verwendet die beiden Kongruenztests im folgenden Abschnitt.

### Uniformer Gammafehler und zwei gerichtete Matrixprüfungen

Die endgültige Approximation verwendet \(z=v/2\) und \(k_{\rm reg}(v)=[\operatorname{sech}z+\operatorname{csch}z-1/z]/4\), am Ursprung stetig fortgesetzt. Ein Taylorpolynom um null unmittelbar bei Grad 160 abzuschneiden kostet auf diesem Intervall bis zu \(4.14\,10^{-20}\) in der verwendeten Fehlerrechnung. Der erste Lauf mit diesem Preis scheiterte bereits an Pivot 17 (gerade) und 18 (ungerade).

In der erfolgreichen Rechnung werden die beiden reziproken Potenzreihen zunächst rational bis zum benötigten Index für Grad 640 entwickelt. Auf \(|z|=1.55\) ist der kombinierte Kern betragsmäßig kleiner als 16. Denn \(|\cosh z|\ge\cos(1.55)>0.02\) und \(|\sinh z|>0.3\), letzteres durch Trennung bei \(|\operatorname{Re}z|=0.3\). Der analytische Rest auf \([0,1.2]\) ist also höchstens \(16(24/31)^{641}/(1-24/31)\). Für \(z=(6/5)(1+t)/2\) gilt
\[
 z^k=(3/10)^k\left[{2k\choose k}+2\sum_{j=1}^k {2k\choose k-j} T_j(t)\right].
\]
Die Terme oberhalb Chebyshevgrad 160 werden mit ihrer vollständigen Binomialsumme nach oben bezahlt. Ab \(j=161\) ist das Verhältnis benachbarter Binomialbeträge höchstens \((k-161)/(k+162)\). Die übrigen Koeffizienten werden mit gerichtet bezahltem Fehler auf ein Gitter \(10^{-162}\) gebracht. Wegen \(|T_j|\le1\) addieren sich alle Preisgrenzen. Die Rückumwandlung in ein gewöhnliches Polynom ist exakt. Der endgültige uniforme Fehler ist kleiner als \(4.01\,10^{-70}\). In der Formel für \(e_K\) steht in diesem Lauf genau diese neue gerichtete Kerngrenze.

Zur Matrixprüfung berechnet der Code eine punktweise invertierbare untere Dreiecksmatrix \(X_0\) aus einer ungeprüften numerischen Choleskynäherung. Die Abnahme erfolgt an der ursprünglichen Intervallmatrix \(F\). Erstens wird \(X_0FX_0^*\) in Intervallarithmetik als strikt diagonaldominant mit positiven Diagonalen geprüft. Zweitens bildet der Prüfer eine rationale Untergrenze \(F_{\mathbb Z}/D\) mit \(D=10^{85}\). Der Koeffizientenfehler des symmetrisch gewählten Ganzzahlnenners beträgt in Einheiten \(1/D\) pro Eintrag weniger als zwei, \(2n/D\) wird daher von der Diagonalen abgezogen. Die rationalisierte Dreiecksmatrix \(S\) hat strikt positive Ganzzahldiagonale. Die gesamte Kongruenz \(C=S F_{\mathbb Z}S^*\) und ihre kleinste Gershgorinreserve \(m\) werden mit ganzen Zahlen gebildet. Somit \(F\succeq m/(D\|S\|_{\rm F}^2) I\). Die Positivität hängt von keiner numerischen Eigenwertausgabe ab.

Sei \(g_F\) diese letzte rationale Untergrenze und \(r\) eine ganze Zahl oberhalb der Quadratwurzel der Spur der vollständigen Kreuzgrammajorante. Für den gesamten physischen Test gilt nach der quadratischen Ergänzung im Hochblock
\[
 \mathcal B(f)\ \ge\
 \frac{\min(g_F,1.61)}{4(1+r/1.61)^2}\,\|f\|^2 .
\]
Der Faktor 4 bezahlt die volle Momentkarte. Die Frobeniusnorm der inversen gescherten Koordinaten wird hier nicht benötigt: Die Operatornorm der inversen Scherung ist höchstens \(1+\|B_{\rm Kreuz}\|/1.61\). [Gerichtete Endpunkte](ABSCHLUSS.json)

## Der alte Inversoperator ist auswertbar

Eine explizite Reihe verwendet ausschließlich alte Daten. In den trägerfreien alten Legendrekoordinaten sei \(D=\operatorname{diag}(1+H_n)\), \(M\) die alte Momentkarte und
\[
  B=D^{-1/2}M^*(A_9-\epsilon I)M D^{-1/2}.
\]
Diese Definition ist eine beschränkte Form auf \(\ell^2\). Für das Nachrechnen der Kondition genügen \(\lambda=10^{-210}\) und \(256\) als untere und obere Schranke. Tatsächlich kontrolliert die alte rohe Form \(D_H-12I\), da \(V_0\ge0\) und die gesamte beschränkte Gamma-/Primwirkung samt Konstante weniger als 12 kostet. Mit der alten physischen Untergrenze und einer konvexen Kombination folgt \(A_9-\epsilon I\succeq\lambda(1+D_H)\) auf dem Momentraum. Die Trägerkorrektur kann diese gewichtete Norm nur erhöhen. Für die andere Richtung ist in orthonormaler Basis der Betrag eines nichtdiagonalen Potentialeintrags bei gleicher Parität \(\sqrt{(2n+1)(2j+1)}/(|n-j|(n+j+1))\). Die Diagonale ist kleiner als 3. Der Schurtest mit Gewichten \(1/\sqrt{2j+1}\) kostet für \(j<n\) höchstens \(2H_n\), für \(j>n\) höchstens \(H_{2n+1}\) durch Teleskopieren von \(1/k-1/(k+2n+1)\). Also \(V_0\preceq6I+3D_H\). Der übrige beschränkte Anteil kostet unter 12. Die Momentkarte erfüllt \(\|D_{\rm voll}^{1/2}M D^{-1/2}\|^2<9\), da nur eine Koordinate in Grad \(p=0,1\) hinzukommt und die volle ungewichtete Momentkarte Norm kleiner als 2 hat. Das ergibt \(B\preceq 256 I\). Die Formdomäne entspricht genau dieser gewichteten Legendre-Domäne: für Polynome folgen beide Richtungen aus den genannten Schranken, und das Potential ist auf der harmonischen Formdomäne stetig. Momentkorrektur und Abschneiden der freien Grade liefern eine dichte Formbasis.

Damit gilt im physischen alten Hilbertraum die normkonvergente Reihe
\[
 U=M D^{-1/2}\frac1{256}\sum_{k=0}^\infty(I-B/256)^kD^{-1/2}M^* .
\]
Nach \(k=0,\ldots,m\) beträgt der Operatorrest höchstens \(4\lambda^{-1}(1-\lambda/256)^{m+1}\). Jeder Faktor lässt sich auf einem endlich gestützten Argument gerichtet anwenden: der physische Eingangsvektor ist ein bekanntes Polynom, seine alte Formwirkung eine Hilbertfunktion mit expliziten Logarithmen, regulärem Kern und endlich vielen verschobenen Polynomen. Nach Anwendung von \(D^{-1/2}\) kostet das Abschneiden ab \(K\) höchstens \(\|M^*r\|/\sqrt{1+H_K}\), \(r\) die alte Hilbertwirkung. Die Norm von \(r\) ist aus dem Polynom, seiner Ableitung, der quadratintegrierbaren Randlogfunktion und den beschränkten übrigen Termen nach oben auswertbar. Endliche Momente werden über die alten rohen Integrale eingeschlossen. Beliebige Hilbertquellen mit L²-Näherungen können zuerst mit ihrem angegebenen Fehler approximiert werden. Fehler einer Faktorenanwendung addieren sich wegen der Kontraktion des normierten Iterationsfaktors. Damit ist insbesondere keine Kenntnis eines alten Eigenvektors erforderlich. Die Schranke ist absichtlich sehr grob.

Für eine berechenbare alte Quelle \(g\) liefert jeder alte Polynomtest \(u\) auch eine a-posteriori-Energieeinschließung. Mit \(a'=a_9-\epsilon\|\cdot\|^2\) und \(r=g-(A_9-\epsilon I)u\) ist \(2\operatorname{Re}\langle g,u\rangle-a'[u]\) die untere Grenze. Als oberen Zusatz genügen \(\lambda^{-1}\|D^{-1/2}M^*r\|^2\) oder \((2\,10^{207})\|r\|^2\). Dies folgt aus derselben vollständigen inversen Variationsidentität. Die Normreihenschranke garantiert einen allgemeinen Weg auch ohne geeigneten Starttest.

## Physische Inversausgabe und nächste Quellen

Setze \(H=P+UR\). Die physische Ausgabe des Inverslemmas ist \(J\,T^{-1}\operatorname{diag}(U,10^{250}I)T^{-*}J^*\), \(T(x,z)=(x+Hz,z)\). Ihr Energiewert zu einer physischen Quelle mit Koordinaten \((g_0,g_1)=J^*g\) ist \(\langle g_0,Ug_0\rangle+10^{250}\|g_1-H^*g_0\|_W^2\). Weiter unten folgt eine unmittelbar auswertbare Skalarmajorante aus dem physischen Boden. Der eigentliche Readout ist exakt
\[
 q[f]=\epsilon\|y\|^2+\|(A_9-\epsilon I)^{1/2}(y+URz)\|^2+
        \beta W[z]+(K_P[z]-\langle Rz,URz\rangle-\beta W[z]).
\]
Die Restklammer wird durch den gemeinsamen Test auf Positivität kontrolliert. Domäne, beide Mellinbedingungen und der arithmetische Wert sind diejenigen der ursprünglichen Prim-/Gamma-Form. Für alte Quellen ist die physische Nullfortsetzung das isometrische Intertwining der Formwerte. Der zusätzliche Primkanal hat auf zwei alten Trägern nur Nullüberlappung; die Gammaform ist dieselbe. Die Inklusionen komponieren sich identisch, auch über mehrere Schritte. Für die beiden getrennten Rohcarrier gelten die Multiplikator-Intertwinings des allgemeinen Ein-Wand-Lemmas, §§4–5. Hier wird keine Gleichheit zwischen physischer Inverse und berechneter Majorante transportiert.

Die rationale Untergrenze für \(\mathcal B\) beträgt gerade mehr als \(3.9333\,10^{-44}\), ungerade mehr als \(5.1592\,10^{-41}\). Zum einen gilt \(q_{\rm roh}\ge\mathcal B\). Daher ist **\(U_{11}=10^{44}I_{\rm phys}\)** eine explizite gemeinsame Inversmajorante. Zum anderen gilt \(\|J(x,z)\|^2\ge W[z]\) bei beliebigem alten \(x\). Das Infimum der **bereits penalisierten** Form über \(x\) liefert also \(K_P-R^*UR\succeq 10^{-44}W\). Als verbesserte Schalenvergleichsform und ihre Inverse können \(10^{-44}W\) und \(10^{44}I_W\) gewählt werden. Auch in der Blockausgabe des Fortsetzungslemmas darf daher \(10^{250}\) durch \(10^{44}\) ersetzt werden. Die einfache physische Skalarmajorante folgt unmittelbar aus dem vollständigen physischen Boden. Eine Ordnung der beiden verschiedenen Inversmajoranten untereinander wird hierfür nicht benötigt.

Eine isometrische Form des exakten Readouts verwendet die vier Komponenten \(\sqrt\epsilon\, y,\ (A_9-\epsilon I)^{1/2}(x+Hz),\ \sqrt\beta z,\ [z]_{\mathfrak S-\beta W}\). Die letzte Komponente ist die kanonische Abbildung in die Vervollständigung für die positive Restform. Die Quadratsumme ist die tatsächliche Form, einschließlich ihrer Mischterme durch Polarisation. Bei physischer Nullfortsetzung \(z=0\) sind die letzten beiden Komponenten null, die ersten beiden sind genau der alte Readout \((\sqrt\epsilon\,x,(A_9-\epsilon I)^{1/2}x)\). Für einen bereits gegebenen isometrischen alten Formreadout ist die Zuordnung auf dem dichten Quellenbild eindeutig und setzt sich isometrisch auf dessen Abschluss fort. Die Koordinaten zur physischen Nullfortsetzung und deren Zusammensetzung stimmen dort auf sämtlichen Quellen überein. Das konstruiert die Verträglichkeit für den vorliegenden Horizontschritt.

Auf nächsten physischen Hilbertquellen \(f,g\) ist die Energie \(10^{44}\langle f,g\rangle\). Für Näherungen \(\tilde f,\tilde g\) mit ganzen \(L^2\)-Fehlern \(e_f,e_g\) kostet der gemischte Fehler höchstens
\[
 10^{44}(e_f\|\tilde g\|+e_g\|\tilde f\|+e_f e_g).
\]
Der Prüfer schnittstelle.py verwendet exakte Brüche mit nach oben gerundeten Normen. In einer gemeinsamen orthonormalen physischen Basis lassen sich Koeffizientenschwänze und Quellenfehler in diesen Radien aufnehmen. Für komplexe Daten wird der bilineare reelle Prüfer auf die vier Real-/Imaginärpaarungen angewandt.

Ein konkreter Anschluss für \(A_{11}\to A_{13}\) ist die physische Quelle des nächsten Momentlifts. Für rechtes Schalenpolynom \(z\) ist sie die orthogonale Momentprojektion der Summe aus Gamma-/Primkontakt mit \(z\) und \(-\lambda(z)Q_b m/\mu_b\). Beide Paritäten verwenden ihre jeweiligen \(m\). Endliche Primtranslationen sind auf den expliziten Schnittzellen Polynome. Für den Gammakontakt wird auf dem alten Flügel bis \(b-\eta\) die Exponentialreihe nach \(J\) Summanden mit Kernrest höchstens \(e^{-(2J+1/2)\eta}/(1-e^{-2\eta})\) ausgewertet. Auf dem Streifen \(b-\eta<t<b\), \(0<\eta<0.01\), ergibt \(k(v)=1/(2v)+k_{\rm reg}(v)\) mit \(|k_{\rm reg}|<1\) eine punktweise Schranke \(10\|z\|_\infty(1+|\log(b-t)|)\) für die Gammakontaktwirkung. Der Normfehler ist dort höchstens \(10\|z\|_\infty\sqrt{2\eta((\log\eta)^2-4\log\eta+5)}\) einschließlich des Maßes. Der alte Momentterm besitzt die gleiche explizite Randlogklasse mit glattem Profil, und die reine Momentprojektion ist kontraktiv. Für allgemeine Quellen wird zuerst \(z\) in \(W\) durch Polynome angenähert. Der Fehlertransport ist beschränkt: Der Carlemanteil hat Norm höchstens \(\pi/2\), regulärer Kontakt und Spiegelkern zusammen unter 2, alle Primverschiebungen zusammen unter 16, \(\|Q_bm\|<100\) aus der rohen Differenzen- und Randlogform, und \(1/\sqrt{2\mu_b}<3\). Somit kostet die Eingangsapproximation in der physischen alten Quellennorm höchstens das 400-Fache ihres \(W\)-Fehlers. Diese Rechnungen liefern einen konstruktiven Restmodul; bei reinen Formdualquellen wäre ein eigener Hilbertanschluss nötig.

## Reproduktion und Geltungsbereich

Python 3.13, python-flint 0.9.0. Vom Handoff-Ordner aus:

    python rohdaten.py ../../research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand roh.json.gz
    python abnahme.py roh.json.gz
    python schnittstelle.py

Der erste Lauf erzeugt alle Rohmatrizen. Der zweite bindet deren mathematische Felder per SHA-256, prüft den vollständigen Gammafehler, beide Vergleichsmatrizen und die physische Ausgabe. Sechs niedrige Formeinträge werden zusätzlich mit einer separaten Polynom-Autokorrelationsrechnung für Potential, Prime und Gamma geprüft. Der gewählte Datenstand, die geerbten Eingaben und der Status der Schnittstellen sind im [Zertifikatszustand](ZERTIFIKAT.json) angegeben. Keine externe Begutachtung. Der feste ungerade Hochraumvergleich mit \(Q_*^{-1}\) hat einen eigenen [Nachweis](../a9-a11-ungerade-hochraumkopplung-2026-11-25/). Die neue gemeinsame Regel wird durch die vollständige gemeinsame Integration ausgewertet und ist rechnerisch aufwendiger. Ihre Kalibrierung auf diesem einen Horizont liefert keine kofinale Folge.
