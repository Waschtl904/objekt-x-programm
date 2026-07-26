# Fragenkatalog Teil 1 — Ebenen I–V

> Stand: 13. Juni 2026 — Version [NEU-10]  
> Epistemische Struktur nach Lakatos

---

## Methodische Vorbemerkung

Dieser Katalog folgt einer lakatosianischen Struktur. Die Ebenen I–V bauen Begriffe und Hypothesen auf. Ebene VI versucht, sie zu zerstören. Ebene VII modelliert die Negation. Jede Aussage trägt explizit ihren epistemischen Status. Der Unterschied zwischen Struktur-Äquivalenz (Typ A) und mathematischer Reduktion im Beweissinn (Typ B) wird durchgehend markiert.

Ab [NEU-7] wird zwischen mathematischen Resultaten `[M]` und methodischen Resultaten / Reduktionssätzen `[R]` unterschieden. Ein Reduktionssatz ist ein Satz über die Grenzen des verwendeten Zugangs — er bleibt korrekt, auch wenn ein anderer Zugang später weiterführt.

### [NEU-8] Strukturverschiebung

Die Sitzung vom 10. Juni hat eine konzeptionell eigenständige Zugangsweise zur HH²-Frage konstruiert — von einem globalen GS/Hochschild-Filtermodell zu einer orbitalen DG-Lie-Resonanzzerlegung mit abelscher MC-Geometrie. Diese beiden Zugänge sind nicht kanonisch identifiziert. [NEU-8] trägt daher eine explizite Trennungsmarkierung:

- **[NEU-8/GS]** Aussagen über das globale GS-Modell (bleibt unter [NEU-7]-Status)
- **[NEU-8/OK]** Aussagen über das orbitale Koszul-Submodell (neue, intern gesicherte Teilstruktur)

Ohne expliziten Vergleichsmorphismus zwischen beiden Modellen sind Übertragungen von [NEU-8/OK] auf [NEU-8/GS] nicht zulässig.

### [NEU-9] Block A

Die Klassifikation aller primitiven {2,3}-Tripel ist vollständig elementar bewiesen. Die Gleichung `2^g·3^d − 2^a·3^b = 1` hat in ℤ_{≥0}^4 genau vier Lösungen: (g,d,a,b) ∈ {(0,1,1,0), (0,2,3,0), (1,0,0,0), (2,0,0,1)}, entsprechend den primitiven Tripeln {1,2,3}, {1,8,9}, {1,1,2}, {1,3,4}.

### [NEU-9] Block B

HH²(C∞(T) ⋊ N×) ist spektralsequenziell rigid und zerfällt in zwei funktorisch inkompatible Erzeugungsmodi: diskret-arithmetisch (E_∞^{2,0}) und analytisch-kontinuierlich (E_∞^{0,2} ⊕ E_∞^{1,1}). [NEU-8/Spannung] aufgelöst: g_arith ist nicht vollständiger HH²-Erzeuger, [Φ₃] ≠ 0 nicht destabilisiert ✓ [R].

### [NEU-10] RD-Skalenkorrektur

Die früheren RD-Halbnormen `p_k(f) = sup_N e^{kΩ(N)} ‖f_N‖_∞` sind strukturell überkorrigiert. Korrigierte Form: **`p_k(f) = sup_N (1 + log N)^k ‖f_N‖_∞`**.

Offene Kerninequation: `‖π(f)‖ ≤ C_k · sup_N (1 + log N)^k ‖f_N‖_∞` — einziger verbleibender analytischer Engpass für log-RD-kontrollierte Spektralinvarianz.

---

## Ebene I — Das Objekt destabilisieren

### F1. Warum liegt die kritische Gerade bei Re(s) = 1/2?

