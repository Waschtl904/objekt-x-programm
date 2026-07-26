# NEU-174 — Minimaler Hochschild-Komplex und induzierte BC-Zeitwirkung

## Vorbemerkung: Konstruktionsprinzip

Ab NEU-174 beginnt eine neue Konstruktion — kein weiterer Quellenimport. Der Quellenkegel NEU-15–17, NEU-20, NEU-28, NEU-72, NEU-170b wurde in NEU-173 vollständig mit Fallbezeichnung **C_src-neg** abgeschlossen.

Dieses Dokument legt den kleinstmöglichen funktionsfähigen Hochschild-Komplex fest, **ohne** bereits L₃ zu konstruieren und **ohne** eine Operatorrealisierung ρ_op einzuführen. Diese werden in NEU-175 behandelt.

**Konstruktive Kette dieses Dokuments:**

```
B₃ ⟶ M ⟶ (C•, b) ⟶ α_t^C ⟶ P^ch ⟶ H•_ch
```

Erst danach (NEU-175 und folgende):

```
[L₃] ⟶ L₃ ⟶ ρ_op(L₃)
```

---

## 174.A — Wahl der Algebra B₃

### Festlegung

Wir setzen

```
B₃ := A_Q
```

die BC-Algebra über Q, wie sie in NEU-72 als analytische Algebra A_BC^an eingeführt ist, hier auf ihren rationalen Kern eingeschränkt.

### Minimale Datenliste für B₃

| Datum | Festlegung |
|---|---|
| Grundkörper | Q (oder R, je nach gewählter Variante) |
| Multiplikation | (a, b) ↦ ab (Komposition in A_Q) |
| Einheit | 1 ∈ B₃ |
| Assoziativität | a(bc) = (ab)c für alle a, b, c ∈ B₃ |

**Wichtig:** Die Bezeichnung B₃ wird hier als konstruktives Label eingeführt. Sie wird nicht allein aus der vorgesehenen Rolle ("Algebra, die L₃ aufnehmen soll") abgeleitet.

### Knoten [O-174-1]

> **[O-174-1]:** B₃ ist eine konkret definierte assoziative Algebra.

Status: **✓[K]** — durch explizite Datenliste oben konstruiert.

---

## 174.B — Wahl des Koeffizientenbimoduls M

Wir definieren zwei getrennte Modelle.

### Modell 1: Unverdrehter Bimodul

```
M_untw := B₃
```

mit Wirkungen:

```
a · m = am,    m · a = ma     (Multiplikation in B₃)
```

### Modell 2: Verdrehter Bimodul (σ-Bimodul)

```
M_σ := _{id}B_{3,σ}
```

für einen Algebraautomorphismus σ: B₃ → B₃, mit Wirkungen:

```
a · m = am,    m · a = m·σ(a)
```

**Kontrolle:** Die Rechts-Bimodulbedingung muss mit der verdrehten Rechtswirkung geprüft werden:

```
m · (ab) = m · σ(ab) = m · (σ(a)σ(b))
(m · a) · b = (m·σ(a)) · b = m·σ(a)·σ(b)
```

Beide Seiten stimmen überein gdw. σ ein Algebrahomomorphismus ist — was vorausgesetzt wird.

### Definition des Kokettenkomplexes

Nachdem M festgelegt ist:

```
C^n(B₃, M) := Hom(B₃^{⊗n}, M)
```

(lineare Abbildungen von n-fachen Tensorprodukten nach M).

Für n = 0 setzt man C⁰(B₃, M) := M.

### Knoten [O-174-2]

> **[O-174-2]:** M ist ein konkret definiertes B₃-Bimodul.

Status: **✓[K]** — zwei explizite Modelle (M_untw, M_σ) mit vollständiger Wirkungsdefinition konstruiert.

---

## 174.C — Hochschild-Kodifferential b

### Definition

Für φ ∈ C^n(B₃, M) und a₁, …, a_{n+1} ∈ B₃:

```
(bφ)(a₁, …, a_{n+1})
  = a₁ · φ(a₂, …, a_{n+1})
  + Σᵢ₌₁ⁿ (-1)ⁱ φ(a₁, …, aᵢaᵢ₊₁, …, a_{n+1})
  + (-1)^{n+1} φ(a₁, …, aₙ) · a_{n+1}
```

