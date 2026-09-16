# A1-COMP — eingefrorene Statuskapsel

**Stand:** 16. September 2026. **Zweck:** konditionaler Import für neue Forschung, kein weiterer Audit.

```text
A1-COMP@0a7c970 / AUTHOR-VERIFIED / EXTERNAL-OPEN
Full SHA: 0a7c970fc5983c9c198915e2c7c1f6280834b13a
Model/main anchor: ac164bbbd2c46623aa64e567d21f813f41f164b0
```

## Aussage und genauer Scope

Der vollständige Autorennachweis behauptet für den beschränkten Vergleichsoperator
auf `L²(-1,1)`:

```math
L_1\succeq9\cdot10^{-36}I.
```

Die kanonische Completion erfüllt auf ihrem Formbereich `mathfrak A_1 >= L_1`.
Wegen `mathfrak A_1[v]-Q_W[v]=|E_+(v)-E_-(v)|²` überträgt sich die Schranke
auf die ursprüngliche Weil-Form für NULLPOL und gerade glatte Testfunktionen
mit Träger in `(-1,1)`, durch Einschränkung ebenso für `0<a<=1`.

**Nicht importiert:** allgemeine ungerade Weil-Positivität; irgendeine Aussage
für `a>1`; all-window NP-GAP; Objekt X; RH; Neuheit; externe Freigabe.
Es handelt sich um einen genau referenzierten Autorennachweis mit rigorosen
numerischen Imports, nicht um einen unabhängig extern freigegebenen Satz.
Ein Folgeargument, das A1-COMP benötigt, trägt denselben Vertrauensvorbehalt.

## Primäre Evidenz — verweisen, nicht neu kopieren

- [Draft-PR #131](https://github.com/Waschtl904/objekt-x-programm/pull/131).
- [Eingefrorener Zweipass-Audit, vollständiger Text](https://github.com/Waschtl904/objekt-x-programm/blob/0a7c970fc5983c9c198915e2c7c1f6280834b13a/audits/P11_A1_COMPOSITION_TWO_PASS_2026-09-15.md).
- [Commitgebundenes COMMENT-Review 5218037890](https://github.com/Waschtl904/objekt-x-programm/pull/131#pullrequestreview-5218037890): kantenweises E/V/I-Gutachten, ausdrücklich derselbe Autor, kein APPROVE.
- [Proposal-Identität, Run 35005611795](https://github.com/Waschtl904/objekt-x-programm/actions/runs/35005611795), Codehead `9e7b570e755e76adce16596348312d26410403ac`.
- [Rationale Reparaturen/Provenienz, Run 35007018039](https://github.com/Waschtl904/objekt-x-programm/actions/runs/35007018039), Codehead `4a2ee118d2a12e945e505a8a76404aa72931cc5b`.

Historische Inputs bleiben namentlich dieselben: reeller Multiplikator
`34921767085`; Legendre-Tail `34921767091`; Quadratur `34921767108` mit
dokumentierter Ergänzung; Knotenenclosures `34921767233`/`34921767203`;
Dyaden `34921767182`/`34921767282`; Odd-Rebuild `34921767177`;
LDL `34921767230`/`34921767303`. Details, Prüftiefen, Datei-/Matrix-/ZIP-Hashes
und Original-Artefakt-IDs stehen in den beiden primären Gutachten.

Die im Gespräch bereitgestellten Pakete heißen
`A1_Kompositionsaudit_2026-09-15.zip` und
`A1_Exact_Head_Gutachten_2026-09-16.zip`.
Dies sind Gesprächsartefakte, keine behaupteten GitHub-Release-Assets.
Der zweite Pakettext `EXACT_HEAD_EDGE_REVIEW.md` liegt nicht als Datei in
PR #131; sein commitgebundener GitHub-Einstieg ist das COMMENT-Review oben.
Actions-Artefakte können ablaufen; ihre Verfügbarkeit wird hier nicht als dauerhaft garantiert.
Der Dokumentationshead wird nicht nachträglich als Head der früheren CI-Läufe bezeichnet.

## Stop-Regel

**Kein weiterer Selbstaudit von PR #131**, außer bei (1) geändertem Review-Head,
(2) konkreter externer Beanstandung einer Kante, (3) echtem Mehrbedarf eines neuen
Satzes über den dokumentierten Scope hinaus oder (4) Ausfall eines historischen
Imports beziehungsweise seiner Provenienz. Ein fehlender externer Reviewer
allein ist kein Anlass für einen weiteren Selbstaudit. Ein Wiederöffnen nennt
zuerst den konkreten Auslöser und die betroffene Kante.

Die SHA-Bindung fixiert den Inhalt; sie behauptet keine administrative
Unveränderlichkeit des Branches oder von GitHub-Kommentaren. Neue externe
Ergebnisse werden als neue Statusversion referenziert, nicht rückwirkend als
Bestandteil dieses Imports ausgegeben.

## Arbeitsteilung

PR #131 bleibt unverändert und extern review-offen. X-C0 arbeitet auf einem
separaten Branch von `main`, ohne Cherry-pick/Merge von #131 oder #116/#127.
Registry und main werden durch diese Statuskapsel nicht promoviert.
Der erste Kandidateneinstieg ist [`../../X_CANDIDATE_C0_SPEC.md`](../../X_CANDIDATE_C0_SPEC.md).
