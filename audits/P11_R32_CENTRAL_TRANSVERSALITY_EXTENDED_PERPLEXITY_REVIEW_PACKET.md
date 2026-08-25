# P11/R32 — unabhängiges Review-Paket: horizon-adaptive zentrale Transversalität

**Status:** Review-Anforderung; keine Promotion.  
**Aktuelle Kandidaten:**
- `a2861928e172a8e85363c77af8d7fe5752b1ae28` — `audits/P11_R32_CENTRAL_TRANSVERSALITY_EXTENDED_AUDIT.md`
- `05ee0432ab3e37db0bfd1a8e023f0e73c3702fe3` — `consolidation/p11_r32_central_transversality_extended_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte den Verifier nur als Cross-check verwenden. Rekonstruieren Sie die Support-/Orbitargumente direkt aus dem Audit und P11s Hub/Full-Rest-Definitionen.

## A. Adaptive Restschwelle

Setze
\[
\varepsilon=T_0-2a,\qquad d=b-a.
\]
Prüfen Sie, dass für
\[
\boxed{R\ge\max\{\varepsilon,d/2\},\qquad R<S<a}
\]
und `y in C_R^+` exakt
\[
Ay=(\log2)2^{-3/2}K_{\log2}^{tr,*}M_{20}K_{\log2}^{tr}y
\]
gilt.

Insbesondere bitte direkt prüfen:

- `(2,0),k=2`: auf `Omega_(2,0)` ist der minimale Abstand `a-epsilon`, und `a-R<=a-epsilon` aus `R>=epsilon`;
- `(2,0),k=3`: noch weiter außen;
- `(2,1)`: verschwindet vollständig;
- `(3,0)`: minimaler Abstand `2d-epsilon`, und `2d>a` aus `9>8`;
- keine Annahme `R>=E` oder `R>=a/2` wird für den Restkollaps benötigt.

```text
CTX-A ADAPTIVE REST THRESHOLD: GREEN / PARTIAL / FAIL
```

## B. Primitive gap

Prüfen Sie exakt
\[
G=p^2-q^2(1+\lambda)^2>0,
\qquad \lambda=(\log2)2^{-3/2}.
\]
Der Audit verwendet
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
Bitte insbesondere die `atanh(z=1/3)`-Tailabschätzung für `log 2 < 25/36` rekonstruieren.

```text
CTX-B PRIMITIVE GAP: GREEN / PARTIAL / FAIL
```

## C. Geometrische Grundschwelle d/2

Prüfen Sie, dass `R>=d/2` tatsächlich alle benötigten reinen Annulusgeometrien liefert:

- `d<2R`;
- `e<2R` mit `e=a-d` und `d>e`;
- `S-R<2d`, sodass die Low-/High-d-Schalen nicht überlappen;
- im Fall `S<=R+d` gilt für jeden `x in (R,S)` sowohl `x+d>S` als auch `|x-d|<R`.

```text
CTX-C GEOMETRY THRESHOLD d/2: GREEN / PARTIAL / FAIL
```

## D. b-freie q-Reflexionsorbits

Prüfen Sie für b-freie Punkte die zwei Punktgleichungen. Falls `t=a-x` außerhalb des Annulus liegt, muss `y(t)=w(x)=0` folgen. Falls `t in (R,S)`, prüfen Sie den 4x4-Block
\[
\begin{pmatrix}
C&0&-p&0\\
1&0&0&-q\\
0&C&0&-p\\
0&1&-q&0
\end{pmatrix},
\qquad C=1+\lambda,
\]
mit
\[
\det=q^2C^2-p^2=-G\ne0.
\]
Da Annuluspunkte strikt größer als `R>=epsilon` sind, müssen ihre epsilon-Indikatoren null sein.

```text
CTX-D REFLECTION ORBITS: GREEN / PARTIAL / FAIL
```

## E. b-gekoppelter Keil S>R+d

Prüfen Sie die Partition
\[
L=(R,S-d),\quad H=(R+d,S),\quad M=(S-d,R+d).
\]
Für `x in L`, setze
\[
X=x+d,\quad t=a-x,\quad h=e-x.
\]
Bitte adversarial bestätigen:

- `x -> X` ist eine Bijektion `L -> H`;
- `t in M subset (R,S)`;
- `0<h<R`;
- `t` ist b-frei;
- am High-Punkt `X` bleibt genau der rückwärtige b-Ast `w(x)`;
- nur `h` darf einen epsilon-Indikator tragen.

Prüfen Sie anschließend die sechs Punktgleichungen und die nach Zeilenoperationen erhaltene Matrix
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
mit
\[
\boxed{
\det M_6=-p\Big(C_h\lambda r^2+D_h[p^2-q^2(1+\lambda)^2]\Big)<0.
}
\]

```text
CTX-E SIX-VARIABLE b-ORBIT: GREEN / PARTIAL / FAIL
```

## F. Mittelschalen-Orbit erschöpft?

Prüfen Sie den letzten Fall vollständig:

- für `z in M` sind beide b-Äste nicht im Annulus;
- `a-z` kann nicht in `H` liegen, weil `a-H subset (0,R)`;
- `a-z in L` bedeutet: bereits 6er-Orbit;
- `a-z in M`: invertibler 4x4-Reflexionsblock;
- `a-z` außerhalb des Annulus: zweizeilige Elimination.

Es darf kein positives Restmaß im Annulus unklassifiziert bleiben.

```text
CTX-F ORBIT EXHAUSTION: GREEN / PARTIAL / FAIL
```

## G. Tiefer Zentralbereich und Gesamtsatz

Prüfen Sie `HE_Aw=0` für `0<t<a-S` und die positive Koeffizientengleichung dort. Danach soll ganz `C_R^+` und ganz `w` verschwinden.

Gewünschte exakte Aussage:
\[
\boxed{
\ker\mathcal K_{I,A}\cap(\mathcal C_R^+\oplus\mathscr H_A^-)=\{0\}
}
\]
für
\[
\boxed{R\ge\max\{\varepsilon,d/2\},\qquad R<S<a.}
\]

Prüfen Sie zusätzlich das horizont-uniforme Korollar:
\[
E=c-2a>d/2,
\qquad \varepsilon<E
\]
und daher
\[
E\le R<S<a\Longrightarrow\text{CTX-1}.
\]

```text
CTX-G ADAPTIVE CENTRAL TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

## H. Firewall

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
CTX-A ADAPTIVE REST THRESHOLD:       GREEN / PARTIAL / FAIL
CTX-B PRIMITIVE GAP:                 GREEN / PARTIAL / FAIL
CTX-C GEOMETRY THRESHOLD d/2:        GREEN / PARTIAL / FAIL
CTX-D REFLECTION ORBITS:             GREEN / PARTIAL / FAIL
CTX-E SIX-VARIABLE b-ORBIT:          GREEN / PARTIAL / FAIL
CTX-F ORBIT EXHAUSTION:              GREEN / PARTIAL / FAIL
CTX-G ADAPTIVE CENTRAL TRANSVERSALITY: GREEN / PARTIAL / FAIL
CTX SCOPE FIREWALL:                  GREEN / PARTIAL / FAIL
CTX OVERALL:                         GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **CTX-1:** `✓[M]_part` — zentraler Unsichtbarkeitssektor transversal im horizon-adaptiven Bereich `R>=max{epsilon,d/2}`, `R<S<a`.

Keine Promotion ohne explizite Freigabe.