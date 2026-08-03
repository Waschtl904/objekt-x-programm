# Archiv: Direktaudit NEU-206

**Datum:** 3. August 2026
**Datei:** `NEU-206_Homogene_Partialisometrieschalen_Orthogonalitaet_und_Charakterkern.md`
**Gesamtstatus:** ✓[M]_part

> Unveränderliches Archivdokument. Aktive Knotenstände in `ZWISCHENBILANZ_2026-08-01.md`.

---

## 1. Auditumfang

Geprüft wurden: NEU-206 vollständig; BC-Relationen aus NEU-183; dyadische Projektions- und Transportgeometrie aus NEU-204; aktuelle Ordnerstruktur zur Bestimmung des nächsten Knotens.

NEU-206 konstruiert für einen festen nichtneutralen Grad g=m/n≠1 homogene Partialisometrieschalen w_j=μ_m q_j μ_n*∈A_g, deren Kommutatoren mit jedem festen Charaktergenerator e(r) ab einer hinreichend hohen Schale verschwinden. Die Normkonvergenz der Kommutatoren mit μ_k, μ_k* wird ausdrücklich offen gelassen.

---

## 2. Primärextrakt

NEU-206 geht in vier Schritten vor:
1. Für M_{g,r}=e(nr)-e(mr) werden offene Untergruppen gesucht, auf denen M_{g,r} verschwindet.
2. Aus einer Abzählung Q/Z={r_1,r_2,...} wird eine Teilbarkeitskette L_j=lcm(L(r_1),...,L(r_j)) konstruiert.
3. Mit P_j=E_{L_j}, q_j=P_j-P_{j+1} werden die geladenen Schalen w_j=μ_m q_j μ_n* definiert.
4. Der Transport unter μ_k wird auf die arithmetische Abbildung L↦L/(L,k) reduziert.

---

## 3. Exakter Charakterkern von M_{g,r}

[O-206-1a]: ✓[M]

Für r=p/q mit (p,q)=1 gilt M_{g,r}=e(mr)(e((n-m)r)-1). Entscheidend ist die additive Ordnung von t=(n-m)r:
ord(t) = q/gcd(q,n-m).

Damit ist der minimale Exponent L_min(g,r) = q/gcd(q,n-m), nicht q.

NEU-206 bezeichnet L(r)=q als minimal; das ist falsch. L(r)=q ist stets zulässig (auf q·Ẑ verschwinden beide Charaktere), aber im Allgemeinen nicht minimal.

Korrigierte Ersatzformel:
L_min(g,r) = ord((n-m)r) = q/gcd(q,n-m).

Auch die Gleichheitsbedingung "np≡mp (mod q)" als Kriterium für das Verschwinden auf qẐ ist fehlerhaft: auf qẑ verschwinden beide Charaktere unabhängig von dieser Kongruenz.

---

## 4. Charakterkern-Erschöpfungskette

[O-206-1b]: ✓[M]

Nach Korrektur setzt man:
L_j = lcm(L_min(g,r_1),...,L_min(g,r_j)),  mit L_0:=1, P_0:=E_1=1.

Dann gilt L_j | L_{j+1}, also P_{j+1}≤P_j. Für ν≤j folgt M_{g,r_ν}P_j=0.

Korrekte Beweisführung: Nicht über eine Ordnungsrelation M·P_j ≤ M·P_L (M ist nicht positiv), sondern über Produktfaktorisierung:
M_{g,r_ν} q_j = (M_{g,r_ν} P_{L(r_ν)}) P_j = 0.

Die Kette wächst unbeschränkt, da Multiplikation mit n-m≠0 auf Q/Z surjektiv ist.

Indexkorrektur: L_0:=1 und P_0:=E_1=1 müssen explizit ergänzt werden.

---

## 5. Projektionen q_j

✓[M]

