# X-C0 — Total-Weyl common-boundary glue and translation-invariant C1 no-go

**Datum:** 16. September 2026  
**Basis:** X-C0 #137 / stacked audit #138; read-only inputs #130, #132, #134.  
**Registry:** unverändert.  
**Nonclaim:** kein full-domain unbounded Boundary-Triple-Freeze, kein positiver C1-Readout, kein NP-GAP/Object-X/RH-Abschluss.

---

## 0. Kurzurteil

Die in PR #134 nur algebraisch addierte Gesamt-Weyl-Selbstenergie

```math
\Omega_a(z)
=2\pi\Sigma_\infty(z)
+\sum_{p\le e^{2a}}(\log p)W_p(z\log p)
```

besitzt eine **kanonische coefficient-free common-boundary assembly**: lokale Prime-circle- und RP2-Line-defect Boundary-Kanaele werden ueber einen gemeinsamen longitudinalen Randwert gekoppelt, mit bereits erzwungenen Gewichten

```math
\alpha_\infty=\sqrt{2\pi},
\qquad
\alpha_p=\sqrt{\log p}.
```

Auf der Weyl-/Response-Ebene ist die Gesamtantwort exakt `Omega_a`.

Dieser Glue schliesst jedoch C1 nicht. Jede positive Parent-Klasse, die

```text
- nur diesen gemeinsamen longitudinalen Rand benutzt,
- translationsinvariant in x ist,
- und nach Fouriertransformation frequenzweise positive Schur-Komplemente bildet,
```

kann den centered Readout

```math
-\Omega_a(D)
```

nicht als positiven Schur-Term liefern, weil `-Omega_a(z)` auf der reellen Frequenzachse das Vorzeichen wechselt.

Damit:

```text
weighted common-boundary assembly for the safe backbone          ✓[K/M]
full project-wide closed unbounded boundary triple                ?[O]
translation-invariant frequencywise positive C1 parent            ×[M]
source/window-conditioned nonlocal boundary parent                ?[O]
```

Strategische Konsequenz:

> Die P11-Source-/Window-Filtration muss **im positiven Parent vor der Feshbach-/Schur-Elimination** eingebaut werden. Eine erst nachtraegliche Kompression des fertigen translationsinvarianten Weyl-Multiplikators erklaert keine Positivitaet.

---

# 1. Abstract weighted common-boundary lemma

Sei `B` ein Hilbertraum (im Projekt `B=L^2(R_x)`). Fuer endlich viele lokale Kanaele `j=1,...,N` seien Boundary-Pairs mit Randdaten

```math
(\Gamma_0^{(j)},\Gamma_1^{(j)})
```

und Weyl-Operatoren

```math
M_j(z):\mathcal B\to\mathcal B
```

gegeben, d.h. auf der lokalen Defektloesung zum Randwert `phi_j`

```math
\Gamma_1^{(j)}=M_j(z)\Gamma_0^{(j)}.
```

Fixiere skalare Gewichte `alpha_j>0` und beschraenke die adjungierte direkte Summe auf den **weighted-continuity**-Rand:

```math
\boxed{
\Gamma_0^{(j)}=\alpha_j\phi
\qquad(j=1,...,N)
}
```

mit einem gemeinsamen `phi in B`.

Definiere den gesamten konjugierten Fluss

```math
\boxed{
\Gamma_1^{tot}
:=\sum_{j=1}^N\alpha_j\Gamma_1^{(j)}.
}
```

Dann reduziert sich die direkte-Summen-Green-Identitaet auf

```math
\sum_j
(\langle\Gamma_1^{(j)}f_j,\Gamma_0^{(j)}g_j\rangle
-\langle\Gamma_0^{(j)}f_j,\Gamma_1^{(j)}g_j\rangle)
```

```math
=
\langle\Gamma_1^{tot}f,\phi_g\rangle
-\langle\phi_f,\Gamma_1^{tot}g\rangle.
```

Auf der Defektloesung mit gemeinsamem Randwert `phi` folgt

```math
\Gamma_1^{tot}
=\sum_j\alpha_j^2M_j(z)\phi.
```

