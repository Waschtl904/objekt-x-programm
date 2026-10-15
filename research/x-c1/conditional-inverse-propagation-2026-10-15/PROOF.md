# Bedingte Fortsetzung einer Inversmajorante

15. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

Dieses Hilfslemma überträgt eine vollständige, bereits bewiesene
Residualuntergrenze in eine explizite Inversmajorante. Es beweist weder,
dass die arithmetischen Eingaben diese Untergrenze erfüllen, noch eine
erneuerbare Zertifikatsklasse oder einen neuen Horizont.

## Voraussetzungen

Seien H0 und H1 komplexe Hilberträume mit den angegebenen physischen
Metriken. Alle Adjunkte beziehen sich auf diese Metriken. Es gelten:

1. A ist der selbstadjungierte Operator einer dicht definierten geschlossenen
   Form a auf H0, mit A >= alpha I für ein alpha > 0. Der beschränkte
   selbstadjungierte Operator U erfüllt A^-1 <= U. Damit ist U positiv
   und injektiv; ein positiver unterer Operatorboden für U wird nicht verlangt.
   U^-1 bezeichnet die geschlossene inverse Form mit Domäne ran(U^(1/2)).
2. E ist eine dichte lineare Formdomäne in H1. Die tatsächliche symmetrische
   Form q auf D(a) x E ist geschlossen und nach unten beschränkt und besitzt
   die exakte Darstellung
   `q[x,z] = a[x] + 2 Re <x,Cz> + d[z]`, mit beschränktem C:H1->H0.
   Ihre Geschlossenheit ist eine Voraussetzung, keine Folgerung aus einem
   einseitigen Untervergleich.
3. P:H1->D(A) ist bezüglich der Graphnorm beschränkt. Insbesondere sind
   P und AP beschränkt. Es ist `R=C-AP:H1->H0` der tatsächliche
   Hilbertresidualoperator. Eine lediglich formdualstetige Quelle wird
   hier nicht stillschweigend mit einem Hilbertvektor identifiziert.
4. Auf E sei
   `k[z] = d[z] - 2 Re <Pz,Cz> + a[Pz]`.
   Eine dicht definierte geschlossene Form b mit Operator B >= beta I,
   beta>0, erfüllt E subset D(b) und auf GANZ E
   `k[z] - <Rz,U Rz> >= b[z]`.
5. V ist beschränkt und selbstadjungiert und `B^-1 <= V`.

Insbesondere bleiben alle Nebenbedingungen und der gesamte unendliche
neue Raum in E enthalten. Ein Test auf endlich vielen Richtungen erfüllt
Voraussetzung 4 nicht. Für Formdualresiduen ist ein gesonderter, bewiesener
Energieraumanschluss erforderlich.

## Aussage

Setze H=P+UR. Der Operator Q der tatsächlichen Form q ist strikt positiv
mit beschränkter Inverse. In den Produktkoordinaten H0 x H1 gilt

```text
Q^-1 <= Unew,
Unew = [ U + H V H*    -H V ]
       [   -V H*        V  ].
```

Bei einer beschränkten invertierbaren physischen Koordinatenabbildung
J:H0 x H1 -> Hphys und `Qcoord=J* Qphys J` lautet die physische Ausgabe
`Qphys^-1 <= J Unew J*`. Dies ist eine Kongruenz; nichtunitäre
Koordinatenwechsel dürfen nicht wie unitäre behandelt werden.

## Beweis auf den vollständigen Formdomänen

Die Variationsdarstellung der inversen Form liefert für v in D(a)

```text
u_inv[v] = sup_f (2 Re <f,v> - <f,Uf>)
         <= sup_f (2 Re <f,v> - <f,A^-1 f>) = a[v].
```

Die Suprema laufen über ganz H0. Insbesondere liegt D(a) in D(u_inv).
Diese Formel folgt durch Spektralabschneidung aus der skalaren
Quadratergänzung; sie gilt auch, wenn U keinen positiven unteren Boden hat.
Injektivität von U folgt aus `<f,Uf> >= <f,A^-1 f> > 0` für f != 0.

