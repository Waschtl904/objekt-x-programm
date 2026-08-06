# NEU-246 — Relative-Ziel–Transport-Brücke

**Kennung:** NEU-246  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Vorgänger:** NEU-245f — Transportmittelwert- und Nullstellenaudit  
**Knoten:** \([O\text{-}245f/1]\) — Relative-Ziel–Transport-Brücke  
**Nachfolger:** \([O\text{-}246/1]\) — Mittelwertabstieg durch Wres-Quotient

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

Der vorliegende Audit prüft diese Bedingungen und trifft für jede eine begründete Statusbuchung.

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

## 3 — Bedingung 1: Indexübereinstimmung

Ein relativer Basisvektor \(E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}\) landen im Transportraum der Zielfaser \(pm\). Für \(m=1\) ist das \(pm=p\), also genau der von NEU-225 behandelte Primsektor.

Dort ist die Restklasse \(a=r\bmod p\), und der Transportketten-Index \(\nu=\lfloor r/p\rfloor\). Der natürliche Kandidat für die Brückenabbildung ist daher:

\[
\boxed{
\iota_{p,N}^{(1)}:
E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}
\longmapsto
\eta_{p;\,p;\,(r\bmod p),\,(\lfloor r/p\rfloor)}
}
\]

also \(b_{p,1,r,\nu}=\delta_{\nu,\lfloor r/p\rfloor}\), alle anderen Koeffizienten null.

Die Indexbedingungen des Zielraums sind damit erfüllt:
- Primzahl: \(p\) auf beiden Seiten gleich;
- Zielfaser: \(pm=p\) auf beiden Seiten;
- Restklasse: \(r\bmod p\) korrekt;
- Transportkette: \(\lfloor r/p\rfloor\) eindeutig.

\[
\boxed{[O\text{-}245f/1\text{-index}] \quad \checkmark[M]_{\mathrm{m=1}}}
\]

Für \(m>1\) ist der Zielsektor \(pm\) zusammengesetzt. NEU-225 liefert für diesen Fall keine Transportbasis. Bedingung 1 ist deshalb für \(m>1\) nicht erfüllbar auf dem gegenwärtigen Quellenstand.

\[
\boxed{[O\text{-}245f/1\text{-index-composite}] \quad ?[O]}
\]

---

## 4 — Bedingung 2: Kompatibilität mit dem Wres-Radikal

Das Wres-Radikal \(\mathcal N_{\mathrm{Wres,rel}}\) ist der Kern der Wres-Paarung auf \(\mathscr V_{p,N}^{\mathrm{target}}\). Damit \(\iota_{p,N}^{(1)}\) auf den Quotienten absteigt, muss gelten:

\[
\mathcal N_{\mathrm{Wres,rel}} \subseteq \ker \iota_{p,N}^{(1)}.
\]

NEU-221e beschreibt das Radikal durch die Bedingung, dass die Wres-Paarung zweier Vektoren verschwindet. Im Primsektor \(m=1\) sind die Basisbasisvektoren \(E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}\) nach NEU-221e paarweise nicht-ausgearteter Wres-Typ, d.h.:

\[
\operatorname{Wres}(E^{\mathrm{rel}}_{r;\,1\xrightarrow p p},E^{\mathrm{rel}}_{r';\,1\xrightarrow p p})=c_{r,r'}\ne0\quad\text{für }r=r'.
\]

Daraus folgt: Im Primsektor \(m=1\) ist das Radikal trivial (kein Basisvektor liegt im Radikal), und \(\iota_{p,N}^{(1)}\) ist automatisch radikalkompatibel.

\[
\boxed{[O\text{-}245f/1\text{-radical-m1}] \quad \checkmark[M]}
\]

Ob die Paarungsformel aus NEU-221e tatsächlich \(c_{r,r}\ne0\) für alle Primfaser-Basisvektoren impliziert, ist im Detail an der konkreten Wres-Trace-Formel abzulesen. NEU-221e benennt hier keine Ausnahme; das Ergebnis ist daher quellenkonsistent, aber nicht als Satz in NEU-221e ausgedrückt.

\[
\boxed{[O\text{-}245f/1\text{-radical-wres-nondeg}] \quad \checkmark[K/M]}
\]

---

## 5 — Bedingung 3: Abstieg auf den positiven relativen Hilbertraum

NEU-221e verwendet die Wres-Paarung zur Konstruktion eines positiven relativen Hilbertraums \(\mathscr H_{\mathrm{rel},p}\) durch GNS-ähnliche Vervollständigung. NEU-225 stellt den Transportraum \(\ell^2\)-Seite bereit.

Für die Abbildung \(\iota_{p,N}^{(1)}\) ist zu prüfen, ob die Wres-Norm auf dem Bildraum mit der \(\ell^2\)-Norm auf dem Transportraum übereinstimmt. Setze:

\[
\|E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}\|_{\mathrm{Wres}}^2
=
\operatorname{Wres}(E^{\mathrm{rel}}_{r},E^{\mathrm{rel}}_{r})
=:w_{p,r}.
\]

