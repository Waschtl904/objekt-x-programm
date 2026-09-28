# A11: dritte Kammer lokal positiv zertifiziert

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN · Lokales Forschungspaket**

Am Terminal A11=log(11)/2 sind die sieben Kanäle 2,3,4,5,7,8,9 aktiv.
Die vollständig bezahlten Schur-Untermatrizen bestehen in beiden Paritäten
nach einer exakt rationalen Basisänderung die gerichtete Arb-Prüfung und
die unabhängige Ganzzahl-Intervallprüfung: **jeweils 285 von 285 strikt
positive Pivots und 285 positive Gershgorin-Zeilenmargen**.

Mit der dokumentierten analytischen Anbindung folgt auf den vollständigen
ursprünglichen Zwei-Mellin-Quellenräumen für alle 1≤A≤A11

\[
\boxed{q_A[u]\ge10^{-50}\|u\|^2,\qquad
G_A\succeq\frac1{13\cdot10^{50}+1}I.}
\]

Die exakten rationalen Untergrenzen stehen in den Ergebnisquittungen.
Die Anzeigen der unabhängigen Rechnung lauten:

| Parität | Physischer unterer Boden, gerundete Anzeige |
| --- | --- |
| Gerade | `6.465650337132697300066E-50` |
| Ungerade | `2.661882688244636626738E-46` |

## Die neue analytische Verbesserung

Die positive Randkomponente V wird gemeinsam mit allen Shiftbeiträgen
abgeschätzt. Für jede Quelle gilt die Differenzidentität

\[
\int r_A|f|^2d\mu-\langle f,S_Af\rangle
=\sum_q w_q\int_{-1}^{1-d_q}|f(x+d_q)-f(x)|^2d\mu(x)\ge0.
\]

Auf den acht A11-Zellen liefert dies S_A−V≤59/20. Der größte rigorose
Zellbound liegt unter 2.946612. Mit Gamma- und Konstantenverlust ist der
Gesamtverlust 14811/2500. Die hohen Grade 572/573 liefern den vollständigen
physischen High-Floor **1**, Defektboden **1/14** und Kodimension **285**.

Damit benötigt diese Rechnung trotz des größeren Fensters weniger niedrige
Koordinaten als die frühere A9-Rechnung mit 296. Das kommt von der neuen
Abschätzung; es behauptet keine monotone Abnahme notwendiger Dimensionen.

## Tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| Neue Tail-/Zell-/Moment-/Quellenkontrollen | **187** bestanden, darunter sieben Git-Bindungen |
| Neue Geometrie, unabhängige Integralzusammensetzung bei N15/M16 | **245** Vergleiche bestanden |
| Vollständiger Integralaufbau | N571, Gamma M416, 3072 Bit, sieben Kanäle, acht Zellen |
| Arb-Zertifikat nach rationaler Kongruenz | 21 Prüfgruppen; 285 positive Pivots und Zeilenmargen je Parität |
| Standardbibliothek-/Ganzzahlzertifikat mit selbst berechneter Kongruenz | 47 Prüfgruppen; 285 positive Pivots und Zeilenmargen je Parität |

Der Gammafehler ist auf Radius 6/5 neu bezahlt: Kernelobergrenze rund
4.794·10^−50. Die Grams enthalten die gesamte unendliche hohe Modellantwort,
einschließlich V², S² und aller Kreuzterme. Der Gamma-Polynomanteil reicht
bis Grad 988; diese endliche Polynomstütze ist keine Trunkierung des hohen
Quellenraums. Hohe Mellinkorrektur und Normumrechnung sind ebenfalls bezahlt.

## Bedeutung für die Fortsetzung

Das allgemeine Wandlemma liefert zusammen mit dem neuen vollständigen
Terminalboden die korrigierten isometrischen Transporte und deren Cocycle
für alle **1≤A≤B≤C≤A11**, über die q8- und q9-Wand hinweg.

Der zusätzliche [allgemeine Tail-Satz](GENERAL_TAIL_PRINCIPLE.md) zeigt:
Auf jedem festen endlichen Horizont lässt sich durch einen hinreichend
hohen Schnitt ein positiver vollständiger Tail gewinnen. Die nötige
Kodimension darf wachsen. Der offene allgemeine Engpass ist die Positivität
des verbleibenden niedrigen Schurrests.

