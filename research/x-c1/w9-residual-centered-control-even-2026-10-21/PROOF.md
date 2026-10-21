# Gemeinsame richtungsbezogene und restzentrierte Kontrolle

21. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Ausgangsbasis: `639d25e38b453f2e10b859553ca49a7a0e4fafdb`.
Alle geerbten Operator-, Formdomänen-, Geometrie-, Quellen- und
Integrationsannahmen bleiben Voraussetzungen. Keine neue Gesamtpositivität.

## 1. Endliche Vorstufe und vollständiger Abschluss

Am unveränderten geraden Zeugen und Testvektor aus #248 wird der bisherige
gemeinsame D/U-Formpreis durch seine richtungsbezogene Auswertung ersetzt.
Die vorhandenen vollständigen Quellenfehler werden dabei weiter bezahlt.

| Größe | Konservative Anzeige |
| --- | ---: |
| Alter D/U-Formpreis | etwa 5.33596882148e-7 |
| Neuer U-Formpreis | <2.66248114096e-14 |
| Neuer D-Formpreis | <1.17313938339e-23 |
| F(Jw) | [53.72788759778; 53.94165395410]e-6 |
| Budgetuntergrenze | >54.11716936070e-6 |
| Norm des endlichen Restfeatures | <1e-5 |

Die maßgeblichen rationalen Endpunkte stehen in RESULT.json. Die geerbten
Basisenergie-, Paarungs-, a_fin- und eta-q-Fehler bleiben unverändert.

Mit dem ganzen Residuum `r=nu-H_new Jw` liefert die endliche Vorstufe die
hinreichende Bedingung

    d := <r,R_L r> <= 1.9e-8

für den vollständigen oberen Vergleich am festen Zeugen. Die Anwendung des
Inverslemmas auf r erhält die bereits herausgerechnete variationale Energie.
Sie benutzt weder den sehr kleinen skalaren Boden kappa aus #250 noch eine
exakte Darstellung von w in der schlecht konditionierten Antwortmatrix.

**Abschnitt 7 schließt d jetzt auf dem vollständigen T ein und beweist den
Vergleich für diesen festen geraden Zeugen.** Die endlichen Ergebnisdateien
RESULT.json und AUDIT.json bleiben als Vorstufe getrennt: Ihre Offen-Flags
beziehen sich auf den Umfang dieses endlichen Teilprüfers. Das gemeinsame
Endergebnis steht in whole/WHOLE_RESULT.json. Der vollständige Grad-11-Raum,
die ungerade Parität, Punkt 4, N12 und externe Prüfung bleiben offen.

## 2. Richtungsbezogener gemeinsamer Formpreis

Die gebundene gemeinsame Quellenrechnung liefert tatsächliche Featureoperatoren
Psi_J=Psi_J,0+Delta_J mit Delta_J*Delta_J <= E_J I und analog
Delta_F*Delta_F <= E_F. Hier werden dieselben konservativen Fehler benutzt wie
in #248:

    E_J = 2 (E_J,common + e_h,J²/delta),
    E_F = 2 (E_F,common + E_F,high/delta).

Der zusätzliche hohe Quellenfehler und der Faktor 2 entfallen nicht.
Für den festen rationalen w setze

    u_w=w*U_JJ,0 w,    e_w=E_J ||w||²,
    delta_U(w)=2 sqrt(u_w e_w)+e_w.

Cauchy–Schwarz auf den tatsächlichen gemeinsamen Features gibt

    | ||Psi_J w||²-||Psi_J,0 w||² | <= delta_U(w).

Die beiden gerichteten direkten Matrizen D_minus <= D_actual <= D_plus
liefern mit D_0=(D_plus+D_minus)/2 und B_D=(D_plus-D_minus)/2 >=0

    |w*(D_actual-D_0)_JJ w| <= w*(B_D)_JJ w = delta_D(w).

Der neue gemeinsame Preis ist delta_new=delta_U+delta_D. Er ersetzt
ausschließlich den alten skalaren delta_old in den Formgrenzen. Deshalb

    F_new,lo=F_old,lo+delta_old-delta_new,
    F_new,up=F_old,up-delta_old+delta_new.

Es werden die veröffentlichten oberen rationalen Fehlerendpunkte verwendet.
Der positive quadratische Fehler des a_fin-Terms in F_up aus #250 bleibt
erhalten. Keine Schranke wird aus einem Quadratur-Netzunterschied abgeleitet.

## 3. Die endlichen Koordinaten des ganzen Residuums

P bezeichnet die bereits zertifizierte rationale Obermatrix
P >= X_ans E_new^-1 X_ans*. Wir begrenzen

    z_r=||P^(1/2) J*r||.

