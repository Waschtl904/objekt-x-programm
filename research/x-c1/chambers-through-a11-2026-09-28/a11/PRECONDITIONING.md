# Rationale Kongruenz statt instabiler direkter Intervall-LDL

## Diagnose

Der erste direkte Intervall-LDL-Lauf der vollständig bezahlten Untermatrix
F bricht nach 43 bzw. 46 positiven Pivots ab. Die nächsten Intervalle
enthalten Null und besitzen große Radien; sie sind nicht strikt negativ.
Schon der niedrige Modellblock ohne Schurabzug zeigt dieselbe Verstärkung.
Die Eingangseinträge der niedrigen Form sind auf 10^−100 eingeschlossen.

Die Mittelpunktsrechnungen haben in beiden Paritäten sämtliche 285 Pivots
positiv. Das dient ausschließlich dazu, eine geeignete Basis vorzuschlagen.
Es ist kein Zertifikat für die Intervallmatrix.

Die ursprünglichen Ergebnisse bleiben als reserve_results.json,
reserve_results_lower_matrices.json.gz, INITIAL_DIAGNOSTIC.json und
WIDTH_DIAGNOSTIC.json erhalten. Das Modell und alle Fehlerabzüge bleiben
für den folgenden Nachweis unverändert.

Beim zusätzlichen LDL-Test der nahezu diagonalen Kongruenz trat außerdem
in der hier installierten python-flint-0.9.0-Umgebung ein reproduzierbarer
arithmetischer Randfall auf: `arb(0, arb('1e-100')) ** 2` ergibt `nan`,
während die Multiplikation desselben Balls mit sich selbst eine endliche
einschließende Schranke liefert. Der neue LDL-Prüfer verwendet daher für
seine Quadrate ausdrücklich `x*x`. Dies ist auch bei Vorzeichenwechsel
ein gültiges, gegebenenfalls breiteres Intervall für x². Ein eigener
Primitiventest kontrolliert Endlichkeit und Einschluss von Null. Die
Ganzzahlarithmetik besitzt einen separat implementierten Quadratoperator.
Der Integralaufbau und seine Dateien wurden für diese Korrektur nicht geändert.

## Exakte Basisänderung

Aus der Mittelpunktszerlegung L D L* wird eine Näherung von L^−* gebildet.
Alle Einträge werden auf das rationale Raster 10^−100 gebracht; die
Diagonale wird exakt auf 1 und der untere Dreiecksteil exakt auf 0 gesetzt.
Die resultierende reelle Matrix P ist daher **exakt invertierbar**, mit
Determinante 1. Ihre Güte als Näherung ist keine Beweisvoraussetzung.

Anschließend wird aus den ursprünglichen vollständigen Intervallen neu

\[
\widetilde F=P^*FP
\]

gerichtet eingeschlossen. Es werden keine Intervallradien verworfen,
keine Fehlerschranken verkleinert und keine hohen Kopplungen entfernt.
Ein gerichteter Gershgorin-Bound

\[
\mu=\min_i\left(\underline{\widetilde F_{ii}}-
\sum_{j\ne i}\max|[\widetilde F_{ij}]|\right)>0
\]

beweist die Positivität jeder tatsächlich eingeschlossenen hermiteschen
Matrix. Zusätzlich wird eine vollständige Intervall-LDL der transformierten
Matrix durchgeführt. Die 285 positiven Pivots beziehen sich auf diese
exakt rationale Kongruenz der ursprünglichen Schur-Untermatrix.

## Rückrechnung in die ursprünglichen Koordinaten

Setze ρ=||P||_F², exakt aus den rationalen Einträgen berechnet. Dann gilt
||P||²≤ρ und für x=Pz

\[
x^*Fx=z^*\widetilde Fz\ge\mu\|z\|^2
\ge\frac\mu\rho\|x\|^2.
\]

Damit ist σ=μ/ρ ein tatsächlich bezahlter Boden in den **ursprünglichen**
niedrigen Koordinaten. Die physische Schur- und Normumrechnung aus PROOF.md
bleibt mit δ=1 unverändert:

\[
c_{phys}=\frac{\min(\sigma,1)}{4(1+b)^2},\qquad
\eta=\frac{c_{phys}}{c_{phys}+13}.
\]

Die unabhängige Ganzzahlprüfung rekonstruiert zuerst F aus den ursprünglichen
Modellintervallen und Fehlertermen. Sie prüft die exakte Dreiecksstruktur
von P, berechnet P*FP mit eigener gerichteter Arithmetik erneut, prüft ihren
eigenen Gershgorin-Boden und alle 285 Pivots und rechnet μ/ρ sowie die
physische Reserve selbst zurück. Die gespeicherte Arb-Kongruenz dient nur
dem zusätzlichen Vergleich, nicht als Ersatz für diese Rechnung.

Die Aussage dieses Zusatzes ist eine Äquivalenz und eine explizite
Normschranke. Das tatsächliche Bestehen der Kontrollen wird ausschließlich
durch die späteren Quittungen preconditioned_results.json und
integer_results.json dokumentiert. Externe analytische Abnahme bleibt offen.
