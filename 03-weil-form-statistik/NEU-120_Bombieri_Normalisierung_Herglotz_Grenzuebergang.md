# NEU-120 — Bombieri-Normalisierung und Herglotz-Grenzübergang

**Stand: 4. Juli 2026**

**Rückverweis:** NEU-119 (Definition m_{Omega,N}), NEU-113 (Bombieri-Normalisierung), NEU-111.4b (Jacobi-Realisierungstest)

---

## Warnsatz (vorangestellt)

```
Warnsatz 120.W:

  Da jedes m_{Omega,N} eine Herglotz-Funktion ist
  (solange A_N^{Jac,-} selbstadjungiert und Omega_N =/= 0),
  kann ein lokal gleichmäßiger Grenzübergang

    m_{Omega,N}(z)  ->  m_arith(z)  (N -> infty, lokal glm. auf C^+)

  nur dann gelingen, wenn m_arith selbst eine Herglotz-Funktion ist.

  Aber:
    m_arith(z) = -i xi'(1/2+iz) / xi(1/2+iz)
  ist genau dann Herglotz, wenn RH gilt  (NEU-63D).

  Daher gilt:

    m_{Omega,N} -> m_arith  (lokal gleichmäßig)  =>  RH.

  Das ist keine Schwäche des Ansatzes, sondern genau der Kern.
  NEU-120 prüft, ob der Grenzübergang überhaupt eine Chance hat,
  d.h. ob die ersten Momente und die Polstruktur von m_{Omega,N}
  für die richtigen Kandidaten Omega_N mit m_arith kompatibel sind.
                                                      (120.W)
```

---

## Leitfrage

```
Gibt es eine Wahl von Omega_N und eine Renormierung R_N, sodass

  R_N m_{Omega,N}(z) -> m_arith(z)  (N -> infty, lokal gleichm. auf C^+)?

Dreiteilige Prüfung:

  120.A — Vektorwahl:      Welches Omega_N ist kanonisch?
  120.B — Massenkontrolle: Sind mu_{Omega,N} tight/normalisierbar?
  120.C — Bombieri-Abgleich: Stimmen Gamma-, Pol- und Primseite?
```

---

## 120.A — Vektorwahl: Momententest der drei Kandidaten

```
Für jeden Kandidaten Omega_N aus NEU-119 berechnen wir:

  Moment 0:  mu_{Omega,N}(R) = || Omega_N ||^2 = 1  (normiert)
  Moment 1:  int lambda d mu_{Omega,N}(lambda) = <Omega_N, A_N^{Jac,-} Omega_N>
  Moment 2:  int lambda^2 d mu_{Omega,N}(lambda) = ||A_N^{Jac,-} Omega_N||^2
```

### 120.A.1 — Kandidat K1: Omega_N = delta_1

```
m_{delta_1, N}(z) = <delta_1, (A_N^{Jac,-} - z)^{-1} delta_1>

Moment 1:
  <delta_1, A_N^{Jac,-} delta_1>
  = <delta_1, H_N delta_1> + beta_N <delta_1, J_N^- delta_1>
  = a_1  +  beta_N sum_{n in Sigma_N} log(n) <delta_1, V_n^{(N)} R_N delta_1>
  = a_1  +  beta_N sum_{n in Sigma_N} log(n) * 1 * <delta_1, delta_{1+n}>
  = a_1  +  0
  (da <delta_1, delta_{1+n}> = 0 fuer n >= 1)

  => Moment 1 = a_1  (Diagonaleintrag von H_N an Position r=1).

Moment 2:
  ||A_N^{Jac,-} delta_1||^2
  = ||H_N delta_1 + beta_N J_N^- delta_1||^2
  = a_1^2  +  beta_N^2 sum_{n in Sigma_N} log(n)^2 * 1^2
  (da V_n^{(N)} R_N delta_1 = 1 * delta_{1+n}, norm. Beiträge)

Diagnose K1:
  Moment 1 = a_1 (diagonal, kein Primterm).
  Moment 2 = a_1^2 + beta_N^2 sum_{n} log(n)^2  (arithmetisch).

  Vergleich mit m_arith:
    m_arith hat Polresidue bei den Nullstellen gamma der Zeta-Funktion,
    nicht bei Eigenwerten eines Jacobi-Operators mit Startvektor delta_1.
    Die Polstruktur ist a priori verschieden.

  Status: Moment-1-Kompatibilitaet unklar.  Hauptkandidat nur vorlaeufig.
                                                          (120.A.1)
```

