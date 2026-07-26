# NEU-29 — X.2.3: Cauchy-Spurformel

> Datum: 28. Juni 2026 | Aufbauend auf NEU-28 (R_X = C_L·K_ξ)
> Status: ✓ [M] lokale Cauchy-Spurformel (relativ zu NEU-28) | ⚠ [M] Konturvertauschung | ❓ [O] BC-intrinsisches D_X^{BC}

---

## Aufgabe

NEU-28 hat gezeigt:

```
R_X^ξ(s) = Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃ ) = C_L · K_ξ(s).
```

X.2.3 muss daraus die Spurformel folgern:

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃ ) = C_L · Σ_ρ m_ρ · f(ρ).
```

Und nach Normierung L₃° := C_L^{-1} · L₃:

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃° ) = Σ_ρ m_ρ · f(ρ).
```

---

## 1. Normalisierungspunkt

### 1.1 Herkunft von C_L

NEU-28 liefert λ_mod(s) = C_L/ζ(s) mit

```
C_L = Tr_Hilbert(L₃|_{diag}) ∈ ℂ×.
```

C_L ist nicht kanonisch 1 — es hängt von der Wahl des Repräsentanten
L₃ ∈ HH⁴(B₃) ab.

### 1.2 Normierung

Da [L₃] ∈ HH⁴(B₃) eine Kohomologieklasse ist, kann man frei skalieren.

**Kanonische Normierung:**

```
L₃° := C_L^{-1} · L₃,
```

so dass Tr_Hilbert(L₃°|_{diag}) = 1 und:

```
R_X^ξ(s) = Tr_Wres^{top}( (s − D_X^{BC})^{-2} · L₃° ) = K_ξ(s).
```

Im Rest von NEU-29 arbeiten wir mit L₃° und lassen das ° aus Gründen
der Lesbarkeit weg (d.h. wir setzen C_L = 1).

**Ohne Normierung** bleibt die korrekte Aussage stets:

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃ ) = C_L · Σ_ρ m_ρ · f(ρ).
```

**Marker:** ✓ [M]

---

## 2. Doppelresolvent-Cauchy-Kalkül

### 2.1 Definition von f(D_X^{BC}) via Cauchy-Formel

Sei Γ eine positiv orientierte, stückweise glatte geschlossene Kurve in
ℂ, die endlich viele Nullstellen ρ₁,...,ρ_N (mit Vielfachheiten m_{ρᵢ})
im Inneren int(Γ) einschließt, und die das Spektrum von D_X^{BC}
außerhalb int(Γ) nicht schneidet.

Sei F : ℂ → ℂ holomorph in einer Umgebung von Γ ∪ int(Γ) mit F' = f.

**Definition (Doppelresolvent-Funktionalkalkül):**

```
f(D_X^{BC}) := 1/(2πi) · ∫_Γ F(s) · (s − D_X^{BC})^{-2} ds,
```

wobei das Integral als stark konvergentes Bochner-Integral auf dem
Definitionsbereich von (s − D_X^{BC})^{-2} zu verstehen ist.

**Begründung:** Per Cauchy-Formel gilt für jeden Pol s = ρ der Ordnung m_ρ:

```
1/(2πi) · ∫_Γ F(s) · m_ρ/(s−ρ)² ds = m_ρ · F'(ρ) = m_ρ · f(ρ).
```

Also realisiert die Formel genau die gewünschten Residuen. ✓ [M]

### 2.2 Konsistenz mit dem Standard-Kalkül

Der Standard-holomorphe Funktionalkalkül (Riesz-Dunford) verwendet:

```
f(D) = 1/(2πi) · ∫_Γ f(s) · (s − D)^{-1} ds   (einfacher Resolvent).
```

Der hier verwendete Doppelresolvent-Kalkül mit F (F' = f) ist damit
konsistent: Partielle Integration auf Γ liefert (formal):

```
1/(2πi) · ∫_Γ F(s) · (s−D)^{-2} ds
= −1/(2πi) · ∫_Γ F'(s) · d/ds[(s−D)^{-1}]^{-1} ds · ...
```

Das ist nicht direkt die Partielle-Integration-Route. Korrekte Begründung:
Die Cauchy-Formel für Doppelpole liefert direkt

```
Res_{s=ρ}[ F(s)·(s−ρ)^{-2} ] = F'(ρ) = f(ρ),
```

und die Summe über alle Pole in int(Γ) ist:

```
1/(2πi) · ∫_Γ F(s) · Σ_ρ m_ρ/(s−ρ)² ds = Σ_ρ m_ρ · f(ρ).   ✓ [M]
```

---

## 3. Lokale Cauchy-Spurformel

### Theorem X.2.3 (lokal) ✓ [M] relativ zu NEU-28

**Voraussetzungen:**

(V1) R_X^ξ(s) = K_ξ(s)  (NEU-28, nach Normierung C_L = 1)

(V2) Γ schließt endlich viele Nullstellen ρ ∈ int(Γ) ein, keinen Pol
     von K_ξ außerhalb int(Γ).

(V3) Die Wres^{top}-Konturvertauschung ist gültig (§4 unten).

(V4) F holomorph auf Γ ∪ int(Γ) mit F' = f.

**Behauptung:**

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃° )
= 1/(2πi) · ∫_Γ F(s) · Tr_Wres^{top}( (s−D_X^{BC})^{-2} · L₃° ) ds
= 1/(2πi) · ∫_Γ F(s) · K_ξ(s) ds
= Σ_{ρ ∈ int(Γ)} m_ρ · f(ρ).
```

