# Forschungsagenda — OP-4.1: Strikte Frobenius-Kompatibilität

> Datum: 20. Juni 2026 | Nach OP-3-Abschluss (NEU-17–20)
> Status: ✓ [M] (OP-4.1 strukturell vollständig, NEU-21–25) | ⚠ [M] (OP-4.1a Stetigkeit, Ext¹)

---

## 1. Kontext

OP-3 hat gezeigt: [L₃] ≠ 0 in HH⁴(F³ A_BC^{an}) — durch den
BC-Wodzicki-Koeffizienten Wres_BC^{(2,0)}.

Die twisted-trace-Eigenschaft von Wres_BC^{top} wurde bewiesen (NEU-19,
Twist-Stabilität). Aber das ist eine **globale** Aussage: Wres_BC^{top} ist
ν₁-twisted für alle a, b ∈ F³ A_BC^{an}.

OP-4.1 fragt nach der **strikten Frobenius-Kompatibilität**: Verträgt sich
diese Struktur mit dem Filtrations-Diagramm R₃ → Gr³ → Π_{diag,0} → ε_β?

---

## 2. OP-4.1 — Präzise Formulierung

**Zu zeigen:**

Das folgende Diagramm ist kommutativ und mit der modularen Frobenius-Paarung
kompatibel:

```
F³ A_BC^{an}  ─────R₃──────→  Gr³ A_BC^{an}  ──Π_{diag,0}──→  ℓ¹_β  ──Σm^{-β}──→  ℂ
     │                               │                                               │
  a·b ↦ ε_β(ab) = ε_β(b·ν_β(a))     │          gleiches Diagramm für b·ν(a)          │
     │                               │                                               │
     └───────────────────────────────┴──────────────────────────────────────────────┘
```

Konkret:

**(OP-4.1a)** Stetigkeit: R₃, Π_{diag,0}, ε_β sind auf der Kette stetig und
die Komposition F³ A_BC^{an} → ℂ ist stetig (β > 1).  ⚠ [M] (aus NEU-18)

**(OP-4.1b)** Frobenius-Kompatibilität:
```
Wres_BC^{top}(ab) = Wres_BC^{top}(b · ν₁(a))
```
für alle a, b aus einem dichten Teilraum von F³ A_BC^{an}.  ✓ [M] (NEU-19, Twist-Stab.)

**(OP-4.1c)** Nicht-Ausgeartheit:
```
Wres_BC^{top} : HH⁴(F³ A_BC^{an}) → ℂ   ist nicht-ausgeartet
```
d.h. kein [Ψ] ≠ 0 mit Wres_BC^{top}(Ψ) = 0.

**(OP-4.1c)** ist der eigentliche neue Inhalt. Es bedeutet: Die Paarung
```
HH⁴(F³ A_BC^{an}) × HH₄(F³ A_BC^{an}) → ℂ,   (Ψ, c) ↦ Wres_BC^{top}(Ψ(c))
```
ist nicht-ausgeartet.

**Status (Stand NEU-23): ✓ [M]**

```
OP-4.1c.1 (NEU-21): B nicht-ausgeartet auf HH⁴_vis       ✓ [M]
OP-4.1c.2 (NEU-22): ker(R₃) ∩ HH⁴ = 0                  ✓ [M]
OP-4.1c.3 (NEU-23): Diagonal-Neutralität (χ=1-Dominanz)  ✓ [M]
```

---

## 3. Warum OP-4.1 vor X.2

X.2 benötigt eine stabile Paarungsmaschine
```
HH• × HH_• → ℂ
```
um die Spektralformel
```
Tr_Wres(f(D_X) · L₃) ↔ Σ_ρ f(ρ)
```
sinnvoll zu formulieren. Ohne nicht-ausgeartete Paarung ist diese Formel
nicht wohldefiniert.

Außerdem: Erst wenn Wres_BC^{top} als echte nicht-ausgeartete Frobenius-Form
etabliert ist, kann man fragen, was das Spektrum des dualen Operators D_X ist.

