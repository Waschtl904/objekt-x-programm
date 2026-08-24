# P12 Runde 29 — ε-Brücke durch beide Next-Shell-Horizonwände

**Status:** Kandidat; **nicht promotet**.  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main@b8aa0f3242d9f69bbcdf5ac5d036138634ae5929`.  
**Input:** Round 28 / A15.1b2m, zentrale `M68`-Doppelhorizont-Box `✓[M]_part`; Round-24 `C44` `✓[M]_part`.  
**Methode:** Rückwärts denken + Invarianten suchen.  
**Firewall:** P11 FROZEN; R14 unverändert; kein globaler `rho`-Descent, keine vollständige Schließung der Next-Shell-Horizon-Lücke, keine Polar-Gauge-, Terminal-Transport-, Objekt-X- oder RH-Aussage.

---

## 1. Ausgangsfrage

Round 28 schließt eine zentrale `J`-symmetrische Zelle, in der beide ersten neuen Supportvariablen

\[
U_-=(-1,5,1),\qquad U_+=(1,5,0)
\]

sichtbar sind, während beide natürlichen Next-Shell-Hilfsquellen

\[
V_-=(-1,4,4),\qquad V_+=(1,4,3)
\]

noch horizon-illegal sind.

Round 24 schließt dagegen die `C44`-Seite, auf der beide `V`-Quellen horizon-legal sind.

Die zunächst offen wirkenden Zwischenfronten sind daher die beiden Zellen, in denen genau eine der Quellen `V_-`, `V_+` legal ist.

Round 29 fragt rückwärts:

> Muss beim Umschalten der Horizon-Legalität von `V_-` oder `V_+` der bereits promovierte `M68`-Block überhaupt wechseln?

Die Antwort des Rohoperators ist: **nein**.

---

## 2. Die gefundene Invariante

Sei `S68` exakt die in Round 28 promovierte Menge aus 68 Quellen.

Entscheidend sind zwei Tatsachen:

1. `V_-` und `V_+` gehören **nicht** zu `S68`.
2. Für eine fest gewählte Quelle aus `S68` hängt die Supportsichtbarkeit ihrer sechs Shift-Slots nur von `(R,x,sigma)` ab. `epsilon` tritt dort nicht auf. Die einzige `epsilon`-Abhängigkeit des ausgewählten Rohzertifikats liegt in den Source-upper-Bedingungen
   \[
   T+\varepsilon-u_s>0.
   \]
   Jede davon ist in `epsilon` strikt monoton steigend.

Daraus folgt die zentrale Round-29-Invariante:

\[
\boxed{
\text{Sobald alle 68 ausgewählten Quellen legal sind, kann }\varepsilon
\text{ nach oben wachsen, ohne das }M_{68}\text{-Pattern zu ändern,}
}
\]

solange `(R,x,sigma)` im gleichen Rohpattern-Bereich bleibt und die arithmetische Decke nicht überschritten wird.

Insbesondere sind die beiden Hyperflächen

\[
H_-:\ \varepsilon+x=2\delta,
\qquad
H_+:\ \varepsilon-x=\delta
\]

**keine Rohfacetten des ausgewählten M68-Zertifikats**.

Sie sind Horizonwände der nicht ausgewählten Quellen `V_-`, `V_+`, nicht des retained 68er-Blocks.

---

## 3. Exakte ε-Brücke B29

Setze wie bisher

\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\kappa=e-\delta,\qquad
E=\varepsilon_{\max},\qquad
\rho=E-\delta.
\]

Schreibe

\[
x=\frac\delta2+y.
\]

Definiere die offene Box

\[
\boxed{
\frac{19}{2000}<R<\frac{21}{2000},
}
\]

\[
\boxed{
|y|<\frac1{5000},
}
\]

\[
\boxed{
\frac{119}{2000}<\sigma<\frac{121}{2000},
}
\]

\[
\boxed{
\frac{139}{2000}<\varepsilon<\frac{11}{100}.
}
\]

Diese Box heiße `B29`.

Sie ist unter

\[
J:\ y\mapsto-y
\]

invariant und vollständig im residual-overlap-Ambientbereich:

\[
0<R<\rho,\qquad R<x,\qquad R<\sigma<\varepsilon<E.
\]

Außerdem bleiben auf ganz `B29` beide ersten Supportvariablen live:

\[
\sigma+x>\kappa,
\qquad
\sigma-x>\eta,
\]

und

\[
\sigma>2\eta.
\]

---

## 4. B29 enthält alle vier Horizonorientierungen

Die beiden Horizonfunktionen seien

\[
\Phi_-:=\varepsilon+x-2\delta,
\qquad
\Phi_+:=\varepsilon-x-\delta.
\]

`V_-` ist legal genau für `Phi_->0`, `V_+` genau für `Phi_+>0`.

### 4.1 Unterer Slice = Round-28-Seite

Für

\[
\frac{139}{2000}<\varepsilon<\frac{141}{2000}
\]

sind auf der gesamten Basiskiste beide Werte strikt negativ:

\[
\Phi_-<0,\qquad \Phi_+<0.
\]

Dies ist genau der in Round 28 verwendete ε-Slice von `B28`.

### 4.2 Offene Minus-only-Zelle

Für

\[
\frac1{10000}<y<\frac1{5000},
\qquad
\frac{883}{10000}<\varepsilon<\frac{221}{2500}
\]

gilt strikt

\[
\Phi_->0,
\qquad
\Phi_+<0.
\]

Also ist `V_-` legal, `V_+` illegal.

### 4.3 Exakter J-Spiegel

Für

\[
-\frac1{5000}<y<-\frac1{10000}
\]

und dasselbe ε-Intervall gilt

\[
\Phi_-<0,
\qquad
\Phi_+>0.
\]

Also ist `V_+` legal, `V_-` illegal.

Damit durchquert `B29` beide bislang fehlenden Einzel-`V`-Orientierungen offen.

### 4.4 Oberer Slice liegt in C44

Der gesamte Slab

\[
\frac{181}{2000}<\varepsilon<\frac1{10}
\]

innerhalb derselben `(R,y,sigma)`-Basiskiste erfüllt die vollständigen C44-Ungleichungen:

\[
R<x<\delta-R,
\qquad
\chi-R<x<\eta+R,
\]

\[
\max\{\kappa-x,x+\eta\}<\sigma
<\min\{2\delta-x,x+\delta\},
\]

\[
\max\{2\delta-x,x+\delta\}<\varepsilon<E.
\]

Damit besitzt `B29` einen offenen Überlapp mit der bereits promovierten C44-Kammer.

---

## 5. Exakte Rohpattern-Stabilität

Der Round-29-Verifier rekonstruiert dieselbe 68-Quellen-Menge wie Round 28 und erzeugt erneut sämtliche Source-/Sign-/Support-/Horizon-Bedingungen.

Es entstehen exakt

\[
\boxed{1204}
\]

strikte affine Rohbedingungen.

Davon hängen exakt 68 von `epsilon` ab — nämlich genau die 68 Source-upper-Ungleichungen. Bei jeder ist der `epsilon`-Koeffizient exakt `+1`.

Alle anderen 1136 Rohbedingungen sind `epsilon`-frei.

Der Verifier bestätigt zusätzlich symbolisch, dass weder

\[
\varepsilon+x-2\delta
\]

noch

\[
\varepsilon-x-\delta
\]

unter den 1204 Rohwänden des ausgewählten Zertifikats vorkommt.

Mit gerichteten rationalen Intervallen für `log 2`, `log 3`, `log 5` bleiben alle 1204 Bedingungen über der **gesamten** Box `B29` strikt positiv.

Die kleinste zertifizierte Rohmarge bleibt

\[
>0.00157927617278058.
\]

Damit ist der Koeffizientenblock auf ganz `B29` coefficient-for-coefficient konstant.

---

## 6. Keine neue Determinantenrechnung nötig

Am unteren Referenzpunkt

\[
(R,x,\sigma,\varepsilon)
=
\left(0.010,\frac\delta2,0.060,0.070\right)
\]

rekonstruiert der Verifier exakt die in Round 28 promovierte Quellen- und Variablenordnung und damit denselben

\[
M_{68}\in\operatorname{Mat}_{68\times68}.
\]

Round 28 hat unabhängig GREEN und formal promoviert:

\[
\det M_{68}\ne0.
\]

Da der Round-29-Verifier auf ganz `B29` exakt dasselbe Raw-Pattern zertifiziert, ist keine neue Gewichtspolynomrechnung erforderlich.

Zusätzlich werden repräsentative Punkte aus allen vier Horizonorientierungen rekonstruiert:

- beide `V` illegal;
- nur `V_-` legal;
- nur `V_+` legal;
- beide `V` legal.

An allen vier Punkten gilt exakt dieselbe symbolische Matrix `M68`.

---

## 7. Kandidatensatz R29-A

Für jeden Punkt

\[
(R,x,\sigma,\varepsilon)\in B_{29}
\]

rekonstruiert der kanonische Rohoperator coefficient-for-coefficient den promovierten invertierbaren Round-28-Block `M68`.

Daher verschwinden alle 68 zugehörigen Sichtbarkeitsvariablen, insbesondere

\[
\boxed{h(x)=h(\delta-x)=0.}
\]

Ferner ist `B29` eine offene konvexe Faserbox, deren unterer Slice in `B28` liegt und deren oberer Slice offen in `C44` liegt. Sie durchquert beide Einzel-`V`-Horizonorientierungen.

Somit ist `B29` ein lokaler **ε-Korridor**

\[
\boxed{
B28\longrightarrow
\text{single-}V_-\ /\ \text{single-}V_+
\longrightarrow C44
}
\]

mit unverändertem invertierbarem `M68`-Zertifikat.

Vor unabhängigem Review bleibt

\[
\boxed{\mathrm{R29\!-\!A}:?[O].}
\]

---

## 8. Scope-Firewall

Round 29-A behauptet **nicht**:

- vollständige Schließung aller Einzel-`V`-Zellen für beliebige `(R,x,sigma)`;
- vollständige Schließung der gesamten Next-Shell-Horizon-Front;
- Schließung des tiefen Horizon-Rests;
- Schließung des Outer-Core-Rests;
- globale Kerneltrivialität für `0<R<rho`, `sigma>R`;
- einen neuen globalen Radius-Schwellenwert;
- Minimalität oder kanonische Bedeutung des 68er-Blocks;
- Polar Gauge, Strong/Terminal Transport, Objekt X oder RH.

Der globale `rho`-Descent bleibt `?[O]`.

P11 bleibt FROZEN. Die R14-Firewall bleibt unverändert.
