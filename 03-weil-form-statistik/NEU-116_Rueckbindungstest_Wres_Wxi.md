# NEU-116 — Rückbindungstest: W_res^top -> W_xi^norm

**Stand: 3. Juli 2026**

---

## Ziel (präzisiert nach 116.C.18)

Verbindliche Vier-Ebenen-Architektur:

```
X_skel     (nacktes Divisibilitäts-/Kantenskelett)
  |
  | [iota_skel]  (Einbettung/Vergessensfunktor)
  v
X          (tatsächliche Residuenstruktur)
  |
  | [iota_val]   (Hinzufügen des logarithmischen Cocycles)
  v
X^val = (X, T_rel)  (Residuenstruktur plus Bewertung)
  |
  | [rho^val]
  v
W_res^{top,crit} = W_xi^norm  (kritisch normierte Weil-Distribution)

Vierschichtensatz:
  X_skel  =/=  X  =/=  X^val  =/=  W_xi^norm.          (116.0.V)
```

Leitfragen nach 116.C.18:

```
(1) Welche Symmetrien liften: Aut(X_skel) -> Aut(X)?
(2) Enthält X bereits arithmetische Rigidität?
(3) X = X^val  (B_ref)  oder  X =/= X^val  (C)?
```

---

## NEU-116.0 — Ausgangspunkt aus NEU-113

```
n^{-s} = n^{-1/2} e^{-iz log n}  (s=1/2+iz).             (113.4)

W_xi^norm[Phi] = (Phi-hat(i/2)+Phi-hat(-i/2))
  + (1/2pi) int Phi-hat(lambda)(-log pi+Re psi(1/4+i lambda/2)) d lambda
  - sum_{n>=2} Lambda(n)/sqrt(n)*(Phi(log n)+Phi(-log n)).(116.0.3)
```

---

## NEU-116.1 — Dreiteiliger Rückbindungstest

```
116.A: W_res^{top,crit,0/1}   =?  E_{0,1}    ?[O]
116.B: W_res^{top,crit,Gamma} =?  G          ?[O]
116.C: W_res^{top,crit,prime} =?  -P         ?[O]  <- HAUPTTEST
```

---

## NEU-116.A, 116.B — Weitere Tests

```
116.A: W_res^{top,0/1}[Phi] = Phi-hat(i/2)+Phi-hat(-i/2).  ?[O]
116.B: W_res^{top,Gamma}[Phi] = (1/2pi) int Phi-hat * Psi_Gamma. ?[O]
```

---

## NEU-116.C — Primkanten-Test

```
Zerlegung: -(log p)/p^{k/2} = (-1)*log p*p^{-k/2}.
[116.C_4] Vz. [116.C_2] Mangoldt. [116.C_3] Theta_{1/2}. [116.C_1] Ort.
Konditionell: 116.C_1&2&3&4 => 116.C => NEU-114.4 von ⚠[M] auf ✓[M].
```

---

## NEU-116.C.9–17 — Analyse des kritischen Faktors (Zusammenfassung)

```
Modularlemma: D^alpha V_n D^{-alpha} = n^{-alpha} V_n.    (116.C.12.1)
Ablesebefund (116.C.13): alpha=1/2 als e^{-sT_rel}|_{s=1/2}, nicht M3.
Internalisationstest (116.C.14): zweistufig; Primterm => -P.
Internalitaetstest (116.C.15): ST-3/ST-4 ✓[M]: Theta_{1/2} extern.
Funktorialitaetsbruch (116.C.16): X^val=(X,T_rel); Lifting-Diagramm.
Intrinsizitaetstest (116.C.17): IT-1/3/4 ✓[M] gegen B_ref; IT-2 ?[O].
Dreischichtensatz: X =/= X^val =/= W_xi^norm.
Hauptaussage: Re(s)=1/2 ist Bewertungsuebergang, keine Topologiekonstante.
```

---

## NEU-116.C.17 — Intrinsizitätstest für T_rel in X (Zusammenfassung)

