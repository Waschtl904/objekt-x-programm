# P11 / R43 — Echte lokale O1-Intervalluniformität

Datum: 2026-09-07.
Quellstand: `main` = `2a43813480629c56200d2910963294fa0c4137fd`.
Status: ausgearbeiteter analytischer Beweis zur Exact-Head-Prüfung;
kein unabhängiger Review, kein Registry-Eintrag, kein mathematischer Freeze.

**Gegenstand:** der erste analytische Auftrag des Arbeitsplans
„Strong Terminal/C6: beweisorientierter Arbeitsplan“ vom 7. September 2026.
Untersucht werden die wirklichen P11-Operatoren auf ihren unendlichdimensionalen
Funktions- und Graph-Hilberträumen, nicht die Drei-Band-/Gitter-Proxys.
`local` bezeichnet hier ein beschränktes Terminalintervall, nicht eine
endlichdimensionale Näherung.

## 0. Abschlussbogen und Statusgrenzen

Für ein festes Paar `0<R<S` lautet das Ziel weiterhin

```math
\forall\epsilon>0\ \exists M>S\ \forall T,U\ge M:
\quad\|W_{R,S}^{[U]}\varepsilon_R-W_{R,S}^{[T]}\varepsilon_R\|<\epsilon.
```

Der Normalbahn-/R42-Rahmen wird aus R43 übernommen, nicht neu zertifiziert.
Die GC-AC-Voraussetzungen der Tightness-/Sign-Route bleiben bedingt und werden
für den nachstehenden lokalen Satz überhaupt nicht benötigt.

| Eingang des Abschlussvertrags | Stand dieses Dokuments |
|---|---|
| Endliche P11-Graphgeometrie, positive Gamma-Form, exakte Terminalmetriken | Ausgewiesene Primärdefinitionen; siehe Quellenverzeichnis |
| Kanonische tiefe Flagge: `P_m -> 0` stark im ungeraden Zielgraphraum | Ausgewiesener C6a-/R43-Eingang; keine Ersatzbasis |
| Für jedes feste Terminalintervall uniforme projizierte vollständige O1-Defekte | In §§1–8 bewiesen, externe Exact-Head-Prüfung offen |
| Summierbare Majorante über alle großen Terminalintervalle | OPEN; nicht aus lokaler Kompaktheit gefolgert |
| GC-AC-/Tangentialvoraussetzungen und gemeinsames terminales Vorzeichen | Status unverändert; nicht Gegenstand dieses Beweises |
| FD23, globale Flag-Tightness, Strong Terminal/C6 | Kein Abschluss in diesem Dokument |

Die zusätzliche exakte Beobachtung in §7 ist: Beide **vollständigen** O1-
Defektoperatoren sind Differenzen von Isometrien und haben Norm höchstens 2.
Eine konstante Majorante über alle Intervalle ist jedoch nicht summierbar.

## 1. Satz und benötigte Quantoren

Arbeite in den festen ungeraden Graph-Hilberträumen
`H_X = K_{X,X}^-` für `X=R,S`; der erste Index in `K` bezeichnet wie in P11
die Object-X-Graphgeometrie. Sei `S<U_0<B<infinity` fest und
`I=[U_0,B]`. Schreibe `W_V=W_{R,S}^{[V]}` und `W_0=W_{U_0}`.
Alle Adjunktionen der Quellmetriken und O1-Operatoren sind Graphraum-Adjunktionen.

Mit den unveränderten Definitionen FD1–FD18 sei

```math
C_X(V)=G_{X,V}^{1/2}G_{X,U_0}^{-1/2}
       =\mathcal U_X(V)A_X(V)^{1/2},
\qquad A_X(V)=C_X(V)^*C_X(V),
```

```math
\mathscr L(V)=(I-W_0W_0^*)A_S(V)^{1/2}W_0,
\qquad
\mathscr J(V)=A_R(V)^{1/2}-W_0^*A_S(V)^{1/2}W_0,
```

```math
\mathcal T_{\rm mod}(V)
 =\mathcal U_S(V)(\mathscr L(V)-W_0\mathscr J(V))
   A_R(V)^{-1/2}\mathcal U_R(V)^*,
```

