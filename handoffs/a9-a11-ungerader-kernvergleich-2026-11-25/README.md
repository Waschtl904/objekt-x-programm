# A9 → A11 mit einer stärkeren gemeinsamen Kernunterform

25. November 2026. Ungerade Parität, äußere Antwort und normalisierte Tests $e,s$ aus dem [Elternbefund](../a9-a11-ungerader-zweiraum-2026-11-25/README.md). Die Rechnung verwendet die dort ausgewiesenen Form-, Quellen-, Quadratur- und Inversverträge. Unabhängige Begutachtung offen. Der bekannte A11-Terminalbefund geht in keine Auswahl und keinen Vergleich ein.

**Ergebnis.** Die neue Regel ist auf dem gesamten festen ungeraden Zweiraum positiv. Die vollständige Determinante nach Abzug der alten Inversenergie liegt über $3{,}16512\,10^{-11}$. Die Kopplung dieses Zweiraums an den neuen Hochraum und die physische Inversausgabe $U_{11}$ bleiben offen. [Endpunkte](ABSCHLUSS.json)

## 1. Geordnete Kernreparatur

$B$ bezeichnet die tatsächliche ganze A8-Kopplung zwischen 191 niedrigen und allen hohen Koordinaten. Es gelten $\delta_0=1{,}8219$, $d=1{,}84298$, $T=C^*/\sqrt{1-\rho}$, $F_0=T^{-1}T^{-*}$. Benutzt werden die gerichteten Common96-Matrizen $F_8,H_B$ der **ungeraden** Parität. Der Common96-Prüfer rundet $F_{\rm old}+H_{B,\rm old}/\delta_{\rm old}-H_B/\delta_0$ rational nach unten ab. Die ersten beiden Summanden zusammen sind der geerbte niedrige Boden. Somit $A_{\rm low}\succeq A_L=F_8+H_B/\delta_0$. Weiter $F_8\succeq F_0$, $H_B\succeq BB^*$ und $A_{\rm high}\succeq d I$. Es gelten die physischen Koordinaten der alten Zerlegung. [Common96-Konstruktion](../../research/x-c1/a8-a9-global-closure-2026-10-13/packages/objekt-x-direkte-restform-und-positiver-96er-block-2026-10-11/refine_old_majorant.py) · [Alter hoher Boden](../../research/x-c1/a8-a9-global-closure-2026-10-13/packages/objekt-x-alte-hohe-reserve-2026-10-08/HERLEITUNG.txt) · [Block- und Formordnung](../../research/x-c1/w9-grad11-new-comparison-even-2026-10-26/proofs/FULL_FORM_ORDER.txt)

$$
 A_{\mathrm{eff},0}=
 \begin{pmatrix}F_0+BB^*/\delta_0&B\\B^*&\delta_0I\end{pmatrix}
 \preceq A_*=
 \begin{pmatrix}A_L&B\\B^*&dI\end{pmatrix}
 \preceq A_8 .
$$

Für beide Differenzen verschwinden die Kreuzblöcke. Die erste hat niedrigen Block $F_8-F_0+(H_B-BB^*)/\delta_0$, die zweite $A_{\rm low}-A_L$. Die positiven hohen Differenzen folgen aus den angegebenen Böden. Ersetze in der vollständig wiederhergestellten alten Schale nur den effektiven Kern durch $A_*$. Die alte Kern-Schalen-Kopplung und der ganze direkte Schalenblock bleiben physisch. Für diese Form $Q_*$ folgt unter den geerbten Domänenverträgen $0<Q_o\preceq Q_*\preceq A_9$. Damit ist $A_9^{-1}\preceq Q_*^{-1}\preceq Q_o^{-1}\preceq W_9$. Das überträgt den positiven ungeraden Einzelzeugen und den Boden $0{,}58 W$ auf $Y_o$. Dies ist ein gemeinsamer Operatorvergleich.

Für den alten fixierten Variationsvektor $(y,w)$ wurde die gemeinsame physische Quelle $j=h-g_Fy-g_Jw$ gebildet. Der nach unten gerichtete Gewinn gegenüber $U_8$ auf genau dieser Quelle ist größer als $0{,}00558833$, die obere Grenze kleiner als $0{,}00563432$. Benötigt waren mehr als $0{,}00366594$. Mit derselben stärkeren niedrigen Matrix und $d=\delta_0$ liegt der Gewinn bereits über $0{,}00558785$. Die gesondert getestete Hochbodenvariante mit normierter niedriger Schurmatrix $I+(1/\delta_0-1/d) T H_B T^*$ gewinnt weniger als $0{,}000088$. Die ausgeschlossene alte Regel und ihre negative Richtung bleiben gültige Regressionen.