### 120.A.2 — Kandidat K2: Omega_N = Omega_N^KMS (bei inverser Temperatur beta)

```
Der KMS-Zustand phi_beta des BC-analogen Systems (NEU-43/44) hat
die GNS-Darstellung mit zyklischem Vektor Omega_beta.

Formal gilt für den KMS-Zustand:
  phi_beta(a) = Z_beta^{-1} sum_{n in Sigma_N} n^{-beta} <n, a n>

wobei Z_beta = sum_n n^{-beta}  (endliche Approximation der Zeta-Summe).

Das KMS-Spektralmaß ist arithmetisch gewichtet:
  d mu_{Omega^KMS, N}(lambda) = Z_beta^{-1} sum_n n^{-beta} delta_{lambda_{n,N}}(lambda) d lambda

(schematisch; exakte Form erfordert GNS-Konstruktion).

Moment 1 (schematisch):
  int lambda d mu_{Omega^KMS, N}  ~  Z_beta^{-1} sum_n n^{-beta} lambda_n

Diagnose K2:
  Arithmetisch gewichtet durch n^{-beta}: passend zu Dirichletreihen.
  Fuer beta = 1 (kritische Temperatur):
    Masse ~ 1/Z_1 sum_n 1/n (Harmonie-Reihe, divergent fuer N -> infty).
    => Normierungsproblem; R_N-Renormierung noetig.

  K2 ist arithmetisch natuerlicher als K1, aber GNS-Konstruktion
  noch nicht im Katalog vorhanden.                         (120.A.2)
  Status: ?[O]
```

### 120.A.3 — Kandidat K3: Omega_N = Omega_N^Fesh (Feshbach-Vektor)

```
Omega_N^Fesh = kappa_N^{-1/2} Pi_N^* delta_1 / ||Pi_N^* delta_1||
             = kappa_N^{-1/2} sum_{n in Sigma_N} eta_{1,n}  (normiert)

Nach Projektion auf H_N = l^2(I_N) durch den Kollapsoperator Pi_N:
  Pi_N Omega_N^Fesh = kappa_N^{-1/2} sum_n delta_1 = kappa_N^{1/2} delta_1.

Das ist kein normierter Vektor in H_N, sondern kappa_N^{1/2} * delta_1.
Fuer den m-Funktionskandidaten:
  m_{Omega^Fesh, N}(z) = kappa_N <delta_1, (A_N^{Jac,-} - z)^{-1} delta_1>
                       = kappa_N * m_{delta_1, N}(z).

Diagnose K3:
  K3 ist nur eine kappa_N-Skalierung von K1.
  Moment 1 = kappa_N * a_1.
  => Wenn K1 falsche Polstruktur hat, hat K3 dieselbe Polstruktur.
  => K3 kein echter neuer Kandidat auf diesem Niveau.

  Renormierung R_N = kappa_N^{-1} führt K3 auf K1 zurück.
                                                          (120.A.3)
```

### 120.A.4 — Zwischendiagnose Vektorwahl

```
Zwischendiagnose:
  K1 (delta_1): Moment 1 diagonal (a_1), kein direkter Primtermbezug.
  K2 (KMS): Arithmetisch gewichtet, aber nicht konstruiert.
  K3 (Fesh): Skalierung von K1, kein Gewinn.

  Entscheidender Befund:
    Kein Kandidat liefert auf diesem Niveau eine klare
    Polstruktur bei den Zeta-Nullstellen.

  Das ist erwartet: Die Zeta-Nullstellen entstehen erst im N -> infty
  Limes aus der spektralen Akkumulation der Jacobi-Eigenwerte.
  Fuer endliches N gibt es keine Zeta-Nullstellen in sigma(A_N^{Jac,-}).

  Deshalb ist der Grenzübergang N -> infty der eigentliche Kern.
                                                          (120.A.4)
  Status: ?[O]
```

---

## 120.B — Massenkontrolle: Tightness von mu_{Omega,N}

