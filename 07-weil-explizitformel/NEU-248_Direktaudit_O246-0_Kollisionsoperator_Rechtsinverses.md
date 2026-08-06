# NEU-248 — Direktaudit \([O\text{-}246/0]\): Wres-Sektionsunabhängigkeit oder nichtkanonischer Kollaps?

**Kennung:** NEU-248  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Auditgegenstand:** Knoten \([O\text{-}246/0]\) aus NEU-247 §14 und der Formel im Rückstufungsvermerk von NEU-246 §11  
**Vorgänger:** NEU-247 — Direktaudit NEU-246  
**Nachfolger:** \([O\text{-}246/0\mathrm{corr}]\) — Gewichteter Kollisionsoperator und kanonisches Rechtsinverses

---

## 0 — Sofortige Repository-Korrektur

In NEU-247 §14 und im Rückstufungsvermerk von NEU-246 §11 steht derzeit sinngemäß:

\[
\eta_{p;p;s+t,u-pt}\in\mathcal N_{\mathrm{Wres,rel}}.
\]

Das ist falsch. Zu prüfen wäre allenfalls die **Differenz**:

\[
\eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}.
\]

Die ohne Differenz formulierte Version fordert bereits für \(t=0\), dass \(\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}\) gilt, und würde damit sämtliche betreffenden Basisvektoren im Quotienten vernichten. Der Fehler steht sowohl im Arbeitsauftrag von NEU-247 §14 als auch in NEU-246 §11.

**Diese Korrektur genügt jedoch noch nicht.** Auch die Differenzformel ist in der gegenwärtigen Architektur typwidrig — das ist der eigentliche Gegenstand dieses Audits.

---

## 1 — Gesamturteil

\[
\boxed{[O\text{-}246/0]\text{ ist in der gegenwärtigen Form nicht korrekt typisiert.}}
\]

Status für die formulierte Radikalaussage: \(\boxed{\times[M]}\).

Der Quellenbestand unterscheidet zwei verschiedene Räume:

- den **relativen Rohzielraum** mit Basis \(E^{\mathrm{rel}}_{R;1\to p}\), auf dem das Wres-Radikal definiert ist;
- den **Transport-/Graphhilbertraum** mit Basis \(\eta_{p;p;s,u}\), die in NEU-225 als orthonormal erklärt wird.

Das Radikal \(\mathcal N_{\mathrm{Wres,rel}}\) ist nach NEU-221e ein Unterraum des algebraischen \(E\)-Rohzielraums. Die \(\eta\)-Vektoren aus NEU-225 liegen nicht ohne eine zusätzliche, noch undefinierte Abbildung in diesem Raum. Daher ist

\[
\eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}
\]

zunächst **keine wohldefinierte Aussage**.

---

## 2 — Die drei Ebenen, die getrennt werden müssen

### 2.1 — Rohkopplungsebene

NEU-221e definiert (nach NEU-041):

\[
T_p^{\mathrm{raw}}(e_uV_p)=-\sum_{s,m}\ell_{s,m}\,us\log p\;E^{\mathrm{rel}}_{u+ps;m\to pm}.
\]

Im Primzielsektor (\(m=1\)) lautet der kollabierte Zielindex \(R=u+ps\). Der Rohzielraum wird aber **nur durch** \(E^{\mathrm{rel}}_{R;1\to p}\) indiziert. Verschiedene Paare \((s,u)\) mit demselben \(R\) bezeichnen daher auf dieser Ebene bereits **denselben** Basisvektor.

Für \((s',u')=(s+t,u-pt)\) gilt \(u'+ps'=(u-pt)+p(s+t)=u+ps=R\). Somit ist im \(E\)-Rohzielraum bereits definitionsgemäß

\[
E^{\mathrm{rel}}_{u+ps;1\to p}=E^{\mathrm{rel}}_{u-pt+p(s+t);1\to p}.
\]

Hier ist **keine** Wres-Radikalrechnung erforderlich.

\[
\boxed{\text{Sektionsunabhängigkeit auf der }E\text{-Ebene: }\checkmark[M]}
\]

Sie ist jedoch nur eine Indexgleichheit im bereits kollabierten Raum.

### 2.2 — Transporthilbertraum

NEU-225 erklärt \(\{\eta_{p;m;r,u}\}\) zu einer Orthonormalbasis: \(\langle\eta_{p;m;r,u},\eta_{p';m';r',u'}\rangle=\delta_{pp'}\delta_{mm'}\delta_{rr'}\delta_{uu'}\). Der \(u\)-Index bleibt dort ein unabhängiger Index und wird durch die Primfaserdynamik nicht bewegt.