Mit q_j=P_j-P_{j+1} gelten q_j²=q_j=q_j* und q_j q_ℓ=0 für j≠ℓ. Teleskopformel:
1 = sum_{j=0}^{N-1} q_j + P_N.

Falls mehrere aufeinanderfolgende L_j gleich sind, ist q_j=0 (beeinträchtigt Orthogonalität nicht). Da L_j unbeschränkt wächst, gibt es unendlich viele nichtverschwindende Schalen.

---

## 6. Partialisometrieeigenschaft und Biorthogonalität

[O-206-2a]: ✓[M]

Setze w_j=μ_m q_j μ_n*. Grad: deg(w_j)=m/n=g.
Anfangsprojektion: w_j* w_j = μ_n q_j μ_n* (Projektion).
Endprojektion: w_j w_j* = μ_m q_j μ_m* (Projektion).

Biorthogonalität für j≠ℓ:
w_j* w_ℓ = μ_n q_j (μ_m* μ_m) q_ℓ μ_n* = μ_n q_j q_ℓ μ_n* = 0,
w_j w_ℓ* = 0 ebenso.

Beweis verwendet nur μ_k* μ_k=1 und Orthogonalität der q_j.

---

## 7. Eventuale Kommutation mit e(r)

[O-206-2b]: ✓[M]
[O-206-2c]: ✓[M]

Korrekte Kommutatorformel:
[w_j, e(r)] = μ_m M_{g,r} q_j μ_n*.

Für festes r_ν und j≥ν: M_{g,r_ν} q_j = 0, also [w_j, e(r_ν)]=0.

Für ungesättigte Partialsummen S_N = sum_{j=0}^{N-1} c_j w_j gilt ab N≥ν:
[S_N, e(r_ν)] = sum_{j=0}^{ν-1} c_j [w_j, e(r_ν)] = konstant.

Der Kommutator ist ab N=ν exakt konstant (stabil).

---

## 8. Harter Fehler beim Sättigungsterm W_N

[O-206-2d]: ×[M]
[O-206-2e]: ✓[K/M]

NEU-206 führt Z_N = sum_{j<N} c_j w_j + c_N W_N mit W_N∈A_g ein und behauptet Stabilität des e(r_ν)-Kommutators. Das folgt nicht: Der Term c_N[W_N,e(r_ν)] kann für beliebiges W_N∈A_g divergieren.

Korrigierte Bedingung: [W_N,e(r_ν)]=0 für alle hinreichend großen N.

Natürliche Wahl: W_N=μ_m P_N μ_n*. Dann:
[W_N, e(r_ν)] = μ_m M_{g,r_ν} P_N μ_n* = 0 für N≥ν.

Diese Wahl löst die e(r)-Seite. Die Isometrietransportbedingungen sind damit noch nicht erfüllt.

---

## 9. Die vier Transportformeln

[O-206-3]: ✓[M]

Korrekte Formeln:
(1) E_L μ_k = μ_k E_{L/(L,k)}
(2) μ_k E_L μ_k* = E_{kL}
(3) μ_k* E_{kL} = E_L μ_k* (aus (1) durch Adjungieren)
(4) E_{L/(L,k)} μ_k* = μ_k* E_L (aus (2) durch Adjungieren)

Direkter Beweis von (1):
E_L = (1/L) sum_{j=0}^{L-1} e(j/L).
Mit e(r)μ_k = μ_k e(kr):
E_L μ_k = μ_k · (1/L) sum_{j=0}^{L-1} e(kj/L).
Mit d=(L,k), L'=L/d: kj/L nimmt jeden Wert a/L' genau d-mal an, also
(1/L) sum_{j} e(kj/L) = E_{L/( L,k)}.

Die Beweisreihenfolge in NEU-206 ist teilweise zirkulär (206.3.1 über 206.3.4 begründet). Das Resultat selbst ist korrekt.

---

## 10. Harter Fehler im dyadischen Rückblick

[O-206-dyadic]: ×[M]

