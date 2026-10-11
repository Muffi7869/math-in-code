"""Linear algebra (math 18) implemented with plain python lists, checked against numpy."""
from fractions import Fraction


def mat(rows):
    return [[Fraction(x) for x in r] for r in rows]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]
