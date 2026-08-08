# F4-Primäraudit — Mangoldt-/Primzahlpotenzstrang und Mediatorstatus

**Datum:** 8. August 2026  
**SYN-Ziel:** P05 — Relative Prime Channels and Arithmetic Edge Geometry  
**Prüfart:** `TARGETED-REAUDIT` / `AUDIT-RECONCILED`  
**Verfahren:** mathematischer Primäraudit; erster externer Repo-Check wegen nachgewiesenem Scope-Fehler **nicht als Gegenprüfung gewertet**; pfadgebundener Zweitcheck noch ausständig  
**Status dieses Auditblatts:** Primäraudit abgeschlossen; **F4 noch nicht `PASS A COMPLETE`** bis gültige Gegenprüfung erfolgt

---

## 0. Scope-Korrektur und explizite Repo-Provenienz

Die ursprüngliche F4-Inventarliste `NEU-250g/i/j` war unvollständig. Für den heute gültigen Endstand müssen mindestens folgende Knoten gemeinsam gelesen werden:

- NEU-250f + Patch 1 (`1579a379`) — Typkorrektur des Filtrations-No-Go,
- NEU-250g — modulare Halbgewichtung im primitiven $p$-Kanal,
- NEU-250h — Testfunktionswert / Matrixkoeffizient,
- NEU-250i — Primzahlpotenzsektor und gradnormierte BC-Energie,
- NEU-250j — Trägertrennung Mangoldt vs. Kreuzprimkollision,
- NEU-250k — adelischer Mediatorport,
- NEU-250l — Streublock-Mediatoraudit, Entscheidung J-A/J-B,
- NEU-250n — spätere Korrektur zu K1: $\mathcal S_{\rm adel}$ ist Architekturplatzhalter, kein fertig konstruierter topologischer Quellenraum.

Zusätzlich wurden die späteren Fortsetzungen NEU-250m/o/p/q/r als **Korrektur- und Superseding-Scan** geprüft. Sie sind nicht sämtlich P05-Kernknoten, verhindern aber, dass ein Zwischenstand aus 250j–n fälschlich als letzter Repo-Stand gelesen wird.

NEU-250p auditiert den **archimedischen** Halbgewichtstransfer $J_{1/2}$; er repariert nicht die unten isolierte BC-Generalisation $h_p^{\rm bal}\to h_n^{\rm bal}$ und ist daher kein Endanker dieses lokalen F4-Punktes.

### 0.1 Verifizierte Repo-Pfade auf `main`

Die F4-Provenienz ist **ordnerübergreifend**. Genau dieser Umstand ist für jeden späteren Repo-Check verbindlich:

| Knoten | Repo-Pfad | Blob-SHA | Rolle im F4-Audit |
|---|---|---|---|
| NEU-250g | `01-primkanten-werkzeuge/NEU-250g_Modulare_Halbgewichtung_und_primitiver_Weilfaktor.md` | `33df3eea74560ce9e1bc24023152df3f2b44e508` | P05-Kern |
| NEU-250i | `01-primkanten-werkzeuge/NEU-250i_Primzahlpotenzsektor_Gradnormierte_BC_Energie_und_vollstaendiger_von_Mangoldt_Faktor.md` | `d78d6746cfbb49f9f4845361ed202d4b008f4436` | P05-Kern |
| NEU-250j | `01-primkanten-werkzeuge/NEU-250j_Traegertrennung_von_Mangoldt_Sektoren_und_Primfaserüberlappungen.md` | `63dd57f81b865616a6aa3084c3ac6c476d6ccada` | P05/P11-Grenzknoten |
| NEU-250f Patch 1 | `07-weil-explizitformel/NEU-250f_PATCH1_Typkorrektur_F3_Kochain_vs_Algebraelement.md` | `606428f74c215c1818efefc64522ad6c1e0774bf` | F1/F4-Korrekturquelle |
| NEU-250h | `07-weil-explizitformel/NEU-250h_Quellenabbildung_und_Testfunktionswert_im_primitiven_Weilkanal.md` | `0abda0bdf2f790928a8a8571543c41e97be8b834` | P05-Kern |
| NEU-250k | `07-weil-explizitformel/NEU-250k_Adelischer_Mediatorport_zwischen_von_Mangoldt_und_Mischsektor.md` | `01b484e01ede4df6f167ffec22f262f065d439f6` | P11-Weiterleitung |
| NEU-250l | `07-weil-explizitformel/NEU-250l_Streublock-Mediatoraudit_und_Entscheidung_J-A_J-B.md` | `27894d535389075a1d6dff6bdf4d24c3c003b032` | Mediator-Endanker |
| NEU-250m | `07-weil-explizitformel/NEU-250m_Praequotientaler_archimedischer_Port_auf_gemeinsamer_adelischer_Quelle.md` | `ecc1c3bd3aff2fda7a8aad4543cb09c01d1ea0b2` | späterer Quellen-/Port-Strang |
| NEU-250n | `07-weil-explizitformel/NEU-250n_Direktaudit_adelisch_archimedische_Quellbruecke_iota_infty.md` | `e0f2f70421a1c1245b70843113faa6fdcae60f4a` | K1-/Quellenkorrektur |
| NEU-250o | `07-weil-explizitformel/NEU-250o_Adelisch_archimedischer_Port_r_infty_W.md` | `18ebb2aaca2ed8edbf22fa713c9f128feb131e20` | Fehlerkorrektur Quellenport |
| NEU-250p | `07-weil-explizitformel/NEU-250p_Direktaudit_Halbgewichtstransfer_J12.md` | `56ba1f7df0592139147a1c6034d0a76b474f38fa` | archimedischer $J_{1/2}$-Audit; **nicht** BC-$h_n^{\rm bal}$ |
| NEU-250q | `07-weil-explizitformel/NEU-250q_Formdomaene_und_Hermitesche_Polarisation.md` | `4021fa2cb96d1d65dc350b12ecac5510f558b5ae` | Primzahlpotenz-Konvergenz-/Formdomänenkorrektur |
| NEU-250r | `07-weil-explizitformel/NEU-250r_Komplexer_Amplitudenport_und_Aufloesung_Realitaets-Firewall.md` | `bd1c0ab717e71bb3f25455a98f41b3fddeb249c9` | späterer Amplitudenport / M3-Weiterführung |

**Buchhaltungsregel:** Ein Repo-Check von F4, der nur `01-primkanten-werkzeuge/` durchsucht, ist unvollständig. Für F4 muss mindestens die oben fixierte Pfadliste aus `01-primkanten-werkzeuge/` **und** `07-weil-explizitformel/` geprüft werden.

### 0.2 Erster externer Gegencheck: als ungültig verworfen

Der erste unabhängige Repo-Check meldete, NEU-250h/k/l/n existierten nicht als Repo-Dateien und nach NEU-250j gebe es keine späteren `NEU-250*`-Knoten. Beide Aussagen sind durch die oben verifizierten `main`-Pfade direkt widerlegt.

Daher gilt:

$$
\boxed{\text{Gegencheck 1: INVALID-SCOPE — nicht als unabhängige F4-Verifikation zählen.}}
$$

Sein Befund, dass kein allgemeines BC-Lemma $h_n^{\rm bal}=n^{-1/2}I$ nachgewiesen wurde, stimmt mit dem Primäraudit überein, kann wegen des unvollständigen Suchraums aber **nicht** als repo-weite Bestätigung gewertet werden. Der nächste Gegencheck muss pfadgebunden erfolgen.

---

## 1. Prüfmatrix

