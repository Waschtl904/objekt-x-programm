# Späterer Nachtrag: genau eine quellenbezogene Schärfung

28. Oktober 2026. Dieser kleine analytische und rationale Zusatz entstand
nach dem eingefrorenen Routenausschluss. Er ändert dessen Originalarchiv nicht.
Keine neue Quadratur, Inversantwort, Richtung oder Parameteroptimierung.

Für dieselbe Quelle `f=Z ell12`, `g9=J*f`, den geerbten tatsächlichen
Formdualrest `R=h-Q1 V` und `Q0=Qold(Knew)` setze

    X=<g9,Q0^-1 g9>, eB=(R B)* Q0^-1 g9,
    r12=B^T k_N, Q=(B^T Gp B)^-1.

Die Blockunterform mit Diagonalblöcken Q0 und Gp sowie Kreuzblock R liefert
wegen `R*Q0^-1R <= theta Gp`, `theta<1/400`, die gültige obere Hülle

    <f,A_E^-1 f> <= A_src
    := X + (r12-eB)^T Q(r12-eB)/(1-theta).

Diese Herleitung erhält die gemeinsame Differenz vor der Normbildung.
Sie ersetzt die bisherigen pauschalen Schritte `20/19` und `X<=W9[g9]`,
behält aber die Schuruntergrenze `(1-theta)Gp`. Formdomänen, physische
Adjunkte und die Inversordnung stehen im
[analytischen Vertrag](source-specific/source-specific-2026-10-28/gpt1/SOURCE_SPECIFIC_CONTRACT.txt).

## Der günstige Test entscheidet bereits über diesen Ansatz

Die Einschränkung der inversen Variationsformel auf reine alte Kernvektoren
ergibt `X>=U8[g8]>18/25`. Dies folgt aus dem tatsächlichen Kernblock von Q0,
nicht aus einer W9-Oberhülle. Der bezahlte Zwölferpreis gibt
`||r12||_Q^2>=215033/50000>(20738/10000)^2`.

Falls `X>=9/2`, gilt sofort `A_src>=9/2`. Andernfalls folgt
`||eB||_Q^2<=theta X<9/800<(107/1000)^2`, also

    A_src > 18/25+(20738/10000-107/1000)^2
          =28676889/6250000 >9/2.

Damit in beiden Fällen

    A_src >=9/2 >D_hi,
    9/2-D_hi=12715016570050523/10^17.

Dieser eine obere Ersatzpreis kann somit keinen positiven Vergleich
nachweisen. **Eine Untergrenze dieses oberen Preises ist keine Untergrenze
der tatsächlichen Inversenergie.** Es folgt kein neuer Ausschluss der
tatsächlichen Schurform. Genauere X-/eB-Werte würden diesen Ansatz nicht
retten und werden hier nicht berechnet.

## Wiederverwendung und fehlende Brücke

Die [Datenzuordnung](source-specific/source-specific-2026-10-28/gpt2/SOURCE_DATA_APPLICATION.txt)
trennt vorhandene Kern-/F-/J-Funktionale und bezahlte r12-Koordinaten von
der fehlenden vollständigen Antwort Q0^-1 g9 und ihren Restpaarungen eB.
Bei Kold→Knew bleibt der alte Tail-Operator eine gültige obere Invershülle;
ein für nu_old ausgewerteter Skalarpreis darf nicht unverändert auf
nu_new übertragen werden.

Die konkret fehlende stärkere Information ist eine quellenwirksame
Schuruntergrenze, die über die beibehaltene Gp-Substitution hinausgeht,
mit konsistenten tatsächlichen Restpaarungen. Ein solcher Satz wird hier
nicht behauptet; keine zweite Darstellung oder weitere Rechnung folgt.

`verify_publication.py` führt die zwei unabhängigen Fraction-Prüfer in
einer separaten Laufkopie aus, vergleicht ihre gespeicherten Ergebnisse
und prüft die zehn Positiv-/Negativ-/Optimierungskontrollen des ersten
Prüfers. Der zweite prüft neun rationale Relationen. Alle Eingänge sind
bytegebunden; die alte Blockherleitung wird angewandt, nicht global neu
geprüft. H1–H4, externe Begutachtung, Punkt 4 und Checkliste 3/10 bleiben.
