"""Math 109 style: checking claims numerically before proving them. induction, divisibility, pigeonhole."""
from itertools import combinations
from math import gcd, comb


def check(claim, values):
    """returns the first counterexample or None"""
    return next((v for v in values if not claim(v)), None)


def sum_of_odds_is_square(n):
    return sum(2 * k - 1 for k in range(1, n + 1)) == n * n


def sum_of_cubes(n):
    return sum(k ** 3 for k in range(1, n + 1)) == (n * (n + 1) // 2) ** 2


def divisible_by_6(n):
    return (n ** 3 - n) % 6 == 0
