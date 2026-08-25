# P11/R32 — unabhängiges Review-Paket: zweite nichtzentrale Schale / 10-von-11-Ledger

**Status:** Review-Anforderung; keine Promotion.  
**Kandidaten:**
- `audits/P11_R32_SECOND_NONCENTRAL_SHELL_LEDGER_AUDIT.md`
- `consolidation/p11_r32_second_noncentral_shell_ledger_verify.py`

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte den Verifier nur als Cross-check verwenden. Die Trägergeometrie und alle elf Full-Rest-Wörter sollen unabhängig gegen P11/SE-2 rekonstruiert werden.

## A. Zweite Rand-Schale wirklich in N_I?

Setze
\[
d=b-a,\qquad e=T-b=2a-b,
\qquad \frac d2\le R<e,
\qquad \ell=e-R.
\]
Prüfen Sie zunächst
\[
0<\ell<R,\qquad R<e<a/2.
\]

Auf der positiven Achse seien
\[
J_b=(b,b+\ell)=(b,T-R),
\]
\[
J_T=(T-\ell,T)=(b+R,T).
\]
Für gerade `y` mit positivem Träger in `J_b union J_T` und
\[
q y(T-u)=r y(b+u),\qquad 0<u<\ell,
\]
soll gelten
\[
\boxed{E_I^*Hy=0.}
\]

Bitte besonders prüfen:

- `a+R<b`, also kein versteckter p=2 primitive branch;
- für `0<u<ell` sind exakt `b+u` und `T-u` aktiv und heben sich gewichtet auf;
- für `ell<u<R` liegen beide Punkte im mittleren Supportloch `(T-R,b+R)`;
- die Rand-Schalen sind wirklich disjunkt;
- der Raum ist unendlichdimensional.

```text
SS-A SECOND SHELL INVISIBILITY: GREEN / PARTIAL / FAIL
```

## B. Warum eine volle Mittelpunkt-Spiegelung falsch wäre

Prüfen Sie die Firewall: Eine Relation
\[
q y(m-v)=r y(m+v)\quad\text{für beide Vorzeichen von }v
\]
würde zusammen mit `v -> -v` wegen `r != q` den Nullvektor erzwingen. Die im Audit verwendete einseitige Rand-Schalenpaarung darf diesen Fehler nicht enthalten.

```text
SS-B ONE-SIDED PAIRING FIREWALL: GREEN / PARTIAL / FAIL
```

## C. Pre-Adjoint-Supports der drei (2,0)-Spalten

Prüfen Sie direkt:

### K1
positive maskierte Outputs
\[
(d,d+\ell),\qquad(a-\ell,a),
\]
beide vollständig in `Omega20`.

### K2
positive maskierte Outputs
\[
(0,\ell),\qquad(R,e),
\]
beide vollständig in `Omega20`.

### K3
mindestens der Output
\[
(a,a+\ell)
\]
und daher wegen `epsilon>0` ein nichttrivialer Schnitt mit `Omega20=(...,a+epsilon)`.

Damit sollen alle drei rechten `(2,0)`-Spalten als Operatoren auf der Schale nicht null sein.

```text
SS-C THREE ACTIVE RIGHT COLUMNS: GREEN / PARTIAL / FAIL
```

## D. Singleton-Blöcke

Prüfen Sie:

- `(2,1)` enthält nur `K2`; dessen Output `(0,ell)` schneidet jede positive epsilon-Maske nichttrivial;
- `(3,0)` enthält `K_b`; dessen positive Outputs `(0,ell) union (R,e)` liegen vollständig in `|u|<e+epsilon`.

```text
SS-D SINGLETON BLOCKS ACTIVE: GREEN / PARTIAL / FAIL
```

## E. Vollständiges 9-Wort-Ledger des (2,0)-Blocks

Mit
\[
W_{lk}=K_l^*M_{20}K_k,
\qquad l,k\in\{1,2,3\},
\]
prüfen Sie **jedes** der neun Wörter.

Behauptet wird:

- `W11,W12,W13,W21,W22,W23,W31,W33` sind als Operatoren auf der Schale nicht identisch null;
- nur
  \[
  \boxed{W32=K_3^*M_{20}K_2=0}
  \]
  stirbt identisch.

Für `W32` bitte die Horizontschranke rekonstruieren:

- `M20 K2 y` liegt in `|u|<e`;
- `K3*` kann innerhalb `|x|<=T0` nur Input ab Abstand `3a-T0=a-epsilon` erreichen;
- `epsilon<E` und
  \[
  a-E>e
  \]
  mit
  \[
  a-E-e=a+b-c>0\iff6>5.
  \]

Für `W31,W33` prüfen Sie dagegen, dass die rechten maskierten Supports bis an bzw. über `a` reichen und daher die Schwelle `a-epsilon<a` schneiden.

```text
SS-E NINE-WORD LEDGER: GREEN / PARTIAL / FAIL
```

## F. 10-von-11-Gesamtbilanz

Aus E plus den beiden aktiven Singleton-Blöcken soll exakt folgen
\[
\boxed{8+1+1=10\text{ von }11}
\]
als Operatoren nicht identisch null.

Bitte die Formulierung eng lesen: `aktiv` bedeutet hier **nicht identisch null auf der Schale**, nicht dass jedes Wort für jeden einzelnen Vektor oder an jedem Auswertungspunkt beiträgt.

```text
SS-F TEN-OF-ELEVEN LEDGER: GREEN / PARTIAL / FAIL
```

## G. Strategische Firewall

Aus der dichten Wortbilanz darf nur geschlossen werden, dass eine naive Wiederholung des sparse NS-1-Supportarguments nicht gerechtfertigt ist.

Nicht erlaubt:

- zweite Schale bereits transversal;
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- `10 active words` bedeutet irgendeine Coercivity- oder Rank-Aussage;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

```text
SS SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
SS-A SECOND SHELL INVISIBILITY:       GREEN / PARTIAL / FAIL
SS-B ONE-SIDED PAIRING FIREWALL:      GREEN / PARTIAL / FAIL
SS-C THREE ACTIVE RIGHT COLUMNS:      GREEN / PARTIAL / FAIL
SS-D SINGLETON BLOCKS ACTIVE:         GREEN / PARTIAL / FAIL
SS-E NINE-WORD LEDGER:                GREEN / PARTIAL / FAIL
SS-F TEN-OF-ELEVEN LEDGER:            GREEN / PARTIAL / FAIL
SS SCOPE FIREWALL:                    GREEN / PARTIAL / FAIL
SECOND NONCENTRAL SHELL OVERALL:      GREEN / PARTIAL / FAIL
```

Bei vollständigem unabhängigem GREEN wäre zulässig:

- **SS-1a:** `✓[M]` — zweite nichtzentrale Rand-Schale ist ein unendlichdimensionaler Unterraum von `N_I` für `d/2<=R<e`;
- **SS-L:** `✓[M]` — exakte 10-von-11-Wortklassifikation auf dieser Schale.

Die Schur-Transversalität dieser zweiten Schale bleibt `?[O]`.

Keine Promotion ohne explizite Freigabe.
