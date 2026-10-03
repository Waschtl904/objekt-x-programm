# Objekt X – Gesamtüberblick

**Projektpriorität:** Zuerst Objekt X gemäß seiner vollständigen Arbeitsdefinition
konstruieren, danach den möglichen RH-Anschluss verfolgen. Die
[Forschungsstrategie](OBJEKT_X_FORSCHUNGSSTRATEGIE.md) begründet die konstruktive
Fortsetzung als Hauptaufgabe; [NEXT_GATES](NEXT_GATES.md) enthält die operative Reihenfolge.

**Forschungsstand und Folgeuntersuchungen:** 3. Oktober 2026

**Frühere integrierte Forschungsbasis:** `83c00ddfe161563f35b31b4ae570faede0834b82` ([PR #204](https://github.com/Waschtl904/objekt-x-programm/pull/204)); ergänzt durch die unten ausgewiesenen Y-Kernel- und H₀-Pakete.
Registry- und Reviewstatus stehen in [CURRENT_STATE](CURRENT_STATE.md).
Der Beweisanker des Direct-Line-Blocks bleibt der Research-Head `c519a1aa58a61d2abe7d5670a2bb5bb642aa2a33`; der aktuelle Main-Head wird live gelesen.

**Zweck:** Überblick über klassische Grundlagen, projektinterne Herleitungen, Ausschlüsse, endliche positive C1-Geometrie und offene globale Schritte. Für eine Prüfung der Belege siehe den [Leitfaden zur externen Begutachtung](EXTERNE_BEGUTACHTUNG.md).

> **Kurzfassung:** Objekt X ist noch nicht vollständig konstruiert und RH ist nicht bewiesen. Der dokumentierte Ansatz verbindet eine physische finite Weil-Form, einen gemeinsamen Prime-/Gamma-Spektralmediator, eine exakte Defektreduktion und mehrere streng positive endliche Kammern mit kompatiblen Transporten. Die projektinternen Ergebnisse sind zur externen Prüfung offen.

---

## 1. Ausgangspunkt

Objekt X begann als sokratischer Fragenkatalog zur Riemannschen Vermutung. Daraus entstand ein Forschungsjournal mit mehreren hundert NEU-Knoten, später die Papers P01–P12 und schließlich die heutige source-first C0/C1-Architektur.

Die Entwicklung war nicht linear. Viele Kandidaten wurden getestet, typisiert, widerlegt oder auf einen kleineren gültigen Scope zurückgestuft. Der heutige mathematische Kern ist deshalb das Ergebnis einer langen Kette aus Konstruktionen **und** No-Gos.

---

## 2. Was klassische Mathematik ist

Das Programm verwendet bekannte Theorie, insbesondere:

- funktionale Gleichung und explizite Formel der Zetafunktion;
- das Weil-Kriterium für RH;
- Mellin- und Fouriertransformation;
- Bost–Connes;
- Herglotz–Nevanlinna, Bochner–Schwartz und Benedetto–Joyner;
- Kato/KLMN;
- Schurkomplement- und Feshbach-Methoden;
- Courant–Fischer-Minmax;
- Suzukis finite Weil-Operatoren;
- externe Primzahlsätze in kurzen Intervallen, wo sie ausdrücklich gebunden werden.

Diese Sätze und Methoden werden **nicht** als projektinterne Originalleistung beansprucht.

---

## 3. Klassische Grundlagen und projektinterne Ableitungen

Die klassischen Sätze tragen die Untersuchung. Das Repository entwickelt
darauf aufbauend konkrete Kandidatenarchitekturen, Ausschlüsse,
Defektreduktionen, Transportgesetze und finite Positivitätsbeweise.
Ihre Einordnung als projektinterne Herleitung ist von einer durch
Literaturvergleich und externen Review bestätigten Neuheit zu unterscheiden.

Ein klassischer Ausgangspunkt ist etwa

```math
B_W\ge0
\quad\Longleftrightarrow\quad
\mathrm{RH}.
```

Im Projekt wird die konkrete Konstruktion untersucht:

```math
q_A(u,v)
=
\langle T_Au,T_Av\rangle
-
\langle D_Au,D_Av\rangle,
```

mit Defekttransfer

```math
R_A(T_Au)=D_Au
```

und der exakten Identität

```math
\boxed{
q_A(u,v)
=
\langle T_Au,(I-R_A^*R_A)T_Av\rangle.
}
```

Zu prüfen sind die konkrete Konstruktion des gemeinsamen Mediators, die
Wohldefiniertheit des Defekttransfers und die Voraussetzungen dieser Identität.
Die gebundenen Beweispakete enthalten die entsprechenden Herleitungen.

---

## 4. Dokumentierter Audit und Korrekturen

Der im Repository geführte [Gesamtaudit](OBJEKT_X_UNABHAENGIGER_GESAMTAUDIT.md)
dokumentiert Prüfungen und Korrekturen zentraler Beweislinien. Dazu gehören:

- Vorzeichen des archimedischen Skalierungsgenerators;
- logarithmischer Koordinatenwechsel;
- Gamma-Normierungs- und Fourier-Shiftfehler;
- eine unzulässige exponentielle Schwartz-Schwanzabschätzung;
- zu starke Typbehauptungen in frühen adelischen Knoten;
- die falsche Ganzadel-Projektion in P02;
- eine zirkuläre RH-Typisierung des Herglotz-Blocks in P07;
- das Vorzeichen des Suzuki-Spektralbodens;
- überstarke Kanonizitätsbehauptungen bei lokalen Shifts und Phasen.

Diese Korrekturen sind bei der Lektüre älterer Kandidaten zu berücksichtigen.
Der Audit hat einen eigenen datierten Prüfumfang. Sein Titel ist keine
Bestätigung einer abgeschlossenen externen Gesamtbegutachtung;
`EXTERNAL_REVIEW_OPEN` bleibt maßgeblich.

---

## 5. Ausschlüsse benannter Kandidatenklassen

Im aktuellen Survivor-Register stehen zwei explizit als projektinterne No-Gos klassifizierte Resultate.

### 5.1 Kurze physische Reichweite plus endlicher Rang

Für Readouts der Form

```math
T_A=L_A+K_A
```

mit physisch zu kurzer Reichweite von $L_A$ und endlichem Rang von $K_A$ wird die gesamte genau benannte Kandidatenklasse ausgeschlossen. Der vollständige Gamma-Mischkern trägt zwischen getrennten Mellin-nulligen Quellenblöcken beliebig hohen Rang.

Das ist **kein** universelles No-Go gegen alle nichtlokalen Readouts.

### 5.2 Einzelne Prime-Power-Kanäle sind keine positiven Gramblöcke

Jeder strikt aktive einzelne signierte Prime-Power-Kanal nimmt auf zulässigen Quellen beide Vorzeichen an. Ein isolierter Kanal kann daher weder in seinem ursprünglichen noch im umgekehrten Vorzeichen als eigene positive Gramkomponente dienen.

Die mathematische Konsequenz ist konstruktiv wichtig: Die Prime-Kanäle müssen in einer gemeinsamen gekoppelten Geometrie erscheinen.

---

## 6. Weitere Grenzen verwendeter Ansätze

### Haar-$L^2$

Auf dem konkreten Haar-$L^2$-Testkern ist Semibeschränktheit der vollständigen Weil-Form bereits RH-äquivalent. Unter RH ist dieselbe Form dort nicht abschließbar. Der naive Kato-/KLMN-Abschluss auf Haar-$L^2$ scheidet daher als Objekt-X-Geometrie aus.

### Adelischer Pullback

Der adelische Amplitudenport ist ein echter RH-freier surjektiver Port. Für seinen Pullback gilt aber exakt

```math
B_W^{\rm adel}\ge0
\quad\Longleftrightarrow\quad
B_W\ge0.
```

Der Port transportiert das Problem, erzeugt aber keine neue Positivität.

### Suzuki-Shift

Jede finite Suzuki-Stufe lässt sich durch Verschiebung unter ihren Spektralboden positiv machen. Ein gemeinsamer Shift für alle Horizonte wäre dagegen bereits RH-relevant. Lokale Shiftpositivität ist also keine globale Objekt-X-Geometrie.

---

## 7. Physische Weil-Form und gemeinsame Defektgeometrie

Die heutige Kernlinie beginnt bei der **physischen signierten Weil-Form**.
Frühere Kandidaten in P02, Haar-$L^2$, Suzuki oder P11 haben ihre jeweils
eigenen, begrenzten Geltungsbereiche.

Für die physischen Zwei-Mellin-Quellen wird ein gemeinsamer Prime-/Gamma-Mediator konstruiert:

```math
T_Au=\frac{m}{\sqrt A}\widehat u,
\qquad
D_Au=\frac{n}{\sqrt A}\widehat u.
```

Bereits unabhängig von der Positivitätsfrage gilt eine quantitative untere Schranke für $T_A$. Damit ist der inverse Quelloperator auf dem abgeschlossenen T-Bild beschränkt und der Defekttransfer $R_A$ wohldefiniert.

Die Positivitätsfrage wird dadurch exakt zu

```math
q_A\ge0
\quad\Longleftrightarrow\quad
\|R_A\|\le1.
```

Strikte Koerzivität ist

```math
I-R_A^*R_A\succeq\eta_A I,
\qquad
\eta_A>0.
```

Erst dann entsteht die invertierbare positive Wurzel

```math
\Delta_A=(I-R_A^*R_A)^{1/2}.
```

Diese Defektgeometrie bildet den Ausgangspunkt der aktuellen C1-Untersuchung.

---

## 8. Projektinterne positive Sätze

Der operative Registerstand enthält mehrere projektintern hergeleitete positive Resultate. Dazu gehören insbesondere:

- Positivität auf frühen endlichen Bändern;
- ein vollständiger beweglicher High-Tail;
- uniforme hohe Defektkontraktion;
- vollständige High-Response-Schurreduktion;
- terminale Positivität bei $A=1$;
- positive C1-Abschlüsse und kompatible Transporte;
- erste positive Kammer bis $A_8=\tfrac12\log8$;
- zweite positive Kammer bis $A_9=\log3$;
- dritte positive Kammer bis $A_{11}=\tfrac12\log11$.

Für die dritte Kammer ist konservativ gebunden:

```math
q_A[u]\ge10^{-50}\|u\|_2^2,
\qquad
1\le A\le A_{11}.
```

Die Ergebnisse sind `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`. Analytische
Herleitungen und zertifizierte Rechnungen sind in den Beweispaketen
ausgewiesen; die unabhängige externe fachliche Prüfung bleibt offen.

---

## 9. Prime-Power-Wände und iterierbare Transportgeometrie

Ein allgemeines Ein-Wand-Lemma liefert für neu aktivierte Prime-Power-Kanäle auf jedem festen endlichen Horizont:

- beschränkte T- und D-Wandtransporte;
- Quotientenabstieg;
- Defektintertwining;
- Formnaturality;
- Gramkompression;
- exakte rohe Cocycles.

Das Wandgesetz transportiert bestehende Struktur, beweist aber **nicht** automatisch die Positivität der neuen Quellrichtungen.

---

## 10. Der allgemeine High-Tail-Satz

Für jeden festen endlichen Horizont $L$ und jeden gewünschten Boden $\delta>0$ existiert ein endlicher Schnitt $N(L,\delta)$, sodass auf dem vollständigen hohen Quellenkern

```math
q_A[u]\ge\delta\|u\|_2^2
```

für alle $1\le A\le L$ gilt.

Die nötige Kodimension darf mit $L$ wachsen.

Die zentrale Konsequenz ist:

```math
\boxed{
\text{Auf jedem festen endlichen Horizont ist die Positivitätsfrage endlich kritisch.}
}
```

Der wiederkehrende schwierige Teil ist der verbleibende **niedrige vollständige Schurrest**.

---

## 11. Was noch nicht bewiesen ist

- keine kofinale positive Familie für $A\to\infty$;
- kein allgemeiner positiver Satz für alle zukünftigen Low-Schurreste;
- kein globaler fensterunabhängiger Readout $T_X$;
- keine globale exakte Weil-Gramidentität;
- Objekt X nicht vollständig konstruiert;
- globale Weil-Positivität nicht bewiesen;
- RH nicht bewiesen.

Kein Merge, kein grüner CI-Lauf und kein lokales Matrixzertifikat darf mit diesen globalen Aussagen verwechselt werden.

---

## 12. Herkunft der Bausteine und Neuheitsprüfung

| Ebene | Einordnung |
| --- | --- |
| Klassische Grundlage | Weil, Mellin/Fourier, Herglotz, Bochner–Schwartz, Kato/KLMN, Schur/Feshbach, Suzuki, externe Primzahlsätze |
| Projektinterne Synthese | adelischer Port, Pullback-Firewall, Haar-$L^2$-Firewall, source-first Fenstergeometrie, gemeinsame Prime-/Gamma-Kopplung |
| Projektinterne Konstruktion | C0-Directed-System, C1-Mediator, Defekttransfer, vollständige High-Response-Schurtechnik, Quadratwurzelkorrektur, Wandcocycle |
| Projektinterne Sätze/No-Gos | endliche Terminal-/Kammerpositivität; No-Go für kurze Reichweite + endlichen Rang; No-Go für isolierte positive Primeblöcke |

Die Tabelle ordnet die Herkunft der dokumentierten Bausteine ein. Ob und
in welchem Umfang die projektinternen Ableitungen über bekannte Resultate
hinausgehen, ist anhand konkreter Aussagen und einschlägiger Literatur
extern zu prüfen.

---

## 13. Kritische Spektralräume und kanonische Ergänzungen

Die [integrierte Forschungsfamilie](../research/x-c1/renewable-low-schur-spectral-2026-09-29/README.md)
enthält sieben aufeinander aufbauende Durchläufe, einschließlich der rigorosen Außenmassenrechnung.
Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

Die alten F-Diagnoseräume lieferten extrem schwache Komplementreserven. Dieser Befund
betrifft die konkrete Raumwahl. Die echte physische Spektralzerlegung liefert bei
`b=q+17||u||²` und Schwelle `q/b=10^-4` genau **5→6→8 kritische Richtungen je Parität**
bei A8→A9→A11. Das vollständige unendliche Spektralkomplement besitzt den robusten
Gap. Die 191/296/285 Zertifikatskoordinaten sind andere Dimensionen.

Physische Nullfortsetzung erhält q und b. Auf dem bereits positiven Horizont ist
`T=P_B J|K_A` injektiv, mit kleinster b-Singularwertschranke
`sqrt(1-alpha_A/beta_B)`. Daraus entstehen die kanonischen Ergänzungen
`E=K_B ⊖_b TK_A` der Dimension 1 bzw. 2 je Parität. Eine Geburt an einer bestimmten
Primzahlpotenzwand wird dadurch nicht lokalisiert.

| Übergang | Minimale Außenmasse gerade | Minimale Außenmasse ungerade |
| --- | --- | --- |
| A8→A9 | [0.9717 %, 2.5620 %] | [5.7863 %, 12.8947 %] |
| A9→A11 | [0.1284 %, 1.2872 %] | [2.1727 %, 8.1344 %] |

Die Grenzen sind rigoros nach außen gerundet und betreffen die kleinste äußere
L2-Masse bei L2-Norm eins. Beim zweidimensionalen E beschränkt die Obergrenze des
Minimums nicht jede Richtung. Die schwächste äußere Richtung bleibt überwiegend im alten Intervall.
Hilfsräume und echte Spektralräume werden durch gerichtete Projektor-/Polargrenzen verbunden.

In `TK_A ⊕ E ⊕ K_B^⊥` ist der robuste Rest q-entkoppelt. Innerhalb K_B gilt
`q_B(Tx,e)=-17<Jx,e>_L2`. Die
[kanonische Schurkopplungsfamilie](../research/x-c1/canonical-schur-coupling-2026-09-30/README.md)
reduziert die relative Kopplung auf Energie und inverse Energie des echten E.
Die neue [gemeinsame Maximiererfamilie](../research/x-c1/canonical-joint-maximizers-2026-09-30/README.md)
verschärft Projektor- und Spektralmomente und schließt damit die beiden
früheren `axis_one`-Alternativen und die ungerade `double`-Alternative aus.

Die Paketberichte bewahren ihren damaligen Veröffentlichungsstand. Für den
aktuellen Integrationsstatus gilt das [Forschungsregister](RESEARCH_STATE.yaml).

Für **A9→A11** ist der tatsächliche größte generalisierte Eigenwert in
beiden Paritäten einfach. Der Gap ist uniform positiv in der zertifizierten
gemeinsamen Familie:

| Parität | β-Gap mindestens | γ-Gap mindestens | Neues Intervall für 1−κ |
| --- | ---: | ---: | --- |
| gerade | 2.2718906e14 | 7.8612134e11 | [2.2405890e-16, 4.3944218e-15] |
| ungerade | 4.2806927e11 | 1.4812085e9 | [9.4820969e-17, 1.1090276e-12] |

Alle Grenzen sind nach außen gerundet. κ bezeichnet die quadrierte
Kopplungsnorm. Exakt gilt `W0=Z0−G0 L0^-1 G0>=0`, `R0=M0+289 W0`
und `β=1+289 γ`. Die γ-Gaps sind ein Korollar des gemeinsamen β-Gaps.
`W0=γ M0` ist in beiden Paritäten ausgeschlossen; gerade liefert auch
`F1<0` einen direkten Ausschluss. Diese Gaps betreffen den generalisierten
Schur-Pencil, nicht das Spektrum des ursprünglichen Energieoperators Q.

Die maximierende Gerade ist für jeden zulässigen Operatorfall eindeutig.
Das bedeutet nicht, dass alle zulässigen Matrizen dieselbe Gerade maximieren.
Gerade gilt `x1/x2` in `[−0.0058383588,0.011976753]` und ein physischer
L2-Winkel in `[−0.850296°,0.381324°]` in der im Beweis definierten
orthonormalen Basis, orientiert mit `x2>0`. Der Winkel gehört zur inversen
Antwort `V0 x`; der Winkel der Schurverschiebung ist damit nicht bestimmt.

**Historischer Zwischenstand vor der Y68-Trennung.** Die damalige
[Projektor-/Transportfamilie](../research/x-c1/canonical-odd-structural-open-2026-10-01/README.md)
bestimmt die Informationsgrenze der dort verwendeten endlichen Relaxation:

1. Die volle gemeinsame b-Grammatrix schließt einen ersten äußeren Zeugen aus.
2. Die notwendige Ordnung `H1>=nuB H0>=0` schließt zwei weitere Beispiele
   durch gemischte negative Richtungen aus.
3. Eine exakte rationale linke Korrektur erhält den jeweiligen Kern von Y
   und erfüllt nun auch die volle gemeinsame Transportordnung.
4. Der rationale Boxtest hat sieben Knoten und vier Blätter. Zwei Blätter
   enthalten explizit zertifizierte Punktzeugen mit mindestens
   **89.987266°** getrennten physischen inversen Antwortrichtungen.

Damit gilt **STRUCTURAL OPEN für diese ursprüngliche endliche Relaxation**.
Die nachfolgende Y68-Schranke schließt einen dieser beiden Zeugen aus;
der Befund überträgt sich deshalb nicht auf die verstärkte Familie. Das ist ein
Existenznachweis aus konkreten gekoppelten Punktzeugen. Das bloße Überleben
einer Intervallbox würde dafür nicht genügen. Eine vollständige gemeinsame
Realisierung sämtlicher ursprünglicher Trial-, Überlappungs- und
Operatordaten durch die beiden Gegenzeugen wird nicht behauptet.

**Ungerade nach Y68: direkte Eigenlinie verbessert bedingte Schnitte.**
Die [Full-Shift-/Primal-Dual-Familie](../research/x-c1/canonical-full-shift-primal-dual-2026-10-02/README.md)
liefert Y68 in [0.0410706614, 0.0725344674] und schließt den alten gedrehten
Gegenzeugen aus. Der frühere STRUCTURAL-OPEN-Nachweis gilt nur für seine
schwächere Relaxation. Der
[adaptive Test](../research/x-c1/canonical-adaptive-odd-angle-2026-10-02/README.md)
mit 255 Knoten bleibt UNRESOLVED. Das nun integrierte
[Direct-Line-Paket](../research/x-c1/canonical-direct-odd-line-2026-10-02/README.md)
erhält gemeinsame Abhängigkeiten in der direkten, zentrierten und affinen
Rechnung. Alle 57 Vergleiche auf denselben 19 Fällen sind reproduziert.

Auf dem **bedingten** zentralen Vier-Y-Schnitt sinkt die Gesamtwinkelobergrenze
von 163.162463° auf **3.405363°**, auf quarter von 165.457773° auf **3.765366°**.
Das belegt dort verlorene Einschließungspräzision der früheren Darstellung.
Alle fünf bekannten zulässigen Punkte bleiben auf dem maximalen Eigenwertast.
Die volle Ausgangsbox und alle acht Diagnoseblätter bleiben **UNRESOLVED**;
die zwei engen Schnitte liefern keinen uniformen Winkelbeweis.

Der anschließende [gemeinsame Y-Kernel](../research/x-c1/canonical-y-kernel-second-order-2026-10-03/README.md)
erhält **Y_L X + Y_R = 0** bis zur zweiten Ordnung mit rigorosem Rest.
Auf denselben 19 Fällen verbessert er central auf ≤2.933357°, quarter auf
≤3.070163° und half auf ≤3.642693°. Die
[Endpunktfolge und H₀-Diagnosen](../research/x-c1/canonical-h0-followups-2026-10-03/README.md)
liefern zusätzlich five_eighths ≤4.933780° und ein exaktes Hindernis für
die ausdrücklich benannte letzte Drei-Cut-Relaxation. Root und die acht
Diagnoseboxen bleiben UNRESOLVED. Der spätere übermittelte Bericht zum
gesamten H₀-Hauptblock (4,5) ist hier noch nicht numerisch reproduziert.

Die [Arbeitsstrategie](OBJEKT_X_FORSCHUNGSSTRATEGIE.md) priorisiert jetzt die
vorwärts gerichtete Schurfortsetzung ohne vorausgesetzte neue
Terminalpositivität. Winkel- und Momentdiagnosen werden für konkret
benannte Schranken eingesetzt. Allgemeine Fortsetzung, A13-Positivität,
kofinale positive Familie und vollständiges Objekt X bleiben offen.
Der mögliche RH-Anschluss folgt erst danach. PR #187 bleibt separat.
Status der reproduzierten Forschungsbefunde: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.

Die bereits positiven Terminals bis A11 bleiben Voraussetzung. Der globale
Verifikationssnapshot ist unverändert; CI-Erfolg ersetzt keinen externen Audit.

---

## 14. Die heutige Beweiskette

```text
klassische Weil-Theorie
        ↓
physische finite signed Form q_A
        ↓
gemeinsamer Prime/Gamma-Mediator (T_A,D_A)
        ↓
Defekttransfer R_A
        ↓
G_A = I - R_A* R_A
        ↓
vollständige High/Low-Schur-Reduktion
        ↓
kammerweise Terminalpositivität
        ↓
Delta_A = G_A^(1/2)
        ↓
positive korrigierte Transporte
        ↓
A8 → q8 → A9 → q9 → A11
        ↓
[offen] allgemeiner Low-Schur-Mechanismus / kofinale Familie
        ↓
[offen] globaler Readout T_X
        ↓
[offen] vollständiges Objekt X mit exakter Weil-Gramidentität
        ↓
danach: möglicher Anschluss an RH
```

---

## 15. Schluss

Dokumentiert sind Ausschlüsse benannter Kandidatenklassen, eine gemeinsame
Prime-/Gamma-Defektgeometrie, vollständige Schurreduktionen und positive
endliche Kammern bis A11. Diese projektinternen Ergebnisse haben jeweils
eigene Voraussetzungen und Belegketten; ihre externe Prüfung bleibt offen.

Der Übergang zu einer kofinalen positiven Familie und zur vollständigen
globalen Weil-Gramidentität ist weiterhin unbewiesen. Davon hängt ab, ob
die endlichen Konstruktionen das globale Ziel des Programms erreichen.

---

## 16. Status- und Leseregel

Die Quellen erfüllen unterschiedliche Rollen:

1. [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml) verwaltet den operativen Status
   und die Bindung an Belege.
2. [CURRENT_STATE.md](CURRENT_STATE.md) und
   [SURVIVOR_REGISTRY.md](SURVIVOR_REGISTRY.md) sind daraus erzeugte Ansichten.
3. Die jeweils gepinnten Beweispakete begründen die mathematischen Aussagen.
4. Der [Gesamtaudit](OBJEKT_X_UNABHAENGIGER_GESAMTAUDIT.md) dokumentiert seine
   datierten Prüfungen und Korrekturen.

Dieser Gesamtüberblick ist eine **Synthese**, keine zusätzliche Beweisautorität.
