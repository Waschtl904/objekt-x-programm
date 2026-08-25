# P11/R32 — unabhängiges Review-Paket: zentrale Schur-Transversalität

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `237324b76ff64cf7cfbdd1a71439881304b2992a` — `audits/P11_R32_CENTRAL_TRANSVERSALITY_AUDIT.md`
- `cb647a65b6fcdf62a12069b1e5ff23511bd2cfa1` — `consolidation/p11_r32_central_transversality_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte den retained verifier nur als Cross-check verwenden und die Supportargumente direkt rekonstruieren.

## A. Restkollaps auf C_R^+

Im Fenster
\[
2a<T_0<c=\tfrac12\log5
\]
und für
\[
a/2\le R<S<a,
\qquad d_R=a-R\le a/2,
\]
prüfen Sie für den Zentralraum
\[
\mathcal C_R^+=\{y\text{ gerade}:\operatorname{supp}y\subset[-d_R,d_R]\}
\]
gegen die exakte Full-Rest-Zerlegung:

1. im `(2,0)`-Block verschwinden `k=2,3` nach der Omega-Maske;
2. der gesamte `(2,1)`-Block verschwindet;
3. der gesamte `(3,0)`-Block verschwindet;
4. übrig bleibt exakt
\[
A y=(\log2)2^{-3/2}K_{\log2}^{tr,*}M_{\Omega_{2,0}}K_{\log2}^{tr}y.
\]

Die kritischen exakten Ungleichungen sind
\[
5a>2c\iff 32>25,
\qquad
2b-c>a/2\iff81>50.
\]

```text
CT-1a CENTRAL REST COLLAPSE: GREEN / PARTIAL / FAIL
```

## B. Primitive Wirkungsformeln

Mit
\[
\lambda=(\log2)2^{-3/2},
\quad\varepsilon=T_0-T,
\]
prüfen Sie direkt aus `K*= -K` und der Omega-Maske für fast jedes `0<t<a-R`:
\[
(Ay)(t)=\lambda(1+1_{t<\varepsilon})y(t).
\]

Für `x in (R,S)`, `t=a-x` prüfen:
\[
(Ay)(a+x)=-\lambda y(t).
\]

```text
CT-1b PRIMITIVE ACTION FORMULAS: GREEN / PARTIAL / FAIL
```

## C. Hub-Branch-Isolation

Unter `a/2<=R<S<a`, bitte alle sechs Branchargumente adversarial prüfen und bestätigen:
\[
(HE_Aw)(a-x)=-p w(x),
\qquad
(HE_Aw)(a+x)=+p w(x).
\]

Verwendete arithmetische Fakten:
\[
b-a>a/2\iff9>8,
\qquad b-a<a\iff3<4,
\qquad a-R\le R.
\]

Prüfen Sie zusätzlich:
\[
(HE_Aw)(t)=0\quad(0<t<a-S).
\]

```text
CT-1c HUB BRANCH ISOLATION: GREEN / PARTIAL / FAIL
```

## D. Zwei-Punkt-Elimination

Für `x in (R,S)`, `t=a-x`, sollen die beiden ersten Blockgleichungen werden:
\[
[1+\lambda(1+1_{t<\varepsilon})]y(t)-p w(x)=0,
\]
\[
-\lambda y(t)+p w(x)=0.
\]

Elimination gibt
\[
[1+\lambda1_{t<\varepsilon}]y(t)=0.
\]
Da der Koeffizient strikt positiv ist, folgen `y(t)=w(x)=0`.
Zusammen mit dem tiefen Zentralbereich `0<t<a-S` soll dies ganz `C_R^+` töten.

```text
CT-1 TWO-POINT ELIMINATION: GREEN / PARTIAL / FAIL
```

## E. Scope

Prüfen Sie, dass daraus exakt nur folgt:
\[
\ker\mathcal K_{I,A}\cap(\mathcal C_R^+\oplus\mathscr H_A^-)=\{0\}
\]
bzw.
\[
\operatorname{Ran}(HE_A|_-)\cap(I+A)\mathcal C_R^+=\{0\}.
\]

Nicht erlaubt:
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- uniforme Winkel-/Coercivity-Aussage;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

```text
CT-1 SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
CT-1a CENTRAL REST COLLAPSE:      GREEN / PARTIAL / FAIL
CT-1b PRIMITIVE ACTION:           GREEN / PARTIAL / FAIL
CT-1c HUB BRANCH ISOLATION:       GREEN / PARTIAL / FAIL
CT-1 TWO-POINT ELIMINATION:       GREEN / PARTIAL / FAIL
CT-1 SCOPE FIREWALL:              GREEN / PARTIAL / FAIL
CENTRAL TRANSVERSALITY OVERALL:   GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN darf **CT-1** als `✓[M]_part` gebucht werden. Der volle Schur-/augmentierte Kernel bleibt `?[O]`.
