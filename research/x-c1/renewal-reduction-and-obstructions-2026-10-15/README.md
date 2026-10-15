# Erneuerungsreduktion und strukturelle Hindernisse (2026-10-15)

**Status:** AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN / PENDING_STATUS_REVIEW. Art: REDUKTION.

## Was dieses Paket ist

Es ist die Antwort auf die Frage, ob sich das Programm über einen echten
Erneuerungssatz abschließen lässt. Die Antwort ist strukturiert negativ
und wird hier präzise gemacht:

| Baustein | Inhalt | Status |
| --- | --- | --- |
| Lemma 1 | Kofinale Positivität auf einer dichten Klasse ist RH (Weil/Yoshida) | bewiesen aus importiertem Satz |
| Lemma 2 | Eingeschränkte Inverse ist monoton: `(Q^-1)_11 >= A^-1`; `Unew >= U (+) 0` | bewiesen |
| Lemma 3 | Wahrer Gap `lambda*(a)` fällt in genesteten Klassen | bewiesen |
| Lemma 5 | Rang-`2m`-Störung mit Trägheit `(m,m)` erzeugt höchstens `m` negative Eigenwerte; RH-Versagen ist endlicher Block (Bombieri) | bewiesen / importiert |
| Satz 4 | Zertifikat `C_n` plus Hypothese `H_n` ergibt `C_(n+1)` mit denselben Konstanten | bewiesen, bedingt |
| `H_n` | Arithmetischer Platzhalter: Residuum, Vergleichsform, Vergleichsinverse, Uniformität | **nicht bewiesen** |

Korollar 2: Die Konjunktion aller `H_n` ist auf der vollen Testklasse
mindestens so stark wie RH. Der Reduktionssatz ist deshalb vom selben
logischen Typ wie Lis Kriterium, eine unendliche Familie expliziter
Ungleichungen. Sein Wert hängt allein davon ab, ob einzelne `H_n` aus
den Kanaldaten beweisbar sind. Das ist offen.

## Was dieses Paket nicht ist

Kein neuer Horizont, kein Beweis von `H_n`, keine Kofinalität, kein
Objekt X, kein RH. Es promoviert keinen bestehenden Status.

## Reproduktion

```bash
python3 research/x-c1/renewal-reduction-and-obstructions-2026-10-15/verify.py
```

Exakte rationale Kontrollen (endliche Modelle): Lemma 2 an fünf
Blockmodellen und einer dreistufigen Kette mit indefiniter
Gegenkontrolle; Struktur von `Unew`; Zeugentransfer für Lemma 3; exakte
Trägheit für Lemma 5 einschließlich scharfer `(2,2)`-Kontrolle;
Spielzeugkette für Satz 4 mit gültigem `H_n` und degenerierter
Gegenkette, in der dieselben Konstanten versagen.

## Dateien

- `PROOF.md` kanonischer Beweistext (SHA-gebunden in `META.yaml`)
- `verify.py` exakte Kontrollen
- `META.yaml` Registerdaten
