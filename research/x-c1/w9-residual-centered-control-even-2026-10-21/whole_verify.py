"""Bound whole-result audit; optional fresh reconstruction of every model panel."""
import argparse,hashlib,json,os,subprocess,sys,tempfile,time
from pathlib import Path
from types import ModuleType
HERE=Path(__file__).resolve().parent
REL=Path('research/x-c1')/HERE.name

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def dump(x):return (json.dumps(x,indent=2)+'\n').encode()

def snapshots():
    entries=json.loads((HERE/'MANIFEST.json').read_bytes());data={}
    for name,want in entries.items():
        path=(HERE/name).resolve();need(path.is_relative_to(HERE.resolve()),'Escaping package path')
        raw=path.read_bytes();need(hashlib.sha256(raw).hexdigest()==want,'Package hash: '+name)
        data[name]=raw
    return data

def run_audit(folder,raw):
    m=ModuleType('bound_whole_residual_audit');m.__file__=str(folder/'whole_audit.py')
    exec(compile(raw,m.__file__,'exec'),m.__dict__)
    return dump(m.audit(folder))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repository',type=Path,default=HERE.parents[2])
    ap.add_argument('--recompute',action='store_true',help='Rebuild both core models and all 411 Taylor panels; potentially over one hour.')
    ap.add_argument('--output-dir',type=Path)
    args=ap.parse_args();need(__debug__,'Do not disable assertions')
    data=snapshots()
    dependencies={}
    for rel,want in json.loads(data['REPLAY_BINDINGS.json'])['repository_files'].items():
        if rel.startswith(str(REL).replace('\\','/')+'/'):continue
        source=(args.repository/rel).resolve()
        need(source.is_relative_to(args.repository.resolve()),'Dependency path')
        raw=source.read_bytes();need(hashlib.sha256(raw).hexdigest()==want,'Dependency hash: '+rel)
        dependencies[rel]=raw
    with tempfile.TemporaryDirectory(prefix='w9-whole-')as td:
        work=Path(td)/'work';task=work/'w9-coherent-rest-search-20261021';task.mkdir(parents=True)
        for name,raw in data.items():
            if name.startswith('whole/'):
                target=task/name[6:];need(target.resolve().is_relative_to(task.resolve()),'Whole path')
                target.parent.mkdir(parents=True,exist_ok=True)
                if args.recompute and (target.suffix=='.gz' or 'taylor-model-panels-205' in target.parts):continue
                target.write_bytes(raw)
        if args.recompute:
            root=work/'objekt-x-integration-20261019';root.mkdir()
            for rel,raw in dependencies.items():
                target=root/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
            for name,raw in data.items():
                if name.startswith('whole/'):continue
                target=root/REL/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
            def run(name,extra=(),cwd=task):
                subprocess.run([sys.executable,'-u','-B',str(cwd/name),*map(str,extra)],cwd=cwd,check=True)
            run('verify.py',['--repository',root,'--check'],root/REL)
            for source,n in [('whole_function_probe.py',64),('whole_function_probe_v2.py',128)]:
                run('portable_entry.py',[source,'--nodes',n])
            for name in ('whole-model-ed58da3caacd.json.gz','whole-model-36d3f3fcb6cb-n128.json.gz'):
                need((task/name).read_bytes()==data['whole/'+name],'Model cache byte replay: '+name)
            common=['--cache',task/'whole-model-ed58da3caacd.json.gz']
            run('cut_audit.py');run('endpoint_preflight.py',common);run('analytic_caps.py',common)
            run('core_quadrature_control_128.py',['--cache',task/'whole-model-36d3f3fcb6cb-n128.json.gz','--source',task/'whole_function_probe_v2.py'])
            run('core_model_bridge.py');run('whole_error_inventory.py')
            workers=[]
            for first,last in ((0,136),(137,273),(274,410)):
                env=dict(os.environ,W9_PANEL_FIRST=str(first),W9_PANEL_LAST=str(last))
                workers.append(subprocess.Popen([sys.executable,'-u','-B',str(task/'taylor_whole_model.py'),*map(str,common),'--panels','205','--suffix=-205'],cwd=task,env=env))
            failed=[]
            for p in workers:
                p.wait()
                if p.returncode:failed.append(p.returncode)
            need(not failed,'Taylor replay worker failed')
            for rel in ('endpoint-ingredients.json','analytic-caps.json','cut-audit.json','core-quadrature-control-128.json','core-model-bridge.json','whole-error-ledger.json','taylor-model-panels-205/SUMMARY.json'):
                path=task/rel;path.write_bytes(dump(json.loads(path.read_bytes())))
        result=run_audit(task,data['whole/whole_audit.py'])
        need(result==data['whole/WHOLE_RESULT.json'],'Whole result byte equality')
        if args.output_dir:
            args.output_dir.mkdir(parents=True,exist_ok=True)
            out=args.output_dir/'WHOLE_RESULT.json';need(not out.exists(),'Refuse output overwrite');out.write_bytes(result)
        print('PASS:',json.loads(result)['outcome'],
              '(fresh complete recomputation)'if args.recompute else'(bound whole-result arithmetic audit; no repeated integration)',flush=True)

if __name__=='__main__':main()
