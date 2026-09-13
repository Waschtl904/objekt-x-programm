# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert eine gemeinsame Prime-/archimedische positive Featurearchitektur. Die aktuelle Hauptfront formuliert Nullpol-Positivität bei festem Fenster exakt als Rang-2-Completionproblem. Eine vollständige positive Objekt-X-Realisierung und RH bleiben offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [NP-DUAL-COMP / Screw audit](audits/P11_NP_DUAL_COMPLETION_SCREW_AUDIT_2026-09-13.md)
3. [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)
4. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## 1. Exact null-pole form

Setze

```math
q_a(v)=\|X_av\|^2-\Gamma_a\|v\|^2,
\qquad
\mathcal Ev=(E_+(v),E_-(v))^T.
```

Dann

```math
D_{NP}(a)=\ker\mathcal E
```

und

```math
\boxed{
Q_W^a(v)=q_a(v)+\langle P\mathcal Ev,\mathcal Ev\rangle,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
}
```

## 2. Screw-Function-Abgleich

Die in PR #110 benutzte pole-cleared Prime-Diskrepanz ist strukturell kanonisch, aber als arithmetisches Objekt literaturbekannt: sie ist die Ableitung des Prime+Polar-Blocks in Suzukis Screw-Funktion.

```text
identity / null-pole use                 ✓[M]
D as literature-new object               ×[M]
publication novelty of architecture      ?[O]
```

## 3. Warum scalar Turán nicht exakt genug ist

Für die Autokorrelation `C_v(t)=<T_t v,v>` gilt

```math
\int e^{st}C_v(t)dt
=E_s(v)\overline{E_{-s}(v)}.
```

Nullpol erzeugt deshalb zwei notwendige lineare Autokorrelationsbedingungen bei `s=1/2`, aber die Autokorrelation sieht nur das Produkt der beiden Faktoren. Selbst beide Bedingungen rekonstruieren `E_+=E_-=0` nicht eindeutig.

Ein scalar-Turán-/positive-definite SDP ist also eine **äußere Relaxation**: ein positives Zertifikat ist gültig, ein negatives Relaxationsresultat ist kein NP-GAP-Gegenbeispiel.

## 4. Exact rank-2 completion

Die exakte Dualität bleibt auf der Funktionsebene.

Strikte Version:

```math
q_a\ge\delta I\text{ on ker E}
\Longrightarrow
\exists\lambda_a>0:\ q_a+\lambda_aE^*E\succeq0.
```

Semidefinite Version:

```math
\boxed{
q_a\ge0\text{ on ker E}
\iff
\forall\varepsilon>0\ \exists\lambda_{a,\varepsilon}>0:
q_a+\varepsilon I+\lambda_{a,\varepsilon}E^*E\succeq0.
}
```

Damit ist fixed-window NP-GAP ein **finite-rank completion problem** mit nur zwei Momentkanälen.

## 5. Verbindung zum klassischen Poleblock

Die volle Weilform verwendet nicht irgendeine Completion, sondern exakt

```math
E^*PE,
\qquad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
```

`H=P` als positive Completion wäre bereits volle fixed-window Weil-Positivität. Das allgemeine Completion-Zertifikat ist schwächer und darf nicht mit einer vollständigen Objekt-X-Realisierung verwechselt werden.

## 6. Nächster harter Gate

Aktuelle Literatur zertifiziert volle Weil-Positivität bereits für Fenster bis `a=0.8`. Ein neuer fixed-window-Test soll daher bei

```text
a=1.0
```

ansetzen.

Ein theorematisches Computerzertifikat braucht gleichzeitig:

- interval-zertifizierte finite PSD;
- exakte Momentconstraints;
- optimierte Rang-2-Completion;
- rigorose Tail-/Schur-Komplement-Untergrenze.

Finite Ritzwerte oder ein endliches SDP ohne Tailkontrolle bleiben Diagnostik.

## 7. Status

```text
COMMON-JUMP / Q0                          ✓[M]
Suzuki screw redundancy                  ✓[M]
D as new arithmetic object              ×[M]
necessary autocorrelation gauges        ✓[M]
scalar Turan exactness                   ×[M]
rank-2 completion duality               ✓[M]
certified completion beyond a=0.8       ?[O]
all-a NP-GAP                             ?[O]
forward Object-X architecture           ✓[M]_part
full positive Object-X / RH             ?[O]
```

Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).
