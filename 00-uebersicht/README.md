# Objekt-X-Programm — Repository-Karte

**Stand:** 2026-08-08  
**Architektur:** Zwei-Ebenen (Forschungsknoten + Synthese-Manuskripte)

---

## Drei Reifestufen

| Stufe | Ort | Charakter |
|---|---|---|
| **NEU-Knoten** (atomare Forschung) | `active/` und `archive-nodes/` | Darf Fehler, No-Gos, Patches, Statuswechsel enthalten. Laborbuch. |
| **SYN-/P-Manuskripte** (konsolidiert) | `papers/` | Nur aktuell gültiger mathematischer Stand. Alle Definitionen konsolidiert. LaTeX. |
| **Publikationspaper** | `papers/` (markiert `PUB`) | Nur wenn Aussage stark genug für Einreichung. |

---

## Repo-Struktur

```
objekt-x-programm/
├── 00-uebersicht/
│   ├── README.md          ← diese Datei
│   ├── AKTUELLER_STAND.md ← aktive Fronten, offene Fragen
│   └── DAG.md             ← Abhängigkeitsgraph
├── papers/
│   ├── README_papers.md   ← Manuskript-Index
│   ├── P01_BC_Prime_Power_Weights.tex
│   ├── P02_Adelic_Weil_Amplitude_Port.tex
│   ├── P03_Haar_L2_Firewall.tex
│   └── P04_Finite_Weil_Geometry.tex
├── active/
│   ├── NEU-260b_Theta-Selektionsaudit.md
│   ├── NEU-260c_Grenznormalisierung.md   (offen)
│   └── NEU-260d_Jab-Geometrie.md         (offen)
└── archive-nodes/
    ├── 00-grundlegung/
    ├── 01-primkanten-werkzeuge/
    ├── ...
    └── 07-weil-explizitformel/   ← NEU-250 bis NEU-260a
```

---

## Tages-Workflow

1. **Neue Mathematik:** `active/NEU-XXX` anlegen.
2. **Abgeschlossener Block:** Block in `papers/PXX` verdichten; Knoten nach `archive-nodes/` verschieben.
3. **Audit:** Immer gegen `papers/` auditieren; für Provenienz `archive-nodes/` konsultieren.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm.*