```
IT-1 ✓[M]: T_rel arithmetisch rekonstruierbar, nicht topologisch.
IT-2 ?[O]: Kein Primzahlpermutations-Automorphismus gefunden/widerlegt.
IT-3 ✓[M]: Nur Familie alpha*T_rel erzwungen, kein eindeutiges alpha.
IT-4 ✓[M]: alpha=1/2 extern durch W_xi^norm selektiert.

Dreischichtensatz (116.C.17.7):
  Schicht 1: X (Topologie, kein alpha).
  Schicht 2: X^val (Arithmetik, T_rel).
  Schicht 3: W_xi^norm (Weil-Norm, alpha=1/2).

Programmsatz (116.C.17.8):
  Re(s)=1/2 entsteht nicht aus Topologie, sondern aus Bewertungsuebergang.

B_ref: nicht falsifiziert, aber durch IT-1/IT-4 stark eingeschränkt.
Kandidat C: verbindliche Arbeitsarchitektur.
```

---

## NEU-116.C.18 — Skelett, Rigidität und Liftbarkeit von Primzahlsymmetrien

### Ziel

NEU-116.C.18 ist kein weiterer Theta_{1/2}-Test, sondern Strukturdiagnose von X:

```
Nicht: Theta_{1/2} in? W_res^top.
Sondern: Welche Struktur von X blockiert oder erlaubt Primzahlpermutationen?

Verbindliche Objektkette:
  X_skel  --[iota_skel]-->  X  --[iota_val]-->  X^val = (X, T_rel).

Entscheidungsfrage:
  Aut(X_skel) --> Aut(X): Welche Symmetrien liften?          (116.C.18.Ziel)
```

### 116.C.18.1 — Das Skelett X_skel

```
Definition:
  X_skel = nacktes Divisibilitäts-/Kantenskelett.

  Objekte: positive ganze Zahlen m in N_+.
  Morphismen: Kanten m -> nm  (für n in N_+).
  Kein arithmetisches Label ausser Quelle und Ziel.
  Keine Metrik, keine Bewertung, keine Primzerlegungsstruktur
  als separates Datum (nur implizit durch m -> p^k m als Spezialfall).

Automorphismen von X_skel:
  Ein Automorphismus phi_sigma kann die Primzahlen permutieren:
    phi_sigma(m -> p^k m) = m -> sigma(p)^k m.
  Das ist ein wohldefinierter Endomorphismus des Kantenskeletts,
  sofern sigma eine Bijektion P -> P ist.

  Damit gilt:
    Aut(X_skel) => Sym(P)  (Permutationen der Primzahlen).   (116.C.18.1a)

  Auf dem Skelett ist T_rel NICHT invariant:
    T_rel(m -> p^k m) = k log p,
    T_rel(phi_sigma(m -> p^k m)) = k log sigma(p).
    => T_rel o phi_sigma =/= T_rel  (falls sigma(p) =/= p).

  Kernsatz des Skeletts:
    T_rel not in Str_int(X_skel).                            (116.C.18.1b)
```

### 116.C.18.2 — Liftbarkeit nach X: Drei Ausgänge

```
Kritischer Pfeil:
  Aut(X_skel) --> Aut(X).

  Frage: Liften Primzahlpermutationen phi_sigma in Aut(X_skel)
         zu Automorphismen von X?

AUSGANG A: Viele Primzahlpermutationen liften.

  Formal: Es gibt sigma in Sym(P) (sigma =/= id) mit
    phi_sigma in Aut(X)  und  phi_sigma rho-strukturtreu.

  Dann gilt:
    T_rel o phi_sigma =/= T_rel.
    => T_rel not in Str_int(X).
    => B_ref falsifiziert.
    => X^val =/= X.  (Kandidat C bestaetigt)               (116.C.18.A)

AUSGANG B: Keine nichttriviale Primzahlpermutation liftet.

  Formal: Fuer alle sigma in Sym(P) \ {id} gilt
    phi_sigma not in Aut(X).

  Dann enthaelt X eine Blockadestruktur, die Primzahlpermutationen
  verhindert. X ist arithmetisch rigid.

  Konsequenz:
    T_rel kommt nicht aus reiner Topologie, sondern aus
    arithmetischer Rigidität innerhalb von X.
    B_ref moeglicherweise als schwache Version gueltig:
      X traegt bereits T_rel-kompatible Arithmetik.         (116.C.18.B)

AUSGANG C: Nur bestimmte Permutationen liften.

  Formal: Im(Aut(X_skel) -> Aut(X)) ist eine echte Untergruppe
    von Sym(P), nicht trivial, aber echt kleiner.

  Dann:
    X liegt strikt zwischen Skelett und Bewertungsobjekt:
      X_skel  ⊊  X  ⊊  X^val  (im Sinne der Strukturreichtums).
    Partielle arithmetische Rigidität; Blockadestruktur identifizieren.
                                                             (116.C.18.C)
```

