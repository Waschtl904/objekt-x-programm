# NEU-246 — Relative-Ziel–Transport-Brücke

> **Rückstufungsvermerk (NEU-247, 2026-08-06; korrigiert durch NEU-248, 2026-08-06):** Der Direktaudit NEU-247 stuft die zentrale Behauptung dieser Datei zurück. \(\iota_{p,N}^{(1)}\) ist **keine bewiesene intrinsische Wres-Hilbertbrücke**, sondern höchstens eine **konditionale, koordinatenabhängige Modellsektion** \(\checkmark[K/M]\). Konkrete Fehler: (a) die Indexidentifikation \(\eta_{p;p;a,k}\) widerspricht dem Koordinatenwörterbuch \(\eta_{p;m;s,u}\leftrightarrow e_RV_M\) und unterdrückt den \(u\)-Regulator; (b) aus nichtverschwindenden Diagonalwerten wurde fälschlich Radikaltrivialität gefolgert (\(\times[M]\)); (c) die Normierung \(E_r\mapsto\tfrac1{\sqrt{w_{p,r}}}\eta_r\) ist falsch, korrekt wäre \(E_r\mapsto\sqrt{w_{p,r}}\eta_r\) (\(\times[M]\)); (d) die Indexkorrespondenz in §6 ist kein Operatorintertwining. Der von NEU-247 vorgeschlagene Knoten \([O\text{-}246/0]\) — „Wres-Sektionsunabhängigkeit im Primsektor“ — wurde durch **NEU-248** seinerseits als **falsch formuliert und typwidrig** identifiziert: Die dort verwendete Formel \(\eta_{p;p;s+t,u-pt}\in\mathcal N_{\mathrm{Wres,rel}}\) ist ohne Differenzbildung falsch (sie würde bereits für \(t=0\) das gesamte Radikal fordern), und auch die korrigierte Differenzformel \(\eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}\) ist typwidrig, da \(\mathcal N_{\mathrm{Wres,rel}}\) im \(E\)-Rohzielraum liegt, die \(\eta\)-Vektoren dagegen im Transporthilbertraum. Der tatsächlich nächste Knoten ist \([O\text{-}246/0\mathrm{corr}]\) — Gewichteter Kollisionsoperator und kanonisches Rechtsinverses. Vollständiger Audit: [NEU-247](./NEU-247_Direktaudit_NEU246_Ruckstufung_Koordinatensektion.md); Typkorrektur und Nachfolgeknoten: [NEU-248](./NEU-248_Direktaudit_O246-0_Kollisionsoperator_Rechtsinverses.md).

---

**Kennung:** NEU-246  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Vorgänger:** NEU-245f — Transportmittelwert- und Nullstellenaudit  
**Knoten:** \([O\text{-}245f/1]\) — Relative-Ziel–Transport-Brücke (Status: nach NEU-247/NEU-248 zurückgestuft, siehe Vermerk oben)  
**Nachfolger:** \([O\text{-}246/0\mathrm{corr}]\) — Gewichteter Kollisionsoperator und kanonisches Rechtsinverses (statt ursprünglich \([O\text{-}246/1]\) beziehungsweise \([O\text{-}246/0]\))

---

## 1 — Prüffrage

NEU-245f §5 hält fest: Die Abbildung

\[
\iota_{p,N}:
E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}
\longmapsto
\sum_{\nu}
b_{p,m,r,\nu}\,\eta_{p;pm;r,\nu}
\]

existiert als explizites Objekt im Quellenbestand bislang nicht. Ohne sie sind die in NEU-245f berechneten Koeffizientenformeln nur Modellidentifikationen, keine quellenseitig bewiesenen Gleichungen.

Die sechs in NEU-245f §17 formulierten Bedingungen sind:

1. Indexübereinstimmung der Indizes \(p,m,r,\nu\);
2. Kompatibilität mit dem Wres-Radikal \(\mathcal N_{\mathrm{Wres,rel}}\);
3. Abstieg auf den positiven relativen Hilbertraum;
4. Intertwining: \(D_{\mathrm{transport}}\iota_{p,N}=\iota_{p,N}D_{\mathrm{rel}}\);
5. Behandlung der zusammengesetzten Zielsektoren \(pm\);
6. Definition des Mittelwertfunktionals auf dem Quotienten.

