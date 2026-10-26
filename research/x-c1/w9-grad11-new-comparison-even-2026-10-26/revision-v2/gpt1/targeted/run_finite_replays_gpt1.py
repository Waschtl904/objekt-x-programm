"""Bounded v2 reproduction in a disposable copy, without integrations."""
import os, sys, json, time, subprocess, hashlib
from pathlib import Path

if sys.flags.optimize or not __debug__:
    raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
P=Path(__file__).resolve().parent
H=P/'replay/workspace/work/breakthrough-2026-10-25'
S=P/'merged/workspace/work/breakthrough-2026-10-25/revision_v2'
env=os.environ.copy()
env['OBJX_FLINT_PATH']=str(P.parent/'grad11-review/deps')
env.pop('PYTHONOPTIMIZE',None)
stages=[
 ['run_reproduction_v2.py','source_block_ledger_v2.py','--gamma-reserve'],
 ['run_reproduction_v2.py','source_arithmetic_closure_v2.py'],
 ['run_reproduction_v2.py','record_exact_gram_radii_v2.py'],
 ['audit_closed_source_gap_v2.py'],
 ['joint_tail_geometry_v2.py'],
 ['run_reproduction_v2.py','batch_physical_errors_v2.py'],
 ['joint_rest_budget_v2.py'],
]
results=[]
for stage in stages:
    name=stage[1] if stage[0]=='run_reproduction_v2.py' else stage[0]
    start=time.monotonic()
    r=subprocess.run([sys.executable,'-B',*stage],cwd=H,env=env,capture_output=True,text=True,timeout=600)
    record={'stage':stage,'exit_code':r.returncode,'seconds':time.monotonic()-start,'stdout':r.stdout,'stderr':r.stderr}
    results.append(record)
    (P/'FINITE_REPLAY_EXECUTION.json').write_text(json.dumps(results,indent=2)+'\n')
    print(name, 'exit', r.returncode, 'seconds', round(record['seconds'],2),flush=True)
    if r.returncode:
        print(r.stdout+r.stderr,flush=True)
        raise SystemExit(r.returncode)
print('ALL_SEVEN_REPRICING_STAGES_COMPLETE',flush=True)
