# Objekt X — Hard-Audit Survivor State

**Stand:** 16. September 2026  
**Rolle:** kanonische Einstiegsebene fuer den Forschungsstand dieses Astes.  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**PR:** #116  
**Registry:** unveraendert.  
**Nonclaim:** kein RH-Beweis, kein Object-X-Abschluss, kein Publikationsneuheitsclaim.

> Diese Datei ist Navigation, kein neuer Beweis. Bei Konflikten gilt der verlinkte Primaeraudit im dort ausgewiesenen Scope.

---

## 0. Ein-Satz-Stand

Nach destruktivem Gegencheck bleibt als einzige ernsthafte Object-X-Front:

```text
relative cancellation first, Critical-half output second
```

Prime- und Continuum-Zustaende muessen zuerst auf der sicheren Root-Skala `Lambda(n)/n` relativ gekoppelt werden; eine getrennte diagonale Anhebung auf die Weil-Skala `Lambda(n)/sqrt(n)` ist unbeschraenkt und ausgeschlossen. Ein erfolgreicher Kandidat muss die relative Ausloeschung intern vollziehen und erst den endlichen relativen Boundary-Output durch den Critical-half-Port fuehren.

---

# 1. Was nach dem Hard Audit steht

## S1 — NULLPOL = Critical-half Green-Range `✓[M]`

```math
C_c^\infty(-a,a)\cap\ker M(0)\cap\ker M(1)
=
(-\partial_x^2+1/4)C_c^\infty(-a,a).
```

Green-Kern:

```math
G_{1/2}(x,y)=e^{-|x-y|/2}.
```

Die zwei Mellinbedingungen loeschen exakt die beiden aeusseren Green-Schwanzladungen.

Primaerquelle: `audits/P11_CRITICAL_HALF_GREEN_TREE_BRIDGE_2026-09-13.md`.

## S2 — P11 Prime-Power-Ledger = sampled Critical-half OU/AR(1) `✓[M]`

Nach Weil-Diagonalnormalisierung:

```math
R_q(j,k)=q^{|j-k|},\qquad q=p^{-1/2}.
```

Hub + Innovationen ergeben den stationaeren AR(1)-Kern. Dies ist eine Aussage ueber den Kanalindex-Ledger, nicht automatisch ueber den vollen raeumlichen P11-Operator.

Primaerquelle: `audits/P11_CRITICAL_HALF_GREEN_TREE_BRIDGE_2026-09-13.md`.

## S3 — P11-Masken = stopped OU filtration `✓[M]`

Mit

```math
L_R(x)=2(R-|x|),\qquad
m_p(x)=\lfloor L_R(x)/\log p\rfloor
```

ist die lokale normalisierte Kovarianz

```math
R_q^{(m)}(j,k)=q^{j+k-2\min(j,k,m)}.
```

Jedes Tiefeninkrement ist positiv Rang eins.

Universeller Kernel:

```math
G_L(s,t)=\exp(-(s+t)/2+\min(s,t,L)).
```

P11 ist dessen logarithmische Gitterabtastung.

Primaerquellen: `audits/P11_SPATIAL_STOPPED_OU_FILTRATION_2026-09-15.md`, `audits/P11_UNIVERSAL_STOPPED_OU_PRECISION_2026-09-15.md`.

## S4 — Boundary-tail shorting `✓[M]`

Diskret:

```math
Y_m=\sqrt{1-q^2}\sum_{k\ge m}q^{k-m}X_k
```

und

```math
\sum_{r=1}^{m-1}\frac{\|Y_r-qY_{r+1}\|^2}{1-q^2}+\|Y_m\|^2
=
\sum_{r<m}\|X_r\|^2+\|Y_m\|^2.
```

Kontinuierlich gilt dieselbe Shorting-Identitaet fuer

```math
Y(u)=\int_u^\infty e^{-(t-u)/2}X(t)dt.
```

Innen wird die nackte Energie exakt rekonstruiert; der aeussere Tail wird auf einen normierten exponentiellen Boundary-Modus komprimiert, das orthogonale Restdefizit bleibt positiv.

Primaerquelle: `audits/P11_BOUNDARY_TAIL_SHORTING_AND_UNIVERSAL_SAMPLING_2026-09-15.md`.

## S5 — Universelles Jump-Feld `✓[M]`

```math
X_v(t)=e^{-t/4}K_tv,
```

und fuer `h=log p`:

```math
\sqrt{w_{p,k}}K_{kh}v
=\sqrt h\,X_v(kh).
```

Alle Primzahlen tasten dasselbe kontinuierliche Feld auf unterschiedlichen logarithmischen Gittern ab.

