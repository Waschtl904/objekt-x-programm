# Promotionsrecord: HT-A4b-SW1-M

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Records:** `main@83e03c6d69ce6dfae2b433977548dd1cd308ebc7`  
> **Gemergter Beweiskandidat:** `audits/P11_R32_HT_A4B_SW1_SELF_CONTAINED_THEOREM_CANDIDATE.md`, Merge-Commit `b06f50f12973e781b87db8b06e54fd590a053b10` (PR #10)  
> **Zweck dieses Records:** kanonische, eigenständige Promotionsbuchung für ausschließlich den in §12 des Kandidatenaudits abgegrenzten Satz.

---

## 1. Was wird promotet

```
HT-A4b-SW1-M
```

unter
\[
0<\sigma\le R<\varepsilon,\qquad R+\varepsilon<\Delta,
\]

exakt der in §12 von `audits/P11_R32_HT_A4B_SW1_SELF_CONTAINED_THEOREM_CANDIDATE.md` formulierte Satz:

1. Für fast jedes \(s\in(R,\varepsilon)\) liegen die sechs Punkte
   \[
   s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s
   \]
   außerhalb aller drei Samplingfenster \((a,b,T)\) — direkte Blindwerte, uniforme Membership \((Z,Z,Z,Z,Z,Z)\).
2. A-Wall-Intervallresultat:
   \[
   I_b\cap I_-=\emptyset,
   \qquad
   I_b\cap I_+\neq\emptyset\iff\varepsilon>\Delta/2,
   \]
   einschließlich des offenen Berührungsfalls bei \(\varepsilon=\Delta/2\) (offener Schnitt leer, Abschlüsse treffen sich in einem Punkt).

Der Beweis ist selbständig: er verwendet HT.17, HT.18, HT.23–HT.27, FG-TR1 und HT-A4a **nicht** als Lemmas.

---

## 2. Auditquelle und GREEN-Basis

- **Auditquelle:** `audits/P11_R32_HT_A4B_SW1_SELF_CONTAINED_THEOREM_CANDIDATE.md`, 1078 Zeilen, gemergt als PR #10, Merge-Commit `b06f50f12973e781b87db8b06e54fd590a053b10`.
- **GREEN-Basis (adversarial vollständig geprüft, alle Kategorien GREEN):**
  - MECHANICAL
  - CONSTANTS/ORDERING
  - SIX-POINT BLINDNESS
  - A-WALL GEOMETRY
  - BLACKBOX FIREWALL
  - PROMOTION SCOPE
- **Mechanischer Diff-Check gegen den Merge-Commit:** genau 1 neue Datei, 1078 Additions, 0 Deletions — bestätigt.

---

## 3. Negativ-Firewall — was NICHT promotet wird

Dieser Record promotet ausdrücklich **nicht**:

- globale HT-A4b-Chamber-Exhaustivität (alle 15 Chambers);
- FG global (allgemeine Fiber-Graph-Exhaustivität über SW1 hinaus);
- HT-RED (vollständige Tail-Gaussian-/Schur-Elimination des Restblocks);
- Kerneltrivialität von \(\mathcal K_{I,A}\) auf SW1 oder allgemein;
- A0 (volle freie-Koordinaten-Abdeckung);
- \(\ker\Gamma_I=\{0\}\) bzw. Schur-Cross-Gram-Injektivität;
- Closed Range / bounded below;
- Strong Terminal Transport;
- Objekt X als konstruiertes Objekt;
- RH.

Alle diese Knoten bleiben nach diesem Record unverändert `?[O]` bzw. offen.

---

## 4. Wirksamkeit dieser Buchung

Dieser Record allein erzeugt **keine** Promotion. Die formale Buchung
\[
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M]
\]
wird erst mit dem nach vollständigem adversarialem GREEN-Review ausdrücklich freigegebenen Merge des diesen Record enthaltenden Promotions-PRs wirksam.

Bis zu diesem ausdrücklich freigegebenen Merge bleibt der kanonische Main-Status
\[
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:?[O]
\]

— GREEN ist nicht gleich \(\checkmark[M]\).

---

## 5. Nach wirksamer Promotion

Nach freigegebenem Merge dieses PRs gilt kanonisch:

\[
\boxed{
\mathrm{HT\!-\!A4b\!-\!SW1\!-\!M}:\checkmark[M]
}
\]

mit diesem Record als kanonischer Promotionsquelle, referenziert in `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` und `CURRENT-FRONT.md`.
