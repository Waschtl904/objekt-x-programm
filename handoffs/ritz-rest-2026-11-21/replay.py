"""Reproduce the frozen witness, finite interval contractions and budget implications."""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json

import contract
import freeze


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def check_transition():
    beta = Fraction(20209999981781, 182190000000000)
    eta = Fraction(1, 10**10)
    for parity, c, u, floor in [
        ("gerade", Fraction(1977, 500000), Fraction(999997138063, 10**12), Fraction("0.0000013285")),
        ("ungerade", Fraction(6967, 10**6), Fraction(999982753528, 10**12), Fraction("0.0000079795")),
    ]:
        kappa = (1-c)*(1-u)
        value = Fraction(21, 5)*(eta+kappa*beta)
        require(kappa > 0 and value > floor, f"Schurboden {parity}")
        print(f"A8 -> A9, {parity}, reduzierter Boden: {float(value):.14g}")


def main():
    root = Path(__file__).resolve().parent
    config = load_json(root / "config.json")
    hashes = load_json(root / "input_hashes.json")
    require(set(hashes) == set(config.values()), "Unvollständige Eingangsbindung")
    for name, digest in hashes.items():
        require(sha256((root / name).read_bytes()).hexdigest() == digest, name)
    paths = {role: root / name for role, name in config.items()}
    witness = load_json(root / "witness.json")
    require(freeze.run(paths) == witness, "Rationale Zeugenkoordinaten")
    require(contract.main(paths, witness) == load_json(root / "bounds.json"), "Gerichtete Schranken")
    check_transition()
    print("Alle endlichen Prüfungen bestanden. Die vollständige physische Restenergie bleibt offen.")


if __name__ == "__main__":
    main()
