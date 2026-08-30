# P11/R32 — SW1-A10 Cross-Gram Cocycle Candidate

> **Stand:** 30. August 2026  
> **Branch:** research/sw1-a10-crossgram-cocycle  
> **Basis:** main@19da654f537868cd72757d2785071f8cf3f36c1b  
> **Status:** ?[O] gesamt — C0 als exakte inversefreie Kernelreduktion formuliert; C1-PROTO, C1B0, C1B1, C1B2A/B/C sowie C1C0-FORMAL im jeweils dokumentierten Scope zertifiziert. C1C1 besitzt ein zertifiziertes algebraisches/Faltungs-Skelett; die korrigierte analytische Hilbertraum-Fassung ist nach externem Cross-Model-Blindreview unabhängig GREEN im dokumentierten Scope. Die frühere Deutung von Boundary-Kollisionen als Fiberquotienten wurde korrigiert. Keine Promotion.  
> **Ziel:** den zu \(\ker\Gamma_I\) äquivalenten SW1-Operator auf der irrationalen H3-Rotationskomponente als endlichen operatorwertigen/finite-range Cocycle formulieren.

---

## 0. Ausgangspunkt und Firewall

A10-H3-INF zeigt im kleinen unteren Subchamber die Existenz mindestens einer unendlichen physischen augmentierten Hub-Inzidenzkomponente über der irrationalen Basisrotation

\[
T_\Delta:x\mapsto x+\Delta\pmod L,
\qquad
\Delta/L\notin\mathbb Q.
\]

Dies widerlegt nur die Strategie, den augmentierten Graphen vollständig in endliche Zusammenhangskomponenten zu zerlegen.

Es sagt weder

\[
\ker\Gamma_I=\{0\}
\]

noch

\[
\ker\Gamma_I\ne\{0\}.
\]

Der nächste Gegenstand ist daher der **wirkliche Operator** auf dieser irrationalen Komponente.

---

# C0 — inversefreie Cross-Gram-Kernelreduktion

## 1. Räume und KNF-Isomorphismus

Setze wie in A2/A3

\[
K:=\mathcal K_R
=
\ker(E_I^*H|_{\mathscr H_+}),
\]

\[
\mathcal F_R
=
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1}),
\]

und

\[
\boxed{
J_R:=\Psi_R^{-1}:\mathcal F_R\to K.
}
\]

Die Injektivitätsfrage von \(J_R\) ist **kein neuer offener Punkt**:

SW1-KNF beweist

\[
\Psi_R:K\xrightarrow{\sim}\mathcal F_R
\]

als beschränkten linearen Isomorphismus. A3 verwendet und re-auditiert daher

\[
\boxed{
J_R=\Psi_R^{-1}
}
\]

als beschränkten Isomorphismus auf \(K\).

Insbesondere

\[
\boxed{
\ker J_R=\{0\}.
}
\tag{C0.1}
\]

Damit entsteht in den freien Koordinaten kein künstlicher Zusatzkernel.

---

## 2. Definition des inversenfreien Operators

Schreibe

\[
\mathscr T:=I+A,
\qquad
Z:=HE_{\mathcal A}.
\]

Definiere

\[
\boxed{
\mathscr C_R:
\mathcal F_R\oplus\mathscr W
\to
\mathscr H_+,
\qquad
\mathscr C_R(\xi,w)
=
\mathscr T J_R\xi+Zw.
}
\tag{C0.2}
\]

Diese Form enthält **kein**

\[
\mathfrak G_R^{-1}.
\]

Sie ist genau die erste augmentierte Gleichung nach Einsetzen der vollständigen KNF-Koordinate

\[
y=J_R\xi\in K.
\]

---

## 3. Exakte Kernelbijektion mit dem augmentierten System

Definiere

\[
\Theta:
\mathcal F_R\oplus\mathscr W
\to
K\oplus\mathscr W,
\qquad
\Theta(\xi,w)
=
(J_R\xi,w).
\]

Da \(J_R\) ein beschränkter Isomorphismus ist, ist auch \(\Theta\) ein beschränkter Isomorphismus.

Für das augmentierte System

\[
\mathcal K_{I,A}(y,w)
=
\bigl(
\mathscr T y+Zw,
E_I^*Hy
\bigr)
\]

gilt für jedes \((\xi,w)\):

\[
E_I^*HJ_R\xi=0
\]

weil \(J_R\xi\in K\).

Daher

\[
\boxed{
\mathcal K_{I,A}\Theta(\xi,w)
=
\bigl(
\mathscr C_R(\xi,w),
0
\bigr).
}
\tag{C0.3}
\]

### 3.1 Explizite Surjektivität auf den augmentierten Kernel

Sei umgekehrt

\[
(y,w)\in\ker\mathcal K_{I,A}.
\]

Aus der zweiten augmentierten Gleichung folgt

\[
E_I^*Hy=0,
\]

also

\[
y\in K.
\]

Da

\[
J_R:\mathcal F_R\xrightarrow{\sim}K
\]

**surjektiv** ist, existiert eindeutig

\[
\xi=\Psi_Ry\in\mathcal F_R
\]

mit

\[
y=J_R\xi.
\]

Die erste augmentierte Gleichung liefert dann

\[
0
=
(I+A)y+HE_{\mathcal A}w
=
(I+A)J_R\xi+HE_{\mathcal A}w
=
\mathscr C_R(\xi,w).
\]

Also

\[
(\xi,w)\in\ker\mathscr C_R
\]

und

\[
\Theta(\xi,w)=(y,w).
\]

Damit ist ausdrücklich sowohl die Injektivität als auch die **Surjektivität von \(\Theta\) auf den Kernel** nachgewiesen; es wird keine alte \(\widehat\Phi_R\)-Parametrisierung als versteckte Zusatzannahme benutzt.

Somit induziert \(\Theta\) exakt

\[
\boxed{
\ker\mathscr C_R
\xrightarrow{\sim}
\ker\mathcal K_{I,A}.
}
\tag{C0.4}
\]

---

## 4. Rückbindung an den Schur-/Cross-Gram-Kern

A2 beweist, dass die Projektion auf die Annuluskoordinate

\[
(y,w)\mapsto w
\]

eine Bijektion

\[
\ker\mathcal K_{I,A}
\xrightarrow{\sim}
\ker\mathcal L_{\rm ann}^{\rm SW1}
\]

induziert.

Ferner gilt dort

\[
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker\mathcal S_{I,A},
\]

mit

\[
\mathcal S_{I,A}
=
E_I^*H(I+A)^{-1}H^*E_{\mathcal A}.
\]

Da

\[
B=(I+A)^{-1},
\]

ist dies genau der in Roadmap A verwendete Cross-Gramoperator

\[
\Gamma_I
=
E_I^*HBH^*E_{\mathcal A}.
\]

Damit entsteht die exakte Kette

\[
\boxed{
\ker\mathscr C_R
\xrightarrow{\sim}
\ker\mathcal K_{I,A}
\xrightarrow{\sim}
\ker\mathcal L_{\rm ann}^{\rm SW1}
=
\ker\Gamma_I.
}
\tag{C0.5}
\]

Explizit ist die letzte Bijektion auf \(\ker\mathscr C_R\) schlicht

\[
\boxed{
(\xi,w)\longmapsto w.
}
\]

Die inverse Abbildung ist

\[
w
\longmapsto
\left(
-J_R^{-1}G^{-1}PHE_{\mathcal A}w,
w
\right),
\]

äquivalent zur A3-Koordinate

\[
\xi_w
=
-\mathfrak G_R^{-1}J_R^*HE_{\mathcal A}w.
\]

Für C0 wird diese inverse Formel **nicht** zur Operatoranalyse benutzt; sie dient nur der Bijektionsidentifikation.

---

## 5. C0-Firewall

C0 beweist keine Injektivität.

Es ändert nur die Form der offenen Frage:

\[
\boxed{
\ker\Gamma_I=\{0\}
\iff
\ker\mathscr C_R=\{0\}.
}
\tag{C0.6}
\]

Der Vorteil ist ausschließlich, dass \(\mathscr C_R\) inversefrei und aus den bereits explizit zellweise beschriebenen Operatoren

\[
(I+A)J_R
\qquad\text{und}\qquad
HE_{\mathcal A}
\]

besteht.

Aktueller C0-Status:

\[
\boxed{
\mathrm{A10\!-\!C0}:
\text{AI-GREEN candidate}
}
\]

bis zu einem separaten adversarialen Review der Kompositionskette.

---

# C1 — Proto-Faser-Abgeschlossenheit

## 6. Warum \(N\) noch nicht geraten wird

Für eine spätere Darstellung

\[
L^2(\mathbb T_L;\mathbb C^N)
\]

müssen gleichzeitig berücksichtigt werden:

- freie \(P/\overline Q\)-Sheets;
- Halbperiodenparität;
- physische Liftlagen;
- A9-KNF-Zustände;
- Annulus-\(t\)-Zellen;
- H2-Hubkanäle;
- sämtliche Gate-Grenzen und Kreis-Wraps.

Die bloße Addition bekannter Zahlen wie \(12+11\) oder \(12+19\) wäre **nicht** zulässig. Unterschiedliche affine Signaturen können physisch denselben Fiberzustand darstellen; umgekehrt kann dieselbe formale Signatur auf verschiedenen Gateatomen verschiedene Aktivität besitzen.

Daher wird zunächst nur ein endliches **Proto-Fiber-Alphabet** zertifiziert.

---

## 7. H2-Kanalalphabet

Der vollständige H2-Endledger besitzt

\[
\boxed{11}
\]

Annulus-\(t\)-Zellen und

\[
\boxed{53}
\]

aggregierte nichtverschwindende Kanal-/Zell-Vorkommen.

