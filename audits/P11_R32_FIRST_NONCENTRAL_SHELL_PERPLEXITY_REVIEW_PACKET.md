# P11/R32 — unabhängiges Review-Paket: erste nichtzentrale Schale

**Status:** Review-Anforderung; keine Promotion.  
**Aktuelle Kandidaten:**
- `050c9b672a2eb952ed28df7c80d053640e5eac27` — `audits/P11_R32_FIRST_NONCENTRAL_SHELL_TRANSVERSALITY_AUDIT.md`
- `596ad55755b1846bc44763f662a09a2db9c3bd2a` — `consolidation/p11_r32_first_noncentral_shell_verify.py`

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

## B. Full-Rest-Supportgap

Prüfen Sie adversarial aus der exakten SE-2-Zerlegung mit den Blöcken `(2,0),(2,1),(3,0)`, dass für `y in S_R^+` auf der positiven Achse
\[
\operatorname{ess\,supp}(Ay)
\subset
(a-h,a+h)\cup(a+2d-h,a+2d+h),
\]
mit Horizontabschnitt der äußeren Schale.

Insbesondere:

1. `(2,0),k=1`: zentraler maskierter Output verschwindet durch die Schalen-Symmetrie; äußere Kopien liegen außerhalb der Maske;
2. `(2,0),k=2`: nach Hin-/Rücktransport nur Zentren `±a`, `±3a`, wobei `3a>T0`;
3. `(2,0),k=3`: nach Maske null;
4. `(2,1)`: kein zusätzlicher positiver Support zwischen der ursprünglichen `a`-Schale und `a+2d`;
5. `(3,0)`: nach Hin-/Rücktransport genau Zentren `±a`, `±(a+2d)`.

Die untere Kante der ursprünglichen positiven Restschale ist
\[
a-h=e+R,
\]
die äußere beginnt erst bei
\[
a+2d-h=a+d+R.
\]

```text
NS-B REST SUPPORT GAP: GREEN / PARTIAL / FAIL
```

## C. Sauberer Auswertungspunkt u=a-x

Für jedes
\[
R<S<a,
\qquad x\in(R,S)
\]
setze `u=a-x`.

Prüfen Sie:

- `u<a-R`;
- aus `R>=d/2` folgt `a-R<=e+R=a-h`, also liegen sowohl `y(u)` als auch `(Ay)(u)` im Supportloch;
- der `a`-Hubkanal liefert genau `-p w(x)`;
- der `b`-Hubkanal liefert genau `-r w(x+d)` falls `x+d<S`, sonst null;
- der `T=2a`-Kanal ist vollständig außerhalb des Annulus.

Damit soll exakt gelten
\[
\boxed{
pw(x)+r1_{\{x+d<S\}}w(x+d)=0
\quad\text{für fast jedes }x\in(R,S).}
\]

```text
NS-C CLEAN LOWER OUTPUT EQUATION: GREEN / PARTIAL / FAIL
```

## D. Zwei-Schritt-d-Descent

Prüfen Sie zunächst die Breitenabschätzung
\[
S-R<a-R\le a-d/2<3d/2<2d,
\]
wobei `d>a/2` aus `9>8` folgt.

Teile den Annulus in
\[
H=(\max\{R,S-d\},S),
\qquad
L=(R,S-d)
\]
(falls `L` nichtleer).

- Für `x in H` gilt `x+d>=S`, also erzwingt die saubere Gleichung `w(x)=0`.
- Für `x in L` liegt `X=x+d` im Annulus. Wegen `S-R<2d` gilt `X+d>S`, also liegt `X in H` und `w(X)=0`; die Gleichung bei `x` erzwingt dann `w(x)=0`.

Damit soll ohne weitere Fallunterscheidung
\[
\boxed{w=0\text{ auf dem ganzen Annulus}}
\]
folgen. Anschließend liefert `(I+A)y=0`, `A>=0`, auch `y=0`.

```text
NS-D TWO-STEP d-DESCENT: GREEN / PARTIAL / FAIL
```

## E. Gesamtsatz

Prüfen Sie die exakte Reichweite
\[
\boxed{\frac d2\le R<d,\qquad R<S<a}
\]
und die Aussage
\[
\boxed{
\ker\mathcal K_{I,A}\cap(\mathcal S_R^+\oplus\mathscr H_A^-)=\{0\}.
}
\]

Es darf **kein** verbleibender `S`-Restkeil für diese erste Schale gebucht werden.

```text
NS-E FULL FIRST-SHELL TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

## F. Scope-Firewall

Nicht erlaubt:

- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Klassifikation sämtlicher weiterer Teile von `N_I`;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

```text
NS SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
NS-A FIRST SHELL INVISIBILITY:       GREEN / PARTIAL / FAIL
NS-B REST SUPPORT GAP:               GREEN / PARTIAL / FAIL
NS-C CLEAN LOWER OUTPUT EQUATION:    GREEN / PARTIAL / FAIL
NS-D TWO-STEP d-DESCENT:             GREEN / PARTIAL / FAIL
NS-E FULL FIRST-SHELL TRANSVERSALITY: GREEN / PARTIAL / FAIL
NS SCOPE FIREWALL:                   GREEN / PARTIAL / FAIL
FIRST NONCENTRAL SHELL OVERALL:      GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN wäre zulässig:

- **NS-1a:** `✓[M]` — unendlichdimensionale erste nichtzentrale Schale liegt in `N_I`;
- **NS-1:** `✓[M]_part` — diese gesamte Schale ist für jedes `R<S<a` transversal, sofern `d/2<=R<d`.

Keine Promotion ohne explizite Freigabe.