NEU-206 behauptet: q_j μ_{2^a} = μ_{2^a} q_{(j-a)+}.

Korrekt ist:
μ_{2^a} q_j = μ_{2^a} (P_j - P_{j+1}) = μ_{2^a} P_{(j-a)+} - μ_{2^a} P_{(j+1-a)+}
= { 0,            falls j < a
  { μ_{2^a} q_{j-a},  falls j ≥ a.

Für j<a sind beide Projektionen gleich P_0, der Ausdruck ist null. Die grundlegende Aussage (Transport verschiebt nur um endlich viele Schalen) bleibt richtig.

---

## 11. Allgemeine Transportgeometrie

[O-206-transport]: ✓[M]_part

Für die allgemeine Kette gilt:
μ_k q_j μ_k* = E_{kL_j} - E_{kL_{j+1}} (korrekt).
μ_k* q_j μ_k enthält Projektionen E_{L_j/(L_j,k)} - E_{L_{j+1}/(L_{j+1},k)},
die im Allgemeinen keine einzelne Schale q_{j'} der Erschöpfungskette sind.

Zentraler Engpass: Die Charakterkernkette ist nicht automatisch unter L↦L/(L,k) schichtstabil.

Die Teilmarkierung ist nötig, weil NEU-206 den Transport diagnostiziert, aber noch keine vollständige Kommutatorformel für ein konkret definiertes gesättigtes Z_N herleitet.

---

## 12. Das Kriterium (206.4.5) ist nicht wohldefiniert

×[M]

NEU-206 verwendet einen Index j'(j,k), der den Schalenindex von E_{L_j/(L_j,k)} bezeichnen soll. Da diese Projektion im Allgemeinen kein Kettenglied P_{j'} ist, existiert ein solcher eindeutiger Index im Allgemeinen nicht.

Korrigierte Formulierung: Direkte Kontrolle der Projektionen auf der gemeinsamen booleschen Algebra erzeugt von {E_{L_j}} und {E_{L_j/(L_j,k)}}. Erst nach Refinementzerlegung in atomare Schalen darf dies in Koeffizientenbedingungen übersetzt werden.

---

## 13. Kein bewiesener Ketten-No-go

⚠[M]

Ein mathematischer Widerspruch zwischen Charakterkernerschöpfung und kontrolliertem Isometrietransport wird nicht bewiesen.

Insbesondere: L_j ≥ lcm(1,...,j) gilt nicht für eine beliebige Abzählung von Q/Z; diese Schranke setzt eine nach Nennern geordnete Enumeration voraus.

Auch schnelles Wachstum allein beweist nicht, dass die Quotientenprojektionen unkontrollierbar sind. Für jedes feste k entfernt L↦L/(L,k) nur einen Teiler von k.

Korrekte Einordnung: arithmetisches Spannungsverhältnis ⚠[M], nicht bewiesener allgemeiner Ketten-No-go.

---

## 14. Fester Multiplikator k₀

[O-206-fixed-k0]: ✓[M]_neg

Eine Kette L_{j+1}=k₀ L_j mit festem k₀ kann nur Primfaktoren absorbieren, die bereits in L_0·k₀ liegen. Sie erschöpft damit nicht die Charakterkerne von Elementen mit Ordnungen, die beliebig viele verschiedene Primteiler besitzen.

Umfangsklausel: Ausgeschlossen ist ausschließlich die eindimensionale Kette mit einem einzigen festen endlichen Multiplikator. Nicht ausgeschlossen: Bewertungsgitter, adaptive Refinementketten, Netze, separierbare Primkanäle.

---

## 15. Was ist mit den e(r)-Fehlern wirklich gelöst?

Bewiesen:
∀r ∃J(r): [w_j,e(r)]=0 für j≥J(r).

Noch nicht bewiesen:
- Stabilität für beliebigen Sättigungsterm W_N
- Normkonvergenz der μ_k-Kommutatoren [O-206-4a] ?[O]
- Normkonvergenz der μ_k*-Kommutatoren [O-206-4b] ?[O]
- Derivation auf algebraischem Kern
- Nichtinnerheit
- Zieltyp A_alg oder A_C*

---

## 16. Dateistatus NEU-206

| Bestandteil | Auditstatus | Befund |
|---|---|---|
| M_{g,r}=e(nr)-e(mr) | ✓[M] | Korrekte Charakterdifferenz |
| M_{g,r}(0)=0 | ✓[M] | Beide Charaktere haben am Ursprung Wert 1 |
| M_{g,r}=0 ⟺ (n-m)r=0 | ✓[M] | Korrekt |
| L(r)=q als hinreichender Kern | ✓[M] | Für r=p/q ausreichend |
| L(r)=q als minimaler Kern | ×[M] | Minimal ist q/gcd(q,n-m) |
| Charakterkernkette L_j | ✓[M] | Nach Korrektur vollständig |
| Beweis mittels M·P_j ≤ M·P_L | ⚠[M] | Keine Positivitätsordnung; Produktfaktorisierung nötig |
| Definition von L_0 | ⚠[M] | Fehlt; L_0=1 ergänzen |
| Projektionen q_j | ✓[M] | Orthogonale Differenzprojektionen |
| w_j∈A_g Partialisometrien | ✓[M] | Anfangs- und Endprojektionen explizit |
| Biorthogonalität | ✓[M] | Vollständig bewiesen |
| Eventuale e(r)-Kommutation | ✓[M] | Für jede feste Charakterrichtung |
| Stabilität ungesättigter Partialsummen | ✓[M] | Ab endlichem Index exakt konstant |
| Stabilität mit beliebigem W_N∈A_g | ×[M] | Sättigungsterm nicht kontrolliert |
| Natürlicher Sättigungskandidat μ_m P_N μ_n* | ✓[K/M] | Löst e(r)-Seite; Isometrietransport offen |
| Vier Transportformeln | ✓[M] | Korrekt; Beweisreihenfolge reparieren |
| Dyadische Formel q_j μ_{2^a} für j<a | ×[M] | Korrekt: Ausdruck ist null |
| Allgemeine Quotientenprojektionsformel | ✓[M] | Richtige Reduktion |
| Indexkriterium j'(j,k) | ×[M] | Index im Allgemeinen nicht definiert |
| Allgemeiner Ketten-No-go | ⚠[M] | Nicht bewiesen |
| Feste Multiplikatorkette L_{j+1}=k₀L_j | ✓[M]_neg | Kann nicht alle Primordnungen absorbieren |
| Normkonvergenz μ_k-Kommutatoren | ?[O] | Zentraler offener Knoten |
| Normkonvergenz μ_k*-Kommutatoren | ?[O] | Ebenfalls offen |
| Geladene Derivation | ✓[M]_neg,Quelle | In NEU-206 noch nicht konstruiert |
| Nichtinnerheit | ?[O] | Kein Grenzobjekt vorhanden |
| **Gesamtstatus** | **✓[M]_part** | Starke Schalenkonstruktion; Transportproblem offen |

---

## 17. Ersetzte Aussagen

1. **Minimaler Charakterkern**
   Falsch: L_min(r)=q.
   Korrekt: L_min(g,r)=ord((n-m)r)=q/gcd(q,n-m).

2. **Stabilität von Z_N**
   Falsch: W_N∈A_g ⟹ [Z_N,e(r)] stabil.
   Korrekt: [Z_N,e(r)] = sum_{j<J(r)} c_j[w_j,e(r)] + c_N[W_N,e(r)].
   Sättigungsterm separat kontrollieren.

3. **Dyadischer Schalentransport**
   Falsch: q_j μ_{2^a} = μ_{2^a} q_{(j-a)+}.
   Korrekt: μ_{2^a} q_j = { 0 falls j<a; μ_{2^a} q_{j-a} falls j≥a }.

4. **Transportkriterium**
   Falsch: |c_{j'(j,k)}-c_j|→0.
   Korrekt: |[Z_N,μ_k]-[Z_M,μ_k]|→0, formuliert auf der gemeinsamen Projektionsverfeinerung.

---

## 18. Beitrag zu Objekt X

NEU-206 erzielt einen echten algebraischen Fortschritt:
- Für jeden festen geladenen Grad g≠1 existiert eine biorthogonale Familie w_j∈A_g,
- deren hochliegende Schalen mit jedem fest gewählten e(r) exakt kommutieren.

Damit ist die Charakterfehlerobstruktion aus NEU-205 auf Schalenebene überwunden.

Nicht erreicht:
- Konvergente Kommutatoren mit μ_k, μ_k*
- Geladene Derivation A_alg→A_C*
- A_alg-wertige Derivation
- Nichtinnerheitsnachweis
- Geladene HH¹-Klasse
- Cup-Aufstieg
- Operator- oder Positivitätsbrücke zur Weil-Form

Zentraler neuer Engpass:
Wie lässt sich die Divisibilitätsgeometrie L↦L/(L,k) auf einer gemeinsamen Schalenverfeinerung kontrollieren?

---

## 19. Aktualisierter DAG

| Knoten | Aussage | Status |
|---|---|---|
| [O-206-1a] | Minimaler Charakterkern: L_min(g,r)=ord((n-m)r) | ✓[M] |
| [O-206-1b] | Erschöpfungskette L_j=lcm(L_min(g,r_1),...) | ✓[M] |
| [O-206-2a] | w_j=μ_m q_j μ_n*∈A_g: Partialisometrien und biorthogonal | ✓[M] |
| [O-206-2b] | [w_j,e(r)]=0 für j≥J(r) | ✓[M] |
| [O-206-2c] | Ungesättigte Partialsummen: stabile e(r)-Kommutatoren | ✓[M] |
| [O-206-2d] | Beliebiger W_N∈A_g erhält Stabilität | ×[M] |
| [O-206-2e] | Natürliche Sättigung W_N=μ_m P_N μ_n* | ✓[K/M] |
| [O-206-3] | Vier Transportformeln für E_L und μ_k, μ_k* | ✓[M] |
| [O-206-dyadic] | q_j μ_{2^a}=μ_{2^a} q_{(j-a)+} (für j<a) | ×[M] |
| [O-206-4a] | Normkonvergenz μ_k-Kommutatoren | ?[O] |
| [O-206-4b] | Normkonvergenz μ_k*-Kommutatoren | ?[O] |
| [O-206-4c] | Refinementzerlegung E_{L_j/(L_j,k)} | ?[O] |
| [O-206-no-go] | Allgemeiner No-go für jede lineare Charakterkernkette | ?[O] |
| [O-206-fixed-k0] | Feste geometrische Kette L_{j+1}=k₀L_j erschöpft alle Charaktere nicht | ✓[M]_neg |
| [O-charged-analytic] | Geladene äußere Derivation A_alg→A_C* | ?[O] |
| [O-charged-algebraic] | Geladene äußere Derivation A_alg→A_alg | ?[O] |

---

## 20. Gesamturteil

**NEU-206: ✓[M]_part**

Der stärkste belastbare Satz lautet:
Es existieren biorthogonale homogene Partialisometrieschalen w_j∈A_g, die mit jedem festen e(r) schließlich exakt kommutieren.

Nicht bewiesen: die zentrale Fortsetzung zu einer geladenen Derivation. Insbesondere sind der Sättigungsterm und die arithmetische Transportgeometrie unter L↦L/(L,k) noch offen.

**Nächster tatsächlicher Auditknoten:** NEU-207 — Bewertungsgitter, Primschalentransport und Ketten-No-go.
