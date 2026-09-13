# CURRENT FRONT — Objekt X / NP-DUAL-COMP → A1-SCHUR

> **Stand:** 13. September 2026; Registry und Objekt-X-Arbeitsdefinition unverändert.  
> **Hauptaudits:** [NP-DUAL-COMP](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md) · [A1 Morse diagnostic](audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md) · [A1 high-frequency / Prolate tail](audits/P11_A1_HIGHFREQ_PROLATE_TAIL_2026-09-13.md).

## 1. Gesicherte Completion-Architektur

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

Strict und semidefinite rank-2 Completion-Dualität, Morse-Index-Filter, Reflection/Parity-Reduktion sowie die kanonische Completion `lambda=1` bleiben `✓[M]`.

## 2. `a=1`: exakter Fouriermultiplikator `✓[M]`

Für zero-extended `v` mit Träger in `(-1,1)` gilt exakt

```math
\boxed{
q_1(v)=\int_{\mathbb R}m_1(\xi)|\widehat v(\xi)|^2\,d\xi,
}
```

mit

```math
\boxed{
m_1(\xi)
=
\operatorname{Re}\psi\left(\frac14+\frac{i\xi}{2}\right)
-\log\pi
-2\sum_{n\in\{2,3,4,5,7\}}
\frac{\Lambda(n)}{\sqrt n}\cos(\xi\log n).
}
```

Die Fensterlokalisierung erzeugt **keinen zusätzlichen Rest im quadratischen Wert**. Sie schränkt lediglich die zulässigen Fouriertransformierten auf die Paley--Wiener-Klasse zeitbegrenzter Funktionen ein.

## 3. Hochfrequenz-Positivität `✓[K/M]`

Aus der DLMF-Reihe

```math
\operatorname{Re}\psi(x+iy)-\psi(x)
=
\sum_{k\ge0}\frac{y^2}{(k+x)((k+x)^2+y^2)}
```

und einem monotonen Integralrest folgt eine elementare explizite Untergrenze.

Der Exact-Head-Arb-Gate

```text
scripts/check_a1_highfreq_multiplier_arb.py
```

zertifiziert

```math
\boxed{
m_1(\xi)>0.04
\qquad(|\xi|\ge2300).
}
```

Global gilt zugleich

```math
m_1(\xi)\ge-\Gamma_1,
```

mit `Gamma_1` explizit aus COMMON-JUMP.

## 4. Rigorous Prolate tail `✓[K/M]`

Sei `B_2300` die Fourierprojektion auf `[-2300,2300]` und

```math
C_{2300}=P_{[-1,1]}B_{2300}P_{[-1,1]}.
```

Seine timelimitierten PSWF-Eigenfunktionen `psi_k` besitzen Konzentrationseigenwerte `lambda_k`.

Karnik--Romberg--Davenport, Corollary 3, liefert für den kontinuierlichen Prolate-Parameter `c=2300` eine explizite nichtasymptotische obere Schranke. Der Arb-Gate zertifiziert

```math
\boxed{
\lambda_{1490}(2300)<0.0035.
}
```

Für

```math
\mathcal R_{1490}
=\operatorname{span}\{\psi_0,\ldots,\psi_{1489}\},
\qquad
\mathcal T_{1490}=\mathcal R_{1490}^{\perp},
```

gilt deshalb für jedes `v in T_1490`

```math
\|B_{2300}v\|^2\le\lambda_{1490}\|v\|^2.
```

Mit Hochfrequenz-Positivität und `m_1>=-Gamma_1` folgt

```math
\boxed{
q_1(v)>0.01\|v\|^2
\qquad(v\in\mathcal T_{1490}).
}
```

**Der gesamte unendlichdimensionale Prolate-Tail ist damit rigoros coercive.**

## 5. Parität

Der Prolate-Konzentrationsoperator kommutiert mit Spiegelung. Die ersten `1490` PSWF-Moden teilen sich in

```text
745 even,
745 odd.
```

Resolved space und Tail sind also mit der bereits bewiesenen even/odd Completion kompatibel.

## 6. Was für `a=1` noch offen ist — A1-SCHUR `?[O]`

Für die kanonische Completion

```math
A_1=q_1+\mathcal E^*\mathcal E
```

zerlege

```math
L^2(-1,1)=\mathcal R_{1490}\oplus\mathcal T_{1490}
```

und schreibe

```math
A_1=
\begin{pmatrix}
A_{RR}&A_{RT}\\
A_{TR}&A_{TT}
\end{pmatrix}.
```

Der neue Tail-Satz gibt bereits

```math
\boxed{A_{TT}>0.01I.}
```

Damit ist ein vollständiges `a=1`-Zertifikat auf den endlichen Schur-Komplement-Gate reduziert:

```math
\boxed{
A_{RR}-A_{RT}A_{TT}^{-1}A_{TR}\succeq0.
}
```

Eine einfache hinreichende Version wäre

```math
A_{RR}\succeq\mu_RI,
\qquad
\|A_{RT}\|^2\le0.01\mu_R.
```

Die offene Wand ist also **nicht mehr der infinite tail selbst**, sondern die zertifizierte resolved matrix und ihre Kopplung an den bereits positiven Tail.

## 7. Nicht-zertifizierte frühere Diagnostik

Die Dirichlet-Galerkinwerte aus PR #112 bleiben reine Diagnostik. Insbesondere der kleine positive Nullpol-Ritzwert und das beobachtete `lambda≈1` erhalten durch den neuen Tail-Satz **noch keinen** theorematischen Status, weil sie in einer anderen endlichen Basis ohne Arb-Schurabschluss berechnet wurden.

## 8. Literaturkontext

Marcus Chuk (arXiv:2608.24827) schreibt denselben exakten Weil-Symbolmultiplikator für kompakte Fenster und zertifiziert volle Weil-Positivität bei `L=0.8` mit einer anderen finite-reduction/envelope-Methode.

Die A1-TAIL-Front beansprucht noch keine Literaturerweiterung: Erst ein vollständiger resolved+cross Schur-Abschluss bei `a=1` wäre ein neuer fixed-window Kandidat.

## 9. Status

```text
COMMON-JUMP / Q0                                      ✓[M]
rank-2 completion / Morse / parity                    ✓[M]
canonical lambda=1 identity                            ✓[M]
exact a=1 Fourier multiplier                           ✓[M]
no window remainder in q_1 Fourier form                ✓[M]
m_1(xi)>0.04 for |xi|>=2300                            ✓[K/M]
KRD lambda_1490(c=2300)<0.0035                         ✓[K/M]
q_1>0.01 on full Prolate tail k>=1490                  ✓[K/M]
resolved 1490-mode Arb block                           ?[O]
resolved-tail coupling                                 ?[O]
final a=1 Schur complement / certificate               ?[O]
all-a NP-GAP                                           ?[O]
forward Object-X candidate architecture                ✓[M]_part
full positive Object-X / RH                            ?[O]
```

## 10. Firewalls

Do not claim:

- the positive Prolate tail proves `a=1` positivity by itself;
- the PSWF basis diagonalizes `q_1`;
- the resolved-tail crossblock is already controlled;
- the old finite Dirichlet Ritz values are now certified;
- fixed-window `a=1`, all-window NP-GAP, Object X, or RH is solved.
