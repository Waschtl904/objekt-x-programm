from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
review=ROOT/'work/infinite-dual-review-input-2026-10-11/Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11'
s=(review/'code/compute_external_probe.py').read_text(encoding='utf-8')
s=s[:s.index('# Batched complete integrals.')]
s=s.replace("ap.add_argument('--proposal'", "ap.add_argument('--probe-model',type=Path,required=True)\nap.add_argument('--proposal'")
s=s.replace('NJ=1+args.count\nNC=NJ+8','NJ=84+args.count\nNC=NJ')
s=s.replace('assert 1<=args.count<=32','assert args.count==8')
s=s.replace("       'inverse':", "       'frozen_J':ROOT/f'work/galerkin84-2026-10-10/MODEL_RAY_{args.parity.upper()}_3072.json',\n       'frozen_K':args.probe_model,\n       'inverse':")
s=s.replace('for i in range(96):YL[i,0]=critical[i,0]', 'for i in range(96):\n    for j in range(84):YL[i,j]=J84[i,j]')
s=s.replace('enumerate(range(96,NLOC),1)', 'enumerate(range(96,NLOC),84)')
s=s.replace('Rmid=arb_mat([[YL[i,j].mid() for j in range(NJ)] for i in range(NLOC)])',
 "fj=data['frozen_J']['working_basis_midpoints_rational'];fk=data['frozen_K']['working_local_coefficients_rational']\nRmid=arb_mat([[af(fj[i][j]) if i<96 and j<84 else arb(0) if j<84 else af(fk[i][j-83]) for j in range(NJ)] for i in range(NLOC)])")
start=s.index('Ymid=arb_mat(');end=s.index('\ndefinition=',start)
s=s[:start]+'Ymid=Rmid'+s[end:]
s=s.replace("definition='r0=J84*wJ; k_n=", "definition='all J84 columns, then k_n=")
s+='\n'+(HERE/'cross_tail.py').read_text(encoding='utf-8')
(HERE/'compute_cross.py').write_text(s,encoding='utf-8')
print('Generated full-source J84/exterior8 cross integrator')
