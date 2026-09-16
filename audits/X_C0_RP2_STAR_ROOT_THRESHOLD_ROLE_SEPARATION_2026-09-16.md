# X-C0 — RP2 star-root renormalization is not the C1 threshold

**Datum:** 16. September 2026  
**Basis:** X-C0 #137 / stacked audit #138; read-only inputs #133 (local RP2 star bulk), #135 (source-stopped RP2 Green filtration), #134 (total Weyl).  
**Registry:** unverändert.  
**Nonclaim:** kein No-Go gegen allgemeine Weyl/Feshbach-Boundary-Kolligationen; kein Object-X-/RH-Claim.

---

## 0. Kurzurteil

Der in PR #133 exakt erzwungene laufende Stern-Rootcounterterm

```math
A_N=(2-N)P,
\qquad NP+A_N=2P,
\qquad P=\sqrt{\Delta_{RP^2}+1/4},
```

ist **nicht** der fehlende X-C0-Threshold und darf nicht mit der COMMON-JUMP-Cutoff-Masse identifiziert werden.

Er hat eine andere mathematische Rolle:

```text
A_N / NP+A_N      = Dirichlet-to-Neumann / root-impedance renormalization;
Gamma_a           = zero-frequency Green/Weyl diagonal mass.
```

Die Trennung ist bereits auf drei Ebenen zwingend:

1. **cutoff dependence:** `NP+A_N=2P` ist unter Astaddition invariant, waehrend `Gamma_a` bei jeder neu aktiven Primzahlpotenz springt;
2. **source-stop dependence:** der gestoppte RP2/P11-Kern hat fuer jede Stopptiefe dieselbe Root-Root-Kovarianz `(2P)^-1`, waehrend `Gamma_a` mit der sichtbaren p-Power-Tiefe waechst;
3. **spectral order:** `A_N` ist von Ordnung `P` (`+1`), die archimedische zero-frequency Thresholdmasse liegt auf der Green-Seite `P^-2` (`-2`, nach transversaler Spur/Finite Part).

Daher ist die naive Klasse

```text
forced RP2 star root counterterm = X-C0 threshold
```

rigoros ausgeschlossen.

```math
\boxed{\text{direct star-root/threshold identification}\quad\times[M]}
```

Was offen bleibt, ist eine **Weyl/Feshbach boundary map**, die den positiven Bulk und seine erzwungene Rootgeometrie in die bereits bekannten zero-frequency Weyl-Werte ueberfuehrt, ohne die exakten X-C0 Jump-/Gamma-Ports zu veraendern.

---

# 1. Der #133-Sternbulk

PR #133 konstruiert fuer endlich viele Aeste den positiven lokalen Operator

```math
\mathcal H_N=-\partial_x^2+P^2
```

mit Rootbedingungen

```math
f_1(0)=\cdots=f_N(0)=f(0),
```

```math
\boxed{
\sum_{j=1}^Nf_j'(0)=(2-N)P f(0).
}
```

Sein Zero-energy-Greenkern ist exakt

```math
\boxed{
(\mathcal H_N^{-1})_{jk}(x,y)
=
\begin{cases}
(2P)^{-1}e^{-P|x-y|},&j=k,\\
(2P)^{-1}e^{-P(x+y)},&j\ne k.
\end{cases}
}
```

und die Kombination im Green-Nenner ist

```math
\boxed{NP+A_N=2P.}
```

Beim Hinzufuegen eines Astes gilt

```math
A_{N+1}-A_N=-P.
```

Das ist ein exakt positiver und coefficient-free Bulk-Renormierungsmechanismus.

---

# 2. Astaddition kann nicht die Prime-Power-Thresholdspruenge sein

Auf X-C0/COMMON-JUMP gilt auf einem Fenster `a`

```math
\boxed{
\Gamma_a
=\kappa_*
+2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}.
}
```

Fuer einen festen Primast `p`, mit

```math
q=p^{-1/2},
\qquad
K_p(a)=\left\lfloor\frac{2a}{\log p}\right\rfloor,
```

ist dessen sichtbare Thresholdmasse

```math
\boxed{
\Gamma_{p,a}
=2(\log p)\sum_{k=1}^{K_p(a)}q^k
=2(\log p)\frac{q(1-q^{K_p(a)})}{1-q}.
}
```

Beim Eintreten der `k`-ten p-Potenz springt sie um

```math
\boxed{
\Delta\Gamma_{p,k}
=2(\log p)p^{-k/2}.
}
```

Demgegenueber ist die renormierte Sternwurzel

```math
NP+A_N=2P
```

unter Astaddition exakt invariant und besitzt keine `p`- oder `k`-Abhaengigkeit.

Schon die Quantoren stimmen daher nicht:

```text
star root flow       : one universal -P correction per newly added branch;
X-C0 threshold       : a weighted sequence of jumps at every visible p^k.
```

Eine direkte Gleichsetzung ist unmoeglich.

---

# 3. Source stopping aendert den Rootblock ebenfalls nicht

PR #135 hebt die reale P11-Sourcefiltration in den gestoppten RP2-Greenkern

```math
\boxed{
\mathcal K_L(x,y)
=(2P)^{-1}
\exp\{-P[x+y-2\min(x,y,L)]\}.
}
```

Am Root `x=y=0` gilt fuer **jedes** `L>=0`

```math
\boxed{
\mathcal K_L(0,0)=(2P)^{-1}.
}
```

Damit ist auch die Root-Root-Kovarianz unter dem Freischalten weiterer Innovations-/p-Power-Schichten invariant.

Das ist kein Mangel, sondern genau die Funktion des gestoppten OU-Shortings: neue innere Innovationen werden positiv aufgeloest, waehrend die gemeinsame Rootkorrelation bestehen bleibt.