---

## 4. Ansatz für OP-4.1c

**Schritt 1 — Trennungsargument:**

Zeige: Für jedes [Ψ] ≠ 0 in HH⁴(F³ A_BC^{an}) existiert ein c₄ mit
Wres_BC^{top}(Ψ(c₄)) ≠ 0.

Das folgt aus der universellen Eigenschaft von Wres_BC^{top} als "dichter"
Funktional auf F³ A_BC^{an}: Ein Funktional, das auf dem nm-Sektor (via Λ²)
den Doppelpol produziert, trennt Klassen, die von null verschiedene
Diagonalkoeffizienten tragen.

**Schritt 2 — Λ-Typ-Argument:**

Da Wres_BC^{(2,0)} durch (-ζ'/ζ)² dominiert wird (Doppelpol), und
(-ζ'/ζ)² ≠ 0 als meromorphe Funktion, ist Wres_BC^{(2,0)} als Funktional
nicht identisch null. Für die Nicht-Ausgeartheit braucht man mehr:
das Bild muss "groß genug" sein.

**Schritt 3 — Filtrations-Kompatibilität:**

Der Grad-3-Quotient Gr³ A_BC^{an} ist ein (A_2D^r)-Bimodul.
Die Nicht-Ausgeartheit von ε_β auf A_2D^r (OP-4 aus NEU-15) überträgt sich
auf Gr³ via R₃, sofern R₃ surjektiv auf den relevanten Diagonalsektoren ist
(was aus der Definition von R₃ als Quotient folgt).

---

## 5. Verbindung zu X.2: Übersetzungsformel

Nach OP-4.1 wird X.2 reformulierbar als:

**Neue X.2-Formulierung:**
```
Die RH-Nullstellen erscheinen als Spektralschatten der Residuenpaarung
Wres_BC^{top}([L₃]).

Konkret: ∃ Operator D_X auf (einem Erweiterungsraum von) F³ A_BC^{an},
so dass:
  Tr_Wres(f(D_X) · L₃) = Σ_ρ f(ρ)   für alle Testfunktionen f.
```

Die Brücke zwischen Primseite und Nullstellenseite:
```
Λ*Λ  ←→  (ζ'/ζ)²  ←→  Σ_ρ 1/(β-ρ)²  (Hadamard-Entwicklung)
```

Das bedeutet: Der Doppelpol von Wres_BC^{(2,0)} korrespondiert auf der
Nullstellenseite zu einem **quadratischen Weil-Term** — genau dem Typ,
der in expliziten Formeln der Primzahltheorie (Weil'sche explizite Formel)
auftritt.

---

## 6. Erwarteter Satz (OP-4.1)

**Lemma OP-4.1 (Vorschau):**

> Die Paarung
>
>     B : HH⁴(F³ A_BC^{an}) × HH₄(F³ A_BC^{an}) → ℂ
>     B(Ψ, c) := Wres_BC^{top}(Ψ(c))
>
> ist ν₁-twisted (✓ [M] aus NEU-19) und nicht-ausgeartet (❓ [O]).
>
> Insbesondere liefert B eine strikte modulare Frobenius-Paarung auf
> der graduierten Komponente Gr³ A_BC^{an}.

---

## 7. Verbindung zum alten OP-4

OP-4 (NEU-15) fragte: Existiert auf A_2D^r ein Frobenius-Funktional im
strikten algebraischen Sinn?

OP-4.1 ist die präzisierte Version: Ist Wres_BC^{top} dieses strikte
Frobenius-Funktional — jetzt nicht mehr auf A_2D^r, sondern auf Gr³ A_BC^{an}?

Das ist eine natürliche Verschärfung: Wres_BC^{top} ist explizit (NEU-19/20),
ν₁-twisted (NEU-19), und kandidiert als das gesuchte Objekt aus OP-4.

---

*Datei: `OP-4-1-forschungsagenda.md` | 20. Juni 2026*
*Vorbereitungsdokument für NEU-21 (OP-4.1-Beweis)*
