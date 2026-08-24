# P11/R32 — unabhängiges Review-Paket: Schur-Inversenelimination

**Status:** Review-Anforderung; keine Promotion.  
**Repo:** `Waschtl904/objekt-x-programm`, Branch `main`.  
**Kandidatenkette:**

- `b71e4101a61dbdabce84d1d2ac00a8544c739a3c` — `audits/P11_R32_SCHUR_INVERSE_ELIMINATION_AUDIT.md`
- `f65d40425969fa5661f96fa886636ff43e74cc59` — erster Verifier-Commit
- `cc31162e8f22ee88e267c1fa00c2357d67233fed` — verstärkter Verifier-Sanity-Check

**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte nicht den retained verifier als Beweisersatz verwenden. Prüfen Sie die Funktionalanalysis direkt gegen P11s Definitionen und verwenden Sie
`consolidation/p11_r32_schur_inverse_elimination_verify.py`
nur als Cross-check.

---

## A. Exakte Schur-Inversenelimination

Setze bei festem `T0`
\[
H=H_{T_0},\quad
A=R_{T_0}^*R_{T_0}\ge0,\quad
B=(I+A)^{-1},
\]
mit P11s
\[
H^*=-H.
\]
Für inneres Fenster `I=(-R,R)` und Annulus
\[
\mathcal A=(-S,-R)\cup(R,S)
\]
definiere
\[
\mathcal S_{I,A}=E_I^*HBH^*E_{\mathcal A}.
\]

Der Kandidat definiert
\[
\mathcal K_{I,A}(y,w)
=
\bigl((I+A)y+HE_{\mathcal A}w,\;E_I^*Hy\bigr).
\]

Bitte unabhängig prüfen:

1. die Paritätstypisierung `y even`, `w odd`, erste Komponente even, zweite odd;
2. für jedes `w in ker S` liefert
   \[
   y=BH^*E_Aw
   \]
   ein Kernelpaar von `K`;
3. jedes Kernelpaar von `K` erfüllt zwingend
   \[
   y=BH^*E_Aw
   \]
   und damit `w in ker S`;
4. `w=0` erzwingt wegen Invertierbarkeit von `I+A` auch `y=0`.

Damit soll exakt gelten:
\[
\boxed{\ker\mathcal S_{I,A}\cong\ker\mathcal K_{I,A}}
\]
und insbesondere
\[
\boxed{\ker\mathcal S_{I,A}=0\iff\ker\mathcal K_{I,A}=0.}
\]

Verdict:

```text
SE-1 BLOCK-KERNEL EQUIVALENCE: GREEN / PARTIAL / FAIL
```

---

## B. Inversefreie Range-Transversalität

Setze
\[
\mathcal N_I:=\ker(E_I^*H|_{\mathscr H^+}).
\]
Für
\[
z=HE_Aw
\]
ist die Schur-Kernbedingung äquivalent zu
\[
Bz\in\mathcal N_I,
\]
also wegen `B^{-1}=I+A`
\[
z\in(I+A)\mathcal N_I.
\]

Bitte prüfen, dass auf einem P12-Stratum mit
\[
\ker(HE_A|_-)=0
\]
exakt gilt:
\[
\boxed{
\ker\mathcal S_{I,A}=0
\iff
\operatorname{Ran}(HE_A|_-)
\cap(I+A)\mathcal N_I
=\{0\}.
}
\]

Bitte ausdrücklich die Firewall bestätigen, dass ohne äußere Hub-Injektivität die reine Schnittformulierung `z!=0` einen möglichen nichttrivialen `w` im Hubkern verlieren könnte; die Blockkern-Äquivalenz selbst benötigt diese Zusatzannahme nicht.

Verdict:

```text
SE-1 INVERSE-FREE RANGE TRANSVERSALITY: GREEN / PARTIAL / FAIL
```

---

## C. Full-Rest-Faktorisierung und aktive Martingaleblöcke

Prüfen Sie direkt aus P11 §3.4:
\[
\widetilde R^*\widetilde R=R^*R
\]
und
\[
(\widetilde Rf)_{p,j}
=\sqrt{(\log p)(p-1)p^j}\,1_{\Omega_{p,j}}\Phi_{p,j}[f],
\]
\[
\Phi_{p,j}
=\sum_{k\ge j+1}p^{-3k/4}K_{k\log p}^{tr}.
\]

Im gesamten Fenster
\[
\log2<T_0<\frac12\log5
\]
soll gelten:

```text
(p,j) = (2,0), (2,1), (3,0)
```

und keine weiteren nichtleeren Martingaleblöcke.

Verdict:

```text
SE-2 ACTIVE REST BLOCKS: GREEN / PARTIAL / FAIL
```

---

## D. Effektive k-Listen auf den jeweiligen Outputfenstern

Bitte nicht nur die grobe Schranke `p^k <= exp(4T0)` verwenden, sondern auf jedem
\(\Omega_{p,j}\) direkt prüfen, wann
\(K_{k\log p}^{tr}\)
identisch verschwindet.