Der Dreieckswechsel y=x+Pz erhält D(a) x E. Aus der sesquilinearen
Formidentität und Pz in D(A) folgt exakt

```text
q[x,z] = a[y] + 2 Re <y,Rz> + k[z].
```

Da URz in ran(U) subset D(u_inv), ist die folgende Quadratergänzung
domänengültig:

```text
q[x,z] >= ||U^(-1/2)(y+URz)||^2 + k[z] - <Rz,U Rz>
       >= ||U^(-1/2)(x+Hz)||^2 + b[z] =: lower[x,z].
```

Die maximale Domäne der unteren Form ist
`{(x,z): z in D(b), x+Hz in D(u_inv)}`. Unter dem beschränkten
invertierbaren Wechsel T(x,z)=(x+Hz,z) ist sie die Domäne der direkten
Summe u_inv+b. Daher ist lower dicht definiert und geschlossen. Ferner

```text
lower[x,z] >= min(1/||U||, beta) ||T(x,z)||^2
           >= min(1/||U||, beta)/||T^-1||^2 (||x||^2+||z||^2).
```

Für triviales H0 entfällt dessen Summand. Die Domäne von q ist in der
Domäne von lower enthalten. Die ursprüngliche Geschlossenheit von q und
der Untervergleich liefern somit Q>=Lower>0 in Formordnung. Wiederum
variational folgt `Q^-1<=Lower^-1`. Direktes Invertieren des beschränkten
Dreieckswechsels ergibt

```text
Lower^-1 = T^-1 diag(U,B^-1) T^(-*)
         = [ U + H B^-1 H*    -H B^-1 ]
           [    -B^-1 H*        B^-1 ].
```

Der Ersatz B^-1<=V ist gerichtet korrekt, denn

```text
Unew-Lower^-1 = [-H; I] (V-B^-1) [-H; I]* >= 0.
```

Keine nichtkommutierenden Faktoren wurden vertauscht. Die physische
Ausgabe folgt aus `Qcoord^-1=J^-1 Qphys^-1 J^(-*)`.

## Grenze eines gescheiterten Zertifikats

Für `Q=[[1,1],[1,3/2]]`, `A=1`, `U=2` und P=0 ist der gewählte
Restvergleich `3/2-2=-1/2`, obwohl Q positiv ist. Mit P=1 gilt R=0,
k=1/2; das Lemma ist mit B=1/2 und V=2 anwendbar. Ein erfolgloser
Vergleich ist deshalb **CERTIFICATE_FAIL**, kein negativer Zeuge von q.

Ein echter negativer Zeuge ist dagegen eine zulässige Richtung mit
nachgewiesenem q<0. Fehlende Integrale oder Domänenidentifikationen
bedeuten **UNRESOLVED**. **PASS** für einen arithmetischen Schritt verlangt
zusätzlich die konkrete Bilanz, Inversausgabe und Schnittstellenprüfung.

## Herkunft und Prüfung

Die konkrete [A9-Inverserneuerung](../a9-inverse-renewal-2026-10-13/README.md)
enthält bereits ein Residuallemma für ihr eigenes Formdualproblem.
Das vorliegende Hilfslemma isoliert die Hilbertresidualfassung für
nachfolgende Zertifikate; es ersetzt deren konkrete Voraussetzungen nicht.

`verify.py` kontrolliert acht rationale vollständige Blockmodelle sowie
vier Gegenkontrollen: unzureichende Majorante bei positiver tatsächlicher
Form, echte negative Form, unzulässig zu kleine alte Inversmajorante und
falsches Vorzeichen der inversen Kreuzblöcke. Alle Kontrollen sind exakte
Bruchrechnungen. Sie prüfen die Algebra, nicht die unendlichen Domänen
oder tatsächliche Prim-/Gamma-Daten. Der allgemeine Beweis steht oben.
