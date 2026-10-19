"""Fresh full replay from checked source snapshots; no subprocess execution."""
import gc
import argparse
import gzip
import hashlib
import json
import sys
import tempfile
from pathlib import Path
from types import ModuleType

HERE=Path(__file__).resolve().parent


def require(condition,message):
    if not condition:
        raise RuntimeError(message)


def own_snapshot():
    spec=json.loads((HERE/'MANIFEST.json').read_bytes())
    own={}
    for name,digest in spec.items():
        path=(HERE/name).resolve()
        require(path.is_relative_to(HERE),'Escaping package path')
        raw=path.read_bytes()
        require(hashlib.sha256(raw).hexdigest()==digest,'Own binding failed: '+name)
        own[name]=raw
    return own


def checked_module(name,own):
    filename=name+'.py'
    require(filename in own,'Unbound executable module: '+name)
    module=ModuleType(name);module.__file__=str(HERE/filename)
    sys.modules[name]=module
    exec(compile(own[filename],module.__file__,'exec'),module.__dict__)
    return module


def input_snapshot_controls(common,InputClass):
    original_root=common.ROOT
    with tempfile.TemporaryDirectory(prefix='w9-input-control-')as td:
        root=Path(td);path=root/'value.json';raw=b'{"value":1}'
        path.write_bytes(raw)
        entry={'path':'value.json','sha256':hashlib.sha256(raw).hexdigest()}
        def spec(item):
            return json.dumps({'files':{'test':item},'members':{}}).encode()
        common.ROOT=root
        try:
            snapshot=InputClass(binding_bytes=spec(entry))
            path.write_bytes(b'{"value":2}')
            require(snapshot.json('test')=={'value':1},'Input snapshot was reread')
            for bad in (entry,dict(entry,path='../escape.json')):
                try:
                    InputClass(binding_bytes=spec(bad))
                except RuntimeError:
                    pass
                else:
                    raise RuntimeError('Invalid input binding accepted')
        finally:
            common.ROOT=original_root
    print('PASS: immutable input snapshot, wrong digest and escaping path controls',flush=True)


def historical_source_controls(common,InputClass):
    """A named historical source stays exact without reverting the live file."""
    original_root=common.ROOT
    ((alias,old_path,digest),snapshot_path),=common.PROVENANCE_SNAPSHOTS.items()
    original=(original_root/snapshot_path).read_bytes()
    require(hashlib.sha256(original).hexdigest()==digest,'Historical source digest')
    with tempfile.TemporaryDirectory(prefix='w9-provenance-control-')as td:
        root=Path(td);historical=root/snapshot_path;live=root/old_path
        historical.parent.mkdir(parents=True);live.parent.mkdir(parents=True)
        historical.write_bytes(original);live.write_bytes(b'current corrected input loader')
        entry={'path':old_path,'sha256':digest}
        def spec(name,item):
            return json.dumps({'files':{name:item},'members':{}}).encode()
        common.ROOT=root
        try:
            frozen=InputClass(binding_bytes=spec(alias,entry))
            require(frozen.data[alias]==original,'Historical source not preserved')
            require(live.read_bytes()==b'current corrected input loader','Live source changed')
            historical.write_bytes(b'corrupt')
            for name,item in ((alias,entry),('other',entry),
                              (alias,dict(entry,sha256='0'*64)),
                              (alias,dict(entry,path='../escape'))):
                try:
                    InputClass(binding_bytes=spec(name,item))
                except RuntimeError:
                    pass
                else:
                    raise RuntimeError('Invalid historical source binding accepted')
        finally:
            common.ROOT=original_root
    print('PASS: historical source, live loader, corruption, alias and path controls',flush=True)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--bindings-only',action='store_true',
                        help='Check immutable inputs and regressions; do not integrate functions')
    args=parser.parse_args()
    require(__debug__,'Run verification without python -O')
    own=own_snapshot()
    common=checked_module('common',own)
    InputClass=common.Inputs
    input_snapshot_controls(common,InputClass)
    historical_source_controls(common,InputClass)
    if args.bindings_only:
        InputClass(binding_bytes=own['INPUT_BINDINGS.json'])
        print('PASS: all bound source and archive-member bytes; no integration run',flush=True)
        return
    # All later callers receive the same checked binding specification. Each
    # instance then parses only its independently hash-checked input bytes.
    common.Inputs=lambda:InputClass(binding_bytes=own['INPUT_BINDINGS.json'])
    modules={'common':common}
    for name in ('residuals','old_fields','source_bounds','checkpoint','integrate','weights','assemble',
                 'controls','source_controls','certify_k','compare_candidate'):
        modules[name]=checked_module(name,own)
    from flint import ctx

    def encoded(value):
        return (json.dumps(common.encode(value),indent=2)+'\n').encode()

    def compare(name,raw):
        require(name in own,'Missing expected output: '+name)
        require(raw==own[name],'Replay differs: '+name)
        print('BYTE_EQUAL',name,flush=True)

    ctx.prec=800;inp=common.Inputs()
    values={par:modules['weights'].build(inp,par)[0]for par in ('even','odd')}
    compare('WEIGHT_BOUNDS.json',encoded(values))
    del inp,values;gc.collect()
    compare('CONTROLS.json',encoded(modules['controls'].run()))
    compare('SOURCE_CONTROLS.json',encoded(modules['source_controls'].run()))
    gc.collect()

    with tempfile.TemporaryDirectory(prefix='w9-partial-fresh-')as td:
        td=Path(td)
        for par in ('even','odd'):
            pair_path=td/('PAIRS_'+par+'.json')
            # This work directory is fresh and cannot import development cells.
            modules['integrate'].run(par,pair_path,work=td/('cells_'+par))
            pair_bytes=gzip.compress(pair_path.read_bytes(),compresslevel=9,mtime=0)
            compare('expected/PAIRS_'+par+'.json.gz',pair_bytes)
            gz_path=pair_path.with_suffix('.json.gz');gz_path.write_bytes(pair_bytes)
            data=modules['assemble'].load_pairs(gz_path)
            ctx.prec=800;inp=common.Inputs()
            compare('expected/ENERGY_'+par+'.json',encoded(modules['assemble'].assemble(inp,data)))
            compare('expected/K_BASELINE_'+par+'.json',encoded(modules['certify_k'].baseline(inp,data)))
            candidate_raw=own['expected/CANDIDATE_'+par+'.json'];candidate=json.loads(candidate_raw)
            require(candidate['parity']==par,'Frozen candidate parity')
            require(candidate['pairs_sha256']==data['_source_sha256'],'Frozen candidate pairing hash')
            kp=modules['certify_k'].certify(inp,data,candidate['raw_coefficients'])
            kp['candidate_sha256']=hashlib.sha256(candidate_raw).hexdigest()
            k_raw=encoded(kp)
            compare('expected/K_P_'+par+'.json',k_raw)
            result=modules['compare_candidate'].compare(inp,data,candidate_raw,k_raw)
            compare('expected/COMPARISON_'+par+'.json',encoded(result))
            del inp,data,kp,result,pair_bytes;gc.collect()
    print('PASS: both full pairing integrations and fixed-direction partial-energy/K_P certificates '
          'replayed byte-for-byte; RL and N12 remain open; external mathematical review open',flush=True)


if __name__=='__main__':main()