Sind \((s+t,u-pt)\ne(s,u)\), so folgt deshalb \(\eta_{p;p;s+t,u-pt}\perp\eta_{p;p;s,u}\) und insbesondere \(\eta_{p;p;s+t,u-pt}\ne\eta_{p;p;s,u}\). Die beiden Vektoren werden im Transporthilbertraum also **gerade nicht** identifiziert.

\[
\boxed{\text{Identifikation verschiedener }(s,u)\text{ im Transporthilbertraum: }\checkmark[M]_{\mathrm{neg}}}
\]

Das ist unabhängig von der unbekannten Wres-Grammatrix: Es folgt unmittelbar aus der in NEU-225 verbindlich gesetzten Orthonormalität.

### 2.3 — Koordinatenwörterbuch

NEU-227 schreibt \(\eta_{p;m;s,u}\longleftrightarrow e_RV_M\), \(M=pm\), \(R=u+ps\). Diese Zuordnung ist **nicht injektiv**, denn \((s,u)\) und \((s+t,u-pt)\) haben dasselbe Bild \(R\). Gleichzeitig behandelt NEU-225 diese Paare als verschiedene orthogonale Basisvektoren.

Damit kann das Symbol \(\longleftrightarrow\) **nicht** als bijektives Koordinatenwörterbuch verstanden werden. Es bezeichnet höchstens eine Kollapsabbildung vom fein indizierten Transport-/Kopplungsraum auf den gröber indizierten \(E\)-Rohzielraum.

\[
\boxed{\text{„exaktes bijektives Wörterbuch“: }\times[M]}
\]

---

## 3 — Die korrekte algebraische Kollapsabbildung

Der sinnvolle Gegenstand ist die algebraische Abbildung

\[
\kappa_p^{\mathrm{alg}}:\operatorname{span}_{\mathrm{fin}}\{\eta_{p;p;s,u}\}\longrightarrow\operatorname{span}_{\mathrm{fin}}\{E^{\mathrm{rel}}_{R;1\to p}\},
\qquad
\kappa_p^{\mathrm{alg}}(\eta_{p;p;s,u})=E^{\mathrm{rel}}_{u+ps;1\to p}.
\]

Dies entspricht dem bereits in NEU-43 eingeführten Übergang vom kantenmarkierten Graphraum zum kollabierten Zielindex.

Sei \(\pi_p:\mathbb Z^2\to\mathbb Z\), \(\pi_p(s,u)=u+ps\). Die Fasern \(\pi_p^{-1}(R)=\{(s,R-ps):s\in\mathbb Z\}\) sind unendlich.

Algebraisch gilt für alle \(t\): \(\eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}\in\ker\kappa_p^{\mathrm{alg}}\). Mehr noch:

\[
\ker\kappa_p^{\mathrm{alg}}=\operatorname{span}_{\mathrm{fin}}\bigl\{\eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}: s,u,t\in\mathbb Z\bigr\}.
\]

Die Differenzen liegen somit im **Kern der Kollapsabbildung**, nicht im Wres-Radikal des Zielraums. Das ist die entscheidende Typkorrektur:

\[
\boxed{\ker\kappa_p^{\mathrm{alg}}\neq\mathcal N_{\mathrm{Wres,rel}}}
\]

schon deshalb, weil beide Unterräume in verschiedenen Räumen liegen.

---

## 4 — Warum die in NEU-246 gewählte Sektion nicht intrinsisch ist

Eine Brücke \(\iota_p:E_R^{\mathrm{rel}}\longmapsto\eta_{p;p;s(R),u(R)}\) ist ein Rechtsinverse-Kandidat zu \(\kappa_p^{\mathrm{alg}}\), sofern \(u(R)+p\,s(R)=R\). Die euklidische Wahl wäre \(u(R)=R\bmod p\), \(s(R)=\lfloor R/p\rfloor\). Aber für jedes \(t(R)\in\mathbb Z\) ist auch \(u_t(R)=u(R)-pt(R)\), \(s_t(R)=s(R)+t(R)\) eine Rechtsinverse.

