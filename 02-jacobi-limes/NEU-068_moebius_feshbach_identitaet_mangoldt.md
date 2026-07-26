# NEU-68 — Möbius-Feshbach-Identität und primitive Mangoldt-Reduktion

**Status:** 1/k-Mechanismus ✓[M]; primitive Zykluszerlegung ❓[O]; Z_N->1/zeta ⚠[M]
**Datum:** 2026-06-29 (Korrektur: Feshbach-Resolvent != 1/k; Z_N->1/zeta nicht xi);
          2026-06-30 (Ergänzung: delta_BC -> log n, Lambda separat; Verbindung NEU-75/76)
**Aufbaut auf:** NEU-67 (Lambda = mu*log; 1/k im Logdet)

---

## WICHTIGE ERGÄNZUNG (NEU-75/76) ✓[M]

Die in NEU-67/68 verwendeten log(n)-Gewichte stammen operatoriell aus
```
delta_BC(mu_n) = log(n) mu_n    [BC-Derivation]
```

Der Übergang zu Lambda(n) ist KEIN automatischer Schritt:
```
log(n) --[Moebius-Inversion]--> Lambda(n)    [separater arithmetischer Extrakt.]
```

Das Euler-Produkt-Argument in NEU-68 bleibt korrekt, aber der Ursprung
des log(n)-Gewichts liegt in der BC-Derivation, nicht in einer
einfachen Operator-Eigenschaft. ✓[M]

---

## Korrektur 1: Feshbach-Resolvent != 1/k-Faktor ✓[M]

Schritt A: Feshbach-Schur-Komplement (geometrische Reihe, kein 1/k):
```
(QA_NQ - z)^{-1} = -sum_{k>=0} (QA_NQ)^k / z^{k+1}
```

Schritt B: log det des Schur-Komplements erzeugt 1/k:
```
log det(I - T) = -sum_{k>=1} Tr(T^k) / k    [1/k aus log det = Tr log]
```

Fazit: log det(Feshbach-Schur-Komplement) = relative Logdet => 1/k. ✓[M]

---

## Korrektur 2: Primitive Zykluszerlegung fehlt ✓[M]

1/k allein genuegt nicht. Benoetigt wird zusaetzlich:
```
Tr(T_N^k) = sum_{gamma prim, gamma^k Wiederholung} w(gamma)^k
```

Erst dann:
```
log Z_N(s) = -sum_{gamma prim} sum_{j>=1} e^{-js*ell(gamma)} / j
-partial_s log Z_N(s) = sum_{gamma prim} sum_{j>=1} ell(gamma) e^{-js*ell(gamma)}
```

Fuer ell(gamma_p) = log(p):
```
= sum_p sum_{j>=1} log(p) p^{-js} = sum_n Lambda(n) n^{-s}    ✓
```

Status der primitiven Zykluszerlegung des Divisorgraphen: ❓[O] -> NEU-69

---

## Korrektur 3: Z_N -> 1/zeta(s), nicht xi(s) ⚠[M]

```
Z_N^{Euler}(s) -> 1/zeta(s)         [endliches Euler-Produkt]
Z_N^{completed}(s) -> C * xi(s)     [nach Gamma-/Hadamard-Korrektur, NEU-65]
```

Fehlende Faktoren: xi(s) = (1/2) s(s-1) pi^{-s/2} Gamma(s/2) zeta(s)
D.h. Gamma-Faktor, triviale Nullstellen, archimedische Regularisierung. ⚠[M]

---

## Satz NEU-68.1 — 1/k aus log det ✓[M]

```
log det(A_N - z) = -sum_{k>=1} Tr(A_N^k) / (k z^k) + N log(-z)    [|z| gross]
```

1/k entsteht aus Tr log, nicht aus der Resolvente. ✓[M]

## Satz NEU-68.2 — Euler-Produkt-Analogie ✓[M]

```
-d/ds log(1-p^{-s}) = sum_{k>=1} log(p) p^{-ks} = sum_k Lambda(p^k) p^{-ks}
```

[k*log(p) aus Ableitung] x [1/k aus log] = log(p) = Lambda(p^k). ✓[M]

Hier erscheint log(p^k) = k log(p) als Operatorgewicht (aus delta_BC),
und der 1/k-Faktor aus der Logdet-Entwicklung reduziert k log(p) -> log(p) = Lambda(p^k). ✓[M]

---

## Status NEU-68

| Objekt | Status |
|---|---|
| 1/k aus log det (nicht Resolvent) | ✓[M] |
| delta_BC liefert log(n), Lambda separat via Moebius | ✓[M] |
| Primitive Zykluszerlegung noetig | ✓[M] |
| Euler-Produkt-Analogie | ✓[M] |
| Z_N^{Euler} -> 1/zeta (nicht xi) | ✓[M] |
| Gamma-Korrektur 1/zeta -> xi | ⚠[M] |
| Primitive Zyklen gamma_p <-> p | ❓[O] -> NEU-69 |

---

## Literatur

- Simon, B.: *Trace Ideals*, AMS 2005 (Tr log = log det, 1/k)
- Ruelle, D.: *Dynamical Zeta Functions*, Bull. AMS 1994
- Titchmarsh, E.C.: *Riemann Zeta-Function* (-zeta'/zeta = sum Lambda n^{-s})
- Apostol: *Analytic Number Theory* (Lambda = mu*log)
- NEU-75/76: delta_BC <-> log n; Lambda-Extraktion separat
