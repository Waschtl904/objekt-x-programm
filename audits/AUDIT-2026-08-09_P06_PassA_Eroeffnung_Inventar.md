# P06 Pass-A — Eröffnung, Inventar und Prüfartmatrix

**Datum:** 9. August 2026  
**SYN-Ziel:** P06 — Jacobi–Feshbach + Divisorgraph  
**Status:** **P06 PASS A OPEN — INVENTAR COMPLETE; TARGETED-REAUDITS ausständig**  
**Verfahren:** Audit-Reuse zuerst; Reconciliation gegen spätere Korrekturknoten; kein SYN-Transfer vor Abschluss der gezielten Konfliktprüfungen.

---

## 0. Eröffnungsurteil

Der historische Ordner `02-jacobi-limes/` umfasst exakt **33 Forschungsknoten, NEU-058 bis NEU-090**. Dieser Block wurde im früheren Gesamtdurchlauf bereits vollständig ausgewertet; die Juli-Zwischenbilanz und die spätere Aktiv-Bilanz enthalten einen konsolidierten Ordner-02-Endstand.

Daraus folgt für P06:

$$
\boxed{\text{Für NEU-058–090 ist kein NEW-DIRECT-AUDIT erforderlich.}}
$$

Die Pass-A-Arbeit besteht aus maximaler Wiederverwendung des bestehenden Auditbestands und gezielten Reaudits nur dort, wo spätere Knoten einen konkreten Konflikt erzeugen.

Vier solche Konfliktstellen sind vorläufig isoliert:

$$
\boxed{\text{NEU-050, NEU-062, NEU-066, NEU-090.}}
$$

Keine P06-SYN-Zeile wird vor deren Abschluss geschrieben.

---

## 1. Auditbestand und heutiger Ordner-02-Endstand

Verbindliche Reuse-Quellen:

- `ZWISCHENBILANZ_2026-07-29.md`: vollständige Auswertung der Ordner 00–03;
- `ZWISCHENBILANZ_2026-08-01.md`: kanonische Aktiv-Bilanz;
- spätere Korrekturschicht NEU-223–228;
- für NEU-225–227 der bereits doppelt geprüfte F3-Endstand aus `PASS-A-PROTOKOLL.md`;
- P05-Firewalls und P05-Routing, Status `SYN FROZEN ✓[K/M]`.

Der heute gültige historische Ordner-02-Befund lautet konservativ:

1. Der direkte Jacobi-Limes als kanonischer Endoperator ist durch NEU-223–225 überholt.
2. Reine Vorwärtsshiftmodelle sind für Spur/Determinante zu trivial; die Jacobi-Schließung benötigt Rückwärtskanten.
3. Die relative Determinanten-/Schleifenschicht ist ein mathematisch kontrollierter Modellstrang, aber kein direkter $\xi$-Anschluss.
4. Der starke Mangoldt-Limes auf festen Vektoren kollabiert; wandernde Fenster und Orbittrunkierung ändern die Frage, lösen sie aber nicht automatisch.
5. Die alte NEU-090-Konstante $\gamma^2/2$ ist gegenüber dem korrigierten Skalenaudit nicht als heutiger Endstand zu übernehmen.

---

## 2. Paketstruktur Gruppe G / P06

### G1 — Jacobi-Limes, Weyl-/Stieltjes- und Determinantenarchitektur

NEU-058–065.

### G2 — Divisorgraph, primitive Orbits, BC-Zeit und Symbolstruktur

NEU-066–076.

### G3 — Endliche Feshbach-Kollapsidentität und Skalierungskonflikte

NEU-077–083.

### G4 — Orbittrunkierung, Null-Limes, Jacobi-Schließung und Schleifendeterminanten

NEU-084–090.

### GX1 — Historische Feshbach-Brücke aus Ordner 01

NEU-040, NEU-045, NEU-046–056.

### GX2 — Superseding-/Korrekturschicht

NEU-223–228.

### P06/P11-Firewall

NEU-228b und NEU-229 werden in P06 nur als **Blocker-/Interfaceknoten** registriert. Die intrinsische verbundene Liftform, der Mischblock $\beta_p$ und die globale Gramgeometrie gehören nach P11. P06 darf aus diesen offenen Strukturen keine Schatten- oder Determinantenaussage ableiten.

