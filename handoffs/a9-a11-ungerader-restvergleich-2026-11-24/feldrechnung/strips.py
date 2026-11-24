"""Directed bounds on selected dyadic intervals of the frozen odd shell model."""
import sys
from pathlib import Path
supplied = sys.argv[4].split(',')
assert len(sys.argv) == 5
depths = [int(i) for i in supplied]
assert len(depths) == len(set(depths)) and all(6 <= k <= 213 for k in depths)
sys.argv[4] = '5'
shared = Path(__file__).with_name('panels.py')
body = shared.read_text(encoding='utf8')
exec(compile(body[:body.index('panels=[]')], str(shared), 'exec'))
import math

rows = []
for depth in depths:
    for side, endpoint, sign, width in [
        ('left', a, 1, outer_edges[1]-a),
        ('right', b, -1, b-outer_edges[-2])
    ]:
        tick = time.monotonic()
        step = width / (2**depth)
        lo, hi = sorted((endpoint+sign*step, endpoint+sign*2*step), key=lambda x: x.mid().fmpq())
        probe = tm.build(globals(), lo, hi, 4)
        tol = q('1e-7') / (2*(hi-lo)).sqrt()
        guess = max(32, math.ceil(float((probe['contour_bound']/tol).log()/arb(2).log()))+12)
        order = 16*((guess+15)//16)
        assert order <= 1536
        result = tm.build(globals(), lo, hi, order)
        center_error = abs(result['polynomial'](0) - outer_value((lo+hi)/2)).upper()
        norm_error = (2*(hi-lo)).sqrt()*result['taylor_error']
        assert center_error < q('1e-15') and norm_error < q('1e-7')
        row = dict(depth=depth, side=side, order=result['order'],
                   upper=c.enc(result['model_Xnorm_squared_upper'])[1],
                   upper_norm_remainder=c.enc(norm_error)[1],
                   center_check=c.enc(center_error)[1], seconds=round(time.monotonic()-tick,2))
        rows.append(row)
        args.output.write_text(json.dumps(dict(cache_sha256=hashlib.sha256(args.cache.read_bytes()).hexdigest(),
            panels=rows), indent=2)+'\n', encoding='utf8')
        print('dyad', side, depth, order, float(result['model_Xnorm_squared_upper'].upper()), row['seconds'], flush=True)
