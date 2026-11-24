# Fester ungerader Zeuge im Übergang A9 → A11

24. November 2026. Projektinterner Nachweis unter den unten angegebenen Form- und Quellenverträgen. Externe Gegenprüfung offen.

Für den ungeraden Zeugen, die äußere Antwort, den rationalen Zwölferblock und den inneren Vektor aus der [endlichen Vorprüfung](../BEWEIS.md) ergibt sich

```math
 \langle r_o,R_Lr_o\rangle \le 5{,}4126542\cdot10^{-13},
 \qquad K_P[e_o]-\langle f,Q_o^{-1}f\rangle\ge 7{,}4034790876\cdot10^{-8}.
```

Der Nachweis reicht über die ganze alte Schale für diese eine Quelle. Für den endlichen Quotienten fehlen die gerichtete gemeinsame Matrix und ihre Hochraumkorrektur. Die Inversausgabe $U_{11}$ bleibt offen. [Gerichtete Endpunkte](ZEUGE.json) · [Rationaler Schlussprüfer](witness_check.py)

| Größe | Sichere obere Grenze |
|---|---:|
| Innenbereich, quadrierte Modellnorm in $X$ | $2{,}072\cdot10^{-12}$ |
| Gesamter linker Rand ab dem Innenbereich | $7{,}00\cdot10^{-14}$ |
| Gesamter rechter Rand ab dem Innenbereich | $2{,}51\cdot10^{-14}$ |
| Ganze quadrierte Modellnorm, aus den ungerundeten Preisen | $2{,}16639714\cdot10^{-12}$ |
| Diskretes zu kontinuierlichem innerem Modell, Dualnorm | $1{,}674\cdot10^{-8}$ |
| Bereits bezahlter gemeinsamer endlicher Kraftfehler, Dualnorm | $7{,}757\cdot10^{-10}$ |
| Übriger Anschluss an die tatsächliche Quelle, Dualnorm | $1{,}0537\cdot10^{-16}$ |
| Gesamte Dualnorm | $7{,}35707426\cdot10^{-7}$ |

## 1. Daten und Reichweite

