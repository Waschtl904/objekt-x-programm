# P11 — Pass-A Opening Audit: Source-First Global Coupling

**Datum:** 9. August 2026  
**Zielblock:** P11 — Global Coupling and the Object-X Candidate Geometry  
**Status:** **PASS-A OPEN — konstruktive Quellenreconciliation, noch kein P11-SYN**  
**Primärquellen:** P02, P03, P05, P10 (frozen), NEU-229/230 (Objekt-X-Arbeitsdefinition), NEU-250 `[O-220-1f0]` (globale Archimedes–Prim-Kopplung)  

> **Leitregel aus P10:** Kein lokaler oder modellgebundener No-Go darf zu einem universellen Existenz-No-Go gegen Objekt X hochgestuft werden. `OPEN`/`CONDITIONAL` bleibt offen.

---

## 0. Eröffnungsurteil

Die zentrale P11-Frage wird **nicht** als freie Wahl paarweiser Mischblöcke

\[
B_{pq},\qquad p\neq q,
\]

eröffnet.

Der nach P05–P10 zulässige konstruktive Typ ist vielmehr:

\[
\boxed{
\text{gemeinsame Quelle}
\longrightarrow
\text{kanonische lokale Analyseabbildungen}
\longrightarrow
\text{gemeinsames globales Bild}
\longrightarrow
\text{abgeleitete Gram-/Überlappungsblöcke }B_{vw}.
}
\]

Damit wird `B_{pq}` von einem **freien Konstruktionsdatum** zu einem **abgeleiteten Datum** herabgestuft.

Das ist noch keine Konstruktion von Objekt X. Es ist eine Typentscheidung darüber, wie eine nichtzirkuläre globale Kopplung überhaupt aussehen darf.

---

## 1. Bindende positive Ausgangsdaten

### 1.1 P02 — gemeinsame adelische Amplitudenquelle und RH-freie Weilform

P02 liefert RH-frei den surjektiven Port

\[
R_{\rm PW}:\mathcal S_{\rm adel}^{\rm amp}\twoheadrightarrow
\mathcal A_{\rm PW}=C_c^\infty(\mathbb R;\mathbb C),
\]

die sesquilineare Evenisierung `(a,b) -> g_{a,b}`, den Weil-Testkern `h_{a,b}` und die vollständige hermitesche Form

\[
\boxed{B_W=B_{\rm pole}+B_\Gamma+B_{\rm fin}.}
\]

Damit existiert bereits eine kanonische **gemeinsame Testfunktions-/Amplitudenebene**. Die offene Frage ist nicht mehr die Formel für `B_W`, sondern eine nichtzirkuläre positive globale Geometrie, deren Gramform diese bereits fixierte Form reproduziert.

### 1.2 P05 — Primkanalbilder können überlappen

P05 beweist, dass verschiedene Primkanalbilder nicht strukturell orthogonal sein müssen. Für geeignete Primkanalabbildungen `V_p,V_q` ist die korrekte spektrale Schreibweise

\[
\mu_{pq}^{a,b}(E)=\langle V_pa,E_D(E)V_qb\rangle,
\]

und

\[
\langle a,K_{pq}(z)b\rangle
=\int_{\mathbb R}\frac{d\mu_{pq}^{a,b}(\lambda)}{\lambda-z}.
\]

Daraus folgt als gesicherte Strukturinformation:

\[
\operatorname{Ran}V_p\not\perp\operatorname{Ran}V_q
\]

ist möglich; globale Primblockdiagonalität ist nicht erzwungen. Dies beweist **nicht**, dass jeder Kreuzblock nichtnull ist.

### 1.3 NEU-250 — gemeinsames Quellenbild statt freier Blockmatrix

NEU-250 schließt zwei Fehltypen:

1. positive Vollblockmatrix auf einem freien direkten Summenraum mit festem negativ-indefinitem archimedischen Hauptblock;
2. einen zusätzlichen hermiteschen Kreuzterm als vierten Summanden neben der bereits exakt fixierten Weil-Zerlegung.

Als zulässigen Typ fixiert NEU-250 dagegen

\[
J_W f=(T_{\infty,+}f,T_{\infty,-}f,T_{\rm pr}f),
\]

