# NEU-240: [O-229-3B.1f-a] Minimalitätsaudit — Minimaler kohomologischer Mechanismus für τ_p

> Datum: 27. Juli 2026 | Status: **?[O]**

---

## 1. Einordnung und Zweck

NEU-239 hat [O-229-3B.1] als `✓[M]_neg,Quelle` geschlossen und [O-229-3B.1f]
als Konstruktionsdesiderat eröffnet. Der vorliegende Knoten

```
[O-229-3B.1f-a-minimal-cohomological-mechanism]
```

ist der erste atomare Unterknoten von [O-229-3B.1f]. Er stellt die
Minimalitätsfrage, bevor eine konkrete Konstruktion begonnen wird:

> Welche minimale koh omologische Struktur genügt, um ein repräsentantenunabhängiges
> lineares Funktional auf D(a_p) zu erzeugen, das die Positivitätsbarriere erfüllt?

Dieser Knoten verhindert, dass vorschnell eine aufwendige kurze exakte Folge
konstruiert wird, die zwar eine Kohomologieklasse erzeugt, aber keine positive,
Wres-verträgliche Mischform liefert.

---

## 2. Unverhandelbare Zielbedingungen

Jeder Realisierungstyp muss dieselben Mindestziele erfüllen. Sie sind nicht
verhandelbar und können nicht durch eine Konstruktionswahl umgangen werden.

### Z.1 Linearität und Repräsentantenunabhängigkeit

```
β_p(k) := τ_p(𝔟_p)(k)   ist linear in k
τ_p(𝔟_p)(k)           hängt nicht vom Koketten- oder Liftrepräsentanten ab
```

### Z.2 Positivitätskontrolle

```
|β_p(k)|² ≤ a_p(k,k)   für alle k ∈ D(a_p)
```

### Z.3 Rad-Verträglichkeit

```
Rad(a_p) ⊆ ker β_p
```

d.h. k ∈ Rad(a_p) ⟹ β_p(k) = 0.

### Z.4 Wres-Nichttrivialität

```
∃ k :  β_p(k) ≠ 0   und   T_p^raw k ∉ N_{Wres,rel}
```

---

## 3. Die Positivitätsbarriere als strukturelle Schranke

Die Zielbedingung Z.2 ist nicht automatisch aus einer Hochschild- oder
zyklischen Paarung gewährleistet. Eine gewöhnliche algebraische Paarung
liefert ein lineares Funktional, aber keine Norm-Abschätzung.

**Schlüsselbeobachtung:** Damit Z.2 gilt, muss β_p durch T_p^raw faktorisieren:

```
β_p = Λ_p ∘ T_p^raw
```

mit einem beschränkten linearen Funktional

```
Λ_p : Ran T_p^raw̅  ⟶  ℂ,    ||Λ_p|| ≤ √α_p.
```

**Begründung:** Es gilt a_p(k,k) = α_p · ||T_p^raw k||² (Definition der
Rohkopplungsform). Aus

```
β_p(k) = Λ_p(T_p^raw k),    |Λ_p(v)| ≤ √α_p · ||v||
```

folgt unmittelbar |β_p(k)|² ≤ α_p · ||T_p^raw k||² = a_p(k,k). ✓

Umgekehrt: Wenn β_p nicht durch T_p^raw faktorisiert, ist Z.2 im Allgemeinen
nicht erfüllbar.

**Konsequenz für das Minimalitätsaudit:**

```
Gesucht ist nicht irgendeine Randklasse, sondern eine kohomologisch erzeugte
beschränkte Funktionalstruktur auf Ran T_p^raw̅.
```

Jeder Realisierungstyp muss erklären, wie er Λ_p auf Ran T_p^raw̅ induziert.

---

## 4. Vier Realisierungstypen — Klassifikation

### Typ I: Verbindungshomomorphismus einer kurzen exakten Folge

**Struktur:**
```
0  ⟶  C_{p,1}^•  ⟶  C_{p,2}^•  ⟶  C_{p,3}^•  ⟶  0
δ_p : H^n(C_{p,3}^•)  ⟶  H^{n+1}(C_{p,1}^•)
τ_p(𝔟)(k) = ⟨ δ_p 𝔟, ȷ_p(k) ⟩
```

