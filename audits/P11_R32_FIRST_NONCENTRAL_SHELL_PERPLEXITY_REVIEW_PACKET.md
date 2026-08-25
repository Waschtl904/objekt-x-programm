# P11/R32 — unabhängiges Review-Paket: erste nichtzentrale Schale

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `01d2be4221872a4b46e12cd74367f2c12299232d` — `audits/P11_R32_FIRST_NONCENTRAL_SHELL_TRANSVERSALITY_AUDIT.md`
- `ae307381c20372f310be59ba1c31d0c98db0a370` — `consolidation/p11_r32_first_noncentral_shell_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte den Verifier nur als Cross-check verwenden. Rekonstruieren Sie die Supportargumente direkt aus P11s Hub- und Full-Rest-Definitionen.

## A. Nichtzentrale Unsichtbarkeitsschale

Setze
\[
d=b-a,
\qquad \frac d2\le R<d,
\qquad h=d-R.
\]
Definiere \(\mathcal S_R^+\) als geraden Schalenraum mit positivem Träger
\[
(a-h,a+h)=(e+R,b-R)
\]
und Profilbedingung
\[
y(a-s)=y(a+s),\qquad |s|<h.
\]

Prüfen Sie direkt für \(0<u<R\):

- die beiden \(a\)-Äste heben sich für \(u<h\) exakt auf und sind für \(u>h\) beide außerhalb;
- der \(b\)-Ast beginnt erst bei \(b-R=a+h\);
- der \(T=2a\)-Ast liegt noch weiter außen.

Damit soll gelten
\[
\boxed{\mathcal S_R^+\subset\ker(E_I^*H|_+)}.
\]

```text
NS-A FIRST SHELL INVISIBILITY: GREEN / PARTIAL / FAIL
```

## B. Full-Rest-Support von A auf dieser Schale

Prüfen Sie adversarial aus der exakten SE-2-Zerlegung mit den drei Blöcken `(2,0),(2,1),(3,0)`, dass für `y in S_R^+` auf der positiven Achse
\[
\operatorname{ess\,supp}(Ay)
\subset
(a-h,a+h)\cup(a+2d-h,a+2d+h),
\]
mit Horizontabschnitt der äußeren Schale.

Insbesondere:

1. `(2,0),k=1`: zentraler maskierter Output verschwindet durch die Schalen-Symmetrie; äußere Outputkopien liegen außerhalb der `Omega_(2,0)`-Maske;
2. `(2,0),k=2`: nach `K^* M K` entstehen nur Rückkopien um `±a` und `±3a`, wobei `3a>T0`;
3. `(2,0),k=3`: nach Maske null;
4. `(2,1)`: erzeugt keine positive Supportzentren zwischen der ursprünglichen `a`-Schale und der äußeren `a+2d`-Schale;
5. `(3,0)`: erzeugt nach Hin- und Rücktransport genau die Zentren `±a` und `±(a+2d)`.

Prüfen Sie besonders die linke Kante der äußeren positiven Restschale:
\[
a+2d-h=a+d+R=b+R=a+(d+R).
\]

```text
NS-B REST SUPPORT GAP: GREEN / PARTIAL / FAIL
```

## C. Auswertung bei u=a+x

Unter
\[
R<S<a,
\qquad S\le R+d
\]
fixiere `x in (R,S)`.

Prüfen Sie:

- `h=d-R<=R<x`, also `y(a+x)=0`;
- wegen des Supportgaps aus B und `x<S<=R+d` gilt `(Ay)(a+x)=0`;
- im Hubterm ist der `a`-Ast genau `+p w(x)`;
- der rückwärtige `b`-Punkt `x-d` liegt stets im inneren Loch, weil `R>=d/2` und `x<R+d`;
- der `T=2a`-Ast ist wegen Ungeradheit genau `-q w(a-x)` sofern `a-x` im Annulus liegt.

Damit soll exakt
\[
pw(x)-q1_{(R,S)}(a-x)w(a-x)=0
\]
gelten.

```text
NS-C CLEAN REFLECTION EQUATION: GREEN / PARTIAL / FAIL
```

## D. Zwei-Punkt-Reflexionsblock

Falls `a-x` außerhalb des Annulus liegt, folgt direkt `w(x)=0`.
Falls `x'=a-x` im Annulus liegt, prüfen Sie die beiden Gleichungen
\[
pw(x)-qw(x')=0,
\qquad
pw(x')-qw(x)=0
\]
mit
\[
\det\begin{pmatrix}p&-q\\-q&p\end{pmatrix}
=p^2-q^2
=(\log2)(2^{-3/2}-2^{-3})>0.
\]

Daraus soll `w=0` auf dem ganzen Annulus folgen. Danach liefert `(I+A)y=0` wegen `A>=0` auch `y=0`.

```text
NS-D FIRST SHELL TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

## E. Reichweite und Restkeil

Prüfen Sie
\[
e=a-d,
\qquad R\ge e\Longrightarrow R+d\ge a.
\]
Damit deckt NS-1 für
\[
e\le R<d
\]
automatisch jedes `R<S<a` ab.

Der einzige offene Teil dieser ersten Schale soll daher sein
\[
\frac d2\le R<e,
\qquad R+d<S<a.
\]

Prüfen Sie zusätzlich die Strukturbeobachtung:

- Schalenreflexion auf der Annuluskoordinate: `J_d(x)=2d-x`;
- q-Reflexion: `J_a(x)=a-x`;
- Komposition:
\[
J_d\circ J_a(x)=x+(2d-a)=x+\delta,
\qquad \delta=d-e.
\]

Dies darf nur als Orbitstruktur, nicht als Injektivität des Restkeils gebucht werden.

```text
NS-E RANGE / DELTA-ORBIT FIREWALL: GREEN / PARTIAL / FAIL
```

## F. Scope-Firewall

Nicht erlaubt:

- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Restkeil bereits gelöst;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

```text
NS SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
NS-A FIRST SHELL INVISIBILITY:       GREEN / PARTIAL / FAIL
NS-B REST SUPPORT GAP:               GREEN / PARTIAL / FAIL
NS-C CLEAN REFLECTION EQUATION:      GREEN / PARTIAL / FAIL
NS-D FIRST SHELL TRANSVERSALITY:     GREEN / PARTIAL / FAIL
NS-E RANGE / DELTA-ORBIT FIREWALL:   GREEN / PARTIAL / FAIL
NS SCOPE FIREWALL:                   GREEN / PARTIAL / FAIL
FIRST NONCENTRAL SHELL OVERALL:      GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **NS-1a:** `✓[M]` — unendlichdimensionale erste nichtzentrale Schale liegt in `N_I`;
- **NS-1:** `✓[M]_part` — diese Schale ist für `S<=R+d` transversal; insbesondere für `e<=R<d` und jedes `R<S<a`.

Keine Promotion ohne explizite Freigabe.