Daher existieren unendlich viele algebraische Sektionen: \(E_R\mapsto\eta_{p;p;s(R)+t(R),\,u(R)-pt(R)}\). Im Transporthilbertraum sind zwei verschiedene solche Bilder orthogonal; für \(t(R)\ne0\) gilt \(\eta_{p;p;s_t(R),u_t(R)}\perp\eta_{p;p;s(R),u(R)}\). Die euklidische Division zeichnet daher zwar einen bequem berechenbaren Repräsentanten aus, aber **keinen durch die vorhandene Hilbert- oder Wres-Geometrie erzwungenen** Repräsentanten.

\[
\boxed{\text{Intrinsizität der euklidischen Sektion: }\checkmark[M]_{\mathrm{neg,Quelle}}}
\]

---

## 5 — Analytische Obstruktion des ungewichteten Kollapses

Nimmt man die in NEU-225 gesetzte orthonormale \(\eta\)-Basis ernst und versucht, den algebraischen Kollaps ungewichtet zwischen Hilberräumen fortzusetzen, \(\kappa_p\eta_{s,u}=E_{u+ps}\), entsteht eine starke Obstruktion.

Fixiere \(R\) und wähle \(N\) verschiedene Paare \((s_j,u_j)\in\pi_p^{-1}(R)\). Setze \(x_N=\tfrac1{\sqrt N}\sum_{j=1}^N\eta_{s_j,u_j}\). Wegen Orthonormalität gilt \(\|x_N\|=1\). Aber \(\kappa_p x_N=\tfrac1{\sqrt N}\sum_{j=1}^N E_R=\sqrt N\,E_R\). Sofern \(E_R\) im Zielquotienten nicht verschwindet, folgt \(\|\kappa_px_N\|=\sqrt N\,\|E_R\|\to\infty\).

\[
\boxed{\kappa_p\text{ ist als ungewichteter Kollaps nicht beschränkt.}}
\]

Noch stärker: Bei orthonormaler Zielbasis ist der auf endlich getragenen Folgen definierte ungewichtete Kollaps **nicht abschließbar**. Sein formales Adjungiertes würde einen Zielkoeffizienten \(y_R\) auf unendlich viele Urbilder kopieren; für jedes \(y_R\ne0\) entstünde eine nicht quadratsummierbare Folge. Die Adjungiertendomäne ist somit nur \(\{0\}\) und nicht dicht.

\[
\boxed{\text{ungewichteter Hilbertkollaps: }\checkmark[M]_{\mathrm{neg}}}
\]

Dieser Befund betrifft nicht die algebraische Kollapsabbildung auf endlich getragenen Vektoren. Er schließt aber ihre naive Fortsetzung als beschränkten oder abgeschlossenen Hilbertoperator aus.

---

## 6 — Gewichteter Kollaps und exaktes Beschränktheitskriterium

Die einzige mögliche Reparatur ist ein gewichteter Faserkollaps:

\[
\kappa_{p,b}\,x=\sum_{u+ps=R}b_{s,u}\,x_{s,u}.
\]

Da die Fasern disjunkt sind, gilt exakt: \(\|\kappa_{p,b}\|^2=\sup_{R\in\mathbb Z}\sum_{u+ps=R}|b_{s,u}|^2\). Somit ist \(\kappa_{p,b}\) genau dann beschränkt, wenn

\[
\boxed{\sup_R\sum_{u+ps=R}|b_{s,u}|^2<\infty.}
\]

Die Rohkopplung liefert allerdings keine frei wählbaren Gewichte. Ihre Koeffizienten haben die Form \(b_{s,u}\sim a_{p,u}\,\ell_{s,1}\,us\log p\). Damit hängt die gewichtete Fasersumme sowohl von der Fourierhebung \(a_{p,u}\), dem \(L_3\)-Vektor \(\ell_{s,1}\), als auch vom Kollisionsfaktor \(us\) ab.

Gerade die \(u\)-Folge ist laut NEU-228 keine harmlose Zielraumkoordinate, sondern Bestandteil der Hebungswahl. Ihre Intrinsizität, die Gramgeometrie und die Hebungsunabhängigkeit sind bereits als offene Barriere registriert.

---

## 7 — Verbindung mit der alten Hebungsbarriere

NEU-221e enthält bereits das korrekte Abstiegsproblem:

\[
\boxed{\widetilde T_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr)\subseteq\mathcal N_{\mathrm{Wres,rel}}.}
\]

Dies prüft, ob zwei tatsächlich zulässige Fourierhebungen nach der Rohkopplung dieselbe Klasse im Wres-Quotienten ergeben. Der Quellenbestand beweist diese Inklusion ausdrücklich nicht.