**Positivitätsprüfung:** Die Paarung ⟨·,·⟩ auf H^{n+1}(C_{p,1}^•) ist
allgemein unbeschränkt. Damit Z.2 gilt, muss ⟨δ_p 𝔟, ȷ_p(k)⟩ durch
||T_p^raw k|| kontrollierbar sein. Das erfordert eine zusätzliche Normabschätzung,
die nicht aus der exakten Folge allein folgt.

**Offene Punkte:**
- Wahl von C_{p,1}^•, C_{p,2}^•, C_{p,3}^• aus den vorhandenen algebraischen Objekten
- Konstruktion von ȷ_p : D(a_p) ⟶ X_p typkorrekt
- Nachweis der Normabschätzung für ⟨δ_p 𝔟, ȷ_p(·)⟩

**Vorläufige Einschätzung:** Möglich, aber nicht minimal — Normkontrolle
erfordert Zusatzstruktur über die exakte Folge hinaus.

---

### Typ II: Relative Hochschild-/zyklische Kohomologie

**Struktur:**
```
HH^n(A, B)   oder   HC^n(A, B)
für ein geeignetes Untermodul B ⊆ A

τ_p(𝔟)(k) = ⟨ [𝔟]_{rel}, k ⟩
```

wobei das relative Paar (A, B) so gewählt wird, dass die relative Klasse
automatisch auf Rad(a_p) verschwindet.

**Positivitätsprüfung:** Relative Klassen sind repräsentantenunabhängig
relativ B. Die Normabschätzung hängt von der Wahl der Paarung auf dem
relativen Komplex ab.

**Offene Punkte:**
- Identifikation des relevanten relativen Paares (A_{2D}^r, B_p)
- Verbindung der relativen Kohomologie mit D(a_p) und T_p^raw
- Ob Rad(a_p) ⊆ ker automatisch folgt oder zusätzlich gefordert werden muss

**Vorläufige Einschätzung:** Vielversprechend für Repräsentantenunabhängigkeit;
Normkontrolle bleibt offen.

---

### Typ III: Mapping-Cone- oder Transgressionskomplex

**Struktur:**
```
Cone(f)^•   für eine Kettenabbildung  f : C_{p,A}^• ⟶ C_{p,B}^•
Transgression T : Ω^n(C_{p,A}) ⟶ Ω^{n+1}(C_{p,B})
```

Der Mapping Cone erzeugt eine lange exakte Kohomologiesequenz mit
naturlichem Verbindungsterm. Alternativ liefert ein Transgressionskomplex
(z.B. aus einer Hauptfaserbundel-analogen Struktur) direkt eine Abbildung
von Randklassen in den nächsthohem Komplex.

**Positivitätsprüfung:** Die Transgression in einem Mapping-Cone-Komplex
ist durch die Kettenabbildung f kontrolliert. Falls f mit T_p^raw kompatibel
ist (d.h. f faktorisiert über T_p^raw), könnte die Normabschätzung aus
der Beschränktheit von T_p^raw folgen.

**Offene Punkte:**
- Konstruktion der Kettenabbildung f aus vorhandenen Objekten
- Nachweis der Kompatibilität f ∘ ȷ_p ~ T_p^raw
- Verbindung mit der Wres-Struktur

**Vorläufige Einschätzung:** Strukturell am direktesten mit der
Faktorisierungsbedingung β_p = Λ_p ∘ T_p^raw vereinbar, wenn f geeignet
gewählt wird. Erfordert aber nichttriviale Konstruktion von f.

---

### Typ IV: Direkte Ketten-Koketten-Paarung

**Struktur:**
```
⟨·,·⟩ : C_n(D(a_p))  ×  C^n(A_{2D}^r)  ⟶  ℂ
β_p(k) := ⟨ c_p, φ_p ⟩
```

wobei c_p ein ausgezeichneter Zyklus in C_n(D(a_p)) und φ_p ein
Hochschild-Kochain ist, der aus der HH²-Struktur von A_{2D}^r gewonnen wird.

**Positivitätsprüfung:** Eine direkte Paarung ohne Verbindungshomomorphismus
umgeht das exakte-Folge-Problem, verlagert aber die Repräsentantenunabhängigkeit
auf die Zykluswahl c_p. Normkontrolle hängt vollständig von der konkreten
Paarungsdefinition ab.

