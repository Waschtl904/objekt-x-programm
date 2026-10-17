"""Downstream audit only: no Gram reconstruction, full replay or integration."""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext
import hashlib, importlib.util, json

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'source'
PKG = SRC / 'original/gpt2-rayleigh-zeugen'

def need(ok, label):
    if not ok:
        raise AssertionError(label)

def display(q):
    with localcontext() as ctx:
        ctx.prec = 18
        return str(Decimal(q.numerator) / Decimal(q.denominator))

def main():
    binding = json.loads((SRC / 'SOURCE_BINDINGS.json').read_bytes())
    hashes = {}
    for path in sorted(SRC.rglob('*')):
        if not path.is_file():
            continue
        rel = str(path.relative_to(SRC))
        if rel in binding['files']:
            data = path.read_bytes()
            h = hashlib.sha256(data).hexdigest()
            need(h == binding['files'][rel]['sha256'], rel + ' hash')
            need(len(data) == binding['files'][rel]['bytes'], rel + ' length')
            hashes[rel] = h
    spec = importlib.util.spec_from_file_location('bound_gamma_code', PKG / 'vendor/rational_bounds.py')
    rb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rb)
    cert = json.loads((PKG / 'expected/RAYLEIGH_CERTIFICATE.json').read_bytes())
    vectors = json.loads((PKG / 'inputs/SOFT_WITNESSES.json').read_bytes())
    eps = rb.gamma_bound(160, F(21,20))
    need(eps == F(cert['Gamma_kernel_error_exact']), 'recomputed Gamma bound')
    eA = F(42,5) * eps
    need(eA == F(cert['whole_coordinate_form_model_error_upper']), 'complete coordinate error')
    out = {
        'scope': 'Independent exact rational downstream checks using saved model-form and physical-norm intervals; Gamma bound replay uses bound source code. No recomputation of Gram contractions or physical norms from model; no full package replay.',
        'head': '3dd6fce08030554f3fc4b398d92e300e82dcaaf9',
        'source_file_hashes_checked': hashes,
        'Gamma_error_display_only': display(eps),
        'coordinate_error_display_only': display(eA),
        'parities': {}
    }
    for sigma, p in enumerate(['even', 'odd']):
        d = cert['parities'][p]
        u = list(map(F, vectors[p]['exact_rational_coordinates']))
        need(len(u) == 191, p + ' dimension')
        need(vectors[p]['degrees'] == list(range(sigma+2, sigma+383, 2)), p + ' degrees')
        n2 = sum((v*v for v in u), F(0))
        need(n2 > 0 and n2 == F(d['coordinate_norm_squared']), p + ' exact coordinate norm')
        norm = list(map(F, d['physical_norm_squared']))
        qm = list(map(F, d['model_form_interval']))
        err = list(map(F, d['complete_Gamma_form_error_upper']))
        qa = list(map(F, d['true_form_interval']))
        rq = list(map(F, d['true_Rayleigh_interval']))
        for pair in (norm, qm, err, qa, rq):
            need(pair[0] <= pair[1], p + ' ordered interval')
        need(0 < n2 <= norm[0], p + ' physical norm lower check')
        need(err[0] <= eA*n2 <= err[1], p + ' Gamma inflation')
        need(qa[0] <= qm[0]-eA*n2 and qa[1] >= qm[1]+eA*n2, p + ' true energy encloses model and error')
        need(qa[0] > 0, p + ' positive witness energy')
        need(rq[0] <= qa[0]/norm[1] and rq[1] >= qa[1]/norm[0], p + ' physical normalization')
        inv = F(d['A9_inverse_norm_lower_bound'])
        safe = F(d['safe_strict_A9_inverse_norm_lower'])
        need(safe < inv <= 1/rq[1], p + ' reciprocal bound')
        lower, upper = map(F, ('1.321892e-26', '1.349065e-26') if sigma == 0 else ('8.531120e-24', '8.531393e-24'))
        need(lower < rq[0] <= rq[1] < upper, p + ' outward decimal endpoints')
        inward_upper = F('1.34906e-26' if sigma == 0 else '8.53139e-24')
        need(inward_upper < rq[1], p + ' report upper endpoint rounds inward')
        need(d['old_PR_softmode_pairing_ratios_certified'] is False, p + ' old ratios remain diagnostic')
        out['parities'][p] = {
            'true_Rayleigh_interval_display_only': list(map(display, rq)),
            'safe_outward_decimal_interval': [str(lower), str(upper)],
            'inverse_lower_display_only': display(inv),
            'safe_strict_inverse_lower': str(safe),
            'printed_report_interval_not_an_enclosure': True,
            'old_pairing_ratios_certified': False
        }
    out['status'] = 'PASS_DOWNSTREAM_CHECKS_ONLY'
    (ROOT / 'CHECK_RESULTS.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'source_file_hashes_checked'}, ensure_ascii=False, indent=2))
    print('source hashes checked:', len(hashes))

if __name__ == '__main__':
    main()
