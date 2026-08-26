# Objekt X — aktuelle Arbeitsdefinition

> **Status dieses Dokuments:** Single Source of Truth für die aktuelle Objekt-X-Arbeitsdefinition.
> **Konsolidierungsdatum:** 2026-08-26.
> **Epistemische Firewall:** Dieses Dokument definiert den heutigen Suchgegenstand; es
> promotet keinen Kandidaten und behauptet weder Existenz von Objekt X noch RH.

---

## 0. Warum dieses Dokument existiert

Das Repository enthielt mehrere zeitlich echte, aber heute überholte Identifikationen von
Objekt X: insbesondere das Fünfer-Tupel aus dem Juli-Stand sowie die P04/Suzuki-Architektur.
Die P11/R32-Front (FG-1, FG-TR1, Schur-Cross-Gram und die Free-Coordinate-Reduktion CG-FG1)
hat den Suchraum inzwischen anders und wesentlich präziser organisiert.

Dieses Dokument trennt deshalb vier Ebenen:

1. die aktuelle Arbeitsdefinition (Abschnitt 1),
2. etablierte bzw. unabhängig GREEN geprüfte Strukturmerkmale (Abschnitt 2),
3. historische Kandidatenarchitekturen (Abschnitt 3),
4. die Firewall zwischen Kandidatenreduktionen und offenen Sätzen (Abschnitte 4–6).

Die älteren Dateien bleiben als Forschungs- und Beweisprovenienz erhalten. Ihre Aussagen
über konkrete Mechanismen, No-Gos oder route-spezifische Sätze werden durch diese
Reklassifikation **nicht** pauschal aufgehoben. Historisiert wird nur ihre damalige
Identifikation dieser Mechanismen mit Objekt X selbst.

---

## 1. Aktuelle Arbeitsdefinition

> **Objekt X** ist der Arbeitsname für eine bislang nicht konstruierte gemeinsame
> nichtorthogonale Hilbert-/Gram-/Mediator-Geometrie, in der Primzahlpotenz- und
> archimedische Beiträge der Weil-Form aus demselben zugrunde liegenden Mechanismus
> hervorgehen. Objekt X ist derzeit weder als einzelner Operator noch als Spektraltripel,
> festes algebraisches Tupel oder P04/Suzuki-Direktlimes identifiziert. Existenz,
> Eindeutigkeit und ein möglicher Weg zur Riemannschen Vermutung sind offen.

Als Leitform wird ein Hilbertraum \(\mathcal K_X\) und eine Zuordnung \(f\mapsto T_Xf\)
gesucht, so dass die Weil-Form — oder ein präzise ausgewiesener positiver Quadratanteil —
in einer gemeinsamen Gramform erscheint:

\[
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}.
\]

Dabei sollen Prime-Power- und archimedischer Kanal nicht durch einen der bereits
widerlegten **naiven** blockweisen/additiven Klebemechanismen zusammengesetzt werden,
sondern als Projektionen, Cross-Gram-Paarungen oder andere Komponenten derselben
zugrunde liegenden Geometrie entstehen. Dies ist **kein** allgemeiner Satz der Form
„jede algebraische Summe ist unmöglich"; ausgeschlossen sind nur die jeweils bewiesenen
No-Go-Routen.

Die historische Ebene-XVI-Revision 2 und die Datei `objekt_x_minimalaxiome.md` bleiben als
Constraint-/Architekturarchive relevant. Identifikationsaussagen wie das definitorische
Fünfschicht-Profil oder ein fester kategorialer Träger gelten seit dieser Konsolidierung
jedoch nicht mehr als aktuelle Definition von X, sofern sie nicht separat in die heutige
Arbeitsdefinition zurückgebunden werden.

---

## 2. Aktuelle strukturelle Forschungsfront

### 2.1 No-Go-Lehre: keine naive Block-/Additivarchitektur

Die bisherigen Block-Positivitäts- und Additiv-Cross-Term-No-Gos schließen konkrete naive
Klebearchitekturen aus. Ihr positiver Gehalt ist eine Konstruktionsanforderung: Eine
tragfähige Prime-/Archimedes-Kopplung muss die Wechselwirkung bereits in der gemeinsamen
Geometrie bzw. im gemeinsamen Quell-/Mediatorbild tragen.

Diese Aussage ist **route-spezifisch** zu lesen. Sie wird nicht zu einem universellen
No-Go gegen jede denkbare Summen- oder Blockdarstellung hochgestuft.

### 2.2 Schur-Cross-Gram als verbleibender P11/R32-Engpass

Mit

\[
H:=H_{T_0},\qquad
B:=(I+R_{T_0}^*R_{T_0})^{-1},\qquad
\mathscr M:=B^{1/2}H^*
\]

