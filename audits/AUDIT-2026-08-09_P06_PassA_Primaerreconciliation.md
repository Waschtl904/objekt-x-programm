# P06 Pass-A — Primärreconciliation Jacobi–Feshbach + Divisorgraph

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Eröffnungsinventar:** `audits/AUDIT-2026-08-09_P06_PassA_Eroeffnung_Inventar.md`, Commit `4c18fb78`  
**Targeted-Reaudits:**
- G-T1 NEU-050: `fbff73d9`
- G-T2 NEU-062: `2b6cb2e8`
- G-T3 NEU-066: `d8746ea1`
- G-T4 NEU-090: `52197cdd`
- G-T5 NEU-089: `dd0fd3a3`

**Status dieses Blatts:**

$$
\boxed{\text{P06 PRIMARY RECONCILIATION COMPLETE — unabhängiger Gegencheck ausständig.}}
$$

Kein P06-SYN-Transfer vor gültigem Zweitcheck und finaler Pass-A-Versiegelung.

---

## 0. Verfahren und Scope

P06 wurde **nicht** als Vollneuaudit eröffnet. Der historische Ordner `02-jacobi-limes/` (NEU-058–090, 33 Knoten) war bereits vollständig auditiert. Zusätzlich gehören thematisch die historische Feshbach-Brücke NEU-040/045/046–056 sowie die spätere Korrekturschicht NEU-223–228 zum P06-Quellenkegel.

Pass-A-Regel:

$$
\text{bestehende Audits}
+
\text{spätere Korrekturen}
+
\text{gezielte Konfliktprüfung}
\longrightarrow
\text{heutiger P06-Endstand}.
$$

Ergebnis:

- `NEW-DIRECT-AUDIT`: **0**;
- initial erkannte `TARGETED-REAUDIT`: **4**;
- während G-T4 neu entdeckter konkreter Typ-/Normkonflikt NEU-089: **+1**;
- endgültig: **5 Targeted-Reaudits**.

---

## 1. Die fünf geschlossenen Konfliktpunkte

### 1.1 NEU-050 — kollektiver Birman–Schwinger-Operator

**Korrektur:** Die volle Blockarchitektur

$$
\mathcal K_N(z)=V_N^*(D_{\rm rel}-z)^{-1}V_N,
\qquad
K_{pq}(z)=V_p^*(D_{\rm rel}-z)^{-1}V_q
$$

bleibt formal korrekt unter den Typvoraussetzungen. Nicht bewiesen ist jedoch

$$
K_{pq}(z)\neq0\qquad\forall p\neq q.
$$

Verbindlich ist nur:

$$
\boxed{\text{Primkanalbilder können überlappen; Primblockdiagonalität ist nicht strukturell erzwungen.}}
$$

Kreuzblöcke können **generisch** nichtverschwinden. Mechanismus: Kanalbildüberlappung / Kreuzspektralmaß, nicht Primmischung durch $D_{\rm rel}$.

**Endstatus:** `INCORPORATED_part / RECONCILED`.

### 1.2 NEU-062 — Normalisierung und $J^-/S_N$-Typ

Historische Gleichsetzungen werden korrigiert zu

$$
J_N^-:=\frac12(\Theta_N-\Theta_N^\dagger),
\qquad
S_N:=\frac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-.
$$

$\gamma_N\equiv1$ ist eine zulässige Wahl **falls** $\gamma_N$ frei ist, aber kein bewiesener intrinsischer Struktursatz. „Weg B ist vollständig geschlossen“ ist durch die spätere Transportdiagnose `SUPERSEDED`.

**Endstatus:** `SUPERSEDED_part / INCORPORATED_part`.

### 1.3 NEU-066 — geschlossene Divisorpfade und Trace

Erhalten:

- endliche Trace = Summe geschlossener gewichteter Pfade;
- $\operatorname{Tr}(A_N)=0$ bei off-diagonaler endlicher Matrix;
- $\operatorname{Tr}(A_N^2)=\|A_N\|_{HS}^2$;
- $\log(p^k)\neq\Lambda(p^k)$ für $k>1$;
- Bipartitheit, nicht bloße $r$-Gradierung, ist das Kriterium für das Verschwinden ungerader Schleifen.

Nicht kanonisch übernommen wird die historische konkrete $\sum r^2\log^2n$-Normalisierung ohne erneutes Einsetzen der verbindlichen $J^-/S_N$-Konvention.

