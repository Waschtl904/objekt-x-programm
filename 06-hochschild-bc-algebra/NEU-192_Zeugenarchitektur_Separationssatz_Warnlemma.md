# NEU-192 rev. 2 — Abstrakte Zeugenarchitektur, Separationssatz und Warnlemma für invariante Spuren

## Einordnung im DAG

NEU-192 ist ein **algebraisch-kohomologischer Seitenknoten** zu NEU-176.
Das Dokument schließt die abstrakte Zeugenlogik für den Nichtrandtest von [O-176-3] ab
und delegiert die konkrete Zykluskonstruktion an NEU-193.

Durchgehend gilt die redaktionelle Fixierung:

\[
A = B_3^{\mathrm{mod}} = A_{\mathbb Q}.
\]

Der betrachtete Komplex ist

\[
C^\bullet_{\mathrm{fin}} = C^\bullet_{\mathrm{fin}}(A_{\mathbb Q}, A_{\mathbb Q}).
\]

NEU-192 **reöffnet weder** die gesperrten Operatorknoten aus NEU-189 noch den in NEU-190
abgeschlossenen Audit zur Operatorbrücke. Es wird insbesondere keine Abbildung

\[
Z^4(A,A) \to O(H)
\qquad\text{oder}\qquad
HH^4(A,A) \to O(H)
\]

konstruiert oder verwendet. NEU-191 bleibt geschlossen.

---

## [O-192-1] — Typwahl des Zeugen

> **Status: ✓[K]**

Da in NEU-176 ein algebraischer endlicher Gewichtsraumkomplex betrachtet wird,
ist der natürliche Zeugenraum das **algebraische Dual** des festen Gewichtssektors:

\[
\tau_\lambda \in \left(C^4_{\mathrm{fin},\lambda}\right)^\vee
= \operatorname{Hom}_{\mathbb C}\!\left(C^4_{\mathrm{fin},\lambda},\mathbb C\right).
\]

Ein stetiges Dual wird nicht verwendet; in NEU-176 ist keine zusätzliche Topologie
auf \(C^4_{\mathrm{fin},\lambda}\) eingeführt worden.

---

## [O-192-2] — Gewichtsstabilität des Hochschild-Differentials

> **Status: ✓[M]**

**Satz.**
Es gilt

\[
\boxed{
b\!\left(C^3_{\mathrm{fin},\lambda}\right) \subseteq C^4_{\mathrm{fin},\lambda}.
}
\]

**Beweis.**
Aus NEU-174 werden importiert:

1. Stabilität: \(b(C^\bullet_{\mathrm{fin}}) \subseteq C^\bullet_{\mathrm{fin}}\).
2. Kommutation: \(b\,\alpha_t^C = \alpha_t^C\,b\).

Sei \(\Psi \in C^3_{\mathrm{fin},\lambda}\), d.h.
\(\alpha_t^C\Psi = e^{it\lambda}\Psi\) für alle \(t \in \mathbb{R}\). Dann:

\[
\begin{aligned}
\alpha_t^C(b\Psi)
&= b(\alpha_t^C\Psi) \\
&= b(e^{it\lambda}\Psi) \\
&= e^{it\lambda}\,b\Psi.
\end{aligned}
\]

Also trägt \(b\Psi\) das Gewicht \(\lambda\),
d.h. \(b\Psi \in C^4_{\mathrm{fin},\lambda}\). \(\square\)

Die Aussage ist ein mathematischer Import- und Folgerungssatz, kein bloßes Typaxiom.

**Konsequenz für den Zeugenbegriff.**
Die Bedingung

\[
\tau_\lambda\!\restriction_{b\,C^3_{\mathrm{fin},\lambda}} = 0
\]

ist typkorrekt als Bedingung innerhalb des festen Gewichtssektors \(\lambda\) formuliert
und hängt nicht von einer Eigenschaft des gesamten Randraums \(b\,C^3_{\mathrm{fin}}\) ab.

---

## [O-192-3] — Nichtrandlemma

> **Status: ✓[M]**

**Lemma.**
Sei \(\tau_\lambda \in (C^4_{\mathrm{fin},\lambda})^\vee\) mit