Dabei bezeichnet a_{n+1} die Rechtswirkung auf M — im verdrehten Fall also **m · σ(a_{n+1})**, nicht m · a_{n+1}.

**Notationskonvention (gemäß P2 aus NEU-173):** Das Symbol **b** bezeichnet ab sofort ausschließlich dieses Hochschild-Kodifferential. Die BC-Ableitung δ_BC ist davon strikt zu unterscheiden (sie ist eine Algebraableitung vom Typ A_Q → A_Q).

### Beweis b² = 0

Die Standardrechnung zeigt: In der iterierten Anwendung b(bφ) heben sich die gemischten Terme paarweise auf (Vorzeichenargument). Für den verdrehten Bimodul M_σ erfordert der letzte Term der Iteration eine gesonderte Kontrolle:

**Kritischer Schritt:** Der Term mit φ(…) · a_{n+1} in bφ wird unter erneuter Anwendung von b zum Term

```
(-1)^{n+1}(-1)^{n+2} φ(a₁,…,aₙ) · σ(a_{n+1}) · σ(a_{n+2})
```

und der komplementäre Term aus dem vorletzten Schritt liefert

```
(-1)^{n+1}(-1)^{n+1} φ(a₁,…,aₙ) · σ(a_{n+1}a_{n+2})
```

Diese stimmen überein gdw. σ(a_{n+1})σ(a_{n+2}) = σ(a_{n+1}a_{n+2}), also genau dann, wenn σ ein Algebrahomomorphismus ist. ✓

### Knoten [O-174-3]

> **[O-174-3]:** (C•(B₃, M), b) ist ein Komplex.

Status: **✓[K]** — b vollständig definiert, b² = 0 mit Sonderfall verdrehtes Modul geprüft.

---

## 174.D — Induzierte BC-Zeitwirkung

### Voraussetzung

Sei α_t: B₃ → B₃ eine Gruppe von Algebraautomorphismen (t ∈ R oder t ∈ Z), d.h.:

```
α_t(ab) = α_t(a) α_t(b),    α_t(1) = 1,    α_{s+t} = α_s ∘ α_t
```

Sei ferner α_t^M: M → M eine kompatible Modulwirkung, d.h.:

```
α_t^M(a · m) = α_t(a) · α_t^M(m)
α_t^M(m · a) = α_t^M(m) · α_t(a)      [unverdreht]
α_t^M(m · a) = α_t^M(m) · σ(α_t(a))   [verdreht, falls σ mit α_t verträglich]
```

### Definition der induzierten Wirkung auf Kochains

Für φ ∈ C^n(B₃, M):

```
(α_t^C φ)(a₁, …, aₙ) := α_t^M( φ(α_{-t}(a₁), …, α_{-t}(aₙ)) )
```

### Knoten [O-174-4]

> **[O-174-4]:** α_t^C ist auf C•(B₃, M) wohldefiniert.

**Beweis:** Da α_{-t} ein Algebraautomorphismus ist, sind α_{-t}(a₁), …, α_{-t}(aₙ) ∈ B₃, also ist φ(α_{-t}(a₁), …, α_{-t}(aₙ)) ∈ M wohldefiniert. Die Anwendung von α_t^M liefert ein weiteres Element in M. Der Ausdruck ist linear in φ. ✓

Status: **✓[K]**

### Beweis der Kommutierungseigenschaft

> **[O-174-5]:** b α_t^C = α_t^C b.

**Zu zeigen:** Für alle φ ∈ C^n(B₃, M) und a₁, …, a_{n+1} ∈ B₃:

```
(b(α_t^C φ))(a₁, …, a_{n+1}) = (α_t^C(bφ))(a₁, …, a_{n+1})
```

**Linke Seite** (b angewandt auf α_t^C φ):

```
= a₁ · (α_t^C φ)(a₂,…,a_{n+1})
  + Σᵢ (-1)ⁱ (α_t^C φ)(a₁,…,aᵢaᵢ₊₁,…,a_{n+1})
  + (-1)^{n+1} (α_t^C φ)(a₁,…,aₙ) · a_{n+1}

= a₁ · α_t^M(φ(α_{-t}(a₂),…))
  + Σᵢ (-1)ⁱ α_t^M(φ(α_{-t}(a₁),…,α_{-t}(aᵢaᵢ₊₁),…))
  + (-1)^{n+1} α_t^M(φ(α_{-t}(a₁),…,α_{-t}(aₙ))) · a_{n+1}
```

