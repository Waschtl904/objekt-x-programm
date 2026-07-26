# NEU-121 — Renormierter Moment-0/1-Abgleich gegen den Hadamard-Koeffizienten

**Stand: 4. Juli 2026**

**Rückverweis:** NEU-120 (Grenzübergangsstruktur), NEU-119 (Definition m_{Omega,N}),
NEU-63D (m_arith Herglotz <=> RH), NEU-113 (Bombieri-Normalisierung)

---

## Vorsatz (Renormierungswarnung)

```
Die rohe Momentenentwicklung

  m_{Omega,N}(z) = -1/z - <Omega_N, A_N^{Jac,-} Omega_N>/z^2 - ...

ist eine Cauchy-Transformierte eines endlichen Spektralmasses.

m_arith(z) = -i xi'(1/2+iz) / xi(1/2+iz)

ist dagegen KEIN endliches Spektralmass-Objekt:
Die Hadamard-Darstellung der xi-Funktion enthalt Renormierungsterme
(Gamma-Beitrag, Pol-Beitrag, logarithmischer Counterterm).

Daher ist ein roher Vergleich

  <Omega_N, A_N^{Jac,-} Omega_N>  =?=  sum_rho 1/rho

falsch: Die rechte Seite ist nicht absolut konvergent;
sie ist nur als symmetrisch paarweiser Limes definiert.

NEU-121 definiert zuerst den richtigen renormierten Vergleichsgegenstand,
bevor die drei Omega_N-Kandidaten getestet werden.
                                                      (121.Vorsatz)
```

---

## 121.1 — Resolventenentwicklung von m_{Omega,N} bei z -> infty

```
Fuer ||Omega_N|| = 1 und z -> infty auf C^+ gilt:

  m_{Omega,N}(z) = <Omega_N, (A_N^{Jac,-} - z)^{-1} Omega_N>
                 = sum_{k=0}^{infty} (-1)^{k+1} * M_k / z^{k+1}

mit den Momenten:

  M_0  :=  <Omega_N, Omega_N>                 = 1
  M_1  :=  <Omega_N, A_N^{Jac,-} Omega_N>    (erster Moment)
  M_2  :=  <Omega_N, (A_N^{Jac,-})^2 Omega_N> = ||A_N^{Jac,-} Omega_N||^2

Also:

  m_{Omega,N}(z) = -1/z - M_1/z^2 - M_2/z^3 - ...

Die Momente M_k sind endlich fuer endliches N
(da A_N^{Jac,-} selbstadjungiert und dim H_N = |I_N| < infty).

Entscheidend: M_1 = <Omega_N, A_N^{Jac,-} Omega_N> haengt von
der Wahl von Omega_N und von A_N^{Jac,-} ab.
                                                      (121.1)
```

---

## 121.2 — Hadamard-Koeffizient C_xi

```
Die vollstaendige xi-Funktion (Riemann) hat die Hadamard-Darstellung:

  xi(s) = xi(0) * exp(A_xi * s) * prod_{rho} (1 - s/rho) exp(s/rho)

wobei das Produkt symmetrisch ueber Nullstellenpaare (rho, 1-rho) laeuft.

Der logarithmische Ableitungskoeffizient bei s=0 ist:

  xi'(s)/xi(s) |_{s=0}  =  A_xi + sum_{rho}^{sym} (1/(s-rho) + 1/rho) |_{s=0}
                         =  A_xi + sum_{rho}^{sym} (-1/rho + 1/rho)
                         ... (die lokalen Terme heben sich)

Korrekte Berechnung:
  -xi'(0)/xi(0) = A_xi = B - sum_{rho}^{sym} Re(1/rho)

wobei die Summe wegen des symmetrischen Paarens abs. konvergent ist.

Numerischer Wert (klassische Formel, vgl. Davenport/Titchmarsh):

  C_xi := sum_{rho}^{sym} 1/rho = -xi'(0)/xi(0)
        = 1 + gamma_E/2 - (1/2) log(4*pi)
        ~ 1 + 0.2886 - 1.8379
        ~ -0.5493 ...

  (Wert abhaengig von Normalisierung; hier xi(0) = 1/2.)

Unter RH (rho = 1/2 + i*gamma, gamma > 0):

  C_xi = sum_{gamma>0} ( 1/(1/2+i*gamma) + 1/(1/2-i*gamma) )
       = sum_{gamma>0} 1 / (1/4 + gamma^2)

Diese Summe ist absolut konvergent (da gamma_n ~ 2*pi*n / log n -> infty).

WARNUNG: sum_gamma 1/gamma (einfach, ohne Symmetrisierung) ist NICHT
der richtige Gegenstand; er ist nicht absolut konvergent und kein
Standard-Hadamard-Term.                               (121.2)
```