\[
\tau_\lambda(b\Psi) = 0 \quad \forall\,\Psi \in C^3_{\mathrm{fin},\lambda},
\qquad
\tau_\lambda(L_{3,\lambda}) \neq 0.
\]

Dann folgt

\[
\boxed{
L_{3,\lambda} \notin b\,C^3_{\mathrm{fin},\lambda}.
}
\]

**Beweis.**
Angenommen \(L_{3,\lambda} = b\Psi\) für ein \(\Psi \in C^3_{\mathrm{fin},\lambda}\).
Dann \(\tau_\lambda(L_{3,\lambda}) = \tau_\lambda(b\Psi) = 0\),
Widerspruch zu \(\tau_\lambda(L_{3,\lambda}) \neq 0\). \(\square\)

**Hinweis zur Vollständigkeit.**
Dieses Lemma schließt [O-176-3] *unter der Voraussetzung*, dass ein konkretes
\(\tau_\lambda\) mit den genannten Eigenschaften konstruiert und berechnet wurde.
Die Konstruktion ist Gegenstand von NEU-193.

---

## [O-192-4] — Kozykel plus Nichtrand impliziert nichttriviale Klasse

> **Status: ✓[M]**

**Satz.**
Es gilt

\[
\boxed{
b\,L_{3,\lambda} = 0
\quad\text{und}\quad
L_{3,\lambda} \notin b\,C^3_{\mathrm{fin},\lambda}
\;\Longrightarrow\;
[L_{3,\lambda}] \neq 0 \in H^4\!\left(C^\bullet_{\mathrm{fin},\lambda}\right).
}
\]

**Beweis.**
Aus \(bL_{3,\lambda}=0\) ist \(L_{3,\lambda}\) ein Kozykel, also
\([L_{3,\lambda}] \in H^4(C^\bullet_{\mathrm{fin},\lambda})\) wohldefiniert.
Wäre \([L_{3,\lambda}]=0\), so gäbe es \(\Psi\in C^3_{\mathrm{fin},\lambda}\) mit
\(L_{3,\lambda}=b\Psi\), im Widerspruch zur Voraussetzung. \(\square\)

**Beweislastverteilung.**
Die offene Stelle ist **nicht** die Gültigkeit dieser Implikation — die ist bewiesen —
sondern das Vorliegen beider Prämissen:

- **[O-176-2]** \(?[O]\): Kozykeltest \(bL_{3,\lambda}=0\) — weiterhin offen in NEU-176.
- **[O-176-3]** \(?[O]\): Nichtrand — wird über [O-192-6] und NEU-193 adressiert.

NEU-192 beweist ausschließlich die abstrakten Implikationen.

---

## [O-192-5] — Methodische Anforderungen an Spuransätze

> **Status: ✓[K]**

Ein Ausdruck der Form \(\tau_\lambda(F) = \operatorname{Tr}_\varepsilon(\mathcal{C}_\lambda(F))\)
ist erst dann ein tragfähiger Zeuge, wenn folgende Daten vollständig angegeben sind:

- eine wohldefinierte Abbildung
  \(\mathcal{C}_\lambda: C^4_{\mathrm{fin},\lambda} \to A_{\mathbb Q}\) oder \(\mathbb{C}\),
- eine Beschreibung, wie die vier Argumentstellen eines Hochschild-4-Kochains
  durch \(\mathcal{C}_\lambda\) ausgewertet oder kontrahiert werden,
- das lineare Auswertungsfunktional (Spur, Charakter oder Paarung),
- ein vollständiger Beweis von \(\tau_\lambda \circ b = 0\),
- eine konkrete Rechnung \(\tau_\lambda(L_{3,\lambda}) \neq 0\).

Eine bloße Spur auf \(A_{\mathbb Q}\) kontrahiert die vier Eingangsargumente nicht automatisch.

### Warnlemma für zeitinvariante Spuren

**Lemma.**
Sei \(\ell: A \to \mathbb{C}\) ein unter der BC-Zeitwirkung invariantes lineares Funktional,

\[
\ell \circ \alpha_t = \ell \qquad \forall\,t \in \mathbb{R},
\]

und sei

\[
\mathcal{C}_\lambda: C^4_{\mathrm{fin},\lambda} \longrightarrow A_\lambda
\]

eine gewichtserhaltende lineare Kontraktion.
Dann gilt für jedes nichttriviale Gewicht \(\lambda \neq 0\):

