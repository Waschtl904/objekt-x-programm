# X-C1-STORAGE — Positiver Speicher, exakter Fluss und kausaler Präfix-No-Go

**Datum:** 16. September 2026. **Spur:** PR #137 / X-C0 common memory.
**C0-Quellanker:** `d7b32ccfb9d0d90f19d4a7a5b0fbd19b0928f257`.
**Rolle:** konstruktive C1-Rechnung mit erstem Falsifikationsgate, kein A1-/C0-Selbstaudit.
**Vertrauensstatus:** analytischer Autorennachweis; externe Prüfung offen; keine Neuheitsbehauptung.

## 0. Ergebnis und Reichweite

Die vorgeschlagene lokale Supply-Form ist wohldefiniert. Positive Hankel-Speicherkernel
und eine positive verteilte Gedächtnisenergie lassen sich aus den festen Ports
konstruieren. Ihre Green-Identitäten benötigen keine Weil-Positivität als Voraussetzung.

Die stärkere vorgeschlagene Identität

```math
s_a[z_x]=\|\mathcal L_a z_x\|^2+\frac d{dx}V_a[z_x],
\qquad V_a\ge0,\quad V_a[0]=0
```

kann jedoch **bereits bei a=1 nicht auf allen physischen NULLPOL-Bahnen gelten**,
wenn der Residualbeitrag nichtnegativ und der Speicher entlang jeder Bahn absolut
stetig ist. Ein explizit geglätteter Anfangsabschnitt hat Supply-Integral kleiner
als -1/20, beginnt im Nullzustand und lässt sich innerhalb desselben Fensters zu
NULLPOL ergänzen. Das ist keine negative vollständige Weil-Testfunktion.

Konstruktiv bleibt die positive Gedächtnisenergie F_a aus §6 mit der exakten
Identität `s_a+dF_a/dx=2 Re(conj(v) B_a v)`. Rechts steht eine signierte
Randpaarung, noch kein positiver Residualport. C1-GEOM bleibt außerhalb der
präzise ausgeschlossenen Klasse offen.

Keiner der folgenden Beweise benutzt A1-COMP. PR #131, sein Review, die
A1-Statuskapsel, die ursprüngliche C0-Spezifikation und ihr Prüfer sowie main und
Registry bleiben unverändert. Dieses Arbeitspaket ergänzt nur dieses Dokument
und einen kleinen eigenständigen rationalen/algebraischen Prüfer, keinen Workflow.

## 1. Lokale Portform und Definitionsbereich

Benutzt werden der C0-Raum h=H^1(0,infinity) mit festem Robin-Randterm,
k_t(r)=exp(-|r-t|/2) und im ersten Argument lineare Skalarprodukte. Setze

```math
c_t=e^{-t/4},\qquad \ell_t(z)=z(t)-c_tz(0)=\langle z,g_t\rangle_h,
\qquad g_t=k_t-c_tk_0,
```

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
\lambda_{p,k}=\log p,\quad t_{p,k}=k\log p,\quad
w_{p,k}=\lambda_{p,k}e^{-t_{p,k}/2},
```

```math
\Gamma_a=\kappa_*+2\sum_{t_{p,k}\le2a}w_{p,k},
\qquad \kappa_*=\log(8\pi)+\gamma+\frac\pi2.
```

Der dichte glatte Kern ist C_c^infinity([0,infinity)), mit freier Spur bei null;
nicht der kleinere Nullspurkern. Die vorgeschlagene Form lautet

```math
s_a[z]=\int_0^\infty\frac{|\ell_t(z)|^2}{1-e^{-2t}}dt
+\sum_{t_{p,k}\le2a}\lambda_{p,k}|\ell_{t_{p,k}}(z)|^2
-\Gamma_a|z(0)|^2.                                      \tag{1}
```

Sie setzt sich sogar als beschränkte hermitesche Form auf ganz h fort. Für 0<t<=1:

```math
|\ell_t(z)|^2\le2t\int_0^t|z'(r)|^2dr+\frac{t^2}{8}|z(0)|^2,
\qquad (1-e^{-2t})^{-1}\le\frac{3}{2t}.
```

Damit ist das Integral über (0,1) höchstens `3||z'||^2+(3/32)|z(0)|^2`.
Für t>=1 gilt `(1-e^{-2t})^-1<3/2`; der Rest ist höchstens
`3||z||_2^2+6|z(0)|^2`. Insgesamt ist die kontinuierliche Portenergie höchstens

