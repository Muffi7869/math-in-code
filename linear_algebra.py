"""Linear algebra (math 18) implemented with plain python lists, checked against numpy."""
from fractions import Fraction


def mat(rows):
    return [[Fraction(x) for x in r] for r in rows]