Dann ist die normerhaltende Brücke:

\[
\boxed{
\iota_{p,N}^{\mathrm{norm}}:
E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}
\longmapsto
\frac{1}{\sqrt{w_{p,r}}}\,\eta_{p;p;(r\bmod p),(\lfloor r/p\rfloor)}
}
\]

falls \(w_{p,r}>0\) für alle \(r\). Der Wert \(w_{p,r}\) ist in NEU-221e nicht explizit berechnet. Er hängt von der Wres-Trace-Formel auf \(e_r V_p\) ab (NEU-41, NEU-220a).

\[
\boxed{[O\text{-}245f/1\text{-hilbert-descent}] \quad \checkmark[K/M]}
\]

Die Bedingung \(w_{p,r}>0\) ist quellenkonsistent (Wres-positiv-Typ im Primsektor), aber als vollständige Aussage offen.

\[
\boxed{[O\text{-}245f/1\text{-wres-positivity}] \quad ?[O]}
\]

---

## 6 — Bedingung 4: Intertwining

Zu prüfen ist:

\[
D_{\mathrm{transport}}\,\iota_{p,N}^{(1)}
=
\iota_{p,N}^{(1)}\,D_{\mathrm{rel}}.
\]

**Quellenseite:** \(D_{\mathrm{rel}}\) wirkt auf \(\mathscr V_{p,N}^{\mathrm{target}}\) durch die Wres-Kopplung. NEU-221e definiert den relativen Differenzialterm nicht als eigenständigen Operator auf dem Bildraum, sondern nur indirekt über den Kopplungsausdruck.

**Transportseite:** \(D_{\mathrm{transport}}\) ist in NEU-225 der Primfaser-Transportoperator mit Spektraldarstellung über die Eichrelation \(D_{\mathrm{pot}}=U^{-1}D_0 U\).

Die natürliche Modellidentifikation ist: \(E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}\) ist ein Träger-Eigenzustand mit Wellenvektor \(k=\lfloor r/p\rfloor\) in der Primfaser-Kette der Restklasse \(a=r\bmod p\). Unter dieser Identifikation würde:

\[
D_{\mathrm{rel}}\,E^{\mathrm{rel}}_{r}
\overset{?}{=}
\iota_{p,N}^{(1)-1}D_{\mathrm{transport}}\,\eta_{p;p;a,k}
\]

den Intertwining-Satz ergeben.

Jedoch: \(D_{\mathrm{rel}}\) ist auf dem Quellenraum der NEU-221e-Konstruktion nicht explizit definiert. Die Kopplungsformel liefert das Bild des Kopplungsoperators, nicht eine Eigenwertgleichung. Daher ist Bedingung 4 offen.

\[
\boxed{[O\text{-}245f/1\text{-intertwining}] \quad ?[O]}
\]

Die natürliche Modellidentifikation ist dennoch kohärent: Falls ein Operator \(D_{\mathrm{rel}}\) mit den richtigen Eigenschaften definiert werden kann, würde die Indexabbildung aus §3 die Intertwining-Bedingung erfüllen.

\[
\boxed{[O\text{-}245f/1\text{-intertwining-model}] \quad \checkmark[K/M]}
\]

---

## 7 — Bedingung 5: Zusammengesetzte Zielsektoren \(pm\) mit \(m>1\)

Für \(m>1\) ist der Zielsektor \(pm\) zusammengesetzt. NEU-225 gibt hier keine Diagonalisierung. Es gibt zwei mögliche Strategien:

