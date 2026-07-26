# NEU-166a — Typ-, Domänen- und Deszentaudit von $\widetilde{T}_p$

**Status:** Offen  
**Vorgänger:** NEU-165a (Rohoperatorbrücke), NEU-157 (Zulässigkeitsraum), NEU-41 §3 (Bedingungen)  
**Nachfolger:** NEU-166b (Rollen- und Provenienzentscheidung), NEU-166 (Modentriage), DAG-Knoten: Weil-Vergleich (bedingt, siehe 166a.J)  
**Eingetragen:** 2026-07-16 | **Letzte Revision:** 2026-07-16 (D' Relationen-Audit; G' Kerntrennung explizit)  

---

## Hintergrund und Motivation

[O-166-0] fragte ursprünglich: „Welcher der drei Typen von $T_p$ ist richtig?" — nämlich

$$
T_p: K_p \to Z_p, \qquad T_p: L_p^{\mathrm{adm}} \to Z_p, \qquad T_p: K_p/N_p \to Z_p.
$$

Diese drei Schreibweisen sind **keine konkurrierenden Definitionen**, sondern Ebenen einer hierarchischen Konstruktion. NEU-166a rekonstruiert diese Hierarchie vollständig, bevor die Modentriage in NEU-166 beginnt.

Zusätzlich wird das Zeugenprogramm (absoluter vs. relativer Liftzeuge) als eigenständige Vorentscheidung eingeführt, da der relevante Zeugenbereich von dieser Wahl abhängt.

**Katalogstatus:** NEU-166a hat die Zeugenfrage nicht gelöst, aber erstmals wohldefiniert.

---

## 166a.0 — Rolle des Operators $\widetilde{T}_p$

Zu klären ist, welche Funktion $\widetilde{T}_p$ im Gesamtprogramm übernimmt:

- **Detektorfunktion:** $\widetilde{T}_p$ soll Lifte unterscheiden, die $C_p$ nicht trennt.
- **Kerntrennungsfunktion:** $\ker C_p \not\subseteq \ker \widetilde{T}_p$ (relativ) oder $C_p(x) = 0, \widetilde{T}_p(x) \neq 0$ (absolut).
- **Faktorisierungsfunktion:** $\widetilde{T}_p$ tritt als $\Theta_p \circ G_p$ in einer gemeinsamen Voroperatorstruktur auf.

Die Rollenentscheidung bestimmt, welche der nachfolgenden Abschnitte bindend sind.

---

## 166a.0a — Absoluter oder relativer Liftzeuge

**Vor** der Definition eines gemeinsamen Zeugenbereichs ist festzulegen, welche Existenzbehauptung das Zeugenprogramm benötigt.

### Absoluter Liftzeuge

Gesucht wird ein Punkt $x = \widehat{\varepsilon}_p^{\,0} + h \in Q_p(\widehat{\varepsilon}_p^{\,0})$ mit

$$
C_p(x) = 0, \qquad \widetilde{T}_p(x) \neq 0.
$$

Bei linearen Operatoren sind die Bedingungen an die Variation $h$:

$$
C_p(h) = -C_p(\widehat{\varepsilon}_p^{\,0}), \qquad \widetilde{T}_p(h) \neq -\widetilde{T}_p(\widehat{\varepsilon}_p^{\,0}).
$$

Die Inkrementformulierung lautet allgemein:

$$
\Delta_{\widehat{\varepsilon}_p^{\,0}} C_p(h) = -C_p(\widehat{\varepsilon}_p^{\,0}), \qquad \Delta_{\widehat{\varepsilon}_p^{\,0}} \widetilde{T}_p(h) \neq -\widetilde{T}_p(\widehat{\varepsilon}_p^{\,0}).
$$

**Wichtig:** Die Bedingung $C_p(\widehat{\varepsilon}_p^{\,0}) = 0$ ist hierfür *nicht* notwendig. Ein geeigneter Variationsvektor $h$ kann den Basiswert kompensieren.

Das absolute Existenzproblem im linearen Fall ist eine **affine Lösbarkeitsfrage**:

