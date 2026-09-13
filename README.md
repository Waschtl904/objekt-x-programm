# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische Beiträge der vollständigen Weil-Form aus demselben Mechanismus hervorgehen. Arbeitsname: **Objekt X**.

> **Redaktioneller Stand: 13. September 2026.**  
> Ein wesentlicher gemeinsamer Prime-/archimedischer Hilbert-Baustein ist konstruiert. Eine vollständige positive Objekt-X-Realisierung und ein Beweis der Riemannschen Hypothese liegen nicht vor.

## Hier beginnen

1. **[Aktueller Arbeitsstand](CURRENT-FRONT.md)**
2. **[Common-Jump-Audit](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)**
3. **[Nullpol-Reklassifikation](audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md)**
4. **[Aktueller Stand](00-uebersicht/AKTUELLER_STAND.md)**
5. **[Forschungsroadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)**
6. **[DAG](00-uebersicht/DAG.md)**

## Aktueller Durchbruch: dieselbe Jump-Geometrie an allen Stellen

Für die unitäre Translation `T_t` setze

```math
\boxed{K_t=T_{t/2}-T_{-t/2}.}
```

Die Weil-Form zeigt dann einen gemeinsamen positiven Mechanismus:

- der **archimedische Ort** ist der kontinuierliche Maßanteil
  ```math
  h(t)dt=\frac{e^{-t/2}}{1-e^{-2t}}dt;
  ```
- jede **Primzahlpotenz** `n=p^k` ist ein Atom bei `t=log n` mit Gewicht
  ```math
  w_n=\frac{\Lambda(n)}{\sqrt n}.
  ```

Für Funktionen mit Träger in `[-a,a]` ist das gemischte positive Maß

```math
\boxed{
\mu_a=h(t)dt+
\sum_{\log n\le2a}w_n\delta_{\log n}.
}
```

Damit entsteht eine konkrete Hilbert-Featureabbildung `X_a`, deren Gramform

```math
\langle X_av,X_aw\rangle
=
\int_0^\infty h(t)\langle K_tv,K_tw\rangle dt
+
\sum_{\log n\le2a}w_n
\langle K_{\log n}v,K_{\log n}w\rangle
```

positiv ist.

**Prime und Archimedes verwenden also exakt dieselbe Operatorfamilie `K_t`; nur das Maß über `t` zerfällt in einen kontinuierlichen und einen atomaren Teil.**

## Exakte Weil-Normalform

Die feste archimedische Schwelle ist

```math
\kappa_*=\log\pi-\psi(1/4)
=\log(8\pi)+\gamma+\frac\pi2,
```

und

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}+\kappa_*.
```

Für jedes `a>0` und kompakt in `[-a,a]` getragene glatte Testfunktionen gilt exakt

```math
\boxed{
Q_W(v,w)
=\langle Ev,PEw\rangle
+\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle.
}
```

Hier ist `E` die bereits identifizierte Polschicht:

```math
E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).
```

## Nullpol-Hauptroute

Auf

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

verschwindet die Polschicht. Daher

```math
\boxed{
Q_W(v,w)
=\langle X_av,X_aw\rangle
-\Gamma_a\langle v,w\rangle.
}
```

Damit sind die bisher getrennten Blöcke `log|D|`, `R_1`, Prime shifts und Exterior-shell-Buchung in einer positiven gemeinsamen Geometrie vereinigt.

## Was jetzt noch offen ist

Der Generator-/Feature-Suchteil ist nicht mehr der Hauptengpass. Offen ist die scharfe Lower-Frame-Bedingung

```math
\boxed{
\lambda_{NP}(a)
:=
\inf_{0\ne v\in C_c^\infty(-a,a)\cap D_{NP}}
\frac{\|X_av\|^2}{\|v\|_2^2}
\stackrel{?}{\ge}\Gamma_a
}
```

für alle `a>0`.

Für die Familie aller Fenster ist dies, über das globale restricted Weil-Kriterium von Connes–Consani, die verbleibende RH-äquivalente Spektralgap-/Frame-Frage.

## Status

```text
common Prime/archimedean K_t geometry       ✓[M]
exact all-a common-jump normal form          ✓[M]
cutoff-gauge covariance                      ✓[M]
forward Object-X candidate architecture      ✓[M]_part
sharp NULLPOL frame bound                    ?[O]
full positive Object-X realization / RH      ?[O]
publication novelty                          ?[O]
```

OX-GEN-A bleibt die exakte Polschicht. POS-DIL #101--#105 bleibt eine mathematisch gültige auxiliary full-class route.

## Firewalls

- Eine exakte Darstellung als **positive Gramform minus Schwelle** ist noch keine positive Gramdarstellung der gesamten Weilform.
- Der Lower-Frame-Bound ist nicht bewiesen.
- Kein einzelnes fixes Fenster wird als RH-äquivalent behauptet.
- Keine Publikationspriorität wird beansprucht.
- Ein Merge oder erfolgreicher CI-Lauf ist keine Theorem-Registry-Promotion.

Ausarbeitungen: [papers/](papers/) · Audits: [audits/](audits/) · Registry: [ACTIVE_THEOREM_REGISTRY](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md) · Einstieg: [EINSTIEGSPROMPT](EINSTIEGSPROMPT.md).

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff).