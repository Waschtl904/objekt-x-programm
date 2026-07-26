# NEU-118 — Bombieri-Normalisierung: direkter Konvergenztest m_{Omega,N} -> m_arith

**Stand: 3. Juli 2026**

> **Programmatischer Neubeginn.**
> NEU-117 beendet die Objekt-X-Diagnose.
> Ab NEU-118 gilt: Nur explizite Operatoren, Kerne, Maße, Transformierte.
> Keine weiteren Strukturaxiome.

---

## Hauptkette (Erinnerung)

```
m_{Omega,N}  --?>  m_arith  -->  Herglotz  <-->  RH

  m_arith = Pi_gamma(X) = Spektralschatten              (NEU-114)
  m_arith Herglotz  <=>  RH                             (NEU-63D, ⚠[M])
  m_{Omega,N} -> m_arith: FLASCHENHALS (NEU-113 offen)  ?[O]
```

NEU-118 greift diesen Flaschenhals direkt an.

---

## NEU-118.1 — Was ist m_{Omega,N} exakt?

```
Zu klären:
  (a) Welcher Raum? L^2, Schwartz, Masse auf R/C?
  (b) Welche Formel?
      m_{Omega,N}(z) = ??
      Kandidat aus Feshbach-Kette:
        m_{Omega,N}(z) = Tr(Pi_N (A_N^{Jac,-} - z)^{-1} Pi_N)
        oder eine Transformierte davon.
  (c) Welche Normierung?
      Referenz: Bombieri (2000), Weil-Funktional.
      Konkrete Normierungskonstante aus NEU-113 zu fixieren.
  (d) Ist m_{Omega,N} bereits in NEU-77--113 explizit hingeschrieben?
      Falls ja: Stelle angeben.
      Falls nein: Das IST der erste Schritt.
```

## NEU-118.2 — Was ist m_arith exakt?

```
Aus NEU-112 (gesichert ✓[M]):
  m_arith = Stieltjes-Nullstellenmass:
    m_arith = sum_gamma delta_gamma
  wobei gamma die nicht-trivialen Nullstellen von zeta(s) durchlaeuft.

Alternativ:
  m_arith ist der Herglotz-Traeger des Nullstellenanteils
  von Q_Weil (Bombieri-Funktional), NICHT Q_Weil selbst.

Zielraum:
  m_arith ist ein positives Radon-Mass auf R
  (falls RH gilt; sonst komplexes Mass mit Anteilen ausserhalb R).
  RH <=> m_arith(C \ R) = 0.
```

## NEU-118.3 — Welche Konvergenz wird behauptet?

```
Drei moegliche Konvergenztypen (zu entscheiden):

  (K1) Schwache Konvergenz als Masse:
       m_{Omega,N}  --w-->  m_arith
       d.h.: integral f dm_{Omega,N} -> integral f dm_arith
       fuer alle f in C_b(R) (oder C_c(R)).

  (K2) Herglotz-Konvergenz:
       m_{Omega,N}(z) -> m_arith(z)  lokal gleichmaessig fuer Im(z) > 0.
       (Konvergenz der Herglotz-/Nevanlinna-Darstellungen)

  (K3) Verteilungskonvergenz:
       Im Sinne von S'(R) oder temperierten Distributionen.

  Relevanz:
       Fuer den RH-Schluss genuegt (K2): Herglotz-Konvergenz
       sichert, dass der Limes selbst Herglotz ist,
       falls die m_{Omega,N} gleichmaessig Herglotz sind.

  Offene Frage:
       Sind m_{Omega,N} fuer alle N Herglotz-Funktionen?
       (d.h. Im(m_{Omega,N}(z)) >= 0 fuer Im(z) > 0)       ?[O]
```

## NEU-118.4 — Wo scheitert oder gelingt die Bombieri-Normalisierung?

