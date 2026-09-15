# P11 / R43 — Quellenabstieg nach C6 und exakte Weil-Trennung

Datum: 2026-09-08. Exakte Definitionsbasis:
`fb49221b50174615d37ffe763b6aa3cdd87b91d6` (Merge von PR90).

**Status:** neue analytische Ableitung mit ausgeschriebenen Beweisen und
Autorengegencheck. Unabhängiger Exact-Head-Review offen. Keine Registry-Promotion.
Der bereits geprüfte ungerade fixed-pair-C6-Satz wird als benannter Eingang
verwendet, nicht erneut geöffnet. Keine Radienuniformität, kein RH-Beweis.

## 0. Auftrag und Ergebnisgrenzen

Die aktuelle Objekt-X-Arbeitsdefinition verlangt eine intrinsische gemeinsame
Geometrie und die vollständige exakte Weil-Gram-Identität auf einer geeigneten
Testklasse. Weder radienuniformer Strong Terminal noch eine Fredholm-Determinante
ist dort als notwendiges Axiom jeder möglichen Realisierung festgelegt.
Die entsprechenden P11-Architekturfragen bleiben getrennte Aufgaben.

Hier wird eine konkrete post-C6-Verbindung untersucht:

1. Der tatsächliche tangentiale Grenztransport wird explizit durch die
   eingeschränkten Gamma-Wurzeln ausgedrückt.
2. Eine Familie begrenzter invertierbarer Quellenabbildungen erfüllt die zuvor
   nur formulierte Gleichung `T_S J = W_infinity T_R` auf einer kofinalen
   Radienfamilie. Sie erhält sogar den rohen Jet nach diesem Quellenwechsel.
3. Ihre erzeugte Gramform wird exakt berechnet. Ein explizites Paar glatter
   ungerader Quellen in `ker beta`, sogar mit verschwindenden Polmomenten,
   liefert einen von null verschiedenen Weil-Defekt `-log(2)/sqrt(2)`.

Das letzte Ergebnis schließt nur eine Realisierungsroute aus: **Den Gamma-Gram
auf dem gesamten Nulljetraum unverändert lassen und nur die Normalrichtung
anpassen reicht auf der P02-Amplitudenklasse nicht.** Es ist kein No-Go gegen
jede Quellenabbildung in den terminalen Hilbertraum und kein negatives
Diagonalergebnis für die Weil-Form. C6 bleibt unberührt.

## 1. Feste Eingänge und Räume

Wir arbeiten ausschließlich im ungeraden Sektor. Für R>0 seien
`H_R=K_(X,R)^-`, `beta_R=beta_R^(0)`, `nu_R` ihr Graph-Rieszvektor,
`rho_R=||nu_R||`, `epsilon_R=nu_R/rho_R`, und
`H_R^0=ker beta_R=epsilon_R^perp`. Das Skalarprodukt ist linear im ersten
Argument. J=J_(R,S) bezeichnet die tatsächliche Nullerweiterung.

Die Gamma-Form `c_Gamma,R` ist auf dem festen Graphraum beschränkt und koerziv.
**Lambda_R** ist ihr Darstellungsoperator auf **H_R^0**:

```math
\langle\Lambda_Rh,k\rangle_{H_R}=\mathfrak c_{\Gamma,R}[h,k],
\qquad h,k\in H_R^0,\qquad c_RI\le\Lambda_R\le I.
\tag{SD1}
```

Lambda_R ist im Allgemeinen eine Kompression des Gamma-Formoperators.
Seine Wurzel darf nicht durch die Einschränkung der Wurzel auf ganz H_R
ersetzt werden. Alle hier verwendeten Lambda-Wurzeln wirken auf H_R^0.

Benannte Primärquellen-Eingänge:

- P11 (4.6)–(4.9): Pullback, endliche Isometrie und endlicher Kozykel.
- R42.40: `G_(R,U)^(-1/2) -> Lambda_R^(-1/2) P_R^0` stark, mit der
  festen positiven Quelluntergrenze.
- R42.51 und PA1–PA2: `W_(R,S)^[U] -> W_(R,S)^infinity` stark,
  tangentialer Grenzwert `W^0:H_R^0 -> H_S^0` und
  `W^infinity epsilon_R=epsilon_S`.
- DT.6: `beta_S J=beta_R`; Gamma-Kompatibilität unter Nullerweiterung.

Diese Eingänge und ihre jeweiligen Reviewgrenzen werden nicht durch die
neue Nachrechnung ersetzt. Der gerade C5e-Satz wird hier nicht benötigt.
Die Primärdefinitionen werden am oben genannten Commit verwendet.

