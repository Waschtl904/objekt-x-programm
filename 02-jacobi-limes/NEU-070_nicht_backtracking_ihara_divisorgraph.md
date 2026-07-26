# NEU-70 — Nicht-Backtracking-/Ihara-Reduktion des Divisorgraphen

**Status:** Ihara-Bass nur plausibel ⚠[M]; p-Sektor ohne nb-Zyklen ✗[M]; additive Zyklen ✓[M]  
**Datum:** 2026-06-29 (Korrektur: S_p={p} => P_nb=leer; Ihara-Bass nicht automatisch; additive Divisorzyklen)
**Aufbaut auf:** NEU-69 (Backtracking-Problem; Doppelstruktur A_N <-> B_N noetig)

---

## Korrektur 1: p-Einzelsektor hat keine nb-Zyklen ✗[M]

**Frueherer Befund (falsch):** "Minimaler nb-Zyklus im p-Sektor hat Laenge >= 4."

**Korrektur:** Im Sektor S_p = {p} liegt auf der r-Achse nur der Graph
```
... r-p  <->  r  <->  r+p  <->  r+2p  ...
```
Das ist ein Pfadgraph (Baum/Linie). Ohne Quotient/Periodisierung:
```
S_p = {p}  =>  P_nb(G_p) = leer     [KEIN nb-Zyklus]  ✗[M]
```

Der angebliche 4er-Zyklus r -> r+p -> r+2p -> r+p -> r enthaelt beim
Schritt r+2p -> r+p den unmittelbaren Ruecklauf der Kante r+p -> r+2p.
Also ist er nb-verboten.

**Konsequenz:** Szenario II (m=p-Feshbach) liefert ohne Quotient keine
primitiven Primzahl-Orbits. ✗[M]

---

## Korrektur 2: Ihara-Bass nicht automatisch verfuegbar ⚠[M]

Die klassische Ihara-Bass-Formel:
```
det(I - uB) = (1-u^2)^{|E|-|V|} det(I - uA + u^2(D-I))
```
gilt fuer **ungewichtete** endliche ungerichtete Graphen mit Adjazenzmatrix A.

Hier traegt A_N Gewichte Theta_{ba} ~ r*log(n) und ist antisymmetrisiert:
```
A_N = (J_N^- - (J_N^-)^*) / (2i)
```

Fuer gewichtete Graphen muss die Bass-Korrektur die Kantengewichtsprodukte
w(e)*w(e_bar) enthalten, nicht den Gradoperator D-I. Die Formel muss
explizit hergeleitet werden.

**Korrekte Aussage:**
```
Ihara-Bass-Bruecke A_N <-> B_N ist plausibel,
aber nur nach Aufbau einer gewichteten Bass-Formel fuer Theta.  ⚠[M]
```

Nicht gesichert: det(I - B_N u) ~ det(I - A_N u + Q u^2).

---

## Hauptbefund: additive Divisorgraph-Zeta ✓[M]

Fuer allgemeine Schrittmenge S_m = {n >= 2 : n | m} entstehen
nb-Zyklen genau aus additiven Relationen:
```
+- n_1 +- ... +- n_k = 0    (kein unmittelbarer Ruecklauf)
```

Beispiel: S_m >= {2,3,5} (z.B. m=30):
```
2 + 3 = 5  =>  Dreieckszyklus 0 -> 2 -> 5 -> 0   [nb, Laenge = log2+log3+log5 = log30]
```

Aber: Das ist eine **additive Divisorrelation**, kein Primzahl-Orbit im
Euler-Produkt-Sinn. Die natuerliche Zeta des sym. Divisorgraphen ist daher:
```
additive Divisorgraph-Zeta  !=  Riemann-Zeta     [BEFUND]  ✓[M]
```

---

## Numerischer Test (revidiert)

Nicht pruefen: P_nb(G_N) =? {2, 3, 5}  [Primzahlbijektions-Test]

Sondern pruefen: P_nb(G_N) =? additive Divisorrelationen.

**Test m=30:** S_30 >= {2,3,5}, Dreieckszyklus 2+3=5 sichtbar.
**Test m=6:** S_6 = {2,3,6}, keine Relation 2+3=6=6, aber 2+... ?
**Test m=12:** S_12 = {2,3,4,6,12}, Relationen 2+4=6, 2+2=4, usw.

Erwartung: P_nb(G_N) ist reichhaltig, entspricht aber additiven Relationen,
nicht den Primzahlen.

---

## Szenarien (revidiert)

| Szenario | Status |
|---|---|
| I: Kanten = Orbits (Divisor-Zeta) | plausibel ⚠[M] |
| II: m=p-Feshbach + Ihara | schwach: S_p={p} leer ohne Quotient ✗[M] |
| III: Quotient/Periodisierung J_N^- | staerkster Kandidat ❓[O] -> NEU-71 |

---

## Status NEU-70

| Objekt | Status |
|---|---|
| Ihara-Bass A_N <-> B_N (allgemein) | ⚠[M] (nicht gesichert) |
| Gewichtete Bass-Formel fuer Theta | ❓[O] |
| S_p={p} => P_nb = leer (ohne Quotient) | ✗[M] |
| Symmetr. Graph erzeugt additive nb-Zyklen | ✓[M] |
| Additive Zyklen -> Riemann-Zeta | ✗/❓[O] |
| Quotient/Periodisierung noetig | ⚠[M] -> NEU-71 |

---

## Literatur

- Bass, H.: IMRN 1992 (Ihara-Bass, gewichtete Version)
- Stark, H.M. & Terras, A.A.: Adv. Math. 121 (1996) (gewichtete Ihara-Zeta)
- Terras, A.: *Zeta Functions of Graphs*, Cambridge 2011, Kap. 2-3
- Sunada, T.: *L-functions in geometry and some applications*, Springer LNM 1201 (1986)
  (Quotienten und Zeta-Funktionen)
