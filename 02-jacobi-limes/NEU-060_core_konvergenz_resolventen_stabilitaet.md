# NEU-60 — Core-Konvergenz und Resolventen-Stabilität des Jacobi-Limes

**Status:** Offene Kernfrage ❓[O]; Teilresultate ⚠[M]  
**Datum:** 2026-06-29  
**Aufbaut auf:** NEU-59 (Weg-B-Architektur), NEU-58 (Weg A geschlossen)

---

## Zentrales Ziel

NEU-60 muss zeigen, dass die Weyl-/Stieltjes-Funktionen
```
m_{a,b}^(N)(z) := ⟨η_a, (A_N^{Jac,-} - z)^{-1} η_b⟩
```
eine eindeutige Herglotz-Grenze besitzen und dass diese Grenze vom selbstadjungierten
Operator D_rel stammt:
```
m_{a,b}^(N)(z)  →  ⟨η_a, (D_rel - z)^{-1} η_b⟩    (N → ∞, z ∈ ℂ\ℝ).
```

**Wichtig (GPT-Präzisierung):** Punktweise Konvergenz der K_pq-Matrixelemente allein
reicht nicht — Resolventen sind nicht linear in den Matrixelementen.
Zusätzlich braucht man Stabilitätsstruktur.

---

## Satz NEU-60.1 — Core-Konvergenz-Kriterium ⚠[M]

**Voraussetzungen:**

(i)  Gemeinsamer dichter Kern:
```
     D_test ⊂ dom(A_N) ∩ dom(D_rel)  für alle N,  und D_test dicht in H.
```

(ii) Starke Konvergenz auf D_test:
```
     A_N ξ  →  D_rel ξ  (in H-Norm)  für alle ξ ∈ D_test.
```

(iii) Automatische Resolventenschranke (aus Selbstadjungiertheit):
```
     ‖(A_N - z)^{-1}‖ ≤ 1/|Im z|,    ‖(D_rel - z)^{-1}‖ ≤ 1/|Im z|.
```

(iv) Range-/Core-Dichte:
```
     (D_rel - z) D_test  ist dicht in H  für ein (und dann alle) z ∈ ℂ\ℝ.
```

**Schlussfolgerung:** Starke Resolventenkonvergenz ⚠[M]
```
(A_N - z)^{-1} ξ  →  (D_rel - z)^{-1} ξ    für alle ξ ∈ H, z ∈ ℂ\ℝ.
```
Insbesondere konvergieren die Weyl-Funktionen:
```
m_{a,b}^(N)(z)  →  ⟨η_a, (D_rel - z)^{-1} η_b⟩.
```

**Beweis-Strategie:**  
Für η = (D_rel - z) ξ ∈ (D_rel - z) D_test (dicht nach (iv)):
```
(A_N - z)^{-1} η - (D_rel - z)^{-1} η
  = (A_N - z)^{-1} [(D_rel - z) - (A_N - z)] ξ
  = (A_N - z)^{-1} [D_rel ξ - A_N ξ]   → 0  (via (ii) und (iii)).
```
Dann Dichte + Resolventenschranke liefern Konvergenz auf ganz H.
(Kato, *Perturbation Theory*, §VIII.1.5; Reed–Simon I, Thm. VIII.25) □ ⚠[M]

**Literatur:**
- Kato, §VIII.1, Thm. VIII.1.5 (starke Resolventenkonvergenz)
- Reed–Simon Bd. I, Thm. VIII.25 (Konvergenzsatz über Kerne)
- Reed–Simon Bd. II, §X.6 (Jacobi-Operatoren und Tridiagonallimiten)

---

## Schritt 2: Herglotz-Eigenschaft der Grenzfunktion ⚠[M]

Die Funktionen m_{a,b}^(N)(z) sind für a = b Herglotz-Funktionen (Nevanlinna-Pick):
```
Im z > 0  ⇒  Im m_{a,a}^(N)(z) > 0,    m_{a,a}^(N)(z̄) = m_{a,a}^(N)(z)*.
```

Die Familie {m_{a,a}^(N)} ist für jedes N eine holomorphe Funktion auf ℂ\ℝ mit
```
|m_{a,a}^(N)(z)| ≤ ‖η_a‖²/|Im z|.
```

**Kompaktheit (Helly-Satz / Montel):** Die Familie ist auf Kompakta von ℂ\ℝ gleichmäßig
beschränkt und gleichgradig stetig. Nach Montel (holomorph) oder Helly (Maßtheorie)
existiert eine Teilfolge mit lokalem Limes. ⚠[M]

**Eindeutigkeit des Limes:** Wenn Bedingungen (i)–(iv) aus NEU-60.1 erfüllt sind,
ist der Limes eindeutig und gleich ⟨η_a, (D_rel - z)^{-1} η_a⟩. ⚠[M]

Ohne (i)–(iv): Limes-Existenz gesichert, Identifikation mit D_rel offen. ❓[O]

---

## Schritt 3: Nachweis von (i)–(iv) im konkreten Modell ❓[O]