```
Frage:
  Bleibt die Masse von mu_{Omega,N} im Limes N -> infty kontrolliert?
  Formal: mu_{Omega,N}(R) = 1  fuer alle N (da ||Omega_N|| = 1).
  Also: Masse ist trivialerweise kontrolliert.

Das eigentliche Problem ist nicht die Gesamtmasse, sondern:
  Wo akkumuliert sich die Masse?

  Wenn die Eigenwerte lambda_{j,N} ins Unendliche driften (lambda_{j,N} -> infty),
  und die Gewichte w_{j,N} = |<u_{j,N}, Omega_N>|^2 sich entsprechend verteilen,
  koennte die schwache Grenzverteilung nicht m_arith ergeben,
  sondern eine andere (oder keine) Herglotz-Funktion.

Massenkontrolle-Test 120.B.1 (notwendige Bedingung):
  Fuer den Grenzübergang m_{Omega,N} -> m_arith ist notwendig:

    (B1) Die Spektralmasse akkumuliert bei den Zeta-Nullstellen:
           w_{j,N} -> |Res_{gamma_j}(m_arith)|
           fuer die j-te aufsteigende Nullstelle gamma_j.

    (B2) Der Beitrag jenseits einer festen Grenze Lambda > 0 verschwindet:
           int_{|lambda|>Lambda} d mu_{Omega,N}(lambda) -> 0.
           (Tightness-Bedingung)

Status: Beide Bedingungen B1 und B2 sind vollständig offen.  ?[O]
```

---

## 120.C — Bombieri-Abgleich: Gamma-, Pol- und Primseite

```
Die Zielgröße m_arith hat drei Bestandteile (aus NEU-63D, NEU-112, NEU-113):

  m_arith(z) = -i xi'(1/2+iz) / xi(1/2+iz)
             = [Nullstellenterm] + [Gamma-Term] + [Pol-Term]

  (a) Nullstellenterm:
      sum_gamma 1/(gamma - z) + 1/(-gamma - z)
      (Summe ueber nichttriviale Nullstellen, RH: gamma reell nach
      Spiegelung; in Bombieri-Normalisierung: Residue-Gewichte 1)

  (b) Gamma-Term (archimedisch):
      Beitrag der Gamma-Funktion in der xi-Funktionalgleichung:
      ~ (1/2) log pi - (1/4) psi(1/4 + iz/2) - (1/4) psi(1/4 - iz/2)
      (psi = Digamma-Funktion)

  (c) Pol-Term:
      Einfache Pole bei z = i/2 und z = -i/2
      (von den trivialen Nullstellen s=0 und s=1 der vollst. Zeta)

Bombieri-Abgleich-Test 120.C.1:
  Für den Grenzübergang m_{Omega,N} -> m_arith muss gelten:

  (C1) Nullstellenterm:
    Die Polbeitraege sum_j w_{j,N} / (lambda_{j,N} - z) akkumulieren
    gegen sum_gamma 1/(gamma - z) im schwachen Sinne.
    => Eigenwerte von A_N^{Jac,-} mussen gegen Zeta-Nullstellen konvergieren.
    => Gewichte w_{j,N} mussen gegen 1 konvergieren.
    Status: ?[O]  (Kernfrage des gesamten Programms)

  (C2) Gamma-Term:
    Der renormierte Grenzwert muss den archimedischen Gamma-Term erzeugen.
    Dies ist nicht durch den Jacobi-Operator allein erklaert;
    es erfordert eine Verbindung zur Funktionalgleichung der xi-Funktion.
    Status: ?[O]  (strukturell offen; moeglicherweise aus KMS-Gewicht)

  (C3) Pol-Term:
    Beitraege bei z = plusminus i/2 mussen entstehen.
    Diese kommen aus dem Beitrag der trivialen Nullstellen,
    die ausserhalb des reellen Spektrums von A_N^{Jac,-} liegen.
    Status: ?[O]

Zusammenfassung 120.C:
  Alle drei Bestandteile des Bombieri-Abgleichs sind offen.
  C1 ist der Kern: Eigenwert-Konvergenz gegen Zeta-Nullstellen.
                                                          (120.C.1)
```

---

## 120.D — Implikationsstruktur