## 2. Gerichtete Rechnung am ganzen Kern

Für eine Kernquelle $(\ell,h)$ setze $t=T(\ell-Bh/\delta_0)$, $u=(\delta_0/d)t+(1-\delta_0/d)T\ell$. Die exakte Energie lautet

$$
 \|h\|^2/d+u^*[T(A_L-BB^*/d)T^*]^{-1}u .
$$

Sei $G_0=B_0B_0^*$ der alte modellierte Kopplungsgram und $\|B-B_0\|\le e_B$. Bei $\tau=10^{-16}$ gilt
$$
 (1-\tau)G_0-(\tau^{-1}-1)e_B^2 I
 \preceq BB^*\preceq
 (1+\tau)G_0+(1+\tau^{-1})e_B^2 I .
$$
Beide Matrizen werden mit $T$ transformiert. Der niedrigere numerische Nenner hat Boden mindestens $1-(1+\tau^{-1})e_B^2\operatorname{tr}(TT^*)/\delta_0>0{,}99$, da die alte Zeilenrundung und das größere Young-Gewicht in $H_B$ den Modellgram decken. Ein Quellenfehler $\epsilon$ in $u$ kostet daher höchstens $\epsilon/\sqrt{1-\mathrm{loss}}$ in der inversen Norm. Die beiden gewichteten Quellen $t$ und $T\ell$ sowie die rohe hohe Norm werden getrennt durch die Quell- und Projektionsfehler aus den gebundenen Oktoberdateien eingeschlossen. Die Subtraktion zweier Energien der Größenordnung $10^{14}$ erfolgt an den rationalen Endpunkten der gerichteten Rechnung. [Numerischer Prüfer](kern.py) · [Eingabebindungen](bindungen.py) · [Ergebnis](ENERGIE.json)

## 3. Gemeinsame Rechnung auf zwei äußeren Tests

Im alten Schalenraum aus zwölf F- und 84 J-Koordinaten wurde für jeden äußeren Test eine Antwort aus dem gemeinsamen neuen 96er Mittelpunktsystem gewählt und anschließend auf ein rationales Raster $10^{-45}$ eingefroren. In den folgenden Tests ist der Kern exakt eliminiert. Für äußere Quelle $f_i=Ri$ und feste Schalenantwort $v_i$ bezeichnet $V_i$ die volle Antwort, deren Kernanteil $A_*^{-1}(h_i-gv_i)$ ist. Mit $r_i=f_i-Q_*V_i$ (als Formdualquelle) ist die tatsächliche Inversenergie gleich dem Variationswert $F_i$ plus $\|r_i\|_{Q_*^{-1}}^2$. Dabei ist $F_i=2\operatorname{Re}f_{\mathrm{Schale},i}[v_i]-D[v_i]+\|h_i-gv_i\|_{A_*^{-1}}^2$.

Dieselbe Identität gilt polarisiert: Die gesuchte Zweiermatrix ist $K_P-F-\mathrm{Gram}_{Q_*^{-1}}(r_e,r_s)$. Alle Rechnungen erfolgen auf reellen Tests und reellen Operatoren. Die gemischte Stelle von $K_P$ wurde neu auf zwei rationalen Summen mit exakter Rücknormierung integriert. Die gemischte Stelle von $F$ wurde mit denselben eingefrorenen Antworten aus den Richtungen $s\pm512e$ rekombiniert. In beiden Fällen blieben die Fehler der physischen Paarungen enthalten. Die Intervallenden für verschiedene Richtungen dürfen voneinander unabhängig nach außen genommen werden. [Direkter Kreuzterm](MISCHBUDGET.json) · [Integration](mischbudget.py)

| Größe | Gerichteter Wert |
|---|---:|
| $F_s$ | $[3{,}73831899,\,3{,}73834275]$ |
| $F_e$ | $[5{,}18296245,\,5{,}18305059]\,10^{-6}$ |
| $(K_P-F)_{ee}$ | $>9{,}77258\,10^{-8}$ |
| $(K_P-F)_{ss}$ | $>0{,}00185751$ |
| $\lvert(K_P-F)_{es}\rvert$ | $<0{,}000012238$ |
| $\det(K_P-F)$ | $>3{,}17618\,10^{-11}$ |