### 116.C.18.3 — Stärkster Falsifikator für B_ref

```
Falsifikator:
  Suche phi in Aut(X) mit:
  (i)  phi ist rho-strukturtreu (erhält W_res^top).
  (ii) T_rel o phi =/= T_rel.

  Falls ein solches phi existiert:
    => T_rel not in Str_int(X).
    => X^val =/= X.
    => B_ref endgueltig falsifiziert.
    => Kandidat C ist vollständig korrekt.                  (116.C.18.F)

  Falls kein solches phi existiert:
    Schluss NICHT: B_ref bewiesen.
    Schluss: X ist arithmetisch rigid (Ausgang B oder C).
    Dann muss die Rigiditsstruktur explizit identifiziert werden.
                                                             (116.C.18.F2)
```

### 116.C.18.4 — Kandidaten für Rigidität in X

```
Falls Ausgang B oder C (keine oder nur partielle Liftbarkeit):
  Welche Struktur von X blockiert Primzahlpermutationen?

Kandidaten (absteigend nach Plausibilität):

  (R1) N_+-Einbettung (konkrete multiplikative Struktur):
    X enthaelt N_+ mit seiner vollen multiplikativen Arithmetik.
    Primzahlen sind KEINE topologischen Symmetrien, sondern
    strukturelle Daten des Monoids.
    => Jede Primzahlpermutation bricht die Monoid-Struktur.
    => Ausgang B.  Stärkste Blockade.                       (R1)

  (R2) Hecke-Korrespondenzen:
    X enthaelt Hecke-Operatoren T_n, die nach Primfaktorzerlegung
    von n differenzieren.
    => T_n =/= T_{sigma(n)} fuer sigma-permutierte Primzahlen.
    => Primzahlpermutationen nicht Hecke-kompatibel.
    => Ausgang B.                                           (R2)

  (R3) Z-hat-Struktur (profinite Vervollständigung):
    X enthaelt Fasern ueber Z-hat = prod_p Z_p.
    Z_p-Fasern sind primspezifisch.
    => Primzahlpermutationen vermischen Z_p- und Z_q-Strukturen.
    => Nicht liftbar.  Ausgang B.                           (R3)

  (R4) n-Level-Geometrie:
    X enthaelt Level-n-Strukturen fuer spezifische n.
    Die Primfaktorzerlegung von n ist strukturell eingebaut.
    => Ausgang B oder C (je nach Level-Definition).          (R4)

  (R5) Lokale Index-/Restklassenstruktur:
    X enthaelt lokale Daten (Z/p^k Z-Restklassen, Indizes).
    Primzahlpermutationen permutieren die lokalen Strukturen.
    => Nicht liftbar, wenn lokale Isomorphieklassen verschieden.
    => Ausgang B oder C.                                    (R5)

Diagnose:
  R1 (N_+-Einbettung) ist die natuerlichste Rigiditsquelle
  und in den ueblichen Konstruktionen (Bost-Connes, etc.) vorhanden.
  Wenn X die konkrete multiplikative Monoid-Struktur von N_+ traegt,
  dann ist Ausgang B die wahrscheinliche Diagnose.           (116.C.18.4)
```

### 116.C.18.5 — Vorläufige Diagnose (auf Basis der verfügbaren Strukturdaten)

```
Basierend auf NEU-43, NEU-44, NEU-38 und der bisherigen
Katalog-Konstruktion von X:

  X traegt die konkrete multiplikative Struktur von N_+.
  Primkanten m -> p^k m sind durch die spezifischen Primzahlen p
  und Exponenten k definiert, nicht als nackte unlabelled Morphismen.
  => X_skel enthaelt bereits mehr als ein abstraktes freies Monoid.

  Vorlaeufige Diagnose: Ausgang B wahrscheinlich.
    Primzahlpermutationen liften nicht nach X,
    weil X die multiplikative Arithmetik von N_+ traegt (R1).

  Damit gilt:
    T_rel kommt nicht aus reiner Topologie,
    sondern aus der arithmetischen Rigidität von X (N_+-Monoid).

  B_ref in schwacher Form moeglicherweise gueltig:
    X traegt T_rel-kompatible Arithmetik (via R1),
    aber T_rel ist nicht topologisch-intrinsisch (IT-1/IT-3).  (116.C.18.5)
```

