from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
s=(ROOT/'work/galerkin84-2026-10-10/compute_galerkin84.py').read_text(encoding='utf-8')
s=s[:s.index('# Batched complete integrals.')]
s=s.replace('ROOT=HERE.parents[1]', "ROOT=Path(sys.argv[sys.argv.index('--root')+1]).resolve() if '--root' in sys.argv else HERE.parents[1]")
s=s.replace("ap.add_argument('--bits'", "ap.add_argument('--root',type=Path)\nap.add_argument('--bits'")
s=s.replace("str(ROOT/'work/compute-deps')", "str(ROOT/'work/compute-deps'),str(ROOT/'work/galerkin84-2026-10-10')")
s=s.replace("       'inverse':", "       'frozen_J':ROOT/f'work/galerkin84-2026-10-10/MODEL_RAY_{args.parity.upper()}_3072.json',\n       'inverse':")
s=s.replace('Rmid=arb_mat([[YL[i,j].mid() for j in range(NJ)] for i in range(96)])',"Rmid=ratmat(data['frozen_J']['working_basis_midpoints_rational'])")
s+='\n'+(HERE/'endpoint_tail.py').read_text(encoding='utf-8')
(HERE/'compute_endpoint_traces.py').write_text(s,encoding='utf-8')
print('Generated complete endpoint-trace integrator')