---

## 3. Prüfartmatrix NEU-058–090

| Knoten | Prüfart für P06 | Begründung / heutige Rolle |
|---|---|---|
| NEU-058 | `AUDIT-REUSED` | Skalenbilanz/Normresolvent-No-Go bereits ausgewertet; direkter Jacobi-Pfad später überholt |
| NEU-059 | `AUDIT-RECONCILED` | Spektralmaßtopologie abstrakt brauchbar; direkte Grenzoperatorarchitektur gegen NEU-223–225 lesen |
| NEU-060 | `AUDIT-RECONCILED` | Core-/Resolventenlemma nur unter sauberer Grenzoperatorvoraussetzung übernehmen |
| NEU-061 | `AUDIT-RECONCILED` | lokale Matrixstabilisierung als technischer Baustein; keine automatische globale Konvergenz |
| **NEU-062** | **`TARGETED-REAUDIT`** | historische $\gamma_N\equiv1$-Empfehlung und $\frac1{2i}(\Theta-\Theta^{Wres})$ kollidieren mit späterer J-/S-Konventionsbereinigung aus NEU-225 |
| NEU-063 | `AUDIT-RECONCILED` | Herglotz-/Weyl-Struktur nur typisiert/regularisiert; arithmetische Identifikation offen |
| NEU-064 | `AUDIT-RECONCILED` | endliche Weyl-/Kettenbruchstruktur brauchbar; $\xi$-Identifikation nicht automatisch |
| NEU-065 | `AUDIT-RECONCILED` | Logdet-/Hurwitz-Mechanismus abstrakt; Hypothese $Z_N\to C\xi$ bleibt äquivalent-naher Hauptengpass `?[O]` |
| **NEU-066** | **`TARGETED-REAUDIT`** | Trace-/Divisorpfadformeln müssen gegen spätere Antisymmetrisierungs-, Graph- und Spektralmaßkorrekturen reconciliert werden |
| NEU-067 | `AUDIT-REUSED` | primitive Orbit-/Mangoldt-Reduktion |
| NEU-068 | `AUDIT-REUSED` | Möbius-/primitive Mangoldt-Identität |
| NEU-069 | `AUDIT-REUSED` | primitive Zykluszerlegung; nur im gültigen Graphscope |
| NEU-070 | `AUDIT-REUSED` | Nicht-Backtracking-/Ihara-No-Gos bereits erfasst |
| NEU-071 | `AUDIT-REUSED` | Quotientierungs-/Periodisierungs-No-Gos bereits erfasst |
| NEU-072 | `AUDIT-REUSED` | BC-Zeit/$\log p$ strukturell relevant; BC-Typfundament ggf. → P09 |
| NEU-073 | `AUDIT-RECONCILED` | $\Theta$-Matrix und BC-Derivation strikt von $J^-$ unterscheiden |
| NEU-074 | `AUDIT-REUSED` | partielle BC-Isometrie-Identifikation; historische No-Go-Grenzen erhalten |
| NEU-075 | `AUDIT-RECONCILED` | Faktorisierung auf $\Theta$-Ebene, nicht automatisch auf antisymmetrischem $J^-$ |
| NEU-076 | `AUDIT-RECONCILED` | Faser-Symbol-No-Go bleibt lokal; Feshbach-Transfer ist andere Schicht |
| NEU-077 | `AUDIT-RECONCILED` | endliche Feshbach-Kollapsidentität gültig; globaler Limes nur punktweise, keine Schattennormkontrolle |
| NEU-078 | `AUDIT-RECONCILED` | Normierungs-No-Go im historischen Scaling; spätere Transport-/Hebungsfirewalls beachten |
| NEU-079 | `AUDIT-RECONCILED` | Kanalzahl-Skalierung nur innerhalb historischem Modell |
| NEU-080 | `AUDIT-RECONCILED` | effektive Jacobi-Skalierung nicht als heutige intrinsische Normalisierung übernehmen |
| NEU-081 | `AUDIT-REUSED` | Feshbach-vs.-Jacobi-Gewichtsstabilität offen/diagnostisch |
| NEU-082 | `AUDIT-REUSED` | kanalabhängige Kopplung/Dichtebedingung offen |
| NEU-083 | `AUDIT-REUSED` | Dreifach-Konflikt Feshbach + Jacobi-Stabilität + Mangoldt auf vollem Fenster gesichert; Auswege offen |
| NEU-084 | `AUDIT-REUSED` | korrekte Trennung pathwise $N/\log N$ vs. operatorische Zeilennormskala $\sqrt{N/\log N}$ |
| NEU-085 | `AUDIT-REUSED` | starker Null-Limes / wandernde Fenster |
| NEU-086 | `AUDIT-REUSED` | Nilpotenzbarriere für reinen Vorwärtsshift |
| NEU-087 | `AUDIT-REUSED` | Jacobi-Schließung bricht Nilpotenz; erste Schleifen quadratisch |
| NEU-088 | `AUDIT-RECONCILED` | relative Resolventdeterminante/formale zweite Schleifenspur; Skalenscope explizit halten |
| NEU-089 | `AUDIT-RECONCILED` | höhere Schleifen/asymptotische Quadratisierung konditional auf Schur-/Diagonalskala |
| **NEU-090** | **`TARGETED-REAUDIT`** | historische $T_N(z)\to\gamma^2/2$-Behauptung widerspricht korrigiertem Skalenaudit; $z$-Rigiditäts-/Determinantenfolge neu reconciliieren |

