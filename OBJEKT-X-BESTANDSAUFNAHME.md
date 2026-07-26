# Objekt X — Bestandsaufnahme und Steckbrief

**Stand: 26. Juli 2026 (nach NEU-221d)**

Eine Inventur nach 324 Dokumenten: Was wissen wir über Objekt X, was ist ausgeschlossen,
wo bricht die Konstruktion, und welche Grabungsschnitte sind als nächste sinnvoll.

Grundlage: systematische Auswertung von `00-grundlegung/` (Soll-Profil), 22 No-Go-Dokumenten
(Negativbild) und der Konstruktionskette NEU-42 bis NEU-221d (Positivbestand).

---

## 1. Die Kernbeobachtung: Wir haben den Abdruck, nicht das Objekt

### 1.1 Das Axiomenregister ist 107 Einträge alt

Die einzige systematische Beschreibung von Objekt X — [`ebene-XVI-objekt-x.md`](00-grundlegung/ebene-XVI-objekt-x.md)
mit den Positivbedingungen X.1–X.10 und den Ausschlussbedingungen X.neg.1–X.neg.7 — trägt
den Stand **NEU-114 (1. Juli 2026)**. Seither sind 107 Journaleinträge entstanden. Keiner
davon wurde in das Register zurückgeschrieben.

Das zweite Axiomensystem, [`objekt_x_minimalaxiome.md`](00-grundlegung/objekt_x_minimalaxiome.md)
mit A1–A7, stammt vom 17. Juni und steht durchgehend auf `✗ [H]` — reine Hypothese.

**Es gibt also zwei nicht identische Axiomatisierungen von X, beide veraltet.**

### 1.2 X kommt in der späteren Arbeit fast nicht mehr vor

Anteil der Dokumente, die Objekt X inhaltlich behandeln:

| Strang | Dokumente mit X | Anteil |
|---|---|---|
| 00-grundlegung | 8 von 20 | 40 % |
| 01-primkanten-werkzeuge | 29 von 58 | 50 % |
| 02-jacobi-limes | 0 von 34 | **0 %** |
| 03-weil-form-statistik | 7 von 32 | 22 % |
| 04-grenzoperator-renormierung | 1 von 42 | **2 %** |
| 05-primkanal-fourierladung | 3 von 34 | 9 % |
| 06-hochschild-bc-algebra | 5 von 79 | **6 %** |
| 07-weil-explizitformel | 3 von 29 | 10 % |

Nach NEU-56 (29. Juni) bricht die direkte X-Arbeit ab. Was danach kommt, ist Arbeit am
**Spektralschatten** $\Pi_\gamma(X)$ und an der BC-Kohomologie — beides legitim und
notwendig, aber nicht dasselbe.

### 1.3 Die vier Rückbindungstests wurden nie ausgeführt

NEU-114 (1. Juli) erkannte genau diese Drift und richtete vier Tests ein, um den
Spektralschatten wieder an X zu binden:

```
Test 114.1  HH²  [ω̃₂]      → Herglotz-Kanal        ❓[O]
Test 114.2  HH⁴  [L₃]      → Obstruktionsterm      ❓[O]
Test 114.3  Wres^top       → Q_Weil                ❓[O]
Test 114.4  m → p^k m      → Λ(p^k)                ⚠[M]
```

Die Zeichenfolge `114.` erscheint danach in **keinem einzigen** der 105 Dokumente ab
NEU-117. Die Tests wurden geöffnet und liegengelassen.

**Das ist die eigentliche Diagnose.** Nicht mangelnder Fortschritt — die Grabung war
außerordentlich produktiv — sondern: Der Grabungsschnitt hat sich vom Fundplatz entfernt,
und die Fundkartierung wurde nicht mitgeführt.

### 1.4 Die gute Nachricht

Viele dieser Tests sind inzwischen **implizit beantwortet**, nur eben nicht verbucht:

- **Test 114.2** ist faktisch durch den gesamten 06-Strang bearbeitet und endet im
  O-219-No-Go (NEU-219u): Der kanonische Weg von $[L_3]$ zu einer zyklischen Klasse ist
  ausgeschlossen.
