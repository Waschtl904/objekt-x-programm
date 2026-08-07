# NEU-250m — Präquotientaler archimedischer Port auf gemeinsamer adelischer Quelle

**Katalog-ID:** NEU-250m  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-07  
**Knoten:** $[O\text{-}250m/1]$ (Quellenidentität), $[O\text{-}250m/2]$ (polarisierter Port), $[O\text{-}250m/3]$ (Formzerlegung), $[O\text{-}250m/4]$ (erster globaler Kopplungstest)  
**Vorgänger:** NEU-250l (J-B aktiv: kein Streublock-Mediator), NEU-250k (K3-Firewall), NEU-220d (archimedische Rohform indefinit), NEU-220j (Konturtransport/Testfunktionsraum), NEU-220l (Weil-Quadratik), NEU-220g (schwacher endlich-archimedischer Anschluss)  
**Status:** M1 ?[O]; M2 ✓[M]; M3 ?[O]; M4 ?[O]

---

## 0. Ausgangslage und Motivation

NEU-250l hat festgestellt: Der Feshbach-Streublock $D_{\rm scatt,N}$ existiert derzeit nicht als prä-quotientaler Operator; J-B ist vorläufig aktiv. Der archimedische Port $T_\infty$ ist damit der **primäre verbleibende globale Kopplungskanal**.

Der entscheidende Methodenwechsel gegenüber dem alten Feshbach-Strang:

$$
\boxed{\text{Der neue Weg beginnt vor dem Wres-Quotienten und darf diesen nicht voraussetzen.}} \qquad (0)
$$

NEU-245d und NEU-221c bauen auf $\mathcal{H}_N^{\rm rel} = \mathcal{H}_{N,\rm raw}/\mathcal{N}_{W_{\rm res},\rm rel}$ auf. Dieser Quotient ist nach NEU-250a ohne $j_{p,N}$ nicht konstruiert. Der archimedische Port muss daher **direkt auf $\mathcal{S}_{\rm adel}$** definiert werden.

Ebenso darf $T_\infty$ nicht als separater positiver Hilbertraumblock modelliert werden
(K3-Firewall aus NEU-250k): Die archimedische Rohform $Q_\infty$ ist nach NEU-220d
**indefinit** mit unendlich vielen positiven und negativen Richtungen. Positivität
darf erst global, nach gemeinsamer Faktorisierung, entstehen.

---

## M1 — Quellenidentität: Ist $\mathcal{S}_{\rm adel}$ derselbe Raum wie $\mathcal{G}_W$?

**Was zu klären ist:**  
NEU-250k (und die 250g–i-Serie) verwenden $\mathcal{S}_{\rm adel}$ als gemeinsame adelische Quelle.  
NEU-220j definiert einen analytischen Weil-Testfunktionsraum (im Folgenden $\mathcal{G}_W$) für den Konturtransport der archimedischen Weil-Explizitformel.  

**Quellenbestand (NEU-220j):**  
NEU-220j beschreibt $\mathcal{G}_W$ als Raum von Testfunktionen, die auf der Mellin-Linie analytisch sind und mit der Konturnormierung aus NEU-220k kompatibel sind. Konkret: Funktionen $g$ mit $g(s)$ holomorph in einem Streifen um Re$(s) = 1/2$ und mit geeignetem Abfall.

**Quellenbestand ($\mathcal{S}_{\rm adel}$):**  
NEU-250k/220j bezeichnen $\mathcal{S}_{\rm adel}$ als adelischen Schwartz-Bruhat-Raum $\mathcal{S}(\mathbb{A}_\mathbb{Q})$ mit Fourier-selbstdualer Normierung. Die Weil-Explizitformel in NEU-220k ist genau für $f \in \mathcal{S}(\mathbb{A}_\mathbb{Q})$ aufgestellt, wobei $g = $ Mellin-Transformierte von $|x|^{1/2}f$.

**Befund M1:**  
Die Beziehung zwischen $\mathcal{S}_{\rm adel} = \mathcal{S}(\mathbb{A}_\mathbb{Q})$ und $\mathcal{G}_W$ ist nicht bloß eine Namensgleichheit, sondern eine **Mellin-Abbildung**:

$$
\boxed{\iota_\infty: \mathcal{S}_{\rm adel} \longrightarrow \mathcal{G}_W, \qquad f \longmapsto g_f(s) := \int_0^\infty f_\infty(x)|x|^{s-1/2}\,d^\times x,} \qquad (M1)
$$