**Endstatus:** `INCORPORATED_part / NORMALIZATION-SUPERSEDED_part`.

### 1.4 NEU-090 — zweite relative Schleifenspur

Die historische uniforme Behauptung

$$
\sum_{n\le N-r}\frac{\Lambda(n)^2}{r+n}
\sim \frac12\log^2N
\quad\text{gleichmäßig bis }r=N/\log N
$$

ist falsch. Mit

$$
\sum_{n\le x}\Lambda(n)^2=O(x\log x)
$$

und einer Splitabschätzung bei $n=M=N/\log N$ folgt für festes zulässiges $z$:

$$
\boxed{
T_N(z)
=O_z\!\left(\frac{\log\log N}{\log N}\right)
\longrightarrow0.
}
$$

Damit:

$$
T_N(z)\not\to\gamma^2/2.
$$

**Endstatus:** historischer Hauptgrenzwert `×[M]`; korrigierter Nullgrenzwert `✓[M]` im NEU-088–90-Modellscope.

### 1.5 NEU-089 — während G-T4 entdeckter Zusatzkonflikt

Für komplexes $z$ ist

$$
C_N(z)=R_N(z)^{1/2}B_N^\Lambda R_N(z)^{1/2}
$$

im Allgemeinen nicht selbstadjungiert. Daher ist die historische Gleichsetzung

$$
\|C_N\|_{HS}^2=\operatorname{Tr}(C_N^2)
$$

unzulässig; korrekt ist

$$
\|C_N\|_{HS}^2=\operatorname{Tr}(C_N^*C_N).
$$

Die betragsweise Matrixabschätzung ergibt aber sogar

$$
\boxed{\|C_N(z)\|_{HS}^2
=O_z\!\left(\frac{\log\log N}{\log N}\right)\to0,}
$$

also $\|C_N(z)\|\to0$. Damit verschwinden alle festen Schleifenterme $k\ge2$. Im endlichen NEU-088–90-Modell folgt

$$
\boxed{D_N(z)\to1.}
$$

**Endstatus:** `SUPERSEDED_part / korrigierte HS-Kontrolle ✓[M]`.

---

## 2. Reconciliierter Endstand G1 — NEU-058–065

| Knoten | P06-Endrolle |
|---|---|
| NEU-058 | Skalen-/Normresolvent-No-Go `AUDIT-REUSED`; direkter Konfinierungsweg überholt |
| NEU-059 | Spektralmaß-/Jacobi-Grenzsprache `AUDIT-RECONCILED`; kein kanonischer HP-Endoperator |
| NEU-060 | Core-/Resolventenstabilität nur unter sauberer Grenzoperatorhypothese |
| NEU-061 | lokale Matrixstabilisierung technischer Baustein, keine automatische globale Konvergenz |
| NEU-062 | siehe G-T2 — `SUPERSEDED_part / INCORPORATED_part` |
| NEU-063 | Weyl-/Herglotz-Interface typisierbar; arithmetische Identifikation offen |
| NEU-064 | endliche Weyl-/Determinantenquotientenstruktur; globaler Grenzdivisor offen |
| NEU-065 | Feshbach-/Jacobi-Determinantenarchitektur; Hypothese $Z_N\to C\xi$ bleibt `?[O]`/äquivalent-nah |

**G1-Endurteil:** Die Weyl-/Resolventen-/Feshbachsprache bleibt; der direkte Jacobi-Limes als HP-Endoperator wird nicht migriert.

---

## 3. Reconciliierter Endstand G2 — NEU-066–076

Robuste mathematische Substanz:

- geschlossene Pfad-/Trace-Grammatik im endlichen Divisorgraphen;
- primitive Orbit-/Möbiusmechanismen NEU-067/068;
- primitive Zykluszerlegung NEU-069;
- negative Resultate zu naiver Ihara-/Periodisierungsroute NEU-070/071;
- BC-Zeit als strukturelle Quelle von $\log p$ NEU-072;
- $\Theta$-/BC-Derivationsbezug, aber strikt getrennt vom antisymmetrischen $J^-$ NEU-073–075;
- Faser-Symbol-No-Go NEU-076 als lokales Darstellungsresultat.

**Firewall:** Kein Knoten dieser Gruppe liefert eine diskrete Eigenbasis von $D_{\rm rel}$ oder eine bereits identifizierte Zeta-Nullstellenmenge.