und

\[
\mathscr M_I:=\mathscr M E_I,
\qquad
\mathscr M_A:=\mathscr M E_{\mathcal A}
\]

gilt exakt

\[
\mathscr M_I^*\mathscr M_A
=E_I^*HBH^*E_{\mathcal A}.
\]

Dies ist RB.16 in Cross-Gram-Form. Der echte offene post-P12-Test lautet

\[
\boxed{\ker(\mathscr M_I^*\mathscr M_A)=\{0\}\ ?}
\]

bzw. RB.17. Auf den global bewiesenen P12-Injektivitätsstrata ist dies eine
Nichtorthogonalitäts-/Transversalitätsfrage zwischen dem annularen und dem inneren
Mediatorbild; außerhalb dieser Strata darf die P12-Injektivitätsfolgerung nicht benutzt
werden.

### 2.3 Volle Koordinatennormalform des inneren Beobachtungsoperators

Die bereits vorhandene Bezeichnung

\[
\Phi_R:\mathcal Z_R^+\oplus(\mathfrak G_R\cap\ker\Lambda_R)\to\mathcal N_I
\]

aus EC.8 bleibt der **Kernelparametrisierung** vorbehalten.

Für die volle Drei-Koordinaten-Darstellung verwenden wir daher ausdrücklich ein anderes
Symbol:

\[
\boxed{
\widehat\Phi_R(z,f,h)
:=z+\operatorname{Ev}_R\!\bigl(\Theta_R^{-1}(f,h)\bigr)
}
\]

mit

\[
\widehat\Phi_R:
\mathcal Z_R^+\oplus L^2(0,R)\oplus L^2(\mathcal V_R)
\xrightarrow{\sim}
L^2(-T_0,T_0)^+.
\]

Aus EC.1–EC.9 und TR.17–TR.19 folgt mechanisch

\[
\boxed{E_I^*H\,\widehat\Phi_R(z,f,h)=f.}
\]

Damit ist \(f\) die **beobachtete/sichtbare Koordinate**, nicht die freie Kernelkoordinate.
Der gesamte unsichtbare Raum liegt in der Ebene \(f=0\); seine freien Daten sind

\[
(z,h)\in\mathcal Z_R^+\oplus L^2(\mathcal V_R).
\]

### 2.4 CG-FG1 — Free-Coordinate Schur Reduction

Definiere

\[
\boxed{
\Gamma_R:=\widehat\Phi_R^{-1}BH^*E_{\mathcal A}
}
\]

und, bei der Koordinatenreihenfolge \((z,f,h)\),

\[
\boxed{
\Gamma_I:=\operatorname{pr}_2\circ\Gamma_R.
}
\]

Dann folgt aus der Beobachtungsnormalform und RB.16 exakt

\[
\boxed{
\Gamma_I
=E_I^*HBH^*E_{\mathcal A}
=\mathscr M_I^*\mathscr M_A.
}
\]

Die immer gültige geometrische Form von RB-4 ist deshalb

\[
\boxed{
\ker\Gamma_I=\{0\}
\iff
\Gamma_R^{-1}\!\left(
\mathcal Z_R^+\oplus\{0\}\oplus L^2(\mathcal V_R)
\right)=\{0\}.
}
\]

**Nur auf den global bewiesenen P12-Injektivitätsstrata**, auf denen
\(BH^*E_{\mathcal A}\) und damit \(\Gamma_R\) injektiv ist, darf dies zusätzlich als
Range-Transversalität geschrieben werden:

\[
\boxed{
\ker\Gamma_I=\{0\}
\iff
\operatorname{Ran}\Gamma_R\cap
\left[
\mathcal Z_R^+\oplus\{0\}\oplus L^2(\mathcal V_R)
\right]
=\{0\}.
}
\]

CG-FG1 ist damit eine Kompositionsreduktion, kein Beweis der Transversalität. Die
Provenienz ist präzise

\[
\boxed{\text{EC.1--EC.9} + \text{TR.17--TR.19} + \text{RB.16}.}
\]

### 2.5 DN-1 separat: der starke Dichtheitsweg ist ausgeschlossen

DN-1 betrifft **nicht** die Frage, ob Prime- und Archimedesanteil additiv gekoppelt werden
können. Es zeigt für \(0<R<a\) lediglich, dass der starke Suffizienzweg

\[
\overline{\operatorname{Ran}\mathscr M_I}
=\mathcal K_{\rm med}^{+}
\]

nicht funktionieren kann. Insbesondere folgt aus
\(\ker\mathscr M_I^*\neq\{0\}\) **nicht** automatisch ein Schur-Annihilator.
Der schwächere und weiterhin offene Test bleibt die relative Transversalität