```math
3\|z'\|_2^2+3\|z\|_2^2+7|z(0)|^2\le14\|z\|_h^2.
```

Die diskreten Punktauswertungen sind beschränkt, die aktive Summe endlich.
Für glattes z ist der vollständige kontinuierliche Integrand bei t→0 von Ordnung
O(t). Im ursprünglichen physischen Ausdruck ist h(t)=O(t^-1) nur die DICHTE,
während `||K_t v||_2^2=O(t^2)` gilt. Das präzisiert die Anmerkung zu C0 §5,
ohne die eingefrorene Datei zu ändern. Die Beschränktheit auf ganz h ist ein
zusätzlicher C1-Satz, keine erneute C0-Prüfung.

## 2. Lokalisierung und Kausalität: die Verschiebungen sichtbar halten

Schreibe u=E_a v und

```math
z_x(r)=e^{-r/4}u(x-r),\qquad
\partial_xz_x=-\partial_rz_x-\tfrac14z_x,\qquad z_x(0)=u(x).
```

Der ursprüngliche C0-Feldport erfüllt

```math
(\mathcal J_tT_a^0v)(x)=\ell_t(z_{x+t/2}).
```

Für JEDES t separat ergibt y=x+t/2:

```math
\int_{\mathbb R}|\mathcal J_tT_a^0v(x)|^2dx
=\int_{\mathbb R}|\ell_t(z_y)|^2dy.
```

Es gibt nicht eine gemeinsame Translation, die alle ursprünglichen lokalen
Portdichten am selben x gleichsetzt. Diese t-abhängige Umindizierung erhält das
Gesamtintegral, nicht beliebige Präfixintegrale. Für die positiven Energien ist
Tonelli anwendbar; die diskrete Summe ist endlich. Auf W_a gilt daher exakt

```math
Q_W[v]=\int_{\mathbb R}s_a[z_x]dx.                       \tag{2}
```

Für allgemeines v ist rechts die NICHTPOL-Form q_a[v], nicht die Completion oder
die volle Weil-Form. Auch eine später NULLPOL-erfüllende Eingabe hat auf einem
Anfangsabschnitt im Allgemeinen keine verschwindenden partiellen Momente.
Gleichung (2) ist keine Präfix-Positivitätsaussage.

Für x<-a ist z_x=0. Für x>a ist sein h-Normquadrat

```math
e^{-x/2}\int_{-a}^a e^{y/2}
\left(\left|v'(y)+\tfrac14v(y)\right|^2+\tfrac14|v(y)|^2\right)dy.
```

Jede beschränkte quadratische Speicherform auf h verschwindet folglich an beiden
Enden dieser Bahnen. Für unbeschränkte Kernel muss dies gesondert bewiesen werden.

## 3. Green-Identität und eine konkrete positive Kernelklasse

Für einen hermiteschen C^1-Kernel P definiere zunächst

```math
V_P^R[z]=\int_0^R\int_0^R P(r,s)z(r)\overline{z(s)}drds.
```

Partielle Integration entlang der Transportgleichung liefert

```math
\begin{aligned}
\frac d{dx}V_P^R[z_x]
={}&2\operatorname{Re}\left[z_x(0)\int_0^R P(0,s)\overline{z_x(s)}ds\right]\\
&-2\operatorname{Re}\left[z_x(R)\int_0^R P(R,s)\overline{z_x(s)}ds\right]\\
&+\int_0^R\int_0^R
(\partial_rP+\partial_sP-\tfrac12P)(r,s)
 z_x(r)\overline{z_x(s)}drds.                           \tag{3}
\end{aligned}
```