### 116.C.18.6 — Ergebnisformulierungen für den Katalog

```
AUSGANG A (falls bewiesen):

  X^val =/= X.  T_rel ist Zusatzstruktur.                   (116.C.18.A.K)

AUSGANG B (vorläufig wahrscheinlich):

  X ist arithmetisch rigid (R1: N_+-Monoid-Struktur).
  T_rel kommt nicht aus reiner Topologie,
  sondern aus arithmetischer Rigidität innerhalb von X.      (116.C.18.B.K)

AUSGANG C (falls partiell):

  X liegt strikt zwischen Skelett und Bewertungsobjekt:
    X_skel ⊊ X ⊊ X^val.                                   (116.C.18.C.K)
```

### 116.C.18.7 — Vierschichtensatz (Hauptergebnis)

```
+---------------------------------------------------------------+
| VIERSCHICHTENSATZ (NEU-116.C.18):                           |
|                                                               |
| Schicht 0: X_skel                                            |
|   Nacktes Divisibilitäts-/Kantenskelett.                    |
|   Aut(X_skel) => Sym(P): Primzahlpermutationen moeglich.    |
|   T_rel nicht intrinsisch.                                   |
|                                                               |
| Schicht 1: X                                                  |
|   Tatsächliche Residuenstruktur.                             |
|   Traegt konkrete N_+-Arithmetik (R1) oder andere Rigidität. |
|   Primzahlpermutationen vermutlich nicht liftbar (Ausgang B).|
|   T_rel arithmetisch ableitbar (via N_+-Struktur).           |
|                                                               |
| Schicht 2: X^val = (X, T_rel)                                |
|   X mit explizitem logarithmischem Kantencocycle.            |
|   T_rel additiv, aus Arithmetik (log auf N_+).               |
|   alpha-Familie T_alpha = alpha*T_rel; kein alpha intrinsisch.|
|                                                               |
| Schicht 3: W_xi^norm                                         |
|   Kritisch normierte Weil-Distribution.                      |
|   alpha = 1/2 durch externen Vergleich selektiert.           |
|   Re(s) = 1/2 ist der Bewertungsuebergang Schicht 2 -> 3.   |
|                                                               |
| Vierschichtensatz:                                            |
|   X_skel =/= X =/= X^val =/= W_xi^norm.                    |
+---------------------------------------------------------------+
                                                  (116.C.18.7)
```

### 116.C.18.8 — Präzisierter Programmsatz

```
Programmsatz (nach 116.C.18, Vierschichten-Version):

  Re(s) = 1/2 entsteht nicht aus X_skel.

  Praezise Herkunftsstruktur:

    X_skel    liefert die nackte Kantenform (Divisibilität).
    X         liefert arithmetische Rigidität (N_+-Monoid oder äquiv.).
    X^val     liefert die logarithmische Bewertung T_rel.
    W_xi^norm selektiert den kritischen Wert alpha = 1/2.

  Die kritische Gerade Re(s) = 1/2 ist der Uebergang:
    arithmetische Bewertung (X^val) -> Weil-Normierung (W_xi^norm).
                                                      (116.C.18.8)

Nicht Theta_{1/2} ist jetzt das Problem,
sondern die genaue Natur von X (Schicht 1).
```

### 116.C.18.9 — Statusuebersicht nach 116.C.18

```
Gesichert:
  - X_skel traegt kein intrinsisches T_rel (Primzahlperm.).  ✓[M]
  - Aut(X_skel) => Sym(P) auf dem Skelett.                   ✓[M]
  - Vierschichtensatz X_skel =/= X =/= X^val =/= W_xi^norm.  ✓[M]
  - Drei moegliche Ausgaenge A/B/C formuliert.                ✓[M]
  - Rigiditsquellen R1--R5 identifiziert.                     ✓[M]
  - Vorlaeufige Diagnose: Ausgang B (R1: N_+-Arithmetik).     ⚠[M]

Offen:
  - Entscheidung Ausgang A / B / C.                           ?[O]
  - Expliziter Nachweis der Rigiditsstruktur in X.            ?[O]
  - IT-2: konkreter Falsifikator oder Rigiditsnachweis.       ?[O]

Hauptaussage:
  Nicht Theta_{1/2}, sondern die Natur von X ist das restliche Problem.
```

