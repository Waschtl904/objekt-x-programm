# P11/R32 — unabhängiges Review-Paket: 11-Wort-Bilanz der ersten nichtzentralen Schale

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `audits/P11_R32_FIRST_NONCENTRAL_SHELL_11WORD_LEDGER_AUDIT.md`
- `consolidation/p11_r32_first_noncentral_shell_11word_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Dies ist ein enger Zusatzreview. Bitte nicht erneut die gesamte NS-1-Kette prüfen, sondern ausschließlich die von der letzten unabhängigen Prüfung markierte Restunsicherheit: vollständige Bilanz aller elf Full-Rest-Wörter auf `S_R^+`.

## A. Ausgangszerlegung

Prüfen Sie direkt aus P11 §3.4 / SE-2:

- `(2,0)` liefert 9 geordnete Wörter `W_lk=K_l^* M20 K_k`, `l,k in {1,2,3}`;
- `(2,1)` liefert 1 Wort;
- `(3,0)` liefert 1 Wort;
- insgesamt exakt 11.

```text
WL-A ELEVEN-WORD DECOMPOSITION: GREEN / PARTIAL / FAIL
```

## B. Rechte-Faktor-Elimination im (2,0)-Block

Für die erste nichtzentrale symmetrische Schale `S_R^+` mit `d/2<=R<d`, `h=d-R` prüfen:
\[
M_{20}K_1y=0,
\qquad M_{20}K_3y=0.
\]

Rekonstruieren Sie dabei:

- zentrale `K1`-Auslöschung durch `y(a-s)=y(a+s)`;
- äußere `K1`- und `K3`-Outputs beginnen bei `2a-h`;
- `2a-h>a+epsilon` folgt aus `a-h=e+R>epsilon`.

Daraus müssen exakt die sechs Wörter
\[
W_{11},W_{21},W_{31},W_{13},W_{23},W_{33}
\]
auf `S_R^+` verschwinden.

```text
WL-B SIX DEAD (2,0) WORDS: GREEN / PARTIAL / FAIL
```

## C. Die drei überlebenden (2,0)-Wörter

Mit `g=M20 K2 y` prüfen Sie, dass global exakt
\[
W_{12},\quad W_{22},\quad W_{32}
\]
übrig bleiben.

Prüfen Sie die Supportzentren nach Rücktransport:

- `W12`: `0` und `+-2a`;
- `W22`: `+-a` und `+-3a`;
- `W32`: `+-2a` und `+-4a`.

`+-3a` und `+-4a` dürfen durch den Horizont verschwinden, aber dies darf nicht benutzt werden, um die drei Wörter vorzeitig algebraisch zu löschen.

```text
WL-C THREE SURVIVING (2,0) WORDS: GREEN / PARTIAL / FAIL
```

## D. Die beiden übrigen Blöcke

Prüfen Sie:

1. `(2,1)` ist identisch null auf `S_R^+`, weil `K2 y` frühestens bei Radius `a-h=e+R` sitzt, während `M21` nur Radius `epsilon` hat und `e+R>epsilon`.
2. `(3,0)` überlebt und besitzt nach Hin-/Rücktransport nur Zentren
   \[
   +-a,\qquad +-(a+2d).
   \]
   Insbesondere kein Zentrum bei `0`.

Damit sollen global exakt `4 von 11` Wörtern aktiv sein.

```text
WL-D REMAINING BLOCKS / FOUR-OF-ELEVEN: GREEN / PARTIAL / FAIL
```

## E. Zentraler Output 0<t<h

Prüfen Sie adversarial, dass von den vier global aktiven Wörtern im Bereich
\[
0<t<h
\]
**nur `W12`** Support besitzen kann.

Verwenden Sie `R>=d/2`, also `h<=d/2`, daher `2h<=d<a`, und damit
\[
a-h>h,
\qquad 2a-h>a+h.
\]

Dann muss die zentrale Formel vollständig sein:
\[
(Ay)(t)
=(\log2)2^{-9/4}(1+1_{t<epsilon})f(t).
\]

Bitte ausdrücklich bestätigen, dass weder `W22`, `W32` noch `(3,0)` einen verdeckten zentralen Beitrag haben.

```text
WL-E CENTRAL FORMULA COMPLETE: GREEN / PARTIAL / FAIL
```

## F. Lokaler Schalenpunkt a+t

Für `0<t<h` prüfen Sie, dass an `a+t` exakt nur

- `W22` mit Koeffizient `q^2`,
- `(3,0)` mit Koeffizient `2r^2 1_{t>=delta-epsilon}`

beitragen.

Insbesondere müssen die `+-2a`-Outputs von `W12` und `W32` wegen
\[
2a-h>a+h
\]
außerhalb liegen, und der äußere `(3,0)`-Output beginnt bei `a+2d-h>a+h`.

Damit soll exakt gelten:
\[
((I+A)y)(a+t)
=\bigl(1+q^2+2r^2 1_{t>=delta-epsilon}\bigr)f(t).
\]

```text
WL-F LOCAL SHELL FORMULA COMPLETE: GREEN / PARTIAL / FAIL
```

## G. Sauberer Zentralbereich

Im NS-Beweis gilt für `x<=R+e`, `t=a-x`:
\[
t>=h,
\qquad t<a-R<=a-h.
\]
Prüfen Sie, dass in diesem gesamten Bereich kein aktives Full-Rest-Wort Support besitzt, also
\[
y(t)=(Ay)(t)=0.
\]

Damit ist die saubere `d`-Gleichung gegen alle elf Wörter abgesichert.

```text
WL-G CLEAN CENTRAL GAP COMPLETE: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
WL-A ELEVEN-WORD DECOMPOSITION:       GREEN / PARTIAL / FAIL
WL-B SIX DEAD (2,0) WORDS:            GREEN / PARTIAL / FAIL
WL-C THREE SURVIVING (2,0) WORDS:     GREEN / PARTIAL / FAIL
WL-D REMAINING BLOCKS / 4 OF 11:      GREEN / PARTIAL / FAIL
WL-E CENTRAL FORMULA COMPLETE:        GREEN / PARTIAL / FAIL
WL-F LOCAL SHELL FORMULA COMPLETE:    GREEN / PARTIAL / FAIL
WL-G CLEAN CENTRAL GAP COMPLETE:      GREEN / PARTIAL / FAIL
NS-1 11-WORD LEDGER OVERALL:          GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN ist genau die letzte von der vorherigen NS-Prüfung markierte Unsicherheit geschlossen. Dann wäre NS-1 inhaltlich vollständig unabhängig GREEN; eine formale Promotion bleibt dennoch von expliziter Freigabe abhängig.