## 2. Expliziter tangentialer Grenztransport

Bei jedem endlichen U gilt exakt

```math
G_{S,U}^{-1/2}W_{R,S}^{[U]}=J G_{R,U}^{-1/2}.
\tag{SD2}
```

Auf f in H_R^0 darf man den starken Grenzwert nehmen: Die inversen Wurzeln
sind durch c_S^(-1/2) gleichmäßig beschränkt; W^[U]f konvergiert stark.
R42.40 identifiziert die inverse Wurzelgrenze, und W^0f liegt in H_S^0.
Daher

```math
\Lambda_S^{-1/2}W_{R,S}^{0}f=J\Lambda_R^{-1/2}f.
```

Multiplikation mit der beschränkten Lambda_S^(1/2) ergibt

```math
\boxed{W_{R,S}^{0}=\Lambda_S^{1/2}J\Lambda_R^{-1/2}.}
\tag{SD3}
```

Dies ist eine ausdrückliche Vereinfachung des vorhandenen tangentialen
Satzes, kein neuer Annahmesatz und kein Grenzübergang durch wachsende positive
Wurzeln. Baseline-Radien T_0 kommen in SD3 nicht mehr vor.

Der starke Grenztransport ist eine Isometrie und erfüllt für jedes feste
Tripel R<S<Q den Kozykel: Beim Produktgrenzwert kontrolliert die Norm eins
des linken endlichen Faktors den beweglichen rechten Vektor. Damit existiert
der übliche Hilbert-Induktivlimes H_infinity mit isometrischen iota_R und
`iota_S W_(R,S)^infinity=iota_R`. Alle Radientripel bleiben fest; keine
zusätzliche radienuniforme Konvergenz wird dafür vorausgesetzt.

## 3. Kanonischer Gamma-Abstieg auf dem Nulljetraum

Sei D_0^- die Menge glatter kompakt getragener ungerader Funktionen auf R
mit beta(f)=0. Für h in H_R^0 definiere

```math
\mathcal I(h):=\iota_R\Lambda_R^{1/2}h.
\tag{SD4}
```

SD3 gibt `W^0 Lambda_R^(1/2)h=Lambda_S^(1/2)Jh`. Somit ist SD4
unabhängig von einem größeren Quellfenster. Ferner

```math
\boxed{\langle\mathcal I(h),\mathcal I(k)\rangle
       =\mathfrak c_\Gamma[h,k].}
\tag{SD5}
```

Die gemeinsame Normale `epsilon_infinity=iota_R epsilon_R` ist wohldefiniert
und orthogonal zum Bild von I. Das normierte globale Funktional ist
`beta_hat_infinity(x)=<x,epsilon_infinity>`.

### Optionale, aber hier bewiesene Identifikation des gesamten ungeraden Limes

Setze

```math
\mathscr G_\Gamma^-=
\left\{f\in L^2(\mathbb R)_{\rm odd}:
  \frac1{2\pi}\int m_\Gamma(\xi)|\widehat f(\xi)|^2d\xi<\infty\right\}.
```

**D_0^- ist dicht in diesem globalen Gamma-Raum.** Zunächst sind glatte
kompakt getragene ungerade Funktionen darin dicht: Glatte kompakte
Fourierapproximation liefert Schwartz-Approximation im gewichteten L2;
anschließende gerade Raumcutoffs approximieren Schwartz-Funktionen in H^1,
also auch in der Gamma-Norm, weil `m_Gamma(xi)<=C(1+xi^2)`.

Nun wähle eine feste glatte ungerade eta, nichtnegativ und nichtnull auf
(1,2), mit Träger in (-2,-1) vereinigt (1,2). Für L>=1 setze
`eta_L(x)=eta(x/L)`. Aus `I_0(r)=2(1-e^(-r/2))` folgt

```math
\beta(\eta_L)=2L\int_1^2 I_0(Ls)\eta(s)ds
             \sim 4L\int_1^2\eta(s)ds>0.
```

Das P11-Symbol ist `m_Gamma=1+g_infinity`, mit positiver monotoner Reihe
in |xi| (O3AF.2–O3AF.3). Deshalb `m_Gamma(zeta/L)<=m_Gamma(zeta)` und

```math
\|\eta_L\|_\Gamma^2
 =\frac L{2\pi}\int m_\Gamma(\zeta/L)|\widehat\eta(\zeta)|^2d\zeta
 \le L\|\eta\|_\Gamma^2.
```

