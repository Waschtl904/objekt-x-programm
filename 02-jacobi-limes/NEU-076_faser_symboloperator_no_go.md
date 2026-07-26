# NEU-76 — Faser-Symboloperator und Darstellungs-No-Go

**Status:** No-Go ✓[M]; Symboloperator S ✓/⚠[M]; Feshbach-Projektion ❓[O]
**Datum:** 2026-06-30
**Aufbaut auf:** NEU-75 (Theta = M_{e_n} partial_theta delta_BC auf Monomen gesichert)

---

## Satz NEU-76.1: Theta = S partial_theta delta_BC ✓/⚠[M]

Definiere den **labelabhaengigen Symboloperator** S durch:
```
S(e_r mu_n) := e_{r+n} mu_n
```

Dann gilt auf Monomen:
```
(S partial_theta delta_BC)(e_r mu_n)
= S [partial_theta (log n e_r mu_n)]
= S [r log n e_r mu_n]
= r log n e_{r+n} mu_n
= Theta(e_r mu_n)                   ✓[M]
```

**Wichtig:** S haengt vom Monoidlabel n ab: S = [n |-> M_{e_n}].
S ist kein fixes Element einer C*-Algebra, sondern ein
labelabhaengiger (faserweiser) Symboloperator. ✓/⚠[M]

---

## Satz NEU-76.2: No-Go fuer naive BC-*-Darstellung ✓[M]

**Behauptung:** Es gibt keine kovariante *-Darstellung
```
Phi: C(T) x| N^x  ->  B(l^2(I_N))
```
die gleichzeitig erfuellt:
```
(a) Phi(mu_n) = V_n     [V_n: additiver Shift r -> r+n]
(b) Phi(e_r) = M_{e_r}  [Kreischarakter-Multiplikation]
```

**Beweis:** Jede kovariante BC-Darstellung muss die Kovarianzbedingung
```
mu_m M_{e_r} mu_m^* ~ M_{e_{mr}}    [Dilatation r -> mr]
```
erfuellen (aus der BC-Algebra-Relation e_r mu_n = mu_n e_{rn}).

