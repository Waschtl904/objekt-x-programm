# F2-Primäraudit — Fourier-/Rohkopplungsstrang NEU-151–173

**Datum:** 9. August 2026  
**SYN-Ziel:** P05 — Relative Prime Channels and Arithmetic Edge Geometry  
**Quellbestand:** 33 Dateien in `05-primkanal-fourierladung/`, NEU-151 bis NEU-173 inklusive Unterknoten  
**Eröffnungsstand:** Commit `8ead5d52cea9a0e62c73f72fc48964cd9b5688ae`  
**Primäraudit-Commit:** `b6a97e2706f9a925b1cbe09535462ee7658d5ac7`  
**Zweitcheck:** `audits/AUDIT-2026-08-09_F2_Zweitcheck_Pfadgebunden.md`, Commit `27a5fe2e40cc760ef20b0ad29ce25b46f5ab1b1f`  
**Endanker:** NEU-170d + NEU-173  
**Prüfart:** `AUDIT-RECONCILED` mit gezielten `TARGETED-REAUDIT`-Checks an kollidierenden Statusaussagen  
**Status dieses Auditblatts:** `F2 PASS A COMPLETE — doppelt geprüft`

---

## 0. Methodik

F2 wird nicht als neuer Vollaudit der 33 historischen Dateien behandelt. Maßgeblich ist

\[
\text{NEU-151–173}
+\text{spätere interne Korrekturen}
+\text{F1–F4-Firewalls}
\longrightarrow
\text{heute gültiger P05-Endstand}.
\]

Die Eröffnungsmatrix aus Commit `8ead5d52` war eine Arbeitsmatrix. Der Primäraudit prüft nur dort neu, wo ein konkreter Status-, Typ- oder Provenienzkonflikt sichtbar ist. NEU-170d ist der epistemisch bereinigte DAG-Endanker für den $L_3^\circ$-/Einmodenstrang; NEU-173 ist der Endanker für den alten Typquellenpfad.

**Wichtig:** `PASS A COMPLETE` bedeutet Migrationsabschluss, nicht Lösung aller mathematischen offenen Punkte. Der unabhängige pfadgebundene Zweitcheck samt Mini-Nachtrag ist ohne konkreten Gegenbefund abgeschlossen; alle `?[O]`-, `CONDITIONAL`- und partiellen Status bleiben unverändert.

---

## 1. DUPLICATE-ID NEU-166b

Im Repo existieren zwei inhaltlich verschiedene Dateien mit ID NEU-166b:

| interne Bezeichnung | Datei | Rolle |
|---|---|---|
| **166b-P** | `NEU-166b_Rollen_Provenienzentscheidung_Rp_Tp.md` | methodisches Provenienz-/Audit-Firewall; Rollenentscheidung inhaltlich offen |
| **166b-T** | `NEU-166b_Typ_Domaenen_Deszentaudit_Tp_Fallverzweigung.md` | substanziell späterer Typ-/Domänen-/Deszentaudit; Fall 2 ausgeschlossen, Fall 3a lokal/modenweise bestätigt, globale Entscheidung offen |

Verbindlich:
- 166b-T hat substanziellen Vorrang für den mathematischen Endstand.
- 166b-P bleibt als Provenienzfirewall erhalten.
- Kein SYN-Satz darf unqualifiziert „NEU-166b beweist ...“ sagen.

---

## 2. Korrigierte Prüfartmatrix NEU-151–173

