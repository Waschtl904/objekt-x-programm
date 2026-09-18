# X-C0 — Common-memory mediator / Kandidatenspezifikation

**Datum:** 16. September 2026. **Status:** aktive Konstruktion; kein fertiges Objekt X.
**Branchbasis:** `main@ac164bbbd2c46623aa64e567d21f813f41f164b0`, nicht PR #131.
**A1-Import:** [A1-COMP@0a7c970 / AUTHOR-VERIFIED / EXTERNAL-OPEN](research/x-c0/A1_COMP_STATUS_CAPSULE.md).
**Namensraum:** X-C0/common-memory-2026-09-16; nicht der ältere SW1-A10-C0-Gate.

## 0. Konstruktionsentscheidung und offene Stelle

Wir konstruieren zuerst EINEN positiven Raum vollständiger Verzögerungszustände.
Prime-Power-, Gamma- und Polports werden aus diesem Raum ausgelesen, nicht als
von Anfang an orthogonale Ortsräume nebeneinandergestellt. Früh abgeschnittene
Gedächtnisschwänze werden nicht stillschweigend verworfen.

Die folgende Konstruktion gibt einen expliziten **Vormediator** `K^0_a` und eine
kanonische Abbildung `T^0_a`. Ihre Norm ist ausdrücklich NICHT die Weil-Form.
Eine positive, geometrisch vorwärts konstruierte Energieauswertung
`C_a:K^0_a -> K_{X,a}` ist der eine noch fehlende Konstruktionsbaustein.
Das Symbol `T_{X,a}=C_a T^0_a` ist eine präzise typisierte Zielschnittstelle,
keine Behauptung, C_a oder eine positive Weil-Faktorisierung sei schon gefunden.
Ein bloßes Umbenennen der bekannten signed COMMON-JUMP-Form erfüllt diesen Gate nicht.

Die Vormediator-Lemmas unten sind neue Herleitungen in dieser Spezifikation,
kein externer Review und keine Neuheitsbehauptung. A1-COMP wird ausschließlich
für die optionale lokale Defektdiagnose in §10 verwendet, nicht zur Definition
der Geometrie, ihrer Ports oder ihrer Fensterabbildungen.

## 1. Hilbert-/Mediatorraum — tatsächlich definiert

Auf der Halbgeraden definiere den Sobolev-Raum

```math
\mathfrak h=H^1(0,\infty),\qquad
\langle h,g\rangle_{\mathfrak h}
=\int_0^\infty(h'\overline{g'}+\tfrac14h\overline g)\,dr
+\tfrac12h(0)\overline{g(0)}.
```

Er ist ein positiver Hilbertraum mit reproduzierendem Kern

```math
k_t(r)=e^{-|r-t|/2},\qquad \langle h,k_t\rangle=h(t),\qquad
\langle k_s,k_t\rangle=e^{-|s-t|/2}.
```

Begründung: `(-d²/dr²+1/4)k_t=delta_t` für t>0, der Ableitungssprung ist -1,
und `k_t'(0)=k_t(0)/2`; partielle Integration liefert die Evaluation.
Für t=0 liefert der Robin-Randterm direkt h(0). Dichte erweitert den Beweis
von glatten Funktionen auf H¹. Insbesondere haben alle k_t Norm 1.

Der gemeinsame Raum ist

```math
\mathfrak M=L^2(\mathbb R_x;\mathfrak h_r).
```

Die x-Variable läuft über die GANZE Linie. Eine Beschränkung auf `x in (-a,a)`
ist nicht Bestandteil dieses Kandidaten. Das ist die bewusste Speicherung
der aus dem Fenster herauslaufenden Verzögerungszustände.

## 2. Testklasse

```math
I_a=(-a,a),\quad \mathcal W_a^{full}=C_c^\infty(I_a;\mathbb C),\quad
\mathcal W_a=\{v\in\mathcal W_a^{full}:E_+(v)=E_-(v)=0\},
\qquad E_\pm(v)=\int e^{\pm x/2}v(x)\,dx.
```

`E_a v` bezeichnet Nullfortsetzung. `U_t v(x)=v(x-t)` und
`K_t=U_{t/2}-U_{-t/2}`. Alle Skalarprodukte sind linear im ersten Argument.
Die primäre positive Zielidentität wird auf W_a gesucht; full und gerade
Tests bleiben getrennte Erweiterungsziele. Sobolevabschlüsse werden ausdrücklich
in H¹₀(I_a), nicht stillschweigend in L² oder einem unbenannten Formbereich gebildet.

