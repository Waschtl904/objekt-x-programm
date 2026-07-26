# NEU-170b — Ursprungsdefinition und Repräsentantenstatus von $L_3$

**Status:** Herkunfts- und Typaudit abgeschlossen. Downstream-Typklassifikation geschlossen; ursprüngliche Konstruktion offen.
**Vorgänger:** NEU-169 → NEU-170 → NEU-170a → NEU-170b.
**Gesperrt:** $P^{ch}(L_3^\circ)\neq0$, $[L_3]_{ch}\neq0$, $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$, $T_p^{pre}(e_uV_p)\neq0$ bis zum Direktaudit NEU-170c.
**Nächster Knoten:** NEU-170c — Direktaudit der ersten $L_3$-Definition in NEU-20/NEU-28.

---

## 170b.0 — DAG-Position und Entscheidungsfrage

$$\text{NEU-169} \longrightarrow \text{NEU-170} \longrightarrow \text{NEU-170a} \longrightarrow \boxed{\text{NEU-170b}}.$$

NEU-170a hat den gewichteten Fourierträger $\operatorname{supp}^{\times}(L_3^\circ)$ auf die Herkunft und den Repräsentantenstatus von $L_3$ zurückgeführt. Die Entscheidungsfrage lautet:

$$\boxed{\text{Was ist }L_3\text{ in der ursprünglichen Architektur?}}$$

Zu unterscheiden sind:
- ein vollständig definierter konkreter Operator,
- ein ausgewählter Kozykel- oder Klassenrepräsentant,
- nur eine abstrakte Kohomologieklasse,
- ein symbolischer Leitoperator ohne vollständige Konstruktion.

---

## 170b.A — Zwei Notationsebenen

Die auditierten Quellen verwenden zwei verschiedene Notationen:

$$[L_3]$$

bezeichnet ein abstraktes Datum des Objekt-$X$-Profils, während

$$L_3 \quad\text{bzw.}\quad L_3^\circ = C_L^{-1}L_3$$

in operatoriellen Spur- und Kopplungsformeln eingesetzt wird. Diese beiden Ebenen dürfen nicht identifiziert werden, solange keine Realisierungs- oder Repräsentantenabbildung

$$\sigma_{L_3}: [L_3] \longmapsto L_3$$

definiert ist.

---

## 170b.B — Audit von NEU-26

NEU-26 beschreibt Objekt $X$ durch das Vierschichtprofil

$$\left(A_{2D}^r,\, [\widetilde\omega_2],\, [L_3],\, Wres_{BC}^{top}\right).$$

Auf dieser Ebene ist $[L_3]$ ein abstraktes Klassen- oder Strukturdatum. Gleichzeitig verwendet die gewünschte Spektralformel einen konkreten Ausdruck

$$\operatorname{Tr}_{Wres}\bigl(f(D_X)L_3\bigr).$$

Im dort eingeführten Minimalmodell wird der formale $L_3$-Einsatz durch den Projektor

$$L_3^{min} := \Pi_Z$$

auf den tautologisch ergänzten Nullstellensektor realisiert. Dieser Projektor ist keine BC-intrinsische Konstruktion des ursprünglichen $L_3$; er zeigt vielmehr, dass für die formale Minimalrealisierung nur die Rolle eines Insertionsoperators nachgebildet wird.

$$\boxed{[L_3]\text{ ist ein abstraktes Objekt-}X\text{-Datum.}}$$

Es folgt nicht, dass ein konkreter BC-intrinsischer Operator $L_3$ dort vollständig konstruiert sei.

---

## 170b.C — Audit von NEU-29

NEU-29 behandelt $L_3$ als konkreten Leitoperator und verwendet:

$$C_L = \operatorname{Tr}_{Hilbert}\bigl(L_3|_{\mathrm{diag}}\bigr) \neq0, \qquad L_3^\circ := C_L^{-1}L_3.$$

Der normalisierte Leitoperator erscheint in den Ausdrücken

$$\operatorname{Tr}_{Wres}^{top}\!\left((s-D_X^{BC})^{-2}L_3^\circ\right) \quad\text{und}\quad \operatorname{Tr}_{Wres}^{top}\!\left(f(D_X^{BC})L_3^\circ\right).$$

