> [!WARNING]
> **HISTORICAL SNAPSHOT — nur die operative Navigation ist ersetzt.**
>
> As of: 2026-09-20
> Nicht zur Bestimmung der aktuellen Forschungsfront verwenden.
> Kanonischer Status: [RESEARCH_STATE.yaml](RESEARCH_STATE.yaml).
> Lesbarer Einstieg: [CURRENT_STATE.md](CURRENT_STATE.md).
> Die chronologischen Nachträge bleiben Forschungsprovenienz; maßgebliche aktuelle Navigation ist das neue Register.
> Mathematische Inhalte werden durch diesen Hinweis nicht pauschal verworfen.

# Transportleiter zu Objekt X

> **Stand:** 19. September 2026  
> **Branch-Anker bei Anlage:** `7d269c7bd3d3507e0109181fcad0b02ddddb2d14`  
> **Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`

## Zweck

Diese Datei trennt den erreichten lokalen Positivitätstransport von den wesentlich stärkeren, weiterhin offenen Stufen bis zu Objekt X. Checker-PASS, CI, Merge und Prüfsummen ändern für sich allein keinen mathematischen Status.

Insbesondere sind zwei Ausdrücke auseinanderzuhalten:

1. **lokaler Positivitätstransport:** Fortsetzung der Positivität vom Endpunkt
   \[
   B=\frac{\log 5}{2}
   \]
   auf ein rechtes Fenster `b=B+h`;
2. **Strong Terminal:** die gesonderte historische P11/R43-Transportfront. Sie ist durch die hier dokumentierte Shell-Schur-Fortsetzung nicht geschlossen.

## Erreichter Sockel

### Eingefrorener Endpunkt auf `main`

Auf `main` bleibt der gemergte PR-#137-Milestone maßgeblich:

```text
main: d455a664c7885eeef9f0d07f246cffc75c1ad267
```

Autorenseitig bewiesen ist

\[
Q_W[u]>10^{-13}\|u\|_2^2
\]

für

\[
0<a\le B=\frac{\log5}{2},
\qquad
0\ne u\in\mathcal W_a.
\]

Dieser eingefrorene Milestone wird ohne konkreten neuen Einwand nicht erneut auditiert.

### Geschlossene Shell-Schnittstelle

Auf der separaten Shell-Schur-Branch sind autorenseitig geschlossen:

- universelle Prime-Power-Familie und exakte Fensterfunktorialität;
- vollständiger gerader Shell-Pivot;
- Identifikation und Entfernung der Trace-Doppelzählung;
- Hilbertraum- und Formbereichs-Bijektion der reduzierten Koordinaten;
- gekoppelte tatsächliche `H^1`-Spurbedingung;
- A-Gauge-Conditioning und exakte Blockkongruenz;
- positive vollständige Shellantwort der bekannten Near-Null-Richtung.

Dabei wird keine dritte Mellinbedingung eingeführt und keine physische Quelle entfernt.

## Erster rechter Transport

Für

\[
0<h=b-B\le 2^{-10^{16}}
\]

ist der gesamte **gerade** reduzierte Core geschlossen. Insbesondere gelten autorenseitig

\[
\Theta_0(b)<1-2\cdot10^{-13}
\]

und

\[
R_0\succeq \frac{331}{500}\,10^{-13}I.
\]

Damit folgt für alle zulässigen geraden Quellen auf diesem extrem kleinen rechten Intervall ein positiver physischer Gap, insbesondere

\[
Q_W[u]>10^{-17}\|u\|_2^2.
\]

Dies ist der erste **Even-All-Source-Transport strikt rechts von `B`**. Er ist kein All-Parity-Satz und darf nicht auf `h<=10^-20` hochgestuft werden.

## Aktueller Even-Frontpunkt

Der aktuelle Branch-Head schließt auf dem vollen Shellintervall

\[
0<h\le10^{-20}
\]

den vollständigen unendlichdimensionalen hohen A-Gauge-Coretail. Für den High/High-Block ist zertifiziert

\[
G_{HH}\preceq\frac{63}{73}I< I.
\]

Die WIDTH-AMPLIFICATION ist dadurch auf folgende Restaufgabe reduziert:

- einen endlichen niedrigen geraden Block von Dimension höchstens `31`;
- Near/Low-Mischterme;
- Low/High-Mischterme;
- die gerichtete rationale Gesamtnormeinschließung des vollständigen Blockoperators.

Eine endliche Matrix ist nur für den vorab exakt definierten Low-Raum zulässig. Sie ersetzt weder den bereits kontrollierten unendlichen Coretail noch den vollständigen Shelltail.

## Forschungsleiter

| Stufe | Mathematisches Ziel | Status am 19.09.2026 |
|---|---|---|
| 1 | Endpunktpositivität bis `B=log(5)/2` | geschlossen auf `main`; autorenseitig |
| 2 | Vollständiger Shell-Pivot und Trace-Quotient | geschlossen; autorenseitig |
| 3 | Formbereich, `H^1`-Gluing und A-Gauge-Kongruenz | geschlossen; autorenseitig |
| 4 | Near-Null-Richtung mit vollständiger Shellantwort | positiv geschlossen; autorenseitig |
| 5 | Even-All-Source für ein rechtes Intervall | geschlossen für `h<=2^(-10^16)` |
| 6 | WIDTH-AMPLIFICATION im Even-Sektor | High-Tail geschlossen für `h<=10^-20`; Low- und Mischblöcke offen |
| 7 | Even-All-Source auf brauchbarer Breite | offen |
| 8 | Odd-All-Source auf demselben Fenster | offen und separat zu beweisen |
| 9 | Lokaler All-Parity-Satz | offen; verlangt Stufen 7 und 8 |
| 10 | Iterierbarer oder globaler Fenstertransport | offen |
| 11 | Connected Unit-Window Coercivity | offen |
| 12 | full C1-GEOM | offen |
| 13 | kanonischer positiver C1-Readout | offen |
| 14 | globaler C0/C1-Vermittler | offen |
| 15 | intrinsischer vollständiger X-Kandidat | noch nicht konstruiert |
| 16 | exakte Weil-Gram-Identität auf der korrekten Testklasse | offen |
| 17 | globale Weil-Positivität | offen |
| 18 | vollständige Anwendung des Weil-Kriteriums / RH | offen; keine Behauptung |

## Begriffliche Statusgrenze

Der bisherige Fortschritt beweist:

```text
lokaler gerader All-Source-Transport rechts von B: JA,
aber bislang nur auf h <= 2^(-10^16).
```

Nicht bewiesen sind insbesondere:

```text
Even-All-Source bis h=10^-20,
Odd-Fortsetzung,
lokaler All-Parity-Transport,
Strong Terminal,
Connected Unit-Window Coercivity,
full C1-GEOM,
kanonischer positiver C1-Readout,
globaler C0/C1-Vermittler,
Objekt X,
globale Weil-Positivität,
RH.
```

## Objekt-X-Zielbild

Objekt X soll nicht bloß eine nachträgliche Faktorisierung einer bereits als positiv angenommenen Form sein. Benötigt wird eine intrinsisch definierte gemeinsame Prime-/Archimedes-Geometrie mit einer kanonischen Abbildung `T_X`, für die auf der vollständigen korrekten Testklasse eine Identität der Form

\[
Q_W(f,g)=\langle T_Xf,T_Xg\rangle_{\mathcal K_X}
\]

bewiesen wird, ohne die gewünschte Positivität oder RH vorauszusetzen.

Die Shell-Schur-Fortsetzung liefert dafür lokale Positivitäts- und Schnittstellenbausteine. Sie ist weder full C1-GEOM noch bereits Objekt X.

## Unmittelbare Arbeitsreihenfolge

1. Den endlichen A-Gauge-Low-Block auf `0<h<=10^-20` exakt einschließen.
2. Near/Low- und Low/High-Mischblöcke vollständig kontrollieren.
3. Erst aus dem gesamten Blockoperator `Theta_A<1` folgern.
4. Danach den Even-All-Source-Satz auf die größere Breite promovieren.
5. Den Odd-Sektor separat behandeln.
6. Erst nach gemeinsamem Even-/Odd-Abschluss einen lokalen All-Parity-Satz formulieren.
7. Danach untersuchen, ob der Transport iteriert oder in eine C1-Geometrie eingebettet werden kann.

## Firewalls

- Keine Hochstufung von `2^(-10^16)` auf `10^-20` ohne Abschluss der Low- und Mischblöcke.
- Kein positiver Odd-Gap ohne neuen Odd-Beweis.
- Keine endliche Matrix als Ersatz für einen unendlichen Tail.
- Scheitern einer hinreichenden Schranke ist kein Negativitätsbefund.
- Nur eine zulässige Quelle mit strikt negativer gerichteter Energieeinschließung wäre ein tatsächlicher Negativitätsbefund.
- Keine Aussage zu `log(7)/2`, `a=1`, full C1-GEOM, Objekt X oder RH ohne neue geschlossene Beweise.
- `main` und der PR-#137-Milestone bleiben ohne konkreten neuen Einwand eingefroren.


---

## Fortschrittsnachtrag — 19.09.2026, Head `7741eca`

> **Kanonischer Branch-Head dieses Nachtrags:**  
> `7741eca6f14bdc3017f6a299aff06eb66db2e697`  
> **main unverändert:** `d455a664c7885eeef9f0d07f246cffc75c1ad267`  
> **Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`

