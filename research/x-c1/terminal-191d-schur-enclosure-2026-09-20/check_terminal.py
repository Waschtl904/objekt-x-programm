#!/usr/bin/env python3
"""Verify actual terminal Schur matrices, rational witnesses and full replays.

No sampled eigenvalues, finite-tail replacement, or assumed Weil positivity.
The analytic enclosure argument is in PROOF.md. External review remains open.
"""
from pathlib import Path
import argparse,contextlib,gzip,hashlib,io,json,runpy
import flint
from flint import arb,arb_mat,fmpq,ctx
from generate_terminal_matrices import compute,ldl,gamma_polynomial

HERE=Path(__file__).resolve().parent
PAYLOAD=['PROOF.md','README.md','META.yaml','requirements.txt','generate_terminal_matrices.py',
         'STATUS_DE.md','check_normalization.py','check_terminal.py','input_bindings.json','terminal_matrices.json.gz',
         'terminal_results.json','terminal_checks.log']

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--verify',action='store_true');ap.add_argument('--write',action='store_true')
    ap.add_argument('--recompute',action='store_true');ap.add_argument('--recomputed-model',type=Path)
    args=ap.parse_args();root=HERE.parents[2];checks=[];values={}
    def check(name,condition):
        if not condition:raise RuntimeError(name)
        checks.append(name)
    check('pinned rigorous arithmetic version',flint.__version__=='0.9.0')
    data=json.loads(gzip.decompress((HERE/'terminal_matrices.json.gz').read_bytes()))
    check('actual terminal dimensions and arithmetic parameters',data['endpoint']==1 and data['cutoff']==383 and data['Gamma_degree']==128 and data['precision_bits']==2048 and data['scale_digits']==55 and data['preconditioner_scale_digits']==80)
    binding=json.loads((HERE/'input_bindings.json').read_bytes())
    check('analytic input anchor is the frozen Schur bridge',binding['anchor']=='79988874cceeb01f17e0cda67485838c0b7c4f63')
    for item in binding['files']:
        raw=(root/item['path']).read_bytes()
        check('pinned input '+item['path'],hashlib.sha256(raw).hexdigest()==item['sha256'] and hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==item['git_blob'])
    normalization=io.StringIO()
    with contextlib.redirect_stdout(normalization):runpy.run_path(str(HERE/'check_normalization.py'),run_name='__main__')
    check('64 independent normalization identities','TOTAL 64 normalization checks PASS' in normalization.getvalue())
    if args.recompute or args.recomputed_model:
        model=json.loads(args.recomputed_model.read_bytes()) if args.recomputed_model else compute()
        for key in ('endpoint','cutoff','Gamma_degree','precision_bits','scale_digits','Gamma_kernel_error','form_error'):
            check('recomputed model parameter '+key,model[key]==data[key])
        for parity in ('even','odd'):
            r=model['parities'][parity]
            for name in ('A','complete_coupling_Gram'):
                tri=[[r[name][i][j][0],str(int(r[name][i][j][1])-int(r[name][i][j][0]))] for i in range(191) for j in range(i+1)]
                check('recomputed every actual '+parity+' '+name+' enclosure',tri==data['parities'][parity][name+'_triangle'])
    ctx.prec=512;scale=10**55
    def ball(pair):
        lo,hi=map(int,pair)
        if lo>hi:raise RuntimeError('unordered interval')
        return arb(lo+hi)/(2*scale)+arb(0,arb(hi-lo)/(2*scale))
    def matrix_from_triangle(tri):
        if len(tri)!=191*192//2:raise RuntimeError('triangle length')
        out=arb_mat(191,191);k=0
        for i in range(191):
            for j in range(i+1):
                lo,width=map(int,tri[k]);k+=1
                if width<0:raise RuntimeError('negative interval width')
                out[i,j]=out[j,i]=ball([lo,lo+width])
        return out
    delta=arb(7)/10;rho=arb(9)/10;error=arb(fmpq(5,10**26))
    check('rational complete form error budget matches artifact',data['form_error_budget']==str(fmpq(5,10**26)))
    check('fixed terminal tail and certificate margin',data['high_floor']=='7/10' and data['rho']=='9/10')
    pg,eps=gamma_polynomial(128)
    check('full Gamma polynomial error bound',arb(eps)<arb(fmpq(12,10**27)))
    check('stored Gamma interval contains the exact residual bound',ball(data['Gamma_kernel_error']).contains(arb(eps)))
    from math import factorial
    moment=arb(5)/2**384/arb(factorial(384))/(1-arb(1)/(4*385*386))
    check('complete high Mellin correction is below 10^-100',moment<arb(fmpq(1,10**100)))
    check('Gamma and moment form errors fit the rational budget',4*arb(eps)+80*moment<error)
    H=sum((arb(1)/k for k in range(1,385)),arb(0))
    q0=-(2*arb.pi()).log()-arb.const_euler()
    g2=(-arb(1)).exp()/(1-(-arb(4)).exp())-arb(1)/4
    snorm=arb(2).log()+sum((arb(p).log()/arb(q).sqrt() for q,p in [(3,3),(4,2),(5,5),(7,7)]),arb(0))
    raw_floor=H+q0-2*(arb(1)/4-g2)-snorm
    check('five terminal channels and three-vertex prime2 chains',arb(7).log()<2<arb(8).log() and arb(3).log()>1)
    check('regular Gamma endpoint lies strictly between zero and one quarter',g2>0 and g2<arb(1)/4)
    check('independent terminal raw high floor exceeds 73/100',raw_floor>arb(73)/100)
    check('actual moment-corrected terminal high floor exceeds 7/10',raw_floor-16*moment-12*moment**2>delta)
    for parity in ('even','odd'):
        r=data['parities'][parity];check(parity+' dimension 191',r['dimension']==191)
        A=matrix_from_triangle(r['A_triangle']);G=matrix_from_triangle(r['complete_coupling_Gram_triangle'])
        P=arb_mat(191,191);k=0
        check(parity+' complete rational triangular preconditioner',len(r['preconditioner_lower_triangle'])==191*192//2)
        for i in range(191):
            for j in range(i+1):P[i,j]=arb(fmpq(int(r['preconditioner_lower_triangle'][k]),10**80));k+=1
        lower=A-G*(arb(1001)/1000)/delta
        for i in range(191):lower[i,i]-=error+1001*error**2/delta
        certified=P*lower*P.transpose()
        for i in range(191):
            row=certified[i,i]-sum((certified[i,j].abs_upper() for j in range(191) if i!=j),arb(0))
            check(parity+' complete directed row '+str(i)+' exceeds 9/10',row>rho)
        for i in range(191):certified[i,i]-=rho
        _,piv,fail=ldl(certified)
        check(parity+' all 191 directed LDL pivots are positive',fail is None and len(piv)==191 and all(d>0 for d in piv))
        trace=(P*P.transpose()).trace();sigma=arb(fmpq(r['schur_sigma']))
        check(parity+' certified Euclidean physical Schur reserve',trace*sigma<rho)
        coupling=(arb(1001)/1000)*G.trace()+191*1001*error**2
        check(parity+' complete inverse shear squared below 169',coupling/delta**2<169)
        gap=arb(fmpq(r['physical_gap']))
        check(parity+' physical norm conversion and strict gap',sigma/(2*196)>gap)
        values[parity]={'dimension':191,'directed_positive_LDL_pivots':len(piv),'Schur_reserve':r['schur_sigma'],
                       'physical_gap':r['physical_gap'],'inverse_shear_norm_upper':14,'preconditioned_floor':'9/10'}
    common=fmpq(1,10**26);defect=fmpq(1,10**28)
    check('uniform all-parity physical gap',all(fmpq(r['physical_gap'])>=common for r in data['parities'].values()))
    check('terminal strict defect reserve',common/(fmpq(23,2)+common)>defect)
    values.update(uniform_physical_gap=str(common),strict_defect_reserve=str(defect),high_floor='7/10',form_error_budget=str(fmpq(5,10**26)))
    # Replay checks are reported separately, so the stable certificate log is
    # identical with and without the optional, expensive matrix regeneration.
    core=[name for name in checks if not name.startswith('recomputed ')]
    result={'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','verdict':'STRICT_POSITIVE_BOTH_PARITIES',
            'scope':'Actual two-Mellin sources, 0<a<=1; fixed horizon 1 only.',
            'checks':core,'check_count':len(core),'values':values,
            'complete_infinite_high_response_paid':True,'negative_full_Weil_source_claimed':False,
            'Object_X_constructed':False,'RH_claimed':False}
    raw=(json.dumps(result,indent=2,sort_keys=True)+'\n').encode()
    log=('\n'.join('PASS '+x for x in core)+'\nTOTAL '+str(len(core))+' terminal certificate checks PASS\nSTATUS AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN\n').encode()
    if args.write:
        (HERE/'terminal_results.json').write_bytes(raw);(HERE/'terminal_checks.log').write_bytes(log)
        (HERE/'SHA256SUMS').write_text(''.join(hashlib.sha256((HERE/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in PAYLOAD),encoding='ascii',newline='\n')
    if args.verify:
        check('byte-identical certificate results',(HERE/'terminal_results.json').read_bytes()==raw)
        check('byte-identical certificate log',(HERE/'terminal_checks.log').read_bytes()==log)
        lines=(HERE/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        check('exact payload manifest',[x.split('  ',1)[1] for x in lines]==PAYLOAD)
        for entry in lines:
            sha,name=entry.split('  ',1);check('payload '+name,hashlib.sha256((HERE/name).read_bytes()).hexdigest()==sha)
    print('TOTAL',len(core),'terminal certificate checks PASS; both parities STRICT_POSITIVE')
    print('PHYSICAL GAP > 10^-26 on 0<a<=1; fixed horizon; external review OPEN')
    if args.recompute or args.recomputed_model:print('PASS every regenerated actual A/G matrix enclosure matches the stored certificate')
    if args.verify:print('PASS byte-identical results/log and all twelve payload hashes')

if __name__=='__main__':main()