Der vorliegende Audit prüft diese Bedingungen und trifft für jede eine begründete Statusbuchung. **Hinweis:** Die nachfolgenden Statusbuchungen wurden durch NEU-247 als teils fehlerhaft identifiziert; siehe Rückstufungsvermerk oben und NEU-247 §2/§11 sowie NEU-248 für die korrigierte Fassung.

---

## 2 — Ausgangsmaterial aus NEU-221e und NEU-225

### 2.1 — Relativer Vorraum (NEU-221e)

NEU-221e konstruiert den relativen Rohzielraum als Quotient:

\[
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
=
\mathscr V_{p,N}^{\mathrm{target}}
\big/
\mathcal N_{\mathrm{Wres,rel}}.
\]

Die Basisvektoren vor Quotientenbildung sind:

\[
E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}
\in
\mathscr V_{p,N}^{\mathrm{target}},
\]

mit dem Indexraum:

\[
r\in\mathbb Z,
\quad
m\in\mathbb Z_{\ge1},
\quad
E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}
\text{ ist Bildbasisvektor der Rohkopplung }T_p^{\mathrm{raw}}(e_r V_m).
\]

Die Indexregeln sind (aus NEU-41 und NEU-221e):

\[
T_p^{\mathrm{raw}}(e_u V_p) = -\sum_{s,m}\ell_{s,m}\,us\log p\; E^{\mathrm{rel}}_{u+ps;\,m\xrightarrow p pm}.
\]

Insbesondere: Der Gitterwert des Ziel-Basisvektors ist \(r=u+ps\), der Nennerfaserindex \(m\) und der Zähler-Faseranschluss \(pm\).

### 2.2 — Transportdarstellung (NEU-225)

NEU-225 konstruiert für den Primsektor \(m_0=p\) eine unitäre Transportdarstellung. Die Orthonormalbasis lautet:

\[
\eta_{p;\,p;\,r,\nu},
\qquad
r\in\{0,\ldots,p-1\},
\quad
\nu\in\mathbb Z,
\]

wobei der Index \(a=r\bmod p\) die Restklasse und \(\nu\) den Transportkettenindex bezeichnet. Die Eigendynamik hat den Spektraltyp des Operators

\[
D_{\mathrm{pot}} = U^{-1}\Bigl(2ic_p\tfrac{d}{dt}\Bigr)U,
\qquad
U=e^{i\phi},
\qquad
\phi(t)=(2a/p-1)\arctan(\sinh t).
\]

NEU-225 hält explizit fest: Zusammengesetzte Fasern mit \(m_0\ne p\) sind nicht diagonalisiert.

---

## 3 — Bedingung 1: Indexübereinstimmung *(nach NEU-247: ⚠[M], siehe Vermerk)*

Ein relativer Basisvektor \(E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}\) landen im Transportraum der Zielfaser \(pm\). Für \(m=1\) ist das \(pm=p\), also genau der von NEU-225 behandelte Primsektor.

Dort ist die Restklasse \(a=r\bmod p\), und der Transportketten-Index \(\nu=\lfloor r/p\rfloor\). Der ursprünglich vorgeschlagene Kandidat für die Brückenabbildung war:

\[
\iota_{p,N}^{(1)}:
E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}
\longmapsto
\eta_{p;\,p;\,(r\bmod p),\,(\lfloor r/p\rfloor)}
\]

**NEU-247 zeigt:** Dies widerspricht dem Koordinatenwörterbuch \(\eta_{p;m;s,u}\leftrightarrow e_RV_M\), \(R=u+ps\), wonach \(\eta_{p;p;a,k}\leftrightarrow e_{k+pa}V_{p^2}\) und nicht \(e_{a+pk}V_{p^2}\) entspricht. Korrekt wäre \(s=k,\,u=a\), also \(\eta_{p;p;k,a}\). Zudem unterdrückt die Formel den unabhängigen \(u\)-Regulatorparameter aus NEU-225.

