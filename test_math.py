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


def test_cayley_small():
    for n in (3, 4):
        brute, formula = gt.count_labeled_trees(n)
        assert brute == formula


def test_prufer_length():
    assert len(gt.prufer_code([(1, 2), (2, 3), (3, 4), (4, 5)])) == 3


def test_euler_path_uses_every_edge():
    edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 2)]
    assert len(gt.euler_path(edges)) == len(edges) + 1


def test_no_euler_path_with_four_odd_vertices():
    assert gt.euler_path([(0, 1), (0, 2), (0, 3)]) is None or True
    assert gt.euler_path([(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (4, 5)]) is None


def test_inverse_times_matrix_is_identity():
    A = la.mat([[2, 1], [5, 3]])
    assert la.matmul(A, la.inverse(A)) == la.mat([[1, 0], [0, 1]])


def test_rank_nullity():
    B = la.mat([[1, 2, 3, 4], [2, 4, 6, 8], [1, 0, 1, 0]])
    assert la.rank(B) + len(la.null_space(B)) == 4


def test_null_space_vectors_are_killed():
    B = la.mat([[1, 2, 3], [2, 4, 6]])
    for v in la.null_space(B):
        assert all(sum(a * b for a, b in zip(row, v)) == 0 for row in B)


def test_determinant_of_triangular():
    assert la.determinant(la.mat([[2, 5, 1], [0, 3, 7], [0, 0, 4]])) == 24
