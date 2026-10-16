# Objekt X — Stufe-2-Gegenprüfung, schneller Quellenevaluator und 191 Paarungen

16. Oktober 2026 · lokale numerische Diagnose mit einzelnen exakten Identitäten · **kein Intervallzertifikat, keine U8-Aktion, kein A9→A11-Abschluss**.

## 1. Eingabe und wirklich ausgeführter Umfang

Unverändertes Eingangsarchiv:
`Objekt-X-Stufe1v2-Stufe2-Diagnose-2026-10-16.zip`

SHA-256:
`62e9f6d860ba98f4defc651b465cfc431f891cd058f52ddaf88d54073da18f13`.

Alle 22 Dateibindungen des Manifests wurden gegen die extrahierten Bytes geprüft. Der darin bezeichnete historische Repository-Head ist `0ded564d5a6eff1c5b64698821a3f7d04b14e68b`; dieser Audit hat GitHub nicht abgefragt oder verändert. Die Hashangaben der großen Vorfahren und des fremden Stufe-1-Prüfpakets sind Herkunftsangaben des Eingangsmanifests: jene Archive wurden in diesem Audit nicht erneut gereplayt. Insbesondere wurde kein eigener Lauf des dort erwähnten `certify.py` behauptet.

`post.py` wurde aus den unveränderten vorhandenen Netzdateien ausgeführt. Nur `qnp_psi.PSI_PATH` wurde zur Laufzeit auf die lokale unveränderte `PSI_DEFINITION.json` gebunden. Der Originalquelltext blieb unverändert. Die erzeugte `STUFE2_RESULTS.json` ist bytegleich:
`6521e2d5cebe11489d63e8cd0ac39e230bd47af476bc95340c1a4a45684982ec`.

Das ist ein Replay der Nachverarbeitung, **kein erneuter Aufbau der beiden ursprünglichen 468-Knoten-Netze mit mpmath**.

Neu ausgeführt wurden:
- ein alternativer schneller Evaluator auf allen 936 gespeicherten Punkten;
- zwölf frisch mit dem ursprünglichen mpmath-Evaluator berechnete Referenzpunkte bei 38 Dezimalstellen, sechs je Parität;
- 191 momentkorrigierte alte Polynom-Paarungen je Parität auf verfeinerten, sprungangepassten Netzen;
- 384 exakte rationale Kontrollen der verwendeten Legendre-Logmomentformel.

Die letzte Liste enthält nicht die 191 vollständigen Funktionen `B8* e_i`, nicht `B8 y`, nicht `U8 f`, nicht die fertige Funktion chi und nicht deren Residualpaarungen.

## 2. Quelle und drei Räume

Es gelten c=A8=3 log(2)/2, a=A9=log(3), h=a-c. Der neue Evaluator behandelt ausschließlich die gelieferten Mittelpunktmodelle von psi_v je Parität. Auf dem Kern (-c,c) ist diese Funktion ein Polynom vom Grad höchstens 9 plus der kleine Mellinterm. Auf (c,a) liegt die ganze gegebene Legendreentwicklung bis Grad 95 vor. Die negative Schale folgt aus der Parität; außerhalb (-a,a) gilt Nullfortsetzung.

Die Quelle ist weiterhin

    f_v = Pi8 [Q_a^np psi_v]|_(0,c),
    Q_a^np = H_Gamma - kappa I - S_a.

Der Operator wirkt vor der Restriktion auf die ganze Funktion. Alle sechs aktiven Primzahlpotenzkanäle {2,3,4,5,7,8} werden direkt ausgewertet. Das Vorzeichen der korrigierten lambda_total wird aus der gelieferten v2-Datei unverändert übernommen.

Der Operator wird nicht auf eine punktweise Interpolation eines alten Netzes angewendet. Die neuen Werte entstehen unmittelbar aus der ganzen Mittelpunktfunktion. Das beseitigt nicht den noch offenen Transport der geerbten Modell- und Koeffizientenfehler durch Q bzw. U8.

## 3. Analytische Zerlegung für den schnellen Evaluator

Schreibe psi=u auf (-c,c) und psi=s auf (c,a), mit Parität epsilon. Für 0<x<c gilt exakt

    H_Gamma psi(x)
      = int_-c^c k(|x-y|) [u(x)-u(y)] dy
        + u(x) [Theta(c-x)+Theta(c+x)]
        - int_c^a [k(y-x)+epsilon k(y+x)] s(y) dy,

    k(r)=exp(-r/2)/(1-exp(-2r)).