Eine hinreichende gemeinsame Abnahme ist $\|r_e\|_{Q_*^{-1}}^2\le10^{-9}$ und $\|r_s\|_{Q_*^{-1}}^2\le10^{-4}$. Die gemischte Restenergie ist dann im Betrag höchstens $\sqrt{10^{-13}}<3{,}17\,10^{-7}$. Beide Diagonalen bleiben positiv, die Determinante der vollständigen Zweiermatrix liegt dann über $1{,}23724\,10^{-11}$. Der rationale Prüfer verwendet ungerundete Endpunkte. [Endpunktprüfung](endpunkte.py)

Zusätzlich wurde die schwächste Richtung eines modellierten äußeren Grad-11-Systems rational eingefroren und mit einer neuen gerichteten direkten Integration geprüft. Der eingeschlossene Abstand zwischen Budget und gewähltem Variationswert enthält null. Dieser Test entscheidet das Vorzeichen im vollen Grad-11-Raum nicht. [Direkter Test](KANDIDAT.json) · [Rechnung](kandidat.py)

## 4. Preis der vollständigen Restquellen

Die Quellen $r_i$ haben nach der exakten Kernantwort Kernkomponente null. Schreibe die verbleibende Wirkung in den alten F- und T-Koordinaten als $(r_F,r_T)$, mit zwölf F-Koordinaten und dem ganzen alten Restformraum T. Dieser Rest betrifft die alte Schale. Die Kopplung an $Y_o$ in der neuen Schale ist eine spätere Aufgabe.

**Restmerkmale.** Die beiden endlichen Preise sind $b_F=\|r_F\|_{K_o^{-1}}$ und $b_J=\|J^*r_T\|_{P_{\rm upper}}$. Für beide werden dieselben 96 Antworten wie im gerichteten Variationswert eingesetzt. Die Modellkraft ist die äußere Kraft minus die direkte Formwirkung plus die Rückwirkung der gemeinsamen Kernquelle. Für eine positive Gewichts-Matrix $M$ und einen Fehlergram $E$ reicht $\sqrt{\operatorname{tr}(ME)}$ für die gemeinsame gewichtete Abbildung. Für zulässige $-D_w\preceq D-D_m\preceq D_w$ kostet der direkte Fehler im Zielblock $I$ höchstens $\sqrt{\operatorname{tr}(M(D_w)_{II})}\sqrt{v^*D_wv}$. Hier ist $D_w=(D_+-D_-)/2$. Dieselbe polarisierte Abschätzung wird für die Differenz zum modellierten inversen Schurblock verwendet. Die Differenz der beiden inversen Hüllen liefert eine positive Matrix, die beide Vorzeichen deckt. Für die hohen und niedrigen Quellenfehler werden zusätzlich tatsächliche Modellnorm, Argumentfehler und ihr Produkt bezahlt. Die Normen betreffen die vollständigen physischen Koordinaten. [Merkmalsprüfer](restmerkmale.py) · [Preise je Fehlerquelle](ENERGIE.json)

**Ganze Wirkung auf T.** In der ungeraden Feldrechnung ist die Zwölferkoordinate $p=-y$, die 84er-Koordinate $w$ und die direkte Schalenwirkung hat $\eta=0$. Im niedrigen Kerngleichungssystem ersetzt die neue gemeinsame Inverse die frühere. Der hohe Nenner ist $d$. Die physische Rückwirkung rekonstruiert weiter mit der tatsächlichen alten Form und deren Gamma- und Primkopplungen. Obergrenzen der quadrierten Modellnorm stammen aus elf gerichteten Innenintervallen und den zwei signierten logarithmischen Endpunktrechnungen. Alle drei Teile benutzen dieselbe zwischengespeicherte Modellfunktion. Die punktweisen Quadraturvergleiche in den Diagnoseausgaben gehen in keine Obergrenze ein. [Feldaufbau](feldprobe.py) · [Intervall- und Randprüfer](modellpreis.py) · [Physische Quellenprüfung](quellpreis.py)

Für die tatsächliche niedrige Lösung sei $N=T(A_L-BB^*/d)T^*$, $N_m$ die Modellmatrix und $\hat\eta=T^{-*}ff$ der gespeicherte niedrige Vektor bei der Vorzeichenwahl des Feldprüfers. Gegen das gerichtete Modell $u_m$ wird der Defekt $u_m-N_m\hat\eta$ gemessen. Die Quellabweichung wird wie in §2 bezahlt. Für den Matrixfehler setze $H=(G_+-G_-)/d$ in normierten Koordinaten. Aus $-H\preceq N-N_m\preceq H$ folgt
$$
 \|(N-N_m)\hat\eta\|^2\le\operatorname{tr}(H)\,\hat\eta^*H\hat\eta .