NEU-228 identifiziert denselben Engpass bereits mit \([O\text{-}153\text{-A/B}]\equiv[O\text{-}221\text{-}1c1a0]\): Hebungsunabhängigkeit des Kopplungsvektors beziehungsweise seines Spektralmaßes. Die Gramwerte und der intrinsische Regulator bleiben offen.

Damit ist das jetzige \([O\text{-}246/0]\) **kein eigenständiger neuer Wres-Knoten**. Es vermischt:

1. die tautologische Indexkollision im \(E\)-Rohzielraum;
2. den Kern der Kollapsabbildung;
3. das Wres-Radikal im Zielraum;
4. die Hebungsunabhängigkeit der gewichteten Rohkopplung;
5. die Wahl eines Rechtsinversen im Transporthilbertraum.

Diese fünf Aussagen sind **nicht äquivalent**.

---

## 8 — Korrigierte Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}246/0\text{-a}]\) | Formel ohne Differenz | \(\times[M]\) |
| \([O\text{-}246/0\text{-b}]\) | \(\eta\)-Differenz liegt im \(E\)-seitigen Wres-Radikal | \(\times[M]\), typwidrig |
| \([O\text{-}246/0\text{-c}]\) | \(u+ps\) ist unter \((s,u)\mapsto(s+t,u-pt)\) invariant | \(\checkmark[M]\) |
| \([O\text{-}246/0\text{-d}]\) | Verschiedene Darstellungen ergeben denselben \(E_R\)-Vektor | \(\checkmark[M]\) |
| \([O\text{-}246/0\text{-e}]\) | Verschiedene Darstellungen ergeben denselben \(\eta\)-Vektor | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}246/0\text{-f}]\) | Algebraischer Kollaps \(\kappa_p^{\mathrm{alg}}\) und sein Kern | \(\checkmark[M]\) |
| \([O\text{-}246/0\text{-g}]\) | Ungewichteter Kollaps besitzt beschränkte Hilbertfortsetzung | \(\checkmark[M]_{\mathrm{neg}}\) |
| \([O\text{-}246/0\text{-h}]\) | Gewichtetes Beschränktheitskriterium | \(\checkmark[M]\) |
| \([O\text{-}246/0\text{-i}]\) | Intrinsische Gewichte aus den Quellen | \(?[O]\) |
| \([O\text{-}246/0\text{-j}]\) | Kanonisches Rechtsinverses beziehungsweise kanonische Sektion | \(?[O]\) |
| \([O\text{-}246/0\text{-k}]\) | Unabhängigkeit von exakt zulässigen Hebungen | \(?[O]\), identisch mit bestehender Barriere |

Gesamt: \(\boxed{[O\text{-}246/0]:\checkmark[M]_{\mathrm{part}}}\)

Der formulierte Radikaltest wird negativ geschlossen; die richtig typisierte gewichtete Kollaps- und Rechtsinversenfrage bleibt offen.

---

## 9 — Korrigierter nächster atomarer Knoten

Der nächste Knoten sollte **nicht mehr** „Wres-Sektionsunabhängigkeit“ heißen.

\[
\boxed{[O\text{-}246/0\mathrm{corr}]\quad\text{Gewichteter Kollisionsoperator und kanonisches Rechtsinverses}}
\]

### Arbeitsauftrag

**A. Räume sauber typisieren.** Definiere ausdrücklich \(H_\eta:=\operatorname{span}_{\mathrm{fin}}\{\eta_{p;p;s,u}\}\) und \(H_E:=\operatorname{span}_{\mathrm{fin}}\{E^{\mathrm{rel}}_{R;1\to p}\}\).

**B. Kollapsoperator definieren.** \(\kappa_{p,b}(\eta_{p;p;s,u})=b_{s,u}\,E^{\mathrm{rel}}_{u+ps;1\to p}\). Die Gewichte \(b_{s,u}\) müssen aus der Rohkopplung stammen und dürfen nicht nachträglich angepasst werden.

**C. Faser-\(\ell^2\)-Bedingung prüfen.** \(\sup_R\sum_{u+ps=R}|b_{s,u}|^2<\infty\).

**D. Kern bestimmen.** Für nichtverschwindende Gewichte ist der Kern nicht mehr bloß durch ungewichtete Differenzen erzeugt, sondern durch gewichtete Faserrelationen: \(\sum_{u+ps=R}b_{s,u}x_{s,u}=0\).