Folglich besitzen `b_L=eta_L/beta(eta_L)` die Eigenschaften
`beta(b_L)=1` und `||b_L||_Gamma=O(L^(-1/2))`. Für jede feste glatte
kompakte ungerade Quelle f liegt `f-beta(f)b_L` in D_0^- und konvergiert
in Gamma-Norm gegen f. Das beweist die Dichtheit. Die globale beta ist damit
nicht als beschränktes Funktional auf G_Gamma^- vorausgesetzt.

Die Fortsetzung von I ist eine Isometrie von G_Gamma^- auf die abgeschlossene
tangentiale Grenzkomponente. Denn `Lambda_R^(1/2)` ist auf H_R^0 bijektiv;
daher werden alle lokalen Tangentialbilder erfasst. Zusammen mit der
Normalen erhält man die konkrete unitäre Darstellung

```math
\boxed{
\mathscr U:\mathscr G_\Gamma^-\oplus\mathbb C\longrightarrow H_\infty,
\qquad \mathscr U(h,z)=\mathcal I(h)+z\varepsilon_\infty.
}
\tag{SD6}
```

Das ist eine **Koordinatendarstellung mit expliziten lokalen Identifikationen**,
keine Behauptung, die ursprüngliche arithmetische Datenstruktur sei verschwunden
oder Objekt X müsse eine naive externe Gamma/Prime-Direktsumme sein.
Die lokale Umrechnung verwendet die ursprünglichen Graphnormen und Lambda_R.
Eine abstrakte Hilbertraumdarstellung allein entscheidet keine Weil-Identität.

## 4. Der Quellenvertrag ist konstruktiv lösbar

Wähle einmal R_0>0 und eine feste reelle
`phi in C_c^infinity((-R_0,R_0))_odd` mit `beta(phi)=1`.
Diese Referenzquelle ist eine **zusätzliche explizite Wahl**, keine aus C6
bewiesene kanonische Auswahl. Für R>=R_0 wird phi durch Nullerweiterung
identifiziert. Definiere auf H_R

```math
\boxed{
T_R^\phi f=\Lambda_R^{1/2}(f-\beta_R(f)\phi)
                     +\beta_R(f)\varepsilon_R.
}
\tag{SD7}
```

Der erste Summand ist wohldefiniert in H_R^0. Diese Abbildung ist für jedes
feste R beschränkt und invertierbar; für `v in H_R^0`, a in C ist

```math
(T_R^\phi)^{-1}(v+a\varepsilon_R)=\Lambda_R^{-1/2}v+a\phi.
```

Aus SD3, Jet-Pullback und Normalentransport folgt exakt

```math
\boxed{T_S^\phi J_{R,S}=W_{R,S}^{[\infty]}T_R^\phi.}
\tag{SD8}
```

Damit ist

```math
\mathcal T_\phi f=\iota_RT_R^\phi f
 =\mathcal I(f-\beta(f)\phi)+\beta(f)\varepsilon_\infty
 =\mathscr U(f-\beta(f)\phi,\beta(f))
\tag{SD9}
```

für alle kompakten ungeraden Quellen unabhängig von R hinreichend groß.
Es gilt sogar `beta_hat_infinity(T_phi f)=beta(f)`.
Das widerspricht nicht dem früheren Rohjet-No-Go: Dort war
`B_infinity iota_R=beta_R` ohne Änderung der lokalen Quellen gefordert.
Hier steht die **nichtidentische Umkodierung T_R^phi** dazwischen.
Keine Monotonie von rho_R wird benutzt.

Die tatsächlich erzeugte positive Gramform ist

```math
\boxed{
Q_\phi(f,g)=\mathfrak c_\Gamma[f-\beta(f)\phi,g-\beta(g)\phi]
                         +\beta(f)\overline{\beta(g)}.
}
\tag{SD10}
```

Dies löst die Quellenverträglichkeit, **nicht** die Weil-Identifikation.
Auf ker beta gilt ausnahmslos `Q_phi(f,g)=c_Gamma[f,g]`.

Für eine zweite Referenz psi mit beta(psi)=1 wird in SD6 nur der Scheroperator
`(h,z) -> (h+z(phi-psi),z)` eingefügt. Er ist beschränkt und invertierbar,
aber für phi!=psi nicht unitär: Der Einheitsvektor (0,1) erhält Normquadrat
`1+||phi-psi||_Gamma^2>1`. C6 legt somit nicht von selbst eine
referenzunabhängige Quellengramform dieses Typs fest.

