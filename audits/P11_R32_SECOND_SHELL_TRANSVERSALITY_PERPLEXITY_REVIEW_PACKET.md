# P11/R32 — unabhängiges Review-Paket: zweite Schale transversal

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `audits/P11_R32_SECOND_SHELL_TRANSVERSALITY_AUDIT.md`
- `consolidation/p11_r32_second_shell_transversality_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

SS-1a, SS-L und SP-1 sind inhaltlich unabhängig GREEN, formal aber unpromotet. Dieses Paket prüft den neuen Kandidaten **ST-1**. Bitte den Verifier nur als Cross-check verwenden und die lokalen Supportargumente Wort für Wort aus dem 11-Wort-Ledger rekonstruieren.

## A. Erster Beobachtungspunkt x1=e-u

Für
\[
0<u<\ell=e-R
\]
setze
\[
x_1=e-u.
\]
Prüfen Sie adversarial, dass unter allen elf Full-Rest-Wörtern exakt nur
\[
W_{11}=K_1^*M_{20}K_1
\]
und
\[
W_{13}=K_1^*M_{20}K_3
\]
bei `x1` beitragen und dass
\[
\boxed{
(AU_Rf)(e-u)
=\left[-p^2+q^2 1_{u>e-\varepsilon}\right]f(u).
}
\]
Bitte insbesondere Vorzeichen und Maskenbedingung des `W13`-Terms prüfen.

```text
ST-A X1 LOCAL 11-WORD LEDGER: GREEN / PARTIAL / FAIL
```

## B. Hub bei x1

Prüfen Sie für ungerades Annulus-`w` und `R<S<a` direkt
\[
\boxed{
(HE_Aw)(e-u)
=-p1_{d+u<S}w(d+u).
}
\]
Alle anderen `a,b,T`-Äste müssen entweder im inneren Loch oder außerhalb des Annulus liegen.

```text
ST-B X1 HUB ISOLATION: GREEN / PARTIAL / FAIL
```

## C. Zweiter Beobachtungspunkt x2=a-u

Prüfen Sie adversarial, dass unter allen elf Full-Rest-Wörtern exakt nur
\[
W_{12}=K_1^*M_{20}K_2
\]
und
\[
W_{23}=K_2^*M_{20}K_3
\]
bei
\[
x_2=a-u
\]
beitragen und
\[
\boxed{
(AU_Rf)(a-u)
=\gamma\rho\left(1+2^{-3/2}1_{u<\varepsilon}\right)f(u),
}
\]
mit
\[
\gamma=(\log2)2^{-9/4}>0.
\]
Bitte besonders ausschließen, dass `(2,1)` oder `(3,0)` an diesem Punkt einen versteckten Beitrag liefern.

```text
ST-C X2 LOCAL 11-WORD LEDGER: GREEN / PARTIAL / FAIL
```

## D. Hub bei x2

Prüfen Sie direkt
\[
\boxed{
(HE_Aw)(a-u)
=-r1_{d+u<S}w(d+u).
}
\]
Der `a`-Rückast liegt bei `-u` im inneren Loch; der `T`-Rückast liegt bei `-(a+u)` außerhalb des Annulus; alle Vorwärtsäste liegen rechts von `S<a`.

```text
ST-D X2 HUB ISOLATION: GREEN / PARTIAL / FAIL
```

## E. Vorzeichen-Elimination

Setze
\[
P_u=p^2-q^2 1_{u>e-\varepsilon}>0,
\]
\[
G_u=\gamma\rho(1+2^{-3/2}1_{u<\varepsilon})>0,
\]
und
\[
\chi=1_{d+u<S}.
\]
Die beiden ambient Gleichungen sollen exakt sein:
\[
-P_uf-p\chi W=0,
\]
\[
G_uf-r\chi W=0,
\qquad W=w(d+u).
\]
Prüfen Sie:

- für `chi=0`: sofort `f=0`;
- für `chi=1`: die Matrix
  \[
  \begin{pmatrix}-P_u&-p\\G_u&-r\end{pmatrix}
  \]
  besitzt
  \[
  \det=P_ur+pG_u>0,
  \]
  also wiederum `f=W=0`.

```text
ST-E SIGN-LOCKED TWO-POINT ELIMINATION: GREEN / PARTIAL / FAIL
```

## F. Schluss w=0

Nach `f=0` ist `y=0` und die erste Blockgleichung reduziert sich auf
\[
HE_Aw=0.
\]
Prüfen Sie, dass unser kompletter Parametersektor
\[
\frac d2\le R<e,
\qquad R<S<a<T
\]
im bereits global bewiesenen P12-Stratum `S<T` liegt und dass die P11↔P12 Odd-Fold-Identifikation daher
\[
\ker(HE_A|_-)=\{0\}
\]
liefert.

```text
ST-F FINAL P12 HUB INJECTIVITY: GREEN / PARTIAL / FAIL
```

## G. Exakter Satz und Firewall

Gewünschte Aussage:
\[
\boxed{
\ker\mathcal K_{I,A}\cap(\mathcal S_{R,2}^+\oplus\mathscr H_A^-)=\{0\}
}
\]
für
\[
\boxed{d/2\le R<e,\qquad R<S<a.}
\]

Nicht erlaubt:

- gesamtes `N_I` klassifiziert;
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal, Objekt X oder RH.

```text
ST SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
ST-A X1 LOCAL 11-WORD LEDGER:          GREEN / PARTIAL / FAIL
ST-B X1 HUB ISOLATION:                 GREEN / PARTIAL / FAIL
ST-C X2 LOCAL 11-WORD LEDGER:          GREEN / PARTIAL / FAIL
ST-D X2 HUB ISOLATION:                 GREEN / PARTIAL / FAIL
ST-E SIGN-LOCKED TWO-POINT ELIMINATION: GREEN / PARTIAL / FAIL
ST-F FINAL P12 HUB INJECTIVITY:         GREEN / PARTIAL / FAIL
ST SCOPE FIREWALL:                     GREEN / PARTIAL / FAIL
ST-1 OVERALL:                          GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **ST-1:** `✓[M]_part` — zweite explizite nichtzentrale Schale ist im gesamten Sektor `d/2<=R<e`, `R<S<a` transversal.

Keine Promotion ohne explizite Freigabe.
