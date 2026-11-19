"""Exact local arithmetic snapshots for exploratory model development."""
import gzip,hashlib,json
from pathlib import Path
from flint import arb,arb_poly,arb_mat
def pack(x):
    if isinstance(x,arb):
        assert x.is_finite()
        m,e=x.mid().man_exp();r,s=x.rad().man_exp()
        return {'ball':[int(m),int(e),int(r),int(s)]}
    if isinstance(x,arb_poly):return {'polynomial':[pack(v)for v in x]}
    if isinstance(x,arb_mat):return {'matrix':[[pack(x[i,j])for j in range(x.ncols())]for i in range(x.nrows())]}
    if isinstance(x,dict):return {'mapping':[[k,pack(v)]for k,v in x.items()]}
    if isinstance(x,(tuple,list)):return [pack(v)for v in x]
    assert x is None or isinstance(x,(int,str,bool))
    return x
def unpack(x):
    if isinstance(x,list):return [unpack(v)for v in x]
    if isinstance(x,dict):
        if 'ball'in x:
            m,e,r,s=x['ball'];return arb((m,e),(r,s))
        if 'polynomial'in x:return arb_poly([unpack(v)for v in x['polynomial']])
        if 'matrix'in x:return arb_mat([[unpack(v)for v in row]for row in x['matrix']])
        if 'mapping'in x:return {k:unpack(v)for k,v in x['mapping']}
        raise ValueError('Unknown cache record')
    return x
def save(path,values,source,inputs):
    payload=json.dumps(pack(values),separators=(',',':')).encode()
    body={'source_sha256':source,'inputs':inputs,'payload_sha256':hashlib.sha256(payload).hexdigest(),'payload':payload.decode()}
    path=Path(path);assert not path.exists()
    path.write_bytes(gzip.compress(json.dumps(body,separators=(',',':')).encode(),compresslevel=1,mtime=0))
def load(path,source):
    body=json.loads(gzip.decompress(Path(path).read_bytes()))
    assert body['source_sha256']==source
    payload=body['payload'].encode();assert hashlib.sha256(payload).hexdigest()==body['payload_sha256']
    return unpack(json.loads(payload)),body['inputs']