Es gelten die geerbten Domänen und Momentadjungierten der physischen Nichtpolform, die positiven alten Unterformen und ihre Ordnung, die physischen Quellen- und Fehlergrame für die gebundenen **ungeraden** Familien $F,J,\Phi$, die Fehlerverträge der festen Antwort sowie $L\succeq(21/5)W_X$ auf $T$. Die ursprünglichen physischen Großintegrationen dieser Daten werden als Projekteingaben verwendet. Die beiden neuen Randrechnungen, der Aufbau der ungeraden Fehlerbilanz und die skalare Abnahme wurden hier ausgeführt. Der zusätzliche Replay der endlichen Vorprüfung mit 1024 Bit ergab dieselben Ergebnisbytes, SHA-256 `2577a74a005ca4c8b4c825b2aa803b95efdfe90076bd2c440bfab063d11106e2`. Die früheren Modell-, Innen-, Quadratur- und Kraftbelege stammen vom Elternstand. [Eingaben der Vorprüfung](../EINGABEBINDUNGEN.json) · [Gebundene Feldquellen](QUELLEN.json) · [Teilrechnung am Elternstand](https://github.com/Waschtl904/objekt-x-programm/blob/00806f873e8246bac03b35d9bd4ab5ac9bbb4810/handoffs/a9-a11-ungerader-restvergleich-2026-11-24/feldrechnung/README.md)

Es sei $a=3\log(2)/2,\ b=\log3,\ X=L^2((a,b),2\,dx)$. Der negative Flügel ist durch ungerade Spiegelung erfasst. In allen drei Ortsintegralen wird schon das Maß $2\,dx$ verwendet. Die Randintervalle reichen von der Grenze der früheren elf Innenabschnitte **bis zum jeweiligen Endpunkt**. Die früheren äußersten Randpreise und die Pilotabschnitte sind deshalb vollständig in diesen Intervallen enthalten.

## 2. Gemeinsame Randrechnung

Als Pilot wurden links und rechts die dyadischen Tiefen 6, 7 und 8 sowie getrennt Tiefe 24 mit dem bisherigen Taylorverfahren eingeschlossen. Die Ordnungen reichen von 688 bis 720. Der Aufwand pro Abschnitt lag hier bei etwa 14 bis 21 Sekunden. Die folgenden zwei Rechnungen ersetzen die Fortsetzung dieses Rasters. [Pilotdaten](pilot-strips.json) · [Prüfer](strips.py)

**Rechts.** Für $v=b-x$ auf der gesamten restlichen Breite $D_r$ hat das signierte Feld die Form $A(x)+B(x)\log v$. Im Momentterm schreibt man $\log(1-e^{-kv})=\log v+\log((1-e^{-kv})/v)$ für $k=1,2$. Der Quotient ist auch bei null analytisch, wie seine Integraldarstellung $k\int_0^1e^{-kvt}\,dt$ zeigt. Der Prüfer sichert positiven Realteil für den Logarithmus des Quotienten. Der lokale Potentialterm und die globalen ungeraden Testfunktionen liefern die weiteren linearen Logarithmen. Die integralen Kernterme sind rechts vom inneren Kern analytisch. Für jede Primwirkung wird die auf der offenen äußeren Zelle gültige Formel fortgesetzt.

Ersetzt man $\log v$ in dieser Darstellung einmal durch 0 und einmal durch 1, erhält man zwei reguläre gemeinsame Funktionen. Ihre Taylorpolynome liefern $A,B$ samt getrennten gerichteten Resten. Für $u=v/D_r$ wird das signierte Quadrat über $0<u<1$ integriert. Die Gewichte ergeben sich aus $\int_0^1u^n(\log u)^jdu=(-1)^j j!/(n+1)^{j+1}$. Auch der Fehler des Koeffizienten von $\log v$ wird in der vollständigen gewichteten Norm integriert. [Rechter Randpreis](right-edge.json) · [Prüfer](right_edge.py)

**Links.** Für $v=x-a$ trennt man aus der gespeicherten inneren Gaußmaß-Darstellung zunächst die rationalen Cauchyterme mit den **vorzeichenbehafteten** Gewichten ab. Der übrige Ausdruck lautet $A(v)+B(v)\log v+C(v)(\log v)^2$ mit auf dem gesamten linken Restintervall analytischen Koeffizienten. Hier entsteht das Quadrat des Logarithmus aus der Cauchywirkung einer inneren Randlogarithmusdichte. Insbesondere gilt bei $s=1+t,\ t=v/a$ für $I_r(s)=\int_0^1\log|y-r|/(s-y)\,dy$

```math
 I_1(1+t)=-\frac{\pi^2}{6}-\frac12\log^2t-\operatorname{Li}_2(-t).
```

Die anderen drei Logarithmuswurzeln haben positiven Abstand von 1. Mit $g(s)=\log|s-r|$ (reeller Zweig, analytisch fortgesetzt) ist $J=I_r+g\log t$ dort regulär. Aus der Cauchyformel des Feldprüfers ergibt sich

```math
 J'(s)=\frac{g(s)-g(1)}t+\frac{\log |r|}s+
           \frac{g(1)-\log |r|+\log s}{s-r}.
```

Der erste Quotient ist durch $1/(|1-r|-|t|)$ begrenzt. Ein Innenwert und die Ableitung begrenzen $J$ auf dem Kontrollkreis. Der reflektierte Cauchyterm ist dort regulär, da sein Argument nahe $-1$ außerhalb der Integrationsstrecke liegt. Die affinen Randlogarithmen im Primkanal beruhen auf $\log8=2a$. Die ersetzten affinen Argumente haben Betrag $v/a$.

Einsetzen von $0,1,-1$ für $\log v$ gibt die drei regulären Kombinationen. Jeder Taylorrest wird bezahlt, ebenso der beim Kürzen des Polynoms entstehende Koeffizientenschwanz. Auf den verbleibenden dyadischen Abschnitten werden die Cauchyatome **mit ihren Vorzeichen** per geometrischer Reihe wieder hinzugefügt. Der Reihenquotient ist höchstens $1/3$. Dann erst wird das gemeinsame Polynom quadriert. Für das tiefste Endstück genügt die neue Hülle $349(1+|\log v|^2)$ für das Modell. Die vorige getrennte Hülle hatte einen Vorfaktor von etwa $1{,}3\cdot10^{22}$. Der linke Prüfer integriert 75 Abschnitte innerhalb der Restbreite und das äußerste Endstück. Auf beiden Seiten liefern drei direkte Feldauswertungen zusätzliche Vorzeichenkontrollen. [Linker Randpreis und Teilintegrale](left-edge.json) · [Prüfer](left_edge.py)

## 3. Vom Modell zum tatsächlichen Funktional

Wir verwenden $m(x)=\sinh(x/2),\ \mu=(\sinh a-a)/2$ und $\lambda(s)=\int_a^b m(x)s(x)\,dx$. Damit ist $\Lambda s=(-m\lambda(s)/\mu,s)$, $\|m\|_{H_8}^2=2\mu$. Für den kurzen ersten ungeraden Legendrevektor $e(x)=\sqrt{3/(2a)}\,x/a$ bezeichnet $M$ in isometrischen Kernkoordinaten die schräge Abbildung $I-e\otimes m/\langle m,e\rangle$. Der Vergleich erfolgt auf tatsächlichen Testfunktionalen. Für ein rohes Feld $g$ gilt auf $T$ die variationale Abschätzung $\|g\|_{L^*}\le\sqrt{5/21}\|g\|_X$.

Am festgelegten $u=Jw_o$ ist
```math
 r_o[t]=\langle\Lambda_Tt,f\rangle-(1-\eta)q[t,u]
       -\langle gt,U_8(h-gu)\rangle-\langle at,K_o^{-1}(v-au)\rangle .
```
Die zwei endlichen Kräfte werden zuerst in ihrer gemeinsamen Metrik durch ihre gespeicherten Vertreter ersetzt. Der Fehler dieser Änderung ist im früheren Kraftpreis enthalten. In den nachfolgenden Schritten bleiben beide Vertreter fest. Für die Zwölferkraft verwendet der Feldaufbau die signierte Koordinate $p_0=K_o^{-1}(a_u-v)$ als Modell. Daher erscheinen im ersten inneren Aufruf $Jw-Fp_0-\Phi ff$ und im zweiten $Fp_0-(1-\eta)Jw$. Die vier globalen Funktionen im Anteil $F$ erstrecken sich über den vollständigen alten Raum.

| Übergang | Kontrolle im ungeraden Fall |
|---|---|
| Antwortquelle $h$ zum gespeicherten Feld | Der D12-Fehler mal der Norm der festen Antwort ist durch den historischen Hilbertpreis gedeckt. Hinzu kommen der Gamma360-Preis, die frische T-Mittelpunktabweichung und die Normalisierung des Zeugen. Der neu berechnete T-Fehler liegt unter dem bezahlten historischen Preis. Gemeinsame Momentanteile verschwinden unter $M^*$, $\Phi^*$ und $\Lambda^*$. |
| $J,Y$ und rationaler Variationsvektor | Die historischen Koordinatenfehler werden in den orthonormalen lokalen Koordinaten gemessen. Der zusätzliche Vergleich der 8 832 gespeicherten $J,Y$-Koordinaten mit ihren rationalen Mittelpunkten ist exakt. Die erneute Rundung von $w_o$ kostet weniger als $5\cdot10^{-923}$ in der Dualnorm. Dafür gilt auf dem echten $J$ die Formschranke $0\preceq H_o\preceq q\preceq C_L L$, und die Spalten haben Grad höchstens 95. |
| Reelle Gammaoperatoren | Für eine gleichmäßige Kernelabweichung $\epsilon$ auf dem ganzen Fenster mit Halblänge $d$ genügt die Operatornorm $2d\epsilon$. Die Kernbasis $\Phi$ benutzt die alten Grad-160-Koeffizienten, die Schalenwirkung und die globalen Funktionen Grad 224. Auch die gespeicherten alten Koeffizienten werden mit der Taylorreihe verglichen. Die normierten Quellen werden mit ihren eigenen ungeraden Normschranken eingesetzt. |
| Niedrige und hohe Kerndaten | Der Fehler der vollständigen rohen Kernquelle und der Fehler ihrer 191 niedrigen Koordinaten werden separat eingeschlossen. Der gespeicherte niedrige Vektor wird gegen $c_Jw-\ell_h c-c_Fp_0-Aff$ einschließlich der Intervallradien von $A$ verglichen. |
| Direkte Wirkung auf der Schale | Die reine Schalenwirkung auf die Basisabweichung wird im Grad-95-Raum abgeschätzt, mit dem Legendrepreis, dem logarithmischen Randpotential, regulärem und reflektiertem Kern. Die Kreuzwirkung und der skalare Momentadjungierte sind eingeschlossen. Die so verwendete Operatorgrenze liegt unter 153. |
| Innere Gaußquadratur | Der Übergang von der kontinuierlichen Kerndichte zum diskreten Modell ist der separate Preis aus dem früheren Feldbeleg. Er enthält singuläre und reflektierte Kopplung, reguläre Faltung und Momentpaarungen. |

**Hohe Rekonstruktion.** Für die gemeinsame wahre Kernquelle $s$, die Einbettung $E$ der 191 niedrigen Koordinaten und $c_s=\Phi^*s$ gilt $y=P_{\rm hoch}M^*Us=M^*Us-Ec_s$ in isometrischen Koordinaten. Die Differenz zur rohen Modellrekonstruktion kostet höchstens $\sqrt\gamma\,\|\Delta s\|+\|\Delta c_s\|$ einschließlich der niedrigen Mittelpunktabweichung. Hier ist $\gamma=\|M\|^2$. Die ungerade äußere Kreuzwirkung einschließlich Momentadjungiertem ist durch $\|B\|+\|\lambda\|\|Q_8m\|/\mu<17{,}152$ begrenzt. Nach Division durch $\delta$ ergibt sich ein roher Schalenfehler unter $2{,}154\cdot10^{-16}$. Der letzte hohe Lift wird separat an **$y$ selbst** bezahlt. Dieser Vektor ist orthogonal zu allen ungeraden Graden bis 383. Daher ist $|\langle m,y\rangle|\le\|m-m_{160}\|\|y\|$, und $\|(M-I)y\|\le\|m-m_{160}\|\|y\|/|\langle e,m\rangle|$. Ein Energiepreis auf nur 191 Koordinaten wäre keine Begründung dafür. [Quellen- und Koordinatenprüfer](source_bridge.py) · [Gerichtete Fehler](source-bridge.json)

**Momentwechsel im kontinuierlichen Modell.** Setze $m_0=m_{160}$, $d=m-m_0$. Funktionswert und räumliche Ableitung des Taylorrests sind durch $2/160!$ begrenzt. Der singuläre Legendre-Differenzoperator auf dem Kernintervall ist auf diesem Rest punktweise durch $a\|d'\|_\infty$ beschränkt. Zusammen mit Potential, regulärem Kern und Translationen ergibt das eine ganze Schranke für $Q_{8,K}d$ im verwendeten endlichen Kernelmodell $K$. Für die beiden inneren Aufrufe seien $\lambda_1,\lambda_2$ die Momente der jeweiligen Schalenkomponenten. Die Änderungen der rohen Kernbilder sind $\Delta g_i=-\lambda_i Q_{8,K}d/\mu$. In der ersten Kernrekonstruktion gilt

```math
 \Delta u=\delta^{-1}(\Delta g_1-\Delta\alpha\,m-\alpha_0d),\qquad
 |\Delta\alpha|\le\|\Delta g_1\|/|\langle e,m\rangle|.
```

Der Nenner ist in beiden Modellständen derselbe exakte ungerade Momentwert. Der zweite Aufruf liefert das Moment von $g_2$. Für dieses Moment verwendet man $\langle d,g_{2,0}\rangle+\langle m,\Delta g_2\rangle$. Für die Rückwirkung gilt $\langle\Delta u,Q_{8,K}m\rangle+\langle u_0,Q_{8,K}d\rangle$. In der Halbintervallintegration ist jeweils der Faktor $1/2$ gegenüber dem physischen Skalarprodukt zu berücksichtigen. Zur äußeren Wirkung auf $\Delta u-\lambda_2d/\mu$ tritt der Wechsel des gemischten direkten Primterms hinzu, der im Code den exakten sinh-Träger verwendet. Auf diese Weise bleiben auch die gemischten Fehler erfasst. Die ganze Modellnorm von $u_0$ wird für diesen Vergleich und den äußeren Gammafehler neu auf der ungeraden Seite begrenzt. Die Kerndichte $h$ wird dazu in jeder tatsächlichen Primzelle eingeschlossen. [Moment- und Rückwirkungsprüfer](moment_bridge.py) · [Gerichtete Endpunkte](moment-bridge.json)

Alle algebraisch identischen Umordnungen benutzen die gebundenen Zellen und die beiden ungeraden Gammaorientierungen des Feldaufbaus. Für die hohe Kernrekonstruktion, den endlichen Krafttransport und die direkte Dichte kann derselbe physische Quellenfehler in verschiedenen Summanden wirken. Die oben angegebenen Dreiecksabschätzungen bezahlen diese Wirkungen jeweils dort. Mit diesen Übergängen ist der Restpreis von Modell zu tatsächlichem Funktional unter den genannten Projektvoraussetzungen eingeschlossen.

## 4. Abnahme am Zeugen und Reproduktion

Die drei räumlichen Preise werden als quadrierte Normen addiert. Nach der Quadratwurzel kommen die Preise für Kernquadratur, endliche Kräfte und physische Modellwechsel in der Dualnorm hinzu. Für $d=\|r_o\|_{L^*}^2$, die endliche Restnorm $z$, $c_o$ und $\beta$ gilt das restzentrierte Inverslemma

```math
 \langle f,Q_o^{-1}f\rangle\le F_{\rm up}
       +\frac{d/\beta+z^2+2z\sqrt{c_od/\beta}}{1-c_o}.
```

Mit den rationalen Eingaben folgt eine obere Grenze von $5{,}206741644265\cdot10^{-6}$. Der Abstand zur unteren tatsächlichen Zeugenbudgetgrenze ist positiv. Die externe Prüfung der analytischen Ableitungen und der geerbten Grundlagen bleibt offen.

Die JSON-Dateien sind im Browser direkt lesbar. Für einen Replay werden die gebundenen Projektdateien im Original-Byteformat, Python und für die Feldprüfer `python-flint==0.9.0` benötigt. Für den kurzen Endpunktprüfer genügt die Python-Standardbibliothek. Aus diesem Ordner:

```sh
python witness_check.py . ../ERGEBNIS.json /tmp/ungerader-zeuge.json
```

Für den vollständigen Replay zuerst die Anweisungen im [Feldaufbau](README.md) in einem frischen Ausgabeverzeichnis ausführen. Mit den dort eingeführten Shellvariablen:

```sh
python strips.py "$repo" "$out/control.json.gz" "$out/pilot-strips.json" 6,7,8,24
python right_edge.py "$repo" "$out/control.json.gz" "$out/right-edge.json" 5
python left_edge.py "$repo" "$out/control.json.gz" "$out/left-edge.json" 5
python source_bridge.py "$repo" ../ERGEBNIS.json "$out/control.json.gz" "$out/transport.json" "$out/source-bridge.json"
python moment_bridge.py "$repo" "$out/control.json.gz" "$out/moment-bridge.json" 5 "$out/source-bridge.json" "$out/transport.json"
python witness_check.py "$out" ../ERGEBNIS.json "$out/ZEUGE.json"
```
