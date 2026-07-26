# NEU-119 — Spektralmaß des Jacobi-Operators: Definition von m_{Omega,N}

**Stand: 4. Juli 2026**

**Rückverweis:** NEU-114 (Pfad-Label), NEU-111.2 (erste Verwendung ohne Definition)

---

## Befund: m_{Omega,N} existiert bisher nicht als definierte Größe

```
NEU-114 beschreibt den Pfad:
  A_N^{Jac,-}  ->  m_{Omega,N}  ->  m_arith  ->  Q_Weil.

NEU-111.2 verwendet m_{Omega,N}(z) := <Omega, (A_N^{Jac,-}-z)^{-1} Omega>
  ohne Definition von Omega_N und ohne Statusbewertung.

NEU-77--83 konstruieren A_N^{Jac,-}, definieren m_{Omega,N} aber nicht.

Dieser Befund gilt katalogweit:
  m_{Omega,N} existiert nicht als definierte Größe.
  Der Pfad A_N^{Jac,-} -> m_arith ist daher bisher kein mathematischer Satz,
  sondern ein Programm-Label.                                  (119.Befund)
```

**Ziel dieses Blatts:** m_{Omega,N} als Weyl-Herglotz-Funktion des Jacobi-Operators
explizit definieren, Kandidaten für Omega_N identifizieren und Statusbewertung setzen.

---

## 119.1 — Voraussetzungen aus NEU-77–83

```
Vorliegende Objekte (alle ✓[M]):

  Hilbertraum:
    H_N = l^2(I_N),  I_N = {1, ..., N}.

  Jacobi-Operator (endlichdimensional, selbstadjungiert):
    A_N^{Jac,-} = H_N + beta_N J_N^-
    J_N^-       = sum_{n in Sigma_N} log(n) V_n^{(N)} R_N
    H_N         = Diagonaloperator (Diagonalgewichte a_j)
    V_n^{(N)}   = getrunkter Shift: delta_r |-> delta_{r+n} (r+n in I_N), 0 sonst.
    R_N         = Multiplikation mit r: R_N delta_r = r delta_r.

  Da A_N^{Jac,-} auf dem endlichdimensionalen H_N = C^N definiert ist
  (N = |I_N| < infty), ist A_N^{Jac,-} eine selbstadjungierte N×N-Matrix
  (nach Wahl der Normierung beta_N).

  Bezeichnung der Eigenwerte und Eigenvektoren:
    A_N^{Jac,-} u_{j,N} = lambda_{j,N} u_{j,N},  j = 1, ..., N,
    lambda_{1,N} <= lambda_{2,N} <= ... <= lambda_{N,N}  (reell).
```

---

## 119.2 — Definition von m_{Omega,N}

### 119.2.1 — Spektralmaß

```
Definition 119.D1 (Spektralmaß):

  Sei Omega_N in H_N, ||Omega_N|| = 1, ein Referenzvektor.

  Das Spektralmaß von A_N^{Jac,-} bezüglich Omega_N ist das Borel-Maß

    mu_{Omega,N}(B) := <Omega_N, E_{A_N^{Jac,-}}(B) Omega_N>,

  wobei E_{A_N^{Jac,-}} das Spektralmaß (Projektionswertiges Maß) von
  A_N^{Jac,-} gemäß Spektralsatz bezeichnet.

  Im endlichdimensionalen Fall (N < infty) gilt explizit:

    mu_{Omega,N} = sum_{j=1}^{N} |<u_{j,N}, Omega_N>|^2  delta_{lambda_{j,N}}.

  mu_{Omega,N} ist ein endliches positives Borel-Maß auf R,
  getragen auf {lambda_{1,N}, ..., lambda_{N,N}}.

  Status: ✓[M] (bei gegebenem Omega_N).                        (119.D1)
```

### 119.2.2 — Weyl-Herglotz-Funktion

```
Definition 119.D2 (m_{Omega,N}):

  Die Weyl-Herglotz-Funktion des Jacobi-Operators A_N^{Jac,-}
  bezüglich Omega_N ist

    m_{Omega,N}(z) := int_R 1/(lambda - z) d mu_{Omega,N}(lambda)
                    = <Omega_N, (A_N^{Jac,-} - z)^{-1} Omega_N>,

  definiert für z in C \ {lambda_{1,N}, ..., lambda_{N,N}},
  insbesondere für Im(z) > 0.

  Im endlichdimensionalen Fall:

    m_{Omega,N}(z) = sum_{j=1}^{N} |<u_{j,N}, Omega_N>|^2 / (lambda_{j,N} - z).

  Eigenschaften:
    (i)  m_{Omega,N} ist holomorph auf C^+ = {Im(z) > 0}.
    (ii) Im(m_{Omega,N}(z)) > 0 für Im(z) > 0  (Herglotz-Eigenschaft),
         sofern Omega_N kein Eigenvektor von A_N^{Jac,-} ist.
    (iii) m_{Omega,N}(z-bar) = m_{Omega,N}(z)-bar  (Schwarz-Spiegelung).

  Status: ✓[M] (bei gegebenem (A_N^{Jac,-}, Omega_N)).         (119.D2)
```