Jeder Kanal hat die Form

\[
\boxed{
x(t)
=
s\,t+\lambda L+k\Delta,
}
\tag{C1.1}
\]

mit

\[
s\in\{\pm1\},
\qquad
2\lambda\in\mathbb Z,
\qquad
k\in\mathbb Z.
\]

Die 53 Vorkommen reduzieren sich auf exakt

\[
\boxed{19}
\]

verschiedene affine Kanalsignaturen.

Schreibe eindeutig

\[
\lambda=m+\frac{\eta}{2},
\qquad
m\in\mathbb Z,
\quad
\eta\in\{0,1\}.
\]

Dann wird jede Signatur durch die endlichen Daten

\[
\boxed{
(s,\eta,m,k)
}
\tag{C1.2}
\]

beschrieben.

Im H2-Ledger gilt sogar

\[
|m|\le4,
\qquad
|k|\le4.
\]

Damit erscheint neben der einzigen irrationalen Basisphase \(\Delta\) nur endliche Halbperioden-/Liftinformation.

---

## 8. Gemeinsames Affinalphabet von A7, A9 und H2

Aus den 53 H2-Kanälen entstehen innerhalb derselben \(t\)-Zelle

\[
115
\]

free-\(t\)-free-Paarvorkommen und exakt

\[
\boxed{
22
}
\]

verschiedene affine Bridge-Typen:

\[
8
\]

Translationsbeträge und

\[
14
\]

Reflexionen.

Entscheidend für C1:

\[
\boxed{
\mathcal A_{\rm A7}
\subset
\mathcal A_{\rm H2},
}
\tag{C1.3}
\]

und

\[
\boxed{
\mathcal A_{\rm A9,new}
\subset
\mathcal A_{\rm H2}.
}
\tag{C1.4}
\]

Das heißt: **sämtliche bekannten A7-Rohkanten und sämtliche genuin neuen A9-KNF-Affintypen liegen bereits im vollständigen H2-Bridge-Alphabet.**

H2 fügt gegenüber der Vereinigung A7+A9 exakt

\[
\boxed{9}
\]

weitere affine Typen hinzu.

Es existiert daher für die bisher vollständig auditierten A7/A9/H2-Kanäle ein einziges endliches Masteralphabet

\[
\boxed{
\mathcal A_{\rm master}
=
\mathcal A_{\rm H2},
\qquad
|\mathcal A_{\rm master}|=22.
}
\tag{C1.5}
\]

---

## 9. Zertifikat C1-PROTO

Zertifikat:

scripts/certify_sw1_a10_c1_protofiber_closure.py

Commit:

22b2a0095c6ad11434ab4c9b270babcabe41177b

Committed Script-Blob:

03ff488da7a771d0391060146553772dfd5db054

Der exakt committed GitHub-Inhalt wurde ausgeführt.

Ergebnis:

SW1-A10-C1 PROTO-FIBER CLOSURE CERTIFICATE: PASS

Damit ist zulässig:

\[
\boxed{
\mathrm{A10\!-\!C1\!-\!PROTO}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, proto-fiber algebraic scope)}.
}
\]

---

## 10. Was C1-PROTO noch **nicht** beweist

Insbesondere ist noch **nicht** bewiesen:

1. die endgültige physische Fiberdimension \(N\);
2. eine global konstante effektive Dimension auf allen Kreisatomen;
3. Closure nach physischer Quotientierung an sämtlichen Wrap-/Gate-Grenzen;
4. eine Darstellung
   \[
   \mathscr C_R
   =
   \sum_{j=-r}^{r}M_j(x)U_\Delta^j;
   \]
5. Injektivität.

C1-PROTO zeigt nur, dass kein bisher bekannter A7/A9/H2-Kanal eine **neue affine Phasensorte** außerhalb des endlichen Masteralphabets erzeugt.

---

# C1B — nächster zwingender Schritt: gemeinsame feinste Kreispartition

## 11. Partition-Firewall

Vor Bestimmung von \(N\) oder irgendeiner Matrix \(M_j(x)\) muss eine gemeinsame endliche Partition

\[
\boxed{
\mathcal P_{\rm coc}
}
\]

von

\[
\mathbb T_L
\]

konstruiert werden, auf der **alle** folgenden Daten simultan konstant sind:

- Existenz der physischen Liftzustände;
- A9-KNF-Gates;
- H2-Annuluszelltyp;
- sämtliche 19 H2-Kanalsignaturen;
- sämtliche 22 Master-Bridges;
- Kreis-Wrap bei \(L\) und \(2L\);
- Vorbilder aller Gategrenzen unter den auftretenden
  \[
  x\mapsto \pm x+\lambda L+k\Delta.
  \]

Erst auf den Atomen dieser gemeinsamen Verfeinerung darf der physische Zustandssatz quotientiert und gezählt werden.

Der nächste exakte Zielknoten lautet daher:

\[
\boxed{
\mathrm{A10\!-\!C1B}:
\text{gemeinsame Gate-/Wrap-Partition und physische Fiber-Closure}.
}
\]

Danach erst:

\[
\boxed{
\mathrm{A10\!-\!C1C}:
\text{Bestimmung des tatsächlichen Fiber-Rangs }N
\text{ bzw. eines stratified/ambient fibers}.
}
\]

---

## 12. Fourier-Firewall für später

Eine Fourier-Dualisierung ist aussichtsreich, aber erst nach C2 korrekt formulierbar.

Wenn später

\[
(\mathscr Cf)(x)
=
\sum_j M_j(x)f(x+j\Delta)
\]

mit **nichtkonstanten** stückweisen Matrixkoeffizienten \(M_j(x)\) entsteht, diagonalisiert Fourier die Rotation zwar durch die Phasen

\[
e^{2\pi i n\Delta/L},
\]

aber Multiplikation mit \(M_j(x)\) wird im Fourierbild im Allgemeinen zu einer Faltung der Fouriermoden.

Daher entsteht **nicht automatisch** für jedes \(n\) eine voneinander unabhängige endliche Matrixgleichung.

Ein vollständig modeweises endliches Problem tritt nur bei konstanten bzw. hinreichend speziell strukturierten \(M_j\) auf.

Diese Frage wird erst nach der exakten C2-Matrixform entschieden.

---

## 13. Gesamt-Firewall

Der aktive Zielknoten bleibt

\[
\boxed{
\ker\Gamma_I=\{0\}\ ?
}
\]

C0 und C1-PROTO sind ausschließlich Reduktions-/Closure-Schritte.

Keine Aussage über HT-RED, Objekt X oder RH.


---

# C1B0 — endliches gemeinsames Boundary-Alphabet

## 14. Direkte Boundary-Quellen

Für die gemeinsame Kreispartition werden zunächst die bereits zertifizierten direkten Gate-/Zellwände zusammengeführt.

### 14.1 Freie/source-seitige Wände

Aus A0/A1/A7/A9 ergibt sich ein endlicher Satz von

\[
\boxed{19}
\]

freien/source-seitigen Wandformen, darunter insbesondere:

\[
0,\ \varepsilon,\ a-\varepsilon,\ a+\varepsilon,\ 2d-\varepsilon,\ T-\varepsilon,
\]

\[
\sigma,\ e+\sigma,\ a+\sigma,
\]

\[
a\pm R,\ b\pm R,\ T\pm R,
\]

sowie die Zentren/Horizontwände

\[
a,\ b,\ T,\ T+\varepsilon.
\]

### 14.2 Annulus-\(t\)-Wände

Der H2-Ledger besitzt exakt

\[
\boxed{12}
\]

direkte \(t\)-Wände:

\[
R,\ \varepsilon,\ e+\varepsilon,\ d,\ d+R,\ a,\ a+R,\ a+\varepsilon,
\]

\[
b,\ T-R,\ T,\ T+\sigma.
\]

Die direkte Vereinigung beider Quellen besitzt

\[
\boxed{24}
\]

verschiedene symbolische Wandformen.

---

## 15. Vollständiger Pullback unter dem bekannten Operatoralphabet

Für simultane Stückweise-Konstanz genügt es nicht, nur die direkten Wände zu schneiden.

Wenn ein freier Operatorzweig

\[
x\mapsto \phi(x)
\]

aktiv ist, muss zusätzlich bekannt sein, wann sein Ziel eine andere physische/Gate-Zelle betritt. Deshalb werden die freien Wände unter allen gerichteten Master-Affintypen zurückgezogen.

Ebenso wird für jeden H2-Kanal

\[
x(t)=s\,t+\lambda L+k\Delta
\]

jede freie Wand nach \(t\) zurückgezogen.

Verwendet werden exakt:

- die \(22\) Master-Affintypen aus C1-PROTO;
- die \(19\) verschiedenen H2-Kanalsignaturen.

Die vollständige Enumeration ist **kein Scan durch alle grob möglichen Koeffiziententupel**.

Sie erzeugt mit Multiplizität exakt

\[
\boxed{
955
=
24
+
8\cdot2\cdot19
+
14\cdot19
+
19\cdot19
}
\]

Vorkommen:

- \(24\) direkte Wandformen;
- \(8\) Translationstypen, beide Richtungen, auf \(19\) freien Wänden;
- \(14\) Reflexionstypen auf \(19\) freien Wänden;
- \(19\) H2-Kanalsignaturen auf \(19\) freien Wänden.

Erst nach exakter Deduplikation dieser **vollständig generierten** Vorkommen bleiben

\[
\boxed{195}
\]

verschiedene symbolische Formen.

Die Zahl

\[
2\cdot9\cdot3^3=486
\]

ist lediglich die Größe einer groben Koeffizientenbox, die aus den späteren Maximalabschätzungen konstruiert werden könnte. Sie ist **nicht** der Enumerationsraum und erzeugt daher keine „291 ungeklärten Ausschlüsse“.

