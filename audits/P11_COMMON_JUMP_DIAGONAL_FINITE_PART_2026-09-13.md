# P11 Audit — COMMON-JUMP diagonal finite part

**Datum:** 13. September 2026  
**Basis:** NULLPOL-COMMON plus Critical-half Gamma-resolvent ladder.  
**Rolle:** theorem-level Identifikation des bisher offenen Skalar-/Threshold-Charakters.  
**Registry:** unveraendert.  
**Nonclaim:** kein NP-GAP-/RH-Beweis; keine Publikationsprioritaet behauptet.

---

## 0. Kurzurteil

Die COMMON-JUMP-Schwelle

```math
\Gamma_a
=2\sum_{n\in\mathcal P_a}w_n+\kappa_*,
\qquad
w_n=\frac{\Lambda(n)}{\sqrt n},
```

ist kein algebraisch fremder Skalar neben der positiven Featuregeometrie.

- Der Prime-Anteil `2 w_n` ist exakt die Diagonalmasse des positiven Jump-Operators `w_n K_{log n}^*K_{log n}`.
- Der archimedische Anteil `kappa_*` ist exakt die **renormalisierte Diagonal-/Hochfrequenzmasse** der positiven Gamma-Resolventenleiter.

Mit

```math
\mu_m=2m+\frac12
```

gilt exakt

```math
\boxed{
\kappa_*
=
\lim_{N\to\infty}
\left(
\sum_{m=0}^N\frac{2}{\mu_m}
-
\log\frac{N+1}{\pi}
\right).
}
```

Damit ist

```math
\boxed{
\Gamma_a
=
\text{finite Prime diagonal mass}
+
\text{renormalized archimedean diagonal mass}.
}
```

Die bisherige `NP-SCALAR`-Frage ist damit strukturell weiter geschlossen: offen bleibt nicht mehr die Herkunft der Schwelle, sondern ausschliesslich, warum die **zentrierte/renormalisierte** Common-Jump-Form auf NULLPOL nichtnegativ sein sollte.

Status:

```text
Prime diagonal threshold interpretation                 ✓[M]
Gamma ladder finite-part identity for kappa_*           ✓[M]
full COMMON-JUMP threshold = canonical diagonal mass    ✓[M]
UV asymptotic normalization at scale 2pi                ✓[M]
sharp centered NP-GAP                                   ?[O]
full positive Object X / RH                             ?[O]
publication novelty                                     ?[O]
```

---

# 1. Prime-Atome: die Schwelle ist exakt die Diagonale

Fuer

```math
K_t=T_{t/2}-T_{-t/2}
```

gilt

```math
\boxed{
K_t^*K_t=2I-T_t-T_{-t}.
}
```

Ein Prime-Power-Atom mit Gewicht `w_n` traegt daher

```math
w_nK_{\log n}^*K_{\log n}
=
2w_nI-w_n(T_{\log n}+T_{-\log n}).
```

Die zugehoerige COMMON-JUMP-Schwelle enthaelt exakt

```math
\boxed{2w_nI.}
```

Nach Zentrierung bleibt nur der off-diagonale/Translationsanteil

```math
-w_n(T_{\log n}+T_{-\log n}).
```

Summiert ueber die aktive endliche Prime-Power-Menge:

```math
\boxed{
A_a^{\rm prime}
=2\sum_{n\in\mathcal P_a}w_n
}
```

ist daher exakt die endliche Diagonalmasse des positiven Prime-Jump-Operators.

Dies erklaert zugleich die bereits bewiesene Cutoff-Gauge-Kovarianz: jedes neu eintretende, fuer den kleineren Traeger exterior liegende Prime-Atom fuegt `2w_n I` sowohl der positiven Gramform als auch der Schwelle hinzu.

---

# 2. Archimedes: positive Resolventenleiter

Die archimedische positive Dichte lautet

```math
h(t)=\frac{e^{-t/2}}{1-e^{-2t}}
=\sum_{m=0}^\infty e^{-\mu_m t},
\qquad
\mu_m=2m+\frac12.
```

Damit ist der positive archimedische COMMON-JUMP-Operator

```math
\boxed{
\Phi_\infty(D)
=
\sum_{m=0}^\infty A_m(D),
}
```

mit

```math
\boxed{
A_m(D)
:=
\frac{2}{\mu_m}
D^2(D^2+\mu_m^2)^{-1}
\succeq0.
}
```

Auf der reellen Fourierachse ist

```math
A_m(z)
=\frac{2}{\mu_m}\frac{z^2}{z^2+\mu_m^2}.
```

Jeder einzelne Modus besitzt daher die endliche Hochfrequenz-/Diagonalmasse

```math
\boxed{
\lim_{|z|\to\infty}A_m(z)
=\frac{2}{\mu_m}.
}
```

Die Summe dieser Diagonalmassen divergiert logarithmisch. Der volle Operator bleibt fuer jedes feste `z` wohldefiniert, weil die Resolventenfaktoren die hohen Moden daempfen. Die Schwelle `kappa_*` ist genau die kanonische finite-part dieser divergenten Diagonalsumme.

---

# 3. Exakte finite-part-Identitaet

Da

```math
\mu_m=2\left(m+\frac14\right),
```

gilt

```math
\frac{2}{\mu_m}
=\frac{1}{m+1/4}.
```

Die Digamma-Teleskopformel liefert fuer jedes `N>=0`

```math
\boxed{
\sum_{m=0}^N\frac{2}{\mu_m}
=
\psi\left(N+\frac54\right)-\psi\left(\frac14\right).
}
```

Mit der Standardasymptotik

```math
\psi(x)=\log x+O(x^{-1})
\qquad(x\to+\infty)
```

