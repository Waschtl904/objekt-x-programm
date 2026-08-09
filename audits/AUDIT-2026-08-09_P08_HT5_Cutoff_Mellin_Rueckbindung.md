# P08 Pass A — H-T5 Cutoff, Mellin, Restkontrolle und Rückbindung

**Datum:** 9. August 2026  
**Scope:** NEU-146–150. H-T4 sowie die P05/P06-Firewalls sind bindend.

## Endstatus

\[
\boxed{\text{H-T5 COMPLETE — analytischer Mangoldt-Mellin-Kern rettbar; Prime-only Mellin-Identität falsch; operatorielle Rückbindung bleibt conditional/offen.}}
\]

Keine H-T5-Reaudits bleiben offen. Die historischen Hochstufungen werden auf den folgenden Stand zurückgesetzt.

## 1. Bindender Eingang aus H-T4

- Intrinsisches T2 / Primorthogonalität: `?[O]`.
- Nichtentartung `c_p != 0` für alle p: `?[O]`.
- Primdiagonales Mangoldt-`R`: `?[O]/CONDITIONAL`.
- `Sigma_rel^ren(beta) in S_1`: `CONDITIONAL ✓[M]_{model}`.
- `Tr_reg := AC[-zeta'/zeta]`: `✓[def]`, keine operatorielle Herleitung.

Daher sind alle Operatorformulierungen in NEU-146–150, die `R`, `P_pP_q=0` oder eine Primdiagonalisierung verwenden, mindestens conditional.

## 2. NEU-146 — scharfer Primcutoff

Die Schichtzerlegung

\[
S_X(\beta)=\sum_{p\le X}\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}
=\sum_{k\ge1}T_k(X,\beta),\qquad
T_k(X,\beta)=\sum_{p\le X}\log p\,p^{-k\beta}
\]

ist exakt.

Für festes `s=k beta` mit `Re s<1` liefert partielle Summation aus `theta(X)~X` den Hauptterm

\[
T_k(X,\beta)\sim \frac{X^{1-k\beta}}{1-k\beta}.
\]

Am Rand `Re(k beta)=1`, `k beta !=1` ist der Hauptterm beschränkt oszillierend und hat im Allgemeinen keinen Grenzwert; NEU-147 korrigiert dies.

Lokaler Fehler in NEU-146: Die Aussage, bei `k beta in Z` trete logarithmische Divergenz auf, ist zu weit. Der logarithmische Sonderfall ist `k beta=1`.

Die Trennung zwischen Primcutoff und `R`-Cutoff ist richtig. Aus

\[
R_p\gtrsim p/\log p
\]

folgt keine asymptotische Äquivalenz. Die Zusatzannahme

\[
[ZA]:\quad R_p\asymp p/\log p
\]

bleibt `?[O]` und reicht später für eine Identität von Finite Parts noch nicht automatisch aus.

**Status NEU-146:** Schichtzerlegung `✓[M]`; PNT-Hauptterm `✓[M]`; Operatorursprung `CONDITIONAL`; [ZA] `?[O]`; Finite-Part-Ziel `?[O]`.

## 3. NEU-147 — Prime-only vs. Mangoldt

Die Randfallkorrektur in §147.1 ist richtig.

Der zentrale Fehler beginnt in §147.2: `T_k(X,beta)` ist eine Primzahl-Summe über

\[
\vartheta(X)=\sum_{p\le X}\log p,
\]

während die verwendete Riemann-von-Mangoldt-Formel die Mangoldt-Summe

\[
\psi(X)=\sum_{p^j\le X}\log p
\]

beschreibt.

Der Übergang `psi -> theta` verlangt Primpotenz-/Möbiuskorrekturen. Schematisch führt

\[
\vartheta(X)=\sum_{j\ge1}\mu(j)\,\psi(X^{1/j})
\]

zu zusätzlichen Exponenten `rho/j`, also nicht nur zu den in NEU-147 notierten Termen `X^{rho-k beta}`.

Daher sind die Aussagen

- „der Defekt ist genau die Summe der `X^{rho-k beta}`-Terme“,
- der daraus direkt formulierte vollständige explizite Finite-Part,
- und der angegebene RH-Äquivalenzbeweis

