# P11/R32 — unabhängiges Review-Paket: ST-1 lokales 11-Wort- und Hub-Ledger

**Status:** Review-Anforderung; keine Promotion.  
**Zu prüfen:**
- `audits/P11_R32_SECOND_SHELL_TRANSVERSALITY_LOCAL_LEDGER_AUDIT.md`
- `consolidation/p11_r32_second_shell_transversality_local_ledger_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Die bisherige unabhängige ST-1-Prüfung bestätigte Vorzeichen-Elimination und P12-Sektoreinbettung, ließ aber die lokalen 11-Wort-Bilanzen an `x1=e-u`, `x2=a-u` sowie die vollständige Hub-Isolation als Restunsicherheit offen. Dieses Paket prüft ausschließlich diese Punkte.

## A. Rechte maskierte Profilkanäle

Rekonstruieren Sie für `y=U_R f` auf der positiven Achse:

\[
g_1=M20K_1y:
\quad d+u\mapsto-f(u),
\quad a-u\mapsto-\rho f(u),
\]
\[
g_2=M20K_2y:
\quad u\mapsto\rho f(u),
\quad e-u\mapsto f(u),
\]
\[
g_3=M20K_3y:
\quad a+u\mapsto\rho f(u)1_{u<\varepsilon},
\quad a+e-u\mapsto f(u)1_{u>e-\varepsilon}.
\]
Prüfen Sie außerdem `K_j^*=-K_j` und die Ungeradheit der `g_k`.

```text
STL-A RIGHT CHANNELS: GREEN / PARTIAL / FAIL
```

## B. Alle elf Wörter an x1=e-u

Prüfen Sie Wort für Wort:

- `W11`: aktiv, Beitrag `-p^2 f(u)`;
- `W12`: null;
- `W13`: aktiv genau für `u>e-epsilon`, Beitrag `+q^2 f(u)`;
- `W21,W22,W23`: null;
- `W31,W32,W33`: null;
- `(2,1)`-Selbstterm: null;
- `(3,0)`-Selbstterm: null.

Kritische Rücktransportidentitäten:
\[
x_1-a=-(d+u),\quad x_1+a=a+e-u,
\]
\[
x_1-T=-(b+u),\quad x_1+b=T-u,
\]
\[
x_1-b=-(2d+u).
\]
Bitte insbesondere sicherstellen, dass kein Wort außerhalb `W11,W13` über einen negativen, durch Ungeradheit zurückgefalteten Kanal doch `x1` erreicht.

Gewünschtes Resultat:
\[
(AU_Rf)(e-u)=\left[-p^2+q^2 1_{u>e-\varepsilon}\right]f(u).
\]

```text
STL-B X1 FULL 11-WORD LEDGER: GREEN / PARTIAL / FAIL
```

## C. Alle elf Wörter an x2=a-u

Prüfen Sie Wort für Wort:

- `W11`: null;
- `W12`: aktiv, Beitrag `+gamma rho f(u)`;
- `W13`: null;
- `W21`: null;
- `W22`: null;
- `W23`: aktiv genau für `u<epsilon`, Beitrag `+gamma rho beta f(u)`;
- `W31,W32,W33`: null;
- `(2,1)`-Selbstterm: null;
- `(3,0)`-Selbstterm: null.

Kritische Identitäten:
\[
x_2-a=-u,\quad x_2+a=T-u,
\]
\[
x_2-T=-(a+u),\quad x_2+b=a+b-u,
\]
\[
x_2-b=-(d+u).
\]
Gewünschtes Resultat:
\[
(AU_Rf)(a-u)
=\gamma\rho\left(1+\beta1_{u<\varepsilon}\right)f(u).
\]

```text
STL-C X2 FULL 11-WORD LEDGER: GREEN / PARTIAL / FAIL
```

## D. Hub-Isolation an x1=e-u

Prüfen Sie alle sechs Hubäste:

- `a` rückwärts: `-(d+u)` — einzig potentiell aktiv;
- `a` vorwärts: `a+e-u>a+R>a>S` — aus;
- `b` rückwärts: `-(2d+u)` mit `2d>a>S` — aus;
- `b` vorwärts: `T-u>b+R>b>a>S` — aus;
- `T` rückwärts: `-(b+u)` — aus;
- `T` vorwärts: `T+e-u>T>S` — aus.

Gewünscht:
\[
(HE_Aw)(e-u)=-p1_{d+u<S}w(d+u).
\]

```text
STL-D X1 HUB ISOLATION: GREEN / PARTIAL / FAIL
```

## E. Hub-Isolation an x2=a-u

Prüfen Sie alle sechs Hubäste:

- `a` rückwärts: `-u`, und `u<ell<R` — inneres Loch;
- `a` vorwärts: `T-u>b+R>b>a>S` — aus;
- `b` rückwärts: `-(d+u)` — einzig potentiell aktiv;
- `b` vorwärts: `a+b-u>a>S` — aus;
- `T` rückwärts: `-(a+u)` — aus;
- `T` vorwärts: `3a-u>T>a>S` — aus.

Gewünscht:
\[
(HE_Aw)(a-u)=-r1_{d+u<S}w(d+u).
\]

```text
STL-E X2 HUB ISOLATION: GREEN / PARTIAL / FAIL
```

## F. ST-1 Schlusskette

Unter vollständigem GREEN von B–E sind die beiden ambient Gleichungen exakt
\[
-P_u f-p\chi W=0,
\qquad
G_u f-r\chi W=0,
\]
mit `P_u>0`, `G_u>0`, `chi=1_{d+u<S}`. Die frühere unabhängige Prüfung hat bereits
\[
\det\begin{pmatrix}-P_u&-p\\G_u&-r\end{pmatrix}
=P_ur+pG_u>0
\]
und die Sektor-Einbettung `S<a<T` in das globale P12-Stratum `S<T` bestätigt.

Bestätigen Sie daher, dass nach B–E keine verbleibende lokale Vollständigkeitslücke in ST-1 übrigbleibt.

```text
STL-F ST-1 CLOSURE: GREEN / PARTIAL / FAIL
```

## G. Firewall

Auch vollständiges GREEN erlaubt nur:

- zweite explizite nichtzentrale Schale transversal;
- kein voller `N_I`-Klassifikationssatz;
- kein voller augmentierter Kernel;
- kein voller Schur-Crossblock;
- kein Closed Range / bounded below / uniforme Winkel;
- kein Polar Gauge / Strong Terminal / Objekt X / RH.

```text
STL SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
STL-A RIGHT CHANNELS:                GREEN / PARTIAL / FAIL
STL-B X1 FULL 11-WORD LEDGER:        GREEN / PARTIAL / FAIL
STL-C X2 FULL 11-WORD LEDGER:        GREEN / PARTIAL / FAIL
STL-D X1 HUB ISOLATION:              GREEN / PARTIAL / FAIL
STL-E X2 HUB ISOLATION:              GREEN / PARTIAL / FAIL
STL-F ST-1 CLOSURE:                  GREEN / PARTIAL / FAIL
STL SCOPE FIREWALL:                  GREEN / PARTIAL / FAIL
ST-1 LOCAL LEDGER OVERALL:           GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre ST-1 inhaltlich unabhängig geschlossen; formale Promotion weiterhin nur nach expliziter Freigabe.
