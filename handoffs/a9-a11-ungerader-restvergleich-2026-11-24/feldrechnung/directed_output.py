"""Short decimal upper endpoints retaining twenty significant digits."""
from fractions import Fraction

def upper_decimal(value):
    bound = Fraction(str(value.upper().fmpq()))
    if bound == 0:
        return "0"
    assert bound > 0
    order = len(str(bound.numerator)) - len(str(bound.denominator))
    if bound < Fraction(10)**order:
        order -= 1
    exponent = order - 19
    scaled = bound / Fraction(10)**exponent
    ceiling = -((-scaled.numerator)//scaled.denominator)
    text = f"{ceiling}e{exponent}"
    assert Fraction(text) >= bound
    return text
