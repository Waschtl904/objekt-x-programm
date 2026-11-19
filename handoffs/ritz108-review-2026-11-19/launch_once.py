"""Single-use process launcher; no mathematical imports or parameter changes."""
from pathlib import Path
import subprocess,sys,json,time,hashlib
from datetime import datetime,timezone
HERE=Path(__file__).resolve().parent
def utc():return datetime.now(timezone.utc).isoformat()
auth=json.loads((HERE/'REPEAT_AUTHORIZATION.json').read_bytes())
assert hashlib.sha256((HERE/'single_measurement.py').read_bytes()).hexdigest()==auth['new_script_sha256']
assert not (HERE/'single_run/START.json').exists()
with (HERE/'EXECUTION_LOCK').open('x',encoding='utf-8') as f:f.write('One authorized invocation only. Do not remove or reuse.\n')
started=utc();tick=time.monotonic()
(HERE/'LAUNCH.json').write_text(json.dumps({'started_utc':started,'script_sha256':auth['new_script_sha256'],'maximum_seconds':14400,'authorized_runs':1},indent=2)+'\n')
with (HERE/'SINGLE_RUN.log').open('wb') as log:
    process=subprocess.run([sys.executable,'-B','-X','utf8',str(HERE/'single_measurement.py')],stdout=log,stderr=subprocess.STDOUT,cwd=HERE.parent.parent)
record={'started_utc':started,'finished_utc':utc(),'elapsed_seconds':time.monotonic()-tick,'exit_code':process.returncode,'script_sha256':auth['new_script_sha256'],'log_sha256':hashlib.sha256((HERE/'SINGLE_RUN.log').read_bytes()).hexdigest(),'result_written':(HERE/'single_run/RESULT.json').exists()}
(HERE/'PROCESS_END.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
sys.exit(process.returncode)
