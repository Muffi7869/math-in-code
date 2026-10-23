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


def collatz_steps(n):
    steps = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1
    return steps


def is_equivalence_relation(elements, rel):
    reflexive = all((a, a) in rel for a in elements)
    symmetric = all((b, a) in rel for a, b in rel)
    transitive = all((a, d) in rel for a, b in rel for c, d in rel if b == c)
    return reflexive and symmetric and transitive


if __name__ == "__main__":
    rng = range(1, 500)
    for f in (sum_of_odds_is_square, sum_of_cubes, divisible_by_6, binomial_identities):
        print(f"{f.__name__:<24} counterexample: {check(f, rng)}")
    print("postage >= 12 counterexample:", check(strong_induction_postage, range(12, 1000)))
    print("bezout(240, 46):", bezout(240, 46), "| sqrt2 has no small rational root:", sqrt2_irrational_witness())
    print("phi(36) =", euler_phi(36), "| fermat holds for p=101, a=2..100:", all(fermat_little(101, a) for a in range(2, 101)))
    print("pigeonhole subset of [3, 8, 5, 1, 9, 4]:", pigeonhole_subset_sum([3, 8, 5, 1, 9, 4]))
    print("max collatz steps under 10k:", max(range(1, 10_000), key=collatz_steps))
    mod3 = {(a, b) for a in range(6) for b in range(6) if (a - b) % 3 == 0}
    print("congruence mod 3 is an equivalence relation:", is_equivalence_relation(range(6), mod3))
    print("number of 2-subsets of a 10-set:", len(list(combinations(range(10), 2))), "=", comb(10, 2))