---

## 4. Reconciliierter Endstand G3 — NEU-077–083

### Endliche Feshbach-Identität

Die endliche Feshbach-/Schur-Kollapsidentität aus NEU-077 bleibt algebraisch gültig.

$$
\boxed{\text{endliche Identität}\neq\text{Schattennorm-kontrollierter globaler Limes}.}
$$

### Skalierung

NEU-078–083 zeigen einen realen Strukturkonflikt zwischen:

- stabiler Feshbach-Gesamtkopplung,
- gleichmäßig kontrollierten Jacobi-Gewichten,
- echter Mangoldt-Gewichtung.

Auf dem vollen Fenster $r\le N$ sind diese Forderungen nicht frei gleichzeitig erfüllbar. Die Orbittrunkierung $N/\log N$ war ein pathwise Kandidat, löst aber nicht automatisch die $\ell^2$-Operatornormfrage.

**G3-Endurteil:** Endliche Feshbach-Grammatik `✓[M]`; globale Skalierung/Schattenrealisierung `?[O]`.

---

## 5. Reconciliierter Endstand G4 — NEU-084–090

### Zwei verschiedene Trunkierungsskalen

NEU-084 trennt verbindlich:

$$
M_N^{\rm path}\lesssim \frac{N}{\log N}
$$

von

$$
M_N^{\rm op}\lesssim\sqrt{\frac{N}{\log N}}.
$$

### Vorwärtsshift versus Jacobi-Schließung

- starker Mangoldt-Vorwärtsshift kollabiert auf festen Vektoren;
- reiner Vorwärtsshift ist nilpotent und für Spur/Determinante trivial;
- die selbstadjungierte Jacobi-Schließung erzeugt Rückkanten und nichttriviale endliche Schleifen.

### Relative Determinante

NEU-088s endliche relative Resolventdeterminante und zweite Schleifenformel bleiben als Modellformeln brauchbar. Nach den Korrekturen G-T4/G-T5 gilt auf der pathwise Skala jedoch

$$
\|C_N(z)\|_{HS}\to0,
\qquad
T_N(z)\to0,
\qquad
D_N(z)\to1.
$$

Damit kollabiert die konkrete NEU-088–90-Schleifendeterminante im auditierten Modell auf die triviale Konstante und liefert keinen direkten $\xi$-Grenzwert.

**Scope:** Dies ist kein No-Go gegen andere renormierte Feshbach-/Fredholmdeterminanten.

---

## 6. Ordnerübergreifende Feshbach-Brücke GX1

### Formal erhalten

- NEU-040: Schurkomplementidentität unter typisierten Blöcken;
- NEU-045: relative Feshbach-/Euler-Unterdeterminantenstruktur;
- NEU-046: zyklische Weyl-/Stieltjesfunktion als Resolventenmatrixelement;
- NEU-049: Birman–Schwinger-/Fredholmindex formal unter Spur-/Holomorphievoraussetzungen;
- NEU-050: kollektive Blockarchitektur, nach G-T1 präzisiert.

### Später superseded/reconciliert

- NEU-051s diskrete Eigenbasisformeln (51.3)/(51.4)/(51.7) werden nicht übernommen;
- NEU-052: Graphbasis ≠ Eigenbasis;
- NEU-053–056: Selbstadjungiertheit, Nelson und Konfinement getrennt; skalare Konfinementroute nicht P06-Endziel.

---

## 7. Superseding-Schicht GX2 — NEU-223–228

### Verbindlicher Spektralendstand

In den auditierten Primfasern:

$$
D_{\rm rel}\big|_{\mathcal H_{p,a}}
\cong
2i\kappa_p^{\rm tr}\frac d{dt},
$$

rein absolutstetiges Spektrum, kein Kern, kein kompakter reduzierter Resolvent.

### Verbindliche Spektralmaßform

$$
\mu_{pq}^{a,b}(B)
:=\langle V_pa,E_D(B)V_qb\rangle,
$$

$$
\boxed{
\langle a,K_{pq}(z)b\rangle
=
\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.
}
$$

### Schattenfirewall

- festes $N$ bedeutet nicht endlicher Rang;
- endliche Feshbachidentitäten kontrollieren keine Schattennorm des Grenzoperators;
- $V\notin\mathcal S_2$ ist nur notwendig für den vorgeschlagenen Nicht-$\mathcal S_1$-Zeugenmechanismus;
- $V\in\mathcal S_4$ bleibt strukturelle Arbeitshypothese/offen.

