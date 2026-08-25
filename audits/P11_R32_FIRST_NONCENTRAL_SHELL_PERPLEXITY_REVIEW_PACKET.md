# P11/R32 — unabhängiges Review-Paket: reparierte erste nichtzentrale Schale

**Status:** Review-Anforderung; keine Promotion.  
**Aktuelle Kandidaten:**
- `6da9c76f659838c55a0570d430130c78ecf50c93` — `audits/P11_R32_FIRST_NONCENTRAL_SHELL_TRANSVERSALITY_AUDIT.md`
- `c6fe2e2e7420e15e4ecf3c3a57ac9a1783c28888` — `consolidation/p11_r32_first_noncentral_shell_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Eine frühere unreviewte Zwischenfassung hatte die adjungierten `(2,0)`-Cross-Terme übersehen. Die aktuelle Fassung führt den zentralen `K1^* M K2`-Echo ausdrücklich mit und repariert die Transversalität über eine `delta=d-e`-Rekursion. Bitte gerade diesen Punkt adversarial prüfen.

## A. Erste nichtzentrale Unsichtbarkeitsschale

Setze
\[
d=b-a,
\qquad \frac d2\le R<d,
\qquad h=d-R.
\]
Definiere `S_R^+` als geraden Schalenraum mit positivem Träger
\[
(a-h,a+h)=(e+R,b-R)
\]
und
\[
y(a-s)=y(a+s),\qquad |s|<h.
\]
Prüfen Sie direkt
\[
\boxed{\mathcal S_R^+\subset\ker(E_I^*H|_+)}.
\]

```text
NS-A FIRST SHELL INVISIBILITY: GREEN / PARTIAL / FAIL
```

## B. Full-Rest-Reduktion vor dem Rücktransport

Im `(2,0)`-Block
\[
\Phi_{20}=\alpha_1K_1+\alpha_2K_2+\alpha_3K_3
\]
soll auf `S_R^+` nach der `Omega20`-Maske gelten
\[
M_{20}K_1y=0,
\qquad M_{20}K_3y=0,
\qquad
M_{20}\Phi_{20}y=\alpha_2M_{20}K_2y.
\]

Prüfen Sie insbesondere:

- zentraler `K1 y`-Output hebt sich durch die Schalen-Symmetrie auf;
- äußere `K1`-Kopien und alle `K3`-Kopien liegen außerhalb der Maske;
- trotzdem bleiben beim Rücktransport in `Phi20*` **alle** Adjungierten `K1*,K2*,K3*` erhalten.

Der `(2,1)`-Block soll auf dieser Schale vollständig null sein; `(3,0)` trägt lokal auf der `a`-Schale, aber nicht zum zentralen Echo bei.

```text
NS-B FULL-REST PRE-ADJOINT REDUCTION: GREEN / PARTIAL / FAIL
```

## C. Zentraler Cross-Term-Echo

Für
\[
f(t)=y(a+t)=y(a-t),
\qquad 0<t<h,
\]
prüfen Sie direkt aus `K1*=-K1`:
\[
\boxed{
(Ay)(t)=\gamma_t f(t),
\quad
\gamma_t=(\log2)2^{-9/4}(1+1_{t<\varepsilon})>0.
}
\]

Bitte sicherstellen, dass kein weiterer Full-Rest-Term am selben zentralen Output sitzt und die Formel verändert.

```text
NS-C CENTRAL CROSS-TERM ECHO: GREEN / PARTIAL / FAIL
```

## D. Lokale Schalenwirkung

Am zugehörigen Punkt `a+t` soll gelten
\[
\boxed{
((I+A)y)(a+t)=C_t f(t),
\quad
C_t=1+q^2+2r^2 1_{t\ge\delta-\varepsilon}>0.
}
\]

Prüfen Sie:

- `q^2` kommt aus dem lokalen `(2,0),k=2`-Selbstterm;
- `(2,1)` bleibt null;
- der `(3,0)`-Selbstterm trägt genau unter der angegebenen Maskenbedingung.

```text
NS-D LOCAL SHELL ACTION: GREEN / PARTIAL / FAIL
```

## E. Sauberer Bereich

Für `x<=R+e`, `t=a-x`, soll `t>=h` gelten und damit
\[
y(t)=(Ay)(t)=0.
\]
Prüfen Sie die exakte Hubgleichung
\[
\boxed{
pw(x)+r1_{x+d<S}w(x+d)=0.}
\]

```text
NS-E CLEAN d-EQUATION: GREEN / PARTIAL / FAIL
```

## F. Echo-Bereich und Elimination

Für
\[
x>R+e,
\qquad t=a-x\in(0,h),
\]
gilt automatisch `x+d>S`. Prüfen Sie die beiden Gleichungen
\[
\gamma_t f(t)-p w(x)=0,
\]
\[
C_t f(t)-r w(x-e)-q w(x)=0.
\]

Elimination soll geben
\[
A_t w(x)-r w(x-e)=0,
\qquad
A_t=\frac{C_t p}{\gamma_t}-q.
\]
Prüfen Sie die strikte Positivität über
\[
C_t\ge1,
\quad \gamma_t\le2\gamma,
\quad
\frac{p}{2\gamma}=\sqrt{\frac2{\log2}}>\sqrt2,
\quad q<1.
\]

```text
NS-F ECHO ELIMINATION / A_t>0: GREEN / PARTIAL / FAIL
```

## G. Entstehung der P12-Skala delta

Setze
\[
z=x-e.
\]
Prüfen Sie:

- `z>R`;
- `z<d<R+e`, wobei `d<R+e` aus `R>=d/2>delta=d-e` folgt;
- daher liegt `z` im sauberen Bereich;
- die saubere Gleichung bei `z` koppelt an
  \[
  z+d=x+(d-e)=x+\delta.
  \]

Daraus soll folgen:

- falls `x+delta>=S`, dann `w(x)=0`;
- sonst
  \[
  B_t w(x)+r w(x+\delta)=0,
  \qquad B_t>0.
  \]

```text
NS-G DELTA RECURSION: GREEN / PARTIAL / FAIL
```

## H. Endliche delta-Streifen und Rückkehr zum sauberen Bereich

Prüfen Sie den endlichen Strip-Descent vom oberen Rand des Echo-Bereichs
\[
(R+e,S)
\]
in Schritten `delta>0` und bestätigen Sie, dass dadurch der gesamte Echo-Bereich stirbt.

Danach im sauberen Bereich:

- wenn `x+d>=S`, direkt `w(x)=0`;
- wenn `x+d<S`, dann `x+d>R+d>R+e`, also liegt `x+d` im bereits getöteten Echo-Bereich.

Damit soll
\[
\boxed{w=0\text{ auf dem ganzen Annulus}}
\]
folgen und anschließend aus `(I+A)y=0`, `A>=0`, auch `y=0`.

```text
NS-H FULL FIRST-SHELL TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