---

## 121.3 — Rohvergleich scheitert ohne Renormierung

```
Naiver Test:

  M_1^{(N)} := <Omega_N, A_N^{Jac,-} Omega_N>

  Zielwert:  C_xi = sum_{rho}^{sym} 1/rho  ~  -0.5493

Problem 1 (Skala):
  A_N^{Jac,-} enthaelt Beitraege O(log n) aus den Primtermen.
  Fuer wachsendes N waechst ||A_N^{Jac,-}||_op  wie O(log N).
  Daher: M_1^{(N)} -> infty fuer generisches Omega_N.

Problem 2 (Renormierung):
  m_arith(z) ist nicht die Cauchy-Transformierte eines endlichen Masses.
  Sie enthaelt einen logarithmischen Gamma-Beitrag, der bei z -> infty
  wie O(log z) waechst, NICHT wie O(1/z).
  Das heisst: m_arith(z) * z -> infty fuer z -> infty auf dem Imagteil.

Problem 3 (Nullstellen-Renormierung):
  Der Nullstellenterm sum_rho 1/(rho-z) braucht die paarweise Symmetrisierung
  (rho, 1-rho), um konvergent zu sein.
  Ein endlicher Jacobi-Operator liefert endlich viele Pole, braucht keine
  Symmetrisierung -- aber das Zielobjekt tut es.

Fazit:
  Ein direkter Vergleich M_1^{(N)} <-> C_xi ist ohne Renormierung R_N
  sinnlos; R_N muss den log N-Wachstum von M_1^{(N)} gegen C_xi kalibrieren.
                                                      (121.3)
```

---

## 121.4 — Definition des renormierten Vergleichsoperators

```
Sei R_N eine (noch zu bestimmende) Renormierungsfolge (R_N > 0).

Definiere den renormierten Moment-1-Test:

  Test 121.T1:  R_N * M_1^{(N)}  ->  C_xi  (N -> infty)?

Damit der Test sinnvoll ist, muss R_N das Wachstum von M_1^{(N)}
kompensieren.

Notwendige Bedingung an R_N:

  (R1) Falls M_1^{(N)} ~ c * log N:     R_N ~ 1/log N
  (R2) Falls M_1^{(N)} ~ c * N^alpha:   R_N ~ N^{-alpha}

Die richtige Wahl von R_N ist Teil des Problems.

Streng paariger Test (Symmetrisierung):

  Hadamard-Zielwert (unter RH):

    C_xi^{(N)} := sum_{j: lambda_{j,N} > 0} 1/(1/4 + lambda_{j,N}^2)

  Anmerkung: Dieser Wert verwendet die Eigenwerte lambda_{j,N} von A_N^{Jac,-}
  so als ob sie Zeta-Ordinaten waeren -- das ist noch nicht gerechtfertigt.
  Test 121.T1 ist daher vorlaeufig; er entscheidet nur,
  ob die Groessenordnung korrekt ist.

Symmetrisierter Moment-1-Vergleich:

  Statt M_1 direkt, betrachte den symmetrisierten Ausdruck

    M_1^{sym,(N)} := (1/2)(M_1^{(N)} + M_1^{(N)*})
                  = Re(M_1^{(N)})

  (ist reell, da A_N^{Jac,-} selbstadjungiert und Omega_N normiert reell).

  Paarter Zielkoeffizient (bei endlichem N):

    C^{(N)} := sum_j w_{j,N} / (1/4 + lambda_{j,N}^2)  *  (1/4 + lambda_{j,N}^2)
             = sum_j w_{j,N}  =  1  (Gesamtmasse; trivial).

  Das zeigt: Der paarweise Summenausdruck kollabiert zur Gesamtmasse 1,
  wenn kein weiterer Strukturzwang vorhanden ist.
  => Test 121.T1 allein ist nicht ausreichend; er muss mit einer
     spektralen Lokalisierungsbedingung kombiniert werden.
                                                      (121.4)
```

---

## 121.5 — Test der drei Omega_N-Kandidaten

### 121.5.1 — K1: Omega_N = delta_1

