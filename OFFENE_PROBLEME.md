# Offene Probleme — NP-DUAL-COMP / A1-CERT

> **Stand:** 13. September 2026.  
> Operative Audits: [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md) · [A1 Morse diagnostic](audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md).

## Neu geschlossen

### `[SCREW-REDUNDANCY]` `✓[M]`

Die pole-cleared Diskrepanz aus PR #110 ist der Prime+Polar-Ableitungsblock der Suzuki-Screw-Funktion. Neuheitsclaim als neues arithmetisches Objekt: `×[M]`.

### `[TURAN-EXACTNESS]` `×[M]`

Die notwendigen Autokorrelationsgauges

```math
L_0(C)=L_1(C)=0
```

charakterisieren `E_+=E_-=0` auf Faktorebene nicht. Scalar-Turán bleibt nur eine äußere Relaxation.

### `[RANK2-COMPLETION]` `✓[M]`

Strict exakt:

```math
\boxed{
q_a\ge\delta I\text{ on }\ker E
\iff
\exists\lambda,\mu>0:
q_a+\lambda E^*E\succeq\mu I.
}
```

Semidefinite exakt:

```math
\boxed{
q_a\ge0\text{ on }\ker E
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon E^*E\succeq0.
}
```

### `[MORSE-FILTER]` `✓[M]`

Für jede Hermitesche `2x2`-Completion `H`:

```math
q_a+E^*HE\succeq0
\Longrightarrow
n_-(q_a)\le n_+(H)\le2.
```

Für die physische Weil-Matrix

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

folgt wegen `n_+(P)=1`:

```math
Q_W^a\succeq0\Longrightarrow n_-(q_a)\le1.
```

Damit gelten die Falsifikationsgates:

```text
certified 3 negative directions of q_a => no fixed-window rank-2 NP completion
certified 2 negative directions of q_a => physical P-completion impossible
```

### `[PARITY-DUAL]` `✓[M]`

Reflection symmetrization reduces every relevant Hermitian completion to

```math
H=\begin{pmatrix}\alpha&\beta\\\beta&\alpha\end{pmatrix},
```

also auf zwei reelle even/odd Dualparameter.

Der physische Poleblock ist in dieser Basis `diag(+1,-1)`.

### `[LAMBDA-ONE]` `✓[M]`

```math
q_a+E^*E
=Q_W^a+E^*(I-P)E,
\qquad I-P\succeq0.
```

Daher ist `lambda=1` der kanonische erste Completion-Kandidat für den `a=1`-Versuch.

---

## Priorität 0 — `[DUAL-CERT-1.0]` `?[O]`

Baue ein **rigoroses** fixed-window Completion-Zertifikat bei

```text
a=1.0.
```

Der externe Lower-Bound-Benchmark `L=0.8`, `8.9e-18` stammt korrekt von **Marcus Chuk**, arXiv:2608.24827.

Pflichten:

1. parity-adaptierte Basis/Trunkierung vor dem Ergebnis festlegen;
2. Arb-Enclosures für Formmatrix und beide Momentzeilen;
3. `lambda=1` zuerst testen; danach höchstens zwei reflection-symmetrische Dualparameter optimieren;
4. finite Inertia/PSD rigoros zertifizieren;
5. Tail-Untergrenze in beiden Paritätssektoren beweisen;
6. resolved-tail Kopplung rigoros begrenzen;
7. finalen Schur-Komplement-Nachweis führen.

**Der Tail ist die Hauptwand.** Eine finite positive Matrix ist ohne Punkte 5--7 nur Diagnostik.

### Aktuelle Diagnostik — kein Status

In der vorab festgelegten Dirichletbasis bei `a=1` wurden beobachtet:

```text
null-pole min Ritz: N=4  ~8.22e-4
                   N=6  ~6.21e-7
                   N=8  ~3.26e-9
                   N=10 ~2.70e-9
                   N=12 ~6.67e-11
```

Der `N=12`-Vollblock von `q_1` zeigte numerisch eine negative Richtung, im even-Sektor, und die scalar completion wurde bei `lambda≈1` numerisch PSD.

Keine Arb-Enclosures, kein Tail: **nicht zertifiziert**.

---

## Priorität 1 — `[A1-TAIL]` `?[O]`

Gesucht ist eine rigorose lower-bound architecture für den unresolved Tail der completed form.

Zu prüfen:

- parity-separierte Fourier-/Dirichlet-Tails;
- resolvent-channel decomposition des archimedischen Operators;
- Prime-shift / AR(1)-Tail nur zentriert, nicht per separater Normsumme;
- Landau--Widom als Kalibrierung, nicht als Beweis;
- Schur-Komplement-Bound für resolved-tail coupling.

Ein bloßer Punktweise-Envelope-Ansatz muss gegen die von Marcus Chuk dokumentierte doppelt-exponentielle Frequenzbarriere geprüft werden.

---

## Priorität 2 — `[COMPLETION-STRUCTURE]` `?[O]`

Suche eine analytische Regel für den even/odd Completionblock

```math
H_a\sim\operatorname{diag}(h_e(a),h_o(a))
```

oder für scalar `lambda_a`, die nicht auf jedem Fenster neu gefittet wird.

Besonders prüfen:

- ob `lambda=1` auf einem größeren Bereich direkt zertifizierbar ist;
- Verbindung zum klassischen Poleblock `diag(+1,-1)`;
- Monotonie oder cutoff-gauge covariance in `a`;
- Q0/COMMON-JUMP als Tailmechanismus.

---

## Priorität 3 — `[TURAN-RELAX]`

Scalar-Turán/positive-definite SDP bleibt als sufficient relaxation zulässig. Ein positives Zertifikat beweist mehr als nötig; ein negativer Relaxationszeuge falsifiziert NP-GAP **nicht**.

---

## Firewalls

- `D` nicht als neue arithmetische Größe verkaufen;
- falsche Attribution `Xuefeng Zhu` nicht weiterverwenden; arXiv:2608.24827 ist Marcus Chuk;
- scalar autocorrelation nicht mit factor-level null-pole verwechseln;
- die `a=1` Galerkinwerte nicht promoten;
- finite PSD ohne tail != theorem;
- fixed-window positivity != RH;
- all-a completion bleibt RH-hart;
- Object X / RH offen.