Primaerquelle: `audits/P11_BOUNDARY_TAIL_SHORTING_AND_UNIVERSAL_SAMPLING_2026-09-15.md`.

## S6 — Prime-Pole-Diskrepanz und Gamma-Grund-Cancellation `✓[M]`

```math
\Delta
=\sum_{n=p^k}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}-e^{t/2}dt.
```

Auf NULLPOL hebt sich der glatte Prime-Hauptterm gegen den Gamma-Grundmodus auf. Die grosse fensterabhaengige Diagonalmasse verschwindet aus der fensterfreien Darstellung.

Primaerquelle: `audits/P11_NULLPOL_PRIME_DISCREPANCY_CANCELLATION_2026-09-15.md`.

## S7 — Critical-half finite-part transfer `✓[M]`

```math
J_\Delta(L)
=e^{L/2}\left(L-\gamma-\sum_{\log n<L}\frac{\Lambda(n)}n\right),
```

```math
J_\Delta(0)=-\gamma,
\qquad
d\Delta=\frac12J_\Delta dL-dJ_\Delta.
```

Dadurch koppelt die Diskrepanz exakt an

```math
D_+=\partial_x+1/2.
```

Primaerquelle: `audits/P11_CRITICAL_HALF_FINITE_PART_TRANSFER_2026-09-15.md`.

## S8 — Kausale Volterra-Normalform `✓[M]` als Identitaet

Mit

```math
(V_Jv)(x)=\int_{-\infty}^xJ_\Delta(x-y)v(y)dy
```

und `D_-=D_+^*`:

```math
D_-V_J+V_J^*D_+=2\gamma I+\mathcal C_\Delta.
```

Die hoehere Gamma-Schicht ist eine positive stabile Filterbank. Auf NULLPOL:

```math
Q_W(v)
=
\sum_{m\ge1}\frac2{\mu_m}\|y_m'\|^2
-c_*\|v\|^2
-2\operatorname{Re}\langle D_+v,V_Jv\rangle.
```

Positivitaet bleibt offen.

Primaerquelle: `audits/P11_CAUSAL_VOLterra_PASSIVITY_NORMAL_FORM_2026-09-15.md`.

## S9 — Eulerfaktor = P11 AR(1)-Resolvent `✓[M]`

```math
T_q^*=\sqrt{1-q^2}(I-qS)^{-1}.
```

Am Root-Impuls ist die Transferfunktion `1/(1-qz)`. Mit

```math
q=p^{-1/2},\qquad z=e^{-s\log p}
```

wird dies exakt

```math
(1-p^{-(s+1/2)})^{-1}.
```

Der Eulerfaktor ist klassisch; projektintern ist relevant, dass exakt derselbe Resolvent im vorhandenen P11-Choleskyfaktor steckt.

Primaerquelle: `audits/P11_EULER_AR1_RESOLVENT_BRIDGE_2026-09-15.md`.

## S10 — Jede Euler-Zelle wird von Gamma-Grund dominiert `✓[M]`

Fuer

```math
A_h=\sum_{k\ge1}h e^{-kh/2}K_{kh}^*K_{kh}
```

und

```math
A_0=\int_0^\infty e^{-t/2}K_t^*K_tdt
=4D^2(D^2+1/4)^{-1}
```

gilt fuer jedes `h>0`:

```math
0\preceq A_h\preceq A_0.
```

Auf Transferniveau existiert daher ein kanonischer lokaler Schur-Faktor

```math
b_h=\Phi_h b_0,
\qquad \|\Phi_h\|_{H^\infty(\Re s>0)}\le1.
```

Lokale Prime-/Euler-Zellen sind somit passive Kontraktionen der Gamma-Grundzelle. Der globale Engpass liegt nicht mehr lokal pro Primzahl, sondern in der Skalenkopplung.

Primaerquelle: `audits/P11_EULER_CELL_DOMINATED_BY_GAMMA_GROUND_2026-09-16.md`.

## S11 — Root-Trace-Bilanz `✓[M]`

P11-Rootmasse bis Tiefe `L`:

```math
M_P(L)=\sum_{\log n<L}\frac{\Lambda(n)}n.
```

Riemann-R- und Gamma-Grund-Referenz:

```math
M_R(L)=L-1+e^{-L},
\qquad
M_{\Gamma,0}(L)=1-e^{-L},
```

also

```math
M_R(L)+M_{\Gamma,0}(L)=L.
```

Damit

```math
e^{-L/2}J_\Delta(L)
=M_R(L)+M_{\Gamma,0}(L)-M_P(L)-\gamma.
```

