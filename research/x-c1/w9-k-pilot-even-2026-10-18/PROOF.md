# Ergebnis des festgelegten geraden K-Piloten

18. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `1fe9c4dabc20201e0ed0436d74909398c6e0cc85`.
Alle Aussagen gelten unter den gebundenen Operator-, Formdomänen-,
Quellenmodell- und Integrationsvoraussetzungen. Externe Prüfung bleibt offen.

## 1. Ergebnis und Aussagegrenze

**PILOT_COMPARISON_EXCLUDED.** Der ausgewählte K-Schritt verbessert die
Teilenergie, reicht aber beim festgelegten geraden Zeugen nicht aus.
Die folgenden Dezimalanzeigen sind nach außen gerundet; die maßgeblichen
exakten rationalen Endpunkte stehen in `RESULT.json`.

| Größe | Gerichtetes Intervall, jeweils mal 10^-6 |
|---|---:|
| Neue tatsächliche Teilenergie | [57.03252199465, 57.25579243309] |
| Unverändertes tatsächliches K_P-Budget | [54.11716936070, 54.11716937864] |
| Teilenergie minus Budget | [2.91535261602, 3.13862307238] |

Insbesondere ist E_lo > K_hi. Die neue zulässige Majorante zusammen mit
der eingefrorenen Antwortmatrix scheitert an diesem Zeugen. Der ausgelassene
R_L-Term ist nichtnegativ und kann diesen Vergleich nicht retten; eine
zusätzliche R_L-Rechnung ist für diese Entscheidung nicht erforderlich.
Dies ist **keine negative Weil-Richtung**, kein allgemeiner Ausschluss
anderer K-Schritte, Antwortregeln oder Inversmajoranten und keine Aussage
gegen die Existenz von Objekt X. Die tatsächliche A9-Inverse wird hier
weiterhin durch eine Obermajorante geprüft, nicht mit ihr identifiziert.
Meilenstein 4, N12 und die externe Prüfung bleiben offen.

## 2. Genau ein unveränderter Pilot

Die [Entscheidungsvorlage](../w9-structural-decision-2026-10-18/PROOF.md)
bindet die Auswahl und die zulässige Erhöhung

\[
K_*=K+\frac{13}{10^8}G_F,\qquad 0<K<K_*\preceq K_B.
\]

G_F ist die alte Zwölfer-Fehlermetrik. Der dortige Nachweis wird unverändert
reproduziert: zwölf positive Pivots für G_F, zwölf für
D_FF,lower - U_F,model - gamma_F,cap G_F - K_*.
Der kleinere F-Fehler wird ausschließlich in diesem F-F-Nachweis verwendet.
U8, X0, die zwölf rationalen Koeffizienten des geraden #238-Zeugen,
die Galerkinantworten X_ans und das separate K_P-Zertifikat bleiben fest.
Es findet keine neue Kandidatensuche, Quadratur oder ungerade Rechnung statt.

Der vollständige Restpreis c=1977/500000 und beta werden gegen die
gebundene unabhängige rationale Abnahme des alten Restnachweises geprüft.
Die festen Gewichte sind a=11/10 und b=500000/478253.
Ihre exakte Zulässigkeitsgleichung

\[
(a(1-c)-1)(b(1-c)-1)=c
\]

wird zusammen mit der Positivität beider Faktoren geprüft.

## 3. Gemeinsamer Schuraufbau

Mit unverändertem M_upper, S, A_force und X_ans gilt

\[
E_*=E_0+\operatorname{diag}(0_{191},K_*-K),\qquad
R^*R_LR\preceq c\beta E_0\preceq c\beta E_*.
\]

Der vollständige alte Rest wird somit übertragen. Es wird keine neue
Restintegration durch eine endliche Galerkinrechnung ersetzt.
Ein 1024-Bit-Arb-Solve E_*Y=X_ans* mit 84 rechten Seiten liefert
P_exact=X_ans Y. Nach Symmetrisierung werden alle Einträge auf einem
60-Dezimalstellen-Gitter eingeschlossen. Der rationale Mittelpunkt erhält
auf jeder Diagonale die Summe der Zeilenradien plus 10^-40. Anschließend
prüft der gebundene unabhängige Integer-Intervallauditor auf dem
120-Dezimalstellen-Gitter den **gesamten 287x287-Block**

\[
\begin{pmatrix}E_*&X_{ans}^*\\X_{ans}&P_*\end{pmatrix}>0.
\]

Alle 287 Pivots sind strikt positiv. Damit ist P_* eine rationale
Obermatrix für X_ans E_*^-1 X_ans*. Die neue Matrix und ihr Zertifikat
stehen in `SCHUR.json.gz`. Die ursprünglichen E0- und X_ans-Matrizen werden
hashgebunden wiederverwendet. Es wird keine ungeprüfte Ordnung zwischen
zwei unabhängig gerundeten P-Obermatrizen behauptet.

Bei unverändertem physischem Residuum f sind h und v unverändert, aber

\[
\nu_*=f_T-g^*U_8h-a_{fin}^*K_*^{-1}v
\]

wird gemeinsam neu gebildet. Die beiden algebraisch äquivalenten
Berechnungen von J*nu_* müssen sich in allen 84x12 Einträgen überlappen.
Ausgewertet wird ausschließlich die festgefrorene Richtung.
Die vier berechneten Features sind hohe U8-, endliche U8-, K_*^-1- und
bP_*-Energie. Die vollständige zulässige Majorante enthält zusätzlich
(a/beta)<nu_*,R_L nu_*>. Nur die vier Features bilden die hier geprüfte
Teilenergie; ihre Obergrenze ist **keine vollständige Energieobergrenze**.

