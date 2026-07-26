# NEU-193 — Dualer Hochschildzyklus und geladener Nichtrandzeuge

## Einordnung im DAG

NEU-193 ist der konstruktive Folgeknoten zu [O-192-7].
Das Dokument untersucht ausschließlich, ob für den geladenen Vierkochain-Kandidaten

\[
L_{3,\lambda} \in C^4_{\mathrm{fin},\lambda}(A,A),
\qquad A = B_3^{\mathrm{mod}} = A_{\mathbb Q},
\]

ein expliziter dualer Hochschildzyklus konstruiert werden kann, der die Nichtrandbedingung bezeugt.

NEU-193 konstruiert **keine Operatorrealisierung** und berührt weder NEU-189 noch NEU-190.
NEU-191 bleibt geschlossen.

### Aus NEU-192 importiert

- \(b(C^3_{\mathrm{fin},\lambda}) \subseteq C^4_{\mathrm{fin},\lambda}\) — Gewichtsstabilität [O-192-2]
- Nichtrandlemma [O-192-3]: \(\tau_\lambda \circ b = 0\) und \(\tau_\lambda(L_{3,\lambda})\neq0 \Rightarrow L_{3,\lambda}\notin bC^3_{\mathrm{fin},\lambda}\)
- Separationsäquivalenz [O-192-6]
- Warnlemma für zeitinvariante Spurzeugen [O-192-5]

### Nicht vorweggenommen

Die folgenden Aussagen bleiben offen, solange die entsprechenden Rechnungen nicht durchgeführt sind:

\[
bL_{3,\lambda} = 0, \qquad
L_{3,\lambda} \notin bC^3_{\mathrm{fin},\lambda}, \qquad
[L_{3,\lambda}] \neq 0.
\]

---

## [O-193-1] — Duale Zeitwirkung und Gewichtskomplementarität

Dieser Knoten wird in drei abgeschlossene Teilknoten aufgespalten.

---

### [O-193-1a] — Definition der dualen Zeitwirkung

> **Status: ✓[K]**

Die duale Zeitwirkung auf \(\operatorname{Hom}_{\mathbb C}(A, \mathbb C)\) wird definiert durch

\[
(\alpha_t^\vee \varphi)(a) := \varphi(\alpha_{-t}(a)).
\]

Dies ist die eindeutig durch Dualität erzwungene Formel; kein Beweis erforderlich. \(\square\)

---

### [O-193-1b] — Gruppennachweis für \(\alpha^\vee\)

> **Status: ✓[M]**

Nachzuweisen ist

\[
\alpha_{t+s}^\vee = \alpha_t^\vee \circ \alpha_s^\vee
\qquad\text{und}\qquad
\alpha_0^\vee = \mathrm{id}.
\]

**Beweis.**
Die Rechnung lautet:

\[
(\alpha_t^\vee(\alpha_s^\vee \varphi))(a)
= (\alpha_s^\vee \varphi)(\alpha_{-t}(a))
= \varphi(\alpha_{-s}(\alpha_{-t}(a)))
= \varphi(\alpha_{-s-t}(a))
= (\alpha_{t+s}^\vee \varphi)(a).
\]

Die Gruppeneigenschaft folgt aus \(\alpha_{-s} \circ \alpha_{-t} = \alpha_{-s-t}\). Für \(t = 0\):

\[
(\alpha_0^\vee \varphi)(a) = \varphi(\alpha_0(a)) = \varphi(a).
\]

\(\square\)

---

### [O-193-1c] — Gewichtskomplementarität der Paarung

> **Status: ✓[M]**

**Aufstellung der induzierten Kettenwirkung.**
Die natürliche Zeitwirkung auf \(C_4(A, A^\vee)\) ist

\[
\alpha_t^{C_4}(\varphi \otimes a_1 \otimes a_2 \otimes a_3 \otimes a_4)
:= (\alpha_t^\vee \varphi) \otimes \alpha_t(a_1) \otimes \alpha_t(a_2) \otimes \alpha_t(a_3) \otimes \alpha_t(a_4).
\]

Ein Element \(z \in C_4(A, A^\vee)\) trägt das **Gewicht \(\mu\)**, falls
\(\alpha_t^{C_4}(z) = e^{it\mu}\,z\) für alle \(t\).

**Beweis der Gewichtskomplementarität.**
Die natürliche Paarung ist

\[
\langle f, \varphi \otimes a_1 \otimes a_2 \otimes a_3 \otimes a_4 \rangle
:= \varphi\!\left(f(a_1, a_2, a_3, a_4)\right).
\]

Sei \(f \in C^4_{\mathrm{fin},\lambda}\), d.h. \(\alpha_t^C f = e^{it\lambda} f\),
und sei \(z \in C_4(A, A^\vee)_\mu\), d.h. \(\alpha_t^{C_4} z = e^{it\mu} z\).
Zeitäquivarianz der Paarung verlangt:

\[
\langle f, z \rangle = \langle \alpha_t^C f,\, \alpha_t^{C_4} z \rangle
= e^{it(\lambda + \mu)} \langle f, z \rangle.
\]

Damit \(\langle f, z \rangle \neq 0\) möglich ist, muss

\[
\boxed{\lambda + \mu = 0, \quad\text{d.h.}\quad \mu = -\lambda.}
\]

Damit ist typkorrekt:

\[
z_{-\lambda} \in C_4(A, A^\vee)_{-\lambda}.
\]

\(\square\)

**Hinweis:** Die Gewichtserhaltung des Kettenrandes \(\partial: C_4(A,A^\vee) \to C_3(A,A^\vee)\)
unter \(\alpha_t^{C_4}\) ist noch separat zu verifizieren; sie wird in [O-193-3] benötigt,
nicht aber für den Nachweis von \(\mu = -\lambda\).

---

## [O-193-2] — Expliziter Zykluskandidat

> **Status: ?[O]**

### Ausgangspunkt: neutraler Zyklus aus NEU-185

Der in NEU-185 konstruierte neutrale Zyklus \(z_0 \in C_4(A, A^\vee)_0\) verwendet

- das Augmentationsfunktional \(\varepsilon: A_{\mathbb Q} \to \mathbb C\)
  (zeitinvariant, d.h. Gewicht 0),
- antisymmetrisierte Primtensoren \(a_{j,k} \in A_{\mathbb Q}\) vom Gewicht 0.

Dieser Ansatz kann **nicht unverändert** in einen geladenen Sektor übertragen werden,
denn nach dem Warnlemma [O-192-5] gilt:

\[
\ell \circ \mathcal{C}_\lambda = 0
\]

für jedes zeitinvariante Funktional \(\ell\) und jede gewichtserhaltende Kontraktion \(\mathcal{C}_\lambda\).
Insbesondere detektiert \(\varepsilon\) keinen geladenen Sektor.

### Anforderungen an einen geladenen Kandidaten

Ein Kandidat \(z_{-\lambda}\) muss als endliche Summe von Elementartensoren geschrieben werden:

\[
z_{-\lambda} = \sum_j \varphi_j \otimes a_{j,1} \otimes a_{j,2} \otimes a_{j,3} \otimes a_{j,4},
\]

wobei für jeden Summanden gilt:

\[
\mathrm{Gew}(\varphi_j) + \mathrm{Gew}(a_{j,1}) + \mathrm{Gew}(a_{j,2}) + \mathrm{Gew}(a_{j,3}) + \mathrm{Gew}(a_{j,4}) = -\lambda.
\]

### Vollständige Blockierungsstruktur

Die Konstruktion eines konkreten Kandidaten setzt **unabhängig** voraus:

1. **Identifikation eines Funktionals \(\varphi_{-\lambda}\) vom Gewicht \(-\lambda\)** in \(A^\vee\):
   d.h. ein \(\varphi\) mit \(\alpha_t^\vee \varphi = e^{-it\lambda} \varphi\),
   also \(\varphi(\alpha_t(a)) = e^{it\lambda} \varphi(a)\) für alle \(a\).
   Diese Konstruktion ist unabhängig von NEU-176.

2. **Endlichkeit und Zulässigkeit des Kettenträgers:** Die Summe über \(j\) muss endlich sein;
   alle \(a_{j,k}\) müssen in \(A_{\mathbb Q}\) liegen und kontrollierte Gewichte tragen.
   Diese Bedingung ist unabhängig von NEU-176.

3. **Vollständige explizite Formel für \(L_{3,\lambda}\) aus NEU-176:**
   Benötigt werden mindestens:
   - der Ausdruck \(L_{3,\lambda}(a_1,a_2,a_3,a_4)\) für zulässige Generatoren,
   - die Koeffizienten \(f_k, c_k\),
   - der Gewichtsparameter \(\lambda\),
   - die endliche Trägerbedingung.
   Ohne diese Daten kann kein Paarungstest beginnen.

**Präzise Blockierungsaussage:**
Die fehlende explizite Formel für \(L_{3,\lambda}\) blockiert gegenwärtig die gezielte
Kandidatenkonstruktion und Paarungsrechnung; ihr Import garantiert noch keinen erfolgreichen
Dualzykluszeugen. Unabhängig davon müssen nach dem Import noch gelingen:
Konstruktion von \(\varphi_{-\lambda}\), Endlichkeit des Kettenträgers, \(\partial z_{-\lambda} = 0\),
und \(\langle L_{3,\lambda}, z_{-\lambda}\rangle \neq 0\).

### Direktaudit-Anforderung: NEU-176