| Knoten | Endstatus für P05 | Heute gültiger Kernbefund |
|---|---|---|
| **NEU-151** | `INCORPORATED_part` | Norm- und Rangidentitäten sind innerhalb des gewählten NEU-44.X-Rang-eins-Modells algebraisch korrekt. Daraus folgt nicht intrinsisch $c_p\neq0$, Hebungsunabhängigkeit oder eine termweise Asymptotik. Der induzierte Operator auf eindimensionaler Quelle hat Rang $\le1$; die Rohkopplung $T_p$ kann höheren Rang besitzen. |
| **NEU-152** | `INCORPORATED_part + ?[O]` | Nichtentartung der Primkanalgewichte ist nicht bewiesen. Die Fallanalyse A/B/C ist gültige Triage; $|c_p|^2$ bleibt hebungsrelativ und die termweise Unter-/Zweiseitenschranke offen. Eine früher importierte obere Größenordnung darf nicht als intrinsischer unbedingter Satz gelesen werden. |
| **NEU-153** | `INCORPORATED_part + ?[O]` | Starke und schwache Hebungsinvarianz bleiben offen. Die elementare Differenzformel für Normen ist `✓[M]`; Existenz, Mehrpunktigkeit und Tangentialgeometrie der normierten Liftfaser bleiben `?[O]`. |
| **NEU-154** | `INCORPORATED_part / CONDITIONAL` | Pullback-, Nullraum-, Gram-, Normierungs- und Dichteaussagen sind Architektur/Reduktion. Der entscheidende Pullback (PB) und die konkreten Gramwerte sind offen; Folgerungen daraus sind konditional. |
| **NEU-155** | `INCORPORATED_part` | Verbindliche Typtrennung: Rohkopplung $T_p$, induzierter Primkanaloperator $C_p^{[\widehat\varepsilon_p]}$ und relative Rang-eins-Erweiterung $C_p^{\rm rel}[\widehat\varepsilon_p]$ sind verschiedene Objekte. $T_p(e_0V_p)=0$ auf der kontrollierten Formel; Rang $\le1$ gilt für die eindimensional induzierte Abbildung, nicht für $T_p$. Isometrie-/Pullbackfragen bleiben offen. |
| **NEU-156** | `INCORPORATED_part / CONDITIONAL` | Die verbundene Restspurform ist aus dem Quellenstand nicht eindeutig rekonstruiert. `(155.F.1)` ist eine zusätzliche Strukturannahme, kein Folgesatz. Eindeutigkeit kann erst über konkrete Symmetrie/Kommutante entschieden werden. |
| **NEU-157** | `INCORPORATED_part + ?[O]` | Rev.3 korrigiert das alte lineare Zulässigkeitsmodell: die $W^{\rm res}$-Normierung ist quadratisch, $R_{p,j}$ sind nicht konstruiert, die exakte Zulässigkeitsmenge ist nicht einfach ein Schnitt linearer Kerne. Präprojektive Nichtverschwindung bei nichtleerem gewichteten $L_3^\circ$-Träger ist ein gültiges Satzschema; ein exakt zulässiger Nichtnullzeuge bleibt `?[O]`. |
| **NEU-158** | `INCORPORATED_part / CONDITIONAL` | Abstrakter Kommutantensatz ist `✓[M]`: beschränkte positive semidefinite $G_p$-invariante Formen sind genau dann skalar proportional zur Referenzform, wenn $\pi(G_p)'=\mathbb CI$. Die konkrete Darstellung $\pi_p$, ihre Irreduzibilität und damit die konkrete Eindeutigkeit bleiben offen. |
| **NEU-159** | `INCORPORATED_part / CONDITIONAL` | Dualzeugenprinzip und Basiszeugenkriterium sind `✓[M]`; die konkrete Mitgliedschaft, Existenz eines Projektionszeugen, $T_p(\mathcal E_p^{\rm lin,ch})\neq0$ und $Q_p\neq0$ bleiben bis zum Zeugen offen. |
| **NEU-160** | `INCORPORATED_part / CONDITIONAL` | Abstrakte Quotienten-, Isometrie-, Nullraumabstiegs- und Intertwining-Lemmata sind `✓[M]`. Die konkrete Nichttrivialität von $Q_p$, die konkrete $G_p$-Wirkung, Unitärität als Anwendung und Irreduzibilität bleiben `?[O]`. |
| **NEU-161** | `CONDITIONAL` | $s\neq0$ ist im Quellblatt Eingangsannahme, kein hergeleiteter Fourierladungsbefund. Der geladene $L_3^\circ$-Träger ist nicht bewiesen. |
| **NEU-162** | `CONDITIONAL` | Die Wahl $L_3^\circ=e_1V_1$ ist rechenzulässig im Testmodell und liefert den nichtverschwindenden Skalar $(p-1)\log p$, aber nach NEU-170d nicht herkunftszulässig als Repräsentant des gegebenen $[L_3]$. |
| **NEU-163** | `CONDITIONAL` | Einmodenrechnung nur im Testmodell aus NEU-162. NEU-170d stellt klar: Nichtverschwindung der Zielkante und weitere Liftbedingungen sind nicht als unbedingter Objekt-X-Befund geschlossen. |
| **NEU-164** | `CONDITIONAL` | Korrekte Falllogik für den $R_{p,j}$-Test; konkrete Wirkungsformeln/zulässige Moden waren nicht importiert. Scheitern des kanonischen Basiszeugen impliziert weder $Q_p^{\rm rel}=0$ noch das Fehlen kombinierter Zeugen. |
| **NEU-165** | `INCORPORATED_part / CONDITIONAL` | Strukturbericht über hypothetische $R_{p,j}$; das Blatt selbst steht `?[O]`. Keine unbedingte Matrix-/Kernberechnung darf ohne tatsächliche Operatorquelle importiert werden. |
| **NEU-165a** | `AUDIT-FIREWALL / INCORPORATED_part` | Quellenregister trennt den tatsächlich vorhandenen $C_p$ von den postulierten $R_{p,j}$; die Brücke bleibt offen. |
| **NEU-165b** | `INCORPORATED` | Konsistenzaudit korrigiert NEU-157: $R_{p,j}$ wurden nicht konstruiert; die Normierungsbedingung ist quadratisch und erzeugt keinen linearen Kern. Diese Korrektur ist verbindlich. |
| **NEU-166** | `INCORPORATED_part / CONDITIONAL` | Ein-/Zweimoden-Triage und Normierungslemma sind als abstrakte Satzschemata brauchbar. Exakte Definition/Faktorisierung der Operatoren, Kerntrennung und tatsächlicher Zeuge bleiben offen und werden durch 166a/b, 167b und 170d eingeschränkt. |
| **NEU-166a** | `INCORPORATED_part / AUDIT-FIREWALL` | Typ-/Domänen-/Deszentarchitektur ist eine saubere Prüfliste, aber kein Beweis einer globalen Operatorverlängerung, vollständigen Domäne, Quotientendeszents oder Kerntrennung. Der Status des Blatts ist ausdrücklich offen. |
| **NEU-166b-P** | `AUDIT-FIREWALL` | Provenienz- und Rollenregeln; verhindert nachträgliche Umdeutung postulierter Operatoren in Quellenkonstruktionen. Inhaltliche Rollenentscheidung bleibt offen. |
| **NEU-166b-T** | `INCORPORATED_part + ?[O]` | Fall 2 ist im geprüften Quellenstand ausgeschlossen. Fall 3a ist lokal/modenweise formelmäßig bestätigt. Globale Verlängerung, Faktorisierung, Quotientendeszent, Detektor und Entscheidung zwischen Fall 1/3b/4 bleiben offen. |
| **NEU-167** | `INCORPORATED_part` | Primärvariation erzeugt auf $K_p$ keinen neuen nichttrivialen Kernoperator; Fourierladung ist eine Nichtverschwindensbedingung und keine homogene Kerngleichung. |
| **NEU-167b** | `INCORPORATED + ✓[M]_neg` | Im explizit auditierten Quellenkegel liefern NEU-157/44 keine zusätzlichen nichttrivialen $L_{p,a}$-Kerngleichungen; Fall 1 ist dort leer. Dies ist ein negativer **Quellenbefund**, kein globaler mathematischer Unmöglichkeitssatz. Die exakte Zulässigkeitsarchitektur bleibt nichtlinear. |
| **NEU-168** | `INCORPORATED_part + ?[O]` | Reduziert die Zeugenfrage auf die nichtlineare exakte Liftmenge und kontrollierte Rohkopplung. $\mathcal M_p^{wit,raw}\neq\varnothing$ bleibt ohne expliziten Zeugen/geometrischen Schnittbeweis offen. |
| **NEU-169** | `INCORPORATED_part` | Exakter **fest-primer** Kollisionssatz und Restklassenzerlegung: bei festem $u$ ist $(s,m)\mapsto(u+ps,pm)$ injektiv; Mehrmodenkern ist ein Restklassen-Faltungsannihilator. Einzelmoden-Nichtverschwindung bleibt konditional auf $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$. |
| **NEU-170** | `SUPERSEDED_part / ?[O]` | Quellenimport findet keinen expliziten geladenen Fourierkoeffizienten und keinen strukturellen Satz, der geladenen Träger erzwingt. Die Trägervoraussetzung bleibt offen und wird durch 170a–d weiter bereinigt. |
| **NEU-170a** | `SUPERSEDED_part / ✓[M]_neg` | Negativer Quellenbefund: geladener Fouriergrad ist ohne Kettenverträglichkeit keine quellenfeste Klasseninvariante. Dies ist kein mathematischer No-Go gegen eine spätere Konstruktion. |
| **NEU-170b** | `SUPERSEDED_part` | Downstream wird $L_3$ als teilweise spezifizierter Repräsentant verwendet; Ursprung, Raumtyp, Kanonizität und Repräsentantenwahl sind nicht hergeleitet. Endstand wird durch 170d/173 bestimmt. |
| **NEU-170c** | `SUPERSEDED_part / AUDIT-ONLY` | Partieller Direktaudit: NEU-28 liefert keinen Fourierträger und konstruiert $L_3$ nicht. Das Blatt selbst ließ Original-/Repräsentantenfragen offen; der spätere Endstand ist 170d/173. |
| **NEU-170d** | `INCORPORATED — DAG-ENDANKER` | Maßgeblicher epistemischer Endstand: $[L_3]\not\mapsto L_3^\circ=e_1V_1$; $(p-1)\log p\neq0$ impliziert nicht das Nichtverschwinden der benötigten Zielkante. NEU-162/163 sind nur konditionale Testmodellresultate. Route A benötigt eine typisierte Repräsentantenbrücke; Route B ist quellennegativ, mathematisch offen. |
| **NEU-171** | `INCORPORATED_part / AUDIT-ONLY` | Typfundament-/Prüfarchitektur; selbst keine Konstruktion und kein Nichtverschwindensnachweis. |
| **NEU-172** | `SUPERSEDED_part` | Alter Endlabel `C₂` wird durch NEU-173 korrigiert. |
| **NEU-173** | `INCORPORATED — TYPQUELLEN-ENDANKER` | Endstatus `C_src-neg`: Im auditierten Quellenkegel ist kein vollständiges Tupel $(B_3,M,C^\bullet,b,L_3,\rho_{op})$ konstruiert. `✓[M]_neg` als Quellenbefund; Existenz eines typkorrekten neuen $L_3$/Realisierungswegs bleibt `?[O]`. $\delta_{BC}$ ist Algebraableitung und nicht das Hochschild-Kodifferential $b$. |

