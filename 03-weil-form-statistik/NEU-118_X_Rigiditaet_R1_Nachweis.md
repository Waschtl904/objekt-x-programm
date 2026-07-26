# NEU-118 — X-Rigidität I: R1-Nachweis der N⁺-Monoid-Blockade

**Stand: 3. Juli 2026**

**Rückverweis:** NEU-117_X_Rigiditaet_R1.md (Rahmensetzung, Leitfrage, Statusmatrix R1–R5)

---

## Ziel dieses Blatts

NEU-117 hat die Leitfrage formuliert und die fünf Rigiditätskandidaten R1–R5
identifiziert. Die vorläufige Diagnose lautete:

```
Ausgang B wahrscheinlich: X ist arithmetisch rigid via R1 (N⁺-Monoid).
```

Dieses Blatt führt den **R1-Nachweis** explizit durch:

```
Falls X die konkrete multiplikative N⁺-Monoid-Struktur trägt,
dann liftet keine nichttriviale Primzahlpermutation nach Aut(X).
```

Das entspricht der Entscheidung

```
IT-2  (116.C.17):  Ausgang B  (116.C.18.2).
```

---

## 118.1 — Was R1 genau behauptet

```
R1-These:
  X enthält N⁺ mit seiner vollen multiplikativen Arithmetik.
  Primzahlen sind KEINE topologischen Symmetrien von X,
  sondern strukturelle Daten des Monoids N⁺.
  => Jede Primzahlpermutation bricht die Monoid-Struktur.
  => Ausgang B: Kein sigma in Sym(P) \ {id} liftet nach Aut(X).  (R1)
```

**Unterschied zum Skelett X_skel:**

```
X_skel:  Kantenskelett, Kanten m -> nm  (n, m in N⁺).
         Kein arithmetisches Label außer Quelle/Ziel.
         Aut(X_skel) => Sym(P)  (Permutationen erlaubt).

X:       Trägt ZUSÄTZLICH die Monoid-Kompositionsstruktur von N⁺.
         Konkret: Kante (m -> nm) trägt das Label n in N⁺.
         Komposition von Kanten entspricht Multiplikation in N⁺.
```

Der Unterschied ist präzis:

```
X_skel  kennt nur die Relation m | nm  (Teilbarkeit).
X       kennt das spezifische n in N⁺  als Multiplizierungsoperator.
```

---

## 118.2 — Drei Formalversionen des R1-Tests

### 118.2.V1 — Monoid-Homomorphismus-Version

```
Sei sigma in Sym(P), sigma =/= id.
Sei phi_sigma : X -> X der induzierte Kandidaten-Automorphismus:
  phi_sigma(m -> p^k m) = m -> sigma(p)^k m.

R1-Blockade (V1):
  phi_sigma ist kein Automorphismus von X,
  weil phi_sigma die Monoid-Multiplikation nicht erhält.

Beweis:
  In X gilt für zwei Primkanten:
    (m -> p m) o (m -> q m) = m -> pq m.
  Unter phi_sigma:
    phi_sigma(m -> p m) = m -> sigma(p) m,
    phi_sigma(m -> q m) = m -> sigma(q) m.
  Die Komposition ist:
    m -> sigma(p) sigma(q) m.
  Der Bildwert der zusammengesetzten Kante wäre:
    phi_sigma(m -> pq m) = m -> sigma(p)^{v_p(pq)} sigma(q)^{v_q(pq)} m
                         = m -> sigma(p) sigma(q) m.
  (Hier stimmt es scheinbar noch.)

Aber: Für gemischte Primzahlpotenzen:
  Die Kante m -> p^a q^b m hat Label n = p^a q^b in N⁺.
  Unter phi_sigma:
    phi_sigma(n) = sigma(p)^a sigma(q)^b.
  Die Kompositionsstruktur von N⁺ ist erhalten, sofern sigma
  als Permutation der Primzahlen aufgefasst wird.

Diagnose V1:
  Als abstrakte Monoid-Permutation ist phi_sigma KEIN Widerspruch
  zu N⁺-Komposition. Die Kompositionsstruktur ist symmetrisch
  unter Primzahlpermutationen, wenn N⁺ als freies kommutatives
  Monoid mit Erzeugendenmenge P betrachtet wird.

  => V1 allein reicht NICHT für die R1-Blockade.             (118.2.V1.neg)
```

**Das ist der entscheidende Befund:** Abstraktes freies Monoid blockiert nicht.

### 118.2.V2 — Ordnungsstruktur-Version (konkrete N⁺-Einbettung)

