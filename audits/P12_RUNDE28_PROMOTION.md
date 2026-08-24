# P12 Runde 28 — Promotion der zentralen Next-Shell-Doppelhorizont-Box

**Status:** A15.1b2m / Round 28, R28-A `✓[M]_part`.  
**Review basis:** vollständige Kandidatenkette bis `main@83bad4b33949634c19643488a5ba185a0d959b36`.  
**Kandidaten:** `1caebfb27f8f56894ac9773de1650f3582763444` (Audit), `a2bfb7869c4d20f576890c6073d787470d39872e` (Verifier), `83bad4b33949634c19643488a5ba185a0d959b36` (Review-Paket).  
**Unabhängiger Review:** Perplexity hat die Kernassertions eigenständig rekonstruiert, ohne den retained verifier als Beweisersatz zu verwenden, und R28-A vollständig GREEN gegeben.  
**Firewall:** P11 FROZEN; R14 unverändert; kein globaler `rho`-Descent, keine vollständige Schließung der Next-Shell-Horizon-Lücke, keine Polar-Gauge-, Terminal-Transport-, Objekt-X- oder RH-Aussage.

---

## 1. Unabhängiges Urteil

Der externe Review hat die Round-28-Konstruktion aus dem kanonischen Rohoperator unabhängig neu aufgebaut und folgende Punkte GREEN bestätigt:

1. die exakte `J`-symmetrische Box `B28` liegt vollständig im residual-overlap-Ambientbereich;
2. auf ganz `B28` sind beide ersten neuen Supportvariablen `U_-`, `U_+` live;
3. auf ganz `B28` sind beide natürlichen Next-Shell-Quellen `V_-`, `V_+` horizon-illegal;
4. die 42 alten Quellen erzeugen dort exakt den Ausgangsdefekt `42 x 44`;
5. die retained 26 Zusatzquellen schließen mit den 42 alten Quellen zu genau 68 verschiedenen, `J`-abgeschlossenen Quellen;
6. diese 68 Quellen erzeugen genau 68 sichtbare Variablen und damit einen quadratischen Rohblock `M68`;
7. alle 1204 Source-/Sign-/Support-/Horizon-Rohbedingungen bleiben über der gesamten Box strikt positiv;
8. die unabhängig reproduzierte kleinste Rohmarge stimmt mit `1.57927617e-3` überein;
9. die exakte `J`-Blockstruktur `M68 = [[A34,B34],[B34,A34]]` wurde coefficient-for-coefficient bestätigt;
10. die Paritätsfaktoren, ihre Homogenität, die Relation `F_-(p,q,r)=F_+(p,-q,r)` und die beiden rigorosen Intervalle für `G_+` und `G_-` wurden unabhängig reproduziert;
11. daraus folgt strikt `det M68 != 0`.

Damit ist der lokale Mechanismus promotionsfähig.

---

## 2. Konstanten und Involution

Retain

\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\delta=\eta+\chi,
\]

\[
\kappa=e-\delta=2\eta+\chi,\qquad
E:=\varepsilon_{\max}=\frac12\log\frac54,\qquad
\rho=E-\delta.
\]

Die Involution lautet

\[
J(s,m,n)=(-s,m,n+s),
\qquad
x\mapsto\delta-x.
\]

---

## 3. Promovierte Box \(B_{28}\)

Die offene Box ist

\[
\boxed{\frac{19}{2000}<R<\frac{21}{2000}},
\]

\[
\boxed{\left|x-\frac{\delta}{2}\right|<\frac1{5000}},
\]

\[
\boxed{\frac{119}{2000}<\sigma<\frac{121}{2000}},
\]

\[
\boxed{\frac{139}{2000}<\varepsilon<\frac{141}{2000}}.
\]

Sie ist unter `x -> delta-x` invariant.

Auf ganz `B28` gelten strikt

\[
0<R<\rho,\qquad R<x,\qquad R<\sigma<\varepsilon<E.
\]

Zusätzlich sind beide ersten Supportvariablen live:

\[
\boxed{\sigma+x>\kappa},
\qquad
\boxed{\sigma-x>\eta}.
\]

