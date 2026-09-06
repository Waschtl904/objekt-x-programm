# Objekt X — kanonische Forschungsroadmap v2.1.1

> **Stand:** 2026-09-06  
> **Rolle:** kanonische Abhängigkeits- und Forschungsstrategiekarte.  
> **Keine Beweisautorität:** Dieses Dokument erzeugt keine `✓[M]`-Promotion, kein `independent GREEN`, keinen Freeze, keinen Merge-Anspruch und keine Object-X-/RH-Folgerung.  
> **Volatile Frontdaten:** [ACTIVE_FRONT.yaml](ACTIVE_FRONT.yaml)  
> **Objekt-X-Definition:** [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)  
> **Theorem-/Review-Registry:** [ACTIVE_THEOREM_REGISTRY.md](ACTIVE_THEOREM_REGISTRY.md)  
> **Operative Front:** [CURRENT-FRONT.md](../CURRENT-FRONT.md)  
> **Offene Problemprovenienz:** [OFFENE_PROBLEME.md](../OFFENE_PROBLEME.md)

---

## 0. Autorität und Konfliktregel

Die Roadmap navigiert; sie beweist nichts. Bei Konflikten gilt nach Zuständigkeit:

1. **Objekt-X-Definition:** `OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`.
2. **Theorem-/Reviewstatus:** `ACTIVE_THEOREM_REGISTRY.md`.
3. **Mathematische Gültigkeit:** kanonische Theorem-/Audit-/Paper-/Certificate-Quelle am exakten Head.
4. **Aktuelle operative Front:** `CURRENT-FRONT.md`.
5. **Volatile Stackmetadaten:** `ACTIVE_FRONT.yaml`.

Eine fehlerhafte Roadmap-Zeile darf niemals eine kanonische mathematische Quelle überschreiben; die Roadmap ist stattdessen zu korrigieren.

---

## 1. Drei orthogonale Statusachsen

Die Roadmap importiert die bestehende Registry-Nomenklatur und erfindet kein zweites Statussystem.

### 1.1 Mathematischer Status

Beispiele: `✓[M]`, `?[O]`, `×[M]`, `✓[M]_neg` sowie bestehende Registry-Varianten.

### 1.2 Review-Provenienz

Gemäß Registry insbesondere:

- `AI-GREEN candidate`,
- `independent GREEN (cross-model)`,
- `independent GREEN (certificate)`,
- `independent GREEN (human)`.

Blind-/Nonblind-Provenienz, Prüfer/System, exakter Head und Scope sind nach Registry-Regel getrennt zu dokumentieren.

### 1.3 GitHub-/Governance-Status

Separat zu führen: Draft/Open, Ready, Merged, Closed, frozen head, exakter SHA.

Ein lokales `✓[M]` in einem Draft-PR ist nicht automatisch extern verifiziert. Umgekehrt erzeugt ein positives Review allein keine mathematische Promotion.

---

## 2. Zwei Klassen von DAG-Kanten

Logische Aussagen und Forschungsabhängigkeiten werden getrennt.

### 2.1 Logische Kanten

- `A ⇔ B`: bewiesene Äquivalenz.
- `A ⇒ B`: bewiesene Implikation.
- `A ?⇒ B`: offene, noch zu beweisende Implikation.

### 2.2 Forschungs-/Beweisabhängigkeiten

Nicht-logische Labels:

`uses`, `requires`, `reduces-to`, `candidate-input`, `sufficient-route`, `optional-route`, `repairs`, `blocks-on`, `open-bridge`, `provenance`.

Ein PR ist dabei Provenienz/Container; **DAG-Knoten sind Sätze oder explizite Forschungsfragen, nicht PR-Nummern**.

Unbeschriftete ASCII-Pfeile sind in technischen DAGs nicht zulässig.

---

## 3. Globale Projektarchitektur

Die heutige Struktur ist kein linearer 0→100%-Pfad.

### 3.1 Bereits bekannte Kandidateninputs

