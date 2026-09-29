"""Directed scalar and physical trial bounds for a fixed spectral rank cut.

No eigenvectors or eigenvalues are computed. The earlier terminal model,
complete-high certificate and fixed rational trial functions are inputs.
"""
from pathlib import Path
from fractions import Fraction
import argparse, gzip, hashlib, json, shutil, subprocess, time
import flint
from flint import arb, arb_mat, fmpq, ctx

PIN = 'd16ba43ebb20f2c61f43379fc65d7a9b9dba76de'
DEN = 10**100
CASES = {
    'A8': ('research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand', 'reserve_refined', 5),
    'A9': ('research/x-c1/chambers-through-a11-2026-09-28/a9', 'reserve_results', 6),
}

def rational(x):
    f = Fraction(x)
    return arb(fmpq(f.numerator, f.denominator))

def ball(x):
    lo, hi = map(int, x)
    assert lo <= hi
    return arb(fmpq(lo+hi, 2*DEN)) + arb(0, arb(fmpq(hi-lo, 2*DEN)))

def matrix(rows):
    return arb_mat([[ball(x) for x in row] for row in rows])

def eye(n):
    return arb_mat([[int(i == j) for j in range(n)] for i in range(n)])

def exact(x, lower=True):
    v = x.lower() if lower else x.upper()
    s = 10**140
    z = (v*s).floor() if lower else (v*s).ceil()
    return str(Fraction(int(z.unique_fmpz()), s))

def interval(x):
    return [exact(x), exact(x, False)]

def main():
    p = argparse.ArgumentParser()
    for k in ('repo', 'vectors', 'out'):
        p.add_argument('--'+k, type=Path, required=True)
    p.add_argument('--bits', type=int, default=512)
    a = p.parse_args()
    ctx.prec = a.bits
    assert flint.__version__ == '0.9.0'
    git = shutil.which('git') or r'C:\Program Files\Git\cmd\git.exe'
    assert subprocess.check_output([git, 'rev-parse', 'HEAD'], cwd=a.repo).decode().strip() == PIN
    sources = {}
    def read(path, zipped=False):
        raw = path.read_bytes()
        rel = path.relative_to(a.repo).as_posix()
        assert raw == subprocess.check_output([git, 'show', PIN+':'+rel], cwd=a.repo)
        sources[rel] = hashlib.sha256(raw).hexdigest()
        return json.loads(gzip.decompress(raw) if zipped else raw)
    vectors = json.loads(a.vectors.read_bytes())
    result = {}
    for name, (rel, stem, rank) in CASES.items():
        folder = a.repo/rel
        model = read(folder/(name.lower()+'_model.json.gz'), True)
        receipt = read(folder/(stem+'.json'))
        saved = read(folder/(stem+'_lower_matrices.json.gz'), True)
        delta = Fraction(receipt['full_high_physical_floor'])
        assert delta == Fraction(2, 3)
        for parity in ('even', 'odd'):
            started = time.time()
            key = name+'-'+parity
            n = model['parities'][parity]['dimension']
            pi = int(parity == 'odd')
            fm = matrix(saved['parities'][parity]['lower_matrix'])
            eB = rational(receipt['parities'][parity]['coupling_operator_error_exact'])
            hup = matrix(model['parities'][parity]['complete_model_raw_high_Gram'])*rational('1001/1000')
            hup += eye(n)*(1001*eB*eB)
            print(key, 'complete-high coupling and mass bounds', flush=True)
            gamma = (fm.solve(eye(n), algorithm='precond')*hup).trace()
            assert gamma > 0
            endpoint = ball(model['endpoint_interval'])
            mnorm = (endpoint.sinh()/endpoint + (1 if pi == 0 else -1))/2
            me = arb(2*pi+1).sqrt()*ball(model['raw_low_moments'][pi])
            rho = mnorm/(me*me)
            assert rho > 1
            # Recompute the physical rank-r trial forms from the pinned model.
            v = arb_mat([[rational(vectors[key+'-'+str(j+1)]['coefficients'][i])
                          for j in range(rank)] for i in range(n)])
            vg = v.transpose()*v
            s = v.transpose()*matrix(model['parities'][parity]['A'])*v
            eL = rational(receipt['low_form_error_exact'])
            for i in range(rank):
                for j in range(rank):
                    s[i,j] += arb(0, (eL*(vg[i,i]*vg[j,j]).sqrt()).upper())
            degrees = list(range(pi+2, model['cutoff']+1, 2))
            assert len(degrees) == n
            carrier = [-sum((v[i,j]*arb(2*k+1).sqrt()*ball(model['raw_low_moments'][k])
                             for i,k in enumerate(degrees)), arb(0))/me for j in range(rank)]
            g = vg + arb_mat([[carrier[i]*carrier[j] for j in range(rank)] for i in range(rank)])
            result[key] = {
                'dimension': n, 'trial_rank': rank, 'delta_exact': str(delta),
                'gamma_interval': interval(gamma), 'mass_norm_squared_interval': interval(rho),
                'physical_form_gram': [[interval(s[i,j]) for j in range(rank)] for i in range(rank)],
                'physical_L2_gram': [[interval(g[i,j]) for j in range(rank)] for i in range(rank)],
                'seconds': time.time()-started,
            }
            print(key, 'gamma', gamma.str(18), 'rho', rho.str(18), 'seconds', round(time.time()-started, 1), flush=True)
    out = {
        'status': 'DIRECTED_COMPLETE_HIGH_AND_PHYSICAL_TRIAL_BOUNDS',
        'source_commit': PIN, 'source_sha256': sources,
        'vectors_sha256': hashlib.sha256(a.vectors.read_bytes()).hexdigest(),
        'precision_bits': a.bits, 'python_flint_version': flint.__version__,
        'eigenvectors_computed': False, 'high_space_truncated': False,
        'results': result,
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print('ALL DIRECTED INPUTS COMPLETE', flush=True)

if __name__ == '__main__':
    main()
