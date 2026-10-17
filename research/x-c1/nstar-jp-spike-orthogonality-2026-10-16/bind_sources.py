#!/usr/bin/env python3
"""Erzeugt SOURCE_BINDINGS.json und SOURCE_BINDINGS.sha256 fuer dieses Paket (Standardbibliothek)."""
import hashlib, json, os, sys, zipfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
def sha(b): return hashlib.sha256(b).hexdigest()
VIS = {'archives/Objekt-X-Stufe1-Intervallzertifikat-Momentkorrektur-und-W9-Diagnose-2026-10-16.zip': 'original/gpt1-stufe1-zertifikat',
       'archives/Objekt-X-Stufe3-Endliche-U8-Antwort-und-Skalaranschluss-2026-10-16.zip': 'original/gpt2-stufe3-endliche-u8-antwort',
       'archives/Objekt-X-Stufe1-4-Diagnose-2026-10-16.zip': None,
       'archives/Objekt-X-Vollstaendige-Hochantwort-und-Spike-Skalarfehler-2026-10-16.zip': 'original/gpt2-stufe4-hochantwort',
       'archives/Objekt-X-PR229-Gegenpruefung-2026-10-17.zip': 'original/gpt1-pr229-gegenpruefung',
       'archives/Objekt-X-Stufe4-Teil2-Gegenpruefung-und-Rayleigh-Zeugen-2026-10-17.zip': 'original/gpt2-rayleigh-zeugen'}
REPO_DEPS = ['research/x-c1/a9-inverse-spike-calibration-2026-10-15/archives/Objekt-X-Nstar-Jp-Funktionsanschluss-und-Koeffizienten-2026-10-16.zip',
             'research/x-c1/a9-inverse-spike-calibration-2026-10-15/archives/Objekt-X-A9-Spike-Artefaktpruefung-und-Korrekter-W9-Anschluss-2026-10-15.zip',
             'research/x-c1/a9-a11-whole-response-gram-2026-10-15/archives/Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip',
             'research/x-c1/a9-a11-whole-response-gram-2026-10-15/archives/Objekt-X-Antwortgram-Nachtrag-Breitenpruefung-und-W9-Klarstellung-2026-10-15.zip']
EXCLUDE = {'SOURCE_BINDINGS.json', 'SOURCE_BINDINGS.sha256', 'META.yaml', 'verify.py', 'bind_sources.py'}
def main():
    b = {'schema_version': 1, 'date': '2026-10-16', 'archives': {}, 'files': {}, 'repository_dependencies': {}}
    for rel, vis in VIS.items():
        data = (HERE / rel).read_bytes(); z = zipfile.ZipFile(HERE / rel)
        root = z.namelist()[0].split('/')[0]
        e = {'sha256': sha(data), 'bytes': len(data), 'members': {}, 'visible_copies': {}}
        for i in z.infolist():
            if i.is_dir() or i.file_size == 0: continue
            raw = z.read(i); e['members'][i.filename] = {'bytes': len(raw), 'sha256': sha(raw)}
            if vis:
                rel2 = i.filename[len(root)+1:]
                if (HERE / vis / rel2).is_file(): e['visible_copies'][i.filename] = vis + '/' + rel2
        b['archives'][rel] = e
    for dp, _, fs in os.walk(HERE):
        for f in sorted(fs):
            rel = os.path.relpath(os.path.join(dp, f), HERE).replace(os.sep, '/')
            if rel.startswith('archives/') or rel in EXCLUDE or '__pycache__' in rel: continue
            data = open(os.path.join(dp, f), 'rb').read(); b['files'][rel] = {'bytes': len(data), 'sha256': sha(data)}
    for rel in REPO_DEPS:
        p = ROOT / rel
        if p.is_file(): b['repository_dependencies'][rel] = {'sha256': sha(p.read_bytes())}
        else: b.setdefault('repository_dependencies_missing_at_generation', []).append(rel)
    s = json.dumps(b, indent=2, ensure_ascii=False) + '\n'
    (HERE / 'SOURCE_BINDINGS.json').write_text(s, encoding='utf-8')
    (HERE / 'SOURCE_BINDINGS.sha256').write_text(sha(s.encode()) + '  SOURCE_BINDINGS.json\n')
    print(len(b['files']), 'files;', len(b['repository_dependencies']), 'repo deps;', b.get('repository_dependencies_missing_at_generation'))
if __name__ == '__main__': main()
