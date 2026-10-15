# Erneuerungsreduktion und strukturelle Hindernisse

15. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Art: REDUKTION.

Dieses Paket beweist keinen Erneuerungssatz. Es leistet drei Dinge:

1. Es formuliert exakt, was ein Erneuerungssatz für die Zertifikatsklasse
   des Programms behaupten müsste, mit einer benannten, nicht bewiesenen
   arithmetischen Hypothese `H_n` (Satz 4).
2. Es beweist drei strukturelle Lemmata, die jede Erneuerungsregel
   einschränken: Klassenkofinalität (Lemma 1), Monotonie der
   eingeschränkten Inversen (Lemma 2) und Monotonie des wahren Gaps
   (Lemma 3), sowie ein Trägheitslemma zum endlichen Rang eines
   Versagens (Lemma 5).
3. Es importiert zwei klassische Sätze (Weil/Yoshida, Bombieri) und
   zieht daraus die Folgerung, dass die kofinale Konklusion eines
   Erneuerungssatzes auf der vollen Testklasse RH selbst ist (Korollar 1
   und 2).

Nichts hiervon konstruiert Objekt X, schließt einen neuen Horizont oder
promoviert einen arithmetischen Status.

## 1. Rahmen und Bezeichnungen

Alle Formen sind hermitesch; Formordnung `p <= q` bedeutet
`p[f] <= q[f]` auf dem gemeinsamen Definitionsbereich. Für positive
invertierbare Operatoren wird die Umkehr der Ordnung unter Inversion
(Operatormonotonie von `t -> -1/t`) als bekannt vorausgesetzt.

- `W` ist die Weil-Form in der Normierung der zitierten Quellen
  (Bombieri 2000). Sie ist auf `C_c^inf((0,inf))` beziehungsweise auf
  geraden, kompakt getragenen glatten Funktionen in der Variablen
  `u = log x` erklärt.
- `K_a := { f in C_c^inf : supp f in [-a,a] }` ist die volle
  Horizontklasse.
- `T_a` ist eine Projektklasse mit `T_a in K_a`, etwa die
  zusammenhängende Zwei-Mellin-NULLPOL-Klasse. Projektvoraussetzung (N):
  `a <= b` impliziert `T_a in T_b` (Nestung).
- Horizonte `a_1 < a_2 < ...`, Formen `q_n := W | T_(a_n)`, in einer
  physischen Hilbertmetrik `g_n` mit Operator `G_n`. `Q_n` ist der
  Operator von `q_n`. Wegen der Einschränkung derselben Form gilt die
  exakte Rückzugsverträglichkeit `q_(n+1) | T_(a_n) = q_n`.
- `W^(n)` ist eine intrinsische Vergleichsmetrik auf `T_(a_n)`, etwa
  `W_X`; sie darf vom Horizont abhängen.

**Zertifikatsklasse.** Ein Zertifikat `C_n = (W^(n), g_n, U_n, c, C)`
mit Konstanten `c, C > 0` besteht aus

```text
(I1)  q_n >= c * W^(n)        auf T_(a_n)              (intrinsische Reserve)
(I2)  Q_n^-1 <= U_n <= C * G_n^-1                       (physische Inversmajorante)
```

Bemerkung: Nach Inversionsordnung ist `Q_n^-1 <= C G_n^-1` äquivalent zu
`q_n >= C^-1 g_n`. (I1) und (I2) sind also zwei Koerzivitätsaussagen
bezüglich zweier Metriken, der intrinsischen und der physischen. Der
explizite Operator `U_n` ist der operative Träger, weil er im nächsten
Schritt als Gewicht des Residualpreises eingesetzt wird. Die Werte
`tau >= (2/3) W_X` und `A_Z^-1 <= (3/2) I` des Basis84-Tailpakets sind
Beispiele dieses Typs auf einem Teilraum; sie sind kein Zertifikat
`C_n` auf ganz `T_(a_n)`.

## 2. Importierte Sätze

**Satz A (Weil; Yoshida).** RH ist äquivalent dazu, dass `W >= 0` auf
`K_a` für alle `a > 0` gilt. Für hinreichend kleines `a` ist `W` auf `K_a`
positiv definit (Yoshida; erneut bewiesen bei Bombieri 2000).

