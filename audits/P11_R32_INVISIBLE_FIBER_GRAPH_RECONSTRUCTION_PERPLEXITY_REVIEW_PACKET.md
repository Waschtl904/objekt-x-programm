# P11/R32 — gezieltes unabhängiges Review: FG-A / FG-B / FG-D

**Status:** Review-Anforderung; keine Promotion.  
**Ziel:** ausschließlich die bislang im externen Review nicht vollständig geprüften Teile des Fiber-Graph-Pakets schließen: Sampling-/Blind-Zerlegung, Horizontschwanz und vor allem die exhaustive L2-Gluing-Rekonstruktion.

Zu prüfen:
- `audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md`
- `audits/P11_R32_INVISIBLE_FIBER_GRAPH_RECONSTRUCTION_ADDENDUM.md`
- `consolidation/p11_r32_invisible_fiber_graph_reconstruction_verify.py` nur als Arithmetik-Cross-check.

**P11 FROZEN; P12 unverändert; R14 unverändert.**

---

## A. Exakter Samplingbereich und blinder Summand

Für `0<R<a` rekonstruieren Sie direkt aus
\[
(E_I^*Hy)(u)
=p[y(a-u)-y(a+u)]
+r[y(b-u)-y(b+u)]
+q[y(T-u)-y(T+u)],
\qquad0<u<R,
\]
die Menge aller positiven physischen Punkte, die überhaupt abgefragt werden:
\[
\mathcal U_R
=\bigcup_{\tau\in\{a,b,T\}}(\tau-R,\tau+R)\cap(0,T_0).
\]
Prüfen Sie, dass eine gerade `L2`-Funktion mit positivem Support in
\[
\mathcal Z_R^{phys}=(0,T_0)\setminus\mathcal U_R
\]
wirklich automatisch in `N_I` liegt.

Für `R>=d/2` prüfen Sie vollständig die Konnektivität der drei Fenster und
\[
\mathcal U_R=(a-R,T+\min\{R,\varepsilon\})
\]
bis auf Endpunkte.

```text
FGR-A SAMPLING / BLIND DECOMPOSITION: GREEN / PARTIAL / FAIL
```

---

## B. Horizontschwanz

Unter `R>=d/2` und `R<epsilon` prüfen Sie
\[
\mathcal T_R=(T+R,T_0)
\]
als nichtleeren Bestandteil von `Z_R^{phys}` mit Länge `epsilon-R>0` und damit als unendlichdimensionalen geraden `L2`-Unterraum von `N_I`.

```text
FGR-B HORIZON TAIL: GREEN / PARTIAL / FAIL
```

---

## C. Exakte Branch-Domains

Prüfen Sie die sechs Parameterdomains des Addendums:
\[
D_{A_-}=D_{A_+}=D_{B_-}=D_{C_-}=(0,R),
\]
\[
D_{B_+}=(0,\min\{R,e+\varepsilon\}),
\qquad
D_{C_+}=(0,\min\{R,\varepsilon\}).
\]
Prüfen Sie insbesondere, dass diese Domains genau aus `T0-b=e+epsilon` und `T0-T=epsilon` folgen und dass
\[
\mathcal U_R=\bigcup_i\pi_i(D_i)
\]
a.e. gilt.

```text
FGR-C EXACT BRANCH DOMAINS: GREEN / PARTIAL / FAIL
```

---

## D. Gluing-Unterraum — keine versteckten Kompatibilitäten

Im Branch-Hilbertraum
\[
\mathscr B_R=\bigoplus_iL^2(D_i)
\]
sei `G_R` durch alle paarweisen a.e. Gluing-Gleichungen auf
\[
O_{ij}=\pi_i(D_i)\cap\pi_j(D_j)
\]
definiert.

Prüfen Sie:

1. Jede Gluing-Gleichung ist der Kern eines beschränkten Restriktions-/Kompositions-Differenzoperators.
2. Wegen endlich vieler Branchpaare ist `G_R` abgeschlossen.
3. Paarweises a.e. Gluing reicht auch bei Drei- oder Mehrfachüberlappungen; es fehlt keine zusätzliche Cocycle-Bedingung.
4. Horizon-Endpunkte sind reine Nullmengen und erzeugen keine zusätzliche Bedingung.

```text
FGR-D CLOSED GLUING SPACE: GREEN / PARTIAL / FAIL
```

---

## E. Pullback-Isomorphismus

