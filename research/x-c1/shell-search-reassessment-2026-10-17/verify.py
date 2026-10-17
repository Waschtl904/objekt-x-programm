"""Fresh numerical replay with explicit tolerances, not a directed proof."""
import hashlib
import json
import sys
import tempfile
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]


def main():
    if not __debug__:raise RuntimeError('Run replay without python -O')
    for name,digest in json.loads((HERE/'MANIFEST.json').read_text()).items():
        path=(HERE/name).resolve()
        if not path.is_relative_to(HERE)or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
            raise RuntimeError('Own binding failed: '+name)
    bindings=json.loads((HERE/'INPUT_BINDINGS.json').read_text())
    for name,digest in bindings['repository_files'].items():
        if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
            raise RuntimeError('Input binding failed: '+name)
    sys.path.insert(0,str(HERE))
    import numpy as np
    import build_k,build_transport,search,controls
    with tempfile.TemporaryDirectory(prefix='objekt-x-reassessment-') as td:
        out=Path(td)
        for module in (build_k,build_transport,search,controls):module.DATA=out
        for par in ('even','odd'):
            for n,inner in ((64,24),(128,40)):
                got=build_k.build(par,n,inner)
                ref=json.loads((HERE/'data'/f'K_MAP_{par}_{n}.json').read_text())
                for key in ('G_W','direct_form','finite_response_correction','K_P_model'):
                    assert np.max(abs(np.array(got[key])-np.array(ref[key])))<1e-10,(par,n,key)
            for n in (384,512):
                got=build_transport.build(par,n)
                ref=json.loads((HERE/'data'/f'TRANSPORT_{par}_{n}.json').read_text())
                for key in ('G_W','I0_row','common_k_gram','high_coordinate_gram','finite_feature_gram'):
                    assert np.max(abs(np.array(got[key])-np.array(ref[key])))<1e-10,(par,n,key)
            got=search.run(par)
            ref=json.loads((HERE/'data'/f'REASSESS_{par}.json').read_text())
            assert got['new_starts']==ref['new_starts'] and got['old_starts_reassessed']==58
            assert got['passing_starts']==ref['passing_starts']==0
            assert abs(got['best_margin_direction']['margin_diagnostic']-ref['best_margin_direction']['margin_diagnostic'])<1e-6
            assert abs(got['global_midpoint_ratio_diagnostic_128']-ref['global_midpoint_ratio_diagnostic_128'])<1e-6
        got=controls.main();ref=json.loads((HERE/'data'/'CONTROLS.json').read_text())
        for par in ('even','odd'):
            for a,b in zip(got['data'][par]['whole_space_support_guard_diagnostic'],ref['data'][par]['whole_space_support_guard_diagnostic']):
                assert abs(a['whole_space_support_ratio_upper_diagnostic']-b['whole_space_support_ratio_upper_diagnostic'])<1e-6
    print('PASS: eight numerical maps, 116 old starts, 145 new starts and controls replayed within declared tolerances; no new certificate')


if __name__=='__main__':main()