Dieser Abschnitt ist ein **append-only Statusnachtrag**. Er ändert die historischen
Zwischenstände weiter oben nicht rückwirkend. Soweit frühere Abschnitte
`Even-All-Source bis h=10^-20`, den 31-dimensionalen Low-Block oder dessen
Mischblöcke noch als offen führen, sind sie durch den folgenden neueren Stand
überholt.

### WIDTH AMPLIFICATION im Even-Sektor geschlossen

Der Commit `7741eca6f14bdc3017f6a299aff06eb66db2e697` schließt die nach
`7d269c7` verbliebenen Even-Verpflichtungen auf dem gesamten bisherigen
Shellintervall

\[
B=\frac{\log5}{2},
\qquad
0<h=b-B\le10^{-20}.
\]

Für jede nichtverschwindende tatsächliche gerade Quelle

\[
u\in H_0^1((-b,b))
\]

mit genau den beiden ursprünglichen Mellinbedingungen gilt autorenseitig

\[
\boxed{
Q_W[u]>3\cdot10^{-15}\|u\|_2^2.
}
\]

Auf Operatorebene sind außerdem zertifiziert

\[
\boxed{
\Theta_A(b)<1-9\cdot10^{-23},
\qquad
\Theta_0(b)<1-2\cdot10^{-29}.
}
\]

Diese relativen Reserven sind konservative Konsequenzen des absoluten
physischen Gaps und keine Aussagen über optimale Spektralabstände.

### Was gegenüber dem Zwischenstand `7d269c7` zusätzlich geschlossen ist

Der neue Beweis enthält gemeinsam:

- den exakt definierten Low-Core
  \[
  L_0=\operatorname{span}\{P_2,P_4,\ldots,P_{62}\},
  \qquad \dim L_0=31;
  \]
- den vollständigen unendlichen Coretail
  \[
  Y=\overline{\operatorname{span}}\{P_{64},P_{66},\ldots\};
  \]
- die vollständige Low/High-Kopplung;
- die vollständige Low/Profile-Kopplung;
- die vollständige High/Profile-Kopplung;
- sämtliche Near/Low-, Near/High- und Low/High-Mischterme;
- die vollständige physische Normumrechnung;
- die daraus folgende vollständige A-Gauge- und ursprüngliche
  physische-`L^2`-Gauge-Operatoraussage.

Die 31-dimensionale Matrix ist dabei ausschließlich der exakt vorab definierte
Low-Block. Sie ersetzt weder den unendlichen Coretail noch die vollständige
Shell.

Die gerichtete rationale `LDL^*`-Zerlegung des Low-Schurvergleichs besitzt
31 strikt positive Pivots und liefert

\[
R_{\rm cmp}\succeq\sigma_LJ,
\qquad
\sigma_L>1.23769\cdot10^{-12}.
\]

Der vollständige Vergleich einschließlich beider Off-Diagonaloperatoren und
der physischen Rücknorm ergibt den veröffentlichten Gap
`3*10^-15`.

### Aktualisierte Forschungsleiter

| Stufe | Mathematisches Ziel | Neuer Status nach `7741eca` |
|---|---|---|
| 1 | Endpunktpositivität bis `B=log(5)/2` | geschlossen auf `main`; autorenseitig |
| 2 | Vollständiger Shell-Pivot und Trace-Quotient | geschlossen; autorenseitig |
| 3 | Formbereich, `H^1`-Gluing und A-Gauge-Kongruenz | geschlossen; autorenseitig |
| 4 | Near-Null-Richtung mit vollständiger Shellantwort | positiv geschlossen; autorenseitig |
| 5 | erster Even-All-Source-Transport rechts von `B` | geschlossen |
| 6 | High-Tail auf `h<=10^-20` | geschlossen; Zwischenstufe `7d269c7` |
| 7 | WIDTH AMPLIFICATION im Even-Sektor bis `10^-20` | **geschlossen** |
| 8 | Even-All-Source auf `0<h<=10^-20` | **geschlossen**, Gap `>3*10^-15` |
| 9 | Odd-All-Source auf demselben Fenster | **nächster lokaler Gate; offen** |
| 10 | Lokaler All-Parity-Satz | offen; verlangt Odd-Abschluss |
| 11 | Größeres oder iterierbares Fenster | offen |
| 12 | Connected Unit-Window Coercivity | offen |
| 13 | full C1-GEOM | offen |
| 14 | kanonischer positiver C1-Readout | offen |
| 15 | globaler C0/C1-Vermittler | offen |
| 16 | intrinsischer vollständiger X-Kandidat | noch nicht konstruiert |
| 17 | exakte Weil-Gram-Identität auf der korrekten Testklasse | offen |
| 18 | globale Weil-Positivität | offen |
| 19 | vollständige Anwendung des Weil-Kriteriums / RH | offen; keine Behauptung |

### Neuer unmittelbarer Forschungsfrontpunkt

Der nächste lokale Gate ist jetzt eindeutig

\[
\boxed{
\text{ODD CONTINUATION auf }0<h\le10^{-20}.
}
\]

Der Odd-Beweis ist separat zu typisieren und darf nicht allein aus dem
Even-Satz gefolgert werden. Erst nach einem Odd-All-Source-Satz auf demselben
Fenster darf ein lokaler All-Parity-Transport formuliert werden.

Eine weitere Vergrößerung des Even-Fensters kann parallel untersucht werden,
ist aber **kein Ersatz** für den fehlenden Odd-Abschluss.

### Aktualisierte Firewalls

- Kein Odd-Gap ohne eigenständigen Odd-Beweis.
- Kein lokaler All-Parity-Satz vor gemeinsamem Even-/Odd-Abschluss.
- Keine endliche Matrix als Ersatz für einen unendlichen Tail.
- Die geschlossene Even-WIDTH bis `10^-20` darf nicht automatisch auf
  größere rechte Breiten, `log(7)/2` oder `a=1` fortgesetzt werden.
- Strong Terminal im historischen P11/R43-Sinn bleibt eine getrennte offene
  Front.
- Connected Unit-Window Coercivity, full C1-GEOM, ein intrinsischer
  vollständiger X-Kandidat, globale Weil-Positivität und RH bleiben offen.
- `main` und der PR-#137-Milestone bleiben ohne konkreten neuen Einwand
  eingefroren.

### Aktueller Kurzstatus

```text
Even-All-Source bis B+10^-20: JA, autorenseitig geschlossen
WIDTH AMPLIFICATION bis 10^-20: JA, autorenseitig geschlossen
Odd-All-Source rechts von B: OFFEN
lokaler All-Parity-Transport: OFFEN
größere / iterierbare Fenster: OFFEN
Strong Terminal: OFFEN
Connected Unit-Window Coercivity: OFFEN
full C1-GEOM: OFFEN
Objekt X: OFFEN
globale Weil-Positivität: OFFEN
RH: OFFEN
```


---

## Fortschrittsnachtrag — 19.09.2026, Odd- und lokaler All-Parity-Abschluss

