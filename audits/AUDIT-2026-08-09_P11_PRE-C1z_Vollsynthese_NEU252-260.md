# AUDIT-2026-08-09 — P11 PRE-C1z
## Vollsynthese NEU-252 bis NEU-260

**Datum:** 2026-08-09  
**Block:** P11 — Global Coupling and the Object-X Candidate Geometry  
**Zweck:** mathematische Vollsynthese der vorhandenen Forschungsknoten NEU-252 bis NEU-260b.2 als bindender Vorbereitungsschritt vor P11-C1z  
**Status:** `✓[K/M] PASS — MATHEMATICAL SYNTHESIS COMPLETE / PRE-C1z RELEASED`  
**Wichtig:** Dies ist **kein P11-SYN und kein P11-Seal**. P11 bleibt `ACTIVE`.

---

# 0. Auditfrage und Scope

Der vorliegende Audit beantwortet nicht nur die Inventarfrage „Welche Dateien existieren?“, sondern liest die mathematische Kette NEU-252–260 direkt und rekonstruiert:

1. die Definitionen und positiven Resultate;
2. die negativen Resultate mit exakt begrenztem Scope;
3. die späteren Patches/Korrekturen und Supersessionen;
4. die noch offenen Teilprobleme;
5. die heutige SYN-Zuordnung nach P02/P03/P04/P11/P12;
6. die für P11-C1z bindenden Firewalls.

Direkt gelesen wurden die vorhandenen Knoten:

- NEU-252,
- NEU-253,
- NEU-254,
- NEU-255,
- NEU-256,
- NEU-257,
- NEU-258,
- NEU-259,
- NEU-260,
- NEU-260a,
- NEU-260b,
- NEU-260b.1,
- NEU-260b.2.

**Physischer Datei-Status:**

- `NEU-260c` existiert auf `main` nicht als Datei;
- `NEU-260d` existiert auf `main` nicht als Datei;
- beide werden in NEU-260/P04 lediglich als geplante offene Nachfolgeknoten geführt;
- in der heutigen SYN-Zielarchitektur gehören die zugehörigen Grenzfragen nach P12.

NEU-251 ist kein Bestandteil des mathematischen 252–260-Audits, wird aber in der Provenienz als `UNALLOCATED / NO PHYSICAL NODE VERIFIED` geführt.

---

# 1. Gesamturteil in einem Satz

Die Kette NEU-252–258 konstruiert die exakte hermitesche Weilform, identifiziert einen kanonischen Haar-$L^2$-Hintergrund und zeigt anschließend **strukturell**, dass dieser Hintergrund nicht der gesuchte Weil-Abschlussraum sein kann; NEU-259–260 wechseln deshalb auf eine RH-freie **finite Intervall-/Suzuki-Geometrie**, deren endliche Operatorstruktur real ist, deren globaler $a\to\infty$-Übergang aber weiterhin offen bleibt.

Formal:

\[
\boxed{
\text{exaktes }B_W
\xrightarrow{252}
\text{RH-freie Geometriefrage}
\xrightarrow{253-255}
H_0=L^2(\mathbb R)
\xrightarrow{256-258}
\text{Haar-}L^2\text{-Firewall}
\xrightarrow{259-260}
\text{finite Suzuki-Geometrie + offener Grenzübergang}
}
\]

Für P11 ist daher bindend:

\[
\boxed{
H_0=L^2(\mathbb R,du)
\text{ ist ein kanonischer Hintergrundraum, aber nicht }\mathcal K_X.
}
\]

---

# 2. NEU-252 — M3: Hermitesche Polarisation der vollständigen Weilform

## 2.1 Kernkonstruktion

Auf

\[
\mathcal A_{\rm PW}:=C_c^\infty(\mathbb R;\mathbb C)
\]

werden mit dem Translationsfluss $U_t$ die Kreuzkorrelationen

\[
C_{a,b}(t)=\langle a,U_t b\rangle
\]

und die Evenisierung

\[
\boxed{
 g_{a,b}(t)=\frac12\bigl(C_{a,b}(t)+C_{a,b}(-t)\bigr)
}
\]

definiert.

Es gilt

\[
g_{b,a}(t)=\overline{g_{a,b}(t)},
\qquad
 g_{a,a}=g_a.
\]

Die Fourier-/Paley-Wiener-Funktion wird korrekt als

\[
\boxed{
 h_{a,b}(z)=\int_{\mathbb R}g_{a,b}(u)e^{izu}\,du
 \in \mathcal H_{\rm PW}^{\mathbb C}
}
\]

gebucht.

### Patch-Firewall

Die ältere Behauptung

\[
h_{a,b}\in\mathcal A_{\rm PW}
\]

ist falsch und wird durch die korrekte Aussage ersetzt:

- $h_{a,b}$ ist ganz;
- $h_{a,b}$ ist gerade;
- $h_{a,b}|_{\mathbb R}$ ist Schwartz;
- der zugehörige Weil-Testkern wird über
  \[
  F_{a,b}(s)=h_{a,b}\!\left(\frac{s-1/2}{i}\right)
  \]
  parametrisiert.

