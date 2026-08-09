# P09 / I3 — Pfadgebundener Gegencheck

**Datum:** 9. August 2026  
**Paket:** I3 — NEU-212–218  
**Bezug:** `AUDIT-2026-08-09_P09_I3_Koeffizientenmodule_Bimodul_Cup_Reconciliation.md`  
**Status:** `VALID — GEGENCHECK OHNE BEFUND — I3 SEALED`

---

## 1. Gegencheckfragen und Ergebnis

### 1. NEU-212 → NEU-216 — Zieltypbrücke

**BESTÄTIGT.** NEU-212 scheitert zentral an der Schwartz-Regularisierung: die geschriebene Konstruktion enthält nicht einmal die Einheit bzw. die Charaktere, und `G/log(nu+2)` fällt nur logarithmisch statt Schwartz-artig ab. NEU-216 repariert dies nicht durch einen nachträglichen Bimodul-Glättungsoperator, sondern durch direkte Konstruktion des logarithmischen Zieltyps `B^log/A^log`. Die Klasse

\[
[D_g^{\rm corr}]\neq0\in HH^1(A_{\rm alg},\mathcal A^{\log})_g
\]

ist belastbar. Der lokale gcd-Formelfehler mit einem fälschlichen `1/r`-Faktor zerstört die Konstruktion nicht.

### 2. NEU-214/215 — No-go-Reichweite

**BESTÄTIGT.** Der No-go betrifft normstetige globale `A_alg`-Bimoduloperatoren

\[
R:A_{C^*}\to \mathcal A^\infty\subsetneq A_{C^*}
\]

und erzwingt über

\[
\operatorname{Cent}_{A_{C^*}}(A_{\rm alg})=\mathbb C1
\]

den Nulloperator. NEU-216 ist davon nicht betroffen, weil dort kein solcher `R` konstruiert wird. Der Befund bleibt `P09-CORE-NOGO`.

### 3. NEU-217 — lokal/global

**BESTÄTIGT.** Die lokale HH1-Behauptung mit `M_{g,p}^log` ist nicht als vollständiger lokaler Koeffizientenbimodul typisiert. Die globale Konstruktion `M_glob^log` bzw. `\mathfrak M_glob^log` ist dagegen tragfähig und trägt `D_g^{corr}`. Die Korrektur in `(G1)` lautet erster Index `nk` statt `nk/delta`; sie beschädigt weder globale Schnittstabilität noch Nichtinnerheit.

### 4. NEU-218 — Følner-Argument und Cup

**BESTÄTIGT.** Kein konkreter Gegenbefund zum Mehrparameter-Følner-Test. Eine Darstellung

\[
G_q=\sum_{r\in R}(1-\sigma_r)F_r
\]

würde eine `O(N^3)`-Schranke für die Følner-Summen erzwingen, während die expliziten Testpunkte und die q-Teleskopierung

\[
\mathcal F_N(G_q)(x_N)\ge N^3(c_{J_N}-c_{K_N}),
\qquad c_{J_N}-c_{K_N}\to\infty
\]

liefern. Der partielle Modulquotient `M_H/C_{H;R}` genügt für Dualfunktional, Grad-4-Zyklus und nichtverschwindende Paarung. Der Vollquotient `M/[A,M]` bleibt offen und wird nicht benötigt.

Damit bleibt

\[
[D_g^{\rm corr}]\smile[\Theta^\wedge]\neq0
\in HH^4(A_{\rm alg},\mathfrak M_{\rm glob}^{\log})_g.
\]

### 5. Reichweite und NEU-219

**BESTÄTIGT.** Der I3-Befund beweist weder

\[
HH^4(A_{\rm alg},A_{\rm alg})_g\neq0
\]

noch eine zyklische, KMS-, Weil- oder Operatorrealisierung. NEU-219 rollt den Hochschild-Cup nicht zurück, sondern trifft erst die kanonische zyklische/Rotationsverfeinerung. Die spätere Bestandsaufnahme bestätigt die singuläre Route bis HH4 und lokalisiert die Blockade erst bei der Zyklizität.

---

## 2. Seal

Es liegt **kein konkreter Gegenbefund** zu den fünf atomaren I3-Fragen vor.

\[
\boxed{\text{P09 / I3 PASS A COMPLETE — GEGENCHECK OHNE BEFUND — SEALED}}
\]

**Seal-Regel:** Wiedereröffnung nur bei einem konkreten neuen mathematischen Gegenbefund; dann ausschließlich atomar am betroffenen Punkt.
