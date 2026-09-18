# Shell-Schur: vollständiger Pivot positiv, Schur-Fortsetzung noch offen

Stand 18. September 2026, aufbauend auf Shell-Head
`0ec5276b2e0a2fe0aa700503e40b4a6a0acb65ff`.
Status: **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Der vollständige gerade Shellblock ist auf einem expliziten rechten Intervall
positiv. Mit B=log(5)/2 und 0<b-B<=10^-20 gilt für jede Shell-Funktion
s in H1(B,b) mit s(b)=0:

\[
\boxed{D_b[s]\ge\frac{|s(B)|^2}{32\cdot10^{13}}+70\|s\|_{L^2(B,b)}^2.}
\]

Die freie innere Spur ist enthalten. Der Beweis umfasst die gesamte
unendlichdimensionale Shell, die vollständige Gamma-Energie und alle
aktiven Kanäle 2, 3, 4, 5. Die Konstanten sind bewusst konservativ;
10^-20 ist ein Beweisintervall und keine optimierte Reichweite.
Verbraucht wird nur die zertifizierte Core-Untergrenze 10^-13.
Der Fast-Null-Rayleigh-Wert 3.3e-12 wird nicht als uniforme Reserve benutzt.

Im Hilbertraum X=C direkt-sum L2(B,b), dessen erste Koordinate die Spur
trägt, besitzt der abgeschlossene Shellblock die echte Operatoruntergrenze
D>=1/(32*10^13) und damit einen beschränkten inversen Operator.
Für den tatsächlichen Lift ergibt sich außerdem die physische Untergrenze
Q_W[Ls]>=||Ls||^2/(2048*10^13).

Ein neuer struktureller Befund ist für den nächsten Schritt entscheidend.
Schreibt man den Core-Anteil des Lifts als t psi-m_s chi, so ist psi die
momentfreie Funktion mit innerer Spur eins. Beim Formabschluss gehört
psi sowohl zum alten Core als auch zum abgeschlossenen Shellbild:

\[
\widetilde L(1,0)=\psi.
\]

Damit stellt das Koordinatenpaar (-psi,(1,0)) die physische Nullquelle dar.
Folglich gilt für den unbereinigten Schur-Operator exakt

\[
(A-C^*D^{-1}C)\psi=0.
\]

Eine uniforme strikt positive Untergrenze auf dem gesamten alten Core ist
in diesen abgeschlossenen Koordinaten unmöglich. Das ist eine
Doppelzählung einer Richtung, keine negative Weil-Quelle und kein
Gegenbeispiel gegen die gewünschte Positivität. Die ursprüngliche
H1-Zerlegung bleibt korrekt; die Doppelzählung entsteht beim Abschluss.

Die Korrektur ist vollständig beschrieben: psi wird ausschließlich dem
Shellblock zugeordnet, der Core wird in den Koordinaten auf psi-perp
komprimiert. Jede ursprüngliche zulässige Quelle bleibt darstellbar.
Es wird keine dritte Mellinbedingung eingeführt. Die physische Norm ist
in diesen Koordinaten mit Faktoren 1/32 und 65 kontrolliert.

Offen bleibt jetzt die konkrete Abschätzung

\[
R_0=A_0-C_0^*D^{-1}C_0\ge\sigma I,\qquad\sigma>0,
\]

auf sämtlichen verbleibenden Core-Richtungen, einschließlich des
Komplements jeder ausgewählten Fast-Null-Quelle. Danach sind inverse
Schur-Norm und physische Norm zu bezahlen. Der Odd-Sektor rechts von B
benötigt ebenfalls ein eigenes Zertifikat. Ein neuer All-Source-Satz
rechts von B ist daher ausdrücklich **nicht** geschlossen.

Die analytischen Beweise stehen in PROOF.md; der Checker verifiziert
19 gebundene Eingabedateien und 43 gerichtete beziehungsweise exakte
Konstanten- und Buchhaltungsentscheidungen. Endlich viele Checks ersetzen
keinen der Formbereichs- oder Vollständigkeitsbeweise. Keine Quadratur,
keine numerischen Eigenwerte, kein A1 und keine Änderung an main.


Der währenddessen hinzugekommene Commit `ea06f01c` mit dem inversenfreien
Schur-Kriterium bleibt vollständig erhalten. Dessen bedingter Satz ist
korrekt. Für die bisherigen Koordinaten ist die geforderte uniforme
Schranke theta<1 aber unmöglich: Tatsächliche H1-Core- und Shell-Folgen
können dieselbe Funktion psi im Energienormabschluss annähern, sodass
|C|^2/(A D) gegen 1 geht. Dies gilt für jedes feste B<b<=1 und benötigt
keine vorherige Behauptung über einen inversen Operator. Die Entfernung
der doppelt dargestellten Spur-Richtung ist daher auch für diesen Ansatz
notwendig. Der Beweis steht in PROOF.md, Abschnitt 10.