```text
A finite-level constraints
        |
        | --candidate-input-->
        v
C genuine X candidate ?[O]

B Strong Terminal result
        |
        | --candidate-input only-->
        v
C genuine X candidate ?[O]
```

Diese Kanten sind **keine logischen Implikationen** und sagen insbesondere nicht, dass A oder B notwendige Bedingungen jeder denkbaren Object-X-Realisierung sind.

### 3.2 R37 bleibt bewusst unverbunden

Für R37/G4c ist die Beziehung zu einer späteren X-Kandidatenarchitektur derzeit `unresolved`. Deshalb wird **keine Kante** von R37/G4c nach C gezeichnet — weder `requires`, noch `candidate-input`, noch eine logische Kante.

### 3.3 X-Pfad

```text
C genuine X candidate ?[O]
        |
        | --requires separate exact proof-->
        v
D exact full Weil-Gram identity ?[O]
        |
        | --component of realization together with
        |    intrinsicity + test class + normalization-->
        v
Object-X realization ?[O]
        |
        | ⇒ by the Gram identity
        v
Q_W(f,f)=||T_X f||² ≥ 0
        |
        | --requires exact Weil-scope verification-->
        v
E Weil-criterion-scope verification ?[O]
        |
        | --unlocks exact classical criterion application-->
        v
RH
```

---

## 4. Front A — finite-level / SW1

Die frühere universelle positive Cross-Gram-/SW1-Route ist in ihrem gebuchten Scope negativ entschieden. Das liefert finite-level Strukturinformation und Constraints, aber weder Strong-Terminal-No-Go noch Object-X-No-Go noch RH-Aussage.

Salvage-/Parameterklassifikationen können weitergeführt werden, sind gegenwärtig jedoch nicht die operative Hauptfront.

---

## 5. Separater R37-/G4c-Pfad

R37/G4c bleibt separat offen. Fortschritt an R38–R43 darf R37/G4c nicht rückwirkend promoten.

Die Beziehung des R37-Pfads zu einer späteren konkreten X-Kandidatenarchitektur ist derzeit **unaufgelöst**; daher wird keine Kante zum X-Pfad gesetzt.

```text
ROADMAP-R37-G4C-DEPENDENCY
  type: research-question
  research_status: open
  math_status: null
```

Frage: Wird R37/G4c für eine spätere X-Kandidatenarchitektur tatsächlich benötigt, oder ist es ein unabhängiger Kandidatenbaustein?

---

## 6. Front B — Strong Terminal / C6

Für jedes feste Paar `0<R<S` ist der operative Endpunkt

\[
L_{R,S}^{T,U}
:=\operatorname{Re}\langle\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R\rangle
\longrightarrow1.
\]

Strong Terminal / C6 bleibt `?[O]`.

### 6.1 R38–R42

Der **exakte Registry-Governance-String** lautet für R38–R42:

```text
FROZEN — independently verified AI-GREEN
```

Die Registry stellt ausdrücklich klar, dass diese projektinterne Freeze-/Reviewer-Buchung nicht automatisch als einer der formal definierten Subtypen `independent GREEN (cross-model/certificate/human)` umgedeutet werden darf.

R38–R42 reduzieren die Future-Transportfrage auf die verbleibende Normalbahn. R43 bleibt OPEN.

---

## 7. R43 — zwei quantitative Ebenen

R43 besitzt zwei unterschiedliche Angriffsebenen:

1. **strukturierter Direktweg** auf der tatsächlichen fixed-normal-/Flagbahn;
2. **stärkerer operatorweiter B-METINC-/Spectral-Width-Weg**.

Ein Decay-Satz auf einem strukturierten Vektor impliziert nicht automatisch einen Operatornorm- oder Spektralbreitensatz.

---

## 8. R43-COND — lokaler Schur-/Resolventenstack

Die volatile PR-/SHA-Struktur steht ausschließlich in `ACTIVE_FRONT.yaml`.

### 8.1 Draft-source IDs versus Registry

