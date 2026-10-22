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


def bezout(a, b):
    if b == 0:
        return a, 1, 0
    g, x, y = bezout(b, a % b)
    return g, y, x - (a // b) * y


def sqrt2_irrational_witness(limit=2000):
    """no p/q with q <= limit squares to exactly 2 (the proof says none ever will)"""
    return all(p * p != 2 * q * q for q in range(1, limit + 1) for p in (int(q * 1.41421356), int(q * 1.41421356) + 1))


def euler_phi(n):
    return sum(1 for k in range(1, n + 1) if gcd(k, n) == 1)


def fermat_little(p, a):
    return pow(a, p - 1, p) == 1