| Knoten | Primäraudit | Endstatus für P05 | Heute gültiger Kernbefund |
|---|---|---|---|
| NEU-250f + Patch 1 | `TARGETED-REAUDIT` bereits F1 | `SUPERSEDED_part / CONDITIONAL` | Aus $L_3\in C^4(F^3A,F^3A)$ folgt nicht $L_3^\circ\in F^3A$. Korrekt bleibt nur: $L_{3,\rm alg}^\circ\in F^3A\Rightarrow \ell_{s,1}=0\Rightarrow P_{m=1}\widetilde T_p^{\rm raw}=0$ `✓[M]`. Existenz/Typisierung von $L_{3,\rm alg}^\circ$: `?[O]`. |
| NEU-250g | `TARGETED-REAUDIT` | `INCORPORATED_part` | Auf dem ausdrücklich behandelten primitiven Kanal $j_R=e_RV_p$ liefert die balancierte modulare Paarung algebraisch $h_p^{\rm bal}=p^{-1/2}I$ und mit $H_{\rm BC}j_R=(\log p)j_R$ den Faktor $\log p/\sqrt p$. Hilbert-Selbstadjungiertheit, Abschluss, Domäne und globaler Funktionalkalkül von $H_{\rm BC}$ bleiben offen. Der historische Satz „NEU-250f schließt den alten $L_3$-Pfad endgültig“ ist durch Patch 1 überholt. |
| NEU-250h | `AUDIT-RECONCILED` | `INCORPORATED_part` | H2 ist typkorrekt: $g_a(\log p)=\operatorname{Re}\langle a,U_{\log p}a\rangle$ und der primitive Weilterm ist $(\log p/\sqrt p)g_a(\log p)$. Die Firewall „Matrixkoeffizient, kein Normquadrat“ bleibt. H1 darf den 250g-Faktor nur im algebraischen/partiellen Sinn erben; H3 globale Faktorisierung bleibt `?[O]`. |
| NEU-250i | `TARGETED-REAUDIT` | `INCORPORATED_part / CONDITIONAL` | Die arithmetische Identität $\Lambda(p^m)/\sqrt{p^m}=\log p/p^{m/2}$ ist `✓[M]`. Die behauptete **operatorische Realisierung** über $h_{p^m}^{\rm bal}$ und $H_{\rm pr}=D_\Omega^{-1}H_{\rm BC}$ ist jedoch noch nicht unbedingter Satz: I1 schreibt NEU-250g die allgemeine Formel $h_n^{\rm bal}=n^{-1/2}I$ für alle $n$ zu, während NEU-250g die Rechnung explizit nur für $j_R=e_RV_p$ durchführt. Ein allgemeines $n$-Lemma bzw. eine direkte Quellenableitung fehlt. Zusätzlich bleibt der Hilbert-Funktionalkalkül von $H_{\rm BC}$ offen. Die Firewall $H_{\rm pr}\neq\Lambda$ auf Zahlen mit mehreren verschiedenen Primteilern bleibt gültig. |
| NEU-250j | `TARGETED-REAUDIT` | `INCORPORATED_part` + **→ P11** | J1–J3 bleiben bestehen: Kreuzprimkollision $pm_p=qm_q=M$ mit $p\neq q$ genau auf $\omega(M)\ge2$; dort $\Lambda(M)=0$; daher $\operatorname{supp}\Lambda\cap\operatorname{supp}(\text{Kreuzprimkollision})=\varnothing$ `✓[M]`. Das widerlegt die in F3 gesicherte nichtorthogonale Primkanalgeometrie nicht. Die pauschale Nebenbehauptung „$D_{\rm rel}$ hat keine Eigenwerte“ ist gegenüber F3 zu stark: NEU-225 beweist dies für die auditierten Primsektoren; zusammengesetzte $m$-Sektoren bleiben `[O-225-3]` offen. Für die Trägertrennung wird diese Nebenbehauptung nicht benötigt. J5 wird durch NEU-250k/l fortgeschrieben. |
| NEU-250k | `AUDIT-RECONCILED` | **→ P11** | Drei-Port-Architektur nur als Zieltyp. K1 wird durch NEU-250n auf `?[O]` korrigiert: $\mathcal S_{\rm adel}$ ist noch kein fertig konstruierter topologischer Quellenraum. $T_{\mathcal M}$ bleibt Kandidat `?[O]`; ein isolierter positiver Selbstterm $\|T_{\mathcal M}a\|^2$ ist als zusätzlicher Weilterm nicht zulässig; Gramblock-Grammatik ist Zieltyp, konkrete Realisierung offen. |
| NEU-250l | `AUDIT-REUSED` | **MEDIATOR-ENDANKER → P11** | Maßgeblicher späterer Endstand zur J-A/J-B-Frage: kein explizit typisierter $D_{\rm scatt,N}$ im Quellenstand; quotientengebundene Realisierung hängt am noch nicht konstruierten Wres-Quotienten; kanonische Mischsektorprojektion ist nicht konstruiert. Deshalb ist $P_{\mathcal M}D_{\rm scatt,N}\neq0$ aktuell nicht formulierbar. **J-B ist vorläufig aktiv als Quellenbefund, nicht als mathematischer Struktursatz.** Präquotientaler Weg über Kreuzspektralmaße bleibt `?[O]`. |
| NEU-250n | `AUDIT-REUSED` | Korrekturquelle → P11 | Korrigiert NEU-250k K1: $\mathcal S_{\rm adel}$ ist Architekturplatzhalter. Die adelisch-archimedische Brücke wird in einen lokalen typisierten Pfeil und einen offenen Quellenpfeil zerlegt. |

