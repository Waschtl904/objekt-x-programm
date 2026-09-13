# Offene Probleme — CRITICAL-HALF SCATTERING / NP-GAP

> **Stand:** 13. September 2026.  
> Operative Quelle: [CURRENT-FRONT](CURRENT-FRONT.md).  
> Registry und Arbeitsdefinition bleiben unveraendert.

## Neu geschlossen

### `[NP-R1]`, `[NP-COMMON]`, `[NP-SCALAR-GAUGE]` — `✓[M]`

Die exakte COMMON-JUMP-Normalform ist

```math
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle,
```

mit

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4).
```

Auf NULLPOL:

```math
\boxed{Q_W|_{NP}=X_a^*X_a-\Gamma_aI.}
```

### `[CRIT-HALF-RANGE]` — `✓[M]`

```math
L_{1/2}=-\partial_x^2+1/4,
\qquad
L_{1/2}^{-1}(x,y)=e^{-|x-y|/2},
```

und fuer jedes Fenster

```math
\boxed{
C_c^\infty(-a,a)\cap\ker M(0)\cap\ker M(1)
=L_{1/2}C_c^\infty(-a,a).
}
```

NULLPOL ist exakt die support-erhaltende Range dieses Operators.

### `[CRIT-HALF-POLE]` — `✓[M]`

Auf getrennten Traegern faktorisiert derselbe Green-Kern in die beiden Pole-Randladungen:

```math
\langle f,G_{1/2}g\rangle
=E_+(f)\overline{E_-(g)}
```

oder in umgekehrter Orientierung

```math
\langle f,G_{1/2}g\rangle
=E_-(f)\overline{E_+(g)}.
```

Die OX-GEN-A-Pole-Amplituden sind somit Außen-Transferdaten desselben Critical-half-Propagators.

### `[CRIT-HALF-TREE]` und `[CRIT-HALF-RIGIDITY]` — `✓[M]`

Der P11-AR(1)-Kern

```math
p^{-|j-k|/2}
```

ist die logarithmische Abtastung von `e^{-|x-y|/2}` auf einem Prim-Sternbaum. Der gesamte fensterlose Hub+Rest-Kanalindex-Ledger besitzt eine explizite positive OU-/Tree-Gram-Realisierung.

In der Familie `e^{-sigma d}` erzwingt die P11-Amplitude `beta=3/4` exakt

```math
sigma=1/2,
```

dieselbe Skala wie NULLPOL und der Gamma-Grundmodus.

### `[NP-GAP-LIFT]` — `✓[M]`

Jedes Nullpol-`v` ist eindeutig

```math
v=L_{1/2}u,
\qquad
u\in C_c^\infty(-a,a).
```

Damit ist NP-GAP eine momentfreie Coercivity-Frage.

### `[GAMMA-RESOLVENT]` — `✓[M]`

```math
\Phi_\infty(D)
=\sum_{m\ge0}\frac2{\mu_m}D^2(D^2+\mu_m^2)^{-1},
\qquad
\mu_m=2m+1/2.
```

Der Grundmodus ist exakt `L_{1/2}`. Ein direkter Schur-Test liefert als Mechanismus-Zertifikat NP-GAP fuer `0<a<=1/16`; kein Neuheits-/Radiusrekord wird beansprucht.

### `[NP-SCALAR-ORIGIN]` — `✓[M]`

Die fruehere Frage nach dem „Restskalar“ ist geschlossen. Prime-Atome tragen exakt ihre endliche Diagonalmasse `2w_n`. Archimedisch gilt

```math
\boxed{
\kappa_*
=
\lim_{N\to\infty}
\left[
\sum_{m=0}^N\frac2{\mu_m}
-
\log\frac{N+1}{\pi}
\right].
}
```

Damit ist `Gamma_a` genau

```text
finite Prime diagonal mass
+
renormalized Gamma diagonal mass.
```

Es wird kein weiterer separater Skalar-Generator gesucht.

### `[PRIME-AR1-POISSON]` — `✓[M]`

Fuer `q_p=p^{-1/2}`:

```math
P_q^{\mathbb D}(\theta)
=1+2\sum_{k\ge1}q^k\cos(k\theta).
```

Der komplette zentrierte `p`-Power-Weil-Turm ist exakt

```math
\boxed{
(\log p)
\left[1-P_{p^{-1/2}}^{\mathbb D}(z\log p)\right].
}
```

`P_q^D` ist exakt das Toeplitz-Symbol der P11-AR(1)-Kovarianz `q^{|j-k|}`.

### `[GAMMA-POISSON]` — `✓[M]`

Mit

```math
P_y^{\mathbb H}(x)=\frac1\pi\frac{y}{x^2+y^2}
```

gilt modeweise

```math
\boxed{
A_m(z)-2/\mu_m=-2\pi P_{\mu_m}^{\mathbb H}(z).
}
```

Prime und Archimedes liegen somit auch in derselben harmonischen Kernelklasse: Disk-/Half-plane-Poisson.

### `[EULER-GAMMA-SCATTERING]` — `✓[M]`

Die expliziten unitären Faktoren

```math
S_p(z)=
\frac{1-p^{-1/2}e^{iz\log p}}
     {1-p^{-1/2}e^{-iz\log p}},