```
N⁺ ist NICHT nur ein freies kommutatives Monoid mit Erzeugendenmenge P.
N⁺ ist eingebettet in (Z, +, *) oder mindestens in (Q_{>0}, *).
Die Einbettung ist Teil der kanonischen Konstruktion von X
(via NEU-43/44: Bost-Connes-Analogon).

Die konkrete Ordnung auf N⁺:
  1 < 2 < 3 < 4 < 5 < ...
ist durch die Additionsstruktur von Z definiert, nicht durch
die Primzahlstruktur.

R1-Blockade (V2):
  sigma(2) =/= 2 => sigma(2) >= 3 (da sigma bijektiv auf P).
  Dann gilt:
    2 + 2 = 4  in Z,
    sigma(2) + sigma(2) >= 6  in Z.
  Die Einbettung N⁺ -> Z -> Q ist nicht sigma-äquivariant:
    sigma(2 + 2) = sigma(4) = sigma(2^2),
    sigma(2) + sigma(2) = 2 sigma(2) =/= sigma(4) im Allgemeinen.

  Konkret: sigma(4) = sigma(2)^2 (als Potenzstruktur),
  aber 4 = 2 + 2 in Z und sigma(2+2) =/= sigma(2) + sigma(2)
  wenn sigma die Addition nicht erhält.

  => phi_sigma bricht die Additionsstruktur von Z.
  => phi_sigma in Aut(X) nur wenn X keine Z-Additionsstruktur trägt.
                                                             (118.2.V2)
```

### 118.2.V3 — Metrische Version (Bewertung)

```
Die kanonische N⁺-Einbettung induziert eine p-adische Bewertung v_p
für jede Primzahl p:
  v_p : N⁺ -> N_0,  v_p(p^k m) = k  (p nmid m).

Eine Primzahlpermutation sigma permutiert die Bewertungen:
  v_{sigma(p)} = v_p o phi_sigma^{-1}.

Falls X die Bewertungsdaten {v_p}_{p in P} intrinsisch trägt
(z.B. als lokale Daten der Bost-Connes-Algebra oder als
profinite Fasern über Z-hat = prod_p Z_p),
dann ist phi_sigma kein Automorphismus von X,
weil sigma die lokalen Daten v_p und v_{sigma(p)} vertauscht,
die aber auf verschiedenen Primfasern Z_p und Z_{sigma(p)} leben:
  Z_p =/= Z_{sigma(p)}  als topologische Ringe (R3).

  => phi_sigma in Aut(X) nur wenn X keine Bewertungsdaten trägt.
                                                             (118.2.V3)
```

---

## 118.3 — Kernfrage: Was ist X kanonisch?

```
Die R1-Blockade ist in V2 und V3 REAL, in V1 NICHT.

Der Test reduziert sich auf:

  Trägt X die N⁺-Einbettung in Z (V2) oder
  die Bewertungsstruktur {v_p} (V3)?
  => Dann Ausgang B.

  Trägt X nur das abstrakte freie Monoid (V1-Niveau)?
  => Dann kein R1-Blockade, weiter zu R2–R5.

Diese Frage ist durch NEU-43/44 zu beantworten.
```

### 118.3.1 — Auswertung der verfügbaren Strukturdaten

```
NEU-43/44 konstruieren X über:
  - Bost-Connes-analoges Kreuzprodukt C(Z-hat) ⋊ N⁺.
  - Z-hat = prod_p Z_p als Basis-Raum.
  - Isometrien V_n : n-te Hecke-Korrespondenz.
  - KMS-Gewichtung n^{-beta} auf V_n.

Befund:
  X enthält Z-hat = prod_p Z_p als Basisraum.
  Die Fasern Z_p sind primspezifisch.
  => V3 ist auf dem Niveau von NEU-43/44 erfüllt.

  X enthält V_n als explizite Hecke-Operatoren,
  die nach Primfaktorzerlegung von n differenzieren.
  => R2 (Hecke) ist ebenfalls erfüllt.

Vorläufiger Befund:
  X trägt gemäß NEU-43/44 die Strukturen V2 und V3.
  => R1-Blockade über V3 ist auf diesem Niveau plausibel gesichert.
  => Ausgang B ist die strukturell korrekte Diagnose.        (118.3.1)
```

---

## 118.4 — Formaler R1-Satz