---

## 2. Isolierter Hauptkonflikt: 250g → 250i

NEU-250i beginnt mit

$$
\boxed{h_n^{\rm bal}=n^{-1/2}I\qquad(n\ge1)}
$$

und schreibt diese Aussage ausdrücklich „NEU-250g, Schritt G1“ zu.

Der aktuelle NEU-250g-Text führt G1 jedoch auf dem primitiven Kanal

$$
j_R=e_RV_p
$$

aus und erhält dort

$$
h_p^{\rm bal}=p^{-1/2}I.
$$

Im auditierten 250g-Text findet sich weder eine Definition $j_{R,n}$ noch ein Beweis der Generalisierung auf alle $n$. NEU-15 liefert zwar den allgemeinen diagonal gewichteten KMS/Frobenius-Hintergrund $\varepsilon_\beta(F)=\sum_m m^{-\beta}F_{m,m,0}$, ersetzt aber ohne zusätzliche Produkt-/Basisrechnung nicht automatisch das fehlende 250g-Lemma.

Daher gilt für Pass A:

$$
\boxed{h_p^{\rm bal}=p^{-1/2}I\quad\checkmark[M]_{\rm part}\ \text{(algebraischer primitiver Kanal)}}
$$

aber

$$
\boxed{h_n^{\rm bal}=n^{-1/2}I\quad\text{für alle }n\ge1\quad ?[O]\ \text{im aktuellen Beweiskegel}.}
$$

Das ist ein **Provenienz-/Beweisgap**, kein Gegenbeweis gegen die Formel. Ein kurzer allgemeiner $n$-Beweis könnte sie später schließen.

### Konsequenz für NEU-250i

Die rein zahlentheoretische Identität

$$
\boxed{\frac{\Lambda(p^m)}{\sqrt{p^m}}=\frac{\log p}{p^{m/2}}}\qquad\checkmark[M]
$$

bleibt selbstverständlich vollständig gültig.

Nicht vollständig bewiesen ist im aktuellen Quellenkegel die stärkere Realisierungsaussage