```
Aus NEU-113 (offen, Flaschenhals):

  Bombieri-Normalisierung bedeutet:
    Q_{Omega,N}[f]  --?>  Q_Weil[f]

  wobei:
    Q_{Omega,N}[f] = <Pi_N f(H_N) Pi_N>  (oder aequivalente Form)
    Q_Weil[f] = Q_zeros + Q_Gamma + Q_poles + Q_prime
                (Bombieri 2000, explizite Formel)

  Bekannte Schwierigkeit:
    Q_Gamma, Q_poles, Q_prime = archimedische/Gamma-Terme.
    Diese tauchen in der Feshbach-Kette NICHT natuerlich auf;
    sie kommen aus dem funktionalen Gleichungsterm.

  Erste konkrete Frage fuer NEU-118:
    Enthaelt die Feshbach-Kette (NEU-77--111) einen Term,
    der nach Normalisierung mit Q_Gamma + Q_poles + Q_prime
    uebereinstimmt?
    Falls nein: Wo liegt die Luecke?
    Falls ja: Welche Normierungskonstante schliesst sie?    ?[O]

  Zweite konkrete Frage:
    Q_zeros[f] = sum_gamma |f-hat(gamma)|^2
    Stimmt die Feshbach-Spur Tr(Pi_N f(H_N)^2 Pi_N) nach N->infty
    mit sum_gamma |f-hat(gamma)|^2 ueberein (bis auf Fehlerterm)?  ?[O]
```

---

## NEU-118.5 — Arbeitsplan

```
Schritt 1: m_{Omega,N} explizit hinschreiben.
  Quelle: NEU-77--113 systematisch nach expliziter Formel durchsuchen.
  Ziel: Eine einzige Formel, kein Verweis auf Axiome.

Schritt 2: Herglotz-Eigenschaft von m_{Omega,N} pruefen.
  Frage: Im(m_{Omega,N}(z)) >= 0 fuer Im(z) > 0?
  Werkzeug: Schur-Test, Positivitaet des Spektralmasses von A_N^{Jac,-}.

Schritt 3: Q_zeros-Term isolieren.
  Feshbach-Spur auf Q_zeros[f] = sum_gamma |f-hat(gamma)|^2 testen.
  Normierungskonstante aus Bombieri fixieren.

Schritt 4: Gamma/Pol/Prim-Terme.
  Pruefen ob archimedische Terme in der Kette vorhanden oder fehlend.
  Falls fehlend: Luecke als Befund festhalten (kein Axiom!).

Schritt 5: Konvergenzaussage formulieren.
  m_{Omega,N} -> m_arith in welchem Sinne?
  Bedingungen dafuer explizit angeben.
```

---

## NEU-118.6 — Statusmatrix (Eröffnungsstand)

| Punkt | Inhalt | Status |
|---|---|---|
| m_{Omega,N} explizit | Formel aus Feshbach-Kette | ?[O] — Schritt 1 |
| m_arith explizit | Stieltjes-Mass sum delta_gamma | ✓[M] (NEU-112) |
| Herglotz-Eigenschaft m_{Omega,N} | Im >= 0 fuer Im(z)>0? | ?[O] — Schritt 2 |
| Q_zeros-Identifikation | Feshbach-Spur = Bombieri-Nullstellenterm? | ?[O] — Schritt 3 |
| Gamma/Pol/Prim-Terme | In Feshbach-Kette vorhanden? | ?[O] — Schritt 4 |
| Konvergenztyp | schwach / Herglotz / Verteilung? | ?[O] — Schritt 5 |
| m_{Omega,N} -> m_arith | Gesamtkonvergenz | ?[O] — Hauptziel |

---

## Anschlüsse

| Voraussetzung | Quelle |
|---|---|
| Feshbach-Kette NEU-77--111 | NEU-77--111 |
| m_arith = Pi_gamma(X), Stieltjes-Mass | NEU-112, NEU-114 |
| Bombieri-Normalisierung (offen) | NEU-113 |
| m_arith Herglotz <=> RH | NEU-63D ⚠[M] |
| Keine weiteren Strukturaxiome | NEU-117.B |
| Hauptkette m_{Omega,N}->m_arith->Herglotz<->RH | kritischer_pfad_aktuell.md |
