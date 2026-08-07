# NEU-250g — Modulare Halbgewichtung und primitiver Weilfaktor

> Datum: 07. August 2026 | Status: ⚠ [M] — Konstruktionsvorschlag mit expliziten Typchecks; kein abschließender Beweis
> Vorgänger: NEU-250f (`P_{m=1}T_p^raw = 0` wegen `L_3^∘ ∈ F^3`)
> Quellenbasis: NEU-015 (`op4_frobenius`)

---

## 0. Ausgangslage

NEU-250f hat den alten `L_3`-Kopplungspfad für den primitiven `m=1`-Sektor endgültig
geschlossen: `L_3^∘ ∈ F^3 ⟹ ℓ_{s,1} = 0 ⟹ P_{m=1}T_p^raw = 0`. Das ist kein Rückschlag,
sondern eine Filtrationsaussage: der `m=1`-Weilterm ist aus `F^3` prinzipiell nicht
erreichbar.

Parallel dazu steht aus NEU-250c–f ein eigenständiges positives primitives Objekt in
`F^1 \ F^2`:

```
h_p^(1)(E_R, E_R') = (1/p) δ_{R,R'}
```

NEU-250g fragt: **Kann aus bereits vorhandenen Grad-1-Objekten (NEU-015) eine
kanonische, gradkompatible Kopplungsquelle in `H_rel,p^(1)` konstruiert werden, die
den primitiven Weilfaktor `log(p)/√p` reproduziert — ohne Rückwärtsdefinition?**

---

## 1. Schichttrennung (verbindlich nach NEU-249-Disziplin)

### 1.1 Quellenbefund (aus NEU-015, wörtlich)

```
ε_β(F) = Σ_{m∈N×} m^{-β} F_{m,m,0}                    (β > 1)      [NEU-015 §3.1]
σ_t(V_p) = p^{it} V_p                                                [BC-Standard, extern]
ν_β := σ_{iβ}  (Nakayama-Automorphismus)                              [NEU-015 §5.3]
β_ε(F,G) := ε_β(F*G)                                                 [NEU-015 §3.3]
KMS-Symmetrie: β_ε(F,G) = β_ε(σ_{iβ}(G), F)                          [NEU-015 §5.2]
```

**Wichtige Sperrklausel (aus NEU-015 selbst übernommen):** `ε_β` ist ausschließlich für
`β > 1` als konvergente Dirichletreihe definiert. Insbesondere ist `ε_{β/2}` nur für
`β > 2` definiert. Bei Residuenpunkt `β = 1` ist `ε_{1/2}` **nicht** durch NEU-015
garantiert. Diese Warnung ist für die gesamte Konstruktion unten bindend: es wird
durchgehend nur `ε_β` selbst verwendet, niemals `ε_{β/2}`.

### 1.2 Neue Konstruktion (Desiderat dieses Knotens, kein Quellenbefund)

Alles Folgende — `ν_β^{-1/2}`, `β_β^bal`, `H_BC`, `H_BC^{1/2}`, `h_p^bal` — ist
**Konstruktion**, nicht in NEU-015 enthalten. NEU-015 beweist nur die modulare
Frobenius-Struktur auf `A_2D^r` und weist ausdrücklich darauf hin, dass die
vollständige topologische Nicht-Ausgeartetheit offen bleibt [NEU-015 §10, R1]. Jede
Aussage über Selbstadjungiertheit oder funktionalen Kalkül von `H_BC` unten ist
**algebraisch auf dem Eigenvektorraum**, nicht als Hilbertraum-Resultat zu lesen.

---

## 2. Konstruktionsschritte

### Schritt 1 — Nakayama-Eigenwert (Vorzeichen fixiert)

Aus `σ_t(j_R) = e^{it log p} j_R` folgt bei analytischer Fortsetzung `t → iβ`:

```
ν_β(j_R) = σ_{iβ}(j_R) = p^{-β} j_R
```

Damit liefert die **linke** Gramform (Argument im ersten Slot fest, zweites Argument
unverdreht):