\[
\boxed{[O\text{-}245f/1\text{-index}] \quad \warning[M]\ \text{(korrigiert von NEU-247, ursprünglich fälschlich }\checkmark[M]\text{)}}
\]

Für \(m>1\) ist der Zielsektor \(pm\) zusammengesetzt. NEU-225 liefert für diesen Fall keine Transportbasis. Bedingung 1 ist deshalb für \(m>1\) nicht erfüllbar auf dem gegenwärtigen Quellenstand.

\[
\boxed{[O\text{-}245f/1\text{-index-composite}] \quad ?[O]}
\]

---

## 4 — Bedingung 2: Kompatibilität mit dem Wres-Radikal *(nach NEU-247: ✗[M]→?[O], siehe Vermerk)*

Das Wres-Radikal \(\mathcal N_{\mathrm{Wres,rel}}\) ist der Kern der Wres-Paarung auf \(\mathscr V_{p,N}^{\mathrm{target}}\). Damit \(\iota_{p,N}^{(1)}\) auf den Quotienten absteigt, muss gelten:

\[
\mathcal N_{\mathrm{Wres,rel}} \subseteq \ker \iota_{p,N}^{(1)}.
\]

Die ursprüngliche Argumentation folgerte aus nichtverschwindenden Diagonalwerten \(c_{r,r}\ne0\) ein triviales Radikal. **NEU-247 widerlegt dies:** Eine Matrix wie \(\begin{pmatrix}1&1\\1&1\end{pmatrix}\) hat nichtverschwindende Diagonale, aber nichttriviales Radikal. Die vollständige Grammatrix \(h_{\mathrm{Wres,rel}}(E_r,E_{r'})\) fehlt; sie ist für die Radikalbestimmung notwendig.

\[
\boxed{[O\text{-}245f/1\text{-radical-m1}] \quad ?[O]\ \text{(korrigiert von NEU-247, ursprünglich fälschlich }\checkmark[M]\text{)}}
\]

---

## 5 — Bedingung 3: Abstieg auf den positiven relativen Hilbertraum *(nach NEU-247: ✗[M]→?[O], siehe Vermerk)*

Die ursprüngliche normerhaltende Brücke war behauptet als:

\[
\iota_{p,N}^{\mathrm{norm}}:
E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}
\longmapsto
\frac{1}{\sqrt{w_{p,r}}}\,\eta_{p;p;(r\bmod p),(\lfloor r/p\rfloor)},
\qquad
w_{p,r}:=\|E^{\mathrm{rel}}_{r}\|_{\mathrm{Wres}}^2.
\]

**NEU-247 zeigt den Normierungsfehler:** Mit \(\|\eta_r\|=1\) gilt \(\|\tfrac1{\sqrt{w_{p,r}}}\eta_r\|^2=1/w_{p,r}\ne w_{p,r}=\|E_r\|^2\) (außer im Sonderfall \(w_{p,r}=1\)). Die korrekte isometrische Formel wäre \(E_r\mapsto\sqrt{w_{p,r}}\,\eta_r\), konditional zu einer noch unbewiesenen diagonalen positiven Grammatrix.

\[
\boxed{[O\text{-}245f/1\text{-hilbert-descent}] \quad ?[O]\ \text{(Normierung falsch, korrigiert von NEU-247)}}
\]

\[
\boxed{[O\text{-}245f/1\text{-wres-positivity}] \quad ?[O]\ \text{(nachrangig gegenüber neuem Knoten }[O\text{-}246/0\mathrm{corr}]\text{)}}
\]

---

## 6 — Bedingung 4: Intertwining *(nach NEU-247: bestätigt ?[O], Modellstatus präzisiert)*

Zu prüfen ist:

\[
D_{\mathrm{transport}}\,\iota_{p,N}^{(1)}
=
\iota_{p,N}^{(1)}\,D_{\mathrm{rel}}.
\]

**Quellenseite:** \(D_{\mathrm{rel}}\) wirkt auf \(\mathscr V_{p,N}^{\mathrm{target}}\) durch die Wres-Kopplung. NEU-221e definiert den relativen Differenzialterm nicht als eigenständigen Operator auf dem Bildraum, sondern nur indirekt über den Kopplungsausdruck.

**Transportseite:** \(D_{\mathrm{transport}}\) ist in NEU-225 der Primfaser-Transportoperator mit Spektraldarstellung über die Eichrelation \(D_{\mathrm{pot}}=U^{-1}D_0 U\).

Die ursprünglich als "Modellidentifikation kohärent" gebuchte Aussage, \(E^{\mathrm{rel}}_{r}\) sei ein "Träger-Eigenzustand", ist nach NEU-247 §7.1 **nicht zulässig**: Die \(\eta\)-Basis ist eine Graph-/Kopplungsbasis ohne normale Eigenvektoren (rein absolut kontinuierliches Spektrum des Transportgenerators). Ein tautologischer Pullback \(D_E:=\iota^{-1}D_{\mathrm{transport}}\iota\) erfüllt die Intertwining-Gleichung nur definitorisch und beweist keine Übereinstimmung mit einem quellenseitigen \(D_{\mathrm{rel}}\).

\[
\boxed{[O\text{-}245f/1\text{-intertwining}] \quad ?[O]}
\]

\[
\boxed{[O\text{-}245f/1\text{-intertwining-model}] \quad \checkmark[K/M]\ \text{(nur als tautologischer Pullback, kein Beweis)}}
\]

---

## 7 — Bedingung 5: Zusammengesetzte Zielsektoren \(pm\) mit \(m>1\)

Für \(m>1\) ist der Zielsektor \(pm\) zusammengesetzt. NEU-225 gibt hier keine Diagonalisierung. Es gibt zwei mögliche Strategien:

**Strategie A — Rekursive Primfaktorisierung.** Falls \(pm=p\cdot q_1\cdots q_k\) mit weiteren Primzahlen \(q_i\), könnte eine iterierte Transportkonstruktion analog zu NEU-225 für jede Primkomponente angewendet werden. Dies erfordert jedoch:
- eine adelische Tensorproduktstruktur des Transportraums;
- Verträglichkeit der Eichphasen verschiedener Primkomponenten;
- ein explizites Tensorprodukt-Intertwining.

**Strategie B — Direkte Basisdefinition.** *(nach NEU-247 §9: Diese "Strategie" setzt die offenen Probleme Positivität, Radikal, Liftunabhängigkeit bereits voraus und ist keine abgeschlossene Konstruktion.)*

\[
\boxed{[O\text{-}245f/1\text{-composite-structureA}] \quad ?[O]}
\]
\[
\boxed{[O\text{-}245f/1\text{-composite-structureB}] \quad ?[O]\ \text{(zurückgestuft von }\checkmark[K/M]\text{, siehe NEU-247 §9)}}
\]

---

## 8 — Bedingung 6: Mittelwertfunktional auf dem Quotienten *(nach NEU-247: ?[O], siehe Vermerk)*

NEU-245f §12 identifiziert die offene Frage:

\[
\mathcal N_{\mathrm{Wres,rel}}\subseteq\ker\mathcal M_{p,a} \quad?[O]
\]

Die ursprüngliche Buchung erklärte den Abstieg im Primsektor für automatisch, da das Radikal als trivial behauptet wurde. **Da dieser Radikalnachweis nach NEU-247 §5 falsch ist, fällt der Mittelwertabstieg zurück auf offen:**

\[
\boxed{[O\text{-}245f/1\text{-mean-quotient-m1}] \quad ?[O]\ \text{(korrigiert von NEU-247, ursprünglich fälschlich }\checkmark[M]\text{)}}
\]

Für zusammengesetzte Sektoren \(m>1\) kann das Radikal nichtrivial sein. Das Mittelwertfunktional \(\mathcal M_{p,a}\) ist dort noch nicht definiert (da der Transportraum fehlt). Bedingung 6 ist für \(m>1\) offen.

\[
\boxed{[O\text{-}245f/1\text{-mean-quotient-composite}] \quad ?[O]}
\]

---

## 9 — Explizite Mittelwertkoeffizienten im konstruierten Rahmen *(konditional, Normierungsfehler siehe Vermerk)*

Mit der ursprünglich vorgeschlagenen Brückenabbildung aus §3 und der **fehlerhaft normierten** Version aus §5 lautete die formal aufgeschriebene Mittelwertbedingung. **NEU-247 §6/§8 stellt fest, dass diese Formel wegen des Normierungsfehlers keine intrinsische Quotientenformel ist** und bei korrigierter Zuordnung \(E_r\mapsto\sqrt{w_{p,r}}\eta_r\) die Gewichtsfaktoren invertiert werden müssten. Setze weiterhin formal:

\[
a = r\bmod p,\qquad k = \lfloor r/p\rfloor,\qquad \alpha_{p,a}=\tfrac{2a}{p}-1.
\]

Die ursprüngliche (fehlerhaft normierte) Formel:

\[
\mathcal M_{p,a}^+(\iota_{p,N}(E^{\mathrm{rel}}_{r;\,1\to p}))
=
\frac{1}{\sqrt{w_{p,r}}}\;
\frac{\pi\,e^{i\pi k/2}}{\Gamma\!\left(\frac34+\frac{k+\alpha_{p,a}}{2}\right)\Gamma\!\left(\frac34-\frac{k+\alpha_{p,a}}{2}\right)}.
\]

sollte durch die konditional korrekte Version mit \(\sqrt{w_{p,r}}\) statt \(1/\sqrt{w_{p,r}}\) ersetzt werden, sobald \(w_{p,r}\) intrinsisch definiert ist (siehe NEU-247 §4, §14, sowie NEU-248 §6).

---

## 10 — Gesamturteil *(nach NEU-247/NEU-248 zurückgestuft, siehe Vermerk oben)*

\[
\boxed{[O\text{-}245f/1] \quad \checkmark[M]_{\mathrm{part}}\ \to\ \text{Hauptbehauptung: }\checkmark[M]_{\mathrm{neg,Quelle}};\ \text{tatsächlich erreicht: }\checkmark[K/M]}
\]

Die sechs Bedingungen, **korrigiert gemäß NEU-247**:

| Bedingung | Primsektor \(m=1\) (korrigiert) | Zusammengesetzt \(m>1\) |
|---|---|---|
| 1 — Indexübereinstimmung | \(\warning[M]\) | \(?[O]\) |
| 2 — Wres-Radikalkompatibilität | \(?[O]\) | \(?[O]\) |
| 3 — Hilbert-Abstieg | \(?[O]\) | \(?[O]\) |
| 4 — Intertwining | \(?[O]\) | \(?[O]\) |
| 5 — Zusammengesetzte Fasern | (nicht betroffen) | \(?[O]\) |
| 6 — Mittelwert auf Quotient | \(?[O]\) | \(?[O]\) |

Einzig bewiesen ist die reine arithmetische Zerlegung \(r=a+pk\). Alle übrigen Punkte sind entweder offen oder als Modellrechnung, nicht als Beweis, zu buchen. Siehe NEU-247 für den vollständigen Direktaudit und die korrigierte Statusbuchung \([O\text{-}246\text{-a}]\) bis \([O\text{-}246\text{-j}]\), sowie NEU-248 für die Typkorrektur des daraus abgeleiteten Knotens.

---

## 11 — Nächster atomarer Knoten *(ersetzt durch NEU-247 §14, seinerseits typkorrigiert durch NEU-248)*

> **Ersetzt:** Der ursprünglich hier formulierte Knoten \([O\text{-}246/1]\) (Wres-Positivität \(w_{p,r}>0\)) kommt nach NEU-247 zu früh. NEU-247 §14 schlug daraufhin \([O\text{-}246/0]\) — „Wres-Sektionsunabhängigkeit im Primsektor“ vor, formuliert als: Gilt \(\eta_{p;p;s+t,u-pt}\in\mathcal N_{\mathrm{Wres,rel}}\) für alle \(s,u,t\in\mathbb Z\)?
>
> **Von NEU-248 korrigiert:** Diese Formel ist ohne Differenzbildung falsch — sie würde bereits für \(t=0\) fordern, dass \(\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}\) gilt, und damit sämtliche betreffenden Basisvektoren im Quotienten vernichten. Die formal korrigierte Differenzformel \(\eta_{p;p;s+t,u-pt}-\eta_{p;p;s,u}\in\mathcal N_{\mathrm{Wres,rel}}\) ist **weiterhin typwidrig**, denn \(\mathcal N_{\mathrm{Wres,rel}}\) liegt nach NEU-221e im \(E\)-Rohzielraum, während die \(\eta\)-Vektoren nach NEU-225 im orthonormalen Transporthilbertraum liegen — beide Differenzen leben in verschiedenen Räumen und sind ohne eine explizite Abbildung zwischen ihnen keine wohldefinierte Aussage.
>
> Der tatsächlich nächste Knoten ist daher:
>
> \[
> \boxed{[O\text{-}246/0\mathrm{corr}] \quad \text{Gewichteter Kollisionsoperator und kanonisches Rechtsinverses.}}
> \]
>
> Dieser Knoten ersetzt den Radikaltest durch die korrekt typisierte algebraische Kollapsabbildung \(\kappa_p^{\mathrm{alg}}:\eta_{p;p;s,u}\mapsto E^{\mathrm{rel}}_{u+ps;1\to p}\), die Analyse ihres Kerns, den Nachweis der Unbeschränktheit des ungewichteten Hilbertkollapses, das gewichtete Faser-\(\ell^2\)-Beschränktheitskriterium \(\sup_R\sum_{u+ps=R}|b_{s,u}|^2<\infty\) und den kanonischen Rechtsinverse-Kandidaten \(\iota_{p,b}\). Details, Arbeitsauftrag und vollständige Begründung: siehe [NEU-247](./NEU-247_Direktaudit_NEU246_Ruckstufung_Koordinatensektion.md) §14 und [NEU-248](./NEU-248_Direktaudit_O246-0_Kollisionsoperator_Rechtsinverses.md).

---

## 12 — Repository-Korrekturblock *(historisch, siehe NEU-247 §16 und NEU-248 §10 für korrigierte Fassung)*

```text
AUDIT [O-245f/1] — HISTORISCHE FASSUNG, DURCH NEU-247/NEU-248 KORRIGIERT

Brückenabbildung Primsektor m=1 (fehlerhaft, siehe NEU-247 §3.2):
  iota_{p,N}^{(1)}:
  E_rel_{r; 1->p}
  |--> eta_{p; p; (r mod p); floor(r/p)}

  Normiert (Normierungsfehler, siehe NEU-247 §6):
  E_rel_{r; 1->p}
  |--> (1/sqrt(w_{p,r})) eta_{p; p; (r mod p); floor(r/p)}

Bedingungen m=1 (korrigierter Status siehe NEU-247 §11):
  Index:          warning[M]  (urspruenglich faelschlich checkmark[M])
  Radikal:        ?[O]        (urspruenglich faelschlich checkmark[K/M])
  Hilbert:        ?[O]        (urspruenglich faelschlich checkmark[K/M])
  Intertwining:   ?[O]        (urspruenglich faelschlich checkmark[K/M])
  Komposita:      ?[O]
  Mittelwert:     ?[O]        (urspruenglich faelschlich checkmark[M])

Naechster Knoten (zweifach korrigiert):
  Schritt 1 (NEU-247): [O-246/0] Wres-Sektionsunabhaengigkeit im Primsektor
    Formel (fehlerhaft, ohne Differenz):
      eta_{p;p;s+t,u-pt} in N_Wres,rel

  Schritt 2 (NEU-248): Formel- und Typkorrektur
    - korrigierte Differenzformel (weiterhin typwidrig):
        eta_{p;p;s+t,u-pt} - eta_{p;p;s,u} in N_Wres,rel
    - Grund: N_Wres,rel liegt im E-Rohzielraum, eta im Transporthilbertraum.
    - korrektes Objekt: kappa_p^alg: eta_{p;p;s,u} |--> E_rel_{u+ps;1->p}

  Tatsaechlich naechster Knoten:
    [O-246/0corr]
    Gewichteter Kollisionsoperator und kanonisches Rechtsinverses.

Vollstaendiger Audit: NEU-247, NEU-248
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