$$
-C_p(\widehat{\varepsilon}_p^{\,0}) \in C_p(E_p^{\mathrm{adm}}).
$$

### Relativer Liftzeuge

Gesucht wird eine zulässige Variation $h \in E_p^{\mathrm{adm}}$ mit

$$
\Delta_{\widehat{\varepsilon}_p^{\,0}} C_p(h) = 0, \qquad \Delta_{\widehat{\varepsilon}_p^{\,0}} \widetilde{T}_p(h) \neq 0.
$$

Der relative Zeuge liefert zwei admissible Lifte mit demselben $C_p$-Schatten, die durch $\widetilde{T}_p$ unterschieden werden. Er liefert im Allgemeinen **keinen** absoluten Lift mit verschwindendem $C_p$-Wert.

Das relative Existenzproblem ist eine **Nichtinjektivitätsfrage**:

$$
\ker\!\left(C_p|_{\mathscr{E}_p^{\mathrm{wit}}}\right) \not\subseteq \ker\!\left(\widetilde{T}_p|_{\mathscr{E}_p^{\mathrm{wit}}}\right).
$$

### Zusammenfassung: absolut vs. relativ

$$
\boxed{
\begin{aligned}
\text{absolut:}\quad& \Delta C_p(h) = -C_p(\widehat{\varepsilon}_p^{\,0}), \quad \Delta\widetilde{T}_p(h) \neq -\widetilde{T}_p(\widehat{\varepsilon}_p^{\,0}); \\
\text{relativ:}\quad& \Delta C_p(h) = 0, \quad \Delta\widetilde{T}_p(h) \neq 0.
\end{aligned}
}
$$

Nur falls $C_p(\widehat{\varepsilon}_p^{\,0}) = 0$ und $\widetilde{T}_p(\widehat{\varepsilon}_p^{\,0}) = 0$ gelten, fallen beide Bedingungen zusammen.

**Die zentrale Leitfrage lautet:**

> Soll $\widetilde{T}_p$ einen einzelnen Lift mit verschwindendem Schatten erkennen,  
> oder soll es verschiedene Lifte innerhalb derselben Schattenfaser unterscheiden?

Diese beiden Mechanismen dürfen in NEU-166 nicht unter einer gemeinsamen unqualifizierten „Kerntrennung" geführt werden.

---

## 166a.0b — Punkt- und Variationsbereich

Nach der Entscheidung in 166a.0a sind unterschiedliche gemeinsame Bereiche zu definieren.

### Für den absoluten Zeugen

$$
\mathscr{X}_p^{\mathrm{wit}} := Q_p(\widehat{\varepsilon}_p^{\,0}) \cap D(C_p) \cap D(\widetilde{T}_p),
$$

gegebenenfalls zusätzlich geschnitten mit den Definitionsbereichen aller verwendeten Faktorisierungsoperatoren ($G_p$, $\mathcal{R}_p$, $\Pi_p$, $\Theta_p$).

Die absolute Zeugenbedingung lautet:

$$
\exists\, x \in \mathscr{X}_p^{\mathrm{wit}}: \quad C_p(x) = 0, \quad \widetilde{T}_p(x) \neq 0.
$$

Dieser Bereich ist typischerweise **affin oder eine bloße Menge** — eine Kerninklusion ist hier im Allgemeinen nicht die passende Sprache.

### Für den relativen Zeugen

$$
\mathscr{E}_p^{\mathrm{wit}}(\widehat{\varepsilon}_p^{\,0}) := \left\{ h \in E_p^{\mathrm{adm}} : \widehat{\varepsilon}_p^{\,0},\, \widehat{\varepsilon}_p^{\,0} + h \in D(C_p) \cap D(\widetilde{T}_p) \right\}.
$$

Die relative Zeugenbedingung lautet:

$$
\exists\, h \in \mathscr{E}_p^{\mathrm{wit}}(\widehat{\varepsilon}_p^{\,0}): \quad \Delta_{\widehat{\varepsilon}_p^{\,0}} C_p(h) = 0, \quad \Delta_{\widehat{\varepsilon}_p^{\,0}} \widetilde{T}_p(h) \neq 0.
$$