Die folgenden lokalen IDs sind **exakte IDs der jeweiligen Draft-Audits** im aktiven Stack. Sie sind auf dem aktuellen `main` noch nicht als neue Zeilen in `ACTIVE_THEOREM_REGISTRY.md` integriert. Die Roadmap darf sie daher als Draft-source IDs referenzieren, aber nicht als bereits registrierte Promotion darstellen.

### 8.2 Strukturierter Schur-Defekt

Draft-source IDs:

```text
R43-COND-C-TWO-SPECIES-RESIDUAL-DECOMPOSITION
R43-COND-SCHUR-NEGATIVE-PART-LEAKAGE-BOUND
```

Für den strukturierten Vektor `v_U=H_U^*E_{X,U}f` wird der negative skalare Schur-Defekt auf gesättigte Leakage reduziert.

**Firewall:** Ein skalarer Schur-Defekt ist nicht automatisch ein Inkrement der komprimierten inversen Metrik.

### 8.3 Halbverschiebungs-/Resolventenvorläufer

Der gestackte Vorläufer fixiert Halbverschiebungs-/Translationskonventionen, terminale Collar-Shell-Geometrie und die relative Resolventendarstellung.

Draft-source IDs umfassen:

```text
R43-TRANSLATION-ANTISYMMETRIC-HALFSHIFT
R43-STRUCTURED-HUB-TERMINAL-COLLAR-SHELL
R43-COND-NORMAL-EQUATION-PRIME-SECTOR-HALFSHIFT
R43-COND-RELATIVE-RESOLVENT-TRANSFER
```

Die frühere Begründung des strikten fixed-pair Bounds `||(L_{U,V})_-||<1` wird durch den nachfolgenden geometrischen-Mittelwert-Audit stärker repariert. Keine cofinale negative Spektraldecay-Aussage wird importiert.

### 8.4 Geometrischer Mittelwert / exakter Resolvententransport

Zentral ist

\[
Q_{U,V}=B_U\#(\iota^*B_V\iota)
\]

und die exakte Kongruenz

\[
\boxed{\iota^*B_V\iota-B_U=-Q_{U,V}K_{U,V}^{\rm Schur}Q_{U,V}.}
\]

Draft-source IDs:

```text
R43-COND-FIXED-PAIR-RELATIVE-SPECTRAL-GAP
R43-COND-GEOMETRIC-MEAN-RESOLVENT-FACTORIZATION
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
```

Für den strukturierten Vektor:

\[
(\Delta s_{\rm cond}^{U,V}(f))_+
\le
\|(I+S^*S)^{-1/2}S^*M Q_{U,V}H_U^*E_{X,U}f\|^2.
\]

**Strategische Konsequenz:** Globale cofinale Kontrolle von `||(L_{U,V})_-||` ist für diese strukturierte Route kein notwendiger Zwischenschritt mehr.

**Firewall:** `Q_{U,V}\le I` ist Normkontraktion, kein Collar-Support- oder Collar-Decay-Satz.

### 8.5 Prime-/Sign-Zerlegung

Draft-source IDs:

```text
R43-COND-NORMAL-SIGN-BRANCH-EXPANSION
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS
R43-COND-GOOD-NORMAL-EXPONENTIAL-DISPLACEMENT-MOMENT
R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL
R43-COND-NORMALIZED-GEOMETRIC-TRANSPORT-CONTRACTION
```

Alle guten Zweige besitzen bei `beta=1/8` ein horizontuniformes exponentielles Verschiebungsmoment. Die einzigen nicht durch diese absolute Summierbarkeit erledigten nichttrivialen diagonal-sum Kanäle sind

\[
\boxed{k=\ell=1},\qquad \boxed{k=\ell=2}.
\]

Für terminal-graph-normalisierte Quellen reduziert sich die resolvententransportierte Leakage schematisch auf

\[
\boxed{\text{hard saturated}+C_*\|\chi_{U,r}Q_{U,V}v_U\|+C_*e^{-r/8}.}
\]

