# P11/R32 — Klassifikation des inneren Unsichtbarkeitsraums als Branch-/Gluing-Graph

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** CTX-1, NS-1, SS-1a/SS-L, SP-1, ST-1.  
**Ziel:** nicht eine weitere Schale zu erraten, sondern eine exakte, exhaustive Normalform fuer
\[
\mathcal N_I:=\ker(E_I^*H|_{\mathscr H^+})
\]
zu formulieren. Die Normalform trennt (i) automatisch unsichtbare physische Supportbereiche von (ii) den innerhalb des gesampelten Bereichs durch Branch-Gluing und eine einzige gewichtete Hubrelation bestimmten Loesungen.

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c=\tfrac12\log5,
\qquad
T_0=T+\varepsilon,
\]
mit
\[
a=\tfrac12\log2,
\qquad
b=\tfrac12\log3,
\qquad
T=2a,
\]
setze
\[
d=b-a,
\qquad
e=T-b,
\qquad\delta=d-e.
\]
Wir betrachten
\[
0<R<a.
\]
Fuer gerade `y in L^2(-T0,T0)^+` gilt fuer `0<u<R`
\[
(E_I^*Hy)(u)
=p[y(a-u)-y(a+u)]
+r[y(b-u)-y(b+u)]
+q[y(T-u)-y(T+u)],
\tag{FG.1}
\]
wobei Werte ausserhalb `(-T0,T0)` als Null verstanden werden.

## 2. Der exakt gesampelte physische Bereich

Auf der positiven Achse koennen in (FG.1) nur Punkte in den drei Radius-R-Fenstern um `a,b,T` auftreten. Definiere
\[
\boxed{
\mathcal U_R
:=
\bigcup_{\tau\in\{a,b,T\}}
(\tau-R,\tau+R)\cap(0,T_0).
}
\tag{FG.2}
\]
und den positiven blinden Bereich
\[
\boxed{
\mathcal Z_R^{\rm phys}:=(0,T_0)\setminus\mathcal U_R.
}
\tag{FG.3}
\]
Sei
\[
\mathcal Z_R^+
:=\{y\in L^2(-T_0,T_0)^+:
\operatorname{ess\,supp}(y|_{(0,T_0)})\subset\mathcal Z_R^{\rm phys}\}.
\]
Dann gilt unmittelbar
\[
\boxed{\mathcal Z_R^+\subset\mathcal N_I.}
\tag{FG.4}
\]
Denn kein in (FG.1) ausgewerteter Punkt trifft den Support von `y`.

### Spezialfall `R>=d/2`

Da
\[
2R\ge d>e,
\]
ueberlappen sowohl das `a/b`- als auch das `b/T`-Samplingfenster. Daher ist `U_R` zusammenhaengend und exakt
\[
\boxed{
\mathcal U_R=(a-R,\ T+\min\{R,\varepsilon\}).
}
\tag{FG.5}
\]
Somit
\[
\boxed{
\mathcal Z_R^{\rm phys}
=(0,a-R)
\cup
(T+\min\{R,\varepsilon\},T_0).
}
\tag{FG.6}
\]
Bis auf Endpunkte.

Der erste Summand ist genau der bereits benutzte zentrale blinde Bereich. Falls
\[
R<\varepsilon,
\]
entsteht ausserdem der nichtleere Horizontschwanz
\[
\boxed{
\mathcal T_R:=(T+R,T_0)=(T+R,T+\varepsilon).
}
\tag{FG.7}
\]
Jede gerade `L2`-Funktion mit positivem Support in `T_R` liegt automatisch in `N_I`. Insbesondere ist dieser Teil unendlichdimensional.

Falls `R>=epsilon`, ist der Horizontschwanz leer.

## 3. Sechs Branch-Koordinaten

Definiere fuer `0<u<R` die sechs Pullback-Branches
\[
A_-(u):=y(a-u),
\qquad
A_+(u):=y(a+u),
\]
\[
B_-(u):=y(b-u),
\qquad
B_+(u):=1_{\{u<e+\varepsilon\}}y(b+u),
\]
\[
C_-(u):=y(T-u),
\qquad
C_+(u):=1_{\{u<\varepsilon\}}y(T+u).
\tag{FG.8}
\]
Die Indikatoren sind exakt die Source-Horizon-Cuts:
\[
T_0-b=e+\varepsilon,
\qquad
T_0-T=\varepsilon.
\]
Da `R<a`, sind `A_-,A_+,B_-,C_-` im ganzen Intervall `(0,R)` definiert; nur `B_+` und `C_+` koennen am Horizont abgeschnitten werden.