\[
\mathcal G_W^{(0)}=J_W(\mathcal D_W),
\qquad
\mathcal D_W=C_c^\infty(\mathbb R),
\]

und die Vervollständigung des **gemeinsamen Quellenbildes**, nicht das freie Produkt unabhängig wählbarer Zielkoordinaten.

### 1.4 P03 — Haar-`L^2` ist nicht der finale Objekt-X-Raum

P03 zeigt: selbst unter RH ist `B_W` auf

\[
H_0=L^2(\mathbb R,du)
\]

nicht abschließbar. KLMN/Friedrichs auf diesem Hintergrundraum ist daher kein zulässiger Endweg.

Für P11 bedeutet das:

\[
\boxed{
L^2(\mathbb R,du)\text{ kann Analyse-/Hintergrundraum sein, aber nicht ungeprüft }\mathcal K_X.
}
\]

---

## 2. Historische Objekt-X-Lesart und ihre Reconciliation

NEU-230 (4. August 2026) formuliert OX-1 als positive Vervollständigung eines global gekoppelten relativen Primkanten-Korrespondenzraums und eröffnet explizit

\[
B_{pq}(\xi_p,\eta_q),\qquad p\ne q.
\]

Diese Formulierung bleibt als Zielbeschreibung sinnvoll, muss nach NEU-250/P05 aber typologisch präzisiert werden:

- `B_{pq}` darf **nicht** frei gewählt werden;
- `B_{pq}` darf **nicht** als zusätzlicher Term zur expliziten Formel addiert werden;
- `B_{pq}` soll aus einer gemeinsamen Quelle bzw. einer gemeinsamen globalen Einbettung folgen;
- die lokalen Diagonalstücke einer solchen Faktorisierung müssen nicht mit den isolierten Summanden `Q_p` identisch sein, solange die Gesamtkompression exakt `B_W` ergibt.

Damit wird der alte Satz „wir müssen `B_{pq}` konstruieren“ ersetzt durch die präzisere Aufgabe:

\[
\boxed{
\text{Konstruiere die gemeinsame Einbettungs-/Korrespondenzgeometrie, aus der }B_{pq}\text{ folgt.}
}
\]

---

## 3. Source-First-Kandidatenarchitektur

### 3.1 Minimaler abstrakter Typ

Gesucht ist zunächst ein RH-frei definierter gemeinsamer algebraischer Kern

\[
\mathscr D_X
\]

mit kanonischen Analyseabbildungen

\[
T_v:\mathscr D_X\to E_v,
\qquad
v\in\{\infty,\mathrm{pole}\}\cup\{(p,m):p\text{ prim},m\ge1\},
\]

und einer **gemeinsamen** globalen Realisierung

\[
\iota_v:E_v\to\mathscr E_X.
\]

Der globale Analysevektor wäre dann formal

\[
\mathcal T_X f
:=
\sum_v \iota_vT_vf,
\]

sofern die Summe/Netzstruktur korrekt definiert ist.

Erst **danach** entstehen die Kreuzblöcke als

\[
\boxed{
B_{vw}(f,g)
:=
\langle \iota_vT_vf,\iota_wT_wg\rangle_X.
}
\]

Für Primrichtungen:

\[
B_{pq}
=
T_p^*\,\iota_p^*\iota_q\,T_q
\]

im rein formalen beschränkten Fall.

Die eigentliche unbekannte Struktur ist also nicht `B_{pq}` allein, sondern der **Überlappungsoperator**

\[
\boxed{G_{pq}:=\iota_p^*\iota_q}
\]

bzw. sein unbeschränkter/Form-analoger Ersatz.

### 3.2 Warum das nicht bloß Notation ist

Diese Lesart hat drei nichttriviale Konsequenzen:

1. **Hermiteschkeit wird strukturell:** `G_{qp}=G_{pq}^*`.
2. **Positivität ist global:** jede endliche Blockmatrix `(G_{vw})_{v,w\in S}` muss als Gram-Kern positiv semidefinit sein, falls die Einbettung in einen positiven Raum bereits RH-frei konstruiert wurde.
3. **Nichtorthogonalität wird messbar:** `G_{pq}=0` bedeutet Orthogonalität genau dieses Kanalpaars; P05 erzwingt nicht, dass dies für alle `p\neq q` geschieht.