Somit ist der common-boundary Weyl-Operator

```math
\boxed{
M_{tot}(z)
=\sum_j\alpha_j^2M_j(z).
}
```

Dies ist eine elementare Green-Identitaetsrechnung; kein Positivitaetssatz ueber den centered Readout wird benutzt.

### Domain firewall

Die lokalen Projekt-Audits liefern die benoetigten line-defect Weyl responses und den gemeinsamen Boundary-Typ. Sie bauen noch nicht alle distributionalen line traces, RP2-Finite-Parts und longitudinalen Sobolev-Domaenen in **einem** geschlossenen ordinary boundary triple zusammen. Daher wird die konkrete globale Instanziierung hier konservativ als `✓[K/M]` und nicht als vollstaendiger neuer `✓[M]`-Operatorfreeze gebucht.

---

# 2. Anwendung auf RP2 + Prime circles

Die vorhandenen lokalen Kanaele sind:

### Archimedisch

PR #130:

```math
M_\infty(z)=\Sigma_\infty(z),
```

mit

```math
\kappa_*=2\pi\Sigma_\infty(0),
```

```math
\Phi_\infty(z)
=2\pi[\Sigma_\infty(0)-\Sigma_\infty(z)].
```

### Prime `p`

PR #132:

```math
M_p(z)=W_p(z\log p),
\qquad
W_p(\theta)=P_{p^{-1/2}}^{\mathbb D}(\theta)-1,
```

mit positiver completed p-Tower-Energie

```math
(\log p)[W_p(0)-W_p(z\log p)].
```

Waehle daher

```math
\boxed{
\alpha_\infty=\sqrt{2\pi},
\qquad
\alpha_p=\sqrt{\log p}.
}
```

Dann liefert das Lemma

```math
\begin{aligned}
M_{tot,a}(z)
&=\alpha_\infty^2\Sigma_\infty(z)
+\sum_{p\le e^{2a}}\alpha_p^2W_p(z\log p)\\
&=2\pi\Sigma_\infty(z)
+\sum_{p\le e^{2a}}(\log p)W_p(z\log p)\\
&=\boxed{\Omega_a(z)}.
\end{aligned}
```

Es bleibt **kein** Kalibrierkoeffizient uebrig.

Damit ist die additive Struktur aus #134 genau diejenige, die ein weighted common-boundary star glue erzeugen muss.

---

# 3. Der positive Backbone ist der zero-frequency drop

PR #134 beweist bereits

```math
\boxed{
\widetilde{\mathcal E}_a(D)
=\Omega_a(0)I-\Omega_a(D)
\succeq0.
}
```

In der common-boundary Sprache ist dies die Differenz zwischen zero-frequency Boundary response und aktueller Boundary response.

Die gleiche Rechnung lokal lautet

```math
M_j(0)-M_j(D)\succeq0
```

in den bereits konstruierten Prime-/Gamma-Backbones; nach weighted star assembly addieren sich diese positiven Drops exakt.

Daher erklaert der gemeinsame Boundary-Glue **den sicheren positiven COMMON-JUMP-Backbone**, ohne neue Arithmetik oder Fit.

Dieser PASS ist strukturell, aber noch nicht das centered Weil-Problem.

---

# 4. Centered Weil benoetigt den zero-boundary Parameter

Auf NULLPOL gilt nach #134

```math
\boxed{
Q_W(v)
=-\langle v,\Omega_a(D)v\rangle.
}
```

Waere ein translationsinvarianter common-boundary Schur-/Feshbach-Readout von der Form

```math
\Theta I-\Omega_a(D),
```

so zwingt exakte Gleichheit mit dem centered Readout

```math
\boxed{\Theta=0.}
```

Der sichere zero-frequency/Krein-artige Backbone entspricht dagegen der nichtzentrierten Wahl

```math
\Theta=\Omega_a(0).
```

Die beiden Rollen duerfen nicht verwechselt werden.

---

# 5. Translation-invariant positive C1 is impossible

Die frueheren Scattering-/Multiplier-Audits zeigen fuer den centered Multiplikator

```math
\tau_a(z)=-\Omega_a(z)
```