```
Satz 118.R1 (R1-Blockade, konditionell):

  Angenommen:
  (H1) X enthält Z-hat = prod_p Z_p als Basisraum (gemäß NEU-43/44).
  (H2) Die Primfasern Z_p sind Teil der Struktur von X.
  (H3) Aut(X) erhält die Faserstruktur über Z-hat.

  Dann gilt:
    Für alle sigma in Sym(P) mit sigma =/= id:
      phi_sigma not in Aut(X).

  Beweis:
    Sei sigma(p) = q =/= p für ein p in P.
    Dann würde phi_sigma die Faser Z_p auf Z_q abbilden:
      phi_sigma : Faser über Z_p -> Faser über Z_q.
    Da Z_p =/= Z_q als topologische Ringe (da p =/= q: |Z_p| = p^infty, |Z_q| = q^infty),
    ist phi_sigma kein Automorphismus der Faserstruktur.
    Widerspruch zu (H3).
    => phi_sigma not in Aut(X).                               []  (118.R1)

  Status: ✓[M] konditionell unter H1–H3.
  Offen: Verifikation von H3 aus Definition von X in NEU-43/44.  ?[O]
```

---

## 118.5 — Konsequenzen für das Gesamtprogramm

```
Falls Satz 118.R1 gilt:

(K1) Ausgang B (116.C.18.2) ist bestätigt.
     => Im(Aut(X_skel) -> Aut(X)) = {id}.
     => X ist arithmetisch rigid.

(K2) T_rel kommt nicht aus reiner Topologie,
     sondern aus der arithmetischen Rigidität von X (N⁺/Z-hat-Struktur).
     => IT-2 (116.C.17): Falsifikator für B_ref gefunden
        (falls phi_sigma rho-strukturtreu wäre und nicht liftet).
     => B_ref endgültig falsifiziert (116.C.18.F).

(K3) Der präzisierte Programmsatz (116.C.18.8) gilt:
     X_skel   -> nackte Kantenform
     X        -> arithmetische Rigidität (Z-hat, N⁺)
     X^val    -> logarithmische Bewertung T_rel
     W_xi^norm -> Selektion alpha = 1/2

(K4) Nächster Schritt: NEU-119 — H3-Verifikation aus NEU-43/44.
     Explizite Faserstruktur von X und Automorphismengruppe bestimmen.
```

---

## 118.6 — Offene Restfrage (O1-präzisiert)

```
O1 (aus NEU-117): Welche Rigiditätsquelle R1–R5 ist definitiv Teil von X?

Präzisierung nach 118.3:
  - R1 (V3) und R2 sind auf NEU-43/44-Niveau strukturell vorhanden.
  - R3 (Z-hat) ist explizit Teil der Konstruktion.
  - R1 (V1, abstraktes Monoid) allein reicht nicht.

Restfragen:
  (O1a) Ist H3 (Automorphismen erhalten Faserstruktur) explizit beweisbar
        aus der Definition von Aut(X) in NEU-43/44?             ?[O]
  (O1b) Sind R4/R5 ebenfalls vorhanden (würde Redundanz schaffen)?  ?[O]
  (O1c) Reicht Z-hat-Faserstruktur für vollständigen Nachweis
        ohne Rückgriff auf Z-Additionsstruktur (V2)?             ?[O]
```

---

## Satzstatusmatrix (NEU-118)

| Satz | Inhalt | Status |
|---|---|---|
| 118.V1 | Abstraktes freies Monoid blockiert nicht (Nullbefund) | ✓[M] |
| 118.V2 | N⁺-Einbettung in Z blockiert sigma via Additionsbruch | ✓[M] kond. |
| 118.V3 | Z-hat-Faserstruktur blockiert sigma (R3-Redundanz mit R1) | ✓[M] kond. |
| 118.3.1 | NEU-43/44 liefert V3-Struktur; Ausgang B plausibel | ⚠[M] |
| 118.R1 | R1-Blockade konditionell unter H1–H3 | ✓[M] kond. |
| 118.K2 | IT-2: Ausgang B falsifiziert B_ref | ⚠[M] |
| O1a | H3-Verifikation aus NEU-43/44 | ?[O] |
| O1b | R4/R5 vorhanden? | ?[O] |

---

## Anschlüsse

| Quelle | Inhalt |
|---|---|
| NEU-117 | Rahmensetzung, R1-Leitfrage, Statusmatrix R1–R5 |
| NEU-116.C.18 | Ausgänge A/B/C, Vierschichtensatz |
| NEU-43/44 | Konstruktion X via BC-Analogon, Z-hat, V_n, KMS |
| NEU-38 | KMS-Gewichtung n^{-beta} |
| → NEU-119 | H3-Verifikation: Aut(X) und Faserstruktur aus NEU-43/44 |
