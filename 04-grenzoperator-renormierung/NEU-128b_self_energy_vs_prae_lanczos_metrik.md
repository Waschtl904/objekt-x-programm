# NEU-128.B — Self-Energy versus Prä-Lanczos-Metrik

**Stand:** 6. Juli 2026
**Vorgänger:** NEU-125, NEU-127, NEU-128A
**Bezug:** NEU-41, NEU-44
**Ziel:** Klärung, ob die Klasse-B-Self-Energy
\[
\Sigma_N(\beta)=C_N E_N(\beta)^{-1}C_N^\#
\]
als intrinsische Prä-Lanczos-Gewichtung \(W_N\) verwendbar ist.

---

## 1. Ausgangspunkt

NEU-41 liefert für eine Fourier-geladene Primhebung \(\widehat\varepsilon_p\) den Kopplungskandidaten
\[
\Psi_p = \Pi_{J,N}\widetilde\omega_2(\widehat\varepsilon_p, L_3^\circ) \in \mathcal H_{J,N}.
\]
Auf dem nichtausgearteten \(Wres\)-Sektor gilt
\[
C_p C_p^\# = |\Psi_p\rangle\langle\Psi_p|_{Wres}.
\]
Dabei ist \(C_p C_p^\#\) im Allgemeinen kein orthogonaler Projektor, sondern ein positiver Rang-eins-Operator. Die Norm \(|\Psi_p|_{Wres}^2\) bleibt arithmetisch relevant, da sie die Stärke der Primkanal-Kopplung aus der Feshbach-Elimination trägt.

Status: \(\checkmark[M]\) relativ zur gewählten Fourier-Hebung.

---

## 2. Klasse-B-Self-Energy

Für festes \(\beta\) definiert NEU-41 die Self-Energy
\[
\Sigma_N(\beta) = \sum_{p \le N}(1-p^{-\beta})^{-1} C_p C_p^\# = C_N E_N(\beta)^{-1} C_N^\#.
\]
Äquivalent wirkt sie auf \(x\) als
\[
\Sigma_N(\beta)\,x = \sum_{p\le N} (1-p^{-\beta})^{-1} |\langle\Psi_p, x\rangle_{Wres}|^2.
\]
Für reelles \(\beta > 0\) gilt \((1-p^{-\beta})^{-1} > 0\), also besitzt \(\Sigma_N(\beta)\) formal eine positive Gram-Faktorisierung
\[
\Sigma_N(\beta) = A_N A_N^\#, \qquad A_N = C_N E_N(\beta)^{-1/2}.
\]
Damit ist \(\Sigma_N(\beta)\) ein Klasse-B-Objekt: Die Positivität stammt nicht aus bloßer formaler Gram-Geometrie, sondern aus der arithmetischen Feshbach-Kopplung der Primkanäle.

Status: \(\checkmark[M]\) für festes reelles \(\beta > 0\), relativ zur Hebung.

---

## 3. Ebenenproblem: post-Krylov statt prä-Lanczos

Der gesuchte Operator aus NEU-125 muss auf der Prä-Lanczos-Feshbach-Ebene wirken:
\[
W_N : \mathcal H_{Fesh,N} \to \mathcal H_{Fesh,N}, \qquad B_N \mapsto W_N^{1/2} B_N W_N^{1/2}.
\]
NEU-41 konstruiert jedoch
\[
C_p C_p^\# : \mathcal H_{J,N} \to \mathcal H_{J,N},
\]
denn bereits in der Definition von \(C_p\) erscheint die Jacobi-Projektion \(\Pi_{J,N}\). Damit liegt \(\Sigma_N(\beta)\) nach der Krylov-/Lanczos-Selektion, nicht davor.

\[
\boxed{
\Sigma_N(\beta) \text{ ist eine Jacobi-seitige Klasse-B-Self-Energy, aber noch keine Prä-Lanczos-Gewichtung.}
}
\]

Status des \(W_N\)-Anspruchs: \(?[O]\).

---

## 4. Richtungsasymmetrie

Der entscheidende Richtungsunterschied lautet:
\[
C_p C_p^\# : \mathcal H_{J,N} \to \mathcal H_{J,N},
\]
aber ein prä-Lanczos Gram-Operator müsste die Form
\[
A_N^\# A_N : \mathcal H_{Fesh,N} \to \mathcal H_{Fesh,N}
\]
haben. NEU-41 liefert also den Operator auf der Zielseite der Kopplung, nicht auf der Ausgangsseite:
\[
C_N C_N^\# \quad \text{ist post-Jacobi,}
\]
während
\[
C_N^\# C_N \quad \text{oder allgemeiner } A_N^\# A_N
\]
ein möglicher Prä-Lanczos-Kandidat wäre.

Status: \(\checkmark[M]\) als Ebenendiagnose.

---

## 5. β-Fixierungsbarriere

Für eine positive Metrik \(W_N > 0\) muss der Gewichtungsparameter fest und real positiv sein.

| Regime von \(\beta\) | Status von \(\Sigma_N(\beta)\) | Konsequenz |
|---|---|---|
| \(\beta > 0\) reell, fest | positive Koeffizienten | \(W_N\)-Kandidat formal möglich |
| \(\beta = \tfrac{1}{2} + iz\) | komplexe Koeffizienten | keine positive Metrik |
| \(\beta = s\) mitlaufend | Weyl-/Resolventen-Self-Energy | kein festes \(W_N\) |

Daher muss vor jeder \(W_N\)-Konstruktion entschieden werden, ob \(\beta\) ein fester geometrischer Parameter ist oder mit dem Spektralparameter läuft. Falls \(\beta = s\), ist \(\Sigma_N(\beta)\) gerade Teil der Weyl-/Resolventenstruktur und kann nicht zugleich die feste positive Prä-Lanczos-Metrik sein.

Status: \(\checkmark[M]\) als Warnkriterium, \(?[O]\) als programmatische Entscheidung.

---

## 6. Hebungsabhängigkeit

NEU-41 setzt eine Fourier-geladene Primhebung \(\widehat\varepsilon_p\) voraus. Gesichert ist die Konstruktion nur relativ zu dieser Wahl. Die benötigte Intrinsizität wäre:
\[
\widehat\varepsilon_p \sim \widehat\varepsilon_p'
\Longrightarrow
C_p C_p^\# = C_p' C_p'^\# \quad \text{im } Wres\text{-Quotienten.}
\]
Diese Hebungsunabhängigkeit ist in NEU-41 als Bedingung 41.4 formuliert, aber nicht bewiesen.

Status: \(?[O]\).

---

## 7. Minimalbedingungen für NEU-44

NEU-44 muss die relative Weil-Paarung / Primkantenstruktur unter drei verschärften Fragen prüfen.

**Bedingung 1 — Prä-Lanczos-Lift**

Existiert ein intrinsischer positiver Operator \(W_N : \mathcal H_{Fesh,N} \to \mathcal H_{Fesh,N}\) oder eine Faktorisierung \(W_N = A_N^\# A_N\) auf der Prä-Lanczos-Ebene, sodass die Jacobi-seitige Self-Energy als Projektion oder Schatten erscheint?

Minimalform:
\[
\Pi_{J,N} W_N \Pi_{J,N}^\# \sim \Sigma_N(\beta).
\]
Stärker:
\[
\Pi_{J,N} W_N^{1/2} B_N^\Lambda W_N^{1/2} \Pi_{J,N}^\#
\]
erzeugt nach Lanczos die gewünschte Jacobi-Renormierung.

**Bedingung 2 — fixer positiver Parameter**

Der Parameter \(\beta\) muss unabhängig vom Spektralparameter \(s\) gewählt werden können, etwa als fester geometrischer Normierungspunkt \(\beta = \beta_0 > 0\). Andernfalls bleibt \(\Sigma_N(\beta)\) eine Weyl-Funktion und keine Metrik.

**Bedingung 3 — Zweistufen-Kontrolle**

Die Gewichtung darf nicht nur den ersten Jacobi-Koeffizienten retten. Erforderlich ist mindestens:
\[
b_{1,N}^{W} \asymp 1,
\]
und zugleich
\[
\frac{b_{2,N}^{W}}{b_{1,N}^{W}} = O(1).
\]
Eine reine \(b_1\)-Rettung verschiebt die Doppelbarriere nur um eine Stufe und löst sie nicht.

---

## 8. Entscheidungssatz

\[
\boxed{
\Sigma_N(\beta) = C_N E_N(\beta)^{-1} C_N^\# \text{ ist eine Klasse-B-Self-Energy auf } \mathcal H_{J,N}.
}
\]

\[
\boxed{
\text{Für festes reelles } \beta > 0 \text{ besitzt sie eine positive Gram-Faktorisierung } \Sigma_N(\beta) = A_N A_N^\#.
}
\]

\[
\boxed{
\text{Der Status als Prä-Lanczos-Gewichtung } W_N \text{ bleibt offen.}
}
\]

Die offenen Hindernisse sind:
- Verwendung von \(\Pi_{J,N}\) bereits in der Definition von \(C_p\);
- Hebungsabhängigkeit der Fourier-geladenen Primkanäle;
- ungeklärte Fixierung von \(\beta\);
- fehlende Zweistufen-Kontrolle von \(b_{1,N}^W\) und \(b_{2,N}^W / b_{1,N}^W\).

\[
\checkmark[M] \quad \text{für Klasse-B-Self-Energy,}
\]
\[
?[O] \quad \text{für Prä-Lanczos-Metrik.}
\]

---

## 9. Entscheidungsbaum

\[
\text{NEU-44: relative Weil-Paarung / Primkantenstruktur}
\]

Drei Prüffragen:
1. Hebt \(C_N E_N^{-1} C_N^\#\) vor \(\Pi_{J,N}\)?
2. Ist \(\beta = \beta_0 > 0\) fest wählbar?
3. Gilt \(b_{1,N}^{W} \asymp 1\) und \(b_{2,N}^{W}/b_{1,N}^{W} = O(1)\)?

Falls ja:
\[
\boxed{\text{NEU-128-Konstruktion möglich.}}
\]

Falls mindestens eine Bedingung scheitert:
\[
\boxed{\text{Die Feshbach-Lanczos-Route bleibt post-Jacobi und löst die Doppelbarriere nicht.}}
\]

---

## 10. Fazit

NEU-41 bestätigt den wichtigsten positiven Baustein: arithmetisch geladene positive Self-Energy. Aber NEU-41 liefert noch nicht den entscheidenden fehlenden Operator: intrinsische positive Prä-Lanczos-Metrik.

Der nächste mathematische Prüfstein ist daher NEU-44:

\[
\boxed{
\text{Kann die relative Weil-/Primkantenstruktur die Jacobi-seitige Self-Energy vor Lanczos heben?}
}
\]

Damit ist die Route sauber zugespitzt: NEU-44 entscheidet nicht mehr allgemein „ob Klasse B interessant ist", sondern nur noch, ob Klasse B vor \(\Pi_{J,N}\) lebt und die Doppelbarriere wirklich verändert.