\[
\boxed{
\ell \circ \mathcal{C}_\lambda = 0.
}
\]

**Beweis.**
Für \(F \in C^4_{\mathrm{fin},\lambda}\) liegt \(\mathcal{C}_\lambda(F) \in A_\lambda\),
also \(\alpha_t(\mathcal{C}_\lambda(F)) = e^{it\lambda}\,\mathcal{C}_\lambda(F)\).
Aus der Invarianz von \(\ell\) folgt:

\[
\begin{aligned}
\ell(\mathcal{C}_\lambda(F))
&= \ell\!\left(\alpha_t(\mathcal{C}_\lambda(F))\right) \\
&= e^{it\lambda}\,\ell(\mathcal{C}_\lambda(F))
\end{aligned}
\]

für alle \(t \in \mathbb{R}\). Da \(\lambda \neq 0\), existiert ein \(t\) mit
\(e^{it\lambda} \neq 1\). Somit muss \(\ell(\mathcal{C}_\lambda(F)) = 0\) gelten.
Da \(F\) beliebig war, folgt \(\ell \circ \mathcal{C}_\lambda = 0\). \(\square\)

**Konsequenz.**
Eine gewöhnliche zeitinvariante Spur oder ein zeitinvariantes Funktional kann
einen geladenen Gewichtssektor nicht detektieren, wenn die vorgelagerte Kontraktion
das Gewicht erhält. Ein möglicher Zeuge muss daher mindestens eine der folgenden
Strukturen besitzen:

- einen dualen Faktor komplementären Gewichts,
- eine geeignet verdrehte Paarung,
- oder eine nicht zeitinvariante Auswertung, deren Randvernichtung separat bewiesen wird.

---

## [O-192-6] — Separationsäquivalenz

> **Status: ✓[M]**

**Satz.**
Setze

\[
V_\lambda = C^4_{\mathrm{fin},\lambda},
\qquad
W_\lambda = b\,C^3_{\mathrm{fin},\lambda}.
\]

Dann gilt rein algebraisch:

\[
\boxed{
L_{3,\lambda} \notin W_\lambda
\;\iff\;
\exists\,\tau_\lambda \in V_\lambda^\vee:\;
\tau_\lambda\big|_{W_\lambda} = 0,\quad
\tau_\lambda(L_{3,\lambda}) \neq 0.
}
\]

**Beweis.**

*Rückrichtung (←):* Folgt unmittelbar aus [O-192-3].

*Hinrichtung (→):* Sei \(L_{3,\lambda} \notin W_\lambda\).
Der Quotientenvektor \(L_{3,\lambda} + W_\lambda \in V_\lambda/W_\lambda\) ist
nach Voraussetzung \(\neq 0\).
Wähle ein lineares Funktional
\(\bar{\tau}_\lambda: V_\lambda/W_\lambda \to \mathbb{C}\)
mit \(\bar{\tau}_\lambda(L_{3,\lambda}+W_\lambda)=1\)
(möglich, da \(L_{3,\lambda}+W_\lambda\) zu einer Basis des Quotienten ergänzt
werden kann).
Setze \(\tau_\lambda := \bar{\tau}_\lambda \circ \pi\) mit der Quotientenabbildung
\(\pi: V_\lambda \twoheadrightarrow V_\lambda/W_\lambda\).
Dann \(\tau_\lambda|_{W_\lambda} = 0\) und \(\tau_\lambda(L_{3,\lambda}) = 1 \neq 0\). \(\square\)

**Epistemische Einschränkung.**

\[
\boxed{
\text{Die Existenz eines beliebigen algebraischen Zeugen ist lediglich eine duale}
}
\]
\[
\boxed{
\text{Umformulierung der Nichtrandbedingung und kein eigenständiges}
}
\]
\[
\boxed{
\text{konstruktives Lösungsverfahren für }[O\text{-}176\text{-}3].
}
\]

Der vollständige algebraische Dualraum ist so groß, dass ein Funktional nach bereits
bekannter Nichtrandheit abstrakt durch Quotientenseparation existiert. Echter
Fortschritt entsteht daher erst durch die Konstruktion eines Zeugen aus einer
natürlichen, eng definierten und konkret berechenbaren Klasse, etwa:

- duale Hochschildzyklen,
- verdrehte Spurfunktionale,
- symmetriekompensierende Paarungen.

Der Separationssatz selbst löst die offene Nichtrandfrage [O-176-3] nicht.

---

## [O-192-7] — Übergabe an NEU-193

> **Status: ?[O] — an NEU-193 übergeben**

Gesucht wird ein expliziter dualer Hochschildzyklus komplementären Gewichts,
der als natürlicher Zeuge für den Nichtrandtest von \(L_{3,\lambda}\) dienen kann.
Zieltyp:

\[
z_{-\lambda} \in Z_4(A,\, A^\vee)_{-\lambda},
\]

mit der angestrebten Bedingung

\[
\langle L_{3,\lambda},\, z_{-\lambda} \rangle \neq 0.
\]

In NEU-192 werden **nicht** ausgearbeitet: die duale Zeitwirkung auf \(A^\vee\),
die endgültige Vorzeichenkonvention des Gewichts, ein konkreter Zykluskandidat,
der Randtest \(\partial z_{-\lambda}=0\) sowie die daraus folgende
Randvernichtungslogik. Diese Punkte gehören ausschließlich in **NEU-193**.

---

## DAG-Knotenübersicht

| Knoten | Inhalt | Status |
|---|---|---|
| [O-192-1] | Typwahl \(\tau_\lambda \in (C^4_{\mathrm{fin},\lambda})^\vee\), kein stetiges Dual | ✓[K] |
| [O-192-2] | Gewichtsstabilität \(b(C^3_{\mathrm{fin},\lambda})\subseteq C^4_{\mathrm{fin},\lambda}\) — Import + Rechenkette aus NEU-174 | ✓[M] |
| [O-192-3] | Nichtrandlemma: \(\tau_\lambda\circ b=0\) und \(\tau_\lambda(L_{3,\lambda})\neq0\) \(\Rightarrow\) \(L_{3,\lambda}\notin bC^3_{\mathrm{fin},\lambda}\) | ✓[M] |
| [O-192-4] | \(bL_{3,\lambda}=0\) und Nichtrand \(\Rightarrow\) \([L_{3,\lambda}]\neq0\) | ✓[M] |
| [O-192-5] | Methodische Anforderungen an Spuransätze; Warnlemma mit vollständigem Beweis | ✓[K] |
| [O-192-6] | Separationsäquivalenz: Nichtrand \(\iff\) algebraischer Zeuge; epistemische Einschränkung | ✓[M] |
| [O-192-7] | Übergabe: dualer Zyklus \(z_{-\lambda}\in Z_4(A,A^\vee)_{-\lambda}\) mit \(\langle L_{3,\lambda},z_{-\lambda}\rangle\neq0\) | ?[O] \(\to\) NEU-193 |

---

## Endstatus

\[
\boxed{
\begin{gathered}
\text{NEU-192 rev. 2 — Zeugenlogik, Separationssatz} \\
\text{und Warnlemma für Spurzeugen}
\qquad \checkmark[K].
\end{gathered}
}
\]

Offen bleiben:

- **[O-176-2]** \(?[O]\) — konkreter Kozykeltest \(bL_{3,\lambda}=0\) in NEU-176.
- **[O-176-3]** \(?[O]\) — kein expliziter natürlicher Zeuge bisher konstruiert.
- **[O-192-7]** \(?[O]\) — an NEU-193 übergeben.

NEU-191 bleibt geschlossen.
Die gesperrten Operatorknoten [O-189-2], [O-189-3], [O-189-4]
sowie der negative Quellenbefund [O-190-1] \(\checkmark[M]\) bleiben unberührt.

---

## DAG-Anschlussbild

\[
L_{3,\lambda} \in C^4_{\mathrm{fin},\lambda}
\xrightarrow{\;[O\text{-}176\text{-}2]:\ bL_{3,\lambda}=0\;}
Z^4_{\mathrm{fin},\lambda}
\xrightarrow{\;[O\text{-}192\text{-}3/6]:\ \text{Nichtrand via }\tau_\lambda\;}
[L_{3,\lambda}] \neq 0.
\]

```
NEU-176 ──[O-176-2, O-176-3]──▶ NEU-192 ──[O-192-7]──▶ NEU-193
```