## 5. Exakte P02/P11-Formen statt Namensgleichheit der Gamma-Beiträge

P02 verwendet `A_PW=C_c^infinity(R;C)`, Fourierzeichen `exp(i xi u)` und

```math
C_{a,b}(u)=\int a(u+t)\overline{b(t)}dt,
\quad g_{a,b}(u)=\tfrac12(C_{a,b}(u)+C_{a,b}(-u)),
\quad h_{a,b}=\widehat g_{a,b}.
```

Die vollständige Form lautet

```math
B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin},\qquad
B_{\rm pole}=h(i/2)+h(-i/2),\qquad
B_{\rm fin}=-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(\log n).
\tag{SD11}
```

Der Ausdruck Lambda(n) in SD11 ist die von-Mangoldt-Funktion, **nicht**
der Quellraumoperator Lambda_R. Der Faktor 2 bleibt ausdrücklich erhalten.

O3AF.4 identifiziert das konkrete P11-Symbol als

```math
m_\Gamma(\xi)=q_\Gamma(\xi)+c_0,
\quad q_\Gamma=\operatorname{Re}\psi(1/4+i\xi/2)-\log\pi,
\quad c_0=1+\log\pi-\psi(1/4).
```

P02s Gamma-Paarung hat Symbol q_Gamma mit Faktor 1/(2pi). Durch
Polarisierung beziehungsweise direktes Zusammenführen der +/-xi-Terme folgt

```math
\boxed{B_W(a,b)-\mathfrak c_\Gamma[a,b]
 =B_{\rm pole}(a,b)+B_{\rm fin}(a,b)-c_0\langle a,b\rangle_{L^2}.}
\tag{SD12}
```

Wir setzen also gerade **nicht** die positive P11-Gamma-Form und den
archimedischen Weil-Beitrag gleich. SD12 verwendet die bereits vorhandene
konkrete Symboldefinition O3AF; keine alternative Gamma-Norm wird eingeführt.

## 6. Ein exakter Primzahl-2-Zeuge, schon im Radius R=1

Setze

```math
\delta=1/100,\qquad y=\tfrac12\log(5/4),\qquad \ell=\log2.
```

Wähle reelles nichtnull `phi_0 in C_c^infinity(R)` mit Träger in
`[y-delta,y+delta]` und

```math
c=\frac{D(D^2-1/4)\phi_0}{\|D(D^2-1/4)\phi_0\|_2},
\qquad D=d/dx.
\tag{SD13}
```

Der Nenner ist nichtnull: Eine Lösung der konstantkoeffizientigen ODE
`D(D^2-1/4)phi_0=0` ist eine Linearkombination von 1 und exp(+/-x/2),
also bei kompaktem Träger identisch null.

Partielle Integration ohne Randterme ergibt für lambda=0,+1/2,-1/2

```math
\int e^{\lambda x}D(D^2-1/4)\phi_0(x)dx
 =(-\lambda^3+\lambda/4)\int e^{\lambda x}\phi_0(x)dx=0.
\tag{SD14}
```

Definiere die beiden tatsächlichen reellen ungeraden Quellen

```math
b(x)=\frac{c(x)-c(-x)}{\sqrt2},\qquad
 a(x)=\frac{c(x-\ell)-c(-x-\ell)}{\sqrt2}.
\tag{SD15}
```

Die vier Quelllappen sind getrennt. Beide Quellen haben L2-Norm eins,
liegen in `C_c^infinity((-1,1))_odd` und besitzen disjunkte Träger.
Insbesondere `C_(a,b)(0)=<a,b>=0`.

Die nötigen strikten Trägergrenzen sind elementar: `log(5/4)>1/5`,
`log(6/5)>1/6`, `log2>1/2`, `log(3/2)>1/3`, während
`log(5/4)<1/4` und `log2<7/10`. Die unteren Schranken folgen aus
`log(1+x)>x/(1+x)`; die letzte obere aus der Exponentialreihe.
Sie implizieren insbesondere `y>delta` und `y+ell+delta<1`.

Weil c auf der positiven Halbachse liegt und
`I_0(x)=2(1-e^(-x/2))`, liefert SD14

```math
\beta(a)=\beta(b)=0.
\tag{SD16}
```

SD14 bleibt unter Translation gültig, und unter Spiegelung werden die beiden
Exponentialmomente vertauscht. Also besitzen a und b beide die Momente
`integral exp(+/-x/2)a(x)dx=integral exp(+/-x/2)b(x)dx=0`.
Direkte Integration der Kreuzkorrelation gegen exp(+/-u/2) ergibt deshalb