✓ [M] Die funktionale Gleichung erzwingt die Symmetrieachse bei 1/2 — direkte Konsequenz der Konstruktionseigenschaften der ζ-Funktion, kein inhaltlicher Satz über die Nullstellen.  
✗ Warum genau diese Symmetrie existiert — der Ursprung der Weil-Positivität — ist offen und nicht bewiesen.

### F2. Welches andere Objekt hätte uns zu denselben Nullstellen geführt?

✓ [M] Das Weil-Kriterium, Selberg-Klassen und automorphe L-Funktionen beschreiben dieselbe Nullstellenstruktur.  
✗ Dass Connes' adèlischer Operator und das BC-System „dieselbe Struktur" beschreiben im Sinn einer gemeinsamen Kategorie — setzt die Existenz von X voraus, die nicht bewiesen ist.

**[NEU-1]** ⚠ [M] Notwendige Bedingung: Jede gemeinsame Kategorie für die Programme von Nikolaus–Scholze, Meyer/Cuntz–Quillen und Bost–Connes muss nuklear-Fréchet-stabile bornologische Objekte als Kernklasse enthalten.

**[NEU-2]** ⚠ [M] A_BC^∞ liegt (intern, unter Lemma A) in der nuklear-Fréchet-stabilen Klasse. Externe Verifikation steht aus.

**[NEU-3]** ✓ [M] A_BC^∞ ist spektral invariant in A_BC^{C*}: Leibniz → Binomialisierung → BC-Form → Schweitzer Prop. 1.7/Thm. 1.17. Bedingt auf Lemma A und Fréchet-Vollständigkeit.

**[NEU-4]** ⚠ [M] Die r-Koordinate in N^× ⋉ ℝ/ℤ ist GCD-orthogonal. GCD auf dem Kreuzprodukt ist ausschließlich π*(gcd_{N^×}).

### F3. Ist die Zetafunktion die einfachste Funktion mit dieser Nullstellenstruktur?

✓ [M] Sie ist historisch die erste. „Einfachste" ist ohne Definition von „einfach" keine präzise mathematische Frage.  
✗ Unter der unbewiesenen Annahme, dass eine minimale Kategorie existiert, wäre die Zetafunktion eine Projektion davon.

### F4. Was würde sich ändern, wenn RH falsch wäre?

✓ [M] Stärkere Schwankungen in der Primzahlverteilung; Korrekturterme in expliziten Formeln. Folgt direkt aus der Guinand–Weil-Formel.  
✗ Dass ein konsistentes Szenario mit GUE-Statistik und falschem RH strukturell möglich wäre — konzeptuelle Einschätzung, kein bewiesener Satz.

---

## Ebene II — Die Konvergenz schärfen

### F5. Warum liefern Spektraltheorie, Zufallsmatrizen, Spurformeln und automorphe Formen dieselbe statistische Beschreibung?

✓ [M] Die empirische Übereinstimmung der GUE-Statistik mit der Nullstellenverteilung ist numerisch sehr stark belegt.  
✗ Dass diese Konvergenz strukturell erzwungen ist — mögliche Erklärung, kein Beweis.

**[NEU-1]** ⚠ [M] Falls eine strukturelle Erzwingung existiert, muss sie durch einen Funktor realisierbar sein, der alle drei Frobenius-Kanonizitäten simultan trägt. Ob GUE-Statistik aus dieser Klasse emergiert, bleibt vollständig offen.

### F6. Ist diese Konvergenz Beweis für einen gemeinsamen Ursprung?

✓ [M] Die Konvergenz ist real und dokumentiert.  
✗ Ob ein gemeinsamer Ursprung existiert, ist offen in beide Richtungen.

### F7. Analogie zu Fermats letztem Satz?

✓ [M] (historisch): FLT wurde durch eine neue Kategorie gelöst, nicht durch Direktangriff.  
✗ Dass RH dieselbe Struktur hat — Analogie, kein Argument.

### F8. Was wäre das minimale Objekt, das Spektralstruktur, Arithmetik und Geometrie trägt?