**Satz B (Bombieri 2000).** Ist RH falsch, aber nur mit endlich vielen
nichttrivialen Nullstellen abseits der kritischen Geraden, so besitzt die
endliche Abschneidung der fouriertransformierten Form ab hinreichend
großer Ordnung genau halb so viele negative Eigenwerte wie es
Ausnahmenullstellen gibt.

Beide Sätze werden importiert, nicht neu bewiesen. Normierungen und
Testklassen sind die der Quellen (Abschnitt 10).

## 3. Lemma 1: Klassenkofinalität

**Lemma 1.** Sei `T_inf := Vereinigung der T_(a_n)`. Es sei `tau` eine
Topologie auf `C_c^inf((0,inf))`, bezüglich der `W` stetig ist und
`T_inf` dicht liegt. Dann gilt:

```text
W >= 0 auf T_inf   ==>   W >= 0 auf C_c^inf((0,inf))   ==>   RH.
```

*Beweis.* Zu `f in C_c^inf` wähle `f_k in T_inf` mit `f_k -> f` in
`tau`. Dann `W[f] = lim W[f_k] >= 0`. Die zweite Implikation ist Satz A.
Ein Beispiel für `tau` ist die induktive Limestopologie von `C_c^inf`,
in der `W` als Paarung mit einer Distribution stetig ist. Bezüglich der
`L^2`-Norm ist `W` nicht stetig; Dichtheit in `L^2` genügt daher nicht.

**Korollar 1.** Jeder Erneuerungssatz, dessen Konklusion (I1) für alle
`n` auf einer in diesem Sinn kofinalen Klasse liefert, hat eine
Konklusion, die RH impliziert. Auf der vollen Klasse `K_(a_n)` mit
`a_n -> inf` ist das unmittelbar der Fall. Auf einer nicht dichten
Projektklasse liefert er RH nicht; das ist der Inhalt des Gates
`FULL-WEIL-TEST-CLASS`.

Es gibt daher keine Fassung, in der ein Erneuerungssatz kofinal schließt
und dabei schwächer als RH ist, ohne zugleich RH nicht zu liefern.

## 4. Lemma 2: Monotonie der eingeschränkten Inversen

**Lemma 2.** Sei `H = H0 (+) H1`, `Q = [[A, C], [C*, D]] >= gamma I`,
`gamma > 0`, beschränkt (oder Operator einer geschlossenen koerziven
Form mit `D(a) x {0} in D(q)`). Dann gilt in Formordnung auf `H0`

```text
(Q^-1)_11 >= A^-1,      Gleichheit genau dann, wenn C = 0.
```

*Beweis (variationell).* Für `f in H0` ist

```text
<f, Q^-1 f> = sup_(x,z) ( 2 Re <f,x> - q[x,z] )
           >= sup_x    ( 2 Re <f,x> - a[x] ) = <f, A^-1 f>,
```

wobei rechts `z = 0` gesetzt wurde; das ist wegen `D(a) x {0} in D(q)`
zulässig. Im beschränkten Fall liest man dasselbe an der
Schurdarstellung `(Q^-1)_11 = (A - C D^-1 C*)^-1` ab, denn
`C D^-1 C* >= 0` und Inversion kehrt die Ordnung um. Gleichheit
erzwingt `C D^-1 C* = 0`, also `C = 0`. QED

**Folgerung 2a (Ketten).** In einer genesteten Kette mit exakter
Rückzugsverträglichkeit `q_(n+1) | T_(a_n) = q_n` gilt: Die Kompression
von `Q_(n+1)^-1` auf den alten Raum ist `>= Q_n^-1`. Die kleinste
zulässige Inversmajorante kann von Horizont zu Horizont nicht fallen.

**Folgerung 2b (fortgesetzte Majorante).** Für die Ausgabe des bedingten
Inversfortsetzungslemmas

```text
Unew = [ U + H V H*   -H V ]
       [   -V H*        V  ]
```

gilt exakt