in dieser Form nicht bewiesen.

Weiterer lokaler Fehler: Für `Re beta>0`, `k>=1`, `n>=1` gilt

\[
\Re(-2n-k\beta)<0.
\]

Triviale Nullstellen können daher in diesem Bereich nicht als wachsende/oszillierende Terme mit `Re(-2n-k beta)>=0` auftreten.

Die RH-Idee bleibt als Richtungsstruktur interessant: Im Halbstrip `1/2<Re beta<1` ist die Existenz von Nullstellen rechts von `1/2` genau die Art zusätzlicher Nullstellenbeiträge, die eine reine Hauptpolsubtraktion stören kann. Ein Äquivalenzsatz verlangt aber eine korrekt typisierte explizite Formel und Nichtauslöschung der betreffenden Koeffizienten.

**Status NEU-147:** Randfall `✓[M]`; direkte Prime-only-Explizitformel `×[M]`; RH-Richtungsstruktur `✓[M]_part`; vollständige Äquivalenz `?[O]`.

## 4. NEU-148 — zentraler Mellin-Typfehler

Live ist definiert

\[
S_{\varphi,X}(\beta)
=\sum_p\varphi(p/X)\frac{\log p\,p^{-\beta}}{1-p^{-\beta}}
=\sum_{p,k\ge1}\varphi(p/X)\log p\,p^{-k\beta}.
\]

Mellin-Inversion von `phi(p/X)` ergibt

\[
S_{\varphi,X}(\beta)
=\frac1{2\pi i}\int_{(c)}\widehat\varphi(s)X^s
\left(\sum_{p,k\ge1}\log p\,p^{-k\beta-s}\right)ds.
\]

Der innere Ausdruck ist **nicht**