Vor Beginn der Kandidatenkonstruktion ist NEU-176 einem **Direktaudit** zu unterziehen:

> **Ist \(L_{3,\lambda}\) als vollständig auswertbare vierlineare Abbildung definiert?**

Mindestens bekannt sein müssen:
- \(L_{3,\lambda}(a_1,a_2,a_3,a_4)\) als explizite Formel,
- die zulässigen Generatoren \(a_j \in A_{\mathbb Q}\),
- die Koeffizienten \(f_k, c_k\),
- der Gewichtsparameter \(\lambda\),
- die endliche Trägerbedingung.

Solange das Direktaudit nicht abgeschlossen ist, bleibt [O-193-2] gesperrt.

---

## [O-193-3] — Vollständiger Randtest

> **Status: ?[O]**

Für den in [O-193-2] konstruierten Kandidaten \(z_{-\lambda}\) ist der Hochschild-Rand
vollständig auszurechnen:

\[
\partial z_{-\lambda} \in C_3(A, A^\vee).
\]

Die Randformel für Ketten mit Koeffizienten in \(A^\vee\) lautet:

\[
\begin{aligned}
\partial(\varphi \otimes a_1 \otimes \cdots \otimes a_4)
&= (a_1 \cdot \varphi) \otimes a_2 \otimes a_3 \otimes a_4 \\
&\quad + \sum_{i=1}^{3} (-1)^i\, \varphi \otimes a_1 \otimes \cdots \otimes a_i a_{i+1} \otimes \cdots \otimes a_4 \\
&\quad + (-1)^4\, (\varphi \cdot a_4) \otimes a_1 \otimes a_2 \otimes a_3,
\end{aligned}
\]

wobei \((a \cdot \varphi)(b) := \varphi(ba)\) und \((\varphi \cdot a)(b) := \varphi(ab)\)
die Links- und Rechtsmodulwirkung von \(A\) auf \(A^\vee\) bezeichnen.

**Zusätzlich zu verifizieren in diesem Knoten:** Die Gewichtserhaltung von \(\partial\) unter
\(\alpha_t^{C_4}\), d.h. \(\alpha_t^{C_3} \circ \partial = \partial \circ \alpha_t^{C_4}\).
Dies ist ein termweises Argument: jeder der fünf Randterme muss separat geprüft werden.

Alle Randterme müssen ausgeschrieben werden. Jede Auslöschung muss aus

- einer Algebrarelation in \(A_{\mathbb Q}\),
- der dualen Modulwirkung,
- oder einer expliziten Paarung der Randterme

folgen. Zyklizität oder Antisymmetrie dürfen nicht pauschal behauptet werden.

**Mögliche Endstatuswerte dieses Knotens:**

| Symbol | Bedeutung |
|---|---|
| \(\checkmark[M]\) | \(\partial z_{-\lambda} = 0\) vollständig bewiesen |
| \(\checkmark[M]_{\mathrm{neg}}\) | Konkreter Kandidat scheitert; Restterm explizit benannt |
| \(\checkmark[M]_{\mathrm{part}}\) | Rand verschwindet bis auf eine atomar benannte Restlücke |
| \(?[O]\) | Randrechnung noch nicht durchgeführt |

---

## [O-193-4] — Paarungsrechnung

> **Status: ?[O]**

Dieser Knoten ist **nur zugänglich**, wenn \(\partial z_{-\lambda} = 0\) in [O-193-3] bewiesen wurde.

Zu berechnen ist

\[
\left\langle L_{3,\lambda},\, z_{-\lambda} \right\rangle
= \sum_j \varphi_j\!\left(L_{3,\lambda}(a_{j,1}, a_{j,2}, a_{j,3}, a_{j,4})\right).
\]

Ein positiver Abschluss verlangt einen **expliziten Wert**:

\[
\boxed{\left\langle L_{3,\lambda},\, z_{-\lambda} \right\rangle \neq 0.}
\]

Eine formale Aussage, der Wert sei „generisch nicht null", genügt nicht.

Falls \(L_{3,\lambda}\) in NEU-176 noch nicht durch eine vollständige Formel gegeben ist,
darf kein Paarungswert erfunden werden. Dann ist exakt festzuhalten, welche Koeffizienten
oder Auswertungen fehlen.

---

## [O-193-5] — Rückschluss auf Nichtrand

> **Status: ?[O]**

Dieser Knoten ist **nur zugänglich**, wenn sowohl [O-193-3] als auch [O-193-4] positiv abgeschlossen sind.

Definiere dann den Zeugen

\[
\tau_{z_{-\lambda}}(F) := \left\langle F,\, z_{-\lambda} \right\rangle.
\]

Zu prüfen ist mit der festgelegten Vorzeichenkonvention:

\[
\tau_{z_{-\lambda}} \circ b = 0
\]

