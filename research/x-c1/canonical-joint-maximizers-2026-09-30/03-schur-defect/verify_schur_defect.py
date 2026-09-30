"""Rational Schur-defect corollary with a byte-exact replay of its dependency."""
from pathlib import Path, PurePosixPath
from fractions import Fraction as F
import argparse, hashlib, importlib, io, json, os, subprocess, sys, tempfile, zipfile

ARCHIVE = 'Gemeinsamer-generalisierter-Diskriminant-2026-09-30.zip'
ARCHIVE_SHA = 'c9760daa202b4eda079d1d2b9cdbd792a1579ba56e573d79f7c8140d75889844'
UPSTREAM_ROOT = 'canonical-joint-discriminant-2026-09-30'


def checked_archive(raw):
    assert hashlib.sha256(raw).hexdigest() == ARCHIVE_SHA, 'upstream archive hash mismatch'
    files = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for info in z.infolist():
            p = PurePosixPath(info.filename)
            assert not p.is_absolute() and '..' not in p.parts and '\\' not in info.filename
            assert p.parts[0] == UPSTREAM_ROOT and len(p.parts) > 1
            rel = '/'.join(p.parts[1:])
            assert not info.is_dir() and rel not in files
            files[rel] = z.read(info)
    manifest = {}
    for line in files['SHA256SUMS'].decode().splitlines():
        sha, name = line.split('  ', 1)
        assert name not in manifest
        manifest[name] = sha
    assert set(manifest) == set(files) - {'SHA256SUMS'}
    for name, sha in manifest.items():
        assert hashlib.sha256(files[name]).hexdigest() == sha, name
    return files


def entry_test(v, r, nr, old):
    g = v.symmetric(v.matrix(nr['compressed_moment_entries']['G0']))
    ll = v.symmetric(v.matrix(r['energy_Loewner_lower_in_raw_basis']))
    lu = v.symmetric(v.matrix(r['energy_Loewner_upper_in_raw_basis']))
    l = v.symmetric(v.intersectmat(v.hull_from_order(ll, lu), v.matrix(nr['compressed_moment_entries']['L0'])))
    v.positive2(l)
    z = v.symmetric(v.intersectmat(v.hull_from_order(v.matrix(r['inverse_lower_family_in_raw_basis']), v.matrix(r['inverse_upper_family_in_raw_basis'])), v.matrix(nr['compressed_moment_entries']['Z0'])))
    h = v.symmetric(v.mm(v.mm(g, v.inverse(l, positive_pivots=True)), g))
    w = v.submat(z, h)
    m = v.addmat(v.addmat(l, v.scale(g, 34)), v.scale(h, 289))
    rr = v.addmat(v.addmat(l, v.scale(g, 34)), v.scale(z, 289))
    a, b, c = m[0][0], m[0][1], m[1][1]
    p, q, s = w[0][0], w[0][1], w[1][1]
    f1 = v.intersect(v.sub(v.mul(a, q), v.mul(b, p)), v.div(v.sub(v.mul(a, rr[0][1]), v.mul(b, rr[0][0])), v.point(289)))
    f2 = v.intersect(v.sub(v.mul(a, s), v.mul(c, p)), v.div(v.sub(v.mul(a, rr[1][1]), v.mul(c, rr[0][0])), v.point(289)))
    # In the inherited receipt, a_interval denotes det(M), not M[0,0].
    d = v.intersect(v.interval(old['a_interval']), v.determinant(m))
    assert a[0] > 0 and d[0] > 0
    separated = f1[0] > 0 or f1[1] < 0
    bound = F(0)
    if separated:
        bound = 2 * min(abs(f1[0]), abs(f1[1])) / (a[1] * v.sqrt_upper(d[1]))
        assert bound > 0
    return {'F1_interval': f1, 'F2_interval': f2,
            'F1_display': v.display(f1), 'F2_display': v.display(f2),
            'F1_separated_from_zero': separated,
            'F2_separated_from_zero': f2[0] > 0 or f2[1] < 0,
            'M11_interval': a, 'detM_interval': d,
            'gamma_gap_from_F1_lower': bound,
            'gamma_gap_from_F1_display': v.sci(bound)}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    files = checked_archive((base/'inputs'/ARCHIVE).read_bytes())
    with tempfile.TemporaryDirectory(prefix='schur-defect-') as tmp:
        dep = Path(tmp)/UPSTREAM_ROOT
        for name, raw in files.items():
            dest = dep/name
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(raw)
        replay = Path(tmp)/'replay.json'
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        run = subprocess.run([sys.executable, '-B', str(dep/'verify_joint_discriminant.py'), '--out', str(replay)], check=True, capture_output=True, text=True, env=env)
        assert not run.stderr, run.stderr
        print(run.stdout, end='', flush=True)
        assert replay.read_bytes() == files['verification.json'], 'upstream replay differs'
        old = json.loads(files['verification.json'])
        assert old['status'] == 'JOINT_GENERALIZED_DISCRIMINANT_STRICTLY_POSITIVE'
        assert old['both_true_generalized_maxima_simple'] is True
        sys.path.insert(0, str(dep))
        v = importlib.import_module('verify_joint_discriminant')
        projected = json.loads(files['inputs/projected_verification.json'])
        results = {}
        for name in ['primary.json', 'crosscheck.json']:
            data = json.loads(files['inputs/'+name])
            results[name] = {}
            for key in ['A9->A11-even', 'A9->A11-odd']:
                inherited = old['results'][name][key]
                gap = F(inherited['gap_lower'])/289
                assert gap > 0
                result = entry_test(v, data['results'][key], projected['runs'][name]['results'][key], inherited)
                result.update({'proportional_completion_exists': False,
                               'gamma_gap_lower': gap, 'gamma_gap_display': v.sci(gap),
                               'normalized_defect_square_lower': gap**2,
                               'distance_to_scalars_operator_lower': gap/2,
                               'distance_to_scalars_display': v.sci(gap/2),
                               'gamma_gap_source': 'replayed_joint_beta_gap_divided_by_289'})
                results[name][key] = result
                print(name, key, 'gamma gap >=', result['gamma_gap_display'],
                      'F1', result['F1_display'], 'F1-only gap >=', result['gamma_gap_from_F1_display'], flush=True)
        out = {'status': 'JOINT_SCHUR_DEFECT_PROPORTIONALITY_EXCLUDED',
               'research_status': 'AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN',
               'source_commit': old['source_commit'], 'integration_base': old['integration_base'],
               'upstream_archive_sha256': ARCHIVE_SHA,
               'upstream_verification_sha256': hashlib.sha256(files['verification.json']).hexdigest(),
               'upstream_manifest_files': len(files)-1, 'upstream_byte_exact_replay': True,
               'results': results, 'large_operator_solves_rerun': False,
               'new_independent_joint_gap_proof': False, 'global_result_proved': False}
        args.out.write_text(json.dumps(v.rational(out), indent=2)+'\n', encoding='utf-8', newline='\n')
    print('BOTH JOINT SCHUR-DEFECT PROPORTIONALITY GATES: NO COMPLETION; PASS', flush=True)


if __name__ == '__main__':
    main()
