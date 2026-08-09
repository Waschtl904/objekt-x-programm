# P06 G-T3 — Targeted-Reaudit NEU-066

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Quellknoten:** `02-jacobi-limes/NEU-066_geschlossene_divisorpfade_trace_feshbach.md`  
**Korrekturquellen:** NEU-067–075, NEU-223–227, P05/F3-Endstand  
**Prüfart:** `TARGETED-REAUDIT`  
**Status:** **G-T3 COMPLETE — NEU-066 `INCORPORATED_part / NORMALIZATION-SUPERSEDED_part`**

---

## 0. Prüfauftrag

Geprüft wurde ausschließlich:

1. die geschlossene-Pfad-Interpretation von $\operatorname{Tr}(A_N^k)$;
2. der Nullspur- und Quadratikbefund;
3. die Bipartit-/ungerade-Spur-Aussagen;
4. die konkrete Matrixnormierung im Licht der späteren $J^-/S_N$-Konvention;
5. ob aus NEU-066 eine heutige diskrete Spektralaussage über $D_{\rm rel}$ importiert werden darf.

---

## 1. Geschlossene-Pfad-Prinzip — bleibt gültig im endlichen Matrixmodell

Für eine endliche Matrix $A_N$ gilt allgemein

$$
\operatorname{Tr}(A_N^k)
=
\sum_{a_0,\ldots,a_{k-1}}
(A_N)_{a_0a_{k-1}}(A_N)_{a_{k-1}a_{k-2}}\cdots(A_N)_{a_1a_0},
$$

also eine Summe über geschlossene $k$-Schritte im zugrunde liegenden gewichteten Graphen.

Dies ist unabhängig von der späteren Spektraltypkorrektur und bleibt ein gültiger endlicher algebraischer Befund.

**Status:** `✓[M]` im endlichen Matrix-/Graphmodell.

### Firewall

$$
\boxed{\text{endliche Trace-Pfadsumme}\neq\text{diskrete Eigenbasis des Grenzoperators }D_{\rm rel}.}
$$

NEU-227s Spektralmaß-Firewall wird dadurch nicht berührt.

---

## 2. $\operatorname{Tr}(A_N)=0$ — robust unter off-diagonaler Jacobi-Schließung

Für jede endliche Matrix ohne Diagonale gilt

$$
\operatorname{Tr}(A_N)=0.
$$

Dieser Teil von NEU-066 ist rein algebraisch und bleibt gültig, sofern $A_N$ tatsächlich die dort definierte off-diagonale endliche Jacobi-Matrix bezeichnet.

**Status:** `✓[M]`.

Er ist **keine** Aussage über eine regulierte Spur des unendlichen $D_{\rm rel}$.

---

## 3. Zweite Spur — Positivität/Quadratik robust, historische Koeffizientenform nicht kanonisch

Für eine endliche selbstadjungierte Matrix gilt

$$
\operatorname{Tr}(A_N^2)=\|A_N\|_{\rm HS}^2
=\sum_{a,b}|(A_N)_{ba}|^2\ge0.
$$

Damit ist die strukturelle Aussage robust:

$$
\boxed{\text{Die erste nichttriviale Schleifenschicht ist quadratisch in den Kantenamplituden.}}
$$

NEU-066 schreibt speziell

$$
\operatorname{Tr}(A_N^2)
=\sum_{a,n\mid m}r^2\log^2 n.
$$

Diese **exakte Normalisierungsform** wird für P06 nicht unverändert übernommen. Der Grund ist die spätere verbindliche Unterscheidung

$$
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger),
\qquad
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-.
$$

NEU-066 liegt im historischen Jacobi-$A_N^{\rm Jac,-}$-Strang und zählt Matrixelemente teilweise direkt über $\Theta$. Nach der J-/S-Bereinigung müssen Faktoren, Rückkantenkoeffizienten und Trunkierungsränder **aus der konkret verwendeten endlichen Matrix neu eingesetzt werden**.

Daher gilt für P06:

- $\operatorname{Tr}(A_N^2)=\|A_N\|_{HS}^2$: `✓[M]`;
- Quadratik in den Kantenamplituden: `✓[M]`;
- die unqualifizierte Formel mit exakt $\sum r^2\log^2 n$: `SUPERSEDED_part` als kanonische Normalisierung.

Dies ist eine Normierungs-/Typkorrektur, kein Widerruf des Schleifenmechanismus.

---

## 4. $\log(p^k)\neq\Lambda(p^k)$ — Korrektur bleibt vollständig gültig

Für $k>1$ gilt

$$
\log(p^k)=k\log p,
\qquad
\Lambda(p^k)=\log p.
$$

Daher erzeugt eine bloße Kantenamplitude $\log n$ auf Primzahlpotenzen noch **nicht** die primitive Mangoldt-Gewichtung. Insbesondere ist

$$
\log^2(p^k)=k^2\log^2p
\neq
\Lambda(p^k)^2=\log^2p
\qquad(k>1).
$$

**Status:** `✓[M]`.

Die spätere primitive-Orbit-/Möbius-Schicht NEU-067/068 ist genau deshalb ein eigener Mechanismus; NEU-066 darf ihn nicht vorwegnehmen.

---

## 5. Ungerade Spuren und Bipartitheit — korrigierter Graphsatz bleibt, Scope lokal