Definiere
\[
(J_Rg)_i=g\circ\pi_i.
\]
Prüfen Sie exakt
\[
\|J_Rg\|_{\mathscr B_R}^2
=\int_{\mathcal U_R}m_R(t)|g(t)|^2dt,
\qquad1\le m_R(t)\le6,
\]
und damit
\[
\|g\|^2\le\|J_Rg\|^2\le6\|g\|^2.
\]

Prüfen Sie die Rückrekonstruktion `R_R` über eine messbare disjunkte Branchpartition
\[
P_1=\pi_1(D_1),
\qquad
P_k=\pi_k(D_k)\setminus\bigcup_{j<k}\pi_j(D_j),
\]
und zeigen Sie:
\[
R_RJ_R=I,
\qquad
J_RR_R=I\text{ auf }\mathfrak G_R
\]
a.e.

Wichtig: Dies ist ein beschränkter Isomorphismus, im Allgemeinen **keine Unitarität** bezüglich des ungegewichteten Direktproduktnorms.

```text
FGR-E L2 PULLBACK / RECONSTRUCTION ISOMORPHISM: GREEN / PARTIAL / FAIL
```

---

## F. Exakter Row-Operator und Exhaustivität

Mit Nullfortsetzungen `E_i:L2(D_i)->L2(0,R)` sei
\[
\Lambda_RF
=p(E_{A_-}F_{A_-}-E_{A_+}F_{A_+})
+r(E_{B_-}F_{B_-}-E_{B_+}F_{B_+})
+q(E_{C_-}F_{C_-}-E_{C_+}F_{C_+}).
\]
Prüfen Sie
\[
\Lambda_RJ_Rg=E_I^*H(g_{even})
\]
exakt.

Dann prüfen Sie die orthogonale physische Zerlegung jedes geraden `y` in
\[
y=y_{blind}+y_{samp}
\]
und die Äquivalenz
\[
y\in\mathcal N_I
\iff
\Lambda_RJ_R(y_{samp}|_{(0,T_0)})=0.
\]

Damit soll wirklich exhaustive folgen:
\[
\boxed{
\mathcal N_I
\cong
\mathcal Z_R^+
\oplus
\{F\in\mathfrak G_R:\Lambda_RF=0\}.
}
\]

Suchen Sie adversarial nach einer möglichen Lösung von `E_I^*Hy=0`, die von dieser Darstellung **nicht** erfasst wird. Falls keine existiert, begründen Sie warum.

```text
FGR-F EXHAUSTIVE NORMAL FORM: GREEN / PARTIAL / FAIL
```

---

## G. Begriffs-/Scope-Firewall

Bitte ausdrücklich bestätigen oder verwerfen:

- `G_R` ist **unendlichdimensional**; sechs Branches bedeuten keine endlichdimensionale Klassifikation.
- Die Normalform ist endlich **beschrieben**, nicht endlichdimensional.
- Die affine Struktur ist domain-beschränkt als Pseudogruppe zu behandeln.
- FG-1 beweist weder endlich viele Schalentypen noch deren Transversalität.
- Keine Konsequenz für vollen Schur-Crossblock, Strong Terminal, Objekt X oder RH.

```text
FGR-G TERMINOLOGY / SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

---

## Gesamtverdict

```text
FGR-A SAMPLING / BLIND DECOMPOSITION:        GREEN / PARTIAL / FAIL
FGR-B HORIZON TAIL:                          GREEN / PARTIAL / FAIL
FGR-C EXACT BRANCH DOMAINS:                  GREEN / PARTIAL / FAIL
FGR-D CLOSED GLUING SPACE:                   GREEN / PARTIAL / FAIL
FGR-E L2 PULLBACK / RECONSTRUCTION:          GREEN / PARTIAL / FAIL
FGR-F EXHAUSTIVE NORMAL FORM:                GREEN / PARTIAL / FAIL
FGR-G TERMINOLOGY / SCOPE FIREWALL:          GREEN / PARTIAL / FAIL
FG-0 OVERALL:                                GREEN / PARTIAL / FAIL
HT-1 OVERALL:                                GREEN / PARTIAL / FAIL
FG-1 OVERALL:                                GREEN / PARTIAL / FAIL
```

Nur bei vollständigem GREEN wären formal zulässig:

- `FG-0: ✓[M]`
- `HT-1: ✓[M]`
- `FG-1: ✓[M]`

Keine Promotion ohne explizite Freigabe.