Die vollständige Schwanzfunktion hat die elementare geschlossene Darstellung

    Theta(d)=int_d^infinity k(r)dr
            =atanh(exp(-d/2))+atan(exp(-d/2)),  d>0.

Beweis: Mit z=exp(-r/2) wird k(r)dr=-2 dz/(1-z^4); die Zerlegung
`2/(1-z^4)=1/(1-z^2)+1/(1+z^2)` ergibt die Formel. Im Code wird der kleine Unterschied `1-exp(-d/2)` durch `-expm1(-d/2)` ausgewertet.

### 3.1 Keine numerische Division einer ausgelöschten Differenz durch r

Im Kern wird `(u(x)-u(y))/(x-y)` direkt berechnet, nicht durch Subtraktion zweier großer fast gleicher Funktionswerte. Für die polynomiale Komponente wird die dividierte Differenz der Legendre-Rekurrenz mitgeführt. Für cosh/sinh wird die entsprechende hyperbolische Differenzformel mit stetig ergänztem sinh(z)/z benutzt. Der verbleibende Faktor `r k(r)` hat den Grenzwert 1/2. Das Kernintegral ist so in zwei glatte Integrale links und rechts von x aufgeteilt.

### 3.2 Die ganze singuläre Schalenwirkung, nicht nur ihr führender Logarithmus

Zerlege k(r)=1/(2r)+k_reg(r). k_reg besitzt bei 0 eine stetige analytische Fortsetzung mit Wert 1/4. Sei

    s(y)=sum_(n=0)^95 A_n P_n(2(y-c)/h-1),
    eta_-=1+2(c-x)/h, eta_+=1+2(c+x)/h.

Definiere hier ausdrücklich die STANDARD-Normierung

    Q_n(eta)=(1/2) int_-1^1 P_n(t)/(eta-t) dt, eta>1.

Dann gilt

    int_c^a s(y)/(2(y-x))dy = sum_n (-1)^n A_n Q_n(eta_-),
    int_c^a s(y)/(2(y+x))dy = sum_n (-1)^n A_n Q_n(eta_+).

Dies folgt durch die affine Variablentransformation und P_n(-t)=(-1)^n P_n(t). Die ganze Cauchy-Wirkung aller 96 Schalenkoeffizienten wird damit gesondert ausgewertet. Nur der reguläre Rest benötigt eine gewöhnliche Quadratur.

NIST DLMF 14.12.13 gibt die zugehörige Neumann-Darstellung in Olvers Normierung an: dort ist der Faktor n! zu beachten. Der Code verwendet die Standard-Q_n von scipy.special.lqmn, nicht ungeprüft Olvers Q. Quellen:
- https://dlmf.nist.gov/14.12.E13
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.lqmn.html

Nahe an der Wand wird Q_0 als `0.5*log1p(h/(c-x))` berechnet und die Rekurrenz in erweiterter Gleitkommaarithmetik benutzt. Der Abstand c-x kann separat übergeben werden. Eine aus einer gerundeten x-Koordinate rekonstruierte winzige Wanddistanz kann sonst viel relative Genauigkeit verlieren.

**Diese Zerlegungen sind analytische Identitäten. Ihre implementierte Gleitkommaauswertung ist dennoch kein Intervallbeweis.** Die angegebene Quadraturordnung ist keine pauschale Exaktheitsbehauptung für reguläre, aber nichtpolynomiale Integranden.

## 4. Zahlenvergleich und Grenzen der Referenzen

Auf allen 468 gespeicherten Punkten je Parität bleibt die maximale absolute Abweichung von Q_raw ungefähr unter 2.5e-7. Die mit den gespeicherten Netzgewichten gebildeten diskreten L2-Abstände liegen bei etwa 1.16e-9 (gerade) und 2.66e-10 (ungerade). Das sind diskrete Vergleiche, **keine ganzen Hilbertnorm-Fehlergrenzen**.

Die größte punktweise Differenz liegt nahe der Wand. Gespeicherte x-Koordinaten besitzen nur die ausgegebenen Dezimalstellen; die logarithmische Ableitung macht die Interpretation solcher Vergleiche empfindlich. Eine vollständige Ursachenzerlegung dieser Differenz wird nicht behauptet.

Zusätzlich wurden zwölf Referenzwerte frisch aus dem ursprünglichen radialen Integral berechnet. Die Punkte umfassen beide Seiten einer Prim-Sprungstelle und Wandabstände 1e-6 sowie 1e-10. Auf diesen zwölf Punkten ist die größte gemessene relative Abweichung <5.7e-14, die größte absolute <5.4e-9. Das bestätigt den alternativen Rechenweg numerisch; zwölf Punkte liefern keine uniforme Schranke.

