# Typaudit NEU-16a/b und NEU-17 — ∂Φ₃=L₃ nicht typologisch geschlossen

> Datum: 17. Juli 2026 | Status: ❓ [O] — diagnostischer Auditcommit
> Grundlage: Direktaudit NEU-16a (`neu16_op3_1_monoidladung.md`),
>            NEU-16b (`neu16_op3_modular_spur.md`), NEU-17 (`neu17_op3_1_2_aequivarianter_lift.md`)

---

## Kernbefund

Der Direktaudit von NEU-16a, NEU-16b und NEU-17 liefert keine typkorrekte Auflösung der
Gleichung

```
∂Φ₃ = L₃
```

gegen die downstream behauptete Nichttrivialität

```
[L₃] ≠ 0  ∈  HH⁴(F³ A_BC^{an}).
```

NEU-16a bezeichnet das Hochschild-Differential mit δ, während NEU-16b und NEU-17 das Symbol ∂
sowohl auf Kochains als auch auf Klassen anwenden. NEU-17 nennt ∂ ausdrücklich „Hochschild-Rand".
Falls Φ₃ und L₃ im selben Hochschild-Komplex liegen und ∂ = b gilt, folgt jedoch unmittelbar:

```
[L₃] = [bΦ₃] = 0.
```

---

## Protokoll A — Algebrastruktur von F³ A_BC^{an}

Das grundlegendste Problem liegt noch vor der Gleichung ∂Φ₃ = L₃.

Wenn A = F³ A_BC^{an} gesetzt und anschließend C^k(A, A) als Hochschild-Komplex verwendet wird,
muss F³ A_BC^{an} überhaupt eine Algebra sein:

```
(F³A)(F³A) ⊆ F³A.
```

Bei einer üblichen multiplikativen Filtration gilt

```
F^p A · F^q A ⊆ F^{p+q} A,
```

also insbesondere F³A · F³A ⊆ F⁶A ⊆ F³A nur dann, wenn die Filtration absteigend ist.
Ist sie aufsteigend, ist die Unteralgebraeigenschaft nicht automatisch gegeben.

**In keiner der drei Dateien wird nachgewiesen, dass F³ A_BC^{an} eine Algebra ist.**
Damit ist bereits HH⁴(F³ A_BC^{an}) möglicherweise nicht wohldefiniert.

---

## Protokoll B — Notationskonflikt δ / ∂

| Datei    | Symbol | Anwendungskontext           | Benennung im Text    |
|----------|--------|-----------------------------|----------------------|
| NEU-16a  | δ      | Kochains C^k(A,A)           | nicht explizit       |
| NEU-16b  | ∂      | Klassen [Φ₃], [L₃]          | nicht explizit       |
| NEU-17   | ∂      | Kochains und Klassen gemischt | „Hochschild-Rand" |

Die Symbole δ und ∂ werden in den drei Blättern nicht konsistent verwendet.

---

## Protokoll C — ∂ auf Klassen: undefiniert, nicht unmöglich

Die Formel [L₃] = ∂([Φ₃]) ist nicht allein deshalb unmöglich, weil beide Argumente Klassen sind.
∂ könnte theoretisch sein:

- ein verbindender Homomorphismus einer langen exakten Sequenz,
- ein Spektralsequenzdifferential,
- eine Massey- oder Obstruktionsabbildung,
- eine Randabbildung zwischen Kohomologien verschiedener Komplexe.

Das präzise Problem lautet:

> **Keine solche induzierte oder verbindende Abbildung ∂ wird definiert.**

Gleichzeitig nennt NEU-17 dasselbe Symbol „Hochschild-Rand". Damit entsteht nicht nur ein
Typfehler, sondern eine Mehrdeutigkeit zwischen zwei mathematisch verschiedenen Abbildungen.

---

## Protokoll D — Filtration F³/F⁴ und Symbol-Lift

Eine mögliche Auflösung durch Exaktheit nur im assoziierten Graduierten (F³/F⁴) ist nicht
belegt. Der Quotient F³/F⁴ erscheint lediglich als Ziel der Symbolprojektion R₃:

```
R₃: F³ A_BC^{an} → F³/F⁴ A_BC^{an},
```

