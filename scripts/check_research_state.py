#!/usr/bin/env python3
"""Validate operative status, provenance and metadata. No theorem promotion."""
from pathlib import Path
import argparse, json, sys
from research_state import StateError, validate

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument('--base-ref')
    args = ap.parse_args()
    try:
        result = validate(args.root, args.base_ref)
    except (StateError, OSError) as e:
        print('RESEARCH_STATE validation FAILED: ' + str(e), file=sys.stderr)
        return 1
    print('RESEARCH_STATE validation PASS: ' + json.dumps(result, sort_keys=True))
    print('This validates navigation and evidence bindings, not mathematical truth or independent review.')
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