**E. Kanonisches Rechtsinverses prüfen.** Falls \(0<B_R:=\sum_{u+ps=R}|b_{s,u}|^2<\infty\), ist der minimale Hilbertraum-Rechtsinverse formal:

\[
\iota_{p,b}(E_R)=\frac1{B_R}\sum_{u+ps=R}\overline{b_{s,u}}\,\eta_{p;p;s,u}.
\]

Dann gilt algebraisch \(\kappa_{p,b}\iota_{p,b}(E_R)=E_R\). Diese Formel ersetzt die willkürliche Auswahl eines einzelnen Paares \((s,u)\). Sie ist jedoch nur dann intrinsisch, wenn die Gewichte \(b_{s,u}\) hebungsunabhängig und quellenseitig kanonisch sind.

**F. Rückbindung an den bestehenden DAG.** Zu prüfen ist anschließend, ob \(\iota_{p,b}\) von der zulässigen Hebung unabhängig ist. Dieser letzte Punkt ist **kein neuer Knoten**, sondern muss auf \([O\text{-}221\text{-}1c1a]\) beziehungsweise \([O\text{-}153\text{-A/B}]\) zurückgebunden werden.

---

## 10 — Repository-Korrekturblock

```text
KORREKTUR ZU NEU-247 §14 UND NEU-246 §11

1. Formelfehler:
   falsch:
     eta_{p;p;s+t,u-pt} in N_Wres,rel

   zunaechst formal korrigiert:
     eta_{p;p;s+t,u-pt} - eta_{p;p;s,u} in N_Wres,rel

2. Typaudit:
   Auch die korrigierte Formel ist typwidrig:
   N_Wres,rel liegt im E-Rohzielraum,
   eta liegt im Transport-/Graphhilbertraum.

3. Korrektes Objekt:
   kappa_p^alg:
     eta_{p;p;s,u} |--> E_rel_{u+ps;1->p}

   ker(kappa_p^alg) wird algebraisch durch die
   Kollisionsdifferenzen entlang u+ps=R erzeugt.

4. Quellenbefund:
   - Im E-Rohzielraum sind verschiedene Darstellungen desselben R
     bereits identisch.
   - Im eta-Hilbertraum sind sie nach NEU-225 orthogonal.
   - Das Wres-Radikal identifiziert diese beiden Ebenen nicht.

5. Negativbefund:
   Der ungewichtete Kollaps von der orthonormalen eta-Basis auf E_R
   ist wegen unendlich grosser Fasern nicht beschraenkt und nicht
   abschliessbar, sofern E_R nicht verschwindet.

6. Neuer Knoten:
   [O-246/0corr]
   Gewichteter Kollisionsoperator und kanonisches Rechtsinverses.

7. Beschraenktheitskriterium:
   sup_R sum_{u+ps=R} |b_{s,u}|^2 < infinity.

8. Kanonischer Rechtsinverse-Kandidat:
   iota_{p,b}(E_R)
     = (1/B_R) sum_{u+ps=R} conjugate(b_{s,u}) eta_{p;p;s,u},
   B_R = sum_{u+ps=R}|b_{s,u}|^2.

9. Intrinsizitaet der Gewichte:
   weiterhin ?[O];
   Ruckbindung an [O-221-1c1a] / [O-153-A/B].
```

---

## 11 — Endurteil

\[
\boxed{\text{Die euklidische Sektion aus NEU-246 ist nicht durch ein Wres-Radikal kanonisiert.}}
\]

Auf der \(E\)-Seite gibt es gar keine Sektionsabhängigkeit: Alle Paare mit demselben \(R=u+ps\) sind bereits auf denselben Rohzielvektor kollabiert. Auf der \(\eta\)-Seite sind dieselben Paare nach NEU-225 verschiedene orthogonale Vektoren. Eine Auswahl eines einzelnen Repräsentanten ist daher nicht intrinsisch.

Der mathematisch richtige Übergang ist kein Radikaltest, sondern ein gewichteter, im Allgemeinen unendlicher Kollisionsoperator. Seine Gewichte führen unmittelbar zurück zur bereits offenen Fourierhebungs- und Gramgeometriebarriere \([O\text{-}221\text{-}1c1a]\)/\([O\text{-}153\text{-A/B}]\).

Die in NEU-247 und im Rückstufungsvermerk von NEU-246 formulierte Fassung des Knotens \([O\text{-}246/0]\) ist daher durch \([O\text{-}246/0\mathrm{corr}]\) gemäß diesem Audit zu ersetzen.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