Schreibe K_i=K_new^-1, a=a_fin,0, Delta a=a_fin-a,
U_F=Psi_F,0*Psi_F,0 und U_J=Psi_J,0*Psi_J,0. Die alte direkte relative
Fehlerschranke d_D bleibt verfügbar. Mit t=K_i a w werden die folgenden
skalaren Gramgrößen gerichtet berechnet:

    g_t=t*G_F t, u_t=t*U_F t, e_t=t*E_F t, g_w=w*G_J w,
    p_G=tr(P G_J), p_U=tr(P U_J), p_E=E_J tr(P),
    k_G=tr(K_i G_F), k_U=tr(K_i U_F), k_E=tr(K_i E_F).

Die gemeinsame bilineare Featureentwicklung ergibt

    e_a := ||K_i^(1/2) Delta a w||
      <= d_D sqrt(k_G g_w)+sqrt(k_U e_w)
         +sqrt(k_E u_w)+sqrt(k_E e_w),

    e_left := ||P^(1/2) Delta a* t||
      <= d_D sqrt(g_t p_G)+sqrt(p_U e_t)
         +sqrt(p_E u_t)+sqrt(p_E e_t),

    e_HS := ||K_i^(1/2) Delta a P^(1/2)||_HS
      <= d_D sqrt(k_G p_G)+sqrt(k_U p_E)
         +sqrt(k_E p_U)+sqrt(k_E p_E).

Dies sind Normobergrenzen aus positiven Gramformen, keine Normuntergrenzen.
Aus der exakten Expansion

    a_actual* K_i a_actual w-a* K_i a w
      = Delta a* t + a* K_i Delta a w + Delta a* K_i Delta a w

folgt der gemeinsame quadratische Aktionspreis

    e_square=e_left+(sqrt(tr(P a* K_i a))+e_HS)e_a.

Für die übrigen Wirkungen werden

    e_U=sqrt(p_U e_w)+sqrt(p_E u_w)+sqrt(p_E e_w),
    e_D=sqrt(tr(P B_D) delta_D(w))

verwendet. Die letzte Ungleichung folgt aus
`-B_D <= Delta D <= B_D`, also der Faktorisierung durch eine Kontraktion
auf dem Träger von B_D; sie benötigt keine Invertierbarkeit von B_D.

Die geerbte normgewichtete nu-Fehlergrenze aus #246 wird durch die
Quadratwurzel ihres dortigen Gewichts geteilt. Der ganze physische Modellfehler
wird konservativ ebenfalls durch diese positive Gesamtfeaturemajorante bezahlt.
Keine neue Unabhängigkeit von Fehlern wird angenommen.

Mit n_0=nu_0-H_0 w+eta D_0,JJ w erhält man

    z_r <= sqrt(n_0*P n_0)+e_nu+(1+eta)e_D+e_U+e_square <1e-5.

Der Faktor 1+eta ist konservativ. Das Ergebnis kontrolliert das endliche
Feature des GANZEN Residuums; es kontrolliert nicht dessen unendlichen Anteil.

## 4. Restzentriertes Inverslemma ohne skalaren Formboden

Für die unveränderte Unterform gelten unter den gebundenen Voraussetzungen

    H_new=S-A*D_new^-1 A,    S>=beta L,
    R*R_L R <= c beta E_new,
    c=1977/500000, beta=20209999981781/182190000000000.

Abschnitt 2 der gebundenen Inversherleitung gilt für jedes zulässige
L-formdualstetige Funktional, also auch für r=nu-H_new Jw. Er liefert

    <r,H_new^-1 r>
      <= [d/beta+z_r²+2 sqrt(c d/beta) z_r]/(1-c).       (1)

Die Zulässigkeit von r wird nicht aus 84 Koordinaten gefolgert. Die festen
stückweisen Polynom-/Momentliftungen F und Jw haben vollständige q-Abbilder
mit logarithmischen Randgliedern in L². Die Kern-Schnittstellenkopplung g
ist auf dem festen Horizont beschränkt: ihr singulärer grenzüberschreitender
Anteil ist ein Carlemanoperator, der reguläre Kernel ist auf dem kompakten
Gebiet beschränkt, die endlich vielen Primverschiebungen sind beschränkt
und die Momentkorrektur hat endlichen Rang. Mit der gebundenen beschränkten
U8-Majorante folgen damit ganze Hilbertfunktionale für nu und H_new Jw.
Aus L>=21/5 W_X folgt ihre L-Formdualstetigkeit. Dies beweist Endlichkeit,
liefert aber noch keine ausreichend kleine numerische Grenze für d.

Die gemeinsame variationale Identität lautet auf dem ganzen Raum

    <f,Q_new^-1 f>=F(Jw)+<r,H_new^-1 r>.                 (2)

