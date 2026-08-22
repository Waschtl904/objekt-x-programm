# WICKIE-CORE-BOTH-ERKUNDUNG — Runde 13

**Datum:** 2026-08-22  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main`, Runde-12-HEAD `2d49fcb`  
**Scope:** P12 b2d core-both only. P11 FROZEN. R14 firewall untouched.

## Status

- `✓[M]`: exakte `J:x↦d-x`-Paritätszerlegung des P1/P2-Subsystems auf core-both.
- `✓[M]_neg`: die spezifische Hoffnung "P1/P2 diagonalisiert ⇒ ein ±-Kanal wird skalar getötet" ist falsch; beide P2-Kanalgleichungen werden nach den gepaarten `T^-`-/`A^+`-Relationen zu algebraischen Identitäten.
- `?[O]`: core-both selbst bleibt offen.

Dies ist **kein** No-Go gegen die gesamte J-Symmetriestrategie. Es ist nur ein Rang-/Redundanzbefund für das hier untersuchte Subsystem.

## 1. Geometrie und Definitionen

Im genuine core-both gilt

\[
I_{\rm both}=\bigl(\max\{R,d-\sigma\},\min\{\sigma,d-R\}\bigr),
\qquad \sigma>d/2.
\]

Für `x∈I_both` setze

\[
y:=d-x,
\quad H_\pm:=H(x)\pm H(y),
\quad l_\pm:=l(x)\pm l(y),
\quad h_\pm:=h(x)\pm h(y).
\]

Weiter

\[
\Delta:=p^2-q^2,
\qquad A:=p^2-q^2-r^2.
\]

## 2. P2 bei x und y=d-x

P2 lautet

\[
H(t)-l(t)=\frac{2}{p^2}D(t),
\qquad
D(t)=A h(t)+qr\,[h(e-t)-h(e+t)].
\]

Auf core-both sind `x,y>R≥e/2` und `x,y<σ<ε_max<e`, daher

\[
0<e-x<R,
\qquad 0<e-y<R.
\]

Außerdem

\[
e-y=x-\delta,
\qquad e+y=a-x,
\]

und

\[
0<x-\delta<\varepsilon_{\max}-\delta<e/2\le R.
\]

Damit

\[
D(x)=A h(x)-qr h(e+x),
\]

\[
D(y)=A h(y)-qr h(a-x).
\]

## 3. Gepaarte T^- Gleichungen

Aus

\[
T^-(t):\quad p h(a-t)+r h(e-t)-q h(t)=0
\]

folgt bei `t=x,y`, da `h(e-x)=h(e-y)=0`,

\[
p h(a-x)=q h(x),
\qquad
p h(e+x)=q h(y).
\]

Also

\[
h(a-x)=\frac qp h(x),
\qquad
h(e+x)=\frac qp h(y).
\]

Substitution ergibt

\[
D(x)=A h(x)-\frac{q^2r}{p}h(y),
\qquad
D(y)=A h(y)-\frac{q^2r}{p}h(x).
\]

Daher exakt

\[
\boxed{D_+=\frac{(p+r)(p^2-pr-q^2)}{p}\,h_+},
\]

\[
\boxed{D_-=\frac{(p-r)(p^2+pr-q^2)}{p}\,h_-}.
\]

Es gibt keine `+/-`-Mischung.

## 4. Gepaarte A^+ Gleichungen

Die raw Gleichung

\[
A^+(t):\quad p h(t)-pH(t)-r h(d-t)-q h(a-t)=0
\]

liefert mit den T^- Relationen

\[
p^2H(x)=\Delta h(x)-pr h(y),
\]

\[
p^2H(y)=\Delta h(y)-pr h(x).
\]

Somit

\[
\boxed{H_+=\frac{p^2-pr-q^2}{p^2}h_+},
\qquad
\boxed{H_-=\frac{p^2+pr-q^2}{p^2}h_-}.
\]

## 5. P1 diagonalisiert

Mit

\[
c_0:=\frac{2r}{p}
\]

gibt P1 bei `x,y`

\[
\boxed{(1+c_0)H_+=-l_+},
\qquad
\boxed{(1-c_0)H_-=-l_-}.
\]

Daraus

\[
\boxed{l_+=-\frac{(p+2r)(p^2-pr-q^2)}{p^3}h_+},
\]

\[
\boxed{l_-=-\frac{(p-2r)(p^2+pr-q^2)}{p^3}h_-}.
\]

Für die tatsächlichen P12-Koeffizienten gilt `c0=2r/p>1`, also insbesondere `p-2r≠0`.

## 6. Exakte λ±-Relationen

SymPy vereinfacht exakt zu

\[
\boxed{D_+=\lambda_+l_+,
\qquad
\lambda_+=-p^2\frac{p+r}{p+2r}},
\]

\[
\boxed{D_-=\lambda_-l_-,
\qquad
\lambda_-=-p^2\frac{p-r}{p-2r}}.
\]

Die Substitutionstests ergeben identisch

```text
D_+ - lambda_+ l_+ = 0
D_- - lambda_- l_- = 0
```

## 7. Negativer Kernbefund

P2 in Paritätsform ist

\[
H_+-l_+=\frac{2}{p^2}D_+,
\qquad
H_--l_-=\frac{2}{p^2}D_-.
\]

Nach Einsetzen der obigen exakten Formeln liefert SymPy

```text
P2_+ residual = 0
P2_- residual = 0
```

und elementar

\[
(2+c_0)\frac{p^2-pr-q^2}{p^2}
-
\frac{2}{p^2}\frac{(p+r)(p^2-pr-q^2)}{p}=0,
\]

weil `2+c0=2(p+r)/p`; analog im Minuskanal mit `2-c0=2(p-r)/p`.

Damit entsteht **kein** unabhängiges

\[
A_+l_+=0
\quad\text{oder}\quad
A_-l_-=0.
\]

Dies ist der `✓[M]_neg`-Befund dieser Runde.

## 8. Stresstests

### 8.1 Formal q=r

Beide symbolischen Residuen bleiben identisch null. Der Befund hängt nicht an `q≠r`.

### 8.2 Formal c0→0, also r→0

\[
\lambda_\pm\to-p^2,
\qquad
D_\pm\to(p^2-q^2)h_\pm,
\]

und die Identität bleibt erhalten.

### 8.3 Formale Ausnahme c0=1, also p=2r

Dann verschwindet der P1-Koeffizient `1-c0` im Minuskanal und `lambda_-` hat den Nenner `p-2r=0`. Dies ist ein echter formaler Sonderfall. Er liegt nicht im tatsächlichen P12-Regime, da dort `c0>1`.

### 8.4 Echte P12-Werte: Stress A am J-Fixpunkt

Mit

\[
R=0.08,
\qquad \sigma=0.105,
\qquad x=d/2+10^{-4},
\qquad y=d/2-10^{-4}
\]

und den tatsächlichen Konstanten

\[
d\approx0.20273255405408225,
\qquad e\approx0.1438410362258904,
\qquad \delta\approx0.05889151782819185,
\]

ist

\[
I_{\rm both}=(d-\sigma,\sigma)
\approx(0.0977325540541,0.105).
\]

Dabei

\[
x\approx0.1014662770270,
\qquad y\approx0.1012662770270,
\]

also beide strikt im Inneren. Die vier support-kritischen Argumente sind

\[
e-x\approx0.0423747591988<R,
\]

\[
e-y\approx0.0425747591988<R,
\]

\[
x-\delta\approx0.0425747591988<R,
\]

\[
y-\delta\approx0.0423747591988<R.
\]

Ferner

\[
p\approx0.4950399336085,
\quad r\approx0.4598130419339,
\quad q\approx0.2943525056289,
\]

und

\[
c_0=2r/p\approx1.857680606016>1.
\]

Damit ist der bisher noch nicht unabhängig nachgerechnete numerische Stress A vollständig bestanden.

## 9. Versuchte Widerlegung

Bewusst getestet wurden:

1. versteckte `+/-`-Mischung in `D`: keine;
2. zweite unabhängige P2-Skalargleichung: existiert nicht;
3. Spezialisation `q=r`: Identität bleibt;
4. Grenzfall `r→0`: Identität bleibt;
5. Symmetrie-Fixpunkt `x=d/2`: Minusmodus verschwindet dort tautologisch, aber nahegelegene echte core-both-Punkte erfüllen dieselben Support-Kills;
6. Ausnahme `c0=1`: genuine formale Entartung, nicht im P12-Regime.

## 10. Unabhängige Zweitprüfung

Perplexity Deep Research berichtete unabhängig in frischem SymPy-Kernel:

- alle Faktorisierungen `beta_±` reproduziert;
- `lambda_±` reproduziert;
- beide `D_±-lambda_±l_±` exakt null;
- beide P2-Residuen exakt null;
- `q=r`, `r→0`, `c0=1` wie oben reproduziert;
- Scope des negativen Status bestätigt.

Der damals einzig noch offene Punkt, Stress A mit den tatsächlichen P12-Konstanten, wurde anschließend durch das reproduzierbare Skript `consolidation/round13_core_both_parity.py` explizit geprüft und bestanden.

## 11. Konsequenz

P1/P2 sind in den J-Paritätskanälen strukturell sauber, aber für einen Kill redundant. Der nächste kleine Hebel soll daher **eine zusätzliche horizon-legale gepaarte Source-Familie** sein, deren J-Summe oder J-Differenz eine von diesem Subsystem linear unabhängige Relation in `h_+` oder `h_-` erzeugt.

Keine große unstrukturierte Matrix, solange ein kleiner symmetrischer Zusatzhebel noch möglich ist.

R14 firewall unverändert. P11 unverändert.
