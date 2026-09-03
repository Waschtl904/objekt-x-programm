# Objekt-X-Programm — Repository-Karte

> **Operativer Hinweis (3. September 2026):** Für den heutigen Forschungsstand zuerst
> [CURRENT-FRONT](../CURRENT-FRONT.md),
> [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md),
> [AKTUELLER_STAND](AKTUELLER_STAND.md),
> [DAG](DAG.md) und die
> [Forschungsroadmap 2026-09-03](FORSCHUNGS_ROADMAP_2026-09-03.md) lesen.
>
> Aktiver mathematischer Kern: **B / Strong Terminal / R43**. R38–R42 sind frozen;
> §3K liefert aktuell einen noch unabhängig zu prüfenden GC-AC-Kandidaten. Unter diesem
> Kandidaten bleibt als finaler C6-Rest nur der Normal-Skalar (b_U). A / universelle
> finite-level SW1-Injektivität ist negativ entschieden; R37/G4c bleibt separat offen.
>
> Die darunterstehende Repository-/Syntheseorganisation ist teilweise historisch
> (Grundstruktur vom 8. August 2026). Historische Navigationsfassungen werden unter
> [archiv/](archiv/) erhalten.

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
