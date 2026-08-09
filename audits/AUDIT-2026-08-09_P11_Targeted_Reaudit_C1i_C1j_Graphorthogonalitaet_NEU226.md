# P11 — Targeted Reaudit C1i/C1j: Graphorthogonalität nach NEU-226

**Datum:** 9. August 2026  
**Betroffene Knoten:** P11-C1i, P11-C1j  
**Auslöser:** Gegencheck gegen `KONVENTIONEN.md`, NEU-226 und eingefrorenes P05  
**Präzedenz:** Dieser Targeted-Reaudit supersediert ausschließlich die unten bezeichneten Orthogonalitäts-/Kettennormbehauptungen aus C1i/C1j. Alle nicht betroffenen Teile bleiben erhalten.

**Urteil:**

\[
\boxed{\text{C1i/C1j PARTIAL SUPERSEDING — globale Graphorthogonalität war zu stark.}}
\]

---

## 1. Verbindlicher späterer Endstand

NEU-226 rollt die frühere globale Orthonormalitätskonvention der `\eta`-Familie ausdrücklich zurück. Verbindlich ist nach `KONVENTIONEN.md` und P05:

\[
\boxed{
\langle\eta_{p;m;r,u},\eta_{p;m;r',u}\rangle=\delta_{rr'}
}
\]

nur **innerhalb einer festen Kette bei festem `(p,m,u)`**.

Über verschiedene `(p,m,u)` hinweg ist das Skalarprodukt nicht durch eine globale Kronecker-Delta-Regel festgelegt; verschiedene Kanalbilder können überlappen.

Damit ist die frühere Festlegung

\[
\delta_{pp'}\delta_{mm'}\delta_{rr'}\delta_{uu'}
\]

`SUPERSEDED`.

---

## 2. Betroffene Aussage in C1i

C1i wählte für die Prime-Power-Kette

\[
e_{p,j}\in\mathcal H_{p^j\to p^{j+1}}
\]

und behauptete für verschiedene `j` automatisch

\[
\langle e_{p,i},e_{p,j}\rangle=\delta_{ij}
\]

aufgrund einer global orthogonalen Graphsumme.

Das ist im späteren Endstand **nicht** gerechtfertigt, weil beim Übergang `j\mapsto j+1` gerade die Fasernummer `m=p^j` wechselt. Die Vektoren liegen also nicht in derselben festgehaltenen `(p,m,u)`-Kette, für die die verbliebene Orthonormalität gilt.

Daher sind folgende C1i-Formeln in der dortigen Allgemeinheit `SUPERSEDED`:

\[
\|\chi_{p,k}\|^2=1
\quad\text{für}\quad
\chi_{p,k}=\frac1{\sqrt k}\sum_{j=0}^{k-1}e_{p,j},
\]

und

\[
\langle\chi_{p,k},\chi_{p,\ell}\rangle
=\frac{\min(k,\ell)}{\sqrt{k\ell}}.
\]

Sie gelten nur unter einer **zusätzlichen** Orthogonalitätsannahme für die gewählten Kantenvektoren, die P05 nicht liefert.

---

## 3. Was von C1i erhalten bleibt

Der Primclock-Befund bleibt typologisch erhalten:

Wenn ein nichtnuller Kettenvektor `x_{p,k}` vollständig im algebraischen `p`-markierten Clocksektor liegt und

\[
T_{rel}x_{p,k}=\log p\,x_{p,k},
\]

dann gilt nach Normierung

\[
\widehat x_{p,k}:=\frac{x_{p,k}}{\|x_{p,k}\|}
\]

formal

\[
\langle\widehat x_{p,k},T_{rel}\widehat x_{p,k}\rangle=\log p.
\]

Setzt man danach

\[
\eta_{p,k}:=p^{-k/4}\widehat x_{p,k},
\]

so folgt algebraisch

\[
\boxed{
\langle\eta_{p,k},T_{rel}\eta_{p,k}\rangle
=\frac{\log p}{p^{k/2}}.
}
\]

Damit bleibt die Aussage erhalten:

\[
\boxed{
\text{Der verbotene Faktor }k\log p\text{ ist nicht zwingend; ein normierter }p\text{-Clockzustand trägt }\log p.
}
\]

Aber die konkrete gleichgewichtete Kette `1/\sqrt k` ist **nicht kanonisch hergeleitet**.

---

## 4. Neuer Status des Prime-Power-Kettenlifts

Der korrekte Kandidat lautet nur noch abstrakt:

\[
\boxed{
0\neq x_{p,k}\in\mathcal K_{p,k}^{\rm chain},
\qquad
T_{rel}x_{p,k}=\log p\,x_{p,k},
\qquad
\eta_{p,k}=p^{-k/4}\frac{x_{p,k}}{\|x_{p,k}\|}.
}
\]

Offen sind:

1. die intrinsische Definition des Kettenunterraums `\mathcal K_{p,k}^{chain}` im späteren Grammodell;
2. die kanonische Auswahl der Richtung `x_{p,k}`;
3. die Gramwerte zwischen verschiedenen Exponenten;
4. die Gramwerte zwischen verschiedenen Primlabels.