## 2.2 Die drei Blöcke

Die vollständige polarisierte Weilform wird komponentenweise definiert:

\[
B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}.
\]

Dabei

\[
B_{\rm pole}(a,b)
 =h_{a,b}(i/2)+h_{a,b}(-i/2),
\]

\[
B_\Gamma(a,b)=2\Lambda_\Gamma(h_{a,b}),
\]

und

\[
\boxed{
B_{\rm fin}(a,b)
=-2\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
 g_{a,b}(\log n).
}
\]

Alle drei Blöcke sind sesquilinear und hermitesch; damit ist

\[
\boxed{B_W(a,b)}
\]

eine wohldefinierte hermitesche Form und

\[
B_W(a,a)=\mathfrak W(a).
\]

Adelisch kann sie über den P02-Port zurückgezogen werden:

\[
B_W^{\rm adel}(F,G)
:=B_W(R_{\rm PW}F,R_{\rm PW}G).
\]

## 2.3 Was NEU-252 **nicht** beweist

NEU-252 beweist ausdrücklich **keine globale Positivität**:

\[
B_W\ge0
\]

wäre im Weil-Kriterium RH-äquivalent. Ebenso gibt es hier noch kein

\[
B_W(a,b)=\langle Ta,Tb\rangle.
\]

### Endstatus

`NEU-252 = INCORPORATED ✓[K/M]`  
SYN-Ziel: P02 §6.

---

# 3. NEU-253 — M4: RH-unabhängige geometrische Realisierung von $B_W$

NEU-253 ist kein fertiger Konstruktionssatz, sondern die präzise Zerlegung der nächsten Geometriefrage in vier atomare Aufgaben.

## 3.1 M4-A — positiver Hintergrund / Repräsentation

Gesucht ist ein kanonischer positiver Hilbertraumhintergrund und — je nach Regularität — entweder ein beschränkter Riesz-Operator oder eine unbeschränkte Form-/Operatorrealisierung von $B_W$.

NEU-253 trennt damit korrekt:

- **beschränkte Riesz-Route**;
- **unbeschränkte/closable Form-Route**.

Diese Trennung wird in NEU-255–257 entscheidend.

## 3.2 M4-B — Signatur-Firewall

Sobald eine selbstadjungierte Repräsentation $A_X$ existiert, gilt schematisch:

\[
\mathcal H_-\ne0
\iff
\exists a:\ B_W(a,a)<0
\iff
\neg RH.
\]

Eine negative Richtung wäre also kein harmloser Zwischenschritt zu einer positiven Theorie, sondern im exakten Weilmodell ein RH-Gegenbefund.

## 3.3 M4-C — arithmetischer physikalischer Unterraum

Ein eventueller Unterraum $K_{\rm phys}$ darf nicht post hoc so gewählt werden, dass Negativität verschwindet. Er muss aus arithmetischen/adèlischen Daten kanonisch entstehen.

## 3.4 M4-D — Positivität erst am Ende

Die Positivitätsfrage darf erst nach Konstruktion und Typisierung des geometrischen Trägers gestellt werden.

## 3.5 Wichtige Quotientenkorrektur

Der isotrope Kegel

\[
\{a:B_W(a,a)=0\}
\]

ist bei einer indefiniten Form im Allgemeinen **kein linearer Unterraum** und daher kein zulässiger Quotientenkern.

Der richtige lineare Begriff lautet

\[
\boxed{
\operatorname{Rad}(B_W|_K)
=\{a\in K:B_W(a,b)=0\ \forall b\in K\}.
}
\]

Nur nach etablierter Positivität kann Nullnorm und Radikal zusammenfallen.

### Endstatus

`NEU-253 = INCORPORATED / FRAMEWORK ✓[K/M]_part`  
Die ursprüngliche M4-Gesamtaufgabe bleibt als Objekt-X-Geometrie offen; ihre Haar-$L^2$-Variante wird durch NEU-257 negativ entschieden.

---

# 4. NEU-254 — Direktaudit dreier positiver Hintergrundkandidaten

NEU-254 prüft drei bereits vorhandene positive Strukturen darauf, ob sie als RH-freier Hintergrund für die **vollständige** Weilform dienen können.

## 4.1 Kandidat I — archimedische semifinite Spur

Positiv und kanonisch im Gamma-/archimedischen Sektor, aber nicht hinreichend für die vollständige Form

\[
B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}.
\]

**Urteil:** echter Baustein, kein vollständiger M4-A-Träger.

## 4.2 Kandidat II — Moment-GNS

Als Ziel-/Kontrollraum nützlich; sobald seine Positivität aber die exakte Weilpositivität voraussetzt, ist er nicht mehr RH-freie Quelle, sondern bereits äquivalent zum Zielproblem.

**Urteil:** kein unabhängiger RH-freier Beweisweg.

