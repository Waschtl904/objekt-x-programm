# NEU-114 — Rückbindung des Spektralschattens an Objekt X

**Stand: 1. Juli 2026 | Patch: 4. Juli 2026 (m_{Omega,N}-Verweis)**

---

## Ausgangsbefund

Die Analyse NEU-77–113 hat nicht Objekt X selbst konstruiert, sondern dessen
spektrale Projektion auf die kritische γ-Achse freigelegt.
Der aktuelle Pfad

```
A_N^{Jac,-}  ->  m_{Omega,N}  ->  m_arith  ->  Q_Weil
```

ist daher als **Spektralschatten-Spur** von X zu klassifizieren, nicht als
Konstruktion von X selbst.

> **Patch (4. Juli 2026):**
> m_{Omega,N} ist **nicht** in NEU-77–83 als definierte Größe vorhanden.
> Definition (Weyl-Herglotz-Funktion des Jacobi-Operators) und Statusbewertung: **NEU-119**.
> Übergang m_{Omega,N} -> m_arith (Bombieri-Normalisierung): **NEU-120** (offen).

---

## Originalstruktur von Objekt X

Objekt X ist höherdimensional und kohomologisch-kategorial definiert
(Ebene XVI, ebene-XVI-objekt-x.md):

```
(A_2D^r,  [omega_2],  [L_3],  W_{res,BC}^{top},  m -> p^k m)
```

Die Nullstellen der Zeta-Funktion erscheinen in diesem Profil nur als
Projektion X.2 — nicht als Definition von X.

Daher gilt:

```
m_arith  =/=  X
```

Korrekt ist höchstens:

```
m_arith = Pi_gamma(X)
```

falls die Rückbindung der oberen Schichten gelingt.

---

## Zwei parallele Spuren (ab NEU-114)

| Spur | Inhalt | Status |
|---|---|---|
| Spektralschatten-Spur | NEU-77–113: Feshbach / Jacobi / Herglotz / Weil | aktiv |
| X-Rückbindungs-Spur | HH2 / HH4 / W_res^top / Frobenius / Primkanten | reaktiviert |

Der aktuelle Pfad gilt als:

```
aktueller Pfad  =  Pi_gamma-Analyse von X
```

Nicht:

```
aktueller Pfad  =  X
```

---

## Kommutativitätsdiagramm

```
X  ---[W_res^top, omega_2, L_3]-->  kohomologisch-topologische Spurform
|                                            |
Pi_N                                         ?
|                                            |
A_N^{Jac,-}  ---[m_{Omega,N}]-->  m_arith  ->  Q_Weil
                      ^
                      |
              Definition: NEU-119
              Uebergang -> m_arith: NEU-120 (offen)
```

Die offene Frage ist nicht mehr nur:

```
m_{Omega,N}  ->  m_arith
```

sondern:

```
Pi_gamma(W_res^top, [omega_2], [L_3], KMS)  =?=  m_arith / Q_Weil
```

---

## Vier Rückbindungstests

**Test 114.1 — HH2-Test:**

```
[omega_2]  ->?  arithmetische Variation des Herglotz-Kanals
```

Status: ❓[O]

**Test 114.2 — HH4-/Sekundärtest:**

```
[L_3]  ->?  Anomalie-/Obstruktionsterm der Projektion
```

Status: ❓[O]

**Test 114.3 — Spurform-Test:**

```
W_{res,BC}^{top}  ->?  Q_Weil  (oder Bombieri-Normalisierung)
```

Status: ❓[O]  ← zentraler Rückbindungstest

**Test 114.4 — Primkanten-Test:**

```
m -> p^k m  ->?  Lambda(p^k) = log p  (Primterm explizite Formel)
```

Status: ⚠[M] (log n gesichert, Lambda(n) via Möbius ausstehend, NEU-67/75)

---

## Statuskorrektur der Äquivalenz

Der Satz

```
RH  <=>  m_arith Herglotz   (NEU-63D)
```

gehört zur **Spektralschatten-Spur**.

Der X-vollständige Satz lautet:

```
X  --Pi_gamma-->  m_arith    und    m_arith Herglotz  <=>  RH
```

Also:

```
X  =>  Pi_gamma(X) = m_arith  =>  RH-Kanal
```

Nicht:

```
X  =  m_arith
```

---

## Satzstatusmatrix

| Satz | Inhalt | Status |
|---|---|---|
| 114.0 | m_arith = Pi_gamma(X), nicht X selbst | ✓[M] |
| 114.1 | HH2-Rückbindung [omega_2] -> Herglotz-Kanal | ❓[O] |
| 114.2 | HH4-Rückbindung [L_3] -> Obstruktionsterm | ❓[O] |
| 114.3 | Spurform W_res^top -> Q_Weil | ❓[O] |
| 114.4 | Primkanten m->p^k m -> Lambda(p^k) | ⚠[M] |
| 114.5 | Vollständige Rückbindung: Pi_gamma(X) = m_arith/Q_Weil | ❓[O] |
| 114.P | m_{Omega,N} Definitionslücke geschlossen: NEU-119 | ✓[M] |

---

## Konsequenz für NEU-113

NEU-113 (Bombieri-Normalisierung) bleibt gültig und notwendig — es ist der
notwendige Abschluss der Spektralschatten-Spur. Aber sein Status ist:

```
NEU-113 beweist hoechstens X.2-Projektion, nicht X selbst.
```

Erst wenn alle vier Tests in NEU-114 bestehen, darf der Spektralschattenpfad
als Projektion des ursprünglichen Objekts X gelten.
