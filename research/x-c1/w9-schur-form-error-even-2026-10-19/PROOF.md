# Gezielte Formfehlerschärfung des festen geraden Schur-Untertests

19. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Alle Aussagen gelten unter den unveränderten gebundenen Operator-,
Formdomänen-, Quellenmodell- und Integrationsvoraussetzungen.

## 1. Ergebnis und genaue Grenze

Der vorhandene gemeinsame Feature-Fehlergram reicht aus, um den
Formfehlerpreis des a_fin-Quadrats am **unveränderten** rationalen
84er-Vektor von etwa 9.76872333113e-6 auf höchstens
1.7454980553957797e-8 zu senken. Alle übrigen veröffentlichten
Fehlergrenzen bleiben enthalten und unverändert.

Die vollständige gerichtete Untergrenze wird dadurch

\[
\langle f,Q_{\mathrm{lower},*}^{-1}f\rangle
\ge 55.33955587587\cdot10^{-6}
>54.11716937864\cdot10^{-6}\ge K_P[z_{\mathrm{fest}}].
\]

Die exakte rationale Untergrenze minus Budgetobergrenze ist größer als
1.22238649724e-6. Die nach außen gerundete Budgeteinschließung lautet
[54.11716936070,54.11716937864]e-6; `RESULT.json` enthält die exakten
rationalen Endpunkte. Die Verkürzung der Untergrenze oben ist nach unten,
diejenige der Budgetobergrenze nach oben gerundet.

Damit gilt **SCHUR_UNDERFORM_COMPARISON_EXCLUDED**: Jeder obere Vergleich W,
der weiterhin Q_lower,*^-1 <= W erfüllt, überschreitet am festen geraden
physischen Zeugen das unveränderte K_P-Budget. Betroffen sind genau die
festgelegte verstärkte Unterform, die eingefrorene Antwortmatrix und dieser
Vergleich. Andere Unterformen, Antwortmatrizen und Majoranten der tatsächlichen
A9-Inverse werden nicht ausgeschlossen. Es ist insbesondere keine negative
Weil-Richtung. Kein Teilpass, keine Dualreserve, kein Abschluss von N12,
Meilenstein 4 oder Objekt X; externe Prüfung bleibt offen.

## 2. Wiederverwendung und einzige Änderung

Ausgangspunkt ist der veröffentlichte
[Schur-Untertest](../w9-schur-variational-even-2026-10-19/PROOF.md)
am Head `35a74079409c2904e89d7628377eb2e5b1c8dcae`.
Dessen damalige Untergrenze und offener Ausgang bleiben als historische
korrekte, gröbere Abschätzung erhalten. Nur sein Formfehler wird hier
schärfer ausgewertet; es wird kein Fehler der alten Ungleichung behauptet.

Fest bleiben K_*=K+(13/10^8)G_F, der physische gerade Zeuge, die Antwortmatrix,
das separate K_P-Zertifikat und der rational eingefrorene Testvektor t
(SHA-256 `42bbf77a09f2e3f71b4c89cd3ad7c959a8f77fb507d049f3243568b53a2c612b`).
Die exakten veröffentlichten Endpunkte für Basisenergie, Paarung und
diagonalen D/U-Formfehler werden unverändert übernommen. Insbesondere
bleiben der a_fin-Paarungsfehler und der ganze physische Residualfehler
bezahlt. Es gibt keine neue Auswahl, lineare Lösung, Integration oder
RL-Rechnung. Die alten Zertifikate werden als gebundene Voraussetzungen
übernommen; der neue Replay berechnet nur diese Fehlerschärfung.

## 3. Erforderlicher Gewinn

Setze mit den veröffentlichten äußeren Endpunkten

\[
L_{\mathrm{ideal}}=E_{b,-}+2\ell_-
 -(B_{0,+}+e_{D/U,+}-n_{0,-}^2).
\]

Wird der Verlust beim unteren a_fin-Quadrat durch p majorisiert,
so gilt L_new >= L_ideal-p. Bei unveränderten anderen Grenzen ist die
hinreichende Schwelle daher strikt

\[
p<L_{\mathrm{ideal}}-K_{P,+}
 =1.239841477796\ldots\cdot10^{-6}.
\]

Das vorab gesetzte Arbeitsziel 1.23e-6 ist konservativ. Die reine Auswertung
des alten relativen Fehlers in der neuen Richtung ergibt nur
3.06435369202e-6 und wäre noch unzureichend. Der entscheidende zusätzliche
Gewinn kommt aus den bereits vorhandenen einzelnen Feature-Fehlergramen.

## 4. Bilineare Fehlerkontrolle ohne globalen Spurverlust

Schreibe a=a_fin, a0 für sein gebundenes Modell, z=a0 t und r=K_*^-1 z.
Mit d=(a-a0)t gilt exakt

\[
(z+d)^*K_*^{-1}(z+d)
=z^*K_*^{-1}z+2\operatorname{Re}(r^*d)+d^*K_*^{-1}d
\ge z^*K_*^{-1}z-2|r^*(a-a0)t|.
\tag{1}
\]