---

## 9. Aktueller quantitative COND-Kern

Offen bleiben:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ?[O]
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY ?[O]
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
```

Für die Forschung dürfen die beiden harten Kanäle zusätzlich getrennt geführt werden:

```text
ROADMAP-HARD11 — research-subquestion — k=l=1
ROADMAP-HARD22 — research-subquestion — k=l=2
```

Diese ROADMAP-Labels sind keine kanonischen Registry-Theorem-IDs und tragen daher keinen Registry-`math_status`.

### 9.1 Quantoren-Firewall

Gebucht/erkennbar: fixes `0<R<S`, strukturierte terminale Quellklasse, Graphnormalisierung wie im aktiven Good-Normal-Draft.

Noch **nicht** erraten werden dürfen:

- erforderliche Relation zwischen `U` und `V`,
- Uniformität in `V`,
- zulässige cofinale Partitionen,
- pointwise-in-`f` versus uniforme Quellkontrolle,
- Wahl von `r=r(U,V)`,
- Reihenfolge der Grenzübergänge.

Unbekannte Quantoren werden ausdrücklich als `unresolved` geführt.

---

## 10. Zwei Wege aus COND

### 10.1 Route S — strukturierter Direktweg

Die DAG-Knoten sind ausschließlich mathematische IDs/Forschungsfragen:

```text
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
        |
        | --used-by-->
        v
R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS
        |
        | --reduces current target to-->
        +---- R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ?[O]
        |
        +---- R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY ?[O]
        |
        v
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
        |
        | --open-bridge-->
        v
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
        |
        | --sufficient-route-->
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGTIGHT ?[O]
```

Die PR-Nummern/Heads zu den Draft-source IDs stehen nur in `ACTIVE_FRONT.yaml` und den jeweiligen Auditquellen.

Der Übergang vom structured leakage decay zu einer direkt B-FLAGDYN-/FD23-kompatiblen Summierbarkeit ist **nicht automatisch** bewiesen.

### 10.2 Route O — stärkerer Operator-/B-METINC-Weg

```text
B-METINC-WIDTH ?[O]
  uses:
    - B-METINC-COND ?[O]
    - B-METINC-GEO  ?[O]
    - B-METINC-NEW  ?[O]

B-METINC-WIDTH ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGMOD ?[O]
```

Diese Route kontrolliert normalisierte metrische Inkremente bzw. Spektralbreiten und ist stärker als bloße structured-vector Kontrolle.

**Firewall:** Scheitert B-METINC-WIDTH, folgt daraus nicht das Scheitern von B-FLAGMOD oder Strong Terminal; dann ist zur genuin projizierten fixed-normal-/Flaggröße zurückzukehren.

---

## 11. B-METINC-WIDTH / FD23

Für

\[
\mathbf H_X^{U,V}=G_{X,U}^{-1/2}(G_{X,V}-G_{X,U})G_{X,U}^{-1/2}
\]

ist der relevante alte/neue Offblock durch die Spektralbreite kontrollierbar, schematisch

\[
\|E_{U,V}\|\le\tfrac12\operatorname{width}(\mathbf H_S^{U,V}).
\]

Der volle modulusseitige Bound enthält pairwise Conditioning-Faktoren.

### Summability-Firewall

Mere Schritt-Kleinheit `||H^{U_k,U_{k+1}}||→0` genügt nicht. Eine hinreichende Partition benötigt insbesondere:

1. summierbare width-/conditioning-Majoranten;
2. fixed-interval projected-tail convergence;
3. die erforderliche FD23-Uniformität.

Punktweise starke Konvergenz allein macht das Zwischenhorizont-Supremum nicht uniform.

```text
FD23-MINIMAL-CONDITION
  type: research-question
  research_status: open
  math_status: null