```math
\mathcal T_{\rm ph}(V)
 =\mathcal U_S(V)W_0\mathcal U_R(V)^*-W_0.
```

**Satz LOCAL-O1.** Für die P11-Definitionen am angegebenen Quellstand gilt:

1. `V -> G_{X,V}` ist auf `I` stückweise operatornormstetig mit endlich vielen
   möglichen Sprungstellen und operatornormseitigen Grenzwerten an allen
   Übergängen. Es gibt explizite positive lokale Spektralschranken, siehe §5.
2. Beide `T_j(V)` sind kompakte Operatoren `H_R -> H_S`, jeweils von Norm
   höchstens 2. Ihre Familien über `I` sind relativ kompakt in Operatornorm.
3. Für die echten kanonischen Flagprojektionen gilt sogar

```math
\lim_{m\to\infty}\sup_{V\in I}
 \bigl(\|P_m\mathcal T_{\rm mod}(V)\|
       +\|P_m\mathcal T_{\rm ph}(V)\|\bigr)=0.
\tag{LI1}
```

Insbesondere folgt für den festen Einheitsvektor `epsilon_R`

```math
\lim_{m\to\infty}\sup_{V\in I}
 \bigl(\mathfrak d_{m,\rm mod}(U_0,V)
       +\mathfrak d_{m,\rm ph}(U_0,V)\bigr)=0.
\tag{LI2}
```

Damit ist für jedes feste `k` der Intervallteil `D_{m,k}->0` des vorgeschlagenen
Abschlussvertrags erfüllt. Keine Uniformität in `B->infinity`, keine Rate in `k`
und keine Summation über `k` sind Bestandteil von LI1 oder LI2.

## 2. Fester Umgebungsraum und wandernde Masken

Benutze `H=L^2(R)` und die ungekürzten Translationen `U_t` auf `H`.
Setze `M_V=1_{(-V,V)}` und `D_s=U_{s/2}-U_{-s/2}`, also `||D_s||<=2`.
Für Primzahl `p` und `a>=0` sei

```math
M_{p,a}(V)=1_{\{|u|<V-(a+1)\log p/2\}},
```

mit leerer Menge, wenn der Radius nicht positiv ist. Endpunkte sind in `L^2`
irrelevant. Dies ist genau die Maske `1_{Omega_{p,a,V}}` der vollständigen
P11-Martingaldarstellung, nicht ein neuer Cutoff.

Für `V_n->V`, jedes `f in H` und jede dieser Masken konvergieren die
Indikatoren fast überall und sind durch 1 beschränkt. Dominierte Konvergenz
auf `|f|^2` ergibt starke Konvergenz der Multiplikatoren. Sie sind selbstadjungiert,
also auch stark-* stetig. Dies gilt ebenfalls beim Entstehen einer Maske aus
einem Radius 0.

**Nicht** operatornormstetig sind die Rohfenstermasken: für `V!=V'` hat
`M_V-M_{V'}` bei nichtleerem Differenzstreifen Norm 1. Die Normstetigkeit in
§5 wird daher bewiesen und nicht von den Rohmasken übernommen.

## 3. Der vollständige Restoperator ist stark-* stetig

Für das feste obere Intervallende `B` genügen die endlichen Indexmengen

```math
\mathcal I_B=\{(p,a):p\ {m prim},\ a\ge0,
                       (a+1)\log p\le2B\},
\qquad K_B(p)=\lfloor4B/\log p\rfloor.
```

Wähle als gemeinsamen Zielraum
`Z_B = direct_sum_{(p,a) in I_B} L^2(R)`.
Dieser Raum ist trotz endlich vieler Zeilen **unendlichdimensional**.
Auf `H -> Z_B` definiere

```math
(\widehat R(V)f)_{p,a}
 =c_{p,a} M_{p,a}(V)
      \sum_{k=a+1}^{K_B(p)}p^{-3k/4}D_{k\log p}M_V f,
\qquad
c_{p,a}=\sqrt{(\log p)(p-1)p^a}.
\tag{LI3}
```