## 4. Neue gewichtete Fehler und neue Teilnorm

`pilot_weights.py` und `pilot_energy.py` sind additive, explizit
parametrisierte Fassungen der gebundenen #238-Herleitung. Historische
Dateien bleiben unverändert. K_*^-1, P_*, k_*=K_*^-1 a0 und b gehen sowohl
in das Modell als auch in jede gewichtete Fehlerschranke ein.

Insbesondere bleiben d_U, d_D und d_a=d_U+d_D die vollständigen bisherigen
96-Quellen-/F-J-Fehler. Der Replay prüft ihre Übereinstimmung mit den alten
gebundenen Einschließungen. Der kleinere gamma_F ersetzt keinen dieser
Fehlerpreise. Der Fehler von a_fin wird in der nu-Featuregrenze genau
einmal bezahlt, einschließlich seiner Wechselwirkung mit dem v-Fehler.
Die gemeinsamen Differenzen werden vor dem Quadrieren gebildet.

Für die ganze Residualmodellabweichung wird eine neue gültige Teilnorm
berechnet. Mit u als alter voller U8-Normmajorante, U_F,up=U_F,model+d_U G_F,
s=(-k_*,I), G=diag(G_F,G_J) und der neuen rationalen Matrix P_* setzt man

\[
d_k=d_a\sqrt{\operatorname{tr}(K_*^{-1}G_FK_*^{-1})\operatorname{tr}(P_*G_J)},
\quad k_P=\sqrt{\operatorname{tr}(P_*k_*^*k_*)}+d_k,
\]
\[
u_s=\left(\sqrt{\operatorname{tr}(P_*s^*U_{model}s)+
d_U\operatorname{tr}(P_*s^*Gs)}+\sqrt{\operatorname{tr}(U_{F,up})}d_k\right)^2,
\]
\[
v_*=16\sqrt{\operatorname{tr}(K_*^{-1})}+
\sqrt{u\operatorname{tr}(K_*^{-1}U_{F,up})},
\]
\[
j_*=\sqrt{1.000502\operatorname{tr}(P_*)}+16k_P+\sqrt{u u_s},
\qquad \|W_{*,partial}\|\le w_*=u+v_*^2+b j_*^2.
\]

Dies sind die bereits hergeleiteten Cauchy-/Dreiecksmajoranten mit
sämtlichen neuen Gewichten. Sie benötigen keinen Ordnungsbeweis zwischen
altem und neuem W_partial. Gerichtet erhält man w_* < 2.543380064e41.
Die große globale Norm ist keine tatsächliche Fehlergröße; sie wird mit
der gebundenen sehr kleinen ganzen Residualmodellabweichung multipliziert.

| Neu berechneter Fehlerpreis (Norm, keine Energie) | Obere Anzeige |
|---|---:|
| zusätzliche endliche U8-Featureabweichung | 3.841235e-18 |
| K_*^-1-Featureabweichung | 1.160958e-12 |
| sqrt(b) P_*-Featureabweichung | 3.326111e-6 |
| ganze Residualmodellabweichung in der neuen Teilnorm | 1.224392e-10 |

Die Integrations- und Rechenintervalle der ursprünglichen Paarungen
bleiben enthalten; die Koordinaten-/Gamma- und Antwortmodellfehler werden
zusätzlich wie in #238 transportiert. Die einzelnen Modellkomponenten,
Intervallradien, der separate a_fin-Anteil und alle Normgrenzen werden in
`RESULT.json` ausgewiesen. Für Modellenergie m, zusätzliche gemeinsame
Featurenormabweichung e_f und ganze Residualabweichung e_r gilt

\[
E\in[(\max(0,\sqrt{\max(0,m_{lo})}-e_f-e_r))^2,
       (\sqrt{m_{hi}}+e_f+e_r)^2].
\]

Negative Normquadrate werden nicht durch Absolutbeträge repariert.
Die Klassifikation verwendet ausschließlich die veröffentlichten äußeren
rationalen Endpunkte und das unveränderte tatsächliche K_P-Intervall.

## 5. Reproduktion und Abschluss

`verify.py --check` prüft unveränderliche Eingabebytes, rekonstruiert K_*,
E_*, P_*, den vollständigen rationalen Block, die gemeinsamen Features,
alle betroffenen Fehler und die Entscheidung. `MANIFEST.json` bindet den
Paketbestand, `INPUT_BINDINGS.json` die direkten und geerbten Quellen.
Der vorab festgelegte Abnahmeplan verlangt einen frischen vollständigen
Git-Archiv-Replay beider Ergebnisdateien sowie Registry- und Diffprüfungen.
Die konkrete Archivbindung, Laufzeiten und Bytevergleichsquittung stehen
in `ACCEPTANCE.json`. Jeder vollständige Rechenaufruf hat eine harte
30-Minuten-Grenze; ein Timeout hätte keine mathematische Bedeutung.

Abgeschlossen sind dieser eine K-Schritt, sein gemeinsamer Schur- und
Fehlertransport und der gerichtete gerade Teilenergievergleich. Es gibt
keine Dualreserve für diesen Pilot und keine automatische Folge-Großrechnung.
Die nächste Entscheidung ist, ob ein neuer begründeter Formvergleich oder
der bereits skizzierte variationale Schur-Untertest einen eng begrenzten
weiteren Auftrag rechtfertigt. Dieser Bericht startet keinen davon.