Die zweite Zeile ist der tatsächliche obere Randterm. Physische glatte Zustände
haben bei festem x kompakten r-Träger; für die folgenden exponentiellen Kernel
ist der Grenzübergang ebenfalls direkt zulässig.

Als vorab festgelegte positive Hankel-Klasse verwende

```math
P_\mu(r,s)=e^{-(\mu-1/4)(r+s)},\qquad \mu=\mu_m=2m+\tfrac12.
```

Dies sind positive Rang-eins-Kernel, unabhängig von Q_W und Testresultaten.
Mit `y_mu(x)=integral exp(-(mu-1/4)r) z_x(r)dr` gilt

```math
V_\mu[z_x]=|y_\mu(x)|^2\ge0,\qquad y_\mu'=u-\mu y_\mu,
```

```math
\frac d{dx}V_\mu[z_x]
=2\operatorname{Re}(u\overline{y_\mu})-2\mu|y_\mu|^2.   \tag{4}
```

Insbesondere ist `P_0=exp(-(r+s)/4)` der explizite erste Versuch bei mu=1/2.
Positive Mischungen mit gesicherter Konvergenz sind ebenfalls wohldefinierte
Speicher. Ihre Existenz beweist NICHT, dass `s_a-dV/dx` positiv ist. Der folgende
Test schließt dies für sämtliche positiven Versuche der angegebenen Art aus,
nicht nur für einen Kernel oder einen endlichdimensionalen Proberaum.

## 4. Früher No-Go auf der tatsächlichen physischen NULLPOL-Klasse

### 4.1 Notwendige Präfixungleichung

Angenommen, bei a=1 gilt für jedes glatte v in W_1

```math
s_1[z_x]=R[z_x]+\frac d{dx}V[z_x],\qquad
R\ge0,\quad V\ge0,\quad V[0]=0,                         \tag{5}
```

mit endlichen Werten, lokal integrierbaren Beiträgen und absolut stetigem
V[z_x]. Ein x-abhängiges V_x hilft ebenso wenig, solange V_x>=0 und V_x[0]=0.
Von einem Zeitpunkt x_0 vor Beginn der Eingabe bis X folgt notwendig

```math
\int_{x_0}^X s_1[z_x]dx
=\int_{x_0}^X R[z_x]dx+V[z_X]\ge0.                     \tag{6}
```

Hier wird weder ein unendlicher Zeitlimes noch eine spektrale Annahme benutzt.

### 4.2 Exakte Rechnung für einen Rampenpräfix

Benutze zunächst die verschobene Zeit y=x+1/2 und L=1/2. Setze
`u_0(y)=y/L` für 0<=y<=L und null für y<0. Die Zukunft bleibt noch offen.
Das Präfix-Normquadrat ist E=L/3=1/6. Direktes Integrieren ergibt

```math
\int_0^L|u_0(y-t)-u_0(y)|^2dy=E\,F(t/L),
```

mit `F(q)=3q^2-2q^3` auf [0,1] und F(q)=1 für q>=1. Wegen

```math
h(t)\le e^{-t/2}\left(1+\frac1{2t}\right)
```

folgen

```math
\int_0^L h(t)F(t/L)dt\le\frac L2+\frac5{12}=\frac23,
\qquad
\int_L^\infty h(t)dt<2+\tfrac12\log2+e^{-1/2}<\frac72.
```

Für die vollständige archimedische Präfixenergie A(u_0) gilt somit

```math
A(u_0)<\frac{25}{6}E=\frac{25}{36}.                    \tag{7}
```

