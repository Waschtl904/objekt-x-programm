"""Set explicit portable input roots; execute unchanged experiment code."""
from pathlib import Path
import sys,argparse
ap=argparse.ArgumentParser();ap.add_argument('--root',type=Path,required=True);ap.add_argument('--source',type=Path,required=True)
ap.add_argument('--bits',type=int,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
sys.path[:0]=[str(args.root/'code'),str(args.source/'vendor')]
import eight_source_refined as engine
engine.ORIGINAL=args.source.resolve();engine.HERE=args.root.resolve()
sys.argv=[sys.argv[0],'--bits',str(args.bits),'--out',str(args.out)]
engine.main()
