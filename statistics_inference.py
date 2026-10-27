"""Statistics (math 181a): estimators, MLE, confidence intervals, checking coverage by simulation."""
import math
import random
import statistics as st


def sample_mean_var(xs):
    n = len(xs)
    m = sum(xs) / n
    return m, sum((x - m) ** 2 for x in xs) / (n - 1)