```text
Unew - [[U,0],[0,0]] = [-H ; I] V [-H ; I]*  >= 0,
```

und die Kompression von `Unew` auf `H1` ist `V`. Also `Unew >= U (+) 0`
in Formordnung und `||Unew|| >= max(||U||, ||V||)`.

**Folgerung 2c (Gewicht des Residualpreises).** Der Residualpreis
`<R_n z, U_n R_n z>` des `n`-ten Schrittes wird mit einem entlang der
Kette nichtfallenden Gewicht bezahlt. Eine Erneuerungsregel muss daher
die Residuen in der `U_n`-gewichteten Norm klein halten, nicht in einer
festen Norm. Eine Regel, die `||R_n||` in einer festen Operatornorm
kontrolliert, ist für Kofinalität strukturell unzureichend.

## 5. Lemma 3: Monotonie des wahren Gaps

**Lemma 3.** Für genestete Klassen `T_a in T_b` (`a <= b`) und eine
feste Referenznorm `|| . ||` ist

```text
lambda*(a) := inf { W[f] / ||f||^2 : f in T_a, f != 0 }
```

nichtwachsend in `a`.

*Beweis.* Das Infimum über eine größere Menge ist nicht größer. QED

**Folgerung 3a.** Eine absolute Reserve kann nicht nach rechts
„erneuert“ werden; das deckt sich mit der Feststellung des Pakets
`scalar-gap-restart-summability-barrier-2026-09-19`, dass Reserve-
Erneuerung nicht bedeuten kann, den wahren physischen Gap nach rechts
wachsen zu lassen. Nur eine Reserve relativ zu einer horizontabhängigen
Metrik `W^(n)` kann gleichmäßig nach unten beschränkt bleiben.

**Folgerung 3b (Verschiebung des Inhalts).** Wählt man `W^(n)` so, dass
(I1) mit fester Konstante `c` gilt, so trägt die Normierung von `W^(n)`
die arithmetische Information. Der Inhalt eines Erneuerungssatzes
verlagert sich dann vollständig in (I2) und in die Konstruierbarkeit
von `W^(n+1)` aus `W^(n)` und den neuen Kanaldaten. Eine Tautologie ist
die Klasse nur dann, wenn `W^(n)` nachträglich aus `q_n` selbst gewonnen
wird; eine zulässige Regel muss `W^(n+1)` vor der Positivitätsauswertung
aus den Rohdaten festlegen.

## 6. Satz 4: Bedingter Reduktionssatz

**Neue Kanaldaten.** `D_n` bezeichnet die beim Übergang
`a_n -> a_(n+1)` neu aktivierten Primzahlpotenzkanäle und das
Gamma-Inkrement. Der neue Raum ist `H1_n := T_(a_(n+1)) (-) T_(a_n)`
bezüglich `g_(n+1)`; die Blockform ist

```text
q_(n+1) = [[ q_n, c_n ], [ c_n*, d_n ]]
```

mit exakter Rückzugsverträglichkeit im linken oberen Block.

**Hypothese `H_n` (benannt, nicht bewiesen).** Es existieren eine
graphbeschränkte Antwort `P_n : H1_n -> D(A_n)`, eine geschlossene Form
`b_n >= beta_n > 0` auf dem ganzen neuen Raum und ein beschränktes
selbstadjungiertes `V_n`, sodass mit dem Hilbertresiduum
`R_n = C_n - A_n P_n` und `k_n[z] = d_n[z] - 2 Re <P_n z, C_n z> + a_n[P_n z]`
gilt:

```text
(H1)  k_n[z] - <R_n z, U_n R_n z> >= b_n[z]      für alle z im neuen Raum,
(H2)  B_n^-1 <= V_n,
(H3)  U_(n+1) := Unew(U_n, P_n + U_n R_n, V_n) <= C * G_(n+1)^-1   und
      lower_n >= c * W^(n+1)   mit denselben c, C wie in C_n,
```

wobei `lower_n` die untere Vergleichsform des Inversfortsetzungslemmas
ist. Alle Domänenvoraussetzungen jenes Lemmas (geschlossene Form `q_(n+1)`,
Hilbertresiduum, inverse Formdomäne, Kongruenz bei nichtunitären
Koordinaten) sind Bestandteil von `H_n`.