```
M_1^{(1)} = <delta_1, A_N^{Jac,-} delta_1>
           = <delta_1, H_N delta_1> + beta_N <delta_1, J_N^- delta_1>

Diagonalterm:
  <delta_1, H_N delta_1> = (H_N)_{1,1}  = a_1  (Diagonal von H_N bei r=1).

Offdiagonalterm:
  <delta_1, J_N^- delta_1>
  = sum_{n in Sigma_N} log(n) <delta_1, V_n^{(N)} R_N delta_1>
  = sum_{n in Sigma_N} log(n) * <delta_1, delta_{n+1}>    [R_N delta_1 = delta_1]
  = log(1) * <delta_1, delta_2>  +  log(2) * <delta_1, delta_3>  + ...
  = 0   (da <delta_1, delta_k> = 0 fuer k >= 2).

Also: M_1^{(1)} = a_1.

Diagnose K1:
  Der Moment-1-Wert haengt nur vom Diagonaleintrag a_1 von H_N ab.
  H_N ist im Programm kein kanonisch festgelegter Operator.
  (Er ist ein Freiheitsgrad der Konstruktion.)

  => K1 liefert a_1 als Moment 1; dieser Wert hat keinen direkten
     Bezug zu C_xi = -xi'(0)/xi(0) ~ -0.5493,
     AUSSER H_N wird explizit so gewaehlt, dass a_1 = C_xi.

  Ergebnis: K1 ist ein FREIHEITSGRAD, kein echter Test.
  Der Test K1 =?= C_xi ist leer, solange H_N nicht festgelegt ist.

  NEGATIVBEFUND:
    Omega_N = delta_1 liefert keinen nicht-trivialen
    Hadamard-Kalibrierungstest.                        (121.5.1)
  Status: ✓[M] (Negativbefund gesichert)
```

### 121.5.2 — K3: Omega_N = Omega_N^{Fesh} ~ kappa_N^{1/2} delta_1

```
Wie in NEU-120 (120.A.3) gezeigt:
  Omega_N^{Fesh} auf H_N = kappa_N^{1/2} delta_1  (nach Projektion und Normierung).

M_1^{(Fesh)} = <kappa_N^{1/2} delta_1, A_N^{Jac,-} kappa_N^{1/2} delta_1>
             = kappa_N * <delta_1, A_N^{Jac,-} delta_1>
             = kappa_N * a_1.

Diagnose K3:
  K3 ist kappa_N-Skalierung von K1.
  Kein neuer Informationsgehalt.

  NEGATIVBEFUND:
    K3 faellt mit K1 zusammen; beide sind leer ohne H_N-Festlegung.
                                                      (121.5.2)
  Status: ✓[M] (Negativbefund gesichert)
```

### 121.5.3 — K2: Omega_N = Omega_N^{KMS}

```
Formal (schematisch, GNS-Konstruktion noch nicht im Katalog):

  Der KMS-Zustand phi_beta des BC-analogen Systems bei inverser Temperatur beta
  hat die GNS-Darstellung mit zyklischem Vektor Omega_beta in H_{GNS}.

  Der zugehoerige m-Funktionskandidat lautet:

    m_{KMS,N}(z) = <Omega_beta, (A_N^{Jac,-} - z)^{-1} Omega_beta>_{H_{GNS}}

  Schematische Momentenentwicklung (fuer endliches N, beta fest):

    M_1^{KMS} = <Omega_beta, A_N^{Jac,-} Omega_beta>
             ~ Z_beta^{-1} sum_{n in Sigma_N} n^{-beta} * lambda_{n,N}

  wobei lambda_{n,N} der n-te Eigenwert von A_N^{Jac,-} in der n-Basis ist
  (schematisch; exakt nur nach GNS-Konstruktion).

  Fuer beta -> 1 (kritische Temperatur der Zeta-Funktion):
    Z_1 ~ log N  (da sum_{n<=N} 1/n ~ log N).
    => Z_1^{-1} -> 0, also: Renormierung R_N ~ log N noetig.

  Renormierter Kandidat:
    R_N^{KMS} * M_1^{KMS}  ~  (1/log N) * sum_{n<=N} (1/n) * lambda_{n,N}

  Frage 121.5.3.Q:
    Konvergiert das gegen C_xi = sum_{gamma>0} 1/(1/4+gamma^2)?

  Das haengt davon ab, ob lambda_{n,N} die Zeta-Ordinaten approxiert.
  Genau das ist die Kernfrage des Programms.

  Diagnose K2:
    Einziger nicht-trivialer Kandidat.
    Renormierung R_N ~ 1/log N ist plausibel (passt zur Bombieri-Normalisierung).
    GNS-Konstruktion fehlt noch (NEU-122 oder separate Einheit noetig).

  Status: ?[O]  Offene Kernfrage.                    (121.5.3)
```

---

## 121.6 — Zentraler Negativbefund und Konsequenz