> **Mathematischer Anker:** `7741eca6f14bdc3017f6a299aff06eb66db2e697`  
> **Erhaltener vorheriger Leiter-Nachtrag:** `cb56df64ca60c046f99ddba2822e4e216657504d`  
> **Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`

Dieser weitere append-only Nachtrag bewahrt alle historischen Abschnitte.
Die zuletzt als offen geführte Odd-Fortsetzung und der davon abhängige
lokale All-Parity-Satz werden durch das neue
[Odd-Beweispaket](../research/x-c1/odd-profile-continuation-2026-09-19/PROOF.md)
auf dem vollständigen bisherigen Shellfenster geschlossen:

\[
B=\frac{\log5}{2},\qquad 0<h=b-B\le10^{-20}.
\]

### Eigenständiger Odd-Satz

Für jede nichtverschwindende tatsächliche ungerade H1_0-Quelle mit genau
den beiden ursprünglichen Mellinbedingungen gilt

\[
\boxed{Q_W[u]>10^{-12}\|u\|_2^2.}
\]

Der Beweis konstruiert einen eigenen ungeraden, exakt sinh-normalisierten
Momentkorrektor und beweist vollständige Hilbert- und Formkoordinaten samt
der tatsächlichen H1-Gluing-Bedingung. Der niedrige Core ist exakt
`span{P3,P5,...,P63}` mit Dimension 31; der gesamte unendliche Tail
`closure span{P65,P67,...}` und das vollständige Shellprofil bleiben
enthalten. Alle Low/High-, Low/Profile- und High/Profile-Mischterme sowie
die physische Normumrechnung sind bezahlt. Alle 31 gerichteten rationalen
Schur-LDL-Pivots sind positiv.

In diesen nichtredundanten Odd-Core/Profil-Koordinaten sind außerdem

\[
R_o\succeq\frac{1}{2\cdot10^{12}}I,\qquad
\Theta_o<1-2\cdot10^{-12}
\]

für die tatsächlichen vollständigen geschlossenen Operatoren bewiesen.
`Theta_o` ist hier eigenständig definiert und wird nicht mit einem der
Even-Gauge-Operatoren identifiziert.

### Lokaler All-Parity-Satz

Die orthogonalen geraden und ungeraden Projektionen erhalten die gemeinsame
ursprüngliche Mellin-Kernbedingung. Reflexionsinvarianz der gesamten
Nichtpolform macht ihren gemischten Formterm exakt null. Aus dem bestehenden
Even-Gap `3*10^-15` und dem neuen Odd-Gap `10^-12` folgt daher für JEDE
nichtverschwindende tatsächliche H1_0-Quelle mit den ursprünglichen zwei
Mellinbedingungen:

\[
\boxed{Q_W[u]>3\cdot10^{-15}\|u\|_2^2.}
\]

Dies gilt für das gesamte obige rechte Fenster. Exakte isometrische
Nullfortsetzung liefert dieselbe Schranke für alle `0<b<=B+10^-20`.
Der stärkere eingefrorene Endpunkt-Gap auf `b<=B` bleibt erhalten.

### Aktualisierte lokale Leiter

| Stufe | Neuer Status |
|---|---|
| Even-All-Source auf `0<h<=10^-20` | geschlossen; Gap `>3*10^-15` |
| Odd-All-Source auf demselben Fenster | **geschlossen; Gap `>10^-12`** |
| Lokaler All-Parity-Transport | **geschlossen; Gap `>3*10^-15`** |
| Größeres oder iterierbares All-Parity-Fenster | nächster Fenster-Gate; offen |
| Strong Terminal im historischen P11/R43-Sinn | getrennte offene Front |
| Connected Unit-Window Coercivity und full C1-GEOM | offen |
| Intrinsisches Objekt X und globale Weil-Positivität | offen |
| RH | offen; keine Behauptung |

Der lokale All-Parity-Abschluss ist keine Iterationsgarantie. Insbesondere
sind `log(7)/2`, `a=1` und die späteren globalen Stufen nicht erreicht.

### Reproduktion und Grenzen

51 neue rationale Prüfungen bestehen. Der Checker bindet 81 Eingabedateien,
reproduziert die vollständige Even-Kette, berechnet die Odd-Matrizen und
den vollständigen unendlichen Kopplungsgram neu und vergleicht JSON,
Protokoll sowie sieben Payload-Hashes. Die neue endliche Matrix dient
ausschließlich dem exakt definierten 31-dimensionalen niedrigen Raum.

Keine zusätzliche Mellinbedingung, keine A1, keine Quadratur oder
numerischen Eigenwerte als Beweis, keine neue Quellenwahl. Reproduktion
ist keine unabhängige externe Prüfung. `main` bleibt der eingefrorene
PR-#137-Milestone; kein neuer PR, kein Merge.


---

## Fortschrittsnachtrag — 19.09.2026, Restart- und schrumpfende Iterationsstufe

> **Mathematischer Anker:** `a659047e00d024c0daa3991ea59fd21afd9f8793`  
> **Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`

Der lokale All-Parity-Satz ist nicht nur am einmaligen Fenster
`B+10^-20` verfügbar. Das Paket
`research/x-c1/all-parity-shrinking-step-iteration-2026-09-19/`
beweist ein eigenständiges Restart-Lemma auf einem festen lokalen
Endpunktband rechts von `B=log(5)/2`.

### Restart-Lemma

Besitzt ein bereits erreichter Endpunkt `a` auf

`B <= a <= B+10^-2`

einen vollständigen All-Parity-Gap `epsilon>0`, dann kann für jedes
`0<gamma<epsilon` eine explizit kleine neue rechte Shellbreite `h>0`
gewählt werden, so dass am neuen Endpunkt `a+h` wieder der vollständige
All-Parity-Gap mindestens `gamma` gilt.

Die Even- und Odd-Profilkorrektoren, der aktive Prime-Power-Satz
`{2,3,4,5}`, die disjunkte Core-Eingabegeometrie, die vollständige
Core/Profile-Kopplung `<4` und der Profilboden sind auf diesem Band
endpoint-uniform. Nur die zulässige Schrittweite hängt vom ausgegebenen
Gap-Budget `epsilon-gamma` ab.

### Explizite unendliche Kette

Ausgehend von

`b_0=B+10^-20`, `epsilon_0=3*10^-15`

werden

`N_n=4*10^16*2^n`,
`h_n=2^(-N_n)`,
`b_(n+1)=b_n+h_n`

und

`epsilon_n=10^-15*(1+2^(1-n))`

gewählt. Dann ist `b_(n+1)>b_n` für jedes `n`, und am gesamten Endpunkt
`b_n` gilt der vollständige All-Parity-Gap mindestens `epsilon_n`.
Insbesondere bleibt an jedem endlichen Schritt

`epsilon_n>10^-15`.

Die gesamte zusätzliche Breite dieser unendlichen Kette ist kleiner als
`10^-20`; die Schrittweiten schrumpfen sehr stark.

### Präzise Statusgrenze

| Stufe | Neuer Status |
|---|---|
| Local All-Parity bis `B+10^-20` | geschlossen |
| Restart von einem neu positiven Endpunkt | **geschlossen** |
| Unendliche shrinking-step Iteration mit positivem Gap-Floor | **geschlossen** |
| Uniforme positive Schrittweite `h_n>=h_*>0` | offen |
| Nicht-summierbarer / makroskopischer Fenstertransport | offen |
| Übergang über `log(7)/2` mit dem Iterationsmechanismus | offen |
| Connected Unit-Window Coercivity | offen |
| Strong Terminal | getrennt offen |
| full C1-GEOM / Objekt X / globale Weil-Positivität / RH | offen |

Damit ist `Iteration Lemma` nur in der präzisen Form
**shrinking-step restartability** erreicht. Die stärkere Form eines
uniformen positiven Schritts ist nicht bewiesen und darf nicht aus der
Existenz der obigen Kette abgeleitet werden.

### Neuer Frontpunkt

Der nächste strukturelle Gate ist nun:

```text
UNIFORM-STEP / NON-SUMMABLE WINDOW TRANSPORT
```

also entweder

1. eine positive Schrittuntergrenze, die bei wiederholter Anwendung nicht
   gegen null kollabiert, oder
2. eine andere quantitative Window-Amplification, die einen tatsächlich
   makroskopischen Endpunkt erreicht.

Erst ein solcher Mechanismus wäre ein ernsthafter Übergang von lokaler
Restartability in Richtung Connected Unit-Window Coercivity.

