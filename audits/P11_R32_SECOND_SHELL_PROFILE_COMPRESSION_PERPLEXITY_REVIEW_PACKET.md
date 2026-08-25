# P11/R32 — unabhängiges Review-Paket: zweite Schale, Profilkompression

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `audits/P11_R32_SECOND_SHELL_PROFILE_COMPRESSION_AUDIT.md`
- `consolidation/p11_r32_second_shell_profile_compression_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

SS-1a und SS-L sind unabhängig inhaltlich GREEN, aber formal unpromotet. Dieses Paket prüft den nächsten Kandidaten **SP-1**. Bitte den Verifier nur als Cross-check verwenden und die Support-/Formrechnung direkt rekonstruieren.

## A. Profilabbildung und Norm

Für
\[
\frac d2\le R<e,
\qquad \ell=e-R,
\qquad \rho=r/q,
\]
prüfen Sie die Parametrisierung
\[
(U_Rf)(b+u)=f(u),
\qquad
(U_Rf)(T-u)=\rho f(u),
\qquad0<u<\ell,
\]
mit gerader Fortsetzung und
\[
\|U_Rf\|^2=2(1+\rho^2)\|f\|^2.
\]

```text
SP-A PROFILE MAP: GREEN / PARTIAL / FAIL
```

## B. Disjunkte Pre-Adjoint-Kanäle

Prüfen Sie für die positive Hälfte die exakten Kanalintervalle:

- `K1`: `(d,d+ell)` mit Profil `-f(u)` und `(a-ell,a)` mit `-rho f(u)`;
- `K2`: `(0,ell)` mit `rho f(u)` und `(R,e)` mit `f(u)`;
- `M20 K3`: `(a,a+min(ell,epsilon))` mit `rho f(u)` sowie, nur falls `epsilon>R`, `(a+R,a+epsilon)` mit `f(u)`.

Prüfen Sie adversarial, dass diese Intervalle paarweise disjunkt sind. Kritische Identitäten:
\[
d+\ell=a-R,
\qquad a-\ell=d+R,
\qquad \ell<R.
\]
Damit sollen im `L^2(Omega20)`-Formwert alle Cross-Terme zwischen verschiedenen rechten `K_k`-Kanälen verschwinden, obwohl die ambient Operatorwörter `K_l^* M K_k` weiterhin real sein können.

```text
SP-B DISJOINT CHANNEL GEOMETRY: GREEN / PARTIAL / FAIL
```

## C. Exakte Restform

Setze
\[
J_\varepsilon(u)=\rho^2 1_{u<\varepsilon}+1_{u>e-\varepsilon}.
\]
Prüfen Sie aus den drei SE-2-Blöcken exakt
\[
\langle A U_Rf,U_Rg\rangle
=2\int_0^\ell[A_0+\kappa J_\varepsilon(u)]f\bar g\,du,
\]
mit
\[
A_0=(1+\rho^2)(p^2+q^2+2r^2),
\]
\[
\kappa=q^2(2+2^{-3/2}).
\]
Bitte die vier Beiträge einzeln rekonstruieren:

1. `(2,0)` `K1/K2`: `(1+rho^2)(p^2+q^2)`;
2. `(2,0)` `K3`: `q^2 2^(-3/2) J_epsilon`;
3. `(2,1)`: `2q^2 J_epsilon`;
4. `(3,0)`: `2r^2(1+rho^2)`.

```text
SP-C REST FORM COEFFICIENTS: GREEN / PARTIAL / FAIL
```

## D. Skalare Kompression

Für
\[
V_R=U_R/\sqrt{2(1+\rho^2)}
\]
soll exakt gelten
\[
\boxed{V_R^*AV_R=M_{\mu_R}}
\]
mit
\[
\mu_R(u)=p^2+q^2+2r^2
+\frac{q^2(2+2^{-3/2})}{1+\rho^2}
\left(\rho^2 1_{u<\varepsilon}+1_{u>e-\varepsilon}\right).
\]
Prüfen Sie besonders, dass dies eine **Kompression** ist und keine Invarianzbehauptung `A S subset S`.

```text
SP-D SCALAR COMPRESSION: GREEN / PARTIAL / FAIL
```

## E. Hubprofil

Prüfen Sie direkt für `g` im Profilraum, dass `H U_R g` auf der positiven Achse innerhalb des Horizonts exakt die drei Kanäle besitzt
\[
x=e-u:\quad h_0 g(u),
\]
\[
x=d+u:\quad -p g(u),
\]
\[
x=a-u:\quad -p\rho g(u),
\]
mit
\[
h_0=q-r\rho=(q^2-r^2)/q<0.
\]
Der zentrale Kanal bei `x=u` muss wegen `q rho=r` exakt verschwinden.

```text
SP-E HUB PROFILE: GREEN / PARTIAL / FAIL
```

## F. Komprimierte notwendige Blockgleichung

Setze
\[
C_R(u)=(1+\rho^2)+A_0+\kappa J_\varepsilon(u),
\qquad
s_0=(r^2-q^2)/q>0.
\]
Für ein augmentiertes Blockkernpaar `(U_R f,w)` soll durch Testen gegen alle `U_R g` notwendig folgen
\[
\boxed{
C_R(u)f(u)
+s_0 1_{e-u<S}w(e-u)
+p1_{d+u<S}w(d+u)
+p\rho1_{a-u<S}w(a-u)=0.
}
\]
Bitte Vorzeichen über `H^*=-H`, Parität und die positive-Halbachsenrechnung prüfen.

```text
SP-F PROJECTED BLOCK EQUATION: GREEN / PARTIAL / FAIL
```

## G. Firewall

Nicht erlaubt:

- `A S_{R,2}^+ subset S_{R,2}^+`;
- ambient 10 Wörter seien verschwunden;
- die komprimierte Gleichung sei äquivalent zum vollen Blocksystem;
- zweite Schale bereits transversal;
- voller Schur-Crossblock / voller augmentierter Kernel;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal, Objekt X oder RH.

```text
SP SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
SP-A PROFILE MAP:                    GREEN / PARTIAL / FAIL
SP-B DISJOINT CHANNEL GEOMETRY:      GREEN / PARTIAL / FAIL
SP-C REST FORM COEFFICIENTS:         GREEN / PARTIAL / FAIL
SP-D SCALAR COMPRESSION:             GREEN / PARTIAL / FAIL
SP-E HUB PROFILE:                    GREEN / PARTIAL / FAIL
SP-F PROJECTED BLOCK EQUATION:       GREEN / PARTIAL / FAIL
SP SCOPE FIREWALL:                   GREEN / PARTIAL / FAIL
SP-1 OVERALL:                        GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **SP-1:** `✓[M]_part` — exakte skalare Profilkompression der zweiten Schale plus notwendige komprimierte Blockgleichung.

Keine Promotion ohne explizite Freigabe.
