"""Extract the hash-bound inputs for l00.py without author-specific paths."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import zipfile

PACKAGE = Path(__file__).resolve().parents[1]
ROOT = PACKAGE.parents[2]


def member(z, suffix):
    matches = [n for n in z.namelist() if n.endswith('/' + suffix)]
    assert len(matches) == 1, (suffix, matches)
    return z.read(matches[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('output', type=Path)
    args = ap.parse_args()
    out = args.output.resolve()
    bindings = json.loads((PACKAGE / 'SOURCE_BINDINGS.json').read_text())
    sources = {}
    def archive(path):
        rel = str(path.relative_to(ROOT))
        if path.is_relative_to(PACKAGE):
            expected = bindings['archives'][str(path.relative_to(PACKAGE))]['sha256']
        else:
            expected = bindings['repository_dependencies'][rel]['sha256']
        raw = path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        assert digest == expected, rel
        sources[rel] = digest
        return zipfile.ZipFile(io.BytesIO(raw))
    def save(rel, raw):
        p = out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(raw)
    stage3 = archive(next((PACKAGE / 'archives').glob('*Stufe3-Endliche*.zip')))
    for rel in ('inputs/REFINED_COMMON96.json.gz', 'inputs/REFINED_INPUT.json.gz', 'expected/FINITE_ACTION.json'):
        save('stage3/' + rel, member(stage3, rel))
    response = archive(next((ROOT / 'research/x-c1/a9-a11-whole-response-gram-2026-10-15/archives').glob('*Vollstaendiger-Antwortgram*.zip')))
    for name in ('FUNCTIONS12.json', 'FROZEN_RESPONSE12.json'):
        save(name, member(response, 'inputs/' + name))
    bridge = archive(next((ROOT / 'research/x-c1/a9-inverse-spike-calibration-2026-10-15/archives').glob('*Nstar-Jp*.zip')))
    save('DIRECTIONS.json', member(bridge, 'expected/DIRECTIONS.json'))
    global_raw = member(bridge, 'inputs/Objekt-X-Globaler-Gram-und-vollstaendige-Projektion-2026-10-13.zip')
    assert hashlib.sha256(global_raw).hexdigest() == '2ca3c682de8a529b12a0d628c2b606fd04df332d1299ccd36dff71ac3e53d80c'
    global_zip = zipfile.ZipFile(io.BytesIO(global_raw))
    save('HALF_INVERSE_1536.json', member(global_zip, 'half-inverse/expected/1536.json'))
    save('INNER_LOG_1536.json', member(global_zip, 'work/inner-log-2026-10-12/INNER_LOG_1536.json'))
    receipt = {'archive_sha256': sources, 'files': {str(p.relative_to(out)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(out.rglob('*')) if p.is_file() and p.name != "INPUT_RECEIPT.json"}}
    save('INPUT_RECEIPT.json', (json.dumps(receipt, indent=2) + '\n').encode())
    print('Prepared', len(receipt['files']), 'files from', len(sources), 'verified archives:', out)


if __name__ == '__main__':
    main()