```

```math
S_\infty(z)=
\pi^{-iz}
\frac{\Gamma(1/4+iz/2)}
     {\Gamma(1/4-iz/2)}
```

haben genau die zentrierten Prime-/Archimedes-Multiplikatoren als Phasenableitungen.

Fuer

```math
S_a(z)=S_\infty(z)\prod_{p\le e^{2a}}S_p(z)
```

ist in der Fenster-Quadratikform

```math
\boxed{
Q_W(v)
=\int|\widehat v(z)|^2
\left[-i\overline{S_a(z)}S_a'(z)\right]dz
}
```

auf NULLPOL.

Die in `S_p` enthaltenen hohen Prime powers jenseits des geometrischen Cutoffs sind auf dem Fenster-Testfunktionsraum exakt null in der zentrierten Form.

---

# Prioritaet 0 — `[NP-GAP]` `?[O]`

Global bleibt

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|X_av\|^2}{\|v\|_2^2}
\stackrel?\ge\Gamma_a
}
```

fuer alle `a>0`.

Fuer die Familie aller Fenster ist dies die verbleibende RH-aequivalente Lower-Frame-/Spektralgap-Frage.

## `[NP-GAP-A]` Source-lift coercivity — Default analytischer Angriff

Nutze

```math
v=L_{1/2}u
```

vollstaendig aus:

1. erste Gamma-Moden lokal/coerciv in der `L_{1/2}`-Metrik behandeln;
2. Gamma-Rest per Resolventen-/Schurtechnik kontrollieren;
3. Prime-Jumps `L_{1/2}K_{log n}u` nicht getrennt wegwerfen, sondern mit Tree-/OU-Innovationen koppeln;
4. nur radiusstabile Mechanismen verfolgen, nicht Radiuskosmetik.

## `[NP-SCATTER]` positive conservative scattering dilation — neuer bevorzugter Struktur-Gate

Gesucht ist eine **vorwaerts definierte** positive conservative/harmonic-extension dilation, deren Compression oder Schur-Komplement auf `Ran L_{1/2}` den Fenster-Wigner--Smith-Operator

```math
-iS_a^*S_a'
```

liefert.

Zulaessige Ausgangsdaten:

```text
critical-half Green propagation L_{1/2}^{-1},
Tree-root / OU innovations,
Disk- und Half-plane-Poisson extension,
COMMON-JUMP incidence operators K_t,
canonical finite-part diagonal renormalization.
```

Nicht zulaessig ist eine Dilation, die aus fertiger Weil-Positivitaet oder aus dem gewuenschten Bound rueckwaerts definiert wird.

## `[NP-SCATTER-NOGO]` naive positivity classes eliminieren

Vor einem globalen Konstruktionsversuch sollen enge No-Go-Klassen geprueft werden:

- punktweise Positivitaet der Phasenableitung;
- Unitaritaet `=>` positive time delay;
- endliche Gamma-Moden ohne Prime-/Tree-Kopplung;
- rein kanalweise Poincare-Schranken;
- Dilationen, die die Paley-Wiener-/Fensterstruktur ignorieren.

Ein theorem-level No-Go gegen eine solche Klasse ist echter Fortschritt.

## `[NP-HARDY/DB]` Hardy-/Blaschke-/de-Branges-Route nur vorwaerts

Die neuen Disk-/Half-plane-Poisson- und Blaschke-Faktoren machen Hardy-/de-Branges-Methoden natuerlich. Offen ist, ob eine kanonische positive Raumstruktur **aus den vorhandenen Faktoren** konstruiert werden kann.

Firewall: keine bekannte RH-aequivalente de-Branges-Bedingung einfach umbenennen und als Fortschritt ausgeben.

---

## Kanonische Architektur nach diesem Durchlauf

```text
critical-half L_{1/2}
   |
   +-- Pole/NULLPOL = Green boundary charges / zero exterior charge
   +-- P11 = logarithmic OU tree / AR(1)
   +-- Prime towers = flat - disk Poisson
   +-- Gamma ladder = resolvents / half-plane Poisson
   +-- Gamma_a = finite + finite-part diagonal mass
   +-- finite-window Euler/Gamma unitary scattering S_a
                         |
                         v
                     -i S_a^* S_a'
                         |
                         v
                       NP-GAP
```

---

## Firewalls

Nicht behaupten:

- `-iS_a^*S_a'` sei punktweise positiv;
- Unitaritaet impliziere Wigner--Smith-Positivitaet;
- der abstrakte Prime-Sternbaum ersetze die raeumliche P11-Fenstergeometrie;
- ein globales klassisches Eulerprodukt werde auf `Re(s)=1/2` gebildet;
- fixed-`a`-Positivitaet allein sei RH-aequivalent;
- Publikationsneuheit sei geklaert;
- NP-GAP, full Object X oder RH seien bewiesen.
