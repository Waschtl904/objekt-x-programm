# NEU-117 — X-Rigidität I: R1-Test der konkreten N⁺-Einbettung

**Stand: 3. Juli 2026**

---

## Anschluss an NEU-116.C.18

NEU-116.C.18 schließt die Θ₁₂-Analyse ab. Ergebnis ist der Vierschichtensatz:

```
X_skel  =/=  X  =/=  X^val  =/=  W_xi^norm.          (116.C.18.7)
```

Mit präzisen Rollen:

```
X_skel    -->  nackte Divisibilitäts-/Kantenform.
X         -->  tatsächliche Residuenstruktur (Rigidität unklar).
X^val     -->  Residuenstruktur + logarithmischer Kantencocycle T_rel.
W_xi^norm -->  kritisch normalisierte Weil-Distribution; alpha=1/2.
```

Auf Skelett-Ebene ist gesichert:

```
T_rel not in Str_int(X_skel).                          (116.C.18.1b)
```

Die neue Leitfrage ist NICHT mehr:

```
Ist Theta_{1/2} intern in W_res^top?
```

sondern:

```
Wie viel Arithmetik steckt bereits in X?               (NEU-117.Ziel)
```

---

## NEU-117.0 — Leitfrage und Entscheidungstest

### 117.0.1 — Primäre Leitfrage

```
Ist die konkrete N_+-Monoid-Einbettung Bestandteil von X,
oder erst Bestandteil von X^val?

Äquivalent:
  Sym(P) ⊆ Aut(X_skel)  [gesichert, 116.C.18.1a]
  aber:
  Lift_X(Sym(P))  =?  {1}.                             (117.0.1)

Falls Lift_X(Sym(P)) = {1}:
  X ist arithmetisch rigid (Ausgang B aus 116.C.18).
  T_rel folgt aus der N_+-Struktur von X (nicht aus reiner Topologie).

Falls Lift_X(Sym(P)) =/= {1}:
  Primzahlpermutationen liften nach X.
  B_ref falsifiziert; X^val =/= X ist vollständig bestätigt.
```

### 117.0.2 — Stärkster Falsifikator (Wiederholung aus 116.C.18.F)

```
Suche phi in Aut(X) mit:
  (i)  phi ist rho-strukturtreu (erhält W_res^top).
  (ii) T_rel o phi =/= T_rel.

Falls gefunden: B_ref endgültig falsifiziert.           (117.0.2.F)
Falls nicht gefunden: X ist arithmetisch rigid;
  Rigiditsstruktur muss explizit benannt werden.        (117.0.2.F2)
```

---

## NEU-117.1 — R1: Konkrete N_+-Monoid-Einbettung

### 117.1.1 — Zwei Varianten der N_+-Struktur in X

```
VARIANTE (α): X enthält N_+ als abstraktes freies kommutatives Monoid.
  Objekte: {1, 2, 3, ...} als nackte Punkte.
  Morphismen: m -> nm  als nackte Kanten, ohne Primfaktorzerlegung
  als separates Strukturdatum.
  => Primzahlen p sind nicht ausgezeichnet als atomare Elemente.
  => Primzahlpermutationen sigma: p_i <-> p_j koennte Monoid-Isomorphismus sein,
     falls sigma sich zu einem Multiplikationsautomorphismus ausdehnt.
  => Aut(X) koennte Sym(P) enthalten.
  => Ausgang A moeglich.                               (117.1.1.alpha)

VARIANTE (β): X enthält N_+ mit seiner konkreten multiplikativen Struktur.
  N_+ = freies kommutatives Monoid mit kanonischen Erzeugern P = {2,3,5,7,...}.
  Die Primzahlen sind die EINZIGEN irreduziblen Elemente des Monoids.
  Primfaktorzerlegung ist eindeutig (FTA).
  => Ein Monoid-Automorphismus muss irreduzible Elemente auf
     irreduzible Elemente abbilden, d.h. Primzahlen auf Primzahlen.
  => Damit waere phi_sigma: p_i |-> sigma(p_i) ein Monoid-Automorphismus.
  => Aber: Der Monoid-Automorphismus phi_sigma sendet
       m = prod p_i^{e_i}  zu  prod sigma(p_i)^{e_i}.
     Das ist wieder ein wohldef. Element von N_+.
  => phi_sigma ist ein Monoid-Automorphismus von N_+ (als abstraktes freies Monoid).
  => Also: Aut(N_+ als freies Monoid) = Sym(P).       (117.1.1.beta)

Zwischenbefund:
  N_+ als freies Monoid ALLEIN blockiert Primzahlpermutationen NICHT.
  Sym(P) ⊆ Aut(N_+ als freies Monoid).
  Die N_+-Einbettung allein reicht als Rigiditsquelle daher nicht.
  => R1 in der schwachen Form (freies Monoid) = kein Falsifikator,
     aber auch kein Rigiditatsbeweis.                  (117.1.1.Z)
```