nicht als Komplex der Gleichung ∂Φ₃ = L₃.

Ebenso wird kein größerer Symbolkomplex definiert, in dem Φ₃ zulässig, aber im analytischen
Hochschild-Komplex unzulässig wäre. Der Ausdruck „Symbol-Lift" bleibt ohne Inklusions- oder
Quotientendiagramm informell.

---

## Protokoll E — Modular verdrehter Koeffizientenkomplex

NEU-16b nennt als natürliche Heimat der modularen Auswertung den verdrehten Koeffizientenkomplex

```
HH⁴(F³ A_BC^{an}, (F³ A_BC^{an})^{σ_{iβ}}),
```

der grundsätzlich nicht dasselbe ist wie HH⁴(F³ A_BC^{an}, F³ A_BC^{an}).

Ungeklärt ist, wo genau jede der folgenden Größen lebt:

```
L₃,    [L₃],    ε_β,    λ_β^{mod} ∘ R₃(L₃).
```

Es könnte sein, dass L₃ eine unverdrillte Kochain ist, während erst ihre modulare Auswertung
einen verdrehten Kozyklus liefert. Es könnte aber auch sein, dass NEU-16b den
Koeffizientenmodul der Klasse selbst korrigiert. Beides ist derzeit nicht auseinandergehalten.

---

## Fallentscheidung

| Fall | Beschreibung | Status |
|------|-------------|--------|
| T1 | gleicher Hochschild-Komplex, ∂ = b | textuell naheliegend; führt zu [L₃] = 0 |
| T2 | Gleichung nur in F³/F⁴ oder gr³ | nicht belegt |
| T3 | Φ₃ nur im größeren Symbolkomplex | nicht belegt |
| T4 | ∂ ≠ b, anderes Differential | durch „Hochschild-Rand" disfavorisiert, wegen Anwendung auf Klassen nicht ausgeschlossen |
| T5 | ∂ ist verbindende Abbildung auf Klassen | denkbar, aber vollständig undefiniert |
| T6 | Wechsel zu verdrehten Koeffizienten löst Widerspruch | denkbar, aber keine Vergleichsabbildung angegeben |

**Bewiesen:** Die Blätter NEU-16a/b und NEU-17 enthalten keine typkorrekte Konstruktion,
die L₃ = ∂Φ₃ mit [L₃] ≠ 0 vereinbar macht.

---

## Offene Punkte

```
[O-170c-2a]: Algebrastruktur von F³ A_BC^{an} sowie Typ von δ/∂
[O-170c-2b]: ∂Φ₃ = L₃  versus  [L₃] ≠ 0
[O-170c-2c]: Grad k=4 und vollständige Basiswirkung von L₃
[O-170c-2d]: C⁴(A,A) → B₃ beziehungsweise Operatorrealisierung
[O-170c-2e]: C'_{4,1} ≠ 0  ⟹  C_L ≠ 0
[O-170c-2f]: unverdrehter versus modular verdrehter Koeffizientenkomplex
```

Alle Punkte [O-170c-2a] bis [O-170c-2f]: ❓ [O]

---

## Nicht-legitime Commitentscheidungen (Stand dieses Audits)

Noch nicht legitim:

```
[O-170c-2] ✓[M]
[O-170c-3] ✓[M]
C_L ≠ 0    ✓[M]
```

oder die Aussage, der operatorielle Weg (F.1) oder der kohomologische Weg (F.2) seien eröffnet.

- Weg F.1 (operatoriell): nicht eröffnet.
- Weg F.2 (kohomologisch): durch die Kette NEU-16–20 nicht validiert.

---

## Nächster Schritt

Das nächste Quellblatt sollte vor NEU-16 liegen: NEU-15 beziehungsweise das ursprüngliche
R₃-Blatt. Dort müssen die Filtration, die Algebrastruktur von F³A, der Symbolquotient und
die ursprüngliche Bedeutung von L₃ festgelegt worden sein.

---

*Datei: `werkzeuge/audit_170c_typaudit_neu16_neu17.md` | Erstellt: 17. Juli 2026*
*Auditgrundlage: NEU-16a, NEU-16b, NEU-17 — Direktaudit ohne Wertung downstream*