Der neue Kontrollweg wendet (1) auf r an. Die ausgeschlossene feste
Young-Familie aus #248 wandte ihre Abschätzung dagegen auf nu an. Deshalb
widerrufen (1),(2) diesen Ausschluss nicht und widersprechen ihm nicht.

Mit den einfachen rationalen Caps

    F_cap=0.000053941654, z_cap=0.00001, d_cap=0.000000019

prüft audit.py unabhängig, ohne Arb, die strikte Ungleichung

    F_cap+[d_cap/beta+z_cap²+2 sqrt(c d_cap/beta)z_cap]/(1-c)
       < Budget_lo.

Alle Quadratwurzeln werden durch ganzzahlige rationale Obergrenzen ersetzt.
Der Kreuzterm bleibt erhalten. Die endliche Rechnung allein beweist die Voraussetzung d<=d_cap nicht;
ihren vollständigen Nachweis liefert erst Abschnitt 7. Eine zu große spätere Obergrenze wäre wiederum
nur unentschieden; einen Ausschluss braucht eine gesamte Energieuntergrenze.

## 5. Abgrenzung der endlichen Vorstufe

Der neue Lauf benutzt die gebundenen vorhandenen Matrizen und Paarungen.
Die Skalarauswertung wird unabhängig rational geprüft; dies ist kein zweiter
analytischer Beweis und keine externe Prüfung. Ein frischer Replay prüft
die Bytegleichheit der Resultate und die vollständige Dateiherkunft.

Der in Abschnitt 7 nachgelieferte Datensatz ist eine gemeinsame Kontrolle der
Funktional-Differenz nu-H_new Jw auf dem vollständigen T, einschließlich
der Quellen-, Randlogarithmen-, Prim-Schnittstellen- und Modellreste.
Die vollständige L-Dualnorm oder eine ausreichende gemeinsame WX-Restnorm
kann (1) schließen. Einzelne Außenkoordinaten können Hindernisse zeigen,
ersetzen aber keine obere Einschließung des ganzen Restes.

Explorative regulierte Darstellungen in X_ans und Außenpaarungen werden
getrennt von diesem endlichen Zertifikat geführt. Keine automatische
Übertragung ihres Modellwerts in die offene Größe d.

## 6. Ganze Quellenwirkung mit D-Normierung

Die vorhandene Antwortidentität lautet `A_force*=S J X_ans+R` mit
`R*R_L R <= c beta E_new`. Setze

    P_D = X_ans D_new^-1 X_ans*.

Die beiden Diagonalblöcke von D_new sind `(1-rho) I_191` und K_new.
E_new und X_ans werden aus den exakt rationalen, gebundenen Matrizen aus #250
rekonstruiert. Insbesondere wird KEINE Ordnung E_new<=D_new vorausgesetzt.
Die Hilbert–Schmidt-Ungleichung gibt auf dem vollständigen Raum

    ||R_L^(1/2) A_force* D_new^-1/2||
      <= ||R_L^(1/2) S J P_D^(1/2)||_HS
         +sqrt(c beta tr(D_new^-1 E_new)).                  (3)

Schreibe `S=(1-eta)q-H_high` mit der gebundenen Ungleichung
`0<=H_high<=h L`, `h=16198/18219`. Daraus folgt
`H_high R_L H_high<=h H_high`. Der gemeinsame U8-Quellengram einschließlich
seines bisherigen Fehlers begrenzt `J*H_high J` von oben. Für den q-Anteil
benutzen wir `L>=21/5 W_X` und die vollständigen physikalischen Q-Abbilder.

Auf der Schale werden der D_H-Anteil mit den Eigenwerten H_n und der
Multiplikationsanteil
`v(t)=-log(2 pi)-Euler-log(hs)-log(t)/2-log(1-t)/2`
getrennt durch Hilbert–Schmidt-Normen
begrenzt. Für v² ist die gemeinsame Polynomdichte `J P_D J*` maßgeblich.
Mit N=n+1 sind die benutzten exakten Momente auf [0,1]

    int t^n log(t) = -1/N²,
    int t^n log(1-t) = -H_N/N,
    int t^n log²(t) = 2/N³,
    int t^n log²(1-t) = (H_N²+H_N^(2))/N,
    int t^n log(t)log(1-t)
      = H_N/N²-(pi²/6-H_N^(2))/N.

Der reguläre Kernel wird durch den absoluten Koeffizientenpreis des
gebundenen Grades 224 plus dessen vollständigen Rest auf |z|<=11/10
eingeschlossen. Der berechnete Preis ist <0.605; benutzt wird konservativ 2.
Der grenzüberschreitende singuläre Operator hat Norm höchstens pi/2
(Carleman), der reflektierte Anteil höchstens sqrt(hs/a8)/2. Die beiden
regulären Anteile kosten höchstens `4 sqrt(a8 hs)`, die endlich vielen
Primverschiebungen höchstens `2 sum log(p)/sqrt(n)`. Zusammen ergibt dies
eine Kopplungsnorm <9.023.