```
Zentraler Negativbefund (121.6.N):

  Von den drei Omega_N-Kandidaten aus NEU-119:
    K1 (delta_1):     Moment 1 = a_1, kein Hadamard-Bezug.  ✗ (leer)
    K3 (Fesh):        = kappa_N * K1.                        ✗ (leer)
    K2 (KMS):         Arithmetisch, aber GNS fehlt.          ? (offen)

  Fazit:
    In der aktuellen Jacobi-Konstruktion (ohne GNS/KMS-Ergaenzung)
    kann der Moment-1-Kalibrierungstest NICHT nicht-trivial durchgefuehrt werden.

    Der einzige echte Kandidat fuer Omega_N ist Omega_N^{KMS},
    aber dafuer muss die KMS/GNS-Konstruktion aus NEU-43/44 explizit
    in den Jacobi-Operator-Formalismus eingebettet werden.

Konsequenz fuer das Programm:

    m_{Omega,N} -> m_arith  (in Herglotz-erhaltender Topologie)

  ist in der aktuellen Form nicht plausibel ohne:

    (P1) Explizite KMS/GNS-Konstruktion des Vektors Omega_N^{KMS}.
    (P2) Nachweis, dass die induzierten Gewichte w_{j,N}^{KMS}
         mit den Bombieri-Gewichten kompatibel sind.
    (P3) Renormierungsformel R_N ~ 1/log N (oder praezisierter).

  Das sind die drei notwendigen Bedingungen fuer NEU-122.
                                                      (121.6.N)
  Status: ✓[M] (Negativbefund und Folgestruktur gesichert)
```

---

## 121.7 — Weichere Variante: Struktureller Vergleich statt numerischer Test

```
Alternativ zu einem numerischen Moment-1-Abgleich
kann ein struktureller Vergleich gefuehrt werden:

  Strukturtest 121.7.S:

    Frage: Hat m_{Omega,N} fuer geeignetes Omega_N
           dieselbe Nullstellen-/Pol-Topologie wie m_arith,
           d.h. dieselbe Anzahl und Anordnung der Pole im Streifen?

    Fuer endliches N: Nein (m_{Omega,N} hat endlich viele Pole auf R,
                             m_arith hat abzaehlbar viele im Streifen).

    Aber: Fuer wachsendes N koennte die endliche Polzahl gegen die
          Nullstellenmenge der Zeta-Funktion konvergieren.

    Naechster struktureller Test:
      Konvergiert das Spektrum sigma(A_N^{Jac,-}) (N -> infty)
      gegen die Menge {Im(rho) : xi(rho) = 0} unter RH?

    Das ist eine Form der Spektralnaherungsfrage,
    die unabhaengig vom Vektor Omega_N formuliert werden kann.
    => Gegenststand von NEU-122 (Spektralnaherung).

  Status: ?[O]                                        (121.7.S)
```

---

## Satzstatusmatrix (NEU-121)

| Satz | Inhalt | Status |
|---|---|---|
| 121.1 | Resolventenentwicklung: m_{Omega,N}(z) = -1/z - M_1/z^2 - ... | ✓[M] |
| 121.2 | Hadamard-Koeffizient C_xi = -xi'(0)/xi(0) = sum_rho^sym 1/rho | ✓[M] |
| 121.3 | Rohvergleich M_1 <-> C_xi scheitert ohne Renormierung R_N | ✓[M] |
| 121.4 | Renormierter Test 121.T1: R_N * M_1^{(N)} -> C_xi? | ?[O] |
| 121.5.1 | K1: Moment 1 = a_1 (leer, kein Hadamard-Bezug) | ✓[M] (negativ) |
| 121.5.2 | K3 = kappa_N * K1 (identisch leer) | ✓[M] (negativ) |
| 121.5.3 | K2 (KMS): einziger nichttrivialer Kandidat, GNS fehlt | ?[O] |
| 121.6.N | Negativbefund: ohne KMS/GNS kein nichtrivialer Test moeglich | ✓[M] |
| 121.7.S | Strukturtest: Spektralnaherung sigma(A_N) -> Zeta-Ordinaten | ?[O] |

---

## Anschlüsse

| Quelle | Inhalt |
|---|---|
| NEU-119 | Definition m_{Omega,N} und drei Kandidaten |
| NEU-120 | Warnsatz 120.W: Grenzübergang => RH; Dreiteilung A/B/C |
| NEU-63D | m_arith Herglotz <=> RH |
| NEU-43/44 | BC-Konstruktion, KMS-Zustand (GNS noch nicht im Jacobi-Formalismus) |
| -> NEU-122 | KMS/GNS-Einbettung ODER Spektralnaherung sigma(A_N) -> Zeta-Ordinaten |
