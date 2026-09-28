# Abgleich mit dem zwischenzeitlichen Main-Commit

27. September 2026 · Abgrenzung der lokalen A9-Rechnung

Die lokale A9-Arbeit verwendet die fest gebundenen Eingaben auf Basis
`69eb8773acd483978e2453019d1e2d5cf009a990`. Während der Rechnung wurde
[PR #176](https://github.com/Waschtl904/objekt-x-programm/pull/176) außerhalb
dieser Arbeit integriert. Main wurde anschließend als
`a77950be027dc1576b016c6a53bfad7ff65a04e4` gelesen.

Der vollständige Diff wurde gelesen und als `inputs/PR176_REVIEWED.diff`
gespeichert. Der Vergleich enthält fünf geänderte Dateien; keine der sieben
mathematischen Eingaben, vier Programmquellen oder der gebundenen
O8-Schurbrücke ist darunter. Die Commit- und Dateibindungen stehen in
`MAIN_COMPATIBILITY.json`.

## Spektralorientierung

PR #176 korrigiert bei der positiven Fourierkonvention den Zusammenhang
zwischen `−i d/dx` und dem Spektralparameter: Der Multiplikator ist −t.
Die C1a-Familie und O1–O4 legen dagegen ausdrücklich die unitäre Konvention
`F₋u(ξ)=(2π)^(−1/2)∫e^(−ixξ)u(x)dx` fest. Unter dieser Konvention entspricht
`−i d/dx` dem Multiplikator ξ.

Auch ein konsistenter Wechsel zwischen den beiden Fourierkonventionen
ändert die betrachtete Form nicht: `F₊u(ξ)=F₋u(−ξ)`, und sämtliche hier
benutzten Symbole sind gerade. Dies gilt für die volle Gamma-Reihe in ξ²,
die Prime-Summen aus cos(log(q)ξ) sowie m, n und h. Durch die Substitution
ξ↦−ξ bleiben die gewichteten sesquilinearen Integrale für beliebige
komplexe Quellen erhalten. Eine Geradheit der Quelle wird dafür nicht benötigt.

Die A9-Engine arbeitet direkt mit der physischen Referenzform
`D_H+V+q₀−K−S`; sie verwendet keine rohe unsymmetrisierte Realisierung
`γ∞(H∞)` aus den korrigierten PD-4-Dokumenten.

## Logarithmischer Koordinatenwechsel

PR #176 berichtigt den Lift zu `g(u)=e^(u/2)h(e^u)`, passend zu `x=e^u`.
Die vorliegende C1a-Familie ist bereits unmittelbar auf der additiven
physischen Achse definiert: Momente `∫u(x)e^(±x/2)dx`, Verschiebungen
`log(q)` und Skalierung `U_Au(ξ)=sqrt(2A)u(Aξ)`.
Die irrtümliche Ersetzung `h(e^(u/2))` wird in diesen Definitionen,
dem Gamma-Kern und der A9-Rechnung nicht verwendet. Der gelesene Patch
ändert zudem die Masterform und ihre Pol-, Gamma- und Prime-Blöcke nicht.

## Konsequenz für diese Arbeit

Der lokale Beweis und die gespeicherten A9-Matrizen behalten ihre konkrete
Bedeutung. Ihr Verifikationsanker wird durch den späteren Main-Commit nicht
verschoben. Die lokale Arbeitskopie wurde für diesen Abgleich nicht geändert.

Dieser Abgleich betrifft die Kompatibilität des A9-Pakets. Er behauptet keine
neue vollständige Abnahme der übrigen Resultate aus PR #176 oder der globalen
Weil-Identifikation.