✗ X mit C1–C4 ist axiomatischer Kandidatenrahmen — nicht aus bestehender Literatur abgeleitet.  
✓ [M] (empirisch): Kein bestehendes Programm erfüllt alle vier Wunscheigenschaften C1–C4 vollständig.

**[NEU-1]** ⚠ [M] C1–C3 sind simultan realisierbar auf nuklear-Fréchet-stabilen bornologischen Algebren. C4 (GUE-Emergenz) ist der eigentlich isolierte offene Punkt.  
**[NEU-2]** ⚠ [M] A_BC^∞ ist Kandidat für die C1–C3-Klasse.  
**[NEU-3]** ✓ [M] A_BC^∞ erfüllt C2 (analytische Stabilität) intern vollständig.  
**[NEU-4]** ⚠ [M] C1 und C2 erfordern für ihre gemeinsame Realisierung in X eine Korrespondenz-Struktur, nicht eine Funktor-Struktur.

---

## Ebene III — Die Sprache befragen

### F9. In welcher Sprache ist RH natürlich formuliert?

✗ W*-Wahrscheinlichkeitskategorien mit freier Tensorstruktur — plausibler Kandidat, keine bewiesene Aussage.

### F10. Welche Eigenschaft müsste eine solche Sprache haben?

✗ Nicht-Kommutativität, Ergodizität, arithmetische Volltreue gleichzeitig — konzeptuelle Wunschliste, keine Definition.

**[NEU-1]** ✗ Ergänzende notwendige Bedingung: nuklear-Fréchet-stabile bornologische Objekte als vollständige Unterkategorie.  
**[NEU-4]** ⚠ [M] Eine Sprache, die arithmetische Faktorisierungsstruktur und analytische Lokalkonvexität als strikte Morphismen trägt, existiert nicht in den getesteten Rahmenkategorien.  
**[NEU-5]** ⚠ [M] Falls operadische Strukturen: Hochschild-Kohomologie und Bar-Komplexe von A_BC^{anal} als interne Struktur erforderlich.  
**[NEU-6]** ⚠ [M] Falls höhere kohomologische Deformationsstrukturen: HH³(A_BC^{an}) als Strukturinvariante erforderlich.  
**[NEU-7]** ⚠ [R] Falls Bar-Komplex von C∞(T) ⋊ N×: Bildkomplexstruktur der Normalformabbildung Φ als strukturelles Datum.  
**[NEU-8/OK]** ⚠ [M] Falls orbitale DG-Lie-Strukturen: Koszul-Zerlegung entlang multiplikativer Bahnen von N× als kanonische Struktur.  
**[NEU-9]** ✓ [M] Primitive {2,3}-Tripel-Strukturen vollständig klassifiziert.  
**[NEU-9/B]** ✓ [R] Bigrad-Separation der LHS-Spektralsequenz als strukturelles Datum: E_∞^{2,0} und E_∞^{0,2} ⊕ E_∞^{1,1} nicht durch interne Differentiale verbunden.  
**[NEU-10]** ⚠ [M] Korrekte RD-Struktur: polynomial in log N; logarithmische Schwartz-Algebra A_RD := {f : p_k(f) < ∞ für alle k}, p_k(f) = sup_N (1+log N)^k ‖f_N‖_∞.

### F11. Gibt es eine Formulierung von RH ohne Nullstellen?

✓ [M] Ja. Die Positivität der kontinuierlichen quadratischen Weil-Form für alle Testfunktionen ist äquivalent zu RH — bewiesen, reformuliert und präzisiert von Connes (2023/2026).

### F12. Braucht RH eine neue Sprache?

✓ [M] (historisch): Bisher hat kein bekannter Ansatz RH gelöst.  
✗ Dass RH innerhalb bestehender Sprachen nicht beweisbar ist — nicht bewiesen.