- **Test 114.3** wurde in NEU-116 teilweise ausgeführt und lieferte den **Vierschichtensatz**
  $$X_{\mathrm{skel}} \neq X \neq X^{\mathrm{val}} \neq W_\xi^{\mathrm{norm}}, \tag{116.0.V}$$
  mit dem Befund, dass der Faktor $\Theta_{1/2}$ **extern** zu $X$ ist (116.C.15, `✓[M]`).
  Das ist eine echte Aussage über X: Die archimedische Normierung gehört nicht zur
  Residuenstruktur, sondern muss hinzugefügt werden.
- **Test 114.4** hängt weiterhin an der T2-Orthogonalität, die NEU-144 selbst als
  unbewiesen markiert.

Ein großer Teil der Antwort liegt also bereits vor und muss nur gehoben werden.

---

## 2. Der Steckbrief: Was X sein muss

Der eigentliche Ertrag von 22 No-Go-Resultaten ist nicht, was ausgeschlossen wurde, sondern
was dadurch **erzwungen** ist. Jedes No-Go dreht sich in eine Positivforderung um. Zusammen
ergibt das ein überraschend scharfes Fahndungsbild.

| # | Eigenschaft, die X haben MUSS | Erzwungen durch |
|---|---|---|
| **S1** | **Echte Off-Diagonal-Kopplung** zwischen Primkanälen: $K_{pq}\neq 0$ für $p\neq q$. Keine direkte Summe, keine Blockdiagonale, keine Kette. | NEU-50, 207, 209 |
| **S2** | **Mehrdimensionales Bewertungsgitter** statt eindimensionaler Kette, mit **gemeinsamer, punktkonzentrierter Singularität** ($\operatorname{Sing}\subseteq Z_g$) statt separierbarer Struktur auf Koordinatenhyperflächen. | NEU-207, 209 |
| **S3** | **Gradierte, nicht skalare Normierung** — eine Diagonalmatrix $D_N$, kein Skalar $\kappa_N$. Und sie muss **intrinsisch** aus der Operatorstruktur folgen (Anti-Fitting). | NEU-78, 82, 83, 123.H |
| **S4** | **Dichte Trägerstruktur** ($\kappa_N \asymp N$), nicht dünn/rein primzahlindiziert. | NEU-82, 83 |
| **S5** | **Nicht-naive Topologie**: X ist kein gewöhnlicher starker Operatorlimes, sondern wird erst durch Zusatzstruktur sichtbar (wandernde Fenster, Funktionale, $N$-abhängige Testtopologie). | NEU-85 |
| **S6** | **Semifinite statt gewöhnlicher Spur**; **Carleman-Determinante $\det_2$** statt Fredholm-Determinante; Schattenklasse zwingend $\mathcal S_2 \setminus \mathcal S_1$. | NEU-86, 220e, 220u |
| **S7** | **Vermittlung über echte Zwischenobjekte** $\Pi_\gamma$ und $W_\xi$. X ist strukturell höherstufig als jede seiner Projektionen; $X \neq m_{\mathrm{arith}}$ ist kategorial. | NEU-114, 115, 116 |
| **S8** | **Keine zentralen Cup-Faktoren, keine globalen Bimodul-Retraktionen** — das Zentrum ist trivial ($Z(A_{C^*}) = \mathbb C\cdot 1$). | NEU-182, 183, 215 |
| **S9** | **Echte Singularität bei 0**: $H \in \mathrm{LC}(\hat{\mathbb Z}\setminus\{0\}) \setminus \mathrm{LC}(\hat{\mathbb Z})$. Regularität ist hier der Feind der Nichttrivialität. | NEU-196, 200 |
| **S10** | **Getwistete/parazyklische Kohomologie** oder Orbitshift $\kappa\neq 0$ — die naivste Cup-mit-KMS-Form ist ausgeschlossen. | NEU-219u |
| **S11** | **Unbeschränkte Operatoren und regulierte Spuren** im RH-relevanten Bereich $0<\Re\beta\le 1$. | NEU-140, 141, 220t |

Dazu kommt das explizite Kriterienbündel für die Spektralkomponente aus NEU-220u — der
präziseste Steckbrief, den das Programm besitzt:

| Kriterium | Forderung | Aktueller Stand |
|---|---|---|
| **HP-1** | $H_X = H_X^*$ | `⚠[M]` — NEU-53/55, unter Nelson-Bedingungen |
| **HP-2** | $H_X$ hat kompakten Resolventen | **`✗[M]` über Vergleichsoperator $L$** (NEU-56, V); `❓[O]` über einen *anderen* Vergleichsoperator (NEU-56, VI) |
| **HP-3** | $H_X^{-1} \in \mathcal S_2\setminus\mathcal S_1$ | `❓[O]` — hängt an HP-2 |
| **HP-4** | $N_{H_X}(T) = \frac{T}{\pi}\log\frac{T}{2\pi} - \frac{T}{\pi} + O(\log T)$ | `❓[O]` |
| **HP-5** | $\det{}_2(I - zH_X^{-1}) = \Xi(z)/\Xi(0)$ | `❓[O]` |
| **HP-6** | Determinantenidentität aus Spur-/Streu-/relativer Determinantenformel | `❓[O]` |
| **HP-7** | Nullstellenlagen nirgends als Eingabedaten | **verletzt** im gesamten 220s–w-Strang, dort selbst als `?[O], RH-stark` markiert |

### 2.1 Die schärfste Kollision im Katalog

> **HP-2 fordert kompakten Resolventen. NEU-56 Satz 56.2 schließt genau das aus.**

NEU-56 (29. Juni) zeigt: Globaler Schur-Test und Konfinement sind mit *einem* Skalar
$\gamma_N$ unvereinbar. Der erzwungene Schur-Wert $\gamma_N = K/(N\log N)$ lässt $J^-$
relativ zu $L$ verschwinden, damit ist (K) verletzt und Weg A verschlossen — `✗[M]`.
Das Programm wich daraufhin auf Weg B (Spektralmaß) aus.

Fast einen Monat später leitet NEU-220u unabhängig HP-1–HP-7 her, und **HP-2 ist genau die
Bedingung, die Weg A verlangt hätte**. Die beiden Dokumente liegen 165 Katalogeinträge
auseinander und kennen einander nicht.

NEU-56 lässt eine Tür offen — Punkt (VI): *„Weg A bleibt offen über einen anderen
Vergleichsoperator"*, `❓[O]`. Dieser Knoten wurde am 29. Juni geöffnet und **nie wieder
angefasst**; ein Blatt NEU-57 existiert bis heute nicht.

---

## 3. Der Positivbestand: Was tatsächlich gebaut ist

### 3.1 Die tragfähige Kette

```
Primkanten H_rel,N = ⊕_{p≤N} ⊕_m H_{m→pm}                        ✓[M]  NEU-44
   │  Rang-1-Struktur von C_p^rel, störungsstabil                ✓[M]  NEU-44.X/X'
   ▼
Fourier-Hebung  T_p^rel = log p                                  ✓[M]  NEU-42
   │
   ▼
D_rel = closure(iJ^-) wesentlich selbstadjungiert                ⚠[M]  NEU-53–55
   │                            (unter Nelson-Bedingungen)
   ▼
Selbstenergie Σ_rel^ren(β) konvergent, spurklassig für Re β > 0   ✓[M]  NEU-136/137
   │
   ▼
Mangoldt-Spur  Tr(R·Σ_rel^ren) = −ζ'/ζ(β)                        ✓[M]  NEU-141
   │                            NUR für Re β > 1  ◄── Bruch
   ▼
kritischer Streifen 0 < Re β ≤ 1                                 ❓[O]  [O-144-3]
```

Das ist die stärkste durchgehende Verbindung von der Primkantenstruktur zur Zetafunktion,
die das Programm besitzt. Sie ist echt — und sie endet exakt dort, wo die RH eine Aussage
macht.

### 3.2 Die neun Bruchstellen