Unter Phi mit (a): V_m M_{e_r} V_m^* wirkt auf e_r' als
```
V_m M_{e_r} V_m^* e_{r'} = V_m M_{e_r} e_{r'-m} = V_m e(r) e_{r'-m} = e(r) e_{r'}
```
(falls r'-m erreichbar, naiv). Das gibt M_{e_r}, nicht M_{e_{mr}}.

Aber die BC-Kovarianz verlangt M_{e_{mr}}. Widerspruch. ✓[M]

**Fazit:** V_n kann nicht gleichzeitig V_n = Phi(mu_n) in einer
kovarianten BC-Darstellung sein. NEU-74 (V_n = M_{e_n} =/= mu_n) ist
daher nicht nur eine Korrektur, sondern ein **strukturelles No-Go-Lemma**.

---

## Satz NEU-76.3 (Ziel): Feshbach-Projektion ❓[O]

Die Zielaussage:
```
Pi S R D_BC Pi^* = J_N^-    auf l^2(I_N)
```

wobei:
```
Pi: l^2(I_N) (x) l^2(N^x)  ->  l^2(I_N)    [Feshbach-/Summationsprojektion]
S: eta_{r,n} |-> eta_{r+n,n}                [Shift auf erweitertem Raum]
R: eta_{r,n} |-> r eta_{r,n}                [r-Multiplikation]
D_BC: eta_{r,n} |-> log(n) eta_{r,n}        [BC-Zeitgewicht]
```

Status: ❓[O]

---

## Kandidat NEU-76/A: Symboloperator direkt auf l^2(I_N) ⚠[M]

Definiere S direkt auf l^2(I_N):
```
S eta_{(p,m,r,u)} = eta_{(p',m,r+n,u')}    (fuer passendes n-Label)
```

Frage:
- Ist S beschraenkt auf l^2(I_N)?
- Ueberlebt P_N S P_N als korrekter V_n-Shift?
- Wie wird das n-Label in S kodiert? (S ist nicht faserweise unitaer)

Status: ⚠[M] (plausibel, Details offen)

---

## Kandidat NEU-76/B: Erweiterter Hilbertraum mit Monoidfaser ⚠[M]

Arbeite auf:
```
H_N = l^2(I_N) (x) l^2(N^x)
```
mit ONB-Vektoren eta_{r,n} (r = r-Koordinate, n = Monoidlabel).

Operatoren:
```
R     eta_{r,n} = r eta_{r,n}          [r-Multiplikation]
D_BC  eta_{r,n} = log(n) eta_{r,n}     [BC-Zeitgewicht]
S     eta_{r,n} = eta_{r+n, n}         [labelerhaltender Shift]
```

Rechnung:
```
S R D_BC eta_{r,n} = S R [log(n) eta_{r,n}]
                  = S [r log(n) eta_{r,n}]
                  = r log(n) eta_{r+n, n}   ✓[M]
```

Feshbach-Projektion:
```
Pi: H_N -> l^2(I_N),  Pi eta_{r,n} = eta_{(p,m,r,u)}  [falls n | m, 0 sonst]

Zielaussage: Pi S R D_BC Pi^* = J_N^-    ❓[O]
```

Das ist die **sauberste Formulierung** des Flaschenhals-Problems. ⚠[M]

---

## Korrektur: delta_BC vs Lambda(n) ✓[M]

In NEU-75 und hier:
```
delta_BC(mu_n) = log(n) mu_n    [gesichert, alle n]
Lambda(n) = log p  falls n = p^k, 0 sonst    [Mangoldt, nur Primpotenzen]
```

Der Ubergang log n -> Lambda(n) ist ein **separater arithmetischer Extraktionsschritt**,
nicht automatisch aus delta_BC. Benoetigt Primpotenz-Projektion oder Moebius-Inversion. ⚠[M]

---

## Status NEU-76

| Objekt | Status |
|---|---|
| S(e_r mu_n) = e_{r+n} mu_n (labelabhaengig) | ✓[M] |
| Theta = S partial_theta delta_BC (Monome) | ✓[M] |
| No-Go: naive *-Darstellung C(T) x| N^x | ✓[M] |
| S beschraenkt auf l^2(I_N) | ⚠[M] |
| Erweiterter Raum H_N = l^2(I_N)(x)l^2(N^x) | ⚠[M] |
| Pi S R D_BC Pi^* = J_N^- | ❓[O] |
| log n -> Lambda(n) (Mangoldt-Projektion) | ⚠[M] |

---

## Aktualisierter kritischer Pfad

```
NEU-73: J_N^- = sum_n log(n) V_n R; Theta = r(a) log n            ✓[M]
NEU-74: V_n ~ M_{e_n}, nicht mu_n; p-adisch No-Go                  ✓[M]
NEU-75: Theta = M_{e_n} partial_theta delta_BC (Monome)            ✓[M]
        delta_BC <-> log n (nicht Lambda(n))                        ✓[M]
NEU-76: S labelabhaengig; No-Go BC-*-Darst.; H_N = l^2(x)l^2      ✓[M]
  +-- Pi S R D_BC Pi^* = J_N^-                                      ❓[O] <- FLASCHENHALS
  +-- S beschraenkt auf l^2(I_N)                                    ⚠[M]
  +-- log n -> Lambda(n) via Primsektor-Projektion                  ⚠[M]
NEU-65: Z_N^{completed} -> C*xi                                     ❓[O]
NEU-63D: m_arith Herglotz <=> RH                                    ⚠[M]
```

---

## Literatur

- Bost & Connes: Selecta Math. 1 (1995) (Kovarianzrelation mu_m e_r mu_m^* = e_{mr})
- Laca & Raeburn: J. London Math. Soc. 59 (1999)
  (C(T) x| N^x; Kovarianzbedingung; Isometrien mu_n)
- Connes & Marcolli: AMS 2008, Kap. 3
  (Faserstruktur, Kreuzprodukt-Darstellungen)
- Feshbach, H.: Ann. Phys. 5 (1958) (Projektionstechnik)
- Schur-Komplement / Feshbach-Projektion: Reed & Simon, *Methods of Mathematical Physics*
  Vol. IV, Kap. XII.6
