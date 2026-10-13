"""Probability (math 180a): checking textbook answers with monte carlo simulation."""
import math
import random
from collections import Counter


def simulate(trial, n=100_000, seed=0):
    rng = random.Random(seed)
    return sum(trial(rng) for _ in range(n)) / n