Leere Summen sind 0. LI3 ist die **exakte** gemeinsame Einbettung der
P11-Analyse `tilde R_V`, deren Gram nach (3.5) `R_V^*R_V` ist.
Die `k`-Summanden innerhalb einer `(p,a)`-Zeile bleiben kohärent;
keine Orthogonalität verschiedener Prime-Powers wird eingeführt.

Warum fehlt kein aktiver Index? Ein aktiver Tiefenindex benötigt
`(a+1)log p<=2V<=2B`. Eine Translation mit einem alten Eingabepunkt und einem
Ausgabepunkt in `[-V,V]` benötigt `k log p/2<=2V<=2B`, also `k<=K_B(p)`.
Alle weiter entfernten Übersetzungen sind auf den relevanten Masken identisch 0.
Das ist eine exakte endliche Indexobergrenze, keine Galerkin-Approximation.
Insbesondere wird der **Rest** nicht fälschlich beim Hub-Cutoff `p^k<=exp(2V)`
abgeschnitten; seine sichere Obergrenze ist `p^k<=exp(4B)`.

Produkte gleichmäßig beschränkter stark stetiger Operatoren sind stark stetig:
für `A_n->A`, `B_n->B` stark folgt dies aus
`(A_n B_n-AB)f=A_n(B_n-B)f+(A_n-A)Bf`.
Auf die endlich vielen Masken-/Translationsprodukte in LI3 angewandt ergibt
dies starke Stetigkeit. Die adjungierte Zeile ist ausdrücklich

```math
c_{p,a} M_V\sum_{k=a+1}^{K_B(p)}p^{-3k/4}D_{k\log p}^*M_{p,a}(V).
```

Sie ist ebenso stark stetig. Die endlich vielen Zeilen geben daher
starke-* Stetigkeit von `Rhat(V)` zwischen den **festen** Hilberträumen.

Eine gültige endliche lokale Normschranke ist

```math
\|\widehat R(V)\|^2\le r_B^2
 :=4\sum_{(p,a)\in\mathcal I_B}c_{p,a}^2
       \left(\sum_{k=a+1}^{K_B(p)}p^{-3k/4}\right)^2<\infty.
\tag{LI4}
```

Es wird weder eine nützliche Wachstumsrate dieser Konstante noch ein
primitives Formdominierungsargument benötigt oder behauptet.

## 4. Resolvente, arithmetische Hub-Sprünge und volle Schurform

Auf dem festen `H` setze

```math
\widehat B(V)=(I+\widehat R(V)^*\widehat R(V))^{-1}.
```

Sie ist selbstadjungiert und `0<Bhat(V)<=I`. Das Gram ist stark stetig nach
§3. Die Resolventenidentität

```math
\widehat B(V_n)-\widehat B(V)
 =\widehat B(V_n)
  (\widehat R(V)^*\widehat R(V)
   -\widehat R(V_n)^*\widehat R(V_n))\widehat B(V)
```

beweist starke, damit hier starke-* Stetigkeit von `Bhat` ohne eine
verdeckte Konditionskonstante.

Der Umgebungsraumoperator ist nicht einfach die durch 0 erweiterte inverse
Matrix: mit Restriktion `P_V` und Erweiterung `E_V` gilt exakt

```math
\widehat B(V)=E_V B_V P_V+(I-M_V).
\tag{LI5}
```

Dies folgt daraus, dass `Rhat(V)=Rhat(V)M_V`; auf dem äußeren orthogonalen
Komplement ist das invertierte Gram gleich `I`.

Der tatsächliche Hub lautet im Umgebungsraum

```math
\widehat H(V)
 =M_V\sum_{p^k\le e^{2B}}
   1_{\{k\log p/2\le V\}}\sqrt{\log p}\,p^{-3k/4}
    D_{k\log p}M_V.
\tag{LI6}
```

Es gilt `Hhat(V)=E_V H_V P_V` und

```math
\|\widehat H(V)\|\le h_B
 :=2\sum_{p^k\le e^{2B}}\sqrt{\log p}\,p^{-3k/4}<\infty.
\tag{LI7}
```