Der kritische Volterra-Kern ist damit direkt die relative gestoppte Root-Storage-Bilanz.

Primaerquelle: `audits/P11_CRITICAL_TRANSFER_AS_STOPPED_ROOT_TRACE_DEFECT_2026-09-16.md`.

## S12 — Monotone Root-Mass-Transportkopplung `✓[K/M]`

Ordne die Prime-Power-Tiefen `h_j=log n_j` und setze

```math
a_j=\Lambda(n_j)/n_j,
\quad
s_0=\gamma,
\quad
s_j=\gamma+\sum_{i\le j}a_i,
\quad
I_0=[0,\gamma),\ I_j=[s_{j-1},s_j).
```

Dann `|I_j|=a_j` und aus dem klassischen PNT-Fehler folgt

```math
\sup_{L\in I_j}|L-h_j|\to0,
\qquad
\sum_j a_j\sup_{L\in I_j}|L-h_j|<\infty.
```

Damit entsteht ein kanonischer positiver Massentransport vom diskreten Root-Raum in `L^2(dL)`, und fuer jedes feste `s` mit `Re s>=0` konvergiert der relative Zelltransfer absolut:

```math
\gamma-\int_0^\gamma e^{-sL}dL
+
\sum_j\left[a_je^{-sh_j}-\int_{I_j}e^{-sL}dL\right].
```

Primaerquellen: `audits/P11_ROOT_MASS_MONOTONE_TRANSPORT_2026-09-16.md`, `audits/P11_ROOT_TRANSPORT_SAFE_TRANSFER_AND_CRITICAL_LIFT_FIREWALL_2026-09-16.md`.

## S13 — Plain Critical-half lift of root storage is impossible `×[M]`

Der Schritt

```math
a_j=\Lambda(n_j)/n_j
\mapsto
e^{h_j/2}a_j=\Lambda(n_j)/\sqrt{n_j}
```

ist auf dem Root-Storage eine unbeschraenkte exponentielle Multiplikation. Fuer jedes nichtverschwindende kompakt getragene `v` gilt fuer grosse `t`

```math
\|K_tv\|^2=2\|v\|^2,
```

sodass die getrennte Critical-half-Verstaerkung des Prime- bzw. Continuum-Tails divergiert. Auch endlich viele Source-Ableitungen beheben dies nicht.

Folge:

```text
prime/continuum cancellation MUST occur before critical amplification.
```

Primaerquelle: `audits/P11_ROOT_TRANSPORT_SAFE_TRANSFER_AND_CRITICAL_LIFT_FIREWALL_2026-09-16.md`.

---

# 2. Was NICHT als Neuheit behauptet wird

Nicht neu beanspruchen:

- RH als Positive-Real/Herglotz-Kriterium fuer `xi'/xi`;
- Lagarias-Positivitaet;
- Zeta-bezogene Kontroll-/Transfer-Systeme allgemein;
- Eulerprodukt, Poisson-, OU-/AR(1)-, Green-, de-Branges-, Paley-Wiener-, Toeplitz-, Prolate-Theorie an sich;
- passive/KYP-Realisierungen an sich;
- klassische PNT-Fehlerabschaetzungen.

Der moegliche projektspezifische Wert kann nur in der konkreten konstruktiven Glueung der bereits vorhandenen P11-/stopped-OU-/Root-Transport-/Gamma-Komponenten liegen.

---

# 3. Aktueller harter Gate

```text
RELATIVE-COLLIGATION / CANCEL-FIRST
```

Gesucht ist eine coefficient-free positive bzw. konservative `2x2`-relative Kolligation auf den Transportzellen `I_j`, die

1. diskrete Prime-Power-Rootzustande und positive Continuum-Zellen koppelt;
2. deren divergent kritische Anteile intern ausloescht, solange sie noch auf der sicheren `Lambda(n)/n`-Skala liegen;
3. nur den endlichen relativen Boundary-State nach aussen gibt;
4. erst diesen Output durch den Critical-half-Port hebt;
5. die bereits fixierten lokalen Schur-Zellen `Phi_h` und Gamma-Filter benutzt;
6. keine Koeffizienten nach Sicht auf die Weilform oder Zeta-Nullen fitten darf;
7. zuerst den exakten `R=1` Prime-2 mixed witness reproduzieren muss.

PASS: erstmals ein substantieller vorwaerts konstruierter Object-X-Mechanismus.

FAIL: die gesamte verbliebene stopped-OU / relative-storage Architekturklasse wird geschlossen; die Survivor-Identitaeten bleiben als eigenstaendige Mathematik erhalten.

Naechster Einstieg: `00-uebersicht/NEXT_GATE.md`.