### 117.1.2 — R1 in der starken Form: N_+ mit arithmetischer Einbettung

```
Die relevante Frage ist nicht, ob N_+ als abstraktes freies Monoid
in X eingebettet ist, sondern:

Ist die KONKRETE arithmetische Einbettung von N_+ vorhanden?

"Konkrete arithmetische Einbettung" bedeutet:
  N_+ ist nicht nur als abstrakter Monoid in X,
  sondern als der SPEZIFISCHE Unterring / die spezifische Unterstruktur
  von Z, Q, A_f, Z-hat, oder eines adèlischen/lokalen Rings.

Dann gilt:
  N_+ ⊆ Z ⊆ Q ⊆ A_f = prod'_p Q_p.

  Eine Primzahlpermutation sigma permutiert die Primzahlen 2,3,5,...
  als konkrete ganze Zahlen. Aber:
    sigma(2) = 3, sigma(3) = 2 (z.B.)
  koennte als Automorphismus des abstrakten freien Monoids wirken,
  aber NICHT als Automorphismus von Z oder Q:
    sigma ist kein Ring-Automorphismus von Z  (weil die Additionsstruktur
    von Z nicht mit Primzahlpermutationen kompatibel ist;
    3+3 = 6 aber sigma(2+2) = sigma(4) = 9 =/= 6 fuer sigma(2)=3).

  Rigiditatsbefund:
    Falls X die additive Struktur von Z oder Q (oder A_f) traegt,
    sind Primzahlpermutationen nicht liftbar.
    => Lift_X(Sym(P)) = {1}.                           (117.1.2.R)
```

### 117.1.3 — Entscheidungsdiagramm R1

```
+------------------------------------------------------------+
| R1-Test: Welche N_+-Struktur traegt X?                    |
|                                                            |
| Fall (i): X traegt N_+ nur als freies Monoid.             |
|   Aut(X) koennte Sym(P) enthalten.                        |
|   => Ausgang A moeglich.  R1 blockiert nicht.             |
|                                                            |
| Fall (ii): X traegt N_+ als Unterstruktur von Z/Q/A_f.   |
|   Primzahlpermutationen brechen Additionsstruktur.        |
|   => Lift_X(Sym(P)) = {1}.                                |
|   => Ausgang B.  R1 blockiert.                            |
|                                                            |
| Diagnose:                                                  |
|   Welcher Fall liegt in der konkreten Definition von X vor?|
+------------------------------------------------------------+
                                                (117.1.3)
```

---

## NEU-117.2 — R2–R5: Weitere Rigiditsquellen (Kurzcheck)

```
R2: Hecke-Korrespondenzen.
  T_n-Operatoren differenzieren nach Primfaktorzerlegung von n.
  Falls X Hecke-Operatoren T_p als ausgezeichnete Morphismen traegt,
  sind Primzahlen strukturell individuiert.
  => phi_sigma muesste T_p auf T_{sigma(p)} abbilden.
  Falls T_p und T_{sigma(p)} nicht isomorph als X-Morphismen:
    => sigma nicht liftbar.  Ausgang B.                (117.2.R2)

R3: Z-hat-Struktur (profinite Completion).
  Z-hat = prod_p Z_p. Z_p-Fasern sind primspezifisch.
  Primzahlpermutation sigma: p <-> q vermischt Z_p und Z_q.
  Z_p =/= Z_q als topologische Ringe (verschiedene Charakteristiken mod p^n).
  => phi_sigma nicht Z-hat-kompatibel.  Ausgang B.    (117.2.R3)

R4: n-Level-Geometrie.
  Levelstruktur H/n*H oder Torsionspunkte E[n] ist
  von der Primfaktorzerlegung von n abhaengig.
  Primzahlpermutation aendert Primfaktoren => Level-Typen aendern sich.
  => Ausgang B oder C.                                (117.2.R4)

R5: Lokale Index-/Restklassenstruktur.
  Z/p^k Z-Restklassen sind p-spezifisch.
  Isomorphie Z/p Z =? Z/q Z als Ringe nur falls p = q.
  => Primzahlpermutation nicht lokal kompatibel.
  => Ausgang B.                                       (117.2.R5)

Diagnose:
  R3 (Z-hat) und R5 (lokale Restklassen) liefern die saubersten
  Rigiditatsnachweise, weil Z_p und Z_q nicht isomorph als
  topologische Ringe sind (wenn p =/= q).
  Diese Argumente funktionieren unabhaengig von der Frage,
  ob N_+ als freies oder konkretes Monoid in X eingebettet ist.
```

