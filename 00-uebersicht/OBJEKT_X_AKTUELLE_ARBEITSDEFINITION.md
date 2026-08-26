# Objekt X — aktuelle Arbeitsdefinition

> **Status dieses Dokuments:** Single Source of Truth für die aktuelle Objekt-X-Arbeitsdefinition.
> **Ersetzt nicht:** historische Kandidatenarchitekturen (siehe Abschnitt 3). Diese bleiben im
> Repo erhalten, gelten aber ausdrücklich nicht mehr als Definition von X.
> **Konsolidierungsdatum:** 2026-08-26.

---

## 0. Warum dieses Dokument existiert

Das Root-`README.md` führte bislang unter dem Datumsstempel „26. Juli 2026" eine feste
Fünfer-Tupel-Konzeption von Objekt X als aktuelle Definition. Seitdem hat die P11/R32-Front
(FG-1, FG-TR1, Cross-Gram-Reduktion, CG-FG1) den Suchraum erheblich präzisiert. Dieses
Dokument schließt die dadurch entstandene Lücke zwischen Root-Dokumentation und aktuellem
Forschungsstand.

Es trennt ausdrücklich drei Ebenen:

1. die aktuelle Arbeitsdefinition (Abschnitt 1),
2. bereits mathematisch erzwungene Strukturmerkmale (Abschnitt 2),
3. historische Kandidatenarchitekturen (Abschnitt 3).

---

## 1. Aktuelle Arbeitsdefinition

> **Objekt X** ist der Arbeitsname für eine bislang nicht konstruierte gemeinsame
> nichtorthogonale Hilbert-/Gram-Geometrie, in der Primzahlpotenz- und archimedische
> Beiträge der Weil-Form aus demselben geometrischen bzw. mediatorischen Mechanismus
> entstehen. Objekt X ist derzeit weder als einzelner Operator noch als Spektraltripel
> oder festes algebraisches Tupel identifiziert. Existenz, Eindeutigkeit und ein
> möglicher Weg zur Riemannschen Vermutung sind offen.

Formal gesucht wird ein Hilbertraum \(\mathcal K_X\) und eine Zuordnung \(f\mapsto T_Xf\),
sodass sich die Weil-Form (bzw. ein geeigneter Quadratanteil davon) als

\[
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
\]

schreiben lässt, wobei Prime-Power- und archimedischer Kanal **nicht** additiv getrennt
sind (\(A\neq A_{\rm fin}+A_\infty\)), sondern als unterschiedliche Projektionen bzw.
Gram-Paarungen derselben zugrunde liegenden Geometrie auftreten.

Dies ist eine Arbeitshypothese, keine bewiesene Existenzaussage. Sie ersetzt keine der
Bedingungen in [Ebene XVI — Kontrollblatt](../00-grundlegung/ebene-XVI-objekt-x.md) oder
den [Minimalaxiomen](../00-grundlegung/objekt_x_minimalaxiome.md); sie ordnet lediglich
den aktuellen, aus P11/R32 gewonnenen Erkenntnisstand diesen bestehenden Rahmen zu.

---

## 2. Bereits mathematisch erzwungene Strukturmerkmale

Diese Merkmale folgen nicht aus Analogie oder Plausibilität, sondern aus bewiesenen
bzw. als Kandidat unabhängig geprüften Audits im P11/R32-Strang.

### 2.1 Keine naive additive Kopplung

Mehrere No-Go-Resultate (u. a. Block-Positivität, additive Cross-Terme, dichter innerer
Mediatorweg — `DN-1`, siehe `audits/P11_R32_INNER_DENSITY_NOGO_AUDIT.md`) schließen aus,
dass Prime- und archimedischer Anteil getrennt additiv zusammengesetzt werden können.
Jedes Konstruktionsaxiom für X muss die Wechselwirkung bereits in der Geometrie selbst
tragen, nicht in einer nachträglichen Summe.

### 2.2 Nichtorthogonale Cross-Gram-Struktur statt Kernel-Frage

Der nach der P11↔P12-Rückbindung verbleibende Engpass ist keine reine Kernelfrage mehr,
sondern eine Cross-Gram-Transversalitätsfrage zwischen zwei nichtorthogonalen
Mediatorbildern (`audits/P11_R32_SCHUR_CROSSGRAM_AUDIT.md`, RB.16/RB.17 in
`audits/P11_P12_R32_RUECKBINDUNG_AUDIT.md`). Mit dem Mediator \(\mathscr M=B^{1/2}H^*\) gilt

\[
\mathscr M_I^*\mathscr M_A=E_I^*HBH^*E_{\mathcal A},
\]

und der offene Test ist \(\ker(\mathscr M_I^*\mathscr M_A)=\{0\}\ ?\)

### 2.3 Vollständige Koordinatendiagonalisierung des inneren Beobachtungsoperators

FG-TR1 (`audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md`,
`audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md`) liefert einen expliziten
Isomorphismus

