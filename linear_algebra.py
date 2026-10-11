"""Linear algebra (math 18) implemented with plain python lists, checked against numpy."""
from fractions import Fraction


def mat(rows):
    return [[Fraction(x) for x in r] for r in rows]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def rref(A):
    """reduced row echelon form with exact fractions. returns (R, pivot columns)"""
    R = [row[:] for row in A]
    rows, cols = len(R), len(R[0])
    pivots, r = [], 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if R[i][c] != 0), None)
        if pivot is None:
            continue
        R[r], R[pivot] = R[pivot], R[r]
        R[r] = [x / R[r][c] for x in R[r]]
        for i in range(rows):
            if i != r and R[i][c] != 0:
                f = R[i][c]
                R[i] = [a - f * b for a, b in zip(R[i], R[r])]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return R, pivots


def rank(A):
    return len(rref(A)[1])


def inverse(A):
    n = len(A)
    aug = [row + [Fraction(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    R, pivots = rref(aug)
    if pivots[:n] != list(range(n)):
        raise ValueError("matrix is singular")
    return [row[n:] for row in R]