Die dritte positive Kammer beendet diese Frage nicht. Eine unbeschränkte
positive Horizontfamilie, die vollständige globale Objekt-X-Konstruktion
und RH bleiben offen. Die nächste aktivierende Wand liegt bei q=11;
eine neue vierte Terminalpositivität wird in diesem Paket nicht behauptet.

## Beweis und Prüfgrenzen

- [Analytischer Beweis und vollständiges Fehlerbudget](PROOF.md)
- [Rationale Basisänderung, Intervallproblem und vollständige Normrückrechnung](PRECONDITIONING.md)
- [Prüfumfang und externe offene Abnahme](AUDIT.md)
- [Abgleich mit den aktuellen Repository-Korrekturen](MAIN_CHECK.md)

Die analytische Herleitung bleibt **EXTERNAL_REVIEW_OPEN**. Die zweite
Arithmetik reproduziert die Zertifikate aus den gelieferten Matrixintervallen;
sie ist keine externe Prüfung sämtlicher analytischer Argumente.

Die erste direkte Intervall-LDL war nach 43 bzw. 46 Pivots unentschieden.
Die Eingangsintervalle wurden deshalb durch eine exakt invertierbare rationale
Basisänderung geprüft. Beide Arithmetiken wenden diese auf die vollständigen
ursprünglichen Intervalle an; der Gershgorin-Boden wird mit der exakt berechneten
Frobeniusnorm von P in die ursprünglichen Koordinaten zurückgerechnet. Die
erste fehlgeschlagene Prüfung und ihre Diagnosen bleiben vollständig erhalten.
Ein separat reproduzierter NaN-Randfall beim Quadrieren nullzentrierter
Arb-Balls wird im neuen LDL-Prüfer durch einschließende Multiplikation vermieden.

Die Tail-Quittung CHECK_RESULTS.json wurde vor dem Matrixlauf erzeugt.
Ihre Markierung `full_terminal_positivity: OPEN` beschreibt ausschließlich
ihren damaligen Prüfumfang. Der abschließende Ergebnisstand steht hier,
in PACKAGE_STATUS.json und den späteren Reservequittungen.

## Reproduktion

Python 3.13; für die Arb-Schritte python-flint==0.9.0. Die unabhängige
Ganzzahlprüfung und der Tail-Prüfer benötigen nur die Standardbibliothek.
Die folgenden Zertifikatsschritte bitte in einer frischen entpackten
Arbeitskopie ausführen: Sie erneuern die Kongruenz- und Reservequittungen.
Das Original-ZIP und sein Manifest bleiben damit als Referenz erhalten.

```text
python check_tail.py --output replay_tail.json
python certify_preconditioned.py
python common_reserve.py
python verify_integer_a11.py --output replay_integer.json
python check_normalization_a11.py --model normalization_model.json.gz --output replay_normalization.json
```

Ohne Repositorypfad führt check_tail.py 180 Kontrollen aus. Die ursprüngliche
Quittung mit 187 Kontrollen wurde zusätzlich mit `--repository PFAD` erzeugt.
Die unabhängige Ganzzahlprüfung verwendet die aktuellen Quittungen derselben
Arbeitskopie und rekonstruiert die rationale Kongruenz selbst. Der ursprüngliche
direkte Versuch kann mit check_a11.py wiederholt werden; er gilt ausdrücklich
nicht als erfolgreicher Positivitätstest. Für einen vollständigen neuen
Integralaufbau in einer frischen Arbeitskopie:

```text
python generate_a11.py --degree 571 --gamma 416 --precision 3072 --output a11_model.json.gz
python check_a11.py
python certify_preconditioned.py
python common_reserve.py
python verify_integer_a11.py
```

Dies ist lokale Forschung. Dieses Paket wurde hier weder veröffentlicht
noch gemergt. Main, Registry, alte Beweise, Branches und Tags bleiben
unverändert. SHA256SUMS bindet sämtliche Paketdateien außer sich selbst.