Eine Formulierung durch eingeschränkte Kerne ist nur zulässig, wenn der Variationsbereich ein linearer Raum ist und die Inkrementoperatoren darauf linear wirken.

---

## 166a.A — Primitive Definition

Explizite Angabe des Rohoperators:

$$
\widetilde{T}_p: D_p \subseteq K_p \longrightarrow Z_p.
$$

Zu spezifizieren sind:
- $D_p$: Definitionsbereich (explizit, nicht nur formal)
- $Z_p$: Zielraum (mit Topologie)
- Linearität oder Affinität
- Topologie auf $D_p$ (Teilraumtopologie, Graphnorm, andere)

**Offene Frage [O-166a-A]:** Aus welchem Ausgangsobjekt geht $\widetilde{T}_p$ hervor? Die Brücke von den Bedingungen in NEU-41 §3 zu einem konkreten Operator ist nach NEU-165a noch nicht vollständig geschlossen (vgl. [O-165a-2]). Näheres in 166a.D'.

---

## 166a.B — Modenformel

Herleitung oder Import von

$$
\widetilde{T}_p(e_u V_p)
$$

für Modenvektoren $e_u V_p \in D_p$.

Separat auszuweisen:
- Konvergenz der Modenentwicklung
- Cutoffabhängigkeit (welche Terme hängen von der Regularisierungswahl ab?)
- Verhalten für $u = 1-p$ als **Domänenkandidat** (noch kein Rechenkandidat, siehe 166a.I)

---

## 166a.C — Admissible Einschränkung

Prüfung der Inklusion

$$
L_p^{\mathrm{adm}} \subseteq D_p
$$

und Definition von $T_p^{\mathrm{adm}} := \widetilde{T}_p|_{L_p^{\mathrm{adm}}}$.

Ohne positiven Befund darf $T_p^{\mathrm{adm}}$ nicht verwendet werden.

---

## 166a.D — Quotientenabstieg

Entscheidung über

$$
N_p \subseteq \ker(\widetilde{T}_p).
$$

Nur bei positivem Befund ist $\overline{T}_p: K_p/N_p \to Z_p$ mit $\overline{T}_p([k]) = \widetilde{T}_p(k)$ wohldefiniert.

---

## 166a.D' — Relationen- und Provenienzaudit von $\mathcal{R}_p$, $\{R_{p,j}\}_j$ und $\widetilde{T}_p$

**[O-165a-2] — Status: offen.**

Dieser Abschnitt ist ein **Audit**, kein Beweis. Er stellt keine DAG-Kante $\{R_{p,j}\}_j \to \widetilde{T}_p$ voraus; eine solche Kante darf erst als *Ergebnis* dieses Audits eingetragen werden.

### Zu unterscheidende Fälle

**Fall 1 — Identifikation:**
$\widetilde{T}_p = (R_{p,j})_j$, d.h. die Operatorfamilie $\{R_{p,j}\}_j$ *ist* der transversale Detektor.

**Fall 2 — Rollentrennung:**
$L_p^{\mathrm{adm}}$ wird durch $\{R_{p,j}\}_j$ definiert (Zulässigkeitsoperator), während $\widetilde{T}_p$ unabhängig davon konstruiert ist.

**Fall 3 — Voroperatorstruktur:**
$\widetilde{T}_p = \Theta_p \circ G_p$, und $\{R_{p,j}\}_j$ kontrollieren nur die Zulässigkeit des Liftbereichs, nicht den Detektor selbst.

**Fall 4 — Unrekonstruierbarkeit:**
$\widetilde{T}_p$ ist aus den vorhandenen Daten (NEU-41, NEU-157, NEU-165a) noch nicht rekonstruierbar; $D_p$ fehlt dem Inhalt nach, nicht nur der Notation.

### Aufgabe dieses Abschnitts

