#!/usr/bin/env python3
"""Generate all operative Markdown views from RESEARCH_STATE.yaml."""
from pathlib import Path
import argparse, sys
from research_state import STATE, StateError, load, render, validate_structure

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    try:
        state = load(args.root / STATE)
        validate_structure(state)
        for name, raw in render(state).items():
            path = args.root / name
            if args.check:
                if not path.is_file() or path.read_bytes() != raw:
                    raise StateError('Generated file differs: ' + name)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(raw)
        print('Research state generation ' + ('CHECK PASS' if args.check else 'complete') + ': three deterministic Markdown views.')
    except StateError as e:
        print(str(e), file=sys.stderr)
        return 1
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