### $u$-Regulator

NEU-228 korrigiert die frühere Lesart:

$$
\boxed{u\text{-Regulator}=\text{Hebungswahl auf der Primfaser},}
$$

kein frei justierbarer Schattenparameter.

---

## 8. P06/P11-Sperrvermerk

NEU-228b/229 zeigen:

- die normierte Liftfaser und ihr Gramblock sind nur partiell konstruiert;
- der intrinsische Mischblock $\beta_p$ fehlt im aktuellen Quellenbestand (`✓[M]_{neg,Quelle}`);
- Hebungsunabhängigkeit und intrinsische Feshbach-Wohldefiniertheit bleiben offen;
- **keine Schattenklassenrechnung vor Abschluss der Lift-/Gramblockfrage.**

P06 darf deshalb die Operatorarchitektur

$$
K(z)=V^*(D_{\rm rel}-z)^{-1}V
$$

typisieren und konditionale Kriterien formulieren, aber die intrinsische globale Quelle nicht voraussetzen.

**Routing:** Lift-/Gram-/Mischblock-/globale Kopplungsgeometrie → P11.

---

## 9. Verbindliche P06-Firewalls nach Primärreconciliation

1. $J_N^-\neq S_N$; verbindlich $J_N^-=\frac12(\Theta-\Theta^\dagger)$ und $S_N=-iJ_N^-$.
2. Direkter Jacobi-Limes ist nicht der HP-Endoperator; $D_{\rm rel}$ ist in auditierten Primfasern Transportgenerator.
3. Diskrete NEU-051-Eigenbasisformeln sind `SUPERSEDED`; Kreuzspektralmaße sind verbindlich.
4. Primblockdiagonalität ist nicht strukturell erzwungen; $K_{pq}\neq0$ aber nicht für jedes Paar bewiesen.
5. Off-Diagonalität entsteht aus Kanalbildüberlappung, nicht notwendigerweise aus Primmischung durch $D_{\rm rel}$.
6. Festes $N$ impliziert keinen endlichen Rang von $K_N$.
7. Endliche Feshbachidentität impliziert keine Schattennormkonvergenz.
8. $u$ ist Liftkoordinate/Hebungswahl, kein frei wählbarer Regulator.
9. Schatten-/Fredholmrealisierung ist bis zur intrinsischen Lift-/Gramgeometrie blockiert.
10. Zusammengesetzte $m$-Sektoren bleiben `[O-225-3]` offen.
11. $Z_N\to C\xi$ und entsprechende Divisoridentifikation bleiben `?[O]` / `CONDITIONAL`.
12. NEU-066s Graphtrace ist endliche Matrixgeometrie, keine diskrete Spektralzerlegung von $D_{\rm rel}$.
13. NEU-089s Selbstadjungiertheitsbehauptung für $C_N(z)$ bei komplexem $z$ ist `×[M]`.
14. Im konkreten NEU-088–90-Scaling gilt $T_N(z)\to0$ und $D_N(z)\to1$, nicht $\gamma^2/2$ bzw. $e^{-\gamma^2/4}$.
15. Dieser Determinantenkollaps ist **modell-/skalenspezifisch** und kein globaler Feshbach-No-Go für Objekt X.

---

## 10. Endstatus der Primärprüfung

$$
\boxed{\text{P06 PRIMARY RECONCILIATION COMPLETE.}}
$$

### Buchhaltung

- Ordner 02: **33/33** Knoten erfasst.
- Historische Feshbach-Brücke NEU-040/045/046–056 erfasst.
- Superseding-Schicht NEU-223–228 erfasst.
- P06/P11-Grenze NEU-228b/229 gebucht.
- `NEW-DIRECT-AUDIT`: **0**.
- `TARGETED-REAUDIT`: **5**, alle abgeschlossen.
- Neu entdeckter Konflikt: NEU-089, während G-T4 isoliert und als G-T5 geschlossen.

### Noch nicht zulässig

$$
\boxed{\text{P06 PASS A COMPLETE}}
$$

wird **noch nicht** gesetzt. Zuerst ist ein unabhängiger pfadgebundener Gegencheck der Primärreconciliation erforderlich.

Ebenso bleibt P06-SYN bis zur Versiegelung gesperrt.