Die arithmetischen Aktivierungsstellen
`E_B={k log p/2 : p^k<=exp(2B)}` sind endlich. Auf jedem offenen
Teilintervall ohne solche Stelle ist `Hhat` stark-* stetig.
An einer Aktivierungsstelle existieren beide starken-* Grenzwerte:
die Masken konvergieren wie zuvor; im linken Grenzwert bleiben genau die
strikt früher aktiven Indizes, im rechten zusätzlich die dort aktivierten.
Die P11-Konvention `<=` stimmt mit dem rechten Grenzwert überein.
Ein linksseitiger Hub-Sprung wird **nicht** als 0 angenommen.
An einem Endpunkt des untersuchten Intervalls wird sein tatsächlicher Wert
gegebenenfalls als zusätzlicher einzelner Wert berücksichtigt.

Setze nun

```math
\widehat\Sigma(V)=\widehat H(V)\widehat B(V)\widehat H(V)^*.
\tag{LI8}
```

Wegen LI5 und der beidseitigen Fensterstütze des Hubs ist dies genau
`E_V Sigma_V P_V`, nicht eine veränderte Feshbach-Geometrie.
Die Familie ist positiv, durch `h_B^2` beschränkt und stückweise stark-*
stetig mit den soeben konstruierten einseitigen Grenzwerten.
Alle höheren Prime-Powers, Residualzeilen und Randmasken bleiben enthalten.
Eine Positivität des **Inkrements** über eine Hub-Sprungstelle wird nicht
behauptet; nur jeder einzelne Schurterm ist positiv.

## 5. Der entscheidende Graphraumtransfer

### 5.1 Kompakte feste Einbettung

Sei `i_X` die Inklusion des festen Quellgraphraums in `L^2(-X,X)` und
`j_X=E_X i_X : H_X -> H`. Sie ist kompakt.

Dies folgt bereits aus der P11-Gamma-Graphraum-Aussage und der festen
Graphnormäquivalenz. Zur expliziten Kontrolle kann man es direkt zeigen:
Für `||f||_{X,X}<=1` gilt wegen `q_X>=c_Gamma,X` und
`m_Gamma(xi)>=c log(2+|xi|)` gleichmäßig

```math
\int_{|\xi|>N}|\widehat{E_X f}(\xi)|^2\,d\xi
 \le \frac{C}{\log(2+N)}.
```

Die Fouriertransformation von `L^2(-X,X)` nach `L^2(-N,N)` hat den
quadrat-integrierbaren Kern `exp(-iu xi)` mit der gewählten Fourier-Normierung.
Sie ist Hilbert-Schmidt, insbesondere kompakt (Approximation des Kerns durch
endliche Summen von Produktfunktionen gibt endlichen Rang).
Inverse Fouriertransformation nach Erweiterung durch 0 und Komposition mit
der beschränkten Graphraum-Inklusion erhalten Kompaktheit.
Die angegebene Frequenzschranke zeigt Konvergenz dieser kompakten Approximationen
zu `j_X` in Operatornorm. Also ist `j_X` kompakt.
Hier wird weder eine positive Sobolev-Regularität der ganzen Graphdomäne noch
eine endlichdimensionale Quellapproximation vorausgesetzt.

### 5.2 Exakte Metrikformel und Spektralschranken

Bezeichne mit `Gamma_X` den beschränkten positiven Operator der Gamma-Form
**im festen Graphraum**. Dann folgt aus der Definition der Terminalmetrik
und der exakten Gamma-Kompatibilität unter Nullerweiterung

```math
G_{X,V}=\Gamma_X+j_X^*\widehat\Sigma(V)j_X.
\tag{LI9}
```

Das `j_X^*` ist das Adjunkt `H -> H_X`, nicht bloß eine rohe L2-Restriktion.
Aus `q_X<= (1+||H_X^{hub}||^2)c_Gamma,X` und `q_X>=c_Gamma,X>=||f||_2^2`
ergeben sich die konkreten Schranken

```math
c_X I\le G_{X,V}\le M_B I,
\qquad c_X=(1+\|H_X^{hub}\|^2)^{-1}>0,
\qquad M_B=1+h_B^2.
\tag{LI10}
```

