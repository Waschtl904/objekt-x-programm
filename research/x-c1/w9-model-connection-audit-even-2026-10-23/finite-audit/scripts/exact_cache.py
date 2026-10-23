"""Restore declared dyadic balls exactly; never accept a changed enclosure.

python-flint 0.9.0's radius constructor sometimes rounds an already representable
stored radius outward once more. We validate midpoint and radius after every
construction. The fallback is accepted only if both exactly equal the signed
original integers/exponents. No mathematical enclosure is tightened relative
to the archive; the archive's declared enclosure is restored verbatim.
"""
import gzip,hashlib,json
from pathlib import Path
from flint import arb,arb_poly,arb_mat

def ball(data):
    m,e,r,s=map(int,data)
    def matches(x):
        return tuple(map(int,x.mid().man_exp()))==(m,e)and tuple(map(int,x.rad().man_exp()))==(r,s)
    x=arb((m,e),(r,s))
    if matches(x):return x
    if r>1:
        # This produces the representable target radius on the pinned runtime;
        # the equality check, rather than a heuristic, decides acceptance.
        x=arb((m,e),(r-1,s))+arb(0,(1,s-40))
        if matches(x):return x
    raise ValueError('Cannot reproduce the declared ball exactly on this runtime')

def unpack(x):
    if isinstance(x,list):return [unpack(v)for v in x]
    if isinstance(x,dict):
        if 'ball'in x:return ball(x['ball'])
        if 'polynomial'in x:return arb_poly([unpack(v)for v in x['polynomial']])
        if 'matrix'in x:return arb_mat([[unpack(v)for v in row]for row in x['matrix']])
        if 'mapping'in x:return {k:unpack(v)for k,v in x['mapping']}
        raise ValueError('Unknown cache record')
    return x

def load(path,source):
    body=json.loads(gzip.decompress(Path(path).read_bytes()))
    if body['source_sha256']!=source:raise ValueError('Source binding mismatch')
    payload=body['payload'].encode()
    if hashlib.sha256(payload).hexdigest()!=body['payload_sha256']:raise ValueError('Payload hash mismatch')
    data=json.loads(payload);values=unpack(data)
    import model_cache
    if model_cache.pack(values)!=data:raise ValueError('Full cache round trip changed declared data')
    return values,body['inputs']