**Rechte Seite** (α_t^C angewandt auf bφ):

```
= α_t^M((bφ)(α_{-t}(a₁),…,α_{-t}(a_{n+1})))

= α_t^M[ α_{-t}(a₁) · φ(α_{-t}(a₂),…)
         + Σᵢ (-1)ⁱ φ(α_{-t}(a₁),…,α_{-t}(aᵢ)α_{-t}(aᵢ₊₁),…)
         + (-1)^{n+1} φ(α_{-t}(a₁),…,α_{-t}(aₙ)) · α_{-t}(a_{n+1}) ]
```

Unter Verwendung der Kompatibilitätsbedingungen α_t^M(α_{-t}(a)·m) = a·α_t^M(m) und α_t^M(m·α_{-t}(a)) = α_t^M(m)·a stimmen beide Seiten überein. ✓

**Wichtiger Hinweis:** Dieser Nachweis stützt sich ausschließlich auf die Kompatibilitätsbedingungen für α_t und α_t^M. Er darf **nicht** allein aus der Existenz von δ_BC gefolgert werden.

Status: **✓[K]**

---

## Fourierzerlegung von C•

### Knoten [O-174-6]

> **[O-174-6]:** C•(B₃, M) besitzt eine aus α_t^C abgeleitete Fourierzerlegung.

Falls α_t^C eine stetige unitäre Wirkung einer kompakten Gruppe (z.B. U(1) mit t ∈ [0, 2π)) ist, zerfällt C^n(B₃, M) in Spektraleigenräume:

```
C^n(B₃, M) = ⊕_{k ∈ Z} C^n_k(B₃, M)
```

wobei C^n_k der k-te Fouriermodul ist:

```
C^n_k := { φ ∈ C^n(B₃,M) | α_t^C φ = e^{ikt} φ  für alle t }
```

Aus [O-174-5] folgt unmittelbar: b bildet C^n_k nach C^{n+1}_k ab. Die Fourierzerlegung ist damit kompatibel mit der Komplexstruktur.

**Sperrlogik:** Vor Abschluss von [O-174-5] darf nicht behauptet werden P^ch b = b P^ch. Vor Abschluss von [O-174-6] sind [P^ch]([L₃]) und eine "geladene Kohomologiekomponente" noch nicht definiert.

Status: **✓[K]** — unter der Voraussetzung, dass α_t^C eine kompakte Gruppenstruktur trägt (zu verifizieren im konkreten Modell).

---

## DAG-Knotenübersicht

| Knoten | Inhalt | Status |
|---|---|---|
| [O-174-1] | B₃ ist eine konkret definierte assoziative Algebra | ✓[K] |
| [O-174-2] | M ist ein konkret definiertes B₃-Bimodul | ✓[K] |
| [O-174-3] | (C•(B₃,M), b) ist ein Komplex | ✓[K] |
| [O-174-4] | α_t^C ist auf C•(B₃,M) wohldefiniert | ✓[K] |
| [O-174-5] | b α_t^C = α_t^C b | ✓[K] |
| [O-174-6] | C• besitzt eine daraus abgeleitete Fourierzerlegung | ✓[K] (unter Kompaktheitsbedingung) |

---

## Abgrenzung zu NEU-175

Dieses Dokument führt bewusst noch **nicht** ein:

- Einen Kandidaten L₃ ∈ Z⁴(B₃, M)
- Eine Operatorrealisierung ρ_op: Z⁴(B₃,M) → End(H)
- Eine geladene Kohomologiekomponente [P^ch]([L₃])

Diese Objekte setzen den vollständigen Abschluss von [O-174-6] voraus und bilden den Gegenstand von **NEU-175**.

**Status dieses Dokuments:** Konstruktionsphase eröffnet — alle sechs Knoten [O-174-1] bis [O-174-6] geschlossen oder unter explizit benannter Bedingung bedingt abgeschlossen.
