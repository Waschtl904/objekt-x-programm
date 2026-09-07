# P11 / R43: positiver Wurzelanker und Strong Terminal

Datum: 2026-09-07. Exakte Definitionsbasis:
`55a3a1617513cc5d82c47d0cfd606c6b0894c984`.
Neue analytische Ableitung zur destruktiven Exact-Head-Prüfung.
Keine Registry-Promotion, keine externe menschliche Zertifizierung
und keine Aussage zur Riemannschen Vermutung.

Zum Eingangsrahmen gehört ausdrücklich die in diesem Paket
enthaltene [Randspur-Reparatur des scharfen Schurbeweises](P11_R43_QUADRATURE_BOUNDARY_TRACE_REPAIR_2026-09-07.md).
Die alte globale Lipschitzbehauptung für den nullfortgesetzten
Quellrepräsentanten wird nicht als richtig vorausgesetzt.

## Aussage und minimaler Eingangsrahmen

Für jedes feste Paar \(0<R<S<\infty\) und die ursprünglichen
P11-Graph-Hilberträume \(\mathcal H_X=\mathcal K_{X,X}^{-}\) sei
\(\nu_X\) der Rieszvektor des nullten Randjets
\(\beta_X=\beta_X^{(0)}\). Setze
\[
\rho_X=\|\nu_X\|,\qquad
\varepsilon_X=\nu_X/\rho_X,\qquad
\beta_X(f)=\langle f,\nu_X\rangle.
\]
Die Phase wird durch \(\beta_X(\varepsilon_X)=\rho_X>0\) festgelegt.
Dies ist die ursprüngliche Graphnormale, nicht R42s
baseline-standardisierte Normale
([R42.57–R42.59](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1427-L1463)).

Aus den unten einzeln geprüften P11-Eingängen folgt
\[
\boxed{
W_{R,S}^{[U]}\varepsilon_R\longrightarrow\varepsilon_S
\quad\text{stark},\qquad U\to\infty.
}
\tag{PA1}
\]
Zusammen mit dem vorhandenen starken tangentialen Satz R42.51
folgt für jedes \(v\in H_R^0=\ker\beta_R\) und \(a\in\mathbb C\)
\[
\boxed{
W_{R,S}^{[U]}(v+a\varepsilon_R)
\longrightarrow
W_{R,S}^{(0)}v+a\varepsilon_S.
}
\tag{PA2}
\]
Damit wird der fehlende Normalkanal in der vorhandenen
Kodimension-eins-Reduktion geschlossen
([R42.51–R42.60](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1480)).

PA1 benutzt weder GC-AC noch eine vorausgesetzte Flag-Tightness.
PA2 importiert ausdrücklich R42.51; der neue Beweis ersetzt nicht
die unabhängige Validierung dieser kanonischen Vorarbeit.
Insbesondere wird keine Aussage über den Status anderer
Objekt-X-Eingänge oder über eine Registry-Promotion abgeleitet.

## Die tatsächlichen P11-Eingänge

Die Adjunktionen von \(J\) und die Quellmetriken \(G_{X,U}\)
beziehen sich auf die jeweils festen Graph-Hilberträume.
Die terminalen Operatoren \(H_U,R_U,\mathcal A_U\) und die
Paarungen in \(d_U,\ell_{X,U}\) behalten dagegen ihre
ursprünglichen \(L^2(-U,U)\)- bzw. Restzielraum-Adjunktionen.
Es gilt exakt
\[
J^*G_{S,U}J=G_{R,U},\qquad
W_U=G_{S,U}^{1/2}JG_{R,U}^{-1/2},\qquad W_U^*W_U=I.
\tag{PA3}
\]
Hier ist \(J\) die echte Nullerweiterung
([P11-Metriken und Transport](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L665-L715)).

### Globaler Rang-eins-Unterbau, kein Ersatzoperator

Sei
\[
\mathcal A_U=I+R_U^*R_U,\qquad
d_U=\langle\mathbf1_U,\mathcal A_U\mathbf1_U\rangle,\qquad
\ell_{X,U}(f)=\langle H_U^*J_{X,U}f,\mathbf1_U\rangle.
\]
Die volle Schurform und Cauchy–Schwarz liefern auf ganz
\(\mathcal H_X\)
\[
\langle G_{X,U}f,f\rangle
\ge \frac{|\ell_{X,U}(f)|^2}{d_U}.
\tag{PA4}
\]
Es wird nicht behauptet, dass \(\mathbf1_U\) im Restkern liegt.
Der tatsächliche Nenner enthält die vollständige Restenergie
([R27, Variationsschranke](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L128-L173)).