Die Unsichtbarkeitsbedingung lautet nun exakt
\[
\boxed{
p(A_--A_+)+r(B_--B_+)+q(C_--C_+)=0
\quad\text{a.e. auf }(0,R).
}
\tag{FG.9}
\]

## 4. Gluing-Bedingungen

Die sechs Branches sind nicht unabhaengig: verschiedene Branch-Koordinaten koennen denselben physischen Punkt darstellen.

Fuer einen Branch `i=(tau,sigma)` mit `sigma in {-1,+1}` schreibe
\[
\pi_i(u):=\tau+\sigma u.
\]
Wann immer
\[
\pi_i(u)=\pi_j(v)
\]
und beide Seiten innerhalb ihrer Branch-Domains liegen, muss gelten
\[
\boxed{F_i(u)=F_j(v).}
\tag{FG.10}
\]
Umgekehrt sind dies die einzigen Kompatibilitaetsbedingungen: Erfuellt eine Familie von sechs Branch-Profilen alle solchen Gluing-Identitaeten, so definiert sie eindeutig eine `L2`-Funktion auf dem gesampelten physischen Bereich `U_R`, indem man am physischen Punkt `t=pi_i(u)` den Wert `F_i(u)` setzt. (FG.10) macht diese Definition a.e. unabhaengig von der Branch-Wahl.

Bezeichne den abgeschlossenen Gluing-Unterraum der sechs Branch-Raeume mit
\[
\mathfrak G_R.
\]
Und definiere den gewichteten Row-Operator
\[
\Lambda_R(F)
:=p(A_--A_+)+r(B_--B_+)+q(C_--C_+).
\tag{FG.11}
\]

## 5. Theorem FG-1 — exhaustive Branch-/Gluing-Normalform

Jedes `y in N_I` zerfaellt eindeutig orthogonal nach physischem Support als
\[
\boxed{y=y_{\rm blind}+y_{\rm samp},}
\tag{FG.12}
\]
mit
\[
y_{\rm blind}\in\mathcal Z_R^+
\]
und `y_samp` getragen in der geraden Fortsetzung von `U_R`.

Der gesampelte Anteil entspricht ueber seine sechs Branch-Pullbacks exakt einer Familie
\[
F\in\mathfrak G_R
\]
mit
\[
\boxed{\Lambda_R F=0.}
\tag{FG.13}
\]
Umgekehrt erzeugt jede solche gegluete Familie zusammen mit einem beliebigen `y_blind in Z_R^+` ein Element von `N_I`.

Damit ist `N_I` exhaustiv beschrieben als
\[
\boxed{
\mathcal N_I
\cong
\mathcal Z_R^+
\oplus
\{F\in\mathfrak G_R:\Lambda_R F=0\}.
}
\tag{FG.14}
\]
Hier bedeutet `cong` die kanonische Branch-Rekonstruktion; es wird keine naive isometrische Identifikation mit dem ungegewichteten sechsfachen Direktprodukt behauptet, weil physische Ueberlappungen dort mehrfach gezaehlt wuerden.

Diese Normalform ist ein echter Klassifikationsrahmen: exotische Loesungen koennen nicht ausserhalb von (FG.14) liegen. Offen bleibt aber die weitere Zerlegung des geglueten Kernes in einfachere Orbit-/Profiltypen.

## 6. Die affine Overlap-Pseudogruppe

Drei besonders wichtige Gluing-Abbildungen zwischen `u`-Koordinaten sind
\[
\boxed{s_d(u)=d-u,}
\tag{FG.15}
\]
aus `a+u=b-v`,
\[
\boxed{s_e(u)=e-u,}
\tag{FG.16}
\]
aus `b+u=T-v`, und
\[
\boxed{s_a(u)=a-u,}
\tag{FG.17}
\]
aus `a+u=T-v`.