```math
h_{a,b}(i/2)=h_{a,b}(-i/2)=0,
\qquad B_{\rm pole}(a,b)=0.
\tag{SD17}
```

Die Stütze von C_(a,b) liegt ausschließlich in den vier Intervallen
mit Halbbreite 2delta um

```math
+\ell,\quad-\ell,\quad+(2y+\ell),\quad-(2y+\ell),
\qquad 2y+\ell=\log(5/2).
\tag{SD18}
```

Unter allen positiven log n, n>=2, trifft diese Stütze nur log2.
Insbesondere liegt das zusätzliche positive Korrelationsintervall um
log(5/2) strikt zwischen log2 und log3, denn die Abstände sind log(5/4)
und log(6/5), beide größer als 2delta. Das Intervall um log2 erreicht weder
0 noch log3. Alle höheren Primzahlen und Primzahlpotenzen sind damit
**durch exakten Trägerausschluss** berücksichtigt, nicht numerisch abgeschnitten.

Bei u=ell trägt genau das Paar der beiden positiven Quelllappen bei;
bei u=-ell genau das Paar der beiden negativen Lappen. Normierung in SD13
und die Faktoren 1/sqrt2 geben

```math
C_{a,b}(\ell)=C_{a,b}(-\ell)=1/2,
\qquad g_{a,b}(\ell)=1/2.
\tag{SD19}
```

Einsetzen in die **volle** P02-Primzahlform liefert exakt

```math
\boxed{B_{\rm fin}(a,b)=-\frac{\log2}{\sqrt2}.}
\tag{SD20}
```

Mit SD12, SD17 und der disjunkten L2-Paarung folgt der angekündigte Satz:

```math
\boxed{
B_W(a,b)-\mathfrak c_\Gamma[a,b]
 =-\frac{\log2}{\sqrt2}\ne0.
}
\tag{SD21}
```

Für jede Referenz phi in SD7 gilt deshalb gleichermaßen
`B_W(a,b)-Q_phi(a,b)=-log2/sqrt2`.
Es ist kein asymptotischer Grenzwert und kein Float64-Positivitätszeugnis.
Die Diagonalen B_W(a,a), B_W(b,b) werden hier nicht negativ behauptet.
Eine negative gemischte Paarung ist mit positiven Gramformen vereinbar.

## 7. Genau ausgeschlossene Route und neuer konkreter Anschluss

**Satz.** Auf einer Testklasse, die die beiden expliziten Quellen SD15 enthält,
kann keine Weil-Gram-Realisierung den Gamma-Gram auf dem gesamten Nulljetraum
unverändert lassen. Schon die Forderung

```math
\langle T h,T k\rangle=\mathfrak c_\Gamma[h,k]
\quad(h,k\in D_0^-)
\tag{SD22}
```

widerspricht SD21, wenn zugleich `B_W(h,k)=<Th,Tk>` verlangt wird.
Das gilt unabhängig davon, wie T außerhalb von ker beta definiert wird.
Insbesondere kann keine ausschließliche Normalen-/Nulljet-Skalierung und
keine andere Wahl von phi die konkrete Familie SD7 zur Weil-Realisierung machen.

Die P02-Amplitudenklasse enthält SD15; auch die vorgeschaltete adelische
Amplitude ist verfügbar, denn der eingefrorene Port R_PW ist auf diese Klasse
surjektiv. Die Wahl einer kleineren künftigen Weil-Testklasse müsste jedoch
separat begründet werden. SD21 schließt nicht jede denkbare kleinere Klasse
oder jede andere arithmetische Quellenumkodierung aus.

Der bisher nur vorgeschlagene Verträglichkeitsvertrag SD8 ist somit tatsächlich
konstruiert. Der **verbleibende Realisierungsschritt liegt nicht allein im
Normalkanal**: Eine erfolgreiche Quellenabbildung muss bereits die Paarungen
im unendlichdimensionalen tangentialen Nulljetraum arithmetisch verändern.
Für das konkrete normalisierte Paar verlangt sie mindestens

```math
\langle T a,T b\rangle-\mathfrak c_\Gamma[a,b]
 =-\frac{\log2}{\sqrt2}.
\tag{SD23}
```

SD23 ist ein zwingender Kalibrierungstest für einen später konstruierten
arithmetischen Mechanismus, kein vorgeschobener Beweis seiner Existenz.
Die zusätzliche benötigte Tangentialgeometrie wird hier nicht konstruiert.
Weder C6 noch der terminale Induktivlimes werden dadurch widerlegt.

