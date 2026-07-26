# NEU-220n — Endliche Fensteroperatoren und globaler Grenztyp

**Katalog-ID:** NEU-220n  
**Knoten:** [O-220-1-PD5a3f1-finite-window-selfadjoint-Weil-operators]  
**Vorgänger:** NEU-220m rev.2 (Commit bf2445a) — Gesamtform ✓[K/M]_part  
**Status:** ?[O]

---

## Motivation

Die Gesamtform $\mathfrak{W}:\mathcal{D}\times\mathcal{D}\to\mathbb{C}$ ist auf dem rigged space $\mathcal{D}\subset L^2\subset\mathcal{D}'$ wohldefiniert (NEU-220m, PD5a3e). Ein globaler selbstadjungierter $L^2$-Operator ist aus zwei Gründen gesperrt:

- $q_{\mathrm{pole}}$ hat keine stetige $L^2$-Fortsetzung.
- $q_{\mathrm{fin}}$ ist als $L^2$-Operatorreihe nicht gesichert konvergent.

Vor jedem globalen Kreinraum oder Randkanalraum ist die kanonische **endliche Fensterfamilie** $(\mathcal{H}_R, W_R)_{R>0}$ zu konstruieren. Auf jedem festen Fenster $[-R,R]$ fallen alle drei Hindernisse weg.

---

## PD5a3f1a — Fensterraum und Projektion

Für $R > 0$ setze

$$
\mathcal{H}_R = L^2([-R,R]), \qquad P_R : L^2(\mathbb{R}) \to \mathcal{H}_R
\quad (\text{Einschränkung + Nullfortsetzung}).
$$

Funktionen in $\mathcal{H}_R$ werden durch Nullfortsetzung als Elemente von $L^2(\mathbb{R})$ aufgefasst.

---

## PD5a3f1b — Randterm als beschränkter Rang-2-Operator

Auf $[-R,R]$ sind $e_\pm(u) = e^{\pm u/2} \in L^2([-R,R])$ quadratintegrierbar:

$$
\|e_\pm\|_{\mathcal{H}_R}^2 = \int_{-R}^R e^{\pm u}\,du = \frac{e^{\pm R}-e^{\mp R}}{\pm 1} < \infty.
$$

Daher sind die Funktionale $\ell_\pm|_{\mathcal{H}_R}$ durch Cauchy-Schwarz beschränkt, und

$$
\boxed{B_{\mathrm{pole},R} = |e_-\rangle\langle e_+| + |e_+\rangle\langle e_-|}
$$

ist ein beschränkter selbstadjungierter Rang-2-Operator auf $\mathcal{H}_R$. Auf der Diagonalen:

$$
\langle a, B_{\mathrm{pole},R}\, a\rangle_{\mathcal{H}_R} = 2\operatorname{Re}(\overline{\ell_-(a)}\,\ell_+(a)) = q_{\mathrm{pole}}(a).
$$

---

## PD5a3f1c — Primterm als endliche Summe beschränkter Operatoren

Für $a \in \mathcal{H}_R$ (Träger $\subseteq [-R,R]$) gilt

$$
\int_{\mathbb{R}} \overline{a(v)}\,a(v\pm\log n)\,dv \ne 0
\quad\Longrightarrow\quad \log n \le 2R.
$$

Daher ist

$$
\boxed{B_{\mathrm{fin},R} = -\sum_{\substack{n\ge2\\ \log n\le 2R}} \frac{\Lambda(n)}{\sqrt{n}}\,P_R(U_{\log n}+U_{-\log n})P_R}
$$

eine **endliche Summe** beschränkter selbstadjungierter Operatoren auf $\mathcal{H}_R$ (da $U_x$ unitär ist, sind alle Summanden beschränkt).

---

## PD5a3f1d — Gammaterm als semibeschränkte geschlossene Form

Das Symbol $\gamma_\infty^{\mathrm{sym}}(t)$ ist reell, nach unten beschränkt (NEU-220m, PD5a3c), und messbarer Multiplikator. Die auf $\mathcal{H}_R$ restringierte quadratische Form

$$
q_{\Gamma,R}(a) = \int_{\mathbb{R}} \gamma_\infty^{\mathrm{sym}}(t)\,|(\mathcal{F}(P_Ra))(t)|^2\,dt
$$

ist **semibeschränkt und geschlossen** auf $\mathcal{H}_R$ (da $P_Ra$ kompakten Träger hat, liegen alle Fouriertransformierten in der Schwartz-Klasse, und $\gamma_\infty^{\mathrm{sym}}$ ist nach unten beschränkt). Der zugehörige selbstadjungierte Operator sei $G_{\infty,R}$.

---