$$
Die korrigierte Kernantwort zu einem niedrigen Lösungsfehler ist der Graphvektor $(x,-B^*x/d)$. Seine $A_*$-Energie ist die $N$-Energie des normierten Fehlers. Wegen $N\succeq I$ genügt die Norm des gesamten Gleichungsdefekts als Normpreis. Für einen alten T-Test gilt aus der positiven Kern-Schalen-Form $\|g_t\|_{A_*^{-1}}^2\le q[t]\le25L[t]$. Der oben bezeichnete Normpreis kostet im rückwirkenden Funktional höchstens das Fünffache. Das verwendet den echten hohen Graphanteil. Die Rundung der beiden alten Schalenkoordinaten kostet analog höchstens $5\sqrt{\Delta v^*D_+\Delta v}$ durch den positiven, von $D$ majorisierten alten Schalenschurblock.

Die übrige Brücke wiederholt für die tatsächlichen neuen Koeffizienten die Rekonstruktion der hohen Quelle, den Vergleich von exaktem $\sinh$-Moment und Polynom, den letzten Lift am hochorthogonalen Vektor, den Gammafehler und die innere Kernquadratur. Der alte Wert eines solchen Postens wird nicht als Zahl auf die neue Quelle übertragen. Die Zahl $u_T$ unten ist die Summe aus $\sqrt{(5/21)\,I_{\rm Modell}}$, innerem Quadraturpreis, übrigem physischem Anschluss und niedrigem Lösungsfehler. [Geerbter ungerader Form- und Quellenanschluss](../a9-a11-ungerader-restvergleich-2026-11-24/feldrechnung/FESTER_UNGERADER_ZEUGE.md)

| Obergrenze | $e$ | $s$ |
|---|---:|---:|
| Ganze rohe Modellnorm zum Quadrat | $2{,}156\,10^{-12}$ | $6{,}109\,10^{-8}$ |
| Oberer Preis $u_T$ für $\lVert r_T\rVert_{L^*}$ | $7{,}330\,10^{-7}$ | $1{,}207\,10^{-4}$ |
| $b_F$ | $4{,}969\,10^{-10}$ | $2{,}577\,10^{-7}$ |
| $b_J$ | $6{,}586\,10^{-10}$ | $3{,}454\,10^{-7}$ |

**Rückkehr in die volle alte Inversmetrik.** Aus $Q_*^{-1}\preceq Q_o^{-1}$ genügt eine Rechnung mit dem geerbten alten Inverslemma. Nach Eliminieren von F ist die Quelle $\nu=r_T-a^*K_o^{-1}r_F$, wobei $a$ der tatsächliche F/T-Kreuzblock nach alter Kernelimination ist. Dessen Energie erfüllt $\|a t\|_{K_o^{-1}}^2\le q[t]\le25L[t]$ durch Positivität der alten Unterform. Auf der tatsächlichen Basis gilt $L[J,J]\preceq8 I$, und absolute Zeilensummen liefern $\|P_{\rm upper}\|<26948$. Folglich genügen
$$
 w=u_T+5b_F,\qquad z=b_J+5\sqrt{8\|P_{\rm upper}\|}\,b_F
$$
als obere Preise für $\|\nu\|_{L^*}$ und $\|J^*\nu\|_{P_{\rm upper}}$. Die frühere 84er-Untergrenze lieferte den hier benutzten Basisvertrag. [Ungerade Basisprüfung](../a9-a11-ungerader-restvergleich-2026-11-24/vorpruefung/BEWEIS.md) · [Inverslemma und Blockzulässigkeit](../a9-a11-ungerader-restvergleich-2026-11-24/BEWEIS.md)

Mit $c_o=6967/10^6$ und $\beta=20209999981781/182190000000000$ folgt für beide Quellen einzeln
$$
 d_i=\|r_i\|_{Q_*^{-1}}^2
 \le b_F^2+\frac{w^2/\beta+z^2+2wz\sqrt{c_o/\beta}}{1-c_o}.
$$
Die gerichteten Endpunkte sind **$d_e<6{,}680\,10^{-12}$ und $d_s<5{,}325\,10^{-7}$**. In der gemeinsamen Matrix kostet der gemischte Rest im Betrag höchstens $\sqrt{d_ed_s}$. Aus den ungerundeten Preisen ergeben sich folgende vollständige Grenzen auf der Basis $(e,s)$.