---

## 3. Korrekturen gegenüber der F2-Eröffnungsmatrix

Der Primäraudit korrigiert insbesondere folgende Lesarten:

1. **NEU-151:** Modellrelative Rang-/Normidentitäten dürfen nicht als intrinsisches $c_p\neq0$, intrinsische Rang-eins-Geometrie oder gesicherte termweise Asymptotik gelesen werden.
2. **NEU-157:** Kein exakt zulässiger Nichtnullzeuge ist bewiesen; das Blatt ist Existenzsatz-Vorbereitung mit gültigen bedingten Teilresultaten.
3. **NEU-158/160:** Die abstrakten Hilbertraum-/Kommutantensätze sind bewiesen, die konkrete Nichttrivialität, Symmetrie und Irreduzibilität aber offen.
4. **NEU-166a:** Typ-/Domänen-/Deszentstruktur ist Auditarchitektur, nicht geschlossene globale Operatorrealisierung.
5. **NEU-169 vs. NEU-250j:** Zwei verschiedene Kollisionsbegriffe. NEU-169 untersucht Kollisionen/Annihilatoren **innerhalb eines festen Primkanals** und Restklassen modulo $p$. NEU-250j untersucht **Kreuzprimkollisionen** $p\neq q$. 250j „verstärkt“ 169 daher nicht direkt.
6. **NEU-170c:** Das Blatt ist partiell und darf nicht als positive Quellendefinition eines typisierten $L_3$ gelesen werden; Endanker sind 170d + 173.
7. **NEU-172:** `C₂` ist superseded durch NEU-173 `C_src-neg`.