$$
\boxed{\text{33/33 Knoten inventarisiert; 0 NEW-DIRECT-AUDIT; 3 TARGETED-REAUDIT in Ordner 02.}}
$$

---

## 4. Prüfartmatrix der ordnerübergreifenden P06-Provenienz

| Knoten | Prüfart / Routing | Heute gültige Rolle |
|---|---|---|
| NEU-040 | `AUDIT-REUSED` (F1) | formale Schur-Komplementidentität; intrinsischer Wres-Koppler/$z$–$\beta$-Intertwining offen |
| NEU-045 | `AUDIT-REUSED` (F1) | Euler-Unterdeterminante gültig; intrinsische Feshbach-Geometrie offen |
| NEU-046 | `AUDIT-RECONCILED` | zyklische Weyl-Funktion $M_p(z)$ formal; konkrete intrinsische Kopplungsvektoren bleiben liftabhängig |
| NEU-047 | `AUDIT-RECONCILED / CONTEXT-ONLY` | Hadamard-/archimedische Separation; Detailrouting später P10/P12 |
| NEU-048 | `AUDIT-RECONCILED / CONTEXT-ONLY` | Divisor-/Residuenneutralität; keine automatische globale $\xi$-Identität |
| NEU-049 | `AUDIT-RECONCILED` | Fredholmindex formal unter Spurklasse; Nichtüberzählung und Nullstellenmultiplizität offen |
| **NEU-050** | **`TARGETED-REAUDIT`** | kollektive Birman–Schwinger-Architektur relevant; universelle Lesart der Off-Diagonalblöcke gegen F3 korrigieren |
| NEU-051 | `AUDIT-RECONCILED / SUPERSEDED_part` | (51.3)/(51.4)/(51.7) in diskreter Eigenbasis superseded; Schattenkriterium nur in typkorrekter Form übernehmen |
| NEU-052 | `AUDIT-RECONCILED` | Graphbasis ≠ Eigenbasis; Spektralsatz bleibt |
| NEU-053 | `AUDIT-RECONCILED` | Operator-/Spektralmaßrahmen; später durch 223–225 typisiert |
| NEU-054 | `AUDIT-RECONCILED` | Nelson vs. Konfinement strikt trennen |
| NEU-055 | `AUDIT-RECONCILED` | Matrix-/Schurabschätzungen; Grenzbedingungen nicht pauschal als unbedingte SA lesen |
| NEU-056 | `AUDIT-RECONCILED` | skalare $\gamma_N$-Konfinementroute scheitert; Weg B Spektralmaß robust; spätere Transportdiagnose supersediert die Hoffnung auf Konfinierung von $D_{rel}$ |
| NEU-223 | `AUDIT-REUSED` | Quellenaudit 52–56; Vergleichsoperatorfrage auf Graphnorm-/Spektralfrage reduziert |
| NEU-224 | `AUDIT-REUSED` | Antisymmetrisierungs-/Kernkorrektur; alte effektive-Raum-Abkürzungen nicht übernehmen |
| NEU-225 | `AUDIT-REUSED` (F3 sealed) | $D_{rel}$ als Transportgenerator in auditierten Primfasern; Feshbach $K(z)$ nur Arbeitshypothese |
| NEU-226 | `AUDIT-REUSED` (F3 sealed) | festes $N$ nicht endlich-rangig; Kanalüberlappung; alte Eigenbasisformeln ungültig; Limes nicht Schattennorm-kontrolliert |
| NEU-227 | `AUDIT-REUSED` (F3 sealed) | Koordinatenwörterbuch und projektionswertige Kreuzspektralmaßform verbindlich |
| NEU-228 | `AUDIT-RECONCILED / BLOCKER` | $u$-Regulator = Hebungswahl; nicht frei; kanonischer $u=0$-Projektor vernichtet Kopplung |
| NEU-228b | `INTERFACE / BLOCKER → P11` | Gram-/Liftfaser partiell typisiert; ausdrücklicher Sperrvermerk gegen Schattenrechnung vor Liftklärung |
| NEU-229 | `ROUTE-OUT → P11` | intrinsischer Mischblock $\beta_p$ im Quellenbestand fehlt; kein globaler Unmöglichkeitssatz; Feshbach-Wohldefiniertheit bis Liftabstieg gesperrt |

