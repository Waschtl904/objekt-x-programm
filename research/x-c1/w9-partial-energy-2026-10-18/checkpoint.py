"""Local resumable arithmetic state, without pickle or rounded decimal balls."""
import gzip
import hashlib
import json
import os
from pathlib import Path
from flint import arb,arb_mat
from common import HERE,need


def pack(x):
    if isinstance(x,arb):
        need(x.is_finite(),'Nonfinite checkpoint')
        m,e=x.mid().man_exp();r,s=x.rad().man_exp()
        return {'ball':[int(m),int(e),int(r),int(s)]}
    if isinstance(x,arb_mat):
        return {'matrix':[x.nrows(),x.ncols(),[pack(x[i,j])for i in range(x.nrows())for j in range(x.ncols())]]}
    if isinstance(x,dict):return {'mapping':[[k,pack(v)]for k,v in x.items()]}
    if isinstance(x,(list,tuple)):return [pack(v)for v in x]
    need(x is None or isinstance(x,(int,str,bool)),'Unsupported checkpoint type')
    return x


def unpack(x):
    if isinstance(x,list):return [unpack(v)for v in x]
    if isinstance(x,dict):
        if set(x)=={'ball'}:
            m,e,r,s=x['ball'];return arb((m,e),(r,s))
        if set(x)=={'matrix'}:
            n,m,values=x['matrix'];need(len(values)==n*m,'Checkpoint matrix dimensions')
            values=[unpack(v)for v in values]
            return arb_mat(n,m,values)
        if set(x)=={'mapping'}:return {k:unpack(v)for k,v in x['mapping']}
        raise RuntimeError('Unknown checkpoint record')
    need(x is None or isinstance(x,(int,str,bool)),'Unexpected checkpoint scalar')
    return x


class Checkpoint:
    def __init__(self,path,parameters):
        self.path=Path(path);self.path.mkdir(parents=True,exist_ok=True)
        self.binding={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                      for name in ('common.py','residuals.py','old_fields.py','source_bounds.py','integrate.py','checkpoint.py','INPUT_BINDINGS.json')}
        self.binding['parameters']=parameters

    def load(self,name):
        p=self.path/(name+'.json.gz')
        if not p.exists():return None
        raw=p.read_bytes();body=json.loads(gzip.decompress(raw))
        need(body['binding']==self.binding,'Checkpoint has a different program or inputs; use a new work directory')
        payload=body['payload'].encode()
        need(hashlib.sha256(payload).hexdigest()==body['sha256'],'Checkpoint checksum')
        return unpack(json.loads(payload))

    def save(self,name,state):
        payload=json.dumps(pack(state),separators=(',',':'))
        body={'binding':self.binding,'sha256':hashlib.sha256(payload.encode()).hexdigest(),'payload':payload}
        raw=gzip.compress(json.dumps(body,separators=(',',':')).encode(),compresslevel=1,mtime=0)
        p=self.path/(name+'.json.gz');tmp=self.path/(name+'.pending')
        tmp.write_bytes(raw);os.replace(tmp,p)
