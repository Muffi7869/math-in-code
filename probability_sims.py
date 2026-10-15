"""Probability (math 180a): checking textbook answers with monte carlo simulation."""
import math
import random
from collections import Counter


def simulate(trial, n=100_000, seed=0):
    rng = random.Random(seed)
    return sum(trial(rng) for _ in range(n)) / n


def birthday_exact(k, days=365):
    p_distinct = 1.0
    for i in range(k):
        p_distinct *= (days - i) / days
    return 1 - p_distinct


def birthday_trial(k):
    return lambda rng: len({rng.randrange(365) for _ in range(k)}) < k


def monty_hall_trial(switch):
    def trial(rng):
        car, pick = rng.randrange(3), rng.randrange(3)
        opened = next(d for d in range(3) if d not in (car, pick))
        if switch:
            pick = next(d for d in range(3) if d not in (pick, opened))
        return pick == car
    return trial


def binomial_pmf(k, n, p):
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def poisson_pmf(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def coupon_collector_expected(n):
    return n * sum(1 / i for i in range(1, n + 1))


def coupon_trial(n):
    def trial(rng):
        seen, draws = set(), 0
        while len(seen) < n:
            seen.add(rng.randrange(n))
            draws += 1
        return draws
    return trial


def derangement_prob(n):
    return sum((-1) ** k / math.factorial(k) for k in range(n + 1))


def derangement_trial(n):
    def trial(rng):
        perm = list(range(n))
        rng.shuffle(perm)
        return all(perm[i] != i for i in range(n))
    return trial


def clt_demo(n_dice=30, samples=20_000, seed=1):
    """sum of 30 dice should be roughly normal with mean 105 and sd sqrt(30*35/12)"""
    rng = random.Random(seed)
    sums = [sum(rng.randint(1, 6) for _ in range(n_dice)) for _ in range(samples)]
    mean = sum(sums) / samples
    sd = math.sqrt(sum((s - mean) ** 2 for s in sums) / (samples - 1))
    within_1sd = sum(abs(s - mean) <= sd for s in sums) / samples
    return round(mean, 2), round(sd, 3), round(math.sqrt(n_dice * 35 / 12), 3), round(within_1sd, 3)