Das hochgestellte `hub` unterscheidet den P11-Huboperator vom hier `H_X`
genannten ungeraden Graph-Hilbertraum. LI10 gilt auch für alle einseitigen
Grenzmetriken. Die untere Schranke hängt nur vom festen Quellradius ab;
die obere darf vom beschränkten Terminalintervall abhängen.

### 5.3 Von starker zu Operatornormkonvergenz

Elementares Kompakttransfer-Lemma: Sind `S_n->S` stark, die Operatoren
uniform beschränkt und `K` kompakt, dann

```math
\|(S_n-S)K\|\longrightarrow0.
```

Beweis: Überdecke `K` der Einheitskugel durch ein endliches `eta`-Netz.
Starke Konvergenz ist auf den endlich vielen Netzzentren uniform; der Fehler
zum jeweiligen Zentrum ist höchstens `sup_n||S_n-S|| eta`.
Erst `n->infinity`, dann `eta->0` ergibt die Behauptung.

Wende das Lemma auf die tatsächlichen starken beziehungsweise einseitigen
Grenzen von `Sigmahat(V)` und das feste kompakte `j_X` an. LI9 liefert
Operatornormstetigkeit auf jeder Zelle sowie einseitige Operatornormgrenzwerte
an jeder Hub-Aktivierung. Damit ist Behauptung 1 des Satzes bewiesen.
Zusätzlich gilt für beliebige zwei endliche Horizonte

```math
G_{X,V}-G_{X,U}
 =j_X^*(\widehat\Sigma(V)-\widehat\Sigma(U))j_X
 \quad\hbox{kompakt auf }H_X.
\tag{LI11}
```

Kompaktheit entsteht hier durch die **feste Gamma-Graphraumeinbettung**, nicht
allein durch Endlichkeit der arithmetischen Indexmenge.

## 6. Wurzeln, Inversen und Polarphasen ohne unkontrollierte Lücke

Für positive beschränkte `A,B>=cI`, `c>0`, gilt auch ohne Kommutativität

```math
A^{1/2}-B^{1/2}
 =\int_0^\infty e^{-tA^{1/2}}(A-B)e^{-tB^{1/2}}\,dt.
\tag{LI12}
```

Denn für `D=A^{1/2}-B^{1/2}` ist
`A^{1/2}D+DB^{1/2}=A-B`; Integration der Ableitung von
`exp(-t A^{1/2}) D exp(-t B^{1/2})` beweist LI12.
Das Integral konvergiert in Norm, und daher

```math
\|A^{1/2}-B^{1/2}\|\le\frac{\|A-B\|}{2\sqrt c},
\qquad
\|A^{-1/2}-B^{-1/2}\|
 \le\frac{\|A-B\|}{2c^{3/2}}.
\tag{LI13}
```

Für die zweite Ungleichung verwende
`A^{-1/2}(B^{1/2}-A^{1/2})B^{-1/2}`.
Ist `A-B` kompakt, so ist auch LI12 kompakt: jedes Integrandprodukt ist
kompakt, das Integral ein Operatornormlimit kompakter Riemannsummen.
Dasselbe gilt für die Differenz der inversen Wurzeln.

Nach LI10 haben deshalb `G_{X,V}^{+/-1/2}` dieselbe stückweise
Operatornormregularität samt einseitigen Grenzwerten. Für die relativen
Metriken liegen ausdrücklich die Schranken

```math
\frac{c_X}{\|G_{X,U_0}\|}I\le A_X(V)
 \le M_B\|G_{X,U_0}^{-1}\|I
\tag{LI14}
```

vor. Somit sind auch `A_X(V)^{+/-1/2}` kontrolliert.
`C_X(V)` ist invertibel, also ist sein Polarfaktor

```math
\mathcal U_X(V)=C_X(V)A_X(V)^{-1/2}
```

unitär, stückweise operatornormstetig und mit einseitigen
Operatornormgrenzwerten versehen. Ein Rangwechsel oder ein unkontrollierter
Near-null-Polarfaktor wird nicht übergangen.

Aus LI11–LI13 folgt außerdem

```math
C_X(V)-I,\quad A_X(V)-I,\quad A_X(V)^{-1/2}-I,
\quad\mathcal U_X(V)-I\quad\hbox{kompakt}.
\tag{LI15}
```