NEU-066 hat den früheren Fehler selbst korrigiert:

$$
\text{$r$-Gradierung allein}\not\Rightarrow
\operatorname{Tr}(A_N^{2j+1})=0.
$$

Bei symmetrischer Hin-/Rückkante können ungerade Zyklen auftreten. Für den Cayley-artigen Divisorgraphen mit Schrittmenge $S_m$ ist Bipartitheit eine zusätzliche arithmetische Bedingung; erst dann verschwinden die ungeraden geschlossenen Wege und damit die ungeraden Traces.

**Status:**

- „ungerade Spuren verschwinden wegen $r$-Gradierung“: `×[M]`;
- „bipartiter endlicher symmetrischer Graph ⇒ ungerade Spuren verschwinden“: `✓[M]`;
- konkrete Bipartitheit eines gegebenen zusammengesetzten $m$-Sektors: sektorabhängig.

NEU-227 bestätigt die Scope-Grenze: im Primsektor bleibt nur ein nichttrivialer Schritt und die Einzelkette ist kontrolliert; in zusammengesetzten Sektoren können mehrere Teilerkanäle $u$-Klassen mischen. `[O-225-3]` bleibt offen.

---

## 6. Nullstellensymmetrie — nur Konsistenzbeobachtung

Aus Bipartitheit folgt für eine endliche selbstadjungierte Adjazenz-/Jacobi-Matrix die Spektralsymmetrie

$$
\sigma(A_N)=-\sigma(A_N).
$$

Dass dies formal zur $\pm\gamma$-Symmetrie der nichttrivialen Zetastellen passt, ist lediglich eine **Konsistenzbeobachtung**. Daraus folgt weder eine Nullstellenidentifikation noch RH.

**Status:** `CONDITIONAL / heuristic interface`, kein P06-Satz über Zeta-Nullstellen.

---

## 7. Keine Übertragung der Pfadformel auf eine diskrete $D_{rel}$-Eigenbasis

NEU-066 ist eine endliche Trace-/Graphrechnung. Der heutige Spektralendstand lautet dagegen:

- $D_{\rm rel}$ besitzt in auditierten Primfasern Transportnormalform und rein absolutstetiges Spektrum;
- die historische diskrete Eigenbasisform von NEU-051 ist `SUPERSEDED`;
- Feshbach-Matrixelemente sind über Kreuzspektralmaße zu schreiben.

Daher ist unzulässig:

$$
\boxed{\text{endliche geschlossene Divisorpfade}
\Rightarrow
\text{diskrete Spektralzerlegung von }D_{\rm rel}.}
$$

Die Pfadexpansion gehört zur **endlichen Jacobi-/Determinantenschicht**, nicht zur Spektralzerlegung des Transportoperators.

---

## 8. P06-Endstand aus NEU-066

### Übernehmbar

- endliche Trace = geschlossene gewichtete Pfade `✓[M]`;
- Nullspur bei off-diagonaler endlicher Matrix `✓[M]`;
- zweite Spur = HS-Quadratik `✓[M]`;
- primitive Mangoldt-Gewichtung folgt nicht aus $\log n$ allein `✓[M]`;
- Bipartitheit, nicht bloße $r$-Gradierung, kontrolliert ungerade Schleifen `✓[M]`.

### Nicht unverändert übernehmen

- die historische exakte Koeffizienten-/Normalisierungsform von $\operatorname{Tr}(A_N^2)$ ohne J-/S-Reconciliation;
- Spektralsymmetrie als Zeta-Nullstellenidentifikation;
- endliche Pfadformeln als diskrete Eigenbasisform des Grenz-$D_{\rm rel}$.

---

## 9. Reconciliierte Statusmatrix

| Aussage | P06-Endstatus |
|---|---|
| geschlossene-Pfad-Traceformel, endliches $N$ | `✓[M]` |
| $\operatorname{Tr}(A_N)=0$ für off-diagonales $A_N$ | `✓[M]` |
| $\operatorname{Tr}(A_N^2)=\|A_N\|_{HS}^2$ | `✓[M]` |
| historische exakte $\sum r^2\log^2 n$-Normierung als kanonische P06-Form | `SUPERSEDED_part` |
| $\log(p^k)=\Lambda(p^k)$ für $k>1$ | `×[M]` |
| $r$-Gradierung ⇒ alle ungeraden Traces null | `×[M]` |
| Bipartitheit ⇒ ungerade Traces null | `✓[M]` |
| konkrete zusammengesetzte Sektoren global kontrolliert | `?[O]` (`[O-225-3]`) |
| bipartite Spektralsymmetrie identifiziert Zeta-Nullstellen | `?[O]` / nicht bewiesen |
| diskrete $D_{rel}$-Eigenbasis aus der Pfadexpansion | `SUPERSEDED / unzulässig` |

---

## 10. Endurteil G-T3

$$
\boxed{\text{NEU-066: TARGETED-REAUDIT COMPLETE.}}
$$

**Endstatus für P06:** `INCORPORATED_part / NORMALIZATION-SUPERSEDED_part`.

Die Graph-/Schleifenstruktur bleibt mathematisch brauchbar; die historische konkrete Matrixnormalisierung und jede diskrete Grenzspektrallesart werden nicht in P06 übernommen.
