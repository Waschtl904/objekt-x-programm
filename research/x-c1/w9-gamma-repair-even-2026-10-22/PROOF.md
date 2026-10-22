# Bedingte Gamma- und Paarungsreparatur des festen geraden Zeugen

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; PENDING_STATUS_REVIEW.**
Die nachstehende Ergänzung betrifft ausschließlich den unveränderten festen
geraden Zeugen des Pakets vom 21. Oktober (#252). Die ganze analytische
Modellidentifikation und die Gesamtabnahme der geerbten Fehlerlemmata bleiben
offen. Der Merge dieses Pakets bedeutet keine solche Abnahme.

## 1. Defekt und eingefrorener Gegenstand

`INPUT_BINDINGS.json` bindet 458 Dateien des ursprünglichen Pakets und 109
externe Eingänge. Der mathematische Bezug ist Commit
`36513b0fad9313906246e835d927b686dbb93174`. Der Builder hat SHA-256
`ed58da3caacd5ca39de1f910c77920e7079eec905a560b487600c71e97c8df64`.
Originalpaket, Zeuge, Antwortregel, K_new, w, J, p0, ff, eta=1e-10 und
Halbachsennorm `||f||_X² = 2 integral |f(x)|² dx` bleiben gebunden.

Für 0<=x<a<y<b verlangt der reguläre innere Transport

    R_in f(x) = integral_a^b f(y) [Gamma((y-x)/2)+Gamma((y+x)/2)] dy.

Die bisher verwendete äußere Formel enthält dagegen Gamma((x-y)/2) anstelle
von Gamma((y-x)/2). Für Gamma(t)=sum gamma_j t^j und M_k=int f(y)y^k dy ist

    [x^ell] R_in = (1+(-1)^ell) sum_{j>=ell} gamma_j binom(j,ell) M_(j-ell)/2^j.

Beim äußeren Ausdruck liegt der Paritätsfaktor an j-ell. Der ungerade
Gamma-Anteil verhindert die Gleichheit. Die exakte Gegenprobe f=1 auf [1,2],
Gamma(t)=-t/24, x=1/2 ergibt innen -1/16, falsch -1/48; Differenz 1/24.
`kernel_geometry.py` prüft diese Werte rational. `corrected_builder.py`
erzeugt die innere Korrektur aus der gehashten Quelle als neue Fassung;
die korrekte äußere Verwendung von regular_out bleibt erhalten. Das
historische Paket wird nicht überschrieben und nicht zum reparierten Cache erklärt.

## 2. Vorzeichenbehaftete ganze Korrektur

Sei C_S=(R_out-R_in)S für S=Jw-Y p_tail und entsprechend C_psi für
psi=Y p_tail-(1-eta)Jw. Das Vorzeichen folgt aus dem Minuszeichen des regulären
Kerns im Q-Operator. In der normierten Kernkoordinate t=x/a werden

    alpha = integral_0^1 C_S(a t) dt / integral_0^1 m(a t) dt,
    v = (C_S-alpha m)/delta,
    I_psi = integral_0^a C_psi(x)m(x) dx

geführt. Die ganze äußere Änderung enthält Q_core v, sämtliche aktiven
Primverschiebungen und den Momentlift aus integral v Qm sowie I_psi. Sie
wird als Summe von Polynomen und logarithmischen Termen dargestellt.
Die beiden gebundenen Darstellungen wurden nach gemeinsamer affiner
Koordinatenumrechnung verglichen; die X-Norm ihrer Differenz ist <4.201e-313.
Die 84 Korrekturpaarungen stimmen auf dem exportierten rationalen Raster
überein. Die 191 zusätzlichen Quellenkontrollen betreffen nur die erste
J-Testrichtung; daraus wird keine Prüfung aller 84 Quellrichtungen abgeleitet.

## 3. Zwei ganze Normpreise

Der konservative Weg benutzt die rohe, auch für niedrige Anteile gültige
g-Operatorcap 14 (berechneter Ausdruck <13.066), einen direkten Momentpreis
und die gebundenen Gamma-/Momentreste. Der zusätzliche X-Preis ist
<1.058217727912e-5; die bedingte Restenergie ist <1.391e-10.

Der engere Weg integriert das Quadrat der tatsächlichen ganzen Korrektur.
Für z=(x-a)/(b-a) lautet ihre Darstellung

    P(z)+A(z) log z+B(z) log(z+2a/(b-a))+D(z) log(z+a/(b-a)).

Primanteile und Momentterm sind enthalten. Der erste gebundene Rechenweg
verwendet Logproduktmomente; `norm/independent_norm.py` benutzt dafür eine
getrennte Implementierung: die beiden glatten Logarithmen werden bis Ordnung
160 entwickelt, log z bleibt exakt. Verwendet werden ausschließlich

    integral_0^1 z^k dz = 1/(k+1),
    integral_0^1 z^k log z dz = -1/(k+1)^2,
    integral_0^1 z^k (log z)^2 dz = 2/(k+1)^3.

Die glatten Reihenreste werden geometrisch begrenzt; der echte cosh-
Momentrest wird zusätzlich als nichtverschwindendes rationales Intervall
bezahlt. Das Quadratintegral liegt bei 1.33373030917235e-13; die ganze
Korrektur hat X-Norm <3.653e-7. Beide Wege verwenden Arb/python-flint,
also keine unabhängigen Rechenbibliotheken. Die ganze Norm folgt nicht aus
84 Paarungen oder aus einem Netzunterschied.

## 4. Paarungsanschluss und korrigierte Konturhülle

Die signierte Paarungsrechnung verwendet 81 äußere Abschnitte (65 übernommene,
16 neu berechnete). Nicht signiert integrierte Zellen bleiben durch die
gebundenen 411 Energiebelege eingeschlossen. Für eine Zelle I mit
E_I>=2 int_I |r0|² und S_i>=sup_I |J_i| gilt

    |2 int_I r0 J_i| <= S_i sqrt(2 |I| E_I).

Die Einzelpreise werden summiert. Die äußersten Stücke verwenden die geerbte
Hülle A(1+log(v)^2), A=1e20, und deren direktes lineares Integral.
Maximaler Integrationspreis: <3.786e-14.

Zusätzlich wird der bisher ausgelassene innere h-Randstreifen der Länge
etwa 1.47238e-16 vorzeichenbehaftet aufgelöst. Für den Taylorrest auf dem
physischen Radius 0.001 gilt R=0.001/(d/2). Die Polynomkontur muss denselben
normierten Radius R verwenden, nicht die fest eingebaute 2. Mit
M>=sup_|z|=R |h(z)| ist die Variation um den Mittelpunkt höchstens

    sum_{k=1}^7 |h_k| + M R^(-8)/(1-R^(-1)).

Die radiusgerechte Fassung liefert einen Cauchy-Rest <1.682e-88 und
h-Variation <2.452e-17. Alle zuvor exportierten mathematischen Enddaten
bleiben unverändert. Der verbleibende ganze Kernfehler einschließlich der
64/128-Brücke ist <4.696e-16 in X-Norm.

Für jede der 84 Koordinaten wird das vollständige arithmetische Intervall

    D_i = Q81(r_alt)_i - n_expanded,i + C_i + H_i

gegen seine eigene Integrations- und Restkernhülle geprüft. Alle Intervalle
sind vollständig enthalten; kleinste strikte Reserve >3.8919e-15. Die
anschließend um Unsicherheiten erweiterten Endhüllen enthalten Null und
haben maximalen Absolutendpunkt <6.724e-14. Bloße Nullüberlappung ist nicht
das Abnahmekriterium.

## 5. Einmalige Fehlerbuchung und bedingter Vergleich

Der alte Operatorpreis wird als

    10*(p_total+low_feature_total)+sqrt(5/21)*raw_X_error

rational rekonstruiert. Sein ursprünglicher oberer Endpunkt wird beibehalten.
Der p-Preis wird einmal geführt. Der innere Randstreifen gehört weiterhin
zum bereits enthaltenen Kernquadraturpreis; seine signierte Auflösung
verursacht keine zweite Buchung. Die korrigierte innere Modellnorm bleibt
unter dem geerbten Deckel 1e20, die rohe g-Cap unter 100. Dies prüft die
Übertragung dieser Deckel unter Voraussetzung ihrer alten Herleitungen.

Mit e_bridge, e_core und e_operator aus dem gebundenen Fehlerbuch gilt bedingt

    ||r||_Ldual <= sqrt(5/21)*(sqrt(E_alt)+||C||_X+e_bridge+e_core)+e_operator.

Der direkt integrierte Korrekturpreis liefert eine Restenergie <4.632e-11;
der konservative Operatorweg liefert <1.391e-10. Beide erfüllen den
unveränderten Deckel 1e-9. Mit diesem Deckel liegt der Gesamtvergleich
unter 5.395092490766814e-5 und die Budgetuntergrenze über
5.41171693607084e-5; Reserve >1.66244e-7.

## 6. Grenzen und nächste Pflicht

Die geerbten Domänen-, Quellen-, Projektions-, qm-, Rand- und Operatorlemmata
wurden hier nicht sämtlich von Grund auf neu bewiesen. Auch die vollständige
analytische Identifikation des korrigierten Modells mit dem beanspruchten
Residuum bleibt ein eigener offener Abnahmegegenstand. `OPEN_OBLIGATIONS.md`
führt ihn endlich und konkret auf. Die vorliegenden Replays beweisen ihren
gebundenen numerischen und algebraischen Umfang, keine Gesamtabnahme.

Keine zweite physische Richtung, kein vollständiger Grad-11-Raum, keine
ungerade Parität, keine bekannte A11-Positivität als Eingang und keine
Promotion von N12, Punkt 4, Objekt X, globaler Weil-Positivität oder RH.
Die eingefrorenen Originale dienen weiterhin der Provenienz; für den
korrigierten Funktionsanspruch ist diese Ergänzung mitzulesen.