Aber gerade deshalb kann der Rootblock nicht die wachsende sichtbare Thresholdmasse `Gamma_(p,a)` kodieren.

---

# 4. Spectral-order mismatch

Auf dem RP2-Transversalraum

```math
P|_{E_m}=\mu_mI,
\qquad
\mu_m=2m+1/2,
\qquad
d_m=4m+1=2\mu_m.
```

Der Sterncounterterm ist linear in `P`:

```math
A_N=(2-N)P.
```

Er ist daher ein Dirichlet-to-Neumann-/Impedanzobjekt von spektraler Ordnung `+1`.

Die positive Gamma-Backbone lautet dagegen

```math
\Phi_\infty(z)
=\operatorname{Tr}
[P^{-2}-(P^2+z^2)^{-1}].
```

Die zero-frequency Diagonalmasse ist entsprechend der renormierte/Finite-Part-Wert der `P^-2`-Spur:

```math
\operatorname{Tr}(P^{-2})
=\sum_m\frac{d_m}{\mu_m^2}
=\sum_m\frac{2}{\mu_m},
```

welche logarithmisch renormiert genau die bereits bekannte archimedische Konstante liefert (mit der festgelegten `pi`-Normalisierung).

Somit stehen sich strukturell gegenueber:

```text
root DtN counterterm      P       (order +1),
zero-frequency Weyl mass  P^-2    (order -2 under transverse trace).
```

Ein direkter Identitaetsanspruch ist typfalsch.

Die Prime-Kreis-Weylseite zeigt dieselbe Trennung: die Prime-Thresholds sind zero-frequency Green/Weyl-Werte der Kreisdefekte und tragen die variablen Gewichte `2(log p)p^{-k/2}`; sie sind keine bloßen Astzaehlterme.

---

# 5. Was #133 trotzdem exakt erklaert

Der Sterncounterterm bleibt ein wichtiger positiver Mechanismus:

```math
\boxed{
J_N^*\mathcal H_{N+1}^{-1}J_N
=\mathcal H_N^{-1}.
}
```

Neue Aeste veraendern die alte Green-Geometrie nicht, weil

```text
new branch DtN load    +P
root running term      -P
-------------------------
old Green denominator  unchanged.
```

Das ist eine lokale **cutoff-covariance** auf Bulk-/Resolventenebene.

Es ist aber nur ein Analogon der COMMON-JUMP-Cutoff-Gauge, nicht dieselbe Thresholdidentitaet.

Damit wird die alte Formulierung geschaerft:

```text
#133 explains how the positive Green parent remains projectively consistent
under branch addition;
it does not explain the scalar zero-frequency subtraction in Q_W.
```

---

# 6. Konsequenz fuer den C1-Gate

Nach den bisherigen gestackten Audits gilt:

```text
already correct and KEEP:
  X-C0 Prime Jump/Euler ports,
  X-C0 Gamma port,
  pole/window ports,
  positive RP2 star bulk,
  forced running DtN root counterterm,
  internal gamma-field / point-mixer geometry.

closed:
  raw-memory equal-mass replacement,
  independent additive point-mixer energy,
  direct identification A_N or NP+A_N with Gamma_a.
```

Der noch offene Mechanismus muss zwischen den beiden Ebenen liegen:

```math
\boxed{
\text{positive local bulk / DtN data}
\quad\xrightarrow{\text{canonical Weyl/Feshbach boundary map}}\quad
\text{zero-frequency Green/Weyl threshold}.
}
```

Dabei darf kein freier Robin- oder Skalierungsparameter nach dem Prime-2-Witness angepasst werden.

---

# 7. Naechster scharfer Test

PR #134 konstruiert bereits den totalen scalar Weyl-Kanal

```math
\Omega_a(z)
=2\pi\Sigma_\infty(z)
+\sum_{p\le e^{2a}}(\log p)W_p(z\log p).
```

und die positive completed difference

```math
\widetilde{\mathcal E}_a(z)=\Omega_a(0)-\Omega_a(z).
```

Der naechste C1-Test soll deshalb **nicht** einen weiteren lokalen Bulk erfinden, sondern pruefen, ob die direkte Summe / gemeinsame Boundary-Kopplung der bereits vorhandenen RP2- und Prime-circle-defect operators eine kanonische Boundary triple besitzt mit

```math
M_a(z)=\Omega_a(z),
```

und ob deren Krein/Friedrichs completion den X-C0 positive backbone exakt liefert.

Dieser erste Teil sollte moeglich sein, weil scalar Weyl functions under parallel/common-boundary coupling addieren.

Die entscheidende Firewall bleibt danach:

```text
M_a(0)-M_a(z) reproduces the positive COMMON-JUMP backbone,
but the centered Weil residual is -M_a(z).
```

Eine Krein completion allein darf daher nicht als NP-GAP-Beweis interpretiert werden.

Der eigentliche offene C1-Schritt waere erst ein **groesserer positiver parent**, dessen relative Boundary-/Storage-Readout die zusaetzliche `-M_a(0)`-Buchung erklaert, ohne die schon korrekten Prime/Gamma-Ports zu veraendern.

---

# 8. Status

```text
#133 forced star-root running law                         ✓[M]
#135 stopped root covariance independent of depth        ✓[M]
X-C0 visible threshold increments depend on p,k          ✓[M]
direct star-root = X-C0 threshold                        ×[M]
spectral-order mismatch P versus P^-2                    ✓[M]
star bulk as projective positive Green parent             ✓[M]
canonical total-Weyl boundary triple                      ?[O]
positive centered C1 parent                               ?[O]
Object X / NP-GAP / RH                                    ?[O]
```

No Registry change.