## 3. Kanonische Zustandsabbildung und Zielabbildung

```math
(T^0_a v)(x,r)=e^{-r/4}(E_a v)(x-r),\qquad r\ge0.
```

Die Dämpfung 1/4 ist eine vorab fixierte Normalisierung: Sie erzeugt bei
`t=k log p` genau die Quadratwurzel der Weil-Dämpfung `p^{-k/2}`.
Es wird weder an Eigenwerten noch an Testvektoren ein Parameter angepasst.

Der Zustand erfüllt geometrisch

```math
(\partial_x+\partial_r+\tfrac14)T^0_a v=0,\qquad
(T^0_a v)(x,0)=E_a v(x).
```

Sein Träger liegt im vollständigen Kegel `r>=0, x-r in [-a,a]`.
Fubini und `Re integral v' conjugate(v)=0` ergeben exakt

```math
\|T^0_a v\|_{\mathfrak M}^2
=2\|v'\|_2^2+\tfrac98\|v\|_2^2.
```

Somit ist T^0_a injektiv und ein Isomorphismus auf seinen abgeschlossenen
Bildraum mit der angegebenen H¹-Norm. Setze

```math
\mathcal K^0_a=
T^0_a\bigl(H^1_0(I_a)\cap\ker E_+\cap\ker E_-\bigr)\subset\mathfrak M.
```

Das ist ein bereits konstruierter positiver Vormediator. Für full lässt man
nur die zwei Momentbedingungen weg. Keine der beiden Normen wird mit Q_W gleichgesetzt.
Die noch offene, vorwärts zu konstruierende Auswertung hat den Typ

```math
C_a:\mathcal K^0_a\supset T^0_a\mathcal W_a\longrightarrow\mathcal K_{X,a},
\qquad T_{X,a}=C_aT^0_a,
```

linear auf dem Testkern, mit nachzuweisender Abschließbarkeit und positivem
Zielraum. Weder `Q_W^(1/2)` noch eine aus bereits angenommener Weil-Positivität
gebildete GNS-Norm ist eine zulässige Definition von C_a.

## 4. Prime-power-Port

Definiere auf dem gemeinsamen Gedächtnisraum für jedes t>0

```math
(\mathcal J_t H)(x)=H(x+t/2,t)-e^{-t/4}H(x+t/2,0).
```

Evaluation in r ist auf h beschränkt, Translation in x unitär; daher ist jeder
J_t ein wohldefinierter beschränkter Port `M -> L²(R)`.
Auf tatsächlichen Zuständen gilt genau

```math
\mathcal J_tT^0_a v=e^{-t/4}K_tE_a v.
```

Für eine Primzahl p und k>=1 ist deshalb

```math
\mathcal P_{p,k}H=\sqrt{\log p}\,\mathcal J_{k\log p}H,
\qquad
\mathcal P_{p,k}T^0_av=\sqrt{(\log p)p^{-k/2}}K_{k\log p}E_av.
```

Alle Einzelports sind vor jeder Positivitätsannahme definiert. In der
unzentrierten endlichen Energie wird nur `k log p<=2a` summiert.
Eine unendliche rohe Prime-Energiesumme wird NICHT als konvergent behauptet.

## 5. Archimedischer Port und Polrand

Derselbe J_t-Port liefert den kontinuierlichen Kanal

```math
(\mathcal G H)(t,x)=(1-e^{-2t})^{-1/2}(\mathcal J_tH)(x).
```

Auf T^0_a W_a ist G ein wohldefinierter L²(dt dx)-Port und

```math
\|\mathcal GT^0_a v\|^2
=\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}\|K_tE_av\|_2^2dt.
```

Wohldefiniertheit: für t<=1 gilt `||K_t v||<=t||v'||`, für t>=1
`||K_t v||<=2||v||`; die Dichte ist O(1/t) beziehungsweise O(e^(-t/2)).
Auf ganz M wird G nur auf seinem natürlichen L²-Portbereich definiert;
eine Beschränktheit auf ganz M ist nicht behauptet.

Die Gamma-Resolventen sind ebenfalls Ports desselben Zustands:

```math
\mu_m=2m+\tfrac12,\qquad
(\mathcal Y_mH)(x)=\int_0^\infty e^{-(\mu_m-1/4)r}H(x,r)dr,
\qquad (\partial_x+\mu_m)\mathcal Y_mT^0_av=E_av.
```