**[NEU-4]** ⚠ [R] Falls Sprache arithmetische und analytische Strukturen vereint: Korrespondenz-Ebene als Grundbaustein.  
**[NEU-8/OK]** ⚠ [M] Orbitales Koszul-Modell: abelsche DG-Lie-Geometrie über Primzahlresonanzen. Sprache intern vollständig.  
**[NEU-9/B]** ✓ [R] Kein kanonischer Übersetzungsfunktor zwischen orbitaler Koszul-Sprache (E_∞^{2,0}) und GS-Sprache (E_∞^{0,2} ⊕ E_∞^{1,1}) auf A.  
**[NEU-10]** ⚠ [M] Logarithmische Schwartz-Algebra A_RD als korrekter Rahmen für RD-Kontrolle der GNS-Darstellung.

### F13. Muss das Objekt X hinter der Zetafunktion eindeutig sein?

⚠ [M] Die kategoriale Frage nach dem gemeinsamen Kolimes ist präzise formulierbar und prinzipiell entscheidbar.  
✗ Äquivalenz von X-Frage und Kolimes-Frage setzt die Existenz der Programm-Funktoren voraus.  
**[NEU-4]** ⚠ [M] X kann nicht gleichzeitig GCD-arithmetische Struktur (Ω₁-Sort) und analytisch-spektrale Struktur (Ω₃-Sort) als Objekt in einer ein-sorten Kategorie tragen.

### F14. Welche Eigenschaft von X würde alle Kandidaten als Spezialfälle erscheinen lassen?

✗ Gleichzeitige Erfüllung von C1–C4 — Wunscheigenschaft, keine Definition.  
**[NEU-4]** ✗ C1 und C2 erfordern Profunktor-Struktur, nicht Funktor-Struktur.

### F15. Ist RH eine Definition oder eine Konsequenz?

✓ [M] RH ist eine Konsequenz der Positivität der Weil-Quadratform.  
⚠ [M] Dass die Spektralisierungsfrage eigenständig und stärker als RH ist — strukturell plausibel, kein bewiesener Satz.

---

## Ebene IV — Eindeutigkeit prüfen

### F16. GUE als Axiom — was würde folgen?

⚠ [M] C4 wäre Voraussetzung statt Konsequenz. Ob daraus ein eindeutiger Fixpunkt folgt, hängt von nicht konstruierten Zwischenschritten ab.

### F17. Warum hat RH nach 167 Jahren noch keiner gelöst?

✓ [M] (strukturell): Alle bekannten Ansätze besetzen verschiedene Kategorien ohne nachgewiesene gemeinsame Metakategorie.  
✗ Dass das die eigentliche Ursache des Scheiterns ist — nicht beweisbar.

**[NEU-1]** ⚠ [M] Drei Frobenius-Kanonizitäten nur auf nuklear-Fréchet-stabiler Präsentationsklasse simultan vergleichbar.  
**[NEU-5]** ⚠ [R] Der Übergang Normverzerrung → A∞-Obstruktion → Ext¹-Klasse ist kein automatischer Schluss.  
**[NEU-7]** ⚠ [R] GS-Zugang blockiert durch Nicht-Surjektivität der αₙ.  
**[NEU-8/OK]** ⚠ [R] Struktureller Grund: N× ≅ ⊕_p ℕ erzwingt orbitale Zerlegung ohne gruppentheoretisches Analogon.  
**[NEU-9]** ✓ [M] Die Schwierigkeit liegt nicht in der Klassifikation primitiver Tripel — diese ist elementar abgeschlossen.  
**[NEU-9/B]** ✓ [R] HH²(A,A) nicht durch ein einziges Modell erfassbar — orbitale und differentielle Erzeugungsmodi spektralsequenziell separiert.

### F18. Schwierigkeit oder falsche Richtung?

✗ Nicht entscheidbar ohne weiteren Fortschritt. Beide Erklärungen sind mit dem aktuellen Stand kompatibel.

