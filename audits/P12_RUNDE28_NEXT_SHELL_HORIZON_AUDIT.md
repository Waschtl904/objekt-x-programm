# P12 Runde 28 — zentrale Next-Shell-Doppelhorizont-Lücke und 68×68-Kreis

**Status:** Kandidat; **nicht promotet**.  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main@e486620f4852baa9d921cece94986d841cf13a1f`.  
**Input:** Round 27 / A15.1b2l, R27-A und R27-B `✓[M]_part`.  
**Firewall:** P11 FROZEN; R14 unverändert; kein globaler `rho`-Descent, keine Polar-Gauge-, Terminal-Transport-, Objekt-X- oder RH-Aussage.

---

## 1. Ziel

Round 27 identifizierte als günstigste noch offene Raw-Pattern-Front die **Next-Shell-Horizon-Lücke**: beide ersten neuen Supportvariablen sind bereits sichtbar, aber die beiden natürlichen Round-24-Hilfsquellen der nächsten Schale sind noch nicht horizon-legal.

Der erste Round-28-Angriff behandelt die zentrale, `J`-symmetrische Doppelhorizont-Zelle, in der **beide** Hilfsquellen `V_-` und `V_+` fehlen.

Das Ergebnis ist ein neuer endlicher Rohoperator-Kandidat:

\[
\boxed{M_{68}\in\operatorname{Mat}_{68\times68}}
\]

mit exakter `J`-Blockstruktur und rigoros von null getrennter Determinante.

Vor unabhängigem Review:

\[
\boxed{\mathrm{R28\!-\!A}:?[O].}
\]

---

## 2. Konstanten

Wie in Round 27 setzen wir

\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\delta=\eta+\chi,
\]

\[
\kappa=e-\delta=2\eta+\chi,
\qquad
E:=\varepsilon_{\max}=\frac12\log\frac54,
\qquad
\rho=E-\delta.
\]

Die Involution ist

\[
J(s,m,n)=(-s,m,n+s),
\qquad x\mapsto\delta-x.
\]

---

## 3. Exakte zentrale Doppelhorizont-Box

Definiere die offene Box `B28` durch

\[
\boxed{\frac{19}{2000}<R<\frac{21}{2000},}
\]

\[
\boxed{\left|x-\frac\delta2\right|<\frac1{5000},}
\]

\[
\boxed{\frac{119}{2000}<\sigma<\frac{121}{2000},}
\]

\[
\boxed{\frac{139}{2000}<\varepsilon<\frac{141}{2000}.}
\]

Diese Box ist unter `x -> delta-x` invariant.

Der retained verifier beweist mit gerichteten rationalen Logarithmusschranken auf der gesamten Box strikt

\[
0<R<\rho,\qquad R<x,\qquad R<\sigma<\varepsilon<E.
\]

### 3.1 Beide ersten Supportvariablen sind live

Mit

\[
U_-=(-1,5,1),\qquad U_+=(1,5,0)
\]

gilt auf ganz `B28`

\[
\boxed{\sigma+x>\kappa,}
\qquad
\boxed{\sigma-x>\eta.}
\]

Damit sind beide neuen Supportspalten live.

### 3.2 Beide natürlichen Next-Shell-Quellen sind noch über dem Horizont

Die Round-24-Hilfsquellen sind

\[
V_-=(-1,4,4),\qquad V_+=(1,4,3).
\]

Ihre Horizon-Legalität wäre äquivalent zu

\[
2\delta-x<\varepsilon
\]

bzw.

\[
x+\delta<\varepsilon.
\]

Auf `B28` gilt jedoch exakt die Gegenorientierung

\[
\boxed{\varepsilon+x<2\delta,}
\qquad
\boxed{\varepsilon-x<\delta.}
\]

Somit sind **beide** `V`-Zeilen auf der gesamten Box horizon-illegal.

### 3.3 Die Box ist tatsächlich neu gegenüber den promovierten lokalen Kammern

- `C42` verlangt auf der entsprechenden Supportseite `sigma+x<kappa` bzw. `sigma-x<eta`; `B28` erfüllt beide Gegenrichtungen.
- `C44` verlangt die Horizon-Legalität beider `V`-Quellen; `B28` erfüllt beide Gegenrichtungen.
- Für `C26^-` und `C26^+` folgt `sigma<2 eta`; auf `B28` gilt strikt
  \[
  \boxed{\sigma>2\eta.}
  \]
- `W43^<` verlangt `sigma+x<kappa`; `W43^>` verlangt `sigma-x<eta`.

Damit liegt `B28` nicht in einer der bereits promovierten C42-, C44-, C26- oder W43-Kammern.

---

## 4. Ausgangsdefekt: 42×44

Am Referenzpunkt

\[
(R,x,\sigma,\varepsilon)
=
\left(0.010,\frac\delta2,0.060,0.070\right)
\]

und wegen des vollständigen Box-Pattern-Zertifikats damit auf ganz `B28` erzeugen die 42 alten C42-Quellen exakt

\[
\boxed{42\text{ Zeilen und }44\text{ sichtbare Variablen}.}
\]

Die beiden zusätzlichen Variablen sind genau

\[
U_-,\qquad U_+.
\]

Die natürlichen zwei Zusatzzeilen `V_-`, `V_+` sind hier nicht verfügbar. Der alte Support-Shell-Mechanismus ist daher tatsächlich blockiert.

---

## 5. Der 68-Quellen-Kreis

Zu den 42 alten Quellen werden folgende 26 Quellen hinzugefügt:

```text
(-1,-1,3), (-1,0,3), (-1,0,4), (-1,1,-1), (-1,1,4),
(-1,2,-2), (-1,2,-1), (-1,2,5), (-1,3,-1), (-1,3,5),
(-1,3,6), (-1,4,-1), (-1,5,0),
( 1,-1,2), ( 1,0,2), ( 1,0,3), ( 1,1,-2), ( 1,1,3),
( 1,2,-3), ( 1,2,-2), ( 1,2,4), ( 1,3,-2), ( 1,3,4),
( 1,3,5), ( 1,4,-2), ( 1,5,-1).
```

Die 68 Quellen sind exakt unter `J` abgeschlossen: 34 `J`-Paare.

Für ihr gemeinsames Rohsystem gilt auf `B28`:

\[
\boxed{68\text{ horizon-legale Zeilen},}
\]

\[
\boxed{68\text{ sichtbare Variablen}.}
\]

Damit entsteht der quadratische Block

\[
\boxed{M_{68}.}
\]

Auch die 68 Variablen sind unter `J` abgeschlossen und bilden 34 Paare. Insbesondere gehören `h(x)` und `h(delta-x)` zum Variablensatz.

**Scope-Hinweis:** Die Zahl 68 ist die Größe dieses retained Zertifikats. Es wird keine Minimalität und keine kanonische Bedeutung der Suchbox bzw. der bei der Entdeckung verwendeten Gittertiefe behauptet.

---

## 6. Exaktes Raw-Pattern-Zertifikat auf der ganzen Box

Für jede der 68 Quellen werden aus dem kanonischen Rohoperator sämtliche folgenden Ereignisse erzeugt:

1. Source lower / Source upper;
2. Vorzeichen jedes der sechs Shift-Slots;
3. für live Slots untere und obere Supportgrenze;
4. für tote Slots die jeweils aktive untere oder obere Trennbedingung.

Insgesamt entstehen

\[
\boxed{1204}
\]

strikte affine Rohbedingungen.

Der retained verifier setzt **keine Stichprobe** an die Stelle des Beweises. Er wertet jede affine Bedingung über der gesamten rationalen Box mit gerichteten `Fraction`-Intervallen für `log 2`, `log 3`, `log 5` aus.

Ergebnis:

```text
R28_BOX_PATTERN_CERTIFICATE = PASS 1204 raw inequalities
```

Die kleinste zertifizierte positive Rohmarge ist größer als

\[
\boxed{0.00157927617278058}.
\]

Damit ist der rekonstruierte 68×68-Koeffizientenblock auf ganz `B28` konstant.

---

## 7. Exakte J-Blockstruktur

In der natürlichen Ordnung aus 34 negativen Quellen/Variablen und deren `J`-Bildern gilt exakt

\[
\boxed{
M_{68}
=
\begin{pmatrix}
A_{34}&B_{34}\\
B_{34}&A_{34}
\end{pmatrix}.}
\]

Mit

\[
Q=
\begin{pmatrix}
I&I\\ I&-I
\end{pmatrix}
\]

prüft der Verifier exakt

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

## 8. Exakte Determinantenfaktoren

Setze wie zuvor

\[
\beta:=\frac qp=2^{-3/4},
\qquad
v:=\left(\frac rp\right)^2
=\frac{\log3}{\log2}\sqrt{\frac8{27}}.
\]

Der Verifier berechnet symbolisch

\[
\det(A_{34}+B_{34})
=-p^{12}qr^8 F_+(p,q,r),
\]

\[
\det(A_{34}-B_{34})
= p^{12}qr^8 F_-(p,q,r),
\]

wobei `F_+` und `F_-` homogen vom Grad 13 sind und exakt

\[
F_-(p,q,r)=F_+(p,-q,r)
\]

gilt.

Nach Normierung

\[
F_+(p,q,r)=p^{13}G_+(\beta,v),
\qquad
F_-(p,q,r)=p^{13}G_-(\beta,v),
\]

mit

\[
G_-(\beta,v)=G_+(-\beta,v).
\]

Ein exakter Ausdruck für `G_+` ist

\[
\begin{aligned}
G_+={}&16\beta^{11}-9\beta^{10}-\beta^9v^2-32\beta^9-12\beta^8v+45\beta^8\\
&+\beta^7v^3-16\beta^7v^2+48\beta^7v-32\beta^7
+\beta^6v^3-13\beta^6v^2+66\beta^6v-90\beta^6\\
&-8\beta^5v^3+59\beta^5v^2-144\beta^5v+128\beta^5
-7\beta^4v^3+54\beta^4v^2-126\beta^4v+90\beta^4\\
&+11\beta^3v^3-66\beta^3v^2+144\beta^3v-112\beta^3
-2\beta^2v^4+23\beta^2v^3-78\beta^2v^2+102\beta^2v-45\beta^2\\
&-4\beta v^3+24\beta v^2-48\beta v+32\beta
+4v^4-20v^3+37v^2-30v+9.
\end{aligned}
\]

Mit gerichteten rationalen Schranken für `beta` und `v` erhält der Verifier

\[
\boxed{
0.3822065426030501
< G_+(\beta,v)
<0.38220654260305015,
}
\]

und

\[
\boxed{
0.20288790549604774
< G_-(\beta,v)
<0.20288790549604777.
}
\]

Insbesondere sind beide Faktoren strikt positiv.

Daher

\[
\boxed{
\det M_{68}
=-p^{68}\beta^2v^8G_+(\beta,v)G_-(\beta,v)\ne0.}
\]

---

## 9. Lokale Konsequenz

Für jeden Parameterpunkt in `B28` ist der Rohblock derselbe invertierbare 68×68-Block. Daher verschwinden alle 68 Sichtbarkeitsvariablen des Blocks. Insbesondere

\[
\boxed{h(x)=h(\delta-x)=0}
\]

auf dieser lokalen Doppelhorizont-Kammer.

Das ist eine echte neue lokale Faserabdeckung innerhalb der von Round 27 identifizierten Next-Shell-Horizon-Front.

Vor unabhängiger Prüfung bleibt der Status

\[
\boxed{\mathrm{R28\!-\!A}:?[O].}
\]

---

## 10. Was ausdrücklich nicht behauptet wird

Round 28-A beweist **nicht**:

- die gesamte Next-Shell-Horizon-Lücke;
- die Zellen, in denen genau eine der Quellen `V_-`, `V_+` horizon-legal ist;
- den tiefen Horizon-Rest außerhalb dieser Box;
- den Outer-Core-Rest;
- globale Kerneltrivialität für `0<R<rho`, `sigma>R`;
- einen neuen globalen Radius-Schwellenwert;
- Minimalität oder kanonische Bedeutung des 68er-Blocks;
- Polar Gauge, Strong/Terminal Transport, Objekt X oder RH.

Der globale `rho`-Descent bleibt `?[O]`.
P11 bleibt FROZEN. Die R14-Firewall bleibt unverändert.
