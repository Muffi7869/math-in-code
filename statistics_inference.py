"""Statistics (math 181a): estimators, MLE, confidence intervals, checking coverage by simulation."""
import math
import random
import statistics as st


def sample_mean_var(xs):
    n = len(xs)
    m = sum(xs) / n
    return m, sum((x - m) ** 2 for x in xs) / (n - 1)


def biased_vs_unbiased_variance(n=5, reps=50_000, seed=0):
    rng = random.Random(seed)
    biased = unbiased = 0.0
    for _ in range(reps):
        xs = [rng.gauss(0, 2) for _ in range(n)]
        m = sum(xs) / n
        ss = sum((x - m) ** 2 for x in xs)
        biased += ss / n
        unbiased += ss / (n - 1)
    return round(biased / reps, 3), round(unbiased / reps, 3), 4.0
