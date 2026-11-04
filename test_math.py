"""quick checks for everything in this repo. run with: python -m pytest -q (or just python test_math.py)"""
import math
from fractions import Fraction

import graph_theory as gt
import linear_algebra as la
import number_theory_proofs as nt
import probability_sims as ps
import statistics_inference as si


def test_havel_hakimi():
    assert gt.is_graphical([3, 3, 3, 3])
    assert not gt.is_graphical([4, 1, 1])


def test_cycle_bipartite_iff_even():
    even = gt.make_graph([(i, (i + 1) % 6) for i in range(6)])
    odd = gt.make_graph([(i, (i + 1) % 5) for i in range(5)])
    assert gt.is_bipartite(even)[0] and not gt.is_bipartite(odd)[0]


def test_coloring_is_proper():
    g = gt.make_graph([(0, 1), (1, 2), (2, 0), (2, 3)])
    colors = gt.greedy_coloring(g)
    assert all(colors[u] != colors[v] for u in g for v in g[u])