## I. Scope-Firewall

Gewünschte exakte Reichweite:
\[
\boxed{\frac d2\le R<d,\qquad R<S<a.}
\]

Nicht erlaubt:

- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Klassifikation aller weiteren Teile von `N_I`;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

```text
NS SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
NS-A FIRST SHELL INVISIBILITY:            GREEN / PARTIAL / FAIL
NS-B FULL-REST PRE-ADJOINT REDUCTION:     GREEN / PARTIAL / FAIL
NS-C CENTRAL CROSS-TERM ECHO:             GREEN / PARTIAL / FAIL
NS-D LOCAL SHELL ACTION:                  GREEN / PARTIAL / FAIL
NS-E CLEAN d-EQUATION:                    GREEN / PARTIAL / FAIL
NS-F ECHO ELIMINATION / A_t>0:            GREEN / PARTIAL / FAIL
NS-G DELTA RECURSION:                     GREEN / PARTIAL / FAIL
NS-H FULL FIRST-SHELL TRANSVERSALITY:     GREEN / PARTIAL / FAIL
NS SCOPE FIREWALL:                        GREEN / PARTIAL / FAIL
FIRST NONCENTRAL SHELL OVERALL:           GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **NS-1a:** `✓[M]` — unendlichdimensionale erste nichtzentrale Schale liegt in `N_I`;
- **NS-1:** `✓[M]_part` — diese gesamte Schale ist für jedes `R<S<a` transversal, sofern `d/2<=R<d`.

Keine Promotion ohne explizite Freigabe.
