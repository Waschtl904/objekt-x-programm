# NEU-166b — Rollen- und Provenienzentscheidung für $\mathcal{R}_p$ und $\widetilde{T}_p$

**Status:** Offen — methodisch vollständig und eingefroren, inhaltlich unentschieden  
**Vorgänger:** NEU-166a (Abschnitt 166a.D'), NEU-165a, NEU-157, NEU-41 §3  
**Nachfolger:** abhängig vom Ergebnis (siehe 166b.6)  
**Eingetragen:** 2026-07-16 | **Letzte Revision:** 2026-07-16 (Kanonizitätspraezisierung, Rohzeilen-Protokoll, negativer Befund, Gesamtbilanz)  

---

## Aufgabe

NEU-166a ist ein Auditblatt. NEU-166b ist das erste **Entscheidungsblatt**: Es schließt die Tore 166a.D' und 166a.A, indem es die tatsächliche Rolle und Provenienz von $\mathcal{R}_p$ und $\widetilde{T}_p$ aus den vorhandenen Quellen rekonstruiert.

$$
\text{Quellenbefund} \;\longrightarrow\; \text{Rollenentscheidung} \;\longrightarrow\; \text{erst danach Operatorrekonstruktion.}
$$

**Ein Modentest für $u = 1-p$ darf erst nach NEU-166b beginnen.**

$$
\boxed{\text{Die möglichen Ergebnisse sind vor der Quellenlektüre festgelegt.}}
$$

Dadurch kann der Befund aus NEU-41 §3 nicht mehr nachträglich so umgedeutet werden, dass er zur gewünschten Zeugenroute passt.

---

## Verbindliche Sperrmarken

Bis 166b.1 und 166b.6 tatsächlich ausgefüllt sind, gelten:

$$
u = 1-p \quad\text{gesperrt},
$$
$$
\ker\!\left(C_p|_{\mathscr{D}_p^{\mathrm{wit}}}\right) \not\subseteq \ker\!\left(\widetilde{T}_p|_{\mathscr{D}_p^{\mathrm{wit}}}\right) \quad\text{nicht behauptbar},
$$
$$
\widetilde{T}_p = \Theta_p G_p \quad\text{nicht importierbar.}
$$

Diese Aussagen sind nicht bloß offen, sondern durch das Auditverfahren **blockiert**.

---

## Beweisrichtung

Die einzig zulässige Leserichtung ist:

$$
\text{NEU-41 §3} \longrightarrow \text{wörtlicher Quellenbefund} \longrightarrow \text{Verwendung in NEU-157} \longrightarrow \text{Korrekturstatus in NEU-165a.}
$$

**Nicht zulässig:**

$$
\text{gewünschten Operator wählen} \longrightarrow \text{passende Quellenaussagen zusammensuchen.}
$$

---

## Vier Quellenstatus-Kategorien

| Status | Bedeutung | DAG-Konsequenz |
|---|---|---|
| **explizit definiert** | Formel, Bereich und Zielwert stehen in der Quelle | bestehende DAG-Kante gerechtfertigt |
| **implizit exportierbar** | Quelle enthält Bedingung, aus der ein Operator **ohne freie Wahl** kanonisch entsteht | neuer Konstruktionsauftrag; noch keine Kante |
| **nachträglich postuliert** | Symbol erscheint erst in NEU-157 ohne gesicherten Import | Platzhalter; keine Kante |
| **nicht rekonstruierbar** | Auch kanonische Konstruktion nicht eindeutig möglich | Klasse-4-Befund; $[O\text{-}166b\text{-block}]$ eröffnen |

Nur **explizit definiert** begründet unmittelbar eine bestehende DAG-Kante.

### Kanonizitätsprazisierung für „implizit exportierbar“

Diese Kategorie ist streng zu verwenden. Eine Bündelung

$$
\mathcal{R}_p(k) := (R_{p,1}(k), \ldots, R_{p,m}(k))
$$

ist nur dann **kanonisch** (ohne freie Wahl), wenn aus der Quelle eindeutig hervorgehen:

1. die vollständige Indexmenge
2. die gemeinsamen Definitionsbereiche
3. die Zielräume der Komponenten $Z_{p,j}$
4. der Produktraum (z.B. $\prod_j Z_{p,j}$ versus $\bigoplus_j Z_{p,j}$ versus $\ell^2(Z_{p,j})$)
5. das Verhalten bei unendlich vielen Komponenten

Fehlt etwa die Wahl des Zielraums, ist die Bündelung möglich, aber noch **nicht vollständig kanonisch**. Der Status bleibt dann *implizit exportierbar* mit explizitem Vermerk der fehlenden Wahl.

---

## Methodischer Schutz

> **A.** „Die Quelle *definiert* einen Operator.“ → *explizit definiert*
>
> **B.** „Aus der Quellenbedingung *könnte man* einen Operator konstruieren.“ → *implizit exportierbar*

Nur A rechtfertigt eine bestehende DAG-Kante. B eröffnet höchstens einen Konstruktionsauftrag.

NEU-165a darf nicht als unabhängiger Beleg gelten, wenn es lediglich dokumentiert, dass eine Operatorfamilie zuvor ungesichert verwendet wurde.

$$
\boxed{\text{Ab jetzt kann ein negativer Quellenbefund nicht mehr durch zusätzliche Formalisierung verdeckt werden.}}
$$

---

## 166b.1 — NEU-41 §3 als Primärquelle: Rohzeilen-Protokoll

### Auswertungsreihenfolge

$$
\text{Einzelaussagen erfassen} \longrightarrow \text{Typen vergleichen} \longrightarrow \text{mögliche Bündelung prüfen} \longrightarrow \text{Quellenstatus vergeben.}
$$

Fur jede relevante Passage wird genau **eine Rohzeile** angelegt, zunächst ohne Synthese. Erst nachdem alle Rohzeilen vorhanden sind, darf geprüft werden, ob mehrere Bedingungen gemeinsam einen Operator bilden.

### Rohzeilen-Felder (je Passage)

- Wörtliche Formel oder Bedingung
- Objekt, auf dem sie wirkt
- Absoluter Lift oder Variation
- Definitionsbereich
- Zielwert
- Linearitätsstatus (linear / affin / linearisiert am Basispunkt / bloße Mengenbedingung)
- In der Quelle vergebene Rolle

### Erhebungsmatrix

| Quelle | Originalbedingung | Bereich | linear? | Zielwert | Quellenstatus | Rolle | kanonisch? |
|---|---|---|---|---|---|---|---|
| NEU-41 §3 | wörtliche Formel | Lift / Variation / Modus | linear / affin / linearisiert / Mengenbedingung | Skalar / Vektor / Bedingung | explizit def. / impl. export. / nachtr. postul. / nicht rekonstru. | Zulässigkeit / Detektor / sonstige | ja / nein / offen |
| NEU-157 | … | … | … | … | … | … | … |
| NEU-165a | … | … | … | … | … | … | … |

**Zur Spalte „Bereich“:** Absolute Lifte ($x \in Q_p(\widehat{\varepsilon}_p^{\,0})$) und homogene Variationen ($h \in E_p^{\mathrm{adm}}$) dürfen nicht zu einem Operator zusammengefasst werden.

---

## 166b.2 — NEU-157 als Verwendungsaudit

Für jede in NEU-157 auftretende Bezeichnung $R_{p,j}$ ist zu prüfen:

1. **Importiert** aus NEU-41 §3 → *explizit definiert*
2. **Neu definiert** in NEU-157 → *explizit definiert* (lokal)
3. **Vorausgesetzt** ohne gesicherten Import → *nachträglich postuliert*

Nur Option 1 oder 2 verleiht $R_{p,j}$ echten Quellenstatus.

---

## 166b.3 — NEU-165a als Korrektur- und Provenienzaudit

NEU-165a darf nicht als unabhängiger Beleg gelten, wenn es lediglich dokumentiert, dass eine Operatorfamilie zuvor ungesichert verwendet wurde. Alles, was nur durch NEU-165a „belegt“ ist, erhält Quellenstatus *nachträglich postuliert* oder *nicht rekonstruierbar*.

---

## 166b.4 — Rolle von $T_p$ in den Quellen

| Mögliche Rolle | Kriterium |
|---|---|
| Zulässigkeitsoperator | $T_p$ definiert oder filtert $L_p^{\mathrm{adm}}$ |
| Transversaler Detektor | $T_p$ unterscheidet Lifte mit gleichem $C_p$-Schatten |
| Faktorisierungskomponente | $T_p = \Theta_p \circ G_p$ mit unabhängigem $G_p$ |
| Nicht vorhanden | $T_p$ erscheint in den Quellen unter diesem Namen nicht |

Falls $T_p$ ein Detektor ist: Identifikation der unabhängigen Ausgangsdaten vor Festlegung von $D(\widetilde{T}_p)$ und $Z_p$.

---

## 166b.5 — Drei-Fragen-Entscheidungsregel

$$
\boxed{
\begin{aligned}
&\text{1. Existiert ein kanonischer Zulässigkeitsoperator } \mathcal{R}_p?\\
&\text{2. Existiert ein davon unabhängiger Detektor } \widetilde{T}_p?\\
&\text{3. Existiert eine belegte Beziehung zu } G_p, \Pi_p, \Theta_p?
\end{aligned}
}
$$

Erst aus den drei Antworten folgt Fall 1, 2, 3 oder 4. Keine Synthese vorher.

---

## 166b.6 — Ergebnismatrix und DAG-Entscheidung

| Befund | Konsequenz |
|---|---|
| $\mathcal{R}_p$ vorhanden, $\widetilde{T}_p$ fehlt | Fall 1: unabhängigen Detektor konstruieren |
| $\mathcal{R}_p$ und $\widetilde{T}_p$ getrennt vorhanden | Fall 2: Domänen- und Kerntrennungstest |
| $G_p$ vorhanden, $\Theta_p$ unvollständig | Fall 3: $\Theta_p$-Rekonstruktion |
| Keine kanonische Rekonstruktion möglich | Fall 4: Platzhalter-/Zusatzdatenbefund |

### Wichtigster möglicher negativer Befund

Der methodisch bedeutsamste Ausgang wäre:

$$
\mathcal{R}_p \text{ ist implizit exportierbar oder nachträglich postuliert,}
\quad\text{aber}\quad
\widetilde{T}_p \text{ kommt in NEU-41 überhaupt nicht vor.}
$$

Dann gilt:

$$
\boxed{\text{Fall 1 oder Fall 4, nicht Fall 3.}}
$$

Das bloße Vorhandensein von $G_p$ darf nicht dazu führen, automatisch ein $\Theta_p$ und damit einen Detektor zu ergänzen. Dafür müssten zusätzliche geometrische Daten ausgewiesen werden.

### DAG-Kantenentscheidung

| Fall | DAG-Kante |
|---|---|
| 1 | Keine Kante $\{R_{p,j}\}_j \to \widetilde{T}_p$; Zweig $\mathcal{R}_p$ separat |
| 2 | Kante $\{R_{p,j}\}_j \to L_p^{\mathrm{adm}}$ und $\widetilde{T}_p$ unabhängig |
| 3 | Kante $G_p \to \widetilde{T}_p$; $\Theta_p$-Rekonstruktionsblatt als Nachfolger |
| 4 | Kein neuer Knoten; $[O\text{-}166b\text{-block}]$ eröffnen |

---

## Stop-Regel

$$
\boxed{
\text{Kein Übergang zu } u=1-p, \text{ solange Fall 2 oder ein ausreichend präzisierter Fall 3 nicht erreicht ist.}
}
$$

- **Fall 1** erlaubt keine Detektorrechnung.
- **Fall 4** erlaubt überhaupt keine $T_p$-Rechnung.
- **Fall 3** erlaubt $u = 1-p$ erst, wenn $e_{1-p}V_p \in D(\widetilde{T}_p)$ und $\Theta_p G_p(e_{1-p}V_p)$ wohldefiniert sind.

---

## Verzweigungstabelle

| Befund aus NEU-166b | Nächster Schritt |
|---|---|
| Fall 1 | Konstruktion eines unabhängigen Detektors $\widetilde{T}_p$ |
| Fall 2 | Domänen- und Kerntrennungstest (NEU-166a.G') |
| Fall 3 | $\Theta_p$-Rekonstruktionsblatt |
| Fall 4 | No-go- / Zusatzdatenblatt |

---

## Gesamtbilanz

| Ebene | Status |
|---|---|
| Auditarchitektur | $\checkmark[M]$ |
| Beweisrichtung | $\checkmark[M]$ |
| Quellenstatussystem | $\checkmark[M]$ |
| Kanonizitätsprazisierung | $\checkmark[M]$ |
| Sperrlogik | $\checkmark[M]$ |
| Ergebnisverzweigung | $\checkmark[M]$ |
| Wörtlicher Quellenbefund NEU-41 §3 | $?[O]$ |
| Existenz von $\mathcal{R}_p$ | $?[O]$ |
| Existenz von $\widetilde{T}_p$ | $?[O]$ |

$$
\boxed{
\text{NEU-166a definiert die zulässigen Architekturen;} \quad \text{NEU-166b entscheidet, welche davon im Katalog wirklich existiert.}
}
$$

$$
\boxed{\text{Der nächste mathematische Fortschritt kann jetzt nur noch aus dem Quellenmaterial kommen.}}
$$

---

## Offene Fragen

| ID | Frage |
|---|---|
| O-166b-1 | Wörtlicher Befund: Welche $R_{p,j}$-artigen Objekte existieren in NEU-41 §3? Quellenstatus? |
| O-166b-2 | Wörtlicher Befund: Welche in NEU-157? Importiert / neu definiert / postuliert? |
| O-166b-3 | Tritt $T_p$ in einer der Quellen unter diesem Namen auf? In welcher Rolle? |
| O-166b-block | (bedingt, Fall 4) Was fehlt für die Rekonstruktion von $\widetilde{T}_p$? |
