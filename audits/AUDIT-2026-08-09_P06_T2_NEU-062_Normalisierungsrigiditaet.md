# P06 G-T2 — Targeted-Reaudit NEU-062

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Quellknoten:** `02-jacobi-limes/NEU-062_normalisierungsrigiditat_jacobi_limes.md`  
**Korrekturquellen:** NEU-223–225, NEU-226/227, P05/F3-Endstand  
**Prüfart:** `TARGETED-REAUDIT`  
**Status:** **G-T2 COMPLETE — NEU-062 `SUPERSEDED_part / INCORPORATED_part`**

---

## 0. Prüfauftrag

Geprüft wurde ausschließlich:

1. die historische Fallunterscheidung für $\gamma_N$;
2. die Behauptung, $\gamma_N\equiv1$ könne bzw. müsse den Jacobi-Limes schließen;
3. die in NEU-062 benutzte Antisymmetrisierungsnormierung;
4. die Aussage „Weg B ist analytisch vollständig“ im Licht von NEU-223–225.

---

## 1. Abstrakte $\gamma_N$-Fallunterscheidung — nur als konditionale Skalenaussage erhalten

NEU-062 unterscheidet formal:

- $\gamma_N\equiv1$ bzw. $\gamma_N\to\gamma_\infty>0$;
- $\gamma_N\to0$;
- oszillierendes/divergierendes $\gamma_N$.

Als **abstrakte Aussage über eine bereits typisierte Familie**, deren lokale Matrixkoeffizienten bis auf den skalaren Faktor $\gamma_N$ stabilisieren, ist diese Fallunterscheidung mathematisch sinnvoll:

$$
\gamma_N\to\gamma_\infty>0
\quad\Rightarrow\quad
\text{lokal derselbe Grenzoperator bis auf den Faktor }\gamma_\infty,
$$

während $\gamma_N\to0$ auf dem kontrollierten festen Core zu einem kollabierenden skalierten Anteil führt.

P06 übernimmt daraus **keinen globalen Operatorgrenzwert ohne zusätzliche Core-/Domänenannahmen**.

**Status:** `✓[M]_part / CONDITIONAL` auf die vorausgesetzte typisierte Familie und Core-Konvergenz.

---

## 2. Hauptkorrektur — NEU-062 verwendet nicht die verbindliche $J_N^-$-Konvention

NEU-062 führt in seinem Szenario I die historische Schreibweise

$$
\frac1{2i}\bigl(\Theta_N-\Theta_N^{\mathrm{Wres}}\bigr)
$$

als $J_N^-$-artige Grunddefinition.

NEU-225 bereinigt dies verbindlich:

$$
\boxed{J_N^-:=\frac12\bigl(\Theta_N-\Theta_N^\dagger\bigr),
\qquad (J_N^-)^*=-J_N^-.}
$$

Der selbstadjungierte Operator

$$
\boxed{S_N:=\frac1{2i}\bigl(\Theta_N-\Theta_N^\dagger\bigr)=-iJ_N^-}
$$

ist **nicht dasselbe Objekt** wie $J_N^-$. Erst

$$
D_{\rm rel}=\overline{iJ^-}
$$

ist die selbstadjungierte relative Transportrealisierung.

Damit ist jede Passage in NEU-062, die $\frac1{2i}(\Theta-\Theta^{Wres})$ ohne Typtrennung als $J^-$ führt, für P06 `SUPERSEDED`.

**Status:** `✓[M]_neg` gegen die historische Gleichsetzung; NEU-225-Konvention verbindlich.

---

## 3. $\gamma_N\equiv1$ — zulässige Modellwahl ist kein struktureller Satz

NEU-062 Satz 62.1 lautet sinngemäß:

> Falls $\gamma_N$ frei wählbar ist, kann man $\gamma_N\equiv1$ setzen.

Diese Implikation ist tautologisch korrekt **unter ihrer Voraussetzung**. Der spätere Text geht jedoch weiter und empfiehlt $\gamma_N\equiv1$ als strukturelle Normalisierung bzw. erklärt sie im intrinsischen Szenario für erzwungen.

Für den heutigen P06-Endstand gilt nur:

$$
\boxed{\gamma_N\equiv1\ \text{ist eine mögliche Normalisierung, falls }\gamma_N\text{ tatsächlich frei ist}.}
$$

Nicht bewiesen ist:

$$
\boxed{\text{Die intrinsische Objekt-X-/Feshbach-Architektur erzwingt }\gamma_N\equiv1.}
$$

Insbesondere zeigen die späteren Feshbach-Knoten zusätzliche Normierungsfaktoren und unterscheiden endliche Trunkierungsidentitäten von einem globalen Limes. Eine Wahl von $\gamma_N$ darf daher nicht benutzt werden, um die fehlende intrinsische Kopplungs-/Liftgeometrie zu ersetzen.