Der quadratische Fehlerterm ist nicht negativ und wird konservativ
weggelassen. Ein globaler Preis für seine Norm ist somit nicht erforderlich.

Aus dem gebundenen vollständigen direkten Sandwich und dessen unverändertem
relativen Fehler d_D folgt

\[
|r^*(D-D_0)_{FJ}t|
\le d_D\sqrt{r^*G_Fr}\sqrt{t^*G_Jt}=:e_D.
\tag{2}
\]

Für U_actual=Phi*Phi und U0=Phi0*Phi0 zerlegen wir dieselben vollständigen
Features in die F- und J-Quellen. Die vorhandene gemeinsame Fehlermatrix
aus dem [Teilenergiepaket, Abschnitt 4](../w9-partial-energy-2026-10-18/PROOF.md)
ist E=2 diag(E_F+E_hF/delta,(E_J+e_hJ^2/delta)I).
**Der Faktor zwei und die hohe Fehlerüberdeckung werden beibehalten.**
Insbesondere werden keine kleineren reinen F-F-Preise auf F-J übertragen.

Seien

\[
u_F=r^*U_{0,FF}r,\quad u_J=t^*U_{0,JJ}t,
\quad e_F=r^*E_{FF}r,\quad e_J=t^*E_{JJ}t.
\]

Das Ausmultiplizieren von Phi=Phi0+DeltaPhi und dreimal Cauchy–Schwarz ergibt

\[
|r^*(U_{actual}-U_0)_{FJ}t|
\le\sqrt{u_Fe_J}+\sqrt{e_Fu_J}+\sqrt{e_Fe_J}=:e_U.
\tag{3}
\]

Diese Abschätzung setzt weder Unabhängigkeit noch verschwindende
Korrelationen voraus. Die gemeinsamen Grame werden in der konkreten
Richtung ausgewertet, bevor Normen genommen werden. Da a=(D-U)_{FJ},
folgt aus (1)–(3) der gültige Verlustpreis p=2(e_D+e_U).
Die Modell- und Gramintervalle werden mit Arb bei 1024 Bit ausgewertet;
alle Eingaberadien bleiben erhalten. Der veröffentlichte obere Preis wird
zusätzlich auf dem rationalen Raster 10^-24 nach oben gerundet.

| Kreuzfehlerbeitrag vor dem Faktor zwei | Größe ungefähr |
|---|---:|
| voller direkter Fehler e_D | 6.20977504130e-9 |
| Modell-F gegen Fehler-J | 2.51717619752e-9 |
| Fehler-F gegen Modell-J | 5.39038154559e-13 |
| Fehler-F gegen Fehler-J | 4.98523513242e-27 |

Das ergibt p <=1.7454980553957797e-8, etwa 559-mal kleiner als der alte
Formfehlerpreis und deutlich unter dem festgelegten Arbeitsziel.

## 5. Vollständige neue Untergrenze

Mit den unveränderten veröffentlichten Endpunkten und dem neuen Preis gilt

\[
H_*^{neu}[Jt]\le B_{0,+}+e_{D/U,+}-\max(0,n_{0,-}^2-p)=:H_{new,+},
\]
\[
E_{new,-}=E_{b,-}+2\ell_- -H_{new,+}
\le\langle f,Q_{lower,*}^{-1}f\rangle.
\]

Wie zuvor bleibt der positive eta-q-Gewinn ungenutzt. Das Variationsprinzip,
die Formdomäne von Jt, die Positivität von Q_lower,* und seine Beziehung zur
tatsächlichen A9-Form werden unverändert aus den gebundenen Herleitungen
übernommen. Eine obere Grenze der vollen Inversenergie wird nicht behauptet.

## 6. Abnahme und nächster Entscheidungspunkt

`INPUT_BINDINGS.json` bindet die alten Ergebnisse, den unveränderten Vektor,
die alte Engine und deren vollständige Eingabekette. `MANIFEST.json` bindet
das neue Paket. `audit.py` prüft die skalaren Endpunkte unabhängig ohne Arb
mittels Fraction und ganzzahlig eingeschlossener Quadratwurzeln. Es prüft
auch, dass die übrigen Grenzen exakt unverändert geblieben sind.
Der neue Certifier wird aus einem frischen vollständigen Repository-Archiv
bytegleich wiederholt. Quittung und Archivhash stehen in `ACCEPTANCE.json`.
Dieser Replay ersetzt keine unabhängige mathematische Begutachtung.

Der lokale Auftrag ist abgeschlossen. Eine weitere Verbesserung bloßer
Obermajoranten von Q_lower,*^-1 kann diesen festen Vergleich nicht retten.
Der nächste sachliche Entscheidungspunkt betrifft daher eine Änderung der
zugrunde gelegten Unterform oder der eingefrorenen Antwortregel einschließlich
ihres Budgets. Dafür braucht es einen getrennten, begründeten Auftrag;
dieses Paket startet keine weitere Großrechnung.
