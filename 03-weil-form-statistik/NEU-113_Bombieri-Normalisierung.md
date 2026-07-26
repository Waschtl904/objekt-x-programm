# NEU-113 — Bombieri-Normalisierung des Weil-Distributionsobjekts W_xi

**Stand: 1. Juli 2026 — ABGESCHLOSSEN (bis auf Rueckbindung NEU-116)**

---

## Ziel

NEU-113 fixiert das lineare Distributionsobjekt

```
W_xi  =  W_zeros + W_Gamma + W_prime + W_{pole/triv}
```

mit exakter Mellin-/Fourier-/Vorzeichen-Normierung, so dass fuer geeignete
Testfunktionen f auf PW_t gilt:

```
Q_Weil[f]  =  < W_xi, f^ast * f >
```

NEU-113 beweist **nicht** die Rueckbindung an X (das ist NEU-116), sondern
kalibriert das Zielobjekt fuer beide Spuren:

```
Spur A:  Pi_gamma(X) = m_arith  -->  W_xi  -->  Q_Weil
Spur B:  X  -->  W_res^top  --?-->  W_xi       (NEU-116)
```

Damit ist NEU-113 ausschliesslich die Kalibrierung von rechts.
Es beweist hoechstens die Projektionsebene Pi_gamma(X), nicht X selbst.

---

## NEU-113.0 — Bombieri-Weil-Referenznormalform

Die drei kritischen Freiheitsgrade, die durch die Normalform fixiert werden:

```
1. Mellin-Shift:        s = 1/2 + iz  (kritische Gerade als reelle Achse)
2. Fourier-Konvention:  phi-hat(z) = integral_R phi(u) e^{izu} du
3. Vorzeichen der Weil-Form: durch explizite Formel festgelegt
```

Referenz: Bombieri, *Remarks on Weil's quadratic functional in number theory* (2000).
Die positive Semidefinitheit von Q_Weil ist dort aequivalent zur RH.

---

## NEU-113.1 — Normierungskonvention (Mellin/Fourier-Shift)

Wir arbeiten in **additiven Koordinaten**:

```
u  =  log x,    x in R_+^times
```

Fuer eine Testfunktion phi(u) setzen wir:

```
phi-hat(z)  =  integral_R  phi(u) e^{izu} du          (113.1.1)
```

Die Mellin-Transformation der zugehoerigen multiplikativen Testfunktion f(x) = phi(log x)
entspricht dann der Fourier-Transformation auf der kritischen Geraden:

```
f-tilde(1/2 + iz)  =  phi-hat(z)                      (113.1.2)
```

**Konsequenz:** Die kritische Gerade Re(s) = 1/2 wird zur reellen Spektralachse z in R.
Eine Nullstelle rho = 1/2 + i*gamma erscheint als reeller Punkt gamma in R (unter RH).

Status: **gesichert ✓[M]**

---

## NEU-113.2 — Autokorrelation und Positivierung

Fuer phi in C_c^infty((-t, t)) definieren wir:

```
phi^ast(u)  =  overline{phi(-u)}
Phi         =  phi^ast * phi      (Faltung auf R)
```

Dann gilt die **zentrale Positivierungsidentitaet**:

```
Phi-hat(lambda)  =  |phi-hat(lambda)|^2               (113.2.1)
```

Beweis: Fourier-Faltungssatz und phi^ast-hat(lambda) = overline{phi-hat(lambda)}.

**Tragerregel:** phi in C_c^infty((-t,t)) impliziert phi-hat in PW_t (Paley-Wiener).

Status: **gesichert ✓[M]**

---

## NEU-113.3 — Nullstellenkomponente W_zeros

Fuer die nichttrivialen Nullstellen rho = 1/2 + i*gamma definieren wir:

```
W_zeros[Phi]  =  sum_gamma  Phi-hat(gamma)             (113.3.1)
```

Mit (113.2.1):

```
Q_zeros[phi]  =  sum_gamma |phi-hat(gamma)|^2          (113.3.2)
```

Positivitaet: Q_zeros[phi] >= 0 fuer alle phi.

Anschluss an NEU-112: Der Nullstellenterm von m_arith liefert genau
sum_gamma delta_gamma; die Paarung mit Phi-hat ergibt (113.3.2) normierungstreu.

Status: **gesichert ✓[M]**

---

## NEU-113.4 — Primkomponente W_prime