\[
-\frac{\zeta'}{\zeta}(\beta+s)
=\sum_{p,k\ge1}\log p\,p^{-k\beta-ks}.
\]

Damit ist NEU-148.A in der Live-Fassung

\[
\boxed{\times[M].}
\]

### Korrektes analytisches Objekt

Definiere stattdessen die geglättete Mangoldt-Summe

\[
\Psi_{\varphi,X}(\beta)
:=\sum_{n\ge1}\Lambda(n)\varphi(n/X)n^{-\beta}
=\sum_{p,k\ge1}\log p\,\varphi(p^k/X)p^{-k\beta}.
\]

Dann gilt für `c>1-Re beta` exakt

\[
\boxed{
\Psi_{\varphi,X}(\beta)
=\frac1{2\pi i}\int_{(c)}\widehat\varphi(s)X^s
\left(-\frac{\zeta'}{\zeta}(\beta+s)\right)ds.
}
\]

Das ist der rettbare Mellin-Kern von H-T5.

### Mellin-Pol bei s=0

Für `phi in C_c^infty([0,infty))` mit `phi=1` nahe 0 ist `hat phi` nicht ganz. Sie besitzt bei `s=0` einen einfachen Pol mit

\[
\operatorname{Res}_{s=0}\widehat\varphi(s)=1.
\]

Daher sind NEU-148s Aussagen „`hat phi` ganz“ und „`hat phi(0)=1`“ `×[M]`. NEU-149 korrigiert diesen Punkt richtig.

### Korrekte Prime-power-Differenz

NEU-148 §148.6 schreibt die Differenz von `Psi` und `S` falsch. Richtig ist

\[
\boxed{
\Psi_{\varphi,X}(\beta)-S_{\varphi,X}(\beta)
=\sum_{k\ge2}\sum_p \log p\,
\bigl[\varphi(p^k/X)-\varphi(p/X)\bigr]p^{-k\beta}.
}
\]

Für `Re beta>1/2` ist die höhere-Primpotenz-Reihe absolut summierbar. Damit ist ein Transfer `Psi-S ->0` per dominierter Konvergenz plausibel; eine quantitative Rate wie `O(X^{1/2-Re beta})` benötigt einen eigenen Beweis.

**Status NEU-148:** Setup des korrekten `Psi`-Strangs `✓[M]`; Live-Mellin-Identität für `S` `×[M]`; Mellin-Pol-Korrektur durch NEU-149 `✓[M]`; `Psi/S`-Transfer `?[O]` quantitativ.

## 5. NEU-149 — Restkontrolle

Positiv: Die Korrektur

\[
\operatorname{Res}_{s=0}\widehat\varphi(s)=1
\]

ist richtig und liefert im **korrigierten `Psi`-Mellin-Strang** den Term

\[
-\zeta'(\beta)/\zeta(\beta)
\]

aus dem Mellin-Pol bei `s=0`.

Auf einer fest gewählten linken Kontur mit `Re s<=-M`, die von allen relevanten Polen quantitativ getrennt bleibt, ist die Grundabschätzung

\[
|X^s|\le X^{-M}
\]

richtig; zusammen mit vertikalem Mellin-Abfall und einer geeigneten Schranke für `zeta'/zeta` ergibt dies conditional einen `O(X^{-M})`-Rest.

Aber die Live-Konstruktion ist noch nicht vollständig:

1. Für variierendes `beta in K` ist die Menge `{omega-beta}` nicht diskret; sie enthält wegen des kontinuierlichen `K` verschobene Mengen. Die behauptete Diskretheit ist falsch.
2. Eine **einheitliche** nullstellenvermeidende Kontur mit uniformem Abstand für alle `beta in K` wird nicht bewiesen.
3. Die vollständige Residuenzählung beim Grenzübergang in der Konturhöhe bleibt offen.
4. Vor allem gilt die Rechnung direkt für `Psi`, nicht für das falsch typisierte `S` aus NEU-148.A.

Daher schließt NEU-149 `[O-148-1]` für `S` nicht.

**Status NEU-149:** Mellin-Pol-Korrektur `✓[M]`; fixed-contour Restlemma für den korrigierten `Psi`-Strang `CONDITIONAL ✓[M]`; uniformer Kontur-/Residuenabschluss `?[O]`; Abschluss für `S` `×[M]` als behauptete direkte Folgerung.

## 6. NEU-150 — Operatorielle Rückbindung

Die Definition

\[
N_{\mathbb P}\Psi_p=p\Psi_p
\]

ist nur dann als Multiplikationsoperator auf dem tatsächlichen Zielraum wohldefiniert, wenn

- die Primkanäle intrinsisch getrennt sind (T2 oder äquivalente direkte Summenstruktur),
- die relevanten `Psi_p` nicht verschwinden,
- und das orthogonale Komplement sowie die maximale Domäne festgelegt werden.

NEU-150 behandelt diese Voraussetzungen als geschlossen; nach H-T4 sind sie offen/conditional.

Für eine nicht normierte orthogonale Familie ist die natürliche Domänenbedingung

\[
\sum_p p^2|\xi_p|^2\|\Psi_p\|^2<\infty,
\]

nicht die Live-Formel ohne `||Psi_p||^2`.

Die formale Identität

\[
\operatorname{Tr}(\varphi(N_{\mathbb P}/X)R\Sigma)=S_{\varphi,X}
\]

ist im primdiagonalen Modell algebraisch richtig, aber conditional auf die obigen Operatorvoraussetzungen.

Die Hochstufungen

- Primlabel-Finite-Part `= -zeta'/zeta`,
- `Tr_reg =` Primlabel-Finite-Part,
- operatorielle Realisierung der NEU-145-Definition

sind nicht bewiesen, weil sie NEU-148.A/149 in der falschen `S`-Typisierung importieren.

### R-Cutoff

Auch [ZA] `R_p asymp p/log p` allein identifiziert Finite Parts nicht. Asymptotische Vergleichbarkeit der Cutoff-Mengen kontrolliert nicht automatisch die konstanten/oscillatorischen Finite-Part-Terme. Für einen Transfer `N_P`-Cutoff -> `R`-Cutoff ist eine quantitativ stärkere Asymptotik samt Fehlerkontrolle nötig.

**Status NEU-150:** Primlabel-Observable `CONDITIONAL`; formale Spuridentität `CONDITIONAL ✓[M]_{model}`; Primlabel-Finite-Part `?[O]`; Gleichheit mit `Tr_reg` `?[O]`; R-Cutoff-Transfer `?[O]` und stärker als [ZA].

## 7. Reparierte H-T5-Kette

Der tragfähige analytische Weg lautet:

\[
\boxed{
\Psi_{\varphi,X}(\beta)
=\sum_n\Lambda(n)\varphi(n/X)n^{-\beta}
\xrightarrow{\mathrm{Mellin}}
\widehat\varphi(s)X^s\left(-\zeta'/\zeta(\beta+s)\right)
}
\]

mit

\[
\operatorname{Res}_{s=0}\widehat\varphi(s)=1.
\]

Dann sind getrennt zu beweisen:

1. nullstellenvermeidende Kontur + vollständige Residuenzählung für `Psi`;
2. für `Re beta>1/2` der korrekte Primpotenztransfer `Psi-S ->0`;
3. erst danach eine Primlabel-Operatorrealisierung;
4. anschließend, falls gewünscht, ein eigener Transfer vom Primlabel-Cutoff zum `R`-Cutoff.

Keine dieser Stufen darf durch `Tr_reg := AC[-zeta'/zeta]` ersetzt werden; diese bleibt nur `✓[def]`.

## 8. Statusmatrix

| Punkt | Endstatus |
|---|---|
| NEU-146 Schichtzerlegung | `✓[M]` |
| PNT-Hauptterm `Re(k beta)<1` | `✓[M]` |
| Log-Sonderfall für alle `k beta in Z` | `×[M]` |
| [ZA] `R_p asymp p/log p` | `?[O]` |
| NEU-147 Randfallkorrektur | `✓[M]` |
| direkte Prime-only-Explizitformel | `×[M]` |
| RH-Richtungsstruktur | `✓[M]_part` |
| NEU-148 Mellin-Identität für `S` | `×[M]` |
| korrekte Mellin-Identität für `Psi` | `✓[M]` |
| `hat phi` ganz / `hat phi(0)=1` | `×[M]` |
| `Res_{s=0} hat phi=1` | `✓[M]` |
| Live-`Psi/S`-Differenzformel | `×[M]` |
| `Psi/S`-Transfer für `Re beta>1/2` | `?[O]` quantitativ |
| NEU-149 fixed-contour Restlemma für `Psi` | `CONDITIONAL ✓[M]` |
| uniforme Kontur + vollständige Residuen | `?[O]` |
| NEU-150 Primlabel-Observable | `CONDITIONAL` |
| Primlabel-Spuridentität | `CONDITIONAL ✓[M]_{model}` |
| Primlabel-Finite-Part `= -zeta'/zeta` | `?[O]` |
| operatorielle Realisierung von `Tr_reg` | `?[O]` |
| R-Cutoff-Transfer | `?[O]`, benötigt mehr als [ZA] |

## 9. Firewalls für P08-Sealing und SYN-Migration

1. **Mellin-Typ:** `phi(p/X)` darf nicht mit `-zeta'/zeta(beta+s)` gekoppelt werden. Der exakte Zeta-Mellin-Kanal trägt `phi(p^k/X)` bzw. `phi(n/X)` mit `Lambda(n)`.
2. **Mellin-Pol:** Bei Cutoffs, die 1 nahe 0 sind, ist `hat phi` meromorph mit Residuum 1 bei 0; `hat phi(0)` ist kein endlicher Normierungswert.
3. **Prime-only-Explizitformel:** `theta` und `psi` nicht identifizieren; Primpotenz-/Möbiuskorrekturen müssen explizit getragen werden.
4. **Operatorbrücke:** `N_P`, `R`, T2 und `c_p!=0` bleiben conditional/intrinsisch offen.
5. **Finite-Part-Tautologie:** `Tr_reg := AC[-zeta'/zeta]` beweist keinen Cutoff-Grenzwert.
6. **Cutoff-Transfer:** bloßes `R_p asymp p/log p` reicht nicht zur Identifikation von Finite Parts.

## 10. Endurteil

\[
\boxed{\text{H-T5 COMPLETE — keine offenen Reaudits; der korrekte analytische Kern ist der geglättete Mangoldt-Kanal }\Psi_{\varphi,X}.}
\]

Damit sind H-T1 bis H-T5 primär reconciliiert. Vor einer SYN-Migration folgt nun der **unabhängige P08-Gesamtgegencheck und das Pass-A-Sealing**.