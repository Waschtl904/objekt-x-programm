"""Propose rational triangular repair factors, without computing eigenvectors.

Floating point output is not a certificate; verify_spectral_ranks.py replays it
using integer intervals from the original pinned terminal inputs.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, gzip, hashlib, json
import numpy as np
from scipy.linalg import solve_triangular
CASES = {
    'A8': ('research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand', 'reserve_refined', 5),
    'A9': ('research/x-c1/chambers-through-a11-2026-09-28/a9', 'reserve_results', 6),
}

def main():
    p = argparse.ArgumentParser()
    for k in ('repo', 'vectors', 'out'):
        p.add_argument('--'+k, type=Path, required=True)
    a = p.parse_args()
    vectors = json.loads(a.vectors.read_bytes())
    den = 10**100
    scale = 10**16
    cut = F(1, 400)
    results = {}
    hashes = {}
    for name, (rel, stem, rank) in CASES.items():
        source = a.repo/rel/(stem+'_lower_matrices.json.gz')
        raw = source.read_bytes()
        hashes[source.relative_to(a.repo).as_posix()] = hashlib.sha256(raw).hexdigest()
        data = json.loads(gzip.decompress(raw))
        for parity in ('even', 'odd'):
            key = name+'-'+parity
            rows = data['parities'][parity]['lower_matrix']
            n = len(rows)
            fm = np.array([[float(F(int(x[0])+int(x[1]),2*den)) for x in row] for row in rows])
            v = np.array([[float(vectors[key+'-'+str(j+1)]['coefficients'][i])
                           for j in range(rank)] for i in range(n)])
            repaired = fm-np.eye(n)*float(cut)+v@v.T
            r = np.linalg.cholesky((repaired+repaired.T)/2).T
            t = solve_triangular(r, np.eye(n), lower=False)
            def grid(x):
                return [[str(int(round(float(x[i,j])*scale))) if j>=i else '0' for j in range(n)] for i in range(n)]
            results[key] = {'rank': rank, 'comparison_cut_exact': str(cut),
                            'R_upper_grid': grid(r), 'T_upper_grid': grid(t)}
            print(key, 'rank', rank, 'rational factors proposed', flush=True)
    out = {'status': 'PROPOSAL_ONLY_REQUIRES_INTEGER_REPLAY', 'factor_scale': str(scale),
           'source_F_sha256': hashes,
           'vectors_sha256': hashlib.sha256(a.vectors.read_bytes()).hexdigest(), 'results': results}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_bytes(gzip.compress((json.dumps(out,separators=(',',':'))+'\n').encode(),mtime=0))

if __name__ == '__main__':
    main()