```
ε_β(j_R^* j_R') = δ_{R,R'} p^{-β} ζ(β)
```

und die **rechte** Gramform (Rollen vertauscht):

```
ε_β(j_R' j_R^*) = δ_{R,R'} ζ(β)
```

Die beiden Randgewichte sind `p^{-β}` und `1`; ihr geometrischer Mittelpunkt bei
`β = 1` ist `p^{-1/2}` — das ist die Zielgröße, die als *kanonisch erreichbar*
geprüft werden soll.

### Schritt 2 — Inverse Halbmodularisierung

Um von der linken Form (`p^{-β}`) zum Mittelpunkt (`p^{-β/2}`) zu gelangen, braucht man
nicht `ν_β^{1/2}`, sondern die **inverse** Halbwurzel, angewandt auf das zweite
Argument:

```
ν_β^{-1/2}(j_R) := p^{β/2} j_R
```

(Dies ist algebraisch wohldefiniert als formale Fortsetzung von `σ_t` auf `t = -iβ/2`;
kein Rückgriff auf `ε_{β/2}`.)

### Schritt 3 — Balancierte Frobeniusform (nur `ε_β`, nicht `ε_{β/2}`)

```
β_β^bal(j_R, j_R') := ε_β( j_R^* ν_β^{-1/2}(j_R') )
                     = p^{β/2} · ε_β(j_R^* j_R')
                     = p^{β/2} · δ_{R,R'} p^{-β} ζ(β)
                     = δ_{R,R'} p^{-β/2} ζ(β)
```

Diese Form ist für **alle** `β > 1` wohldefiniert, da sie nur `ε_β` (nicht `ε_{β/2}`)
verwendet und `ν_β^{-1/2}` rein algebraisch auf dem Eigenvektor wirkt. Die
Sperrklausel aus §1.1 ist damit eingehalten.

### Schritt 4 — Residuum bei `β = 1`

`ζ(β)` hat bei `β = 1` einen einfachen Pol mit Residuum 1. Nach Herausdividieren des
Pols (Standard-Regularisierung, wie in den vorherigen NEU-250-Knoten praktiziert):

```
Res_{β=1} β_β^bal(j_R, j_R') = p^{-1/2} δ_{R,R'}
```

Definition (balancierte Residuenform):

```
h_p^bal(E_R, E_R') := p^{-1/2} δ_{R,R'}
```

### Schritt 5 — Algebraischer BC-Energiemultiplikator

Aus `σ_t(j_R) = e^{it log p} j_R` liest man auf dem algebraischen Eigenvektorraum
den Generator ab:

```
H_BC j_R := (log p) j_R
```

**Firewall D2/technische Warnung:** Dies ist eine Definition auf dem
Eigenvektor-Erzeugendensystem, keine Aussage über einen selbstadjungierten Operator
mit Definitionsbereich, Abschluss und funktionalem Kalkül auf einem vollständigen
Hilbertraum. Diese Lücke ist ein offener Folgeknoten (siehe §5).

### Schritt 6 — Halbenergie

Algebraisch, punktweise auf dem Eigenvektor:

```
H_BC^{1/2} j_R := √(log p) j_R
```

### Schritt 7 — Primitive Weilidentität

```
h_p^bal( H_BC^{1/2} E_R, H_BC^{1/2} E_R' )
    = √(log p) · √(log p) · h_p^bal(E_R, E_R')
    = log(p) · p^{-1/2} δ_{R,R'}
    = (log p / √p) δ_{R,R'}
```

**Ergebnis:**

```
h_p^bal( H_BC^{1/2} E_R, H_BC^{1/2} E_R' ) = (log p / √p) δ_{R,R'}
```

Das ist exakt der primitive `m=1`-Weilfaktor.

---

## 3. Firewall-Protokoll D1–D4