Jede Primverzögerung ist mindestens log2>L. Auf dem Präfix ist ihre vergangene
Abtastung null; ihr zentrierter Beitrag beträgt genau `-w_{p,k}E`.
Außerdem ist `kappa_*>9/2`: Aus pi>3, gamma>=0, e<11/4 und e^3<24 folgen
`log(8pi)>3` und pi/2>3/2. Gamma>=0 folgt beispielsweise aus der aufsteigenden
unteren Folge `H_n-log(n+1)`, deren erster Wert 1-log2 positiv ist.
Daher liefert der zunächst UNGEGLÄTTETE Präfix

```math
\int_0^L s_1[z_y]dy
\le A(u_0)-\kappa_*E
<\frac{25}{36}-\frac34=-\frac1{18}.                   \tag{8}
```

z_y bezeichnet hier die verschobene physische Historie; zurückübersetzt ist
der Abschnitt x in [-1/2,0]. A1-COMP wird nicht verwendet.

### 4.3 Feste Glättung — nicht nur ein Dichteargument

Wähle die einmal festgelegte Einheitsintegral-Mollifikation

```math
\eta(t)=c\exp\!\left[-\frac1{t(1-t)}\right]\ (0<t<1),
\quad \eta=0\ \text{sonst},\quad
\eta_\varepsilon(t)=\varepsilon^{-1}\eta(t/\varepsilon),
\quad \varepsilon=10^{-6}.
```

c normiert das Integral, es ist kein angepasster Speicherkernkoeffizient. Setze

```math
u_\varepsilon(y)=\frac1L\int_0^\varepsilon
\eta_\varepsilon(s)(y-s)_+ds.                          \tag{9}
```

Diese Funktion ist glatt, vor y=0 identisch null und erfüllt auf dem Präfix

```math
0\le u_0-u_\varepsilon\le\varepsilon/L,\qquad
\|(u_0-u_\varepsilon)'\|_2^2\le4\varepsilon,
```

```math
\|u_0-u_\varepsilon\|_2^2\le2\varepsilon^2,\qquad
\|u_\varepsilon\|_2^2\ge\frac16-\varepsilon.            \tag{10}
```

Für eine Präfixstörung d mit d(0)=0 gilt

```math
A(d)\le\frac7{12}\|d'\|_2^2+12\|d\|_2^2.
```

Beweis: Bei t<=1 ist die integrierte Differenz höchstens t^2||d'||^2 und
`integral_0^1 t^2 h(t)dt<=7/12`. Bei t>=1 genügen 4||d||^2 und
`integral_1^infinity h<3`. Folglich

```math
A(u_0-u_\varepsilon)\le\tfrac73\varepsilon+24\varepsilon^2
<3\varepsilon,\qquad \sqrt{3\varepsilon}<2/1000.
```

Mit sqrt(A(u_0))<1 und Cauchy-Schwarz in der positiven Portenergie folgt
`A(u_eps)<25/36+4/1000+3eps`. Die negativen Primbeiträge dürfen für eine obere
Schranke weiterhin entfallen. Zusammen mit (10) und kappa_*>9/2 ergibt sich

```math
\boxed{
\int_{-1/2}^0s_1[z_x]dx
<-\frac1{18}+\frac4{1000}+\frac{15}{2}\,10^{-6}
<-\frac1{20}.
}                                                       \tag{11}
```

Die Akzeptanzkonstanten in (7)--(11) werden im neuen Standalone-Prüfer exakt
rational kontrolliert. Es wird keine numerische Quadratur als Beweis verwendet.

### 4.4 Glatte NULLPOL-Ergänzung im SELBEN Einheitsfenster

Wähle einen glatten Cutoff chi, der für y<=5/8 gleich eins und für y>=3/4 null
ist, und setze `v_0(x)=chi(x+1/2)u_eps(x+1/2)`. Diese glatte Funktion ist in
[-1/2,1/4] getragen und stimmt auf dem gesamten negativen Präfix mit (9) überein.

Fixiere eine nichtverschwindende nichtnegative glatte Funktion beta mit Träger
in (-1/100,1/100), und `beta_j(x)=beta(x-c_j)` bei c_1=1/2, c_2=3/4.
Mit `m_+=E_+(beta)>0`, `m_-=E_-(beta)>0` hat ihre Momentmatrix Determinante

