# Kritischer Pfad — Gesamtübersicht (Stand: 28. Juli 2026, NEU-249/NEU-250)

Dieses Dokument ist die zentrale, stets aktuelle Übersicht über den
kritischen Pfad des RH-Fragenkatalogs.

---

## Notationskonventionen (ab NEU-79 verbindlich)

```
NEU-114 (Kursabgleich):
  m_arith  =  Pi_gamma(X)   -- Spektralschatten, nicht X selbst
  aktueller Pfad NEU-77-113 = Pi_gamma-Analyse von X
  X-Rückbindung: vier Tests in NEU-114

NEU-112:
  mu_xi = sum_gamma delta_gamma + mu_{Gamma,ren}  (Stieltjes-Nullstellenmass)
  Q_zeros[f] = sum_gamma |f-hat(gamma)|^2         (Nullstellenterm Bombieri)
  Q_Weil[f] = Q_zeros + Q_Gamma + Q_poles + Q_prime  (volle Form, Normierung offen)
  m_arith = Herglotz-Träger des Nullstellenanteils, nicht Q_Weil
  Renormierungstest: m_{Gamma,ren}+Pol+Prim =? Q_Gamma+Q_poles+Q_prime  ?[O]

NEU-229 (O229-Architektur ab NEU-229):
  Rohkopplung T_p^raw: Hebungsfaser + Mischblock-Gram
  u-Regulator = Hebungswahl (NEU-228)
  O229-Unterknoten: 2a (Symmetrie/GNS), 2b (NEU-041-Brücke), 3B1 (Transgression)

NEU-247ff (Koszul-Typbrücke ab NEU-246):
  Koszul-Kandidat: Typ-Grad-Kerninvarianz (NEU-246)
  Tensor-Lift-Typbrücke: Bewertungsableitungen (NEU-247/247a/247b)
  c2b2a-Wohldefiniertheit: Tensoroperator (NEU-248)
  Präzisierungen Notation/Konstruktion/Stabilität (NEU-249)

[alle früheren Notationen bleiben gültig]
```

---

## Hauptziel

```
RH  <=>  Spec(lim A_N^{Jac,-}) subset R  <=>  m_arith(z) Herglotz  (NEU-63D)

Architektur (ab NEU-229):
  Objekt X  ->  Pi_gamma(X) = m_arith  ->  Q_Weil  ->  RH
               |
               v
          T_p^raw (Rohkopplung, Hebungsfaser)
               |
          O229-Unterknoten (Symmetrie, Transgression, Koszul)
               |
          NEU-246–249: Koszul-Typbrücke, c2b2a-Wohldefiniertheit
               |
          NEU-250: [nächster Schritt — siehe unten]
```

---

## Drei parallele Spuren (Stand NEU-249)

```
Spur A: Spektralschatten-Spur  (NEU-77–113, gesichert)
  Pi_gamma(X) = m_arith -> Q_Weil -> RH-Kanal
  Flaschenhals: NEU-113/118/120 Bombieri-Normalisierung
  Status: Normierung strukturell klar, Grenzübergang m_{Omega,N}->m_arith offen

Spur B: X-Rückbindungs-Spur  (NEU-114–173, aktiv)
  Test 114.1: HH2 [omega_2] -> Herglotz-Kanal             ?[O]
  Test 114.2: HH4 [L_3] -> Obstruktionsterm               [M] (NEU-176)
  Test 114.3: W_res^top -> Q_Weil                          ?[O]
  Test 114.4: m->p^k m -> Lambda(p^k)                     ⚠[M]
  L3-Typfundament: NEU-171–173                             [M]

Spur C: O229-Rohkopplungs-/Koszul-Spur  (NEU-229–249, aktiv)
  O229-2a: Symmetrieklassifikation kanonischer Randvektor  [M] (NEU-230)
  O229-2a-ii: Wres-Äquivarianz Fixraum/Nullraum            [M] (NEU-231)
  O229-2a-ii-2b: NEU-041-Brückenaudit                      [M] (NEU-232)
  O229-2a-iii: Ladungsgraduierung P_ch                     [M] (NEU-234)
  O229-2a-i: GNS-Typisierung Rohzielraum                   [M] (NEU-235)
  O229-2: Formaler Abschluss                               x[M] neg. (NEU-236)
  O229-3B1: Transgression + Quellenaudit                   [M] (NEU-238/239)
  O229-3B1f-b: Kettenabbildungs-Audit T_p^raw              ?[O] (NEU-241)
  O229-3B1f-b1: Quell-/Zielkomplex-Audit                  ?[O] (NEU-242, Ordner 01)
  Koszul-Kandidat Typ-Grad-Kerninvarianz                   [M] (NEU-246)
  Tensor-Lift-Typbrücke                                    [M] (NEU-247/247a/247b)
  c2b2a-Wohldefiniertheit Tensoroperator                   [M] (NEU-248)
  Präzisierungen Notation/Konstruktion/Stabilität          [M] (NEU-249)
  FLASCHENHALS SPUR C: NEU-250 — inhaltlicher Anschluss offen
```