```

Frage: Was ist die schwächste quantitative Bedingung, die tatsächlich genügt, um die benötigte cofinale FD23-/Flag-Summierbarkeit zu schließen?

Diese Frage optimiert die Route; sie ist kein Pflicht-Theoremknoten. Exponentielles Decay wird nicht zum Selbstzweck erhoben.

---

## 12. B-FLAGDYN / B-FLAGMOD / B-FLAGPHASE

Mit

\[
Q_{m,U}=W_U^*P_mW_U,\qquad
q_m(U)=\langle\varepsilon_R,Q_{m,U}\varepsilon_R\rangle=\|P_mh_U\|^2
\]

lautet der exakte Tightness-Gate

\[
\boxed{\mathrm{B\!-\!FLAGTIGHT}\Longleftrightarrow\lim_m\limsup_U q_m(U)=0.}
\]

B-FLAGDYN bezeichnet die quantitative Kontrolle der echten Terminalvariation dieser festen Quellraumgröße.

Ein stärkerer hinreichender Weg zerlegt in `B-FLAGMOD` und `B-FLAGPHASE` und summiert projizierte Defekte entlang einer geeigneten Terminalpartition.

**Firewall:** Dieser Zwei-Defekt-Weg ist hinreichend; er ist nicht als einzige denkbare Beweisroute zu B-FLAGTIGHT gebucht.

---

## 13. Nach B-FLAGTIGHT — Sign/Orient und Strong Terminal

Unter B-TIGHT/B-FLAGTIGHT gilt im gebuchten Scope der scharfe Resttest

\[
\boxed{\text{Strong Terminal}\Longleftrightarrow\liminf_{T,U\to\infty}L_{R,S}^{T,U}>-1.}
\]

B-SIGN/B-ORIENT bezeichnet die verbleibende normale Vorzeichen-/Orientierungsfront. Strong Terminal bleibt `?[O]`.

---

## 14. Strong Terminal ist noch nicht Objekt X

Ein positiver Abschluss von Strong Terminal/C6 wäre zunächst ein **X-Kandidatenbaustein**.

Es existiert derzeit kein Satz

\[
\text{Strong Terminal}\Longrightarrow\text{Objekt X}.
\]

Ebenso ist Strong Terminal nicht als notwendige Bedingung jeder denkbaren Object-X-Realisierung etabliert. Positive oder negative Ergebnisse an B dürfen daher nicht automatisch als Object-X- oder RH-Ergebnisse kommuniziert werden.

---

## 15. Front C — erster echter X-Kandidat

Die kanonische Arbeitsdefinition von Objekt X ist bereits vorhanden. Ein echter X-Kandidat muss mindestens spezifizieren:

- intrinsische gemeinsame Geometrie,
- Hilbertraum/Mediatorraum,
- kanonische Abbildung `T_X`,
- Prime-Power-Kanal,
- archimedischen Kanal,
- gemeinsame nichtorthogonale Kopplung,
- Testklasse,
- Normalisierung,
- Nicht-Zirkularität.

```text
C — GENUINE X CANDIDATE ?[O]
```

Historische konkrete Architekturen sind Constraints/Kandidaten, nicht die aktuelle Definition von X.

---

## 16. Front D — exakte vollständige Weil-Gram-Identität

Für einen konkret spezifizierten X-Kandidaten ist separat zu beweisen:

\[
\boxed{Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}}
\]

auf der richtigen vollständig normalisierten Weil-Testklasse.

Nicht ausreichend sind ein bloßer positiver Teil, eine nachträgliche GNS-Faktorisierung bereits vorausgesetzter Positivität oder getrennte Prime-/Archimedes-Blöcke ohne gemeinsamen geometrischen Ursprung.

```text
D — EXACT FULL WEIL-GRAM IDENTITY ?[O]
```

---

## 17. Object-X-Realisierung und Positivität

Eine erfolgreiche Object-X-Realisierung bedeutet gemäß Arbeitsdefinition: intrinsische gemeinsame Geometrie + nicht-zirkuläre Konstruktion + korrekte Prime-/Archimedes-Kopplung + geeignete Testklasse/Normalisierung + exakte vollständige Weil-Gram-Identität.

Dann folgt unmittelbar

\[
Q_W(f,f)=\|T_Xf\|_{\mathcal K_X}^2\ge0.
\]

Die Nichtnegativität ist daher kein zusätzlicher schwerer Forschungsübergang **nach** einer vollständigen Object-X-Realisierung; die Arbeit liegt in Konstruktion, Testklasse, Normalisierung und Identität.

---

## 18. Front E — Weil-Kriterium / RH-Rückbindung

Auch nach einer Gram-Realisierung ist exakt zu prüfen:

- welche Weil-Form realisiert wurde,
- welche Testklasse verwendet wird,
- ob sie für das benötigte Weil-Kriterium vollständig ist,
- Fourier-/Gamma-/Pol-Normalisierung,
- welche exakte etablierte Weil-Kriterium-Version auf diesem Scope gilt.

```text
E — WEIL-CRITERION-SCOPE-VERIFICATION ?[O]
```

Erst danach darf ein exakt referenzierter `Q_W≥0 ⇔ RH`-Satz mit passender Testklasse als logische Kante im finalen DAG eingetragen werden.

---

## 19. Rollback-/Falsifikationsregeln

- **Draft-source Schur-Leakage fällt:** abhängige Schur-/Leakage-Argumente neu auditieren; Strong Terminal bleibt offen.
- **Geometric-mean transport fällt:** davon abhängige Good-Normal-/transportierte Teile verlieren ihre Grundlage; unabhängige Branchklassifikation nur nach Re-Audit weiterführen.
- **Good-Normal reduction fällt:** Zwei-Hard-Channel-/Good-Tail-Reduktion fällt; geometrischer Mittelwert bleibt logisch unberührt.
- **Transported-Collar-Decay fällt:** aktuelle Structured-COND-Route scheitert/reparaturbedürftig; Strong Terminal nicht automatisch widerlegt.
- **Hard-channel decay fällt:** aktuelle COND-Decay-Route scheitert; alternative Saturation/Cancellation/direct-projected routes bleiben möglich.
- **B-METINC-WIDTH fällt:** nur globale Operator-/Spectral-Width-Route fällt; direkte projected Flagroute bleibt offen.
- **Strong Terminal negativ:** heutige B-/Future-Transport-Kandidatenroute negativ; ohne Necessity-Satz kein Object-X-No-Go und keine RH-Folgerung.
- **R37/G4c fällt:** konkreter R37-Pfad fällt; R43/Strong Terminal/Object X bleiben ohne Abhängigkeitssatz unentschieden.
- **Ein X-Kandidat fällt an D:** dieser Kandidat ist kein Objekt X; kein universelles Object-X-No-Go.

---

## 20. Pflicht-Ledger für neue Roadmap-Knoten

Theorem-/open-theorem-Knoten:

```yaml
id: <canonical theorem id>
type: <theorem | open-theorem>
math_status: <exact registry/canonical-source value>
review_status: <exact registry value or null if not booked>
source:
  file: <canonical source>
  pr: <if applicable>
  head_sha: <exact SHA if applicable>