```math
m_+m_-\left(e^{(c_1-c_2)/2}-e^{(c_2-c_1)/2}\right)\ne0.
```

Somit existieren eindeutige alpha_1, alpha_2, sodass
`v=v_0+alpha_1 beta_1+alpha_2 beta_2` beide E-Momente vernichtet.
v liegt in C_c^infinity(-1,1) und NULLPOL. Für x<=0 ist seine gesamte
Vergangenheit unverändert; (11) bleibt gültig. Die Eingabekoeffizienten setzen
nur die vorgeschriebenen Nebenbedingungen um; kein Speicherparameter wird gefittet.
Der Anfangszustand bei x=-1/2 ist null.

### 4.5 Schluss und präzise Ausschlussklasse

(11) widerspricht (6). Deshalb

```math
\boxed{
\text{Keine Identität (5) mit }V\ge0,\ V[0]=0,\ R\ge0
\text{ gilt auf allen physischen }v\in\mathcal W_1.
}                                                       \tag{12}
```

Dies erfasst alle positiven Kernel-Speicher mit den angegebenen Bahnannahmen,
auch größere nichtnegative Speicherklassen. Der Beweis benutzt NICHT den
unzulässigen unendlich langen stationären Eingang. Der Zeuge ist ein echter
glatter, im selben Fenster zu NULLPOL ergänzter physischer Präfix.

Nicht ausgeschlossen sind: positive vollständige Q_W auf W_1; C0; nichtkausale
Auswertungen; andere lokale Supply-Gauges; indefinite Randspeicher; oder eine
explizit terminalbedingte Geometrie. Bloße x-Abhängigkeit eines weiterhin
nichtnegativen, im Nullzustand bei null startenden Speichers hilft nicht.
Eine Fortsetzung muss eine benannte Hypothese von (12) ändern, nicht lediglich
einen anderen positiven Kernel oder eine größere Probenmatrix wählen.

## 5. Der eingefrorene Prime-2-Mischtest

Die C0-Funktionen `f=(-partial_x^2+1/4)b_eps(x+log2/2)` und `g=U_log2 f`
mit ursprünglichem Bumpradius 1/100 bleiben unverändert. Dieser Radius ist
nicht die Glättungsbreite aus §4. Partielle Integration liefert NULLPOL.
Nur log2 unter den aktiven Einheitsfensterverschiebungen verbindet ihre Träger.
Mit w=log2/sqrt2 ist deshalb exakt

```math
\left.Q_{fin}\right|_{\operatorname{span}\{f,g\}}
=w\|f\|_2^2\begin{pmatrix}0&-1\\-1&0\end{pmatrix},
\qquad Q_{fin}(f,g)=-\frac{\log2}{\sqrt2}\|f\|_2^2.      \tag{13}
```

Die Gamma-Paarung bleibt Teil jedes vollständigen Residualtests. Weder die
Indefinitheit dieses ISOLIERTEN Primblocks noch der Präfix-No-Go widerlegt
die gesamte Weil-Positivität. Der kernelunabhängige Präfixtest schließt bereits
die vorgeschlagene positive Speicherklasse aus. (13) wird nicht fälschlich als
bestandener positiver C1-Gate bezeichnet; der vorgeschriebene Mischterm bleibt erhalten.

## 6. Konstruktiv erhalten: explizite positive Gedächtnisenergie

Für jeden Primport definiere

```math
F_{p,k}[z]=w_{p,k}\int_0^{t_{p,k}}e^{r/2}|z(r)|^2dr\ge0.
```

Auf physischen Zuständen gilt

```math
F_{p,k}[z_x]=w_{p,k}\int_{x-t_{p,k}}^x|u(y)|^2dy,
\qquad \frac d{dx}F_{p,k}[z_x]
=w_{p,k}(|u(x)|^2-|u(x-t_{p,k})|^2).                   \tag{14}
```

