"""Compare a separately certified K_P interval with one frozen partial energy."""
import argparse
import hashlib
import json
from pathlib import Path
from flint import ctx
from common import Inputs,need,encode
from assemble import Energy,load_pairs


def compare(inp,data,candidate_raw,k_raw):
    frozen=json.loads(candidate_raw);kp=json.loads(k_raw)
    digest=hashlib.sha256(candidate_raw).hexdigest()
    need(frozen['parity']==kp['parity']==data['parity'],'Comparison parity')
    need(frozen['pairs_sha256']==data['_source_sha256'],'Frozen pairing binding')
    need(kp['candidate_sha256']==digest,'Certified candidate binding')
    need(frozen['raw_coefficients']==kp['raw_coefficients'],'Coefficient identity')
    result=Energy(inp,data).certificate(frozen['raw_coefficients'],kp['K_P_interval'],
                                      'frozen_partial_energy_candidate_'+data['parity'])
    result.update(parity=data['parity'],pairs_sha256=data['_source_sha256'],
                  candidate_sha256=digest,K_P_certificate_sha256=hashlib.sha256(k_raw).hexdigest(),
                  status='AUTHOR_DERIVED_CONDITIONAL_PARTIAL_ENERGY_EXTERNAL_REVIEW_OPEN',
                  criterion='FIXED_W9_COMPARISON_RULE_PARTIAL_LOWER_VS_K_P_UPPER')
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('pairs',type=Path)
    ap.add_argument('candidate',type=Path);ap.add_argument('kp',type=Path)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();ctx.prec=800
    data=load_pairs(args.pairs);candidate_raw=args.candidate.read_bytes();k_raw=args.kp.read_bytes()
    result=compare(Inputs(),data,candidate_raw,k_raw)
    args.output.write_text(json.dumps(encode(result),indent=2)+'\n')
    print(result['parity'],result['partial_actual_energy_interval'],result['budget_interval_or_upper'],result['outcome'],flush=True)