folgt

```math
\lim_{N\to\infty}
\left[
\sum_{m=0}^N\frac{2}{\mu_m}-\log(N+1)
\right]
=-\psi(1/4).
```

Da aus NULLPOL-COMMON

```math
\kappa_*=\log\pi-\psi(1/4)
```

bekannt ist, erhalten wir exakt

```math
\boxed{
\kappa_*
=
\log\pi+
\lim_{N\to\infty}
\left[
\sum_{m=0}^N\frac{2}{\mu_m}-\log(N+1)
\right].
}
```

Aequivalent und kompakter:

```math
\boxed{
\kappa_*
=
\lim_{N\to\infty}
\left[
\sum_{m=0}^N\frac{2}{\mu_m}
-
\log\frac{N+1}{\pi}
\right].
}
```

Dies ist keine numerische Beobachtung, sondern eine exakte Digamma-Identitaet.

---

# 4. UV-Normalisierung der zentrierten Gamma-Schicht

Die volle archimedische positive Symbolfunktion ist

```math
\Phi_\infty(z)
=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)
-\psi(1/4).
```

Nach Abzug der finite-part-Diagonalmasse:

```math
\Phi_\infty(z)-\kappa_*
=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)
-\log\pi.
```

Aus der Digamma-Asymptotik folgt fuer reelles `|z|->infty`

```math
\boxed{
\Phi_\infty(z)-\kappa_*
=
\log\frac{|z|}{2\pi}+O(|z|^{-2}).
}
```

Die Schwelle ist somit genau die Konstante, welche die positive Resolventenleiter auf die natuerliche archimedische Hochfrequenzskala `2pi` renormiert.

Dies erklaert auch, warum die fruehere Zerlegung

```math
\kappa_*=\log(4\pi)+\gamma+\log2+\frac\pi2
```

strukturell irrefuehrend sein kann: sie zerlegt eine intrinsische finite-part-Konstante in zwei rechnerische Stuecke. In der Resolventenbasis ist `kappa_*` ein einziges kanonisches Renormierungsdatum derselben positiven Gamma-Schicht.

---

# 5. Vollstaendige COMMON-JUMP-Diagonalmasse

Fuer festes Fenster `a` ist die Prime-Power-Menge endlich. Deshalb ist keine Prime-Renormierung notwendig. Kombiniert mit §3:

```math
\boxed{
\Gamma_a
=
2\sum_{n\in\mathcal P_a}w_n
+
\operatorname{FP}_{\pi}
\sum_{m\ge0}\frac{2}{\mu_m},
}
```

wobei `FP_pi` hier exakt die in §3 definierte finite part

```math
\operatorname{FP}_{\pi}
\sum_{m\ge0}\frac{2}{\mu_m}
:=
\lim_{N\to\infty}
\left[
\sum_{m=0}^N\frac{2}{\mu_m}
-
\log\frac{N+1}{\pi}
\right]
```

bedeutet.

Damit ist `Gamma_a` kanonisch aus den **Diagonalmassen der positiven COMMON-JUMP-Moden** rekonstruiert.

---

# 6. Reinterpretation der zentrierten Weilform

Auf NULLPOL gilt exakt

```math
Q_W(v)
=\langle v,(X_a^*X_a-\Gamma_aI)v\rangle.
```

Nach diesem Audit kann dies gelesen werden als

> positive COMMON-JUMP-Energie minus ihre endliche/renormalisierte Diagonalmasse.

Auf der Prime-Seite ist die Zentrierung algebraisch

```math
2w_nI-w_n(T_t+T_{-t})-2w_nI
=
-w_n(T_t+T_{-t}).
```

Auf der Gamma-Seite ist sie die finite-part-Zentrierung

```math
\Phi_\infty(D)-\kappa_*I.
```

Damit ist die verbleibende NP-GAP-Frage praeziser:

```text
Warum ist die renormalisierte off-diagonale/common-jump Paarung
auf der critical-half Range-Klasse nichtnegativ?
```

Der Skalar selbst benoetigt keinen unabhaengigen Generator mehr.

---

# 7. Object-X-Bedeutung

Dieser Befund schliesst eine der zuletzt verbliebenen konzeptionellen Luecken:

```text
Prime channels      -> positive modes + exact finite diagonal masses
Gamma channels      -> positive modes + exact finite-part diagonal mass
Threshold Gamma_a   -> Summe genau dieser beiden Diagonalbuchungen
```

Gemeinsam mit dem Critical-half Pole-Transfer-Audit ergibt sich nun:

```text
critical-half L_{1/2}
   |
   +-- boundary charges / pole transfer E_±
   +-- logarithmic Prime OU/AR(1) geometry
   +-- Gamma resolvent ground mode and ladder
   +-- COMMON-JUMP diagonal finite-part threshold
```

Damit sind Pole, Prime-Korrelation, archimedische positive Schicht und der zuvor isolierte Threshold alle auf dieselbe dokumentierte Operatorfamilie zurueckgefuehrt.

Was weiterhin fehlt, ist die **Positivitaet der zentrierten Form auf NULLPOL fuer alle Fenster**. Genau dies ist NP-GAP und global RH-aequivalent.

---

# 8. Firewalls

Nicht behaupten:

- finite-part-Zentrierung erhalte automatisch Positivitaet;
- eine renormalisierte Diagonalmasse sei bereits eine positive Gramnorm;
- NP-GAP oder RH seien bewiesen;
- das gesamte Object X sei fertig konstruiert;
- Publikationsneuheit sei geklaert.

Die neue Aussage ist die exakte strukturelle Herkunft des gesamten Skalars `Gamma_a`, nicht seine Positivitaetswirkung nach Subtraktion.