---

## 119.3 — Kandidaten für Omega_N

```
Die Definition setzt Omega_N voraus. Im Katalog ist Omega_N nicht festgelegt.
Drei Kandidaten:
```

### Kandidat K1 — delta_1 (kanonischer Startvektor)

```
Omega_N := delta_1  in H_N = l^2(I_N).

Bedeutung:
  Vakuumvektor / Startvektor des Shifts.
  Kanonisch in der Darstellungstheorie von Monoid-Algebren:
  V_n^{(N)} delta_1 = delta_{1+n}  (falls 1+n in I_N).

Vorteil:
  Rein strukturell, keine zusätzliche Wahl.
  mu_{delta_1,N} ist das klassische Jacobi-Spektralmaß bezüglich
  des Startvektors (Stieltjes-Standardkonstruktion).

Risiko:
  delta_1 ist möglicherweise zu "skelettnah" — sie sieht nur
  lokale Struktur nahe r=1 und nicht die arithmetische Gewichtung
  durch R_N (Multiplikation mit r).

Status: ⚠[M] / Hauptkandidat K1.                              (K1)
```

### Kandidat K2 — KMS-/BC-Gleichgewichtsvektor

```
Omega_N := KMS-Zustandsvektor bei Temperatur beta
           des Bost-Connes-analogen Systems aus NEU-43/44.

Bedeutung:
  Der KMS-Zustand phi_beta erfüllt
    phi_beta(a) = Z_beta^{-1} Tr(e^{-beta H} a),
  wobei H = D_{BC,N} (Diagonaloperator mit log(n) als Eigenwert).
  Der GNS-Konstruktion liefert einen zyklischen Vektor Omega_beta.

Vorteil:
  Omega_beta kodiert die arithmetische KMS-Gewichtung n^{-beta}.
  Für beta -> infty: Omega_beta -> delta_1 (Grundzustand).
  Für beta = 1 (kritische Temperatur BC): arithmetisch natürlich.

Risiko:
  Omega_beta muss aus der GNS-Darstellung von A_{BC}^infty (NEU-43/44)
  explizit konstruiert werden — noch nicht im Katalog vorhanden.

Status: ?[O] / Kandidat K2.                                    (K2)
```

### Kandidat K3 — zyklischer Feshbach-Vektor

```
Omega_N := Pi_N^* delta_1 / ||Pi_N^* delta_1||  (normiert),

wobei Pi_N : H_N^{ext} -> H_N der Feshbach-Kollapsoperator (NEU-77) ist.

Bedeutung:
  Der Vektor, der durch den Feshbach-Kollaps aus dem erweiterten
  Hilbertraum auf H_N projiziert wird, wenn man mit delta_1 startet.
  Explizit:
    Pi_N^* delta_1 = sum_{n in Sigma_N} eta_{1,n}  in H_N^{ext}.
  Nach Kollaps zurück auf H_N: das sind die Einträge am Startpunkt r=1.

Vorteil:
  Direkt aus der Feshbach-Konstruktion NEU-77 identifiziert.

Risiko:
  Pi_N^* delta_1 liegt in H_N^{ext}, nicht in H_N = l^2(I_N).
  Der Kollaps Pi_N bringt ihn zurück in H_N, aber der normierte
  Vektor ist sum_{n} eta_{1,n} / sqrt(kappa_N), d.h. ein
  gleichgewichteter Superpositionsvektor über alle Kanäle.
  Ob das arithmetisch sinnvoll ist, ist unklar.

Status: ?[O] / Kandidat K3.                                    (K3)
```

---

## 119.4 — Kandidatentabelle

| Kandidat | Definition | Vorteil | Risiko | Status |
|---|---|---|---|---|
| K1: delta_1 | Standardstartvektor | kanonisch, keine Zusatzwahl | zu skelettnah? | ⚠[M] |
| K2: KMS-Vektor | GNS aus A_{BC}^infty | arithmetisch natürlich | aus NEU-43/44 noch nicht konstruiert | ?[O] |
| K3: Feshbach-Vektor | Pi_N^* delta_1 / kappa_N^{1/2} | aus NEU-77 identifiziert | liegt in H_N^{ext} | ?[O] |

---

## 119.5 — Zwischensatz: m_{Omega,N} ist wohldefiniert unter K1