Sie gelten jeweils nur auf den Teilintervallen, auf denen beide betreffenden Branches aktiv sind. Algebraisch erzeugen sie aber die Translationen
\[
\boxed{s_d\circ s_e(u)=u+\delta,}
\tag{FG.18}
\]
\[
\boxed{s_a\circ s_d(u)=u+e,}
\tag{FG.19}
\]
\[
\boxed{s_a\circ s_e(u)=u+d.}
\tag{FG.20}
\]
Damit enthaelt die unbeschraenkte affine Gruppe der Overlap-Regeln die Translationen um `d` und `e`.

## 7. Arithmetische Firewall: `d/e` ist irrational

Es gilt
\[
d=\tfrac12\log(3/2),
\qquad
e=\tfrac12\log(4/3).
\]
Angenommen `d/e=m/n in Q_{>0}` mit positiven ganzen `m,n`. Dann
\[
n\log(3/2)=m\log(4/3),
\]
also
\[
(3/2)^n=(4/3)^m.
\]
Damit
\[
3^{n+m}=2^{n+2m},
\]
was durch eindeutige Primfaktorzerlegung unmoeglich ist. Also
\[
\boxed{d/e\notin\mathbb Q.}
\tag{FG.21}
\]
Insbesondere ist die von `d,e` erzeugte additive Translationsgruppe nicht zyklisch/discret durch eine gemeinsame Grundlaenge erzeugt; die unbeschraenkte affine Overlap-Gruppe ist unendlich und aperiodisch.

### Exakte Reichweite dieses No-Go

Dies widerlegt die Schlussregel

> `nur drei Hub-Shifts`  =>  `automatisch endlich viele periodische Orbittypen`.

Es beweist **nicht**, dass fuer jedes feste `R` jeder tatsaechliche, domain-beschraenkte Orbit unendlich ist. Die Branch-Domains koennen Iterationen an den Raendern abbrechen. Ebenso beweist (FG.21) noch nicht, dass es zwingend unendlich viele irreduzible Schalentypen in `N_I` gibt.

Der richtige naechste Gegenstand ist daher die **domain-beschraenkte Overlap-Pseudogruppe** auf `(0,R)`, nicht eine ungepruefte endliche Schalenliste.

## 8. Konsequenzen fuer CTX/NS/ST

- `C_R^+` ist ein Teil des automatisch blinden Summanden `Z_R^+`.
- Der Horizontschwanz (FG.7) ist ein weiterer automatisch blinder Summand, falls `R<epsilon`.
- NS-1 und ST-1 sind nichttriviale Loesungstypen innerhalb des gesampelten Gluing-Kernes `ker Lambda_R cap G_R`.
- Dass CTX/NS/ST drei geschlossene Transversalitaetsmechanismen liefern, impliziert daher noch keine Vollstaendigkeit dieser drei Typen.

## 9. Firewall und Kandidatenstatus

Dieser Audit beweist als Kandidat nur die Struktur von `N_I`; keinerlei neuer Schur-Transversalitaetssatz wird behauptet.

Nicht bewiesen:

- dass `C_R^+`, erste Schale, zweite Schale und Horizontschwanz ganz `N_I` erzeugen;
- dass der domain-beschraenkte Overlap-Graph nur endlich viele Orbittypen besitzt;
- Transversalitaet des Horizontschwanzes;
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Kandidatenstatus bis unabhhaengigem Review:

- **FG-0:** `?[O]` — exakter automatisch blinder Supportraum `Z_R^+`; fuer `R>=d/2` Formel (FG.6).
- **HT-1:** `?[O]` — falls `R<epsilon`, ist der Horizontschwanz `(T+R,T0)` ein unendlichdimensionaler Unterraum von `N_I`.
- **FG-1:** `?[O]` — exhaustive Branch-/Gluing-Normalform (FG.14).
- **FG-NG1:** `?[O]` — No-Go gegen die Schlussregel `endlich viele Hub-Shifts => endliche periodische Overlap-Gruppe`; arithmetischer Kern `d/e irrational`.

Bei vollstaendigem GREEN waere zulaessig:

- **FG-0:** `✓[M]`;
- **HT-1:** `✓[M]`;
- **FG-1:** `✓[M]`;
- **FG-NG1:** `✓[M]_neg` fuer genau die oben formulierte Schlussregel, nicht fuer die staerkere Aussage `es gibt unendlich viele Schalentypen`.

Keine Promotion ohne explizite Freigabe.