Für die natürlichen Next-Shell-Quellen

\[
V_-=(-1,4,4),\qquad V_+=(1,4,3)
\]

gilt dagegen auf ganz `B28`

\[
\boxed{\varepsilon+x<2\delta},
\qquad
\boxed{\varepsilon-x<\delta}.
\]

Damit sind beide `V`-Quellen horizon-illegal.

Ferner gilt

\[
\boxed{\sigma>2\eta}.
\]

Somit liegt `B28` außerhalb der bereits promovierten C42-, C44-, C26- und W43-Kammern.

---

## 4. Ausgangsdefekt und 68-Quellen-Kreis

Die 42 alten Round-23/C42-Quellen erzeugen auf `B28` exakt

\[
42\text{ horizon-legale Zeilen}
\]

und

\[
44\text{ sichtbare Variablen}.
\]

Die zwei zusätzlichen Variablen sind genau

\[
U_-=(-1,5,1),\qquad U_+=(1,5,0).
\]

Der alte Support-Shell-Mechanismus steht daher bei

\[
\boxed{42\times44}.
\]

Die beiden naheliegenden Zusatzzeilen `V_-`, `V_+` sind gerade nicht verfügbar.

Der retained 68-Quellen-Kreis entsteht durch Hinzunahme der folgenden 26 Quellen:

```text
(-1,-1,3), (-1,0,3), (-1,0,4), (-1,1,-1), (-1,1,4),
(-1,2,-2), (-1,2,-1), (-1,2,5), (-1,3,-1), (-1,3,5),
(-1,3,6), (-1,4,-1), (-1,5,0),
( 1,-1,2), ( 1,0,2), ( 1,0,3), ( 1,1,-2), ( 1,1,3),
( 1,2,-3), ( 1,2,-2), ( 1,2,4), ( 1,3,-2), ( 1,3,4),
( 1,3,5), ( 1,4,-2), ( 1,5,-1).
```

Zusammen mit den 42 alten Quellen sind dies genau 68 verschiedene Quellen. Die Menge ist exakt unter `J` abgeschlossen und besteht aus 34 `J`-Paaren.

Die zugehörigen Rohzeilen erzeugen exakt 68 sichtbare Variablen. Auch diese Variablenmenge ist `J`-abgeschlossen und enthält insbesondere die Zielwerte

\[
h(x),\qquad h(\delta-x).
\]

Damit entsteht

\[
\boxed{M_{68}\in\operatorname{Mat}_{68\times68}}.
\]

Es wird weder Minimalität noch kanonische Bedeutung der Zahl 68 behauptet.

---

## 5. Vollständiges Raw-Pattern-Zertifikat

Für die 68 Quellen werden sämtliche Source-, Sign-, Support- und Horizon-Ereignisse des kanonischen Rohoperators erfasst:

- Source lower / Source upper;
- Vorzeichen der sechs Shift-Slots;
- bei live Slots untere und obere Supportgrenze;
- bei toten Slots die aktive dead-lower- bzw. dead-upper-Bedingung.

Insgesamt entstehen exakt

\[
\boxed{1204}
\]

strikte affine Rohbedingungen.

Die gesamte Box wird mit gerichteten rationalen Intervallen für `\log 2`, `\log 3`, `\log 5` zertifiziert. Der unabhängige Review reproduzierte die vollständige Positivität aller 1204 Bedingungen sowie dieselbe kleinste positive Rohmarge:

\[
\boxed{\text{min raw margin}>0.00157927617}.
\]

Damit schneidet keine verborgene Pattern-Wand `B28`, und derselbe symbolische Block `M68` gilt auf der gesamten Box.

---

## 6. Exakte \(J\)-Blockstruktur

In natürlicher Ordnung aus 34 negativen Quellen/Variablen und ihren `J`-Bildern gilt exakt

\[
\boxed{
M_{68}
=
\begin{pmatrix}
A_{34}&B_{34}\\
B_{34}&A_{34}
\end{pmatrix}.
}
\]

Mit