| Firewall | Prüfung | Status |
|---|---|---|
| D1 (Gradkompatibilität) | `j_R = e_R V_p ∈ F^1 \ F^2`; kein Element aus `F^3` importiert | ✓ [M] |
| D2 (Arithmetische Kanonizität) | `ν_β^{-1/2}` folgt aus `σ_t`, nicht aus Weil-Zielform; `H_BC` folgt aus BC-Zeitentwicklung, nicht aus Rückwärtsvergleich | ✓ [M] |
| D3 (Explizite Formel) | Jede Basiswirkung (Schritte 1–6) ist auf `j_R`/`E_R` konkret ausgerechnet | ✓ [M] |
| D4 (Weil-Kompatibilität) | Vergleich in Schritt 7 ergibt exakt `log(p)/√p`, ohne Koeffizienten frei zu wählen | ✓ [M] |

**Zusätzliche Firewall (neu, verbindlich):** Diese Rechnung reproduziert ausschließlich
den arithmetischen Gewichtsfaktor `log(p)/√p`. Sie reproduziert **nicht** automatisch
den vollständigen Primterm der expliziten Formel

```
Σ_{m≥1} (log p / p^{m/2}) g(m log p)
```

insbesondere nicht den Testfunktionswert `g(log p)`. Die Einbettung von `g` in eine
positive Quadratform bzw. Quellenabbildung ist ein **eigener, nachfolgender Knoten**
und darf mit diesem Ergebnis nicht zusammengezogen werden.

---

## 4. Hauptresultat NEU-250g

```
Quelleninduzierte Faktorisierung des primitiven Weilgewichts:

    log(p)/√p  =  p^{-1/2}          ·  log(p)
                  ⌞  KMS/Nakayama-  ⌟   ⌞ BC-Energie ⌟
                     Balance (ν_β^{-1/2}, ε_β)    (H_BC)

Beide Faktoren stammen aus bereits in NEU-015 vorhandenen Objekten
(σ_t, ν_β = σ_{iβ}, ε_β), kombiniert durch neu konstruierte, aber
gradkompatible Operationen (ν_β^{-1/2}, H_BC^{1/2}).

Kein Koeffizient wurde durch Rückwärtsvergleich mit der Weilform gewählt.
```

Status: ⚠ [M] — algebraisch vollständig durchgerechnet; Hilbertraum-Fundierung von
`H_BC` (Selbstadjungiertheit, Definitionsbereich, Abschluss) offen.

---

## 5. Offene Restfragen

| Frage | Status |
|---|---|
| NEU-250g/R1: Ist `ν_β^{-1/2} = σ_{-iβ/2}` als Automorphismus auf `A_2D^r` (nicht nur auf dem Eigenvektor) wohldefiniert? | ❓ [O] |
| NEU-250g/R2: Selbstadjungiertheit und Definitionsbereich von `H_BC` auf einer konkreten Hilbertdarstellung | ❓ [O] |
| NEU-250g/R3: Symmetrischere Viertelschritt-Variante der balancierten Form — separat auf `*`-Verträglichkeit zu prüfen | ❓ [O] |
| NEU-250g/R4: Einbettung des Testfunktionswerts `g(log p)` in die positive Quadratform (eigener Folgeknoten, nicht mit R1–R3 zu vermischen) | ❓ [O] |
| NEU-250g/R5: Verhalten für `m > 1` — systematischer Übergang nach Abschluss von R1–R4 | ❓ [O] |

---

## 6. Zusammenfassung

```
NEU-250g Hauptresultat:

h_p^bal(E_R, E_R') = p^{-1/2} δ_{R,R'}        (Residuum von ε_β(j_R^* ν_β^{-1/2} j_R') bei β=1)
H_BC j_R = (log p) j_R                         (algebraischer BC-Energiemultiplikator)

⟹ h_p^bal(H_BC^{1/2}E_R, H_BC^{1/2}E_R') = (log p/√p) δ_{R,R'}

Beide Faktoren quellenkanonisch, kein Rückwärtsimport aus der Weilform.
Vollständige Formel (mit g(log p)) bleibt eigener Folgeknoten.
```

---

*Datei: `01-primkanten-werkzeuge/NEU-250g_Modulare_Halbgewichtung_und_primitiver_Weilfaktor.md` | Erstellt: 07. August 2026 | NEU-250g*