Die zentrierte diskrete Supply erfüllt damit EXAKT

```math
\lambda|\ell_t(z_x)|^2-2w|u(x)|^2
=-\frac d{dx}F_{p,k}[z_x]
-2w\operatorname{Re}(u(x-t)\overline{u(x)}).            \tag{15}
```

Für die kontinuierlichen Ports setze

```math
F_\gamma[z]=\int_0^\infty h(t)\int_0^t e^{r/2}|z(r)|^2drdt
=\int_0^\infty W_\gamma(r)|z(r)|^2dr,
\quad W_\gamma(r)=e^{r/2}\int_r^\infty h(t)dt.           \tag{16}
```

Hier ist `W_gamma(r)=(1/2)log(1/r)+O(1)` nahe null und W_gamma→2 im Unendlichen.
Daher ist (16) positiv und auf h beschränkt: Benutze beschränkte
Punktauswertungen auf [0,1] und die L2-Norm danach. Es handelt sich um eine
positive Multiplikationsform, also einen diagonalen Maßkernel, nicht einen
vorgeblich glatten Doppelkernel. Der logarithmisch singuläre Rand darf nicht
durch unzulässiges Separieren divergenter Terme behandelt werden.

Die sichere endliche Flussidentität lautet

```math
\frac d{dx}F_\gamma[z_x]
=\int_0^\infty h(t)(|u(x)|^2-|u(x-t)|^2)dt.            \tag{17}
```

Die Differenz ist bei t→0 von Ordnung O(t). Ein positiver unterer Cutoff und
dominierte Konvergenz rechtfertigen (17); die oberen Randterme verschwinden.
Mit `F_a=F_gamma+sum_active F_{p,k}` ist eine positive, geometrisch festgelegte,
unendlichdimensionale Speicherform konstruiert. Ihre Endwerte verschwinden.
Aus (15)--(17) folgt

```math
\boxed{
s_a[z_x]+\frac d{dx}F_a[z_x]
=2\operatorname{Re}\bigl(\overline{u(x)}(\mathcal B_a u)(x)\bigr),
}                                                       \tag{18}
```

mit dem konkreten kausalen Randport

```math
(\mathcal B_a u)(x)=
\int_0^\infty h(t)(u(x)-u(x-t))dt
-\sum_{t_{p,k}\le2a}w_{p,k}u(x-t_{p,k})
-\frac{\kappa_*}{2}u(x).                               \tag{19}
```

Das Integral konvergiert für glattes kompaktes u. Es wurde keine Positivität von
Q_W benutzt. Die rechte Seite von (18) ist jedoch noch nicht als nichtnegative
Form oder Quadratsumme bewiesen. Sie wird nicht zum positiven Residualport umbenannt.
Für `tilde s_a=s_a+dF_a/dx` entspräche eine positive neue Speicherform tilde V_a
im ORIGINALEN Supply einer Differenz `V_a=tilde V_a-F_a`, die im Allgemeinen
indefinit ist. Genau diese Hypothese von (12) würde dadurch geändert.

## 7. Exakter Fenster-Kokzyklus und sein Vorzeichen

Sei a<b und v in I_a getragen. Für jeden neu aktivierten Kanal t>=2a gilt
`u(x-t)conj(u(x))=0`. Aus (15) folgt daher

```math
\boxed{
s_b[z_x]-s_a[z_x]
=-\frac d{dx}\sum_{2a<t_{p,k}\le2b}F_{p,k}[z_x].
}                                                       \tag{20}
```

Die Wahl an einer exakten Schwelle ändert die zentrierte Aussage nicht.
Insbesondere gilt auf allen alten physischen Zuständen

```math
F_b-F_a=\sum_{new}F_{p,k}\ge0,\qquad
\tilde s_b[z_x]=\tilde s_a[z_x].                       \tag{21}
```