$$
h_{p^m}^{\rm bal}\!\left(H_{\rm pr}^{1/2}E_R,H_{\rm pr}^{1/2}E_{R'}\right)
=\frac{\log p}{p^{m/2}}\delta_{RR'}
$$

als **unbedingte Hilbertraum-/Operatoraussage**. Sie ist gegenwärtig konditional auf:

1. die allgemeine Halbgewichtungsformel $h_n^{\rm bal}=n^{-1/2}I$ auf den benötigten $p^m$-Sektoren,
2. eine typkorrekte Realisierung von $H_{\rm BC}$ / $H_{\rm pr}$ samt Quadratwurzel auf dem verwendeten Raum.

---

## 3. NEU-250j gegen F3

Die starke Aussage von NEU-250j ist **nicht** „Kreuzterme existieren nicht“, sondern:

$$
\boxed{\operatorname{supp}\Lambda\cap\operatorname{supp}(\text{Kreuzprimkollision})=\varnothing.}
$$

F3/NEU-226–227 bleibt davon unberührt:

- verschiedene Primkanalbilder können generisch nichtorthogonal überlappen,
- Primblockdiagonalität ist nicht strukturell erzwungen,
- das Koordinatenwörterbuch $\eta_{p;m;s,u}\leftrightarrow e_RV_M$ bleibt verbindlich.

Die Kombination lautet:

$$
\boxed{\text{Nichtorthogonale Primkanalgeometrie existiert, aber ihre direkte Kreuzprimkollision trägt keinen Mangoldt-Selbstterm.}}
$$

Das ist ein strukturell wichtiger **No-Go für die direkte Identifikation**, kein No-Go gegen globale Kopplung überhaupt.

### Spektral-Firewall

NEU-250j beruft sich pauschal auf „$D_{\rm rel}$ hat keine Eigenwerte“. Nach F3 ist nur die diskrete Eigenbasisdarstellung aus NEU-51 vollständig superseded; die Primfaserdiagonalisierung von NEU-225 beweist rein absolutstetiges Spektrum in den auditierten Primsektoren. Für zusammengesetzte $m$-Sektoren führt NEU-225 `[O-225-3]` ausdrücklich als offen.

Daher darf P05 keine globale Aussage „$D_{\rm rel}$ hat auf sämtlichen Mischsektoren keine Eigenwerte“ aus NEU-250j übernehmen.

---

## 4. Mediator-Endstand: 250j → 250k → 250l → 250n

NEU-250j endet mit offenem Mediatorweg. NEU-250k konkretisiert die gewünschte Drei-Port-Grammatik, konstruiert aber $T_{\mathcal M}$ nicht. NEU-250l auditiert den naheliegenden Streublockweg und findet:

1. $D_{\rm scatt,N}$ besitzt im Quellenstand keine explizite Raum-/Typdefinition — `✓[M]_{neg}` als Quellenbefund.
2. Eine quotientengebundene Version hängt am noch nicht konstruierten Wres-Quotienten.
3. Eine kanonische Projektion $P_{\mathcal M}$ ist in der nichtorthogonalen Geometrie nicht konstruiert.
4. Deshalb ist $P_{\mathcal M}D_{\rm scatt,N}\neq0$ aktuell nicht typkorrekt formulierbar.

Der Endstatus ist somit:

$$
\boxed{\text{J-B vorläufig aktiv als Quellenbefund; J-A mathematisch offen.}}
$$

Das ist **kein** Beweis, dass ein Mischsektormediator unmöglich ist. Ein präquotientaler Kandidat aus Kreuzspektralmaßen bleibt offen und gehört nach P11.

NEU-250n verschärft zusätzlich die Quellenfirewall: $\mathcal S_{\rm adel}$ ist selbst noch Architekturplatzhalter; eine vollständige gemeinsame topologische Quelle ist nicht konstruiert.

Der spätere Scan NEU-250o–r verändert diesen Mediator-Endstatus nicht. Er korrigiert und typisiert vor allem den adelisch-archimedischen Quellen-/Amplitudenport. Insbesondere NEU-250p betrifft $J_{1/2}$ auf dem archimedischen Testfunktionsweg und liefert **keinen** Ersatzbeweis für das BC-Lemma $h_n^{\rm bal}=n^{-1/2}I$.

---

## 5. Verbindliche F4-Firewalls nach Primäraudit

11. **Trägertrennung ≠ Orthogonalitäts-No-Go.** NEU-250j widerlegt nicht die generische Nichtorthogonalität aus NEU-226/227; es trennt den Mangoldt-Träger von der direkten Kreuzprimkollision.
12. **Arithmetische Identität ≠ Operatorrealisierung.** $\Lambda(p^m)/\sqrt{p^m}=\log p/p^{m/2}$ ist `✓[M]`; die Realisierung über $h_{p^m}^{\rm bal}$ und $H_{\rm pr}^{1/2}$ bleibt bis zum allgemeinen $n$-Lemma und zur Hilbert-Fundierung konditional.
13. **250g bleibt primitiver Kanal.** $h_p^{\rm bal}=p^{-1/2}I$ und $\log p/\sqrt p$ dürfen nicht ohne Beweis zu $h_n^{\rm bal}=n^{-1/2}I$ für alle $n$ hochgestuft werden.
14. **250h-Matrixkoeffizient ist kein Normquadrat.** $g_a(x)=\operatorname{Re}\langle a,U_xa\rangle$ kann negativ oder null sein; kein lokaler positiver Gramterm folgt daraus.
15. **Keine globale Eigenwertbehauptung aus 250j.** Primsektoren: a.c.-Spektrum / keine Eigenwerte `✓[M]`; zusammengesetzte $m$-Sektoren bleiben gemäß `[O-225-3]` offen.
16. **Mediatorstatus:** NEU-250l ist Endanker. J-B ist `✓[M]_{neg,prov}` (Quellenbefund), nicht `✓[M]_{neg}` als struktureller Unmöglichkeitssatz; J-A bleibt `?[O]` und wird nach P11 weitergereicht.
17. **Gemeinsame Quelle:** $\mathcal S_{\rm adel}$ nicht als fertig konstruierter topologischer Raum behaupten; NEU-250n korrigiert K1 auf `?[O]`.
18. **Ordnerübergreifende Provenienz:** F4 darf nicht aus `01-primkanten-werkzeuge/` allein auditiert werden. Die Korrektur-/Endstandkette in `07-weil-explizitformel/NEU-250h…r` ist zwingend mitzulesen.

---

## 6. P05-Endstand aus F4 nach Primäraudit

### Darf nach P05 übernommen werden

- primitiver algebraischer Weilfaktor
  $$\frac{\log p}{\sqrt p}$$
  aus der balancierten modularen Paarung: `✓[M]_{part}`;
- typkorrekter Testfunktionsfaktor
  $$g_a(\log p)=\operatorname{Re}\langle a,U_{\log p}a\rangle$$
  und seine Einbettung in den primitiven Weilterm: `✓[M]`;
- arithmetische Primzahlpotenzidentität
  $$\frac{\Lambda(p^m)}{\sqrt{p^m}}=\frac{\log p}{p^{m/2}}$$
  `✓[M]`;
- Trägertrennung direkte Kreuzprimkollision vs. Mangoldt-Träger: `✓[M]`;
- Firewall, dass nichtorthogonale Primkanalgeometrie dadurch **nicht** widerlegt wird.

### Nur konditional / offen in P05

- allgemeine BC-Halbgewichtung $h_n^{\rm bal}=n^{-1/2}I$ für alle $n$;
- vollständige operatorische Realisierung des Primzahlpotenzfaktors über $H_{\rm pr}^{1/2}$;
- Hilbert-Selbstadjungiertheit / Abschluss / globaler Funktionalkalkül von $H_{\rm BC}$ und $H_{\rm pr}$.

### Weiterleitung

- Feshbach-/Spektralmaß-/Schattenklassenanteile → **P06**;
- Mischsektormediator, gemeinsame adelische Quelle, Gramblock-Kopplung und J-A/J-B → **P11**.

---

## 7. F4-Primärurteil

$$
\boxed{\text{F4 PRIMARY AUDIT COMPLETE — mit zwei epistemischen Rückstufungen und erweitertem Scope.}}
$$

Die zwei zentralen Rückstufungen sind:

1. **NEU-250i:** vollständige operatorische Primzahlpotenzrealisierung von `✓[M]` auf `CONDITIONAL / INCORPORATED_part`, bis das allgemeine $n$-Halbgewichtslemma und der Operator-Funktionalkalkül belegt sind.
2. **NEU-250j:** pauschale globale „keine Eigenwerte“-Nebenbehauptung wird nicht übernommen; nur die auditierten Primsektoren sind gesichert. Die Trägertrennung selbst bleibt `✓[M]`.

**Gegencheck 1:** `INVALID-SCOPE` — wegen der falschen Behauptung, NEU-250h/k/l/n und spätere 250-Knoten existierten nicht im Repo; zählt nicht als Zweitprüfung.

**Noch ausständig vor `F4 PASS A COMPLETE`:** ein **pfadgebundener unabhängiger Gegencheck** dieses Auditblatts. Er muss die in §0.1 fixierten Dateien direkt lesen und nur zwei Sachfragen prüfen:

1. Existiert in `01-primkanten-werkzeuge/NEU-250g…j` oder `07-weil-explizitformel/NEU-250h…r` ein tatsächlicher Beweis des allgemeinen BC-Lemmas $h_n^{\rm bal}=n^{-1/2}I$ für alle $n\ge1$?
2. Gibt es in derselben expliziten Kette eine spätere Aussage, die den Mediator-Endstatus von NEU-250l oder die Spektral-Firewall zu NEU-250j mathematisch superseded?

Ohne konkreten Quellfund bleibt der Primäraudit-Endstand unverändert.