## 4.3 Kandidat III — adèlischer Momentquellraum

Konzeptionell der stärkste Kandidat. NEU-254 erkennt aber, dass ältere Aussagen zu Scattering-/Operatoridentifikationen nicht vollständig typisiert sind.

Die belastbare Struktur ist der P02-Port.

## 4.4 Korrektur: kein $R_{\rm PW}^{-1}$

Da $R_{\rm PW}$ surjektiv, aber nicht injektiv ist, darf kein kanonisches

\[
R_{\rm PW}^{-1}
\]

behauptet werden.

Stattdessen gibt es die explizite Sektion

\[
S_{\rm PW}a=h_a\otimes 1_{\widehat{\mathbb Z}},
\qquad
R_{\rm PW}S_{\rm PW}=I.
\]

Sie ist $L^2$-isometrisch, sodass auf Hilbertebene

\[
L^2(\mathbb A_{\mathbb Q})/\ker\overline R_{\rm PW}
\cong L^2(\mathbb R,du).
\]

### Heutige P11-Korrektur

Die historische Hoffnung, dass nach dem Haarquotienten alle fehlende Arithmetik einfach in einem späteren Operator/Domain wieder auftauchen könne, ist **nicht mehr als automatische Aussage zulässig**. P11-C1l zeigt konkret, dass der Haar-Port BC-Labelmomente verlieren kann.

Daher gilt heute nur:

\[
\boxed{
L^2(\mathbb R,du)
\text{ ist der kanonische Haar-Hintergrund, nicht die vollständige finite-adische Geometrie.}
}
\]

### Endstatus

`NEU-254 = INCORPORATED / REFINED`  
SYN-Ziel: P03; durch P11-C1l in seiner Interpretation weiter eingeengt.

---

# 5. NEU-255 — Haar-Koisometrie, $L^2$-Majorante und Operatoraudit

NEU-255 macht die in NEU-254 vorbereitete Hilbertstruktur exakt.

## 5.1 Koisometrie

Auf Hilbertebene wird gezeigt:

\[
\boxed{
\overline R_{\rm PW}=S_{\rm PW}^*.
}
\]

Damit ist $\overline R_{\rm PW}$ eine Koisometrie und

\[
\boxed{
L^2(\mathbb A_{\mathbb Q})/\ker\overline R_{\rm PW}
\cong
H_0:=L^2(\mathbb R,du).
}
\]

Dies ist eine echte RH-freie positive Hintergrundgeometrie.

## 5.2 Unbeschränktheit der Weilform auf $H_0$

Für modulierte Testfunktionen

\[
a_N(u)=e^{iNu}\varphi(u),
\qquad \|a_N\|_2=1,
\]

werden die Blöcke getrennt analysiert:

- Primterm bleibt in diesem Test $O(1)$;
- Polterm verschwindet asymptotisch;
- Gamma-Term wächst logarithmisch positiv.

Daraus folgt

\[
\boxed{
B_W(a_N,a_N)\to+\infty.
}
\]

Also ist $B_W$ auf $H_0$ nicht durch die $L^2$-Norm beschränkt.

Damit ist die **beschränkte Riesz-Route** aus M4-A ausgeschlossen.

## 5.3 Was 255 offen lässt

Unbeschränktheit bedeutet noch nicht:

- nicht semibeschränkt;
- nicht closable;
- keine unbeschränkte selbstadjungierte Realisierung.

Diese Fragen werden erst in 256/257 entschieden bzw. korrigiert.

### Endstatus

`NEU-255 = INCORPORATED ✓[K/M]`  
SYN-Ziel: P03 §2.  
$H_0=L^2$ ist **background Hilbert space**, nicht finaler Weilraum.

---

# 6. NEU-256 — Semibeschränktheit/Abschließbarkeit: Diagnose des KLMN-Wegs

NEU-256 untersucht, ob die unbeschränkte Weilform dennoch als closable semibeschränkte Form auf Haar-$L^2$ behandelt werden kann.

## 6.1 Gamma als Referenzform

Als positiver Referenzblock wird eine logarithmische Fourierenergie betrachtet, schematisch

\[
q_\Gamma^+(a,a)
=\int |\widehat a(t)|^2\log(1+|t|)\,dt+\|a\|_2^2.
\]

Die gewünschte KLMN-Struktur wäre eine relative Abschätzung

\[
|R_{\rm arith}(a,a)|
\le
\alpha q_\Gamma^+(a,a)+C\|a\|_2^2,
\qquad \alpha<1,
\]

mit

\[
R_{\rm arith}=B_{\rm pole}+B_{\rm fin}.
\]

## 6.2 Dilationstest und Prime-Divergenz

Für

\[
a_L(u)=L^{-1/2}\varphi(u/L)
\]

gilt

\[
g_{a_L,a_L}(t)=C_\varphi(t/L).
\]

Über PNT-Asymptotik wird sichtbar, dass der **isolierte** Primblock entlang dieser Familie stark nach unten laufen kann:

\[
B_{\rm fin}(a_L,a_L)\to-\infty.
\]

Damit ist

\[
B_{\rm fin}
\]

weder $L^2$-beschränkt noch separat nach unten beschränkt.

## 6.3 Zentrale Patch-Korrektur: Pol und Prim dürfen nicht getrennt werden

Die spätere Korrektur in NEU-256 ist wesentlich:

Der Polterm wächst beim selben Dilationstest positiv und kompensiert den führenden negativen Primbeitrag. Deshalb ist es mathematisch falsch, aus der isolierten Prime-Divergenz unmittelbar eine Divergenz der **vollen** Weilform abzuleiten.

Die explizite Formel erzwingt gerade diese globale Kompensation.

## 6.4 Zweite Korrektur: Semibeschränktheit impliziert nicht automatisch Closability

Eine frühere Gårding/KLMN-Hoffnung wird eingeengt:

\[
\boxed{
\text{Semibeschränktheit allein} \not\Rightarrow \text{Abschließbarkeit}.
}
\]

Die Closability-Frage benötigt einen unabhängigen Test.

### Endstatus

`NEU-256 = INCORPORATED / DIAGNOSTIC; KLMN ROUTE SUPERSEDED`  
Die asymptotischen Diagnosen bleiben gültig; der Versuch, daraus allein eine Haar-$L^2$-Formrealisierung zu gewinnen, wird durch NEU-257 endgültig ersetzt.

---

# 7. NEU-257 — die bindende Haar-$L^2$-Firewall

NEU-257 ist der mathematische Wendepunkt des Blocks.

## 7.1 Präzise Semibeschränktheitsäquivalenz

Auf dem Haar-Hintergrund gilt:

\[
\boxed{
\exists \lambda\ge0:\
B_W(a,a)\ge-\lambda\|a\|_2^2\ \forall a
\iff RH.
}
\]

Damit ist bereits die $L^2$-Semibeschränktheit kein RH-freier Zwischenschritt.

## 7.2 Spektraldarstellung unter RH

Unter RH besitzt die Weilform die atomare Darstellung

\[
\boxed{
B_W(a,b)
=
\sum_{\gamma\in\Gamma}
 m_\gamma\,
\widehat a(-\gamma)
\overline{\widehat b(-\gamma)}
}
\]

mit

\[
\mu_W
=
\sum_{\gamma\in\Gamma}m_\gamma\delta_{-\gamma}.
\]

Das Spektralmaß ist rein atomar und daher singulär bezüglich Lebesgue-/Haarmaß.

## 7.3 Non-closability

Für Formen

\[
q_\sigma(f)=\int|\widehat f|^2\,d\sigma
\]

ist die Abschließbarkeit auf $L^2(dx)$ an absolute Stetigkeit des Maßes gekoppelt. Da

\[
\mu_W\perp du,
\]

folgt unter RH:

\[
\boxed{
B_W\text{ ist auf }H_0=L^2(\mathbb R,du)\text{ nicht abschließbar.}
}
\]

NEU-257 bestätigt dies zusätzlich durch eine explizite Folge $a_n$ mit

\[
a_n\to0\quad\text{in }L^2,
\]

\[
B_W(a_n-a_m,a_n-a_m)\to0,
\]

aber

\[
B_W(a_n,a_n)\not\to0.
\]

## 7.4 Konsequenz für KLMN/Friedrichs

Auf Haar-$L^2$ sind Semibeschränktheit und Closability in der benötigten positiven Formroute nicht gleichzeitig verfügbar.

Daher:

\[
\boxed{
\text{KLMN/Friedrichs auf Haar-}L^2\text{ ist kein Objekt-X-Weg.}
}
\]

## 7.5 Exakter Scope des No-Gos

NEU-257 beweist **nicht**:

- dass es keinen stärkeren Hilbertraum gibt;
- dass es keine RKHS-/Graphnorm gibt;
- dass keine adèlische/relative Geometrie existiert;
- dass kein Objekt X existiert.

Es beweist nur den sehr starken, aber präzisen Satz:

\[
\boxed{
\text{Die exakte Weilform kann nicht als closable Form auf dem Haar-}L^2
\text{-Hintergrund enden.}
}
\]

### Endstatus

`NEU-257 = INCORPORATED ✓[K/M] — BINDING FIREWALL`  
SYN-Ziel: P03 §3–§5, `FROZEN`.

---

# 8. NEU-258 — Normierungsidentifikation der Weil-Distribution

NEU-258 prüft, ob die harte NEU-257-Firewall eventuell nur auf einer fehlerhaften Normalisierung von NEU-252 beruht.

## 8.1 Direkt geprüfte Normalisierungen

Geprüft werden insbesondere:

1. Fourierkonvention;
2. Zentrierung $s=1/2+it$;
3. Polauswertungen bei $\pm i/2$;
4. Gamma-Vorfaktor;
5. endlicher Primterm mit
   \[
   -2\frac{\Lambda(n)}{\sqrt n}.
   \]