| Größe der tatsächlichen Vergleichsform $\mathfrak S_*=K_P-R^*Q_*^{-1}R$ | Gerichtete Grenze |
|---|---:|
| $\mathfrak S_*[e]$ | $>9{,}7719\,10^{-8}$ |
| $\mathfrak S_*[s]$ | $>0{,}00185697$ |
| $\lvert\mathfrak S_*[e,s]\rvert$ | $<0{,}000012240$ |
| Zweierdeterminante | $>3{,}16512\,10^{-11}$ |

Damit ist der ganze feste ungerade Zweiraum unter den genannten Verträgen positiv. Die tatsächliche A11-Form wurde weder invertiert noch zur Wahl der Antworten verwendet. [Rationale Schlussrechnung](abschluss.py) · [Endergebnis](ABSCHLUSS.json)

## 5. Nächster Prüfgegenstand

Für die Erweiterung um $Y_o$ sei $G^Y=C_Y^*A_Y^{-1}C_Y$ der volle Preis der Kopplung der beiden äußeren Tests an diesen Hochraum. Hinreichend wären $G^Y_{ee}\le3\,10^{-9}$ und $G^Y_{ss}\le10^{-4}$. Dann gilt $|G^Y_{es}|\le\sqrt{G^Y_{ee}G^Y_{ss}}$, und die verbleibende Zweierdeterminante wäre größer als $2{,}9004\,10^{-12}$. Die beiden Hochkopplungspreise sind offen. Sie sind von den bereits eingeschlossenen Restenergien $d_e,d_s$ der **alten** Inversanwendung zu unterscheiden. Auch nach diesem Test bleiben die übrigen Quotientenrichtungen, beide ganzen Paritätsräume und die konstruktive physische Inversausgabe $U_{11}$ zu prüfen.

## Reproduktion

Die schnelle Schlussrechnung verwendet Python mit Standardbibliothek. Aus diesem Handoff-Ordner:

~~~text
python abschluss.py ../a9-a11-ungerader-zweiraum-2026-11-25/BUDGET.json ../a9-a11-ungerader-restvergleich-2026-11-24/ERGEBNIS.json
~~~

Für die Neuberechnung werden die Eingaben des gepinnten Repositorys, python-flint 0.9.0 und mpmath benötigt. Die Verzeichnisse ROOT, ALT und FELD stehen nachfolgend für den Checkout, den Zweiraum-Handoff des Elternstands und den Ordner feldrechnung im älteren ungeraden Handoff. K_ALT ist dessen benachbarte ERGEBNIS.json.

~~~text
python kern.py ROOT ALT/VARIATION.json ENERGIE.json --finite K_ALT
python mischbudget.py ROOT ENERGIE.json MISCHBUDGET.json
python kandidat.py ROOT ENERGIE.json KANDIDAT.json
~~~

Für jede Wahl (i,D) aus (e,E) und (s,S) sind getrennte Cache- und Ausgabepfade zu verwenden. Der Feldbau erzeugt zusätzlich zur Diagnose D_feld.json einen D_feld.json.gz-Cache. Dieser lässt sich aus den lesbaren Quellen wieder aufbauen.

~~~text
python feldprobe.py --case i FELD ROOT ENERGIE.json D_feld.json --nodes 64 --outer-nodes 16
python modellpreis.py FELD interior ROOT D_feld.json.gz D_interior.json 5
python modellpreis.py FELD left ROOT D_feld.json.gz D_left.json 5
python modellpreis.py FELD right ROOT D_feld.json.gz D_right.json 5
python modellpreis.py FELD core ROOT D_feld.json.gz D_core.json 5
python quellpreis.py ROOT FELD ENERGIE.json D_feld.json.gz D_quelle.json i
python modellpreis.py FELD moment ROOT D_feld.json.gz D_moment.json 5 D_quelle.json FELD/transport.json
~~~

Für den früher erzeugten s-Cache bindet der Prüfer zusätzlich die exakte Modellnutzlast der Pilotfassung. Deren überflüssige Referenzrechnung betraf nur die Diagnostikausgabe nach dem Aufbau des Modells. Prüfer, Ergebnisse und Beweis sind einzeln als Text lesbar. Die alten Ursprungsintegrationen und die übernommene Domänenkette wurden für diesen Handoff als Projekteingaben verwendet.

