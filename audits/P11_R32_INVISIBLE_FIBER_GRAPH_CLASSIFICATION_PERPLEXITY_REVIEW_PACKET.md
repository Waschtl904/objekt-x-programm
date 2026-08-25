# P11/R32 — unabhängiges Review-Paket: Branch-/Gluing-Klassifikation von N_I

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md`
- `consolidation/p11_r32_invisible_fiber_graph_classification_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Dieses Paket soll bewusst **keine weitere Schale** prüfen. Es geht um die exhaustivere Normalform des gesamten inneren Unsichtbarkeitsraums
\[
\mathcal N_I=\ker(E_I^*H|_+)
\]
und um die Frage, ob die bisherige Shell-by-shell-Sicht überhaupt eine endliche Klassifikation erwarten lässt.

## A. Exakter gesampelter physischer Bereich

Prüfen Sie für `0<R<a`:
\[
\mathcal U_R
=\bigcup_{\tau\in\{a,b,T\}}(\tau-R,\tau+R)\cap(0,T_0).
\]
Zeigen Sie direkt, dass jede gerade `L2`-Funktion mit positivem Support im Komplement von `U_R` in `N_I` liegt.

Für `R>=d/2` prüfen Sie die exakte Vereinfachung
\[
\mathcal U_R=(a-R,T+\min\{R,\varepsilon\})
\]
und damit
\[
\mathcal Z_R^{phys}
=(0,a-R)\cup(T+\min\{R,\varepsilon\},T_0).
\]

```text
FG-A SAMPLING / BLIND COMPLEMENT: GREEN / PARTIAL / FAIL
```

## B. Horizontschwanz

Falls `R<epsilon`, prüfen Sie
\[
\mathcal T_R=(T+R,T_0)
\]
als nichtleeren automatisch unsichtbaren Supportbereich und damit einen unendlichdimensionalen geraden Unterraum von `N_I`.

```text
FG-B HORIZON TAIL: GREEN / PARTIAL / FAIL
```

## C. Sechs Branches und Horizon-Cuts

Prüfen Sie die sechs Pullbacks
\[
A_\pm(u)=y(a\pm u),
\quad
B_-(u)=y(b-u),
\quad
B_+(u)=1_{u<e+\varepsilon}y(b+u),
\]
\[
C_-(u)=y(T-u),
\quad
C_+(u)=1_{u<\varepsilon}y(T+u),
\]
und die exakte Hubrelation
\[
p(A_--A_+)+r(B_--B_+)+q(C_--C_+)=0.
\]
Prüfen Sie insbesondere `T0-b=e+epsilon` und `T0-T=epsilon`.

```text
FG-C BRANCH EQUATION: GREEN / PARTIAL / FAIL
```

## D. Gluing-Rekonstruktion

Für Branches `i=(tau,sigma)` mit
\[
\pi_i(u)=\tau+\sigma u
\]
prüfen Sie die Aussage:

- notwendige Kompatibilität: `pi_i(u)=pi_j(v)` impliziert `F_i(u)=F_j(v)`;
- hinreichend: eine messbare Branchfamilie, die alle solchen Gluing-Identitäten erfüllt, rekonstruiert a.e. eindeutig eine `L2`-Funktion auf `U_R`;
- zusammen mit einem beliebigen blinden Anteil ergibt sich damit exakt
  \[
  \mathcal N_I
  \cong
  \mathcal Z_R^+
  \oplus
  \{F\in\mathfrak G_R:\Lambda_R F=0\}.
  \]

Prüfen Sie, ob hier noch eine versteckte Kompatibilitätsbedingung fehlt (z.B. Mehrfachüberlappung, Horizon-Endpunkte, Parität). Endpunkte dürfen a.e. ignoriert werden.

```text
FG-D EXHAUSTIVE GLUING NORMAL FORM: GREEN / PARTIAL / FAIL
```

## E. Affine Overlap-Regeln

Prüfen Sie die drei zentralen Reflexionen
\[
s_d(u)=d-u,
\qquad
s_e(u)=e-u,
\qquad
s_a(u)=a-u
\]
und die Kompositionen
\[
s_d\circ s_e(u)=u+\delta,
\]
\[
s_a\circ s_d(u)=u+e,
\]
\[
s_a\circ s_e(u)=u+d.
\]
Wichtig: Diese Abbildungen gelten jeweils nur auf den tatsächlichen Overlap-Domains; die Algebra wird zunächst in der unbeschränkten affinen Gruppe betrachtet.

```text
FG-E OVERLAP AFFINE ALGEBRA: GREEN / PARTIAL / FAIL
```

## F. Irrationalität und No-Go-Reichweite

Prüfen Sie exakt
\[
d/e\notin\mathbb Q
\]
über:
\[
d/e=m/n
\Rightarrow
(3/2)^n=(4/3)^m
\Rightarrow
3^{n+m}=2^{n+2m},
\]
Widerspruch zur eindeutigen Primfaktorzerlegung.

Bewerten Sie anschließend die Reichweite korrekt:

**erlaubt:** Die unbeschränkte affine Overlap-Gruppe ist nicht endlich-periodisch bzw. nicht aus einer gemeinsamen diskreten Grundlänge erzeugt; aus „nur drei Hub-Shifts“ folgt daher nicht automatisch „endlich viele periodische Orbittypen“.

**nicht erlaubt:** daraus bereits zu schließen, dass für jedes feste `R` tatsächliche domain-beschränkte Orbits unendlich sind oder dass `N_I` zwingend unendlich viele irreduzible Schalentypen besitzt.

```text
FG-F IRRATIONALITY / NO-GO FIREWALL: GREEN / PARTIAL / FAIL
```

## G. Scope-Firewall

Nicht behauptet werden dürfen:

- `C_R`, erste Schale, zweite Schale und Horizontschwanz erzeugen schon ganz `N_I`;
- domain-beschränkter Overlap-Graph hat sicher unendlich viele Orbits;
- Horizontschwanz ist bereits Schur-transversal;
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Closed Range / bounded below / uniformer Winkel;
- Polar Gauge, Strong Terminal, Objekt X oder RH.

```text
FG SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
FG-A SAMPLING / BLIND COMPLEMENT:       GREEN / PARTIAL / FAIL
FG-B HORIZON TAIL:                     GREEN / PARTIAL / FAIL
FG-C BRANCH EQUATION:                  GREEN / PARTIAL / FAIL
FG-D EXHAUSTIVE GLUING NORMAL FORM:     GREEN / PARTIAL / FAIL
FG-E OVERLAP AFFINE ALGEBRA:            GREEN / PARTIAL / FAIL
FG-F IRRATIONALITY / NO-GO FIREWALL:    GREEN / PARTIAL / FAIL
FG SCOPE FIREWALL:                      GREEN / PARTIAL / FAIL
FG OVERALL:                             GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wären zulässig:

- **FG-0:** `✓[M]` — exakter automatisch blinder Supportraum;
- **HT-1:** `✓[M]` — Horizontschwanz bei `R<epsilon`;
- **FG-1:** `✓[M]` — exhaustive Branch-/Gluing-Normalform;
- **FG-NG1:** `✓[M]_neg` — No-Go nur gegen die Schlussregel `endlich viele Hub-Shifts => endliche periodische Overlap-Gruppe`.

Keine Promotion ohne explizite Freigabe.
