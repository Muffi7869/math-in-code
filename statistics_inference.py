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


def mle_exponential(xs):
    return len(xs) / sum(xs)


def mle_normal(xs):
    n = len(xs)
    mu = sum(xs) / n
    return mu, math.sqrt(sum((x - mu) ** 2 for x in xs) / n)


def log_likelihood_poisson(lam, xs):
    return sum(x * math.log(lam) - lam - math.lgamma(x + 1) for x in xs)


def mle_poisson_grid(xs, grid=None):
    grid = grid or [i / 100 for i in range(1, 1001)]
    return max(grid, key=lambda lam: log_likelihood_poisson(lam, xs))
