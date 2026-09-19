# Präziser Satz über die reduzierten Shell-Koordinaten

19. September 2026. AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.
Grundlage: `6f24422ee8e074d387e9656e5307b607edb6c809`.

Der verlangte formale Satz ist isoliert. Die schematische Abbildung mit
(psi-perp intersect W_B^even) direkt-sum X als Definitionsbereich muss
allerdings korrigiert werden: W_B^even verlangt H1 mit Randspur null.
Nach der Projektion auf psi-perp hat der einzelne Core-Anteil diese
Randspur im Allgemeinen nicht mehr.

Orthogonalität bedeutet hier ausdrücklich das physische L2((-B,B),dx)-
Skalarprodukt, nicht das Core-Energieprodukt. Mit K_B^0=K_B intersect psi-perp
und X=C direkt-sum L2(B,b) gilt die echte Bijektion

\[
\Phi_0:K_B^0\oplus X\longrightarrow K_b,\qquad\ker\Phi_0=\{0\}.
\]

Die eindimensionale Trace-Redundanz war der Kern der UNREDUZIERTEN
Abbildung. Nach ihrer Entfernung ist kein solcher Restkern mehr vorhanden.
Die explizite Inverse steht im Beweis. Die physischen Normen erfüllen

\[
\frac1{32}(\|w\|^2+|t|^2+\|s\|^2)
\le\|\Phi_0(w,(t,s))\|^2
\le65(\|w\|^2+|t|^2+\|s\|^2).
\]

Zusätzlich ist die Gleichheit der geschlossenen Formbereiche bewiesen:
Phi_0 bildet F_B^0 direkt-sum F_D bijektiv und mit beidseitiger
Graphnormkontrolle auf F_b ab. F_b wird präzise als Formnormabschluss der
tatsächlichen zulässigen H1-Quellen definiert; keine unbewiesene Gleichheit
mit einem noch größeren Formbereich wird vorausgesetzt.

Für tatsächliche H1-Quellen lautet die gemeinsame Spurbedingung

\[
\boxed{w(B)+t=s(B),\qquad s(b)=0.}
\]

Der Core w liegt in H1 auf dem Core, aber nicht notwendig in H1_0.
Zusammen mit dieser Bedingung erfasst die reduzierte Abbildung exakt alle
ursprünglichen geraden H1_0-Quellen mit den beiden Mellinbedingungen.
Es geht keine Quelle verloren und es entsteht keine weitere Mellinbedingung.

Ein einfaches Gegenbeispiel erklärt die Unterscheidung: Für eine alte
Core-Quelle w_old mit <w_old,psi> ungleich null hat ihre Nullfortsetzung
u=Jw_old die neuen Koordinaten s=0, t=<w_old,psi>/||psi||^2 und
w=w_old-t psi. Dann ist w(B)=-t ungleich null, während die gesamte
physische Quelle weiterhin Randspur null hat.

A_0 ist nun eindeutig als geschlossene Formkompression definiert, C_0 als
beschränkter Kopplungsoperator mit dem festgelegten L2-Adjungierten.
Die nächste offene Rechnung bleibt die uniforme Untergrenze für
R_0=A_0-C_0^*D^-1 C_0 auf dem ganzen reduzierten Core. Alternativ ist ein
inversenfreier relativer Beweis in diesen korrigierten Räumen möglich.
Beide Wege müssen den physischen Normfaktor 65 berücksichtigen.

Das Paket schließt die formale Schnittstelle. Es behauptet keinen neuen
All-Source-Satz rechts von B und keine Odd-Fortsetzung. main bleibt unverändert.


Das parallele Quotientenpaket `309f7be2` bleibt vollständig erhalten. Es
verwendet dieselbe L2-Projektion und denselben bedingten Kopplungsgate.
Dieser Nachtrag ergänzt die explizite Formbereichs-Surjektivität mit
Graphnormkontrolle und die genaue gemeinsame H1-Spurbedingung. Die oben
korrigierte H1_0-Produktformel stammt aus dem eingefügten Review; sie ist
kein Einwand gegen GPT 1s Quotientensatz auf den abgeschlossenen Räumen.