**Satz 4.** Gelten `C_n` und `H_n`, so gilt `C_(n+1)` mit denselben
Konstanten `c, C`, und `U_(n+1)` ist explizit durch `U_n, P_n, R_n, V_n`
gegeben.

*Beweis.* Das bedingte Inversfortsetzungslemma liefert aus (H1), (H2)
und der Rückzugsverträglichkeit `q_(n+1) >= lower_n` und
`Q_(n+1)^-1 <= U_(n+1)`. (H3) ergibt (I1) und (I2) für `n+1`. QED

Der Satz ist nach Konstruktion fast tautologisch: `H_n` ist genau das,
was fehlt. Sein Zweck ist nicht Tiefe, sondern Präzision darüber, wo die
Arithmetik eingeht.

**Korollar 2 (Reduktion).** Gilt `C_(n0)` und `H_n` für alle `n >= n0`,
so gilt (I1) für alle `n`. Ist die Klasse im Sinn von Lemma 1 kofinal,
folgt RH. Insbesondere ist die Konjunktion aller `H_n` auf der vollen
Klasse mindestens so stark wie RH. `H_n` ist daher kein
operatortheoretischer, sondern ein arithmetischer Platzhalter.

**Bemerkung (Vergleich mit Li).** Lis Kriterium ist ebenfalls eine
unendliche Folge expliziter Ungleichungen, die zu RH äquivalent ist, und
nach Bombieri und Lagarias eine Spezialisierung des Weilschen Kriteriums
auf bestimmte Testfunktionen. Die Familie `H_n` hat denselben logischen
Typ. Ihr Wert bemisst sich allein daran, ob einzelne `H_n` aus den
Kanaldaten `D_n` beweisbar sind, wo Lis `lambda_n >= 0` es nicht ist.
Das ist offen.

**Bemerkung (Notwendigkeit).** Unter RH ist jedes `q_n` auf `T_(a_n)`
positiv; endliche Zertifikate existieren dann für jedes `n` mit
horizontabhängigen Konstanten. Ob RH umgekehrt für geeignete Familien
`(W^(n), g_n)` gleichmäßige Konstanten `c, C` und damit `H_n` erzwingt,
ist hier nicht entschieden.

## 7. Lemma 5: Endlicher Rang eines Versagens

**Lemma 5 (Trägheit).** Sei `Q = Pi + S` auf einem endlichdimensionalen
Raum, `Pi >= 0`, `S` hermitesch vom Rang `2m` mit Trägheit `(m, m)`.
Dann hat `Q` höchstens `m` negative Eigenwerte.

*Beweis.* Sei `N` der `m`-dimensionale negative Eigenraum von `S`. Auf
`N^perp` ist `S >= 0`, also `Q >= 0`. Hätte `Q` mindestens `m+1` negative
Eigenwerte, so schnitte deren Eigenraum `N^perp` nichttrivial, Widerspruch.
QED

**Folgerung 5a.** Satz B ist die arithmetische Fassung mit
`m = (Anzahl der Ausnahmenullstellen)/2` und Gleichheit ab hinreichender
Abschneidung. Ein hypothetisches Versagen von RH zeigt sich in der
Zertifikatskette als endlicher negativer Block fester Dimension, nicht
als Tail-Effekt. Hochfrequenz- und Tailabschätzungen können einen solchen
Block weder erzeugen noch verbergen.

**Folgerung 5b (Diagnose).** Eine Erneuerungsregel muss den endlichen
kritischen Block jedes Horizonts exakt kontrollieren. Die im Paket
`renewable-low-schur-spectral-2026-09-29` berichteten kanonischen
kritischen Spektralränge `5 -> 6 -> 8` je Parität für `A8 -> A9 -> A11`
sind deshalb die Größe, die `H_n` verfolgen muss; Tailböden allein
ersetzen sie nicht.

