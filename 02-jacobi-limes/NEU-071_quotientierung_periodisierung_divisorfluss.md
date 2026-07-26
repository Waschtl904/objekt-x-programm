# NEU-71 — Quotientierung/Periodisierung des gerichteten Divisorflusses

**Status:** Frobenius-Korrektur ✓[M]; einfacher mod-Quotient unzureichend ✓[M]; BC-Quotient nötig ✓[M]
**Datum:** 2026-06-29/30 (Korrektur: Frobenius nur für p∤m; Orbitlänge ord_m(p), nicht log p; BC-Zeit nötig)
**Aufbaut auf:** NEU-70 (additive Divisorzyklen; p-Sektor leer; Ihara-Bass plausibel)

---

## Kerndiagnose ✓[M]

```
Der bisherige Divisorgraph lebt additiv:  r |-> r + n
Die Riemann-Zeta lebt multiplikativ:      n = p^k

Solange Zyklen aus additiven Relationen n_1 + n_2 = n_3 kommen,
entsteht nicht die Riemannsche Eulerstruktur.
```

Der gesuchte Quotient muss die **multiplikative BC-Zeit** sichtbar machen,
nicht nur additive Periodizität der r-Koordinate.

---

## Korrigierte Kandidatentabelle

| Kandidat | Mechanismus | Status |
|---|---|---|
| A — Z/pZ-Periodisierung | r |-> r+p mod p trivialisiert (Fixpunkte) | ✗[M] |
| B — Frobenius auf (Z/mZ)^* | nur für p∤m; Orbitlänge ord_m(p), nicht log p | ✗/⚠[M] |
| B' — Adélischer Skalierungsquotient / BC-Zeit | p als Skalierungsorbit mit Gewicht log p | ❓[O], stärkster Kandidat |
| C — Additive mod-m Ihara-Periodisierung | Perioden p^{k-1}, nicht log p | ⚠[M] |

---

## Harte Korrektur: Frobenius auf (Z/mZ)^* nur für p∤m ✓[M]

**Frühere Formulierung (falsch):**
```
r |-> r*p (mod m) auf (Z/mZ)^*  =>  Orbits <-> {p : p | m}
```

**Korrektur:** Die Multiplikation r |-> r*p ist auf (Z/mZ)^* nur dann eine
Automorphismusaktion, wenn (p,m) = 1, also p∤m.

Wenn p | m: Multiplikation mit p ist nicht invertierbar mod m, also keine
Aktion auf der Einheitengruppe (Z/mZ)^*.

Für p∤m liefert der klassische Frobenius:
```
sigma_p: zeta_m |-> zeta_m^p    [Frobenius im m-ten Kreisteilungskörper]
```
aber die Orbitlänge ist ord_m(p) (Ordnung von p mod m), **nicht** log p.

**Fazit:** Kandidat B in der mod-m-Form liefert nicht l(gamma_p) = log p. ✗/⚠[M]

---

## Kandidat B' — Adélischer Skalierungsquotient / Bost–Connes-Zeit ❓[O]

Stattdessen muss p als **Skalierungsendomorphismus** mit Zeitgewicht log p
auftreten. Das ist die Bost–Connes-Struktur:

```
BC-Algebra:  A_Q/Q^*   oder   Z_hat ⋊ N^x
Zeitentwicklung:  sigma_t(mu_n) = n^{it} mu_n
=> p hat Hamilton-Gewicht log p
```

Dort kommt die Primzahllänge nicht aus einer endlichen Periodenlänge mod m,
sondern aus der **Zeitentwicklung / dem Modul der Skalierungsmultiplikation**.

Konkrete Frage für NEU-72:
```
Kann A_N^{Jac,-} als Transferoperator einer BC-artigen Skalierungsaktion
rekonstruiert werden, sodass primitive Orbits gamma_p die Länge log p tragen?
```

Status: ❓[O] -> NEU-72

---

## Haupthypothese NEU-71.H (revidiert) ❓[O]

Es existiert ein Quotient Q_N (adélisch/BC-artig) derart, dass:
```
(H1) Primitive nb-Zyklen von Q_N  <->  Primzahlen p <= P(N)
(H2) l(gamma_p) = log p    [aus BC-Zeitgewicht, nicht aus mod-m-Periode]
(H3) log Z_{Q_N}(s) -> -log zeta(s)
(H4) Verbindung zu A_N: Ihara-Bass oder Schur-Komplement  =>  Doppelstruktur
```

Status: ❓[O]

---

## Verbindung zu RH-Pfad ⚠[M]

Wenn Hypothese NEU-71.H gilt:
```
m_arith(z) = -d/dz log Z_{Q_N}^{completed}(1/2+iz)
           -> -i zeta'/zeta(1/2+iz)    [Mangoldt]
```
Und Herglotz-Bedingung (NEU-63D):
```
m_arith Herglotz  <=>  RH
```

---

## Status NEU-71 (korrigiert)

| Objekt | Status |
|---|---|
| Kandidat A: Z/pZ-Periodisierung | ✗[M] |
| Kandidat B: Frobenius auf (Z/mZ)^*, nur p∤m, Länge ord_m(p) | ✗/⚠[M] |
| Kandidat B': Adélischer/BC-Skalierungsquotient | ❓[O] -> NEU-72 |
| Kandidat C: mod-m Ihara, Länge p^{k-1} log p | ⚠[M] |
| Multiplikativ-adélischer Quotient nötig (nicht additiv mod m) | ✓[M] |

---

## Literatur

- Bost, J.-B. & Connes, A.: *Hecke algebras, Type III factors and phase transitions*,
  Selecta Math. 1 (1995) (BC-System, sigma_t, Hamilton-Gewicht log p)
- Connes, A.: Selecta Math. 5 (1999) (Adeles, Skalierungsorbits, Primzahlen)
- Connes, A. & Marcolli, M.: *Noncommutative Geometry, Quantum Fields and Motives*,
  AMS 2008, Kap. 3 (BC-System und Nullstellen)
- Neukirch, J.: *Algebraic Number Theory*, Springer 1999,
  §II.10 (Frobenius, Kreisteilungskörper, ord_m(p))