---

## Gesicherter Kern

```
[Feshbach-Kette bis NEU-111: unveraendert]
NEU-112:
  Satz 112.1: m_arith Stieltjes-Nullstellenmass sum_gamma delta_gamma  [M]
  Satz 112.2: Nullstellenterm -> sum|f-hat(gamma)|^2 strukturell       [M]/⚠
  Satz 112.3: m_arith = Herglotz-Träger Nullstellenanteil, nicht X    [M]
NEU-114:
  Satz 114.0: m_arith = Pi_gamma(X), nicht X selbst                   [M]
  Test 114.4: m->p^k m -> Lambda(p^k) teilweise gesichert             ⚠[M]
NEU-171–173:
  L3-Typfundament vollständig etabliert                               [M]
NEU-229–235:
  O229-Rohkopplungsarchitektur, Symmetrie, GNS-Typisierung            [M]
NEU-236:
  O229-2 Negativbefund formaler Abschluss                            x[M]
NEU-238–239:
  Transgression O229-3B1: Quellenaudit abgeschlossen                  [M]
NEU-246–249:
  Koszul-Typbrücke + c2b2a-Wohldefiniertheit                         [M]
```

---

## No-Go-Resultate (x[M])

```
[alle vorherigen bleiben]
"X = m_arith"  ->  kategorial falsch (NEU-114)                       x[M]
O229-2: Formaler Abschluss negativ — kein direkter Lift via O229-2   x[M] (NEU-236)
O229-3B1f-b1: Kettenabbildungs-Negativbefund (in 07: NEU-242)        x[M]
Kone-No-Go (NEU-244): tautologischer Cone ist kein Ausweg            x[M]
```

---

## Offene Kerne (?) nach Dringlichkeit

```
1. NEU-250: Anschluss an NEU-249             <- FLASCHENHALS SPUR C (aktuell)
   Präzisierungen Notation/Konstruktion/Stabilität abgeschlossen (NEU-249)
   Nächster Knoten: [inhaltlich zu bestimmen bei NEU-250]

2. NEU-242: O229-3B1f-b1 Quell-/Zielkomplex-Audit T_p^raw
   (liegt in 07-weil-explizitformel, Negativbefund x[M])
   Folgepfad aus Negativbefund noch offen

3. NEU-114 Test 114.3: W_res^top -> Q_Weil  <- FLASCHENHALS SPUR B
   zentraler Rückbindungstest, noch nicht gelöst

4. NEU-113/118/120: Bombieri-Normalisierung Grenzübergang
   m_{Omega,N}->m_arith => Q_{Omega,N}->Q_Weil?

5. NEU-114 Test 114.1: HH2 -> Herglotz-Kanal  [noch offen]

6. NEU-101.2: Transferlemma V_{N,H}^Delta ~ V(M,H)  [noch offen]
```

---

## Kritischer Pfad Detail (NEU-220 bis 250)

