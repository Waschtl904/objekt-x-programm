#!/usr/bin/env python3
"""Bounded repair replay; inherited analytic identification remains open."""
import sys
if not __debug__:
    raise SystemExit('Verification requires assertions enabled; Python -O/-OO is rejected.')
sys.dont_write_bytecode=True
from pathlib import Path, PurePosixPath
from fractions import Fraction as Q
import argparse, hashlib, json, shutil, subprocess, tempfile
from kernel_geometry import controls
from corrected_builder import corrected_source
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]

def need(ok, message):
    if not ok: raise RuntimeError(message)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def read(path):return json.loads(path.read_bytes())
def within(root, name):
    pp=PurePosixPath(name)
    need(not pp.is_absolute() and '..' not in pp.parts and '\\' not in name,'Invalid bound path')
    p=root.joinpath(*pp.parts)
    need(p.resolve().is_relative_to(root.resolve()) and not p.is_symlink(),'Escaping/symlink input')
    return p

def bindings():
    manifest=read(HERE/'MANIFEST.json')
    actual={p.relative_to(HERE).as_posix()for p in HERE.rglob('*')if p.is_file()}
    need(set(manifest)==actual-{'MANIFEST.json'},'Package manifest coverage')
    for name,h in manifest.items():need(sha(within(HERE,name))==h,'Package hash: '+name)
    old=read(HERE/'INPUT_BINDINGS.json')['repository_files']
    for name,h in old.items():need(sha(within(ROOT,name))==h,'Inherited input hash: '+name)
    return len(manifest),len(old)

def run(path,*args):
    proc=subprocess.run([sys.executable,'-B',str(path),*map(str,args)],cwd=path.parent,
                        text=True,capture_output=True,timeout=900)
    need(proc.returncode==0,f'{path.name} failed:\n{proc.stdout}\n{proc.stderr}')
    return proc.stdout

def math_fields(value):return {k:v for k,v in value.items()if k!='seconds'}

def replay_core(work, panels=False):
    source=HERE/'pairing-review/connection-audit/repair-review/work'
    dest=work/'core';refine=dest/'pairing-refinement';check=dest/'pairing-check'
    refine.mkdir(parents=True);check.mkdir()
    for name in ['kernel_orientation.py','core_tail_review.py','add_panels.py']:
        shutil.copyfile(source/'pairing-refinement'/name,refine/name)
    shutil.copyfile(HERE/'norm/inputs/kernel-orientation-81.json',refine/'kernel-orientation-81.json')
    code=(source/'pairing-check/run_pairs.py').read_text(encoding='utf-8')
    replacements={"ROOT=(BASE/'snapshot').resolve()":'ROOT=Path('+repr(str(ROOT))+').resolve()',
      "ORIGINAL=BASE.parent/'repo/research/x-c1/w9-residual-centered-control-even-2026-10-21'":"ORIGINAL=ROOT/'research/x-c1/w9-residual-centered-control-even-2026-10-21'",
      "BASE.parent/'research-review/data/whole-model-ed58da3caacd.json.gz'":"WHOLE/'whole-model-ed58da3caacd.json.gz'"}
    for a,b in replacements.items():
        need(code.count(a)==1,'Bootstrap adapter binding: '+a);code=code.replace(a,b)
    (check/'run_pairs.py').write_text(code,encoding='utf-8')
    run(refine/'core_tail_review.py')
    need(math_fields(read(refine/'core-tail.json'))==math_fields(read(HERE/'norm/inputs/core-tail.json')),
         'Radius-corrected core-tail mathematical result changed')
    contour=read(refine/'contour-review.json')
    R=Q(contour['normalized_radius'][0]);M=Q(contour['corrected_contour_bound'][1])
    need(R>1 and M*R**(-8)/(1-1/R)<Q('1.682e-88'),'Cauchy tail cap')
    if panels:
        run(refine/'add_panels.py')
        receipts=list((refine/'extra-panels').glob('*.json'));need(len(receipts)==16,'16 replay panels required')
        for p in receipts:
            need(math_fields(read(p))==math_fields(read(HERE/'pairing-review/Replayed-panels'/p.name)),
                 'Signed panel changed: '+p.name)
    return {'corrected_core_tail_rows':84,'contour_remainder_upper_cap':'1.682e-88','new_panels_recomputed':16 if panels else 0}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true')
    ap.add_argument('--bindings-only',action='store_true');ap.add_argument('--replay-panels',action='store_true')
    ap.add_argument('--report',type=Path);args=ap.parse_args()
    package_count,old_count=bindings()
    need(controls()['signed_defect']=='1/24','Kernel controls')
    source=corrected_source(ROOT)
    need('regular_core(ym)(arb_poly([0,a]))'in source,'Corrected inner source')
    compile(source,'corrected_builder_candidate','exec')
    report={'status':'BOUND_REPAIR_REPLAY_PASS_CONDITIONAL','package_files':package_count,
      'inherited_files':old_count,'mathematical_status':'AUTHOR_DERIVED','external_review':'EXTERNAL_REVIEW_OPEN',
      'complete_model_identification_accepted':False,'all_inherited_analytic_lemmas_reproved':False}
    if not args.bindings_only:
        with tempfile.TemporaryDirectory(prefix='objekt-x-repair-')as temp:
            work=Path(temp);norm=work/'norm';review=work/'pairing-review'
            shutil.copytree(HERE/'norm',norm);shutil.copytree(HERE/'pairing-review',review)
            run(review/'verify_package.py')
            expected=math_fields(read(norm/'independent-norm.json'))
            run(norm/'independent_norm.py')
            need(math_fields(read(norm/'independent-norm.json'))==expected,'Independent norm mathematical fields changed')
            run(norm/'rational_cross_audit.py')
            fresh=read(norm/'cross-audit.json');stored=read(HERE/'norm/cross-audit.json')
            fresh.pop('new_norm_result_sha256');stored.pop('new_norm_result_sha256')
            need(fresh==stored,'Cross audit mathematical fields changed')
            report.update(replay_core(work,args.replay_panels))
            report.update({'whole_arithmetic_hulls_inside_errors':84,'direct_energy_upper_cap':'4.632e-11',
                           'operator_energy_upper_cap':'1.391e-10','retained_energy_cap':'1e-9'})
    if args.report:
        need(not args.report.resolve().is_relative_to(HERE),'Report must be outside the bound package')
        args.report.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__':
    try:main()
    except (RuntimeError,ValueError,OSError,subprocess.TimeoutExpired)as exc:
        print('REPAIR CHECK FAILED: '+str(exc),file=sys.stderr);raise SystemExit(1)
