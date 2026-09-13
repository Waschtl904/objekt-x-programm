# Objekt X — kanonische Forschungsroadmap v3.0

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Nullpol-Filter bleibt verbindlich

```math
D_{NP}=\ker M(0)\cap\ker M(1),
\qquad E|_{D_{NP}}=0.
```

Ein Hauptfront-Mechanismus muss auf `D_NP` nichttrivial bleiben. Connes–Consani Proposition C.1 liefert den global RH-äquivalenten Weil-Scope; keine fixed-window-Äquivalenz wird importiert.

## 2. COMMON-JUMP abgeschlossen `✓[M]`

Die eine Generatorfamilie ist

```math
\boxed{K_t=T_{t/2}-T_{-t/2}.}
```

Die positive gemischte Maßstruktur lautet

```math
\boxed{
\mu_a
=
h(t)dt+
\sum_{\log n\le2a}w_n\delta_{\log n},
}
```

mit

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n}.
```

Damit sind

```text
archimedean gamma contribution = continuous K_t energy
prime powers                    = atomic K_t energies
```

innerhalb derselben positiven Hilbert-Geometrie realisiert.

## 3. Exakte gemeinsame Normalform `✓[M]`

Definiere die positive Featureabbildung `X_a` aus `mu_a`. Dann für alle `a>0` und kompakt in `[-a,a]` getragene Testfunktionen:

```math
\boxed{
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle,
}
```

wobei

```math
\boxed{
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+\log\pi-\psi(1/4).
}
```

Auf Nullpol:

```math
\boxed{
Q_W(v,w)
=\langle X_av,X_aw\rangle-\Gamma_a\langle v,w\rangle.
}
```

## 4. Frühere getrennte Fronten werden subsumiert

### NP-R1

`R_1` ist kein eigener notwendiger Generatorblock mehr. Gemeinsam mit der logarithmischen archimedischen Form steckt er im kontinuierlichen positiven `K_t`-Kanal.

```text
NP-R1 separate geometry question -> closed/subsumed ✓[M]
```

### NP-SCALAR

Der isolierte Skalar ist cutoffabhängig; die Kovarianz ist jetzt vollständig geometrisiert. Neue Außen-Prime-Atome erhöhen Gramenergie und Schwelle exakt gleich.

```text
NP-SCALAR gauge covariance -> ✓[M]
```

### NP-COMMON

```text
NP-COMMON common Prime/archimedean feature geometry -> ✓[M]
```

## 5. Neue Default-Priorität — NP-GAP

Der einzige harte Rest ist

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{\substack{0\ne v\in C_c^\infty(-a,a)\\M(v)(0)=M(v)(1)=0}}
\frac{\|X_av\|^2}{\|v\|_2^2}
\stackrel{?}{\ge}\Gamma_a.
}
```

Für alle Fenster zusammen ist dies die verbleibende RH-äquivalente Frame-/Spektralgap-Frage.

### Gate NP-GAP-A — Momentfaktorisierung

Nutze

```math
M(v)(0)=M(v)(1)=0
\Longleftrightarrow
\widehat v(i/2)=\widehat v(-i/2)=0
```

und die support-erhaltende Faktorisierung durch

```math
Q_0=-\frac{d^2}{dx^2}+\frac14.
```

Ziel: intrinsische coercivity des Common-Jump-Operators auf `Ran Q_0` oder enger No-Go.

### Gate NP-GAP-B — symbol / Paley-Wiener

Untersuche den positiven Multiplikator

```math
\Phi_a(z)=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)-\psi(1/4)
+2\sum_{\log n\le2a}w_n(1-\cos(z\log n))
```

unter den komplexen Nullstellenbedingungen bei `z=±i/2`.

### Gate NP-GAP-C — nonlocal Poincare / frame theory

Teste vorab definierte Klassen von Poincare-, sampling-, de-Branges-/Paley-Wiener- oder Dirichlet-form-Mechanismen. Keine Rückwärtsdefinition aus Weil-Positivität.

## 6. Object-X-Pfad

```text
common positive K_t geometry ✓[M]
        |
        v
forward Object-X architecture ✓[M]_part
        |
        | sharp lower frame bound
        v
NP-GAP ?[O]
        |
        | if solved for all a
        v
Weil positivity on global null-pole class
        |
        v
RH
```

Der Generator-/Geometrie-Suchteil des Programms ist damit wesentlich enger: der offene Kern ist jetzt ein präziser Spektralgap in einem bereits konstruierten positiven Hilbertraum.

## 7. Auxiliary routes

- OX-GEN-A = exakte Pole-layer geometry;
- POS-DIL #101--#105 = auxiliary full-class route;
- Prime-Power AR(1) = eigenständige positive Struktur;
- PR #91, PR #49, R37/G4c separat.

## 8. Firewalls

- COMMON-JUMP beweist den Lower-Frame-Bound **nicht**.
- Kein einzelnes fixes `a` wird als RH-äquivalent behauptet.
- `forward Object-X architecture` bedeutet nicht vollständige positive Weil-Gram-Realisierung.
- Publikationsneuheit bleibt `?[O]`.
- Keine Registry-Promotion durch Roadmap/CI.