Normierungswarnung: Bei s = 1/2 + iz gilt n^{-s} = n^{-1/2} e^{-iz log n}.
Daher erscheint in der Primkomponente der Faktor Lambda(n)/sqrt(n), nicht Lambda(n)/n.

```
W_prime[Phi]  =  - sum_{n >= 2}  Lambda(n)/sqrt(n)  *  ( Phi(log n) + Phi(-log n) )
                                                        (113.4.1)
```

wobei Lambda(n) = log p fuer n = p^k, Lambda(n) = 0 sonst.

Anschluss an NEU-114.4: Primkanten m -> p^k m in Objekt X erzeugen strukturell
Gewichte log p. Test 114.4 prueft, ob dies exakt Lambda(p^k) = log p reproduziert.

Status: **strukturell plausibel ⚠[M]** (sqrt(n)-Faktor und Vorzeichen aus
m_arith-Herglotz-Renormierung noch zu verifizieren)

---

## NEU-113.5 — Archimedische Komponente W_Gamma

Der archimedische Anteil stammt aus dem Gamma-Faktor pi^{-s/2} Gamma(s/2).
Seine logarithmische Ableitung ist

```
-(1/2) log(pi) + (1/2) psi(s/2),     psi = Gamma'/Gamma.
```

Auf der kritischen Geraden s = 1/2 + i lambda ergibt sich der Gewichtskern:

```
Psi_Gamma(lambda)
  :=  -log(pi) + Re psi( 1/4 + i lambda/2 ).           (113.5.1)
```

In der W_xi-Konvention:

```
W_Gamma[Phi]
  :=  (1/2pi) integral_R  Phi-hat(lambda) Psi_Gamma(lambda) d lambda.   (113.5.2)
```

Vorzeichenwarnung: In der klassischen Weil-Form erscheint derselbe Term mit
negativem Vorzeichen auf der anderen Seite der expliziten Formel.
Die Wahl (113.5.2) ist konsistent mit W_prime in (113.4.1); das globale
Vorzeichen wird durch Satz 113.7.A abschliessend gesichert.

Fuer Autokorrelationen Phi = phi^ast * phi:

```
W_Gamma[Phi]
  =  (1/2pi) integral_R |phi-hat(lambda)|^2 Psi_Gamma(lambda) d lambda.  (113.5.3)
```

W_Gamma ist ein renormierender archimedischer Beitrag, kein isoliert positiver Term.

Status: **explizit normiert ✓/⚠[M]** (globales Vorzeichen durch 113.7 gesichert)

---

## NEU-113.6 — Kompensationskomponente W_{pole/triv}

**Zentraler Punkt: xi(s) selbst besitzt keine Pole.**

Die Terme bei s=0,1 und die trivialen Nullstellen erscheinen erst, wenn man
xi'/xi in die Standardfaktoren

```
s(s-1),    pi^{-s/2} Gamma(s/2),    zeta(s)
```

zerlegt. W_{pole/triv} ist daher **keine zusaetzliche Spektralmasse**,
sondern eine Kompensationskomponente.

### 113.6.1 — Logarithmische Standardzerlegung

Aus

```
xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
```

folgt die Zerlegung von xi'/xi:

```
xi'/xi(s)  =  P_{0,1}(s) + G(s) + Z(s)                (113.6.1)

P_{0,1}(s)  :=  1/s + 1/(s-1)
G(s)        :=  -(1/2) log(pi) + (1/2) psi(s/2)
Z(s)        :=  zeta'/zeta(s)
```

### 113.6.2 — Lokale Kompensationen

```
Bei s = 1:
  P_{0,1} ~ +1/(s-1),   zeta'/zeta ~ -1/(s-1)   =>  regulaer

Bei s = 0:
  P_{0,1} ~ +1/s,       (1/2)psi(s/2) ~ -1/s    =>  regulaer

Bei s = -2k (k >= 1):
  zeta'/zeta ~ +1/(s+2k), (1/2)psi(s/2) ~ -1/(s+2k)  =>  regulaer
```

**Satz 113.6.A:** Pole bei s=0,1 und triviale Nullstellen sind
Kompensationsartefakte der Zerlegung, nicht Pole von xi.  ✓[M]

### 113.6.3 — Lage in z-Koordinaten

```
s = 0  <=>  z = +i/2
s = 1  <=>  z = -i/2
```

Endpunktausdruck (wohldefiniert, weil Phi-hat ganz):

```
E_{0,1}[Phi]  :=  Phi-hat(i/2) + Phi-hat(-i/2).       (113.6.2)
```

