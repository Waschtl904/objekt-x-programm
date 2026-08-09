# P09 / Gruppe I1 — BC/Hochschild-Grundblock: Pass-A-Reconciliation

**Datum:** 9. August 2026  
**SYN-Ziel:** P09 — BC + Hochschild  
**Paket:** I1  
**Quellbereich:** `06-hochschild-bc-algebra/`, NEU-174–190 (inkl. Doppeldatei NEU-183; NEU-191 fehlt live)  
**Prüfart:** überwiegend `AUDIT-RECONCILED` / `AUDIT-REUSED`; kein blindes Vollneuaudit  
**Status:** `I1 PASS A COMPLETE — Gegencheck ausstehend`

---

## 0. Verbindliche Leserichtung

Dieses Paket wird nicht numerisch-naiv gelesen. Maßgeblich ist die Revisionskette

```text
NEU-174/175 Modellkomplex
→ NEU-176/177 frühe geladene Kandidaten und Dualzyklus-Setup
→ NEU-178 geladene Modellklasse auf S_p
→ NEU-179–183 direkte BC-Konstruktion / Präsentationsaudit
→ NEU-184 regulärer Zentrum-No-go (rev2)
→ NEU-185 neutrale nichttriviale HH^4-Klasse auf A_Q^alg
→ NEU-186–188 geladene HH^1/HH^4-Triage
→ NEU-189/190 Operatorbrücken-Typaudit und globaler Quellenbefund.
```

Spätere korrigierende Knoten haben Vorrang vor Zwischenständen. Insbesondere wird die ältere Datei
`NEU-183_Zentrumstest_Strukturbruch_BC-Algebra.md` beim Zentrumbeweis durch `NEU-184 ... rev2` ersetzt.

---

## 1. Kernbefund I1

Der gültige Endstand trennt vier Ebenen strikt:

1. **Hochschild-Modellarchitektur:** Ein algebraischer BC-Hochschildkomplex und ein endlicher Eigenkochain-/Ladungsprojektor sind konstruiert.
2. **Geladene Modellkohomologie:** Im separaten Vier-Prim-Polynommodell `S_p` existiert eine explizite nichttriviale geladene HH^4-Klasse.
3. **Echte BC-Kohomologie:** Auf `A := A_Q^alg` ist eine explizite **neutrale** nichttriviale Klasse `[Ω_p] ∈ HH^4(A,A)` bewiesen.
4. **Operatorbrücke:** Aus `Z^4(A,A)` oder `HH^4(A,A)` zu einem ausgezeichneten Hilbertraumoperator ist im geprüften Katalog kein typisierter Mechanismus konstruiert. Dies ist ein negativer **Quellenbefund**, kein mathematischer Unmöglichkeitssatz.

Damit ist ausdrücklich **nicht** bewiesen:

```text
HH^4(A_Q^alg,A_Q^alg)_ch ≠ 0,
```

und ebenfalls **nicht** konstruiert:

```text
ρ_op : HH^4(A,A) → O(H).
```

---

## 2. Reconciliation-Matrix