### 3.3 Anti-Tautologie

Nicht zulässig ist, `G_{pq}` nachträglich so zu wählen, dass

\[
\langle \mathcal T_Xf,\mathcal T_Xg\rangle_X=B_W(f,g)
\]

herauskommt.

Zulässig wäre nur eine Konstruktion von `\mathscr E_X`, `\iota_v` und `T_v` aus adelischen/BC-/Primkanten-/Wres-/Skalierungsdaten, gefolgt vom **Beweis** der Weil-Identität.

---

## 4. Zwei verschiedene Off-Diagonal-Probleme

P11 muss ab jetzt zwei Ebenen strikt trennen.

### P11-C1 — Prime–Prime-Überlappung

Für `p\neq q`:

\[
G_{pq}=\iota_p^*\iota_q.
\]

P05 liefert hierfür bereits eine spektrale Überlappungssprache über `\mu_{pq}^{a,b}` und `K_{pq}(z)`. Offen ist, ob diese Daten aus einer einzigen kanonischen globalen Einbettung stammen und mit der vollständigen Prime-Power-Struktur kompatibel sind.

### P11-C2 — Archimedes–Prime-Überlappung

Hier greift NEU-250 unmittelbar. Die Kopplung darf nicht als additiver vierter Weil-Summand und nicht als positiver freier Vollblock interpretiert werden. Gesucht ist eine quellseitig abhängige Faktorisierung auf einem gemeinsamen Bild.

Diese beiden Probleme können denselben globalen Mechanismus haben, sind aber **nicht identisch**.

---

## 5. P11-Pass-A-Matrix: was lebt, was ist gesperrt

| ID | Baustein / Frage | Endstatus für P11 | Bedeutung |
|---|---|---|---|
| P11-A01 | `\mathcal S_{adel}^{amp} -> \mathcal A_{PW}` als gemeinsame Amplitudenquelle | `✓[K/M]` | lebender globaler Quellanker |
| P11-A02 | vollständige hermitesche `B_W`-Formel | `✓[K/M]` | Vergleichsziel, nicht Definition der positiven Geometrie |
| P11-A03 | Primkanalbilder können überlappen | `✓[M]` | Prime–Prime-Offdiagonalität möglich |
| P11-A04 | globale Primorthogonalität | `?[O]` | weder bewiesen noch widerlegt |
| P11-A05 | paarweise freie Wahl von `B_{pq}` | **gesperrt** | verletzt Kanonizität/Anti-Fitting |
| P11-A06 | `B_{pq}` als abgeleitetes Gram-/Überlappungsdatum | **P11-Leitkandidat** | aus gemeinsamer Einbettung herzuleiten |
| P11-A07 | positiver freier Archimedes–Prim-Vollblock mit festem `A_\infty` | `✓[M]_neg` | P10/NEU-250-Firewall |
| P11-A08 | zusätzlicher Kreuzterm als vierter Weil-Summand | `✓[M]_neg` | P10/NEU-250-Firewall |
| P11-A09 | gemeinsames Quellenbild `\mathcal G_W=\overline{J_W(\mathcal D_W)}` | `✓[K/M]` | bindender Architekturtyp |
| P11-A10 | kanonischer primarithmetischer Zielraum `E_pr` | `?[O]` | notwendiger Konstruktionsschritt |
| P11-A11 | unendlich-rangige Kopplungskontrolle | `✓[M]` notwendig | endlicher effektiver Rang genügt im Grenzmodell nicht |
| P11-A12 | Haar-`L^2` als finale positive Vervollständigung | `✓[K/M]_neg` im P03-Scope | `B_W` dort nicht closable |
| P11-A13 | alternative RH-freie positive globale Vervollständigung | `?[O]` | eigentliches Objekt-X-Problem |
| P11-A14 | `Rampe => LFF`, Selbstkoeffizienten-HH4 usw. | `?[O]` | keine P11-Abkürzung; nur mögliche Nebenquellen |

---

## 6. Neue atomare P11-Arbeitsknoten