Modulo \(L\) reduzieren sich diese auf

\[
\boxed{92}
\]

symbolische Kreisgrenzen.

---

## 16. Struktur aller 92 Kreisgrenzen

Jede der 92 Formen besitzt die Gestalt

\[
\boxed{
\theta
=
\frac{\eta}{2}L
+
k\Delta
+
\rho R
+
\mu\varepsilon
+
\nu\sigma
\pmod L,
}
\tag{C1B.1}
\]

mit

\[
\eta\in\{0,1\},
\qquad
|k|\le4,
\]

und

\[
\rho,\mu,\nu\in\{-1,0,1\}.
\]

Damit ist bereits bewiesen:

> Für die bisher vollständig auditierten A0/A1/A7/A9/H2-Operatorzweige existiert ein **endliches symbolisches Boundary-Alphabet auf \(\mathbb T_L\)**, das alle direkten Wände und alle one-step relevanten Pullbacks enthält.

Es tritt keine zusätzliche irrationale Phase auf.

---

## 17. Zertifikat C1B0

Zertifikat:

scripts/certify_sw1_a10_c1b_boundary_alphabet.py

Commit:

622432d0b7a579d73f076aee33ea9f7ac8f5916f

Committed Script-Blob:

15146ac9b887ec34ce328a56d07dbdfb59a2456c

Der exakt committed GitHub-Inhalt wurde ausgeführt.

Ergebnis:

SW1-A10-C1B COMMON BOUNDARY-ALPHABET CERTIFICATE: PASS

Damit ist zulässig:

\[
\boxed{
\mathrm{A10\!-\!C1B0}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, boundary-alphabet scope)}.
}
\]

---

## 18. Warum dies noch nicht die fertige Partition ist

Die \(92\) Formen sind ein **symbolisches Alphabet**, noch keine universell sortierte Folge von 92 verschiedenen Punkten.

Je nach zulässigen Parametern können:

1. zwei Formen zusammenfallen;
2. ihre Ordnung wechseln;
3. einzelne Formen an \(0\pmod L\) wrappen.

Daher muss vor Bestimmung der tatsächlichen Atome die Parameterregion selbst nach sämtlichen möglichen Gleichheitswänden

\[
\theta_i=\theta_j\pmod L
\]

stratifiziert werden.

Der nächste Knoten lautet deshalb präziser:

\[
\boxed{
\mathrm{A10\!-\!C1B1}:
\text{Kollisions-/Ordnungsstratifizierung der 92 Boundary-Signaturen}.
}
\]

Erst danach kann auf jedem Parameterstratum der physische Fiberzustandsraum geschlossen und sein Rang bestimmt werden.

---

## 19. C1B0-Firewall

C1B0 beweist **nicht**:

- dass alle 92 Formen für jeden Parameterwert verschieden sind;
- dass es stets 92 Kreisatome gibt;
- dass die effektive Fiberdimension global konstant ist;
- die Matrixdarstellung C2;
- Injektivität.

Es beweist nur die **endliche Exhaustivität des benötigten Boundary-Alphabets**.


---

# C1B1 — exakte Kollisionshyperflächen im kleinen unteren Subchamber

## 20. Warum \(\Delta/L\notin\mathbb Q\) hier **nicht** \(k'=0\) erzwingt

Für zwei Boundary-Signaturen besitzt eine Kollisionsgleichung modulo \(L\) die Form

\[
qL
+
k\Delta
+
\rho R
+
\mu\varepsilon
+
\nu\sigma
=
0.
\tag{C1B1.1}
\]

Obwohl

\[
\Delta/L\notin\mathbb Q,
\]

sind

\[
R,\varepsilon,\sigma
\]

freie reelle Parameter im SW1-Keil. Daher können ihre linearen Kombinationen einen nichtverschwindenden \(\Delta\)-Term kompensieren.

Eine Reduktion

\[
k\ne0\Longrightarrow\text{unmöglich}
\]

wäre nur unter einer zusätzlichen algebraischen Unabhängigkeitsannahme über die Parameter zulässig. Eine solche Annahme existiert hier **nicht**.

Die vollständige exakte Enumeration bestätigt sogar, dass genuine Kollisionsflächen mit nichtverschwindendem \(\Delta\)-Koeffizienten tatsächlich im zulässigen Chamber auftreten.

---

## 21. Parameterregion

Für H3/C1 betrachten wir den kleinen unteren Subchamber

\[
\boxed{
0<\sigma\le R<\varepsilon<\varepsilon_*,
\qquad
\varepsilon_*:=\frac{6\Delta-L}{4}.
}
\tag{C1B1.2}
\]

Wegen

\[
\varepsilon_*<\Delta/2
\]

liegt dieser vollständig im bisherigen unteren SW1-Chamber.

---

## 22. Von 92 Boundary-Signaturen zu allen Kollisionsgleichungen

Aus den

\[
92
\]

symbolischen Kreisgrenzen entstehen

\[
\binom{92}{2}
=
\boxed{4186}
\]

ungeordnete Boundary-Paare.

Nach Deduplikation bleiben

\[
\boxed{463}
\]

verschiedene rohe Differenzsignaturen.

Für die nicht-\(L\)-Terme gilt uniform:

\[
|k|\le8
\]

und wegen

\[
|\rho|,|\mu|,|\nu|\le2,
\qquad
0<\sigma\le R<\varepsilon<\varepsilon_*,
\]

\[
|\rho R+\mu\varepsilon+\nu\sigma|
<
6\varepsilon_*.
\]

Ferner gilt exakt

\[
2L
>
8\Delta+6\varepsilon_*,
\]

denn

\[
2L-(8\Delta+6\varepsilon_*)
=
\frac{7L-34\Delta}{2}
>0.
\]

Damit können Kollisionsgleichungen mit

\[
|q|\ge2
\]

exakt ausgeschlossen werden.

Nach Kreis-Wrap und Vorzeichenkanonisierung bleiben

\[
\boxed{1087}
\]

verschiedene kanonische Kollisionsgleichungen.

---

## 23. Exakte Keilprüfung

Der Abschluss der Parameterregion ist der Ordnungssimplex

\[
0\le\sigma\le R\le\varepsilon\le\varepsilon_*.
\]

Für die lineare Parameterform

\[
\ell(R,\varepsilon,\sigma)
=
\rho R+\mu\varepsilon+\nu\sigma
\]

liegen alle Extremwerte auf den vier Simplex-Ecken. Daher genügt exakt die endliche Liste

\[
0,\quad
\mu\varepsilon_*,
\quad
(\rho+\mu)\varepsilon_*,
\quad
(\rho+\mu+\nu)\varepsilon_*.
\]

Damit werden alle 1087 Gleichungen ohne numerischen Scan klassifiziert.

Ergebnis:

\[
\boxed{1051}
\]

schneiden nicht einmal den abgeschlossenen Parameterkeil.

Weitere

\[
\boxed{18}
\]

treffen nur dessen Rand.

Genau eine dieser Randgleichungen ist im SW1-Scope erlaubt:

\[
\boxed{\sigma=R.}
\]

Die übrigen 17 erzwingen entweder

- einen Nullparameter;
- eine durch \(R<\varepsilon\) ausgeschlossene Ordnungsdegeneration;
- oder die ausgeschlossene obere Wand
  \[
  \varepsilon=\varepsilon_*.
  \]

Schließlich schneiden exakt

\[
\boxed{18}
\]

Kollisionshyperflächen das **strikte Chamberinnere**.

---

## 24. Familie A — sechs \(s_*\)-Flächen

Setze

\[
\boxed{
s_*:=\frac L2-2\Delta>0.
}
\]

Die erste genuine Familie lautet

\[
\boxed{
s_*
\in
\{
2R,\,
R+\varepsilon,\,
R+\sigma,\,
2\varepsilon,\,
\varepsilon+\sigma,\,
2\sigma
\}.
}
\tag{C1B1.3}
\]

Dies sind sechs verschiedene im Chamber realisierbare Kollisionshyperflächen.

Ihre kanonischen Gleichungen besitzen

\[
q=\frac12,
\qquad
k=-2,
\]

also ausdrücklich einen nichtverschwindenden \(\Delta\)-Anteil.

---

## 25. Familie B — zwölf \(\chi\)-Flächen

Setze

\[
\boxed{
\chi:=5\Delta-L>0.
}
\]

Die zweite genuine Familie lautet

\[
\boxed{
\chi
\in
\{
\varepsilon-R,\,
\sigma,\,
2\sigma,\,
\varepsilon-\sigma,\,
\varepsilon,\,
\varepsilon+\sigma,\,
2\varepsilon,
}
\]

\[
\boxed{
R-\sigma,\,
R,\,
R+\sigma,\,
R+\varepsilon,\,
2R
\}.
}
\tag{C1B1.4}
\]

Dies sind zwölf weitere im Chamber realisierbare Kollisionshyperflächen.

Ihre kanonische Konstantenseite stammt aus

\[
q=1,
\qquad
k=-5,
\]

also wiederum aus einer genuine \(L/\Delta\)-Mischung.

---

## 26. Vollständiger aktueller Kollisionsledger

Im für H3 relevanten kleinen unteren Parameterbereich ist die gesamte Boundary-Kollisionsgeometrie damit auf

\[
\boxed{
18\text{ innere Hyperflächen}
+
1\text{ erlaubte Randfläche }(\sigma=R)
}
\]

reduziert.

Dies ist eine sehr viel kleinere Stratifizierungsaufgabe als ein naiver \(92\times92\)-Vergleich.

---

## 27. Zertifikat C1B1

Zertifikat:

scripts/certify_sw1_a10_c1b1_collision_strata.py

Commit:

9efac30808cea8072878af43dcc94c72be145949

Committed Script-Blob:

76c4d07e0e0228fadf7cd460c72bd4609dd0258e

Der exakt committed GitHub-Inhalt wurde rekonstruiert, nach dem Git-Blob-Verfahren gehasht und ausgeführt.

Ergebnis:

SW1-A10-C1B1 COLLISION-STRATIFICATION CERTIFICATE: PASS

Damit ist zulässig:

\[
\boxed{
\mathrm{A10\!-\!C1B1}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, collision-strata scope)}.
}
\]

---

## 28. Nächster Knoten C1B2

C1B1 klassifiziert **wo Grenzen kollidieren**, aber noch nicht die vollständige Reihenfolge der 92 Grenzen in jedem offenen Parameterstratum.

Der nächste exakte Schritt ist daher:

\[
\boxed{
\mathrm{A10\!-\!C1B2}:
\text{Hyperflächen-Arrangement und Boundary-Order pro Parameterstratum}.
}
\]

Erst danach darf

\[
N
\]

bestimmt beziehungsweise ein konstanter Ambient-Fiber gewählt werden.

### Firewall

C1B1 beweist keine Atomzahl, keine Fiberdimension, keine Matrixdarstellung und keine Injektivität.


---

# C1B2A — exakte Arrangementkammerzahl am rationalen Referenzwert

## 29. Normierung durch \(\chi\)

Setze

\[
s_*:=\frac L2-2\Delta,
\qquad
\chi:=5\Delta-L.
\]

Aus diesen beiden Konstanten folgen exakt

\[
\boxed{
\Delta=\chi+2s_*,
\qquad
L=4\chi+10s_*,
}
\tag{C1B2.1}
\]

und

\[
\boxed{
\varepsilon_*=\frac{s_*+\chi}{2}.
}
\tag{C1B2.2}
\]

Definiere das dimensionslose Verhältnis

\[
\boxed{
r:=\frac{s_*}{\chi}.
}
\]

Die bereits in C1B1 verwendete Ungleichung

\[
7L-34\Delta>0
\]

ist äquivalent zu

\[
s_*>3\chi.
\]

Ferner gilt exakt

\[
4\chi-s_*
=
\frac{44\Delta-9L}{2}>0.
\]

In Primzahlform reduziert sich die letzte Positivität auf

\[
3^{53}>2^{84}.
\]

Damit

\[
\boxed{
3<r<4.
}
\tag{C1B2.3}
\]

---

## 30. Normiertes 18-Ebenen-Arrangement

Nach Division der Parameter durch \(\chi\) lautet der offene Parameterkeil

\[
0<\sigma<R<\varepsilon<\frac{r+1}{2}.
\]

Die sechs \(s_*\)-Ebenen werden zu Ebenen mit rechter Seite \(r\):

\[
2R=r,\quad
R+\varepsilon=r,\quad
R+\sigma=r,\quad
2\varepsilon=r,\quad
\varepsilon+\sigma=r,\quad
2\sigma=r.
\]

Die zwölf \(\chi\)-Ebenen besitzen rechte Seite \(1\):

\[
\varepsilon-R=1,\quad
\sigma=1,\quad
2\sigma=1,\quad
\varepsilon-\sigma=1,
\]

\[
\varepsilon=1,\quad
\varepsilon+\sigma=1,\quad
2\varepsilon=1,\quad
R-\sigma=1,
\]

\[
R=1,\quad
R+\sigma=1,\quad
R+\varepsilon=1,\quad
2R=1.
\]

---

## 31. Alle möglichen kombinatorischen Degenerationswerte

Um die Kammerzahl nicht numerisch zu extrapolieren, werden zusätzlich die vier Simplexfacetten

\[
\sigma=0,\qquad
R=\sigma,\qquad
\varepsilon=R,\qquad
\varepsilon=\frac{r+1}{2}
\]

in die Inzidenzanalyse aufgenommen.

Da sämtliche Ebenennormalen unabhängig von \(r\) sind, kann sich die kombinatorische Struktur nur ändern, wenn ein zuvor inkonsistentes abhängiges Teilssystem von bis zu vier Ebenen konsistent wird: Parallel-/Koinzidenz-, Linien-, Punkt-, Rand- oder Tangentialdegeneration.

Die vollständige exakte Enumeration ergibt die kritische Menge

\[
\boxed{
\left\{
-3,-2,-1,-\frac12,0,\frac13,\frac12,\frac23,1,
\frac43,\frac32,2,\frac52,3,4,5,6
\right\}.
}
\tag{C1B2.4}
\]

Insbesondere:

\[
\boxed{
(3,4)\cap\mathcal R_{\rm crit}=\varnothing.
}
\tag{C1B2.5}
\]

---

## 32. Exakte Kammerzahl bei \(r_0=7/2\)

Wähle den rationalen Referenzwert

\[
\boxed{
r_0=\frac72.
}
\]

Nach Normierung \(\chi=1\) gilt dann

\[
\Delta=1+2r_0=8,
\qquad
L=4+10r_0=39,
\]

und

\[
\varepsilon_*=\frac{r_0+1}{2}=\frac94.
\]

Für dieses vollständig rationale Arrangement wird die Kammerzahl exakt durch sukzessive Ebenenschnitte gezählt.

Wenn die 18 Ebenen in der C1B1-Reihenfolge eingefügt werden, lauten die exakten 2D-Schnittregionenzahlen

\[
\boxed{
1,1,1,1,2,1,2,5,6,8,2,1,1,9,9,6,1,6.
}
\]

Mit der anfänglichen ungeschnittenen Simplexkammer ergibt sich

\[
\boxed{
N_{\rm chamber}(r_0)=64.
}
\tag{C1B2.6}
\]

Die Rechnung verwendet ausschließlich rationale lineare Algebra: aktive Schnittlinien werden als exakte RREF-Systeme dedupliziert, ihre Simplex-Innenaktivität exakt geprüft und konkurrente Schnittpunkte nur einmal gezählt.

---

## 33. Zertifikat C1B2A

Zertifikat:

scripts/certify_sw1_a10_c1b2a_arrangement.py

Commit:

812b9cfbe32e71352ddc33256d021bf008c93ed1

Committed Script-Blob:

6c412820b564caeb13913111d7ef11277e58967a

Der Dateiinhalt wurde **vor** dem Commit exakt ausgeführt; GitHub meldete danach denselben Git-Blob-SHA.

Ergebnis:

SW1-A10-C1B2A HYPERPLANE-ARRANGEMENT CERTIFICATE: PASS

Damit ist im engen Zertifikatsscope zulässig:

\[
\boxed{
\mathrm{A10\!-\!C1B2A\!-\!ALG}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

für

1. \(3<r<4\);
2. die vollständige kritische \(r\)-Menge;
3. das Fehlen kritischer Werte in \((3,4)\);
4. die exakte Referenzkammerzahl \(64\) bei \(r_0=7/2\).

### 33.1 Noch separat sichtbarer Transfer-Schritt

Der Schluss

\[
N_{\rm chamber}(r)=64
\qquad
\text{für unser tatsächliches }r\in(3,4)
\]

verwendet zusätzlich das Standardlemma für stetige affine Hyperflächenarrangements:

> Solange bei einer stetigen Variation der Offsets keine Parallel-/Koinzidenz-, Inzidenz-, Tangential- oder Randdegeneration auftritt, bleibt der kombinatorische Typ des durch einen konvexen Polytope geschnittenen Arrangements konstant.

C1B2A hat **alle** hierfür relevanten kritischen Werte enumeriert und zeigt, dass zwischen \(r_0\) und dem tatsächlichen \(r\) keiner liegt.

Dieser Isotopieschluss wird vor einer unabhängigen Gegenprüfung bewusst als

\[
\boxed{
\mathrm{A10\!-\!C1B2A\!-\!TRANSFER}:
\text{AI-GREEN candidate}
}
\]

geführt.

---

# C1B2B — vollständiger Boundary-Order-Ledger am Referenzarrangement

## 34. 64 exakte Kammerrepräsentanten

Für \(r_0=7/2\) wurden

\[
\boxed{64}
\]

rationale Punkte

\[
(\sigma,R,\varepsilon)
\]

im offenen Simplex konstruiert.

Für jeden Repräsentanten werden die Vorzeichen aller 18 Kollisionshyperflächen exakt geprüft.

Die 64 Punkte erzeugen

\[
\boxed{64}
\]

verschiedene 18-Bit-Signmuster.

Da C1B2A bereits exakt beweist, dass das Referenzarrangement insgesamt nur 64 offene Kammern besitzt, ist die Repräsentantenliste exhaustiv:

\[
\boxed{
\text{genau ein verifizierter Repräsentant pro Referenzkammer}.
}
\]

---

## 35. Exakte Kreisordnung aller 92 Boundary-Signaturen

Bei

\[
r_0=\frac72,\qquad
\chi=1
\]

gilt

\[
L=39,\qquad
\Delta=8.
\]

Damit besitzt jede der 92 C1B0-Signaturen an jedem rationalen Kammerrepräsentanten einen **rationalen** Kreiswert modulo \(39\).

Das Zertifikat:

1. rekonstruiert die 92 Signaturen direkt aus dem vollständigen C1B0-Generationsschema;
2. wertet sie an jedem der 64 Repräsentanten exakt aus;
3. beweist, dass innerhalb jeder offenen Kammer alle 92 Werte paarweise verschieden sind;
4. sortiert sie exakt auf
   \[
   [0,39);
   \]
5. erhält
   \[
   \boxed{64}
   \]
   verschiedene vollständige Kreisordnungen.

Der deterministische Gesamtledger besitzt SHA-256

\[
\boxed{
\texttt{d1a9767f147b405980d8f9989752a5b90f1fa0bc78ef0a73de2878248d928ba2}.
}
\]

---

## 36. Zertifikat C1B2B

Zertifikat:

scripts/certify_sw1_a10_c1b2b_chamber_orders.py

Commit:

f6c04fd4c8b9fb94160e5c5d8b2030dbf54a055a

Committed Script-Blob:

76dae2ee56bde14cbf64eb2bd7cb0d447c8e6f5c

Der Dateiinhalt wurde **vor** dem Commit exakt ausgeführt; GitHub meldete danach denselben Git-Blob-SHA.

Ergebnis:

SW1-A10-C1B2B CHAMBER-ORDER LEDGER CERTIFICATE: PASS

Damit:

\[
\boxed{
\mathrm{A10\!-\!C1B2B}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, reference-order scope)}.
}
\]

