"""Choose a simple rational common reserve below both certified intervals."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json

here=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--input',type=Path,default=here/'reserve_results.json')
parser.add_argument('--output',type=Path,default=here/'common_reserve.json')
args=parser.parse_args()
source=args.input
data=json.loads(source.read_bytes())
assert data['both_parities_strictly_certified']
assert all(row['positive_directed_pivots']==296 for row in data['parities'].values())
scale=10**data['scale_digits']
lower=min(F(int(row['full_physical_reserve'][0]),scale) for row in data['parities'].values())
assert lower>0
physical=F(1)
while physical>=lower:physical/=10
defect=physical/(physical+12)
assert all(F(int(row['full_defect_reserve'][0]),scale)>defect for row in data['parities'].values())
result={'status':'COMMON_RATIONAL_RESERVE_PASS',
    'endpoint':'A9=log(3)', 'reserve_results_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'common_physical_floor_exact':str(physical),'common_defect_floor_exact':str(defect),
    'claim':'Conditional on PROOF.md and the complete model, both parities exceed these rational floors.',
    'external_review':'OPEN','repository_status_changed':False}
args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('Common physical reserve '+str(physical)+'; common defect reserve '+str(defect))