## Append 2026-09-19: Fünfzigfaches All-Parity-Fenster und quantitatives Neustartlemma

Aufbauend auf `a659047e00d024c0daa3991ea59fd21afd9f8793` liefert
[`all-parity-window-and-restart-2026-09-19`](../research/x-c1/all-parity-window-and-restart-2026-09-19/README.md)
zwei getrennte Fortschritte. Status bleibt **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Der parallele Nachtrag aus `829019d7e62f936ab4db903bb9c7758edf427609`
mit positivem uniformen Gap-Floor seiner schrumpfenden Kette bleibt
vollständig bestehen. Die unten gewählte Halbungskette ist eine andere,
schwächere Gap-Strategie. Der neue Beitrag dieses Pakets liegt in der
fünfzigfachen tatsächlichen Fensterbreite und der größeren bedingten
Endpunktreichweite bis b<=1 samt Kanal 7, nicht in einer Rücknahme des
bereits eingetragenen positiven Gap-Floors.

Für B=log(5)/2 sind jetzt folgende geschachtelte All-Source-Bereiche
unter genau den ursprünglichen zwei Mellinbedingungen zertifiziert:

| Endpunkt b höchstens | Physischer All-Parity-Gap |
| --- | --- |
| B+10^-19 | >3*10^-15 |
| B+4*10^-19 | >10^-15 |
| B+5*10^-19 | >3*10^-16 |

Der Odd-Gap bleibt jeweils >10^-12. Die maximale neue Breite ist
fünfzigmal so groß wie 10^-20. Beide vollständigen ursprünglichen
Schur-Matrizen und unendlichen Tails werden reproduziert; die Erweiterung
folgt aus einem exakt rationalen zusätzlichen skalaren Schalenabzug.
Die früheren stärkeren Aussagen auf kleineren Intervallen bleiben gültig.
Die früheren relativen A-Gauge-Konstanten werden hier nicht ungeprüft
auf das größere Fenster übertragen.

Das neue bedingte Neustartlemma gilt mit uniformen analytischen Konstanten
für B<=a<b<=1: Aus q_a>=epsilon I, 0<epsilon<=1, und
0<b-a<=2^(-ceil(1600/epsilon)) folgt q_b>=(epsilon/2)I.
Die tatsächliche vollständige Profil-Schur-Norm erfüllt Theta<49/200.
Kontrolliert sind vollständiger Kern, sämtliche Mischblöcke, Formbereiche,
Konditionierung, beide Mellinbedingungen und alle möglichen Kanäle
2,3,4,5,7 einschließlich neu eintretender Schalen-Selbstwechselwirkungen.
Separate mitwandernde Legendre-Tailkonstanten werden durch volle
Kernkoerzivität und volle Kern-Profil-Operatorkontrolle ersetzt.

Ein konkreter Start ist a_0=B+5*10^-19, epsilon_0=3*10^-16. Mit
N_0=5333333333333333334, N_n=2^n N_0 und h_n=2^(-N_n) ist jeder endliche
Schritt a_(n+1)=a_n+h_n mit Gap epsilon_0/2^(n+1) zertifiziert.
Die Breiten erfüllen aber h_(n+1)=h_n^2 und sum h_n<2^(1-N_0).
Die garantierte Kette akkumuliert und ihr Gap geht gegen null. Sie
erreicht insbesondere keinen neuen Prime-Power-Eintritt.

Damit gilt die aktualisierte Leiter:

    lokales All-Parity-Fenster 10^-20
      -> All-Parity-Fenster 5*10^-19
      -> uniformes bedingtes Neustartlemma mit explizitem Gapverbrauch
      -> jeder endliche Schritt einer summierbaren Neustartkette.

**Weiter offen:** Reserveerneuerung beziehungsweise nicht summierbarer
zertifizierter Fortschritt, positiver Grenzendpunkt-Gap dieser Halbungskette, Connected
Unit-Window Coercivity, historisches P11/R43 Strong Terminal, C1-GEOM,
Objekt X, globale Weil-Positivität und RH. Die neue Aussage ist kein
uniform koerziver Transport über unendlich viele Schritte. Ein Scheitern
eines hinreichenden Vergleichs wäre UNDECIDED, keine negative Quelle.

88 neue exakte Prüfungen bestehen. 95 Eingabedateien sind nach Bytezahl, SHA-256 und Git-Blob gebunden;
reproduziert werden die 51/41/38/40/31/28/43/9-Kette und 349 universelle
algebraische Regressionen. Ganzzahlen, rationale Zahlen und gerichtete
Intervalle tragen alle arithmetischen Entscheidungen. Der vollständige
analytische Beweis in `PROOF.md` bleibt extern zu prüfen; Reproduktion
ist kein unabhängiges Audit. Keine neue Quellenwahl, kein A1, keine
dritte Mellinbedingung, keine numerischen Eigenwerte oder Quadratur als
Beweis. Die bisherigen Einträge dieser Leiter bleiben unverändert.


---

## Fortschrittsnachtrag — 19.09.2026, Scalar-Gap-Iterationsbarriere