---

## 4. Verbindliche F2-Firewalls

**6. DUPLICATE-ID-Firewall.** `NEU-166b` stets als 166b-P oder 166b-T disambiguieren.

**7. $L_3^\circ$-Provenienz-Firewall.** Alle nichtverschwindenden/geladenen Aussagen aus NEU-161–169, die $L_3^\circ=e_1V_1$ oder einen nichtleeren gewichteten Träger benötigen, sind nur konditional zu lesen. NEU-170d dominiert.

**8. Kernzeugen-Firewall.** Die historische Route $k\in\ker C_p\setminus\ker T_p$ ist im auditierten Quellenkegel nicht konstruktiv geschlossen. NEU-167b schließt insbesondere die postulierte zusätzliche lineare Kernfamilie negativ als Quellenbefund. Nicht stillschweigend wieder eröffnen.

**9. Kollisions-Firewall.** NEU-169 (festes $p$, Restklassen-/Faltungskollision) und NEU-250j (Kreuzprimkollision $p\neq q$) sind typologisch verschiedene Sätze. Keine direkte „Verstärkung“ oder Identifikation behaupten.

**10. Zulässigkeits-Firewall.** Nach NEU-157 rev.3 / 165b / 167b ist die exakte Zulässigkeitsmenge nicht als reiner Schnitt homogen-linearer Kerne zu behandeln. Fourierladung ist offen/nichtverschwindend, Normierung quadratisch, weitere Bedingungen sind Faktorisierungs-/Abstiegsfragen.