exakt:

```math
\tau_a(0)<0,
```

und

```math
\tau_a(z)
=\log\frac{|z|}{2\pi}+O_a(1)
\longrightarrow+\infty
\qquad(|z|\to\infty).
```

Also

```math
\boxed{-\Omega_a(z)\text{ wechselt fuer jedes }a>0\text{ das Vorzeichen}.}
```

Betrachte nun eine Parent-Klasse, die nach Fouriertransformation in `x` als direkte Integrale positiver Blockmatrizen

```math
\mathbb B(z)\succeq0
```

zerfaellt und deren C1-Readout der frequenzweise Schur-Komplementblock ist.

Jedes wohldefinierte Schur-Komplement eines positiven Blocks ist positiv semidefinit. Daher kann sein skalarer/Boundary-Wert fuer fast jedes `z` nicht das vorzeichenwechselnde

```math
-\Omega_a(z)
```

sein.

Somit ist die Klasse

```text
translation invariant in x
+
frequencywise positive parent
+
scalar common-boundary Schur elimination
+
centered C1 output
```

rigoros ausgeschlossen:

```math
\boxed{\text{TI scalar common-boundary C1}\quad\times[M].}
```

### Scope

Nicht ausgeschlossen sind positive Parents, bei denen **vor** der Elimination

```text
- die Source-/Window-Projektion,
- die stopped-OU-Filtration,
- overlap-cone incidence,
- Paley-Wiener/NULLPOL shorting,
- oder andere nichttranslationsinvariante Randgeometrie
```

Teil des Zustandsraums ist.

Gerade diese Mechanismen verhindern eine punktweise Frequenzzerlegung und koennen daher prinzipiell komprimierte Positivitaet erzeugen, obwohl der nackte Multiplikator vorzeichenwechselt.

---

# 6. Warum dies den C1-Gate wirklich verschaerft

Vor diesem Audit war noch offen, ob der fehlende positive Glue bereits durch eine geeignete gemeinsame scalar boundary condition der fertigen Prime-/Gamma-Bulks entstehen koennte.

Jetzt gilt:

```text
common-boundary weighted assembly            PASS for Omega_a / positive backbone
translation-invariant scalar boundary C1    FAIL for centered Weil
```

Der fehlende Mechanismus muss daher die **Source-Geometrie in den Parent hineinheben**.

Das passt exakt zu PR #135:

```math
\mathcal K_L(x,y)
=(2P)^{-1}e^{-P[x+y-2\min(x,y,L)]},
```

wo `L` die reale P11-Stopp-/Boundarytiefe ist und die positiven Innovationen vor der spaeteren Beobachtung bereits source-abhaengig selektiert werden.

---

# 7. Neuer minimaler Gate: source-conditioned common boundary

Der kleinste noch zulaessige Kandidat ist nun:

```text
1. Start with the local positive RP2/prime bulks.
2. Insert the actual P11 source/window stops inside the bulk feature spaces.
3. Only then impose the weighted common boundary coupling.
4. Keep the X-C0 Jump/Gamma/pole ports exact.
5. Form the boundary/Feshbach quotient only after the stopped source geometry
   has destroyed translation invariance.
6. Test the resulting finite-window block on the fixed Prime-2 quartet
   f,g,f+g,f-g before any global claim.
```

Ein blosses

```text
build Omega_a(D) first, then compress afterward
```

ist keine neue positive Konstruktion; es ist nur die bereits bekannte NP-GAP-Reformulierung.

Der Parent muss **vorwaerts** mit den Source-Stops definiert sein.

---

# 8. Status

```text
abstract weighted common-boundary sum lemma                 ✓[M]
application to project Weyl responses at algebraic level    ✓[K/M]
weights sqrt(2pi), sqrt(log p) fixed, no fitting            ✓[M]
positive backbone Omega_a(0)-Omega_a(D)                     ✓[M]
centered output requires Theta=0                            ✓[M]
TI scalar positive common-boundary C1                       ×[M]
source-conditioned common-boundary parent                   ?[O]
Object X / NP-GAP / RH                                      ?[O]
```

No Registry change.