## 8. Autorengegencheck, Ausführung und Status

Der Begleittest `scripts/check_r43_post_c6_prime2_witness.py` verwendet
`phi_0(x)=exp(-1/(1-((x-y)/delta)^2))` im Inneren seines Trägers und 0
außerhalb. Ableitungen werden symbolisch gebildet, die reelle Glattquelle
wird anschließend numerisch integriert. Exakte rationale Kontrollen betreffen
das Momentpolynom, die sicheren Logarithmusgrenzen, R=1 und den Faktor 2.
Die numerischen Kontrollen betreffen Normierung, Momente und Korrelationen.

Ausgeführt: 41 Kontrollen, maximale absolute Testabweichung ungefähr
`1.67e-15`; Primzahlpaarung ungefähr `-0.490129071734275`.
Die separat ausgegebene adaptive Quadraturfehlerabschätzung wird nicht mit
diesem Residuum verwechselt. Dies sind finite Algebra-/Implementationschecks,
**kein** P11-/C6-, Intervall- oder Unendlichkeitshorizontzertifikat.
Der analytische Trägerbeweis, nicht eine endliche Primzahlliste im Skript,
sichert das Verschwinden aller übrigen Prime-Power-Beiträge.

Destruktiv kontrolliert wurden: inverse statt unkontrollierte positive
Wurzelgrenzwerte; Lambda als eingeschränkter Gammaoperator; eine feste
kofinale Referenzquelle; Unterschied zwischen iota und iota T; positive
P11-Gamma-Norm versus P02-Gamma-Beitrag; beide exponentiellen Polmomente;
die zusätzlichen spiegelungsbedingten Korrelationslappen bei log(5/2);
Prime-Power-Vollständigkeit und der Evenisierungsfaktor 1/2.

Buchung ausschließlich für diesen neuen Draft: analytischer Kandidat,
externer Exact-Head-Review offen. Keine Änderung der alten C6-Beweisdateien,
keine Registry-/Freeze-Promotion, kein Merge und keine Änderung an PR89/PR49.

## 9. Primärquellen und exakte Ableitungsgrenze

Alle Repositoryquellen beziehen sich auf den angegebenen Mergehead.
Die Aussagen SD3–SD23 sind die in diesem Dokument ausgeschriebenen neuen
Ableitungen; die folgenden Quellen liefern ihre benannten Eingänge.

1. [Objekt-X-Arbeitsdefinition, §§1–1.4](../00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md):
   exakte vollständige Weil-Gram-Identität, Intrinsizität, Realisierungsneutralität.
2. [P11, (2.7)–(3.3), (4.6)–(4.9)](../papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex):
   Gamma-/Graphgeometrie, Pullback, Isometrie, Kozykel.
3. [PR90, PA1–PA3 und PA14–PA19](P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md):
   starker Normalenlimes und kompletter ungerader Limes mit R42.51;
   Blob `a3229f0882a31046434389e5915badea686dae73`.
4. [R42, (R42.40) und (R42.51)](P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md):
   inverse Wurzelgrenze und tatsächlicher tangentialer Transport;
   Blob `804d9040db4867f5f3967fbccc62e189492a7e2e`.
5. [P11 Direct Terminal Bridge, DT.1–DT.6, DT.24](../papers/P11_sections/P11_Direct_Terminal_Bridge.tex):
   Jetdefinition, Pullback und glatter Graphkern.
6. [P11 Gamma Symbol Bridge, O3AF.1–O3AF.4](../papers/P11_sections/P11_O3af_Gamma_Symbol_Bridge.tex):
   konkretes Gamma-Symbol und exakte affine P02/P11-Normalisierung;
   Blob `f0f1357dbef8811db516a9e86b8475e0f6056ae0`.
7. [P02, Stage 1/2 und vollständige Hermitesche Weil-Form](../papers/P02_Adelic_Weil_Amplitude_Port.tex):
   tatsächliche Testklasse, surjektiver Amplitudenport, Kreuzkorrelation,
   Pol- und Primzahlterme; Blob `c3fb26a1b4c1c383834a790d630b0d9df08f714e`.

Keine externe Kurzintervallhypothese, keine Primzahlzähl-Asymptotik und
keine RH-Annahme wird für den neuen Trennungstest verwendet. Das Beispiel
benutzt ausschließlich den tatsächlichen Kanal n=2 und exakte Trägergrenzen.