**11. Symmetrie-Firewall.** NEU-158s Kommutantensatz und NEU-160s abstrakte Quotienten-/Intertwining-Lemmata sind `✓[M]`; konkrete $Q_p\neq0$, konkrete unitäre Wirkung und Irreduzibilität sind nicht automatisch mitbewiesen.

**12. Deszent-Firewall.** NEU-166a/166b liefern keine unbedingte globale Erweiterung von $T_p^{pre}$, keinen vollständigen Definitionsbereich, keinen Quotientendeszent und keinen kanonischen transversalen Detektor.

**13. Endanker-Firewall.** NEU-170/170a/170b/170c werden nur durch NEU-170d + NEU-173 in SYN migriert. Kein geladener $L_3^\circ$-Ursprung darf aus Zwischenständen importiert werden.

**14. Primgewicht-Firewall.** NEU-151-Norm-/Rangidentitäten sind modellrelativ. Intrinsisches $c_p\neq0$, Hebungsunabhängigkeit, Nichtentartung und termweise Größenordnung sind nicht gesichert.

**15. Quellennegativ ≠ mathematisch unmöglich.** Negative Befunde in NEU-167b, NEU-170d und NEU-173 schließen den auditierten Quellenweg; sie schließen eine neue typkorrekte Konstruktion nicht aus, sofern diese weiterhin `?[O]` ist.