Damit besitzt P06 insgesamt **vier** gezielte Reaudit-Punkte:

$$
\boxed{\text{NEU-050, NEU-062, NEU-066, NEU-090.}}
$$

---

## 5. Verbindliche P06-Firewalls aus früheren Audits

1. **Kein direkter Jacobi-Endoperator aus der historischen Trunkierungskette.** NEU-223–225 superseden die alte Konfinierungs-/HP-Lesart.
2. **Transport ≠ Hilbert–Pólya.** In den auditierten Primfasern ist $D_{rel}$ ein Transport-/Streugenerator; kompakter reduzierter Resolvent dort ausgeschlossen. Objekt X insgesamt wird dadurch nicht ausgeschlossen.
3. **J-/S-Konvention:**
   $$J_N^-:=\tfrac12(\Theta_N-\Theta_N^\dagger),\qquad S_N:=\tfrac1{2i}(\Theta_N-\Theta_N^\dagger)=-iJ_N^-.$$
   Historische Gleichsetzungen sind zu korrigieren.
4. **Spektralmaß statt diskreter Eigenbasis.** Die historische diskrete Darstellung (51.3)/(51.4)/(51.7) ist durch NEU-227 zu ersetzen:
   $$\mu_{pq}^{a,b}(B)=\langle V_pa,E_D(B)V_qb\rangle,$$
   $$\langle a,K_{pq}(z)b\rangle=\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.$$
5. **Off-Diagonalität nur generisch/non-forced.** Primkanalbilder können überlappen; daraus folgt nicht $K_{pq}\neq0$ für jedes $p\neq q$. Der Mechanismus ist Kanalbildüberlappung, nicht Primmischung durch $D_{rel}$.
6. **Festes $N$ ≠ endlicher Rang.** Jeder Primkanal trägt einen unendlichdimensionalen internen Quellindex; $K_N$ ist nicht durch $\pi(N)$ im Rang beschränkt.
7. **Schattenklasse nicht aus Trunkierungen erben.** NEU-77 liefert endliche Identität, aber keinen Schattennorm-kontrollierten globalen Limes. $V\notin\mathcal S_2$ ist nur notwendig für den vorgeschlagenen Nicht-$\mathcal S_1$-Zeugen; $V\in\mathcal S_4$ bleibt Arbeitshypothese.
8. **Der $u$-Regulator ist kein freier Tuningparameter.** NEU-228 identifiziert ihn mit der Hebungswahl auf der affinen Primfaser.
9. **Lift-/Gramblockade vor Schattenrechnung.** NEU-228b/229 sperren intrinsische Feshbach-/Schattenaussagen bis zur wohldefinierten Lift-/Mischblockgeometrie. P06 registriert den Blocker; die Konstruktion selbst → P11.
10. **Zusammengesetzte Sektoren offen.** `[O-225-3]` bleibt `?[O]`; Mehrfachsprünge können $u$-Klassen mischen.
11. **Feshbach-Determinante ≠ $\xi$ bewiesen.** $Z_N\to C\xi$, charakteristische Werte bei Zetastellen und passende Fredholmdivisoren bleiben `?[O]`/`CONDITIONAL`.
12. **NEU-090 nicht unbesehen übernehmen.** Die historische Konstante $\gamma^2/2$ und daraus folgende konstante Determinante müssen gegen die korrigierte Orbit-/Operator-Skala reauditert werden.