## 8.2 Ergebnis

Die in NEU-252 definierte Distribution stimmt mit der Literatur-Weilform überein:

\[
\boxed{
B_{W,\mathrm{NEU\text{-}252}}
=B_{W,\mathrm{Lit}}.
}
\]

Damit gibt es **keinen Normierungs-Ausweg** aus NEU-257.

### Endstatus

`NEU-258 = INCORPORATED ✓[K/M]`  
SYN-Ziel: P02 §6 / P03 Normalisierungs-Firewall.

---

# 9. Synthese 252–258: der Haar-$L^2$-Pfad ist vollständig entschieden

Die Kette lautet jetzt ohne Lücke:

\[
\boxed{
\begin{array}{rcl}
252 &:& B_W\text{ exakt hermitesch polarisiert},\\
253 &:& RH\text{-freie Geometriefrage typisiert},\\
254 &:& positive Hintergrundkandidaten auditiert},\\
255 &:& H_0=L^2\text{ kanonisch, aber }B_W\text{ unbeschränkt},\\
256 &:& KLMN-/Dilationstest diagnostiziert globale Kompensation},\\
257 &:& \text{unter RH: }B_W\text{ auf }L^2\text{ nicht closable},\\
258 &:& \text{Normalisierung exakt; Firewall kein Artefakt}.
\end{array}
}
\]

Die heutige bindende Interpretation ist daher:

\[
\boxed{
H_0=L^2(\mathbb R,du)
\text{ ist Referenz-/Hintergrundraum, nicht der finale Weilraum.}
}
\]

Dies ist bereits im eingefrorenen SYN-Paper P03 konsolidiert.

---

# 10. NEU-259 — Finite-Intervall-Grenzwertweg / Suzuki-Träger

Nach der Haar-$L^2$-Firewall wechselt NEU-259 die Ebene: Nicht mehr die globale Form auf ganz $\mathbb R$ soll direkt geschlossen werden, sondern zunächst eine **endliche Intervallgeometrie**.

## 10.1 RH-freie finite Operatorstruktur

Für jedes $a>0$ ist auf der endlichen Suzuki-Ebene eine reale Operatorstruktur vorhanden. In der heutigen P04-Synthese wird festgehalten:

- $Q_W^a$ ist semibeschränkt und closable auf $L^2(-a,a)$;
- es gibt einen selbstadjungierten Operator
  \[
  A_a=A_a^*;
  \]
- $A_a$ besitzt diskretes, nach unten beschränktes Spektrum;
- mit
  \[
  \lambda_a=\inf\sigma(A_a)
  \]
  und $\lambda<\lambda_a$ ist
  \[
  T_{a,\lambda}=A_a-\lambda I>0;
  \]
- daraus entsteht ein Hilbertraum
  \[
  \mathcal H(T_{a,\lambda});
  \]
- die zugehörigen first-order Operatoren besitzen selbstadjungierte Erweiterungen mit Defizienzindizes $(1,1)$.

Diese Ebene ist **RH-frei und theorematisch**, nicht bloß heuristisch.

## 10.2 Was noch fehlt

Der globale Objekt-X-Schritt ist nicht konstruiert. Offen sind insbesondere:

- kanonische Grenz-/Normalisierungsdaten;
- die Phase bzw. intrinsische Randabbildung;
- $\phi(a,z)$;
- Übergangskarten
  \[
  J_{a,b};
  \]
- ein kanonischer $a\to\infty$-Grenzraum;
- die genaue geometrische Identifikation des Grenzobjekts mit der vollständigen Weilgeometrie.

## 10.3 P11/P12-Firewall

NEU-259 ist **kein Ersatz für P11s globale Primkopplung**.

Seine natürliche heutige Rolle lautet:

\[
\boxed{
\text{finite RH-freie Weilgeometrie}
\longrightarrow
\text{P12 finite-to-infinite frontier}.
}
\]

Gleichzeitig ist die endliche Intervallgeometrie für P11-C1z-ZA konzeptionell relevant: Sie ist ein existierendes Beispiel dafür, dass eine source-/window-bedingte Geometrie die volle Translationinvarianz bricht. Daraus folgt jedoch noch **keine** Übertragung der Suzuki-Operatoren auf die neue BC-Kopplungsfrage.

### Endstatus

`NEU-259 = PARTIAL-INCORPORATED / GLOBAL LIMIT OPEN`  
SYN-Ziel: P04 für finite Struktur; P12 für Grenzstruktur.

---

# 11. NEU-260 — Kanonizitätsaudit der Suzuki-Grenzdaten

NEU-260 ist ausdrücklich ein Arbeitsauftrag und zerlegt die noch fehlenden Grenzdaten in vier Teile:

\[
\boxed{
\text{A }\lambda,
\qquad
\text{B }\theta/U_a,
\qquad
\text{C }\phi(a,z),
\qquad
\text{D }J_{a,b}.
}
\]

Es ist **kein abgeschlossener Einzelknoten**.