Damit wird C1i von einem konkreten Ketten-Gramresultat auf einen **typkorrekten normierten Clock-Ansatz** zurückgestuft.

---

## 5. Betroffene Aussage in C1j

C1j formulierte stellenweise, die rohen markierten Graphzustände seien für `p\neq q` aufgrund der Graph-Direktsumme orthogonal.

Diese Aussage ist nach NEU-226/P05 ebenfalls zu stark.

Korrekt ist:

- die **historische kantendiagonale Hebung** `Wres_rel` aus NEU-044-x3 setzt verschiedene Kantenlabels definitorisch orthogonal;
- der **spätere globale P05-Gramstand** tut dies nicht generell;
- verschiedene Primkanalbilder können nichttrivial überlappen.

C1j bleibt jedoch in seinem Haupturteil gültig, weil NEU-250j separat beweist:

\[
\boxed{
\text{direkte Kreuzprimkollision }pm_p=qm_q
\text{ lebt auf }\Lambda=0\text{-Mischträgern}.
}
\]

Daher ist die direkte `pq`-Kollision auch nach Rücknahme der globalen Orthogonalitätsbehauptung **nicht** bereits die gesuchte Weil-gewichtete Prime-Power-Kopplung.

---

## 6. Drei nun strikt getrennte Gramtypen

P11 muss ab jetzt unterscheiden:

### G1 — Historischer orthogonaler Graphlift

Definitorische Kantenorthogonalität aus NEU-044-Variante B. Clock-kompatibel, aber nicht intrinsisch hergeleitet.

### G2 — Kollabierter Pullback-`Wres`

Kann `pq`-Kreuzüberlappung besitzen, verliert aber Kantenmarkierung/Clock-Funktorialität.

### G3 — Späterer globaler P05-Gramstand

Über verschiedene `(p,m,u)` hinweg nicht allgemein orthogonal; Primkanalbilder können überlappen. Die konkrete intrinsische Gramform und ihr Prime-Power-Restriktionskern sind jedoch nicht vollständig kanonisiert.

Nur G3 ist als Ausgangstyp für P11 aktuell kompatibel mit dem eingefrorenen P05-Endstand.

---

## 7. Konsequenz für `C_R^{can}`

Der frühere C1i-Schluss

\[
\text{„roher Graph liefert blockdiagonales }C_R\text{“}
\]

ist `SUPERSEDED`.

Ebenso folgt aber aus P05 nicht automatisch eine explizite kanonische Matrix

\[
C_R^{can}=(c_{\alpha\beta}).
\]

Der aktuelle Stand ist stärker und zugleich offener:

\[
\boxed{
\text{Nichtorthogonalität ist strukturell möglich/teilweise gesichert,}
\quad
\text{aber ihre intrinsische Prime-Power-Labelmatrix bleibt zu bestimmen.}
}
\]

---

## 8. Statusreconciliation

| Aussage | Korrigierter Status |
|---|---|
| globale `eta`-Orthonormalität über verschiedene `(p,m,u)` | `×[M] / SUPERSEDED` |
| Orthonormalität innerhalb einer festen `(p,m,u)`-Kette | `✓[M]` |
| `1/sqrt(k)`-Prime-Power-Kettennorm folgt aus P05 | `×[M]` |
| `min(k,l)/sqrt(kl)`-Exponentkernel folgt aus P05 | `×[M]` |
| normierter `p`-Clockzustand trägt Erwartung `log p` | `✓[M]` im Clock-Scope |
| Skalierung `p^{-k/4}` reproduziert danach das arithmetische Halbgewicht | `✓[M]` algebraisch |
| globale Primkanalorthogonalität | **nicht bewiesen; P05 erlaubt Überlappung** |
| direkte `pq`-Kollision = gesuchte Weil-Kopplung | `×[M]` durch Trägertrennung |
| intrinsische Prime-Power-Label-Grammatrix | `?[O]` |

---

## 9. Präzedenzvermerk

Für P11 gilt ab jetzt:

```text
P11 Targeted Reaudit C1i/C1j (dieses Dokument)
    > P11-C1i / P11-C1j Orthogonalitätsformulierungen
    > historisches NEU-043/044 Graph-Direktsummenbild.
```

Die C1c/C1d-Inzidenzgeometrie auf der analytischen `U_t`-Quelle ist von diesem Reaudit **nicht betroffen**, da ihre Positivität direkt aus dem gemeinsamen `L^2`-Translationsraum folgt und keine `eta`-Graphorthogonalität benutzt.

---

## 10. Nächster Knoten

Der geplante Mediator-Audit C1k bleibt sinnvoll, wird aber mit korrigierter Ausgangslage formuliert:

\[
\boxed{[P11\text{-}C1k]\quad\text{Kann BC-/adelische Multiplikation eine kanonische Prime-Power-Label-Gramform erzeugen, statt nur direkte Kollisionsüberlappung?}}
\]

Dabei wird **keine** globale Graphorthogonalität mehr vorausgesetzt.