---

## 37. Aktuelle C1B2-Firewall

Jetzt ist exakt bekannt:

- die gesamte kritische \(r\)-Menge;
- die Referenzkammerzahl \(64\);
- ein exhaustiver rationaler Repräsentantensatz;
- die vollständige Kreisordnung aller 92 Boundary-Labels in jeder Referenzkammer.

Noch offen:

1. unabhängiger Review des No-Degeneracy-Isotopie-Transfers auf das tatsächliche \(r\);
2. Kollisionsklassen der 92 Labels **auf** jeder der 18 Hyperflächen;
3. mögliche Mehrfachkollisionen an Hyperflächenschnitten;
4. finales physisches Fiber-\(N\).

Der nächste finite Knoten ist deshalb

\[
\boxed{
\mathrm{A10\!-\!C1B2C}:
\text{Boundary-Kollisionsklassen auf den 18 Ebenen und ihren Schnittstrata}.
}
\]

Keine Matrix- oder Injektivitätsaussage.


---

# C1B2C — höhere Degenerationen und Boundary-Kollisionsklassen

## 38. Retrospektiver Vollständigkeitscheck für \(\mathcal R_{\rm crit}\)

Der Einwand, dass eine Kammeränderung nicht nur durch paarweise Parallelität/Kollision, sondern auch durch höhere Mehrfachinzidenzen ausgelöst werden kann, ist korrekt.

Deshalb wird die kritische \(r\)-Menge nochmals unabhängig auf Arrangementebene geprüft.

Verwendet werden sämtliche

\[
18
\]

inneren Kollisionshyperflächen sowie die vier Simplexfacetten

\[
\sigma=0,\qquad
R=\sigma,\qquad
\varepsilon=R,\qquad
\varepsilon=\frac{r+1}{2}.
\]

In Dimension \(3\) besitzt jeder minimale affine Konsistenz-/Inzidenzzeuge höchstens

\[
3+1=4
\]

Gleichungen. Daher genügt es exhaustiv, alle abhängigen Teilmengen der Größen

\[
2,\quad3,\quad4
\]

zu untersuchen.

Die exakte Enumeration ergibt:

\[
\boxed{
12
}
\]

parameterabhängige Zeugen bei Größe \(2\),

\[
\boxed{
359
}
\]

bei Größe \(3\),

und

\[
\boxed{
3841
}
\]

bei Größe \(4\).

Die zugehörigen kritischen Mengen besitzen Größen

\[
|\mathcal R_2|=3,\qquad
|\mathcal R_3|=8,\qquad
|\mathcal R_4|=17.
\]

Ihre Vereinigung ist **exakt** die bereits in C1B2A gefundene 17-Werte-Menge

\[
\boxed{
\mathcal R_{\rm crit}
=
\left\{
-3,-2,-1,-\frac12,0,\frac13,\frac12,\frac23,1,
\frac43,\frac32,2,\frac52,3,4,5,6
\right\}.
}
\]

Wichtig:

\[
\boxed{
|\mathcal R_4\setminus(\mathcal R_2\cup\mathcal R_3)|=9.
}
\]

Diese neun Werte sind

\[
\boxed{
-3,-2,-\frac12,\frac13,\frac23,\frac43,\frac52,5,6.
}
\]

Damit ist explizit bestätigt:

> Eine bloße Paar-/Tripelprüfung wäre **nicht** vollständig gewesen. Die 4-Ebenen-Prüfung ist mathematisch notwendig und wurde tatsächlich durchgeführt.

Insbesondere bleibt

\[
\boxed{
(3,4)\cap\mathcal R_{\rm crit}=\varnothing.
}
\]

---

## 39. Welche Boundary-Labels kollidieren auf den 18 Ebenen?

Die 92 C1B0-Boundary-Signaturen werden vollständig rekonstruiert.

Für jede der 18 genuine Kollisionsgleichungen werden sämtliche ungeordneten Labelpaare

\[
(i,j),\qquad 0\le i<j<92,
\]

bestimmt, deren Kreiswerte auf genau dieser Parameterhyperfläche zusammenfallen.

Die exakten Paarzahlen pro Ebene in der C1B1-Reihenfolge lauten:

\[
\boxed{
10,19,15,9,14,5,\;
8,8,4,3,8,8,4,3,8,8,8,4.
}
\tag{C1B2C.1}
\]

Auf **jeder einzelnen inneren Ebene** bestehen die transitiven Boundary-Kollisionsklassen ausschließlich aus Zweierklassen.

Es gibt also generisch auf einer einzelnen inneren Hyperfläche keine Dreier- oder größere Boundary-Identifikation.

---

## 40. Schnittstrata im offenen 3D-Simplex

Beim rationalen Referenzwert

\[
r_0=\frac72
\]

besitzt das 18-Ebenen-Arrangement im offenen Simplex exakt

\[
\boxed{35}
\]

verschiedene Codimension-2-Schnittlinien.

Jede dieser Linien liegt auf **genau zwei** der 18 Hyperflächen:

\[
\boxed{
\text{Linien-Multiplizität}=2\quad\text{für alle 35 Linien}.
}
\]

Ferner existieren exakt

\[
\boxed{10}
\]

innere Codimension-3-Schnittpunkte.

Jeder dieser Punkte liegt auf **genau drei** der 18 Hyperflächen:

\[
\boxed{
\text{Punkt-Multiplizität}=3\quad\text{für alle 10 Punkte}.
}
\]

Insbesondere gibt es im offenen Referenzsimplex:

- keine Vierfachlinie;
- keinen Vierfach- oder höheren inneren Punkt.

### 40.1 Boundary-Klassen auf den Schnittstrata

Für jede der 35 Linien werden die Paarrelationen beider aktiver Hyperflächen vereinigt und transitiv abgeschlossen.

Für jeden der 10 Punkte werden entsprechend die Paarrelationen aller drei aktiven Hyperflächen vereinigt.

Ergebnis:

\[
\boxed{
\text{Auf allen 35 inneren Linien und allen 10 inneren Punkten bleiben sämtliche Boundary-Kollisionsklassen Größe }2.
}
\tag{C1B2C.2}
\]

Das ist ein starker Vereinfachungsbefund:

> Im **offenen** 3D-Parameterchamber entstehen trotz Mehrfachschnitten keine transitiven Dreier- oder größeren Boundary-Quotienten.

---

## 41. Die erlaubte Randfläche \(\sigma=R\) ist qualitativ anders

C1B1 hatte bereits gezeigt, dass von den closure-only Kollisionsgleichungen genau

\[
\boxed{\sigma=R}
\]

im SW1-Scope erlaubt ist.

Die Gleichung \(R-\sigma=0\) erzeugt selbst

\[
\boxed{23}
\]

generische Boundary-Paarkollisionen.

Auf einem generischen Punkt dieser Randfläche sind auch diese Klassen zunächst nur Zweierklassen.

### 41.1 Schnittlinien auf \(\sigma=R\)

Von den 18 inneren Hyperflächen schneiden exakt

\[
\boxed{17}
\]

die relative innere Fläche

\[
0<\sigma=R<\varepsilon<\varepsilon_*.
\]

Die einzige fehlende Ebene ist die genuine Gleichung

\[
\chi=R-\sigma,
\]

die auf \(\sigma=R\) wegen \(\chi>0\) unmöglich ist.

Nach Vereinigung der Randflächen-Kollisionen mit der jeweils aktiven inneren Hyperfläche besitzen die 17 Face-Lines maximale Boundary-Klassengrößen

\[
\boxed{
4,3,4,2,3,4,3,3,4,3,2,3,2,3,4,3,4.
}
\tag{C1B2C.3}
\]

Damit:

- 3 Face-Lines haben maximale Klasse \(2\);
- 8 Face-Lines maximale Klasse \(3\);
- 6 Face-Lines maximale Klasse \(4\).

### 41.2 Innere Schnittpunkte auf \(\sigma=R\)

Auf der relativen inneren Randfläche existieren exakt

\[
\boxed{6}
\]

Mehrfachschnittpunkte.

Die Zahl zusätzlich aktiver innerer Hyperflächen besitzt die Verteilung

\[
\boxed{
3:2,\qquad
4:3,\qquad
5:1.
}
\]

Die sechs Punkte sind im normierten Referenzsimplex exakt:

\[
\left(\frac12,\frac12,1\right),
\quad
\left(\frac12,\frac12,\frac32\right),
\quad
\left(\frac12,\frac12,\frac74\right),
\]

\[
\left(\frac34,\frac34,\frac74\right),
\quad
\left(1,1,\frac74\right),
\quad
(1,1,2).
\]

Die maximalen Boundary-Klassengrößen an diesen sechs Punkten lauten:

\[
\boxed{
4,4,4,3,3,3.
}
\tag{C1B2C.4}
\]

Damit ist erstmals exakt sichtbar:

> Größere Boundary-Quotientklassen entstehen in dieser Referenzstratifizierung **nicht im offenen 3D-Chamber**, sondern auf der zugelassenen Randfläche \(\sigma=R\).

---

## 42. Zertifikat C1B2C

Zertifikat:

scripts/certify_sw1_a10_c1b2c_collision_classes.py

Commit:

d1c4cd040958810958e2e77b885b57d55fe3532e

Committed Script-Blob:

af09075bdf8f81e5d02ebd99e80d3f2ede564064

Der committed GitHub-Blob wurde bytegenau lokal rekonstruiert:

\[
\texttt{git hash-object}
=
\texttt{af09075bdf8f81e5d02ebd99e80d3f2ede564064}.
\]

Exakt dieser Inhalt wurde ausgeführt.

Ergebnis:

SW1-A10-C1B2C HIGHER-DEGENERACY / COLLISION-STRATA CERTIFICATE: PASS

Damit ist zulässig:

\[
\boxed{
\mathrm{A10\!-\!C1B2C}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, reference-strata scope)}.
}
\]

---

## 43. Bedeutung für den Isotopie-Transfer

C1B2C liefert zwei retrospektive Stützen für C1B2A-TRANSFER:

1. die kritische \(r\)-Menge wurde tatsächlich mit allen minimal nötigen höheren Degenerationen bis Größe \(4\) erzeugt;
2. das vollständige Referenz-Schnittlattice wurde explizit berechnet.

Da

\[
(3,4)\cap\mathcal R_{\rm crit}=\varnothing,
\]

gibt es zwischen

\[
r_0=\frac72
\]

und dem tatsächlichen Projektwert keine neu auftretende oder verschwindende minimal affine Degeneration.

Trotzdem bleibt der formale Schluss

\[
\text{Referenz-Lattice}
\longrightarrow
\text{tatsächliches Projekt-Lattice}
\]

bis zu einem unabhängigen Review weiterhin separat als

\[
\boxed{
\mathrm{A10\!-\!C1B2\!-\!TRANSFER}:
\text{AI-GREEN candidate}.
}
\]

---

## 44. Korrektur der Interpretation von C1B2C

C1B2C klassifiziert **Boundary-Signaturen der gemeinsamen Gate-/Zellpartition**.

Die 92 C1B0-Labels sind daher keine Hilbert-Fiberkoordinaten.

Insbesondere bedeutet eine transitive Boundary-Klasse der Größe

\[
3
\quad\text{oder}\quad
4
\]

auf

\[
\sigma=R
\]

nur:

> Mehrere symbolische Partitionierungswände liegen am selben Kreispunkt.

Daraus folgt **nicht**, dass drei oder vier Funktionszustände zu einer Fiberkoordinate quotientiert werden.

Die frühere Interpretation

\[
\text{Boundary-Kollision}
\Longrightarrow
\text{Änderung der effektiven Fiberdimension}
\]

war zu stark und wird hiermit ausdrücklich verworfen.

C1B2C bleibt als Arrangement-/Partitionsergebnis vollständig gültig; korrigiert wird nur seine Interpretation für die Hilbert-Fiberisierung.

---

# C1C0 — formaler konstanter Ambient-Cover

## 45. Drei verschiedene Objektarten

Vor jeder Buchung eines Fiber-\(N\) müssen drei Ebenen getrennt werden.

### 45.1 Boundary-Signaturen

Die 92 C1B0-Labels sind **Wände der gemeinsamen stückweisen Partition**.

Sie bestimmen, wo Gate-/Lift-/Wrap-Formeln wechseln.

Sie sind keine unabhängigen Funktionskoordinaten.

### 45.2 Operatorzweige

Die 19 H2-Kanalsignaturen und die 22 affine Mastertypen beschreiben **Abbildungen zwischen Zuständen**.

Auch sie sind keine zusätzlichen Fiberkoordinaten.

### 45.3 Formale Orbit-Cover-Zustände

A9 verwendet dagegen die diskrete Zustandsmenge

\[
\boxed{
\mathscr S_{\rm free}^{\rm form}
=
\{P,\overline Q\}
\times
\{0,1\}_{\rm parity}
\times
\{0,1,2\}_{\rm lift}.
}
\tag{C1C0.1}
\]

Damit

\[
\boxed{
|\mathscr S_{\rm free}^{\rm form}|=2\cdot2\cdot3=12.
}
\tag{C1C0.2}
\]

Diese 12 Objekte sind zunächst **formale Mehrblatt-Cover-Slots**.

Sie dürfen noch nicht ohne analytisches Fiberisierungslemma als 12 unabhängige Hilbert-Fiberkoordinaten bezeichnet werden.

---

## 46. Drei positive Annulus-Lifts

Im kleinen unteren Chamber gilt

\[
S=T+\sigma<T+\varepsilon=T_0.
\]

Aus C1B2 folgt nach Normierung

\[
L=4+10r,
\qquad
\Delta=1+2r,
\qquad
\varepsilon_*=\frac{r+1}{2},
\qquad
3<r<4.
\]

Ferner

\[
T=2L+2\Delta.
\]

Daher

\[
3L-(T+\varepsilon_*)
=
\frac{3+11r}{2}
>0.
\]

Also

\[
\boxed{
S<T_0<3L.
}
\tag{C1C0.3}
\]

Nach positiver Odd-Faltung besitzt eine Annulusrestklasse modulo \(L\) somit höchstens drei physische Lifts.

Definiere formal

\[
\boxed{
\mathscr S_w^{\rm form}
=
\{W_0,W_1,W_2\},
}
\]

also

\[
\boxed{
|\mathscr S_w^{\rm form}|=3.
}
\tag{C1C0.4}
\]

---

## 47. H2 schließt auf denselben vier Sheet/Parity-Spezies

Jede der 19 H2-Kanalsignaturen besitzt die Form

\[
x(t)
=
s\,t+\frac{\ell}{2}L+k\Delta,
\qquad
s\in\{\pm1\}.
\tag{C1C0.5}
\]

Schreibe eindeutig

\[
\ell=2m+\eta,
\qquad
\eta\in\{0,1\}.
\]

### 47.1 Positiver Slope

Für

\[
s=+1
\]

ist der Kanal modulo \(L\) ein \(P\)-Zustand mit Parität \(\eta\) und lokalem Basisindex

\[
j=k.
\]

### 47.2 Negativer Slope

Für

\[
s=-1
\]

verwenden wir

\[
\overline Q_{j,\eta}
\equiv
-t+(4-j)\Delta+\frac{\eta}{2}L
\pmod L.
\]

Daher gilt

\[
j=4-k.
\]

Die vollständige 19-Signaturen-Liste trifft exakt die vier Spezies

\[
\boxed{
(P,0),\ (P,1),\ (\overline Q,0),\ (\overline Q,1).
}
\tag{C1C0.6}
\]

Es ist kein fünftes Sheet und keine weitere Parität erforderlich.

---

## 48. Direkte H2-Reichweite im inversefreien Operator

Für alle 19 direkten \(w\to\)physisch-Kanalsignaturen liegen die lokalen Basisindexsprünge in

\[
\boxed{
j\in\{-2,-1,0,1,2,3\}.
}
\]

Insbesondere

\[
\boxed{
|j|\le3.
}
\tag{C1C0.7}
\]

Dies ist kleiner als die H2-Bridge-Reichweite \(4\).

Kein Widerspruch:

Die Reichweite \(4\) entsteht erst nach der **zweistufigen Eliminations-/Bridge-Komposition**

\[
\text{free}\to t\to\text{free}.
\]

Der inversefreie C0-Operator behält \(w\) als eigene Variable und benötigt für den direkten Hubteil nur Reichweite \(3\).

---

## 49. Formale feste Coverform

Damit besitzt der inversefreie Operator formal die feste Slotstruktur

\[
\boxed{
12_{\rm free}
+
3_w
=
15
}
\]

auf der Eingangsseite und

\[
\boxed{
12_{\rm phys}
}
\]

auf der Ausgangsseite.

Symbolisch:

\[
\boxed{
\mathbb C^{15}_{\rm form}
\longrightarrow
\mathbb C^{12}_{\rm form}.
}
\tag{C1C0.8}
\]

Dies ist bewusst **rechteckig**.

Die Kernelaufgabe verlangt nicht, dass die fiberisierte Darstellung quadratisch ist.

---

## 50. Zertifikat C1C0

Zertifikat:

scripts/certify_sw1_a10_c1c0_formal_ambient_cover.py

Commit:

cfeeeb4f9bc1f5c5a511508c327e6f9359071745

Committed Script-Blob:

71bdcb2fd4ae5d8187ef15936508cdb6c6930f81

Der Dateiinhalt wurde vor dem Commit exakt ausgeführt.

GitHub meldete danach exakt denselben Blob-SHA.

Ergebnis:

SW1-A10-C1C0 FORMAL AMBIENT-COVER CERTIFICATE: PASS

Damit ist im ausdrücklich begrenzten Scope zulässig:

\[
\boxed{
\mathrm{A10\!-\!C1C0\!-\!FORMAL}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}.
}
\]

---

## 51. C1C0-Firewall

Noch **nicht** bewiesen ist:

1. dass die 12 formalen \(P/\overline Q\)-Parity-Lift-Slots 12 unabhängige Hilbert-Fiberkoordinaten sind;
2. eine unitäre oder isometrische Fiberisierung
   \[
   \mathcal F_R\oplus L^2(\mathcal A)
   \longrightarrow
   L^2(\mathbb T_L;\mathbb C^{15});
   \]
3. die genaue Bild-/Konsistenzbedingung des formalen Mehrblatt-Covers;
4. der direkte vollständige Ledger von
   \[
   (I+A)J_R
   \]
   vom freien Cover in den physischen Cover;
5. eine endgültige Matrixform;
6. Injektivität.