Zum Beispiel ist `C_X-I=(G_{X,V}^{1/2}-G_{X,U_0}^{1/2})G_{X,U_0}^{-1/2}`,
`A_X-I=(C_X^*-I)C_X+(C_X-I)` und
`U_X-I=(C_X-I)A_X^{-1/2}+(A_X^{-1/2}-I)`.

Für den festen beschränkten Übergang `J=J_{R,S}` ist

```math
W_V=G_{S,V}^{1/2}J G_{R,V}^{-1/2}
```

folglich ebenfalls stückweise operatornormstetig mit den genannten Grenzen.
Die Differenz zum Basiswert ist kompakt, denn

```math
W_V-W_0
 =(G_{S,V}^{1/2}-G_{S,U_0}^{1/2})J G_{R,V}^{-1/2}
 +G_{S,U_0}^{1/2}J(G_{R,V}^{-1/2}-G_{R,U_0}^{-1/2}).
\tag{LI16}
```

Die Isometrie jedes tatsächlichen `W_V` ist die exakte P11-Pullback-Identität,
nicht eine asymptotische Voraussetzung.

## 7. Beide vollständigen O1-Kanäle sind kompakte Isometriedifferenzen

Die exakte Algebra ergibt

```math
\mathscr L-W_0\mathscr J
 =A_S^{1/2}W_0-W_0A_R^{1/2}.
```

Außerdem liefert FD1 in der Polarschreibweise

```math
W_V=\mathcal U_S A_S^{1/2}W_0A_R^{-1/2}\mathcal U_R^*.
```

Setze `Y(V)=U_S(V) W_0 U_R(V)^*`. Dann gelten exakt

```math
\boxed{\mathcal T_{\rm mod}(V)=W_V-Y(V)},
\qquad
\boxed{\mathcal T_{\rm ph}(V)=Y(V)-W_0}.
\tag{LI17}
```

Alle drei Operatoren `W_V,Y(V),W_0` sind Isometrien. Daher

```math
\|\mathcal T_{\rm mod}(V)\|\le2,
\qquad \|\mathcal T_{\rm ph}(V)\|\le2.
\tag{LI18}
```

Dies gilt auch dann, wenn einzelne rohe Normmajoranten der nicht vereinfachten
O1-Produkte große Konditionszahlen enthalten. Es ist aber nur Beschränktheit,
keine kleine inkrementelle oder summierbare Abschätzung.

Nach LI15 ist

```math
Y(V)-W_0
 =(\mathcal U_S(V)-I)W_0\mathcal U_R(V)^*
   +W_0(\mathcal U_R(V)^*-I)
```

kompakt. LI16 und LI17 machen auch `T_mod(V)` kompakt.
Beide Familien sind stückweise operatornormstetig mit endlich vielen
Sprungstellen und allen einseitigen Normgrenzen. Bei `V=U_0` verschwinden
beide exakt. Es werden die tatsächlichen vollständigen O1-Kanäle behandelt;
keine additive COND/GEO/NEW-Zerlegung wird auf Wurzeln übertragen.

## 8. Normrelative Kompaktheit und uniforme Flagprojektion

Eine operatornormstetige Familie auf einem offenen Teilintervall mit
Normgrenzwerten an beiden Enden besitzt durch Hinzufügen dieser Grenzwerte
eine kompakte Bildmenge. Hier gibt es nur endlich viele solche Teilintervalle
und gegebenenfalls einzelne tatsächliche Übergangswerte.
Daher sind beide Familien `{T_j(V):V in I}` relativ operatornormkompakt.
Ihre Abschlüsse bestehen weiter aus kompakten Operatoren, weil diese in
Operatornorm abgeschlossen sind.

Die kanonische C6a-Eigenschaft gibt `P_m->0` stark auf `H_S^0`.
Weil `P_m epsilon_S=0` für `m>=1` und
`H_S = C epsilon_S direct_sum H_S^0`, gilt sie auf dem ganzen ungeraden
Zielgraphraum. Für jeden festen kompakten Operator `K:H_R->H_S` folgt
daraus mit `||P_m||<=1`, dass `||P_m K||->0`.
Dies folgt aus demselben endlichen Netzargument auf `K` der Einheitskugel.
Für ein endliches Operatornorm-`eta`-Netz `K_1,...,K_N` der Familie erhält man