### 113.6.4 — Rohform auf der kritischen Geraden

Beitrag von P_{0,1} zu -i*(xi'/xi)(1/2+iz):

```
-i ( 1/(1/2+iz) + 1/(-1/2+iz) )
  =  -i * (-2iz)/(z^2+1/4)
  =  -2z/(z^2+1/4).                                    (113.6.3)
```

Cauchy-/Herglotz-Rohform der Endpunktkompensation; kein positives Mass.

### 113.6.5 — Definition (Vorzeichen durch 113.7 fixiert)

```
W_{pole/triv}[Phi]  =  E_{0,1}[Phi]                    (113.6.4)
                     =  Phi-hat(i/2) + Phi-hat(-i/2).
```

(eps_{0,1} = +1 durch Satz 113.7.A gesichert.)

**Satz 113.6.B:** W_{pole/triv} ist die Endpunkt-/Kompensationsauswertung
bei z = +/- i/2.  ✓[M]

### 113.6.6 — Triviale Nullstellen kompensiert

Bei vollstaendigem Gamma-Kern Psi_Gamma heben sich Pole von (1/2)psi(s/2)
und zeta'/zeta bei s=-2k residuenexakt auf.

**Satz 113.6.C:** W_triv ist in der gewaehlten Gamma-Normalform bereits
kompensiert. Einzige sichtbare Restkomponente: Endpunktterm s=0,1.  ✓[M]

### 113.6.7 — Autokorrelationsform

```
W_{pole/triv}[phi^ast*phi]
  =  Phi-hat(i/2) + Phi-hat(-i/2).                     (113.6.5)
```

Nicht strukturell positiv; renormierender Endpunktterm.

Status: **gesichert ✓[M]** (eps_{0,1}=+1 durch 113.7.A)

---

## NEU-113.7 — Bombieri-Gesamtabgleich und finale W_xi-Normalisierung

### 113.7.1 — Abkuerzungen

```
Z[Phi]     :=  sum_gamma Phi-hat(gamma)
               = sum_gamma |phi-hat(gamma)|^2    (Autokorrelation, unter RH)

E_{0,1}[Phi] :=  Phi-hat(i/2) + Phi-hat(-i/2)

P[Phi]     :=  sum_{n>=2} Lambda(n)/sqrt(n) * (Phi(log n) + Phi(-log n))

G[Phi]     :=  (1/2pi) integral_R Phi-hat(lambda) Psi_Gamma(lambda) d lambda
```

Die bisher bestimmten Komponenten lauten:

```
W_Gamma[Phi]     =  +G[Phi]
W_prime[Phi]     =  -P[Phi]
W_{pole/triv}[Phi] =  eps_{0,1} * E_{0,1}[Phi]
```

### 113.7.2 — Bombieri-Weil-Seitenform

In der verwendeten Fourier-/Mellin-Konvention lautet die Weil-Explizitformel:

```
Z[Phi]  =  E_{0,1}[Phi] - P[Phi] + G[Phi].             (113.7.1)
```

Aequivalent:

```
W_zeros  =  W_{pole/triv} + W_Gamma + W_prime           (113.7.2)
```

(Nullstellendistribution = Summe aus Endpunkt-, Gamma- und Primkomponente.)

### 113.7.3 — Vorzeichenfixierung

**Satz 113.7.A (eps_{0,1} = +1):**

Vergleich von (113.7.1) mit den W_xi-Definitionen liefert unmittelbar:

```
eps_{0,1}  =  +1.                                       (113.7.3)   ✓[M]
```

Damit:

```
W_{pole/triv}[Phi]  =  Phi-hat(i/2) + Phi-hat(-i/2).   (113.7.4)
```

**Satz 113.7.B (Vorzeichentripel):**

```
W_Gamma      =  +G,
W_prime      =  -P,
W_{pole/triv}  =  +E_{0,1}.                             (113.7.5)   ✓[M]
```

### 113.7.4 — Normalisierte Weil-Distribution (Zielobjekt fuer NEU-116)

Die normalisierte Weil-Distribution wird durch eine der zwei aequivalenten
Formen definiert:

```
W_xi^norm  :=  W_zeros                                  (Form I)
```

oder explizit:

```
W_xi^norm  :=  W_{pole/triv} + W_Gamma + W_prime        (Form II)
             =  E_{0,1}[Phi] + G[Phi] - P[Phi].         (113.7.6)
```

**Buchhaltungswarnung:**

Falls man die vierteilige NEU-115-Schreibweise
W_zeros + W_Gamma + W_prime + W_{pole/triv}
als formal getrennte Summe beibehalt, ergibt sich wegen (113.7.2):

```
W_zeros + W_Gamma + W_prime + W_{pole/triv}
  =  W_zeros + W_zeros
  =  2 W_zeros.                                         (113.7.7)
```

Das ist als Buchhaltungsform zulaessig, aber **nicht** die normalisierte
Weil-Distribution.

Fuer NEU-116 gilt daher verbindlich:

```
Zielobjekt  :=  W_xi^norm  =  W_zeros
                            =  W_{pole/triv} + W_Gamma + W_prime.  (113.7.8)
```

### 113.7.5 — Quadratform (Weil-Quadratform vollstaendig)

Fuer Autokorrelationen Phi = phi^ast * phi:

```
Q_Weil[phi]  =  < W_xi^norm, Phi-hat >

             =  ( Phi-hat(i/2) + Phi-hat(-i/2) )
              + (1/2pi) integral_R |phi-hat(lambda)|^2 Psi_Gamma(lambda) dlambda
              - sum_{n>=2} Lambda(n)/sqrt(n) * (Phi(log n) + Phi(-log n))

             =  sum_gamma |phi-hat(gamma)|^2.            (113.7.9)
```

Die letzte Gleichheit gilt unter RH (explizite Formel).

Status: **gesichert ✓/⚠[M]**
(W_prime sqrt(n)-Faktor aus m_arith-Renormierung noch zu verifizieren; NEU-116)

---

## Satzstatusmatrix (NEU-113, abgeschlossen)

| Satz | Inhalt | Status |
|---|---|---|
| 113.0 | Bombieri-Referenznormalform: drei Freiheitsgrade | ✓[M] |
| 113.1 | Fourier/Mellin: kritische Gerade = reelle Achse | ✓[M] |
| 113.2 | Autokorrelation: Phi-hat = \|phi-hat\|^2 | ✓[M] |
| 113.3 | Q_zeros normierungstreu | ✓[M] |
| 113.4 | W_prime = -P mit Lambda(n)/sqrt(n) | ⚠[M] |
| 113.5 | W_Gamma = +G explizit | ✓/⚠[M] |
| 113.6.A | Kompensationsartefakte, nicht Pole von xi | ✓[M] |
| 113.6.B | W_{pole/triv} = Endpunktauswertung z=+/-i/2 | ✓[M] |
| 113.6.C | W_triv in W_Gamma kompensiert | ✓[M] |
| 113.7.A | eps_{0,1} = +1 gesichert | ✓[M] |
| 113.7.B | Vorzeichentripel W_Gamma=+G, W_prime=-P, W_{pole/triv}=+E_{0,1} | ✓[M] |
| 113.7 | Q_Weil vollstaendig; W_xi^norm = W_zeros = W_{pole/triv}+W_Gamma+W_prime | ✓/⚠[M] |

---

## Konsequenz fuer NEU-116

Zielobjekt fuer NEU-116 (verbindlich):

```
W_xi^norm  =  W_{pole/triv} + W_Gamma + W_prime
           =  E_{0,1} + G - P
```

NEU-116 prueft:

```
W_res^top  =?  W_xi^norm
```

Zerfaellt in drei (nicht vier) scharfe Komponententests:

```
Test 116.A:  W_res^{top,pole/triv}  =?  E_{0,1}   ?[O]
Test 116.B:  W_res^{top,Gamma}      =?  G          ?[O]
Test 116.C:  W_res^{top,prime}      =?  -P         ?[O]  <- Hauptanschluss NEU-114.4
```

Test 116.C ist der entscheidende Rueckbindungstest fuer die Primkanten-Schicht X.7:

```
m -> p^k m  =?  -sum_{n>=2} Lambda(n)/sqrt(n) * (Phi(log n) + Phi(-log n))
```

---

## Verbleibende offene Kerne

| Kern | Status | Naechster Schritt |
|---|---|---|
| W_prime sqrt(n)-Verifikation aus m_arith | ⚠[M] | m_arith-Herglotz-Renormierung vs. 113.4.1 |
| NEU-116 Test 116.A: W_res^{top,pole/triv} =? E_{0,1} | ❓[O] | NEU-116 |
| NEU-116 Test 116.B: W_res^{top,Gamma} =? G | ❓[O] | NEU-116 |
| NEU-116 Test 116.C: W_res^{top,prime} =? -P | ❓[O] | NEU-116 / Haupttest |