**Beweis:**

```
Schritt 1: Definition f(D_X^{BC}) = (2πi)^{-1}∫_Γ F(s)(s−D_X^{BC})^{-2}ds.

Schritt 2: Wres-Linearität und Konturvertauschung (V3):
  Tr_Wres^{top}(f(D_X^{BC})·L₃°)
  = (2πi)^{-1} ∫_Γ F(s) · Tr_Wres^{top}((s−D_X^{BC})^{-2}·L₃°) ds.

Schritt 3: Einsetzen von (V1):
  = (2πi)^{-1} ∫_Γ F(s) · K_ξ(s) ds.

Schritt 4: Cauchy-Residuensatz (V4):
  = Σ_{ρ ∈ int(Γ)} Res_{s=ρ}[ F(s)·K_ξ(s) ]
  = Σ_{ρ ∈ int(Γ)} m_ρ · F'(ρ)
  = Σ_{ρ ∈ int(Γ)} m_ρ · f(ρ).   □
```

---

## 4. Konturvertauschung: Wres und ∫_Γ

### 4.1 Das Problem

Schritt 2 im Beweis vertauscht Wres_BC^{top} (ein stetiges lineares
Funktional auf B₃) mit dem Bochner-Integral ∫_Γ. Das erfordert:

```
Wres_BC^{top}( ∫_Γ F(s) A(s) ds ) = ∫_Γ F(s) · Wres_BC^{top}(A(s)) ds
```

für A(s) = (s − D_X^{BC})^{-2} · L₃°.

### 4.2 Hinreichende Bedingung

Das gilt, wenn:

(a) s ↦ A(s) stetig (als B₃-wertige Abbildung) auf Γ,

(b) Wres_BC^{top} stetig als lineares Funktional auf B₃ (das ist OP-4.1a).

Unter (a) und (b) ist das Bochner-Integral mit stetigen Funktionalen
vertauschbar (Standard-Satz über Bochner-Integration, vgl. Diestel-Uhl §II.2).

### 4.3 Status

(b) ist OP-4.1a — aktuell ⚠ [M] (NEU-18, offen).

(a) hängt von der Stetigkeit von s ↦ (s − D_X^{BC})^{-2} auf Γ ab,
was aus der Resolventen-Analytizität von D_X^{BC} folgt — gesichert,
sobald D_X^{BC} normal ist und Γ das Spektrum nicht trifft.

**Marker:** ⚠ [M] (abhängig von OP-4.1a)

---

## 5. Globale Spurformel: Übergang zu allen Nullstellen

### 5.1 Das Problem

