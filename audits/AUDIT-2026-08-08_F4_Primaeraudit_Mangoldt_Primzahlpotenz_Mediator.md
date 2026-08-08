# F4-Primäraudit — Mangoldt-/Primzahlpotenzstrang und Mediatorstatus

**Datum:** 8. August 2026  
**SYN-Ziel:** P05 — Relative Prime Channels and Arithmetic Edge Geometry  
**Prüfart:** `TARGETED-REAUDIT` / `AUDIT-RECONCILED`  
**Verfahren:** mathematischer Primäraudit; unabhängiger Repo-/Konsistenzcheck noch ausständig  
**Status dieses Auditblatts:** Primäraudit abgeschlossen; **F4 noch nicht `PASS A COMPLETE`** bis Gegenprüfung erfolgt

---

## 0. Scope-Korrektur

Die ursprüngliche F4-Inventarliste `NEU-250g/i/j` war unvollständig. Für den heute gültigen Endstand müssen mindestens folgende Knoten gemeinsam gelesen werden:

- NEU-250f + Patch 1 (`1579a379`) — Typkorrektur des Filtrations-No-Go,
- NEU-250g — modulare Halbgewichtung im primitiven $p$-Kanal,
- NEU-250h — Testfunktionswert / Matrixkoeffizient,
- NEU-250i — Primzahlpotenzsektor und gradnormierte BC-Energie,
- NEU-250j — Trägertrennung Mangoldt vs. Kreuzprimkollision,
- NEU-250k — adelischer Mediatorport,
- NEU-250l — Streublock-Mediatoraudit, Entscheidung J-A/J-B,
- NEU-250n — spätere Korrektur zu K1: $\mathcal S_{\rm adel}$ ist Architekturplatzhalter, kein fertig konstruierter topologischer Quellenraum.

NEU-250p auditiert den **archimedischen** Halbgewichtstransfer $J_{1/2}$; er repariert nicht die unten isolierte BC-Generalisation $h_p^{\rm bal}\to h_n^{\rm bal}$ und ist daher kein Endanker dieses lokalen F4-Punktes.

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

---

## 5. Verbindliche F4-Firewalls nach Primäraudit

11. **Trägertrennung ≠ Orthogonalitäts-No-Go.** NEU-250j widerlegt nicht die generische Nichtorthogonalität aus NEU-226/227; es trennt den Mangoldt-Träger von der direkten Kreuzprimkollision.
12. **Arithmetische Identität ≠ Operatorrealisierung.** $\Lambda(p^m)/\sqrt{p^m}=\log p/p^{m/2}$ ist `✓[M]`; die Realisierung über $h_{p^m}^{\rm bal}$ und $H_{\rm pr}^{1/2}$ bleibt bis zum allgemeinen $n$-Lemma und zur Hilbert-Fundierung konditional.
13. **250g bleibt primitiver Kanal.** $h_p^{\rm bal}=p^{-1/2}I$ und $\log p/\sqrt p$ dürfen nicht ohne Beweis zu $h_n^{\rm bal}=n^{-1/2}I$ für alle $n$ hochgestuft werden.
14. **250h-Matrixkoeffizient ist kein Normquadrat.** $g_a(x)=\operatorname{Re}\langle a,U_xa\rangle$ kann negativ oder null sein; kein lokaler positiver Gramterm folgt daraus.
15. **Keine globale Eigenwertbehauptung aus 250j.** Primsektoren: a.c.-Spektrum / keine Eigenwerte `✓[M]`; zusammengesetzte $m$-Sektoren bleiben gemäß `[O-225-3]` offen.
16. **Mediatorstatus:** NEU-250l ist Endanker. J-B ist `✓[M]_{neg,prov}` (Quellenbefund), nicht `✓[M]_{neg}` als struktureller Unmöglichkeitssatz; J-A bleibt `?[O]` und wird nach P11 weitergereicht.
17. **Gemeinsame Quelle:** $\mathcal S_{\rm adel}$ nicht als fertig konstruierter topologischer Raum behaupten; NEU-250n korrigiert K1 auf `?[O]`.

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

**Noch ausständig vor `F4 PASS A COMPLETE`:** unabhängiger repo-weiter Gegencheck dieses Auditblatts, insbesondere auf spätere Korrekturen/Superseding-Knoten zu NEU-250g–n und auf einen eventuell bereits vorhandenen allgemeinen $n$-Beweis für $h_n^{\rm bal}=n^{-1/2}I$.
