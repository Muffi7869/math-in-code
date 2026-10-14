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
