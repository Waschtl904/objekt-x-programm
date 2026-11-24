# A9 → A11 · Feldrechnung am festen ungeraden Zeugen

**Nachtrag vom 24. November.** Die beiden Randintervalle und der physische Quellenanschluss sind inzwischen für diesen festen Zeugen projektintern eingeschlossen. Die folgende Teilrechnung dokumentiert den Ausgangsstand am Commit `00806f8`. [Vollständiger fester Zeugenvergleich](FESTER_UNGERADER_ZEUGE.md) · [Gerichtete Endpunkte](ZEUGE.json)

24. November 2026. Projektinterne Teilrechnung. Externe Gegenprüfung offen.

Der feste Zeuge braucht eine obere Schranke von $8{,}1\cdot10^{-9}$ für die vollständige Energie seiner Restquelle. Das entspricht einer Dualnorm von höchstens $9\cdot10^{-5}$. Die folgende Rechnung erfasst den Innenbereich des gemeinsamen ungeraden Feldmodells, beide äußersten Ränder und zwei Fehlerbeiträge. Offen bleiben zwei Übergangsstreifen des Modells und die vollständige Übertragung auf die physische Quelle. Damit bleibt auch der Zeugenvergleich offen. [Endliche Vorprüfung](../BEWEIS.md) · [Rationaler Block, Zeuge und Eingaben](../ERGEBNIS.json)

| Größe | Ergebnis | Bedeutung |
|---|---:|---|
| Elf Teilintervalle der alten Schale | $2\int \vert r_{\rm mod}(x)\vert ^2\,dx<2{,}072\cdot10^{-12}$ | Gerichtete Summe, 97,7106 % der Länge |
| Beide äußersten Randintervalle zusammen | $<6{,}0\cdot10^{-13}$ | Gerichtete quadrierte Modellnorm |
| Gesamte Schale mit 24 bzw. 48 äußeren Gaußpunkten je Teilintervall | $2{,}1035\cdot10^{-12}$ bzw. $2{,}0973\cdot10^{-12}$ | Quadraturwerte der quadrierten Modellnorm |
| Kontinuierliches inneres Modellintegral gegenüber diskreter Kernquadratur | $<1{,}674\cdot10^{-8}$ | Fehler in der Dualnorm, über die ganze äußere Schale |
| Gemeinsamer Transport der 191 und 12 endlichen Kraftkoordinaten | $<7{,}757\cdot10^{-10}$ | Fehler in der Dualnorm unter den geerbten Form- und Fehlerverträgen |

## Welches Feld wird ausgewertet?

Für $a=\tfrac32\log 2$, $b=\log3$ sei $X=L^2((a,b),2\,dx)$. Die negative Halbschale ergibt sich durch ungerade Spiegelung. Fest sind die rationale Antwort $w_o$, der Block $K_o$ und $u=Jw_o$ aus der Vorprüfung. Für einen Test $t$ auf dem ganzen alten Raum lautet die Quelle

```math
r_o[t]=\langle\Lambda_Tt,f\rangle-(1-\eta)q[t,u]
-\langle gt,U_8(h-gu)\rangle-\langle at,K_o^{-1}(v-au)\rangle.
```

Der Feldaufbau bildet die beiden Kraftunterschiede vor dem Quadrieren und setzt die signierten Beiträge in derselben logarithmischen Ortskoordinate zusammen. Für die ungerade Parität verwendet er das sinh-Moment, die ungeraden Kerngrade 3 bis 383 und die ungeraden globalen Grade 3, 5, 7 und 9. Für die reguläre Gammafaltung ist bei Schale → Kern die Potenz des Ausgabearguments für die Spiegelung maßgeblich, bei Kern → Schale die Potenz der Integrationsvariablen. Die beiden Vorzeichenfaktoren lauten entsprechend $(-1)^j-1$ und $(-1)^{n-j}-1$. Der Kontrollprüfer testet je 25 425 Binomialterme und die Intervallgrenzen gegen die gespeicherten exakten Primlogarithmen. Die numerische Gegenprobe vergleicht das integrierte Feld außerdem mit den unabhängig gebildeten 84 Modellpaarungen. [Feldaufbau](odd_field_control.py) · [Kontrollrechnung](control.json)

Der rohe Feldvertreter und der Rieszvektor in der physischen Metrik unterscheiden sich. Stellt ein Feld $g\in X$ das tatsächliche Funktional als $t\mapsto\langle t,g\rangle_X$ dar, folgt aus $W_X\succeq I_X$ und $L\succeq(21/5)W_X$ die Abschätzung $\|g\|_{L^*}\le\sqrt{5/21}\,\|g\|_X$. Sie folgt auch direkt aus dem Variationsprinzip auf dem zulässigen Testraum. Damit ist eine obere Feldnorm ein hinreichender Test für die Dualenergie. Ihre Anwendung auf das Modell allein liefert noch keine Schranke für die tatsächliche Quelle.