| Knoten | Prüfart | Endstatus für P09 | Heute gültiger Kernbefund |
|---|---|---|---|
| NEU-174 | `AUDIT-RECONCILED` | `INCORPORATED_part` | `B_3^mod := A_Q` ist eine Modellwahl. Standard-Hochschildkomplex `(C^•,b)` und induzierte Zeitwirkung sind konstruktiv; keine Identifikation mit einem historisch gemeinten `B_3`/`L_3`, keine Operatorrealisierung. |
| NEU-175 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Sauber ist der algebraische Eigenkochainkomplex `C_fin^•`; `P^ch` ist dort ein Kettenprojektor und induziert `[P^ch]` auf Kohomologie. Keine Vollständigkeit `C_fin^•=C^•`, kein Hilbertraumprojektor. |
| NEU-176 | `AUDIT-REUSED` (Direktaudit 19.07.) | `SUPERSEDED_part / AUDIT-ONLY` | Produktschablone für `L_{3,λ}` war nicht vollständig typisiert; Zielmodul, explizite Eigenfunktionale, Kozykel- und Nichtrandnachweis fehlten. Nicht als bewiesene geladene Klasse auf `A_Q` migrieren. |
| NEU-177 | `AUDIT-RECONCILED` via NEU-178 | `INCORPORATED_part` | Allgemeine duale Ketten-/Paarungsgrammatik und Adjungiertheit `⟨bψ,z⟩=⟨ψ,∂z⟩` sind brauchbar; objektspezifische Schließung erfolgt erst im Modell `S_p`. |
| NEU-178 | `AUDIT-REUSED` | `INCORPORATED_model` | Explizite nichttriviale geladene Klasse `[L_ν]∈HH^4(S_p,S_p)` mit Dualzyklus und Paarung `24`. **Strikte Reichweite:** `S_p` ist separates Polynommodell; kein automatischer Transfer zu `A_Q`. |
| NEU-179 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Naiver Hochschild-Transfer über Inklusion/Retraktion ist nicht automatisch funktoriell. Richtige Weiterarbeit: direkte BC-Gradierung, Primderivationen und Koeffizientenfaktor. |
| NEU-180 | `AUDIT-RECONCILED` | `SUPERSEDED_part → NEU-183` | `Γ=Q_+^×`, Gradzuweisung und Primvaluationsderivationen sind der richtige Mechanismus, zunächst konditional auf Homogenität der Präsentation. Diese Voraussetzung wird in NEU-183 geschlossen. |
| NEU-181 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Algebraischer Modular-Twist und Cup-Typisierung sind nach Gradierungsabschluss gültig. Existenz geladener regulärer/verdrehter Nullkozykel war hier noch offen; beide einfachen Faktorisierungsrouten werden später negativ geschlossen. |
| NEU-182 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Verdrehter Nullkozykel-No-go für `Re β>0` zunächst konditional auf BC-`C*`-Einbettung/Isometrierelation; neutraler Vierkozykel `Ω_p` konstruktiv vorbereitet. NEU-183 schließt die Voraussetzungen. |
| NEU-183 — Quellen/Präsentation | `AUDIT-REUSED` | `INCORPORATED` | BC-Relationen, Homogenität des Ideals, `μ_n^*μ_n=1`, treue `C*`-Einbettung, Normalform und damit unbedingter verdrehter Nullkozykel-No-go (`Re β>0`). |
| NEU-183 — Zentrum/Strukturbruch | `AUDIT-RECONCILED` | `SUPERSEDED_part / AUDIT-ONLY` | Konzeptueller Strukturbruch `S_p` vs. BC bleibt nützlich. Der dortige Zentrumbeweis und schwankende Alt-Normierung werden **nicht** migriert; Zentrumbeweis durch NEU-184 rev2 ersetzt, unnormalisierte Alt-Konvention durch NEU-185/Endstand fixiert. |
| NEU-184 rev2 | `AUDIT-REUSED` | `INCORPORATED` | `Z(A_Q^alg)_g=0` für `g≠1` über Normalform + endlichen Träger + Surjektivität von `s↦(m-n)s` auf `Q/Z`. Reguläre geladene Nullkozykelroute `✓[M]_neg`. |
| NEU-185 | `AUDIT-REUSED` | `INCORPORATED` | Augmentationscharakter und Dualzyklus liefern `⟨Ω_p,z_p^ε⟩=24` und damit `[Ω_p]≠0` in `HH^4(A_Q^alg,A_Q^alg)`. **Grad:** `deg_Γ Ω_p=1_Γ` (neutral), nicht geladener Sektor. |
| NEU-186 | `AUDIT-REUSED` | `INCORPORATED_part` | Geladener `HH^4`-Sektor bleibt offen. Innere geladene Derivationen liefern nur Koränder; Ansatz `u_g D_p` bzw. `D_p u_g` scheitert für `g≠1`. Andere `HH^1/HH^2/HH^3`-/Direktrouten bleiben offen. |
| NEU-187 | `AUDIT-REUSED` | `INCORPORATED_part → I2` | Restriktion `HH^1(A,A)_g→HH^1(B,A)_g` ist injektiv; Gruppenalgebra-Kohomologie auf der punktierten Fourierseite ist nichttrivial. Erweiterung auf die volle BC-Algebra bleibt offen. |
| NEU-188 | `AUDIT-RECONCILED` | `INCORPORATED_part → I2/I6` | Vollständige BC-Erweiterung eines punktierten Potentials ist **nicht** bewiesen. `α_k(H)-H∈B`, nicht-teilerfremde Transferbedingungen und restliche differenzierte Relationen sind offen. Erfolgreiche Erweiterung wäre automatisch äußerlich (`✓[M]` konditional). |
| NEU-189 | `AUDIT-REUSED` | `INCORPORATED` | Exakte Typblockade: `Ω_p` ist vierlinear `A`-wertig, kein einzelner Hilbertraumoperator. Kein Schluss `[Ω_p]≠0 ⇒ ρ_op([Ω_p])≠0`. Kein struktureller No-go. |
| NEU-190 | `AUDIT-REUSED` | `INCORPORATED` | Globaler Katalogbefund NEU-1–188: keine konstruierte Abbildung `Z^4(A,A)` oder `HH^4(A,A)→O(H)`. Status `✓[M]_neg,Quelle`, ausdrücklich kein mathematischer Unmöglichkeitssatz. |