scope:
  known: []
  unresolved: []
quantifiers:
  resolved: []
  unresolved: []
depends_on: []
used_by: []
edge_types: []
if_false:
  direct_effect: []
  does_not_imply: []
firewalls: []
```

Reine Roadmap-/Research-Knoten:

```yaml
id: <ROADMAP label>
type: <research-question | research-subquestion | open-bridge>
math_status: null
review_status: null
research_status: <open | parked | resolved>
source: null
scope:
  known: []
  unresolved: []
quantifiers:
  resolved: []
  unresolved: []
depends_on: []
used_by: []
edge_types: []
if_false:
  direct_effect: []
  does_not_imply: []
firewalls: []
```

Unbekannte Quantoren werden als `unresolved` gebucht, nicht geraten.

---

## 21. Gestackte Draft-Arbeit

Explorative Downstream-Arbeit darf auf einem exakten Draft-/Candidate-Head aufbauen, sofern:

1. Parent-SHA explizit ist;
2. Abhängigkeit dokumentiert ist;
3. Parent-Status nicht still hochgestuft wird;
4. bei Fall des Parent-Heads abhängige Claims neu auditiert werden;
5. unabhängige GREEN-Provenienz nur nach Registry-Regel behauptet wird.

`ACTIVE_FRONT.yaml` enthält deshalb neben `parent_pr` auch `parent_head_sha`.

---

## 22. Review, Formalisierung, Numerik

### Review

Vor Merge/Promotion gilt die bestehende Registry-Governance. Menschlicher Fachreview ist spätestens vor öffentlichen Behauptungen eines großen globalen Struktursatzes, einer Object-X-Realisierung oder einer RH-Konsequenz erforderlich.

### Lean / Formalisierung

Nicht mechanisch jedes n-te Lemma. Priorität haben strukturell zentrale Resultate mit großem Downstream-Radius, z. B. geometrischer-Mittelwert-/Resolventenidentität, Riccati-Identitäten für `Q`, finite Branch-/Summationslemmas und zentrale FD23-Kompositionslemmas. Axiom-Inventar bleibt Pflicht.

### Numerik

Gezielt bei falsifizierbaren quantitativen Hypothesen: Gegenbeispiele, Skalierung, Multiplikität, konkurrierende Asymptotiken, Cancellation, Konditionierung. Numerik erzeugt keine Promotion.

---

## 23. Source-of-Truth-Drift

`ACTIVE_FRONT.yaml` hält ausschließlich volatile Stackdaten: Main-Head, aktive PRs, Heads, Parentbeziehungen, GitHub-State, Hauptgate. Theoremstatus bleibt in Registry/kanonischen Quellen.

`CURRENT-FRONT.md`, diese Roadmap, `AKTUELLER_STAND.md` und `ACTIVE_THEOREM_REGISTRY.md` sollen auf `ACTIVE_FRONT.yaml` referenzieren statt dieselben SHA-Werte mehrfach manuell zu pflegen.

Eine technische Validierung soll insbesondere prüfen:

- 40-Hex-Format aller gespeicherten Heads;
- `parent_pr`/`parent_head_sha`-Konsistenz;
- Parent-Head des Stack-Roots gegen den gespeicherten Main-Head;
- keine Duplizierung der in `ACTIVE_FRONT.yaml` gespeicherten volatilen SHA-Werte in den operativen Navigationsdateien.

---

## 24. Aktuelle Default-Forschungspriorität

Die aktuelle COND-Front ist nicht mehr „short/long/sum finden“. Der aktive Good-Normal-Draft hat diese Struktur bereits lokal isoliert.

Prioritäten:

1. gesättigte Kontrolle des Hard Channels `k=l=1`;
2. gesättigte Kontrolle des Hard Channels `k=l=2`;
3. transported collar mass `||chi_{U,r}Q_{U,V}v_U||`;
4. exakte direkte Kompositionsbrücke von structured COND control zu B-FLAGDYN/FD23;
5. parallel: `FD23-MINIMAL-CONDITION` — wie schwach darf die ausreichende Summierbarkeit sein?

R37/G4c bleibt separat offen, aber nicht Default, solange die R43/B-Front produktiv bleibt.

---

## 25. Explizit weiter OPEN

Unter anderem:

```text
R43-COND-TRANSPORTED-COLLAR-MASS-DECAY
R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
B-METINC-COND
B-METINC-GEO
B-METINC-NEW
B-METINC-WIDTH
FD23-UNIF
B-FLAGMOD
B-FLAGPHASE
B-FLAGDYN
B-FLAGTIGHT
B-SIGN / B-ORIENT
Strong Terminal / C6
R43 as a whole
R37/G4c
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope verification
RH
```

Keine lokale Buchung aus dem aktiven Draft-Stack promoviert einen dieser globalen Knoten.

---

# Research Heuristics Appendix — kein Beweisgewicht

Alles ab hier ist Ideengenerator, keine mathematische Prämisse. Bei Konflikt gilt ausschließlich die technische Roadmap und die kanonische Mathematik.

## H1. Pi-/Euklid-Heuristik

Frage nicht nach der stärksten verfügbaren Abschätzung, sondern nach der einfachsten Invariante oder Konstruktion, die den **nächsten echten Gate** erzwingt.

Praktisch:

1. aktuellen offenen Knoten zehn Minuten ohne Fachvokabular beschreiben;
2. fragen, was bei Variation von `U,V,p,k` invariant bleibt;
3. nach einer expliziten Konstruktion statt eines Grenzwerts suchen;
4. in Fachsprache rückübersetzen;
5. Nullresultate dokumentieren.

## H2. Sokratische Gegenfrage

Vor einem neuen Theoremvorschlag mindestens drei konkrete Mechanismen formulieren, durch die der gewünschte Satz falsch sein könnte.

## H3. Rückübersetzung

Nach jeder neuen Operatorabschätzung fragen: Was sagt dieser Bound arithmetisch/geometrisch ohne Operatorsymbole? Wenn nichts Sinnvolles übrigbleibt, prüfen, ob ein strategisch irrelevanter stärkerer Satz verfolgt wird.

## H4. Anamnesis / Literatur

Vor neuer Konstruktion prüfen, ob die Struktur bereits in anderer Sprache existiert: Weil-Positivität, de-Branges/screw-function, geometrische Mittel, Feshbach/Schur, Martingal-/Flaggeometrie. Literaturverweise müssen source-checked werden.

## H5. Kontraposition / Umkehr

Wenn eine globale Schranke schwer ist: Negation konkretisieren, Witness suchen, Firewalls testen und ggf. vom globalen Operatorweg auf eine strukturierte/projected Route wechseln. Das ist Suchstrategie, keine Metatheorem-Folgerung.

---

## Leitsätze

> **Beweise nicht die stärkste Aussage, die du formulieren kannst. Beweise die schwächste Aussage, die der nächste echte Gate tatsächlich braucht.**

> **Ein gescheiterter Beweisweg ist kein gescheitertes Fernziel, solange keine Notwendigkeitskante bewiesen wurde.**

---

## Kurzkarte

PR-Nummern erscheinen hier bewusst nicht als Knoten; ihre Provenienz steht in `ACTIVE_FRONT.yaml`.

```text
[R38,R39,R40,R41,R42]
        |
        | --reduces-to-->
        v
