# P11/R32 — unabhängiges Review-Paket: erweiterte zentrale Transversalität

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `4245be2393c0ffefd65d4e6e831276a1e4671207` — `audits/P11_R32_CENTRAL_TRANSVERSALITY_EXTENDED_AUDIT.md`
- `a123c1a92b74955ff9714ac5ac1ccc0de189e7da` — `consolidation/p11_r32_central_transversality_extended_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte den Verifier nur als Cross-check verwenden. Rekonstruieren Sie die Support-/Orbitargumente direkt aus dem Audit und P11s Hub/Full-Rest-Definitionen.

## A. Restschwelle E

Prüfen Sie, dass für
\[
E=c-2a=\tfrac12\log(5/4),\qquad E\le R<S<a,
\]
und `y in C_R^+` weiterhin exakt
\[
Ay=(\log2)2^{-3/2}K_{\log2}^{tr,*}M_{20}K_{\log2}^{tr}y
\]
gilt. Insbesondere prüfen:

- `(2,0), k=2,3` verschwinden bereits aus `R>=E` und `T0<c`;
- `(2,1)` verschwindet;
- `(3,0)` verschwindet;
- keine frühere Annahme `R>=a/2` wird heimlich benötigt.

```text
CTX-A REST THRESHOLD E: GREEN / PARTIAL / FAIL
```

## B. Primitive gap

Prüfen Sie exakt
\[
G=p^2-q^2(1+\lambda)^2>0,
\qquad \lambda=(\log2)2^{-3/2}.
\]
Der Audit gibt eine rationale Beweiskette über
\[
\log2<25/36,
\quad 2^{-3/2}<9/25,
\quad \lambda<1/4,
\quad 2^{-3/2}<3/8,
\]
und damit
\[
2^{-3/2}(1+\lambda)^2<75/128<1.
\]

```text
CTX-B PRIMITIVE GAP: GREEN / PARTIAL / FAIL
```

## C. b-freie Reflexionsorbits

Prüfen Sie für Annuluspunkte, bei denen `x+d>S` und `|x-d|<R`, die exakten zwei Punktgleichungen. Wenn `t=a-x` außerhalb des Annulus liegt, muss die 2-Zeilen-Elimination `y(t)=w(x)=0` liefern. Wenn `t` im Annulus liegt, prüfen Sie den 4x4-Block
\[
\begin{pmatrix}
C&0&-p&0\\
1&0&0&-q\\
0&C&0&-p\\
0&1&-q&0
\end{pmatrix}
\]
mit Determinante `q^2 C^2-p^2=-G`.

```text
CTX-C REFLECTION ORBITS: GREEN / PARTIAL / FAIL
```

## D. b-gekoppelter Restkeil

Im Fall `S>R+d` prüfen Sie die Partition
\[
L=(R,S-d),\quad H=(R+d,S),\quad M=(S-d,R+d).
\]
Prüfen Sie insbesondere:

- `L` und `H` sind disjunkt;
- `x -> x+d` ist eine Bijektion `L -> H`;
- für `x in L`, mit `X=x+d`, `t=a-x`, `h=e-x`, gilt `t in M subset (R,S)` und `0<h<R`;
- die sechs Punktgleichungen sind nach zulässigen Zeilenoperationen genau durch
\[
M_6=
\begin{pmatrix}
C&0&0&-p&0&-r\\
1&0&0&0&-q&-r\\
0&C&0&0&-p&0\\
0&1&0&-q&0&0\\
0&0&C_h&0&0&-p\\
0&0&D_h&r&0&0
\end{pmatrix}
\]
repräsentiert;
- exakt
\[
\det M_6=-p\big(C_h\lambda r^2+D_h[p^2-q^2(1+\lambda)^2]\big)<0.
\]

```text
CTX-D SIX-VARIABLE b-ORBIT: GREEN / PARTIAL / FAIL
```

## E. Mittelschale vollständig erschöpft?

Prüfen Sie adversarial den letzten Orbitschritt:

- für `z in M` sind beide b-Äste nicht im Annulus;
- `a-z` kann nicht in `H` liegen;
- falls `a-z in L`, ist `z` bereits Teil eines 6er-Orbits;
- falls `a-z in M`, greift der invertible 4x4-Reflexionsblock;
- falls `a-z` außerhalb des Annulus liegt, greift die 2-Zeilen-Elimination.

Damit darf kein offenes Restintervall im Annulus übrig bleiben.

```text
CTX-E ORBIT EXHAUSTION: GREEN / PARTIAL / FAIL
```

## F. Tiefer Zentralbereich und Gesamtsatz

Prüfen Sie `HE_A w=0` auf `0<t<a-S` und die positive primitive Koeffizientengleichung dort. Danach soll ganz `C_R^+` und ganz `w` verschwinden.

Gewünschte exakte Aussage:
\[
\ker K_{I,A}\cap(C_R^+\oplus H_A^-)=\{0\}
\]
für **alle**
\[
E\le R<S<a.
\]

```text
CTX-F EXTENDED CENTRAL TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

## G. Firewall

Nicht erlaubt:

- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- bounded below / closed range / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

```text
CTX SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
CTX-A REST THRESHOLD E:              GREEN / PARTIAL / FAIL
CTX-B PRIMITIVE GAP:                 GREEN / PARTIAL / FAIL
CTX-C REFLECTION ORBITS:             GREEN / PARTIAL / FAIL
CTX-D SIX-VARIABLE b-ORBIT:          GREEN / PARTIAL / FAIL
CTX-E ORBIT EXHAUSTION:              GREEN / PARTIAL / FAIL
CTX-F EXTENDED CENTRAL TRANSVERSALITY: GREEN / PARTIAL / FAIL
CTX SCOPE FIREWALL:                  GREEN / PARTIAL / FAIL
CTX OVERALL:                         GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **CTX-1:** `✓[M]_part` — zentraler Unsichtbarkeitssektor transversal für `E<=R<S<a`.

Keine Promotion ohne explizite Freigabe.