Jeder Y_m ist auf M beschränkt. Die klassische Digammareihe liefert auf dem
Testkern alternativ `||G T^0 v||²=sum_{m>=0}(2/mu_m)||(Y_mT^0v)'||²`.
Dies ist eine zweite Auslesung, KEIN zusätzlicher Energiebeitrag.
Quelle für die Digammareihe: [DLMF 5.7.6](https://dlmf.nist.gov/5.7#E6).

Der gemeinsame Randport ist `R_0H(x)=H(x,0)`. Definiere

```math
\mathcal E_{\pm,a}H=\int_{-a}^a e^{\pm x/2}(R_0H)(x)dx.
```

Beide Funktionale sind auf M beschränkt. Auf T^0_av ergeben sie E_±(v).
Der Polbeitrag wird als gekreuzte Paarung aus dem Projekt importiert,
nicht fälschlich als positive Summe der Betragsquadrate.

## 6. Gemeinsame NICHTorthogonale Kopplung

Die internen Rieszvektoren des Jump-Ports sind

```math
g_t=k_t-e^{-t/4}k_0.
```

Ihr Gram lautet explizit

```math
\langle g_s,g_t\rangle
=e^{-|s-t|/2}-e^{-s/2-t/4}-e^{-s/4-t/2}+e^{-(s+t)/4}.
```

Insbesondere ist `⟨g_t,k_0⟩=e^(-t/2)-e^(-t/4) !=0` für t>0.
Auch die Rieszvektoren der Gamma-Laplaceports liegen im selben h:

```math
\ell_m=\int_0^\infty e^{-(\mu_m-1/4)r}k_r\,dr,\qquad
\langle k_t,\ell_m\rangle
=\int_0^\infty e^{-(\mu_m-1/4)r-|t-r|/2}dr>0.
```

Prime-, Gamma- und Randports benutzen also überlappende Richtungen desselben
Raums. Getrennte Ausgaberegister zum Buchführen ihrer Energien bedeuten keine
orthogonale Zerlegung des Mediators. Diese Nichtorthogonalität beweist jedoch
NICHT den benötigten Lower-Frame-Bound oder die Positivität der zentrierten Form.

**P11-Abgrenzung:** `exp(-|k log p-j log q|/2)` ist ein zeitlicher Delay-Gram.
Für verschiedene Primzahlen ist er NICHT der adelische P11-Tree-Gram
`p^(-k/2)q^(-j/2)`. X-C0 behauptet keine Isometrie dieser unterschiedlichen
Grams. Eine Verwendung der P11-spezifischen Tree-/Feshbachstruktur benötigt
einen gesonderten Intertwiner; gemeinsame OU-Sprache ersetzt ihn nicht.

## 7. Normierungen

Unitäre Fouriertransformation:

```math
\widehat v(\xi)=(2\pi)^{-1/2}\int e^{-i\xi x}v(x)dx.
```

Bei nichtunitärer Transformation F tritt `1/(2pi)` im Energieintegral auf.
`||v||_2` bleibt die L²-Norm der Nullfortsetzung. Die Vormediatornorm aus §3
ist eine stärkere H¹-Norm, kein Ersatz für diesen Nenner.

Vorab fest: Critical-half-Kern 1/2; Liftingdämpfung 1/4; Gewichte
`w_{p,k}=(log p)p^{-k/2}`; archimedische Dichte `e^(-t/2)/(1-e^(-2t))`;
Polfunktionale E_±. Keine Fits, keine frei erfundenen Prime/Gamma-Cross-Koeffizienten.

## 8. Fensterkompatibilität — auf der Vormediatorebene geschlossen

Für 0<a<b ist die Nullfortsetzung `i_{a,b}:H¹₀(I_a)->H¹₀(I_b)` isometrisch
für die Graphnorm aus §3. Es gilt als wörtliche Feldgleichheit

```math
T^0_b i_{a,b}v=T^0_a v.
```

Daher sind `K^0_a subset K^0_b subset M` und die natürlichen Einbettungen
`J^0_{a,b}` isometrisch, mit `J^0_{b,c}J^0_{a,b}=J^0_{a,c}`. Alle bereits
benannten Einzelports kommutieren auf den alten Zuständen mit der Einbettung.
Die Polports stimmen dort ebenfalls überein, weil die Randspur außerhalb I_a null ist.

Neu aktivierte Primeports mit t>=2a sind NICHT null: ihre Jumpenergie beträgt
`2w_n||v||²`. Genau derselbe Betrag wird neu in Gamma_b gebucht. Somit ist
die unten stehende SIGNIERTE Energie auf alten Zuständen kompatibel.

Für fertige X-Räume bleibt zusätzlich zu konstruieren

```math
J_{a,b}C_aH=C_bJ^0_{a,b}H,
```

mit isometrischen Connecting Maps auf den erzeugten Zielräumen. Die Existenz
von J^0 allein ist kein Nachweis dieser stärkeren Identität.

**Früher Stop-Test für abgeschnittenes Gedächtnis:** Für den bekannten
stopped-OU-Gram `G_L(s,t)=exp(-(s+t)/2+min(s,t,L))` haben bei t=log 4
L=0 und L=log 2 die jeweiligen Zustände Normquadrate 1/4 und 1/2.
Keine Isometrie kann diese zwei Zustandsvektoren aufeinander abbilden.
Dies widerlegt nur das naive Intertwining auf dem GANZEN gestoppten
Koordinatenspan, nicht jede Abbildung auf einem eingeschränkten physischen
Bildraum. X-C0 behält deshalb vorerst die vollständigen Gedächtnisschwänze.

## 9. Exakte Zielidentität und der nicht verdeckte Rest

Setze `Gamma_a=kappa_*+2 sum_{k log p<=2a}w_{p,k}`,
`kappa_*=log pi-psi(1/4)`. Auf physischen Testzuständen definiert die bekannte
COMMON-JUMP-Form die explizite SIGNIERTE Portbilanz

```math
\mathfrak q^0_a[H]
=2\operatorname{Re}(\mathcal E_{+,a}H\,\overline{\mathcal E_{-,a}H})
+\|\mathcal GH\|^2+\sum_{k\log p\le2a}\|\mathcal P_{p,k}H\|^2
-\Gamma_a\|R_0H\|_2^2.
```

Mit der eingefrorenen COMMON-JUMP-Identität folgt exakt

```math
\mathfrak q^0_a[T^0_av]=Q_W[v].
```

Diese Bilanz ist aus dem Quellenmodell hergeleitet; sie ist noch keine
positive Norm und wird nicht als Skalarprodukt auf K^0_a ausgegeben.

Der konstruktive Gate C1 lautet: Gib C_a und einen positiven Zielraum aus der
Transport-/Portgeometrie an und beweise, OHNE q^0>=0 vorauszusetzen,

```math
\langle C_aT^0_av,C_aT^0_aw\rangle_{\mathcal K_{X,a}}=Q_W(v,w)
\quad(v,w\in\mathcal W_a),
```

zusammen mit §8. Unzulässig sind die Definition `||C_aT^0v||²:=Q_W[v]`,
ein formales `C_a=(q^0_a)^(1/2)` oder eine auf schon angenommener
Positive-real-/Weil-Positivität beruhende Realisierung. Eine positive
Storage-/Quotientenkonstruktion muss die negative Diagonalmasse tatsächlich
erklären. Ein endlicher Hilfsblock kann bei festgehaltenem oberen Block
`X_a*X_a` nicht die Subtraktion `Gamma_a I` auf dem unendlichdimensionalen
NULLPOL-Raum erzeugen (Rangargument; PR #127).

## 10. Falsifikation, Diagnose und unmittelbarer nächster Gate

### 10.1 Lokaler Defekt — A1-COMP konditional, KEIN X-Konstruktionsbeweis

`D_1(v)=E_+(v)-E_-(v)=<v,d_1>`, `d_1(x)=2sinh(x/2)`.
Unter dem eingefrorenen A1-Import besitzt die geschlossene Completion ihren
positiven selbstadjungierten Formoperator Acal_1. Der Riesz-Test ist exakt

```math
\rho_1=\sup_{0\ne v\in D(\mathfrak A_1)}\frac{|D_1(v)|^2}{\mathfrak A_1[v]}
=\langle d_1,\mathcal A_1^{-1}d_1\rangle
=4\langle\sinh(x/2),\mathcal A_1^{-1}\sinh(x/2)\rangle.
```

Er liegt ganz im ungeraden Sektor. `rho_1<=1` bedeutet vollständigen lokalen
Weil-Rücktransfer auf diesem Formbereich; bei Gleichheit ist Striktheit nicht
gesichert. Ein rigoroses tatsächliches `rho_1>1` liefert dort einen negativen
Weil-Testvektor, nicht nur eine unbrauchbare Abschätzung. Ein OBERBOUND >1 ist
dagegen lediglich unentschieden. Eine Ersetzung von Acal_1 durch L_1 liefert
nur einen ausreichenden oberen Vergleich, keinen äquivalenten Gegenbeweistest.
Hier wird kein Wert für rho_1 behauptet und keine neue Großrechnung gestartet.

### 10.2 Vorab fixierter Prime-2-Mischtest für jedes konkrete C1

Setze `ell=log 2`, `eps=1/100` und
`b_eps(x)=exp(-1/(1-(x/eps)²))` für |x|<eps, sonst 0.
Definiere `f=(-d²+1/4)b_eps(x+ell/2)`, `g=U_ell f`.
Beide liegen in W_1: partielle Integration vernichtet E_±. Ihre Träger sind
disjunkt. Unter den aktiven Verschiebungen log(2),log(3),log(4),log(5),log(7)
verbindet nur log 2 diese zwei Träger. Deshalb exakt

```math
Q_{fin}(f,g)=-\frac{\log2}{\sqrt2}\|f\|_2^2.
```

Jedes C1 muss diesen Anteil mit korrekter Gamma-/Polbilanz auf f, g, f+g und
f-g reproduzieren. Positive Gramformen dürfen negative gemischte Einträge
haben. Erfolg dieser Kalibrierung ist nur notwendig, kein Gesamtbeweis.
Dieser Test wird VOR Wahl zusätzlicher Koeffizienten fixiert.

### 10.3 Gates und Stop-Regeln für X-C0

- **C0-TYPE:** positiver Vormediator, explizites Lifting, vollständige Ports,
  nichtorthogonale Kopplung und J^0 sind in §§1–8 konstruiert; Beweise im Text.
- **C1-GEOM (aktiv/offen):** ein konkretes vorwärts definiertes C_a samt
  gemeinsamer positiver Storage- oder Quotientenkonstruktion; zuerst 10.2.
  Ein noch beliebiger positiver Operator als Platzhalter zählt nicht als Ergebnis.
- **C2-ID/C3-WINDOW (offen):** volle polarisierte Weil-Identität und
  kompatible J_{a,b} mit Domains/Kernen/Grenzübergängen.

Ein einzelner falscher Mischterm verwirft den betreffenden konkreten Kandidaten.
Eine fitted Cross-Matrix, ein endlicher Gamma_a-I-Shorting-Block, eine
unerklärte Tail-Löschung oder ein vorausgesetztes positives Q_W stoppen ihn.
Bleibt nur die signed Bilanz aus §9, lautet der Status weiterhin
**typisierte Vorstruktur / Positivitätsmechanismus offen**, nicht Objekt X.
Keine dieser Stop-Regeln öffnet automatisch den A1-Selbstaudit wieder.

## Quellenbindung und Abgrenzung

[COMMON-JUMP auf main](https://github.com/Waschtl904/objekt-x-programm/blob/ac164bbbd2c46623aa64e567d21f813f41f164b0/audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)
fixiert Q_W, K_t, Gewichte, Pole und Cutoff-Gauge.
[PR #116 @ b3a74a7](https://github.com/Waschtl904/objekt-x-programm/commit/b3a74a7497d9c92c4dcb289d72a395b341deb727)
und [PR #127 @ 76d5c96](https://github.com/Waschtl904/objekt-x-programm/commit/76d5c9671df3b84bd5a9b4257b4b9f07f9749490)
sind getrennte, ungemergte Strukturquellen/Negativtests, keine blanket Imports
von Positivität. Besonders relevant: `P11_COMMON_JUMP_TYPED_TREE_BRIDGE_2026-09-15.md`
und `P11_FINITE_RANK_SHORTING_NO_GO_2026-09-16.md` in PR #127.
Der Halbgeraden-RKHS, das Lifting und die Portformeln werden hier selbst
hergeleitet; die bekannte Digammareihe ist separat oben belegt.

Begleitend: `scripts/check_x_c0_memory_identities.py` prüft nur kleine exakte
C0-Identitäten und den algebraischen Mischtest. Es importiert KEINE A1-Daten,
startet KEINE CI-/Matrix-/LDL-Läufe und zertifiziert weder C1 noch RH.