---

## 6. Vier gezielte Reaudit-Aufträge

### G-T1 — NEU-050

Prüfe ausschließlich:
- welche Teile der kollektiven Birman–Schwinger-Architektur formal gültig bleiben;
- ob $\mathcal K_N=(K_{pq})$ nur als nicht blockdiagonal erzwungene Architektur oder fälschlich als universell off-diagonal formuliert wurde;
- trenne strukturelle Definition von offenen Divisor-/Nullstellenbehauptungen;
- reconcile mit F3-Korrektur: **generisch/non-forced**, nicht $K_{pq}\neq0$ für jedes $p\neq q$.

### G-T2 — NEU-062

Prüfe ausschließlich:
- historische Normalisierung $\gamma_N$;
- Verwendung von $\frac1{2i}(\Theta-\Theta^{Wres})$;
- Behauptung, Weg B sei mit $\gamma_N\equiv1$ analytisch vollständig;
- reconcile mit NEU-225-Konvention $J^- = \frac12(\Theta-\Theta^\dagger)$ und $S=-iJ^-$ sowie späterem Transportbefund.

### G-T3 — NEU-066

Prüfe ausschließlich:
- geschlossene Divisorpfad-/Traceformeln;
- welche Aussagen nur für das historische endliche Jacobi-Modell gelten;
- welche bipartiten/Grading-/Antisymmetrisierungsannahmen später korrigiert wurden;
- keine Übertragung einer diskreten $D_{rel}$-Eigenbasis in den heutigen P06-Stand.

### G-T4 — NEU-090

Prüfe ausschließlich:
- zweite Schleifenspur unter der **korrekten** Orbit-/Operator-Skala;
- ob $T_N(z)\to\gamma^2/2$ haltbar ist;
- Folgen für $z$-Rigidität und $D_N(z)$;
- historische No-Go-Aussage nur in dem Umfang übernehmen, den die korrigierte Rechnung tatsächlich trägt.

**Ausführungsreihenfolge:**

$$
\boxed{\text{NEU-050} \to \text{NEU-062} \to \text{NEU-066} \to \text{NEU-090}.}
$$

---

## 7. Routinggrenze P06 ↔ P11

P06 übernimmt die operatorisch/spektrale Transfersprache:

- Schur-/Feshbach-Komplement,
- zyklische Weyl-/Stieltjesfunktionen,
- $K_{pq}(z)$ und Kreuzspektralmaße,
- Birman–Schwinger-/Fredholmarchitektur,
- Schattenkriterien,
- Divisorgraph-/Schleifenanalyse,
- `[O-225-3]` als offenes Spektralproblem.

P11 übernimmt die intrinsische globale Kopplungsgeometrie:

- Liftunabhängigkeit und gemeinsamer Quellhilbertraum,
- Gramoperator der Primkanalbilder,
- intrinsischer Mischblock $\beta_p$,
- nichtorthogonale globale Gramkopplung,
- Mediator und globale Weil-/Objekt-X-Geometrie.

Die Schnittstelle ist bewusst asymmetrisch:

$$
\boxed{\text{P06 darf die offene P11-Quellgeometrie als Blocker referenzieren, aber nicht voraussetzen.}}
$$

---

## 8. Eröffnungsstatus

$$
\boxed{\text{P06 PASS A OPEN — INVENTAR COMPLETE.}}
$$

- 33/33 Knoten NEU-058–090 inventarisiert.
- Historische Brücke NEU-040/045/046–056 ergänzt.
- Superseding-Schicht NEU-223–228 gebucht.
- NEU-228b/229 als P06/P11-Blocker geroutet.
- `NEW-DIRECT-AUDIT`: **0**.
- `TARGETED-REAUDIT`: **4** — NEU-050, 062, 066, 090.
- P06-SYN: **gesperrt bis Abschluss der vier Targeted-Reaudits, Reconciliation und unabhängigem Gegencheck.**
