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


def pigeonhole_subset_sum(nums):
    """any n integers have a nonempty subset whose sum is divisible by n. find one via prefix sums"""
    n = len(nums)
    seen = {0: 0}
    total = 0
    for i, x in enumerate(nums, 1):
        total = (total + x) % n
        if total in seen:
            return nums[seen[total]:i]
        seen[total] = i
    return None


def binomial_identities(n):
    return (sum(comb(n, k) for k in range(n + 1)) == 2 ** n
            and sum((-1) ** k * comb(n, k) for k in range(n + 1)) == 0
            and sum(comb(n, k) ** 2 for k in range(n + 1)) == comb(2 * n, n))


def strong_induction_postage(n):
    """every amount >= 12 can be made with 4c and 5c stamps"""
    return any((n - 5 * b) >= 0 and (n - 5 * b) % 4 == 0 for b in range(n // 5 + 1))