```math
\sup_{V\in I}\|P_m\mathcal T_j(V)\|
 \le\max_{1\le l\le N}\|P_mK_l\|+\eta.
```

Erst `m->infinity`, dann `eta->0` beweist LI1. Anwendung auf den festen
Einheitsvektor `epsilon_R` beweist LI2 und den im Arbeitsplan verlangten
Grenzwert `D_{m,k}->0` für jedes feste `k`.

Die behauptete normrelative Kompaktheit der tatsächlichen unprojizierten
Vektorfamilien `Z_k^mod,Z_k^ph` folgt ebenso direkt, indem die
operatornormkompakten Familien auf `epsilon_R` angewendet werden.
Hier wird also nicht bloß eine äquivalente Kompaktheitsvermutung formuliert:
alle benötigten Rohoperator-, Graphraum- und Normalisierungsschritte sind
oben aus den P11-Definitionen abgeleitet.

## 9. Was nicht geschlossen ist: der große Terminalbereich

LI1 ist lokal in `B` und besitzt keine Rate, die über dyadische Intervalle
summiert werden kann. LI18 liefert lediglich `D_{m,k}<=4`; die Reihe mit
dieser Majorante divergiert.

Offen bleibt insbesondere eine Majorante unabhängig von `m` mit

```math
D_{m,k}\le a_k,\qquad\sum_{k\ge0}a_k<\infty,
```

oder eine geeignete schwächere positive-Flagvariationskontrolle aus dem
Arbeitsplan. Erst eine solche zusätzliche Aussage gestattet das dominierte
Summieren in `k`. Weder der kanonische Reverse-Stretch noch die quantitative
vollständige Modulus-/Phasenbewegung wird hier abgeschätzt.

### Explizite Firewall gegen eine falsche lokale-zu-globale Folgerung

Auf `ell^2(N)` mit Basis `e_k` definiere für `V in [2^k,2^{k+1}]`, `k>=1`,

```math
w(V)=\cos\theta(V)e_k+\sin\theta(V)e_{k+1},
\qquad \theta(V)=\frac\pi2\frac{V-2^k}{2^k}.
```

Das ist eine normstetige Einheitsbahn; ihre Bildmenge auf jedem beschränkten
Intervall ist sogar in einem endlichdimensionalen Unterraum enthalten.
Für jede tiefe Standard-Flagge `P_m` gilt deshalb lokale Uniformität.
Trotzdem ist `sup_{V>=2}||P_m w(V)||=1` für jedes `m`, und
`w(2^k)=e_k` ist nicht Cauchy. Die dyadische maximale Bewegung ist `sqrt(2)`
in jedem Intervall.

Dies ist ein abstraktes Gegenbeispiel nur zur Folgerung
„lokale Kompaktheit impliziert globale Tightness/C6“, **kein** P11-Gegenbeispiel.
Ebenso liefert stückweise Normregularität mit endlich vielen Sprüngen auf
jedem beschränkten Intervall keine asymptotisch uniforme Antipoden-Schranke.
Die separate Orientierungskontrolle bleibt offen.

## 10. Destruktiver Eigencheck und Reviewauftrag