Status:

```
116.C.18  Skelett-Rigidität-Liftbarkeit; Vierschichten      ✓[M]
IT-2      X-Rigidität vorläufig Ausgang B; Nachweis offen    ⚠/?[O]
```

---

## NEU-116.2 — Komponentensatz

```
Satz 116.Z: W_res^{top,crit}[Phi] = W_xi^norm[Phi]  fuer alle Phi in PW_t.
Mit NEU-113.7: = sum_gamma Phi-hat(gamma).             (116.2.2)
```

---

## NEU-116.3 — Bedeutung fuer Objekt X

```
X_skel --[iota_skel]--> X --[iota_val]--> X^val=(X,T_rel) --[rho^val]-->
  W_res^{top,crit} = W_xi^norm = W_zeros --[Q_Weil]--> RH.

Vierschichten:
  X_skel (nackt) -> X (rigid) -> X^val (bewertet) -> W_xi^norm (normiert).
```

---

## Satzstatusmatrix (NEU-116 gesamt)

| Test | Inhalt | Status |
|---|---|---|
| 116.A | W_res^{top,crit,0/1} =? E_{0,1} | ?[O] |
| 116.B | W_res^{top,crit,Gamma} =? G | ?[O] |
| 116.C_1 | Ort: k log p | ?[O] |
| 116.C_2 | Gewicht: log p | ?[O] |
| 116.C_3 | Theta_{1/2} extern; M3 in W_res^top? | ⚠/?[O] |
| 116.C_4 | Vorzeichen: Minus | ?[O] |
| 116.C | W_res^{top,crit,prime} =? -P | ?[O] |
| 116.Z | W_res^{top,crit} = W_xi^norm | ?[O] |
| 116.C.12 | Modularlemma + Inspektionsprotokoll | ✓[M] |
| 116.C.13 | Ableseschritt; Kandidat C > B | ✓[M] |
| 116.C.14 | Internalisationstest; zweistu. Architektur | ✓[M] |
| 116.C.15 | Internalitaetstest (4 Subtests) | ✓[M] |
| 116.C.16 | Funktorialitaetsbruch; X^val-Architektur | ✓[M] |
| 116.C.17 | Intrinsizitaetstest T_rel in X; Dreischichten | ✓[M] |
| 116.C.18 | Skelett-Rigidität-Liftbarkeit; Vierschichten | ✓[M] |

---

## Anschluesse

| Voraussetzung | Quelle |
|---|---|
| W_xi^norm = E_{0,1}+G-P | NEU-113.7 |
| Lambda(n)/sqrt(n)-Normierung | NEU-113.4 |
| Primkanten m->p^k m, Gewicht log p | NEU-114.4 ⚠[M] |
| T_rel(m->p^k m) = k log p | NEU-43 |
| e^{-sT_rel} = p^{-ks} auf Primkanten | NEU-43 |
| Graph-Schicht noetig fuer T_rel | NEU-44 |
| KMS-Gewichtung n^{-beta} auf V_n | NEU-38 |
| Zweistufige Architektur | 116.C.14.5 |
| Theta_{1/2} = e^{-(1/2)T_rel} | 116.C.14.2 |
| Theta_{1/2} topol. extern (ST-3/ST-4) | 116.C.15.3/4 |
| X^val = (X, T_rel) Lifting-Objekt | 116.C.16.3 |
| B_ref-Bedingung | 116.C.16.6 |
| IT-1/3/4: T_rel extern | 116.C.17 |
| Dreischichtensatz | 116.C.17.7 |
| Programmsatz Re(s)=1/2 | 116.C.17.8 |
| X_skel: Aut => Sym(P) | 116.C.18.1 |
| T_rel not in Str_int(X_skel) | 116.C.18.1b |
| Drei Ausgaenge A/B/C | 116.C.18.2 |
| Rigiditsquellen R1--R5 | 116.C.18.4 |
| Vorl. Diagnose: Ausgang B (R1) | 116.C.18.5 |
| Vierschichtensatz | 116.C.18.7 |
| Praezisierter Programmsatz | 116.C.18.8 |
| 116.C_3 Halbdichte => NEU-114.4 ✓[M] | konditionell |