> **Mathematischer Anker:** `ca3849ab2a5abf6268ee892109a293332c1030e9`  
> **Paralleler Restart-Satz:** `829019d7e62f936ab4db903bb9c7758edf427609`  
> **Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`

Das Paket
`research/x-c1/scalar-gap-restart-summability-barrier-2026-09-19/`
schließt ein negatives Struktur-Gate für die beiden derzeit bewiesenen
skalaren Restartgesetze.

### Exakte Barriere

1. Beim Halbierungs-Restart aus `ca3849a`

```text
epsilon -> epsilon/2,
h <= 2^(-ceil(1600/epsilon))
```

ist jede allein aus diesem Gesetz garantierte unendliche Schrittfolge
summierbar.

2. Beim Target-Gap-Restart aus `829019d` gilt für den Verlust
`m=epsilon-gamma` unter anderem

```text
h <= 2 exp(-16/m).
```

Jede ausschließlich damit erzeugte Folge, deren zertifizierter Gap gegen
einen positiven Grenzwert konvergiert, besitzt summierbare Verluste
`sum m_n<infinity`; daraus folgt elementar `h_n<=m_n^2` für alle
hinreichend großen `n` und damit ebenfalls `sum h_n<infinity`.

Die Aussage betrifft **nur diese beiden hinreichenden skalaren
Zertifikatsmechanismen**. Sie ist kein Negativitätsbefund für die Weil-Form.

### Monotonie-Firewall

Die exakte Nullfortsetzung liefert für den wahren optimalen Gap

```text
lambda(b) <= lambda(a)   für a<=b.
```

"Reserve Renewal" kann daher nicht bedeuten, dass der wahre optimale physische
Gap nach rechts wieder anwächst. Erneuert oder getrennt transportiert werden
müssen interne Reserven: Soft-Schur-, Low-, Tail-, Profil- oder andere
Blockreserven.

### Neuer positiver Frontpunkt

Damit ist die nächste lokale Front enger gefasst:

```text
BLOCK-ADAPTIVE RESERVE RENEWAL / NON-SUMMABLE TRANSPORT
```

Gesucht ist ein Satz, der den kleinen endlichen Soft-Block explizit hält und
die wesentlich größeren Hard-Tail-/Profilreserven separat bezahlt. Alternativ
müsste das Breiten-Gesetz selbst von der exponentiellen
Inverse-Reserve-Abhängigkeit auf eine mildere quantitative Abhängigkeit
verbessert werden.

| Stufe | Status |
|---|---|
| Reale All-Parity-Breite bis `B+5*10^-19` | geschlossen |
| Bedingter Restart bis `b<=1` | geschlossen |
| Shrinking-step Iteration | geschlossen |
| Scalar-gap-only nicht-summierbarer Transport | **durch Barriere ausgeschlossen** |
| Blockadaptive Reserve Renewal | **offen; nächster positiver Gate** |
| Nicht-summierbarer / uniform-step Transport | offen |
| Tatsächlicher Transport bis Kanal 7 | offen |
| Connected Unit-Window Coercivity | offen |
| Strong Terminal | getrennt offen |
| full C1-GEOM / Objekt X / globale Weil-Positivität / RH | offen |

## Append 2026-09-19: Blockadaptive Fortsetzung bis B+5*10^-13

Mathematischer Anker: `ca3849ab2a5abf6268ee892109a293332c1030e9`.
Der parallele Summierbarkeitsbeitrag `6cbef9d` bleibt vollständig erhalten;
eine quantitative Rundungskorrektur dazu steht am Ende dieses Nachtrags.
Status: **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Das neue Paket
[`block-adaptive-profile-transport-2026-09-19`](../research/x-c1/block-adaptive-profile-transport-2026-09-19/README.md)
realisiert die getrennte Behandlung der Blockreserven an einem festen
Core B=log(5)/2. Für alle tatsächlichen komplexen H1_0-Quellen unter genau
den ursprünglichen zwei Mellinbedingungen gilt:

| Rechter Endpunkt höchstens | Physischer All-Parity-Gap |
| --- | --- |
| B+10^-13 | >4*10^-15 |
| B+5*10^-13 | >10^-15 |

Der Odd-Gap ist jeweils >10^-12. Die äußere Breite ist **eine Million
Mal größer** als die bisherige Breite 5*10^-19. Die bessere zertifizierte
Gap-Untergrenze ist eine schärfere Abschätzung, kein Anstieg des wahren
optimalen Gaps unter Nullfortsetzung.

Zwei Verbesserungen tragen den Beweis:

1. Eine Trennung der Core-Eingaben nahe dem Rand und im übrigen Core
   verbessert die vollständige Tail-Profil-Kopplung. Die Eingaben sind
   getrennt; Ausgaben in dieselbe Shell dürfen vollständig ausgerichtet sein.
2. Der gesamte Low-Block wird in seiner eigenen Schur-Energiemetrik
   ausgewertet. Logarithmischer Randterm und konstanter Kopplungsterm
   werden mit ihrem vorzeichenbehafteten Mischterm exakt integriert.
   Der Rest ist auf dem vollständigen Low-Raum und Shellprofil kontrolliert.

Der relative Low-Profil-Abzug dieses benannten Vergleichs liegt auf
dem äußeren Bereich unter 10^-3. Er ist nicht mit der tatsächlichen
vollständigen Profil-Schur-Norm Theta gleichgesetzt. Beide Paritäten,
sämtliche 31 Low-Richtungen, die vollständigen unendlichen Tails und
alle Mischblöcke bleiben erhalten. Das analytische Zweitermodell ist
keine endliche Shellersetzung ohne Fehlerkontrolle.

71 neue exakte Prüfungen bestehen. 103 Eingabedateien sind nach Bytes, SHA-256 und Git-Blob gebunden. Beide
Corematrizen, die vollständigen Gram-Ausdrücke, die Kopplungsvektoren und
vier Vergleiche mit jeweils 31 positiven rationalen LDL-Pivots werden
neu berechnet. Die gesamte Voraussetzungskette aus ca3849a wird ebenfalls
reproduziert. Keine Quellenneuwahl, physische Renormierung, A1, zusätzliche
Mellinbedingung, Quadratur oder numerischen Eigenwerte als Beweis.

Aktualisierter positiver Stand:

    All-Parity-Fenster 5*10^-19
      -> blockadaptives All-Parity-Fenster 5*10^-13
      -> getrennte Low-, Tail- und Profilbudgets an festem Core B.

**Weiter offen:** Erneuerung dieser feineren Reserven an beweglichen
Endpunkten oder gemeinsame Mehrschalenkontrolle mit genügend Gesamtbreite.
Insbesondere folgen daraus kein nicht summierbarer Transport, kein
Erreichen von log7/2, keine Connected Unit-Window Coercivity, kein
historischer Strong Terminal und keine Konstruktion von Objekt X.
Volle C1-GEOM, globale Weil-Positivität und RH bleiben offen. Die
Summierbarkeitsbarriere der früheren reinen Globalgap-Regeln bleibt
qualitativ bestehen. Reproduktion ist kein unabhängiges externes Audit.

### Append-only Korrektur der Ceiling-Abschätzung aus 6cbef9d

Für c=1600/epsilon_0 und N_n=ceil(2^n c) gilt im Allgemeinen nicht
N_n>=2^n ceil(c). Am dort diskutierten epsilon_0=3*10^-16 ist
N_0=5333333333333333334 und N_1=10666666666666666667<2N_0.
Die dortige Zwischenabschätzung h_n<=(2^(-ceil(c)))^(2^n) ist deshalb
in dieser Form nicht gültig.

Die qualitative Schlussfolgerung wird durch K=floor(c) repariert:
Für das tatsächliche Neustartregime 0<epsilon_0<=1 gilt K>=1600,
s=2^(-K)<1/2 und h_n<=s^(2^n)<=s^(n+1). Also
sum h_n<=s/(1-s)<2s<infinity. Abschnitt 9 des neuen Beweises gibt
die vollständige Korrektur. Die explizite ca3849a-Folge mit per Definition
N_n=2^n ceil(c) und das separate Target-Gap-Argument aus 6cbef9d sind
hiervon nicht betroffen. Die historischen Dateien bleiben unverändert.


---

## Fortschrittsnachtrag — 19.09.2026, Moving-Endpoint High-Tail Renewal

> **Mathematischer Anker:** `b1c01860fef2a960cae57634041f75b29d37f836`  
> **Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`

Das Paket
`research/x-c1/moving-endpoint-uniform-high-tail-2026-09-19/`
schließt eine der bislang offenen Moving-Endpoint-Verpflichtungen unabhängig
vom winzigen globalen All-Source-Gap.

### Endpunktuniformer High-Tail

Für jeden bereits betrachteten Core-Endpunkt

[
B=\frac{\log5}{2}\le a\le1
]

werden feste Referenz-Tails gewählt:

[
Y_0=\overline{\operatorname{span}}\{P_{384},P_{386},\ldots\},
\qquad
Y_1=\overline{\operatorname{span}}\{P_{385},P_{387},\ldots\}.
]

Nach der jeweils exakten cosh-/sinh-Mellinrekonstruktion gilt auf dem
vollständigen unendlichen Tail beider Paritäten

[
\boxed{
q_a[f]>\frac1{41}\|f\|_2^2.
}
]

Die Schranke ist uniform auf dem gesamten Band `B<=a<=1`. Sie bezahlt alle
dort möglichen Prime-Power-Kanäle `2,3,4,5,7` und verwendet keinen
bereits bewiesenen kleinen All-Source-Gap als Tailreserve.

### Konsequenz für die bewegliche Blockzerlegung

Der unendliche High-Tail ist damit nicht mehr der offene Teil des
Moving-Endpoint-Problems. Es genügt fortan, einen festen endlichen Low-Raum je
Parität zu behandeln:

[
L_0=\operatorname{span}\{P_2,P_4,\ldots,P_{382}\},
\qquad
L_1=\operatorname{span}\{P_3,P_5,\ldots,P_{383}\},
]

also jeweils

[
\dim L_0=\dim L_1=191.
]

Der Preis für die endpoint-uniforme Tailreserve ist somit ein größerer, aber
fester endlicher Low-Block.

### Präzisierter Frontpunkt

| Stufe | Status |
|---|---|
| Reale All-Parity-Breite bis `B+5*10^-13` | geschlossen |
| Blockadaptive feste-Core-Verstärkung | geschlossen |
| Moving High-Tail auf `B<=a<=1` | **geschlossen; Floor `>1/41`** |
| Moving Low-Dimension | **fest 191 je Parität** |
| Moving 191D Low-Block-Positivität/Konditionierung | offen |
| Moving Low/High-Mischterm | offen |
| Moving Low/Profile-Rank-2-Modell und Operatorrest | offen |
| Moving blockadaptives Restartgesetz | offen |
| Nicht-summierbarer Transport | offen |
| Tatsächlicher Endpunkt `log(7)/2` | offen |
| Connected Unit-Window Coercivity / Strong Terminal | offen |
| full C1-GEOM / Objekt X / globale Weil-Positivität / RH | offen |

Der neue unmittelbare Gate lautet daher:

```text
MOVING 191D LOW-BLOCK + PROFILE RESERVE RENEWAL
```

Ein positiver Tailfloor allein beweist weder die Positivität des
191-dimensionalen beweglichen Low-Blocks noch einen nicht-summierbaren
Fenstertransport.


---

