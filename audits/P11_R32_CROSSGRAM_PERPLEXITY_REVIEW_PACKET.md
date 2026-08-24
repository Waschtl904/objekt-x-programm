# P11/R32 — unabhängiges Review-Paket: Schur-Cross-Gram und Dichtheits-No-Go

**Status:** Review-Anforderung; keine Promotion.  
**Repo:** `Waschtl904/objekt-x-programm`, Branch `main`.  
**Kandidaten:**

- `92289a0e7000c2e636dfc5073a66d6b61977d4fb` — `audits/P11_R32_SCHUR_CROSSGRAM_AUDIT.md`
- `5a58130a49b37a31ec7a3c865734f2921730bf89` — `audits/P11_R32_INNER_DENSITY_NOGO_AUDIT.md`

Diese Kandidaten bauen logisch auf dem noch separat zu prüfenden P11↔P12-Rückbindungs-Audit auf.  Bitte die hier behaupteten funktionalanalytischen Identitäten dennoch eigenständig prüfen.

**P11 FROZEN; R14 unverändert.**

---

## A. Cross-Gram-Faktorisierung

Fixiere
\[
H=H_{T_0},
\qquad
B=(I+R_{T_0}^*R_{T_0})^{-1}>0,
\qquad
\mathscr M=B^{1/2}H^*.
\]

Bitte unabhängig bestätigen:

1. `B^{1/2}` ist beschränkt und beschränkt invertierbar;
2. der feste Schurterm faktorisiert exakt als
   \[
   \Sigma_{T_0}=HBH^*=\mathscr M^*\mathscr M;
   \]
3. für inneres Fenster `I` und Annulus `A`, mit
   \[
   \mathscr M_I=\mathscr M E_I,
   \qquad
   \mathscr M_A=\mathscr M E_A,
   \]
   gilt
   \[
   E_A^*\Sigma E_I=\mathscr M_A^*\mathscr M_I,
   \qquad
   E_I^*\Sigma E_A=\mathscr M_I^*\mathscr M_A.
   \]

Verdict:

```text
CG-1 SCHUR CROSS-GRAM FACTORIZATION: GREEN / PARTIAL / FAIL
```

---

## B. Exakte Annihilatorcharakterisierung

Setze
\[
\mathcal N_I=\overline{\operatorname{Ran}\mathscr M_I}
\]
und `P_I` als orthogonale Projektion darauf.

Bitte prüfen:
\[
\ker(E_I^*\Sigma E_A)
=
\ker(\mathscr M_I^*\mathscr M_A)
=
\{w:\mathscr M_Aw\in\mathcal N_I^\perp\}
=
\ker(P_I\mathscr M_A).
\]

Wenn die P11↔P12-Rückbindung GREEN ist, gilt auf den global geschlossenen P12-Strata
\[
\ker(H E_A|_-)=0.
\]
Mit `H*=-H` und invertiblem `B^{1/2}` soll daraus
\[
\ker\mathscr M_A=0
\]
folgen.

Damit müsste ein nichttrivialer Schur-Annihilator zwingend
\[
0\ne\mathscr M_Aw\in\mathcal N_I^\perp
\]
erzeugen.

Bitte prüfen, ob daher die Formulierung
\[
\operatorname{Ran}\mathscr M_A\cap\mathcal N_I^\perp=\{0\}?
\]
als **exakte relative Transversalitätsfrage** korrekt ist, unter Beachtung möglicher Nichtabgeschlossenheit von `Ran M_A`.

Verdict:

```text
CG-2 ANNIHILATOR = CROSS-GRAM TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

---

## C. Quantitative Firewall

Der Kandidat definiert punktweise
\[
\alpha(w)
=\frac{\|P_I\mathscr M_Aw\|}{\|\mathscr M_Aw\|}
\]
auf P12-Injektivitätsstrata.

Bitte bestätigen:

- `T* w=0 iff alpha(w)=0`;
- `inf alpha(w)>0` wäre eine stärkere uniforme Winkelbedingung;
- selbst eine uniforme Winkelbedingung liefert ohne bounded-below-Kontrolle von `M_A` noch keinen bounded-below-Satz in der ursprünglichen `w`-Norm.

Verdict:

```text
CG-3 QUANTITATIVE FIREWALL: GREEN / PARTIAL / FAIL
```

---

## D. Starker Dichtheitstest

Der Kandidat notiert als hinreichend:
\[
\overline{\operatorname{Ran}\mathscr M_I}
=\mathcal K_{med}^{+}
\Longrightarrow
\ker(\mathscr M_I^*\mathscr M_A)=0.
\]

Bitte prüfen außerdem die behauptete Äquivalenz der Dichtheit mit Injektivität der adjungierten inneren Beobachtung:
\[
\overline{\operatorname{Ran}(B^{1/2}H^*E_I)}=\mathcal K_{med}^{+}
\iff
\ker(E_I^*H B^{1/2})=0.
\]
Da `B^{1/2}` bijektiv ist, ist der Nullraum von `E_I^*H B^{1/2}` genau `B^{-1/2} ker(E_I^*H)`.

Verdict:

```text
CG-4 DENSE-INNER SUFFICIENCY TEST: GREEN / PARTIAL / FAIL
```

---

## E. DN-1: expliziter No-Go für R<a

Im P12-Drei-Shift-Fenster sind die aktiven Halbshifts
\[
a=\frac12\log2,
\quad b>a,
\quad T>a.
\]

Fixiere `0<R<a`.  Wähle
\[
0<\varepsilon<a-R
\]
und einen nichtzero geraden
\[
v\in C_c^\infty(-\varepsilon,\varepsilon)^+.
\]

Bitte direkt prüfen, dass für jedes `|u|<R` und jeden aktiven Halbshift `tau>=a`
\[
|u\pm\tau|>\varepsilon,
\]
also
\[
D_{2\tau}v(u)=0
\]
und damit
\[
E_I^*Hv=0.
\]

Anschließend mit
\[
y=B^{-1/2}v
\]
prüfen:
\[
\mathscr M_I^*y
=E_I^*HB^{1/2}y
=0,
\]
so
\[
\ker\mathscr M_I^*\ne0
\]
und deshalb
\[
\overline{\operatorname{Ran}\mathscr M_I}
e\mathcal K_{med}^{+}.
\]

Der gewünschte Status bei GREEN ist ausschließlich:

> `DN-1: ✓[M]_neg` für den **zu starken dichten inneren Mediator-Suffizienzweg** bei `0<R<a`.

Nicht erlaubt ist daraus die Existenz eines Schur-Annihilators zu folgern.

Verdict:

```text
DN-1 CENTRAL INVISIBLE VECTOR: GREEN / PARTIAL / FAIL
DN-1 INNER MEDIATOR NOT DENSE: GREEN / PARTIAL / FAIL
DN-1 SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

---

## F. Verbleibende echte Frage

Bitte adversarial prüfen, ob nach CG + DN korrekt nur folgende relative Lagefrage übrig bleibt:
\[
\boxed{
\operatorname{Ran}\mathscr M_A
\cap
\ker\mathscr M_I^*
\stackrel?=\{0\}.
}
\]

DN-1 zeigt nur, dass `ker M_I*` nichtzero ist.  P12-Injektivität zeigt nur, dass `M_A w` für `w !=0` nichtzero ist.  Keines von beidem entscheidet, ob das Annulusbild die unsichtbaren inneren Richtungen tatsächlich trifft.

Verdict:

```text
POST-P12 TRUE TRANSVERSALITY STILL OPEN: GREEN / PARTIAL / FAIL
```

---

## G. Gesamtverdict

Bitte ausgeben:

```text
CG-1 SCHUR CROSS-GRAM FACTORIZATION:       GREEN / PARTIAL / FAIL
CG-2 EXACT TRANSVERSALITY REDUCTION:       GREEN / PARTIAL / FAIL
CG-3 QUANTITATIVE FIREWALL:                GREEN / PARTIAL / FAIL
CG-4 DENSE-INNER SUFFICIENCY:              GREEN / PARTIAL / FAIL
DN-1 CENTRAL INVISIBLE VECTOR:             GREEN / PARTIAL / FAIL
DN-1 INNER RANGE DENSITY NO-GO:            GREEN / PARTIAL / FAIL
POST-P12 TRUE TRANSVERSALITY REMAINS OPEN: GREEN / PARTIAL / FAIL
CROSS-GRAM PACKAGE OVERALL:                GREEN / PARTIAL / FAIL
```

Bei `PARTIAL` oder `FAIL` bitte die erste konkrete mathematische Abweichung angeben.

Bei vollständigem GREEN darf **CG-1** als exakter Reduktionssatz `✓[M]`, **DN-1** als Route-No-Go `✓[M]_neg` gebucht werden.  Die eigentliche Transversalitätsfrage bleibt `?[O]`.

Keine Polar-Gauge-, Strong-Terminal-Transport-, Objekt-X- oder RH-Aussage ist zulässig.