### Endstatus

`NEU-260 = WORK-ORDER / PARTIAL-OPEN`.

---

# 12. NEU-260a — $\lambda$-Gauge / positive Arbeitsnormalisierung

NEU-260a klärt die Rolle des Verschiebungsparameters $\lambda$.

Für eine strikt positive Arbeitsform kann für jedes $c>0$ gesetzt werden

\[
\lambda_{a,c}=\lambda_a-c,
\qquad
T_{a,c}=A_a-\lambda_{a,c}I\ge cI.
\]

Die P04-Arbeitskonvention ist

\[
\boxed{
\lambda_{\rm w}(a)=\lambda_a-1,
\qquad
T_a^{\rm w}\ge I.
}
\]

Diese Wahl ist kanonisch **als festgelegte Arbeitsnormalisierung im Programm**, aber nicht mathematisch einzigartig.

Die verschiedenen strikt positiven Verschiebungen verändern die Hilberttopologie nur in einer kontrollierten äquivalenten Weise; in diesem Sinn ist $\lambda$ ein topologisches Gauge und kein bereits identifiziertes intrinsisches Objekt-X-Datum.

### Firewall

Daraus folgt **nicht** automatisch Spektralinvarianz sämtlicher späterer first-order Erweiterungen oder Grenzoperatoren.

\[
\boxed{
\lambda\text{-Topologiegauge }\neq
\text{ bewiesene globale Spektralgauge.}
}
\]

### Endstatus

`NEU-260a = PARTIAL-INCORPORATED ✓[K/M]`  
Topologische/Arbeitsnormalisierung geklärt; weitergehende Spektralfrage offen.

---

# 13. NEU-260b — intrinsische Randabbildung statt Koordinatenphase

Die Defizienzräume sind eindimensional:

\[
\mathcal N_{\pm,a}=\operatorname{span}\{v_\pm\}.
\]

Eine Wahl von Basisvektoren parametrisiert selbstadjungierte Erweiterungen durch einen Winkel $\theta$, aber unter Rephasierung der Defizienzbasen verschiebt sich dieser Winkel.

Daher ist nicht $\theta$ selbst das intrinsische Datum, sondern die unitäre Abbildung

\[
\boxed{
U_a:\mathcal N_{+,a}\to\mathcal N_{-,a}.
}
\]

NEU-260b prüft mögliche arithmetische Selektionsmechanismen.

## 13.1 KMS/Frobenius-Firewall

BC/KMS-Zeitpfeil oder Frobeniusorientierung sind konzeptionell suggestiv, aber im geprüften Stand gibt es **keine typisierte Abbildung** von diesen Daten auf die konkreten Suzuki-Defizienzlinien.

Daher darf daraus keine Phasenauswahl behauptet werden.

### Endstatus

`NEU-260b = INCORPORATED / SELECTION STILL OPEN`.

---

# 14. NEU-260b.1 — Parität reduziert $U(1)$ auf $\mathbb Z_2$

Der Paritätsoperator

\[
(Pf)(x)=f(-x)
\]

kommutiert mit $A_a$ bzw. $T_a$ und vertauscht die beiden Defizienzräume.

In der kanonischen Trivialisierung gilt

\[
Pv_+=v_-.
\]

Paritätsstabile selbstadjungierte Erweiterungen lassen daher nur noch zwei Möglichkeiten zu:

\[
\boxed{
U_a\in\{+P,-P\}
\cong\mathbb Z_2.
}
\]

Äquivalent in der Winkelkoordinate:

\[
\theta\in\{0,\pi\}.
\]

Das ist eine echte strukturelle Reduktion

\[
\boxed{U(1)\to\mathbb Z_2,}
\]

aber noch keine Auswahl eines Zweiges.

### Endstatus

`NEU-260b.1 = INCORPORATED ✓[K/M] — Z2 REDUCTION`.

---

# 15. NEU-260b.2 — konditionale Auswahl des $+P$-Zweigs

NEU-260b.2 untersucht, ob die von Suzuki erwartete globale Grenzfunktion die verbleibende $\mathbb Z_2$-Mehrdeutigkeit beseitigt.

Das Resultat ist ein **konditionaler Selektionssatz**:

\[
\boxed{
\text{Suzuki-Grenzrelation}
\Longrightarrow
U_a=+P
\text{ asymptotisch / im kanonischen Grenzzweig}.
}
\]

Damit ist die Zweigfrage nicht mehr völlig frei.

## 15.1 Zentrale Firewall

Die verwendete globale Grenzrelation ist selbst **nicht bewiesen**.

Daher gilt nicht unconditionally

\[
U_a=+P.
\]

Und aus NEU-260b.2 folgt insbesondere **kein RH-Beweis**.

### Heutiger SYN-Abgleich

P04 vom 2026-08-08 konsolidiert NEU-259, 260a, 260b und 260b.1, enthält aber NEU-260b.2 noch nicht als synchronisierten Endstand.

Daher:

`P04/P12-SYNC OPEN: NEU-260b.2 conditional +P selection`.

### Endstatus

`NEU-260b.2 = CONDITIONAL-INCORPORATION / P12-SYNC OPEN`.

---

# 16. NEU-260c / NEU-260d — physisch nicht angelegt

Im aktuellen Repo existieren keine Dateien

- `NEU-260c_*`,
- `NEU-260d_*`.

NEU-260/P04 führen sie nur als geplante offene Teilprobleme:

## 16.1 260c — Boundary normalization $\phi(a,z)$

Zu klären wäre eine kanonische/arithmetiche Normalisierung des Grenzausdrucks. Suzuki weist darauf hin, dass in bestimmten Formulierungen $\phi\equiv0$ ausreichen könnte; eine Objekt-X-Kanonisierung ist aber nicht konstruiert.

## 16.2 260d — Übergangskarten $J_{a,b}$

Gesucht wären kanonische Karten

\[
J_{a,b}:\mathcal H(T_a)\to\mathcal H(T_b),
\qquad a<b,
\]

mit geeigneter Intertwining-Eigenschaft für die selbstadjungierten Erweiterungen.

Ohne solche Karten gibt es keinen konstruierten induktiven Grenzraum

\[
\varinjlim_a\mathcal H(T_a).
\]

### Heutige Disposition

\[
\boxed{
\text{NEU-260c,d = PLANNED / DEFERRED }\to P12.
}
\]

Keine fehlende Datei darf als bereits bewiesene Mathematik behandelt werden.

---

# 17. Moderne Reconciliation gegen P02/P03/P04/P11/P12

| Knoten | Gültiger Kern | Heutiger Status | SYN-Ziel |
|---|---|---|---|
| NEU-252 | vollständige hermitesche Polarisation von $B_W$ | `INCORPORATED ✓[K/M]` | P02 |
| NEU-253 | M4-Architektur, Radikal-Firewall | `INCORPORATED / FRAMEWORK` | P03 / P11-Firewall |
| NEU-254 | RH-freie Hintergrundkandidaten, P02-Port/Sektion | `INCORPORATED / REFINED` | P03 |
| NEU-255 | Haar-Koisometrie, $H_0=L^2$, $B_W$ unbeschränkt | `INCORPORATED ✓[K/M]` | P03 |
| NEU-256 | Dilation/Kompensationsdiagnostik | `INCORPORATED`; KLMN-Hoffnung `SUPERSEDED` | P03 |
| NEU-257 | Semibdd. iff RH; unter RH non-closable auf Haar-$L^2$ | `INCORPORATED ✓[K/M]` | P03 FROZEN |
| NEU-258 | exakte Literatur-/Normierungsidentifikation | `INCORPORATED ✓[K/M]` | P02/P03 |
| NEU-259 | RH-freie finite Suzuki-Operatorstruktur | `PARTIAL-INCORPORATED`; global OPEN | P04 → P12 |
| NEU-260 | Kanonizitäts-Arbeitsauftrag A–D | `PARTIAL-OPEN` | P04/P12 |
| NEU-260a | positive Arbeitsnormalisierung / $\lambda$-Topologiegauge | `PARTIAL-INCORPORATED` | P04/P12 |
| NEU-260b | intrinsisches $U_a$, keine KMS/Frobenius-Brücke | `INCORPORATED / OPEN selection` | P04/P12 |
| NEU-260b.1 | Parität $U(1)\to\mathbb Z_2$ | `INCORPORATED ✓[K/M]` | P04 |
| NEU-260b.2 | Suzuki-Grenzrelation $\Rightarrow +P$ | `CONDITIONAL`; Sync offen | P12 / P04-sync |
| NEU-260c | keine Datei; $\phi(a,z)$ | `PLANNED / OPEN` | P12 |
| NEU-260d | keine Datei; $J_{a,b}$ | `PLANNED / OPEN` | P12 |

---

# 18. Acht bindende Firewalls aus NEU-252–260

## F1 — Hermitesch ist nicht positiv

NEU-252 konstruiert $B_W$ exakt als hermitesche Form. Daraus folgt keine RH-freie Positivität.

## F2 — Der isotrope Kegel ist kein Quotientenkern

Vor Positivität muss mit dem echten Radikal gearbeitet werden.

## F3 — Haar-$L^2$ ist Hintergrund, nicht Endraum

Die Koisometrie aus NEU-254/255 ist korrekt; sie konstruiert aber nur den kanonischen Haar-Hintergrund.

## F4 — Unbeschränktheit ist nicht Non-closability

NEU-255 schließt nur die bounded-Riesz-Route. Erst NEU-257 liefert den unabhängigen Closability-No-Go.

## F5 — Unter RH ist die Weilform gerade **nicht** closable auf Haar-$L^2$

Der atomare Nullstellenraum ist mit der Lebesgue-$L^2$-Topologie inkompatibel. Das ist die P03-Firewall.

## F6 — Die Firewall ist kein Normierungsartefakt