## Strategische Stop-Regel und X-Interface — 19.09.2026

Der Transportstrang und der X-Strang werden ab diesem Stand ausdrücklich
getrennt.

### Transport

Hauptfront ist ausschließlich ein skalierbarer Fortschritt, derzeit

```text
MOVING 191D LOW-BLOCK + PROFILE RESERVE RENEWAL
```

mit dem Ziel eines nicht summierbaren beziehungsweise uniformen
All-Parity-Transports.

Reine mikroskopische Fensterverbesserungen ohne neues Skalierungsgesetz werden
nicht mehr als strategische Hauptfront geführt.

### Objekt X

Das neue Interface-Dokument

`00-uebersicht/OBJEKT_X_INTERFACE_2026-09-19.md`

hält fest: Die physischen Quellenräume besitzen bereits kanonische
kompositionale Nullfortsetzungen und eine exakt kompatible Hermiteform.
Damit ist auf dieser Ebene ein C0-Direktsystem vorhanden.

Offen ist die C1-Schicht: intrinsische positive Readouts und Mediatorräume,
deren Übergänge mit den Quellenabbildungen intertwinen und Prime/Gamma als
Komponenten derselben positiven Geometrie erklären.

### Commit-Filter

Ein weiterer technischer Commit zählt als strategischer Transport-/X-Schritt
nur, wenn er mindestens eine der folgenden Fragen schließt:

- nicht summierbare oder uniforme Transportskalierung;
- erneuerbare bewegliche Blockreserve;
- Moving-191D-Low/Profile-Interface;
- kanonischer positiver Readout-/Mediatorübergang;
- neues Kompositions-/Intertwininggesetz;
- intrinsische gemeinsame Prime-/Gamma-Geometrie;
- ausdrücklich benannte C1-/Objekt-X-Schnittstelle;
- globale Testklasse beziehungsweise exakte Weil-Gram-Identität.

---

## 2026-09-19: Harmonische Blockreserven an beweglichen Endpunkten bis B+10^-10

Status: **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Einordnung nach dem inzwischen hinzugekommenen C0/C1-Interface
`0dea95c` / `56231ad`: ergänzender, bereits ausgearbeiteter endlicher
Bandsatz; keine Promotion der strategischen Hauptfront.
Mathematischer Anker: `b1c01860fef2a960cae57634041f75b29d37f836`.
Der parallele Nachtrag `a0ea6f80f317e4ef1132fc02c86be5bd2064e738`
mit uniformem beweglichem High-Tail-Boden bis a=1 bleibt vollständig
erhalten. Er ist kein benötigter mathematischer Eingang des neuen Satzes.

Neues Paket:
`research/x-c1/moving-endpoint-harmonic-block-renewal-2026-09-19/`.

### Tatsächlich bewiesenes größeres Fenster

Für B=log(5)/2 gilt für jede nichttriviale ursprüngliche Zwei-Mellin-
Quelle u in H1_0((-b,b)), 0<b<=B+10^-10:

    Q_W[u] > 2*10^-15 ||u||_2^2.

Der Odd-Gap ist >10^-12. Das zusätzliche Fenster ist 200-mal breiter
als das äußere Fenster von b1c0186. Die stärkeren älteren Schranken
auf schmaleren Fenstern bleiben als eigene Aussagen erhalten.

Der vollständige korrigierte Profilboden wird durch die exakte
Gamma-Stammfunktion von 2log(2/h)-17 auf 2log(2/h)-5 verschärft.
Alle Prime-Power-, Moment-, Gamma- und Operatorrestkosten sind bezahlt.

### Uniforme tatsächliche Zerlegung auf dem endlichen Band

Für jeden a in [B,B+10^-10] wird F_a=N_a direct-sum L_a direct-sum H_a
konstruiert. N_a folgt der geerbten Even-Near-Null-Linie durch tatsächliche
Formprojektion. L_a hat 61 übrige Koordinaten über beide Paritäten;
der gesamte Soft-Raum hat unverändert 31 Koordinaten je Parität.
Der vollständige Hard-Raum umfasst die beiden unendlichen Core-Tails
und sämtliche angesammelten Profile.

| Größe | Uniforme Schranke |
| --- | --- |
| Vollständiger Hard-Boden in Referenzkoordinaten | >2/5 |
| Vollständiger Hard-Boden in physischer Norm | >1/15 |
| Low/Hard-Operatornorm | <3 |
| Tatsächlicher harmonischer Lift | Norm <15/2 |
| Physische Gesamtkoordinaten | Quadratische Normfaktoren 1/162 und 486 |
| Tatsächlicher Soft-Schur-Boden Even / Odd | >8*10^-13 / >4*10^-10 |
| Zusammengesetzter Endpunkttransport | Norm und inverse Norm auf dem Bild <16 |
| Gesamte quadrierte physische Near-Null-Veränderung | <8.2*10^-12 |

Verschachtelte tatsächliche Hard-Räume liefern exakte Formprojektionen,
eine Schur-Energiebilanz und einen Transportkokzyklus. Die Konstanten
hängen nicht von der Zahl der Unterteilungen dieses Bandes ab.
Alle Near-Null/Low-Mischterme bleiben im Soft-Schur-Block erhalten.
Die physische ursprüngliche Quelle wird weder gewechselt noch normiert.

Zwei gleich große Schritte 5*10^-11 füllen das neue Band, ohne einen
skalaren Gap zu halbieren. Jeder zuvor erreichte neue Endpunkt
B<=a<=B+5*10^-13 erlaubt diesen tatsächlichen weiteren Schritt.

### Reichweite und nächste Restobligation

Geschlossen ist die **endliche Bandversion** von MOVING-ENDPOINT
BLOCK-ADAPTIVE RESERVE RENEWAL. Die Vergleichsdaten bleiben an B
verankert; das angesammelte Profil wird nicht an neuen Endpunkten
auf null zurückgesetzt. Die Summe der Schrittweiten innerhalb des
Bandes ist weiterhin höchstens 10^-10.

Die Erneuerung jenseits dieses Bandes, nicht summierbarer Transport,
Positivität bis log(7)/2 oder 1, Connected Unit-Window Coercivity,
Full C1-GEOM, Objekt X und RH bleiben offen. Der parallele Satz bis
a=1 kontrolliert dort allein den High-Tail mit 191 offenen Low-
Koordinaten je Parität; seine Reichweite darf nicht mit unseren
vollständigen Blockschranken auf dem kleinen Band vermischt werden.

### Reproduktion und Modusnotiz

Das neue Paket liefert 80 neue exakte Prüfungen, 111 byte-/SHA-/Git-
gebundene Eingaben, zwei volle rationale LDL-Vergleiche mit insgesamt
62 positiven Pivots und die vollständige frühere Prüfkette. JSON und
Log reproduzieren bytegleich; alle sieben Payload-Hashes werden geprüft.
Die unendlichdimensionalen Projektions- und Formbereichsargumente
stehen im Beweis; numerische Reproduktion ist kein unabhängiges Audit.

Append-only zur parallelen Veröffentlichung a0ea6f8: Ihr normaler
`check_tail.py --verify` erzeugt 26 Prüfungen, während die veröffentlichten
Ergebnisdateien die 25 Prüfungen von `--math-only` enthalten. Erfolgreich
reproduziert wurden `check_tail.py --math-only --verify` (25 Prüfungen,
sieben Hashes) und anschließend `check_tail.py` ohne Modusargument
(26 Prüfungen einschließlich aller vier Eingabebindungen). Die genaue
Modusabweichung steht in PROOF.md, Abschnitt 10. Keine alte Datei wurde
korrigierend überschrieben; kein negativer mathematischer Befund folgt.

### Anschluss an das inzwischen kanonische C0/C1-Interface

Die C0-Quellenabbildungen sind bereits die kanonischen Nullfortsetzungen.
Der hier quantitativ kontrollierte harmonische Kokzyklus beschreibt
diese Abbildungen in beweglichen Koordinaten; er erfindet keine neuen
physischen Übergänge. Seine q-orthogonalen Projektionen verwenden die
auf dem endlichen Band separat bewiesene Positivität. Sie sind deshalb
keine intrinsische Konstruktion eines positiven C1-Readouts oder
gemeinsamen Prime-/Gamma-Mediators.