Für den Momentlift wird die ganze Norm `||Q8 m||<100` verwendet, nicht die
Norm eines eingeschränkten Kerns. Der Code begrenzt den D_H-Anteil durch
den Differenzenquotienten und `sup|m'|`, den Potentialanteil durch seine
Log-L²-Normen und die übrigen Teile durch die vollständigen Kernel- und
Primoperatornormen. Das Ergebnis ist <23.401. Dieselben Ungleichungen und
die Polynom-Abschätzung `||p||_infty <=96 ||p||_X/sqrt(2 hs)` ergeben auf
dem gesamten lokalen Grad-95-Raum eine Q-Norm <191.701. Für die geerbte
J-Koordinatenrundung wird zusätzlich der gröbere Faktor 10000 bezahlt.

Die gerichtete Auswertung liefert

    tr(D_new^-1 E_new) <200.656,
    ||Q Lambda J P_D^(1/2)||_HS <10.500,
    ||R_L^(1/2) S J P_D^(1/2)||_HS <5.754,
    ||R_L^(1/2) A_force* D_new^-1/2|| <6.051 <10.

Die einfachen Caps werden im rationalen Endpunktaudit erneut geprüft.
Dieser Transport gilt für alle 203 Quellen gemeinsam. Er begrenzt keine
noch nicht bezahlte Modellabweichung automatisch: deren D-Norm muss zuerst
bestimmt werden. Das vollständige Restfehlerinventar wird in Abschnitt 7 separat bezahlt.

## 7. Vollständiger Vergleich am festen geraden Zeugen

Die [analytische Restherleitung](whole/ANALYTIC_CAPS.md) und die eingefrorenen
Quellen unter whole/ rekonstruieren die ganze Funktion r. Alle Prim-Schnittstellen,
logarithmischen Ränder, Quellen- und Modellfehler bleiben enthalten. Es wird
weder eine 84-Koordinatennorm noch ein Netzunterschied zur Ganzrestobergrenze
erklärt. Der vollständige Erstlauf und der reine rationale Endpunktaudit liefern

    ||r_model||_X² < 1e-10,
    e_bridge,X < 1e-20,
    e_core,X < 1e-7,
    e_operator,Ldual < 1e-5,
    d=<r,R_L r> < 1e-9.

Die tatsächlichen engeren rationalen Endpunkte stehen in
[whole/WHOLE_RESULT.json](whole/WHOLE_RESULT.json). 411 analytische
Taylorabschnitte und zwei explizite logarithmische Randintegrale überdecken
die gesamte äußere Schale. Der gemeinsame Quellenoperator kostet <10 in
D-Normierung; der rohe Kern-Schalenoperator einschließlich Momentlift <100.
Die vollständige Kernquadratur und der gerichtete Vergleich der beiden
endlichen Kernmodelle sind gesonderte Preise. Insbesondere ist das kleine
Modellresiduum nicht ungeprüft mit dem tatsächlichen Residuum gleichgesetzt.

Mit d_cap=1e-9, F_cap=0.000053941654 und z_cap=0.00001 ergibt (1),(2)
einschließlich des positiven Kreuzterms für die feste Schalenrichtung
z_fixed und ihr Residuum f=(C-D_hat T)z_fixed

    <f,Q_new^-1 f> < 53.950924907669e-6
                   < 54.117169360708e-6 < K_P[z_fixed].

Der sichere Abstand ist größer als 0.166244453040e-6, also rund 0.307 %
der Budgetuntergrenze. Diese Anzeigen sind nach außen gerundet. Maßgeblich
sind die exakten rationalen Endpunkte des gemeinsamen Ergebnisses.

**FIXED_EVEN_RESIDUAL_CENTERED_COMPARISON_PASS**, unter sämtlichen gebundenen
Voraussetzungen. Dies ist ein vollständiger oberer Vergleich an genau einem
unveränderten physischen geraden Zeugen. Es ist kein N12-Abschluss und keine
Aussage über alle Richtungen des Grad-11-Raums, die andere Parität oder eine
kofinale Fortsetzung. Die ausgeschlossene feste Young-Familie aus #248 und
der ungeeignete exakte E-Transport aus #250 bleiben ausgeschlossen bzw.
ungeeignet; hier wird ihre Anwendung auf nu durch eine gemeinsame Kontrolle
von nu-H_new Jw ersetzt. Die äußere Antwortregel wurde nicht geändert.

Der Abnahmebeleg trennt vollständige numerische Reproduktion, den schnellen
gebundenen Endpunktaudit, Tests, Git-Integration und externe Prüfung. Ein
laufender oder fehlgeschlagener Replay gilt nicht als bestanden.
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN bleibt bestehen.
