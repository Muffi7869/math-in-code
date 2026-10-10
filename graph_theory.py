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


def is_bipartite(g):
    color = {}
    for start in g:
        if start in color:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            for w in g[v]:
                if w not in color:
                    color[w] = 1 - color[v]
                    q.append(w)
                elif color[w] == color[v]:
                    return False, None
    return True, color


def greedy_coloring(g, order=None):
    colors = {}
    for v in order or sorted(g, key=lambda x: -len(g[x])):
        used = {colors[w] for w in g[v] if w in colors}
        colors[v] = next(c for c in range(len(g) + 1) if c not in used)
    return colors


def is_tree(g, n_vertices):
    edges = sum(len(nb) for nb in g.values()) // 2
    if edges != n_vertices - 1:
        return False
    seen, stack = set(), [next(iter(g))]
    while stack:
        v = stack.pop()
        if v not in seen:
            seen.add(v)
            stack.extend(g[v] - seen)
    return len(seen) == n_vertices


def prufer_code(tree_edges):
    g = make_graph(tree_edges)
    code = []
    while len(g) > 2:
        leaf = min(v for v in g if len(g[v]) == 1)
        parent = next(iter(g[leaf]))
        code.append(parent)
        g[parent].discard(leaf)
        del g[leaf]
    return code