\[
Q=
\begin{pmatrix}
I&I\\
I&-I
\end{pmatrix}
\]

folgt exakt

\[
Q^{-1}M_{68}Q
=
\operatorname{diag}(A_{34}+B_{34},A_{34}-B_{34}).
\]

Daher

\[
\det M_{68}
=
\det(A_{34}+B_{34})\det(A_{34}-B_{34}).
\]

---

## 7. Exakte Nichtsingularität

Setze

\[
\beta:=\frac qp=2^{-3/4},
\qquad
v:=\left(\frac rp\right)^2
=\frac{\log3}{\log2}\sqrt{\frac8{27}}.
\]

Die beiden Paritätsdeterminanten faktorisierten symbolisch als

\[
\det(A_{34}+B_{34})
=
-p^{12}qr^8F_+(p,q,r),
\]

\[
\det(A_{34}-B_{34})
=
p^{12}qr^8F_-(p,q,r),
\]

wobei `F_+` und `F_-` homogen vom Grad 13 sind und exakt

\[
F_-(p,q,r)=F_+(p,-q,r)
\]

gilt.

Nach

\[
F_+(p,q,r)=p^{13}G_+(\beta,v),
\qquad
F_-(p,q,r)=p^{13}G_-(\beta,v)
\]

gilt

\[
G_-(\beta,v)=G_+(-\beta,v).
\]

Der unabhängige Review reproduzierte die rigorosen Intervalle

\[
\boxed{
0.3822065426030501
<
G_+(\beta,v)
<
0.38220654260305015
}
\]

und

\[
\boxed{
0.20288790549604774
<
G_-(\beta,v)
<
0.20288790549604777
}.
\]

Beide Faktoren sind strikt positiv. Daher

\[
\boxed{
\det M_{68}
=
-p^{68}\beta^2v^8
G_+(\beta,v)G_-(\beta,v)
\neq0.
}
\]

---

## 8. Promovierte lokale Konsequenz

Für jeden Parameterpunkt in `B28` rekonstruiert der kanonische Rohoperator denselben invertierbaren 68×68-Block. Somit verschwinden alle 68 Sichtbarkeitsvariablen dieses Blocks. Insbesondere

\[
\boxed{h(x)=h(\delta-x)=0}.
\]

Formal wird daher gebucht:

\[
\boxed{\mathrm{R28\!-\!A}:\checkmark[M]_{\rm part}.}
\]

Dies ist ein lokaler Fasermechanismus innerhalb der zentralen Next-Shell-Doppelhorizont-Front.

---

## 9. Scope-Firewall

Round 28-A beweist ausdrücklich **nicht**:

- die vollständige Next-Shell-Horizon-Lücke;
- die beiden Zwischenzellen, in denen genau eine der Quellen `V_-`, `V_+` horizon-legal ist;
- den tiefen Horizon-Rest außerhalb `B28`;
- den Outer-Core-Rest;
- globale Kerneltrivialität für `0<R<rho`, `sigma>R`;
- einen neuen globalen Radius-Schwellenwert;
- Minimalität oder kanonische Bedeutung des 68er-Blocks;
- Polar Gauge, Strong/Terminal Transport, Objekt X oder RH.

Der globale Descent unterhalb `rho` bleibt

\[
\boxed{?[O]}.
\]

P11 bleibt FROZEN. Die R14-Firewall bleibt unverändert.

---

## 10. Nächste Patternfront

Nach Promotion der zentralen Doppelhorizont-Box ist die unmittelbar benachbarte Front nicht mehr die zentrale `V_-`/`V_+`-illegale Zelle, sondern die **einseitigen Zwischenzellen**, in denen genau eine der beiden Quellen horizon-legal ist.

Für Round 29 ist daher eine rückwärts gerichtete Invariantensuche sinnvoll: Welche algebraische oder `J`-gepaarte Eigenschaft muss ein Zertifikat unmittelbar vor dem Übergang von der zentralen 68er-Zelle zur vollständig legalen C44-Seite bewahren? Diese Frage ist Forschungsheuristik, kein Teil der Promotion.