## PD5a3f1e — Gesamtoperator $W_R$ auf $\mathcal{H}_R$

Da $B_{\mathrm{pole},R}$ und $B_{\mathrm{fin},R}$ beschränkt sind, definiert

$$
\boxed{W_R := G_{\infty,R} + B_{\mathrm{pole},R} + B_{\mathrm{fin},R}}
$$

einen **selbstadjungierten Operator** auf $\mathcal{H}_R$ mit der Domäne $\mathcal{D}(W_R) = \mathcal{D}(G_{\infty,R})$.

**Konsistenz:** Für $a, b \in C_c^\infty((-R,R))$ gilt

$$
\langle a, W_R b\rangle_{\mathcal{H}_R} = \mathfrak{W}(a,b).
$$

Alle drei analytisch unterschiedlichen Kanäle kommen damit auf $\mathcal{H}_R$ erstmals im selben echten Operatorobjekt zusammen.

---

## PD5a3f1f — Die Familie $(\mathcal{H}_R, W_R)_{R>0}$

Für jedes $R > 0$ existiert ein selbstadjungierter Operator $W_R$ auf $\mathcal{H}_R$ mit

$$
\boxed{\langle a, W_R a\rangle_{\mathcal{H}_R} = \mathfrak{W}(a,a) = q_{\mathrm{pole}}(a)+q_\Gamma(a)+q_{\mathrm{fin}}(a)
\qquad\forall a\in C_c^\infty((-R,R)).}
$$

Diese Familie ist **RH-frei konstruiert**.

---

## PD5a3f1g — Globaler Engpass: präzise Hindernisse

Der globale Grenztyp ist nicht automatisch vorhanden. Die Hindernisse sind konkret:

| Hindernis | Beschreibung |
|-----------|--------------|
| Fehlende untere Schranke | Keine bekannte $R$-unabhängige untere Schranke für $W_R$ |
| Normwachstum Polblock | $\|B_{\mathrm{pole},R}\| \sim e^R$, wächst mit $R$ |
| Normwachstum Primblock | $\|B_{\mathrm{fin},R}\|$ wächst mit Anzahl der Primpotenzen $\le e^{2R}$ |
| Keine starke Resolventenkonvergenz | Kein kanonischer Limes $W_R \to W$ bekannt |
| Positivität des Grenzobjekts | $W_\infty \ge 0$ wäre RH-stark |

$$
\boxed{\text{Existiert aus }(W_R)_{R>0}\text{ ein kontrollierter globaler Grenzoperator oder eine Grenzrelation?}}
$$

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|-------------|--------|--------|
| PD5a3f1a | Fensterraum $\mathcal{H}_R$, Projektion $P_R$ | ✓[M] |
| PD5a3f1b | $B_{\mathrm{pole},R}$ beschränkter Rang-2-Operator | ✓[K/M] |
| PD5a3f1c | $B_{\mathrm{fin},R}$ endliche Summe beschränkter Operatoren | ✓[K/M] |
| PD5a3f1d | $G_{\infty,R}$ semibeschränkte geschlossene Form | ✓[K/M] |
| PD5a3f1e | $W_R = G_{\infty,R}+B_{\mathrm{pole},R}+B_{\mathrm{fin},R}$ selbstadjungiert | ✓[K/M] |
| PD5a3f1f | Konsistenz $\langle a,W_Ra\rangle = \mathfrak{W}(a,a)$ | ✓[K/M] |
| PD5a3f1g | Globaler Engpass: 5 Hindernisse isoliert | ?[O] |

```
[O-220-1-PD5a3f1-finite-window-selfadjoint-Weil-operators]
  → ✓[K/M]  (PD5a3f1a–f abgeschlossen)
  → ?[O]    (PD5a3f1g: globaler Grenztyp offen)
```

---

## Verbindung zu PD5a3g

Die Fensterfamilie liefert den richtigen Ausgangspunkt für den adelischen Intertwiner:

- Falls ein adelischer Operator $A_X$ auf $\mathcal{H}_X$ existiert mit $J_R^* A_X J_R = W_R$ für alle $R$, und falls $A_X \ge 0$, dann folgt RH.
- Der Grenztyp der Familie $(W_R)$ ist damit das Verbindungsstück zwischen der lokalen Operatorrealisierung und dem globalen adelischen Programm.

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220m rev.2 (bf2445a) | Korrekte Polarisation, Typklassifikation, alle Kanäle indefinit |
| NEU-220l (ddac5ff) | Weil-Quadratik $\mathfrak{W}(a)$ |
| NEU-220k (cc4345b) | Masterform |
| Bombieri (2000) | Weil-Kriterium, RH-Äquivalenz |
| Connes (1999) | Spurformel, BC-Kern, adelischer Rahmen |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
