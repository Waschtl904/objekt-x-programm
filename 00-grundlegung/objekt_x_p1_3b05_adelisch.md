# X-P1.3b.0.5 — Adèlische Ergänzung X_ad

> Angelegt: 17. Juni 2026
> Konstruktion von X_ad = X_f hat-otimes S(R) als adel. Vervollstaendigung von X.
> Epistemischer Status: kanonisch unter Nuklearitaetsannahme; F_f auf X_f noch offen.

---

## Ausgangspunkt (aus X-P1.3b.0.4)

```
X_f = A_2D^r  liefert  Z_{X,f}(s) ~ zeta(s)   [intern, Re(s) > 1]
X_inf = S(R)  liefert  Z_{X,inf}(s) = Gamma_R(s) = pi^{-s/2} Gamma(s/2)
```

Adel. Ergaenzungsobjekt:
```
X_ad := X_f  hat-otimes  X_inf
      = A_2D^r  hat-otimes  S(R)
```

---

## Frage 1: Welches Tensorprodukt?  kanonisch unter Nuklearitaet

X_inf = S(R) ist nuklearer Frechet-Raum.
Falls X_f = A_2D^r ebenfalls nuklear: projektiv = injektiv (Standardergebnis).

```
+-------------------------------------------------------+
| X_ad := A_2D^r  hat-otimes_pi  S(R)                  |
|       = abgeschlossenes projektives Tensorprodukt     |
| In CBorn: bornologisch-projektives Tensorprodukt.     |
+-------------------------------------------------------+
```

---

## Frage 2: Wie traegt X_inf die Gamma-Spur?  ✓ [M]

Auf X_inf = S(R): Mellin-Funktional
```
Z_inf(phi; s) = int_{R^x} phi(x) |x|^s d^x x,    d^x x = dx/|x|
```

Fuer den Standardgauss g_inf(x) = e^{-pi x^2}:
```
Z_inf(g_inf; s) = int_{R^x} e^{-pi x^2} |x|^s d^x x
               = 2 int_0^inf e^{-pi x^2} x^{s-1} dx     (g_inf gerade)
```

Substitution u = pi x^2:
```
               = pi^{-s/2} int_0^inf e^{-u} u^{s/2-1} du
               = pi^{-s/2} Gamma(s/2)
               = Gamma_R(s).
```

---

## Produktspur auf X_ad  ✗ [H] (als Ziel)

Fuer einfache Tensoren a otimes phi in X_f hat-otimes S(R):
```
Z_ad(a otimes phi; s) := Z_f(a; s) * Z_inf(phi; s)
```

Fuer den Testvektor K_s otimes g_inf:
```
Z_ad(K_s otimes g_inf; s) ~ zeta(s) * Gamma_R(s)
                          = Lambda_X(s)
```

Xi-Completion:
```
xi_X(s) = (1/2) s(s-1) * Lambda_X(s)
        = (1/2) s(s-1) * pi^{-s/2} Gamma(s/2) * zeta(s)
        = xi(s)       (im Riemann-Fall)
```

---

## Frage 3: Funktionalgleichung aus Fourier-Selbstdualitaet  ✗ [H]

Auf X_inf = S(R): Fourier-Transformation F_inf.
Gauss ist selbstdual:
```
F_inf(g_inf) = g_inf,    d.h. F_inf(e^{-pi x^2}) = e^{-pi x^2}.
```

Diese Selbstdualitaet liefert den archimedischen Anteil der Funktionalgl.

Die volle Funktionalgleichung braucht zusaetzlich eine endliche Fourier-/
Poisson-Symmetrie F_f auf X_f:
```
F_ad = F_f  hat-otimes  F_inf
```

Ziel: Fuer den selbstdualen Testvektor K_f otimes g_inf soll gelten:
```
Z_ad(F_ad(K_f otimes g_inf); 1-s)  =  Z_ad(K_f otimes g_inf; s)
```
(bis auf Polkorrektur), woraus folgt:
```
xi_X(1-s) = xi_X(s).
```

```
+-------------------------------------------------------+
| Die Funktionalgleichung ist Fourier-Selbstdualitaet   |
| von X_ad = X_f hat-otimes X_inf.                     |
+-------------------------------------------------------+
```

**Archimedischer Teil: klar (F_inf(g_inf) = g_inf).**
**Endlicher Teil F_f auf X_f = A_2D^r: offen --> X-P1.3b.0.6.**

---

## Frage 4: Bleibt X_ad nuklear?  bedingt ✓

```
S(R) nuklear + A_2D^r nuklear  ==>  A_2D^r hat-otimes_pi S(R) nuklear.
```

```
+-------------------------------------------------------+
| X_ad in CBorn^nuc                                     |
| UNTER DER VORAUSSETZUNG: X_f = A_2D^r in CBorn^nuc.  |
| (Nuklearitaet von A_2D^r = OP-1 offene Frage)        |
+-------------------------------------------------------+
```

Status: bedingt ✓ [M] -- Bedingung = OP-1-Nuklearitaetsfrage.

---

## Ergebnistabelle

```
+-------+----------------------------------------------+------------------+
| Frage | Antwort                                      | Status           |
+-------+----------------------------------------------+------------------+
| (1)   | hat-otimes_pi (proj./born.-proj.)            | kanonisch (nukl.)|
| (2)   | Z_inf(phi;s) = Mellin-Integral; g_inf->Gamma_R| ✓ [M]           |
| (3)   | F_inf klar; F_f auf X_f offen                | ✗ [H] --> 0.6   |
| (4)   | nuklear, bedingt auf A_2D^r nuklear           | bed. ✓           |
+-------+----------------------------------------------+------------------+
```

---

## Vollstaendige adel. Spur (Zusammenfassung)

```
+-------------------------------------------------------+
| xi_X(s) = (1/2) s(s-1) * Gamma_R(s) * Z_{X,f}(s)   |
|         = (1/2) s(s-1) * pi^{-s/2} Gamma(s/2) * zeta(s)|
|         = xi(s)                                      |
|                                                       |
| Traeger:                                              |
|   Z_{X,f}  aus  X_f = A_2D^r   (endlich, Beurling)  |
|   Gamma_R  aus  X_inf = S(R)   (archimedisch, Gauss) |
+-------------------------------------------------------+
```

---

## Naechster Schritt: X-P1.3b.0.6  ✗ [H]

```
+-------------------------------------------------------+
| Existiert eine endliche Fourier-/Poisson-Symmetrie   |
| F_f auf X_f = A_2D^r?                                |
|                                                       |
| Kandidaten:                                           |
|   (a) Adel. Fourier-Transformation auf Q_+^x-Seite   |
|   (b) BC-involutiver Automorphismus                   |
|   (c) Poisson-Summenformel-Interpretation             |
|                                                       |
| Ziel: F_f so, dass F_ad = F_f hat-otimes F_inf        |
|       die xi-Funktionalgleichung erzeugt.             |
+-------------------------------------------------------+
```

**Status: ✗ [H] -- naechste Frage.**