| # | Bruchstelle | Kern | Quelle |
|---|---|---|---|
| 1 | Primkanten-Kollaps | $T_{\mathrm{rel}}$ auf dem kollabierten Raum nicht wohldefiniert ohne Kantenmarkierung; $\kappa^*\mathrm{Wres}$ **nicht** kantendiagonal. Geschlossen durch **Definition**, nicht durch Beweis — Intrinsizität offen. | NEU-43 Satz 43.3, NEU-44.X3 |
| 2 | Nichtüberzählung | $\dim\ker(1-\mathcal K_\infty(\rho)) = m_\rho$ ist „Kern-Engpass". Genau der Punkt, an dem die Konstruktion die Nullstellen berühren müsste, **ohne sie als Input zu nehmen**. | NEU-49 Satz 49.3 |
| 3 | Spurklasse global | Off-Diagonal-Terme existieren generisch; das Kriterium braucht die echte Spektralbasis von $D_{\mathrm{rel}}$ — die es nicht gibt (Graphbasis ≠ Eigenbasis). | NEU-51/52 |
| 4 | Konfinement | kompakter Resolvent blockiert (siehe §2.1) | NEU-56 |
| 5 | Kritischer Streifen | Spurformel nur für $\Re\beta>1$ | NEU-141/144 |
| 6 | T2-Orthogonalität | $\langle\Psi_p,\Psi_q\rangle = 0$ ist **Voraussetzung, nicht Satz**. Quelle selbst: „noch kein formaler Beweis". Trägt die gesamte primdiagonale Struktur von $R$. | NEU-144 [O-144-1] |
| 7 | Zyklisches Tripel | $(\mathcal H_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)$ nicht vollständig typisiert | NEU-221d |
| 8 | Abel-Lemma quantitativ | Kanalgewichte unbekannt; Kancellation „gefährdet nahe $\beta_0\approx s$" — gerade nahe möglicher Nullstellenlagen | NEU-133 |
| 9 | RH-Tautologie | 220s–w konstruiert aus der Nullstellenliste bzw. unter RH-Annahme | NEU-220s–w |

### 3.3 Der Feshbach-Kandidat NEU-221

NEU-46 liefert die lokale Weyl-Funktion
$$M_p(z) = \langle \Psi_p, (z - D^-_{rel,p})^{-1}\Psi_p\rangle, \qquad \Psi_p := C_p^{\mathrm{rel}}\varepsilon_p$$
und die Zerlegung $D_{\mathrm{Fesh}} = D_{\mathrm{Euler}}^{\mathrm{conn}}\cdot D_{\mathrm{Jac}}\cdot D_{\mathrm{scatt}}$.
Beides ist, so NEU-221d wörtlich, „formal korrekt aufgeschrieben".

**Was NEU-46 nicht enthält:** ein explizites globales Skalarprodukt auf $\mathcal H_N^{\mathrm{rel}}$
und eine Kopplungsnormalisierung für $\Psi_N$. Daher die vier Sperren:

```
[O-221-1c1a]  Vektorkonkretisierung / Normierung  ‖Ψ_N‖
      ↓
[O-221-1c1b]  Nullmodusfreiheit  E_D({0})Ψ_N = 0
      ↓
[O-221-1c1c]  inverse Momente  ∫|λ|^{−2k−2} dμ_{Ψ_N} < ∞,  k = 0,1,2
      ↓
   Ω_{X,N} = (D_N^rel)^{−1}Ψ_N  und  J_{X,N} = (D_N^rel)^{−2}   ← gesperrt

[O-221-1c1d]  globale Kopplung in D_scatt,N        (parallel, unabhängig)
```

**Wichtige Typbeobachtung:** Der 221-Weg zielt auf ein *zyklisches Vektormodell*
($\mu_k = \langle\Omega_X, J_X^k\Omega_X\rangle$), nicht auf den vollen HP-Steckbrief.
Die Bedingung `[O-221-1c1c]` ist eine **vektorrelative Abschwächung** von HP-3: Sie fordert
Endlichkeit inverser Momente bezüglich $\mu_{\Psi_N}$, nicht $H_X^{-1}\in\mathcal S_2$ für
den ganzen Operator. Selbst wenn alle vier Sperren fallen, hat man damit ein
Stieltjes-Modell — noch keinen Hilbert–Pólya-Operator.

Die Quellen behaupten **kein** bewiesenes Hindernis gegen [O-221-1c1a–d]. Aber drei
vorgelagerte, seit Wochen offene Engpässe (Nichtüberzählung, Spurklassenkriterium für
$K_{pq}$, Konfinement) sprechen gegen eine schnelle Erfüllbarkeit.

---

## 4. Die zwei ernsten Risiken

### 4.1 Die kohomologische Schicht steuert auf Leere zu

Drei No-Go-Cluster laufen auf dieselbe Engstelle zu:

- **NEU-182/183:** Das Zentrum ist trivial — beide Cup-Produkt-Routen (regulär und verdreht) sind tot.
- **NEU-215:** Kein globaler Bimoduloperator retrahiert $A_{C^*}$ nichttrivial.
- **NEU-196/200:** Reguläre Potentiale verschwinden im Kommutatorquotienten.

Damit ist die geladene Klasse weder über zentrale Elemente noch über globale Retraktionen
noch über reguläre Potentiale erzeugbar. Übrig bleibt **allein die echt singuläre Route**
(NEU-207/209, Randtermkontrolle [O-207-5b], gemeinsame Charakterkernmenge $Z_g$).

> Scheitert auch diese, hat die HH-Schicht von X **keinen bekannten Konstruktionsweg mehr**.

Das ist eine Aussage, die eine Entscheidung verlangt, bevor weiter investiert wird.

### 4.2 Das Tautologieproblem

NEU-220t zeigt: Eine positive, invertierbare Metrik im Kreinraum-Modell existiert **genau
dann, wenn RH gilt**. Jede Reparatur innerhalb dieses Modells ist damit selbst RH-tautologisch.
Der 220-Strang ist sich dessen bewusst und markiert alle betroffenen Knoten als
`?[O], RH-stark`; NEU-220u formuliert es direkt:

> „Die bloße Äquivalenz ist noch kein Fortschritt gegen RH. Der Fortschritt müsste in der
> quellseitigen (adelischen) Konstruktion von $H_X$ liegen."

Der 220-Strang ist damit richtig einzuordnen: nicht als Fortschritt Richtung Beweis,
sondern als **Kriteriengewinnung**. Sein Ertrag ist HP-1–HP-7 und das Hankel-Kriterium —
ein präzises Lastenheft. NEU-221 ist der erste Versuch, es nicht-tautologisch zu erfüllen.

---

## 5. Fünf Grabungsschnitte

### G1 — Fundkartierung nachziehen: Ebene XVI auf NEU-221d

Aufwand gering, Ertrag hoch. Konkret:

- X.neg.8 bis X.neg.29 aus den 22 No-Gos formulieren (die Liste steht in §2 als S1–S11).
- X.1–X.10 auf den aktuellen Stand bringen; insbesondere X.2 (Spektralbedingung) durch
  HP-1–HP-7 ersetzen, X.8 um die Konfinement-Obstruktion ergänzen.
- Die beiden Axiomensysteme A1–A7 und X.1–X.10 explizit gegeneinander stellen und
  entscheiden, welches führt.

### G2 — Fundauswertung: die vier Rückbindungstests abschließen

Sie sind teilweise längst beantwortet. Konkret zu verbuchen:

| Test | Was inzwischen vorliegt | Restaufgabe |
|---|---|---|
| 114.1 HH² → Herglotz | wenig | offen halten |
| 114.2 HH⁴ → Obstruktion | O-219-No-Go (NEU-219u) | negativ verbuchen, Reparaturpfade als Nachfolger eintragen |
| 114.3 Wres → Q_Weil | Vierschichtensatz NEU-116; $\Theta_{1/2}$ extern | Ergebnis als `✓[M]_part` verbuchen, Restlücke IT-2 benennen |
| 114.4 Primkanten → Λ | hängt an T2-Orthogonalität | mit [O-144-1] zusammenlegen |

### G3 — Den 27 Tage schlafenden Knoten wecken: NEU-57

NEU-56 (VI) — *Weg A über einen anderen Vergleichsoperator* — ist der einzige offene Pfad
zu HP-2, und HP-2 ist Voraussetzung für HP-3 bis HP-6. Solange dieser Knoten geschlossen
bleibt, kann der HP-Steckbrief prinzipiell nicht erfüllt werden. Konkrete Frage:

> Gibt es einen Vergleichsoperator $\tilde L$, der gleichzeitig
> $\|J^-x\| \lesssim \|\tilde Lx\|$ (Schur/Nelson) und $\|D_{\mathrm{rel}}x\| + \|x\| \ge c\|\tilde Lx\|$ (Konfinement)
> erlaubt — also die in NEU-56 §1 gezeigte Zwangslage $\tilde L \simeq |D_{\mathrm{rel}}|$ nicht
> in einen Widerspruch treibt?

