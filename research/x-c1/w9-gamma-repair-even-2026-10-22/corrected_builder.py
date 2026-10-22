"""Construct a corrected-source revision without editing the frozen builder.
The cached-model correction and its price are verified separately. This adapter
alone makes no full operator/model-identification claim.
"""
from pathlib import Path
import hashlib
EXPECTED='ed58da3caacd5ca39de1f910c77920e7079eec905a560b487600c71e97c8df64'
OLD='research/x-c1/w9-residual-centered-control-even-2026-10-21/whole/whole_function_probe.py'

def corrected_source(repository):
    raw=(Path(repository)/OLD).read_bytes()
    if hashlib.sha256(raw).hexdigest()!=EXPECTED:
        raise ValueError('Frozen builder source changed')
    source=raw.decode('utf-8')
    needle='regular_out(ym)(arb_poly([0,a]))'
    if source.count(needle)!=1 or source.count('def build_core(')!=1:
        raise ValueError('Unexpected builder geometry')
    helper='''def regular_core(moments):
    # Inner point x, outer source y: Gamma((y-x)/2)+Gamma((y+x)/2).
    co=convker*arb_poly([moments[k]/fac[k]for k in range(225)])
    return arb_poly([co[224-k]/fac[k]*(1+(-1)**k)for k in range(225)])
'''
    return source.replace(needle,'regular_core(ym)(arb_poly([0,a]))').replace('def build_core(',helper+'def build_core(',1)