R43 fixed-normal gate ?[O]
        |
        | --optional-route: structured-->
        v
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
        |
        | --used-by-->
        v
[R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL,
 R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS]
        |
        | --reduces current target to-->
        +---- collar mass decay ?[O]
        |
        +---- hard (1,1)+(2,2) saturated decay ?[O]
        |
        v
structured leakage decay ?[O]
        |
        | --open-bridge-->
        v
projected B-FLAGDYN / FD23 ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGTIGHT ?[O]
        |
        | --reduces-to-->
        v
B-SIGN / B-ORIENT ?[O]
        |
        | --current open route-->
        v
Strong Terminal ?[O]
        |
        | --candidate-input only-->
        v
genuine X candidate ?[O]
        |
        | --requires separate proof-->
        v
exact full Weil-Gram identity ?[O]
        |
        | --component-of-->
        v
Object-X realization ?[O]
        |
        | ⇒
        v
Q_W(f,f)≥0
        |
        | --requires exact scope verification-->
        v
Weil criterion / RH bridge
```

Separat und **ohne Kante zum X-Pfad**:

```text
R37 / G4c ?[O]
relation to X route: unresolved
```

**Firewall:** Keine strategische, `candidate-input`-, `uses`-, `open-bridge`- oder `sufficient-route`-Kante darf als logische Implikation gelesen werden.
