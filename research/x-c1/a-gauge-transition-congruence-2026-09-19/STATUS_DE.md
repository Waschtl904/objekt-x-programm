# A-Gauge-Uebergang und exakte Blockkongruenz

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 19. September 2026.

Der eingefuegte Review bezog sich auf d145ba88. Inzwischen liegen der
A-Gauge-Koordinatensatz (4ab3341) und der gesamte Core-Gate auf dem sehr
kleinen Fenster h<=2^(-10^16) (04bc246) vor. Beide bleiben erhalten.

Dieses Paket ergaenzt fuer das gesamte bisherige Fenster 0<h<=10^-20:

- eine explizite inverse Formel fuer T_A zwischen den beiden reduzierten
  Koordinatenraeumen, mit dem korrekten Pluszeichen im Shellanteil;
- ||x||^2/3 <= ||T_A x||^2 <= 3111^2 ||x||^2 und
  ||T_A^-1|| <= sqrt(3) < 2;
- Erhaltung der gesamten geschlossenen Formbereiche und der gekoppelten
  H1-Spurbedingung;
- exakte Blockkongruenz und R_0[w]=R_A[P_A w];
- eta_(v,A)<7.55e-6 fuer die festgelegte Richtung mit voller Shellantwort.

Es wird keine neue Quelle gewaehlt und kein neuer Richtungs-Riesz-Solver
gerechnet. Der A-Gauge-Quotient folgt gerichtet aus dem vorhandenen
Residualzertifikat. Die physische Quelle bleibt unveraendert.

Fuer das vollstaendige a_A-orthogonale Komplement Z_A ist die genaue
Restaufgabe angegeben: Ein uniformer Kopplungsbound kappa_* mit
kappa_*+7.55e-6<1 genuegt, weil auch alle gemischten Beitraege kontrolliert
werden. Beispielsweise wuerde kappa_*<=0.999 den Gesamt-Gate schliessen.
Dieser Komplementbound ist auf dem vollen Fenster NICHT bewiesen.

Damit bleibt das volle Fenster h<=10^-20 UNDECIDED. Der bereits bewiesene
Even-All-Source-Satz mit physischem Gap >10^-17 gilt unveraendert auf
h<=2^(-10^16). Odd-Fortsetzung und groessere Fenster bleiben offen.

Der Checker bindet 65 Dateien, reproduziert das vorige 40-Pruefungen-Paket
einschliesslich seiner 31/28/43/9 Voraussetzungen und prueft die neuen
rationalen Konstanten und Identitaeten. Dies ist kein externer Audit.
Append-only auf der Forschungsbranch, keine Aenderung an main oder
Vorgaengerpaketen, kein PR und kein Merge.
