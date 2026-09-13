# CURRENT FRONT — Objekt X / NP-DUAL-COMP → A1-CERT

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudits:** [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md) · [A1 Morse diagnostic](audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md).

## 1. Gesicherte Architektur

Mit

```math
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
\qquad
\mathcal Ev=(E_+(v),E_-(v))^T,
```

gilt

```math
D_{NP}(a)=\ker\mathcal E,
```

und

```math
\boxed{
Q_W^a(v)=q_a(v)+\langle P\mathcal Ev,\mathcal Ev\rangle,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

COMMON-JUMP und die support-erhaltende `Q_0`-Nullpolparametrisierung bleiben `✓[M]`.

## 2. Screw- und Literaturkorrektur

Die pole-cleared Diskrepanz aus PR #110 ist algebraisch korrekt, aber als arithmetisches Objekt bereits im Prime+Polar-Teil von Suzukis Screw-Funktion enthalten:

```math
\mathfrak D(t)=\frac d{dt}(g_0(t)+r_0(t)).
```

Daher

```text
prime/polar discrepancy identity             ✓[M]
D as literature-new arithmetic object         ×[M]
null-pole gauge/use                           ✓[M]
publication novelty of the architecture/use   ?[O]
```

**Bibliographisches Erratum:** arXiv:2608.24827 (*Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*) ist von **Marcus Chuk**, nicht Xuefeng Zhu. Die inhaltlich importierten Zahlen bleiben unverändert: voller `L=0.8`-Lower-Bound `8.9e-18`, Upper-Bounds bis `3.2e-283` bei `L=2`, Landau--Widom-Plunge und doppelt-exponentielle Envelope-Barriere.

## 3. Turán-Firewall

Für

```math
C_v(t)=\langle T_tv,v\rangle
```

gilt

```math
\int_{\mathbb R}e^{st}C_v(t)dt
=E_s(v)\overline{E_{-s}(v)}.
```

Nullpol erzwingt zwar die beiden notwendigen linearen Gauges

```math
L_0(C_v)=0,
\qquad
L_1(C_v)=0,
```

aber selbst beide charakterisieren die Faktorbedingung `E_+=E_-=0` nicht. Daher ist ein skalares positiv-definites Turán-SDP nur eine **äußere Relaxation**.

```text
scalar Turan exactness   ×[M]
L0,L1 necessary gauges   ✓[M]
```

## 4. Exakte rank-2 completion `✓[M]`

### Strikte Coercivity

```math
\boxed{
q_a\ge\delta I\text{ auf }\ker\mathcal E
\iff
\exists\lambda,\mu>0:\
q_a+\lambda\mathcal E^*\mathcal E\succeq\mu I.
}
```

### Semidefinite Grenze

```math
\boxed{
q_a\ge0\text{ auf }\ker\mathcal E
\iff
\forall\varepsilon>0\ \exists\lambda_{a,\varepsilon}>0:\
q_a+\varepsilon I+\lambda_{a,\varepsilon}\mathcal E^*\mathcal E\succeq0.
}
```

Damit ist fixed-window NP-GAP exakt ein zweikanaliges finite-rank completion problem auf Funktionsebene.

## 5. Morse-Index-Falsifikationsgates `✓[M]`

Für jede Hermitesche Completion `H` gilt notwendig

```math
q_a+\mathcal E^*H\mathcal E\succeq0
\Longrightarrow
n_-(q_a)\le n_+(H)\le2.
```

Also:

```math
\boxed{\text{fixed-window NP completion}\Rightarrow n_-(q_a)\le2.}
```

Für den physischen Poleblock `P` ist `n_+(P)=1`, daher

```math
\boxed{Q_W^a\succeq0\Rightarrow n_-(q_a)\le1.}
```

Ein zertifizierter dritter negativer Modus von `q_a` widerlegt fixed-window NP-GAP; ein zertifizierter zweiter negativer Modus schließt die spezielle `P`-Completion aus.

## 6. Reflection/parity reduction `✓[M]`

Mit `Jv(x)=v(-x)` gilt

```math
q_a(Jv,Jw)=q_a(v,w),
\qquad
\mathcal E(Jv)=P\mathcal Ev.
```

Jede gültige Hermitesche Completion kann daher mit ihrer Spiegelung gemittelt werden. Es genügt

```math
\boxed{
H=\begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix},
\qquad \alpha,\beta\in\mathbb R.
}
```

Im even/odd Momentkanal ist dies diagonal. Der physische Poleblock ist

```math
P\sim\operatorname{diag}(+1,-1),
```

während eine skalare Completion `lambda I` zu `diag(lambda,lambda)` wird.

Unter voller Weil-Positivität ist der odd-Sektor von `q_a` automatisch nichtnegativ; jede negative Richtung von `q_a` muss dann even sein.

## 7. Kanonische Completion `lambda=1` `✓[M]`

Exakt:

```math
\boxed{
q_a+\mathcal E^*\mathcal E
=Q_W^a+\mathcal E^*(I-P)\mathcal E,
}
```

und `I-P\succeq0`. Daher würde volle fixed-window Weil-Positivität automatisch die skalare Completion `lambda=1` liefern.

`lambda=1` ist somit der erste **vorab festgelegte** Completion-Kandidat für `a=1`, nicht ein numerisch gefitteter Parameter.

## 8. Nicht-zertifizierter `a=1` Galerkin-Stresstest

Vorab festgelegte Basis:

```math
\phi_n(x)=\sin\left(\frac{n\pi(x+1)}2\right),
\qquad -1<x<1.
```

Für die verschachtelten Nullpol-Unterräume wurden diagnostisch beobachtet:

```text
N=4    min Ritz ~ 8.22e-4
N=6    min Ritz ~ 6.21e-7
N=8    min Ritz ~ 3.26e-9
N=10   min Ritz ~ 2.70e-9
N=12   min Ritz ~ 6.67e-11
```

Der `N=12`-Block von `q_1` zeigt diagnostisch genau eine negative Richtung (`~ -4.15624`), im even-Sektor; der odd-Block blieb numerisch nichtnegativ. Die finite scalar completion wurde bei `lambda≈1` numerisch PSD, mit einem winzigen resolved margin von Größenordnung `1e-15`.

**Firewall:** gewöhnliche Floating-Point-Quadratur, endlicher Frequenzcutoff, keine Arb-Enclosures und kein operatorischer Tail. Diese Zahlen sind ausschließlich Diagnostik.

## 9. Neue Default-Front — A1-CERT `?[O]`

Ziel ist ein rigoroses fixed-window Completion-Zertifikat bei

```text
a=1.0
```

— dem ersten natürlichen Stresspunkt oberhalb des publizierten `L=0.8`-Lower-Bound-Benchmarks von Marcus Chuk.

Ein gültiges Zertifikat braucht gleichzeitig:

1. vorab festgelegte parity-adaptierte Basis und Trunkierung;
2. Arb-Enclosures aller resolved Formeinträge und Momentzeilen;
3. Completion zunächst bei `lambda=1`, danach höchstens zwei reelle parity-Dualparameter;
4. zertifizierte finite Inertia/PSD;
5. rigorose Tail-Untergrenze in beiden Paritätssektoren;
6. rigorose resolved-tail Kopplungsnorm;
7. finalen Schur-Komplement-Nachweis.

Die Dualdimension ist nicht mehr die Wand. **Der theorematische Engpass ist der unendlichdimensionale Tail.**

## 10. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
Screw redundancy                                      ✓[M]
D as literature-new object                            ×[M]
scalar Turan exactness                                 ×[M]
strict rank-2 completion equivalence                  ✓[M]
semidefinite epsilon-completion equivalence            ✓[M]
Morse filters                                          ✓[M]
reflection-symmetric 2-parameter completion            ✓[M]
canonical lambda=1 identity                            ✓[M]
a=1 finite Galerkin diagnostic                        non-certified
rigorous a=1 finite block                              ?[O]
rigorous a=1 tail / Schur complement                   ?[O]
certified a=1 NP-DUAL completion                       ?[O]
all-a NP-GAP                                           ?[O]
forward Object-X candidate architecture                ✓[M]_part
full positive Object-X / RH                            ?[O]
```