## Innenbereich und Rand

Die vier Grenzen der drei Primzellen sind $a,x_1,x_2,b$, mit $x_1\approx1{,}065416244$ und $x_2\approx1{,}081164601$. Setze $d_l=x_1-a$, $d_r=b-x_2$. Eingeschlossen sind die mittlere Zelle und je fünf dyadische Teilintervalle der äußeren Zellen. Zusammen reichen sie von $a+d_l/32$ bis $b-d_r/32$. Jeder Preis enthält das Maß $2\,dx$, das Polynomquadrat und den Taylorrest. Die Taylorrechnung verwendet Arb mit 3072 Bit, behält die Spiegelvorzeichen in den Koeffizienten bei und begrenzt die analytisch fortgesetzten Cauchyintegrale auf dem Kontrollkreis durch ihre Integralform. Bei einem Polynom vom Grad $n$ genügt dafür die Schranke $(n+1)\sqrt{\operatorname{Mittel}(|p|^2)}$ für die Supremumsnorm auf dem betreffenden reellen Intervall. Der Vergleich mit dem getrennten direkten Auswerter in der Intervallmitte ist ein zusätzlicher Kontrollwert. [Teilintervallgrenzen und obere Preise](panels.json) · [Taylorprüfer](panels.py)

Für $v=\min(x-a,b-x)$ begrenzt der Randprüfer das diskrete Modell durch $C(1+|\log v|^2)$. Dazu wird die singuläre Kernwirkung in Integralform begrenzt. Das Integral von $(1+|\log y|)/(v+y)$ lässt sich bei $y=v$ und $y=1$ aufteilen. Bei jeder aktiven Primverschiebung in den Kern gilt $a-|x-\log q|\ge v$. Nach dem Quadrieren lässt sich die logarithmische Hülle exakt integrieren. Für Randbreiten $d_l/2^{213}$ und $d_r/2^{213}$ trägt diese Hülle zusammen weniger als $6\cdot10^{-13}$ zur quadrierten Modellnorm bei. Auf Breiten $d_l/32,d_r/32$ liefert dieselbe Hülle eine Obergrenze von rund $2{,}44\cdot10^{45}$. Sie entscheidet den Vergleich dort nicht. Offen sind somit die Streifen mit Abstand zwischen $d_i/2^{213}$ und $d_i/32$ vom jeweiligen Rand. [Randpreise](endpoints.json) · [Randprüfer](endpoints.py)

## Zwei über die ganze Schale begrenzte Fehler

**Innere Kernquadratur.** Im Modell werden die Integrale der Kerndichte durch 2 560 gewichtete Knoten ersetzt. Für jeden der glatten Abschnitte wird eine komplexe Schranke für die Dichte mit einer Taylorentwicklung vom Grad unter 128 eingeschlossen. Auf einer Bernsteinellipse mit Parameter 2 genügt für $n$ Gaußpunkte die Restschranke $8\,|I|M2^{-2n}$. Der singuläre Übergang auf die Schale wird in der äußeren $X$-Norm über den Abstand des Kontrollkreises begrenzt. Auf dem ausgesparten inneren Randstück geht die Carleman-Schranke $\pi/2$ ein. Der Prüfer erfasst auch reguläre Faltung, ungerade erste Legendrekoordinate und Momentpaarungen. Daraus folgen $3{,}430\cdot10^{-8}$ als obere Schranke in $X$ und $1{,}674\cdot10^{-8}$ in der Dualnorm für diesen Übergang zwischen den beiden Feldmodellen. [Quadraturpreis](core.json) · [Prüfer](core_price.py)

**Endliche Kraftfehler.** In der Schurzerlegung der positiven ungeraden Unterform sei $D=\operatorname{diag}((1-\rho)I_{191},K_o)$ in den normalisierten Kraftkoordinaten. Für die zugehörige Kopplung $A$ erhält man $A^*D^{-1}A\preceq (1-\eta)q\$ aus der Positivität des Restblocks und des bereits abgespaltenen hohen Kernpreises. Hier bezeichnet $q$ die direkte geliftete Form auf dem alten Resttestraum. Eine obere Schranke $q\preceq C_L L$ transportiert daher einen Fehler im normierten gemeinsamen Kraftvektor mit Faktor höchstens $\sqrt{C_L}$ in die Dualnorm.

Für diese obere Schranke kann man auf dem normierten Einheitsintervall zuerst die beiden Endpunktgewichte kontrollieren. Bei einer Endpunktmenge der Länge $e^{-t}$ verwende man die Legendreprojektion auf die Grade unter $N=\lfloor e^{t/4}\rfloor$. Die projizierte Funktion ist durch $N\|s\|_2$ punktweise begrenzt. Integration des Quadrats über die Endpunktmenge und dann über $t\ge0$ liefert für jedes der Gewichte $-\log x,-\log(1-x)$ höchstens $4\|s\|_2^2+8D_H[s]$, mit $D_H[s]=\sum H_n|s_n|^2$. Hier verwendet man $\log(n+1)\le H_n$. Der reine Schalenanteil hat keine innere Primkante und kostet höchstens $9D_H+4{,}505 I$. Für den Momentlift mit $m(x)=\sinh(x/2)$, $h=b-a$ und $\mu=(\sinh a-a)/2$ gilt $\|m\|_{H_8}^2=2\mu$ und $\|\lambda\|^2=(\sinh b-\sinh a-h)/4$.