Dies ist der eigentliche offene Kern von NEU-60.

### Kandidat für D_test:
```
D_test = span{ η_{p;m;r,u} : p ≤ P, m ≤ M, |r| ≤ R, |u| ≤ U }
```
für endliche Schranken P, M, R, U. Dichtheit in H_rel^eff: ✓[M] (per Definition).

### Bedingung (ii): A_N ξ → D_rel ξ für ξ ∈ D_test

Für ξ = η_{p;m;r,u} mit m ≤ M, r ≤ R gilt:
```
A_N^{Jac,-} η_{p;m;r,u} = Σ_{b} Θ_{ba}^(N) η_b
```
Der Grenzoperator ist:
```
D_rel η_{p;m;r,u} = lim_{N→∞} (iJ_N^-) η_{p;m;r,u}
```

Konkrete Frage: Stabilisiert sich Θ_{ba}^(N) für feste a, b bei N → ∞? ❓[O]

Falls die Matrixelemente Θ_{ba}^(N) für N > max(m, |r|) stabil sind
(d.h. keine N-Abhängigkeit mehr eintritt), dann ist (ii) erfüllt. ⚠[M]

### Bedingung (iv): (D_rel - z) D_test dicht in H ❓[O]

Dies ist äquivalent zur Forderung, dass D_rel|_{D_test} wesentlich selbstadjungiert ist
(Nelson-Kriterium: wenn D_test ⊂ ker(D_rel* ∓ i)⊥). ⚠[M]

Dies ist bereits aus NEU-57 bekannt: D_rel ist selbstadjungiert auf H_rel^eff mit
Kern D_test (via Nelson-Energieschranke J⁻ ≲ L). ✓[M]

Also ist (iv) **gesichert**, sofern D_test ⊂ dom(D_rel). ✓[M]

---

## Schritt 4: Zyklizitäts-/Totalitätsbedingung für vollständige Spektralrekonstruktion ❓[O]

Für volle RH-Äquivalenz (nicht nur Teilspektrum) braucht man:
```
span{ f(D_rel) ξ : ξ ∈ D_test, f ∈ C_c(ℝ) }  dicht in H.
```

Dies ist eine nicht-triviale Bedingung: Sie verlangt, dass D_test keine D_rel-invariante
echte Unterraumstruktur trägt. Äquivalent: D_rel hat keinen zyklischen Vektor außerhalb
von D_test (Simon, *Spectral Theory and Differential Operators*, §3).

Natürliche Vermutung: Da D_test = span{η_a} über alle Indizes a geht, ist D_test
"arithmetisch total" in dem Sinne, dass alle Primzahlen, alle Teiler und alle Levels
vertreten sind. Formaler Nachweis fehlt. ❓[O]

---

## Zusammenfassung: Offene Schritte für NEU-61+

| Bedingung | Status | Priorität |
|---|---|---|
| (i) D_test dichter gemeinsamer Kern | ✓[M] | — |
| (ii) A_N ξ → D_rel ξ auf D_test | ❓[O] | **hoch** |
| (iii) Resolventenschranke 1/|Im z| | ✓[M] | — |
| (iv) Range-Dichte (D_rel-z) D_test | ✓[M] | — |
| Starke Resolventenkonvergenz (NEU-60.1) | ⚠[M] | **hoch** |
| Herglotz-Limes eindeutig = D_rel | ⚠[M] | **hoch** |
| Zyklizität / Totalität von D_test | ❓[O] | mittel |
| Arithmetische Identifikation Spec(D_rel) | ❓[O] | **Hauptziel** |

---

## Kritischer Pfad NEU-61

Der kleinste nächste Schritt mit maximaler Hebelwirkung:

**Zeige:** Für feste Basisvektoren η_a, η_b mit m_a, m_b ≤ M stabilisieren sich die
Matrixelemente Θ_{ba}^(N) für N > N_0(a,b), und:
```
‖A_N^{Jac,-} η_a - D_rel η_a‖  →  0    (N → ∞).
```

Wenn ja: NEU-60.1 ist vollständig anwendbar, starke Resolventenkonvergenz ist gesichert,
Weg B steht auf solidem Fundament.

Wenn nein (Θ_{ba}^(N) driftet mit N): Dann muss die Trunkierungsstrategie überarbeitet
werden (andere Einbettung H_N → H_rel^eff).

---

## Literatur

- Kato, T.: *Perturbation Theory for Linear Operators*, Springer 1995, §VIII.1, Thm. VIII.1.5
- Reed, M. & Simon, B.: Bd. I, Thm. VIII.25; Bd. II, §X.6
- Simon, B.: *Szegő's Theorem*, AMS 2011, Kap. 2 (Herglotz-Theorie)
- Simon, B.: *Spectral Theory and Differential Operators* (zyklische Vektoren, §3)
- Akhiezer, N.I. & Glazman, I.M.: *Theory of Linear Operators in Hilbert Space*
  (Jacobi-Matrizen und ihre spektrale Theorie)