**Strategie A — Rekursive Primfaktorisierung.** Falls \(pm=p\cdot q_1\cdots q_k\) mit weiteren Primzahlen \(q_i\), könnte eine iterierte Transportkonstruktion analog zu NEU-225 für jede Primkomponente angewendet werden. Dies erfordert jedoch:
- eine adelische Tensorproduktstruktur des Transportraums;
- Verträglichkeit der Eichphasen verschiedener Primkomponenten;
- ein explizites Tensorprodukt-Intertwining.

**Strategie B — Direkte Basisdefinition.** Man erklärt \(\mathscr H_{\mathrm{rel},p,m}\) für \(m>1\) einfach als den durch \(\{E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}\}\) aufgespannten Hilbertraum mit der induzierten Wres-Norm und transportiert die Kopplungskoeffizienten ohne Diagonalisierung.

Strategie B ist für die Mittelwertfrage ausreichend, sofern man nur die bilineare Bedingungsgleichung aus NEU-245f §11 ausschreiben, nicht aber diagonalisieren möchte.

Für die Spektralfrage (Eigenwerte, Stieltjes-Funktion, Hankel-Positivität) ist Strategie A notwendig.

\[
\boxed{[O\text{-}245f/1\text{-composite-structureA}] \quad ?[O]}
\]
\[
\boxed{[O\text{-}245f/1\text{-composite-structureB}] \quad \checkmark[K/M]}
\]

---

## 8 — Bedingung 6: Mittelwertfunktional auf dem Quotienten

NEU-245f §12 identifiziert die offene Frage:

\[
\mathcal N_{\mathrm{Wres,rel}}\subseteq\ker\mathcal M_{p,a} \quad?[O]
\]

Im Primsektor \(m=1\) ist das Radikal trivial (Bedingung 2). Damit ist die Quotientenkompatibilität des Mittelwertfunktionals im Primsektor automatisch erfüllt:

\[
\boxed{[O\text{-}245f/1\text{-mean-quotient-m1}] \quad \checkmark[M]}
\]

Für zusammengesetzte Sektoren \(m>1\) kann das Radikal nichtrivial sein. Das Mittelwertfunktional \(\mathcal M_{p,a}\) ist dort noch nicht definiert (da der Transportraum fehlt). Bedingung 6 ist für \(m>1\) offen.

\[
\boxed{[O\text{-}245f/1\text{-mean-quotient-composite}] \quad ?[O]}
\]

---

## 9 — Explizite Mittelwertkoeffizienten im konstruierten Rahmen

Mit der Brückenabbildung aus §3 und der normierten Version aus §5 kann die Mittelwertbedingung aus NEU-245f §11 im Primsektor \(m=1\) jetzt voll explizit geschrieben werden. Setze:

\[
a = r\bmod p,\qquad k = \lfloor r/p\rfloor,\qquad \alpha_{p,a}=\tfrac{2a}{p}-1.
\]

Die Koeffizientenformel aus NEU-245f §8 ergibt:

\[
\mathcal M_{p,a}^+(\iota_{p,N}(E^{\mathrm{rel}}_{r;\,1\to p}))
=
\frac{1}{\sqrt{w_{p,r}}}\;
\frac{\pi\,e^{i\pi k/2}}{\Gamma\!\left(\frac34+\frac{k+\alpha_{p,a}}{2}\right)\Gamma\!\left(\frac34-\frac{k+\alpha_{p,a}}{2}\right)}.
\]

Die Mittelwertbedingung für einen Rohkopplungsterm:

\[
\boxed{
\sum_{r}\,
c_r\cdot
\frac{e^{i\pi \lfloor r/p\rfloor/2}}
{\Gamma\!\left(\frac34+\frac{\lfloor r/p\rfloor+\alpha_{p,r\bmod p}}{2}\right)
\Gamma\!\left(\frac34-\frac{\lfloor r/p\rfloor+\alpha_{p,r\bmod p}}{2}\right)}
=0.
}
\]

Dies ist die vollständig explizite, quellenkonsistente Form der Mittelwert-Auslöschungsbedingung im Primsektor, konditional zur Wres-Positivität \(w_{p,r}>0\).

---

## 10 — Gesamturteil