---

## 3. Verbindliche I1-Firewalls für P09

1. **Modell ≠ BC-Algebra.** `[L_ν]∈HH^4(S_p,S_p)_ch` darf nicht als geladene BC-Klasse ausgegeben werden.
2. **Neutral ≠ geladen.** `[Ω_p]≠0` beweist `HH^4(A,A)≠0`, aber nicht `HH^4(A,A)_ch≠0`.
3. **P^ch ist algebraischer Kettenprojektor.** Keine Aussage über orthogonale Hilbertraumprojektionen oder Vollständigkeit des gesamten Kochainraums.
4. **Zwei Nullkozykel-No-Gos getrennt halten:**
   - verdreht `Re β>0`: `Z^0(A, _id A_{σ_β})={0}`;
   - regulär geladen: `Z(A)_g=0` für `g≠1`.
   Keines davon beweist das Verschwinden des gesamten geladenen `HH^4`.
5. **NEU-183-Doppeldatei:** Der ältere Zentrumbeweis ist `SUPERSEDED` durch NEU-184 rev2; nicht beide Beweise parallel migrieren.
6. **Alt-Normierung:** Für `Ω_p` gilt im kanonischen I1-Endstand die **unnormalisierte Alternierung**; daher Paarungswert `24`. Frühere `1/4!`-Zwischenformulierungen sind redaktionell überholt.
7. **Punktierte Gruppenkozykel ≠ BC-Derivationen.** NEU-187 beweist nicht `HH^1(A,A)_g≠0`; die Erweiterung ist der eigentliche offene Schritt.
8. **Operatorquellen-No-go ≠ mathematischer No-go.** NEU-190 sagt nur, dass der Mechanismus im geprüften Katalog nicht konstruiert war.
9. **Keine Abkürzung zu Objekt X.** Eine Hochschildklasse liefert ohne zusätzliche Realisierungs-/Paarungsstruktur weder `L_3^∘`, `C_p` noch einen Hilbert–Pólya-Operator.

---

## 4. P09 vs. P10-Routing aus I1

Folgende Negativresultate bleiben **inhaltlich in P09**, weil sie die BC/Hochschild-Architektur definieren:

- verdrehter Nullkozykel-No-go (`Re β>0`),
- regulärer geladener Zentrum-No-go,
- No-go für die spezielle Ableitungsform `u_gD_p`/`D_pu_g`,
- Quellen-No-go der fehlenden Operatorbrücke.

P10 darf sie später als **kondensierte No-Go-Sammlung spiegeln**, aber P09 benötigt sie zur Erklärung der verbleibenden Suchräume. Die vom Gegencheck markierte Entscheidung für die singuläre Potentialroute wird **nicht hier vorweggenommen**: I2 + I6 müssen erst NEU-192–211 gegen NEU-222 reconciliieren; danach wird entschieden, welche dortigen Kandidaten nur P10-Archiv und welche P09-Strukturfirewalls sind.

---

## 5. Belastbarer I1-SYN-Kern

P09 darf aus I1 später im Wesentlichen folgende mathematische Aussagen übernehmen:

### 5.1 Algebraischer BC-Hochschildrahmen

```text
A := A_Q^alg,
Γ := Q_+^×,
A = ⊕_{g∈Γ} A_g,
D_p|_{A_g} = v_p(g) id,
```

mit algebraischer BC-Zeitwirkung und endlichem Eigenkochainkomplex `C_fin^•`.

### 5.2 Zwei einfache geladene Nullkozykelrouten sind geschlossen

```text
Re β>0 ⇒ Z^0(A, _id A_{σ_β})={0},
Z(A)_g={0} for g≠1.
```

### 5.3 Neutrale Vierklasse

Für vier verschiedene Primzahlen:

```text
Ω_p := Σ_{π∈S4} sgn(π)
       D_{p_{π(1)}}⌣D_{p_{π(2)}}⌣D_{p_{π(3)}}⌣D_{p_{π(4)}} ∈ Z^4(A,A),
```

und mit dem Augmentations-Dualzyklus:

```text
⟨Ω_p,z_p^ε⟩=24,
[Ω_p]≠0 in HH^4(A,A).
```

Diese Klasse ist neutral: `deg_Γ Ω_p=1_Γ`.

### 5.4 Offener geladener Sektor

```text
HH^4(A,A)_ch ≠ 0 ?
```

bleibt nach I1 offen und wird über I2/I3 weiterverfolgt.

### 5.5 Operatorbrücke

```text
Z^4(A,A) / HH^4(A,A) → O(H)
```

ist im geprüften Quellenbestand nicht konstruiert; kein struktureller Ausschluss.

---

## 6. Gegencheck-Fragen für I1

Ein unabhängiger Gegencheck soll ausschließlich folgende Punkte prüfen:

1. **Neutralitätsfrage:** Wird irgendwo in NEU-174–190 nach NEU-185 tatsächlich `HH^4(A,A)_ch≠0` bewiesen, oder bleibt `[Ω_p]` neutral?
2. **NEU-183-Doppeldatei:** Ist NEU-184 rev2 tatsächlich der spätere/saubere Zentrum-Endanker gegenüber dem älteren `NEU-183_Zentrumstest_Strukturbruch...`?
3. **Operatorbrücke:** Behauptet NEU-190 einen mathematischen Unmöglichkeitssatz oder nur `✓[M]_neg,Quelle`?
4. **HH^1-Route:** Beweist NEU-187/188 bereits eine geladene äußere Derivation auf der vollen BC-Algebra, oder nur nichttriviale punktierte Gruppenkozykel plus offene Erweiterung?
5. **Alt-Konvention:** Ist für den in NEU-185 verwendeten Endstand die unnormalisierte Alternierung mit Paarungswert `24` verbindlich?

Nur ein konkreter Gegenbefund zu diesen fünf Punkten öffnet I1 erneut.

---

## 7. Endstatus

\[
\boxed{\text{P09 / I1 PASS A COMPLETE — Gegencheck ausstehend}}
\]

**Nächster aktiver Block nach Gegencheck:** I2 — NEU-192–211, mit verbindlichem späteren Superseding-Scan durch I6/NEU-222.
