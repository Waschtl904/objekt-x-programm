# Offene Probleme — COMMON-JUMP / NP-GAP

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [Common-Jump-Audit](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md).

## Neu geschlossen

### `[NP-R1]` separate Geometriefrage — `✓[M]`

`R_1` ist nicht mehr als separater Generatorblock offen. Zusammen mit dem logarithmischen archimedischen Anteil wird er vom kontinuierlichen positiven Kanal

```math
K_t=T_{t/2}-T_{-t/2},
\qquad
h(t)dt=\frac{e^{-t/2}}{1-e^{-2t}}dt
```

erzeugt.

### `[NP-COMMON]` — `✓[M]`

Archimedischer Ort und Primzahlpotenzen liegen in derselben positiven Hilbert-Geometrie:

```math
\mu_a=h(t)dt+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
```

Die Featureform ist `X_a^*X_a>=0`.

### `[NP-SCALAR-GAUGE]` — `✓[M]`

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4).
```

Neue Außen-Prime-Atome erhöhen `X_a^*X_a` und `Gamma_a I` exakt gleich. Gaugeinvariant ist die zentrierte Paarung

```math
X_a^*X_a-\Gamma_aI.
```

### `[COMMON-JUMP-NORMAL-FORM]` — `✓[M]`

Für alle `a>0`:

```math
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle.
```

Auf Nullpol:

```math
\boxed{Q_W|_{NP}=X_a^*X_a-\Gamma_aI.}
```

---

## Priorität 0 — `[NP-GAP]` `?[O]`

Der neue einzige harte Hauptengpass ist

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|X_av\|^2}{\|v\|_2^2}
\stackrel{?}{\ge}\Gamma_a.
}
```

Für die Familie aller Fenster ist dies die verbleibende RH-äquivalente Lower-Frame-/Spektralgap-Frage.

### `[NP-GAP-A]` support-erhaltende Momentfaktorisierung

Nutze die Nullpolbedingungen als

```math
\widehat v(i/2)=\widehat v(-i/2)=0
```

und untersuche die Faktorisierung

```math
v=Q_0u,
\qquad
Q_0=-d^2/dx^2+1/4,
```

mit gleichem kompaktem Trägerscope.

Ziel: echte coercivity von `X_a^*X_a` auf `Ran Q_0`, oder ein enger No-Go gegen diese Methode.

### `[NP-GAP-B]` Fourier-/Paley-Wiener

Arbeite mit

```math
\Phi_a(z)=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)-\psi(1/4)
+2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}(1-\cos(z\log n)).
```

Die Schwierigkeit ist nicht `Phi_a>=0`, sondern die scharfe Untergrenze auf Funktionen mit den komplexen Nullbedingungen `z=±i/2`.

### `[NP-GAP-C]` nonlocal Poincare / frame mechanism

Teste nur vorab definierte, nichtzirkuläre Mechanismen:

- nonlocal Poincare-/Dirichlet-form-Ungleichungen;
- Paley-Wiener-/sampling-Struktur;
- de-Branges-/reproduzierende-Kern-Methoden;
- Schur-/Shorting-Mechanismen, sofern sie den Bound nicht aus fertiger Weil-Positivität zurückdefinieren.

---

## Danach

```text
NP-GAP
  |
  v
positive Weil form on global null-pole class
  |
  v
RH
```

Ein Beweis von NP-GAP für alle `a` wäre daher bereits RH. Hier ist besondere Zirkularitätskontrolle Pflicht.

## Auxiliary / separate

- OX-GEN-A: exakte Pole-layer geometry;
- POS-DIL #101--#105: auxiliary full-class route;
- Prime-Power AR(1): eigenständige positive Struktur;
- R37/G4c, PR #91, PR #49 separat.

## Firewalls

Nicht behaupten:

- COMMON-JUMP beweise den Lower-Frame-Bound;
- die exakte Differenz `X_a^*X_a-Gamma_aI` sei bereits eine positive Gramdarstellung der Weilform;
- fixed-`a`-Positivität allein sei RH-äquivalent;
- Publikationsneuheit sei geklärt;
- Object X oder RH seien bewiesen.