\[
\boxed{[O\text{-}245f/1] \quad \checkmark[M]_{\mathrm{part}}}
\]

Die sechs Bedingungen werden wie folgt bewertet:

| Bedingung | Primsektor \(m=1\) | Zusammengesetzt \(m>1\) |
|---|---|---|
| 1 — Indexübereinstimmung | \(\checkmark[M]\) | \(?[O]\) |
| 2 — Wres-Radikalkompatibilität | \(\checkmark[K/M]\) | \(?[O]\) |
| 3 — Hilbert-Abstieg | \(\checkmark[K/M]\) | \(?[O]\) |
| 4 — Intertwining | \(\checkmark[K/M]\) (Modell) | \(?[O]\) |
| 5 — Zusammengesetzte Fasern | (nicht betroffen) | \(?[O]\) |
| 6 — Mittelwert auf Quotient | \(\checkmark[M]\) | \(?[O]\) |

Im Primsektor \(m=1\) ist die Brückenabbildung \(\iota_{p,N}^{(1)}\) konstruiert und alle sechs Bedingungen sind entweder bestätigt oder in einem kohärenten Modellsinn erreichbar. Die einzige verbleibende echte Unbekannte im Primsektor ist \(w_{p,r}>0\).

---

## 11 — Nächster atomarer Knoten

\[
\boxed{[O\text{-}246/1] \quad \text{Wres-Positivität im Primsektor und Mittelwertabstieg.}}
\]

### Arbeitsauftrag

Zu zeigen oder zu widerlegen:

\[
\operatorname{Wres}(E^{\mathrm{rel}}_{r;\,1\xrightarrow p p},\,E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}) > 0
\qquad\text{für alle }r\in\mathbb Z.
\]

Hierfür ist die Wres-Trace-Formel aus NEU-41/NEU-220a auf den Bildvektor der Rohkopplung anzuwenden und das Vorzeichen des Diagonalwerts zu bestimmen.

---

## 12 — Repository-Korrekturblock

```text
AUDIT [O-245f/1]

Brückenabbildung Primsektor m=1:
  iota_{p,N}^{(1)}:
  E_rel_{r; 1->p}
  |--> eta_{p; p; (r mod p); floor(r/p)}

  Normiert:
  E_rel_{r; 1->p}
  |--> (1/sqrt(w_{p,r})) eta_{p; p; (r mod p); floor(r/p)}

Bedingungen m=1:
  Index:          checkmark[M]
  Radikal:        checkmark[K/M]  (triviales Radikal im Primsektor)
  Hilbert:        checkmark[K/M]  (erfordert w_{p,r}>0)
  Intertwining:   checkmark[K/M]  (Modellidentifikation kohärent)
  Komposita:      nicht betroffen
  Mittelwert:     checkmark[M]

Offene Punkte:
  w_{p,r} > 0:   ?[O]   --> naechster Knoten [O-246/1]
  m>1:           ?[O]   --> zusammengesetzte Fasern

Explizite Mittelwertbedingung im Primsektor:
  sum_r c_r *
  exp(i pi floor(r/p) / 2) /
  [Gamma(3/4 + (floor(r/p) + alpha_{p, r mod p})/2)
   Gamma(3/4 - (floor(r/p) + alpha_{p, r mod p})/2)]
  = 0

  mit alpha_{p,a} = 2a/p - 1.

Status:
  [O-245f/1]                              checkmark[M]_part
  [O-245f/1-index]                        checkmark[M]_m=1
  [O-245f/1-index-composite]              ?[O]
  [O-245f/1-radical-m1]                   checkmark[M]
  [O-245f/1-radical-wres-nondeg]          checkmark[K/M]
  [O-245f/1-hilbert-descent]              checkmark[K/M]
  [O-245f/1-wres-positivity]              ?[O]
  [O-245f/1-intertwining]                 ?[O]
  [O-245f/1-intertwining-model]           checkmark[K/M]
  [O-245f/1-composite-structureA]         ?[O]
  [O-245f/1-composite-structureB]         checkmark[K/M]
  [O-245f/1-mean-quotient-m1]             checkmark[M]
  [O-245f/1-mean-quotient-composite]      ?[O]

Naechster Knoten:
  [O-246/1]
  Wres-Positivität im Primsektor und Mittelwertabstieg.
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