```
Satz 119.S1 (Wohldefiniertheit unter K1):

  Sei Omega_N = delta_1 in l^2(I_N).
  Dann ist

    m_{delta_1,N}(z) = sum_{j=1}^{N} |<u_{j,N}, delta_1>|^2 / (lambda_{j,N} - z)

  eine wohldefinierte Herglotz-Funktion auf C^+.
  Sie ist rational mit N einfachen Polen auf der reellen Achse
  und hat das asymptotische Verhalten

    m_{delta_1,N}(z) = -1/z + O(1/z^2)  für |z| -> infty.

  Status: ✓[M].                                                 (119.S1)

Bemerkung:
  Dies ist die klassische m-Funktion (Weyl-Titchmarsh-Kodobaev) des
  endlichdimensionalen Jacobi-Systems. Existenz und Herglotz-Eigenschaft
  sind Standardresultate (Teschl, "Jacobi Operators", Kap. 2).
```

---

## 119.6 — Kritischer Übergang: m_{Omega,N} -> m_arith

```
Die Definition 119.D2 löst die Lücke auf dem Definitionsniveau.
Der kritische offene Pfeil ist:

    m_{Omega,N}(z)  ->  m_arith(z)  =  -i xi'(1/2+iz) / xi(1/2+iz)

in einem präzisen Limessinn (N -> infty, lokal gleichmäßig auf C^+).

Dafür sind drei Teilfragen offen:

(O1) Kanonische Wahl von Omega_N:                              ?[O]
     Welcher Kandidat K1/K2/K3 liefert den richtigen Limes?

(O2) Konvergenz mu_{Omega,N} -> mu_arith schwach:             ?[O]
     Das Spektralmaß mu_{Omega,N} muss schwach gegen das
     Spektralmaß von m_arith (Nullstellenmaß der Zeta-Funktion)
     konvergieren.

(O3) Bombieri-Normalisierung:                                  ?[O]
     m_arith ist nicht einfach ein Stieltjes-Integral mit einem
     Maß auf R, sondern enthält archimedische Gamma-Terme.
     Der Übergang muss die Bombieri-Renormierung aus NEU-113
     mit m_{Omega,N} abgleichen.
     => Gegenstand von NEU-120.
```

---

## 119.7 — Patch für NEU-114

```
In NEU-114 ist der Pfad

    A_N^{Jac,-}  ->  m_{Omega,N}  ->  m_arith  ->  Q_Weil

nachzupflegen mit:

  "m_{Omega,N} ist nicht in NEU-77--83 definiert.
   Definition und Wohldefiniertheit: NEU-119.
   Übergang m_{Omega,N} -> m_arith: NEU-120 (offen)."
```

---

## Satzstatusmatrix (NEU-119)

| Satz/Def | Inhalt | Status |
|---|---|---|
| 119.Befund | m_{Omega,N} fehlt im Katalog als definierte Größe | ✓[M] |
| 119.D1 | Spektralmaß mu_{Omega,N} bei gegebenem Omega_N | ✓[M] |
| 119.D2 | m_{Omega,N} als Weyl-Herglotz-Funktion | ✓[M] (bei gegebenem Omega_N) |
| 119.S1 | Wohldefiniertheit unter K1 (delta_1) | ✓[M] |
| K1 | delta_1 als Omega_N-Kandidat | ⚠[M] |
| K2 | KMS-Vektor aus NEU-43/44 | ?[O] |
| K3 | Feshbach-Vektor aus NEU-77 | ?[O] |
| O1 | Kanonische Wahl von Omega_N | ?[O] |
| O2 | Schwache Konvergenz mu_{Omega,N} -> mu_arith | ?[O] |
| O3 | Bombieri-Normalisierung (-> NEU-120) | ?[O] |

---

## Anschlüsse

| Quelle | Inhalt |
|---|---|
| NEU-77 | Feshbach-Kollaps; J_N^- = Pi_N S_N R_N D_{BC,N} Pi_N^* |
| NEU-80/81/82 | beta_N, kappa_N, Dreifach-Konflikt |
| NEU-91 | A_N^{Jac,-} explizit |
| NEU-111.2 | Erste Verwendung von m_{Omega,N} (ohne Definition) |
| NEU-113 | Bombieri-Normalisierung |
| NEU-114 | Pfad-Label; Patch nötig |
| -> NEU-120 | Bombieri-Normalisierungstest: m_{Omega,N} -> m_arith |

---

## Literatur

- Teschl, *Jacobi Operators and Completely Integrable Nonlinear Lattices* (AMS 2000),
  Kap. 2: m-Funktion, Spektralmaß, Herglotz-Darstellung.
- Simon, *Szegő's Theorem and Its Descendants* (Princeton 2011),
  Kap. 3: Weyl-Titchmarsh m-Funktion für Jacobi-Matrizen.
- Akhiezer, *The Classical Moment Problem* (Oliver & Boyd 1965),
  Kap. 2: Stieltjes-Darstellung, Herglotz-Funktionen.
- Bombieri, *Remarks on Weil's quadratic functional* (2000): Q_Weil, Normalisierung.
