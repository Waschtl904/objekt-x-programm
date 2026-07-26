# Kritischer Pfad — Gesamtuebersicht (Stand: 1. Juli 2026, NEU-114)

Dieses Dokument ist die zentrale, stets aktuelle Uebersicht ueber den
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
  m_arith = Herglotz-Traeger des Nullstellenanteils, nicht Q_Weil
  Renormierungstest: m_{Gamma,ren}+Pol+Prim =? Q_Gamma+Q_poles+Q_prime  ?[O]
[alle frueheren Notationen bleiben gueltig]
```

---

## Hauptziel

```
RH  <=>  Spec(lim A_N^{Jac,-}) subset R  <=>  m_arith(z) Herglotz  (NEU-63D)

Architektur (ab NEU-114):
  Objekt X  ->  Pi_gamma(X) = m_arith  ->  Q_Weil  ->  RH
```

---

## Zwei parallele Spuren (ab NEU-114)

```
Spur A: Spektralschatten-Spur  (NEU-77-113, aktiv)
  Pi_gamma(X) = m_arith -> Q_Weil -> RH-Kanal
  Flaschenhals: NEU-113 Bombieri-Normalisierung

Spur B: X-Rueckbindungs-Spur  (NEU-114, reaktiviert)
  Test 114.1: HH2 [omega_2] -> Herglotz-Kanal      ?[O]
  Test 114.2: HH4 [L_3] -> Obstruktionsterm         ?[O]
  Test 114.3: W_res^top -> Q_Weil                   ?[O]
  Test 114.4: m->p^k m -> Lambda(p^k)               ⚠[M]
```

---

## Gesicherter Kern

```
[Feshbach-Kette bis NEU-111: unveraendert]
NEU-112:
  Satz 112.1: m_arith Stieltjes-Nullstellenmass sum_gamma delta_gamma  [M]
  Satz 112.2: Nullstellenterm -> sum|f-hat(gamma)|^2 strukturell       [M]/⚠
  Satz 112.3: m_arith = Herglotz-Traeger Nullstellenanteil, nicht X    [M]
NEU-114:
  Satz 114.0: m_arith = Pi_gamma(X), nicht X selbst                    [M]
  Test 114.4: m->p^k m -> Lambda(p^k) teilweise gesichert              ⚠[M]
```

---

## No-Go-Resultate (x[M])

```
[alle vorherigen bleiben]
(kein neues No-Go in NEU-112-114)
"X = m_arith"  ->  kategorial falsch (NEU-114)                        x[M]
```

---

## Offene Kerne (?) nach Dringlichkeit

```
1. NEU-113: Bombieri-Normalisierung exakt fixieren   <- FLASCHENHALS SPUR A
   Q_zeros/Q_Gamma/Q_prime auf PW_t
   m_arith einsetzen; Vorzeichen/Normierung
   dann: m_{Omega,N}->m_arith => Q_{Omega,N}->Q_Weil?

2. NEU-114 Test 114.3: W_res^top -> Q_Weil           <- FLASCHENHALS SPUR B
   zentraler Rueckbindungstest

3. NEU-114 Test 114.1/2: HH2/HH4 -> Herglotz/Obstruktion

4. Jacobi-Realisierungstest: m_{Omega,N}->m_arith  (nach NEU-113)

5. NEU-101.2: Transferlemma V_{N,H}^Delta ~ V(M,H)  [noch offen]
```

---

## Kritischer Pfad Detail (NEU-112 bis 114)

```
NEU-111 Herglotz-Weil-Bruecke; Pfadordnung; No-Go Jacobi=/=Connes-Weil   [M]/?[O]
NEU-112 Herglotz-Weil-Test:                                               [M]/?[O]
        m_arith = Spektralschatten Pi_gamma(X)  [M]
        Stieltjes-Nullstellenmass  [M]
        Nullstellenterm strukturell  [M]/⚠
        Renormierungstest offen  ?[O]
  +-- NEU-113: Bombieri-Normalisierung exakt   <- FLASCHENHALS SPUR A
NEU-114 Kursabgleich: Rueckbindung Schatten -> X:                        ?[O]
        m_arith = Pi_gamma(X), nicht X  [M]
        Test 114.3: W_res^top -> Q_Weil   <- FLASCHENHALS SPUR B
        Test 114.1/2: HH2/HH4  ?[O]
        Test 114.4: Primkanten  ⚠[M]
NEU-63D m_arith Herglotz <=> RH                                          ⚠[M]
```

---

## Weg B — Hauptpfad (aktualisiert NEU-114)

```
Feshbach + Bochner-Tor + Skalenleiter (NEU-77-98)                       [M]
  +
Singulaerserien + Shift + G.-M. (NEU-99-102)                           [M]/⚠
  +
Entfaltung + Rampen-Test + LFF (NEU-103-110)                           [M]
  +
Herglotz-Weil-Bruecke (NEU-111-112):                                   [M]/?[O]
  m_arith = Pi_gamma(X) = Spektralschatten
  Nullstellenterm strukturell positiv
  Renormierung: Q_Gamma+Q_poles+Q_prime offen
  +
NEU-113: Bombieri-Normalisierung (SPUR A FLASCHENHALS)
  m_{Omega,N} -> Q_Weil?
  +
NEU-114: Rueckbindung Pi_gamma(X) -> X (SPUR B FLASCHENHALS)
  W_res^top -> Q_Weil?
  HH2/HH4 -> Herglotz/Obstruktion?
  Primkanten -> Lambda(p^k)?
  +
m_arith(z) Herglotz <=> RH  (NEU-63D)                                 ⚠[M]
```

---

## Kataloglücke: NEU-126 (bewusst fehlend)

```
NEU-125  Intrinsische Feshbach-Skala vor Lanczos              [gepusht 6. Juli 2026]
NEU-126  Rückleseprotokoll W_N (NEU-62)                       [FEHLT — bewusst]
         Grund: 126.A und 126.B verloren; nur Gesamtzweck
         und 126.C inhaltlich bekannt. Rekonstruktion aus
         Zusammenfassungen methodisch nicht vertretbar.
         Inhaltlicher Anschluss läuft direkt über NEU-127.
NEU-127  Kanalseiten-Gramform-Triage: Klasse A vs. Klasse B   [M/❓O]
```

---

## Literatur

- Bombieri: *Remarks on Weil's quadratic functional in number theory* (2000)
- Connes: *Trace formula in noncommutative geometry* (1999)
- Connes & Consani: *PSWF-Korrekturen / archimedische Terme*
- Goldston & Montgomery: *Pair correlation* (1987)
- Montgomery: *Pair correlation of zeros* (1973)
- Weil: *Sur les formules explicites*