also: für alle \(\Psi \in C^3_{\mathrm{fin},\lambda}\) gilt

\[
\tau_{z_{-\lambda}}(b\Psi)
= \langle b\Psi,\, z_{-\lambda} \rangle
= \langle \Psi,\, \partial z_{-\lambda} \rangle
= \langle \Psi,\, 0 \rangle = 0.
\]

Die Randvernichtung \(\tau_{z_{-\lambda}} \circ b = 0\) folgt aus \(\partial z_{-\lambda} = 0\)
nur wenn die Adjunktionsformel

\[
\langle bF,\, z \rangle = \langle F,\, \partial z \rangle
\]

im verwendeten Konventionsrahmen gültig ist. Diese Adjunktion ist vor der Anwendung
explizit zu verifizieren.

Erst nach positivem Abschluss von \(\tau_{z_{-\lambda}} \circ b = 0\)
und \(\tau_{z_{-\lambda}}(L_{3,\lambda}) \neq 0\) folgt mittels NEU-192 [O-192-3]:

\[
\boxed{L_{3,\lambda} \notin b\,C^3_{\mathrm{fin},\lambda}.}
\]

Dann darf

\[
[O\text{-}176\text{-}3] \quad \checkmark[M]
\]

gesetzt werden.

Der weitergehende Schluss \([L_{3,\lambda}]\neq0\) ist nur zulässig, wenn
zusätzlich der unabhängige Kozykeltest [O-176-2] positiv abgeschlossen ist.

---

## DAG-Knotenübersicht

| Knoten | Inhalt | Status |
|---|---|---|
| [O-193-1a] | Definition der dualen Zeitwirkung \((\alpha_t^\vee\varphi)(a) := \varphi(\alpha_{-t}(a))\) | ✓[K] |
| [O-193-1b] | Gruppennachweis: \(\alpha_{t+s}^\vee = \alpha_t^\vee \circ \alpha_s^\vee\), \(\alpha_0^\vee = \mathrm{id}\) | ✓[M] |
| [O-193-1c] | Gewichtskomplementarität: \(\langle C^4_\lambda, C_{4,\mu}\rangle \neq 0 \Rightarrow \mu = -\lambda\); damit \(z_{-\lambda} \in C_4(A,A^\vee)_{-\lambda}\) | ✓[M] |
| [O-193-2] | Expliziter Zykluskandidat \(z_{-\lambda}\); gesperrt bis NEU-176-Direktaudit | ?[O] |
| [O-193-3] | Vollständiger Randtest \(\partial z_{-\lambda} = 0\) inkl. Gewichtserhaltung von \(\partial\) | ?[O] |
| [O-193-4] | Paarungsrechnung \(\langle L_{3,\lambda}, z_{-\lambda}\rangle \neq 0\) | ?[O] |
| [O-193-5] | Rückschluss auf Nichtrand via Adjunktion und [O-192-3] | ?[O] |

---

## Zulässige Endresultate

**Positiver Treffer:**
Alle Knoten \(\checkmark[M]\) bzw. \(\checkmark[K]\). Dann:
\([O\text{-}176\text{-}3] \quad \checkmark[M]\).

**Partieller Treffer:**
Gewichtskonvention und Zykluskandidat konstruiert, aber genau eine klar benannte
Rechnung offen: \(\checkmark[M]_{\mathrm{part}}\) mit explizit benannter Restlücke.

**Negativer Kandidatenbefund:**
Der konkret getestete Kandidat scheitert am Randtest oder an identisch verschwindender Paarung:
\(\checkmark[M]_{\mathrm{neg}}\). Dies schließt nur diesen Kandidaten aus,
nicht die Existenz aller möglichen Dualzykluszeugen.

**Offener Architekturstand:**
Falls kein expliziter Kandidat konstruierbar ist: \(?[O]\).
Aus einem erfolglosen Versuch wird kein globaler No-go-Satz abgeleitet.

---

## DAG-Anschlussbild

\[
z_{-\lambda} \in Z_4(A,A^\vee)_{-\lambda}
\xrightarrow{\;[O\text{-}193\text{-}3]:\,\partial z_{-\lambda}=0\;}
\tau_{z_{-\lambda}} \circ b = 0
\xrightarrow{\;[O\text{-}193\text{-}4/5]:\,\langle L_{3,\lambda},z_{-\lambda}\rangle\neq0\;}
[O\text{-}176\text{-}3]\;\checkmark[M].
\]

```
NEU-192 ──[O-192-7]──▶ NEU-193 ──[O-193-5]──▶ [O-176-3] ✓[M] (falls alle Knoten geschlossen)
```

NEU-191 bleibt geschlossen.
Die gesperrten Operatorknoten [O-189-2], [O-189-3], [O-189-4]
sowie [O-190-1] \(\checkmark[M]\) bleiben unberührt.