Damit muss $L_3$ auf dieser Ebene mindestens ein fest gewähltes konkretes Objekt sein, für das:
- die diagonale Hilbertspur definiert ist,
- die Multiplikation bzw. Komposition mit dem Resolventen zulässig ist,
- die $Wres$-Insertion wohldefiniert ist.

NEU-29 liefert jedoch keine Formel für die Wirkung von $L_3$, keinen vollständigen Definitionsbereich und keine Repräsentantenauswahl aus $[L_3]$. Der Nichtverschwindensbefund für $C_L$ wird aus NEU-20/NEU-28 importiert.

$$\boxed{\text{NEU-29 setzt einen konkreten Leitoperator voraus, konstruiert ihn aber nicht innerhalb des Blatts.}}$$

---

## 170b.D — Audit der späteren Objekt-$X$-Architektur

Die nachfolgenden Blätter behalten die Doppelstruktur bei. Auf der abstrakten Architekturebene werden die Daten weiterhin als

$$\left(B_3,\, [\widetilde\omega_2],\, [L_3],\, Wres_{BC}^{top}\right)$$

angegeben. Auf der analytischen Ebene wird dagegen der konkrete Ausdruck $L_3^\circ = C_L^{-1}L_3$ als Polarisations- und Insertionsoperator verwendet. Insbesondere hängt das Funktional

$$\varphi_{L_3^\circ}(a) := Wres_{BC}^{top}(aL_3^\circ)$$

von einem konkreten Repräsentanten ab. In den auditierten Quellen wurde nicht gezeigt, dass dieses Funktional nur von der Klasse $[L_3]$ abhängt.

---

## 170b.E — Fehlende Repräsentantenbrücke

Um die abstrakte und die konkrete Ebene quellenfest zu verbinden, wäre mindestens eine der folgenden Aussagen erforderlich:

**E.1 — Kanonische Auswahl**

$$\sigma_{L_3}: [L_3] \longmapsto L_3 \quad\text{mit eindeutig bestimmtem Repräsentanten.}$$

**E.2 — Repräsentantenunabhängigkeit**

Für $L_3' = L_3 + dH$ gilt:

$$Wres_{BC}^{top}\!\left(f(D)L_3'\right) = Wres_{BC}^{top}\!\left(f(D)L_3\right),$$

d.h. insbesondere $Wres_{BC}^{top}\!\left(f(D)dH\right) = 0$.

**E.3 — Quotientenrealisierung**

$$[L] \longmapsto \left[a \longmapsto Wres_{BC}^{top}(aL)\right]$$

steigt unmittelbar auf die Klasse ab.

$$\boxed{\text{Keine dieser drei Brücken ist im auditierten Quellenkegel ausgewiesen.}}$$

---

## 170b.F — Entscheidung zwischen den vier Befundtypen

**Typ 1 — Vollständig definierter konkreter Operator:** Nicht bestätigt. Es fehlen vollständige Formel, präziser Definitionsbereich und BC-intrinsische Konstruktion.

**Typ 2 — Ausgewählter Kozykel- oder Klassenrepräsentant:** Dies entspricht am besten der tatsächlichen downstream Verwendung. Die Wahl dieses Repräsentanten ist jedoch nicht konstruiert oder als kanonisch bewiesen.

**Typ 3 — Nur abstrakte Klasse:** Gilt für $[L_3]$ auf Architekturebene, beschreibt aber nicht vollständig die späteren Rechnungen.

**Typ 4 — Symbolischer Leitoperator:** Trifft teilweise zu: importierte Eigenschaften wie $C_L\neq0$, aber keine vollständige Konstruktion.

**Gesamtklassifikation:**

$$\boxed{L_3\text{ ist ein teilweise spezifizierter konkreter Operatorrepräsentant des abstrakten Objekt-}X\text{-Datums }[L_3].}$$

Er ist mehr als ein bloßes Symbol, weil konkrete Spur- und Normierungseigenschaften vorausgesetzt werden. Er ist weniger als ein vollständig konstruierter Operator, weil Herkunft, Definitionsbereich und Repräsentantenwahl nicht quellenfest vorliegen.

---

## 170b.G — Konsequenz für den Fouriergrad

Der gewichtete Fourierträger $\operatorname{supp}^{\times}(L_3^\circ)$ ist zunächst eine Eigenschaft des konkret verwendeten Repräsentanten $L_3^\circ$, nicht automatisch der Klasse $[L_3]$. Daher sind zwei Angriffswege strikt zu trennen:

**Operatorieller Weg F.1**

Bestimme den tatsächlich ausgewählten Leitoperator $L_3$ und berechne $\sum_{s,m}\ell_{s,m}e_sV_m$. Dieser Weg benötigt keine Klasseninvarianz; es genügt $\exists(s_0,m_0): s_0\ell_{s_0,m_0}\neq0$.

**Kohomologischer Weg F.2/F.3**

Zeige zunächst, dass der Fouriergrad auf die Klasse absteigt, und untersuche $[L_3]_{ch}\neq0$ oder $[L_3]\notin\operatorname{im}H^\bullet(C_0)$. Dieser Weg ist stärker, setzt aber die noch offene Differentialverträglichkeit voraus.

---

## 170b.H — Statusänderungen

$$\boxed{[O\text{-}170a\text{-}1a] \quad \checkmark[M].}$$

Befund: $L_3$ ist downstream ein fest verwendeter, teilweise spezifizierter Operatorrepräsentant des abstrakten Datums $[L_3]$.

$$\boxed{[O\text{-}170a\text{-}1b] \quad ?[O].}$$

Ursprüngliche Konstruktion offen: Wo wird $L_3$ erstmals definiert, und welche Freiheit besteht bei seiner Wahl?

---

## 170b.I — Neue offene Punkte

| Punkt | Inhalt |
|---|---|
| $[O\text{-}170b\text{-}1]$ | Direktaudit NEU-20/NEU-28: erste Definition von $L_3$ |
| $[O\text{-}170b\text{-}2]$ | Bestimmung des Raums: $L_3\in B_3$, $M(B_3)$, $\operatorname{End}(B_3)$, oder anderer Operatorraum |
| $[O\text{-}170b\text{-}3]$ | Definitionsbereich von $\operatorname{Tr}_{Hilbert}(L_3|_{\mathrm{diag}})$ und Bedeutung von „diagonal" |
| $[O\text{-}170b\text{-}4]$ | Konstruktion oder Ausschluss einer kanonischen Auswahl $\sigma_{L_3}:[L_3]\to L_3$ |
| $[O\text{-}170b\text{-}5]$ | Repräsentantenunabhängigkeit des $Wres$-Insertionsfunktionals |
| $[O\text{-}170b\text{-}6]$ | Nach positiver Ursprungsidentifikation: Fourierträger des tatsächlich gewählten Repräsentanten |

---

## 170b.J — Gesamtbefund und Stop-Regel

$$\boxed{[L_3]\text{ ist das abstrakte Strukturdatum;}}$$

$$\boxed{L_3\text{ ist der downstream fest eingesetzte, aber nicht vollständig hergeleitete Operatorrepräsentant.}}$$

Damit ist der nächste zulässige Angriff operatoriell, aber nur relativ zu einer direkten Identifikation des tatsächlich verwendeten Repräsentanten in NEU-20/NEU-28. Bis dahin bleiben gesperrt: $P^{ch}(L_3^\circ)\neq0$, $[L_3]_{ch}\neq0$, $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$.

$$\boxed{\text{NEU-170c — Direktaudit der ersten }L_3\text{-Definition in NEU-20/NEU-28}.}$$

Erst dieses Blatt entscheidet, ob der operatorielle Weg F.1 tatsächlich eröffnet ist oder ob zunächst eine fehlende Repräsentantenkonstruktion nachgetragen werden muss.

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-26 | $[L_3]$ als abstraktes Vierschichtdatum |
| NEU-29 | $L_3$ als konkreter Leitoperator (importiert, nicht konstruiert) |
| NEU-20/28 | Ursprungsblätter; Direktaudit in NEU-170c |
| NEU-170a | Vorblatt: negativer Fouriergrad-Quellenbefund |
| NEU-170c (nächster Knoten) | Direktaudit erste $L_3$-Definition |
| NEU-171 (gesperrt) | Normierungsgeometrie Einzelmodus |