```
Satz 120.D (Implikationskette):

  Falls 120.A + 120.B + 120.C gelingen (d.h. R_N m_{Omega,N} -> m_arith
  lokal gleichmäßig auf C^+), dann:

    (D1) m_arith ist Herglotz-Funktion.
    (D2) Also: RH gilt  (Umkehrung von NEU-63D).

  Die Implikationskette ist:

    Geeignetes Omega_N + Normierung R_N
    => m_{Omega,N} -> m_arith  (lok. glm.)
    => m_arith Herglotz
    => RH.

  Richtung der Schwierigkeit:
    Der Beweis von D1 setzt voraus, dass C1 gilt,
    d.h. die Eigenwerte von A_N^{Jac,-} konvergieren gegen Zeta-Nullstellen.
    Das ist aequivalent zu einer Spektraldichte-Aussage,
    die mindestens so schwer ist wie RH selbst.

  Status: ?[O]  (haerter Kern des Programms).
                                                          (120.D)
```

---

## 120.E — Erster konkreter Schritt: Moment-1-Kalibrierung

```
Bevor der volle Grenzuebergang angegangen wird,
kann Moment 1 als Kalibrierungstest dienen.

Zielgröße (Moment 1 von m_arith bei z -> i*infty):
  m_arith(z) ~ -1/z + c_0/z^2 + ...
  Moment 1 von m_arith = c_0 = <m_arith, lambda>_{Stieltjes}

Fuer m_arith = -i xi'(1/2+iz)/xi(1/2+iz):
  Das erste Moment ist der logarithmische Ableitungsterm;
  es haengt von der Summe sum_gamma 1/gamma ab (Hadamard-Produkt).

Konkreter Test 120.E.1:
  Vergleiche <Omega_N, A_N^{Jac,-} Omega_N> fuer K1, K2
  mit dem Zielwert sum_gamma (1/gamma + 1/gamma-bar) aus der
  Hadamard-Produktdarstellung von xi.

  Falls K1 (Omega_N = delta_1):
    Moment 1 = a_1  (Diagonaleintrag von H_N bei r=1).
    Dieser haengt von der Wahl von H_N ab (nicht aus dem Programm festgelegt).
    => Freiheitsgrad in H_N noetig, um Moment-1-Kalibrierung zu ermoeglichen.

  Falls K2 (KMS-Vektor, schematisch):
    Moment 1 ~ Z_beta^{-1} sum_n n^{-beta} lambda_n
    Fuer beta -> 1: Verbindung zur Dirichletreihen-Struktur.

Status: ?[O]  Ausgangspunkt fuer NEU-121.                 (120.E.1)
```

---

## Satzstatusmatrix (NEU-120)

| Test | Inhalt | Status |
|---|---|---|
| 120.W | Warnsatz: m_{Omega,N}->m_arith => RH | ✓[M] |
| 120.A.1 | K1: Moment 1 = a_1, kein Primtermbezug | ✓[M] |
| 120.A.2 | K2: KMS-Masse arithmetisch, aber nicht konstruiert | ?[O] |
| 120.A.3 | K3 = kappa_N * K1 (keine neue Info) | ✓[M] |
| 120.A.4 | Kein Kandidat zeigt Zeta-Polstruktur fuer endliches N | ✓[M] |
| 120.B.1 | Tightness und Akkumulation bei Zeta-Nullstellen | ?[O] |
| 120.C.1 | Nullstellenterm: Eigenwert-Konvergenz gegen gamma_j | ?[O] |
| 120.C.2 | Gamma-Term (archimedisch) | ?[O] |
| 120.C.3 | Pol-Term (triviale Nullstellen) | ?[O] |
| 120.D | Implikation: Grenzuebergang => RH | ✓[M] |
| 120.E.1 | Moment-1-Kalibrierung als erster konkreter Schritt | ?[O] |

---

## Anschlüsse

| Quelle | Inhalt |
|---|---|
| NEU-63D | m_arith Herglotz <=> RH |
| NEU-111.4b | Jacobi-Realisierungstest: m_{Omega,N} -> m_arith |
| NEU-113 | Bombieri-Normalisierung der W_xi^norm-Seite |
| NEU-119 | Definition m_{Omega,N} |
| -> NEU-121 | Moment-1-Kalibrierung: H_N-Wahl und Hadamard-Abgleich |