1. Alle $R_{p,j}$-artigen Bedingungen aus NEU-41 §3, NEU-157 und NEU-165a wörtlich rekonstruieren.
2. Entscheiden, ob sie einen linearen Operator $\mathcal{R}_p = (R_{p,j})_j$ definieren.
3. Prüfen, ob das bisherige Symbol $T_p$ dort als Zulässigkeitsoperator, Detektor oder überhaupt nicht vorkommt.
4. Falls $T_p$ ein Detektor ist: seine unabhängigen Ausgangsdaten identifizieren.
5. Erst danach $D(\widetilde{T}_p)$, $Z_p$ und eine mögliche Formel $\widetilde{T}_p = \Theta_p G_p$ festlegen.
6. DAG-Kante $\{R_{p,j}\}_j \to \widetilde{T}_p$ nur bei positivem Befund aus Fall 1 eintragen.

Der nächste Katalogschritt für diesen Abschnitt ist **NEU-166b**.

---

## 166a.E — Quotientennorm und Hausdorff-Abstieg

Die Quotientennorm auf $D_p/(D_p \cap N_p)$,

$$
\|[k]\|_{\mathrm{quot}} := \inf_{n \in D_p \cap N_p} \|k + n\|_{D_p},
$$

ist **nur dann eine echte Norm**, wenn $D_p \cap N_p$ im normierten Raum $D_p$ abgeschlossen ist.

Ist der Schnitt nicht abgeschlossen, verschwindet die Quotientenseminorm auf $\overline{D_p \cap N_p}^{\,D_p}$, und der natürliche Hausdorff-Quotient ist

$$
D_p / \overline{D_p \cap N_p}^{\,D_p}.
$$

Analog ist $K_p/N_p$ nur dann Hausdorff-normiert, wenn $N_p$ in $K_p$ abgeschlossen ist.

### Vier Ebenen des Quotientenabstiegs (166a.E.3)

| Ebene | Zu prüfende Bedingung |
|---|---|
| Algebraischer Abstieg | $D_p \cap N_p \subseteq \ker \widetilde{T}_p$ |
| Hausdorff-Abstieg im Domänenraum | $D_p \cap N_p$ ist in $D_p$ abgeschlossen |
| Stetigkeit in der Domänen-/Graphnorm | Kontrolle durch Quotientennorm auf $D_p/(D_p \cap N_p)$ |
| Umgebungsquotient | $N_p$ ist in $K_p$ abgeschlossen; Kontrolle durch $\operatorname{dist}_{K_p}(k, N_p)$ |

Ist $D_p$ mit der Graphnorm von $\widetilde{T}_p$ versehen,

$$
\|k\|_{\mathrm{gr}} = \|k\|_{K_p} + \|\widetilde{T}_p(k)\|_{Z_p},
$$

so gilt $\|\widetilde{T}_p(k)\|_{Z_p} \leq \|k\|_{\mathrm{gr}}$ unmittelbar. Der Abstieg auf den Quotienten verlangt aber weiterhin die Kernbedingung und die passende Abgeschlossenheit.

---

## 166a.F — Gemeinsamer Voroperator

Prüfung, ob

$$
C_p = \Pi_p \circ G_p, \qquad \widetilde{T}_p = \Theta_p \circ G_p
$$

auf demselben Bereich gelten.

Falls ja: Das korrekte Kerntrennungskriterium lautet

$$
\operatorname{ran}(G_p) \cap (\ker \Pi_p \setminus \ker \Theta_p) \neq \varnothing.
$$

Mit Zulässigkeitsbedingung (engeres Kriterium):

$$
G_p(D_p^{\mathrm{adm}}) \cap (\ker \Pi_p \setminus \ker \Theta_p) \neq \varnothing.
$$

Ein beliebiges Element aus $\operatorname{ran}(G_p)$ ohne Zulässigkeitsnachweis ist kein Zeuge, sondern ein Kandidat.

---

## 166a.G — Faktorisierungsklasse T1–T5

Erst nach Abschluss von 166a.A–F wird entschieden, welcher Faktorisierungsfall tatsächlich vorliegt:

- **T1:** $T_p = A_p \circ C_p$ — dann $\ker C_p \subseteq \ker T_p$, kein Zeuge in $\ker C_p \setminus \ker T_p$ möglich.
- **T2:** $C_p = B_p \circ T_p$ — dann $\ker T_p \subseteq \ker C_p$, Zeuge in $\ker C_p \setminus \ker T_p$ möglich, aber nicht garantiert (erfordert $T_p(k) \in \ker(B_p) \setminus \{0\}$).
- **T3–T5:** Gemeinsamer Voroperator $G_p$ mit verschiedenen Projektionspaaren $(\Pi_p, \Theta_p)$, Kriterium siehe 166a.F.

---

## 166a.G' — Kerntrennung: absolutes und relatives Existenzproblem

Nach Festlegung der Faktorisierungsklasse in 166a.G werden die beiden Existenzprobleme separat geführt.

### Absolutes Existenzproblem

Im linearen Fall: Existiert $h \in E_p^{\mathrm{adm}}$ mit

$$
C_p(h) = -C_p(\widehat{\varepsilon}_p^{\,0}) \qquad \text{und} \qquad \widetilde{T}_p(h) \neq -\widetilde{T}_p(\widehat{\varepsilon}_p^{\,0})\,?
$$

Die erste Gleichung ist eine affine Lösbarkeitsfrage: $-C_p(\widehat{\varepsilon}_p^{\,0}) \in C_p(E_p^{\mathrm{adm}})$.

### Relatives Existenzproblem

Existiert $h \in \mathscr{E}_p^{\mathrm{wit}}(\widehat{\varepsilon}_p^{\,0})$ mit

$$
C_p(h) = 0 \qquad \text{und} \qquad \widetilde{T}_p(h) \neq 0\,?
$$

Das ist die eingeschränkte Kerntrennung:

$$
\ker\!\left(C_p|_{\mathscr{E}_p^{\mathrm{wit}}}\right) \not\subseteq \ker\!\left(\widetilde{T}_p|_{\mathscr{E}_p^{\mathrm{wit}}}\right).
$$

**Diese beiden Probleme dürfen nicht unter derselben unqualifizierten Zeugenformel geführt werden.**

---

## 166a.H — Gemeinsamer Voroperatortest und Zulässigkeitscheck

Prüfung, ob der gemeinsame Voroperator $G_p$ auf dem zulässigen Teil des Bildes tatsächlich definiert ist (Erweiterung von 166a.F auf den Domänenkontext aus 166a.C):

$$
G_p\!\left(D_p^{\mathrm{adm}}\right) \subseteq \operatorname{dom}(\Pi_p) \cap \operatorname{dom}(\Theta_p).
$$

Ohne positiven Befund ist das engere Kerntrennungskriterium aus 166a.F nicht anwendbar.

---

## 166a.I — Kandidat $u = 1-p$

Der Primkandidat $e_{1-p} V_p$ darf erst ausgewertet werden, wenn alle vorherigen Tore geschlossen sind. Vier Schranken müssen vorliegen:

1. $e_{1-p} V_p \in D_p = \operatorname{dom}(\widetilde{T}_p)$
2. $e_{1-p} V_p \in K_p^{\mathrm{hom}}$ beziehungsweise $L_p^{\mathrm{adm}}$
3. $G_p(e_{1-p} V_p)$ ist im verwendeten Zielraum tatsächlich definiert (nicht nur eine formale Summe)
4. $\Theta_p(G_p(e_{1-p} V_p))$ ist unabhängig von Lift-, Repräsentanten- und Cutoff-Entscheidungen

**$u = 1-p$ ist daher zunächst ein Domänenkandidat, kein Rechenkandidat.**

---

## 166a.J — DAG-Abhängigkeit vom Weil-Vergleich

**[O-166a-dep]:** Die Aussage „NEU-166a muss vor dem Weil-Vergleich $W_{\mathrm{res},BC}^{\mathrm{top}} \to Q_{\mathrm{Weil}}$ stehen" gilt **nicht unbedingt**.

