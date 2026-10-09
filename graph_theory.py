"""Graph theory (math 154 style): degree sequences, bipartiteness, coloring, trees, euler paths."""
from collections import defaultdict, deque
from itertools import combinations


def make_graph(edges):
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)
    return g
