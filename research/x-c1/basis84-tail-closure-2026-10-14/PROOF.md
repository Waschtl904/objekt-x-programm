# Ursprünglicher Basis84-Tail: Komplementwechsel und Inversanschluss

14. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

Unter den gebundenen Operator-, Domänen- und Integrationsvoraussetzungen gilt
für beide Paritäten auf dem ursprünglichen Raum
`Z84=(ran J84)^(perp W_X)` innerhalb `R12`:

    tau[z] >= (2/3) W_X[z] >= (1/20) W_X[z],
    A_Z^(-1) <= (3/2) I_Z.

`tau` ist die tatsächliche vollständige Schurform nach dem ganzen alten A8-Raum
und den zwölf physischen Quellen. `A_Z` ist der Operator ihrer ursprünglichen
geschlossenen Restriktion auf Z84. Niedrige Momentkomponenten bleiben enthalten.

## Beweisanker und Brücke

Die [Originalherleitung](original/author/HERLEITUNG.txt), Abschnitte 1–3,
identifiziert Form und Basis und beweist den Komplementwechsel auf der ganzen
Formdomäne. Die [Gegenprüfung](original/countercheck/HERLEITUNG_GPT2.txt),
Abschnitte 2–3, prüft dies eigenständig. Mit K=ran J, P=P_J^L und v=z-Pz gilt
für z orthogonal_W K:

    inf_k tau[z+k] = inf_k tau[v+k] >= (2/3) W_X[v]
                  = (2/3)(W_X[z]+W_X[Pz]) >= (2/3)W_X[z].

Die Voraussetzung ist die vollständige Schurminimierung der
[A9-Inverserneuerung](../a9-inverse-renewal-2026-10-13/PROOF.md), nicht bloß die
Restriktion auf deren neues L-orthogonales Komplement. P erhält die Formdomäne,
weil seine Funktionale nur endliche gewichtete Koeffizienten verwenden und sein
Bild aus festen Formvektoren besteht. Für den Übergang wird keine Kopplung entfernt.

## Gerichtete Inverse und zweiter Beweisweg

Abschnitt 4 der Gegenprüfung beweist für die isometrische Einbettung i:Z84->R12:

    A_Z^(-1) <= i* T_tau^(-1) i <= i* H_*^(-1) i
             <= [(1-c)beta]^(-1) i* R_L i.

Die erste Ungleichung folgt durch Erweiterung des Supremums in der Variationsformel
der Inverse. Die Inverse der Restriktion wird dabei nicht mit der komprimierten
vollen Inverse gleichgesetzt. Da R_L<=5/21 I, folgt unabhängig von der besonderen
hohen Momentgeometrie bereits tau|Z84>231/500 W_X>1/20 W_X.

Für spätere vollständige Hilbertresiduen R mit Werten in Z84 ist hier also
`R* A_Z^(-1) R <= (3/2) R*R` verfügbar. Die Antwortfunktionen, ihre Domänen und
der ganze Residualgram einer neuen Anwendung bleiben gesondert zu prüfen.

## Herkunft, Prüfung und Statuskorrektur

Beide vollständigen Originalarchive werden unverändert in `archives/` erhalten.
[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) bindet sämtliche Archivmitglieder
und lesbaren Originalkopien. Der Repository-Replay rekonstruiert zusätzlich die
historischen Schur- und Basisarchive; er führt 1344 Basisrelationen, 574 positive
Pivots und die vollständigen ursprünglichen Feldabgleiche frisch aus. Die separate
Gegenprüfung bindet außerdem die Antworten über Common96 an dieselben Basisdateien.
Die [Abnahme](ACCEPTANCE_PLAN.md) trennt die ausgeführten Prüfungen von übernommenen
Integrationen und analytischen Voraussetzungen.

Der bisherige offene Status des ursprünglichen Tailbodens wird durch diesen neuen
Beweisanschluss ersetzt. Frühere Archive und Beweisanker bleiben historische
Originale. Der alte hinreichende 268-Funktional-Fittest bleibt als Test ungeklärt;
der neue Boden setzt sein Bestehen nicht voraus. Der globale Residualabschluss
hatte den Faktor 20 nicht benutzt, deshalb liegt kein Zirkelschluss vor.

Kein Boden 2/3 auf ganz R12 oder dem ganzen physischen A9-Raum wird behauptet.
Große Integrationen bleiben gebundene Eingaben; externe Gesamtbegutachtung,
weitere konstruktive Horizonte, Kofinalität, Objekt X und RH bleiben offen.
