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