NEU-166a ist zwingend für:
- die lokale Zeugenroute $\ker C_p \not\subseteq \ker T_p$
- jede Konstruktion von $X$, die diese Liftgeometrie verwendet

Der globale Vergleich $W_{\mathrm{res},BC}^{\mathrm{top}} \to Q_{\mathrm{Weil}}$ könnte logisch unabhängig davon über eine direkte Korrespondenz, Spurformel oder globale Paarung konstruiert werden.

**Korrekte DAG-Formulierung:**

> NEU-166a ist genau dann ein notwendiger Vorgänger des Weil-Vergleichs, wenn dessen Konstruktion über die $T_p$-kontrollierte Lift- oder Quotientengeometrie faktorisiert.

Diese Abhängigkeit muss im DAG **ausdrücklich geprüft**, nicht vorausgesetzt werden.

---

## Plausibilitätseinschätzung für $X$

Ohne Anforderungen wie Funktorialität, Rekonstruktionseindeutigkeit oder arithmetische Natürlichkeit ist die Existenz eines abstrakten $X$ mit $\Pi_\gamma(X) = m_{\mathrm{arith}}$ nahezu tautologisch.

| Behauptung | Plausible Einschätzung |
|---|---|
| Formale Verdickung $X$ mit $\Pi_\gamma(X) = m_{\mathrm{arith}}$ | >90%, geringe Aussagekraft |
| Natürliches, nicht künstlich angepasstes $X$ | 25–35% |
| $X$ rekonstruiert kanonisch $Q_{\mathrm{Weil}}$ | 15–30% |
| Positivität von $X$ beweist RH unbedingt | 10–20% |

Der Vergleich $W_{\mathrm{res},BC}^{\mathrm{top}} \to Q_{\mathrm{Weil}}$ erhöht die Wahrscheinlichkeit für ein kanonisches $X$ nur dann massiv, wenn er zugleich kanonisch/funktoriell, nicht zirkulär, mit den arithmetischen Operationen kompatibel und positivitätsverträglich ist.

---

## Offene Fragen

| ID | Frage |
|---|---|
| O-166a-A | Was ist $D_p$ explizit, und aus welchem Ausgangsobjekt geht $\widetilde{T}_p$ hervor? |
| O-166a-B | Konvergenz und Cutoffabhängigkeit der Modenformel $\widetilde{T}_p(e_u V_p)$ |
| O-166a-C | Gilt $L_p^{\mathrm{adm}} \subseteq D_p$? |
| O-166a-D | Gilt $N_p \subseteq \ker(\widetilde{T}_p)$? Ist $N_p$ in $K_p$ abgeschlossen? |
| O-165a-2 | Brücke $\{R_{p,j}\}_j$ / $\widetilde{T}_p$: Relationen-Audit (→ NEU-166b) |
| O-166a-dep | Faktorisiert der Weil-Vergleich über die $T_p$-Liftgeometrie? (DAG-Prüfung) |

---

## Sequenz der Abschnitte

$$
\text{166a.0 Rolle}
\;\to\;
\text{166a.0a absolut/relativ}
\;\to\;
\text{166a.0b Punkt-/Variationsbereich}
\;\to\;
\text{166a.A Provenienz}
\;\to\;
\text{166a.B Modenformel}
\;\to\;
\text{166a.C adm. Einschränkung}
\;\to\;
\text{166a.D Quotientenabstieg}
\;\to\;
\text{166a.D' Relationen-Audit } \mathcal{R}_p / \widetilde{T}_p
\;\to\;
\text{166a.E Quotientennorm}
\;\to\;
\text{166a.F Voroperator}
\;\to\;
\text{166a.G Faktorisierungsklasse}
\;\to\;
\text{166a.G' Kerntrennung}
\;\to\;
\text{166a.H Voroperatortest}
\;\to\;
\text{166a.I Kandidat } u{=}1{-}p
\;\to\;
\text{166a.J DAG-Abhängigkeit}
$$