Die positive Gedächtnisenergie besitzt somit ein kanonisches additives
Fenstergesetz. Die gauge-korrigierte Rand-Supply ist dort sogar punktweise
kompatibel. Das beweist noch keine positive Endauswertung oder ihre Connecting Maps.

Bei ORIGINAL-Gauge-Identitäten mit punktweise gleicher alter Residualdichte
würde deren Differenz dagegen `V_b-V_a=-sum_new F_{p,k}` erzwingen, wegen der
Nullanfangswerte. Das Vorzeichen ist NEGATIV. Wenn Connecting Maps nur die
integrierte Norm erhalten, ist punktweise Gleichheit der Residualdichten eine
zusätzliche Annahme und darf nicht untergeschoben werden.

## 8. Status und nächster zulässiger Konstruktionsgegenstand

| Ergebnis | Status |
|---|---|
| Lokale Supply, Kern, Konvergenz und Beschränktheit auf h | analytischer Autorennachweis |
| Positive Hankelversuche und Green-Randidentität | explizit konstruiert |
| Gemeinsame positive Gedächtnisenergie F_a und (18) | konstruiert, Randoutput bleibt signiert |
| Glatter NULLPOL-Präfix mit Supply <-1/20 | analytischer Zeuge; skalare Konstanten exakt geprüft |
| Original-Gauge: nichtnegativer kausaler Speicher + nichtnegativer Residualport | durch (12) ausgeschlossen, ✓[M]_neg auf Autorenebene |
| Positives endgültiges C_a / C1-GEOM und X-Connecting-Maps | ?[O] |

Sinnvoll ist jetzt nicht ein weiterer beliebiger positiver P für (5), sondern
eine explizit endpunktbedingte Faktorisierung der konkreten Randpaarung (18)--(19).
Dabei muss der Speicher in der ORIGINAL-Gauge beide Vorzeichen annehmen dürfen,
oder die tatsächlich zweiseitige zentrierte Portgeometrie muss erhalten bleiben.
Die zwei Mellinbedingungen und (21) gehören von Anfang an zum Definitionsbereich.
Eine Existenzbehauptung wird nicht gemacht. Verdeckte Terminalzustände,
unbewiesene Positive-real-Eigenschaften oder GNS-Quadratwurzeln lösen diesen Gate nicht.

Der neue Prüfer `scripts/check_x_c1_storage_prefix.py` führt 26 kleine exakte
rationale/algebraische Tests aus. Er unterstützt den analytischen Beweis,
diskretisiert keinen Hilbertraum und ersetzt weder den Glättungsbeweis noch die
NULLPOL-Ergänzung. Der vorhandene C0-Prüfer wird weder erweitert noch erneut ausgeführt.

## Quellen und Herkunft

- [Eingefrorene C0-Spezifikation](https://github.com/Waschtl904/objekt-x-programm/blob/d7b32ccfb9d0d90f19d4a7a5b0fbd19b0928f257/X_CANDIDATE_C0_SPEC.md): Zustand, Ports, Normierung und ursprünglicher Mischtest.
- [COMMON-JUMP-Modellanker](https://github.com/Waschtl904/objekt-x-programm/blob/ac164bbbd2c46623aa64e567d21f813f41f164b0/audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md): Weil-Normierung, Momentkonvention, h, w und Gamma_a.
- [DLMF 5.7.6](https://dlmf.nist.gov/5.7#E6) und [DLMF 5.4](https://dlmf.nist.gov/5.4): klassische Digammareihe und Konstantenkonventionen; kein importierter Positivitätssatz.

Die lokale Supply wurde im aktuellen Forschungsaustausch vorgeschlagen.
Beschränktheitsfortsetzung, Green-Rechnung, quantitativer glatter Präfix samt
NULLPOL-Ergänzung, positiver verteilter Speicher und signierter Fenster-Kokzyklus
werden hier hergeleitet. Weder allgemeine Speicherideen noch diese konkreten
Sätze werden als Literatur-Neuheit beansprucht. Nichts davon öffnet den A1-Audit.