Insbesondere wird **kein**

\[
N_{\rm ambient}=15
\]

als Hilbert-Fiberdimension gebucht.

Die Zahl \(15\) ist derzeit nur die Größe eines **formal geschlossenen Eingangscovers**.

---

## 52. Nächster Knoten

Der nächste notwendige Schritt lautet jetzt präzise:

\[
\boxed{
\mathrm{A10\!-\!C1C1}:
\text{analytische Fiberisierung des formalen Covers}.
}
\]

Dazu müssen wir entweder

1. einen expliziten isometrischen Mehrblatt-Embeddingoperator mit exakt beschriebenem Bild konstruieren,

oder

2. einen kleineren echten physischen Fiber wählen und die Reflexions-/Parity-Operationen als nichtlokale endliche Pullbacks behalten.

Erst nach dieser Entscheidung ist eine Aussage

\[
(\mathscr C f)(x)
=
\sum_j M_j(x)f(x+j\Delta)
\]

auf einem **wirklich definierten Hilbert-Fiberraum** zulässig.

Keine Injektivitätsaussage.


---

# C1C1 — korrigierte analytische Fiberisierung des formalen Mehrblatt-Covers

## 53. Review-Fund: positive Restriktion war nicht unitär normiert

Der erste C1C1-Entwurf wechselte still von den ursprünglichen Paritätsräumen

\[
\mathscr H_+
=
L^2(-T_0,T_0)^+
\]

und

\[
\mathscr W
=
\mathscr H_{\mathcal A}^-,
\qquad
\mathcal A=(-S,-R)\cup(R,S),
\]

auf die positiven Halbräume

\[
L^2(0,T_0),
\qquad
L^2(R,S).
\]

Die bloße Restriktion ist dort **nicht unitär**:

für gerades \(y\)

\[
\|y\|_{\mathscr H_+}^2
=
2\int_0^{T_0}|y(x)|^2\,dx,
\]

und für ungerades \(w\)

\[
\|w\|_{\mathscr W}^2
=
2\int_R^S|w(t)|^2\,dt.
\]

Daher war die frühere Formulierung der C1C1-Isometrie auf den **ursprünglichen** Hilberträumen falsch normiert.

Diese Fassung wird hiermit ersetzt.

---

## 54. Unitäre Paritätsfaltungen

Definiere

\[
\boxed{
F_+:
\mathscr H_+
\longrightarrow
L^2(0,T_0),
\qquad
(F_+y)(x)
=
\sqrt2\,y(x).
}
\tag{C1C1.1}
\]

Wegen der Geradheit ist \(F_+\) unitär.

Die Inverse lautet

\[
(F_+^{-1}f)(x)
=
\frac1{\sqrt2}\,f(|x|).
\]

Analog definiere auf dem ungeraden Annulus

\[
\boxed{
F_-:
\mathscr W
\longrightarrow
L^2(R,S),
\qquad
(F_-w)(t)
=
\sqrt2\,w(t),
\quad t>0.
}
\tag{C1C1.2}
\]

Wegen der Ungeradheit ist auch \(F_-\) unitär, mit

\[
(F_-^{-1}u)(t)
=
\frac{\operatorname{sgn}(t)}{\sqrt2}\,
u(|t|).
\]

Damit ist die positive H2-Darstellung nun explizit und normtreu an die ursprünglichen signierten Operatorräume zurückgebunden.

---

## 55. Physische Reparametrisierung des inversefreien Operators

Wie bereits in C0:

\[
\widetilde{\mathscr C}_R(y,w)
=
(I+A)y+HE_{\mathcal A}w,
\qquad
y\in K.
\tag{C1C1.3}
\]

Hier bleiben

\[
y\in K\subset\mathscr H_+,
\qquad
w\in\mathscr W
\]

in den **ursprünglichen** Hilberträumen.

Erst für die Fiberisierung werden \(F_+\) und \(F_-\) angewandt.

---

## 56. Vier kreismaßerhaltende Sheet/Parity-Transformationen

Auf

\[
\mathbb T_L=\mathbb R/L\mathbb Z
\]

definiere

\[
\phi_{P,0}(\theta)=\theta,
\]

\[
\phi_{P,1}(\theta)=\theta+\frac L2,
\]

\[
\phi_{\overline Q,0}(\theta)=4\Delta-\theta,
\]

\[
\phi_{\overline Q,1}(\theta)
=
4\Delta-\theta+\frac L2
\pmod L.
\]

Mit

\[
h(\theta)=\theta+\frac L2,
\qquad
q(\theta)=4\Delta-\theta
\]

gilt

\[
h^2=q^2=\mathrm{id},
\qquad
hq=qh.
\]

Damit ist

\[
\{\mathrm{id},h,q,hq\}
\]

eine Klein-Vierergruppe von maßerhaltenden Kreistransformationen.

---

## 57. Fixpunkt-Firewall

Für die Isometrie ist **nicht** erforderlich, dass

\[
\phi_g(\theta)
\]

für ein festes \(\theta\) vier verschiedene Kreispunkte sind.

Die vier \(g\)-Werte indexieren vier verschiedene Komponenten eines direkten Summenraums.

Die Norm ist

\[
\sum_g\sum_k
\|(V_Hf)_{g,k}\|_2^2,
\]

nicht die Norm einer punktweisen Vereinigung der vier Orbitpunkte.

Insbesondere dürfen zwei Komponenten denselben physischen Wert auswerten.

Tatsächlich können nur die Paare mit entgegengesetztem Slope kollidieren. Ihre Gleichungen reduzieren sich auf

\[
2\theta
\equiv
4\Delta
\pmod L
\]

oder

\[
2\theta
\equiv
4\Delta+\frac L2
\pmod L.
\]

Dies ergibt insgesamt höchstens vier Kreispunkte.

Diese endliche Nullmenge beeinflusst die \(L^2\)-Isometrie ohnehin nicht; stärker noch: selbst dort bleibt die direkte-Summen-Normformel korrekt.

---

## 58. Positiver Vierblatt-Cover \(V_H\)

Schreibe

\[
[\alpha]_L\in[0,L)
\]

für den kanonischen Kreisrepräsentanten und

\[
\rho_g(\theta)
=
[\phi_g(\theta)]_L.
\]

Für

\[
k=0,1,2
\]

setze

\[
m_{g,k}(\theta)
=
\mathbf1_{\{0<\rho_g(\theta)+kL<T_0\}}.
\]

Für

\[
f\in L^2(0,T_0)
\]

definiere

\[
\boxed{
(V_Hf)_{g,k}(\theta)
=
\frac12\,
m_{g,k}(\theta)\,
f(\rho_g(\theta)+kL).
}
\tag{C1C1.4}
\]

Für jedes feste \(g\) ist \(\rho_g\) maßerhaltend, und wegen

\[
T_0<3L
\]

gilt exakt

\[
\sum_{k=0}^2
\int_{\mathbb T_L}
m_{g,k}(\theta)
|f(\rho_g(\theta)+kL)|^2\,d\theta
=
\|f\|_{L^2(0,T_0)}^2.
\]

Somit

\[
\|V_Hf\|^2
=
4\cdot\frac14\|f\|^2
=
\|f\|^2.
\]

Also ist

\[
\boxed{
V_H:
L^2(0,T_0)
\hookrightarrow
L^2(\mathbb T_L;\mathbb C^{12})
}
\]

eine Isometrie.

---

## 59. Korrigiertes Horizont-Embedding vom ursprünglichen geraden Raum

Definiere nun

\[
\boxed{
U_H:=V_HF_+.
}
\tag{C1C1.5}
\]

Dann

\[
U_H:
\mathscr H_+
\hookrightarrow
L^2(\mathbb T_L;\mathbb C^{12})
\]

eine Isometrie.

Direkt in den ursprünglichen \(y\)-Werten lautet die Komponentenformel

\[
\boxed{
(U_Hy)_{g,k}(\theta)
=
\frac1{\sqrt2}\,
m_{g,k}(\theta)\,
y(\rho_g(\theta)+kL).
}
\tag{C1C1.6}
\]

Denn

\[
\frac12\sqrt2=\frac1{\sqrt2}.
\]

Die Normrechnung ist jetzt exakt zum ursprünglichen geraden Raum passend:

\[
4\cdot\frac12
\int_0^{T_0}|y(x)|^2\,dx
=
2\int_0^{T_0}|y(x)|^2\,dx
=
\|y\|_{\mathscr H_+}^2.
\]

---

## 60. Korrigiertes Annulus-Embedding

Definiere zunächst für

\[
u\in L^2(R,S)
\]

\[
(V_Wu)_k(\theta)
=
n_k(\theta)\,u(\theta+kL),
\]

mit

\[
n_k(\theta)
=
\mathbf1_{\{R<\theta+kL<S\}},
\qquad
k=0,1,2.
\]

Wegen

\[
S<T_0<3L
\]

partitionieren diese drei Liftkomponenten den positiven Annulus nach Restklasse modulo \(L\), und

\[
V_W:
L^2(R,S)
\hookrightarrow
L^2(\mathbb T_L;\mathbb C^3)
\]

ist eine Isometrie.

Setze

\[
\boxed{
U_W:=V_WF_-.
}
\tag{C1C1.7}
\]

Dann ist

\[
U_W:
\mathscr W
\hookrightarrow
L^2(\mathbb T_L;\mathbb C^3)
\]

eine Isometrie.

In ursprünglichen Annuluswerten:

\[
\boxed{
(U_Ww)_k(\theta)
=
\sqrt2\,
n_k(\theta)\,
w(\theta+kL).
}
\tag{C1C1.8}
\]

---

## 61. Abgeschlossenheit von \(U_H(K)\)

A2 beweist:

\[
K
=
\ker(E_I^*H|_{\mathscr H_+})
\]

ist abgeschlossen in \(\mathscr H_+\), weil \(E_I^*H\) beschränkt ist.

Da \(U_H\) eine Isometrie ist, ist

\[
\boxed{
\mathcal R_K:=U_HK
}
\]

abgeschlossen in

\[
L^2(\mathbb T_L;\mathbb C^{12}).
\]

Ebenso sind

\[
\mathcal R_H:=U_H\mathscr H_+
\]

und

\[
\mathcal R_W:=U_W\mathscr W
\]

geschlossen.

Damit ist

\[
(U_H|_K)^{-1}:
\mathcal R_K\to K
\]

beschränkt und wohldefiniert.

---

## 62. Kompatibilität von Horizont- und Annuluscover

Beide Cover benutzen denselben Basiskreis

\[
\mathbb T_L
\]

und dieselbe Liftperiode \(L\).

Für die **abstrakte Intertwining-Wohldefiniertheit** ist keine zusätzliche Rand-Matching-Bedingung nötig.

Definiere auf

\[
\mathcal R_K\oplus\mathcal R_W
\]

\[
\boxed{
\widehat{\mathscr C}_R
=
U_H\,
\widetilde{\mathscr C}_R\,
\bigl(
(U_H|_K)^{-1}
\oplus
U_W^{-1}
\bigr).
}
\tag{C1C1.9}
\]

Alle Faktoren sind beschränkt und wohldefiniert.

Die Gate-/Liftgrenzen sind Nullmengen und beeinflussen \(L^2\)-Operatoren nicht.

Die **explizite** Frage, welche drei Annuluskomponenten auf welchen Kreisatomen in welche zwölf Horizontkomponenten koppeln, ist genau der C2-Matrixledger.

Sie ist für die Existenz des transportierten Operators nicht zusätzlich vorauszusetzen.

---

## 63. Kernel-Intertwining

Weil

\[
U_H|_K:K\to\mathcal R_K
\]

und

\[
U_W:\mathscr W\to\mathcal R_W
\]

Isometrien auf ihre Bilder sind,

\[
\widehat{\mathscr C}_R(F,G)=0
\]

genau dann, wenn

\[
\widetilde{\mathscr C}_R
\left(
(U_H|_K)^{-1}F,\,
U_W^{-1}G
\right)=0.
\]

Daher

\[
\boxed{
\ker\widehat{\mathscr C}_R
\cong
\ker\widetilde{\mathscr C}_R
\cong
\ker\mathscr C_R
\cong
\ker\Gamma_I.
}
\tag{C1C1.10}
\]

---

## 64. Zertifikate

### 64.1 Mehrblatt-Algebra

scripts/certify_sw1_a10_c1c1_multisheet_cover.py

Commit:

fdab6b94b81e6e8cdd39c11b3b5134406e7ba8ed

Committed Script-Blob:

c1c5c97a0e5b3c5d40e06b4d6ae310aa5e06f9da

Ergebnis:

SW1-A10-C1C1 MULTI-SHEET COVER SKELETON CERTIFICATE: PASS

### 64.2 Paritätsfaltungs-Normierung

scripts/certify_sw1_a10_c1c1_parity_fold_normalization.py

Commit:

1c5de41024d954e6afb6a9d64a97223f0d6678b5

Committed Script-Blob:

015fcb7505ca4a8ede6513d4ab01d815cef44606

Der committed Blob stimmt bytegenau mit der vorab ausgeführten Datei überein.

Ergebnis:

SW1-A10-C1C1 PARITY-FOLD NORMALIZATION CERTIFICATE: PASS

---

## 65. C1C1-Status nach adversarialem Review

Der Review hat einen echten Normierungsfehler im ersten analytischen Entwurf gefunden und repariert.

Zulässig ist:

\[
\boxed{
\mathrm{A10\!-\!C1C1\!-\!ALG/FOLD}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, finite algebraic/mechanical scope)}.
}
\]

Für die korrigierte unendlichdimensionale Aussage

- \(U_H,U_W\) sind Isometrien;
- \(U_H(K)\) ist abgeschlossen;
- C1C1.9 ist ein wohldefinierter transportierter Operator;
- C1C1.10 erhält den Kernel,

steht nun ein vollständiger interner adversarialer Beweis.

Der externe Cross-Model-Blindcheck vom 30. August 2026 bestätigt die korrigierte Fassung. Daher gilt

\[
\boxed{
\mathrm{A10\!-\!C1C1\!-\!AN}:
\text{AI-GREEN}
+
\text{independent GREEN (cross-model blind review, Hilbert-space scope)}.
}
\]

Keine Promotion.

---

## 66. Nächster Knoten C2

Erst nach externer Bestätigung der korrigierten C1C1-AN-Fassung wird C2 gebucht.

C2 soll dann getrennt herleiten:

1. den freien physischen Block
   \[
   U_H(I+A)(U_H|_K)^{-1};
   \]
2. den Hubblock
   \[
   U_HHE_{\mathcal A}U_W^{-1};
   \]
3. die gemeinsame C1B-Partition, auf der sämtliche Matrixeinträge simultan stückweise konstant/algebraisch sind.

Erst dann ist eine finite-range Matrixform

\[
(\widehat{\mathscr C}_RF)(\theta)
=
\sum_j M_j(\theta)F(\theta+j\Delta)
\]

zulässig.

Keine Injektivitätsaussage.


---

# C1C1-AN — externer Blindreview abgeschlossen

Das fokussierte Reviewpaket

audits/P11_R32_SW1_A10_C1C1_AN_REVIEW_PACKET.md

wurde am 30. August 2026 unabhängig cross-model geprüft.

Bestätigt wurden getrennt:

1. **Fixpunkt-/Direktsummenfrage:** PASS. Die vier Sheet/Parity-Komponenten sind direkte-Summen-Komponenten; punktweise Orbitkollisionen ändern die \(L^2\)-Norm nicht.
2. **Closure:** PASS. \(K\) ist abgeschlossen und die korrigierte \(U_H\)-Abbildung isometrisch, daher ist \(U_H(K)\) abgeschlossen.
3. **Abstraktes Intertwining:** PASS. Die Konjugationsdefinition auf den geschlossenen Bildunterräumen ist wohldefiniert; eine punktweise Gate-Rand-Matching-Bedingung wird erst für die explizite C2-Matrixdarstellung relevant.
4. **Gesamt C1C1-AN:** PASS für die korrigierte \(\sqrt2\)-Faltungsfassung.

Die frühere, unnormierte positive Restriktionsfassung bleibt ausdrücklich verworfen.

Zulässiger Status:

\[
\boxed{
\mathrm{A10\!-\!C1C1\!-\!AN}:
\text{AI-GREEN}
+
\text{independent GREEN (cross-model blind review, Hilbert-space scope)}
}
\]

**Keine Promotion. Keine Injektivitätsaussage.**

---

# C2-Vorprüfung — physischer Hubblock versus KNF-H2-Ledger

Für die C2-Matrixdarstellung ist eine Scope-Korrektur wesentlich.

Der H2-53-Kanalledger beschreibt

\[
J_R^*HE_{\mathcal A},
\]

also den bereits in freie KNF-Koordinaten zurückgezogenen Huboperator.

C1C1 verwendet dagegen die physische Reparametrisierung

\[
\widetilde{\mathscr C}_R(y,w)
=
(I+A)y+HE_{\mathcal A}w.
\]

Daher muss der direkte C2-Hubblock aus

\[
HE_{\mathcal A}
\]

selbst aufgebaut werden.

Nach positiver Odd-Faltung besitzt dieser physische Hub genau neun geometrische Zweige:

\[
x=a-t,\quad x=t+a,\quad x=t-a,
\]

\[
x=b-t,\quad x=t+b,\quad x=t-b,
\]

\[
x=T-t,\quad x=t+T,\quad x=t-T,
\]

jeweils mit den bekannten Gewichten

\[
(-p,+p,-p),\quad
(-r,+r,-r),\quad
(-q,+q,-q),
\]

und den entsprechenden Support-/Horizon-Gates.

Die 53 H2-Kanäle bleiben für spätere Konsistenzchecks wertvoll, sind aber **nicht** der direkte C2-Hubmatrixledger.

---

# C2-Cover-Firewall — 15→12 abstrakt, 24→12 für reinen \(\Delta\)-Cocycle

Der C1C1-Cover

\[
12_H+3_W\to12_H
\]

ist als abstrakte Hilbertraum-Konjugation korrekt.

Für eine Darstellung ausschließlich durch Basisrotationen

\[
\theta\mapsto\theta+j\Delta
\]

ist der dreifache Annuluscover jedoch nicht unter allen Sheet/Parity-Pullbacks geschlossen.

Eine physische Hubrelation

\[
x=s\,t+\lambda L+k\Delta
\]

transformiert bei Verwendung der vier Horizont-Sheets im Allgemeinen auch die Annulusbasis durch Halbshift/Reflexion.

Um diese endliche Klein-Vierer-Wirkung vollständig in Fiberindizes statt in zusätzliche Basispullbacks zu absorbieren, ist der natürliche symmetrische Annuluscover

\[
4\text{ Sheet/Parity-Spezies}\times3\text{ Lifts}
=
12_W.
\]

Damit entsteht als C2-Arbeitscover

\[
\boxed{
(12_H+12_W)\longrightarrow12_H.
}
\]

Dies ist **keine neue physische Fiberdimension** und keine Änderung des Operators, sondern eine redundante symmetrische Darstellung für einen reinen endlichen \(\Delta\)-Rotationsledger.

Die Minimalität dieses 12er Annuluscovers ist noch nicht gebucht; zunächst wird nur seine Closure geprüft.
