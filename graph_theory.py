"""Graph theory (math 154 style): degree sequences, bipartiteness, coloring, trees, euler paths."""
from collections import defaultdict, deque
from itertools import combinations


def make_graph(edges):
    g = defaultdict(set)
    for u, v in edges:
        g[u].add(v)
        g[v].add(u)
    return g


def degree_sequence(g):
    return sorted((len(nbrs) for nbrs in g.values()), reverse=True)


def is_graphical(seq):
    """Havel-Hakimi: can this degree sequence come from a simple graph?"""
    seq = sorted(seq, reverse=True)
    while seq and seq[0] > 0:
        d = seq.pop(0)
        if d > len(seq):
            return False
        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0:
                return False
        seq.sort(reverse=True)
    return True