**Offene Punkte:**
- Kanonische Auswahl von c_p (ohne Zirkularität)
- Verbindung mit T_p^raw für Normabschätzung
- Repräsentantenunabhängigkeit ohne exakte Folge als Schutzstruktur

**Vorläufige Einschätzung:** Am wenigsten strukturiert; Repräsentantenunabhängigkeit
erfordert zusätzliche Axiome oder Kanonizitätsbedingungen.

---

## 5. Vergleichsmatrix der vier Typen

| Typ | Repräsentantenunabh. | Positivität Z.2 | Rad-Verträgl. Z.3 | Wres-Nichttrivialität Z.4 | Minimalität |
|---|---|---|---|---|---|
| I (kurze exakte Folge) | ✓ durch δ_p | Zusätzliche Normabsch. nötig | Offen | Offen | Nicht minimal |
| II (relativ HH/HC) | ✓ relativ B | Offen | Evtl. automatisch | Offen | Teilweise minimal |
| III (Mapping Cone) | ✓ durch f | Evtl. durch f ~ T_p^raw | Offen | Offen | Vielversprechend |
| IV (direkte Paarung) | Zusätzl. Axiome nötig | Vollständig offen | Offen | Offen | Nicht minimal |

**Zwischenfazit:** Kein Typ erfüllt alle vier Zielbedingungen automatisch.
Die Positivitätsbarriere (Z.2) ist in allen Fällen die härteste Hürde.
Typ III erscheint am direktesten mit der Faktorisierungsbedingung
β_p = Λ_p ∘ T_p^raw vereinbar, ist aber noch nicht konstruiert.

---

## 6. Leitfrage für den weiteren Audit

```
┌──────────────────────────────────────────────────────────────────────────┐
│  Welcher der vier Realisierungstypen ermöglicht eine kohomologisch             │
│  erzeugte beschränkte Funktionalstruktur                                    │
│                                                                             │
│      Λ_p : Ran T_p^raw̅  ⟶  ℂ,   ||Λ_p|| ≤ √α_p,                       │
│                                                                             │
│  mit minimaler zusätzlicher Struktur über das vorhandene algebraische       │
│  Gerüst (A_{2D}^r, a_p, T_p^raw, N_{Wres,rel}) hinaus?                     │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Abhängigkeitsstruktur

```
[O-229-3B.1]     ✓[M]_neg,Quelle       (NEU-239, geschlossen)
       │
       ▼
[O-229-3B.1f]    ?[O]                  (NEU-239, geöffnet)
       │
       ▼
[O-229-3B.1f-a]  ?[O]                  (NEU-240, aktiv)
       │
       ├──▶ [O-229-3B.1f-b]  Typ-I-Konstruktion     (blockiert bis 3B.1f-a)
       ├──▶ [O-229-3B.1f-c]  Typ-II-Konstruktion    (blockiert bis 3B.1f-a)
       ├──▶ [O-229-3B.1f-d]  Typ-III-Konstruktion   (blockiert bis 3B.1f-a)
       └──▶ [O-229-3B.1f-e]  Typ-IV-Konstruktion    (blockiert bis 3B.1f-a)
```

| Knoten | Status | Bedingung |
|---|---|---|
| [O-229-3B.1f-a] | ?[O] | aktiv (NEU-240) |
| [O-229-3B.1f-b] bis [O-229-3B.1f-e] | ?[O]_blockiert | warten auf Minimalitätsentscheid aus 3B.1f-a |
| [O-229-3B.2] bis [O-229-3B.5] | ?[O]_blockiert | warten auf positiven Abschluss von 3B.1f |

---

## 8. Arbeitsstatus

```
[O-229-3B.1f-a]   ?[O]

Zwischenfazit: Kein Realisierungstyp erfüllt die Positivitätsbarriere
automatisch. Typ III (Mapping Cone / Transgressionskomplex) ist am
direktesten mit der Faktorisierungsbedingung β_p = Λ_p ∘ T_p^raw vereinbar.
Konstruktion steht aus.
```

---

*Datei: `NEU-240_O229-3B1f-a_Minimalitaetsaudit_kohomologischer_Mechanismus.md` | Erstellt: 27. Juli 2026*