---

## NEU-117.3 — Hauptbefund

### 117.3.1 — Rigiditatsbefund

```
Wenn X eine der folgenden Strukturen traegt:
  (R2) Hecke-Operatoren T_p als ausgezeichnete Morphismen, ODER
  (R3) Z-hat = prod_p Z_p als profinite Faserstruktur, ODER
  (R5) Lokale Restklassen Z/p^k Z fuer Primzahlpotenzen,

dann gilt:
  Lift_X(Sym(P)) = {1}.                               (117.3.1.R)

Denn: In allen drei Faellen sind die p-spezifischen Strukturen
(Z_p, T_p, Z/p Z) paarweise nicht-isomorph fuer verschiedene Primzahlen p.
Eine Primzahlpermutation sigma koennte also keinen
Strukturautomorphismus von X liefern.
```

### 117.3.2 — Konsequenz fuer B_ref

```
Falls 117.3.1.R gilt (Ausgang B):

  T_rel kommt nicht aus reiner Topologie (gesichert seit 116.C.17),
  aber auch nicht erst aus X^val.
  Stattdessen:
    T_rel ist durch die arithmetische Rigiditsstruktur von X
    (R2/R3/R5) strukturell erzwungen.

  B_ref in schwacher Form:
    X traegt T_rel-kompatible Arithmetik.
    Aber: X =/= X^val (T_rel ist noch nicht der explizite Cocycle).
    X ist arithmetisch rigid; X^val macht T_rel explizit.

  Praeziser Satz:
    T_rel kommt nicht aus Topologie (X_skel),
    sondern aus arithmetischer Rigiditsstruktur (X),
    und wird durch X^val = (X, T_rel) als expliziter Cocycle notiert.
                                                      (117.3.2)
```

### 117.3.3 — Kernsatz

```
+--------------------------------------------------------------+
| KERNSATZ (NEU-117):                                         |
|                                                              |
| X_skel ist permutations-symmetrisch:                        |
|   Aut(X_skel) ⊇ Sym(P).                                    |
|   T_rel not in Str_int(X_skel).                             |
|                                                              |
| X ist arithmetisch rigid (via R2/R3/R5):                   |
|   Lift_X(Sym(P)) = {1}.  (vorläufige Diagnose Ausgang B)   |
|   T_rel kommt aus arithmetischer Rigidität von X.           |
|                                                              |
| X^val = (X, T_rel) macht T_rel explizit als Cocycle.        |
|                                                              |
| W_xi^norm selektiert alpha = 1/2 durch externen Vergleich.  |
|                                                              |
| Vierschichtensatz (117.3.3):                                 |
|   X_skel (Symmetrie) -> X (Rigidität) ->                   |
|   X^val (Bewertung) -> W_xi^norm (Normierung).             |
+--------------------------------------------------------------+
```

---

## NEU-117.A — Lesetest von NEU-43/44 auf Rigiditätsquellen

### 117.A.0 — Ziel

```
Bestimme, welche arithmetische Struktur in der Definition von X
TATSAECHLICH kanonisch enthalten ist.
Nicht hypothetisch, sondern durch Ruecklesung von NEU-43/44
bzw. des konsolidierten X-Axiomensystems in Ebene XVI.
                                                     (117.A.0)
```

### 117.A.1 — Quellbefund aus der X-Definition