Aus der Reconciliation ergibt sich folgende Reihenfolge.

### `[P11-C0]` Gemeinsamer globaler Kern

Bestimme den kleinsten kanonischen algebraischen Kern, auf dem adelische Amplituden, Prime-Power-Translationen und archimedische Analyse gleichzeitig typisiert sind.

**Startkandidat:** `\mathcal A_{PW}=C_c^\infty(\mathbb R)` als analytischer Kern, mit Rückbindung an `\mathcal S_{adel}^{amp}` über `R_{PW}`.

Status: `?[O]` als Objekt-X-Kern; vorhandene Ports `✓[K/M]`.

### `[P11-C1]` Prime–Prime-Überlappungsoperator

Prüfe, ob die P05-Daten `\mu_{pq}^{a,b}`/`K_{pq}(z)` einen kanonischen positiven-definiten Operatorwertkern

\[
G=(G_{pq})_{p,q}
\]

definieren, ohne Hebungswahl und ohne Nullstellendaten.

Status: `?[O]`.

### `[P11-C2]` Prime-Power-Verfeinerung

Ersetze bloße Primlabels durch `(p,m)` und teste die Kompatibilität von

\[
G_{(p,m),(q,n)}
\]

mit den exakten Gewichten `\log p/p^{m/2}`.

Status: `?[O]`.

### `[P11-C3]` Archimedes–Prime gemeinsame Einbettung

Suche keine additive Kreuzform, sondern eine gemeinsame Einbettung/Faktorisierung, deren Kompression exakt die bereits fixierte Weilform erhält.

Status: `?[O]`.

### `[P11-C4]` Positive Vervollständigung ohne Haar-`L^2`

Falls ein positiver Gramkern aus C1–C3 entsteht, konstruiere seinen Radikalquotienten und die positive Vervollständigung. Diese Norm darf nicht stillschweigend die Haar-`L^2`-Norm sein.

Status: `?[O]`.

### `[P11-C5]` Weil-Identifikation

Erst nach C0–C4:

\[
\langle \mathcal T_Xf,\mathcal T_Xg\rangle_X
\stackrel{?}{=}B_W(f,g).
\]

Status: `?[O]`; nachgelagert, Anti-Zirkularitätsfirewall.

---

## 7. Wichtigster konstruktiver Suchtest für den nächsten Durchlauf

Der nächste sinnvolle Direktaudit ist **nicht** eine neue Formel für `B_{pq}`.

Er lautet:

\[
\boxed{
\text{Können die P05-Überlappungsmaße }\mu_{pq}^{a,b}
\text{ als Matrixkoeffizienten eines einzigen positiven operatorwertigen Gramkerns gelesen werden?}
}
\]

Konkret zu prüfen:

1. Sesquilinearität in `(a,b)`;
2. Hermitesche Symmetrie `\mu_{qp}^{b,a}=\overline{\mu_{pq}^{a,b}}`;
3. Positivität endlicher Primblockmatrizen
   \[
   \sum_{p,q\in S}\mu_{pq}^{a_p,a_q}(E)\ge0
   \]
   für messbare `E`, soweit die gemeinsame PVM-Realisierung dies trägt;
4. Abhängigkeit von Hebungen `V_p`;
5. Prime-Power-Verfeinerbarkeit;
6. Kompatibilität mit dem adelischen Port `R_{PW}`;
7. ob daraus ein intrinsischer `G_{pq}` folgt oder nur ein modellrelativer Überlappungskern.

Wenn dieser Test positiv ausfällt, hätten wir erstmals einen **nicht ad hoc gewählten mathematischen Ursprung** der Prime–Prime-Kreuzblöcke. Wenn er nur hebungsrelativ ausfällt, lokalisiert P11 den nächsten echten Engpass auf die Kanonisierung der Primkanalabbildungen `V_p`.

---

## 8. Pass-A-Eröffnungsstatus

\[
\boxed{\text{P11 PASS-A OPEN: source-first architecture selected; no global coupling constructed yet.}}
\]

Kein P11-SYN schreiben. Nächster Arbeitsknoten ist der pfadgebundene Audit `[P11-C1]` der P05-Spektralmaß-/Überlappungsstruktur.