---

## 5. Was F2 nach P05 liefert

### Übernehmbar

- die strikte Typtrennung
  \[
  T_p\neq C_p^{[\widehat\varepsilon_p]}\neq C_p^{\rm rel}[\widehat\varepsilon_p];
  \]
- Nullmodusobstruktion $T_p(e_0V_p)=0$ auf der kontrollierten modalen Formel;
- Rang $\le1$ des eindimensional induzierten Primkanaloperators, ohne Rangbehauptung über $T_p$;
- finite/modale Rohkopplungsformel und ihre algebraischen Kollisionskriterien nur auf dem kontrollierten Definitionsbereich;
- die Erkenntnis, dass exakte Liftzulässigkeit nicht durch das alte lineare Kernmodell beschrieben wird;
- den fest-primer Restklassen-/Faltungs-Kollisionssatz aus NEU-169;
- die negative Provenienzdiagnose: kein quellenfest hergeleiteter geladener Repräsentant $L_3^\circ$ im alten Pfad.

### Nicht als unbedingter P05-Satz übernehmen

- intrinsisches $c_p\neq0$ oder intrinsische Nichtentartung;
- allgemeine Hebungsunabhängigkeit;
- Existenz eines exakt zulässigen Nichtnullzeugen;
- konkrete Irreduzibilität/Einzigkeit der verbundenen Form;
- globale Operatorverlängerung oder Quotientendeszent von $T_p^{pre}$;
- $L_3^\circ=e_1V_1$ als aus $[L_3]$ hergeleitete Wahl;
- geladene Fourierträger- oder Nichtverschwindensaussagen ohne die Endanker-Firewall.

---

## 6. Weiterleitungen

**→ P06:** Quotienten-/Feshbach-/Hilbertisierungsfragen, operatorische Grenz-/Deszentfragen und später die Spektralmaß-/Schattenklassenfassung.

**→ P09:** $L_3$-/Hochschild-Typquellenpfad, insbesondere $(B_3,M,C^\bullet,b,L_3,\rho_{op})$ und die Trennung $\delta_{BC}$ vs. Hochschild-$b$.

**→ P11:** globale nichtorthogonale Kopplung, gemeinsame Quellen-/Quotientenbrücken und jede globale Gramblock-Realisierung.

P05 übernimmt aus F2 nur die für relative Primkanäle und arithmetische Kantengeometrie nötigen lokalen Struktur- und Firewall-Aussagen.

---

## 7. Endurteil nach Zweitcheck

Der unabhängige pfadgebundene Gegencheck prüfte die 33 vorgegebenen Quelldateien, die sieben Primäraudit-Korrekturen A–G und die Weiterleitungen. Ein formaler Zwischenfehler („alle gelesen“ bei gleichzeitig nicht direkt gelesenen NEU-159/160/166b-T) wurde vor der Versiegelung durch einen gezielten Mini-Nachtrag geschlossen. Dieser las genau diese drei Dateien direkt und bestätigte die Primäraudit-Befunde ohne Gegenbefund.

Verbindlicher Zweitcheck-Nachweis:

`audits/AUDIT-2026-08-09_F2_Zweitcheck_Pfadgebunden.md` — Commit `27a5fe2e40cc760ef20b0ad29ce25b46f5ab1b1f`.

\[
\boxed{\text{F2 PASS A COMPLETE — doppelt geprüft.}}
\]

**Epistemische Firewall:** Dieses Siegel bestätigt den reconcilierten Migrationsstand. Es schließt insbesondere weder die exakt zulässige Zeugenexistenz noch Hebungsunabhängigkeit, konkrete Irreduzibilität, globale Operatorverlängerung, $L_3$-Realisierung oder andere als `?[O]`/`CONDITIONAL` geführte mathematische Punkte.