Die hierfür benötigten scharfen, kanonischen Grenzwerte sind
\[
d_U=2U+O(1),\qquad
e^{-U/2}U^{1/2}\ell_{X,U}
\longrightarrow-\sqrt2\,\beta_X
\quad\text{in }\mathcal H_X^*.
\tag{PA5}
\]
Der Nenner wird aus den vollständigen Martingalzeilen mit den
richtigen Tiefenmasken gewonnen, einschließlich der kohärenten
Primzahlpotenzsummen
([scharfer Nenner (6.4)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Odd_Asymptotic_FullProof.tex#L29-L78),
[duale Normkonvergenz](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md#L128-L164)).

### Nur die scharfe führende feste Quellenergie wird benötigt

Setze für beide Radien dieselbe Skala
\[
\lambda_U=\frac{e^U}{U^2},\qquad
M_{X,U}=\lambda_U^{-1}G_{X,U},\qquad
T_{X,U}=M_{X,U}^{1/2}.
\]
Für jedes feste glatte ungerade \(f\) mit \(\beta_X(f)\ne0\)
gibt der Fall \(m=0\), \(c_0=1\), des scharfen P11-Satzes
\[
\langle M_{X,U}f,f\rangle\longrightarrow|\beta_X(f)|^2.
\tag{PA6}
\]
Die feste Gammaenergie verschwindet nach Division durch
\(\lambda_U\). Entscheidend ist der genaue führende Faktor eins,
nicht bloß eine Größenordnung
([P11, Satz (6.1)](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex#L764-L791)).

Auch für festes glattes \(g\in\ker\beta_X\) folgt der Grenzwert null
schon aus diesem \(m=0\)-Fall. Wähle ein festes glattes \(f_0\)
mit \(\beta_X(f_0)=1\). Nach der exakten Parallelogrammidentität ist
\[
\langle M_{X,U}g,g\rangle
=\tfrac12\langle M_{X,U}(f_0+g),f_0+g\rangle
 +\tfrac12\langle M_{X,U}(f_0-g),f_0-g\rangle
 -\langle M_{X,U}f_0,f_0\rangle
\longrightarrow0.
\tag{PA7}
\]
Höhere Jetordnungen oder die Existenz eines ersten nichtverschwindenden
höheren Jets werden für diesen Schritt nicht gebraucht.

Der glatte ungerade Kern \(\mathcal D_X\) ist graphdicht.
Durch Korrektur mit einem festen glatten \(f_0\) ist
\(\mathcal D_X\cap\ker\beta_X\) dicht in \(\ker\beta_X\);
außerdem gilt \(\beta_S(Jf)=\beta_R(f)\)
([Graphkerndichte](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Direct_Terminal_Bridge.tex#L296-L338),
[Jetkompatibilität](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/papers/P11_sections/P11_Direct_Terminal_Bridge.tex#L43-L62)).

## Lemma: positiver Wurzelanker durch Normsättigung

Sei \(\beta(f)=\langle f,\nu\rangle\) eine nichtnull beschränkte
Linearform auf einem Hilbertraum, \(\rho=\|\nu\|\),
\(\varepsilon=\nu/\rho\). Sei \(\mathcal D\) ein dichter
linearer Teilraum mit \(\mathcal D\cap\ker\beta\) dicht in
\(\ker\beta\). Angenommen:

- **Globale Ordnung:** \(M_u\succeq|\nu_u\rangle\langle\nu_u|\),
  wobei \(M_u\) für jedes endliche \(u\) beschränkt und positiv ist.
- **Feste Rieszrichtung:** \(\nu_u\to\nu\) in Hilbertnorm.
- **Scharfe Kernenergien:** \(\langle M_uf,f\rangle\to|\beta(f)|^2\)
  für jedes feste \(f\in\mathcal D\).

Dann
\[
\boxed{M_u^{1/2}f\longrightarrow\beta(f)\varepsilon
\quad(f\in\mathcal D).}
\tag{PA8}
\]
Weder eine uniforme obere Operatornormschranke noch Konvergenz auf
der gesamten Einheitskugel wird vorausgesetzt oder gefolgert.

### Beweis

Die positive Quadratwurzel erhält die Operatorordnung. Hier kann
dies ohne Kompressionsargument aus der Resolventenformel gesehen werden:
für \(M\succeq B\succeq0\) gilt
\[
\sqrt M-\sqrt B
=\frac1\pi\int_0^\infty t^{1/2}
\bigl((B+tI)^{-1}-(M+tI)^{-1}\bigr)\,dt\succeq0.
\tag{PA9}
\]
Für jedes einzelne beschränkte Operatorpaar ist das Integral
normkonvergent: am Ursprung genügt \(O(t^{-1/2})\), am
Unendlichen \(O_{M,B}(t^{-3/2})\). Daher
\[
M_u^{1/2}\succeq
\frac{|\nu_u\rangle\langle\nu_u|}{\|\nu_u\|}
\quad\text{für alle hinreichend großen }u.
\tag{PA10}
\]

Wähle zunächst fest \(f\in\mathcal D\) mit \(\beta(f)=1\)
und setze \(x_u=M_u^{1/2}f\). Die scharfe Kernenergie gibt
\(\|x_u\|^2\to1\). Für jedes feste
\(g\in\mathcal D\cap\ker\beta\) ist
\(\|M_u^{1/2}g\|\to0\), also wegen Selbstadjungiertheit
\[
\langle x_u,g\rangle=\langle f,M_u^{1/2}g\rangle\to0.
\tag{PA11}
\]
Somit ist jeder schwache Teilfolgengrenzwert gleich
\(c\varepsilon\), mit \(|c|\le1\).

Andererseits erzwingt PA10
\[
\langle x_u,f\rangle
\ge\frac{|\langle f,\nu_u\rangle|^2}{\|\nu_u\|}
\longrightarrow\frac1\rho.
\tag{PA12}
\]
Am schwachen Grenzwert ist die linke Seite \(c/\rho\),
weil \(\beta(f)=1\). Sie ist reell. Also ist \(c\) reell
und \(c\ge1\); mit \(|c|\le1\) folgt \(c=1\).
Der schwache Grenzwert besitzt damit die ganze Grenznorm.
Folglich konvergiert \(x_u\) stark gegen \(\varepsilon\).
Das Argument gilt entlang jeder Folge \(u_n\to\infty\)
und somit für den ganzen Horizontlimes.

Für \(\beta(f)\ne0\) folgt PA8 durch Skalierung, für
\(\beta(f)=0\) unmittelbar aus der Kernenergie. Der Beweis
benutzt die volle positive Wurzel, nicht die Wurzel eines
endlichen komprimierten Grams.

## Anwendung auf die wirkliche Normalbahn

Definiere die Rieszvektoren \(\nu_{X,U}\) durch
\[
\langle f,\nu_{X,U}\rangle
:=-\frac{\ell_{X,U}(f)}{\sqrt{\lambda_Ud_U}}.
\tag{PA13}
\]
PA5 gibt \(\nu_{X,U}\to\nu_X\) in Norm; PA4 gibt
\(M_{X,U}\succeq|\nu_{X,U}\rangle\langle\nu_{X,U}|\).
PA6–PA7 und die Graphkerndichte erfüllen die übrigen
Voraussetzungen des Lemmas. Damit
\[
Ue^{-U/2}G_{X,U}^{1/2}f
\longrightarrow\beta_X(f)\varepsilon_X
\quad(f\in\mathcal D_X).
\tag{PA14}
\]

Wähle ein einziges festes reelles \(f\in\mathcal D_R\)
mit \(\beta_R(f)=1\) und setze
\[
f_R=f,\quad f_S=Jf,\quad x_{X,U}=T_{X,U}f_X.
\]
Beide Anker konvergieren stark: \(x_{X,U}\to\varepsilon_X\).
Aufgrund derselben Skala und PA3 gilt jedoch auch exakt
\[
W_Ux_{R,U}=x_{S,U}.
\tag{PA15}
\]
Der letzte Grenzübergang läuft deshalb durch die normeinsbeschränkte
Isometrie, nicht durch eine wachsende Quadratwurzel:
\[
\boxed{
\|W_U\varepsilon_R-\varepsilon_S\|
\le\|\varepsilon_R-x_{R,U}\|
 +\|x_{S,U}-\varepsilon_S\|
\longrightarrow0.
}
\tag{PA16}
\]
Damit ist PA1 bewiesen. Es wird weder die Phase entfernt
noch ein kleiner inverser Wurzelrest ungeprüft verstärkt.

## Globale Tightness und C6

Setze
\[
\Theta_*=|\varepsilon_S\rangle\langle\varepsilon_S|,
\quad h_U=(I-\Theta_*)W_U\varepsilon_R,\quad
q_m(U)=\|P_mW_U\varepsilon_R\|^2.
\]
Für die kanonischen tiefen Flagprojektionen mit \(m\ge1\) gilt
\(P_m\varepsilon_S=0\), \(\|P_m\|\le1\). Aus PA16 folgt
\[
\sup_{m\ge1} q_m(U)\le\|h_U\|^2
\le\|W_U\varepsilon_R-\varepsilon_S\|^2\longrightarrow0.
\tag{PA17}
\]
Insbesondere gilt der echte globale Tail-Quantor
\[
\forall\epsilon>0\ \exists U_0\
\forall U\ge U_0\ \forall m\ge1:\quad q_m(U)<\epsilon^2.
\tag{PA18}
\]
Das ist ein direkter No-escape-Nachweis, kein neuer
hinreichender Budgetvertrag. Alle großen reellen Horizonte
werden erfasst, einschließlich der tatsächlichen Sprungwerte.
Keine Stetigkeit oder Variationsrate in \(U\) wird gebraucht.

Zusammen mit R42.51 und
\(\mathcal H_R=H_R^0\oplus\mathbb C\varepsilon_R\)
folgt PA2. Auch der exakte C6-Kreuzterminaltest erfüllt
\[
2(1-L_{R,S}^{T,U})
=\|W_U\varepsilon_R-W_T\varepsilon_R\|^2
\longrightarrow0
\qquad(T,U\to\infty).
\tag{PA19}
\]
Der Grenzoperator in PA2 ist eine Isometrie. Das folgt entweder
aus der Orthogonalität des tangentialen Zielraums zu
\(\varepsilon_S\) oder aus dem starken Grenzübergang der
endlichen Isometrien
([R42.51–R42.59](https://github.com/Waschtl904/objekt-x-programm/blob/55a3a1617513cc5d82c47d0cfd606c6b0894c984/audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md#L1322-L1463)).

## Destruktiver Gegencheck: warum feste Grams allein nicht reichen

Auf \(\ell^2(\mathbb N_0)\) definiere \(T_n\succeq0\) durch
\[
T_n\big|_{\operatorname{span}\{e_0,e_n\}}
=\begin{pmatrix}1/n&1\\1&n\end{pmatrix}+n^{-2}I,
\qquad
T_n=n^{-2}I\quad\text{auf dem Komplement},
\quad M_n=T_n^2.
\]
Für jeden fest endlich getragenen Vektor \(f\) gilt
\(\langle M_nf,f\rangle\to|\langle f,e_0\rangle|^2\).
Dennoch ist
\[
T_ne_0=(n^{-1}+n^{-2})e_0+e_n
\]
schwach null bei Normgrenzwert eins. Der Wurzelanker flieht.

Dieses Modell kann aber gerade nicht die zusätzliche globale
Unterordnung \(M_n\succeq|\nu_n\rangle\langle\nu_n|\)
mit \(\nu_n\to e_0\) erfüllen. Sonst würde PA10
\(\langle T_ne_0,e_0\rangle\gtrsim1\) erzwingen, während
der tatsächliche Wert gegen null geht. Es ist ein abstraktes
Gegenmodell zur Gram-only-Abkürzung, kein P11-Gegenbeispiel.

## Was durch diesen Abschluss nicht mitbehauptet wird

- **Keine normuniforme Metrikasymptotik:** Eine obere
  globale Normschranke für \(M_{X,U}\) oder einen abgespaltenen
  Schurrest wird nicht vorausgesetzt oder bewiesen.
- **Keine Variationssummation:** FD23, das J12–J15-Budget
  positiver Endpunktzuwächse und globale O1-Variation werden
  nicht geschlossen. Sie sind für den direkten Weg nicht nötig.
- **Keine gemeinsame Conditioning-Grenze:** Keine Aussage
  über simultanes \(U,V\to\infty\) wird importiert.
- **Keine zusätzliche GC-AC-Pflicht:** Die neue Normalbahn
  wird unmittelbar kontrolliert. Der Status von GC-AC
  selbst wird weder verbessert noch verschlechtert.
- **Kein vollständiges Objekt X oder RH:** Der analytische
  Strong-Terminal-Schluss im ausgewiesenen P11-/R42-Rahmen
  ersetzt keine weiteren globalen Realisierungsbedingungen.
- **Keine automatische Promotion:** Repository-Integration,
  Exact-Head-Review und Theorem-Registry bleiben getrennte
  Entscheidungen.