wobei $f_\infty$ die archimedische Komponente von $f \in \mathcal{S}(\mathbb{A}_\mathbb{Q})$ bezeichnet.

**Was zu zeigen bleibt $[O\text{-}250m/1]$:**

1. Ist $\iota_\infty$ wohldefiniert und stetig (als Abbildung von Fréchet-Räumen)?
2. Ist $\iota_\infty$ surjektiv oder zumindest dicht auf dem für NEU-220k benötigten Unterraum?
3. Hängt $\iota_\infty$ von der archimedischen Zerlegung $f = f_\infty \otimes f_{\rm fin}$ ab, oder kann sie kanonisch auf ganz $\mathcal{S}_{\rm adel}$ erweitert werden?

Bis zur Klärung dieser drei Punkte gilt:

$$
\iota_\infty: \mathcal{S}_{\rm adel} \to \mathcal{G}_W \qquad \checkmark[K]\text{ (kanonischer Kandidat)}, \qquad ?[O]\text{ (Wohldefiniertheit/Stetigkeit)} \qquad (M1\text{-Status})
$$

---

## M2 — Archimedischer Port als sesquilineare Form, nicht als positiver Hilbertblock

**Was bekannt ist (NEU-220d):**  
Die archimedische Rohform
$$
Q_\infty(a) = \int_{\mathbb{R}^\times} \hat a(u)\overline{\hat a(u)} \cdot \frac{\Gamma'}{\Gamma}(\tfrac{1}{2}+iu)\,du + \text{(Polterme)}
$$
ist **indefinit**: $\frac{\Gamma'}{\Gamma}(\frac{1}{2}+iu)$ wechselt das Vorzeichen, und die Form besitzt unendlich viele positive und negative Richtungen (NEU-220d §4).

**Konsequenz (K3-Firewall, NEU-250k §K3):**  
Es kann **nicht** gelten $Q_\infty(a) = \|T_\infty a\|^2_{\mathcal{H}_\infty}$ für einen gewöhnlichen positiven Hilbertraum $\mathcal{H}_\infty$. Ein solcher Ansatz würde einen neuen positiven Weilterm erzeugen, der arithmetisch nicht vorhanden ist.

**Der richtige Typ:**  
Der archimedische Port entsteht zunächst als **sesquilineare Form auf $\mathcal{S}_{\rm adel}$**:

$$
\boxed{b_\infty(a,b) = \langle W_\infty, g_{a,b}\rangle,} \qquad (M2)
$$

wobei $W_\infty$ die archimedische Weil-Distribution (NEU-220b/c) und $g_{a,b}(t)$ die **polarisierte** Version der Autokorrelationsfunktion ist:

$$
\boxed{g_{a,b}(t) := \langle a, U_t b\rangle_{\mathcal{S}_{\rm adel}}, \qquad g_{a,a}(t) = g_a(t) = \operatorname{Re}\langle a, U_t a\rangle.} \qquad (M2\text{-Pol})
$$

Diese Form $b_\infty$ ist im Allgemeinen **nicht positiv**. Das ist korrekt und notwendig.

**Wichtige Konsequenz für die Gesamtarchitektur:**  
NEU-221c §6 verbietet eine orthogonale direkte Summe lokaler positiver Kanäle. Positivität des Gesamtoperators $\mathcal{T}$ entsteht erst **nach der globalen Kopplung**, nicht vorher. $b_\infty$ darf indefinit sein.

$$
\boxed{b_\infty\text{ ist eine sesquilineare Form auf }\mathcal{S}_{\rm adel}\text{; Positivität entsteht erst global.}} \qquad \checkmark[M] \qquad (M2\text{-Status})
$$

---

## M3 — Polarisierung der gesamten Weil-Form und kanonische Zerlegung

**Das Problem:**  
NEU-220l und NEU-250h liefern bisher im Wesentlichen die **diagonale** Quadratik
$$
Q_W(a) = B_W(a,a).
$$
Für den späteren Kreuzblock $B_{\Lambda\infty} = T_\Lambda^* T_\infty$ brauchen wir aber die **sesquilineare Polarisierung** $B_W(a,b)$ — ohne die wir keine intrinsische Kopplung testen können.

**Polarisierungsformel:**  
Jede hermitesche Form bestimmt sich aus ihrer Diagonale durch

$$
\boxed{B_W(a,b) = \frac{1}{4}\bigl[Q_W(a+b)-Q_W(a-b)+i\,Q_W(a+ib)-i\,Q_W(a-ib)\bigr].} \qquad (M3\text{-Pol})
$$

Angewendet auf die Weil-Explizitformel (NEU-220k) mit
$$
Q_W(a) = \sum_{p,k} \frac{\log p}{p^{k/2}} \operatorname{Re}\langle a, U_{k\log p}a\rangle + b_\infty(a,a) + Q_{\rm pole}(a)
$$
ergibt sich die **kanonische Zerlegung der hermiteschen Weil-Form**:

$$
\boxed{B_W(a,b) = B_\Lambda(a,b) + B_\infty(a,b) + B_{\rm pole}(a,b),} \qquad (M3\text{-Zerlg})
$$

wobei
- $B_\Lambda(a,b) := \sum_{p,k} \frac{\log p}{p^{k/2}} \langle a, U_{k\log p}b\rangle$ — der endliche Port (NEU-250g–i)
- $B_\infty(a,b) := b_\infty(a,b)$ — der archimedische Port (M2)
- $B_{\rm pole}(a,b)$ — Polterme bei $s=0,1$ (NEU-220k §3)

**Was zu zeigen bleibt $[O\text{-}250m/2]$:**

1. Ist die Polarisierungsformel auf $\mathcal{S}_{\rm adel}$ wohldefiniert und konvergent?
2. Ist $B_\Lambda(a,b)$ tatsächlich dasselbe Objekt wie das in NEU-250g–i konstruierte (Verträglichkeitsprüfung)?
3. Ist $B_W(a,b)$ hermitesch (nicht nur symmetrisch)?

$$
\text{Polarisierung }B_W\text{ als kanonischer Kandidat} \quad \checkmark[K], \qquad \text{Wohldefiniertheit} \quad ?[O] \qquad (M3\text{-Status})
$$

---

## M4 — Erster globaler Kopplungstest: Faktorisierung von $B_\Lambda + B_\infty$

**Die entscheidende Frage:**

$$
\boxed{\text{Existiert eine gemeinsame Faktorisierung von }B_\Lambda(a,b)+B_\infty(a,b)\text{ auf }\mathcal{S}_{\rm adel}, \text{ bei der }B_\Lambda\text{ unverändert erhalten bleibt?}} \qquad (M4)
$$

Das wäre der erste Test, ob $B_{\Lambda\infty} \neq 0$ intrinsisch entsteht.

**Was das konkret bedeutet:**  
Gesucht ist ein Zielraum $\mathcal{K}_X$ (kein positiver Hilbertraum notwendig — im Fall der Indefinitheit ein Krein-/Pontryagin-Raum) und Operatoren
$$
\mathcal{T}: \mathcal{S}_{\rm adel} \longrightarrow \mathcal{K}_X
$$
mit
$$
\boxed{Q_W(a,b) = \langle \mathcal{T}a, \mathcal{T}b\rangle_{\mathcal{K}_X}, \qquad \mathcal{T} = T_\Lambda + T_\infty (+T_{\mathcal{M}}\text{ falls J-A})}
$$
ohne Wres-Quotienten vorauszusetzen und ohne Positivität tautologisch einzubauen.

Der Kreuzblock entsteht dann automatisch:
$$
B_{\Lambda\infty}(a,b) = \langle T_\Lambda a, T_\infty b\rangle_{\mathcal{K}_X} = (T_\Lambda^* T_\infty)(a,b).
$$

**Notwendige Bedingungen für den Faktorisierungstest $[O\text{-}250m/3]$:**

| Bedingung | Status |
|---|---|
| $B_\Lambda$ aus NEU-250g–i kanonisch bekannt | $\checkmark[M]$ |
| $B_\infty$ als sesquilineare Form wohldefiniert | $?[O]$ — abhängig von M1/M3 |
| $\mathcal{K}_X$-Typ: positiver Hilbertraum oder Krein-Raum? | $?[O]$ — Indefinitheit von $Q_\infty$ spricht für Krein |
| Kreuzblock $B_{\Lambda\infty}\neq0$ als Gram-Block | $?[O]$ — dies ist das Ziel |

**Warnfirewall (aus NEU-221c §6 und NEU-250k §K3):**

$$
\boxed{\mathcal{K}_X \text{ darf kein }\mathcal{H}_\Lambda \oplus \mathcal{H}_\infty\text{ sein, wenn }\langle\mathcal{H}_\Lambda,\mathcal{H}_\infty\rangle_{\mathcal{K}_X}=0.\text{ Das wäre Orthogonalsumme statt Kopplung.}}
$$

Die nichttriviale Kopplung verlangt explizit $\langle T_\Lambda a, T_\infty b\rangle_{\mathcal{K}_X}\neq0$ für generische $a,b$.

$$
\text{Faktorisierungstest} \quad ?[O] \qquad [O\text{-}250m/3] \qquad (M4\text{-Status})
$$

---

## Stufenplan und Abhängigkeits-DAG

```
[O-250m/1]: Quellenidentität S_adel / G_W
    -> iota_infty wohldefiniert und stetig  ?[O]

[O-250m/2]: Polarisierung B_W(a,b) auf S_adel
    -> Wohldefiniertheit und hermitesche Symmetrie  ?[O]
    -> setzt M1 voraus

[O-250m/3]: Faktorisierungstest B_Lambda + B_infty
    -> Existenz von K_X und T_infty mit richtigem Kreuzblock  ?[O]
    -> setzt M1 + M2 + M3 voraus
    -> Ziel: B_{Lambda,infty} != 0 intrinsisch als Gram-Block

[O-250l/1]: Mischsektormediator aus mu^{a,b}_{pq}  ?[O]  (parallel, blockiert nichts)
    -> Falls positiv: B_{Lambda,M} als dritter Kreuzblock
```

**Welcher Schritt ist atomar und als nächster zugänglich:**

$$
\boxed{[O\text{-}250m/1]: \text{ Wohldefiniertheit von }\iota_\infty: \mathcal{S}_{\rm adel}\to\mathcal{G}_W \text{ als Mellin-Abbildung.}}
$$

Dieser Schritt benötigt keine neuen globalen Konstruktionen. Er erfordert nur:
- die archimedische Komponente $f_\infty$ von $f\in\mathcal{S}(\mathbb{A}_\mathbb{Q})$ zu isolieren,
- die Mellin-Transformation auf dem Streifen Re$(s)\in(0,1)$ zu kontrollieren,
- zu prüfen, ob das Ergebnis in $\mathcal{G}_W$ (dem Testfunktionsraum von NEU-220j) liegt.

Das ist eine lokale analytische Aufgabe — keine neue globale Struktur.

---

## Gesamtstatustabelle

| Schritt | Frage | Quellenstand | Status |
|---|---|---|---|
| M1 | $\iota_\infty: \mathcal{S}_{\rm adel}\to\mathcal{G}_W$ kanonisch? | NEU-220j: Mellin-Struktur vorhanden | $\checkmark[K]$, $?[O]$ (Stetigkeit) |
| M2 | $b_\infty(a,b)$ als sesquilineare Form, nicht pos. Hilbert | NEU-220d: Indefinitheit gesichert | $\checkmark[M]$ |
| M3 | Polarisierung $B_W(a,b)$ wohldefiniert | NEU-220l/250h: Diagonale bekannt | $\checkmark[K]$, $?[O]$ (Wohldefiniertheit) |
| M4 | Faktorisierung $B_\Lambda+B_\infty$ auf $\mathcal{S}_{\rm adel}$ | NEU-250g–i: $B_\Lambda$ bekannt | $?[O]$ — Hauptziel |
| $[O\text{-}250m/1]$ | nächster atomarer Schritt: Mellin-Abbildung | NEU-220j | $?[O]$ |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-220b/c | Archimedische Weil-Distribution $W_\infty$, Normierung |
| NEU-220d (7ff3afe) | Archimedische Rohform indefinit; Polseparation |
| NEU-220g (7c4f74a) | Schwacher endlich-archimedischer Anschluss; früherer Versuch |
| NEU-220j (781653e) | Analytischer Weil-Testfunktionsraum $\mathcal{G}_W$, Konturtransport |
| NEU-220k | Masterkontur, Weil-Explizitformel, Vorzeichenbuchhaltung |
| NEU-220l (1dc07b3) | Weil-Quadratik, Autokorrelation, Positiver Kegel |
| NEU-221c (b0f4e02) | Verbot orthogonaler Primkanal-Direktsumme |
| NEU-250g–i | Lokale Arithmetik: $B_\Lambda$ konstruiert |
| NEU-250k (dbd892a) | K3-Firewall: $\|T_{\mathcal{M}}a\|^2$ nicht isoliert zulässig |
| NEU-250l (27894d5) | J-B aktiv: kein Streublock-Mediator; $T_\infty$ primärer Pfad |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung.*  
*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/objekt-x-programm.*
