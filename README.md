# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert eine gemeinsame Prime-/archimedische positive Featurearchitektur. Die aktuelle Hauptfront formuliert Nullpol-Positivität bei festem Fenster exakt als Rang-2-Completionproblem; der erste neue Stresspunkt ist `a=1`. Eine vollständige positive Objekt-X-Realisierung und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [A1 Morse / Completion diagnostic](audits/P11_NP_DUAL_A1_MORSE_DIAGNOSTIC_2026-09-13.md)
3. [NP-DUAL-COMP / Screw audit](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md)
4. [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)
5. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## 1. Exact null-pole form

```math
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
\qquad
\mathcal Ev=(E_+(v),E_-(v))^T,
\qquad
D_{NP}(a)=\ker\mathcal E.
```

Die volle lokale Weilform ist

```math
\boxed{
Q_W^a(v)=q_a(v)+\langle P\mathcal Ev,\mathcal Ev\rangle,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

## 2. Literaturkorrekturen

Die pole-cleared Prime-Diskrepanz aus PR #110 ist als arithmetisches Objekt literaturbekannt: sie ist die Ableitung des Prime+Polar-Blocks in Suzukis Screw-Funktion.

```text
identity / null-pole use                 ✓[M]
D as literature-new object               ×[M]
publication novelty of architecture      ?[O]
```

Bibliographisches Erratum: arXiv:2608.24827 (*Weil positivity in compact windows: certified two-sided bounds and a Landau--Widom decay law*) ist von **Marcus Chuk**, nicht Xuefeng Zhu. Das Paper zertifiziert volle Positivität bei `L=0.8` mit Lower Bound `8.9e-18` und dokumentiert die Landau--Widom-/Tail-Barriere.

## 3. Scalar Turán ist nur eine Relaxation

Für `C_v(t)=<T_t v,v>` gilt

```math
\int e^{st}C_v(t)dt
=E_s(v)\overline{E_{-s}(v)}.
```

Nullpol erzeugt notwendige lineare Autokorrelationsgauges, aber die Autokorrelation sieht nur das Produkt der beiden Faktoren. Selbst zwei skalare Bedingungen rekonstruieren `E_+=E_-=0` nicht.

Ein scalar-Turán-/positive-definite SDP ist daher eine **äußere Relaxation**: ein positives Zertifikat genügt; ein negativer Relaxationszeuge ist kein NP-GAP-Gegenbeispiel.

## 4. Exact rank-2 completion

Strikte Coercivity:

```math
\boxed{
q_a\ge\delta I\text{ on }\ker E
\iff
\exists\lambda,\mu>0:
q_a+\lambda E^*E\succeq\mu I.
}
```

Semidefinite Grenze:

```math
\boxed{
q_a\ge0\text{ on }\ker E
\iff
\forall\varepsilon>0\ \exists\lambda_\varepsilon>0:
q_a+\varepsilon I+\lambda_\varepsilon E^*E\succeq0.
}
```

Damit ist fixed-window NP-GAP ein zweikanaliges finite-rank completion problem auf Funktionsebene.

## 5. Morse-Index-Filter

Für jede positive Hermitian Completion gilt notwendig

```math
q_a+E^*HE\succeq0
\Longrightarrow
n_-(q_a)\le n_+(H)\le2.
```

Für den physischen Weil-Poleblock `P`, der nur eine positive Eigenrichtung besitzt,

```math
\boxed{Q_W^a\succeq0\Longrightarrow n_-(q_a)\le1.}
```

Damit sind drei bzw. zwei zertifizierte negative Richtungen sofortige Falsifikationsgates für allgemeine bzw. physische Completion.

## 6. Parity-reduced dual and canonical `lambda=1`

Reflection symmetry reduziert jede relevante Hermitian Completion auf zwei reelle even/odd Parameter:

```math
H\sim\operatorname{diag}(h_e,h_o),
\qquad
P\sim\operatorname{diag}(+1,-1).
```

Zudem gilt exakt

```math
\boxed{
q_a+E^*E
=Q_W^a+E^*(I-P)E,
\qquad I-P\succeq0.
}
```

Daher ist `lambda=1` der kanonische erste scalar-completion Kandidat für `a=1`, nicht ein nachträglich gefitteter Wert.

## 7. `a=1` Diagnostic — ausdrücklich nicht zertifiziert

In der vorab festgelegten Dirichletbasis

```math
\phi_n(x)=\sin\left(\frac{n\pi(x+1)}2\right)
```

wurden auf den endlichen Nullpol-Unterräumen ungefähr beobachtet:

```text
N=4    min Ritz ~ 8.22e-4
N=6    min Ritz ~ 6.21e-7
N=8    min Ritz ~ 3.26e-9
N=10   min Ritz ~ 2.70e-9
N=12   min Ritz ~ 6.67e-11
```

Der `N=12`-Block von `q_1` zeigte numerisch eine negative Richtung im even-Sektor; die scalar completion wurde bei `lambda≈1` numerisch PSD.

Diese Werte beruhen auf ordinary floating-point quadrature und besitzen **keine** Arb-/Tail-Zertifizierung.

## 8. Nächster harter Gate — A1-CERT

Der erste natürliche Stresspunkt jenseits des publizierten Marcus-Chuk-Lower-Bound-Fensters `L=0.8` ist

```text
a=1.0.
```

Ein theorematisches Computerzertifikat benötigt gemeinsam:

1. parity-adaptierte vorab festgelegte Basis/Trunkierung;
2. Arb-Enclosures der Formmatrix und Momentzeilen;
3. `lambda=1` als ersten Completiontest, danach höchstens zwei even/odd Dualparameter;
4. certified finite inertia / PSD;
5. rigorose lower bounds für unresolved even/odd tails;
6. rigorous resolved-tail coupling bounds;
7. finalen Schur-Komplement-Nachweis.

**Finite PSD ohne Tailkontrolle bleibt Diagnostik. Der Tail ist jetzt der eigentliche theorematische Engpass.**

## 9. Status

```text
COMMON-JUMP / Q0                          ✓[M]
Suzuki screw redundancy                  ✓[M]
D as new arithmetic object              ×[M]
scalar Turan exactness                   ×[M]
rank-2 completion duality               ✓[M]
Morse filters                            ✓[M]
parity-reduced dual                      ✓[M]
canonical lambda=1 identity              ✓[M]
a=1 finite diagnostic                   non-certified
rigorous a=1 tail / Schur complement    ?[O]
certified a=1 completion                ?[O]
all-a NP-GAP                             ?[O]
forward Object-X architecture           ✓[M]_part
full positive Object-X / RH             ?[O]
```

Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).