Behauptet wird:

\[
\Phi_{2,0}
=2^{-3/4}K_{\log2}^{tr}
+2^{-3/2}K_{2\log2}^{tr}
+2^{-9/4}K_{3\log2}^{tr},
\]
\[
\Phi_{2,1}=2^{-3/2}K_{2\log2}^{tr},
\]
\[
\Phi_{3,0}=3^{-3/4}K_{\log3}^{tr}.
\]

Die Ausschlüsse beruhen auf den exakten Ungleichungen
\[
5a>\log5=2c,
\qquad
3b>\log5=2c,
\]
äquivalent zu
\[
2^5>5^2,
\qquad
3^3>5^2.
\]

Bitte insbesondere adversarial prüfen, ob ein `k=4` im `(2,0)`-Block oder ein `k=2` im `(3,0)`-Block auf einem Teil von `Omega` doch noch beitragen könnte.

Verdict:

```text
SE-2 EFFECTIVE K LISTS: GREEN / PARTIAL / FAIL
```

---

## E. Exakte 11-Wort-Darstellung von R*R

Mit
\[
M_\Omega=1_\Omega
\]
behauptet der Kandidat:
\[
\begin{aligned}
R^*R={}&(\log2)\Phi_{2,0}^*M_{\Omega_{2,0}}\Phi_{2,0}\\
&+2(\log2)\Phi_{2,1}^*M_{\Omega_{2,1}}\Phi_{2,1}\\
&+2(\log3)\Phi_{3,0}^*M_{\Omega_{3,0}}\Phi_{3,0}.
\end{aligned}
\]

Nach Expansion sollen exakt
\[
3^2+1^2+1^2=11
\]
`K* M_Omega K`-Wortterme entstehen.

Bitte prüfen:

- die drei Vorfaktoren;
- dass keine Cross-Terme zwischen verschiedenen `(p,j)`-Blöcken auftreten, weil der Full-Rest-Analyseraum orthogonal direkt summiert ist;
- dass innerhalb des `(2,0)`-Blocks alle 9 geordneten `k,l`-Paare enthalten sind.

Verdict:

```text
SE-2 RSTAR-R FINITE WORD FORM: GREEN / PARTIAL / FAIL
```

---

## F. Strategische Aussage

Der Kandidat behauptet **nicht**, dass der augmentierte Block bereits injektiv ist.
Er behauptet nur:

> Für die reine Schur-Kernfrage ist die nichtlokale Inverse `B` exakt eliminierbar. Der äquivalente augmentierte Operator enthält nur `I`, den drei-shiftigen Hub `H`, das finite `R*R` und Fensterrestriktionen. Im Drei-Shift-Fenster reduziert `R*R` sogar auf drei Martingaleblöcke bzw. 11 endliche Translation-/Cutoff-Wörter. Damit ist der echte post-P12-Schur-Kern prinzipiell wieder einer P12-artigen Rohoperatoranalyse zugänglich.

Bitte beurteilen, ob diese Aussage logisch exakt ist. Insbesondere nicht erlauben:

- `finite operator word` ⇒ `finite-dimensional operator`;
- `inverse eliminated` ⇒ `kernel solved`;
- `11 words` ⇒ irgendeine automatische Coercivity;
- Polar-Gauge-, Strong-Terminal-, Objekt-X- oder RH-Aussagen.

Verdict:

```text
SE ARCHITECTURAL SCOPE FIREWALL: GREEN / PARTIAL / FAIL
```

---

## G. Gewünschtes Gesamtverdict

```text
SE-1 BLOCK-KERNEL EQUIVALENCE:             GREEN / PARTIAL / FAIL
SE-1 INVERSE-FREE RANGE TRANSVERSALITY:    GREEN / PARTIAL / FAIL
SE-2 ACTIVE REST BLOCKS:                   GREEN / PARTIAL / FAIL
SE-2 EFFECTIVE K LISTS:                    GREEN / PARTIAL / FAIL
SE-2 RSTAR-R FINITE WORD FORM:             GREEN / PARTIAL / FAIL
SE ARCHITECTURAL SCOPE FIREWALL:           GREEN / PARTIAL / FAIL
SCHUR INVERSE-ELIMINATION OVERALL:         GREEN / PARTIAL / FAIL
```

Bei `PARTIAL` oder `FAIL` bitte die erste konkrete mathematische Abweichung nennen.

Bei vollständigem unabhängigem GREEN wäre als Kandidatenbuchung erlaubt:

- **SE-1:** `✓[M]` — exakte Schur-Kern/augmentierter-Block-Kern-Äquivalenz;
- **SE-2:** `✓[M]` — exakte Drei-Rest-Block-/11-Wort-Reduktion im Drei-Shift-Fenster.

Die Injektivität des augmentierten Blocks selbst bleibt `?[O]`.