**Bemerkung (Verbindung zur Arbeitsdefinition).** Unter RH ist die
Nullstellenseite der expliziten Formel eine Summe positiver Quadrate
`sum 2 |f^(gamma)|^2`, also eine exakte Gram-Identität. Objekt X verlangt
eine solche Identität aus der Prim-/Gamma-Seite ohne Voraussetzung von
RH. Lemma 5 erklärt, warum eine nur approximative untere Vergleichsform
hierfür nicht genügt: Der Unterschied zwischen `lower_n` und `q_n` ist
genau der Ort, an dem ein endlicher negativer Block unbemerkt bliebe.

## 8. Ergebnisstatus

| Aussage | Status |
| --- | --- |
| Satz A, Satz B | importiert, Quellen in Abschnitt 10 |
| Lemma 1, 2, 3, 5 | bewiesen, elementar, AUTHOR_DERIVED |
| Satz 4 | bewiesen, bedingt auf `H_n` und das Inversfortsetzungslemma |
| Korollar 1, 2 | bewiesen aus den Vorstehenden |
| `H_n` | benannter Platzhalter, nicht bewiesen, nicht widerlegt |

Nicht behauptet: ein Beweis von `H_n` für irgendein `n`, ein neuer
Horizont, Kofinalität, Objekt X oder RH. Ebenfalls nicht behauptet: dass
die Familie `H_n` handhabbarer ist als bekannte RH-äquivalente Kriterien.

## 9. Exakte Kontrollen

`verify.py` führt ausschließlich rationale Bruchrechnungen aus und bindet
diesen Beweistext per SHA-256. Geprüft werden:

1. Lemma 2 an fünf vollständigen positiven Blockmodellen einschließlich
   einer dreistufigen genesteten Kette; Gleichheit bei `C = 0`; eine
   indefinite Gegenkontrolle, bei der die Monotonie nicht gilt.
2. Folgerung 2b: `Unew - U (+) 0` ist positiv semidefinit und die
   Kompression auf den neuen Raum ist `V`.
3. Lemma 3 als Zeugentransfer in genesteten Teilräumen mit exakten
   Rayleighquotienten und eine nicht genestete Gegenkontrolle.
4. Lemma 5 über exakte Trägheitsberechnung durch Kongruenz: Rang-2-
   Störungen mit Trägheit `(1,1)` erzeugen höchstens einen negativen
   Eigenwert, mit einem Fall der Gleichheit; eine `(2,2)`-Störung mit
   zwei negativen Eigenwerten zeigt, dass die Schranke `m` scharf ist.
5. Satz 4 an einer dreistufigen Spielzeugkette, in der `H_n` mit
   gleichbleibenden `c, C` gilt und die Invarianten propagieren, sowie
   an einer degenerierten Kette, in der die Reserve kollabiert und
   dieselben Konstanten im zweiten Schritt versagen. Das zeigt, dass
   `H_n` nicht automatisch ist.

Diese Kontrollen prüfen Algebra und Trägheit endlicher Modelle, keine
unendlichen Domänen und keine Prim-/Gamma-Daten.

## 10. Quellen

- E. Bombieri, Remarks on Weil's quadratic functional in the theory of
  prime numbers, I. Rend. Lincei Mat. Appl. 11 (2000), 183–233.
  https://eudml.org/doc/252338
- K. Broughan, Equivalents of the Riemann Hypothesis, Vol. 2, Kap. 9 und
  11 (Weil-Kriterium, Yoshida-Kriterium, Li-Kriterium).
  https://assets.cambridge.org/97811071/97121/excerpt/9781107197121_excerpt.pdf
- A. Connes, C. Consani, Weil positivity and trace formula, the
  archimedean place. Selecta Math. 27 (2021).
  https://arxiv.org/abs/2006.13771
- Projektintern: `research/x-c1/scalar-gap-restart-summability-barrier-2026-09-19/README.md`,
  `research/x-c1/renewable-low-schur-spectral-2026-09-29/README.md`,
  `research/x-c1/basis84-tail-closure-2026-10-14/README.md`; bedingtes
  Inversfortsetzungslemma in Pull Request #223 (zum Zeitpunkt dieses
  Pakets nicht integriert).
