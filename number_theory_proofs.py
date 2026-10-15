"""Math 109 style: checking claims numerically before proving them. induction, divisibility, pigeonhole."""
from itertools import combinations
from math import gcd, comb


def check(claim, values):
    """returns the first counterexample or None"""
    return next((v for v in values if not claim(v)), None)