NEU-258 identifiziert die verwendete Weilform exakt mit der Literaturform.

## F7 — Finite Suzuki-Geometrie ist nicht der globale Grenzraum

NEU-259 liefert einen echten RH-freien endlichen Operatorträger; $J_{a,b}$ und der $a\to\infty$-Grenzraum bleiben offen.

## F8 — Parität reduziert, aber selektiert nicht unconditional

$U(1)\to\mathbb Z_2$ ist bewiesen; $+P$ folgt bisher nur konditional aus der offenen Suzuki-Grenzrelation.

---

# 19. Konsequenzen für P11-C1z

Die Vollsynthese verändert den C1z-Suchraum nicht durch einen neuen fertigen Kandidaten, aber sie macht zwei Richtungen wesentlich schärfer.

## 19.1 C1z-ZA — Source-window / boundary geometry

NEU-259 liefert einen realen Präzedenzfall:

\[
L^2(-a,a)
\]

und die endliche Weilgeometrie brechen die volle Translationsinvarianz und besitzen dennoch eine RH-freie semibeschränkte/closable Operatorstruktur.

Das rechtfertigt Z-A als mathematisch ernsthafte Vergleichsroute.

**Firewall:** Die Suzuki-Geometrie liefert noch keine P11-Primkopplung $B_{pq}$ und keinen globalen Objekt-X-Grenzraum.

## 19.2 C1z-ZB — finite-adische Konditionierung vor $P_{\rm Haar}$

NEU-254/255 zeigen exakt, wie der Haar-Port den kanonischen Hintergrund

\[
H_0=L^2(\mathbb R)
\]

erzeugt.

P11-C1l zeigt inzwischen zusätzlich, dass dieser Port finite-adische BC-Labelinformation verlieren kann.

Zusammen mit NEU-257 ergibt sich daher ein starkes strukturelles Motiv:

\[
\boxed{
\text{Die fehlende Objekt-X-Geometrie darf nicht erst nach vollständigem Haar-Kollaps rekonstruiert werden.}
}
\]

Dies ist **kein Existenzbeweis**, aber eine source-first Suchraumreduktion.

## 19.3 Reihenfolge nach diesem Audit

Für P11 wird daher freigegeben:

1. **C1z-ZB zuerst:** source-kanonische finite-adische Konditionierung vor $P_{\rm Haar}$;
2. **C1z-ZA als Kontrollroute:** nichttranslationsinvariante Window-/Boundary-Kompression;
3. P12 bleibt zuständig für Suzuki-$J_{a,b}$, $\phi(a,z)$ und $a\to\infty$.

---

# 20. Provenienz-Sonderfälle des angrenzenden Inventars

Der separate Vollständigkeitscheck vor diesem Audit hat folgende repo-seitige Sonderfälle bestätigt, die in `SYN_PROVENIENZ.md` sichtbar bleiben müssen:

1. **NEU-242 = DUPLICATE-ID:** zwei verschiedene Dokumente unter derselben NEU-Nummer in verschiedenen Ordnern;
2. **NEU-251 = UNALLOCATED / NO PHYSICAL NODE VERIFIED:** keine Datei auf aktuellem `main`;
3. **NEU-260c,d = PLANNED / DEFERRED → P12:** keine physischen Dateien;
4. **cross-folder nodes NEU-246–250x:** thematisch/physisch über mehrere Ordner verteilt; Dateipfad ist Teil der Provenienzidentität.

Daraus folgt für historische Verweise die zusätzliche Regel:

\[
\boxed{
\text{NEU-ID allein ist bei Duplicate-/Cross-folder-Fällen kein eindeutiger Dokumentbezeichner.}
}
\]

Mindestens ID **plus Dateipfad/Titel** müssen angegeben werden.

---

# 21. Abschlussurteil

Die mathematische Kette NEU-252–260 ist damit für die aktuelle SYN-/P11-Arbeit vollständig reconciliiert.

Der zentrale Erkenntnisbogen lautet:

\[
\boxed{
\begin{aligned}
&\text{NEU-252: exaktes hermitesches }B_W,\\
&\text{NEU-253--255: kanonischer positiver Haar-Hintergrund},\\
&\text{NEU-256--258: Haar-}L^2\text{-Endpunkt strukturell ausgeschlossen},\\
&\text{NEU-259--260: RH-freie finite Suzuki-Geometrie, globaler Grenzübergang offen}.
\end{aligned}
}
\]

Daher:

\[
\boxed{
\text{✓[K/M] PASS — MATHEMATICAL SYNTHESIS COMPLETE / PRE-C1z RELEASED.}
}
\]

**Kein P11-Seal. Kein RH-Beweis. Kein universeller No-Go gegen Objekt X.**

Der nächste aktive mathematische Knoten ist:

\[
\boxed{
\text{P11-C1z — non-translation-invariant source geometry, ZB first.}
}
\]

---

*Objekt-X-Programm — Auditstand 2026-08-09.*