```
Aus Ebene XVI (Stand NEU-114) folgt:

  X.4  = Frobenius- und Zeitentwicklungskompatibilitaet.      ✓[M]
  X.6  = Spurform Wres_BC^{top} - notwendig, nicht optional.  ✓[M]
  X.7  = relative Primkanten H_{rel,N} = oplus_{p<=N} oplus_m
         H_{m->^p pm} strukturell notwendig (NEU-44).         ✓[M]

Damit ist X nicht als blosses freies Monoid-Skelett definiert,
sondern mindestens mit konkreter relativer Primkantenstruktur.
                                                     (117.A.1.a)

Aber:
  Weder X.1--X.10 noch NEU-44 enthalten explizit die starke
  R1-Quelle

     N_+ -> Z -> Q

  als formale Teilstruktur von X.
  Die additive Ringumgebung ist in der Definition von X
  NICHT explizit eingebaut.                            (117.A.1.b)

Ferner:
  X.4/X.6 verweisen auf BC-/Frobenius-/Spur-Kontext,
  also auf eine arithmetische/profinite Modellumgebung.
  Offen bleibt aber, ob diese Umgebung zur inneren Struktur von X
  gehoert oder nur zum Kontext, in dem X modelliert wird.
                                                     (117.A.1.c)
```

### 117.A.2 — Abgleich mit A1/A2/A3

| Test | Frage | Befund |
|---|---|---|
| A1 | nur N_+ als freies Monoid? | **Nein.** X.7 fordert konkrete relative Primkanten `m ->^p pm`; X ist nicht bloss freies Monoid-Skelett. |
| A2 | additive Ringumgebung `N_+ -> Z -> Q` direkt in X? | **Nein.** Diese starke R1-Quelle ist in X.1–X.10 / NEU-44 nicht explizit enthalten. |
| A3 | profinite/lokale Umgebung (`Z-hat`, `Z_p`, `Z/pZ`, BC-Kontext)? | **Indirekt ja.** X.4/X.6 binden X an Frobenius-, KMS- und Spur-Kontext; ob dies formale Teilstruktur oder nur Modellumgebung ist, bleibt offen. |

### 117.A.3 — Präziser Befund

```
Der richtige Zwischenbefund lautet daher NICHT:
  "X blockiert Primzahlpermutationen bereits eindeutig."

Sondern praeziser:
  X ist nicht skelettfrei,
  aber die Rigiditaet der Primlabels haengt daran,
  ob X.4/X.6/X.7 formal zur Struktur von X gehoeren
  oder nur zur Modellumgebung.                         (117.A.3.P)

Insbesondere folgt aus der blossen Notation H_{m->pm}
noch nicht automatisch volle Primrigiditaet.
Entscheidend ist, ob das p nur Skelett-Label ist,
oder durch BC-/Spur-/Frobenius-Struktur arithmetisch gebunden wird.
                                                     (117.A.3.L)
```

### 117.A.4 — Vorläufiger Entscheid

```
VORLAEUFIGER ENTSCHEID:
  Fall C - partielle Rigiditaet.                       (117.A.4)

Praezisierung:
  Fall C ist gesichert als Befund aus X.7:
    X_skel  subsetneq  X.                              ✓[M]

  Aber offen bleibt:
    folgt aus X.4/X.6/X.7 bereits volle Primrigiditaet?
    also insbesondere:
      Lift_X(Sym(P)) = {1} ?                           ?[O]

Daher gilt vorlaeufig nur:
  X ist nicht bloss monoid-skelettnah,
  aber X = X^val ist nicht bewiesen,
  und B_ref ist durch 117.A weder gerettet noch widerlegt.
                                                     (117.A.4.C)
```

### 117.A.5 — Kernsatz des Befundblatts

```
+--------------------------------------------------------------+
| KERNSATZ (NEU-117.A):                                       |
|                                                              |
| NEU-43/44 definieren X nicht als blosses freies             |
| Monoid-Skelett, sondern mit konkreter relativer             |
| Primkantenstruktur H_{m->pm}.                               |
|                                                              |
| Die starke R1-Quelle                                        |
|   N_+ -> Z -> Q                                             |
| ist in der Definition von X jedoch NICHT explizit enthalten.|
|                                                              |
| Die moegliche Rigiditaet von X kommt daher                  |
| wahrscheinlich nicht aus R1 stark, sondern aus der in       |
| X.4/X.6/X.7 impliziten BC-/profiniter Umgebung.             |
|                                                              |
| Ob diese Umgebung Struktur oder nur Kontext ist,            |
| bleibt die entscheidende Anschlussfrage — wird aber         |
| als Setzungsfrage in NEU-117.B abgeschlossen.               |
+--------------------------------------------------------------+
```

