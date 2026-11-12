"""Read-only archive binding and rational result replay; no physical integration."""
from fractions import Fraction as Q
from pathlib import Path
import gzip
import hashlib
import json
import sys
import zipfile

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(100000)
ROOT = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def scalar_unpack(value):
    if isinstance(value, list):
        return [scalar_unpack(x) for x in value]
    if isinstance(value, dict):
        assert set(value) == {'mapping'}
        return {k: scalar_unpack(v) for k, v in value['mapping']}
    assert value is None or isinstance(value, (int, str, bool))
    return value


def interval_product(a, b):
    p = [x*y for x in a for y in b]
    return min(p), max(p)


def verify():
    assert not sys.flags.optimize
    if (ROOT/'ERGEBNISMANIFEST.json').exists():
        for name, expected in json.loads((ROOT/'ERGEBNISMANIFEST.json').read_bytes()).items():
            path = (ROOT/name).resolve()
            assert path.is_relative_to(ROOT)
            h = hashlib.sha256()
            with path.open('rb') as stream:
                for block in iter(lambda: stream.read(1048576), b''):
                    h.update(block)
            assert h.hexdigest() == expected, name
    start = json.loads((ROOT/'STARTBINDUNG.json').read_bytes())
    end = json.loads((ROOT/'ENDBINDUNG.json').read_bytes())
    assert end['start_binding_sha256'] == digest((ROOT/'STARTBINDUNG.json').read_bytes())
    original = (ROOT/'ORIGINAL_VORBEREITUNG.zip').read_bytes()
    acceptance = (ROOT/'GPT1_ABNAHME.zip').read_bytes()
    assert digest(original) == start['original_archive_sha256']
    assert digest(acceptance) == start['GPT1_acceptance_archive_sha256']
    with zipfile.ZipFile(ROOT/'GPT1_ABNAHME.zip') as z:
        assert z.testzip() is None
        for name, sha in start['GPT1_acceptance_members'].items():
            assert digest(z.read(name)) == sha
        assert json.loads(z.read('PRUEFERGEBNIS.json'))['original_sha256'] == digest(original)
    with zipfile.ZipFile(ROOT/'ORIGINAL_VORBEREITUNG.zip') as z:
        assert z.testzip() is None
        prefix = next(x for x in z.namelist() if x.endswith('/MANIFEST.json')).removesuffix('MANIFEST.json')
        manifest_bytes = z.read(prefix+'MANIFEST.json')
        assert digest(manifest_bytes) == start['original_manifest_sha256']
        manifest = json.loads(manifest_bytes)
        for name, sha in manifest.items():
            assert digest(z.read(prefix+name)) == sha
        cache = z.read(prefix+'PREPARED_CORE.json.gz')
        assert digest(cache) == start['cache_sha256']
        spec = json.loads(z.read(prefix+'JOB_SPEC.json'))
        assert spec['max_seconds'] == start['seconds_limit'] == 1800
        rational_code = z.read(prefix+'schluss.py')
    actual_start = json.loads((ROOT/'lauf/START.json').read_bytes())
    assert actual_start['JOB_SPEC_sha256'] == start['JOB_SPEC_sha256']
    assert actual_start['seconds_limit'] == 1800
    status = json.loads((ROOT/'lauf/LAUFSTATUS.json').read_bytes())
    result = {'bindings': 'PASS', 'physical_replays': 0, 'run_status': status,
              'new_physical_source_passes': 1, 'external_GPT1_result_review': 'OFFEN'}
    if status['status'] != 'LAUF_BEENDET':
        result['mathematical_decision'] = 'KEINE'
        result['reason'] = 'Der einmalige physische Hauptlauf hat nicht vollstaendig abgeschlossen.'
        return result
    body = json.loads(gzip.decompress(cache))
    assert digest(body['payload'].encode()) == body['payload_sha256']
    packed = dict(json.loads(body['payload'])['mapping'])
    scalars = scalar_unpack(packed['scalars'])
    data = json.loads((ROOT/'lauf/X_INTERVALLE.json').read_bytes())
    saved = json.loads((ROOT/'lauf/SCHLUSS.json').read_bytes())
    namespace = {}
    exec(compile(rational_code, 'original/schluss.py', 'exec'), namespace)
    repeated = namespace['check'](data, scalars)
    assert repeated == saved
    if saved['status'] == 'FESTER_VERGLEICH_AUSGESCHLOSSEN':
        x = list(map(Q, saved['witness']))
        assert len(x) == 2 and any(v != 0 for v in x)
        upper = Q(0)
        lower = Q(0)
        for i in range(2):
            for j in range(2):
                a = tuple(map(Q, saved['D_k_minus_J_K'][i][j]))
                lo, hi = interval_product(a, (x[i]*x[j], x[i]*x[j]))
                lower += lo
                upper += hi
        assert upper <= 0
        assert (lower, upper) == tuple(map(Q, saved['witness_value']))
        result['nonzero_witness_upper_endpoint_check'] = 'PASS'
    result['rational_replay'] = 'PASS'
    result['mathematical_decision'] = saved['status']
    result['actual_Schur_positivity'] = 'OFFEN'
    return result


if __name__ == '__main__':
    print(json.dumps(verify(), indent=2, ensure_ascii=False))