Theorem X.2.3 (lokal) gilt für feste Kontur Γ mit endlich vielen
Nullstellen in int(Γ). Die volle Spurformel

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃° ) = Σ_{alle ρ} m_ρ · f(ρ)
```

erfordert, dass die Summe über alle (unendlich vielen) Nullstellen konvergiert.

### 5.2 Testklasse A_ξ

Definiere die **Testklasse**:

```
A_ξ := { f : ℂ → ℂ holomorph : Σ_ρ m_ρ |f(ρ)| < ∞ }.
```

Für f ∈ A_ξ konvergiert die globale Nullstellensumme absolut.

**Beispiele:**

- f(s) = s^{-k} für k groß genug (da Nullstellen ρ mit |ρ| → ∞).
- f(s) = e^{-t|s|²} für t > 0 (Gauß-Typ).
- f(s) holomorph mit schnellem Abfall auf der kritischen Geraden.

### 5.3 Globale Aussage ⚠ [M]

Für f ∈ A_ξ gilt (formal durch Grenzübergang Γ_N → Γ_∞):

```
Tr_Wres^{top}( f(D_X^{BC}) · L₃° ) = Σ_{alle ρ} m_ρ · f(ρ).
```

Der Grenzübergang erfordert Kontrolle der Konvergenz von
∫_{Γ_N} F(s) K_ξ(s) ds für wachsende Konturen Γ_N.

Aus der bekannten Nullstellendichte von ζ (N(T) ~ T/(2π) log(T/2π)):

```
Σ_{|Im(ρ)|≤T} m_ρ |f(ρ)|  →  konvergiert für f ∈ A_ξ.
```

**Marker:** ⚠ [M]

---

## 6. RH-Anschluss

### 6.1 Was die Spurformel über RH sagt

Die Spurformel selbst ist **RH-neutral** — sie gilt für alle Nullstellen ρ,
unabhängig davon ob Re(ρ) = ½ oder nicht.

RH tritt ein bei der **Selbstadjungiertheitsfrage** (NEU-26 §8):

```
RH  ⟺  D_X^{BC} − ½·I  ist schief-selbstadjungiert bzgl. Wres_BC^{top}.
```

Die Spurformel ist die notwendige Voraussetzung dafür, dass diese
Frage überhaupt sinnvoll gestellt werden kann.

### 6.2 Gesamtkette X.2

```
NEU-26: Architektur, Kernbehauptung, RH-Operatorbild
NEU-27: R_X(s) nicht-tautologisch definiert via KMS
NEU-28: λ_mod(s) = C_L/ζ(s) → R_X^ξ = C_L·K_ξ  ✓ [M]
NEU-29: Cauchy-Spurformel (lokal ✓ [M], global ⚠ [M])
──────────────────────────────────────────────────────
X.2 strukturell vollständig.
Offener Kernpunkt: BC-intrinsisches D_X^{BC}.  ❓ [O]
```

---

## 7. Epistemologische Bilanz

| Baustein | Status |
|----------|--------|
| Doppelresolvent-Cauchy-Kalkül f(D) = (2πi)^{-1}∫F(s)(s−D)^{-2}ds | ✓ [M] |
| Primitive Testfunktion F' = f | ✓ [M] |
| Lokale Residuenformel Σ_{int(Γ)} m_ρ f(ρ) | ✓ [M] relativ zu NEU-28 |
| Normierung L₃° = C_L^{-1}·L₃ | ✓ [M] |
| Wres-Konturvertauschung | ⚠ [M] abhängig von OP-4.1a |
| Globale Summe über alle Nullstellen (Testklasse A_ξ) | ⚠ [M] |
| BC-intrinsisches D_X^{BC} | ❓ [O] |

---

## 8. Nächster Schritt: X.3

Mit NEU-29 ist X.2 (Spurformel-Architektur) strukturell abgeschlossen.

**X.3** ist der Selbstadjungiertheitssatz:

```
Zeige: D_X^{BC} − ½·I  ist schief-selbstadjungiert bzgl. Wres_BC^{top}.
⟺ RH.
```

Das erfordert zunächst die explizite BC-intrinsische Konstruktion von
D_X^{BC} — der verbleibende ❓ [O]-Punkt.

---

*Datei: `werkzeuge/neu29_x2_3_cauchy_spurformel.md` | 28. Juni 2026*
*Kernresultat: Tr_Wres^{top}(f(D_X^{BC})·L₃°) = Σ_ρ m_ρ·f(ρ)  (lokal ✓ [M])*
*Nächster Schritt: X.3 — Selbstadjungiertheit von D_X^{BC} − ½·I ↔ RH*
