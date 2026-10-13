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
