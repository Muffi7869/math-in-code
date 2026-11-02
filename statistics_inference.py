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


def t_critical(df, conf=0.95):
    """bisection on the t cdf (via the regularized incomplete beta relationship is overkill; use normal approx for large df)"""
    z = st.NormalDist().inv_cdf(0.5 + conf / 2)
    return z + (z ** 3 + z) / (4 * df) + (5 * z ** 5 + 16 * z ** 3 + 3 * z) / (96 * df ** 2)


def mean_ci(xs, conf=0.95):
    m, v = sample_mean_var(xs)
    half = t_critical(len(xs) - 1, conf) * math.sqrt(v / len(xs))
    return m - half, m + half


def ci_coverage(true_mu=10, sigma=3, n=15, reps=10_000, seed=2):
    rng = random.Random(seed)
    hits = 0
    for _ in range(reps):
        lo, hi = mean_ci([rng.gauss(true_mu, sigma) for _ in range(n)])
        hits += lo <= true_mu <= hi
    return hits / reps


def proportion_ci(successes, n, conf=0.95):
    """wilson interval, better than the textbook wald interval for small n"""
    z = st.NormalDist().inv_cdf(0.5 + conf / 2)
    p = successes / n
    denom = 1 + z ** 2 / n
    center = (p + z ** 2 / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / denom
    return center - half, center + half


def mse_of_estimators(reps=20_000, n=10, seed=4):
    """uniform(0, theta): compare 2*mean vs (n+1)/n * max as estimators of theta"""
    rng = random.Random(seed)
    theta = 5.0
    e1 = e2 = 0.0
    for _ in range(reps):
        xs = [rng.uniform(0, theta) for _ in range(n)]
        e1 += (2 * sum(xs) / n - theta) ** 2
        e2 += ((n + 1) / n * max(xs) - theta) ** 2
    return round(e1 / reps, 4), round(e2 / reps, 4)


if __name__ == "__main__":
    rng = random.Random(9)
    print("E[biased var], E[unbiased var], true:", biased_vs_unbiased_variance())
    data_exp = [rng.expovariate(2.5) for _ in range(5000)]
    print(f"exponential MLE rate {mle_exponential(data_exp):.3f} (true 2.5)")
    data_norm = [rng.gauss(4, 1.5) for _ in range(5000)]
    print("normal MLE (mu, sigma):", tuple(round(x, 3) for x in mle_normal(data_norm)))
    print("poisson MLE by grid:", mle_poisson_grid([2, 3, 1, 4, 2, 5, 3, 2]), "sample mean", st.mean([2, 3, 1, 4, 2, 5, 3, 2]))
    print(f"t* df=14: {t_critical(14):.3f} (table 2.145) | 95% CI coverage: {ci_coverage():.3f}")
    print("wilson CI 3/20:", tuple(round(x, 3) for x in proportion_ci(3, 20)))
    print("MSE 2*mean vs adjusted max:", mse_of_estimators())