Die uniforme Konditionierung und Energiebilanz dieses Hilfssatzes sind
auf das genannte Band beschränkt. Sie ersetzen weder den beweglichen
191D-Low/Profile-Nachweis noch ein nicht kollabierendes Fortsetzungsgesetz
über weitere Bänder. Hauptfront bleibt gemäß der vorstehenden Stop-Regel
**MOVING 191D LOW-BLOCK + PROFILE RESERVE RENEWAL** beziehungsweise die
intrinsische kompatible C1-Mediatorgeometrie. Eine weitere Reihe rein
mikroskopischer Breitenoptimierungen wird daraus nicht als Hauptfront
abgeleitet. Die neuen Interface-Dateien von 0dea95c/56231ad bleiben
unverändert erhalten.

---

## 2026-09-19: C1-Kandidaten ausgeschlossen – kurze räumliche Reichweite plus endlicher globaler Rang

Status: **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anker: `617ffe2a3bfe12bef768b536b9eeffbbfb21f1da`.
Neues Paket:
`research/x-c1/c1-readout-nonlocality-obstruction-2026-09-19/`.

Dieser Nachtrag bearbeitet die benannte C1-Schnittstelle durch den
rigorosen Ausschluss konkreter Kandidatenklassen. Er ist kein weiterer
mikroskopischer Breitenrekord und keine Konstruktion von Objekt X.

### Nichtlokalität lässt sich nicht durch endlich viele globale Merkmale ersetzen

Für jeden B<=a<=1 ist ein exakter positiver Weil-Gram-Readout

    T_a=L_a+K_a,
    q_a(u,v)=<T_a u,T_a v>

ausgeschlossen, falls L_a die physische räumliche Reichweite R_a<a hat
und K_a eine beliebige nichtlokale Korrektur endlichen Ranges ist.
Die Zielanteile müssen nicht orthogonal sein; der endliche Rang darf
vom Endpunkt abhängen. Räumliche Reichweite bedeutet eine festgelegte
physische Ortsstruktur der lokalen Ausgabe, nicht bloß ein Fensterlabel.

Der Beweis konstruiert echte kompakte H1-Quellen mittels

    phi=(D^2-1/4)psi.

Sie erfüllen exakt die beiden ursprünglichen Mellinbedingungen.
Zwischen zwei getrennten Quellenblöcken verschwinden alle Prime-
und L2-Paarungen. Der vollständige Gamma-Kern liefert dennoch
Mischmatrizen jedes Ranges N. Nach Auslöschung des ersten Exponentialmodus
bleiben unendlich viele positive Modengewichte; eine exakte
Vandermonde-Identität beweist Rang N für jedes N.

Eine lokale Ausgabe plus Korrektur vom Rang m kann auf solchen Blöcken
nur Mischrang <=2m erzeugen. N=2m+1 ergibt den Widerspruch. Insbesondere
können 31 oder 191 globale Merkmale einen räumlich lokalen unendlichen
Rest nicht zu einer exakten C1-Gram-Darstellung ergänzen. Die bisherigen
Low/Hard-Beweise bleiben unberührt: Ihre vollständigen Hard-Formen wurden
nie als räumlich lokale Readouts vorausgesetzt.

Für einen rein räumlich begrenzten linearen Readout ohne globale
Zusatzkorrektur gilt außerdem: Bei R<73/200 erzwingt ein festes
Even/Odd-Quellenpaar im schon positiven B-Core einen relativen
Darstellungsfehler >10^-11 in physischer L2-Norm. Diese quantitative
Schranke wird nicht für den Fall eines zusätzlichen K_a beansprucht;
dort gilt der separate exakte Rang-Ausschluss.

### Einzelne Prime-Beiträge sind keine positiven Gram-Komponenten

Jeder strikt aktive Prime-Power-Kanal hat auf jeder Parität beide
Vorzeichen. Vier exakt Mellin-nullige kompakte Quellenstücke isolieren
den gewünschten Kanal und lassen alle anderen arithmetischen Beiträge
verschwinden. Sein signierter Rayleigh-Wert ist dabei exakt +/-w_q.

Der Checker enthält zwanzig Fälle für q=2,3,4,5,7 bei a=1. Diese
isolierten Kanalwerte beweisen dort keine Positivität oder Negativität
der vollständigen Weil-Form. Die q=2-Gegenbeispiele passen bereits
in den positiven B-Core. Weder das ursprüngliche Vorzeichen noch
sein Gegenteil erlaubt eine individuelle positive Kanal-Gram-Identität.

### Geschlossen und offen

| C1-Frage | Stand |
| --- | --- |
| Readout mit R_a<a plus beliebiger Korrektur endlichen Ranges | Kandidatenklasse ausgeschlossen |
| Einzelne signierte Prime-Beiträge als positive Gram-Komponenten | Kandidatenklasse ausgeschlossen |
| Nichtlokaler gemeinsamer Prime-/Gamma-Readout | Offen |
| Indefinite Prime-Beobachtungen in einem positiven Mediator | Nicht ausgeschlossen; Konstruktion offen |
| Kompatible intrinsische C1-Mediatorgeometrie | Offen |
| Moving 191D Low/Profile | Unverändert offen |
| Objekt X / globale Weil-Gram-Identität / RH | Nicht erreicht |

Der Ausschluss betrifft die ausdrücklich definierte räumliche Klasse.
Abstrakte, Fourier-indizierte oder vollständig nichtlokale Readouts
werden nicht pauschal ausgeschlossen. Eine negative gemischte Paarung
ist keine negative Weil-Energie einer Quelle. Das vorhandene C0-System
und die physischen Nullfortsetzungen bleiben unverändert.

### Reproduktion und Vergleichsanker

84 neue exakte Prüfungen, sechs byte-/SHA-/Git-gebundene analytische
Herkunftsdateien, rationale Quellennormen und Fehlerschranken, ein exaktes
Rang-drei-Beispiel sowie alle zwanzig Kanal-/Paritätsfälle reproduzieren.
JSON und Log sind bytegleich; alle sieben Payload-Hashes stimmen.
Die allgemeinen Rang-, Träger- und Ausschlusssätze sind analytische
Beweise, keine Folgerungen aus endlichen Stichproben. Der neue Checker
benötigt keine früheren numerischen Matrizen und wiederholt deren
Prüfkette nicht. Reproduktion bleibt von unabhängigem Audit getrennt.

Die Breitenfaktoren werden mit ihren richtigen Ankern festgehalten:

    10^-10 / (5*10^-13) = 200       gegenüber b1c0186,
    10^-10 / (5*10^-19) = 200000000 gegenüber ca3849a.

617ffe2 verwendete ausdrücklich den ersten Vergleich. Beide Rechnungen
sind korrekt; historische Pakete oder Satzschranken werden nicht geändert.


## Nachtrag 20.09.2026: gekoppelter spektraler C1-Kandidat und kompakter Defekt

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anker: `f77116a890410dfbb2c612956dee9e5342247cd7`.
Paket: `research/x-c1/c1-coupled-spectral-mediator-2026-09-20/`.

Nach dem Ausschluss lokaler-plus-endlichrangiger Readouts wird jetzt ein
konkreter wesentlich nichtlokaler Kandidat konstruiert. Der Horizont ist
fest auf 1 gesetzt; alle Fenster `B<=a<=1` verwenden dieselben fuenf
Prime-Power-Kanaele 2,3,4,5,7 und das vollstaendige Gamma-Symbol g.
Schreibe omega fuer die Summe der Gewichte, c fuer ihre Kosinussumme und
`s=kappa+2 omega`. Dann sind im positiven gemeinsamen Spektralraum
`H=L2(R,dxi)` intrinsisch definiert:

    T u = (g+omega-c)/sqrt(g+s) * Fourier(u),
    D u = (kappa+omega+c)/sqrt(g+s) * Fourier(u).

Die Definition verwendet weder vorausgesetzte Weil-Positivitaet noch eine
nachtraegliche GNS-Vervollstaendigung. Prime-/Gamma-Mischterme und
Prime-/Prime-Mischterme sind Teil desselben Gram-Multiplikators.

Die geschlossenen unendlichdimensionalen Raeume `H_a=closure(T W_a)`
besitzen isometrische Inklusionen `I_ab` mit den exakten Identitaeten

    T_b J_ab = I_ab T_a,    I_bc I_ab = I_ac.