Der Evaluator nutzt NumPy longdouble, SciPy für Q_n und mpmath bei der Initialisierung. Auf dem geprüften System hat longdouble 63 explizite Mantissenbits; es handelt sich nicht um eine validierte reine Binary64-Implementierung. Auf Plattformen ohne diese longdouble-Genauigkeit bricht der Code ab. Verwendete Versionen: Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0.

## 5. Exakter Logarithmusabzug vor den 191 Paarungen

Sei j=psi(c+)-psi(c-). Auf der positiven Kernhälfte wird

    L_j(x)=(j/2)[log(c-x)+epsilon log(c+x)]

von Q_raw abgezogen. Die führende Wandsingularität ist damit explizit. Für n mit derselben Parität, n>=1, gilt

    int_0^c P_n(x/c)[log(c-x)+epsilon log(c+x)]dx
       = -2c/[n(n+1)].

Für n=0 (gerade) ist der Wert `2c(log(2c)-1)`. In den physisch normierten Koeffizienten entspricht das

    a_n(L_j)=-j sqrt(2c(2n+1))/[n(n+1)], n>=1,
    a_0(L_j)= j sqrt(2c)[log(2c)-1].

Die Formel folgt aus Parität und der Legendre-Logmomentidentität. Diese wurde für alle Grade 0,...,383 zusätzlich exakt mit rationalen Rodrigues-Koeffizienten und den Integralen

    int_0^1 t^k log(1-t)dt = -H_(k+1)/(k+1)

kontrolliert. Es bestehen 384 rationale Gleichheiten. Weder j noch die übrigen Quellparameter werden dadurch zu zertifizierten Eingaben promoviert.

Die neun echten Prim-Sprungstellen bleiben Zellgrenzen. Die alten Dateien enthalten zehn Einträge, weil `c-log(2)` und `log(4)-c` trotz exakter Gleichheit durch Rundung zweimal in die Punktmenge gelangten. Beide wurden mit demselben Dezimaltext gespeichert; daraus entstand eine scheinbar entartete zusätzliche Zelle. Der neue Generator benutzt die symbolisch verschiedenen neun Orte. Diese Diagnose wird nicht als Ursache aller alten Quadraturabweichungen ausgegeben.

Die Momentprojektion wird mit dem gesonderten Logarithmusmoment vollzogen; das verbleibende reguläre Stück wird numerisch integriert. Die niedrigen Korrektur-Momente werden über eine positive Taylorreihe berechnet. Die Modelle bleiben Gleitkommadaten und besitzen keine exakt zertifizierte Momentnullheit.

## 6. Die 191 gelieferten Paarungen

Setze

    e_n(x/c)=sqrt(2n+1)P_n(x/c),
    phi_n(x)=(e_n(x/c)-r_n e_sigma(x/c))/sqrt(2c),
    r_n=<m_scaled,e_n>/<m_scaled,e_sigma>,
    n=sigma+2,...,sigma+382, Schrittweite 2.

Dann ist `Phi*f` der Vektor der 191 Paarungen `<phi_n,f>_(L2(2dx))`. Der neue Code berechnet genau diesen Vektor. Er berechnet weder die Low/High-Kopplungsfunktionen B8*e_i noch d=Phi*f-B8 y/delta.

Für 3.520, 7.040 und 14.080 Punkte je Parität liegen folgende Diagnosen vor:

| Größe | Gerade | Ungerade |
|---|---:|---:|
| Norm f (feinster Lauf) | 237738.801112947 | 268775.539807705 |
| Rohes Parseval-Restnorm-Schätzergebnis ab Grad 62 | 616.68448 | 715.05791 |
| Rohes Parseval-Restnorm-Schätzergebnis oberhalb Grad 382/383 | 135.23728 | 147.07328 |
| Max. Änderung eines Phi*f-Eintrags 64→128 Knoten je Zelle | <4e-13 | <4e-13 |
| Max. Änderung 128→256 Knoten je Zelle | <9e-13 | <9e-13 |

Die Unterschiede der Paarungsvektoren sind Konvergenzbeobachtungen, keine wahren Fehlerobergrenzen. Der gleiche Zustand der Rundungsarithmetik kann auch gemeinsame Fehler erzeugen. Die genannten Parseval-Reste stammen aus numerischer Subtraktion und sind **keine unendlichen Tailzertifikate**. Sie sind auch nicht ohne weitere Behandlung des gesamten M*-Momentterms als exakte Norm von T_h f zu lesen.