**Status:** Wahl unter Voraussetzung `✓[M]`; strukturelle Erzwingung `?[O]`.

---

## 4. „Weg B ist analytisch vollständig“ — als heutiger Endstatus zu stark

NEU-062 folgert bei $\gamma_N\equiv1$, die Kette NEU-58–61 und „Weg B“ sei analytisch geschlossen und nur die arithmetische Spektralidentifikation bleibe offen.

Diese Formulierung ist durch spätere Ergebnisse überholt:

1. NEU-223 trennt Selbstadjungiertheit, Konfinement und Spektraltyp strikt.
2. NEU-225 identifiziert $D_{\rm rel}$ in auditierten Primfasern als Transportgenerator mit rein absolutstetigem Spektrum und ohne kompakten Resolventen.
3. Damit ist der direkte Jacobi-/Transportoperator **nicht** der HP-Endoperator.
4. Die neue P06-Hauptlinie liegt eine Schicht später beim Feshbach-/Birman–Schwinger-Transfer
   $$K(z)=V^*(D_{\rm rel}-z)^{-1}V,$$
   dessen Schattenklasse, intrinsische Wohldefiniertheit und Determinantenidentität offen sind.

Daher lautet der heutige Endsatz:

$$
\boxed{\text{Die Spektralmaßform von }D_{\rm rel}\text{ ist tragfähig;}
\quad\text{der P06-Feshbach-Limes ist dadurch nicht geschlossen.}}
$$

**Status:** alte Abschlussbehauptung `SUPERSEDED`; Spektralmaß-Interface `INCORPORATED`.

---

## 5. Kollaps bei $\gamma_N\to0$ — Scope präzisieren

Die historische Zeile „$\gamma_N\to0\Rightarrow D_{\rm rel}=0$“ darf nicht als allgemeiner Satz über beliebige bewegte Domänen oder renormierte Grenzoperatoren gelesen werden.

Gesichert ist im historischen lokalen Stabilisierungsschema:

$$
\gamma_N\to0
\quad\Longrightarrow\quad
\text{die mit }\gamma_N\text{ multiplizierten festen Matrixkoeffizienten kollabieren auf dem festen Core.}
$$

Ein globaler starker/normresolventer Schluss benötigt zusätzliche Grenzannahmen.

**Status:** `✓[M]_part / CONDITIONAL`, nicht unbedingter globaler Nulloperatorsatz.

---

## 6. Was aus NEU-062 nach P06 übernommen wird

### Übernehmbar

- Normalisierung und Grenzoperator müssen getrennt bilanziert werden.
- Eine $N$-abhängige Skalierung kann einen nichttrivialen lokalen Grenzoperator zerstören.
- Ein positiver Grenzwert von $\gamma_N$ erhält im lokal stabilisierten Modell den Operator bis auf Skala.
- Externe Normalisierung darf nicht stillschweigend als frei behandelt werden.

### Nicht übernehmen

- $\frac1{2i}(\Theta-\Theta^{Wres})$ als verbindliches $J^-$;
- „$\gamma_N=1$ ist strukturell erzwungen“;
- „Weg B ist vollständig geschlossen“ als heutiger P06-Endstand;
- „$\gamma_N\to0$ beweist global $D_{\rm rel}=0$“ ohne Grenzoperatorhypothesen.

---

## 7. Reconciliierte Statusmatrix

| Aussage | P06-Endstatus |
|---|---|
| abstrakte $\gamma_N$-Fallunterscheidung | `✓[M]_part / CONDITIONAL` |
| $\gamma_N\equiv1$ bei frei wählbarem Parameter | `✓[M]` als Wahl unter Voraussetzung |
| intrinsische Erzwingung $\gamma_N\equiv1$ | `?[O]` |
| historische $\frac1{2i}(\Theta-\Theta^{Wres})=J^-$-Lesart | `SUPERSEDED / ✓[M]_neg` |
| $J_N^-=\frac12(\Theta_N-\Theta_N^\dagger)$ | `✓[M]` verbindliche Konvention |
| $S_N=-iJ_N^-$, $D_{rel}=\overline{iJ^-}$ | `✓[M]` verbindliche Typtrennung |
| Spektralmaßform als robuste Sprache | `✓[K/M]` |
| direkter Jacobi-/Transportweg als P06-Endoperator geschlossen | `SUPERSEDED` |
| Feshbach-Transfer $K(z)$ dadurch vollständig konstruiert | `?[O]` |

---

## 8. Endurteil G-T2

$$
\boxed{\text{NEU-062: TARGETED-REAUDIT COMPLETE.}}
$$

**Endstatus für P06:** `SUPERSEDED_part / INCORPORATED_part`.

Der mathematisch brauchbare Kern ist die Normalisierungs-Fallunterscheidung. Die historische Operatorbezeichnung und die Schlussfolgerung einer vollständig geschlossenen direkten Jacobi-Schicht werden nicht in P06 übernommen.