\[
\operatorname{Ran}\mathscr M_A\cap\ker\mathscr M_I^*\stackrel?=\{0\}.
\]

---

## 3. Historische Kandidatenarchitekturen

Diese Architekturen waren reale Forschungsphasen. Sie werden nicht aus der Provenienz
gelöscht, gelten aber nicht mehr als aktuelle Definition von X.

### 3.1 Fünfer-Tupel-Architektur — Stand 26. Juli 2026

\[
\text{Objekt X (historisch)}
=\bigl(A_{2D}^{r},[\tilde\omega_2],[L_3],
\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}},m\xrightarrow{p}pm\bigr).
\]

Siehe Root-`README.md` und Ebene XVI Revision 2. Die dort bewiesenen oder route-spezifisch
gebuchten Einzelresultate behalten ihre jeweilige Provenienz; **historisiert wird die
Identifikation des gesamten Fünfschichtprofils mit X**.

### 3.2 P04/Suzuki-Architektur — Stand 8. August 2026

\[
\text{Objekt X (historisch)}
=\left\{
\mathcal H(T_a^{\rm w}),J_{a,b},
\overline{\mathscr D}_{a,\varepsilon(a)\cdot P}
\right\}_{0<a<b}.
\]

Siehe `00-uebersicht/AKTUELLER_STAND.md`. Auch hier bleiben die jeweiligen analytischen
Teilresultate als historische Forschungsprovenienz bestehen; die Gesamtidentifikation ist
nicht mehr die aktuelle Definition von X.

---

## 4. Firewall — was hieraus NICHT folgt

Keine der obigen Aussagen impliziert:

- dass \(\ker\Gamma_I=\{0\}\) bewiesen ist — dieser Test bleibt `?[O]`;
- dass die Range-Intersection-Form ohne P12-Injektivität verwendet werden darf;
- dass Objekt X existiert;
- dass ein Weg zu RH etabliert ist;
- dass Ebene XVI Revision 2 oder die Minimalaxiome als ganze mathematisch widerlegt wären;
- irgendeine formale Promotion von FG-1, FG-TR1 oder CG-FG1.

---

## 5. Status der zugrunde liegenden Bausteine

| Baustein | Status | Provenienz |
|---|---|---|
| FG-1 | independently GREEN candidate — keine formale Promotion | `audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md` + Exhaustivitätsabschluss |
| FG-TR1 | OVERALL GREEN candidate — keine formale Promotion | `audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md` + unabhängiges Review |
| \(\widehat\Phi_R\)-Normalform | CANDIDATE GREEN als mechanische Komposition | EC.1–EC.9 + TR.17–TR.19 |
| CG-FG1 | CANDIDATE GREEN als Kompositionsreduktion | EC.1–EC.9 + TR.17–TR.19 + RB.16 |
| \(\ker\Gamma_I=\{0\}\) | `?[O]` — offene Schur-Transversalität | RB.17 / RB-4 |
| Closed Range / bounded below / uniforme Winkel | `?[O]` | stärkere quantitative Front |

---

## 6. Notations- und Scope-Regeln

Für den unsichtbaren Fiber-Graph-Raum wird künftig reserviert

\[
\boxed{\mathcal K_R:=\ker(E_I^*H|_+).}
\]

Im Schur-Cross-Gram-Audit bezeichnet dagegen

\[
\boxed{\mathcal N_I:=\overline{\operatorname{Ran}\mathscr M_I}}
\]

einen anderen Raum. Diese Objekte dürfen nicht verwechselt werden. Die historische
`N_I`-Notation in älteren Fiber-Graph-Audits wird in einem separaten, dateiweise geprüften
Bereinigungs-PR ersetzt; eine blinde globale Ersetzung ist unzulässig.

Ebenso bleiben die Symbole getrennt:

- \(\Phi_R\): historische/etablierte Kernelparametrisierung aus EC.8;
- \(\widehat\Phi_R\): volle Drei-Koordinaten-Normalform;
- \(\Gamma_R\): annulares Schurbild in diesen freien Koordinaten;
- \(\Gamma_I=\operatorname{pr}_2\Gamma_R\): sichtbare mittlere Koordinate und RB-4-Operator.

---

**Aktuelle Forschungsfront:** Zuerst ist \(\ker\Gamma_I=\{0\}\) bzw. die äquivalente
Preimage-Transversalität zu entscheiden. Parallel können Objekt-X-Prototypen rückwärts aus
den bereits feststehenden Gram-/Mediator- und No-Go-Daten konstruiert werden. Ein
quantitativer Winkel-/Closed-Range-Satz ist eine spätere, stärkere Stufe und darf nicht in
den aktuellen Injektivitätstest hineingelesen werden.
