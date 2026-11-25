# A9 → A11 · Zwei ungerade Richtungen entscheiden den Vergleich mit festem Kern

25. November 2026. Projektinterne Herleitung unter den Form-, Invers-, Quellen- und Fehlerverträgen des Elternstands [6c9eba9](https://github.com/Waschtl904/objekt-x-programm/commit/6c9eba92e0f13c21e6e4e9d97e9ac940159dc137). Die externe Prüfung und Punkt 4 sind offen.

Für die feste äußere Antwort $P$ und die verbesserte ungerade Majorante $Q_o^{-1}$ setze
$\mathfrak S[s]=K_P[s]-\langle Rs,Q_o^{-1}Rs\rangle$. Auf dem Zweiraum aus dem bisherigen Zeugen $e_o$ und dem unten angegebenen $s$ ist diese Vergleichsform **indefinit**. Außerdem scheitert bei festem $P,U_8$ der Vergleich, der den vollständigen physischen alten Schalenblock wieder einsetzt. Das Ergebnis betrifft die gewählten Vergleichsoperatoren. Die tatsächliche A11-Form und die Existenz eines anderen Zertifikats bleiben offen.

| Gerichteter Endpunkt | Wert |
|---|---:|
| Früherer Zeuge, untere Grenze für $\mathfrak S[e_o]$ | $7{,}4034790876\cdot10^{-8}$ |
| Neuer Zeuge, obere Grenze für $K_P[s]$ | $3{,}7402002545039$ |
| Neuer Zeuge, untere Grenze für $\langle Rs,Q_o^{-1}Rs\rangle$ | $3{,}7438933640601$ |
| Neuer Zeuge, obere Grenze für $\mathfrak S[s]$ | $-0{,}0036931095562$ |
| Obere Grenze für die Determinante in der Basis $(e_o,s)$ | $-2{,}73418\cdot10^{-10}$ |
| Vergleich am neuen Zeugen mit wiederhergestelltem altem Schalenblock | $<-0{,}00366594$ |

[Budget und Integrationsbeleg](BUDGET.json) · [Variationsbeleg mit beiden rationalen Testvektoren](VARIATION.json) · [Rationaler Endpunktprüfer](endpunkte.py)

## 1. Richtungen, Metrik und Auswahl

In der rohen orthonormalen Legendrebasis der neuen rechten Schale $(\log 3,\frac12\log 11)$, ungerade auf den linken Flügel fortgesetzt, verwende die Grade 0 bis 11 in aufsteigender Reihenfolge. Die zwölf ganzzahligen Koeffizienten sind

    -960, -1786, -1111, 735, 2564, 1686, -2634, -3352, 6471, -4543, 1858, -485

Der physische Test $s$ entsteht durch den gebundenen Momentlift und Division durch $\sqrt{c^*G_Wc}$ für diese Koeffizientenspalte $c$. Somit ist $W[s]=1$. Der alte Zeuge wird mit seinen eigenen unveränderten Koeffizienten und derselben physischen Norm verwendet. Bereits der Minor der ersten beiden Rohkoordinaten belegt lineare Unabhängigkeit.

Zur Auswahl wurde auf dem Modell des Zwölferraums die symmetrisierte Matrix aus Budget abzüglich endlichem Variationspreis in der Metrik $G_W$ diagonalisiert. Der Variationspreis enthält die Basisenergie und die auf $J$ restringierte innere Antwort. Die Richtung mit kleinstem Modelleigenwert wurde auf ganzzahlige Koeffizienten gerundet und vor den gerichteten Läufen festgelegt. Jede Eingangsgröße des Beweises wird für diese konkrete Richtung neu ausgewertet. Der explorative Eigenwert und die numerische Eigenvektorgüte gehen in keine Schranke ein.

Der Budgetprüfer verwendet den gebundenen direkten Integrator mit Nahnullpreis, 55 Abschnitten, 128 Gaußknoten pro Abschnitt, analytischen Resten, Gammaaußenschwanz, Primkorrelationen und Fehler der festen äußeren Antwort. Die Präzision beträgt 1536 Bit. [Budgetprüfer](budget.py) · [Historischer Integrator](../../research/x-c1/w9-partial-energy-2026-10-18/certify_k.py)

## 2. Eine gerichtete Untergrenze der vollständigen Inversenergie

Schreibe $f=Rs$, $h$ für seine Kernquelle, $v$ für die um den Kern ergänzte Zwölferquelle, $g$ für die Kernkopplung auf dem alten Rest und $a$ für den tatsächlichen Zwölfer-Kreuzblock. Verwende dasselbe $K_o$, dieselbe tatsächliche Testabbildung $J$ und $\eta=10^{-10}$ wie am positiven ungeraden Zeugen. Mit $u=Jw$ gilt in der alten Formdomäne

$$
\begin{aligned}
\nu &= \Lambda_T^*f-g^*U_8 h-a^*K_o^{-1}v,\\
H_o &=(1-\eta)q-g^*U_8g-a^*K_o^{-1}a,\\
F(w)&=\langle h,U_8h\rangle+\|v\|_{K_o^{-1}}^2
          +2\operatorname{Re}\nu[u]-H_o[u]
       \ \le\ \langle f,Q_o^{-1}f\rangle .
\end{aligned}
$$

Hier steht $a u$ für die Zwölferkraft des Tests $u$. Die Ungleichung gilt für jeden zulässigen Test. Der Prüfer löst das innere 84er-Mittelpunktproblem einmal und rundet seine Komponenten auf das rationale Raster $10^{-40}$. Die gebundene Domäne von $J$ macht diesen Test zulässig. Der vollständige Rest nach dem Test hat nichtnegative Inversenergie. Ein positiver Unterüberschuss entscheidet daher den Vergleich.

Der gerichtete Lauf mit 1024 Bit übernimmt die physischen Vollquellenverträge von [Common96 und der ungeraden Vorprüfung](../a9-a11-ungerader-restvergleich-2026-11-24/BEWEIS.md). Die Basisenergie wird nach Abzug des gemeinsamen Normfehlers nach unten quadriert. Der Rang-eins-Gram $ww^*$ kontrolliert den Fehler der einen Paarung $\nu[Jw]$. Für $q-g^*U_8g$ gehen der direkte Matrixeinschluss und die Modell- und Fehlergrame in Richtung $w$ ein. Für $\|a u\|_{K_o^{-1}}^2$ wird der volle lineare Kreuzfehler abgezogen. Der quadratische Fehler ist positiv. Der Term $\eta q[u]$ erhält die direkte untere Schranke. Die rohen Modellbeiträge von ungefähr $29202$ und $29200$ werden mit gerichteten Endpunkten verrechnet. Die tatsächliche Paarung, der Formtest und die inverse Ordnung stammen aus der alten Zertifikatskette. [Variationsprüfer](variation.py) · [Quellen- und Fehlerformeln](../../research/x-c1/w9-partial-energy-2026-10-18/assemble.py)

## 3. Entscheidung für die gemeinsame Matrix und die Hochraumkorrektur

Sei $b=\mathfrak S[e_o,s]$ die tatsächliche gemischte Paarung. Die beiden nachgewiesenen Vorzeichen ergeben für die hermitesche Zweiraummatrix

$$
\det\begin{pmatrix}\mathfrak S[e_o]&b\\\bar b&\mathfrak S[s]\end{pmatrix}
=\mathfrak S[e_o]\,\mathfrak S[s]-|b|^2
<-2{,}73418\cdot 10^{-10}.
$$

Das ist eine gemeinsame Aussage für jeden tatsächlichen Wert von $b$. Ein größerer Betrag des Kreuzterms macht die Determinante weiter negativ. Eine Zahl für $b$ wurde nicht ausgewertet. Beide äußeren Tests liegen in der Grad-11-Familie. Auf dem alten Hochraum $Y_p$ verschwinden das neue Moment und alle neuen rohen Legendrekoeffizienten unter 4096. Damit stehen die Tests in der physischen $W$-Metrik senkrecht auf $Y_p$. Der Hochblock bleibt durch die Ordnung $A_9^{-1}\preceq Q_o^{-1}\preceq W_9$ positiv. Das Minimieren über $Y_p$ kann den Wert in der neuen negativen Richtung nur weiter verringern, denn schon $y=0$ ist zulässig. Für diese Regel ist damit auch ein positiver voller Quotienten-Schurrest ausgeschlossen. [Hochraumbeweis](../../research/x-c1/a9-a11-hochblock-2026-11-23/A9-A11-Randkopplung-und-Hochblock-2026-11-23.md)

## 4. Was eine Verbesserung der alten Schale allein erreichen kann

Halte $U_8,P$, die tatsächlichen Kreuzblöcke und die Quelle fest. Setze in der alten Unterform den vollständigen Block $K_B=D_{FF}-\Psi_F^*\Psi_F$ und den vollständigen direkten $T$-Anteil einschließlich $\eta q$ wieder ein. Dies ist die Unterform mit demselben effektiven Kern wie zuvor und mit dem tatsächlichen alten Schalenblock. Die geerbte Blockzerlegung und $K_B\succeq K_o$, $\eta q\succeq0$ ergeben $Q_o\preceq Q_{\rm Schale}\preceq A_9$ auf den gemeinsamen Formdomänen. Für diese Aussage wird die bereits gebundene alte Formordnung vorausgesetzt. [Blockzerlegung](../../research/x-c1/w9-grad11-new-comparison-even-2026-10-26/proofs/FULL_FORM_ORDER.txt) · [Definition des physischen F-Blocks und Gramverträge](../../research/x-c1/w9-matrix-error-selection-2026-10-20/PROOF.md)

Nach der Kernreduktion hat für festes $w$ nur der Anteil $\|b_w\|_{K_o^{-1}}^2$ mit $b_w=v-a u$ die Zwölferantwort eliminiert. Öffne diesen Anteil wieder mit einem festen rationalen Zwölfertest $y$. Die Quadratidentität liefert den Variationswert für die wiederhergestellte Schale

$$
F_{\rm Schale}(w,y)=F(w)
 -\|b_w-K_o y\|_{K_o^{-1}}^2
 -y^*(K_B-K_o)y-\eta q[u].
$$

Dabei wird $y$ aus $K_o^{-1}(v_0-a_0u)$ auf das Raster $10^{-40}$ gerundet. Die Norm der gemeinsamen Kraftabweichung bezahlt den tatsächlichen Fehler von $v$, den direkten und den U-Featurefehler von $a u$ und die Rundung in der $K_o$-Norm. Für den Preis des Blocks sei $\Psi_F=\Psi_0+\Delta$, $U_F=\Psi_0^*\Psi_0$, $\Delta^*\Delta\preceq E_F$. Für das gespeicherte $0<\varepsilon<1$ liefert die untere Young-Schranke des Grams

$$
K_B\preceq D_{FF,+}-(1-\varepsilon)U_F+
                 (\varepsilon^{-1}-1)E_F .
$$

Hier ist $E_F$ der gerichtete vollständige F-Fehlergram der Blockkonstruktion. Für den gemischten Fehler von $a$ verwendet der Prüfer die größeren, hochfehlerüberdeckenden Grame der Vorprüfung. Die Auswertung der rechten Seite erfolgt an genau dem gespeicherten $y$. Es ergeben sich

| Oberer Preis | Sichere Grenze |
|---|---:|
| $\|b_w-K_o y\|_{K_o^{-1}}$ vor dem Quadrieren | $1{,}25\cdot10^{-7}$ |
| $y^*(K_B-K_o)y$ | $0{,}000023727346$ |
| $\eta q[u]$ | $0{,}000003436102$ |

Selbst nach diesen Abzügen ist $F_{\rm Schale}(w,y)-K_P[s]>0{,}00366594$. Jede positive alte Unterform unter $Q_{\rm Schale}$ mit derselben äußeren Antwort kostet im Inversvergleich mindestens ebenso viel. Insbesondere reicht eine beliebig genaue Auswertung des physischen F-Blocks und der direkten alten Restenergie bei festem effektiven Kern für diesen Zeugen nicht aus.

**Gezielter Test für eine andere Kernmajorante.** Setze für die gespeicherten $y,w$ die gemeinsame Kernquelle $j=h-g_F y-g u$ an. Nach Eliminieren des Kernvektors lautet sein Beitrag zum Variationswert $\langle j,U_8j\rangle$. Bleiben $P$, die physischen Quellen und Schalenblöcke fest, muss eine verbesserte zulässige Kernmajorante $U'_8$ auf genau dieser Quelle einen Preisrückgang von mehr als $0{,}00366594$ liefern, damit der Vergleich auf $s$ positiv werden kann. Das ist eine notwendige Bedingung. Eine Änderung der äußeren Antwort ändert auch $R$ und $K_P$ und benötigt ihre eigene Bilanz.

## 5. Regressionen und Reproduktion

Der rationale Abschluss des früheren **ungeraden** Zeugen erzeugte wieder die veröffentlichten Ergebnisbytes. Die rationale Rekombination des früheren **geraden** Zeugen lieferte dieselben Ergebnisdaten und eine Reserve $>1{,}66244453\cdot10^{-7}$ für seinen eigenen gekoppelten Untervergleich. Die dortige Blockverbesserung erhält ebenfalls die alte Inversordnung. Für den ganzen reellen geraden Grad-11-Raum existiert außerdem der getrennte Vergleich mit $Q_1^{-1}$ unter H1–H4. Die ungerade Rechnung verwendet durchgehend $Q_o^{-1}$ beziehungsweise die in §4 ausdrücklich definierte Verstärkung. [Ungerader Einzelzeuge](../a9-a11-ungerader-restvergleich-2026-11-24/feldrechnung/ZEUGE.json) · [Gerader Einzelzeuge](../../research/x-c1/w9-residual-centered-control-even-2026-10-21/whole/WHOLE_RESULT.json) · [Gerader Grad-11-Vergleich v2](../../research/x-c1/w9-grad11-new-comparison-even-2026-10-26/revision-v2/README.md)

Für den schnellen Endpunkttest genügt Standard-Python. Für die beiden gerichteten Rechenläufe wird zusätzlich python-flint 0.9.0 benötigt. Im unveränderten Repository-Checkout mit den gebundenen Originalbytes, aus diesem Ordner aufgerufen, lauten die Befehle

~~~text
python endpunkte.py
python budget.py ../.. budget-replay.json
python variation.py ../.. ../a9-a11-ungerader-restvergleich-2026-11-24/ERGEBNIS.json variation-replay.json
python endpunkte.py --budget budget-replay.json --variation variation-replay.json
~~~

Die Endpunktprüfung benutzt die mitgelieferten BUDGET.json und VARIATION.json. Die beiden numerischen Prüfer schreiben ihre Ergebnisse an die angegebenen Pfade. Die physischen Ursprungsintegrationen und der ganze Feldlauf des früheren Zeugen wurden für diesen Nachweis als geerbte Ergebnisse verwendet. Punkt 4 und die physische Inversausgabe $U_{11}$ bleiben offen.