| Möglicher Bruchpunkt | Im Beweis verwendete Kontrolle |
|---|---|
| Wandernde Indikatoren fälschlich operatornormstetig | §2 verwendet starke-* Grenzwerte; Roh-Normstetigkeit wird ausdrücklich verneint |
| Endlich viele Indizes als endlichdimensionaler Funktionenraum gelesen | §3 behält vollständige L2-Zeilen; Kompaktheit entsteht erst in §5 |
| Höhere Prime-Powers durch Hub-Cutoff verloren | Restobergrenze `p^k<=exp(4B)`; Hubobergrenze getrennt `p^k<=exp(2B)` |
| Innerprimzahlige Kreuzterme ignoriert | Kohärente `k`-Summe bleibt innerhalb jeder Martingalzeile erhalten |
| Inverse außerhalb des Fensters falsch erweitert | LI5 enthält ausdrücklich `I-M_V` |
| Arithmetische Aktivierung als stetig angenommen | §4 konstruiert linke und rechte Hubgrenzen getrennt; tatsächlicher Wert rechtsseitig |
| Falsches Adjunkt oder falscher Hilbertraum | LI9 benutzt das Adjunkt der festen Graphraum-Einbettung |
| Spektrallücke bei Wurzeln/Polarphase verloren | LI10, LI13 und LI14 liefern explizite positive lokale Schranken |
| Nur Modulus, nicht Phase untersucht | LI15 und LI17 behandeln den tatsächlichen unitären Polarfaktor und beide Defekte |
| Lokale Kompaktheit setzt globale Tightness voraus | Eingänge sind ausschließlich lokale P11-Geometrie und feste Gamma-Einbettung |
| `m`-Grenze ohne Majorante durch unendliche `k`-Summe getauscht | §9 lässt genau diese globale Beweisverpflichtung offen |

Der Eigencheck ist keine unabhängige Freigabe. Der externe Reviewer soll
insbesondere LI3 gegen (2.6)/(3.4), LI5 gegen die tatsächliche Kompression,
LI9 gegen die Graphraumdefinition, LI14 gegen die Normalisierungsreihenfolge
und LI17 gegen FD5/FD17/FD18 prüfen. Danach sind die beiden Kompakttransfer-
Argumente und sämtliche Quantoren von LI1/LI2 zu kontrollieren.

**Buchungsvorschlag nur für den dokumentierten Satz:**
`R43-O1-LOCAL-INTERVAL-UNIFORMITY — analytischer lokaler Kandidat`.
Keine unabhängige GREEN-Buchung; das bestehende Registry bleibt unverändert.
`FD23-SUMMABILITY`, globale `B-FLAGDYN/TIGHT`, `B-SIGN`, Strong Terminal/C6,
Objekt X und RH erhalten keine Promotion.

## 11. Primärquellen und exakter Ableitungsumfang

Alle Repository-Quellen sind auf denselben oben genannten Commit gepinnt.
Der neue Beweis benötigt keine numerischen XBAND-Ergebnisse und kein
Asymptotik- oder GC-AC-Lemma.

1. [P11: vollständige Definitionen und feste Graphgeometrie](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex).
   Verwendet: (2.1)–(2.8), Gamma-Graphraum-Proposition, (3.1)–(3.5),
   (4.4)–(4.8). Gelesener Git-Blob:
   `6d9260d2f3e9b0f3bb463578a8530e078aa0a050`.
2. [O1-/FD23-Reduktion](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_FLAGDYN_O1_MODULUS_PHASE_REDUCTION_2026-09-04.md).
   Verwendet: FD1–FD5, FD17–FD24. Gelesener Git-Blob:
   `e8dae49eeed26471ddb9061a56da9433c67e7379`.
3. [R43: kanonischer Normalvektor und Flagge](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_REFEREE_E2E_R43_SINGLE_NORMAL_C6_GATE_2026-09-02.md).
   Verwendet: R43.1–R43.6 und die dort ausgewiesene C6a-Flagge.
   Gelesener Git-Blob: `983b42949d6a4a1806c0b333727cb49000b99972`.
4. [FD23-Kompaktheitsaudit](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md).
   Verwendet: §7, starkes Verschwinden der echten kanonischen Tailprojektionen
   und die bisher ausdrücklich offen gehaltene konkrete Intervallkompaktheit.
5. [R43-Stackintegration](https://github.com/Waschtl904/objekt-x-programm/blob/2a43813480629c56200d2910963294fa0c4137fd/audits/R43_STACK_INTEGRATION_2026-09-07.md).
   Governance-/Statusquelle, kein zusätzlicher mathematischer Eingang.

Zusätzliche Hilfsschritte — Maskengrenzen, vollständige lokale Indexbindung,
Kompakttransfer, Normkontinuität/Kompatheit der Wurzeldifferenzen und die
uniforme Projektion der Defektfamilien — sind in diesem Dokument bewiesen,
nicht als ungeprüfte Literaturbehauptung ergänzt.