Für die Kreuzwirkung Kern–Schale summiert der Prüfer den Carlemanpreis, den getrennten Spiegelkern, den regulären Kern und die Primtranslationen. Für die Kernwirkung auf $m$ lassen sich Differenzquotient, logarithmisches Potential, regulärer Kern und Primtranslationen einzeln auf dem Kernintervall begrenzen. Die Schranken für beide Größen sind $8{,}280$ und $9{,}119$. Der ganze zusätzliche Liftpreis ist kleiner als $11{,}003\|s\|_X^2$. Mit $L=D_H+1{,}1I$ auf dem Resttestraum und der älteren Untergrenze $L\succeq(21/5)W_X$ ergibt die ungerundete Auswertung $C_L<10{,}334812$. Der Prüfer führt die Fehler der gemeinsam gebildeten Zwölferkraft und der 191 normalisierten Kraftkoordinaten vor dem Transport im Produktraum zusammen. Ihr gemeinsamer Preis liegt unter $7{,}757\cdot10^{-10}$ in der Dualnorm. [Formabschätzung](transport.json) · [Gemeinsamer Fehler](features.json)

## Was entscheidet den Zeugen?

Sei $I_{\rm Streifen}$ die Summe der zwei offenen **quadrierten Modellnormen**. Sei $e_{\rm phys}$ eine obere Schranke in **Dualnorm** für den gesamten weiteren Übergang zum physischen Funktional nach den oben erfassten Kraft- und Quadraturfehlern. Dazu gehören die hohe Kernrekonstruktion und ihre Rückwirkung, der exakte Momentträger gegenüber seinem Polynom und die übrigen Gamma-, Formwirkungs- und Quellenfehler. Jede bereits bezahlte Abweichung muss eindeutig zugeordnet werden. Die gerade Rechnung allein begründet diesen Anschluss in der ungeraden Parität nicht.

Eine konkrete hinreichende Kombination ist $I_{\rm Streifen}\le3\cdot10^{-8}$ und $e_{\rm phys}\le5\cdot10^{-6}$. Dann gilt

```math
\|r_o\|_{L^*}\le
\sqrt{\tfrac5{21}(2{,}672\cdot10^{-12}+I_{\rm Streifen})}
+1{,}674\cdot10^{-8}+7{,}757\cdot10^{-10}+e_{\rm phys}
<8{,}954\cdot10^{-5}<9\cdot10^{-5}.
```

Diese beiden Zahlen sind verfügbare Budgets. Für die tatsächlichen Werte fehlen noch die gerichteten Obergrenzen. Der vollständige Quotientenvergleich und die Ausgabe von $U_{11}$ setzen weitere Nachweise voraus. [Rationale Prüfung des Budgets](domain_check.py)

## Reproduktion

Die Grundlage ist der Commit `0cc0da92891b09e417bfe1bd14f2b2f3cffd27a4`. Die Eingabebindungen werden durch die veröffentlichte Vorprüfung, die Originaldaten des Oktober-Zertifikats und die Git-Blob-IDs fixiert. Die Prüfer verwenden Python und `python-flint==0.9.0`. Beim Checkout müssen die Originalbytes einschließlich Zeilenenden erhalten bleiben. [Eingabebindungen der Vorprüfung](../EINGABEBINDUNGEN.json) · [Dateibindungen dieser Feldrechnung](QUELLEN.json)

Beispiel für eine POSIX-Shell aus diesem Ordner im vollständigen Checkout. Das Ausgabeverzeichnis wird frisch angelegt. Die Zahlen sind direkt in den verlinkten JSON-Dateien einsehbar.

```sh
repo=$(git rev-parse --show-toplevel)
out=$(mktemp -d)
python odd_field_control.py "$repo" ../ERGEBNIS.json "$out/control.json" --nodes 64 --outer-nodes 48
python transport.py ../ERGEBNIS.json "$out/transport.json"
python features.py "$repo" ../ERGEBNIS.json "$out/control.json.gz" "$out/transport.json" "$out/features.json"
python panels.py "$repo" "$out/control.json.gz" "$out/panels.json" 5
python core_price.py "$repo" "$out/control.json.gz" "$out/core.json" 5
python endpoints.py "$repo" "$out/control.json.gz" "$out/endpoints.json" 5
python domain_check.py "$repo" "$out/control.json.gz" "$out"
```