Ein analytischer Pol bei `i beta`, rational lokalisiert durch
`2/5<beta<9/20`, beweist nichtkompakten physischen Output fuer geeignete
gerade und ungerade glatte Zwei-Mellin-Quellen. Der Readout ist damit
tatsaechlich langreichweitig, nicht nur spektral umgeschrieben.

Die exakte verbleibende Gramabweichung lautet

    q_a(u,v) = <T u,T v> - <D u,D v>,
    E_a(u,v) = -<D u,D v>.

Fuer jede nichtverschwindende Quelle ist `E_a[u]<0`. Das beweist keine
negative volle Weil-Energie; es beweist, dass der unberichtigte Kandidat
die gewuenschte Gramidentitaet noch nicht erfuellt.

Der Defekttransfer `R_a(Tu)=Du` ist kompakt, injektiv und von unendlichem
Rang. Er ist explizit die Multiplikation mit
`(kappa+omega+c)/(g+omega-c)` auf dem konstruierten Unterraum H_a und
erfuellt `R_b I_ab=R_a`. Ein Frequenz-/Taylorverfahren liefert quantitative
normkonvergente endlichrangige Approximationen mit vollstaendigem Rest.

Die normierte Form ist `I-R_a*R_a`. Damit ist der verbleibende Gate genau

    q_a >= 0  genau dann, wenn  ||R_a|| <= 1.

Kompaktheit beschraenkt moegliche Spektralhindernisse bei oder ueber eins
auf einen endlichen Raum, entscheidet deren Vorhandensein aber nicht.
Die konservative Beispielschranke im Paket ist UNDECIDED hinsichtlich
Kontraktion. Fuer `C_a=R_a*R_a` gilt lediglich die bewiesene Kompressionslaw
`I_ab* C_b I_ab=C_a`; lokale Quadratwurzelkorrekturen duerfen nicht ohne
Beweis als miteinander intertwiniert behandelt werden.

Die alten positiven Gap-Aussagen koennen bedingt in
`||R_a||^2 <= s/(s+delta)` uebersetzt werden. Das ist kein neues Fenster.
Der bestehende Bereich bis B+10^-10 und der uniforme High-Tail bis 1
werden durch diesen Nachtrag nicht erweitert.

**Geschlossen fuer den benannten Kandidaten:** intrinsische Konstruktion,
gemeinsame Kanalbeobachtungen, Readout-Intertwining, exakter kompakter
Gramdefekt, Direktsystem innerhalb des festgelegten Horizonts 1.
**Offen:** C1c, voller positiver C1-Mediator, kompatible unbeschraenkte
Horizontfolge, Moving-191D Low/Profile, nicht summierbarer Transport,
Strong Terminal, Objekt X und RH.

Reproduktion: 53 exakte neue Pruefungen einschliesslich fuenf gebundener
Herkunftsdateien; bytegleiche Ergebnis-JSON/Log und sieben Nutzdatei-Hashes.
Keine Quadratur, keine numerischen Eigenwerte als Beweis, keine dritte
Mellinbedingung, keine Aenderung der geerbten Near-Null-Quelle und kein
erneuter Lauf der alten numerischen Matrixkette. Checker-Reproduktion
bleibt von einem unabhaengigen analytischen Audit getrennt.

## Nachtrag 20.09.2026: kompakter Defekt und Moving-191D exakt verbunden

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anker: `5557d94d048dc05e7c3b4534a5a2d1711bdc71dc`.
Paket: `research/x-c1/compact-defect-moving-191d-schur-bridge-2026-09-20/`.

Der bestehende physische High-Tail-Satz `q>=1/41` und das konkrete
Spektralmodell `q=||T.||^2-||D.||^2` mit `||D.||^2<=s||.||^2`, `s<23/2`,
liefern auf dem vollstaendigen hohen Bildraum uniform fuer `B<=a<=1`:

    q[T^(-1)h] >= (2/945) ||h||^2,
    ||R_a h||^2 <= (943/945) ||h||^2.

Der hohe Raum hat Kodimension 191 je Paritaet. Daher gilt fuer die
geordneten Singularwerte des tatsaechlichen kompakten Defekttransfers

    s_192(R_a^p)^2 <= 943/945,
    s_192(R_a^p) < 999/1000,

beziehungsweise dieselbe Schranke fuer `s_383(R_a)` ueber beide Paritaeten.
Es koennen also hoechstens 191 Singularwerte je Paritaet die Grenze eins
erreichen. Die endlichrangige Approximation `R_a Q_low` hat den kompletten
Operatorrest `||R_a(I-Q_low)||^2<=943/945`; kein hoher Modus wird verworfen.

Mit dem T-orthogonalen Low-/High-Split hat `C_a=R_a*R_a` die Bloecke
`alpha,beta,K`, wobei `0<=K<=943/945`. Der exakte verbleibende Gate ist

    S_a^p = I-alpha-beta* (I-K)^(-1) beta >= 0.

Der volle High-Inversenrest wird durch

    0 <= S_N-S_a^p <= 42525*(943/945)^(N+2) I

kontrolliert. Die rational gepruefte Blockabschaetzung
`(943/945)^1024<1/8` liefert beliebig kleine Restschranken. Die benoetigten
endlichen Eintraege wurden damit noch nicht eingeschlossen; der positive
endliche Gate bleibt auf neuen Fenstern **UNDECIDED**.

Die vorgeschlagene Verbindungshypothese zum Transportkern wird in einem
genauen Scope zum Satz: Fuer die kanonischen 191 physischen Low-Koordinaten
und ihre vollstaendige q-harmonische High-Elimination gilt

    S_physical = G^(1/2) S_a^p G^(1/2),  G>0.

Beide Schurformen haben damit dieselbe Inertie. Das ist eine Kongruenz der
vollstaendigen Formen, keine Gleichsetzung der Legendre-Low-Basis mit den
fuehrenden Singularvektoren. Kritische Eigenvektoren besitzen einen
eigenwertabhaengigen High-Anteil `(lambda I-K)^(-1) beta x`.
Die zusaetzlichen Low/Profile-Kopplungen einer Fortsetzung a->b sind durch
diesen Core-Vergleich nicht geschlossen.

Auf den geschachtelten Kandidatenraeumen sind die geordneten Singularwerte
stetig und monoton wachsend in a. Das gilt auch am Eintritt von Kanal 7.
Der feste Horizont verwendet bereits alle fuenf Kanaele; es entsteht kein
neuer Ausgaberaum und kein Sprung. Eine quantitative Schrittweite oder
nicht summierbare Transportregel folgt daraus nicht.

Die Dichte echter glatter Zwei-Mellin-Quellen im abgeschlossenen
Gamma-/Weil-Formbereich wird explizit bewiesen. Polynomiellen
Low-Repräsentanten wird keine falsche H1-Nullrandbedingung zugeschrieben.
Die geerbte Near-Null-Quelle und die beiden urspruenglichen Mellinbedingungen
bleiben unveraendert; kein A1-Import.

**Neu geschlossen:** uniforme hohe Defektkontraktion, endliche kritische
Dimension, physische/Defekt-Schur-Kongruenz, vollstaendiger Rest des
High-Responses und qualitative Endpunktkontrolle.
**Offen:** rigorose endliche Schur-Eintraege und positiver Vorzeichennachweis,
volle Kontraktion bis 1, Moving-Low/Profile-Reserve, groessere positive
Fenster, unbegrenzte Horizontkompatibilitaet, positiver C1-Abschluss,
Strong Terminal, Objekt X und RH. Keine negative volle Weil-Quelle.

Reproduktion: 67 neue Ledger-Checks einschliesslich 24 Herkunftsbindungen
und drei gepruefter Replay-Aufrufe. Die Kandidatenpruefung mit 53 Checks
sowie die beiden dokumentierten High-Tail-Modi (25 eingefrorene
Math-only-Checks und 26 Checks mit voller Eingabeprovenienz) bestehen.
JSON/Log sind bytegleich; sieben Nutzdatei-Hashes passen. Kleine rationale
Modellmatrizen pruefen ausschliesslich die Blockalgebra, keine physischen
191D-Singularwerte. Kein unabhaengiger analytischer Audit und keine erneute
Ausfuehrung der alten finiten Matrixkette.
