# NEU-69 — Primitive Zykluszerlegung des relativen Jacobi-Logdet

**Status:** Backtracking-Problem ✓[M]; J_N^- azyklisch ✓[M]; Ihara-Reduktion nötig ❓[O]  
**Datum:** 2026-06-29 (Korrektur: Backtracking != Primorbit; ungerade Zyklen nicht automatisch 0; J_N^- azyklisch)  
**Aufbaut auf:** NEU-68 (1/k im Logdet; primitive Zerlegung fehlend)

---

## Zentralfrage

```
Hat der Divisorgraph primitive nicht-backtracking Zyklen gamma_p
bijektiv zu den Primzahlen p <= P(N) mit Laenge l(gamma_p) = log(p)?
```

---

## Korrektur 1: Nicht alle primitiven Zyklen sind gerade ✓[M]

**Frühere Aussage (zu stark):**
```
"Im symmetrisierten Graphen sind alle primitiven Zyklen gerade."  [FALSCH allgemein]
```

**Korrekt:** Das gilt nur in **bipartiten** Sektoren.

Falls die Schrittmenge S_m additive Relationen besitzt (n_1 + n_2 = n_3), existieren
Dreieckszyklen (ungerade Laenge 3):

```
S_m = {2, 3, 5}:  Zyklus 0 -> 2 -> 5 -> 0   (Laenge 3, da 2+3=5)  => NICHT bipartit
S_m = {2}:        nur Hin-Rueck-Paare          => bipartit
```

**Korrekte Aussage:**
```
Ungerade Zyklen verschwinden nur im bipartiten Divisorgraphen.
Der p-Einzelsektor S={p} ist bipartit; allgemeine m-Sektoren meist nicht.
```

✓[M]

---

## Korrektur 2: Rückweg r->r+p->r ist Backtracking, kein Primorbit ✓[M]

Der Zyklus r -> r+p -> r hat Laenge 2 log(p), aber er ist **kein** primitiver Orbit
im Selberg-/Ihara-Sinn. Es ist ein **unmittelbarer Ruecklauf** entlang derselben Kante.

In dynamischen Zeta-Funktionen (Ihara, Selberg, Ruelle) werden
**nicht-backtracking** primitive Zyklen gezaehlt: Ruecklaeufe e -> e_bar werden
explizit entfernt.

**Konsequenz:**
```
Der symmetrisierte Jacobi-Graph erzeugt zunaechst Backtracking-Zyklen,
nicht Primorbits.

Ohne Backtracking-Entfernung: Graph-/Divisor-Zeta, nicht Riemann-Zeta.
```

✓[M]

---

## Korrektur 3: Gerichtetes J_N^- ist azyklisch ✓[M]

Szenario III (J_N^- als gerichteter Operator) ist strukturell interessant, aber:

Falls J_N^-: r |-> r+n streng r-erhoehend ist, dann ist der gerichtete Graph
**azyklisch** (DAG). Es gibt keine geschlossenen gerichteten Zyklen:

```
r < r+n_1 < r+n_1+n_2 < ...   [streng monoton, kehrt nie zurueck]
```

**Vergleich mit Selberg:** Der geodaetische Fluss schliesst sich durch den
hyperbolischen Quotientenraum. Ohne analogen Quotienten/Periodisierung
bleibt J_N^- azyklisch.

**Konsequenz:**
```
J_N^- hat natuerliche Orientierung, aber keine geschlossenen Orbits
ohne Quotient, Periodisierung oder Rueckkopplung.
```

✓[M]

---

## Gesamtbild: Strukturvergleich

| Struktur | Vorteil | Problem |
|---|---|---|
| Symm. A_N | selbstadjungiert, Herglotz | Backtracking-Zyklen, Laenge 2 log(p) |
| Gericht. J_N^- | natuerliche Richtung | azyklisch ohne Quotient |
| m=p-Feshbach | filtert Primsektoren | noch keine p^k-Wiederholungen mit log(p) |
| Ihara/non-bt | entfernt Ruecklaeufe | muss neu konstruiert werden |

Die eigentliche Krise:
```
Selbstadjungiertheit gibt Herglotz, aber erzeugt falsche Graphzyklen.
```

---

## Hypothese NEU-69.H (revidiert) ❓[O]

Eine Doppelstruktur ist noetig:

```
(1) Selbstadjungierter Operator A_N  => Spektralpositiv itaet, Herglotz
(2) Nicht-backtracking Transferoperator B_N  =>  Eulerprodukt-Orbits
```

Gekoppelt via Feshbach, Ihara-Bass oder Schur-Komplement-Identitaet:

```
det(I - B_N)  rel.  det(A_N - z)  =>  Brücke zur Riemann-Zeta
```

Status: ❓[O] -> NEU-70

---

## Status NEU-69 (korrigiert)

| Aussage | Status |
|---|---|
| Rueckweg r->r+p->r hat Laenge 2 log(p) | ✓[M] |
| Rueckweg ist Backtracking, kein Primorbit | ✓[M] |
| Ungerade Zyklen = 0 nur in bipartiten Sektoren | ✓[M] |
| J_N^- ist azyklisch ohne Quotient | ✓[M] |
| Primorbit-Struktur erfordert Nicht-Backtracking-Reduktion | ✓[M] |
| Konkrete Konstruktion: Ihara/non-bt Transferoperator | ❓[O] -> NEU-70 |

---

## Literatur

- Ihara, Y.: *On discrete subgroups of the two by two projective linear group*,
  J. Math. Soc. Japan 18 (1966) (Ihara-Zeta, nicht-backtracking Zyklen)
- Bass, H.: *The Ihara-Selberg zeta function of a tree lattice*, IMRN 1992
  (Ihara-Bass-Determinantenformel)
- Ruelle, D.: *Dynamical Zeta Functions*, Bull. AMS 1994 (nicht-backtracking, 1/k)
- Hashimoto, K.: *Zeta functions of finite graphs and representations of p-adic groups*,
  Adv. Studies Pure Math. 15 (1989) (Hashimoto-Zeta = Ihara-Zeta)
- Terras, A.: *Zeta Functions of Graphs*, Cambridge 2011 (Ihara, Backtracking, Kap. 1-2)