---

## NEU-117.B — Abschlusskonvention: X.4/X.6/X.7 als formale Strukturaxiome

**Stand: 3. Juli 2026 — Schlussstein des NEU-117-Blocks**

```
KONVENTION (NEU-117.B):                                (117.B.K)

  X.4 (Frobenius/KMS-Kompatibilitaet),
  X.6 (Spurform Wres_BC^{top}),
  X.7 (relative Primkanten H_{m->pm})

  werden ab NEU-118 als FORMALE STRUKTURAXIOME von X behandelt,
  nicht als blossen Modellierungskontext.

  Das heisst:
    Automorphismen von X muessen X.4/X.6/X.7 respektieren.
    Primlabels p in H_{m->pm} sind strukturell gebunden,
    nicht nur Notationsschema.

  Diese Setzung ist eine Konvention, kein Beweis.
  Sie stabilisiert die Sprache fuer den Beweisangriff in NEU-118.
```

```
KONSEQUENZ fuer den Vierschichtensatz:

  X_skel  subsetneq  X  subseteq  X^val.               (117.B.V)

  X_skel <  X:  gesichert durch X.7 / NEU-44.          ✓[M]
  X = X^val:    nicht bewiesen; bleibt offene Frage.    ?[O]

  Aber: Die Frage X = X^val? wird ab jetzt nicht mehr
  als Axiom-Diagnosefrage weiterverfolgt, sondern nur noch
  durch konkrete Konstruktionen entscheidbar.
```

```
KERNSATZ (NEU-117.B):

  NEU-117 beendet die Objekt-X-Rigiditaetsdiagnose.
  Fuer Beweiszwecke wird X fortan nur noch ueber konkrete
  Konstruktionen akzeptiert: explizite Operatoren, Kerne,
  Masse, Transformierte.

  Keine weiteren Strukturaxiome ab NEU-118.             (117.B.S)

Anschluss:
  NEU-118 -- Bombieri-Normalisierung: direkter Konvergenztest
  fuer m_{Omega,N} -> m_arith.                          --> NEU-118
```

---

## Satzstatusmatrix (NEU-117, abgeschlossen)

| Test | Inhalt | Status |
|---|---|---|
| 117.0 | Leitfrage: N_+-Einbettung in X oder X^val? | ?[O] |
| 117.1.1 | Freies Monoid: Aut(N_+) = Sym(P) | ✓[M] |
| 117.1.2 | Starke R1: N_+ in Z/Q/A_f => Perm. nicht liftbar | ✓[M] konditionell |
| 117.2.R3 | Z-hat: Z_p =/= Z_q => Perm. nicht liftbar | ✓[M] konditionell |
| 117.2.R5 | Lokal: Z/pZ =/= Z/qZ => Ausgang B | ✓[M] konditionell |
| 117.3.3 | Vierschichtensatz Symmetrie->Rig->Bew->Norm | ✓[M] |
| 117.A | Lesetest NEU-43/44: Fall C, partielle Rigidität | ✓[M]/?[O] |
| 117.B | X.4/X.6/X.7 als formale Struktur deklariert (Konvention) | ✓[K] |

---

## Anschlüsse

| Voraussetzung | Quelle |
|---|---|
| Vierschichtensatz | NEU-116.C.18.7 |
| T_rel not in Str_int(X_skel) | NEU-116.C.18.1b |
| Relative Primkanten H_{m->^p pm} | NEU-44 / Ebene XVI, X.7 |
| Frobenius-/Zeitentwicklung | Ebene XVI, X.4 |
| Spurform Wres_BC^{top} | Ebene XVI, X.6 |
| X.4/X.6/X.7 als Strukturaxiome (Konvention) | NEU-117.B |
| Nächster Schritt: Bombieri-Normalisierung | --> NEU-118 |