```
NEU-220–220w  Weil-Explizitformel, Gammafaktor, Konturtransport,
              Kreinraum, Spektraldeterminante, Hankelvollständigkeit    [M]
NEU-221–221e  Adelische Momentquelle, Feshbach-Weyl-Kandidat,
              Hebungsfaser, Spektralmassabstieg                         [M]
NEU-222       Trassenaudit singuläre Route                              [M]
NEU-223–228   Quellenaudit, Kern, Primfaser, Gram, u-Regulator         [M]
NEU-229       Verbundene Form + Mischblock-Gram Hebungsfaser            [M]
NEU-230–235   O229-2a Symmetrie, Wres-Äquivarianz, NEU-041-Brücke,
              Ladungsgraduierung, GNS-Typisierung                       [M]
NEU-236       O229-2 Formaler Abschluss NEGATIV                       x[M]
NEU-237–239   O229-3/3B/3B1 Randdatum, Transgression, Quellenaudit    [M]
NEU-240–241   O229-3B1f-a/b Minimalitäts- + Kettenabbildungsaudit     ?[O]
NEU-242 (01)  O229-3B1f-b1 Quell-/Zielkomplex Audit T_p^raw          x[M] neg
NEU-242 (07)  Abschlussaudit Kettenabbildungs-Negativbefund           x[M]
NEU-243       Kompatibilitätsfirewall Quell-/Zielkomplex               [M]
NEU-244       Quotient-first + Cone-No-Go                             x[M]
NEU-245       c2a Operatortypaudit NEU-195/216                         [M]
NEU-246       Koszul-Kandidat Typ-Grad-Kerninvarianz                   [M]
NEU-247–247b  Tensor-Lift-Typbrücke, Domänenpräzisierung               [M]
NEU-248       c2b2a-Wohldefiniertheit Tensoroperator                   [M]
NEU-249       Präzisierungen Notation/Konstruktion/Stabilität          [M]
NEU-250       [NÄCHSTER KNOTEN — Flaschenhals Spur C]                 ?[O]
```

---

## Weg B+C — Hauptpfad (aktualisiert NEU-249)

```
Feshbach + Bochner-Tor + Skalenleiter (NEU-77–98)                    [M]
  +
Singulaerserien + Shift + G.-M. (NEU-99–102)                         [M]/⚠
  +
Entfaltung + Rampen-Test + LFF (NEU-103–110)                         [M]
  +
Herglotz-Weil-Brücke (NEU-111–112):                                  [M]/?[O]
  m_arith = Pi_gamma(X) = Spektralschatten
  +
Bombieri-Normalisierung (NEU-113/118/120) — SPUR A FLASCHENHALS
  m_{Omega,N} -> Q_Weil?  offen
  +
Rückbindung Pi_gamma(X) -> X (NEU-114–173) — SPUR B FLASCHENHALS
  W_res^top -> Q_Weil?  offen
  L3-Typfundament: etabliert (NEU-171–173)  [M]
  +
Rohkopplungs-Architektur O229 (NEU-229–235):                         [M]
  Symmetrie, GNS, Äquivarianz, Ladungsgraduierung
  O229-2 Negativbefund: x[M] (NEU-236)
  +
Transgression O229-3B1 (NEU-238–241):                                [M]/?[O]
  Kettenabbildung T_p^raw: Negativbefund (NEU-242)  x[M]
  +
Kone-No-Go + Kompatibilitätsfirewall (NEU-243–245):                  [M]/x[M]
  +
Koszul-Typbrücke + c2b2a (NEU-246–249):                              [M]
  Wohldefiniertheit Tensoroperator gesichert
  +
NEU-250: [NÄCHSTER KNOTEN]                                           ?[O]
  +
m_arith(z) Herglotz <=> RH  (NEU-63D)                               ⚠[M]
```

---

## Kataloglücken (bewusst fehlend)

```
NEU-126: Rückleseprotokoll W_N (NEU-62)
  Grund: 126.A und 126.B verloren; Rekonstruktion methodisch
  nicht vertretbar. Anschluss läuft direkt über NEU-127.

NEU-129: [Inhalt unbekannt, bewusst übersprungen]

NEU-191, NEU-198: In 06-hochschild-bc-algebra fehlend.
  Status: offen — ob bewusst oder Lücke, klären.

NEU-221a, NEU-221b: In 07-weil-explizitformel fehlend.
  Status: offen.
```

---

## Literatur

- Bombieri: *Remarks on Weil's quadratic functional in number theory* (2000)
- Connes: *Trace formula in noncommutative geometry* (1999)
- Connes & Consani: *PSWF-Korrekturen / archimedische Terme*
- Goldston & Montgomery: *Pair correlation* (1987)
- Montgomery: *Pair correlation of zeros* (1973)
- Weil: *Sur les formules explicites*
- Laca & Raeburn: *BC-Algebra und Dilatationen* (Referenz für NEU-219i)