Das ist zugleich die Frage nach der Singulärwertasymptotik $s_k(J^-|_{H^{\mathrm{eff}}_{\mathrm{rel}}})$.

### G4 — Testschacht statt Großgrabung: die singuläre Route entscheiden

Vor weiterer Investition in die HH-Schicht: einen schmalen, tiefen Test auf [O-207-5b] und
[O-209-5/6]. Ergebnis entweder „singuläre Route trägt" — dann ist der Weg frei — oder
„trägt nicht" — dann ist die kohomologische Schicht von X nach heutigem Wissen leer, und
das Programm sollte sich ganz auf die analytische Schiene (Feshbach/Weil) konzentrieren.
Beides ist ein Fortschritt. Der teure Fall ist, es offen zu lassen.

### G5 — Numerik als unabhängige Sonde

Das Programm ist zu 100 % analytisch. Drei Rechnungen wären billig und sofort
aussagekräftig:

1. **Zielwerte erzeugen.** $\mu_k = -\frac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0)$ ist numerisch
   berechenbar. Damit liegen die Zahlen vor, die **jede** Konstruktion reproduzieren muss —
   und die Hankelmatrizen $H_N^{(0)}, H_N^{(1)}$ lassen sich für kleine $N$ direkt auf
   Positivität prüfen. Das validiert zugleich die Formel aus NEU-220w.
2. **Die Sperren testen, bevor man sie beweist.** $D_N^{\mathrm{rel}}$ und $\Psi_N$ für
   $N = 50, 100, 500$ explizit aufstellen und numerisch nachsehen: Wie verhält sich
   $\|\Psi_N\|$? Liegt ein Nullmodus vor? Konvergieren $\int|\lambda|^{-2k-2}d\mu_{\Psi_N}$?
   Das entscheidet [O-221-1c1a–c] empirisch in Stunden statt analytisch in Wochen.
3. **Off-Diagonal-Kopplung messen.** $K_{pq}$ für kleine $p,q$ numerisch — trägt S1
   tatsächlich, oder ist die Kopplung asymptotisch vernachlässigbar? Das prüft zugleich
   [O-221-1c1d].

Vorhandene Infrastruktur: [`Riemann`](https://github.com/Waschtl904/Riemann) (Python) und
[`arith-spectral-bridge`](https://github.com/Waschtl904/arith-spectral-bridge) (Jupyter).

---

## 6. Antwort auf die Ausgangsfrage

**Können wir Aussagen über X treffen?** Ja, und zwar deutlich schärfere als vor einem Monat.
Elf erzwungene Struktureigenschaften S1–S11 plus ein siebenteiliges Kriterienbündel
HP-1–HP-7. Das ist ein Fahndungsbild, kein Nebel.

**Können wir es konstruieren?** Nein. Die Kette Primkanten → Selbstenergie → Mangoldt-Spur
trägt bis $\Re\beta>1$ und bricht genau am kritischen Streifen. Der Feshbach-Kandidat ist
formal notiert, aber nicht typisiert.

**Können wir es eingrenzen?** Das ist genau das, was passiert ist — nur unverbucht.
22 No-Gos haben den Möglichkeitsraum massiv verkleinert. An zwei Stellen so stark, dass
Leere droht (§4.1) oder Tautologie (§4.2).

**Die archäologische Analogie trägt, aber mit einer Korrektur.** Wir graben nicht das
Objekt aus. Wir haben das Erdreich rundum abgetragen und dabei einen **Hohlraum** freigelegt,
dessen Wände immer schärfer werden. Was fehlt, ist der Abguss: die Sammlung aller
Wandbedingungen an einem Ort, gegen die ein Kandidat geprüft werden kann. Das ist G1, und
es ist die billigste und wirksamste nächste Maßnahme.

---

*Grundlagendokumente dieser Auswertung: Soll-Profil aus `00-grundlegung/`, Negativbild aus
22 No-Go-Dokumenten, Positivbestand aus der Konstruktionskette NEU-42 bis NEU-221d.
Alle Statusmarken unverändert aus den Quellen übernommen. Die Synthesen in §2, §4 und §5
sind Ableitungen aus den Quellen, keine Quellenaussagen.*