\[
\Phi_R(z,f,h):=z+\operatorname{Ev}_R(\Theta_R^{-1}(f,h)),
\qquad
\Phi_R:\mathcal Z_R^+\oplus L^2(0,R)\oplus L^2(\mathcal V_R)\;\xrightarrow{\sim}\;L^2(-T_0,T_0)^+,
\]

mit der Eigenschaft \(E_I^*H\Phi_R(z,f,h)=f\). Der innere Beobachtungsoperator wird also
zu einer reinen Koordinatenprojektion — kein neues No-Go, aber eine strukturelle
Vereinfachung, die zeigt, dass die verbleibende Freiheit in einer sauber benannten
freien Koordinate \(f\) sitzt.

### 2.4 Free-Coordinate Schur Reduction (CG-FG1)

Durch Komposition von 2.2 und 2.3 folgt

\[
\Gamma_R:=\Phi_R^{-1}BH^*E_{\mathcal A},
\qquad
\Gamma_I:=\operatorname{pr}_2\circ\Gamma_R=E_I^*HBH^*E_{\mathcal A}=\mathscr M_I^*\mathscr M_A,
\]

und damit die geometrische Umformulierung des offenen Tests als

\[
\operatorname{Ran}\Gamma_R\cap\bigl[\mathcal Z_R^+\oplus\{0\}\oplus L^2(\mathcal V_R)\bigr]=\{0\}\ ?
\]

Dies ist eine reine Kompositionsreduktion bereits etablierter Isomorphismen, kein neuer
analytischer Beweisschritt.

---

## 3. Historische Kandidatenarchitekturen

Diese Architekturen waren echte Forschungsphasen des Programms. Sie werden nicht
gelöscht oder umgeschrieben, gelten aber **nicht mehr als aktuelle Definition von X**.

### 3.1 Fünfer-Tupel-Architektur (Stand 26. Juli 2026)

\[
\text{Objekt X (historisch)}=\bigl(A_{2D}^{r},\,[\tilde\omega_2],\,[L_3],\,
\mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}},\,m\xrightarrow{p}pm\bigr)
\]

Siehe Root-`README.md` (vor dieser Konsolidierung) und
[Ebene XVI — Kontrollblatt](../00-grundlegung/ebene-XVI-objekt-x.md).

### 3.2 Weitere in `STATUS.md` referenzierte Hypothese

\[
\text{Objekt X}=\left\{\mathcal H(T_a^{\rm w}),\;J_{a,b},\;\overline{\mathscr D}_{a,\varepsilon(a)\cdot P}\right\}_{0<a<b}
\]

Siehe `00-uebersicht/AKTUELLER_STAND.md`, Abschnitt „Objekt-X-Hypothese".

Beide Architekturen bleiben als dokumentierte Suchphasen wertvoll; sie zeigen, wie sich
der Suchraum entwickelt hat. Für den aktuellen Stand ist ausschließlich Abschnitt 1
maßgeblich.

---

## 4. Firewall — was hieraus NICHT folgt

Keine der obigen Aussagen impliziert:

- dass \(\ker\Gamma_I=\{0\}\) bewiesen ist (dieser Test bleibt `?[O]`);
- dass Objekt X existiert;
- dass ein Weg zu RH etabliert ist;
- irgendeine Promotion von FG-1, FG-TR1 oder CG-FG1 über Kandidatenstatus hinaus.

---

## 5. Status der zugrunde liegenden Bausteine

| Baustein | Status | Provenienz |
|---|---|---|
| FG-1 | independently GREEN candidate — keine formale Promotion | `audits/P11_R32_INVISIBLE_FIBER_GRAPH_CLASSIFICATION_AUDIT.md` |
| FG-TR1 | OVERALL GREEN candidate — keine formale Promotion | `audits/P11_R32_TRIANGULAR_ROW_SPLITTING_AUDIT.md` |
| CG-FG1 (Free-Coordinate Schur Reduction) | CANDIDATE GREEN als Kompositionsreduktion | dieses Dokument, Abschnitt 2.4 |
| \(\ker\Gamma_I=\{0\}\) | `?[O]` — offene Schur-Transversalität | `audits/P11_P12_R32_RUECKBINDUNG_AUDIT.md` (RB-4) |

---

## 6. Notationshinweis

Im Fiber-Graph-/Triangular-Row-Strang bezeichnet

\[
\mathcal K_R:=\ker(E_I^*H|_{\mathscr H^+})
\]

den unsichtbaren Raum. Im Schur-Cross-Gram-Audit bezeichnet \(\mathcal N_I\) einen
**anderen** Raum, den Abschluss des inneren Mediatorbildes \(\overline{\operatorname{Ran}\mathscr M_I}\).
Diese beiden Objekte dürfen nicht verwechselt werden. Siehe auch den entsprechenden
Hinweis in `audits/P11_R32_SCHUR_INVERSE_ELIMINATION_AUDIT.md`, wo \(\mathcal N_I\)
wörtlich als \(\ker(E_I^*H|_{\mathscr H^+})\) verwendet wird — dort ist daher künftig
ebenfalls \(\mathcal K_R\) zu lesen.