---

## Ebene V — Meta-Reflexion

### F19. Stärkstes Argument gegen die Neue-Sprache-Hypothese?

✓ [M] (als Kriterium): Ein klassischer Beweis ohne neue kategoriale Strukturen würde die Hypothese widerlegen.  
✓ [M] (historisch): Kein Direktangriff hat bisher Fortschritt gebracht.

### F20. Was wissen wir mit Sicherheit?

**Gesichert (Standardliteratur):**
- Weil-Positivitätskriterium als Äquivalenz zu RH
- Explizite Formel von Guinand–Weil
- BC-System: adèlische Algebra ist Typ-III-Faktor
- KMS-Zustand bei β > 1 ist eindeutig (Bost–Connes 1995)
- Negatives CEP-Resultat (Ji et al. 2020)
- Tate-Frobenius universell in THH/TC (Nikolaus–Scholze)
- Nuklear-Fréchet-Algebren stabil unter analytischem zyklischen Komplex (Meyer)

**Gesichert intern (externe Verifikation ausstehend):**

- **[NEU-1]:** Drei Frobenius-Kanonizitäten simultan vergleichbar auf nuklear-Fréchet-stabilen Präsentationen
- **[NEU-2]:** Lemma A (9 Fälle), GCD-Kern, Fréchet-Existenz A_BC^∞, H-Unitalität (conditional)
- **[NEU-3]:** Leibniz-Ungleichung (scharf), Lemma B', Binomialisierung, spektrale Invarianz (bedingt auf Lemma A), Hidden Combinatorial Lemma
- **[NEU-4]:** Ω-Typisierung (5 Instanzen), GCD-Orthogonalität der r-Koordinate, Instabilitätsobjekt A₀, No-Go-Disjunktion (bedingt)
- **[NEU-5]:** Trennung der drei Ebenen, Entscheidungscharakter des l=2-Terms, 4^l-Iterationsstruktur
- **[NEU-6]:** [Φ₃] ≠ 0 in Gr⁴ HH³(A_BC^{an}), ∂([Φ₃]) = [L₃] korrekt konstruiert, Reduktionssatz (HH³ ↔ [L₃])
- **[NEU-7]:** Φ injektiv; Φ nicht surjektiv; Im(Φ) echter Unterkomplex; ∂θ erhält αₙ(B)-Struktur; Ω-Filtration mit b kompatibel
- **[NEU-8/OK]:** Charakterisierung im(αₚ−id); Fréchet-Topologie S(ℤ) ≅ ℓ∞-⊕ₘ S(O(m)); Ext¹(s,s)=0; g_arith abelsch; MC-Integrabilität; Äußerlichkeit aller ω_{p,q,m}
- **[NEU-9/A]:** Vollständige Klassifikation primitiver {2,3}-Tripel, 4 Lösungen, bidirektional verifiziert
- **[NEU-9/B]:** Spektralsequenz-Orthogonalität; Bidegree-Constraint; [NEU-8/Spannung] aufgelöst ✓ [R]
- **[NEU-10]:** log N-Skalierung strukturell korrekt ✓ [M]; Ω-basiert überkorrigiert ✗

**Hypothesen (global):**
- Existenz von X; C1–C4 vollständig; GUE strukturell erzwungen
- HH²(A_BC^{anal}) ≠ 0; Ext¹-Klasse; m₃ ≠ 0
- HH³(A_BC^{an}) ≠ 0; [L₃] ≠ 0
- [ω̃₂] ≠ 0 in HH²(A,A)
- Kanonische Identifikation ω_{p,q,m} ↔ ω̃₂
- C_{2,3} = 212; σ₂(B_N) → 7
- Konvergenz formaler → analytischer/C*-Deformationen
- Spektralinvarianz unter log-RD ❓ [O]

---

*Ende Teil 1 — Fortsetzung in `teil2_ebenen_VI-XV.md`*