Die 64-Knoten-Läufe einschließlich aller 191 Paarungen benötigten auf dem geprüften System ungefähr eine Sekunde je Parität, die 256-Knoten-Läufe ungefähr vier Sekunden. Diese beobachteten Laufzeiten betreffen nur diese Berechnung und sind keine Schätzung für die noch offene Stufe 3 oder eine Zertifizierung.

Das ursprüngliche Netz liefert bei Grad 60 (gerade) etwa 250.37515041 statt 249.85717946, bei Grad 61 (ungerade) etwa -396.03611833 statt -394.84004641. Der Quellenbericht hatte die Unzuverlässigkeit der höheren Koeffizienten bereits eingeräumt. Die alten Zahlen über den >61-Anteil sollten daher nicht als Nachweis benutzt werden. Die feinere Diagnose bestätigt die qualitative Niedriggradigkeit, nicht deren zertifizierte Stärke.

## 7. Begrenzte Aussage über U8 und nächster Schritt

Mit der gegebenen U8-Formel sind weiterhin nötig:

    y=T_h f,
    d=Phi*f-B8 y/delta,
    cvec=C_inv C_inv* d/(1-rho),
    U8 f=Phi cvec+T_h*(y-B8*cvec)/delta.

Eine kleine rohe Hochenergie des Eingangsfunktionals zeigt nicht, dass B8 y oder die Hochkorrektur T_h*B8*cvec klein ist. Die Wirkung von C_inv, die Korrelation mit Phi*f und die ganze Low/High-Kopplung entscheiden darüber. Daher folgt keine Dominanz von Phi cvec aus der hier beobachteten Niedriggradigkeit allein.

Der nächste Rechenauftrag ist nicht ein weiterer Punktplot, sondern die vollständigen B8*e_i-Paarungen und die gemeinsame Größe d. P_Y ist als Identität minus vollständige endliche niedrige Projektion zu behandeln; die hohe Funktion darf nicht durch wenige hohe Koeffizienten ersetzt werden.

Für den unteren späteren Richtungstest ist weiterhin p exakt zu verwenden oder e in p=alpha v+e mit seinem ganzen Fehler zu transportieren. Dieses Paket behandelt nur t=v. Eine globale error<=1e-12|f(x)|-Vorgabe wäre an Nullstellen ohnehin ungeeignet. Erforderlich sind abs+rel Diagnosekriterien, anschließend ein gerichtetes Fehlerbudget für die tatsächlich benötigten Paarungen.

Die geerbte gemeinsame k-Unsicherheit bleibt als K-Ellipsoid zu transportieren. Neue Evaluationsgenauigkeit macht diese physische Modellunsicherheit nicht kleiner. U8 ist unverändert die gegebene Majorante, nicht die tatsächliche A8-Inverse. Keine neue obere Norm von U8 oder W9 wurde ermittelt.

## 8. Redaktion und Reproduktion

Im Stufe-1-v2-Bericht stehen unterhalb des Korrekturkopfs weiterhin die historischen Plusformeln und die unzulässigen p=qv-Identitäten; sogar der alte kopierbare Prompt enthält sie noch. Die Originaldatei bleibt hier unverändert. Für neue Übergaben gilt ausschließlich der Korrekturkopf und die v2-JSON. Bei Integration sollten die alten Passagen ausdrücklich als überholt markiert und der aktive Übergabeprompt ersetzt werden.

Reproduktion aus frischer Entpackung:

    python -B verify_diagnostic.py --output ../new-unused-directory --full-reference

Das Ziel muss neu und außerhalb des Pakets sein. Eingaben und Originalcode werden nicht überschrieben. Der Lauf prüft Quellenhashes, die 384 rationalen Loggleichheiten, den bytegleichen Original-Postprozessor, alle alten Netzpunkte, zwölf mpmath-Referenzpunkte und die 64/128-Netzverfeinerung der Paarungen. Ohne --full-reference werden die mitgelieferten hochpräzisen Punktreferenzen verglichen, nicht frisch berechnet.

Die Prüfresultate behalten ausdrücklich die Flags `full_operator_error_certified=false`, `U8_action_computed=false`, `weighted_residual_energy_certified=false` und `A9_A11_closed=false`. Das Wort PASS im Diagnoselauf bezeichnet nur die ausgeführten und beschriebenen Kontrollen.
